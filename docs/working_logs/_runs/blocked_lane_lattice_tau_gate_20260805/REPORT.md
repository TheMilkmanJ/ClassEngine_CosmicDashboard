# Blocked lane audit — lattice tau gate / P-048 external referee (2026-08-05)

Purpose: freeze the live external lattice state exactly, so the dark-energy shelf distinguishes the
ready gap note from the still-blocked tau referee.

## Lane

Primary blocked lane for:

- `docs/PRTOE_cosmological_constant.md`

Secondary spillover:

- `docs/PRTOE_lattice_note.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

This lane controls whether the desk may quote:

- the tau referee as already landed
- crown/null discrimination as currently executable
- the lattice gap note's readiness as if it promoted the blocked DE stack

## Authority sources

Exact authority used for this freeze:

- `docs/PRTOE_cosmological_constant.md`
- `docs/PRTOE_lattice_note.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

## Exact state

### 1. The live falsifier is still clause 4

Current shelf state:

- live falsifier window is `tau_hat outside [0.330, 0.370]`
- neighbor inference on shelf remains centered above the target window

Referee read:

- clause 4 is still the live executable kill

### 2. Crown/null remains sky-limited

Current shelf state:

- crown value `0.34657`
- null value `0.34506`
- separation is about `0.44%`
- even `sigma_lattice = 0` gives only about `0.98 sigma` discrimination because the cosmological
  `rho_Lambda` uncertainty dominates

Referee read:

- clauses 2 and 3 are still not executable at current sky precision
- ordinary `1-3%` lattice work still scores neither way on crown/null

### 3. The public lattice note is ready, but the DE stack is not

Current shelf state:

- `PRTOE_lattice_note.md` is a `READY_PACKAGE` gap note
- `PRTOE_cosmological_constant.md` is still blocked on the external tau referee and separate desk
  amplitude residuals

Referee read:

- shipping the gap note does not promote the cosmological-constant stack

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| DE tau referee as landed | not landed | external lattice computation still owed |
| crown/null as executable current test | not executable | sky precision dominates even at zero lattice error |
| cosmological-constant stack as promoted by the gap note | forbidden | gap note readiness does not close the DE stack |

## Allowed

- quote clause 4 as the live falsifier
- quote crown/null as sky-limited
- quote `lattice-tc-gap` as a ready external gap note

## Forbidden

- claim the tau referee has already landed
- claim ordinary lattice precision decides crown/null
- use `lattice-tc-gap` readiness to imply the DE stack is arXiv-ready

## Honest unblock path

There are only two honest closure paths:

1. external lattice computation lands with a result inside or outside the clause-4 window
2. cosmological precision changes enough to make crown/null executable

Update this audit first if either condition changes, then propagate the exact new state into
dependent docs.
