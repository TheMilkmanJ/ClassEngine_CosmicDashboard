#!/usr/bin/env python3
"""Week-3 Page-curve *null suite* (P1) — instrument behavior only.

Plan: PAGE_CURVE_IMPLEMENTATION_PLAN.md Week 3–4 nulls (Milestone C / early D).
Parent instrument: scripts/quantum_page_core_skeleton_week3.py

Nulls (pre-registered instrument checks — NOT Page physics claims):
  Null A: g=0 (no coupling) → S_rad must not grow from coupling
  Null B: infinite-bath proxy — re-thermalize radiation each step
          → must NOT show purification-style late drop we would call Page
  Null C: pure vacuum everywhere → no thermal Page fabrication from vacuum

What this does NOT do:
  - Claim a dynamical Page curve as a PRTOE result
  - Close Q6 / information paradox
  - Promote baseline late_drop to a Page turn

NO FABRICATIONS. page_curve_claimed stays False.
Exit 0 if instrument null suite runs; PASS/FAIL is per-null instrument grade.
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

# Reuse week3 Gaussian instrument primitives (script may be run from repo root)
import sys
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))
from quantum_page_core_skeleton_week3 import (  # type: ignore
    DT,
    G_COUPLE,
    KAPPA,
    N_C,
    N_R,
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

OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
OUT_JSON = OUT_DIR / "page_curve" / "week3_nulls.json"
OUT_WEEK3_MD = OUT_DIR / "PAGE_CURVE_WEEK3.md"
OUT_P1 = Path("docs/working_logs/_runs/derivation_sprint_20260803/P1_PAGE_NULLS.md")
BASELINE_JSON = OUT_DIR / "page_curve" / "week3_core_skeleton.json"

# Instrument thresholds (pre-registered; not physics Page criteria)
NULL_A_MAX_DELTA = 1e-10
NULL_B_DROP_TOL = 1e-6  # same peak/late scale as week3 late_drop flag
NULL_C_S_FLOOR = 1e-8  # near-vacuum initial S_rad


def omega_r_default() -> np.ndarray:
    omega_r = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0])[:N_R] * T_H * 10.0
    return np.maximum(omega_r, 0.05)


def nbar_hawking(w: float) -> float:
    x = w / T_H
    if x >= 50:
        return 0.0
    return 1.0 / (math.exp(x) - 1.0)


def initial_gamma(
    *,
    vacuum: bool = False,
    rad_thermal_frac: float = 0.15,
) -> tuple[np.ndarray, np.ndarray]:
    """Build initial covariance. vacuum=True → pure vacuum everywhere."""
    omega_r = omega_r_default()
    core_mats = [thermal_cov_1mode(0.0) for _ in range(N_C)]
    rad_mats = []
    for w in omega_r:
        if vacuum:
            rad_mats.append(thermal_cov_1mode(0.0))
        else:
            rad_mats.append(thermal_cov_1mode(rad_thermal_frac * nbar_hawking(float(w))))
    gamma = block_diag(core_mats + rad_mats)
    return gamma, omega_r


def rethermalize_rad(gamma: np.ndarray, omega_r: np.ndarray, n_c: int) -> np.ndarray:
    """Hold radiation modes at fixed thermal (T_H) — infinite-bath proxy.
    Core block and core–rad correlations left as evolved (then rad diagonal reset
    kills purification partner structure on the rad reduced state).
    """
    g = gamma.copy()
    for j, w in enumerate(omega_r):
        nbar = nbar_hawking(float(w))
        block = thermal_cov_1mode(nbar)
        iq = 2 * (n_c + j)
        # zero cross-correlations involving this rad mode (bath re-equilibrates)
        g[iq : iq + 2, :] = 0.0
        g[:, iq : iq + 2] = 0.0
        g[iq : iq + 2, iq : iq + 2] = block
    return 0.5 * (g + g.T)


def run_trajectory(
    *,
    g_couple: float,
    vacuum: bool = False,
    rethermalize: bool = False,
    rad_thermal_frac: float = 0.15,
    n_steps: int = N_STEPS,
    dt: float = DT,
) -> dict[str, Any]:
    gamma, omega_r = initial_gamma(vacuum=vacuum, rad_thermal_frac=rad_thermal_frac)
    n_c, n_r = N_C, N_R
    Omega = symplectic_form(n_c + n_r)
    A = hamiltonian_matrix(n_c, n_r, g_couple, omega_r)
    core_idx = slice(0, 2 * n_c)
    rad_idx = slice(2 * n_c, 2 * (n_c + n_r))
    Omega_c = Omega[core_idx, core_idx]
    Omega_r = Omega[rad_idx, rad_idx]

    history: list[dict[str, float]] = []
    S_rad_vals: list[float] = []
    for step in range(n_steps + 1):
        t = step * dt
        S_c = entropy_from_cov(gamma[core_idx, core_idx], Omega_c)
        S_r = entropy_from_cov(gamma[rad_idx, rad_idx], Omega_r)
        e_c, e_r = energy_proxy(gamma, n_c, n_r, omega_r)
        v = e_r / (e_c + e_r + 1e-15)
        history.append(
            {
                "t": float(t),
                "S_core": float(S_c),
                "S_rad": float(S_r),
                "S_sum": float(S_c + S_r),
                "E_core": float(e_c),
                "E_rad": float(e_r),
                "v": float(v),
            }
        )
        S_rad_vals.append(float(S_r))
        if step < n_steps:
            gamma = evolve_cov(gamma, A, Omega, dt)
            gamma = 0.5 * (gamma + gamma.T)
            if rethermalize:
                gamma = rethermalize_rad(gamma, omega_r, n_c)

    S_arr = np.array(S_rad_vals)
    peak_i = int(np.argmax(S_arr))
    peak_S = float(S_arr[peak_i])
    late_S = float(S_arr[-1])
    S0 = float(S_arr[0])
    max_abs_delta = float(np.max(np.abs(S_arr - S0)))
    has_late_drop = bool(late_S < peak_S - NULL_B_DROP_TOL and peak_i < len(S_arr) - 5)
    return {
        "g_couple": g_couple,
        "vacuum": vacuum,
        "rethermalize_rad": rethermalize,
        "n_steps": n_steps,
        "dt": dt,
        "S_rad_0": S0,
        "S_rad_peak": peak_S,
        "S_rad_late": late_S,
        "peak_index": peak_i,
        "max_abs_delta_S_rad": max_abs_delta,
        "late_drop_after_peak": has_late_drop,
        "history_len": len(history),
        # keep only compact history endpoints for JSON size
        "history_endpoints": {
            "first": history[0],
            "mid": history[len(history) // 2],
            "last": history[-1],
        },
    }


def grade_nulls(results: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Instrument PASS/FAIL only — not physics Page grades."""
    a = results["null_A_g0"]
    b = results["null_B_infinite_bath"]
    c = results["null_C_vacuum"]

    a_pass = a["max_abs_delta_S_rad"] <= NULL_A_MAX_DELTA
    # Infinite bath must not produce purification-style late drop
    b_pass = not b["late_drop_after_peak"]
    # Vacuum: start near zero; do not fabricate a large thermal Page from vacuum alone
    c_pass = c["S_rad_0"] <= NULL_C_S_FLOOR and c["S_rad_peak"] < 0.5 * max(
        results.get("baseline_ref", {}).get("S_rad_peak", 0.01), 1e-6
    )

    return {
        "null_A_g0": {
            "pass": bool(a_pass),
            "criterion": (
                f"max|S_rad(t)-S_rad(0)| <= {NULL_A_MAX_DELTA:g} "
                "(no entropy growth from coupling when g=0)"
            ),
            "observed_max_abs_delta_S_rad": a["max_abs_delta_S_rad"],
            "late_drop_after_peak": a["late_drop_after_peak"],
        },
        "null_B_infinite_bath": {
            "pass": bool(b_pass),
            "criterion": (
                "no purification-style late_drop_after_peak when rad is "
                "re-thermalized each step (infinite-bath proxy)"
            ),
            "observed_late_drop_after_peak": b["late_drop_after_peak"],
            "S_rad_0": b["S_rad_0"],
            "S_rad_peak": b["S_rad_peak"],
            "S_rad_late": b["S_rad_late"],
        },
        "null_C_vacuum": {
            "pass": bool(c_pass),
            "criterion": (
                f"S_rad(0) <= {NULL_C_S_FLOOR:g} and peak S_rad not a "
                "fabricated thermal Page-scale rise from vacuum alone"
            ),
            "observed_S_rad_0": c["S_rad_0"],
            "observed_S_rad_peak": c["S_rad_peak"],
            "late_drop_after_peak": c["late_drop_after_peak"],
        },
    }


