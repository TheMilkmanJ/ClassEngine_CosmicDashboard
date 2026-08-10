# EDITS — live machine surfaces currency (2026-08-04)

**Rule:** NO FABRICATIONS · leave MCMCs alone · no PolyChord · no peek-book H₀ · no invented posteriors.

This pass fully restamped the three living “where is the machine” surfaces to the same
gate truth as `docs/PRTOE_CHAIN_TABLES.md` residual freeze (2026-08-04), and wrote this package.

---

## Package dir (new)

| path | purpose |
|---|---|
| `docs/working_logs/_runs/live_surfaces_full_20260804/REPORT.md` | mission report |
| `docs/working_logs/_runs/live_surfaces_full_20260804/EDITS.md` | this list |
| `docs/working_logs/_runs/live_surfaces_full_20260804/GATE_SNAPSHOT.md` | full gate snapshot |
| `docs/working_logs/_runs/live_surfaces_full_20260804/progress_raw.txt` | progress / checkpoint / row counts |
| `docs/working_logs/_runs/live_surfaces_full_20260804/watch_diag_live.txt` | `bbnfix_mcmc_watch_diag.py` stdout |
| `docs/working_logs/_runs/live_surfaces_full_20260804/book_gate_live.txt` | `book_bbnfix_when_ready.py` stdout (REFUSED) |

Side-effect of the read-only booking gate (expected refuse card, not a booking):

- `docs/working_logs/_runs/bbnfix_booking_20260804_084239/REPORT.md`
- `docs/working_logs/_runs/bbnfix_booking_20260804_084239/booking.json`

---

## Living surfaces edited (full updates, not one-line)

### 1. `docs/PRTOE_CODE_MANIFEST.md`

| edit | detail |
|---|---|
| §1 live production stamp | New **2026-08-04** block: triple table (dyad 0.189201 / lcdm 0.059055 / routeD 102.79), bookable **NO**, GetDist diag fence, lcdm temporary-dip note, PolyChord off |
| dyad row | **Live (2026-08-04)** — N=18837, R−1=0.189201, converged false, oversampled accept note, chain growth note, bookable NO |
| lcdm twin row | **Live (2026-08-04)** — N=19013, R−1=0.059055, closest (~1.18×), not self-stopped, bookable NO |
| routeD row | **Live (2026-08-04)** — N=1609, R−1=102.79, raw accept ~5.6%, early, not bookable |
| PolyChord sampled-ε row | Explicit **PolyChord off (2026-08-04 stamp)** |
| zon_disp / conv_desi row | **not running (2026-08-04)** with last R−1 17.81 / 13.25 |

**Removed as current:** 2026-08-02 R−1 ≈ 0.19 / 0.14 / 129 and N ≈ 14544 / 13193 / 1593.

### 2. `docs/PRTOE_REFEREE_CALENDAR.md`

| edit | detail |
|---|---|
| Sitting now banner | **Live read 2026-08-04** + authority table + book REFUSED path + PolyChord off |
| dyad Sitting NOW row | R−1=0.189201 at N=18837; not bookable; gate rule restated |
| lcdm Sitting NOW row | R−1=0.059055 at N=19013; temporary 0.048827 note; not bookable |
| routeD Sitting NOW row | R−1=102.79 at N=1609; raw accept ~5.6%; not bookable; separate instrument |
| nested referee ETA | **PolyChord off (2026-08-04 stamp)** |
| zon_disp / conv_desi ETA | stamped 2026-08-04 parked / unproduced |
| historical notes | “as of 2026-08-02” → 2026-08-04 where they described present live state |

**Removed as current:** Sitting NOW R−1 = 0.192 / 0.141 / 129.1 (2026-08-02 progress rows).

### 3. `docs/PRTOE_honest_status.md`

| edit | detail |
|---|---|
| New **CURRENT (2026-08-04)** section | Inserted at top after header notes, before former CURRENT (2026-07-31) |
| expansion fence | Theory of Expansion, not TOE |
| bbnfix NOT bookable | triple gate table lcdm 0.059 / dyad 0.189 / routeD 102.79 |
| BBN ε ARITHMETIC VERIFIED (internal) | 3.196% ≈ 3.20% PASS (reverify 2026-08-04); EXTERNAL WIN PENDING (no DOI) |
| Page near-miss freeze | v13 T8 fail; page_curve_claimed false; D4 freeze |
| Strong CP abstention | constitutional silence stands |
| PolyChord off | Laplace grades until cluster time |
| demote prior CURRENT | retitled **CURRENT (2026-07-31) — retained (E2E board detail)** |
| snapshot operational line | 2026-08-02 routeD burn-in language → 2026-08-04 gate numbers |

---

## Numbers used (sources only)

| source | value |
|---|---|
| `chains/dyad_mnu_bbnfix.progress` last row | R−1=**0.189201**, N=18837 |
| `chains/cmp_lcdm_mnu_bbnfix.progress` last row | R−1=**0.059055**, N=19013 |
| `chains/cmp_prtoe_routeD.progress` last row | R−1=**102.794555**, N=1609 |
| checkpoints | all three `converged: false` |
| `bbnfix_mcmc_watch_diag.py` | GetDist GR ~0.086 / ~0.07; bookable_leg False |
| `book_bbnfix_when_ready.py` | **REFUSED** exit 2 |
| `PRTOE_CHAIN_TABLES.md` | residual freeze already 2026-08-04 (read, not re-edited this pass) |
| BBN ε reverify | 3.196% ≈ 3.20% (prior `BBN_EPS_REVERIFY_20260804.md` / physics_improve parent gate) |
| Page freeze | `page_full_freeze_20260804/` champion v13 T8 fail |

No invented H₀, Σm_ν, S₈, or booked posteriors.

---

## Not edited (by design)

- Live MCMCs / `chains/*.txt` (left running)  
- PolyChord configs or launches  
- `docs/PRTOE_CHAIN_TABLES.md` (already residual-frozen 2026-08-04; authority source)  
- Any GetDist H₀ / Σm_ν tables  
- OPEN-MACHINE residual freezes already done by `open_machine_full_20260804`  

---

## Scripts run (read-only)

| command | result |
|---|---|
| `python3 scripts/bbnfix_mcmc_watch_diag.py` | **UNBOOKABLE** (GetDist GR printed; not booked) |
| `python3 scripts/book_bbnfix_when_ready.py` | **REFUSED** (exit 2) |

*NO FABRICATIONS.*
