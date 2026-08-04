# RED CURE — BBN ε EXTERNAL WIN DELIVERED (2026-08-04)

**Finding:** Claude red DENIED `debts_hardwins_full` for booking BBN ε as **"EXTERNAL WIN DELIVERED"**.  
Win definition of done requires a **public** record (Zenodo one record / DOI). On disk: bbn-eps-bound is READY (endorsement pending, no DOI); only supertrace has a real DOI. Self-consistency of `recompute_eps_bound.py` (3.196%) vs paper (3.20%) is **internal arithmetic**, not an external win.

**Cure (applied):**  
- Status → **ARITHMETIC VERIFIED (internal)**  
- Public half → **EXTERNAL WIN PENDING (no DOI)**  
- Removed “owner-optional ship; does not un-deliver arithmetic” hedge.  
- Arithmetic PASS card **kept** as internal verification only.

**Rule lock:** do not claim EXTERNAL WIN as delivered for BBN ε until a DOI / public record exists.

---

## Before → after (status phrase)

| Before | After |
|---|---|
| **EXTERNAL WIN DELIVERED** | **ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** |
| External win remains **DELIVERED** | **ARITHMETIC VERIFIED (internal)**. **EXTERNAL WIN PENDING (no DOI)** |
| BBN ε **DELIVERED** (arithmetic external win) | BBN ε **ARITHMETIC VERIFIED (internal)**; external win PENDING public record |
| Zenodo DOI still owner-optional ship; does not un-deliver arithmetic | Public record (Zenodo one record / DOI) still required for done |

---

## Files touched

### Primary package (`debts_hardwins_full_20260804/`)

| File | Change |
|---|---|
| `HARD_WINS_TABLE.md` | Rank-2 status (L15); Language row (L33); language-lock matrix (L75) |
| `REPORT.md` | Hard-wins summary (~L52); residual class B; promotion honesty; anti-contradiction checklist; surfaces-updated line |
| `DEBT_TABLE.md` | Compact code DELIVERED→ARITHMETIC VERIFIED; hard-win language table (~L53) |
| `RED_CURE_EXTERNAL_WIN_20260804.md` | This receipt |

### Required related surfaces

| File | Change |
|---|---|
| `docs/working_logs/SCIENCE_DEBTS_2026-08-03.md` | Hard-win crosswalk (×2) + HW-BBN-ε status row |
| `docs/working_logs/_runs/hard_wins_90day_20260803/REPORT.md` | Promotion stamp; 2026-08-04 status table; language locks |
| `docs/working_logs/_runs/PROMOTION_BOARD_20260803_IMPROVE.md` | P-BBN promote row + still-valid promotions row |
| `docs/working_logs/_runs/MASTER_CLOSURE_DASHBOARD_20260803.md` | HW3 / HW3-ship status; REF backlog rank 2 |
| `docs/working_logs/_runs/live_surfaces_full_20260804/REPORT.md` | honest_status bullet 3 |
| `docs/working_logs/_runs/live_surfaces_full_20260804/EDITS.md` | BBN ε row |

### Other load-bearing / consistent surfaces

| File | Change |
|---|---|
| `docs/PRTOE_INDEX.md` | Live status stamp BBN ε row; papers packages line |
| `docs/PRTOE_honest_status.md` | BBN ε paragraph |
| `docs/PRTOE_READERS_RISK.md` | Claims ledger row 8 |
| `docs/working_logs/_runs/MODEL_IMPROVE_NO_POLYCHORD_20260803.md` | BBN ε promotion grade |
| `docs/working_logs/_runs/hard_win3_bbn_eps_recompute_20260803/RECHECK_20260803_continue.md` | Night promotion stamp cured |
| `docs/working_logs/_runs/open_board_split_20260803/BBN_EPS_REVERIFY_20260804.md` | “External win remains DELIVERED” cured |
| `docs/working_logs/_runs/RESIDUAL_IMPROVE_INVENTORY_20260803.md` | Class B1/B2 + paid stamp |
| `docs/working_logs/_runs/shelf_map_currency_20260804/REPORT.md` | Package summary + currency table |
| `docs/working_logs/_runs/shelf_map_currency_20260804/EDITS.md` | INDEX / papers / claims edit notes |
| `docs/working_logs/_runs/master_integrate_20260804/MASTER_REPORT.md` | debts_hardwins one-liner |
| `docs/working_logs/_runs/IMPROVEMENT_BOARD_20260803.md` | §2 BBN ε heading + PENDING fence |
| `papers/bbn-eps-bound/README.md` | External-win reverify paragraph restamped |
| `ForGrok&Claude.md` | P-BBN promotion tables + cure stamp under DENIED finding |

---

## Residual grep

```bash
rg -n 'EXTERNAL WIN DELIVERED' docs/
```

**Expected:** zero live status claims for BBN ε.  
(Historical red denial text under `ForGrok&Claude.md` may still quote the denied phrase as audit trail only — outside `docs/`.)

---

## Final status line (BBN ε)

**ARITHMETIC VERIFIED (internal)** — 3.196% ≈ 3.20% PASS (`recompute_eps_bound.py`).  
**EXTERNAL WIN PENDING (no DOI)** — public record still owed.

*NO FABRICATIONS.*
