# Laplace / bbnfix booking — full readiness package

**Stamp:** 2026-08-04  
**Scope:** one-command-ready Step C + full booking stack when the BBN-fixed pair grades.  
**Hard rules:** NO PolyChord. NO kill chains. NO book while R−1 ≥ 0.05.  
**Authority:** `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` +  
`docs/working_logs/_runs/open_board_split_20260803/LAPLACE_PREP.md`.

**This package does not run booking early.** Gate is **CLOSED** at prep stamp.

---

## Live gate (prep stamp)

| chain | progress R−1 (field 4) | N | checkpoint | ranks `.1–3` |
|---|---:|---:|---|---|
| `dyad_mnu_bbnfix` | **0.189201** | 18837 | `converged: false` | present |
| `cmp_lcdm_mnu_bbnfix` | **0.059055** | 19013 | `converged: false` | present |

```
python3 scripts/book_bbnfix_when_ready.py  → REFUSED (exit 2)
python3 scripts/finalize_h0_at_convergence.py → NOT YET (exit 2)
```

Gate definition: **both** R−1 **< 0.05** **and** both `converged: true` (self-stop).  
Strict `<`, not `≤`. Both legs required.

---

## Readiness matrix

| # | Piece | Path | Status | Notes |
|---|-------|------|:------:|-------|
| 1 | Posterior booking checklist | `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` | **READY** | Steps A–C; gate + non-actions |
| 2 | Laplace prep audit | `_runs/open_board_split_20260803/LAPLACE_PREP.md` | **READY** | inventory; MISSING full Laplace CLI honest |
| 3 | Prior preflight | `_runs/hard_wins_90day_20260803/BBNFIX_BOOKING_PREFLIGHT.md` | **READY** | older stamp; same gate |
| 4 | **This package RUNBOOK** | `_runs/laplace_booking_full_20260804/RUNBOOK.md` | **READY** | ordered commands; owner executes |
| 5 | **This package PREFLIGHT** | `_runs/laplace_booking_full_20260804/PREFLIGHT.md` | **READY** | checklist boxes |
| 6 | Gate + GetDist booking entrypoint | `scripts/book_bbnfix_when_ready.py` | **READY** | R−1 + self-stop; exit 2 refuse; three-rank |
| 7 | H₀ letter gate | `scripts/finalize_h0_at_convergence.py` | **READY** | NOT YET exit **2**; stdout only |
| 8 | GetDist tables instrument | `scripts/make_getdist_tables.py` | **READY** | `--include-bbnfix` after gate; exit **2** if not ready (no table clobber) |
| 9 | Δχ² proxy (Step C.1) | `scripts/bbnfix_delta_chi2_proxy.py` | **READY** | gate-hard; **not** bookable Laplace |
| 10 | One-command pipeline | `scripts/bbnfix_when_ready_all.sh` | **READY** | Stage A book+finalize; tables only after red stamp (`--write-tables`) |
| 11 | CosmicForge Laplace (Hessian) | `run_cosmicforge.py` ~L2083–2095 | **READY (generic)** | `log_z_laplace = -0.5 χ² + 0.5 n log(4π) - 0.5 logdet`; needs yaml + capacity |
| 12 | Bridge sampling library | `forge/evidence.py` | **READY (library)** | non-default; fresh likelihoods |
| 13 | Standalone cobaya-pair full Laplace CLI | `scripts/laplace_bbnfix.py` | **MISSING** | **honest** — not invented; use CosmicForge or proxy |
| 14 | Bookable ΔlnZ under **BBN-fixed** stack | — | **BLOCKED** | needs graded pair + Hessian path |
| 15 | Pre-bbnfix ΔlnZ ≈ +2.6 | historical CosmicForge | **historical only** | **wrong stack** — do not silently replace |
| 16 | PolyChord nested | — | **OUT OF SCOPE** | do not open for this booking session |
| 17 | RouteD thaw | `cmp_prtoe_routeD` | **separate** | stop 0.1; not letter pair |

---

## Script gate behaviour (verified in source; stdout capture optional residual)

Refuse strings and exit codes **verified in source** (e.g. `book_bbnfix_when_ready.py`
refuse + `return 2`; `make_getdist_tables.py` `--include-bbnfix` → exit 2 / `--force-bbnfix`
→ UNBOOKABLE working_logs only). Live refuse **cards** exist under
`docs/working_logs/_runs/bbnfix_booking_*/` — e.g.
[`../bbnfix_booking_20260804_085747/REPORT.md`](../bbnfix_booking_20260804_085747/REPORT.md)
(**REFUSED**, exit 2; dyad R−1=0.189201 / lcdm 0.059055; both not self-stopped).
Package-local full stdout dumps under `smoke_captures/` are an **optional residual**
(not required to trust refuse behaviour). Force-path smoke log:
`smoke_force_bbnfix.txt` — completed to UNBOOKABLE path (see force status check below);
living shelf not written.
**Do not read “READY” as “Claude AGREE”** (delivered ≠ graded).

