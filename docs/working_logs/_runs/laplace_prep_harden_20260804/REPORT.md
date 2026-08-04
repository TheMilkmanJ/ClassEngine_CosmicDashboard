# Laplace / booking readiness harden — 2026-08-04

**Package:** `docs/working_logs/_runs/laplace_prep_harden_20260804/`  
**Upstream:** `docs/working_logs/_runs/laplace_booking_full_20260804/`  
**Laplace inventory:** `docs/working_logs/_runs/open_board_split_20260803/LAPLACE_PREP.md`  
**Hard rules:** NO FABRICATIONS · do not book unconverged · leave live MCMCs alone ·  
booking ≠ publishing (tables need `RED_AUDIT`) · no nested sampling · no invented Laplace number ·  
no long GetDist force this pass.

---

## Live gate (smoke stamp 2026-08-04)

| chain | progress R−1 | N | checkpoint | bookable |
|---|---:|---:|---|---|
| `dyad_mnu_bbnfix` | **0.128943** | 20302 | `converged: false` | **NO** |
| `cmp_lcdm_mnu_bbnfix` | **0.059055** | 19013 | `converged: false` | **NO** |

Gate still **CLOSED** (both R−1 ≥ 0.05 and/or not self-stopped).  
Dyad moved from earlier prep stamp ~0.189 → ~0.129 during live run — still over bar.  
**Left MCMCs alone.** No booking. No PolyChord. No Laplace number invented.

---

## Script verification (this pass; stdout in `smoke_captures/`)

| script | expected | result | exit |
|--------|----------|--------|-----:|
| `book_bbnfix_when_ready.py` | REFUSED + refuse card | **PASS** — clearer refuse fences | **2** |
| `finalize_h0_at_convergence.py` | NOT YET when gate closed | **PASS** — no H₀ extract | **2** |
| `make_getdist_tables.py --include-bbnfix` | NOT READY; no shelf write | **PASS** — Stage B note + force fence | **2** |
| `bbnfix_when_ready_all.sh` | refuse at book; no finalize/tables | **PASS** | **2** |
| `WRITE_TABLES` default | **0** | **PASS** (source L39) | — |
| `--write-tables` needs `RED_AUDIT` | `red: AGREE` / `AGREE-IF` | **PASS** (source + clearer empty-BOOK_DIR msg) | — |
| `--force-bbnfix` path | UNBOOKABLE-only | **PASS** (source + prior artifact `getdist_force_UNBOOKABLE_20260804_030942/`) | — |
| Long GetDist force this pass | **not run** | **PASS** (fence) | — |

Smoke files:

- `smoke_captures/book_refuse.txt` (`book_exit=2`)
- `smoke_captures/finalize_refuse.txt` (`finalize_exit=2`)
- `smoke_captures/tables_refuse.txt` (`tables_exit=2`)
- `smoke_captures/all_sh_refuse.txt` (`all_exit=2`)

Latest refuse cards from this pass include e.g.  
`docs/working_logs/_runs/bbnfix_booking_20260804_092707/` (book) and  
`docs/working_logs/_runs/bbnfix_booking_20260804_092723/` (all.sh).

### Force path (source + prior smoke; no new long force)

`scripts/make_getdist_tables.py`: incomplete gate + `--force-bbnfix` →  
`unbookable_force=True` → writes only  
`docs/working_logs/_runs/getdist_force_UNBOOKABLE_<stamp>/CHAIN_TABLES_UNCONVERGED.md`  
with in-file UNCONVERGED / UNBOOKABLE banner; living `PRTOE_CHAIN_TABLES.md` **untouched**.  
Verified artifact still present: `../getdist_force_UNBOOKABLE_20260804_030942/`.  
Living shelf still carries OPEN-MACHINE residual freeze banner (not force numbers).

---

## Stage A vs Stage B (post-gate) — now explicit in runbooks

