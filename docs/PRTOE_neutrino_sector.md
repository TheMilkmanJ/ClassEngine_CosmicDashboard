# The Neutrino Sector — Dark Energy Weighs the Neutrino

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> This consolidates the model's most experiment-facing claim block.
> Components range from recorded (the Majoron structure, P-2026-012/020) to exploratory
> (the ρ_inf closure, on review hold). The relevant tests are ton-scale 0νββ (nEXO, LEGEND-1000,
> CUPID) and next-generation cosmology.

> Status: the mass relation and 0νββ window are established; the remaining open items are the
> exact μ value, the flavor-distribution calculation, the Majoron mechanism's next falsifiable
> consequence, and the ρ_inf closure.

## 0. The claims, stacked

1. If neutrinos are Majorana in this model, the 0νββ process should exist (P-2026-020). The
 observable rate still carries the §3 phase-cancellation caveat: m_ββ can sit as low as 0.04 meV at
 unlucky phases. The falsification is one-directional: a detection above the ceiling kills the
 model, while a null at any sensitivity does not. Dirac nature cannot be demonstrated directly; it
 can only be inferred from nulls together with the absence of other Majorana channels.
2. The lightest mass is the fourth root of the dark-energy density: m₁ = ρ_Λ¼ = 2.25 meV
 (the lepton-number-breaking scale associated with the Majoron sector — PRTOE_MATH_SPINE.md
 §6; "Majoron" = the Goldstone boson of spontaneously broken lepton number). This is a relation,
 not a coincidence: the model ties the lightest neutrino mass to the dark-energy scale through
 m₁ = κ_m·ρ_inf¼ with κ_m ≈ 1; see the addendum below.
 What the model does not do is derive the value 2.25 meV itself; that is the dark-energy-value
 problem (§2). The claim is that one un-derived number does two jobs that standard cosmology treats
 as unrelated, not that the number is explained.
3. The sum: with measured splittings, Σm_ν = 61.4 meV, **normal ordering** (the ordering
 favored by the registered P-2026-004 prediction-collision test, not by P-2026-012, which does
 not fix it — ANN-2026-025). **This number is not a discriminator**: it sits 2.6 meV above the
 m₁ = 0 floor of 58.8 meV, against a planned cosmological resolution of ~20 meV. The distinctive
 content is in m_ββ (§3), which is sensitive to m₁ where the sum is not.
4. The exploratory closure is that an occupancy-corrected derivation of ρ_inf (the model's
 constant dark-energy floor density — the quantity that plays the role of ρ_Λ) reproduces the
 same sum by an independent route through the recorded relation chaining ρ_Λ, the derived scale
 M₂ = α²·T_c, and 3α; the running α_c chain checks that claim.

## 1. Why this block is the model's tightest constraint

Every claim is measurable this decade, and none is adjustable: (i) ton-scale 0νββ experiments
reach the normal-ordering floor's neighborhood — a confirmed Dirac nature (0νββ nulls at full
sensitivity plus other Majorana channels closed) kills claim 1; (ii) cosmology's Σm_ν sensitivity
(DESI+CMB) is already brushing 60–80 meV. Two kills live here, and the likelier one comes from
below: a robust Σ > 70 meV kills claims 2 and 3, but so does a ΛCDM-conditional upper limit
descending through 61.4 meV, which is the direction the frontier is actually moving. The model's
answer is that those limits are ΛCDM-conditional and the squeeze relaxes under its own
recombination history — a testable claim, and the fastest route to grading this block. Inverted
ordering from oscillation experiments also kills claims 2 and 3; (iii) an in-house tension:
P-2026-023's de-biased band (0.07–0.09 eV) sits above this block's 0.061 — the running chains'
own posterior arbitrates between the model's two
neutrino numbers.

## 2. The mechanism's open items

The parameter μ that ties the dark-energy floor to the lightest neutrino mass is a dimension-1
lepton-number-breaking parameter, distinct from the dimensionless varying-m_e amplitude.
What remains un-derived is the *value* μ = 2.25 meV (the
dark-energy-value problem). Remaining open items: the Majoron mechanism still needs a new falsifiable
consequence, and the ρ_inf closure depends on the running α_c chain.

## 3. For 0νββ specifically

The model's effective mass, computed from m₁ = 2.25 meV + normal ordering + NuFIT-class
mixings (sin²θ₁₂ = 0.307, sin²θ₁₃ = 0.022): the three mass contributions are
|U²m| = (1.52, 2.67, 1.10) meV, giving

