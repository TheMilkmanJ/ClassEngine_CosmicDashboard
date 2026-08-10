# Blocked lane audit — S8 conversion channel (2026-08-05)

Purpose: freeze the shared S8 conversion lane exactly, so the shelf stops mixing three different
objects into one vague blocker:

1. `cmp_prtoe_conv_desi` — the intended conversion posterior instrument
2. `cmp_prtoe_routeD` — a live thaw instrument, related but not a substitute
3. matched DES/KiDS lensing likelihood — still owed before any published easing claim

## Lane

Shared blocked lane for:

- `docs/PRTOE_s8_growth.md`
- `docs/PRTOE_s8_tension.md`

Secondary relevance:

- `docs/PRTOE_neutrino_home.md` claim-ledger row on conv_g double-duty
- `docs/PRTOE_CHAIN_TABLES.md` live machine board

This lane controls whether the desk may quote:

- a produced conversion posterior for `conv_g`
- a measured S8-easing claim
- a published tension-easing claim against matched lensing

## Authority sources

Exact authority used for this freeze:

- `chains/cmp_prtoe_conv_desi.progress`
- `chains/cmp_prtoe_conv_desi.checkpoint`
- `chains/cmp_prtoe_routeD.progress`
- `chains/cmp_prtoe_routeD.checkpoint`
- `docs/PRTOE_CHAIN_TABLES.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

## Exact machine state

### 1. `cmp_prtoe_conv_desi` — unproduced, not live

Last progress row on disk:

- `N = 3744`
- `timestamp = 2026-07-22T11:06:00.255576`
- `R−1 = 13.251101`
- checkpoint `converged: false`
- `mpi_size: 1`

Referee read:

- this is a dead archive-row instrument, not a live posterior
- it never reached its own stop
- nothing in its archived GetDist table is quotable as a posterior

### 2. `cmp_prtoe_routeD` — live, exploratory, not a substitute

Latest live progress row:

- `N = 8120`
- `timestamp = 2026-08-05T12:54:11.741884`
- `R−1 = 0.728432`
- checkpoint `converged: false`
- `mpi_size: 3`

Referee read:

- routeD is alive, but still about `7.28x` above its `0.1` stop
- routeD is a thaw instrument, not the conversion-posterior instrument
- routeD therefore does **not** unblock the S8 conversion lane by itself

### 3. Matched lensing is still owed

The top-level S8 docs both still carry the same requirement:

- a matched DES/KiDS lensing likelihood campaign is required before any published tension-easing
  claim

So even a converged restart of `conv_desi` would not by itself create the full publishable claim.

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| `conv_g` posterior from `cmp_prtoe_conv_desi` | unproduced | chain dead / unconverged / not live |
| measured S8 easing from the conversion lane | blocked | no produced conversion posterior |
| published S8 tension-easing claim | blocked | matched lensing still owed even after posterior |

## Allowed

- quote the exact dead/live distinction between `conv_desi` and `routeD`
- quote current chain state with `N`, `R−1`, timestamp, and `converged`
- describe routeD as exploratory and live
- describe conv_desi as unproduced and owner-restart-gated

## Forbidden

- quote archived `conv_desi` GetDist rows as a posterior
- treat routeD early samples as the conversion test
- claim a measured S8 win
- claim a published tension-easing result
- collapse routeD, conv_desi, and matched lensing into one “basically done” story

## Honest unblock path

There are two separate closures, in order:

1. **Machine closure**
   - owner restarts `cmp_prtoe_conv_desi`
   - chain reaches its stop and self-stabilizes
   - only then may `conv_g` posterior language be refreshed from the live run

2. **Phenomenology closure**
   - matched DES/KiDS lensing likelihood campaign lands
   - only then may the desk claim a published tension-easing result

RouteD may remain useful science in parallel, but it does not skip either closure.

## Dependent docs

Use this audit as the shared blocker reference for:

- `docs/PRTOE_s8_growth.md`
- `docs/PRTOE_s8_tension.md`

If the machine state changes, update this audit first, then propagate the exact new state into the
dependent docs.
