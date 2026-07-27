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

## Addendum 2 (2026-07-27): the cell fraction reduced to the held fraction β

`scripts/cell_fraction_reduction.py`. A derivation of f must supply the imprint
clock and the coherence scale; self-similarity constrains both jointly, and the
elimination is computable:

- single-epoch census: n_s = 4 (the recorded excluded branch);
- mode-scaled clock with CONSTANT physical ξ: f = H·ξ at crossing ⟹ f ∝ k² in the
  radiation era ⟹ n_s ≈ 7, and f ~ 10⁻⁶ at the pivot — wrong scaling AND ~150×
  under the window. Dead twice over.
- mode-scaled clock with HORIZON-TRACKING coherence (ξ_eff = β·c_s/H): f = β for
  every mode — constant, self-similar, and verbatim the hunt's recorded scaling
  ruling. THE SOLE SURVIVOR: the clock is derived by elimination.

**The reduction: f = β**, the medium's early-era coherence-to-causal-range
fraction, with the triangle demanding β ∈ [1.0, 2.6]×10⁻⁴ and the closed form's
point at 2.21×10⁻⁴. The requirement β names: standard coarsening cannot hold a
fixed ordering fraction (coherence ∝ t^½ against horizon ∝ t) — the radiation-like
era must be scale-free (critical). Deriving β = deriving that critical fraction.
Two numerological temptations in range are recorded as temptations with weight
zero. β is now the program's single sharpest open number: one value closes #15,
gates #8, and referees #9.

## Addendum 3 (2026-07-27): the β derivation attempt returns a structured negative

`scripts/beta_holders_elimination.py`. Every standard mechanism class was run to
its scaling law: thermal coherence falls (∝ T/M_Pl); coarsening falls (∝ t^{−½});
critical-riding at the adiabatic–impulse boundary with the on-file ν = 2/3 falls
(∝ H^{0.6} — ~16 orders across the window). The ONE class that holds a constant
fraction — the scaling defect-network attractor — lands at 0.1–0.3, three orders
above the demanded 2×10⁻⁴.

**The named tension:** no standard class delivers a held fraction at the window.
Survivor space, named not asserted: (a) a dissipation-suppressed dense network
(~10³ density shift, mechanism unwritten); (b) a two-scale structure (network at
~0.1 of the causal range with coherent sub-cells at β — hierarchy factor ~500
unexplained); (c) an upstream revision of the imprint clock. **Sharpened kill:**
if no non-standard holder is derived, the β link fails and the envelope mechanism
loses its promotion path — the tilt's numerical success would then need a
different engine, and every other route is already route-eliminated.

**Consistency note from reconnaissance:** the retired height-field tilt route died
on "+1/ln, IR-anchored, wrong sign" — the conserved-charge conversion delivers
−2/ln, UV-anchored, passing the autopsy that killed its predecessor. Consistency,
not evidence.

## Addendum 4 (2026-07-27): the two-scale closure — the tension dissolves

`scripts/two_scale_closure.py`. β = γ/N₁, with the algebra/structure split stated
so nothing is double-counted:

- **Algebra (confirms nothing):** given the mechanism and the closed form, the
  identity β = γ/N₁ with γ ≡ (2π²/(r²L*²))^{1/3} is a rewriting.
- **New structure:** (1) the counting volume is PHYSICAL — the census count
  N₁³ = (4πk/α_c)³ lives per NETWORK CELL, closing the old factor-250
  "pivot-volume convention" question: it was never a convention, it was an
  unidentified physical volume. (2) The demanded network density lands INSIDE the
  vanilla scaling band: γ runs 0.20 → 0.10 across r ∈ [0.8, 2.0] against the
  standard reconnecting-network band 0.1–0.3 — no exotic network, no 10³
  suppression; the elimination's one surviving holder does the holding at its
  natural density. (3) Four observables sit on one rate with no strain at
  r ∈ [0.8, ~2.3]: A_s (construction), the tilt (mechanism), the isocurvature
  residual (0.7–2.0%, the registered band), the network density (vanilla band).

**The gates, localized and named:** (i) derive N₁-per-cell from the screened
interaction — the old normalization keystone, relocated from cosmology to a
local problem with a physical container; (ii) compute γ for the medium's own
network (reconnection ≈ 1, Goldstone losses; the vanilla band contains every
demanded value). Nothing promoted; the ledger carries the eliminations.

## Addendum 5 (2026-07-27): the per-cell count — decomposed exactly, cells narrowed, gate specified

`scripts/per_cell_count_structure.py`. The count is not derived; it is decomposed
and its owner named:

