# REPORT — T6 Page micro R1/R2/R5 + F1 S⋆ fence

**Package:** `docs/working_logs/_runs/theory_construction_20260804/desk_t6_page_micro_20260804/`  
**Date:** 2026-08-04  
**Mode:** REQUIRED_INPUTS for R1/R2/R5 · can-exist / should-not-exist (+ S⋆-only) · F1 protocol · arrays-only v13 reconfirm  
**Priors:** `page_d4_microphysics_20260804` · `page_t8_residual_demand` R1–R8 · `DEAD_DENIFY` F1 denominator-only · champion `coevolve_v13`  
**Fences held:** NO FABRICATIONS · `page_curve_claimed: false` · no densify thrash · no coevolve production campaign · leave MCMCs · exit0≠PASS · no CANDIDATE without T8≤0.10+red · no PolyChord · Strong CP abstention

---

## 0. Return stamp

| item | value |
|---|---|
| **T8 status** | **FAIL** range/\(S_\star\) = **0.113154…** (need ≤ **0.10**) on bin **[0.10, 0.11)** |
| **any land?** | **NO** |
| **grade** | **OPEN near-miss · D4 active · R1/R2/R5 MISSING_INPUT · F1 fence ON** |
| **path** | `docs/working_logs/_runs/theory_construction_20260804/desk_t6_page_micro_20260804/` |
| **claim** | **`page_curve_claimed: false`** |
| **CANDIDATE packet** | **none** |

---

## 1. Mission (what this desk did)

| # | Goal | Result |
|---|---|---|
| 1 | R1, R2, R5 only: REQUIRED_INPUTS + can-exist / should-not-exist; MISSING_INPUT unless stocked law found | **DONE** — no stocked law; all three **MISSING_INPUT** ([`R1_R2_R5.md`](R1_R2_R5.md)) |
| 2 | Encode F1 as protocol: any T8_pass reports early-bin range **and** \(S_\star\) vs v13; pure \(S_\star\) inflation DEAD | **DONE** — [`F1_PROTOCOL.md`](F1_PROTOCOL.md) |
| 3 | Arrays-only scorecard reconfirm v13 if cheap (sha256 match); no new dynamics inventing T8 pass | **DONE** — match `048de43e…`; T8 still **0.113 FAIL** ([`SCORECARD.md`](SCORECARD.md)) |
| 4 | Extend each R1/R2/R5 should-not-exist with **S⋆-only lever** | **DONE** — in R1_R2_R5 + F1 map |

**What this desk did *not* do:** invent dump/entangle/co-mod law; coevolve_v39+ production; densify; reopen D1–D3; file CANDIDATE; flip claim; MCMC; PolyChord; soft-pass 0.113.

---

## 2. Prior surfaces used (read-only)

| surface | use |
|---|---|
| `page_t8_residual_demand/CANDIDATE_LEVERS.md` | R1–R8 statements; R1/R2/R5 primary |
| `page_t8_residual_demand/WHAT_RESIDUAL_DEMANDS.md` | RD1–RD21; early dS/du demand |
| `page_t8_residual_demand/SURVIVORS.md` · `DEAD_LANES.md` | Schema grades; thrash death |
| `page_d4_microphysics_20260804/` | D4 map; DEAD_DENIFY + F1 denominator-only seed |
| `page_full_freeze_20260804/` | Outsider freeze; D4 active |
| Champion JSON | `.../page_curve/coevolve_v13.json` · sha256 `048de43e…` |

---

## 3. T8 reconfirm (arrays-only; no coevolve)

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

**Log:** [`logs/scorecard_v13_rerun_20260804_t6.log`](logs/scorecard_v13_rerun_20260804_t6.log)  
**Writeup:** [`SCORECARD.md`](SCORECARD.md)

| quantity | value |
|---|---|
| Artifact | `coevolve_v13.json` |
| **input_sha256** | **`048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8`** (**match**) |
| **tool_sha256** | `06bd9661be39d1ff…` |
| **T8_pass** | **False** |
| Worst / sole fail bin | **[0.10, 0.11)** |
| **range / \(S_\star\)** | **0.11315435176934464** |
| Need | ≤ **0.10** |
| Early-bin range (num) | 0.0018883423986319587 |
| \(S_\star\) (den) | 0.016688199517780646 |
| T1–T6 machine | **PASS** |
| T2 u_late | **0.9021 PASS** |
| DC3 | **PASS** |
| `CANDIDATE_TURN_binding` | **False** |
| `page_curve_claimed` | **false** |

**Explicit:** T8 **still fails**. exit 0 of scorecard ≠ physics PASS. No land from re-score alone.

---

## 4. Package contents

