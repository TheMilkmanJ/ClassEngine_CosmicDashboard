# Blocked lane audit — Route-D thaw chain (2026-08-05)

Purpose: freeze one shared authority for `cmp_prtoe_routeD`'s live state, so the ten forward-facing
files that quote its R−1 stop carrying ten independently-ageing copies of the same number.

This card exists for the same reason the `bbnfix` card does
([`blocked_lane_bbnfix_20260805/REPORT.md`](../blocked_lane_bbnfix_20260805/REPORT.md)), and it is
needed **more**, because Route-D is still running: every inline stamp of a live chain's R−1 is
stale the moment the chain writes its next row.

## Lane

Forward-facing files that quote Route-D's convergence state:

- `docs/PRTOE_MATH_SPINE.md`
- `docs/PRTOE_CHAIN_TABLES.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_CODE_MANIFEST.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`
- `docs/PRTOE_honest_status.md`
- `docs/PRTOE_DEPENDENCY_TREE.md`
- `docs/PRTOE_s8_growth.md`
- `docs/PRTOE_INDEX.md`
- `docs/PRTOE_PREREGISTERED_PREDICTIONS.md` (P-2026-056, the DESI DR3 branch entry)

This lane controls whether the desk may quote a **booked** Route-D thaw posterior. It may not.

## Gate definition

From `cmp_prtoe_routeD.yaml` (and the matching `chains/cmp_prtoe_routeD.input.yaml`):

- `Rminus1_stop: 0.1`
- `Rminus1_cl_stop: 0.2`
- `max_tries: 2000`

The gate is the **progress file's** `Rminus1` against `Rminus1_stop`, plus the checkpoint's
`converged` flag. Offline GetDist diagnostics are not the gate.

## Exact state at this card's stamp

| field | value |
|---|---|
| N | 9745 |
| progress `Rminus1` | **0.536955** |
| stamp | `2026-08-05T18:43:45.023658` |
| checkpoint `converged` | **false** |
| ranks | 3 |
| distance to stop | **≈ 5.37×** its 0.1 stop |
| gate state | **NOT BOOKABLE** |

Recent trajectory, so the direction is visible rather than asserted:

| N | stamp | R−1 |
|---:|---|---:|
| 6517 | `2026-08-05T04:07:15` | 0.705291 |
| 8120 | `2026-08-05T12:54:11` | 0.728432 |
| 9745 | `2026-08-05T18:43:45` | **0.536955** |

It rose, then fell. **It is moving toward the stop and has not reached it.** No trend is bookable
from three rows, and none is claimed here.

## The staleness rule this card exists to enforce

**Route-D is live.** As of this card the launchlog was still writing (19:32). Therefore:

- A forward-facing file that stamps an R−1 inline **must** carry the `N` and the timestamp with it,
  so a reader can tell the number's age. A bare R−1 for a live chain is not a fact, it is a
  snapshot presented as one.
- Any *derived* figure — "≈ 5.37× its stop" — ages with the number it came from and must be
  recomputed, not carried. The corpus previously carried "~7.28× stop" from the 0.728432 row; that
  multiplier survived after its input moved.
- The authority is this card plus the progress file, in that order.

## One caution on acceptance, because two numbers are in circulation

- The **progress file** column `acceptance_rate` reads **0.997544**.
- The **launchlog** reports, per rank: 3409/55971, 3340/54941, 3166/52205 — **≈ 6.1%**.

These are not the same quantity. The run uses `oversample_power: 0.4` with `oversample_thin: true`,
so the launchlog's step counter includes oversampled sub-steps while the accepted counter does not.
The shelf's existing "accept ~0.997 ⚠ oversampled" annotation is reading the progress column and
flagging it, which is defensible — but **the operationally meaningful acceptance for this run is the
launchlog's, and the two must not be quoted as though they were one number.**

Not adjudicated here: which of the two the convergence discussion should cite. Recorded so the
question is visible rather than resolved by whichever number a given file happened to copy.

## What is NOT bookable

- No Route-D thaw posterior.
- No dark-energy branch verdict from Route-D's internal state. `P-2026-056` is explicit that
  **DESI DR3 is the external adjudicator and is unaffected by the internal chain's state** — the
  registration's pre-commitment does not weaken because this chain is slow.
- Route-D is a **separate instrument** from the `bbnfix` pair. It is not part of that dual gate and
  does not open or close it.

## Standing instruction

The chain is running and is not to be stopped, restarted, or reconfigured. Slowness is not a reason;
only demonstrated inability to converge would be, and that is the owner's call.
