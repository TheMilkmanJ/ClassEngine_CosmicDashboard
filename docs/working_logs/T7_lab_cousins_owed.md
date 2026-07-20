# T7 lab cousins — OWED
1. Design notes for the three flagged bench tests: (a) f̄-ramp on a ring BEC (Z4-patterned tilt; measure the partition's TIME-DRIFT — internal review on a bench); (b) toroidal-quench winding statistics vs Kibble √N; (c) phase-slip statistics (the co-link corner).
2. The bench↔cosmos parameter mapping TABLE (which dimensionless ratios carry over; internal review "bench ≠ cosmos" caveat made precise).
3. Literature pass: has any existing ring-BEC dataset already measured (a) implicitly?

Coupling-geometry status: screened-room (bench experiments) — verdicts hold by geometry.

## PAID (2026-07-19 reconciliation): items 1 and 2 — the three bench proposals are specified
and the bench↔cosmos mapping table is written (the thread file's 2026-07-18 addendum: the
⟨|cos|⟩ = 2/π target vs the rejected rivals, the quench-statistics corroboration fence, the
phase-slip barrier-vs-Arrhenius discriminator, and the two-"no" mapping rows).

## Item 3 — PAID (2026-07-20): no dataset measures f̄, and the question splits in two

**The answer is no, and the reason is more useful than the answer.** The search for an existing
ring-BEC measurement of ⟨|cos|⟩ = 2/π was chasing two different objects under one symbol.

**The first object is not measurable, because it is an identity.** Given an equidistributed phase,
⟨|cos|⟩ = 2/π is the rectified-sinusoid form factor — the same 0.637 electrical metrology has used
for a century as a sine wave's average value. Existing ring interferometry does bear on its one
physical premise, and confirms it: a single ring's azimuthal phase gradient is uniform, with the
winding read directly off the number of spiral fringes when the ring is interfered with a
concentric reference condensate (the technique of arXiv:1406.1095; local phase around the ring is
resolved in arXiv:2204.06542). **But equidistribution is the piece the corpus already grants**
([PRTOE_DERIVATION_HUNT.md](../PRTOE_DERIVATION_HUNT.md) §1), so this half refs a premise, not a
result.

**The second object has no dataset, and is the one worth building.** The corpus's f̄ is not the
identity — it is ∫f_amp(θᵢ)dθᵢ/(π/4), the release-averaged radial/angular energy partition of a
*tilted roll*, a dynamical quantity whose single draws scatter across [0.034, 0.964] and whose mean
lands at 0.635 ± 0.026. Nothing in the ring-BEC literature has run that experiment: it needs a
four-fold azimuthal modulation imposed on the ring potential, release at rest from a *controlled*
azimuthal phase, a scan over that phase, and a read of the energy partition. The apparatus classes
all exist separately — phase imprinting with local phase readout, azimuthally modulated "necklace"
ring potentials — so this is unrun rather than impossible.

**Why it is hard, stated so the proposal is honest:** (i) the tilt must be deep enough to torque and
shallow enough not to pin the phase, and an azimuthal lattice that localises kills the superflow the
measurement needs; (ii) because f_amp(θᵢ) is chaotic with adjacent-bin jumps, the observable is an
*average over a scanned release phase* — many shots per bin, not one good shot; (iii) standard ring
readout is destructive time-of-flight, one number per realisation, while the proposal wants the
partition's time-drift; (iv) the discrimination target is percent-level — 2/π = 0.6366 against the
rejected RMS 0.7071 is an 11% gap, against a simulation scatter already at 4%.

**And the ceiling, from the corpus's own mapping table:** even a clean result refs the granted half.
The owed piece is the *coupling form* — which functional of the winding projection the mass shift
couples to — and the mapping table's own second "no" is that no laboratory analogue of the lepton
portal exists. That is a structural bar, not a funding one.

*Bonus, unlooked-for:* proposal (c)'s discriminator has an apparatus on record — quantized phase
slips are directly imaged as vortex emission above a critical circulation in arXiv:2204.06542.

NEW candidate (protocol run): lab-BEC quantum-turbulence / Kelvin-cascade statistics as the genesis dice's bench analog — the roll-up's draw statistics (ε_spin, f̄) may have a measurable laboratory counterpart in dilute-BEC turbulence experiments. Candidate grade; needs the statistics mapping before it earns a row.

