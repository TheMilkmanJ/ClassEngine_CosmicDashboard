# bbnfix GetDist booking — 20260803_162329

**Generated (UTC):** 2026-08-03T16:23:29.840807+00:00
**Script:** `scripts/book_bbnfix_when_ready.py`
**Gate:** both of {dyad_mnu_bbnfix, cmp_lcdm_mnu_bbnfix} with R−1 **< 0.05**
**Result:** REFUSED
**Exit code:** 2

## Progress gate

| chain | present | N | timestamp | R−1 | ready |
|---|---|---:|---|---:|---|
| `dyad_mnu_bbnfix` | YES | 17384.0 | 2026-08-03T09:32:30.354800 | 0.159888 | NO |
| `cmp_lcdm_mnu_bbnfix` | YES | 16075.0 | 2026-08-03T07:49:13.988426 | 0.053867 | NO |

### Gate messages

- dyad_mnu_bbnfix: R−1 = 0.159888 >= 0.05 (N=17384.0, t=2026-08-03T09:32:30.354800) — NOT READY
- cmp_lcdm_mnu_bbnfix: R−1 = 0.053867 >= 0.05 (N=16075.0, t=2026-08-03T07:49:13.988426) — NOT READY

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

**REFUSED.** Do not quote H₀ / Σm_ν / Ω_b h² / S8 as bookable posteriors while either chain has R−1 ≥ 0.05 or missing progress.

Re-run when both progress tails show R−1 < 0.05:

```bash
python3 scripts/book_bbnfix_when_ready.py
```

See also: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`,
`scripts/finalize_h0_at_convergence.py`,
`docs/working_logs/_runs/hard_win1_bbnfix_booking_prep_20260803/`.

