# Blocked lane audit — zon_disp alpha_c / onset instrument (2026-08-05)

Purpose: freeze the parked `zon_disp` lane exactly, so multiple shelf files stop carrying partial
or drifting versions of the same machine blocker.

## Lane

Primary blocked lane for:

- `docs/PRTOE_quartet_clock.md`
- `docs/PRTOE_galactic_atoms.md`
- `docs/PRTOE_smbh_atoms.md`

Secondary spillover:

- `docs/PRTOE_neutrino_sector.md` occupancy-corrected `rho_inf` closure note
- `docs/PRTOE_THE_AMPLITUDE.md` / alpha_c bet language
- `docs/PRTOE_CHAIN_TABLES.md` machine board

This lane controls whether the desk may quote:

- an instrument verdict on the registered `log10_z_on` / pair-call lineup
- a measured `alpha_c` / onset posterior
- a propagated recorded-mass posterior for galaxy / SMBH atom claims

## Authority sources

Exact authority used for this freeze:

- `chains/cmp_prtoe_zon_disp.progress`
- `chains/cmp_prtoe_zon_disp.checkpoint`
- `chains/zon_disp_seed.covmat`
- `docs/PRTOE_CHAIN_TABLES.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

## Exact machine state

### 1. `cmp_prtoe_zon_disp` — parked, unconverged, not live

Last progress row on disk:

- `N = 3456`
- `timestamp = 2026-07-22T09:37:45.977656`
- `R−1 = 17.812870`
- checkpoint `converged: false`
- `mpi_size: 1`

Referee read:

- the instrument is **not running**
- it never approached its stop
- it has no quotable center

### 2. Seed state

The restart seed exists on disk:

- `chains/zon_disp_seed.covmat`

Calendar authority already records the key process lesson:

- the collapsed config seed covered `12/13` parameters and missed `log10_zon`
- relaunching on the wrong seed would just reproduce the failure
- restart is an owner action on the from-samples seed, not a desk inference

### 3. Archive tables are diagnostics only

`PRTOE_CHAIN_TABLES.md` still contains archive GetDist rows for `cmp_prtoe_zon_disp`, but those are
diagnostic history only. They are not a posterior because the run never converged.

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| pair-call / lineup verdict in `quartet_clock` | no instrument verdict | chain parked and unconverged |
| `alpha_c` / onset posterior | unproduced | no live converged instrument |
| recorded-mass propagation into galactic / SMBH atoms | blocked | mass pin still rides the parked onset instrument |

## Allowed

- quote the exact parked state with `N`, `R−1`, timestamp, and `converged`
- say the seed exists
- say restart is owner-gated
- say archive tables are diagnostics, not posteriors

## Forbidden

- quote any `zon_disp` center as a measured result
- treat the cumulative near-hit around `7.55` as confirmation
- claim the pair-call is instrument-confirmed
- propagate a measured mass posterior into galactic or SMBH claims

## Honest unblock path

There is only one closure path:

1. owner restarts `cmp_prtoe_zon_disp` or a stated successor onset instrument
2. chain reaches its stop and self-stabilizes
3. only then may `alpha_c` / `log10_zon` language be refreshed from the live posterior
4. only then may dependent mass-propagation claims be repriced

No docs-only cleanup cures this lane.

## Dependent docs

Use this audit as the shared blocker reference for:

- `docs/PRTOE_quartet_clock.md`
- `docs/PRTOE_galactic_atoms.md`
- `docs/PRTOE_smbh_atoms.md`

If the machine state changes, update this audit first, then propagate the exact new state into the
dependent docs.
