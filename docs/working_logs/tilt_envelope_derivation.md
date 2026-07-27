# The tilt envelope derived: conserved-charge conversion (2026-07-27)

Task #9's finish path, executed. Companion script: `scripts/ns_envelope_mechanism.py`
(arithmetic verified; residual test run). Route context: the data had already
eliminated the alternatives (`ns_modulation_check.py` v2 — running-coupling killed by
sign; incoherent accumulation excluded at +4.5σ).

## The chain, each link recorded or computed

1. **The source is a conserved charge.** The census imprint is an occupancy-number
   fluctuation, and the sum-rule computation (the τ program's own m₁(0) = 0, exact)
   says the long-wavelength number mode is conserved: short-scale census activity
   cannot redraw it. Each mode carries one frozen realization S_k.
2. **Constant rate per e-fold.** A conserved-number (isocurvature) fluctuation in a
   component of constant energy fraction sources curvature at a constant rate:
   dζ_k/dN = r·S_k. The medium's excitation sector is radiation-like early with a
   fixed fraction (recorded: one fluid, two eras).
3. **The interval is the log.** Sourcing runs from the medium's birth scale (the
   verified anchor k_UV) to the mode's horizon crossing: N(k) = ln(k_UV/k).

⟹ ζ_k = r·ln(k_UV/k)·S_k — the modulation map produced, not postulated: envelope ×
shot, amplitude ∝ L, the "2 = amplitude-squared," n_s = 1 − 2/L = 0.9677 (+0.66σ),
α_s = −(1−n_s)²/2 = −5.2×10⁻⁴.

**The coherence is forced, not assumed:** incoherent per-decade accumulation would
require the number fluctuation to be redrawn — forbidden by the conservation law.
The route the data selected is the only route the medium's charge conservation
permits. (The same conservation protects the lepton null — one computed fact, two
loads, noted and not stacked.)

## The built-in test, run

Conversion leaves a correlated residual isocurvature S/ζ = 1/(r·L) at entry.
Across the rate range the normalization allows: 1.6% (r = 1) to 16% (r = 0.1).
The registered percent-class isocurvature line (P-2026-031 band) is the RIGHT SIZE
to be this mechanism's own residual at r ~ O(1), and a real tension for r ≲ 0.1.
The residual is not an escape hatch: it is correlated, sits at the registered
line's amplitude class, and the rate that sets it is the same normalization the
amplitude's C = 1 identification owes (task #15). **One number now feeds three
claims: A_s's normalization, the tilt's envelope rate, and the isocurvature line's
amplitude — three measurements of r, refereeing each other.**

## Grade and gates

**Candidate derivation** — mechanism class identified (conserved-charge isocurvature
conversion at constant fraction), coherence forced by a computed conservation law,
arithmetic verified, residual test run. **Promotion gates:** the rate normalization
(#15) and the residual's consistency against the registered isocurvature bounds.
**Kill:** a rate landing that pushes the residual outside the registered band, or
the constant-fraction premise failing at the imprint epochs. Nothing promoted today.

## Addendum (2026-07-27, same day): the normalization triangle, and the premise made exact

`scripts/as_normalization_triangle.py` (task #15). The mechanism transforms the old
one-shot normalization (C with its factor-250 convention spread) into two physical
parameters: A_s = r²L*²f³/2π² — the conversion rate r and the imprint cell fraction
f = k·ξ. Results:

- **The component-identity ruling.** The rate normalizes as r = c·f_E. The
  dark-subcomponent reading (census in the dark fluid's radiation-like phase,
  fraction (Ω_dm/Ω_r)/(1+z_on) ≈ 7.2×10⁻⁵) needs c ≳ 10⁴ to meet the registered
  residual band — dead by four orders (ledger row filed). The census is the
  SUBSTRATE's own occupancy — the same counting that prices the vacuum energy —
  whose fraction is identically 1: **the constant-fraction premise becomes exact.**
- **The rate is bounded two-sided by the registered band:** r ∈ [0.8, 3.2].
- **The cell fraction is pinned given r:** f ≈ 2×10⁻⁴ — the basement's forward
  target, REVISED from the one-shot 3.45×10⁻³ (the L*² factor is computed, not
  chosen).
- **The closed form is a consistent point:** (α_c/4πk)³ demands f = 2.206×10⁻⁴ at
  r = 1, against the measured-A_s pin of 2.213×10⁻⁴ — 0.3% apart. Deriving f from
  the medium now decides #15, gates #8, and referees #9 in one stroke.
