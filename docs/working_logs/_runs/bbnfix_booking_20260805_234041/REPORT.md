# bbnfix GetDist booking — 20260805_234041

**Generated (UTC):** 2026-08-05T23:40:41.265315+00:00
**Script:** `scripts/book_bbnfix_when_ready.py`
**Gate:** both of {dyad_mnu_bbnfix, cmp_lcdm_mnu_bbnfix} with R−1 **< 0.05** **AND** `converged: true` (self-stop) — both legs required
**Result:** REFUSED
**Exit code:** 2

## Progress + self-stop gate

| chain | present | N | timestamp | R−1 | converged | ready |
|---|---|---:|---|---:|---|---|
| `dyad_mnu_bbnfix` | YES | 26135.0 | 2026-08-05T15:50:02.745947 | 0.060201 | false | NO |
| `cmp_lcdm_mnu_bbnfix` | YES | 26294.0 | 2026-08-05T11:52:10.194879 | 0.049324 | true | YES |

### Gate messages

- dyad_mnu_bbnfix: R−1 = 0.060201 >= 0.05 (N=26135.0, t=2026-08-05T15:50:02.745947) — NOT READY
- dyad_mnu_bbnfix: checkpoint converged: false — NOT READY (self-stop required)
- dyad_mnu_bbnfix: checkpoint Rminus1_last=0.060201 (informational; gate uses progress R−1)
- cmp_lcdm_mnu_bbnfix: R−1 = 0.049324 < 0.05 (N=26294.0) — R−1 GRADED
- cmp_lcdm_mnu_bbnfix: checkpoint converged: true — self-stop OK
- cmp_lcdm_mnu_bbnfix: checkpoint Rminus1_last=0.049324 (informational; gate uses progress R−1)

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

Also blocked while gate closed: living `PRTOE_CHAIN_TABLES.md` writes,
bookable Laplace ΔlnZ under the BBN-fixed stack, and promotion of
pre-bbnfix ΔlnZ ≈ +2.6 as if it were this pair's result.

Publish split (when gate later opens): **Stage A** = book + finalize only;
**Stage B** = tables only after `RED_AUDIT.md` (`red: AGREE` / `AGREE-IF`).

Re-run when both progress tails show R−1 < 0.05 **and** both checkpoints have `converged: true`:

```bash
python3 scripts/book_bbnfix_when_ready.py
# preferred one-shot Stage A: bash scripts/bbnfix_when_ready_all.sh
```

See also: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`,
`scripts/finalize_h0_at_convergence.py`,
`docs/working_logs/_runs/laplace_booking_full_20260804/`,
`docs/working_logs/_runs/laplace_prep_harden_20260804/`.

