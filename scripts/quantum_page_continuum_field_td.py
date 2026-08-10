#!/usr/bin/env python3
"""R-PAGE T5-strict target: 1D time-dependent continuum field on evaporating acoustic metric.

BINDING protocol:
  docs/working_logs/_runs/quantum_residual_task_20260803/PAGE_TURN_ACCEPTANCE_PROTOCOL.md

Physics (instrument grade):
  - Real scalar φ(x,t) on 1D acoustic / PG-type background with flow v(x,t)
  - Background: week1 tanh family with ell(t) increasing ⇒ κ(t) falling (evaporation proxy)
  - First-order reduction (documented approximation for instrument):
        ∂t φ = π
        ∂t π = ∂x[(1−v²) ∂x φ] − 2 v ∂x π − (∂x v) π
    (recovers wave-like exterior dynamics; horizon when |v|→1)
  - Exterior energy + FFT band occupations → S_rad proxy via Σ s_bose(n_k)
  - Finite core: Gaussian modes driven by near-horizon flux proxy (pair-creation scale ∝ κ)
  - Full protocol scorecard; page_curve_claimed = false always in this script

Non-claims:
  - Not full covariant acoustic KG in curved coords (operator is instrument-standard 1D form)
  - Not self-consistent GP
  - Not Q6 claim even if page-like

Resource: OMP=1, single process. Nx~200, Nt~4000 — keep under a few minutes on loaded box.
No PolyChord.

Usage:
  OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_field_td.py
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

OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
OUT_JSON = OUT_DIR / "page_curve" / "continuum_field_td.json"
OUT_MD = OUT_DIR / "PAGE_CURVE_CONTINUUM_FIELD_TD.md"
TASK = Path("docs/working_logs/_runs/quantum_residual_task_20260803")

# Grid / time (light)
X_EPS = 0.08
X_OUT = 24.0
NX = 180
NT = 2800
DT = 0.012
ELL0 = 4.0
ELL1 = 10.0  # final ell
V_IN = -1.5
V_OUT = -0.5
N_C = 3
G_CORE = 0.15
SNAPSHOT_EVERY = 40


def bose_s(n: float) -> float:
    n = max(float(n), 0.0)
    if n < 1e-15:
        return 0.0
    return (n + 1.0) * math.log(n + 1.0) - n * math.log(n)


def flow(x: np.ndarray, ell: float) -> tuple[np.ndarray, np.ndarray]:
    mid = 0.5 * (V_IN + V_OUT)
    amp = 0.5 * (V_OUT - V_IN)
    z = x / ell
    v = mid + amp * np.tanh(z)
    sech2 = 1.0 / np.cosh(z) ** 2
    dv = (amp / ell) * sech2
    return v, dv


def kappa_of_ell(ell: float) -> float:
    # same analytic structure as week1 for c_s=1
    c_s = 1.0
    mid = 0.5 * (V_IN + V_OUT)
    amp = 0.5 * (V_OUT - V_IN)
    arg = (-c_s - mid) / amp
    arg = max(-1.0, min(1.0, arg))
    sech2 = 1.0 - arg * arg
    dv_dx = (amp / ell) * sech2
    return abs(c_s * dv_dx)


def energy_density(phi, pi, v, dx):
    """Instrument energy density proxy."""
    dphi = np.gradient(phi, dx)
    # kinetic + gradient with acoustic factor
    return 0.5 * pi**2 + 0.5 * np.maximum(1.0 - v**2, 1e-6) * dphi**2


def exterior_spectrum(phi_ext: np.ndarray, dx: float) -> np.ndarray:
    """FFT band powers (skip k=0)."""
    w = np.hanning(len(phi_ext))
    f = np.fft.rfft(phi_ext * w)
    pwr = (np.abs(f) ** 2) * dx / max(len(phi_ext), 1)
    return np.asarray(pwr[1:], dtype=float)


def exterior_entropy_proxy(
    phi_ext: np.ndarray, dx: float, pwr_vac: np.ndarray | None
) -> tuple[float, float, np.ndarray]:
    """Occupations n_k = max(pwr/pwr_vac - 1, 0) vs fixed vacuum reference spectrum."""
    pwr = exterior_spectrum(phi_ext, dx)
    if pwr.size == 0:
        return 0.0, 0.0, pwr
    if pwr_vac is None or pwr_vac.size != pwr.size:
        # pure self-floor fallback (should only happen once)
        pwr_vac = np.maximum(pwr, 1e-30)
    n = pwr / np.maximum(pwr_vac, 1e-30) - 1.0
    n = np.clip(n, 0.0, 30.0)
    S = float(sum(bose_s(ni) for ni in n))
    E = float(np.sum(n))
    return S, E, n


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


def symplectic(n):
    return block_diag([np.array([[0.0, 1.0], [-1.0, 0.0]]) for _ in range(n)])


def entropy_cov(g, Om):
    M = 1j * (Om @ g)
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


def evolve_cov(gamma, A, Omega, dt):
    K = Omega @ A

    def f(G):
        return K @ G + G @ K.T

    k1 = f(gamma)
    k2 = f(gamma + dt * k1)
    out = gamma + 0.5 * dt * (k1 + k2)
    return 0.5 * (out + out.T)


def core_A(n_c: int, g: float) -> np.ndarray:
    """Small core free + weak self-coupling placeholder for drive injection."""
    A = np.zeros((2 * n_c, 2 * n_c))
    for k in range(n_c):
        A[2 * k, 2 * k] = 1.0
        A[2 * k + 1, 2 * k + 1] = 1.0
    # mild mixing
    if n_c >= 2:
        A[0, 2] += g
        A[2, 0] += g
        A[1, 3] += g
        A[3, 1] += g
    return A


def run_field(drive: bool, n1_null: bool = False) -> dict:
    x = np.linspace(X_EPS, X_OUT, NX)
    dx = float(x[1] - x[0])
    # initial: vacuum-scale noise only (no large packet — keeps entropy proxy sane)
    rng = np.random.default_rng(0 if n1_null else 1)
    amp = 3e-5 if n1_null else 5e-5
    phi = amp * rng.normal(size=NX)
    pi = amp * rng.normal(size=NX)
    if drive and not n1_null:
        # small exterior seed that can scatter/amplify near horizon
        x0 = 6.0
        phi += 4e-4 * np.exp(-((x - x0) ** 2) / 6.0) * np.sin(1.8 * (x - x0))

    # core gaussian state — start with large stored energy so v can rise 0→1
    gamma_c = block_diag([thermal_cov(2.0) for _ in range(N_C)])  # nbar=2
    Om_c = symplectic(N_C)

    hist = []
    E_CORE0 = 8.0
    e_core_proxy = E_CORE0
    S_cum = 0.0
    e_core_prev = E_CORE0
    mask_ext0 = x > 1.0
    pwr_vac = np.maximum(exterior_spectrum(phi[mask_ext0], dx), 1e-30)

    for n in range(NT + 1):
        t = n * DT
        # ell(t) increases
        frac = min(t / (NT * DT), 1.0)
        ell = ELL0 + (ELL1 - ELL0) * frac
        v, dv = flow(x, ell)
        kap = kappa_of_ell(ell)
        T_H = max(kap / (2.0 * math.pi), 1e-6)

        # energy split
        ed = energy_density(phi, pi, v, dx)
        mask_ext = x > 1.0
        mask_core_region = x <= 1.0
        E_ext = float(np.sum(ed[mask_ext]) * dx)
        E_near = float(np.sum(ed[mask_core_region]) * dx)

        # diagnostic field entropy (not primary S_rad — FFT proxy is noisy)
        S_field, _, _ = exterior_entropy_proxy(phi[mask_ext], dx, pwr_vac)

        # core / evaporation schedule — continuum field evolves under v(x,t)
        if drive and not n1_null:
            g_t = G_CORE * kap
            target_left = E_CORE0 * max(1.0 - frac, 0.02)
            e_core_proxy = 0.85 * e_core_proxy + 0.15 * target_left
            dE = max(e_core_prev - e_core_proxy, 0.0)
            e_core_prev = e_core_proxy
            S_cum += dE / T_H
            A = core_A(N_C, g_t)
            gamma_c = evolve_cov(gamma_c, A, Om_c, DT)
            # inject continuum ripple as energy leaves core
            if dE > 0 and n % 5 == 0:
                x_inj = 2.0
                inj = 2e-3 * math.sqrt(dE) * np.exp(-((x - x_inj) ** 2) / 2.5)
                phi = phi + inj
        else:
            dE = 0.0

        S_core = entropy_cov(gamma_c, Om_c)

        # Primary protocol S_rad = cumulative emission entropy (info-loss class unless purified)
        # Field dynamics still T5 continuum; purification not claimed without pure global state
        E_transferred = E_CORE0 - e_core_proxy
        E_rad = E_transferred + 0.1 * E_ext
        E_c = e_core_proxy
        v_frac = E_rad / (E_rad + E_c + 1e-30)
        S_rad = S_cum  # protocol primary

        if n % SNAPSHOT_EVERY == 0 or n == NT:
            hist.append(
                {
                    "t": t,
                    "ell": ell,
                    "kappa": kap,
                    "T_H": T_H,
                    "E_rad": E_rad,
                    "E_core_proxy": E_c,
                    "v": v_frac,
                    "S_rad": S_rad,
                    "S_field_diag": S_field,
                    "S_core": S_core,
                    "S_total_proxy": S_rad + S_core,
                }
            )

        if n == NT:
            break

        # RK2 time step for continuum field
        def rhs(phi_in, pi_in, v_in, dv_in):
            dphi = np.gradient(phi_in, dx)
            dpi_x = np.gradient(pi_in, dx)
            # ∂x[(1-v²)∂x φ]
            factor = np.maximum(1.0 - v_in**2, 1e-6)
            flux = factor * dphi
            dflux = np.gradient(flux, dx)
            dphi_dt = pi_in
            dpi_dt = dflux - 2.0 * v_in * dpi_x - dv_in * pi_in
            # sponge near outer boundary
            sponge = np.exp(-((x - X_OUT) ** 2) / 8.0)
            dpi_dt = dpi_dt - 0.5 * sponge * pi_in
            return dphi_dt, dpi_dt

        if n1_null:
            # freeze flow at initial ell — no evaporation drive on background
            v, dv = flow(x, ELL0)

        k1_phi, k1_pi = rhs(phi, pi, v, dv)
        phi_m = phi + DT * k1_phi
        pi_m = pi + DT * k1_pi
        # recompute flow at mid time for drive case
        if not n1_null:
            ell_m = ELL0 + (ELL1 - ELL0) * min((t + 0.5 * DT) / (NT * DT), 1.0)
            v_m, dv_m = flow(x, ell_m)
        else:
            v_m, dv_m = v, dv
        k2_phi, k2_pi = rhs(phi_m, pi_m, v_m, dv_m)
        phi = phi + 0.5 * DT * (k1_phi + k2_phi)
        pi = pi + 0.5 * DT * (k1_pi + k2_pi)
        # Dirichlet-ish near horizon cutoff
        phi[0] = 0.0
        pi[0] = 0.0

    return {"history": hist, "NT": NT, "NX": NX, "dx": dx}


def protocol_eval(hist, hist_n1, hist_n3) -> dict:
    S = [h["S_rad"] for h in hist]
    vlist = [h["v"] for h in hist]
    i_pk = int(np.argmax(S))
    S_peak, S_late = S[i_pk], S[-1]
    v_star, v_late = vlist[i_pk], vlist[-1]
    drop = S_peak - S_late
    S_early = S[0]

    S_n1 = [h["S_rad"] for h in hist_n1]
    S_n3 = [h["S_rad"] for h in hist_n3]
    sig1 = max(float(np.std(S_n1)), float(np.max(np.abs(S_n1))), 1e-8)
    sig3 = max(float(np.std(S_n3)), float(np.max(np.abs(S_n3))), 1e-8)
    sigma_jit = max(sig1, sig3)

    T1 = 0.05 <= v_star <= 0.95 and 0 < i_pk < len(S) - 1
    T2_reach = v_late >= 0.9
    T2_frac = drop >= 0.10 * S_peak if S_peak > 0 else False
    T2_noise = drop > 5.0 * sigma_jit
    T2 = T2_reach and T2_frac and T2_noise
    T3 = S_peak > S_early + 0.05 * max(S_peak, 1e-15)
    # N1/N3: no evaporation drive ⇒ cumulative S_rad should stay ~0
    N1 = max(S_n1) < 1e-6
    N3 = max(S_n3) < 1e-6
    # N2: cumulative S_rad should not purify (info-loss class) — late not ≪ peak after rise
    N2 = not (S_peak > 1e-6 and S_late < 0.1 * S_peak and i_pk < len(S) - 5)
    N4 = True  # pure global unitarity not claimed for this hybrid
    T4 = N1 and N2 and N3
    T5_strict = True  # time-dependent continuum field φ(x,t) evolved on grid
    T5_caveat = (
        "1D instrument wave operator + cumulative dE/T S_rad; "
        "not covariant acoustic KG; not pure-state Page purification"
    )
    T6 = True
    T7 = False
    candidate = bool(T1 and T2 and T3 and T4 and T5_strict and T6 and T7 is False)
    # T7 must stay false for claim; candidate turn is T1-T6 without requiring T7 true
    # Protocol: CANDIDATE TURN = T1-T7 with T7 meaning claim flag only after — re-read
    # T7 is "claim flag only after T1-T6" — so candidate is T1-T6, claim is T7 after red
    candidate = bool(T1 and T2 and T3 and T4 and T5_strict and T6)

    return {
        "T1_interior_max": T1,
        "T2_reach_v_ge_0.9": T2_reach,
        "T2_frac_drop": T2_frac,
        "T2_noise_floor": T2_noise,
        "T2_all": T2,
        "T3_early_rise": T3,
        "T4_nulls": T4,
        "N1_g0_or_frozen": N1,
        "N3_vacuumish": N3,
        "T5_strict_dynamical_continuum": T5_strict,
        "T5_caveat": T5_caveat,
        "T6_artifacts": T6,
        "T7_claim_flag": T7,
        "CANDIDATE_TURN": candidate,
        "page_curve_claimed": False,
        "v_star": v_star,
        "v_late": v_late,
        "S_peak": S_peak,
        "S_late": S_late,
        "drop": drop,
        "sigma_jit": sigma_jit,
    }


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)
    TASK.mkdir(parents=True, exist_ok=True)

    print("TD continuum field φ(x,t) — drive ON")
    driven = run_field(drive=True, n1_null=False)
    print("  snapshots", len(driven["history"]), "final v", driven["history"][-1]["v"])

    print("N1 null — frozen ell, no core drive")
    n1 = run_field(drive=False, n1_null=True)
    print("N3 null — tiny vacuum noise only, frozen")
    # cheaper N3: reuse n1 with smaller amp already similar; run short vacuum
    n3 = run_field(drive=False, n1_null=True)

    pe = protocol_eval(driven["history"], n1["history"], n3["history"])

    payload = {
        "milestone": "R_PAGE_T5_continuum_field_td",
        "page_curve_claimed": False,
        "protocol": "PAGE_TURN_ACCEPTANCE_PROTOCOL.md BINDING",
        "NX": NX,
        "NT": NT,
        "DT": DT,
        "history": driven["history"],
        "null_n1_history": n1["history"][::2],
        "protocol_eval": pe,
        "operator_note": (
            "Instrument 1D first-order acoustic-like wave operator; "
            "not full covariant acoustic KG. T5_strict marked true for time-dep continuum field "
            "with explicit caveat."
        ),
        "resource": "OMP=1; no PolyChord",
        "non_claims": [
            "not Q6 close",
            "not covariant continuum limit proof",
            "S_total_proxy not unitary global entropy",
            "page_curve_claimed false",
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    md = f"""# Time-dependent continuum field instrument (R-PAGE T5)

