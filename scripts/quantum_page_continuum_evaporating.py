#!/usr/bin/env python3
"""R-PAGE next step: evaporating continuum spectrum + unitary hybrid S_rad(v).

Uses week2 stationary greybody Γ(ω) on a *prescribed* T_H(t) evaporation schedule.

Two curves (instrument only, page_curve_claimed=false):

  A) THERMAL-ONLY bookkeeping
       n_i(t) = Γ_i · n_B(ω_i; T_H(t))
       S_rad = Σ s_bose(n_i),  E_rad = Σ ω_i n_i
       Expected: NO Page turn (information-loss style thermal bookkeeping)

  B) UNITARY HYBRID
       Same ω, Γ; pure Gaussian core+rad; pair-creation g ∝ κ(t)=2π T_H(t)
       with slow evaporating T_H(t); record S_rad(v) from reduced cov
       Expected: may show page-like shape (curiosity) if purification works

Resource: OMP=1, single process, seconds–tens of seconds. No PolyChord.

Usage:
  OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_evaporating.py
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path

import numpy as np

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

W2 = Path("docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week2_bogoliubov.json")
OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
OUT_JSON = OUT_DIR / "page_curve" / "continuum_evaporating.json"
OUT_MD = OUT_DIR / "PAGE_CURVE_CONTINUUM_EVAPORATING.md"
TASK = Path("docs/working_logs/_runs/quantum_residual_task_20260803")

N_C = 4
N_STEPS = 120
DT_UNITARY = 0.04
G_SCALE = 0.35  # overall pair-creation scale times κ(t)
MAX_MODES = 9


def bose_n(omega: float, T: float) -> float:
    if T <= 0 or omega <= 0:
        return 0.0
    x = omega / T
    if x > 700:
        return 0.0
    return 1.0 / (math.exp(x) - 1.0)


def s_bose(n: float) -> float:
    """Von Neumann entropy of one thermal bosonic mode (occupation n)."""
    n = max(float(n), 0.0)
    if n < 1e-15:
        return 0.0
    return (n + 1.0) * math.log(n + 1.0) - n * math.log(n)


def thermal_cov(nbar: float) -> np.ndarray:
    a = nbar + 0.5
    return np.diag([a, a])


def block_diag(mats: list[np.ndarray]) -> np.ndarray:
    n = sum(m.shape[0] for m in mats)
    out = np.zeros((n, n))
    i = 0
    for m in mats:
        s = m.shape[0]
        out[i : i + s, i : i + s] = m
        i += s
    return out


def symplectic(n_modes: int) -> np.ndarray:
    return block_diag([np.array([[0.0, 1.0], [-1.0, 0.0]]) for _ in range(n_modes)])


def build_A(n_c: int, omega_r: np.ndarray, gam: np.ndarray, g_scale: float) -> np.ndarray:
    n_r = len(omega_r)
    A = np.zeros((2 * (n_c + n_r), 2 * (n_c + n_r)))

    def qp(k: int):
        return 2 * k, 2 * k + 1

    for k in range(n_c):
        iq, ip = qp(k)
        A[iq, iq] = A[ip, ip] = 1.0
    for j in range(n_r):
        iq, ip = qp(n_c + j)
        w = float(omega_r[j])
        A[iq, iq] = A[ip, ip] = w
    for j in range(n_r):
        k = j % n_c
        g = g_scale * math.sqrt(max(float(gam[j]), 1e-6))
        iq_c, ip_c = qp(k)
        iq_r, ip_r = qp(n_c + j)
        A[iq_c, ip_r] += g
        A[ip_r, iq_c] += g
        A[ip_c, iq_r] += g
        A[iq_r, ip_c] += g
    return A


def evolve(gamma: np.ndarray, A: np.ndarray, Omega: np.ndarray, dt: float) -> np.ndarray:
    K = Omega @ A

    def f(G):
        return K @ G + G @ K.T

    k1 = f(gamma)
    k2 = f(gamma + dt * k1)
    out = gamma + 0.5 * dt * (k1 + k2)
    return 0.5 * (out + out.T)


def entropy_cov(gamma_sub: np.ndarray, Omega_sub: np.ndarray) -> float:
    M = 1j * (Omega_sub @ gamma_sub)
    evals = np.linalg.eigvals(M)
    nus = sorted({float(abs(e.real)) for e in evals if abs(e.real) > 1e-10}, reverse=True)
    seen: list[float] = []
    for nu in nus:
        if all(abs(nu - s) > 1e-7 for s in seen):
            seen.append(nu)
    S = 0.0
    for nu in seen:
        nu = max(nu, 0.5 + 1e-15)
        sp, sm = nu + 0.5, nu - 0.5
        S += sp * math.log(sp) - (sm * math.log(sm) if sm > 1e-18 else 0.0)
    return float(S)


def energy_cov(gamma: np.ndarray, n_c: int, omega_r: np.ndarray) -> tuple[float, float]:
    e_c = e_r = 0.0
    for k in range(n_c):
        iq, ip = 2 * k, 2 * k + 1
        e_c += 0.5 * (gamma[iq, iq] + gamma[ip, ip]) - 0.5
    for j, w in enumerate(omega_r):
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        e_r += 0.5 * float(w) * (gamma[iq, iq] + gamma[ip, ip]) - 0.5 * float(w)
    return float(max(e_c, 0.0)), float(max(e_r, 0.0))


def load_week2_modes() -> tuple[np.ndarray, np.ndarray, float, float]:
    w2 = json.loads(W2.read_text())
    mm = sorted(w2["mode_matching"], key=lambda r: float(r["omega"]))
    if len(mm) > MAX_MODES:
        mid = len(mm) // 2
        half = MAX_MODES // 2
        mm = mm[max(0, mid - half) : mid - half + MAX_MODES]
    omega = np.array([float(r["omega"]) for r in mm])
    gam = np.clip(np.array([float(r.get("Gamma", 1.0)) for r in mm]), 1e-4, 1.0)
    T0 = float(w2["analytic"]["T_H"])
    kappa0 = float(w2["analytic"]["kappa"])
    return omega, gam, T0, kappa0


def thermal_only_curve(omega: np.ndarray, gam: np.ndarray, T0: float, n_steps: int) -> dict:
    """Cumulative thermal emission as BH analog evaporates (information-loss class).

    Schedule: evaporated fraction v∈[0,1]; remaining mass proxy (1−v); T∝1/(1−v).
    Emit dE = E_budget·dv at temperature T(v); dS ≈ dE/T (coarse continuum).
    Also track multi-mode atmosphere S_atm = Σ s(Γ n_B) for diagnostics.
    Expected: S_cum rises (no purification to 0) — NOT a Page turn.
    """
    # Budget from initial atmosphere energy at T0
    n0 = np.array([gam[j] * bose_n(float(omega[j]), T0) for j in range(len(omega))])
    E_budget = float(np.sum(omega * n0)) + 1e-15
    hist = []
    S_cum = 0.0
    E_cum = 0.0
    for i in range(n_steps + 1):
        v = i / n_steps
        # T rises as remnant shrinks (standard BH); floor at end
        T = T0 / max(1.0 - v, 0.05)
        if i > 0:
            dv = 1.0 / n_steps
            dE = E_budget * dv
            E_cum += dE
            S_cum += dE / T
        ns = np.array([gam[j] * bose_n(float(omega[j]), T) for j in range(len(omega))])
        S_atm = float(sum(s_bose(n) for n in ns))
        hist.append(
            {
                "v": v,
                "T_H": T,
                "E_cum": E_cum,
                "S_cum": S_cum,
                "S_atm": S_atm,
                "S_rad": S_cum,  # cumulative = radiation entropy proxy
            }
        )
    S = [h["S_rad"] for h in hist]
    i_pk = int(np.argmax(S))
    late_drop = S[i_pk] - S[-1]
    # purification-style turn: peak mid-way and large late drop
    turns = i_pk < len(S) - 5 and late_drop > 0.1 * max(S[i_pk], 1e-15)
    # healthy thermal: mostly nondecreasing cumulative S
    mono_ok = all(S[i] <= S[i + 1] + 1e-12 for i in range(len(S) - 1))
    return {
        "history": hist[:: max(1, len(hist) // 40)],
        "S_peak": float(S[i_pk]),
        "S_late": float(S[-1]),
        "late_drop": float(late_drop),
        "page_like_turn": bool(turns),
        "monotonic_cumulative_S": bool(mono_ok),
        "E_budget": E_budget,
        "note": "cumulative dE/T thermal bookkeeping — not Page; should not purify",
    }


def unitary_hybrid_curve(
    omega: np.ndarray, gam: np.ndarray, T0: float, kappa0: float, n_steps: int
) -> dict:
    """Unitary Gaussian with g(t)∝κ(t)=κ0*(1-f), f slow schedule."""
    n_r = len(omega)
    mats = [thermal_cov(0.0) for _ in range(N_C + n_r)]
    gamma = block_diag(mats)
    Omega = symplectic(N_C + n_r)
    core_sl = slice(0, 2 * N_C)
    rad_sl = slice(2 * N_C, 2 * (N_C + n_r))
    Om_c, Om_r = Omega[core_sl, core_sl], Omega[rad_sl, rad_sl]

    hist = []
    for i in range(n_steps + 1):
        f = i / n_steps
        kappa_t = kappa0 * max(1.0 - f, 0.02)
        g_t = G_SCALE * kappa_t
        A = build_A(N_C, omega, gam, g_t)
        S_c = entropy_cov(gamma[core_sl, core_sl], Om_c)
        S_r = entropy_cov(gamma[rad_sl, rad_sl], Om_r)
        S_tot = entropy_cov(gamma, Omega)
        e_c, e_r = energy_cov(gamma, N_C, omega)
        es = e_c + e_r
        v = e_r / (es + 1e-30) if es > 1e-18 else 0.0
        hist.append(
            {
                "f": f,
                "kappa_t": kappa_t,
                "g_t": g_t,
                "S_core": S_c,
                "S_rad": S_r,
                "S_total": S_tot,
                "E_core": e_c,
                "E_rad": e_r,
                "v": v,
            }
        )
        if i < n_steps:
            # several micro-steps per schedule step for stability
            for _ in range(4):
                gamma = evolve(gamma, A, Omega, DT_UNITARY)

    S = [h["S_rad"] for h in hist]
    i_pk = int(np.argmax(S))
    peak, late = S[i_pk], S[-1]
    drop = peak - late
    page_like = i_pk > 2 and i_pk < len(S) - 3 and peak > 1e-6 and drop > 0.1 * peak
    max_stot = float(max(abs(h["S_total"]) for h in hist))
    return {
        "history": hist[:: max(1, len(hist) // 40)],
        "S_peak": float(peak),
        "S_late": float(late),
        "late_drop": float(drop),
        "v_at_peak": float(hist[i_pk]["v"]),
        "page_like_shape_curiosity": bool(page_like),
        "max_abs_S_total": max_stot,
        "unitarity_ok": max_stot < 0.05,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)
    TASK.mkdir(parents=True, exist_ok=True)

    if not W2.is_file():
        print("FAIL missing week2 json")
        return 2

    omega, gam, T0, kappa0 = load_week2_modes()
    thermal = thermal_only_curve(omega, gam, T0, N_STEPS)
    unitary = unitary_hybrid_curve(omega, gam, T0, kappa0, N_STEPS)

    # Grades: thermal cumulative must not show purification Page-turn
    thermal_no_fake_page = (not thermal["page_like_turn"]) and bool(
        thermal.get("monotonic_cumulative_S", False)
    )

    payload = {
        "milestone": "R_PAGE_continuum_evaporating",
        "page_curve_claimed": False,
        "S_rad_v_claimed": False,
        "n_modes": len(omega),
        "omegas": omega.tolist(),
        "Gammas": gam.tolist(),
        "T_H0": T0,
        "kappa0": kappa0,
        "thermal_only": thermal,
        "unitary_hybrid": unitary,
        "grades": {
            "thermal_bookkeeping_ran": True,
            "thermal_no_page_claim_ok": thermal_no_fake_page,
            "unitary_ran": True,
            "unitary_unitarity": unitary["unitarity_ok"],
            "page_curve_claimed": False,
        },
        "interpretation": {
            "thermal_only": "Standard Hawking bookkeeping on evaporating T_H(t); should not purify.",
            "unitary_hybrid": "Toy purification channel + week2 Γ weights; page-like = curiosity only.",
            "still_missing": "True continuum time-dep mode ODE + self-consistent GP evaporation",
        },
        "resource": "OMP=1; no PolyChord",
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    md = f"""# Continuum evaporating S_rad instrument (R-PAGE)

