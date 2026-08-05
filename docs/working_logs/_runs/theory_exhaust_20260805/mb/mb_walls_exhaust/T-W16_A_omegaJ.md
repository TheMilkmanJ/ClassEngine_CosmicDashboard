# T-W16 / T-W16a — Forward ω_J / A_ωJ seat content

**Package:** `docs/working_logs/_runs/theory_exhaust_20260805/mb/mb_walls_exhaust/`  
**Date:** 2026-08-05  
**Class:** model-building  
**Prior desk:** `theory_construction_20260804/desk_t5_aomegaJ_seat_20260804/`  
**Rule:** NO FABRICATIONS. Do not invent seat coefficients. No free dial to 5.672 keV. Charge A holds. exit0 ≠ PASS.

---

## GRADE

| field | value |
|---|---|
| **GRADE (T-W16)** | **OPEN-BLOCKED** · forward ω_J non-circular land **none** |
| **GRADE (T-W16a)** | **EMPTY_CORPUS_SEAT** · P2-1/P2-2 schemas **MISSING_INPUT** |
| A_ωJ | **CANDIDATE** (structure only; unchanged) |
| Charge A | **holds** |
| independent χ | **EMPTY** |
| independent J_seat | **EMPTY** |
| independent ω_J^micro | **EMPTY** |
| ω_J 5.672 keV | **BACK-SOLVED** hygiene only — **not a land** |
| lands | **0** |
| K5 | open, **not fired** (empty ≠ impossibility) |
| COMPLETE | **NO** |

### EMPTY_CORPUS_SEAT stamp (cite desk_t5)

> After corpus hunt (desk_t5 + priors): **no independent χ, no independent J_seat, no independent ω_J^micro**. Fill under Rule 1 **refused**. Residual **#39 OPEN-BLOCKED**. **Charge A holds.**  
> Authority: `desk_t5_aomegaJ_seat_20260804/EMPTY_CORPUS_SEAT.md` · `MASTER.md:13` · `CHARGE_A.md`.

**D5 note (inventory):** T-W16a ⊂ T-W16 — W16a Close is subset; one K5 event would close both IDs. This exhaust keeps both IDs for fence clarity but grades them as one empty seat object.

---

## CORPUS_HUNT (file:line)

| object | grade | file:line / path |
|---|---|---|
| desk_t5 MASTER | EMPTY_CORPUS_SEAT; Charge A holds; lands 0 | `desk_t5_aomegaJ_seat_20260804/MASTER.md:10-21` |
| EMPTY_CORPUS_SEAT stamp | empty χ / J_seat / ω_J^micro | `EMPTY_CORPUS_SEAT.md:1-15`, `:41-69`, `:109-119` |
| CHARGE_A | rename residual without second premise | `CHARGE_A.md:14-36` |
| CORPUS_HUNT desk_t5 | file:line empty | `desk_t5/CORPUS_HUNT.md` |
| Living baryogenesis #39 | forward OPEN-BLOCKED | `docs/PRTOE_baryogenesis.md` residual / #39 |
| Wall table W16 | junction COMPLETE-CONDITIONAL; forward OPEN-BLOCKED | `open_theory_full_20260804/WALL_TABLE.md:29` |
| Task inventory T-W16 / T-W16a | OPEN-BLOCKED / empty schemas | `theory_task_inventory_20260804/TASKS.md:27-28`; `REPORT.md:245-263` |
| Formulability debt | zero non-circular lands | `debt_omegaJ_forward_formulability_20260803` |
| Priors A_omegaJ_seat_UV / rule1 | no land content | `A_omegaJ_seat_UV/`; `A_omegaJ_rule1/` |
| Accept / kill bands (locked) | ACCEPT [3,12] keV; KILL < 0.057 keV | desk_t5 MASTER |

---

## REQUIRED_INPUTS (what would unstick — still empty)

Any of the following with **I1–I7** audit and **no** free dial to 5.672 keV (`EMPTY_CORPUS_SEAT.md` §3):

### Package B (pair)

1. UV/IR matching → **numeric or closed-form J_seat** (driven cos curvature, not U_pin).  
2. Micro **χ** ≠ v_L, ≠ silent f_e-scalar, ≠ η-fit.  
3. ω_J² = J_seat/χ **before** looking at R_need / η.  
4. Band score vs locked ACCEPT/KILL.

### Package A (direct)

1. ω_J = ω_J^micro(…) with every symbol η-blind.  
2. Not secretly √(2 R_need Γ_φ θ̇).  
3. I1–I7 symbol-by-symbol.  
4. Band score.

### Lattice / external (preferred Charge A answer)

1. External seat–visible junction response at T_sph that cannot see η.  
2. Or new named axiom with Rule-1 package forcing a number without free constant aimed at back-solve.

**P2-1 / P2-2 (T-W16a):** still SURVIVOR-SCHEMA / **MISSING_INPUT** — no fill this exhaust.

---

## DEAD lanes / honesty kills

| lane | status |
|---|---|
| Free dial so ω_J = 5.672 keV | **honesty kill** |
| Invent seat coefficients / χ / c_A | **forbidden** |
| Quartet exit0 / back-solve as land | **false** (hygiene) |
| v_L as χ | **FORBIDDEN ID** (#39) |
| U_pin ∝ m₁² as J_seat | **WRONG OBJECT** |
| Jeans √(4πGρ) as ω_J | **WRONG OBJECT** |
| Charge A breach (rename residual as axiom) | **holds / kill if breached** |
| K5 fire from empty alone | **not fired** (empty ≠ impossibility proof) |

---

## Charge A (holds)

Calling ω_J² = J_seat/χ with J_seat and χ **unstated** does **not** add physics; it renames residual #39. Until a **second independent premise** supplies χ or J_seat or ω_J^micro η-blind, A_ωJ is **not gradeable** against the pre-locked band.

---

## One-liner

> **T-W16 / T-W16a EMPTY_CORPUS_SEAT** (desk_t5): no independent χ / J_seat / ω_J^micro; **Charge A holds**; lands 0; #39 OPEN-BLOCKED.

*NO FABRICATIONS. No free dial to 5.672 keV. Leave MCMCs.*
