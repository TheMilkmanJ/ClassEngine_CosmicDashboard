# EDITS — OPEN-MACHINE full residual freeze (2026-08-04)

**Rule:** NO FABRICATIONS · no MCMC kill · no PolyChord · no peek-book H₀ · no invented numbers.

This pass finished the residual-freeze mission on all eight OPEN-MACHINE shelf files, refreshed the chain-tables banner from live progress + booking gate, touched inventory one-liners, and wrote this package.

---

## Package dir (new)

| path | purpose |
|---|---|
| `docs/working_logs/_runs/open_machine_full_20260804/REPORT.md` | mission report |
| `docs/working_logs/_runs/open_machine_full_20260804/EDITS.md` | this list |
| `docs/working_logs/_runs/open_machine_full_20260804/WATCH_SNAPSHOT.md` | live chain + gate snapshot |
| `docs/working_logs/_runs/open_machine_full_20260804/book_gate_live.txt` | stdout of `book_bbnfix_when_ready.py` (REFUSED) |
| `docs/working_logs/_runs/open_machine_full_20260804/watch_diag_live.txt` | stdout of `bbnfix_mcmc_watch_diag.py` (UNBOOKABLE) |

Side-effect of the read-only gate script (expected refuse card, not a booking):

- `docs/working_logs/_runs/bbnfix_booking_20260804_084008/REPORT.md`
- `docs/working_logs/_runs/bbnfix_booking_20260804_084008/booking.json`

---

## Shelf files — residual freeze content

Each of the eight OPEN-MACHINE shelves carries a **2026-08-04** freeze with:

1. **Machine residual** (what is waiting on chains/sims)  
2. **What unblocks** (owner/machine condition)  
3. **Forbidden claims**  
4. Claims ledger dated **2026-08-04 residual freeze** (where applicable)

| file | freeze content | this pass action |
|---|---|---|
| `docs/PRTOE_CHAIN_TABLES.md` | Full live triple table + gate + GetDist diag fence + forbidden | **Banner refreshed** to stamp 02:40 from progress/checkpoint/diag; explicit quote lcdm~0.059 / dyad~0.189 / not self-stopped / NOT bookable; GetDist ~0.07/~0.086 diagnostic only |
| `docs/PRTOE_s8_growth.md` | Banner + ledger: conv_desi unproduced; lensing OPEN; routeD early ≠ substitute | Verified complete (prior partial + this pass) |
| `docs/PRTOE_s8_tension.md` | Banner + ledger: same instrument debt | Verified complete |
| `docs/PRTOE_neutrino_home.md` | Banner + ledger: joint Σm_ν waits bbnfix gate; numbers from progress | Verified complete |
| `docs/PRTOE_galactic_atoms.md` | Banner + ledger: α_c→r_1s blocked on zon_disp | Verified complete |
| `docs/PRTOE_smbh_atoms.md` | Banner + ledger: α_g chain-gated; NewAthena WATCH | Verified complete |
| `docs/PRTOE_quartet_clock.md` | Banner + ledger: zon_disp not running R−1=17.81 | Verified complete |
| `docs/PRTOE_granule_scoping.md` | Banner + ledger: SP campaign not started | Verified complete |

Numbers on freezes are **only** from:

- `chains/dyad_mnu_bbnfix.progress` → R−1=0.189201  
- `chains/cmp_lcdm_mnu_bbnfix.progress` → R−1=0.059055  
- `chains/cmp_prtoe_routeD.progress` → R−1=102.794555  
- `chains/cmp_prtoe_conv_desi.progress` → R−1=13.25  
- `chains/cmp_prtoe_zon_disp.progress` → R−1=17.81  
- checkpoints `sampler.mcmc.converged = False`  
- diag GetDist GR 0.085714 / 0.072109  

No invented H₀, Σm_ν, S₈, or α_c posteriors.

---

## Inventory touch

| file | edit |
|---|---|
| `docs/working_logs/_FILE_COMPLETION_STATUS.md` | One-line evidence for all **8** OPEN-MACHINE rows restamped with 2026-08-04 freeze language (CHAIN_TABLES includes GetDist diag ~0.086/~0.07 + NOT bookable) |

Status tags **unchanged** (all remain OPEN-MACHINE). Counts unchanged (OPEN-MACHINE = 8).

---

## Not edited (by design)

- Live MCMCs / `chains/*.txt` (left running)  
- PolyChord configs or launches  
- Any booked H₀ / Σm_ν / S₈ tables  
- OPEN-THEORY shelves (out of scope)  
- Physics content beyond residual-freeze honesty banners/ledgers  

---

## Scripts run (read-only)

| command | result |
|---|---|
| `python3 scripts/book_bbnfix_when_ready.py` | **REFUSED** (exit 2) |
| `python3 scripts/bbnfix_mcmc_watch_diag.py` | **UNBOOKABLE** (GetDist GR printed; not booked) |
