# Fence consistency check — 2026-08-03

**Scope:** shelf fence audit only (INDEX, exploratory README, fence log paths, exploratory presence/stubs).  
**Method:** filesystem existence + relative-link target resolution.  
**Discipline:** NO FABRICATIONS — broken links / missing stubs / location mismatches only. No physics claims.

**Sources checked:**
- `docs/PRTOE_INDEX.md`
- `docs/exploratory/README.md`
- `docs/working_logs/TOE_EXPANSION_SHELF_FENCE_20260803.md`
- On-disk paths under `docs/` and `docs/exploratory/`

---

## 1. INDEX entries (`docs/PRTOE_INDEX.md`)

| Topic | INDEX link target | On disk | Verdict |
|---|---|---|---|
| induced_gravity | `PRTOE_induced_gravity.md` (shelf) | `docs/PRTOE_induced_gravity.md` **exists** | **OK** |
| quantum_gravity | `PRTOE_quantum_gravity.md` (shelf) | `docs/PRTOE_quantum_gravity.md` **exists** | **OK** |
| small_scale_structure | **no INDEX entry** | `docs/PRTOE_small_scale_structure.md` **exists** (shelf) | **MISSING INDEX entry** |

Related INDEX links for fence-moved exploratory topics (spot-check): hierarchy, forced_combination, laboratory_cousins, no_singularities, white_holes, arrow_of_time, information_paradox, entropy all point at `exploratory/PRTOE_*.md` and those files **exist**. **OK**.

**Also stale (not a broken link):** INDEX Exploratory blurb still says “holds **36** files moved … on 2026-07-28”; exploratory currently has **44** content files (after 2026-08-03 fence pass).

---

## 2. Exploratory README redirects / fence narrative

| Claim in `docs/exploratory/README.md` | Actual | Verdict |
|---|---|---|
| QG promoted to shelf; stub may remain at `exploratory/PRTOE_quantum_gravity.md` | Stub **exists** (MOVED banner → `../PRTOE_quantum_gravity.md`, `../PRTOE_induced_gravity.md`, promotion record) | **OK** |
| Stub targets resolve | `docs/PRTOE_quantum_gravity.md`, `docs/PRTOE_induced_gravity.md`, `docs/working_logs/_runs/qg_goalA_20260803/PROMOTION_RECORD.md` all **exist** | **OK** |
| Promoted to shelf: `PRTOE_small_scale_structure.md` | `docs/PRTOE_small_scale_structure.md` **exists**; **no** `docs/exploratory/PRTOE_small_scale_structure.md` | Path OK; **no exploratory redirect stub** (unlike QG) |
| Contents group still lists `small_scale_structure` under exploratory domain stubs | File **not** in `docs/exploratory/` | **STALE contents list** |
| Fence-moved set listed under “Moved here…” | hierarchy, forced_combination, laboratory_cousins, arrow_of_time, information_paradox, white_holes, no_singularities, entropy all present under exploratory | **OK** |
| Contents five-group census | Does **not** enumerate the eight fence arrivals (or QG stub); still lists promoted-away `small_scale_structure` | **Incomplete / stale contents** |

---

## 3. Fence log vs actual paths (`TOE_EXPANSION_SHELF_FENCE_20260803.md`)

| Fence listing | Expected location after fence | Actual | Verdict |
|---|---|---|---|
| Moved: `PRTOE_quantum_gravity.md` (then amendment re-promotes) | shelf + exploratory stub | `docs/PRTOE_quantum_gravity.md` + `docs/exploratory/PRTOE_quantum_gravity.md` (stub) | **OK** |
| Moved: hierarchy_problem | exploratory | `docs/exploratory/PRTOE_hierarchy_problem.md` | **OK** |
| Moved: forced_combination | exploratory | `docs/exploratory/PRTOE_forced_combination.md` | **OK** |
| Moved: laboratory_cousins | exploratory | `docs/exploratory/PRTOE_laboratory_cousins.md` | **OK** |
| Moved: arrow_of_time | exploratory | `docs/exploratory/PRTOE_arrow_of_time.md` | **OK** |
| Moved: information_paradox | exploratory | `docs/exploratory/PRTOE_information_paradox.md` | **OK** |
| Moved: white_holes | exploratory | `docs/exploratory/PRTOE_white_holes.md` | **OK** |
| Moved: no_singularities | exploratory | `docs/exploratory/PRTOE_no_singularities.md` | **OK** |
| Moved: entropy | exploratory | `docs/exploratory/PRTOE_entropy.md` | **OK** |
| Promoted: small_scale_structure | shelf | `docs/PRTOE_small_scale_structure.md` | **OK** |
| Amendment: induced_gravity thin slice | shelf | `docs/PRTOE_induced_gravity.md` | **OK** |

**No missing fence-listed content files.** All nine original move names + small_scale promotion + induced_gravity land on disk as documented (QG dual: full shelf + stub).

---

## 4. Exploratory presence / stubs (requested set)

