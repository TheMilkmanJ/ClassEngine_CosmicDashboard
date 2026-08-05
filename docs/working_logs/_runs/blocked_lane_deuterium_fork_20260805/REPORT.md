# Blocked lane audit — deuterium fork / radio referee (2026-08-05)

Purpose: freeze the deuterium fork exactly, so the BBN shelf stops carrying drifting versions of
the same external blocker.

## Lane

Primary blocked lane for:

- `docs/PRTOE_deuterium_row.md`
- `docs/PRTOE_bbn_witness.md`

Secondary spillover:

- `docs/PRTOE_fingerprint_lattice.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

This lane controls whether the desk may quote:

- the absolute D/H row as settled
- the observational side of the D/H fork as decided
- the nuclear-theory side of the row as closed

## Authority sources

Exact authority used for this freeze:

- `docs/PRTOE_deuterium_row.md`
- `docs/PRTOE_bbn_witness.md`
- `docs/PRTOE_fingerprint_lattice.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

## Exact state

### 1. Standing absolute row remains adverse and width-sensitive

Current booked standing row:

- model prediction `D/H = 2.387 x 10^-5`
- standing width `+-0.0476`
- standing pull `-2.94 sigma`

The same shelf also records the honest width spread:

- across current literature/error constructions the row spans about `-3.6 sigma` to `-1.6 sigma`
- the standing number is not the only defensible width construction

Referee read:

- absolute D/H is adverse, not solved
- exact sigma class is still width-construction-sensitive

### 2. The compilation-robust statement is narrower and stable

What survives every rate-compilation choice on the shelf:

- model is worse than its own in-house `LambdaCDM` control by about `0.6-0.7 sigma`
- that comparison does not turn favorable under the named nuclear alternatives

Referee read:

- no nuclear choice turns this into a model win
- the robust adverse statement is model-versus-control, not the exact absolute sigma

### 3. The fork still has two external sides

The shelf already names the two external decision channels:

- `P-2026-058`: theory side, driven by the `d(d,n)^3He` rate
- `P-2026-027`: observational side, the radio referee

Live external state from the shelf:

- the LUNA collaboration still names `d(d,n)^3He` as the top remaining priority in primordial
  deuterium
- that measurement has not yet landed
- the radio referee has not yet landed either

Referee read:

- the full D/H fork is still open externally
- the narrow `bbn-eps-bound` ship package stays clean because it intentionally does not rely on
  absolute D/H closure

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| absolute D/H row as a settled public result | not closed | theory-side rate and observational-side referee both still open |
| any claim that BBN is a model win | not allowed | model remains adverse vs its own control |
| radio-arbitrated D/H observational fork | pending | `P-2026-027` has not landed |
| nuclear-side rate closure | pending | `d(d,n)^3He` measurement still outstanding |

## Allowed

- quote `D/H = 2.387 x 10^-5`
- quote the standing `-2.94 sigma` on width `+-0.0476`
- quote the honest width span `-3.6 sigma` to `-1.6 sigma`
- quote the robust model-minus-control adverse gap `~0.6-0.7 sigma`
- keep `bbn-eps-bound` as a ready narrow package that excludes absolute D/H closure claims

## Forbidden

- present the absolute D/H row as settled
- present BBN as a model win
- claim the radio referee has already decided the fork
- claim the `d(d,n)^3He` priority measurement has already landed
- use the narrow BBN package's readiness to imply full deuterium-row closure

## Honest unblock path

There are only external closure paths here:

1. the `d(d,n)^3He` measurement lands or the theory-side rate dispute closes by another stated
   external result
2. the radio referee lands on the observational side
3. update this audit first
4. only then refresh dependent shelf language from the exact landed outcome

No docs-only cleanup cures this lane.

## Dependent docs

Use this audit as the shared blocker reference for:

- `docs/PRTOE_deuterium_row.md`
- `docs/PRTOE_bbn_witness.md`
- `docs/PRTOE_fingerprint_lattice.md`

If either side of the fork lands, update this audit first, then propagate the exact new state into
the dependent docs.
