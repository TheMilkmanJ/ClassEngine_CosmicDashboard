# bbnfix GetDist booking — 20260804_060351

**Generated (UTC):** 2026-08-04T06:03:51.281936+00:00
**Script:** `scripts/book_bbnfix_when_ready.py`
**Gate:** both of {dyad_mnu_bbnfix, cmp_lcdm_mnu_bbnfix} with R−1 **< 0.05** **AND** `converged: true` (self-stop) — both legs required
**Result:** REFUSED
**Exit code:** 2

## Progress + self-stop gate

| chain | present | N | timestamp | R−1 | converged | ready |
|---|---|---:|---|---:|---|---|
| `dyad_mnu_bbnfix` | YES | 18837.0 | 2026-08-03T17:57:59.890097 | 0.189201 | false | NO |
| `cmp_lcdm_mnu_bbnfix` | YES | 19013.0 | 2026-08-03T21:05:36.968557 | 0.059055 | false | NO |

### Gate messages

- dyad_mnu_bbnfix: R−1 = 0.189201 >= 0.05 (N=18837.0, t=2026-08-03T17:57:59.890097) — NOT READY
- dyad_mnu_bbnfix: checkpoint converged: false — NOT READY (self-stop required)
- cmp_lcdm_mnu_bbnfix: R−1 = 0.059055 >= 0.05 (N=19013.0, t=2026-08-03T21:05:36.968557) — NOT READY
- cmp_lcdm_mnu_bbnfix: checkpoint converged: false — NOT READY (self-stop required)

## Rank files

- `dyad_mnu_bbnfix`: 3 files
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.1.txt`
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.2.txt`
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.3.txt`
- `cmp_lcdm_mnu_bbnfix`: 3 files
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.1.txt`
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.2.txt`
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.3.txt`

## Booking status

**REFUSED.** Do not quote H₀ / Σm_ν / Ω_b h² / S8 as bookable posteriors while either chain has R−1 ≥ 0.05, missing progress, or has not self-stopped (`converged: true`).

Re-run when both progress tails show R−1 < 0.05 **and** both checkpoints have `converged: true`:

```bash
python3 scripts/book_bbnfix_when_ready.py
```

See also: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`,
`scripts/finalize_h0_at_convergence.py`,
`docs/working_logs/_runs/hard_win1_bbnfix_booking_prep_20260803/`.

