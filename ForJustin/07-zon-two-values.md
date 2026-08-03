# 07 — z_on: RESOLVED by computation. The mass is right; the running job's z_on is the outlier.

**Settled 2026-07-19. No decision needed from you on the physics — the model pins its own mass three
independent ways and they agree. One live consequence is flagged at the bottom.**

## The question

Two values appeared under one name: z_on = 4.03×10⁷ (the H = m identity in `include/background.h`)
and 3.5619×10⁷ (what the running evidence job uses). Since z_on ∝ √m these imply dyad masses 28%
apart — 2.24×10⁻²⁰ vs 1.75×10⁻²⁰ eV — so one of them had to be wrong.

## The test that settles it

The mass is not a free label. Three recorded quantities depend on it, and all three were computed
before this question came up:

| test | recorded | m = 2.24×10⁻²⁰ | m = 1.75×10⁻²⁰ |
|---|---|---|---|
| coherence length ξ = ħ/(m c_s) | 402 AU | **398 AU** ✓ | 509 AU ✗ (27% off) |
| Schive core radius, 10⁹ M☉ halo | 7.0 pc | **7.14 pc** ✓ | 9.13 pc ✗ (30% off) |
| SMBH superradiance window | 6×10⁸–3×10⁹ M☉ | **exact** ✓ | 28% off ✗ |

Inverting the first: ξ = 402 AU requires m = 2.218×10⁻²⁰ eV.

**The mass is 2.24×10⁻²⁰ eV, and z_on = 4.03×10⁷ (log₁₀ 7.605) is the consistent onset.** The
running job's 3.5619×10⁷ is the outlier — it implies a mass that breaks every other place the mass
is used.

## What was fixed

- `PRTOE_MATH_SPINE.md` §0 — the mass keeps its MEASURED grade, but now on the three independent
  uses rather than on the recorded "free-z_on optimizer → m = 2.29×10⁻²⁰, 2% above" reading, which
  was arithmetically inverted (7.5517 implies 1.75×10⁻²⁰, 22% *below*). The old basis is noted as
  corrected rather than quietly dropped.
- `PRTOE_THREE_EQUATIONS.md` — the stated-stack row now gives the identity as the model's z_on and
  lists the run's setting separately, as what the run actually tests.
- Five checks added to `scripts/audit_math_pass.py`, including two that assert the run's implied
  mass *misses* the ξ target — so if anyone re-derives toward 1.75×10⁻²⁰, the harness objects.

## The one thing left, and it is yours because it decides what the next run tests

**The evidence configuration sits at z_on = 3.5619×10⁷, which is not the model's own identity
value.** It tests a point 0.053 dex off, corresponding to a mass 28% from the one every other sector
uses. That was a deliberate, disclosed choice — the config calls it a profiled freeze and prices it
at "χ² cost +7.4 vs the free champion" — but its consequence for the mass does not appear to have
been noticed when it was made.

**The scheduling half of this decided itself on 2026-07-20** (#99): the nested run was ended and
archived, because at 9.8 h per iteration its first checkpoint sat 163 days out. So there is no
running job to protect, and the choice below is about what the configuration should say whenever
the comparison is next computed — from the MCMC now, or nested when cluster time is bought:

1. **Report it as-is**, noting in the write-up that the frozen z_on sits off the identity. Cheapest,
   and honest if stated.
2. **Treat the result as a bound rather than the model's own evidence**, since the frozen point is
   not the model's stated configuration.
3. **Move the configuration to the identity.** This no longer costs a restart — nothing is running —
   so its only price is that every number computed at the old freeze stops being comparable.

Related: `cmp_prtoe_zon`, the chain the config names as its arbiter, has not run since 2026-07-12
(two R−1 points ever, 93.10 → 40.36, no live process). The "ILLEGAL until the zon chain converges"
condition cannot be met by waiting. If option 1 or 2 is chosen, that comment should be rewritten to
say what actually governs the value.