- **Exact decomposition:** N₁ = 4πk/α_c = (8R/π)·ln(1+R) = 4π/g_scr, with
  R = π/2α_c = 71.8 (the squared Fermi-to-screening scale ratio) and
  g_scr = α_c/k the Fermi-surface-averaged screened coupling. The count per
  dimension is the inverse screened coupling in loop units — structurally a
  Coulomb-log-weighted channel count.
- **Cell-identity elimination (ledger row filed):** particle-quanta cells die by
  e⁶⁰ (count ∝ a³ per network cell — tilt-destroying scale dependence). The
  surviving identity: network substructure (kinks/loops/wiggles), whose per-cell
  count is a pure number, constant in the scaling regime by construction.
- **The refined gate:** compute the substructure count per cell of a scaling
  vortex network with screened interactions at α_c — the small-scale cutoff where
  screened damping beats stretching. Demanded answer: 4π/g_scr per dimension.
  The Coulomb-log structural resemblance aims the computation at weight zero.

## Addendum 6 (2026-07-27): the keystone's candidate derivation — the cascade-cutoff closure

`scripts/substructure_count_closure.py`. The substructure count now has a
derivation at candidate grade:

- **The closure:** small-scale structure on the vortex lines (Kelvin-wave
  structure) is erased where cumulative emission beats the cascade. With a
  per-oscillation emission probability p = g_scr/4π (one perturbative vertex at
  the screened coupling — flagged identification) and L_net/ℓ oscillations per
  network time, the cutoff lands at L_net/ℓ_min = 4π/g_scr = N₁ = 783 — the
  recorded count as output, no tuning.
- **The bare-channel suppression (second flagged step):** order-unity Goldstone
  smoothing would kill the count; Kelvin structure is deeply subsonic at small
  scales with emission suppressed by high powers of v/c_s — the physics that
  lets laboratory quantum turbulence run Kelvin cascades 10²–10³ below the
  inter-vortex spacing. The medium's own exponent is uncomputed.
- **Class anchor:** the demanded 783 sits inside the hierarchy class laboratory
  superfluids already build.

**Promotion:** compute the medium's Kelvin-emission cutoff from recorded
parameters and land 4π/g_scr. **Kill:** that computation landing elsewhere, or
the bare channel proving unsuppressed. The keystone is now a specified
superfluid-turbulence computation with a demanded answer — the triangle's last
abstract link is physical.

## Addendum 7 (2026-07-27): the Kelvin cutoff computed — one flag resolved, one sharpened, one edge discovered

`scripts/kelvin_cutoff_compute.py`, recorded parameters only.

- **Flag (ii) RESOLVED BY COMPUTATION:** the bare (quadrupole) channel's
  per-cycle emission against the screened channel's: 8×10⁻¹⁴ at the largest
  observable scales, 9×10⁻⁴ at the pivot, narrowing to 7×10⁻² at the window's
  UV edge — the screened channel sets the cutoff throughout, margin reported
  exactly as it tightens. The bare-alone count is epoch-dependent (10⁵ → 1200
  across the window): its subdominance is REQUIRED for scale invariance and
  HOLDS.
- **Flag (i) SHARPENED:** the count's structure N₁ ∝ 4π/g_scr stands; the exact
  prefactor awaits the vertex derivation. Consistency: the identical 4π loop
  convention is already fixed in the recorded closed form — one convention, two
  appearances, zero freedom once the vertex lands.
- **THE UV VALIDITY EDGE (new, named exposure):** the cell size tracks the
  causal range while the core is fixed, so ℓ_min/ξ shrinks toward early times
  and saturates at z ≈ 8.9×10⁴ — k_edge ≈ 0.26/Mpc, essentially at the
  observable window's boundary. Beyond it the imprint construction cannot
  continue unchanged; the consequence for smaller scales (the Lyman-α range,
  k ~ 1–3/Mpc, where data reads the spectrum as roughly standard) is
  UNASSESSED. Filed as its own task.

## Addendum 8 (2026-07-28): the vertex flag reduced to one property; the screening structure unified

`scripts/screened_vertex_reduction.py`, with the host result of
`scripts/host_mismatch_mu_resolution.py` (hierarchy §6n) feeding it.

- **Structure check (exact):** R = π/2α_c is not an independent input — it is
  the backscattering range over the booked screening mass, R = 4k_F²/m_D² with
  m_D² = 8α_c k_F²/π. R, m_D², k, and g_scr are one screening object seen four
  ways, and §6n's finite-μ result hosts all four at once (the hot basement
  screens cold when μ-dominated; condition μ/T ≳ 18, arrow-sourced, task #16).
