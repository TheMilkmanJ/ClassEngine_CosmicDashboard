# Booking pipeline red gate cure — 2026-08-04

**Claude RED FINDING booking-pipeline:** gate robust (20/20 refusals); post-gate path skipped red audit before forward-file write.

## Cure applied

| change | detail |
|---|---|
| `scripts/bbnfix_when_ready_all.sh` | Tables **OFF by default**; Stage A = book+finalize only |
| `--write-tables` | Requires `bbnfix_booking_*/RED_AUDIT.md` with `red: AGREE` or `AGREE-IF` |
| `--force-tables` | Owner emergency override only (logged) |
| RUNBOOK.md | Publish-split section |

## Not a breach

Nothing was booked; CHAIN_TABLES not modified by booking runs.

*NO FABRICATIONS.*
