# Blocked lane audit — primordial helium benchmark fork (2026-08-05)

Purpose: freeze the live helium benchmark state exactly, so the BBN shelf stops carrying stale
pre-2026 comparison numbers as if they were the current literature state.

## Lane

Primary blocked lane for:

- `docs/PRTOE_bbn_witness.md`

Secondary spillover:

- `docs/PRTOE_deuterium_row.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_fairbank_note_draft.md`

This lane controls whether the desk may quote:

- the old `Aver = 0.2453 +- 0.0034` / `EMPRESS = 0.2370 +- 0.0034` pair as the current helium
  literature state
- the shelf's old helium sigma summaries as live benchmark language
- the helium benchmark as a settled single external referee

## Authority sources

Exact authority used for this freeze:

- arXiv:2601.22238, *The LBT Y_p Project IV: A New Value of the Primordial Helium Abundance*
- arXiv:2506.24050, *EMPRESS. XV. A New Determination of the Primordial Helium Abundance
  Suggesting a Moderately Low Y_P Value*
- `docs/PRTOE_bbn_witness.md`
- `docs/PRTOE_READERS_RISK.md`

## Exact state

### 1. The LBT Y_p Project IV result is now the high-precision benchmark

arXiv:2601.22238 reports:

- `Y_p = 0.2458 +- 0.0013`
- the paper describes this as in good agreement with the BBN result `Y_p = 0.2467 +- 0.0002`

Referee read:

- this is materially tighter than the older Aver benchmark the shelf was still quoting
- the shelf may no longer headline `0.2453 +- 0.0034` as the live Aver-side number

### 2. EMPRESS XV moved too, but remains lower

arXiv:2506.24050v3 reports:

- `Y_p = 0.2402 +- 0.0040`
- the paper describes it as a moderately low result with mild tension against the Standard Model /
  Planck expectation

Referee read:

- the lower-helium side of the literature still exists
- but it is no longer the older `0.2370 +- 0.0034` number the shelf was carrying

### 3. The old shelf sigma lines are now stale as current-benchmark prose

The shelf's current helium sigma shorthand was built against older benchmark values. That means:

- the model's direction of tension remains adverse
- but the exact old `Aver` / `EMPRESS` sigma pair should not be used as live benchmark currency
  until the comparisons are rerolled against the 2025-2026 external numbers

Referee read:

- keep the model's helium direction adverse
- stop presenting the old benchmark pair as current literature state

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| old Aver / EMPRESS pair as live benchmark | stale | both sides have newer published values |
| exact old helium sigma pair as current currency | stale | benchmark papers changed |
| single settled helium external verdict | not available | literature still carries a high-precision LBT result and a lower EMPRESS result |

## Allowed

- quote the model's own Y_p outputs
- quote `Y_p = 0.2458 +- 0.0013` from LBT Y_p Project IV
- quote `Y_p = 0.2402 +- 0.0040` from EMPRESS XV
- say the model's helium direction remains adverse

## Forbidden

- quote `0.2453 +- 0.0034` / `0.2370 +- 0.0034` as the current helium literature state
- use the old helium sigma pair as live benchmark prose
- pretend the helium benchmark is externally settled to one number

## Honest unblock path

There are only two honest closure paths:

1. reroll the shelf's helium comparisons against the current external benchmark papers
2. or wait for the outside literature to converge further on one benchmark class

If the helium benchmark changes again, update this audit first, then propagate the exact new state
into the dependent docs.