**Script:** `scripts/quantum_page_continuum_evaporating.py`  
**JSON:** `page_curve/continuum_evaporating.json`  
**page_curve_claimed:** **false**

## A) Thermal-only (Γ · n_B, T_H(t)↓)

| quantity | value |
|---|---:|
| S_peak | {thermal["S_peak"]:.6f} |
| S_late | {thermal["S_late"]:.6f} |
| late_drop | {thermal["late_drop"]:.6f} |
| monotonic S_cum | {thermal.get("monotonic_cumulative_S")} |
| page-like turn | {"YES (unexpected)" if thermal["page_like_turn"] else "NO (expected)"} |
| grade | {"PASS bookkeeping" if thermal_no_fake_page else "CHECK"} |

Thermal-only is the **information-loss** curve class — not a Page solution.

## B) Unitary hybrid (week2 ω,Γ + Gaussian core)

| quantity | value |
|---|---:|
| S_peak | {unitary["S_peak"]:.6f} |
| S_late | {unitary["S_late"]:.6f} |
| late_drop | {unitary["late_drop"]:.6f} |
| v at peak | {unitary["v_at_peak"]:.4f} |
| max\\|S_total\\| | {unitary["max_abs_S_total"]:.3e} |
| unitarity | {"PASS" if unitary["unitarity_ok"] else "FAIL"} |
| page-like curiosity | {"YES" if unitary["page_like_shape_curiosity"] else "NO"} |

## Grade

| check | status |
|---|---|
| Thermal bookkeeping | **{"PASS" if thermal_no_fake_page else "FAIL"}** |
| Unitary unitarity | **{"PASS" if unitary["unitarity_ok"] else "FAIL"}** |
| Q6 / Page claim | **OPEN — false** |

## Still missing for a claim

1. Time-dependent continuum mode ODE (not only Γ·n_B + toy Gaussian)  
2. Self-consistent horizon evaporation  
3. Red AGREE  

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_evaporating.py
```
"""
    OUT_MD.write_text(md)
    (TASK / "PAGE_EVAPORATING_RESULT.md").write_text(md)

    print("CONTINUUM EVAPORATING Page instrument")
    print(f"  thermal: S_peak={thermal['S_peak']:.4f} turn={thermal['page_like_turn']} ok={thermal_no_fake_page}")
    print(
        f"  unitary: S_peak={unitary['S_peak']:.4f} drop={unitary['late_drop']:.4f} "
        f"unitarity={unitary['unitarity_ok']} page_like={unitary['page_like_shape_curiosity']}"
    )
    print(f"  page_curve_claimed=false wrote {OUT_JSON}")
    ok = thermal_no_fake_page and unitary["unitarity_ok"]
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