| file | role |
|---|---|
| [`REPORT.md`](REPORT.md) | this executive |
| [`R1_R2_R5.md`](R1_R2_R5.md) | REQUIRED_INPUTS + can/should-not (+ S⋆-only) for R1/R2/R5 |
| [`F1_PROTOCOL.md`](F1_PROTOCOL.md) | pure \(S_\star\) DEAD; mandatory num+den disclosure on T8_pass |
| [`SCORECARD.md`](SCORECARD.md) | arrays-only reconfirm writeup |
| [`SURVIVORS.md`](SURVIVORS.md) | schemas that survive; deeper-work queue |
| [`NON_CLAIMS.md`](NON_CLAIMS.md) | hard non-claims |
| [`MASTER.md`](MASTER.md) | one-page stamp / return |
| [`logs/scorecard_v13_rerun_20260804_t6.log`](logs/scorecard_v13_rerun_20260804_t6.log) | console re-score |

---

## 5. R1 / R2 / R5 (headline)

Full text: [`R1_R2_R5.md`](R1_R2_R5.md).

| ID | Name | REQUIRED_INPUTS | Stocked law? | S⋆-only should-not | Grade |
|---|---|---|---|---|---|
| **R1** | Dump / occupation-transfer (L1) | I1–I5 open (operator, schedule, channels, independence, write-once plan) | **MISSING_INPUT** | **Yes** | SURVIVOR-SCHEMA |
| **R2** | Entangling operator (L2) | I1–I5 open (generator, weights, N4, peak/T3, stickiness break) | **MISSING_INPUT** | **Yes** | SURVIVOR-SCHEMA |
| **R5** | TMS×BS co-modulation | I1–I5 open (single H, non-factorized, continuity, O(1) params, joint plan) | **MISSING_INPUT** | **Yes** | SURVIVOR-SCHEMA |

**Stocked law search:** residual + D4 schemas only; no independent licensed dump/entangle/co-mod law text in corpus → **MISSING_INPUT** for all three.  
**Primary schemas if content appears:** still **R1 / R2 / R5**.

---

## 6. F1 protocol (headline)

Full text: [`F1_PROTOCOL.md`](F1_PROTOCOL.md).

| rule | status |
|---|---|
| Any T8_pass must report early-bin **range** and **\(S_\star\)** vs v13 | **BINDING** |
| State which moved (num / den / both) | **BINDING** |
| Pure \(S_\star\) inflation (num fixed, den only) | **DEAD** |
| Class A (num-led) or B (joint disclosed) | allowed if joint gates hold |
| Class C (den-only) or D (undisclosed) | protocol fail |
| Arithmetic: +13.15% \(S_\star\) alone would fake ≤0.10 with range fixed | documented |

---

## 7. Stocked score decision

| Question | Answer |
|---|---|
| Stocked new micro law for R1/R2/R5 without densify? | **No** |
| Stocked history scorable arrays-only? | **Yes** — `coevolve_v13.json` |
| Action taken | Arrays-only scorecard **only** |
| Did T8 pass? | **No** (0.113) |
| Invent dynamics to fabricate ≤0.10? | **No** |

---

## 8. Survivors / next

| Item | Status |
|---|---|
| Deeper work if licensed content appears | R1 / R2 / R5 → write-once → full gate stack → **F1 table** |
| Default now | **D4 / R8** — accept near-miss; zero thrash |
| F1 | **ON** for all future T8_pass claims |
| Champion | **v13** locked; schedule `v23_champion_locked` |
| Q6 | **OPEN**; claimed **false** |

Details: [`SURVIVORS.md`](SURVIVORS.md).

---

## 9. Non-claims (hard)

1. Page curve **not** closed; Q6 **not** paid.  
2. **`page_curve_claimed`** remains **false**.  
3. **No** standing CANDIDATE packet.  
4. **0.113 is FAIL**, not soft pass.  
5. REQUIRED_INPUTS **not** filled laws.  
6. No invented microphysics.  
7. Scorecard re-run ≠ physics progress.  
8. F1 encoding ≠ land.  
9. exit 0 ≠ PASS.  
10. MCMCs / PolyChord / Strong CP / ownership: untouched / abstained.

Full list: [`NON_CLAIMS.md`](NON_CLAIMS.md).

---

## 10. Bottom line

| item | value |
|---|---|
| Champion | `coevolve_v13` · sha256 `048de43e…` (**match**) |
| T8 | **FAIL 0.113154…** (need ≤0.10) on **[0.10,0.11)** only |
| Joint other gates | **PASS** |
| Binding candidate | **False** |
| Page claimed | **false** |
| Lands | **0** |
| R1/R2/R5 stocked laws | **0** (all MISSING_INPUT) |
| F1 pure S⋆ | **DEAD**; protocol ON |
| Residual program | licensed micro only; densify/knob/D1–D3 **dead**; **D4 active** |

*NO FABRICATIONS. Zero densify. Zero coevolve production. Zero premature CANDIDATE. Desk complete.*
