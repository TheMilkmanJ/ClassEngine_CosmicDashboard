# Claude open-board-split cures applied (Grok blue)

**Date:** 2026-08-03 night  
**Source:** RED VERDICT open-board-split + RED NOTE reconcile + RED CONCUR  
**Owner path:** improve model, every step **except PolyChord**

---

## Applied

| ID | Cure | Status |
|---|---|---|
| R-A | T3 only credits rise with du&gt;0; scorecard coevolution_gates | **DONE** `page_protocol_scorecard.py` |
| R-C.6 | Write-once `coevolve_v{N}.json` | **DONE** `quantum_page_coevolve.py` |
| R-D | Booking: R−1&lt;0.05 **and** self-stop; no moving-file hatch | **DONE** checklist + preflight + finalize_h0 |
| R-F | Rename legacy null test | **DONE** `test_legacy_st_null_limit.py` + shim |
| Stale T8 | PAGE_CANDIDATE_REBUILD SUPERSEDED note | **DONE** |
| B-B | LEGACY_ST vs CURRENT_CORE labels | **DONE** (subagent) |
| B-C | MCMC watch | **DONE** NOT bookable |

---

## coevolve_v1 (write-once) scorecard

| gate | result |
|---|---|
| T8_pass | **True** (first binding T8 pass on versioned artifact) |
| T1–T4 individual | T1/T2/T3/T4 True |
| coevolution_gates | see scorecard JSON (may still fail stall/swap/co_frac composite) |
| CANDIDATE_TURN_binding | **False** (no filing; gates incomplete and claim-decoupling) |
| page_curve_claimed | **false** |

Artifact: `page_curve/coevolve_v1.json`  
Scorecard: `page_curve/coevolve_v1_scorecard_recompute.json` (separate write)

---

## Still open (improve path, no PolyChord)

1. MCMC → both R−1&lt;0.05 + self-stop → book GetDist  
2. Page: tighten coevolution_gates if any fail; red before any CANDIDATE  
3. arXiv — owner Fairbank HOLD  
4. Theory walls — no invent  

*NO FABRICATIONS.*