| Topic | Path | Kind | Verdict |
|---|---|---|---|
| quantum_gravity | `docs/exploratory/PRTOE_quantum_gravity.md` | **redirect stub** (not content) | **OK** |
| hierarchy | `docs/exploratory/PRTOE_hierarchy_problem.md` | full content (not a stub) | **present** |
| forced_combination | `docs/exploratory/PRTOE_forced_combination.md` | full content | **present** |
| lab_cousins | `docs/exploratory/PRTOE_laboratory_cousins.md` | full content | **present** |
| arrow | `docs/exploratory/PRTOE_arrow_of_time.md` | full content | **present** |
| info paradox | `docs/exploratory/PRTOE_information_paradox.md` | full content | **present** |
| white_holes | `docs/exploratory/PRTOE_white_holes.md` | full content | **present** |
| no_singularities | `docs/exploratory/PRTOE_no_singularities.md` | full content | **present** |
| entropy | `docs/exploratory/PRTOE_entropy.md` | full content | **present** |
| small_scale_structure (promoted **out**) | no exploratory path | no redirect stub | **no stub** (only noted if old links expected; live INDEX also omits shelf entry) |

---

## 5. Broken links only (resolved relative to containing file)

### Live shelf / core docs

| Source | Link | Resolves to | Status |
|---|---|---|---|
| `docs/PRTOE_small_scale_structure.md` L40 | `[BIBLIOGRAPHY.md](../BIBLIOGRAPHY.md)` | `BIBLIOGRAPHY.md` at **repo root** (not `docs/BIBLIOGRAPHY.md`) | **BROKEN** (post-promotion leftover `../` depth) |

Shelf INDEX and parent wiring for induced_gravity / quantum_gravity / exploratory fence set: **no broken markdown targets found** in the INDEX spot-check (targets exist).

### Working-log run reports still pointing at **pre-fence shelf** paths

These markdown links resolve under `docs/` (missing `exploratory/`), so they 404 against the current tree:

| Source | Broken targets (examples) |
|---|---|
| `docs/working_logs/_runs/debt_page_curve_20260803/REPORT.md` | `../../../PRTOE_information_paradox.md`, `../../../PRTOE_entropy.md`, `../../../PRTOE_no_singularities.md` → should be `docs/exploratory/…` |
| `docs/working_logs/_runs/debt_koide_wilson_20260803/REPORT.md` | `../../../PRTOE_forced_combination.md` |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/PAGE_CURVE_IMPLEMENTATION_PLAN.md` | `../../../PRTOE_information_paradox.md` |
| `docs/working_logs/_runs/story_grade_triage_20260803/PASS3_DERIVE_PAYDOWN.md` | `../../../PRTOE_hierarchy_problem.md`, `../../../PRTOE_information_paradox.md` |

**Note:** many other `_runs/story_grade_triage_*` files *name* old shelf paths in backticks/tables without always linking; those are stale path strings, not all clickable links. Historical inventory still places moved files on shelf / small_scale under exploratory — **stale records**, not re-checked as every link.

### Stale path strings (non-link / inventory; fence-relevant)

- `docs/working_logs/_runs/story_grade_triage_20260803/PASS2_EXPLORATORY_BATCH.md` cites `docs/exploratory/PRTOE_small_scale_structure.md` — **path gone** (promoted to shelf).
- `docs/working_logs/_runs/story_grade_triage_20260803/INVENTORY.md` still lists fence-moved files as `docs/PRTOE_*.md` shelf and small_scale as exploratory — **stale**.
- `docs/PRTOE_DOMAIN_COVERAGE.md` row 33a path text `` `PRTOE_hierarchy_problem.md` `` omits `exploratory/` (not a markdown link; wrong bare path).
- `ForGrok&Claude.md` entry paths still say `docs/PRTOE_forced_combination.md`, `docs/PRTOE_white_holes.md` (shelf) — files live under exploratory.
- `docs/working_logs/_SCRIPT_REGRESSION_2026-08-02.md` names `docs/PRTOE_entropy.md` (pre-move).

---

## 6. Top inconsistencies (summary)

1. **`PRTOE_small_scale_structure` promoted to shelf but absent from `docs/PRTOE_INDEX.md`.**  
2. **Broken link in shelf `docs/PRTOE_small_scale_structure.md`:** `../BIBLIOGRAPHY.md` (wrong relative depth).  
3. **`docs/exploratory/README.md` Contents still lists `small_scale_structure`** after promotion; does not place fence arrivals into the group census.  
4. **No exploratory redirect stub for small_scale_structure** (optional; QG has one by design).  
5. **Multiple `_runs/*.md` reports still deep-link to `docs/PRTOE_{information_paradox,entropy,no_singularities,forced_combination,hierarchy_problem}.md`** — those shelf paths **do not exist**; content is under `docs/exploratory/`.  
6. INDEX exploratory file-count “36” is stale vs current exploratory tree (~44).

**Non-issues (verified OK):**  
- Shelf homes for `induced_gravity` + full `quantum_gravity`.  
- Exploratory QG stub + promotion record targets.  
- All eight fence demotions present under exploratory as full files.  
- INDEX links for those demotions use `exploratory/` correctly.

---

*End of report. Paths absolute under repo root `prtoe_class/`.*

## BLUE CURES AFTER AUDIT (14:15)

| Issue | Cure |
|---|---|
| small_scale missing INDEX | **added** to PRTOE_INDEX.md Structure section |
| BIBLIOGRAPHY ../ wrong | **fixed** to `BIBLIOGRAPHY.md` |
| exploratory README still listed small_scale | **note** promoted to shelf |
| INDEX "36 files" | **rewrote** to non-stale count language |
| deep-links in debt/page reports | **rewired** to exploratory/ paths |
