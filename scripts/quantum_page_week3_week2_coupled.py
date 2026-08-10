#!/usr/bin/env python3
"""Week3 skeleton seeded by week2 Hawking spectrum — instrument only.

NO FABRICATIONS. page_curve_claimed = False always.

What this does:
  - Load week2_bogoliubov.json near_horizon_beta table (ω, n_B)
  - Build week3 Gaussian core+rad with rad modes at those ω and n_B (or Γ n_B if present)
  - Evolve with same bilinear coupling as week3 skeleton
  - Compare late_drop flag vs baseline toy spectrum

What this does NOT:
  - Claim Page turn / Q6 close
  - Continuum mode ODE evolution (still Gaussian toy)
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from quantum_page_core_skeleton_week3 import (
    DT,
    G_COUPLE,
    N_C,
    N_STEPS,
    T_H,
    block_diag,
    energy_proxy,
    entropy_from_cov,
    evolve_cov,
    hamiltonian_matrix,
    symplectic_form,
    thermal_cov_1mode,
)

W2 = Path("docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week2_bogoliubov.json")
OUT = Path("docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_week2_coupled.json")
OUT_MD = Path("docs/working_logs/_runs/derivation_sprint_20260803/P1b_PAGE_WEEK2_COUPLED.md")


def run_with_spectrum(omegas: np.ndarray, nbars: np.ndarray, g: float = G_COUPLE) -> dict:
    n_r = len(omegas)
    core = [thermal_cov_1mode(0.0) for _ in range(N_C)]
    rad = [thermal_cov_1mode(float(n)) for n in nbars]
    gamma = block_diag(core + rad)
    Omega = symplectic_form(N_C + n_r)
    A = hamiltonian_matrix(N_C, n_r, g, omegas)
    core_idx = slice(0, 2 * N_C)
    rad_idx = slice(2 * N_C, 2 * (N_C + n_r))
    Omega_c = Omega[core_idx, core_idx]
    Omega_r = Omega[rad_idx, rad_idx]

    history = []
    S_rads = []
    for step in range(N_STEPS + 1):
        g_c = gamma[core_idx, core_idx]
        g_r = gamma[rad_idx, rad_idx]
        S_c = entropy_from_cov(g_c, Omega_c)
        S_r = entropy_from_cov(g_r, Omega_r)
        e_c, e_r = energy_proxy(gamma, N_C, n_r, omegas)
        v = e_r / (e_c + e_r + 1e-15)
        history.append({"t": step * DT, "S_core": S_c, "S_rad": S_r, "v": v, "E_core": e_c, "E_rad": e_r})
        S_rads.append(S_r)
        if step < N_STEPS:
            gamma = 0.5 * (evolve_cov(gamma, A, Omega, DT) + evolve_cov(gamma, A, Omega, DT).T)

    arr = np.array(S_rads)
    peak_i = int(np.argmax(arr))
    late = float(arr[-1])
    peak = float(arr[peak_i])
    return {
        "peak_S_rad": peak,
        "peak_v": history[peak_i]["v"],
        "late_S_rad": late,
        "late_drop": late < peak - 1e-6 and peak_i < len(arr) - 5,
        "history_len": len(history),
        "n_r": n_r,
        "omegas": omegas.tolist(),
        "nbars": nbars.tolist(),
    }


def main() -> int:
    w2 = json.loads(W2.read_text())
    rows = w2.get("near_horizon_beta") or []
    # Prefer mode_matching n if available
    mm = w2.get("mode_matching") or []
    if mm and isinstance(mm, list) and "n_mode" in (mm[0] or {}):
        omegas = np.array([float(r["omega"]) for r in mm], dtype=float)
        nbars = np.array([float(r.get("n_mode", r.get("n_B", 0.0))) for r in mm], dtype=float)
        source = "mode_matching.n_mode"
    else:
        omegas = np.array([float(r["omega"]) for r in rows], dtype=float)
        nbars = np.array([float(r["n_B"]) for r in rows], dtype=float)
        source = "near_horizon_beta.n_B"

    # Cap occupations for numerical stability of Gaussian entropy
    nbars = np.clip(nbars, 0.0, 20.0)
    # Take up to 8 mid-band modes
    if len(omegas) > 8:
        omegas, nbars = omegas[:8], nbars[:8]

    coupled = run_with_spectrum(omegas, nbars, G_COUPLE)
    null_g0 = run_with_spectrum(omegas, nbars, 0.0)

    out = {
        "milestone": "P1b_week3_seeded_by_week2",
        "page_curve_claimed": False,
        "S_rad_v_claimed": False,
        "spectrum_source": source,
        "week2_T_H": w2.get("analytic", {}).get("T_H", T_H),
        "coupled": coupled,
        "null_g0": null_g0,
        "non_claims": [
            "NOT a Page-curve derivation",
            "Gaussian toy + bilinear coupling only",
            "week2 continuum ODE not evolved here — occupations seed only",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2))

    md = f"""# P1b — Week3 skeleton seeded by week2 spectrum

**page_curve_claimed: false**

## Setup
- Spectrum source: **{source}**
- Modes: {len(omegas)} (ω from week2; n̄ clipped ≤20 for Gaussian stability)
- Coupling: g={G_COUPLE} vs g=0 null

## Results (instrument)

| run | peak S_rad | late S_rad | late_drop |
|---|---:|---:|---|
| week2-seeded g={G_COUPLE} | {coupled['peak_S_rad']:.6g} | {coupled['late_S_rad']:.6g} | {coupled['late_drop']} |
| null g=0 | {null_g0['peak_S_rad']:.6g} | {null_g0['late_S_rad']:.6g} | {null_g0['late_drop']} |

## Non-claims
Not Q6. Not continuum Page. Not PRTOE result.

## Recompute
```bash
python3 scripts/quantum_page_week3_week2_coupled.py
```
"""
    OUT_MD.write_text(md)
    print(md)
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
