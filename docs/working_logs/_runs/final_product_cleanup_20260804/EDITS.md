# EDITS.md — final_product_cleanup_20260804

**Job A:** DELETE pure currency back-references from living surfaces.  
**Scope:** `docs/PRTOE_*.md` living shelves + owner-facing `ForJustin/` pastes.  
**Out of scope:** `docs/working_logs/_runs/**` refuse cards / dated packages (not rewritten).

---

## Pattern classes deleted

### lcdm multi-hop was / earlier
- `was 0.086466@N=20409; earlier 0.059@N=19013`
- `was 0.086466@N=20409; earlier 0.059055@N=19013`
- `was 0.086@N=20409; earlier 0.059`
- `was 0.086@N=20409 / 0.059@N=19013`
- `was **0.086466**@N=20409; earlier **0.059055**@N=19013`

### dyad prior stamp / wander history
- `was 0.189201@N=18837`
- `was 0.189 earlier`
- `was **0.189201**@N=18837`
- `History wandered (0.16 → 0.189 → 0.129)`

### routeD prior stamp / trend hop
- `was 102.79@N=1609`
- `was 102.794555@N=1609 (2026-08-03T20:53)`
- `was ~103@N=1609` / `was ~103`
- `improving (was 102.79@N=1609 → **4.941933**@N=3290)`
- `**improving** (102.79→4.94)` / `102.79→**4.941933**`
- `was ~1028× at 102.79`
- currency trend adjective **improving** when tied to prior R−1 stamps

### lcdm multi-hop trajectory (living narrative)
- ``0.093682 → 0.053867 → 0.048827 → 0.059055 → 0.086466 → 0.071122``
- `Trajectory continues … → 0.086466 → 0.071122`
- `trajectory … → 0.086466 → 0.071122`

### repair-log / supersedes lists
- Fairbank banner: `Supersedes any “as of 2 August R−1 = 0.19 / 0.14”, mid-day “0.189 / 0.059”, “0.086 as current”, or “~1.18× closest” / permanent “nearest-and-receding” as-current language`
- `Historical stamps 0.059 / 0.086 as past are OK`
- `was 0.086 / 0.059 as past stamps`

---

## Per-file deletions

### 1. `docs/PRTOE_CHAIN_TABLES.md`
- Quote freeze: removed `was 0.086466@N=20409; earlier 0.059@N=19013` after lcdm current
- Quote freeze: removed `routeD **improving** (was 102.79@N=1609 → **4.941933**@N=3290)` → current only
- Table live? column: removed `was 0.189201@N=18837` (dyad)
- Table live? column: removed `was 0.086466@N=20409; earlier 0.059055@N=19013`
- Table live? column: removed `was 102.79@N=1609 — **improving**`
- Removed full **lcdm trajectory** multi-hop line + “Historical stamps … as past are OK”
- Distances line: removed `was ~1028× at 102.79` and trend **improving**
- Claims ledger rows 2–3: stripped was/earlier and was-102.79 improving

### 2. `docs/PRTOE_CODE_MANIFEST.md`
- Live stamp banner: stripped lcdm was/earlier; routeD `improving (102.79→…)`
- Removed lcdm multi-hop trajectory line
- Table bookable column: `(early; improving)` → `(early)`
- Model/twin/routeD status rows: removed was 0.189 / was 0.086…earlier 0.059 / was 102.79 improving; removed “Trajectory continues…”

### 3. `docs/PRTOE_INDEX.md`
- Production chains cell: stripped was/earlier on lcdm; stripped routeD was ~103 improving
- Restored permanent **Must not claim** bans (nearly there / nearest-and-receding / stuck at 103) if thinned

### 4. `docs/PRTOE_READERS_RISK.md`
- Banner: stripped was/earlier
- §3c progress stamp: stripped was/earlier + trajectory hop
- §4 table: dyad was 0.189; lcdm was/earlier + receding trail; routeD was 102.79 improving
- Basin-resolved paragraph: stripped was/earlier
- Claims row 5: stripped was 0.086 / 0.059

