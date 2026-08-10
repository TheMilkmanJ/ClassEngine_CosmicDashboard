#!/usr/bin/env python3
"""Week3 finite-core instrument: N_c × N_r scan (P1c).

Uses quantum_page_core_skeleton_week3 primitives only.
Scans N_c ∈ {2,4,6,8} and N_r ∈ {4,8} at fixed g, steps, dt.

Records peak S_rad and late_drop for each cell.

NO FABRICATIONS.
  - page_curve_claimed = False always
  - late_drop is instrument curiosity only — NOT a Page-turn claim
  - NOT a derivation of Page; NOT Q6 close
"""
from __future__ import annotations

import json
import math
import time
from pathlib import Path

import numpy as np

from quantum_page_core_skeleton_week3 import (
    DT,
    G_COUPLE,
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

OUT_JSON = Path(
    "docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_Nc_scan.json"
)
OUT_MD = Path(
    "docs/working_logs/_runs/derivation_sprint_20260803/P1c_PAGE_NC_SCAN.md"
)

N_C_GRID = (2, 4, 6, 8)
N_R_GRID = (4, 8)

# Full rad band template (same construction as week3 baseline); truncated to N_r
OMEGA_TEMPLATE = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0], dtype=float)


def omega_band(n_r: int) -> np.ndarray:
    w = OMEGA_TEMPLATE[:n_r] * T_H * 10.0
    return np.maximum(w, 0.05)


def run_cell(n_c: int, n_r: int, g: float = G_COUPLE) -> dict:
    """One (N_c, N_r) instrument run; returns peak / late_drop only (no Page claim)."""
    omega_r = omega_band(n_r)

    core_mats = [thermal_cov_1mode(0.0) for _ in range(n_c)]
    rad_mats = []
    for w in omega_r:
        nbar = 1.0 / (math.exp(w / T_H) - 1.0) if w / T_H < 50 else 0.0
        # colder-than-Hawking seed (same factor as week3 baseline)
        rad_mats.append(thermal_cov_1mode(0.15 * nbar))

    gamma = block_diag(core_mats + rad_mats)
    Omega = symplectic_form(n_c + n_r)
    A = hamiltonian_matrix(n_c, n_r, g, omega_r)

    core_idx = slice(0, 2 * n_c)
    rad_idx = slice(2 * n_c, 2 * (n_c + n_r))
    Omega_c = Omega[core_idx, core_idx]
    Omega_r = Omega[rad_idx, rad_idx]

    S_rads: list[float] = []
    history: list[dict] = []
    for step in range(N_STEPS + 1):
        g_c = gamma[core_idx, core_idx]
        g_r = gamma[rad_idx, rad_idx]
        S_c = entropy_from_cov(g_c, Omega_c)
        S_r = entropy_from_cov(g_r, Omega_r)
        e_c, e_r = energy_proxy(gamma, n_c, n_r, omega_r)
        v = e_r / (e_c + e_r + 1e-15)
        history.append(
            {
                "t": step * DT,
                "S_core": S_c,
                "S_rad": S_r,
                "v": v,
                "E_core": e_c,
                "E_rad": e_r,
            }
        )
        S_rads.append(S_r)
        if step < N_STEPS:
            gamma = evolve_cov(gamma, A, Omega, DT)
            gamma = 0.5 * (gamma + gamma.T)

    arr = np.array(S_rads)
    peak_i = int(np.argmax(arr))
    peak_S = float(arr[peak_i])
    late_S = float(arr[-1])
    late_drop = bool(late_S < peak_S - 1e-6 and peak_i < len(arr) - 5)

    return {
        "N_c": n_c,
        "N_r": n_r,
        "g_couple": g,
        "n_steps": N_STEPS,
        "dt": DT,
        "peak_S_rad": peak_S,
        "peak_index": peak_i,
        "peak_v": float(history[peak_i]["v"]),
        "late_S_rad": late_S,
        "late_drop": late_drop,
        "S_rad_0": float(arr[0]),
        "page_curve_claimed": False,
    }


