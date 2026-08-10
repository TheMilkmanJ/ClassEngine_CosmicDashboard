# F1_PROTOCOL — S⋆ fence for any future T8_pass

**Package:** `docs/working_logs/_runs/theory_construction_20260804/desk_t6_page_micro_20260804/`  
**Date:** 2026-08-04  
**Name:** **F1** = denominator-only / pure-\(S_\star\) inflation kill (from `page_d4_microphysics/DEAD_DENIFY.md` red cure)  
**Role:** bind reporting and kill rules so a T8 “pass” cannot be laundered by raising Page peak alone  
**Authority parents:** `DEAD_DENIFY.md` § denominator-only · `page_t8` T8 pin · `page_t8_residual_demand` RD3 (not pure \(G_{\mathrm{TMS}}\))  
**`page_curve_claimed`:** **false** (this protocol does not flip claim)

---

## 0. One-line rule

**Any future `T8_pass` claim must report early-bin absolute range AND \(S_\star\) vs champion v13, and state which moved. Pure \(S_\star\) inflation with fixed early range is DEAD as a T8 pass path.**

---

## 1. T8 definition (binding; not renegotiated)

For every occupied bin of \(u=\max_{s\le t}v(s)\) with \(\Delta u=0.01\):

\[
\frac{\max S - \min S}{S_\star} \le 0.10
\]

where \(S_\star = \max_t S\) over the scored history (Page peak).

| piece | role |
|---|---|
| **Numerator** | early-bin (or any bin) absolute range \(\max S-\min S\) |
| **Denominator** | global \(S_\star\) |
| **Bar** | **0.10** (binding; 0.113 is **FAIL**) |

Champion v13 sole fail:

| field | value |
|---|---|
| Bin | **[0.10, 0.11)** |
| range (num) | **0.0018883423986319587** |
| \(S_\star\) (den) | **0.016688199517780646** |
| range/\(S_\star\) | **0.11315435176934464** |
| threshold \(0.1\cdot S_\star\) | **0.0016688199517780646** |
| Relative gap | need ~**13.15%** ratio cut (or equivalent) |

**Geometry note:** fail bin is **early** (frames 43–54); peak \(S_\star\) sits later (\(u^*\approx0.267\), frame ~104). Numerator and denominator are **disjoint windows** on the trajectory — so denominator-only games are not “the same physics as early slope.”

---

## 2. Dead lane: pure \(S_\star\) inflation (F1)

### Definition

A construction is **pure \(S_\star\) inflation** if:

1. Early-bin absolute range on the sole fail bin (or the bin that would fail under v13 pins) is **unchanged** within numerical noise vs v13 (range stays ≈ 0.001888…), **and**  
2. Global \(S_\star\) is **raised** enough that range/\(S_\star\) ≤ 0.10, **and**  
3. The filing presents this as a T8 / microphysics win without disclosing that only the denominator moved.

**Arithmetic (v13 numbers, numerator fixed):**

\[
S_\star^{\mathrm{need}} \ge \frac{\mathrm{range}}{0.10} \approx \frac{0.00188834}{0.10} \approx 0.018883
\quad\Rightarrow\quad
\frac{S_\star^{\mathrm{need}}}{S_\star^{\mathrm{v13}}} \approx 1.1315
\]

≈ **+13.15%** peak inflation alone would “pass” T8 **without** any early \(\mathrm{d}S/\mathrm{d}u\) fix.

### Why DEAD

| reason | detail |
|---|---|
| Wrong object | Residual demand is early \(\mathrm{d}S/\mathrm{d}u\) (RD1–RD2), not late peak height |
| Gate-silent theater | Can help T3 cosmetics / preserve T1 while faking T8 |
| Sticky dual | Pure \(G_{\mathrm{TMS}}\) scale moves num and den together; pure den-only is the opposite cheat |
| Honesty | Scorecard ratio alone does not disclose *which* factor moved |

**Disposition:** **DEAD** as T8 pass path.  
**Fairness clause:** raising \(S_\star\) **and** lowering early range **together** remains legitimate — **show both** deltas vs v13.

---

## 3. Required disclosure on any future T8_pass

