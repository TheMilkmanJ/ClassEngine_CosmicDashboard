# P1c — Week3 instrument N_c × N_r scan

**Status:** INSTRUMENT SCAN ONLY  
**page_curve_claimed:** **false** (every cell; top-level)  
**Parent instrument:** `scripts/quantum_page_core_skeleton_week3.py`  
**Script:** `scripts/quantum_page_week3_Nc_scan.py`  
**JSON:** `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_Nc_scan.json`  
**Stamp:** runtime 0.74s (wall)

---

## 1. What this is

Finite-core Gaussian skeleton from week3, re-run on a small **(N_c, N_r)** grid with
**fixed** coupling and schedule:

| fixed parameter | value |
|---|---:|
| g_couple | 0.08 |
| n_steps | 80 |
| dt | 0.05 |
| T_H (week1 bookkeeping) | 0.019894 |
| N_c grid | [2, 4, 6, 8] |
| N_r grid | [4, 8] |

Initial seed matches week3 baseline: core near-vacuum; rad at `0.15 ×` Bose occupation
on the truncated week3 ω template. Evolution: bilinear core↔rad coupling, symplectic
Euler–Heun on covariance (same primitives as parent).

This is an **instrument sensitivity scan** — how peak S_rad and the `late_drop` flag
move with Hilbert-space size under the toy model. It is **not** a Page-curve derivation.

---

## 2. Results (instrument numbers only)

| N_c | N_r | peak S_rad | late S_rad | late_drop | page_curve_claimed |
|---:|---:|---:|---:|---|---|
| 2 | 4 | 0.00811799 | 0.00793251 | True | false |
| 2 | 8 | 0.00811799 | 0.00793251 | True | false |
| 4 | 4 | 0.00811799 | 0.00793251 | True | false |
| 4 | 8 | 0.00811799 | 0.00793251 | True | false |
| 6 | 4 | 0.00811799 | 0.00793251 | True | false |
| 6 | 8 | 0.00811799 | 0.00793251 | True | false |
| 8 | 4 | 0.00811799 | 0.00793251 | True | false |
| 8 | 8 | 0.00811799 | 0.00793251 | True | false |

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

Wall clock: **0.74 s** (target &lt; 60 s for full grid).

---

## 5. Recompute

```bash
python3 scripts/quantum_page_week3_Nc_scan.py
```

*P1c instrument package. page_curve_claimed: false. No fabrications. No “Page derived.”*