### 5. `docs/PRTOE_READERS_GUIDE.md`
- Currency board: stripped was/earlier multi-hop after lcdm current

### 6. `docs/PRTOE_DEPENDENCY_TREE.md`
- Residual banner live-product row: stripped was/earlier

### 7. `docs/PRTOE_DOMAIN_COVERAGE.md`
- Cosmology domain row: stripped was/earlier

### 8. `docs/PRTOE_REFEREE_CALENDAR.md`
- Sitting NOW banner: stripped was/earlier + routeD improving hop
- Table bookable: `(early; improving)` → `(early)`
- dyad ETA: removed was 0.189 + History wandered
- lcdm ETA: removed was/earlier + multi-hop Trajectory chain
- routeD ETA: removed was 102.79 improving hop
- Historical 07-20 note present stamp: removed “improving from 102.79@N=1609”

### 9. `docs/PRTOE_honest_status.md`
- Header: stripped was/earlier + routeD improving hop
- Table: `(early; improving)` → `(early)`
- Removed lcdm multi-hop trajectory
- Evidence bullet: stripped was/earlier + was ~103 improving

### 10. `docs/PRTOE_hubble_tension.md`
- Residual freeze table: stripped was/earlier from lcdm R−1 cell
- Removed lcdm multi-hop trajectory line
- Status paragraph: stripped was/earlier
- Claims row 1 residual: stripped was 0.086 / earlier 0.059

### 11. `docs/PRTOE_neutrino_home.md`
- Residual freeze §1: stripped lcdm was/earlier
- Claims row 2 residual: stripped was 0.086 / earlier 0.059

### 12. `docs/PRTOE_s8_growth.md`
- Machine residual: removed routeD **improving** + was 102.79
- Live stamp line: stripped lcdm was/earlier + routeD was ~103 improving
- Claims row 3: stripped was ~103

### 13. `docs/PRTOE_s8_tension.md`
- Live progress line: stripped lcdm was/earlier + routeD was ~103 improving

### 14. `docs/PRTOE_fairbank_note_draft.md`
- Currency banner: stripped dyad was 0.189 + lcdm was/earlier; removed multi-hop Supersedes list (kept permanent nearest-and-receding ban)
- Body fit-status: stripped was 0.189 + was/earlier
- Claims row 4: stripped was 0.086 / earlier 0.059

### 15. `ForJustin/STATUS_CONTINUE.md`
- Machine lcdm line: stripped was 0.086466 / earlier 0.059055

### 16. `ForJustin/PASTE_CHATGPT_REF.md`
- E2 row + machine one-liner: stripped was/earlier multi-hop

### 17. `ForJustin/PASTE_CLAUDE_RED.md`
- bbnfix gate row + standing fences: stripped was/earlier and “as past stamps”

---

## Kept (current fact only)

| chain | R−1 | N | timestamp | ratio-to-stop | converged | bookable |
|---|---:|---:|---|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | **0.071122** | 21886 | 2026-08-04T13:01:13 | **1.42×** (stop 0.05) | **false** | **NO** |
| `dyad_mnu_bbnfix` | **0.128943** | 20302 | 2026-08-04T03:25:56 | **~2.58×** (stop 0.05) | **false** | **NO** |
| `cmp_prtoe_routeD` | **4.941933** | 3290 | 2026-08-04T09:00:36 | **~49.4×** (stop 0.1) | **false** | **NO** (early; not dual-gate) |

Book: **REFUSED**.

### Kept permanent facts (not trend currency)
- Temporary R−1 < 0.05 without self-stop is **not** bookable
- Do **not** freeze “nearest-and-receding forever” / “~1.18× closest” / “nearly there”
- Gate = both bbnfix legs R−1 < 0.05 **and** `converged: true` → `scripts/book_bbnfix_when_ready.py` only
- Offline GetDist GR diagnostic only — not booking authority

---

## Files cleaned count

**17**
