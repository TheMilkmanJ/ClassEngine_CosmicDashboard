# T14 four_branch — booking restated after RED R3 DENIED (2026-08-05)

**Artifact:** `four_branch/summary.json` (this run, elapsed ~4.24 h)  
**Red:** `RED VERDICT R3 T14 four_branch — DENIED`

## Binding restatement (quote this)

> **Antisymmetry in n confirmed at f = +1** (two branches, t = 1.00): n+1_f+1 → H≈+1.933, helA=−1, ampA≈1.70; n−1_f+1 → H≈−1.993, helA=+1, ampA≈1.42; genuine dial spreads. **The f = −1 branches did not form a ring** (ampA ≈ 0.0012 / 0.00087 ≪ instrument helA floor 0.15) and are **NOT_MEASURED**, not passing. **Overall four-branch sign is NOT BOOKABLE.**

## Grade

| claim | status |
|---|---|
| overall sign BOOKABLE (four-branch) | **DENIED / NOT BOOKABLE** |
| n-antisymmetry at f=+1, t=1.00 | **real** (two-branch candidate evidence) |
| f=−1 as measurements | **NOT_MEASURED** (noise floor) |

## Instrument cure (code)

`scripts/fill_t14_i6_tc_when_ready.py`: branches with ampA ≤ 0.15 are `verdict_null` / `not_measured`; excluded from margin aggregate; full four-branch eligible only if all four measured.

## Living stamp

Production overall sign remains **OPEN-MACHINE / NOT BOOKED** until four matched measured branches or red AGREE on a two-branch candidate-only restatement.

*NO FABRICATIONS. A noise-floor zero is not a measurement.*

## Artifact regeneration (R3 AGREE-IF 2026-08-05)

`four_branch/summary.json` re-written so machine-readable fields match booking:

| branch | ampA | margin_ok | not_measured |
|---|---:|---|---|
| n+1_f+1 | ~1.70 | True | false |
| n−1_f+1 | ~1.42 | True | false |
| n+1_f−1 | ~0.0012 | **False** | **true** |
| n−1_f−1 | ~0.00087 | **False** | **true** |

Booking line unchanged (NOT BOOKABLE). Source gates in fill + ring scripts already fixed for future runs.

## R3-b mirror gate (2026-08-05)

Red: margin gate already sound; **mirror gate** was the surviving fake pass (pairs mixed measured × unmeasured).

**Cure:** `fill_t14_i6_tc_when_ready.py` — `mirror_residual` / `mirror_ok` refuse when either branch is not_measured (ampA ≤ 0.15); scorecard prints `N/A — unmeasured branch in pair`, never PASS.

Re-emit: `TC_GATES_R3b.md` for this run.
