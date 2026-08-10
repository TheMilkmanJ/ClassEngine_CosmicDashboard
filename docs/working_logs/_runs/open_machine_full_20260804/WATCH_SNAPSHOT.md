# OPEN-MACHINE watch snapshot — 2026-08-04T02:40 local

**Rules:** read-only. No MCMC kill. No PolyChord. No peek-book H₀.  
**Sources:** `chains/*.progress`, checkpoints, chain `.txt` mtimes,  
`python3 scripts/book_bbnfix_when_ready.py`, `python3 scripts/bbnfix_mcmc_watch_diag.py`.

Raw captures in this package: `book_gate_live.txt`, `watch_diag_live.txt`.  
Gate refuse card: `docs/working_logs/_runs/bbnfix_booking_20260804_084008/`.

### Currency note (machine_watch_hygiene_20260804 — no new R−1)

Progress tails re-read later same calendar day: **unchanged** vs this snapshot  
(lcdm **0.059055** N=19013; dyad **0.189201** N=18837; routeD **102.794555** N=1609;  
both bbnfix `converged: false`). Latest refuse card with identical inputs:  
`docs/working_logs/_runs/bbnfix_booking_20260804_091234/` (**REFUSED**, exit 2).  
Hygiene package: `docs/working_logs/_runs/machine_watch_hygiene_20260804/REPORT.md`.  
**Do not invent fresher R−1** until cobaya writes a new progress row.

---

## Quote (authority)

| fact | value |
|---|---|
| lcdm progress R−1 | **~0.059** (exact **0.059055**, N=19013) |
| dyad progress R−1 | **~0.189** (exact **0.189201**, N=18837) |
| self-stop | **false** both bbnfix legs |
| bookable | **NO** |
| GetDist offline max GR (`ignore_rows=0.3`) | lcdm **~0.07** (0.0721); dyad **~0.086** (0.0857) — **diagnostic only** |

Gate authority is progress R−1 **< 0.05** *and* checkpoint **`converged: true`** on **both** bbnfix legs, then `scripts/book_bbnfix_when_ready.py`. Diagnostic GetDist GR never books.

---

## Progress tails (cobaya authority)

| chain | N (progress) | timestamp (progress) | R−1 | stop | converged |
|---|---:|---|---:|---:|---|
| `dyad_mnu_bbnfix` | 18837 | 2026-08-03T17:57:59 | **0.189201** | 0.05 | **false** |
| `cmp_lcdm_mnu_bbnfix` | 19013 | 2026-08-03T21:05:36 | **0.059055** | 0.05 | **false** |
| `cmp_prtoe_routeD` | 1609 | 2026-08-03T20:53:57 | **102.794555** | 0.1 | **false** |

**lcdm history note:** progress once showed R−1 = 0.048827 at N=17458 (2026-08-03T14:21) then rose to 0.059055. Temporary R−1 < 0.05 without self-stop is **not** bookable.

---

## Offline diagnostics (UNBOOKABLE)

From `bbnfix_mcmc_watch_diag.py` stamp **2026-08-04T02:40:09**:

| measure | dyad | lcdm twin |
|---|---:|---:|
| crude max-param R−1 (burn 50%) | 0.0344 | 0.0203 |
| GetDist max GR (`ignore_rows=0.3`) | **0.085714** | **0.072109** |
| bookable_leg | False | False |

Crude param R−1 is optimistically low; GetDist GR is the better offline proxy; both still **> 0.05**. Neither replaces cobaya self-stop.

---

## Live chain growth (progress lag is normal)

| chain | rank rows (approx) | latest `.txt` mtime |
|---|---|---|
| dyad | 6752 / 6698 / 6785 | ~2026-08-04T02:38 |
| lcdm | 6718 / 6707 / 6576 | ~2026-08-04T02:37 |
| routeD | ~759 / 849 / 810 | ~2026-08-04T02:37 |

Progress/checkpoint files **lag** chain `.txt` growth until cobaya’s next R−1 write — expected; **not** a license to book.

---

## Process health (do not kill)

Confirmed running at snapshot:

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
→ wrote docs/working_logs/_runs/bbnfix_booking_20260804_084008/
```

Later same-day reconfirm (progress tails still identical):  
`docs/working_logs/_runs/bbnfix_booking_20260804_091234/` — **REFUSED** exit 2.

**Verdict:** leave cobaya alone until both bbnfix legs self-stop with R−1 < 0.05, then re-run the booking script only.

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀.*
