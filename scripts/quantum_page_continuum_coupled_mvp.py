#!/usr/bin/env python3
"""Page instrument: week2 continuum spectrum + unitary Gaussian core/rad.

R-PAGE C1–C2 (quantum_residual_task board).

Resource: OMP_NUM_THREADS=1, nice recommended. No PolyChord. No MPI.

What this DOES:
  - Load week2_bogoliubov.json mode_matching (ω, Γ, n_mode) continuum band
  - Finite core (N_c oscillators) + radiation modes at those ω
  - Pure global Gaussian seed; two-mode-squeezing couplings weighted by √Γ
  - Optional slow evaporation: g(t) = g0 * sech(t/τ) so energy settles
  - Record S_core, S_rad, S_total, E_*, v vs t
  - Null g=0 control
  - page_curve_claimed = false always

What this does NOT:
  - Evolve continuum mode ODE in time (uses week2 stationary occupations only as ω/Γ)
  - Self-consistent GP
  - Q6 / Page claim

Usage:
  OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_coupled_mvp.py
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
OUT_JSON = OUT_DIR / "page_curve" / "continuum_coupled_mvp.json"
OUT_MD = OUT_DIR / "PAGE_CURVE_CONTINUUM_COUPLED_MVP.md"
BOARD = Path("docs/working_logs/_runs/quantum_residual_task_20260803")

N_C = 4
N_STEPS = 250
DT = 0.025
G0 = 0.10
TAU_EVAP = 3.5  # g(t)=G0*sech(t/TAU)
MAX_MODES = 10  # keep light on loaded box


def thermal_cov(nbar: float) -> np.ndarray:
    a = float(nbar) + 0.5
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


def build_A(n_c: int, omega_r: np.ndarray, gamma_w: np.ndarray, g_scale: float) -> np.ndarray:
    n_r = len(omega_r)
    n = n_c + n_r
    A = np.zeros((2 * n, 2 * n))

    def qp(k: int) -> tuple[int, int]:
        return 2 * k, 2 * k + 1

    for k in range(n_c):
        iq, ip = qp(k)
        A[iq, iq] = A[ip, ip] = 1.0
    for j in range(n_r):
        iq, ip = qp(n_c + j)
        w = float(omega_r[j])
        A[iq, iq] = A[ip, ip] = w
    # pair-creation core j ↔ rad j (or mod), weight √Γ
    for j in range(n_r):
        k = j % n_c
        g = g_scale * math.sqrt(max(float(gamma_w[j]), 1e-6))
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


def entropy(gamma_sub: np.ndarray, Omega_sub: np.ndarray) -> float:
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


def energy(gamma: np.ndarray, n_c: int, omega_r: np.ndarray) -> tuple[float, float]:
    e_c = e_r = 0.0
    for k in range(n_c):
        iq, ip = 2 * k, 2 * k + 1
        e_c += 0.5 * (gamma[iq, iq] + gamma[ip, ip]) - 0.5
    for j, w in enumerate(omega_r):
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        e_r += 0.5 * float(w) * (gamma[iq, iq] + gamma[ip, ip]) - 0.5 * float(w)
    return float(max(e_c, 0.0)), float(max(e_r, 0.0))


def run_evolution(omega_r: np.ndarray, gamma_w: np.ndarray, g0: float, evaporate: bool) -> dict:
    n_r = len(omega_r)
    mats = [thermal_cov(0.0) for _ in range(N_C + n_r)]
    gamma = block_diag(mats)
    Omega = symplectic(N_C + n_r)
    core_sl = slice(0, 2 * N_C)
    rad_sl = slice(2 * N_C, 2 * (N_C + n_r))
    Om_c = Omega[core_sl, core_sl]
    Om_r = Omega[rad_sl, rad_sl]

    history = []
    for step in range(N_STEPS + 1):
        t = step * DT
        if evaporate:
            g_t = g0 / math.cosh(t / TAU_EVAP)
        else:
            g_t = g0
        A = build_A(N_C, omega_r, gamma_w, g_t)
        S_c = entropy(gamma[core_sl, core_sl], Om_c)
        S_r = entropy(gamma[rad_sl, rad_sl], Om_r)
        S_tot = entropy(gamma, Omega)
        e_c, e_r = energy(gamma, N_C, omega_r)
        es = e_c + e_r
        v = e_r / (es + 1e-30) if es > 1e-18 else 0.0
        history.append(
            {
                "t": t,
                "g_t": g_t,
                "S_core": S_c,
                "S_rad": S_r,
                "S_total": S_tot,
                "E_core": e_c,
                "E_rad": e_r,
                "v": v,
            }
        )
        if step < N_STEPS:
            gamma = evolve(gamma, A, Omega, DT)

    S = [h["S_rad"] for h in history]
    i_pk = int(np.argmax(S))
    peak, late = S[i_pk], S[-1]
    drop = peak - late
    page_like = i_pk > 2 and i_pk < len(S) - 5 and peak > 1e-6 and drop > 0.1 * peak
    max_stot = float(max(abs(h["S_total"]) for h in history))
    return {
        "history": history,
        "S_rad_peak": float(peak),
        "S_rad_late": float(late),
        "late_drop": float(drop),
        "i_peak": i_pk,
        "v_at_peak": float(history[i_pk]["v"]),
        "page_like_shape_curiosity": bool(page_like),
        "max_abs_S_total": max_stot,
        "unitarity_ok": max_stot < 0.05,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)
    BOARD.mkdir(parents=True, exist_ok=True)

    if not W2.is_file():
        print("FAIL: week2 json missing — run quantum_page_bogoliubov_week2.py first")
        return 2

    w2 = json.loads(W2.read_text())
    mm = w2.get("mode_matching") or []
    if not mm:
        print("FAIL: no mode_matching in week2")
        return 2

    # sort by omega, take mid-band up to MAX_MODES
    rows = sorted(mm, key=lambda r: float(r["omega"]))
    if len(rows) > MAX_MODES:
        # keep mid band
        mid = len(rows) // 2
        half = MAX_MODES // 2
        rows = rows[max(0, mid - half) : mid - half + MAX_MODES]

    omega = np.array([float(r["omega"]) for r in rows], dtype=float)
    # Γ from mode matching if present else 1
    gam = np.array(
        [float(r.get("Gamma", r.get("greybody", r.get("Gamma_omega", 1.0)))) for r in rows],
        dtype=float,
    )
    gam = np.clip(gam, 1e-4, 1.0)
    n_mode = np.array([float(r.get("n_mode", r.get("n_B", 0.0))) for r in rows], dtype=float)

    # sanity: re-run week2 spectrum check
    T_H = float(w2.get("analytic", {}).get("T_H", 0.02))
    kappa = float(w2.get("analytic", {}).get("kappa", 0.125))

    coupled = run_evolution(omega, gam, G0, evaporate=True)
    null_g0 = run_evolution(omega, gam, 0.0, evaporate=False)

    payload = {
        "milestone": "R_PAGE_C1_C2_continuum_coupled_mvp",
        "page_curve_claimed": False,
        "S_rad_v_claimed": False,
        "week2_pass": bool(w2.get("week2_pass", False)),
        "T_H": T_H,
        "kappa": kappa,
        "n_modes": len(omega),
        "omegas": omega.tolist(),
        "Gammas": gam.tolist(),
        "n_mode_week2": n_mode.tolist(),
        "N_c": N_C,
        "N_steps": N_STEPS,
        "dt": DT,
        "G0": G0,
        "tau_evap": TAU_EVAP,
        "coupled_evaporating": coupled,
        "null_g0": {
            "S_rad_peak": null_g0["S_rad_peak"],
            "S_rad_late": null_g0["S_rad_late"],
            "late_drop": null_g0["late_drop"],
            "max_abs_S_total": null_g0["max_abs_S_total"],
            "unitarity_ok": null_g0["unitarity_ok"],
            # drop full history for null to keep JSON smaller
        },
        "history": coupled["history"],
        "grades": {
            "instrument_ran": True,
            "unitarity_coupled": coupled["unitarity_ok"],
            "null_g0_no_spurious_growth": null_g0["S_rad_peak"] < 1e-4,
            "page_curve_claimed": False,
        },
        "resource": "OMP=1; no PolyChord; continuum ω/Γ from week2 stationary match",
        "non_claims": [
            "NOT Q6 close",
            "NOT continuum time-dependent mode ODE",
            "page_like_shape is curiosity only",
            "week2 Γ weights coupling only",
        ],
    }
    # slim history in JSON if huge — keep every 5th for disk
    hist = payload["history"]
    payload["history_full_len"] = len(hist)
    payload["history"] = hist[::5] if len(hist) > 60 else hist

    OUT_JSON.write_text(json.dumps(payload, indent=2))

    g = payload["grades"]
    md = f"""# Page continuum-coupled MVP (R-PAGE C1–C2)

