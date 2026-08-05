# T-W5 — Koide #101/#102 + Wilson holonomy inputs

**Package:** `docs/working_logs/_runs/theory_exhaust_20260805/mb/mb_walls_exhaust/`  
**Date:** 2026-08-05  
**Class:** model-building  
**Prior desk:** `theory_construction_20260804/desk_t7_koide_wilson_20260804/`  
**Instrument:** `scripts/koide_wilson_holonomy_inventory.py`  
**This re-run log:** [`logs/koide_wilson_inventory.log`](logs/koide_wilson_inventory.log)  
**Rule:** NO FABRICATIONS. No invent holonomy / A_μ / n / α_d / θ_W. exit2 expected. Thermal delivery stays KILLED.

---

## GRADE

| field | value |
|---|---|
| **GRADE** | **OPEN-BLOCKED · MISSING_INPUTS 5/5** |
| n_filled (PRESENT) | **0** |
| n_still_missing | **5** |
| θ_W scored | **0** |
| bins scored | **0** |
| inventory exit (this exhaust) | **2** |
| #101 / #102 | **OPEN-BLOCKED** |
| packaging (c) | **LOCKED** |
| thermal delivery | **KILLED** (not restored) |
| lands | **0** |
| COMPLETE | **NO** |

**Reconfirm vs desk_t7:** **stable** — 0 filled / 5 still missing. No change.

---

## CORPUS_HUNT (file:line)

| object | status | file:line / path |
|---|---|---|
| desk_t7 MASTER | n_filled=0; n_still_missing=5; grade OPEN-BLOCKED | `desk_t7_koide_wilson_20260804/MASTER.md:9-24` |
| desk_t7 STATUS_TABLE | 0 PRESENT / 2 PARTIAL / 3 MISSING | `STATUS_TABLE.md:15-32` |
| desk_t7 WILSON_HUNT aggregate | 5/5 block | `WILSON_HUNT.md:108-126` |
| Living Koide residual | protection derived; mechanism OPEN-BLOCKED | `docs/PRTOE_koide_relation.md` residual freeze 2026-08-04 |
| Wall table W5 | mechanism OPEN-BLOCKED; Wilson research only | `open_theory_full_20260804/WALL_TABLE.md:18` |
| Task inventory T-W5 | OPEN-BLOCKED | `theory_task_inventory_20260804/TASKS.md:16`; `REPORT.md:135-143` |
| debt Wilson | 5/5 MISSING_INPUTS | `debt_koide_wilson_20260803/REPORT.md` |
| koide_residual MISSING list | reconfirm 5/5 | `koide_residual/WILSON_MISSING_INPUTS.md` |
| Inventory script gate | refuses score without 5 PRESENT | `scripts/koide_wilson_holonomy_inventory.py` |
| This exhaust inventory | EXIT 2; MISSING_INPUTS 5 of 5 | `logs/koide_wilson_inventory.log` |

---

## Five MISSING still (all block zero-knob Wilson)

| # | Requirement | Status | Why still blocks | Hunt anchors |
|---|---|---|---|---|
| 1 | `dark_SU2_A_mu` | **MISSING** | No dark-SU(2) A archive; T14 `psi_n*.npy` = condensate ψ ≠ A_μ; CLASS gauge tests = metric | desk_t7 `WILSON_HUNT.md:37-48`; inventory log |
| 2 | `family_cycle_path_C` | **PARTIAL** (still missing for zero-knob) | Equilateral asserted; bare √3 ≠ phase c_K; phase-derived spacing circular for 2/9 test | `WILSON_HUNT.md:52-62` |
| 3 | `winding_background_n` | **MISSING** | n ≳ 1.65 bound only; L_gen unassigned; Widnall n~11–25 ≠ family dark-gauge n | `WILSON_HUNT.md:66-77` |
| 4 | `alpha_d_or_electric_projection` | **PARTIAL** (still missing for zero-knob) | α_d ≲ 2.2 window not fixed; pure-gauge collapses; hybrid A unbuilt | `WILSON_HUNT.md:81-92` |
| 5 | `holonomy_evaluator` | **MISSING** | Only inventory gate; evaluator scripts ABSENT; building over missing A_μ = invent | `WILSON_HUNT.md:96-104` |

**Count rule (desk_t7 / this exhaust):**  
`n_filled` = PRESENT only → **0**.  
`n_still_missing` = PARTIAL + MISSING → **5**.

---

## REQUIRED_INPUTS (promotion bar — not present)

All five **PRESENT** without free dials → evaluator → **single** score of pre-registered bins.  
HIT_PRIMARY = Branch A **#102 candidate only**; **#101 still needs exactness source**.

Licensed fill shapes only: lattice SU(2) N_f=3 configs or fixed hybrid connection; independent path metric; fixed n or n-independence proof; fixed α_d/projection; path-ordered evaluator **after** 1–4.  
**Forbidden:** toy A_μ, dialed n, phase-derived c₂ as geometry for 2/9, α_d bound edge as dial, evaluator embedding 2/9.

---

## DEAD lanes

| lane | status |
|---|---|
| Thermal / flat delivery as land | **KILLED** (~171×; not restored) |
| Fake Wilson close / invent holonomy | **refused** |
| `tau_parseval` PASS as mechanism close | desk audit only; `locking_without_Q` OPEN |
| `koide_lock` exit 0 as mechanism close | desk algebra audit only |
| Treat PARTIAL as filled | **false** |

---

## One-liner

> **T-W5 OPEN-BLOCKED:** desk_t7 reconfirmed — **0/5 filled, 5 still MISSING**; no θ_W; no invent holonomy.

*NO FABRICATIONS. exit2 ≠ broken honesty. Leave MCMCs.*
