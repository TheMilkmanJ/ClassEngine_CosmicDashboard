#!/usr/bin/env python3
"""R-PAGE P2 partial: dynamical continuum via adiabatic κ(t) snapshots + re-solved Γ(ω).

BINDING protocol:
  docs/working_logs/_runs/quantum_residual_task_20260803/PAGE_TURN_ACCEPTANCE_PROTOCOL.md

What this DOES:
  - Vary acoustic profile scale (ell) → κ(t) decreases (evaporation proxy)
  - At each snapshot, re-solve week2 exterior mode ODE → Γ(ω) (continuum dynamics
    of the *background family*, adiabatic)
  - Cumulative thermal emission + unitary Gaussian hybrid with snapshot Γ
  - Score against protocol T1–T7 / N1–N4 **without claiming** (page_curve_claimed=false)
  - Expect: not CANDIDATE TURN yet (full time-dep ψ(x,t) still missing for strict T5)

What this does NOT:
  - Full time-dependent continuum wave equation on evaporating geometry
  - Self-consistent GP
  - Q6 / Page claim (forbidden until T1–T7 + red)

Resource: OMP=1, nice recommended. 5 modes × ~6 snapshots of solve_ivp — light minutes max.
No PolyChord. Leave cobaya alone.

Usage:
  OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_dynamical_p2.py
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import sys
from pathlib import Path

import numpy as np

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs/working_logs/_runs/quantum_null_hardening_20260803"
OUT_JSON = OUT_DIR / "page_curve" / "continuum_dynamical_p2.json"
OUT_MD = OUT_DIR / "PAGE_CURVE_CONTINUUM_DYNAMICAL_P2.md"
TASK = ROOT / "docs/working_logs/_runs/quantum_residual_task_20260803"

# Light grid for loaded box
FRACS = [0.25, 0.50, 0.75, 1.00, 1.50]  # ω/κ
ELL_SCALES = [1.0, 1.25, 1.5, 1.8, 2.2, 2.8]  # increasing ell → falling κ
N_C = 3
UNITARY_MICRO = 3
DT = 0.05
G_SCALE = 0.40


def load_w2():
    path = ROOT / "scripts" / "quantum_page_bogoliubov_week2.py"
    spec = importlib.util.spec_from_file_location("qpage_w2", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def bose_n(omega: float, T: float) -> float:
    if T <= 0 or omega <= 0:
        return 0.0
    x = omega / T
    if x > 700:
        return 0.0
    return 1.0 / (math.exp(x) - 1.0)


def s_bose(n: float) -> float:
    n = max(float(n), 0.0)
    if n < 1e-15:
        return 0.0
    return (n + 1.0) * math.log(n + 1.0) - n * math.log(n)


def thermal_cov(nbar: float) -> np.ndarray:
    a = nbar + 0.5
    return np.diag([a, a])


def block_diag(mats):
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


def build_A(n_c, omega_r, gam, g_scale):
    n_r = len(omega_r)
    A = np.zeros((2 * (n_c + n_r), 2 * (n_c + n_r)))

    def qp(k):
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


def evolve(gamma, A, Omega, dt):
    K = Omega @ A

    def f(G):
        return K @ G + G @ K.T

    k1 = f(gamma)
    k2 = f(gamma + dt * k1)
    out = gamma + 0.5 * dt * (k1 + k2)
    return 0.5 * (out + out.T)


def entropy_cov(gamma_sub, Omega_sub):
    M = 1j * (Omega_sub @ gamma_sub)
    evals = np.linalg.eigvals(M)
    nus = sorted({float(abs(e.real)) for e in evals if abs(e.real) > 1e-10}, reverse=True)
    seen = []
    for nu in nus:
        if all(abs(nu - s) > 1e-7 for s in seen):
            seen.append(nu)
    S = 0.0
    for nu in seen:
        nu = max(nu, 0.5 + 1e-15)
        sp, sm = nu + 0.5, nu - 0.5
        S += sp * math.log(sp) - (sm * math.log(sm) if sm > 1e-18 else 0.0)
    return float(S)


def energy_cov(gamma, n_c, omega_r):
    e_c = e_r = 0.0
    for k in range(n_c):
        iq, ip = 2 * k, 2 * k + 1
        e_c += 0.5 * (gamma[iq, iq] + gamma[ip, ip]) - 0.5
    for j, w in enumerate(omega_r):
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        e_r += 0.5 * float(w) * (gamma[iq, iq] + gamma[ip, ip]) - 0.5 * float(w)
    return float(max(e_c, 0.0)), float(max(e_r, 0.0))


def snapshot_greybodies(w2, ell_scale: float) -> dict:
    """Re-solve continuum modes on scaled profile."""
    base_ell = 4.0
    w2.ELL = base_ell * ell_scale
    # keep V_IN, V_OUT as module defaults
    ana = w2.analytic_kappa_tanh(ell=w2.ELL)
    if not ana.get("found"):
        return {"ok": False, "ell": w2.ELL}
    kappa = float(ana["kappa"])
    T_H = float(ana["T_H"])
    rows = []
    for frac in FRACS:
        omega = frac * kappa
        m = w2.greybody_mode_match(omega, kappa, x_eps=0.05, x_out=30.0)
        g = float(m["Gamma"]) if m.get("ok") else float("nan")
        rows.append(
            {
                "frac": frac,
                "omega": omega,
                "Gamma": g,
                "n_B": bose_n(omega, T_H),
                "n_mode": (g * bose_n(omega, T_H)) if m.get("ok") else float("nan"),
                "ok": bool(m.get("ok")),
            }
        )
    n_ok = sum(1 for r in rows if r["ok"])
    return {
        "ok": n_ok >= 3,
        "ell": w2.ELL,
        "ell_scale": ell_scale,
        "kappa": kappa,
        "T_H": T_H,
        "rows": rows,
        "n_ok": n_ok,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)
    TASK.mkdir(parents=True, exist_ok=True)

    w2 = load_w2()
    snaps = []
    print("P2 dynamical continuum — adiabatic κ snapshots + re-solved Γ")
    for sc in ELL_SCALES:
        s = snapshot_greybodies(w2, sc)
        snaps.append(s)
        print(
            f"  ell_scale={sc:.2f} ell={s.get('ell', float('nan')):.3f} "
            f"κ={s.get('kappa', float('nan')):.5f} n_ok={s.get('n_ok', 0)}"
        )
        if not s.get("ok"):
            print("  WARN: sparse greybodies at this snapshot")

    good = [s for s in snaps if s.get("ok")]
    if len(good) < 3:
        print("FAIL: too few successful continuum snapshots")
        return 2

    # sort by decreasing kappa (evaporation order)
    good.sort(key=lambda s: -s["kappa"])
    n_snap = len(good)
    # align modes by frac index
    n_modes = len(FRACS)

    # --- cumulative thermal emission between snapshots ---
    # assign each interval equal Δv, T from snapshot, E budget from first atmosphere
    rows0 = good[0]["rows"]
    omegas0 = np.array([r["omega"] for r in rows0])
    # use first-snap omegas as fixed lab frequencies? Better: use frac*kappa evolving.
    # Cumulative dE/T with multi-mode n_mode from each snap:
    S_cum = 0.0
    E_cum = 0.0
    thermal_hist = []
    # budget: initial snap energy
    E_budget = 0.0
    for r in rows0:
        if r["ok"]:
            E_budget += r["omega"] * r["n_mode"]
    E_budget = max(E_budget, 1e-15)

    for i, s in enumerate(good):
        v = i / max(n_snap - 1, 1)
        T = s["T_H"]
        if i > 0:
            dv = 1.0 / max(n_snap - 1, 1)
            dE = E_budget * dv
            E_cum += dE
            S_cum += dE / max(T, 1e-12)
        S_atm = sum(s_bose(r["n_mode"]) for r in s["rows"] if r["ok"] and r["n_mode"] == r["n_mode"])
        thermal_hist.append(
            {
                "v": v,
                "kappa": s["kappa"],
                "T_H": T,
                "ell": s["ell"],
                "S_cum": S_cum,
                "S_atm": S_atm,
                "E_cum": E_cum,
                "mean_Gamma": float(
                    np.nanmean([r["Gamma"] for r in s["rows"] if r["ok"]])
                ),
            }
        )

    # --- unitary hybrid: stepwise Γ from snaps, g∝κ ---
    # fix omega to first snap absolute ω for continuous modes
    omega = np.array([r["omega"] for r in good[0]["rows"]], dtype=float)
    mats = [thermal_cov(0.0) for _ in range(N_C + n_modes)]
    gamma = block_diag(mats)
    Omega = symplectic(N_C + n_modes)
    core_sl = slice(0, 2 * N_C)
    rad_sl = slice(2 * N_C, 2 * (N_C + n_modes))
    Om_c, Om_r = Omega[core_sl, core_sl], Omega[rad_sl, rad_sl]

    unitary_hist = []
    null_g0_S = []
    # N1: g=0 path (jitter)
    gamma_n1 = gamma.copy()
    for i, s in enumerate(good):
        gam = np.array(
            [r["Gamma"] if r["ok"] else 1e-3 for r in s["rows"]], dtype=float
        )
        # map gamma to fixed omega count
        if len(gam) != n_modes:
            gam = np.resize(gam, n_modes)
        A0 = build_A(N_C, omega, gam, 0.0)
        for _ in range(UNITARY_MICRO):
            gamma_n1 = evolve(gamma_n1, A0, Omega, DT)
        S_r_n1 = entropy_cov(gamma_n1[rad_sl, rad_sl], Om_r)
        null_g0_S.append(S_r_n1)

    # N3: vacuum already ~0; record
    sigma_n1 = float(np.std(null_g0_S)) if len(null_g0_S) > 1 else 0.0
    sigma_n1 = max(sigma_n1, float(np.max(np.abs(null_g0_S))), 1e-8)
    sigma_n3 = 1e-8  # vacuum
    sigma_jit = max(sigma_n1, sigma_n3)

    gamma = block_diag([thermal_cov(0.0) for _ in range(N_C + n_modes)])
    for i, s in enumerate(good):
        gam = np.array([r["Gamma"] if r["ok"] else 1e-3 for r in s["rows"]], dtype=float)
        if len(gam) != n_modes:
            gam = np.resize(gam, n_modes)
        g_t = G_SCALE * s["kappa"]
        A = build_A(N_C, omega, gam, g_t)
        for _ in range(UNITARY_MICRO):
            gamma = evolve(gamma, A, Omega, DT)
        S_c = entropy_cov(gamma[core_sl, core_sl], Om_c)
        S_r = entropy_cov(gamma[rad_sl, rad_sl], Om_r)
        S_tot = entropy_cov(gamma, Omega)
        e_c, e_r = energy_cov(gamma, N_C, omega)
        es = e_c + e_r
        v = e_r / (es + 1e-30) if es > 1e-18 else float(i / max(n_snap - 1, 1))
        unitary_hist.append(
            {
                "snap": i,
                "kappa": s["kappa"],
                "g_t": g_t,
                "S_core": S_c,
                "S_rad": S_r,
                "S_total": S_tot,
                "E_core": e_c,
                "E_rad": e_r,
                "v": v,
            }
        )

    # Protocol scoring (claim still false)
    S = [h["S_rad"] for h in unitary_hist]
    vlist = [h["v"] for h in unitary_hist]
    i_pk = int(np.argmax(S)) if S else 0
    S_peak = S[i_pk] if S else 0.0
    v_star = vlist[i_pk] if vlist else 0.0
    v_late = vlist[-1] if vlist else 0.0
    S_late = S[-1] if S else 0.0
    drop = S_peak - S_late
    v_early = vlist[0] if vlist else 0.0
    S_early = S[0] if S else 0.0

    T1 = 0.05 <= v_star <= 0.95 and 0 < i_pk < len(S) - 1
    T2_reach = v_late >= 0.9
    T2_frac = drop >= 0.10 * S_peak if S_peak > 0 else False
    T2_noise = drop > 5.0 * sigma_jit
    T2 = T2_reach and T2_frac and T2_noise
    T3 = S_peak > S_early + 0.05 * S_peak if S_peak > 0 else False
    N1_pass = max(null_g0_S) < 1e-4 if null_g0_S else False
    N2_pass = all(
        thermal_hist[i]["S_cum"] <= thermal_hist[i + 1]["S_cum"] + 1e-12
        for i in range(len(thermal_hist) - 1)
    ) and (thermal_hist[-1]["S_cum"] >= thermal_hist[0]["S_cum"])
    # thermal should not purify to ~0 if it rose
    N2_pass = N2_pass and not (
        thermal_hist[-1]["S_cum"] < 0.1 * max(h["S_cum"] for h in thermal_hist) + 1e-15
        and max(h["S_cum"] for h in thermal_hist) > 1e-6
    )
    N3_pass = True  # vacuum seed by construction at start
    N4_pass = max(abs(h["S_total"]) for h in unitary_hist) < 0.05 if unitary_hist else False
    T4 = N1_pass and N2_pass and N3_pass and N4_pass
    # T5: adiabatic snapshot re-solve is PARTIAL dynamical continuum — NOT full time-dep ψ
    T5_strict = False  # full time-dep continuum ODE not implemented
    T5_partial = True  # re-solved Γ(κ(t)) is stronger than fixed-Γ toy
    T6 = True  # we write artifacts
    T7 = False  # must stay false

    candidate = all([T1, T2, T3, T4, T5_strict, T6])  # T5_strict fails → no candidate

    payload = {
        "milestone": "R_PAGE_P2_adiabatic_continuum_snapshots",
        "page_curve_claimed": False,
        "S_rad_v_claimed": False,
        "protocol": "PAGE_TURN_ACCEPTANCE_PROTOCOL.md BINDING",
        "n_snapshots": n_snap,
        "n_modes": n_modes,
        "fracs": FRACS,
        "ell_scales": ELL_SCALES,
        "snapshots": [
            {
                "ell": s["ell"],
                "kappa": s["kappa"],
                "T_H": s["T_H"],
                "n_ok": s["n_ok"],
                "mean_Gamma": float(np.nanmean([r["Gamma"] for r in s["rows"] if r["ok"]])),
            }
            for s in good
        ],
        "thermal_hist": thermal_hist,
        "unitary_hist": unitary_hist,
        "null_g0_S_series": null_g0_S,
        "sigma_jit": sigma_jit,
        "v_late": v_late,
        "v_star": v_star,
        "S_peak": S_peak,
        "S_late": S_late,
        "drop": drop,
        "protocol_eval": {
            "T1_interior_max": T1,
            "T2_reach_v_ge_0.9": T2_reach,
            "T2_frac_drop": T2_frac,
            "T2_noise_floor": T2_noise,
            "T2_all": T2,
            "T3_early_rise": T3,
            "T4_nulls": T4,
            "N1_g0": N1_pass,
            "N2_thermal": N2_pass,
            "N3_vacuum": N3_pass,
            "N4_unitarity": N4_pass,
            "T5_strict_dynamical_continuum": T5_strict,
            "T5_partial_adiabatic_resolves": T5_partial,
            "T6_artifacts": T6,
            "T7_claim_flag": T7,
            "CANDIDATE_TURN": candidate,
            "page_curve_claimed": False,
        },
        "gap_to_candidate": "T5_strict: need time-dependent continuum field evolution, not only adiabatic Γ(κ) snapshots",
        "resource": "OMP=1; no PolyChord; week2 mode ODE re-solved per snapshot",
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    pe = payload["protocol_eval"]
    md = f"""# P2 dynamical continuum (adiabatic snapshots) — instrument

