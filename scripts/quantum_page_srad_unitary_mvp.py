#!/usr/bin/env python3
"""Page-curve *instrument* MVP: unitary Gaussian core+rad, S_rad(v) recorded.

Resource: single-thread numpy only. Do NOT run under heavy MPI. No PolyChord.

Physics intent (plan Milestone C):
  - Pure global Gaussian state (vacuum seed)
  - Quadratic H with free terms + two-mode-squeezing-like core↔rad couplings
    (pair creation proxy for Hawking, NOT continuum sonic modes)
  - Evolve covariances; record S_core, S_rad, S_sum vs energy fraction v
  - Unitarity null: pure global ⇒ S_total ≈ 0 within numerr

HARD NON-CLAIMS:
  - page_curve_claimed = false always in this script (instrument grade)
  - Not continuum week2 modes; not self-consistent GP; not Q6 close
  - A late drop in S_rad is *curiosity* until continuum + red AGREE

Usage (from repo root, leave headroom for cobaya):
  OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_srad_unitary_mvp.py
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path

import numpy as np

# Single-thread BLAS if available
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
OUT_JSON = OUT_DIR / "page_curve" / "srad_unitary_mvp.json"
OUT_MD = OUT_DIR / "PAGE_CURVE_SRAD_UNITARY_MVP.md"

# Small so it finishes in seconds on a loaded 6c/12t box
N_C = 3
N_R = 6
N_STEPS = 200
DT = 0.02
G_SQUEEZE = 0.12  # pair-creation strength
KAPPA = 0.125
T_H = KAPPA / (2.0 * math.pi)


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


def omega_symplectic(n_modes: int) -> np.ndarray:
    blocks = [np.array([[0.0, 1.0], [-1.0, 0.0]]) for _ in range(n_modes)]
    return block_diag(blocks)


def build_A(n_c: int, n_r: int, g: float, omega_r: np.ndarray) -> np.ndarray:
    """Quadratic A: free core ω=1, free rad ω_j, TMS-like g(q_c p_r + p_c q_r) pairs."""
    n = n_c + n_r
    dim = 2 * n
    A = np.zeros((dim, dim))

    def qp(k: int) -> tuple[int, int]:
        return 2 * k, 2 * k + 1

    for k in range(n_c):
        iq, ip = qp(k)
        A[iq, iq] = 1.0
        A[ip, ip] = 1.0
    for j in range(n_r):
        iq, ip = qp(n_c + j)
        w = float(omega_r[j])
        A[iq, iq] = w
        A[ip, ip] = w
    # pair-creation style: couple core mode k to rad mode k (mod)
    n_pair = min(n_c, n_r)
    for k in range(n_pair):
        iq_c, ip_c = qp(k)
        iq_r, ip_r = qp(n_c + k)
        # g (q_c p_r + p_c q_r) → off-diagonal in A
        A[iq_c, ip_r] += g
        A[ip_r, iq_c] += g
        A[ip_c, iq_r] += g
        A[iq_r, ip_c] += g
    return A


def evolve_cov_heun(gamma: np.ndarray, A: np.ndarray, Omega: np.ndarray, dt: float) -> np.ndarray:
    K = Omega @ A

    def f(G):
        return K @ G + G @ K.T

    k1 = f(gamma)
    k2 = f(gamma + dt * k1)
    return gamma + 0.5 * dt * (k1 + k2)


def entropy_from_cov(gamma_sub: np.ndarray, Omega_sub: np.ndarray) -> float:
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


def energy_excess(gamma: np.ndarray, n_c: int, n_r: int, omega_r: np.ndarray) -> tuple[float, float]:
    e_c = e_r = 0.0
    for k in range(n_c):
        iq, ip = 2 * k, 2 * k + 1
        e_c += 0.5 * (gamma[iq, iq] + gamma[ip, ip]) - 0.5
    for j in range(n_r):
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        w = float(omega_r[j])
        e_r += 0.5 * w * (gamma[iq, iq] + gamma[ip, ip]) - 0.5 * w
    return float(max(e_c, 0.0)), float(max(e_r, 0.0))


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)

    omega_r = np.linspace(0.8, 4.0, N_R) * T_H * 8.0
    omega_r = np.maximum(omega_r, 0.02)

    # Pure vacuum everywhere (pure global Gaussian)
    mats = [thermal_cov(0.0) for _ in range(N_C + N_R)]
    gamma = block_diag(mats)
    Omega = omega_symplectic(N_C + N_R)
    A = build_A(N_C, N_R, G_SQUEEZE, omega_r)

    core_sl = slice(0, 2 * N_C)
    rad_sl = slice(2 * N_C, 2 * (N_C + N_R))
    Om_c = Omega[core_sl, core_sl]
    Om_r = Omega[rad_sl, rad_sl]
    Om_all = Omega

    history = []
    for step in range(N_STEPS + 1):
        t = step * DT
        S_c = entropy_from_cov(gamma[core_sl, core_sl], Om_c)
        S_r = entropy_from_cov(gamma[rad_sl, rad_sl], Om_r)
        S_tot = entropy_from_cov(gamma, Om_all)
        e_c, e_r = energy_excess(gamma, N_C, N_R, omega_r)
        e_sum = e_c + e_r
        v = e_r / (e_sum + 1e-30) if e_sum > 1e-18 else 0.0
        history.append(
            {
                "t": t,
                "S_core": S_c,
                "S_rad": S_r,
                "S_total": S_tot,
                "E_core": e_c,
                "E_rad": e_r,
                "v": v,
            }
        )
        if step < N_STEPS:
            gamma = evolve_cov_heun(gamma, A, Omega, DT)
            # keep symmetric
            gamma = 0.5 * (gamma + gamma.T)

    S_rads = [h["S_rad"] for h in history]
    vs = [h["v"] for h in history]
    S_tots = [h["S_total"] for h in history]
    i_peak = int(np.argmax(S_rads))
    S_peak = S_rads[i_peak]
    S_late = S_rads[-1]
    late_drop = S_peak - S_late
    # crude Page-like: peak not at end and late drop > 10% of peak
    page_like_shape = (
        i_peak > 2
        and i_peak < len(S_rads) - 3
        and S_peak > 1e-6
        and late_drop > 0.1 * S_peak
    )
    unitarity_ok = max(abs(s) for s in S_tots) < 0.05  # pure → ~0; allow numerical leak

    payload = {
        "milestone": "C_srad_unitary_mvp",
        "page_curve_claimed": False,
        "S_rad_v_is_physical_page": False,
        "page_like_shape_curiosity": bool(page_like_shape),
        "unitarity_S_total_near_zero": bool(unitarity_ok),
        "max_abs_S_total": float(max(abs(s) for s in S_tots)),
        "N_c": N_C,
        "N_r": N_R,
        "g_squeeze": G_SQUEEZE,
        "n_steps": N_STEPS,
        "dt": DT,
        "kappa_bookkeeping": KAPPA,
        "T_H_bookkeeping": T_H,
        "S_rad_peak": float(S_peak),
        "S_rad_late": float(S_late),
        "late_drop": float(late_drop),
        "i_peak": i_peak,
        "v_at_peak": float(vs[i_peak]),
        "history": history,
        "resource": "OMP_NUM_THREADS=1; no MPI; no PolyChord",
        "non_claims": [
            "not continuum sonic modes",
            "not GP self-consistent evaporation",
            "not Q6 close",
            "page_like_shape is curiosity only",
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    md = f"""# Page S_rad(v) unitary MVP — instrument only

