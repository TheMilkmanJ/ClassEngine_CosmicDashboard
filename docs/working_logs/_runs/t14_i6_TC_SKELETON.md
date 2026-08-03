# TASK COMPLETE R1-t14-i6 — skeleton (fill when pipeline exits)

**Path:** `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/`  
**NO FABRICATIONS.** Partial fill from disk only. Full TC only after [3/4]+[4/4].

## Gates (Claude i6)

| Gate | Target | Result |
|---|---|---|
| Calibrate planar+helix | PASS | **PASS** (`calibrate.log`) |
| nowinding |H| at selected | ≪0.2 | **PASS** — f+1 H≈1.87e-15 @t=1.0; f-1 H=0 @t=0.25 |
| nowinding mid-frame phase | clean | **OPEN** — f-1 t=0.50–1.25 NaN/phase-blind (disclosed) |
| nojet | no false ring | **TBD** (IN FLIGHT) |
| True-mirror residual | **<5%** at 128³ | **TBD** (four-branch) |
| Margins |H|>3×spread | all four | **TBD** / nulls margin_ok=false expected |
| Blind selector | no Tw/Wr/H | held on SELECTED lines |

## nowinding selected (from summary.json)

| branch | t | H | drift_phys | ampA | margin_ok |
|---|---:|---:|---:|---:|---|
| n+0_f+1 | 1.0 | 1.873e-15 | 0.03983 | 3.133e-17 | False |
| n+0_f-1 | 0.25 | 0.000e+00 | 0.07305 | 8.654e-04 | False |

elapsed_s nowinding = 5684.48

## Booking

- Smoke-grade H≈sign(n)·2 already booked (i5).
- Production books overall sign of H_kin vs n **only if** gates pass.
- Thread-closure per hard-win ranking — not top external cosmology win.
- **ChatGPT REMAND:** no full production booking before nojet+four-branch artifacts on disk.


## Pre-registered red conditions (Claude NEXT ISSUE R1-t14-i6-fullTC-conditions)

1. NaN wording: gate is nphase < 12/16 (`ring_toroidal_hkin.py:298`), not only nphase=0.
2. Per-branch candidate-pool size + per-frame nphase table; ≤2 candidates → label **instrument-censored**.
3. Mirror <5% rows state t of each member; mismatched-t pairs flagged.
4. Per-branch ampA quoted; helA never as null evidence (forced 0 below amp 0.15).
5. No "null clean" for f−1 nowinding — endpoints-only; "instrument to the bench" until true-mirror measured.
6. No production sign(H vs n) booking unless all skeleton gates pass on [4/4] artifacts.