A filing that asserts `T8_pass: True` (or binding candidate after T8) **must** include a table at least as specific as:

| field | v13 baseline | this artifact | Δ (this − v13) | moved? |
|---|---|---|---|---|
| early fail-bin label | [0.10, 0.11) | (report) | — | — |
| early-bin **range** (num) | 0.0018883423986319587 | **required** | **required** | yes/no |
| \(S_\star\) (den) | 0.016688199517780646 | **required** | **required** | yes/no |
| range/\(S_\star\) | 0.113154… | **required** (≤0.10) | **required** | — |
| other failing bins | 1 | **required** (must be 0) | — | — |
| joint gates T1–T6, T2, stall, DC3 | PASS | **required reconfirm** | — | no regress |

**Pass classification (required one-liner):**

| class | criterion | allowed as T8_pass? |
|---|---|---|
| **A — numerator-led** | early range down enough; \(S_\star\) flat or down | **Yes** (if joint gates hold) |
| **B — joint num+den** | early range down **and** \(S_\star\) up; both disclosed | **Yes** if both shown |
| **C — denominator-only** | early range flat; only \(S_\star\) up to force ratio ≤0.10 | **NO — F1 DEAD** |
| **D — undisclosed** | T8_pass true without num/den table | **NO — protocol fail** |

**Also required (unchanged from PAGE_TURN / residual):**

- Write-once versioned JSON (never overwrite v13).  
- Arrays-only scorecard on that artifact.  
- Joint: T1–T6 + stall≤10 + coevo + DC3 + **all** T8 bins ≤0.10.  
- Claim-decoupling + red AGREE before claim; scorecard **never** sets `page_curve_claimed`.  
- `exit 0` on a tool run **≠** PASS (process hygiene).

---

## 4. How F1 extends R1 / R2 / R5 should-not-exist

| Lever | S⋆-only collapse mode | F1 kill |
|---|---|---|
| **R1** dump | “Dump” that only boosts late peak height / EXTRA_BS cosmetics without cutting early \(\Delta S\) | Early range flat → DEAD |
| **R2** entangle | Late entangling boost that inflates \(S_\star\) while early TMS slope unchanged | Early range flat → DEAD |
| **R5** co-mod | Single-H story whose scored effect is only larger peak, not early slope | Early range flat → DEAD |

Full adversarial text lives in [`R1_R2_R5.md`](R1_R2_R5.md).  
**Parent one-liner** in `DEAD_DENIFY.md` (denominator-only lever) is **reaffirmed and operationalized** here.

---

## 5. What F1 does *not* do

| non-action | why |
|---|---|
| Does not loosen the 0.10 bar | Protocol pin fixed |
| Does not pass v13 | 0.113 still FAIL |
| Does not invent micro law | NO FABRICATIONS |
| Does not forbid all \(S_\star\) change | Joint num+den moves OK if disclosed |
| Does not set `page_curve_claimed` | Claim is separate step |
| Does not authorize densify / coevolve thrash | Still DEAD under D4 |

---

## 6. Checklist (copy into future T8_pass filings)

```
[ ] Artifact write-once; sha256 recorded; not overwriting coevolve_v13
[ ] Scorecard arrays-only; OMP=1; log stored
[ ] Table: early-bin range vs v13 (absolute)
[ ] Table: S_star vs v13 (absolute)
[ ] One-line class: A / B / C / D  (C and D = fail protocol)
[ ] If class C: STOP — F1 DEAD, do not file T8_pass
[ ] All T8 bins ≤ 0.10; failing bins = 0
[ ] T1–T6 + T2 + stall + coevo + DC3 reconfirmed PASS
[ ] page_curve_claimed remains false until claim step + red
[ ] No densify thrash; no pure G_TMS-only story without stickiness check
```

---

## 7. Explicit non-claims

- Encoding F1 ≠ T8 pass on v13.  
- F1 ≠ Page closed / Q6 paid.  
- F1 ≠ prediction that R1/R2/R5 will clear.  
- This desk runs **no** new dynamics to demonstrate A/B classes.

---

*End F1_PROTOCOL.md. Pure S⋆ inflation DEAD. Disclose num and den.*
