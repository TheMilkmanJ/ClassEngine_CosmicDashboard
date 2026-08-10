# PREFLIGHT — bbnfix + Laplace booking (tick before one-shot)

**Package:** `docs/working_logs/_runs/laplace_booking_full_20260804/`  
**Gate (both required):** R−1 **< 0.05** on both chains **AND** `converged: true`.  
**Do not book while over bar. Do not peek-quote H₀. Do not GetDist a moving chain.**

---

## A. Live status (fill at booking time)

| check | box | evidence |
|-------|:---:|----------|
| `dyad_mnu_bbnfix` progress R−1 **< 0.05** | ☐ | `tail -1 chains/dyad_mnu_bbnfix.progress` field 4 = ______ |
| `cmp_lcdm_mnu_bbnfix` progress R−1 **< 0.05** | ☐ | `tail -1 chains/cmp_lcdm_mnu_bbnfix.progress` field 4 = ______ |
| `dyad_mnu_bbnfix` `converged: true` | ☐ | checkpoint grep |
| `cmp_lcdm_mnu_bbnfix` `converged: true` | ☐ | checkpoint grep |
| Ranks `.1 .2 .3` exist for both | ☐ | `ls chains/*bbnfix.[123].txt` |
| Chains idle (no active rank writers) | ☐ | `ps` / cobaya idle |
| CWD = repo root | ☐ | `pwd` → `/home/themilkmanj/prtoe_class` |
| Env: getdist, numpy, classy stack | ☐ | same stack as last samples |

**Prep stamp (2026-08-04 — gate CLOSED):** dyad R−1=0.189 / lcdm R−1=0.059 / both not-stopped.

---

## B. Instruments present

| check | box | path |
|-------|:---:|------|
| Booking entrypoint | ☐ | `scripts/book_bbnfix_when_ready.py` |
| H₀ letter gate | ☐ | `scripts/finalize_h0_at_convergence.py` |
| GetDist tables | ☐ | `scripts/make_getdist_tables.py` |
| Δχ² proxy | ☐ | `scripts/bbnfix_delta_chi2_proxy.py` |
| One-shot shell | ☐ | `scripts/bbnfix_when_ready_all.sh` |
| Checklist | ☐ | `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` |
| Laplace prep | ☐ | `_runs/open_board_split_20260803/LAPLACE_PREP.md` |
| This RUNBOOK | ☐ | `_runs/laplace_booking_full_20260804/RUNBOOK.md` |
| CosmicForge CLI reachable | ☐ | `python3 run_cosmicforge.py --help` |
| Yamls for CF path | ☐ | `dyad_mnu_bbnfix.yaml`, `cmp_lcdm_mnu_bbnfix.yaml` |

---

## C. Refuse-path smoke (safe anytime, ≪2 min)

| check | box | expected |
|-------|:---:|----------|
| Book refuses while over bar | ☐ | `python3 scripts/book_bbnfix_when_ready.py` → **REFUSED** exit 2 |
| Finalize refuses | ☐ | `python3 scripts/finalize_h0_at_convergence.py` → **NOT YET** exit 2 |
| Tables refuse with flag | ☐ | `python3 scripts/make_getdist_tables.py --include-bbnfix` → **NOT READY** exit 2 |
| Delta refuses | ☐ | `python3 scripts/bbnfix_delta_chi2_proxy.py` → **REFUSED** exit 2 |
| All-shell refuses | ☐ | `bash scripts/bbnfix_when_ready_all.sh` → exit 2 before finalize/tables |

If any of the above **books** while R−1 ≥ 0.05 or not self-stopped → **STOP** (process kill).

---

## D. When gate opens — execution order (Stage A then Stage B)

| # | stage | step | box | command / note |
|---|-------|------|:---:|----------------|
| 1 | A | Reconfirm gate | ☐ | progress + checkpoint both OK; idle |
| 2 | A | One-shot Stage A | ☐ | `bash scripts/bbnfix_when_ready_all.sh` (**tables default OFF**) |
| 3 | A | Book card written | ☐ | `_runs/bbnfix_booking_<stamp>/REPORT.md` |
| 4 | A | Letter H₀ sentence captured | ☐ | finalize stdout → paste later (prefer after red if publishing) |
| 5 | A | Δχ² proxy labeled | ☐ | **proxy only** — not Laplace ΔlnZ |
| 6 | red | Claude red audit | ☐ | write `RED_AUDIT.md` with `red: AGREE` or `red: AGREE-IF` |
| 7 | B | Tables publish | ☐ | `bash scripts/bbnfix_when_ready_all.sh --write-tables` only; restore banner if clobbered |
| 8 | C | CosmicForge Laplace (optional) | ☐ | only if capacity after stop; no PolyChord; BBN-fixed yamls |
| 9 | — | Living docs sync | ☐ | snapshot, calendar, manifest, T11 |
| 10 | — | Letter HOLD #1 | ☐ | owner manual paste |

**booking ≠ publishing:** Stage A success does **not** authorize forward `PRTOE_CHAIN_TABLES.md` rows.

---

## E. Kill criteria (do not tick “done” if any apply)

| # | anti-pattern | box if violated |
|---|--------------|:---------------:|
| K1 | Book while either R−1 ≥ 0.05 | ☐ kill |
| K2 | Book before both self-stop | ☐ kill |
| K3 | PolyChord / nested for booking | ☐ kill |
| K4 | Kill live chains to free CPU without owner order | ☐ kill |
| K5 | Promote pre-bbnfix ΔlnZ ≈ +2.6 as final bbnfix evidence without fence | ☐ kill |
| K6 | Quote rank-1-only as production when three ranks exist (prefer book card) | ☐ incomplete |
| K7 | RouteD substitute for letter pair | ☐ wrong object |
| K8 | Peek-book with `--force-bbnfix` / `--force-peek` as bookable | ☐ kill |
| K9 | Treat force peek as living `PRTOE_CHAIN_TABLES.md` | ☐ kill — force path must only write `getdist_force_UNBOOKABLE_*` |
| K10 | Stage B tables without RED_AUDIT (except owner `--force-tables`) | ☐ kill |
| K11 | Invent a Laplace number / invent `scripts/laplace_bbnfix.py` | ☐ kill |

---

## F. Honesty on missing pieces

| item | status |
|------|--------|
| Full cobaya-pair Hessian CLI (`scripts/laplace_bbnfix.py`) | **MISSING** — intentional; do not invent |
| Bookable ΔlnZ under BBN-fixed stack | **BLOCKED** until gate + C.2 (or C.1 with proxy label) |
| Bridge sampling default | **no** — library only |

---

## Sign-off

| role | name | date | gate open? |
|------|------|------|------------|
| Runner | | | yes / no |
| Owner (letter paste) | | | HOLD until Fairbank path |

*NO FABRICATIONS. NO EARLY BOOK. NO POLYCHORD.*