def load_baseline_ref() -> dict[str, Any]:
    if not BASELINE_JSON.is_file():
        return {"available": False}
    data = json.loads(BASELINE_JSON.read_text())
    peak = data.get("peak", {})
    return {
        "available": True,
        "page_curve_claimed": data.get("page_curve_claimed", None),
        "S_rad_peak": peak.get("S_rad"),
        "S_rad_late": peak.get("late_S_rad"),
        "late_drop_after_peak": peak.get("late_drop_after_peak"),
        "v_at_peak": peak.get("v"),
        "claim_grade": data.get("claim_grade"),
    }


def write_p1_md(
    grades: dict[str, dict[str, Any]],
    results: dict[str, dict[str, Any]],
    baseline_ref: dict[str, Any],
    stamp: str,
) -> str:
    ga, gb, gc = (
        grades["null_A_g0"],
        grades["null_B_infinite_bath"],
        grades["null_C_vacuum"],
    )
    a, b, c = (
        results["null_A_g0"],
        results["null_B_infinite_bath"],
        results["null_C_vacuum"],
    )
    all_pass = ga["pass"] and gb["pass"] and gc["pass"]

    def pf(x: bool) -> str:
        return "PASS" if x else "FAIL"

    md = f"""# P1 — Page week3 null suite (instrument only)

**Stamp:** {stamp}  
**Status:** INSTRUMENT nulls on week3 finite-core skeleton.  
**Page curve claimed:** **false** (hard lock).  
**Sprint:** derivation_sprint_20260803 · track **P1**  
**Script:** `scripts/quantum_page_week3_nulls.py`  
**JSON:** `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_nulls.json`  
**Parent instrument:** `scripts/quantum_page_core_skeleton_week3.py` · `PAGE_CURVE_WEEK3.md`

---

## 0. Standing locks

| lock | value |
|---|---|
| `page_curve_claimed` | **false** |
| Dynamical Page as PRTOE result | **OPEN / not claimed** |
| Baseline `late_drop` (if true) | **instrument curiosity only** until nulls + hardening |
| Q6 / information paradox close | **forbidden** from this package |

---

## 1. What was run

Same Gaussian covariance instrument as week3 (N_c={N_C}, N_r={N_R}, dt={DT}, n_steps={N_STEPS}, week1 T_H={T_H:.6f}).

| null | setup | expected instrument behavior |
|---|---|---|
| **A** | g=0, same initial seed as baseline | S_rad does **not** grow from coupling |
| **B** | g={G_COUPLE}, rad modes **re-thermalized** each step (infinite-bath proxy) | **no** purification-style late drop callable as Page |
| **C** | pure vacuum core+rad, g={G_COUPLE} | near-zero initial S_rad; no fabricated thermal Page-scale curve from vacuum alone |

---

## 2. Null table (instrument PASS/FAIL)

| null | grade | key numbers | criterion |
|---|---|---|---|
| **A g=0** | **{pf(ga["pass"])}** | max\\|ΔS_rad\\|={a["max_abs_delta_S_rad"]:.3e}; S0={a["S_rad_0"]:.6e}; late_drop={a["late_drop_after_peak"]} | {ga["criterion"]} |
| **B infinite bath** | **{pf(gb["pass"])}** | S0={b["S_rad_0"]:.6f}; peak={b["S_rad_peak"]:.6f}; late={b["S_rad_late"]:.6f}; late_drop={b["late_drop_after_peak"]} | {gb["criterion"]} |
| **C vacuum** | **{pf(gc["pass"])}** | S0={c["S_rad_0"]:.6e}; peak={c["S_rad_peak"]:.6e}; late_drop={c["late_drop_after_peak"]} | {gc["criterion"]} |
| **suite** | **{pf(all_pass)}** | — | all three instrument nulls |

---

## 3. Baseline reference (not a Page claim)

Loaded from `week3_core_skeleton.json` if present:

| quantity | value |
|---|---|
| available | {baseline_ref.get("available")} |
| page_curve_claimed | {baseline_ref.get("page_curve_claimed")} |
| peak S_rad | {baseline_ref.get("S_rad_peak")} |
| late S_rad | {baseline_ref.get("S_rad_late")} |
| late_drop_after_peak | {baseline_ref.get("late_drop_after_peak")} |
| claim_grade | {baseline_ref.get("claim_grade")} |

If baseline `late_drop_after_peak` is true, that remains an **instrument curiosity**. Null B is the control that would have to fail (show the same purification-style drop under infinite bath) to *discredit* reading baseline late drop as finite-core purification — and Null B must **not** show that drop for the control to behave. **None of this books a Page turn.**

---

## 4. Explicit non-claims

1. **Not** a derived Page curve.  
2. **Not** continuum sonic-horizon modes (week2 separate).  
3. **Not** self-consistent κ(E) evaporation.  
4. **Not** DYNAMICS-PASS grade (week4 full hardening still open).  
5. Toy bilinear coupling + Gaussian covariance only.

---

## 5. Recompute

```bash
python3 scripts/quantum_page_core_skeleton_week3.py
python3 scripts/quantum_page_week3_nulls.py
python3 scripts/quantum_page_sonic_horizon_week1.py
python3 scripts/quantum_page_bogoliubov_week2.py
```

---

*P1 instrument package. page_curve_claimed: false. No fabrications.*
"""
    return md


