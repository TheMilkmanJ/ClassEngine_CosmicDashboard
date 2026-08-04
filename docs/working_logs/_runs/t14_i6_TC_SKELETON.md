# TASK COMPLETE R1-t14-i6 — skeleton (live fill)

**Path:** `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/`  
**NO FABRICATIONS.** Fill four-branch only when `four_branch/summary.json` exists.

## Gates

| Gate | Target | Result |
|---|---|---|
| Calibrate planar+helix | PASS | **PASS** |
| nowinding \|H\| selected | ≪0.2 | **PASS** (H≈0; f−1 instrument-censored 2-cand) |
| nowinding mid-frame phase | clean | **OPEN** f−1 nphase&lt;12/16 mid-frames |
| nojet | no false ring | **PASS** both n=±1 no verdict (elapsed 5622s) |
| True-mirror residual | **&lt;5%** at 128³ | **PASS** 3.40% / 0.36% |
| Margins \|H\|&gt;3×spread | all four | **PASS** all margin_ok |
| f−1 arms n_cand | &gt;2 clean | **FAIL cond.2** both f−1 are 2-cand censored |
| Blind selector | no Tw/Wr/H | held |

## nowinding selected

| branch | t | H | drift_phys | ampA | margin_ok | n_cand (console) |
|---|---:|---:|---:|---:|---|---:|
| n+0_f+1 | 1.0 | 1.873e-15 | 0.03983 | 3.133e-17 | False | 5 |
| n+0_f-1 | 0.25 | 0.000e+00 | 0.07305 | 8.654e-04 | False | **2 (instrument-censored)** |

## nojet

Booking: `nothing graded (no ring / no verdict frame)` — no ring either branch.

## Pre-registered red conditions 1–6 (armed)

1. NaN gate = nphase &lt; 12/16  
2. Per-branch candidate-pool; ≤2 → **instrument-censored**  
3. Mirror rows state member t; flag mismatched-t  
4. ampA quoted; not helA as null evidence  
5. No "null clean" for f−1 nowinding without disclosure  
6. No production sign booking unless skeleton gates pass on four-branch  

## Booking

- Smoke-grade H≈sign(n)·2 (i5) separate.  
- Production sign(H vs n) **only if** four-branch gates pass.  
- ChatGPT REMAND until four-branch artifacts on disk.

## four-branch (fill when ready)

| branch | t | H | Tw | Wr | ampA | n_cand | margin_ok |
|---|---:|---:|---:|---:|---:|---:|---|
| n+1_f+1 | 1 | 1.933 | 0 | -0.06686 | 1.696 | 5 | True |
| n+1_f-1 | 0.25 | 2 | 0 | 0 | 0.001224 | **2 censored** | True |
| n-1_f+1 | 1 | -1.993 | -4.441e-16 | 0.007137 | 1.418 | 5 | True |
| n-1_f-1 | 0.25 | -2 | 0 | 0 | 0.0008654 | **2 censored** | True |

Mirror residual (1,1)↔(−1,−1): 3.4%
Mirror residual (1,−1)↔(−1,1): 0.3575%
mirror_ok: True
any_instrument_censored: True
production_auto_eligible: False

*Auto-filled from `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/four_branch/summary.json` + console n_cand. Verify before booking.*
