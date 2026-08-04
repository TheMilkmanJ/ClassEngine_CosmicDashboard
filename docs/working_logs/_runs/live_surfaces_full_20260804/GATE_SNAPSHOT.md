# GATE_SNAPSHOT — live machine surfaces currency — 2026-08-04

**Rules:** read-only gate read. No MCMC kill. No PolyChord. No peek-book H₀.  
**Local stamp:** 2026-08-04T02:42–02:45 (America/Denver; `date -Iseconds` ≈ 2026-08-04T02:42:59-06:00).

Raw captures in this package:

- `progress_raw.txt` — progress tails, checkpoints, chain row counts / mtimes  
- `watch_diag_live.txt` — stdout of `python3 scripts/bbnfix_mcmc_watch_diag.py`  
- `book_gate_live.txt` — stdout of `python3 scripts/book_bbnfix_when_ready.py` (**REFUSED**, exit 2)

Gate refuse card (side-effect of the booking script, not a booking):

- `docs/working_logs/_runs/bbnfix_booking_20260804_084239/REPORT.md`  
- `docs/working_logs/_runs/bbnfix_booking_20260804_084239/booking.json`

Authority match: `docs/PRTOE_CHAIN_TABLES.md` residual freeze (OPEN-MACHINE, stamp 2026-08-04).

---

## Authority quote

| fact | value |
|---|---|
| lcdm progress R−1 | **0.059055** (N=19013, t=2026-08-03T21:05:36) |
| dyad progress R−1 | **0.189201** (N=18837, t=2026-08-03T17:57:59) |
| routeD progress R−1 | **102.794555** (N=1609, t=2026-08-03T20:53:57) |
| self-stop (bbnfix both) | **false** |
| bookable | **NO** |
| GetDist offline max GR (`ignore_rows=0.3`) | lcdm **0.072425** (~0.07); dyad **0.085622** (~0.086) — **diagnostic only** |
| crude max-param R−1 (burn 50%) | lcdm 0.0204; dyad 0.0344 — **not** cobaya; **not** bookable |
| PolyChord | **off** (not running) |

Gate authority = progress R−1 **< 0.05** *and* checkpoint **`converged: true`** on **both** bbnfix legs, then `scripts/book_bbnfix_when_ready.py` only. Temporary R−1 < 0.05 without self-stop is **not** bookable (lcdm once hit 0.048827 at N=17458 then rose).

---

## Progress tails (cobaya authority)

| chain | N (progress) | timestamp (progress) | acceptance_rate (oversampled) | R−1 | stop | converged |
|---|---:|---|---:|---:|---:|---|
| `dyad_mnu_bbnfix` | 18837 | 2026-08-03T17:57:59 | 0.99672 | **0.189201** | 0.05 | **false** |
| `cmp_lcdm_mnu_bbnfix` | 19013 | 2026-08-03T21:05:36 | 0.983857 | **0.059055** | 0.05 | **false** |
| `cmp_prtoe_routeD` | 1609 | 2026-08-03T20:53:57 | 1.0 | **102.794555** | 0.1 | **false** |

### Last progress rows (verbatim)

**dyad_mnu_bbnfix** (last five):

```
13072.000000 2026-08-01T21:32:26.865951  0.996039  0.259021 NaN
14544.000000 2026-08-02T15:41:03.442384  0.996438  0.191848 NaN
15969.000000 2026-08-03T02:35:30.101631  0.99663  0.19103 NaN
17384.000000 2026-08-03T09:32:30.354800  0.996446  0.159888 NaN
18837.000000 2026-08-03T17:57:59.890097  0.99672  0.189201 NaN
```

**cmp_lcdm_mnu_bbnfix** (last five):

```
13193.000000 2026-08-02T19:00:03.737574  0.984491  0.140949 NaN
14675.000000 2026-08-03T02:48:30.957531  0.983923  0.093682 NaN
16075.000000 2026-08-03T07:49:13.988426  0.985174  0.053867 NaN
17458.000000 2026-08-03T14:21:54.839631  0.984884  0.048827 NaN
19013.000000 2026-08-03T21:05:36.968557  0.983857  0.059055 NaN
```

**cmp_prtoe_routeD** (only data row):

```
1609.000000 2026-08-03T20:53:57.575011  1.0  102.794555 NaN
```