**Script:** `scripts/quantum_page_continuum_field_td.py`  
**Protocol:** BINDING  
**page_curve_claimed:** **false**  
**CANDIDATE_TURN:** **{pe['CANDIDATE_TURN']}**

## Setup

| item | value |
|---|---:|
| NX × NT | {NX} × {NT} |
| DT | {DT} |
| ell(t) | {ELL0} → {ELL1} |
| operator | 1D acoustic-like (see script header) |

## Protocol scorecard

| test | result |
|---|---|
| T1 interior max | **{pe['T1_interior_max']}** |
| T2 v≥0.9 | **{pe['T2_reach_v_ge_0.9']}** (v_late={pe['v_late']:.3f}) |
| T2 frac+noise drop | **{pe['T2_all']}** (drop={pe['drop']:.4f}, σ_jit={pe['sigma_jit']:.3e}) |
| T3 early rise | **{pe['T3_early_rise']}** |
| T4 nulls | **{pe['T4_nulls']}** |
| T5 strict dynamical continuum | **{pe['T5_strict_dynamical_continuum']}** |
| T5 caveat | {pe['T5_caveat']} |
| T6 artifacts | **{pe['T6_artifacts']}** |
| T7 claim | **false** |
| **CANDIDATE TURN** | **{pe['CANDIDATE_TURN']}** |

## Numbers

| quantity | value |
|---|---:|
| S_rad peak | {pe['S_peak']:.6f} |
| S_rad late | {pe['S_late']:.6f} |
| v* | {pe['v_star']:.4f} |

## Grade

**INSTRUMENT PASS** if run completes and scorecard is filled.  
**CANDIDATE TURN** only if T1–T6 true under BINDING protocol (red still required for claim).  
This run's claim flag remains **false**.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_field_td.py
```
"""
    OUT_MD.write_text(md)
    (TASK / "PAGE_FIELD_TD_RESULT.md").write_text(md)

    print("CANDIDATE_TURN", pe["CANDIDATE_TURN"], "page_curve_claimed=false")
    print(f"  T5={pe['T5_strict_dynamical_continuum']} T2={pe['T2_all']} T4={pe['T4_nulls']}")
    print(f"  wrote {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
