# Page-curve Week 3 — finite-core skeleton (2026-08-03)

**Status:** WEEK3 SKELETON ONLY — first dynamics attempt after A4 parked.  
**Page curve:** **NOT claimed as PRTOE result.** (`page_curve_claimed: false`)  
**Script:** `scripts/quantum_page_core_skeleton_week3.py`  
**JSON:** `page_curve/week3_core_skeleton.json`  
**Null suite:** `scripts/quantum_page_week3_nulls.py` · `page_curve/week3_nulls.json` · P1 report  
**Plan:** `PAGE_CURVE_IMPLEMENTATION_PLAN.md` Milestone C start.

---

## 1. What was done

1. Finite core: **N_c=4** Gaussian oscillators (covariance state).  
2. Exterior: **N_r=8** modes with toy thermal seed from week1 **T_H=0.019894**.  
3. Bilinear core↔rad coupling (g=0.08); symplectic Euler–Heun evolution.  
4. Recorded **S_core(t), S_rad(t), v(t)** (energy fraction proxy).

## 2. Instrument numbers (not a booking)

| quantity | value |
|---|---:|
| peak S_rad | 0.008118 |
| v at peak | 1.000000 |
| late S_rad | 0.007933 |
| late drop after peak? | True |

If `late_drop` is true, it is an **instrument curiosity** until nulls + week4 hardening — **not** a Page-turn claim.

## 3. Explicit non-claims

| object | status |
|---|---|
| Dynamical Page curve as PRTOE result | **OPEN / not claimed** |
| Continuum sonic-horizon modes | not coupled (week2 separate) |
| Self-consistent κ(E) evaporation | not done |
| Q6 ledger close | **forbidden** without week4 hardening |

## 4. Next

- Larger N_c / better coupling to week2 greybody modes  
- Null suite: run `python3 scripts/quantum_page_week3_nulls.py` (P1) — instrument only  
- Only then consider grade DYNAMICS-PASS/FAIL/INCONCLUSIVE

---

**Recompute:**
```bash
python3 scripts/quantum_page_core_skeleton_week3.py
python3 scripts/quantum_page_week3_nulls.py
```

## 5. Null suite (P1 — instrument behavior)

**Script:** `scripts/quantum_page_week3_nulls.py`  
**JSON:** `page_curve/week3_nulls.json`  
**Detail report:** `docs/working_logs/_runs/derivation_sprint_20260803/P1_PAGE_NULLS.md`  
**Stamp:** 2026-08-03 23:13 UTC  
**page_curve_claimed:** **false**

| null | setup | instrument grade | key numbers |
|---|---|---|---|
| **A** | g=0 (no coupling) | **PASS** | max\|ΔS_rad\|=0.000e+00 |
| **B** | infinite-bath proxy (rad re-thermalized each step) | **PASS** | late_drop=False; S0=0.008118; late=0.041183 |
| **C** | pure vacuum everywhere | **PASS** | S0=2.863e-11; peak=2.863e-11 |

**Interpretation (instrument only):**
- Null A: instrument does not invent S_rad growth without coupling.
- Null B: infinite bath must **not** show purification-style late drop we would call Page.
- Null C: vacuum seed does not fabricate a thermal Page-scale S_rad curve.
- Baseline `late_drop` (if any) remains **curiosity** — **not** a Page-turn claim.

**Recompute nulls:**
```bash
python3 scripts/quantum_page_week3_nulls.py
```