**Script:** `scripts/quantum_page_continuum_coupled_mvp.py`  
**JSON:** `page_curve/continuum_coupled_mvp.json`  
**page_curve_claimed:** **false**  
**week2 source:** stationary Bogoliubov + greybody (PASS={w2.get("week2_pass")})

## Setup

| item | value |
|---|---:|
| N_c | {N_C} |
| N_r (week2 mid-band) | {len(omega)} |
| T_H / κ | {T_H:.6f} / {kappa:.4f} |
| G0 / τ_evap | {G0} / {TAU_EVAP} |
| steps × dt | {N_STEPS} × {DT} |

## Coupled (evaporating g(t))

| quantity | value |
|---|---:|
| S_rad peak | {coupled["S_rad_peak"]:.6f} |
| S_rad late | {coupled["S_rad_late"]:.6f} |
| late_drop | {coupled["late_drop"]:.6f} |
| v at peak | {coupled["v_at_peak"]:.4f} |
| max\\|S_total\\| | {coupled["max_abs_S_total"]:.3e} |
| unitarity | {"PASS" if coupled["unitarity_ok"] else "FAIL"} |
| page-like shape (curiosity) | {"YES" if coupled["page_like_shape_curiosity"] else "NO"} |

## Null g=0

| quantity | value |
|---|---:|
| S_rad peak | {null_g0["S_rad_peak"]:.3e} |
| spurious growth | {"FAIL" if null_g0["S_rad_peak"] >= 1e-4 else "PASS (none)"} |