def append_null_section_to_week3_md(grades: dict[str, dict[str, Any]], results: dict[str, Any], stamp: str) -> None:
    """Update PAGE_CURVE_WEEK3.md with a null table; preserve non-claims."""
    ga, gb, gc = (
        grades["null_A_g0"],
        grades["null_B_infinite_bath"],
        grades["null_C_vacuum"],
    )
    a, b, c = (
        results["null_A_g0"],
        results["null_B_infinite_bath"],
        results["null_C_vacuum"],
    )

    def pf(x: bool) -> str:
        return "PASS" if x else "FAIL"

    # Prefer regenerating a complete week3 MD that includes nulls so re-running
    # week3 alone does not silently erase them — but week3 script may overwrite.
    # We patch/append a durable section and also write a null block the week3
    # skeleton can leave alone if we rewrite week3 to stop clobbering §5+.
    null_block = f"""
## 5. Null suite (P1 — instrument behavior)

**Script:** `scripts/quantum_page_week3_nulls.py`  
**JSON:** `page_curve/week3_nulls.json`  
**Detail report:** `docs/working_logs/_runs/derivation_sprint_20260803/P1_PAGE_NULLS.md`  
**Stamp:** {stamp}  
**page_curve_claimed:** **false**

| null | setup | instrument grade | key numbers |
|---|---|---|---|
| **A** | g=0 (no coupling) | **{pf(ga["pass"])}** | max\\|ΔS_rad\\|={a["max_abs_delta_S_rad"]:.3e} |
| **B** | infinite-bath proxy (rad re-thermalized each step) | **{pf(gb["pass"])}** | late_drop={b["late_drop_after_peak"]}; S0={b["S_rad_0"]:.6f}; late={b["S_rad_late"]:.6f} |
| **C** | pure vacuum everywhere | **{pf(gc["pass"])}** | S0={c["S_rad_0"]:.3e}; peak={c["S_rad_peak"]:.3e} |

**Interpretation (instrument only):**
- Null A: instrument does not invent S_rad growth without coupling.
- Null B: infinite bath must **not** show purification-style late drop we would call Page.
- Null C: vacuum seed does not fabricate a thermal Page-scale S_rad curve.
- Baseline `late_drop` (if any) remains **curiosity** — **not** a Page-turn claim.

**Recompute nulls:**
```bash
python3 scripts/quantum_page_week3_nulls.py
```
"""

    if OUT_WEEK3_MD.is_file():
        text = OUT_WEEK3_MD.read_text()
        # Strip previous null suite sections if re-running
        markers = [
            "\n## 5. Null suite (P1",
            "\n## 5. Null control",
            "\n## 5. Null",
        ]
        cut = len(text)
        for m in markers:
            i = text.find(m)
            if i != -1:
                cut = min(cut, i)
        # Also strip old trailing "Stamped" one-liners after null control
        base = text[:cut].rstrip() + "\n"
        # Ensure §4 Next does not claim nulls are still future-only
        base = base.replace(
            "- Null suite (infinite bath should not turn; pure thermal control)  \n",
            "- Null suite: **landed** (P1) — see §5; still not a Page claim  \n",
        )
        OUT_WEEK3_MD.write_text(base + null_block)
    else:
        OUT_WEEK3_MD.write_text(
            "# Page-curve Week 3 — finite-core skeleton\n\n"
            "**page_curve_claimed:** false\n"
            + null_block
        )


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)
    OUT_P1.parent.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    baseline_ref = load_baseline_ref()

    # Null A: no coupling
    null_A = run_trajectory(g_couple=0.0, vacuum=False, rethermalize=False)
    # Null B: infinite bath proxy
    null_B = run_trajectory(g_couple=G_COUPLE, vacuum=False, rethermalize=True)
    # Null C: pure vacuum
    null_C = run_trajectory(g_couple=G_COUPLE, vacuum=True, rethermalize=False)

    results = {
        "null_A_g0": null_A,
        "null_B_infinite_bath": null_B,
        "null_C_vacuum": null_C,
        "baseline_ref": {
            "S_rad_peak": baseline_ref.get("S_rad_peak") or 0.01,
        },
    }
    grades = grade_nulls(results)
    # drop internal baseline_ref helper from results before dump
    results_out = {
        "null_A_g0": null_A,
        "null_B_infinite_bath": null_B,
        "null_C_vacuum": null_C,
    }

    all_pass = all(grades[k]["pass"] for k in ("null_A_g0", "null_B_infinite_bath", "null_C_vacuum"))

    payload = {
        "milestone": "C_week3_null_suite_P1",
        "claim_grade": "instrument_nulls_only",
        "page_curve_claimed": False,
        "S_rad_v_is_physical_page": False,
        "stamp_utc": stamp,
        "parent_instrument": "scripts/quantum_page_core_skeleton_week3.py",
        "week1_T_H_used": T_H,
        "week1_kappa_used": KAPPA,
        "N_c": N_C,
        "N_r": N_R,
        "g_couple_baseline": G_COUPLE,
        "thresholds": {
            "null_A_max_delta_S_rad": NULL_A_MAX_DELTA,
            "null_B_drop_tol": NULL_B_DROP_TOL,
            "null_C_S_floor": NULL_C_S_FLOOR,
        },
        "baseline_ref": baseline_ref,
        "nulls": results_out,
        "grades": grades,
        "suite_pass": bool(all_pass),
        "non_claims": [
            "NOT a PRTOE Page-curve result",
            "NOT DYNAMICS-PASS / week4 full hardening",
            "Baseline late_drop is curiosity until nulls+hardening — still not a Page claim",
            "Null PASS/FAIL is instrument behavior only",
        ],
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))

    p1_md = write_p1_md(grades, results_out, baseline_ref, stamp)
    OUT_P1.write_text(p1_md)
    append_null_section_to_week3_md(grades, results_out, stamp)

    print(p1_md)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_P1}")
    print(f"updated {OUT_WEEK3_MD}")
    print(
        "P1 NULL SUITE DONE — page_curve_claimed=False; "
        f"A={grades['null_A_g0']['pass']} "
        f"B={grades['null_B_infinite_bath']['pass']} "
        f"C={grades['null_C_vacuum']['pass']} "
        f"suite={all_pass}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