> **m_ββ ∈ [0.04, 5.3] meV over free Majorana phases, ~3.3 meV typical**

— below ton-scale reach (nEXO/LEGEND-1000 target ~5–20 meV). The model does not predict the
Majorana phases, so the position within that window is unconstrained; that is an open item.

The floor is real but not protected by a symmetry, and it is sensitive to the anchor. It exists only
because the middle term exceeds the other two combined — 2.67 against 2.62 at m₁ = 2.25 meV — so the
three phasors cannot close a triangle and exact cancellation is impossible. The margin is 0.05 meV
on terms of order 2.

**The margin's sign is a coin toss on today's data, and where the coin lands is itself structured
(computed 2026-08-02, `scripts/funnel_edge_identity.py`, 9 controls).** At the global-fit central
values (NuFIT 5.0: sin²θ₁₂ = 0.304) the margin's sign flips to −0.0002 meV: the floor's existence
is decided by which side of the closure threshold m₁ sits on, and the 1σ band on the margin,
±0.24 meV, is dominated by θ₁₂ and makes the sign a 50/50 draw. The threshold itself — the smallest
m₁ at which exact cancellation first becomes possible, the lower edge of the well-known
normal-ordering "funnel" — computes to **m₁\* = 2.2496 meV at current centrals, against
ρ_Λ^{1/4} = 2.2395 ± 0.0108 meV: agreement to 0.45%, i.e. the registered m₁ sits ON the closure
threshold**, a coincidence found stated nowhere in the funnel literature (three searches, null).
Exact cancellation at the threshold occurs at exactly one phase point, and it is CP-conserving:
(α₂₁, α₃₁) = (π, 0). JUNO (θ₁₂ and Δm²₂₁ below 0.5% by ~2031–32) tightens the threshold's error
to 0.06 meV, after which θ₁₃ — frozen at Daya Bay's final precision, with no successor planned —
gates the test at ~3% and the sign stays uncalled if the true margin is under ~0.04 meV. What
would decide it structurally is recorded with its price at the registry annotation to P-2026-012:
a closure mechanism exists in the literature (ee-texture zero, symmetry-protected, viable only in
normal ordering with m₁ pinned to the funnel) but is flavor structure, which this model's own
constitution declares not writable — and adopting it would invert the discriminating band above
into a falsifier, since it predicts m_ββ = |margin| ≲ 0.05 meV, no observable signal.

The model's derived dark-energy scale sits 0.44% from the observed value: the observation is at
2.25 meV and the current derived anchor from the composite quartic lands at 2.2599 meV. **This small
gap is not a propagated uncertainty or formal error bar.** The derived value carries a radiative
correction bounded at 0.10–0.90%
([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md), the control-edge
re-examination), comparable to the gap itself. The quoted 2.2599 meV is therefore best read as an
anchor comparison rather than a fully converged model prediction.

The sum is insensitive to this: Σm_ν varies only from 61.34 to 61.37 meV across the observed
range, which is why it is quoted as 61.4 meV. The effective mass floor is more sensitive due to
near-cancellation. It shifts from 0.050 meV (at the low edge of the observed range) to 0.038 meV
(at the derived anchor), while the ceiling remains stable at ~5.30 meV in either case. The window
is therefore quoted as **m_ββ ∈ [0.04, 5.3] meV**. (The derived anchor sits 2.8% below the
2.324 meV threshold where the floor vanishes entirely.)

The floor is the soft end of the window and nothing observable rides on it — it is two orders
below any experiment's reach on any timeline. Every conclusion in this file and in the
experimental overlay turns on the ceiling, which the anchor barely moves.

One consequence is worth stating for the double-β community: the near-cancellation makes **m_ββ an
unusually sharp probe of the dark-energy scale**, since small changes in m₁ move it hard.

The prediction's value is structural: (i) 0νββ must exist if the model's Majorana assumption is
correct, so evidence for Dirac nature ends this sector — though that evidence can only ever be
indirect; (ii) the normal-ordering floor's shape is fixed in advance; (iii) **one experiment,
and only one, can reach this model.** Projected 10-year
reaches (each span is the matrix-element range): nEXO 4.7–20.3 meV, LEGEND-1000 9–21 meV, CUPID
12–34 meV. Against a model ceiling of 5.30 meV, LEGEND-1000 and CUPID sit entirely above and cannot
touch it at any matrix element; **nEXO overlaps at 4.7–5.3 meV** if the ¹³⁶Xe matrix element falls
at the favourable end. Over flat Majorana phases the model exceeds 4.7 meV about **10.8%** of the
time, so nEXO carries a roughly one-in-nine chance of a confirming signal, conditional on both the
model and the matrix element. Outside that thin band a detection falsifies the model outright, and a
null constrains nothing — a null is consistent with phase cancellation at any sensitivity.

