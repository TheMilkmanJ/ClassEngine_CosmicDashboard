# Blocked lane audit — BipoSH joint axis-family referee (2026-08-05)

Purpose: freeze the shared BipoSH / axis-family blocker exactly, so the anomaly shelf stops
carrying partial or drifting versions of the same referee debt.

## Lane

Primary blocked lane for:

- `docs/PRTOE_cmb_anomalies.md`
- `docs/PRTOE_lowell_anomalies.md`

Secondary spillover:

- `docs/PRTOE_fingerprint_lattice.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

This lane controls whether the desk may quote:

- the low-ell axis family as a referee-closed public win
- the HPA as a settled family member rather than a candidate
- the compact-topology reading as a data-applied BipoSH result rather than a predicted pattern

## Authority sources

Exact authority used for this freeze:

- `docs/PRTOE_REFEREE_CALENDAR.md`
- `docs/PRTOE_cmb_anomalies.md`
- `docs/PRTOE_lowell_anomalies.md`
- `scripts/torus_lowell_pattern.py`

## Exact state

### 1. Power-spectrum route is closed as a referee

The compact-topology power-spectrum route is already graded, and it does not referee the family:

- total signal-to-noise across `ell = 2..6` is `0.16`
- at the smallest torus the matched-circle nulls permit, the quadrupole retains about `90%` of its
  power
- the predicted depth and the observed deficit sit only about `0.9 sigma` apart

Referee read:

- the power spectrum cannot grade the model here
- it may be quoted as a computed null / insufficiency result only

### 2. The off-diagonal covariance route is the live path

The same torus computation does supply a specific correlation pattern:

- `990` independent off-diagonal pairs over `ell <= 6`
- `111` non-zero pairs
- strongest entries are `m <-> -m` at fixed `ell` and `ell <-> ell+2` at fixed `m`
- total signal-to-noise is `1.4`
- every non-zero entry obeys the cube selection rule `Delta m == 0 (mod 4)` with even
  `ell - ell'`

Referee read:

- this is the only live axis-family referee path presently on the shelf
- at `1.4`, it constrains more than it decides

### 3. The data-confrontation step is still owed

Calendar authority already records the BipoSH joint pass as:

- `analysis-limited`
- `data exists`

What is still missing from the live shelf is the actual map-level confrontation that scores the
measured covariance and family alignment against the predicted pattern.

Referee read:

- the family remains `registered / candidate`
- the BipoSH pass is a real queued referee, not a completed one
- no public closure exists yet for the axis family on data

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| axis family as a closed public claim | not closed | BipoSH data application still owed |
| HPA as a settled fifth member | adverse-leaning candidate only | joint family referee not applied |
| compact-topology anomaly reading as a measured result | not allowed | current shelf holds prediction + pattern, not confrontation |
| fingerprint-lattice axis-family master | pending | same BipoSH referee debt |

## Allowed

- quote the exact `S/N = 0.16` power-spectrum null result
- quote the exact `S/N = 1.4` off-diagonal route and its `990 / 111` structure
- say the BipoSH pass exists on the calendar and is `analysis-limited` with data already in hand
- keep the axis family at `registered / candidate`

## Forbidden

- book the axis family as a confirmed anomaly win
- use the power spectrum as the deciding referee
- claim the BipoSH joint pass has already been applied to data
- settle the HPA mapping as closed

## Honest unblock path

There is only one honest closure path:

1. build or recover the actual map-level BipoSH confrontation against the predicted covariance
   pattern
2. score the measured covariance and family alignment jointly
3. if the pattern or alignment fails, kill the family accordingly
4. if it passes, update this audit first, then promote the dependent docs exactly to that grade

No docs-only cleanup cures this lane.

## Dependent docs

Use this audit as the shared blocker reference for:

- `docs/PRTOE_cmb_anomalies.md`
- `docs/PRTOE_lowell_anomalies.md`
- `docs/PRTOE_fingerprint_lattice.md`

If the BipoSH referee lands, update this audit first, then propagate the exact new state into the
dependent docs.
