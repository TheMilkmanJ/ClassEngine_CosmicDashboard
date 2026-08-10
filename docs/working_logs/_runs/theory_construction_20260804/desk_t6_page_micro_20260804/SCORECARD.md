# SCORECARD — champion `coevolve_v13` (T6 desk arrays-only reconfirm)

**Package:** `desk_t6_page_micro_20260804`  
**Date:** 2026-08-04  
**NO FABRICATIONS.** Arrays-only recompute. **Not** a CANDIDATE filing.  
**`page_curve_claimed`:** **false**  
**Purpose:** reconfirm v13 if cheap (sha256 match); **no** new dynamics inventing T8 pass.

## Command

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

**Log:** [`logs/scorecard_v13_rerun_20260804_t6.log`](logs/scorecard_v13_rerun_20260804_t6.log)

## Provenance

| item | value |
|---|---|
| Artifact | `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| **input_sha256** | **`048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8`** |
| sha256 match prior freeze / residual / D4 | **YES** (identical full hash) |
| Tool | `scripts/page_protocol_scorecard.py` |
| **tool_sha256** | **`06bd9661be39d1ffb0479898a2c0d6e444c45d7b0d127fcfc2abd903c460a390`** |
| Scorecard write | `.../page_curve/coevolve_v13_scorecard_recompute.json` (tool rewrite; numbers match freeze) |
| Resource | OMP=1; no PolyChord; no MCMC; **no densify; no coevolve production** |

## Binding gates

| gate | result | detail |
|---|---|---|
| T1 interior max | **PASS** | u* ≈ 0.2670 |
| T2 reach u≥0.9 | **PASS** | u_late = 0.9021 |
| T2 frac/noise | **PASS** | T2_all True |
| T3 early rise | **PASS** | True |
| T4 nulls N1–N4 | **PASS** | all True |
| T5 continuum | **PASS** | structural inherit |
| T6 artifacts | **PASS** | True |
| T1–T6 machine | **PASS** | True |
| T7 claim flag | **False** | correct — tool never claim-flips |
| stall / coevo co_frac / swap / peak | **PASS** | binding stack intact (champion) |
| **DC3** weight-invariant reach | **PASS** | v_frozen env = 0.9021; method `e_c_raw_stored` |
| **T8** single-valued S(u) | **FAIL** | sole fail |
| T8 worst bin | **[0.10, 0.11)** | n=12 |
| **range / \(S_\star\)** | **0.11315435176934464** | need ≤ **0.10** |
| S range in bin (num) | **0.0018883423986319587** | |
| \(S_\star\) (den) | **0.016688199517780646** | |
| threshold \(0.1\cdot S_\star\) | 0.0016688199517780646 | |
| occupied bins | 83 | failing bins = **1** |
| **`CANDIDATE_TURN_binding`** | **False** | requires T8_pass |
| **`page_curve_claimed`** | **false** | |

## F1 disclosure baseline (v13 — for future compare)

| field | v13 |
|---|---|
| early-bin range | 0.0018883423986319587 |
| \(S_\star\) | 0.016688199517780646 |
| range/\(S_\star\) | 0.11315435176934464 |
| class | **FAIL** (not A/B/C — no T8_pass) |

Any future T8_pass must fill the F1 table in [`F1_PROTOCOL.md`](F1_PROTOCOL.md) against **this** baseline.

## Explicit: T8 still fails

**0.113 is FAIL**, not soft pass. Residual ≈ 0.01315 in ratio units over the 0.10 bar.  
No new dynamics invented. No densify. No coevolve re-run.  
**exit 0 of scorecard tool ≠ physics PASS.**  
**Q6 remains OPEN.** No land.

## Curve numbers (reference only)

| quantity | value |
|---:|
| S_peak (S*) | 0.016688199517780646 |
| drop | 0.010546 |
| u* | ≈ 0.2670 |
| u_late | 0.9021 |

*NO FABRICATIONS. sha256 match. T8=0.113 FAIL.*
