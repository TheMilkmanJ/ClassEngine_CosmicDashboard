# CANDIDATE DIRECTION — the late-time single lever: one unfinished thaw for BOTH H₀=73 and DESI's w(z)

*Opened 2026-07-17 (JP). Grade: **CANDIDATE / EXPLORATORY, unfired.** This entry is licensed to
kill the model's own proud predictions — see the governing principle at the bottom. Nothing here is
banked; it is a direction to chase and, if it fails, to bury in the FAILURES LEDGER with the why.*

## The two walls this is aimed at (both corpus-confirmed)

1. **PRTOE cannot reach H₀ = 73.** Its own file says so: *"The model cannot reach 73, and says so"*
   ([PRTOE_hubble_tension.md](../PRTOE_hubble_tension.md):46); the ceiling is ~71 (ς=−1 → ~70.6).
   The mechanism is **early-time** — *"earlier decoupling, a smaller sound horizon."* Early-time
   sound-horizon solutions are known to top out near ~70 (the "H₀ Olympics" result): the same CMB
   that reveals the tension caps how far r_s can shrink.
2. **The dCDF's w = −1 is rigid**, so DESI's w ≠ −1 hint is currently a **kill** (P-2026-005),
   not a feature. Two separate walls.

**JP's insight:** if SH0ES = 73 is genuinely right (the Cepheid calibration is the most-scrutinised
measurement in cosmology), then an early-time lever is **structurally insufficient** — and the fix
is a **late-time** one. And late-time is exactly where DESI lives. **So one late-time thing might
answer both.**

## The mechanism (the honest, corpus-native version)

The dCDF's w = −1 is an **asymptotic floor** ("never crossed"). The *approach* to it — the
**thaw/settling** — is a low-z dynamical process. If the dCDF is **still settling toward w = −1 near
z ~ 0 (an UNFINISHED thaw)**, then a single fact produces both effects:

- **w(z) at low z ≠ −1** (evolving) → **DESI's w₀–wₐ hint, as a feature not a kill**;
- **the modified low-z expansion** → **raises the ladder H₀**.

One lever — the unfinished thaw — for both walls. The machinery already exists: the
`dcdf_floor_thaw` parameter, the `routeD` / `conv_desi` thaw chains, and T4's recorded
*"DESI-policed w(z) meaning-inversion"* note (the kill→feature flip, already half-written).

## What it COSTS (stated up front, because it is real)

- **It reverses the DE stance.** "w = −1 exactly" stops being a proud rigid prediction and becomes
  a specific dynamical *trajectory* (w settling to −1). **P-2026-005 (w = −1) is on the table to
  die** if this direction wins. That is allowed (see below).
- **"One knob does both" is a GAMBLE, not a gimme.** Late-time DE that raises H₀ tends to fight the
  BAO+SN distances (tightly measured geometry), and DESI's own w₀–wₐ fit usually pulls H₀ *lower*.
  The same thaw trajectory must thread: bend w(z) to match DESI **and** bend expansion the right way
  for the ladder **and** not break BAO. A real needle.

## The test (computable, machinery exists)

Fit the **unfinished-thaw dCDF** (thaw not complete by z~0) against **DESI w(z) + BAO + SN + SH0ES**
and ask, simultaneously:
1. does it reproduce DESI's w₀–wₐ preference (~2–4σ from w=−1)?
2. does it raise the ladder H₀ toward 73?
3. does it keep BAO/SN?

`routeD` / `conv_desi` were built for exactly this (both currently down — conv_desi died at startup
per T4; routeD was killed 2026-07-17 — so they need a clean relaunch, symmetric-BBN like the
evidence pair). **Gated behind the running pc_prtoe evidence run for cores.**

## Kill conditions for THIS candidate (so it can be buried honestly)

- The thaw trajectory that fits DESI pulls H₀ the **wrong way** (down, or no higher than the
  early-time ~71 ceiling) → the "single lever" claim is dead; the two walls are two problems.
- Matching DESI's w(z) **breaks BAO/SN** beyond tolerance → the late lever is excluded.
- The thaw needed is so recent/sharp it violates the depth law (a step, not a ramp) → illegal.
- A robust DESI result **consistent with w = −1** → there is no second wall to knock down, and the
  rigid-floor prediction (P-005) simply stands.

## THE GOVERNING PRINCIPLE (JP, 2026-07-17) — why we are allowed to chase this

> **The model's proud predictions are NOT mandated by the model. Nothing is set in stone until the
> model is ~99–100% complete and there is nothing left to do but run the PolyChord evidences.** A
> prediction that a better mechanism would kill is not a wall to defend — it is a candidate to test.
> This is what the FAILURES LEDGER is for: chasing a direction that may cost us w=−1 is not
> recklessness, it is the method. We bury what dies, with the why, and keep what survives the full
> build.

*Related: [T4_s8_growth_owed.md](T4_s8_growth_owed.md) (the thaw/DESI machinery),
[PRTOE_H0_CEILING.md](../PRTOE_H0_CEILING.md) (the ~71 early ceiling this would break past),
P-2026-005 (the w=−1 prediction on the table).*