| script | refuse message | exit on refuse | self-stop required |
|---|---|---:|---|
| `book_bbnfix_when_ready.py` | `REFUSED — booking blocked` | **2** | yes |
| `finalize_h0_at_convergence.py` | `NOT YET — need R−1 < 0.05 … AND sampler self-stop` | **2** | yes |
| `make_getdist_tables.py --include-bbnfix` | `NOT READY` / `REFUSED: will not write …` | **2** | yes |
| `make_getdist_tables.py --force-bbnfix` | gate incomplete → **does not** write living `PRTOE_CHAIN_TABLES.md`; writes `docs/working_logs/_runs/getdist_force_UNBOOKABLE_<stamp>/` with in-file UNCONVERGED banner (code cure 2026-08-04) | **0** (unbookable path) | n/a |
| `bbnfix_delta_chi2_proxy.py` | `REFUSED — need both R−1 < 0.05 AND converged:true` | **2** | yes |
| `bbnfix_when_ready_all.sh` | exits when book refuses | **2** | via book |

---

## What is bookable after gate (ordered)

| Step | Output | Bookable as |
|------|--------|-------------|
| A | finalize H₀ sentence | letter draft (prefer GetDist for public σ) |
| B | `book_bbnfix_when_ready.py` REPORT + booking.json | H₀ / Σm_ν / ω_b / S8 three-rank marginals |
| B′ | `make_getdist_tables.py --include-bbnfix` | rank-1 tables + triangles (restore banner) |
| C.1 | `bbnfix_delta_chi2_proxy.py` | **proxy only** — Δ(min −logpost); not Laplace ΔlnZ |
| C.2 | CosmicForge Hessian `log_z_laplace` model − ΛCDM | bookable ΔlnZ **if** run under BBN-fixed yamls after stop |

---

## Explicit non-actions

- Do not invent `scripts/laplace_bbnfix.py` Hessian CLI in this package.  
- Do not kill `dyad_mnu_bbnfix` / `cmp_lcdm_mnu_bbnfix` / `cmp_prtoe_routeD` for booking prep.  
- Do not quote 68% while R−1 ≥ stop.  
- Do not use progress `acceptance_rate` as R−1.  
- Do not promote pre-bbnfix ΔlnZ ≈ +2.6 under the BBN-fixed stack.  
- Do not run PolyChord for booking.

---

## Definition of done (package)

Owner can open **`RUNBOOK.md`** and execute without inventing steps.  
Owner can open **`PREFLIGHT.md`** and tick boxes before the one-shot.  
Until gate opens, all entrypoints **refuse** with exit 2.

---

## Force-bbnfix status check (batch-1 residual cure; 2026-08-04)

**Do not start a new long `--force-bbnfix` run** for “results”; force path is
**UNBOOKABLE only**. Living shelf must stay free of force peeks.

| check | status |
|---|---|
| Code: `--force-bbnfix` never writes living `docs/PRTOE_CHAIN_TABLES.md` | **CURED in source** (`scripts/make_getdist_tables.py` ~L106–228: `unbookable_force` → `getdist_force_UNBOOKABLE_<stamp>/CHAIN_TABLES_UNCONVERGED.md` with UNCONVERGED banner; living path only on bookable gate) |
| Living shelf `docs/PRTOE_CHAIN_TABLES.md` | **UNTOUCHED** by force path this stamp — still carries OPEN-MACHINE residual freeze (2026-08-04); no clean force numbers on shelf |
| `docs/working_logs/_runs/getdist_force_UNBOOKABLE_*` | **PASS artifact present** → [`../getdist_force_UNBOOKABLE_20260804_030942/CHAIN_TABLES_UNCONVERGED.md`](../getdist_force_UNBOOKABLE_20260804_030942/CHAIN_TABLES_UNCONVERGED.md) (in-file UNCONVERGED / UNBOOKABLE banner) |
| Package log `smoke_force_bbnfix.txt` | **COMPLETE** — ends with `tables → …/getdist_force_UNBOOKABLE_20260804_030942/…` and `living shelf PRTOE_CHAIN_TABLES.md left UNTOUCHED` |
| Force smoke overall | **PASS** (UNBOOKABLE path only) — **do not quote force peek as results**; not a booking |

*NO FABRICATIONS. NO EARLY BOOK. NO FORCE PEEK AS BOOKING.*
