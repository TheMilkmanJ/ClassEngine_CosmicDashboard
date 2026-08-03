# The first-roll sign run — scope (2026-07-27)

*Working note for task #10. Scoping only; nothing here is run yet beyond the two
symbolic checks, which are exact.*

## What the run must decide

P-2026-057's conditional needs one integer from genesis: **s = sign(μ·n)** — the
product of the temporal rotation's sign and the spatial winding's sign. The chain
around it is fully walked (links A–E in the registration); s is the one input.

## What already exists

1. **The temporal half is a fair coin, exactly** (recorded 2026-07-20): the
   reflection σ: θ → 2π/N − θ preserves the single-harmonic tilt, release-at-rest,
   and friction, while flipping θ̇. So sign(μ) alone is unpredictable — proven, not
   suspected.
2. **Homogeneous release machinery exists** (`genesis_famp_orbit.py`,
   `genesis_famp_Z4.py`): the (R, θ) roll under the Z₄ tilt with Hubble friction.
   No script anywhere evolves spatial winding — the n side has never been run.
3. **The owed objects, per the debt census:** link 5 — the correlation of
   sign(θ̇) with sign(n) over the release ensemble; link 4 (heavier) — the relative
   sign of the rolled-up ring's poloidal and toroidal circulations.

## Two symbolic checks (new, exact — the scope's own results)

**The mirror preserves the product.** Under σ applied pointwise to a spatially
extended field, ∂ₓθ → −∂ₓθ, so the winding flips too: σ sends (θ̇, n) → (−θ̇, −n),
and the PRODUCT is σ-even. The symmetry that makes each factor a fair coin does
NOT make the product one. A lock is symmetry-allowed — this was not guaranteed.

**Parity is the genuine adversary.** Under x → −x alone, n → −n while θ̇ is
unchanged — the product flips. The field equation is parity-symmetric; only the
seeds (or the roll's own dynamics) break it. So the run decides exactly this:
does the roll's charge–current dynamics CORRELATE the drawn winding direction
with the temporal rotation (lock ⟹ the map closes), or does the winding direction
come independently from the seed draw (coin ⟹ P-2026-057's map dies honestly)?
Neither outcome is foregone; the run is genuinely decisive either way.

## The minimum decisive run (link 5)

Complex field on the compact axis (1+1 dimensions, periodic, ~512–1024 points),
Z₄-tilted potential, Hubble friction, release from rest at phase θᵢ with small
structured seeds. Evolve through the roll; record final sign(θ̇) and the final
winding integer n. Scan: ~20 release phases over one tilt period × ~10
deterministic seed realizations. Deliverable: the distribution of sign(θ̇·n) —
locked, phase-dependent-but-mirror-paired, or coin.

**Fences:** the 1+1D reduction addresses link 5 only; link 4 (the ring's
bilinear helicity) needs an axisymmetric 2+1D run — separate, heavier. The
trigger convention is P-2026-057's named fence and must be carried verbatim.

## Effort

- Link-5 run: ~1 day of careful build (winding-number and charge diagnostics,
  energy guard), a few hours of shared-core compute for ~200 evolutions.
- Link-4 run: weekend-class; hold until link 5 reports.

## Payoff

If the product locks: P-2026-057 graduates from conditional to a live
two-observable, zero-freedom prediction spanning a laboratory mass ratio and a
megaparsec magnetic field. If it does not lock: the map is retired to the
failures ledger and the handedness hint stays a watch. Either result is a real
one.
