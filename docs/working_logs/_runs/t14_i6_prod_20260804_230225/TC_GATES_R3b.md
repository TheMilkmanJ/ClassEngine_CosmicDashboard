# R1-t14-i6 gates FROM DISK (auto)

**Source:** `docs/working_logs/_runs/t14_i6_prod_20260804_230225/four_branch/summary.json`
**elapsed_s:** 2e+04
**booking string (instrument):** antisymmetry in n CONFIRMED at f=+1 only (two branches, t=1.00); f=-1 branches NOT_MEASURED (ampA below instrument 0.15 helA floor); overall four-branch sign NOT BOOKABLE

**NO FABRICATIONS.** Production sign booking only if gates PASS + conditions 1–6 + red/ref.

## four-branch selected

| branch | t | H | Tw | Wr | ampA | n_cand | margin_ok |
|---|---:|---:|---:|---:|---:|---:|---|
| n+1_f+1 | 1 | 1.933 | 0 | -0.06686 | 1.696 | 5 | True |
| n+1_f-1 | 0.25 | 2 | 0 | 0 | 0.001224 | **2 censored** | False |
| n-1_f+1 | 1 | -1.993 | -4.441e-16 | 0.007137 | 1.418 | 5 | True |
| n-1_f-1 | 0.25 | -2 | 0 | 0 | 0.0008654 | **2 censored** | False |

## Mirror residuals

- (n+1_f+1) ↔ (n-1_f-1): N/A — unmeasured branch in pair
- (n+1_f-1) ↔ (n-1_f+1): N/A — unmeasured branch in pair
- **mirror_ok:** False (False: unmeasured branch in pair — red R3-b)

## Condition 3 — member t

- (1,1)↔(−1,−1): **mismatched-t** (1.0 vs 0.25)
- (1,−1)↔(−1,1): **mismatched-t** (0.25 vs 1.0)

## Condition 2 — candidate pools

- console n_cand: {'n+1_f+1': 5, 'n+1_f-1': 2, 'n-1_f+1': 5, 'n-1_f-1': 2}
- any instrument-censored (≤2): **True**

## Gate scorecard

| Gate | Target | Result |
|---|---|---|
| Calibrate planar+helix | PASS | PASS (prior) |
| nowinding | H≪0.2 + disclosure | PASS (prior) |
| nojet no false ring | no ring | PASS (prior; red M1) |
| True-mirror residual <5% | <5% | —% / —% → FAIL/TBD |
| Margins all four | margin_ok | False |
| No censored production rows | n_cand>2 | False |
| Blind selector | no Tw/Wr/H | held if instrument unchanged |

## Booking stance (auto)

- Smoke-grade H≈sign(n)·2 remains separate.
- Production sign(H vs n) **auto-eligible:** **False**
  (mirror_ok AND all verdicts AND all margin_ok AND no ≤2-cand rows).
- Even if eligible: **do not self-book** — tribunal + conditions 1–6 + red/ref required.
- Checklist: `docs/working_logs/_runs/t14_i6_CONDITIONS_1_6_CHECKLIST.md`
