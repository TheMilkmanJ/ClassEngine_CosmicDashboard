# Claim-decoupling checklist (ACTIVE / BINDING)

**Status:** **ACTIVE / BINDING** (ChatGPT REFEREE batch9-T8-claim-decoupling)  
**Source:** PAGE_TURN_ACCEPTANCE_PROTOCOL.md §4.4  
**Companion tooling:** `scripts/page_protocol_scorecard.py` (arrays-only T1–T8)  
**Fence:** `page_curve_claimed` remains **false** until a separate claim step after red AGREE.

---

## Rule (binding)

A **CANDIDATE** claim packet may be filed **only after** the run artifact and scorecard
exist independently of the packet — never in the same write as the first production of
that run JSON.

---

## Checklist (in order)

| # | Gate | Done? | Notes |
|---|---|---|---|
| 1 | **Run complete** | ☐ | Producing script finished cleanly (OMP=1; no PolyChord; no MCMC touch) |
| 2 | **JSON on disk** | ☐ | Full histories written (`history_full` / n1·n2·n3 or coevolve equivalent) |
| 3 | **Scorecard from arrays** | ☐ | `python3 scripts/page_protocol_scorecard.py <run.json>` recomputes T1–T8 from arrays only; writes `*_scorecard_recompute.json` |
| 4 | **Script sha256** | ☐ | Scorecard (and producing script) content hash recorded |
| 5 | **Git commit when owner allows** | ☐ | Prefer committed scripts for T6; seats may accept content-hash as interim |
| 6 | **Only then file CANDIDATE packet** | ☐ | Packet references existing JSON + scorecard paths; does **not** re-mint the run |
| 7 | **T8_pass** | ☐ | Binding: single-valued \(S(u)\); entropy rise at frozen \(u\) earns no T3 credit |

---

## T8 (ACTIVE / BINDING)

| Item | State |
|---|---|
| T8 single-valued \(S(u)\) (§4.3) | **ACTIVE / BINDING** |
| Scorecard reports `T8_pass` / worst bin | Yes (`protocol_binding_T8`) |
| Gates `CANDIDATE_TURN_binding` | **Yes** — requires T1–T6 machine score **and** `T8_pass` |
| Auto-sets `page_curve_claimed` | **Never** |

---

## Explicit non-actions

- Do **not** set `page_curve_claimed: true` in scorecard tooling or run scripts by default  
- Do **not** file a CANDIDATE packet in the same step as the first write of the run JSON  
- Do **not** treat hand-transcribed numbers as scorecard evidence  
- Do **not** treat `CANDIDATE_TURN_binding: true` in a scorecard as a filed CANDIDATE — filing is a separate packet after this checklist  

---

## Recompute command (example)

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve.json
# writes: .../page_curve/coevolve_scorecard_recompute.json
```

---

*Ratified 2026-08-03 with T8 ACTIVE. NO FABRICATIONS.*