A factor-of-four half-life gain — the barium-tagging upgrade nEXO's collaboration has
projected — is √4 = 2 in m_ββ, taking the reach to ≈ 2.35 meV and the detection probability
from 10.8% to **69%**. It does not
buy discrimination: minimal normal ordering (m₁ = 0, window [1.48, 3.69] meV) exceeds 2.35 meV
**63.7%** of the time, so a tagged detection there separates almost nothing. **The discriminating
band is 3.69–5.30 meV** — above minimal ordering's hard ceiling, below this model's — where minimal
ordering is impossible at any phases and this model lands **31.7%** of the time. All of baseline
nEXO's 10.8% falls inside it. Tagging makes the test likely; the baseline machine makes it decisive.

0νββ has never been observed — the one historical claim (Heidelberg–Moscow, ~200–600 meV) was
refuted by KamLAND-Zen and GERDA; current limits (m_ββ ≲ 28–180 meV, depending on the nuclear
matrix element) sit 5–30× above this band, so no existing measurement executes either side of
the kill clause. Cosmology will grade this
sooner; the ton-scale program grades it more cleanly. DESI-era CMB+BAO limits already reach
Σm_ν ≲ 72 meV (with some combinations pressing lower, toward the normal-ordering floor
itself) — this model's Σ = 61.4 meV sits just inside, and the frontier is actively
squeezing. This sector may be graded within one to two years by exactly that number.

## 3b. The second channel — Majoron emission, and why it is the wrong instrument

There is a second neutrinoless mode: **0νββχ**, where a Majoron is emitted alongside the two
electrons. It is a genuinely different observable. The mass mode puts the electron sum-energy at a
sharp peak on Q_ββ; the Majoron carries energy away, so this mode is a **continuum**, and
experiments search for it separately.

The rate is not free here: the model's Majoron is a mass-basis-diagonal singlet, so its coupling
matrix is g_ij = (m_i/v_L)δ_ij and the effective coupling that drives double beta decay is

> **⟨g_ee⟩ = m_ββ / v_L**

— the *same* m_ββ that governs the mass mode, divided by the lepton-number-breaking scale. Nothing
new enters. (Consistency check: the recorded g₃₃ = 1.2×10⁻⁸ returns
v_L = m₃/g₃₃ = 4.18 MeV, the MeV-scale point's own value.)

What is not pinned is v_L, which still has two viable parameter points. Both are priced:

| parameter point | v_L | ⟨g_ee⟩ at m_ββ = 3.05 meV | T½(¹³⁶Xe) |
|---|---|---|---|
| the MeV-scale point | 4.18 MeV | 7.3×10⁻¹⁰ | 3×10³² – 1×10³³ yr |
| the high-v_L point, GeV end | 1 GeV | 3.1×10⁻¹² | ~2×10³⁷ yr |
| the high-v_L point, at its 2.4 TeV ceiling | 2.4 TeV | 1.3×10⁻¹⁵ | ~10⁴⁴ yr |

*(Each half-life span is the matrix-element range, calibrated on KamLAND-Zen's published
ordinary-Majoron limit: T½ > 2.6×10²⁴ yr at ⟨g_ee⟩ < (0.8–1.6)×10⁻⁵, arXiv:1205.6372.)*

The conclusion does not need the parameter point resolved. Even at the most favourable one the
Majoron mode is **four orders of magnitude slower than the mass mode**, which is itself already
just past nEXO's baseline reach; the coupling sits four orders below the experimental limit,
which is eight orders in rate. **The model predicts no observable Majoron mode, at every
surviving parameter point** — a kill-only bet of the same shape as the indirect-detection and
laboratory zeros.

Two things make this more useful than a null.

The coupling is measurable by a CMB experiment, not a ββ experiment. CMB-S4's Majoron search
reaches g ~ 10⁻⁸–10⁻⁹, and the model's largest coupling, g₃₃ = 1.2×10⁻⁸ (which involves
m₃ = 50 meV rather than m_ββ = 3 meV), sits inside that band. CMB-S4 is roughly **four orders
more sensitive to this coupling than 0νββχ is**, and it is already the registered discriminator: a
detection there selects the MeV-scale point and its resonant-leptogenesis lane, while a null favors
the high-v_L point. The best probe of the Majoron coupling is not a ββ experiment.