**Script:** `scripts/quantum_page_continuum_dynamical_p2.py`  
**Protocol:** BINDING `PAGE_TURN_ACCEPTANCE_PROTOCOL.md`  
**page_curve_claimed:** **false**  
**CANDIDATE_TURN:** **{candidate}**

## What advanced

- Acoustic profile scaled (ell↑ ⇒ κ↓) as evaporation proxy  
- At each snapshot: **re-solved** week2 exterior mode ODE → Γ(ω) (continuum, not frozen table)  
- Thermal cumulative + unitary hybrid with snapshot Γ  
- Full protocol scorecard T1–T7 / N1–N4  

## Snapshot table

| ell | κ | T_H | mean Γ | n_ok |
|---:|---:|---:|---:|---:|
"""
    for s in good:
        md += (
            f"| {s['ell']:.3f} | {s['kappa']:.5f} | {s['T_H']:.5f} | "
            f"{float(np.nanmean([r['Gamma'] for r in s['rows'] if r['ok']])):.3f} | {s['n_ok']} |\n"
        )

    md += f"""
## Protocol evaluation (unitary hybrid)

| test | result |
|---|---|
| T1 interior max | **{pe['T1_interior_max']}** |
| T2 v_late≥0.9 | **{pe['T2_reach_v_ge_0.9']}** (v_late={v_late:.3f}) |
| T2 frac drop ≥0.10 | **{pe['T2_frac_drop']}** (drop={drop:.4f}, S*={S_peak:.4f}) |
| T2 drop >5 σ_jit | **{pe['T2_noise_floor']}** (σ_jit={sigma_jit:.3e}) |
| T2 all | **{pe['T2_all']}** |
| T3 early rise | **{pe['T3_early_rise']}** |
| T4 nulls | **{pe['T4_nulls']}** (N1={N1_pass}, N2={N2_pass}, N4={N4_pass}) |
| T5 strict dynamical continuum | **{pe['T5_strict_dynamical_continuum']}** |
| T5 partial (adiabatic re-solve) | **{pe['T5_partial_adiabatic_resolves']}** |
| T6 artifacts | **{pe['T6_artifacts']}** |
| T7 claim | **false** |
| **CANDIDATE TURN** | **{candidate}** |

## Grade

**INSTRUMENT PASS** (continuum re-solved along evaporation family).  
**Not CANDIDATE TURN** — fails T5 strict (no time-dependent continuum field \(\\psi(x,t)\)).  
**page_curve_claimed: false**

## Gap

Full P2 for protocol T5: evolve continuum modes in time on evaporating geometry (or
controlled non-adiabatic Bogoliubov), not only adiabatic snapshot greybodies.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_dynamical_p2.py
```
"""
    # fix double escape in md
    md = md.replace("\\\\psi", "\\psi")
    OUT_MD.write_text(md)
    (TASK / "PAGE_P2_DYNAMICAL_RESULT.md").write_text(md)

    print("PROTOCOL CANDIDATE_TURN=", candidate, "page_curve_claimed=false")
    print(f"  T5_strict={T5_strict} T5_partial={T5_partial} T4={T4} T2={T2}")
    print(f"  wrote {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