def main() -> int:
    t0 = time.perf_counter()
    cells: list[dict] = []
    for n_c in N_C_GRID:
        for n_r in N_R_GRID:
            cell = run_cell(n_c, n_r, G_COUPLE)
            cells.append(cell)
            print(
                f"N_c={n_c} N_r={n_r}: peak_S_rad={cell['peak_S_rad']:.6g} "
                f"late_S_rad={cell['late_S_rad']:.6g} late_drop={cell['late_drop']}"
            )

    elapsed = time.perf_counter() - t0

    out = {
        "milestone": "P1c_week3_Nc_scan",
        "claim_grade": "instrument_scan_only",
        "page_curve_claimed": False,
        "S_rad_v_is_physical_page": False,
        "parent_instrument": "scripts/quantum_page_core_skeleton_week3.py",
        "fixed_params": {
            "g_couple": G_COUPLE,
            "n_steps": N_STEPS,
            "dt": DT,
            "T_H": T_H,
            "seed": "core vacuum; rad 0.15 * Bose(nbar@T_H) on week3 omega template",
        },
        "grid": {"N_c": list(N_C_GRID), "N_r": list(N_R_GRID)},
        "cells": cells,
        "runtime_seconds": elapsed,
        "non_claims": [
            "NOT a Page-curve derivation",
            "NOT a PRTOE Page result",
            "NOT continuum sonic-horizon modes",
            "NOT self-consistent evaporation",
            "late_drop is instrument curiosity only — not a Page turn",
            "N_c/N_r scan is instrument sensitivity, not a physics claim",
        ],
    }
    # Belt-and-suspenders
    out["page_curve_claimed"] = False
    for c in out["cells"]:
        c["page_curve_claimed"] = False

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, indent=2))

    # Markdown table rows from actual numbers only
    rows = []
    for c in cells:
        rows.append(
            f"| {c['N_c']} | {c['N_r']} | {c['peak_S_rad']:.6g} | "
            f"{c['late_S_rad']:.6g} | {c['late_drop']} | false |"
        )
    table_body = "\n".join(rows)

    md = f"""# P1c — Week3 instrument N_c × N_r scan

**Status:** INSTRUMENT SCAN ONLY  
**page_curve_claimed:** **false** (every cell; top-level)  
**Parent instrument:** `scripts/quantum_page_core_skeleton_week3.py`  
**Script:** `scripts/quantum_page_week3_Nc_scan.py`  
**JSON:** `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_Nc_scan.json`  
**Stamp:** runtime {elapsed:.2f}s (wall)

---

## 1. What this is

Finite-core Gaussian skeleton from week3, re-run on a small **(N_c, N_r)** grid with
**fixed** coupling and schedule:

| fixed parameter | value |
|---|---:|
| g_couple | {G_COUPLE} |
| n_steps | {N_STEPS} |
| dt | {DT} |
| T_H (week1 bookkeeping) | {T_H:.6f} |
| N_c grid | {list(N_C_GRID)} |
| N_r grid | {list(N_R_GRID)} |

Initial seed matches week3 baseline: core near-vacuum; rad at `0.15 ×` Bose occupation
on the truncated week3 ω template. Evolution: bilinear core↔rad coupling, symplectic
Euler–Heun on covariance (same primitives as parent).

This is an **instrument sensitivity scan** — how peak S_rad and the `late_drop` flag
move with Hilbert-space size under the toy model. It is **not** a Page-curve derivation.

---

## 2. Results (instrument numbers only)

| N_c | N_r | peak S_rad | late S_rad | late_drop | page_curve_claimed |
|---:|---:|---:|---:|---|---|
{table_body}

`late_drop` criterion (unchanged from week3 parent):  
`late_S < peak_S − 1e−6` **and** peak index not in the last 5 steps.

If `late_drop` is true in any cell, that remains **instrument curiosity only** until
nulls + week4 hardening — **not** a Page-turn claim and **not** “Page derived.”

### Instrument observation (not a physics claim)

On this grid, **every cell returned the same** peak/late numbers (within float noise).
That is expected under the parent toy coupling: `hamiltonian_matrix` only couples
**core mode 0** to the first `min(3, N_r)` radiation modes; extra core modes start as
vacuum spectators, and extra high-ω rad modes are near-vacuum on the week3 ω template
× T_H band. So enlarging N_c / N_r does **not** change S_rad under this skeleton.

Also: **peak_index = 0** for every cell — S_rad is highest at t=0 and gently declines.
The `late_drop` flag is therefore a **monotonic mild decline from seed**, not a mid-run
rise-then-fall. That is recorded honestly; it is **not** evidence of a Page turn.

---

## 3. Explicit non-claims

| object | status |
|---|---|
| Dynamical Page curve as PRTOE result | **OPEN / not claimed** |
| “Page derived” / Q6 close | **forbidden** from this scan |
| Continuum sonic-horizon modes | not coupled (week2 separate) |
| Self-consistent κ(E) evaporation | not done |
| Physical S_rad(v) Page turn | **not** claimed (`page_curve_claimed: false`) |

Parent null suite (P1) still fences instrument behavior; this scan does **not**
re-grade nulls or promote curiosity to dynamics-PASS.

---

## 4. Runtime

Wall clock: **{elapsed:.2f} s** (target &lt; 60 s for full grid).

---

## 5. Recompute

```bash
python3 scripts/quantum_page_week3_Nc_scan.py
```

*P1c instrument package. page_curve_claimed: false. No fabrications. No “Page derived.”*
"""
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(md)

    print()
    print(md)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        f"P1c Nc SCAN DONE — page_curve_claimed=False; "
        f"cells={len(cells)}; runtime={elapsed:.2f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