---

## Checkpoints (verbatim fields)

| chain | converged | Rminus1_last | mpi_size | file mtime |
|---|---|---:|---:|---|
| `dyad_mnu_bbnfix` | **false** | 0.18920075919140164 | 3 | 2026-08-03T17:57 |
| `cmp_lcdm_mnu_bbnfix` | **false** | 0.05905511181721022 | 3 | 2026-08-03T21:05 |
| `cmp_prtoe_routeD` | **false** | 102.79455471855752 | 3 | 2026-08-03T20:53 |

---

## Offline diagnostics (UNBOOKABLE)

From `bbnfix_mcmc_watch_diag.py` stamp **2026-08-04T02:42:19** (re-run to package ~02:45):

| measure | dyad | lcdm twin |
|---|---:|---:|
| crude max-param R−1 (burn 50%) | 0.0344 | 0.0204 |
| GetDist max GR (`ignore_rows=0.3`) | **0.085622** | **0.072425** |
| bookable_leg | False | False |

Script ends: **REFUSE booking from this script. Use: `python3 scripts/book_bbnfix_when_ready.py`.**

---

## Live chain growth (progress lag is normal)

| chain | rank rows (wc -l) | latest `.txt` mtime (approx) |
|---|---|---|
| dyad | 6753 / 6700 / 6788 | 2026-08-04 02:38–02:42 |
| lcdm | 6720 / 6708 / 6579 | 2026-08-04 02:34–02:42 |
| routeD | 760 / 850 / 814 | 2026-08-04 02:40–02:41 |

Progress/checkpoint files **lag** chain `.txt` growth until cobaya’s next R−1 write — expected; **not** a license to book.

Route-D raw accept from live launchlog (~02:40–02:41): accepted/steps ≈ 759/13518, 849/14894, 813/14399 → **~5.6%** (healthy high-d Metropolis). Progress accept 1.0 is oversampled.

---

## Process health (do not kill)

Confirmed running at snapshot (`ps`):

- `mpirun -n 3 … cobaya.run -r dyad_mnu_bbnfix.input.yaml` (3 ranks)  
- `mpirun -n 3 … cobaya.run -r cmp_lcdm_mnu_bbnfix.input.yaml` (3 ranks)  
- `mpirun -n 3 … cobaya.run cmp_prtoe_routeD.input.yaml` (3 ranks)  

**PolyChord:** not running (not started by this pass).

---

## Archive / dead instruments (not live)

| chain | last progress R−1 | live? |
|---|---:|---|
| `cmp_prtoe_conv_desi` | **13.25** (N=3744, 2026-07-22) | **no** — unproduced; owner restart |
| `cmp_prtoe_zon_disp` | **17.81** (N=3456, 2026-07-22) | **no** — collapsed; seed ready |
| `cmp_prtoe_zon` | **40.36** | **no** — stopped since 07-12 |

---

## Booking gate result

```
python3 scripts/book_bbnfix_when_ready.py
→ REFUSED (exit 2)
→ dyad: R−1 = 0.189201 >= 0.05; converged: false
→ lcdm: R−1 = 0.059055 >= 0.05; converged: false
→ wrote docs/working_logs/_runs/bbnfix_booking_20260804_084239/
```

**Verdict:** leave cobaya alone until both bbnfix legs self-stop with R−1 < 0.05, then re-run the booking script only. No peek-book H₀. No GetDist posterior insert.

---

## Surface agreement (definition of done)

| surface | stamp | lcdm R−1 | dyad R−1 | routeD R−1 | bookable |
|---|---|---:|---:|---:|---|
| `PRTOE_CHAIN_TABLES.md` residual freeze | 2026-08-04 | 0.059055 | 0.189201 | 102.79 | **NO** |
| `PRTOE_CODE_MANIFEST.md` §1 live stamp | 2026-08-04 | 0.059055 | 0.189201 | 102.79 | **NO** |
| `PRTOE_REFEREE_CALENDAR.md` Sitting NOW | 2026-08-04 | 0.059055 | 0.189201 | 102.79 | **NO** |
| `PRTOE_honest_status.md` CURRENT | 2026-08-04 | 0.059055 | 0.189201 | 102.79 | **NO** |

No 2026-08-02 R−1 numbers remain as “current” on those three living surfaces.

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀.*