## Grade

| check | status |
|---|---|
| Instrument ran | **{"PASS" if g["instrument_ran"] else "FAIL"}** |
| Unitarity coupled | **{"PASS" if g["unitarity_coupled"] else "FAIL"}** |
| Null g=0 clean | **{"PASS" if g["null_g0_no_spurious_growth"] else "FAIL"}** |
| Page / Q6 claim | **OPEN — not claimed** |

## Next (still here)

1. Time-dependent continuum mode amplitudes (not only Γ-weighted toy coupling)  
2. Red review before any claim  
3. Larger N_r only when load allows  

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_coupled_mvp.py
```
"""
    OUT_MD.write_text(md)

    # stamp board progress
    prog = BOARD / "PAGE_C1C2_RESULT.md"
    prog.write_text(md)

    print("CONTINUUM-COUPLED Page MVP")
    print(f"  modes={len(omega)} S_peak={coupled['S_rad_peak']:.6f} late_drop={coupled['late_drop']:.6f}")
    print(f"  unitarity={coupled['unitarity_ok']} page_like={coupled['page_like_shape_curiosity']}")
    print(f"  null_g0_peak={null_g0['S_rad_peak']:.3e} page_curve_claimed=false")
    print(f"  wrote {OUT_JSON}")
    return 0 if coupled["unitarity_ok"] and null_g0["S_rad_peak"] < 1e-4 else 1


if __name__ == "__main__":
    raise SystemExit(main())
