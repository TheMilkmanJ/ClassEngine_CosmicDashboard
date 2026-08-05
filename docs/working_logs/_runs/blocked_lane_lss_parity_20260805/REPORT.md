# Blocked lane audit — LSS parity / DESI 4PCF (2026-08-05)

Purpose: freeze the LSS parity lane exactly, so the shelf stops carrying stale versions of the
external referee state.

## Lane

Primary blocked lane for:

- `docs/PRTOE_lss_parity.md`

Secondary spillover:

- `docs/PRTOE_REFEREE_CALENDAR.md`
- `docs/PRTOE_PREREGISTERED_PREDICTIONS.md`
- `docs/BIBLIOGRAPHY.md`

This lane controls whether the desk may quote:

- the anti-anomaly bet as fully externally closed
- the DESI status as still awaiting a first direct 4PCF measurement
- the parity claim's systematics status as final rather than favorable-but-limited

## Authority sources

Exact authority used for this freeze:

- `docs/PRTOE_lss_parity.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`
- arXiv:2512.20132, *Parity-odd Four-Point Correlation Function from DESI Data Release 1 Luminous Red Galaxy Sample* (2025-12-23)
- arXiv:2604.06021, *Testing parity with composite-field spectra of BOSS and DESI luminous red galaxies* (2026-04-07)

## Exact state

### 1. The model-side pricing remains short by about seven orders

The shelf's own model-side result still stands:

- native parity channel exists
- induced parity-odd 4PCF amplitude is priced at about `(v/c)^3 ~ 10^-9`
- this is about seven orders below the claimed BOSS-scale amplitude

Referee read:

- the model cannot source the claimed large BOSS signal
- the anti-anomaly bet remains an owned exposure, not a fit

### 2. A direct DESI DR1 4PCF paper has already landed

Direct external result now on arXiv:

- arXiv:2512.20132 measures the parity-odd 4PCF on the DESI DR1 LRG sample
- with one uncorrected covariance treatment, apparent auto-correlation excesses can reach up to
  `4 sigma`
- the paper's overall conclusion is that the current DESI DR1 parity-odd signal is consistent with
  zero
- the paper explicitly flags low DR1 completeness as a likely sensitivity limitation and points to
  future data releases for sharper tests

Referee read:

- the shelf can no longer say a direct DESI 4PCF measurement is wholly missing
- the landed direct DR1 result is favorable to the anti-anomaly bet, but not decisive

### 3. The composite-field null and blind BOSS downgrade remain corroborating context

Additional external state already on the shelf:

- arXiv:2604.06021 finds no evidence for a cosmological parity-violating signal in either BOSS or
  DESI using composite-field spectra
- DESI scatter is about four times tighter than BOSS DR12 in that analysis
- the blind BOSS CMASS 4PCF test yields `2.9 sigma` versus `7.1 sigma` unblinded

Referee read:

- the external drift is favorable to the anti-anomaly bet
- but the composite-field null is not itself the same statistic as the original 4PCF claim

### 4. What still remains owed

Two things are still genuinely open:

- higher-completeness direct DESI 4PCF releases
- the axis protocol, if any parity signal survives at a material level

Referee read:

- this lane is favorable, but not fully closed

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| full external closure of the anti-anomaly bet | not closed | direct DR1 result is favorable but sensitivity-limited |
| claim that DESI had no direct 4PCF measurement | false | arXiv:2512.20132 already exists |
| axis-correlation protocol | still data-gated | only relevant if a real parity signal survives |

## Allowed

- quote the model-side shortfall of about seven orders
- quote the direct DESI DR1 4PCF result as consistent with zero
- quote the composite-field null and blind BOSS downgrade as favorable corroboration
- keep the anti-anomaly bet registered and favorable

## Forbidden

- claim the anti-anomaly bet is fully closed
- claim a direct DESI 4PCF measurement is still wholly missing
- claim the current external state is decisive enough to mark the lane COMPLETE
- claim the model detects or sources LSS parity violation

## Honest unblock path

There are only two closure paths:

1. future higher-completeness direct DESI 4PCF releases continue to find no material signal,
   letting the anti-anomaly bet strengthen
2. a confirmed parity signal at the claimed amplitude lands on the direct statistic, which calls in
   the model's owned exposure

If the external state changes, update this audit first, then propagate the exact new state into
dependent docs.