And the peak search is clean of this background. A Majoron continuum under the 0νββ peak is a
recognised complication for the mass-mode search. This model says there is none at any reachable
level, which is a small positive statement for the ton-scale program rather than merely an absence.

*Computed at the same matrix-element uncertainty the mass mode carries, and using the model's own
g = m/v_L relation. Some singlet-Majoron treatments carry an additional seesaw suppression on top
of that; it would push the rate further down, so "unobservable" survives either way.*

## Sources

[SNO 2002]/[Super-K 1998] (oscillations), [Planck 2018] (Σm_ν context); internal:
PRTOE_MATH_SPINE.md §6, [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md),
P-2026-012/020/023. Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## 4. Addendum — one vertex, two roles

The baryogenesis transfer computation's first run requires a portal coupling y ≈ 0.7–3×10⁻⁵;
the seesaw vertex that gives neutrino masses is y ≈ 1.3–1.8×10⁻⁶. They are the same order of
magnitude, within a factor of 4–20 in the crude rate estimate. If the detailed calculation
closes that gap, the same vertex could account for neutrino mass and the baryon asymmetry,
provided the portal carries no lepton-number channel.

Including the resonance condition μ ≈ Γ_N pushes the required coupling roughly 100 times larger,
so a single vertex does not easily do both jobs at TeV-scale M. The shared-vertex picture only
survives if leptogenesis is non-resonant; then v_L ≥ GeV and the Majoron coupling is too small for
CMB-S4. CMB-S4 can test that point: a detection at g ~ 10⁻⁸–10⁻⁹ would favor the shared-vertex
picture; a null would favor the high-v_L point.

---

## The mass-generation channel and the lightest-mass relation (2026-07-18)

In this model the neutrino mass splittings come from the seesaw, while the lightest neutrino mass is
tied to the dark-energy scale. At the surviving parameter points (either the MeV-scale or the
TeV-scale lepton-number-breaking scale, both consistent with the model's constraints and selected by
CMB-S4), a Yukawa coupling of about 6×10⁻⁷ reproduces m₃ = 50 meV. The lightest eigenvalue can
still sit far below 1 meV in the seesaw sector.

The absolute floor is different: the lightest mass is written as

> **m_ν,lightest = κ_m · ρ_inf¼, κ_m ≈ 1**

This is the mass relation used in the model. It does not mean the model derives the observed value
2.25 meV from first principles; that value remains the dark-energy-value problem. It does mean that
the same lightest-mass scale appears in both the dark-energy sector and the neutrino sector.

The relation ρ_Λ¼ = m_ν,lightest is therefore a mass-generation identity, not a thermal
coincidence. The dark-energy floor sets the lightest neutrino mass, and the last neutrino species to
become non-relativistic does so at that scale. The freeze-out dynamics remain the mechanism that
connects the mass relation to the thermal history; the relation itself is the source of the tie.

What is still open is how the mass term is distributed across the three neutrino eigenstates. The
simplest operator at the medium level is flavor-blind, so a state-selective result has to come from
the dynamics, not from the operator alone.

The operator above the lepton-number-breaking scale is

> **O_A = (c_A/v_L)·Φ_med·σ_L·ν̄₁ᶜν₁ + h.c.**

(Φ_med is the medium's scalar field; σ_L carries the lepton-number-breaking expectation value.)
It is a dimension-5 operator with the cutoff set by the symmetry-breaking scale itself. Below
v_L it reduces to the lightest-state Majorana term. The associated Majoron coupling is

> **g = m₁/v_L**

which gives g = 5.4×10⁻¹⁰ at the MeV-scale point (v_L = 4.18 MeV) and g = 9.4×10⁻¹⁶ at the
TeV-scale point's 2.4 TeV ceiling. That keeps the UV completion safe with respect to supernova
limits and makes the Majoron signal far below current ββ limits.

The remaining open pieces are:

- the pure number b in ρ_inf = b·m₁⁴,
- the detailed settling calculation that decides how the mass term is shared among the neutrino
  eigenstates,
- and the running α_c chain that checks the occupancy-corrected ρ_inf closure.