**Script:** `scripts/quantum_page_srad_unitary_mvp.py`  
**JSON:** `page_curve/srad_unitary_mvp.json`  
**page_curve_claimed:** **false**  
**Resource:** single-thread; no PolyChord; niced vs cobaya MCMCs.

## Numbers

| quantity | value |
|---|---:|
| N_c, N_r | {N_C}, {N_R} |
| S_rad peak | {S_peak:.6f} |
| S_rad late | {S_late:.6f} |
| late_drop | {late_drop:.6f} |
| v at peak | {vs[i_peak]:.4f} |
| max\\|S_total\\| | {payload["max_abs_S_total"]:.3e} |
| unitarity (S_total~0) | {"PASS" if unitarity_ok else "FAIL"} |
| page-like shape (curiosity) | {"YES" if page_like_shape else "NO"} |

## Grade

**Instrument PASS** if the run completes and unitarity holds.  
**Page curve / Q6:** still **OPEN** — continuum modes + red required before any claim.

## Forbidden readings

- Do not book page-like shape as PRTOE Page turn  
- Do not replace continuum Hawking with this toy TMS coupling  

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_srad_unitary_mvp.py
```
"""
    OUT_MD.write_text(md)

    print("PAGE S_rad unitary MVP")
    print(f"  S_peak={S_peak:.6f} S_late={S_late:.6f} late_drop={late_drop:.6f}")
    print(f"  max|S_total|={payload['max_abs_S_total']:.3e} unitarity={'PASS' if unitarity_ok else 'FAIL'}")
    print(f"  page_like_shape_curiosity={page_like_shape} page_curve_claimed=false")
    print(f"  wrote {OUT_JSON}")
    print(f"  wrote {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