- **k re-verified independently:** the Fermi-surface average of the screened
  exchange over the full backscattering range reproduces the closed form to
  9×10⁻¹² relative, with the landing conventions printed openly (per-band
  density of states with both spins, two velocity-matched bands,
  pairing-channel ½, transfer measure q dq/2k_F²).
- **Flag (i) reduced, not closed:** the golden rule gives P_cycle = g_scr/4π
  exactly when the emission has WEIGHT ZERO — |M|² = 1 under the unit s-wave
  measure, no velocity suppression (that is the computed-subdominant dipole/
  bare channel), no phase-space enhancement. The remaining gate is the
  weight-zero exhibit for the erasure channel; identifying the microscopic
  process is owed, and is not invented here.

**The keystone's gates after tonight:** (a) the weight-zero exhibit;
(b) the μ ≫ T host condition (#16). Both sharp, neither promoted.

## Addendum 9 (2026-07-28): the validity edge assessed — a referee, not a wound

`scripts/uv_edge_assessment.py`. Beyond the edge (k_edge = 0.262/Mpc,
recomputed) the realized count per cell falls as N₁·(k_edge/k)² — 54 by
k = 1/Mpc, 6 by 3/Mpc — and the cascade cannot terminate within one network
time. That makes the edge a DISCRIMINATOR between the amplitude's two
normalization readings, which is exactly task #15's question: the
coupling-normalized reading (the closed form's literal structure, three powers
of g_scr/4π) is flat through the edge and the Lyman-α range's recorded
roughly-standard power is an automatic consistency; the count-normalized
(shot-noise-class) reading breaks blue as (k/k_edge)⁶ — ×3×10³ in power by
k = 1/Mpc — and is excluded by the recorded sky. The small-scale data thereby
constrain #15's gate from the observation side: the weight-zero exhibit must
land coupling-class. #25's promotion rides on that landing; its kill applies
only to the reading the sky already disfavors.

## Addendum 10 (2026-07-28): the residual gate checked — one object read twice

`scripts/ns_residual_gate_check.py`. Gate (2) of the tilt's promotion: over the
construction's surviving band r ∈ [0.8, 2.3], the mechanism's correlated
residual S/ζ = 1/(rL) spans 0.70–2.02% — the percent class that P-2026-031
registers as the isocurvature line's amplitude. Consistency passes across the
whole band; the r ≲ 0.1 tension zone lies outside it. The tilt now waits on
one gate only: the rate normalization (task #15's weight-zero exhibit), with
P-2026-031's external referee (a CMB bound at ℓ ≈ 170) unchanged.

## Addendum 11 (2026-07-28): the weight-zero hunt — four channels priced out, one lands with zero dials

`scripts/weight_zero_channel_pricing.py`. Every standard erasure-channel shape
priced against the demanded p = g_scr/4π = 1.277×10⁻³ at the pivot's cutoff
geometry (ℓ_min/ξ = 25.0, Kelvin Mach 0.064):

| channel | result | verdict |
|---|---|---|
| quadrupole (bare) radiation | M⁵ = 1.1×10⁻⁶, ×8.6×10⁻⁴ of demand | wrong shape (velocity powers); cross-validates the recorded bare suppression |
| contact particle-hole damping | [λ², π²λ²] = ×0.70–6.9 of demand | right order, wrong structure: ∝ k² where the demand is ∝ 1/k |
| reconnection | geometric, not ∝ g_scr | wrong shape |
| resonant mode conversion | \|M\|² → 1 only at kξ ~ 1 — the UV edge | holds nowhere in the window except the edge |
| **pairwise screened de-excitation × occupancy-one** | **p = g_scr·1·(1/4π) — exact, no dial** | **the surviving candidate** |

The landing channel's unit partner count is the corpus's occupancy-one
principle — the same principle that prices ρ_Λ — and the 1/4π is the
unit-normalized isotropic measure of the one partner, weight zero because
screened exchange is contact-class below the screening scale. The keystone's
remaining exhibit is therefore ONE corpus-native identification: occupancy-one
governs the network's substructure cells as it governs the condensate's
binding quanta. The UV edge's takeover by resonant conversion at ℓ_min = ξ is
consistent with the edge's referee role (Addendum 9) rather than an anomaly.
An in-file erratum records that v1's bare channel was written as a dipole and
refused by its own assert — vortex momentum conservation forces the
quadrupole, and the corrected number matches the recorded suppression.