| stage | what | default command | forward shelf? |
|-------|------|-----------------|:--------------:|
| **Stage A** | book + finalize (+ delta proxy) | `bash scripts/bbnfix_when_ready_all.sh` | **NO** |
| **Red** | audit booking package | write `RED_AUDIT.md` with `red: AGREE` or `AGREE-IF` | no |
| **Stage B** | tables → `PRTOE_CHAIN_TABLES.md` | `… --write-tables` | **YES** (stamp required) |

`WRITE_TABLES=0` by default. booking ≠ publishing.

---

## Kill criteria (canonical list K1–K10)

Documented in hardened runbooks (checklist, LAPLACE_PREP, PREFLIGHT, RUNBOOK):

| # | kill if… |
|---|----------|
| K1 | Book while either R−1 ≥ 0.05 |
| K2 | Book before both `converged: true` |
| K3 | Quote peeks / force paths as results |
| K4 | Living shelf written from `--force-bbnfix` |
| K5 | Stage B without RED_AUDIT (except owner `--force-tables`) |
| K6 | PolyChord / nested for booking |
| K7 | Kill live MCMCs without owner order |
| K8 | Promote pre-bbnfix ΔlnZ ≈ +2.6 as final bbnfix evidence without fence |
| K9 | RouteD substitute for letter pair |
| K10 | Invent Laplace number / invent `scripts/laplace_bbnfix.py` |

---

## What Laplace ΔlnZ prep exists vs waits for bbnfix book

| exists now | waits for bbnfix Stage A book |
|------------|--------------------------------|
| Gate refuse on all booking entrypoints | Bookable three-rank H₀ / Σm_ν / S8 |
| CosmicForge Hessian formula (generic) | Bookable ΔlnZ under **BBN-fixed** stack |
| Δχ² proxy script (gate-hard; not Laplace) | Proxy number itself |
| Historical pre-bbnfix ΔlnZ ≈ +2.6 (**fenced**) | Replacing standing claim with bbnfix ΔlnZ |
| Honest MISSING: no `scripts/laplace_bbnfix.py` | Inventing that CLI or a number |

**No Laplace number produced this pass.** Nested sampling not opened.

---

## Code safety edits (small)

| file | change |
|------|--------|
| `scripts/book_bbnfix_when_ready.py` | Refuse stdout + REPORT: no H₀/tables/Laplace; pre-bbnfix fence; Stage A/B pointer |
| `scripts/finalize_h0_at_convergence.py` | Gate-closed: no H₀/tables/Laplace; pre-bbnfix fence |
| `scripts/bbnfix_when_ready_all.sh` | Stage B missing-stamp message: empty BOOK_DIR + booking≠publishing |
| `scripts/make_getdist_tables.py` | Gate refuse: Stage B / RED_AUDIT note; force = UNBOOKABLE-only reminder |

No tests suite for these scripts existed; refuse smokes above serve as regression checks.

---

## Docs hardened

| path | change |
|------|--------|
| `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` | Stage A/B; kill list; book entrypoint; fix stale ROOTS instruction; pre-bbnfix fence |
| `docs/working_logs/_runs/open_board_split_20260803/LAPLACE_PREP.md` | Stage A/B; prep vs wait; kill list; ΔlnZ fences |
| `docs/working_logs/_runs/laplace_booking_full_20260804/RUNBOOK.md` | Option 1 Stage A default / Stage B --write-tables; kill list; Laplace prep table |
| `docs/working_logs/_runs/laplace_booking_full_20260804/PREFLIGHT.md` | Stage A→red→B order; K1–K11 |

See **EDITS.md** for file-level inventory. **RUNBOOK.md** (this package) is the short post-gate operator card.

---

## Explicit non-actions this pass

- Did **not** book posteriors  
- Did **not** invent a Laplace / ΔlnZ number  
- Did **not** run nested sampling / PolyChord  
- Did **not** run long GetDist force  
- Did **not** kill live MCMCs  
- Did **not** write living `PRTOE_CHAIN_TABLES.md` body  

*NO FABRICATIONS. NO EARLY BOOK. NO POLYCHORD. booking ≠ publishing.*
