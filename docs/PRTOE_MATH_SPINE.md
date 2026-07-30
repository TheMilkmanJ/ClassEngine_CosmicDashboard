# PRTOE — THE MATH SPINE (genesis → now → end)

> The headline result: the dark-energy scale is
> **ρ_Λ¼ = (9/2)·α⁴·τ·m_e** — α⁴ times a temperature tied to the electron. Every factor is sourced
> except τ = T_c/m_e, and τ is where the claim lives.
>
> τ is sourced by the lepton-mass relation, and nothing cosmological enters. The linear-algebra
> kernel fixes its own modulus through Parseval: Q = 2/3 forces |f₁/f₀| = 1/√2, hence
>
> > **τ = ½ln2 ⟹ T_c ≈ 177 keV ⟹ ρ_Λ¼ lands on the observed dark-energy scale, with nothing
> > cosmological in the chain.** *(An existence claim. The decimals are given in
> > [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md), where the radiative control
> > that would be needed to defend them is also priced.)*
>
> descending from Q, a lepton-mass fact measured to ten parts per million, through an exact identity
> ([PRTOE_koide_relation.md](PRTOE_koide_relation.md)).
>
> It is an **existence** claim — that the chain
> lands on the observed scale with nothing cosmological in it — and **not a precision** claim. The
> composite quartic maps to λ = 26–46, the whole band above the control edge λ\* = 22.41, so the LHY
> correction is uncontrolled at this order on every reading: its formal size would be 5.4–9.8% on
> ρ_Λ¼, while the next term of the same series is already larger. The agreement is therefore good to
> the order the series can be trusted, and the two decimal places are not the claim.
>
> This is a conditional claim, and its price is one hypothesis: that the charged-lepton √m values are
> thermally populated, which is what Q = 2/3 asserts (the variance of √m equals the mean squared,
> the Boltzmann second moment, to 18 ppm). **Its referee is one number:** a lattice T_c/√σ for
> SU(2), N_f = 3. **And it is one job, not two:** the same non-perturbative calculation that fixes
> τ is the one the radiative band needs, so the λ and τ gates open together.
> A lattice return at 0.34657 crowns the kernel and the dark-energy prediction together; one at
> 0.34506 shows the model reading the sky back, and kills both.


> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*2026-07-10. The full quantitative chain in one document: every epoch, its governing equation,
what is derived vs input vs phenomenological, and where it lives in the code. Cross-references:
PRTOE_me_mechanism_math.md (electron-mass sector detail), PRTOE_cyclic_torus_genesis.md
(origin narrative), PRTOE_UV_completion.md, PRTOE_cosmological_constant.md (J1).*

---

## 0\. The objects

One dark superfluid, two components (the two-field split):

* **Field 1** — the dCDF fluid: charge/abundance carrier, DM+DE unified. Mass m = 2.24×10⁻²⁰ eV
[**MEASURED** via the onset clock. **The "three independent ways" wording is withdrawn
(2026-07-28, circularity sweep, check 34)** and the three legs now read: **(1) ξ is circular** —
ξ ≡ ħ/(m c_s) is *defined* from m and the "recorded 402 AU" is itself computed from m, so 398
against 402 compares two computations from the same input, differing by rounding. No measurement of
the coherence length exists. **(2) the Schive core radius is unresolved but may be real** — the
external relation goes as 1/m and the model's own as 1/m², so they intersect at one m only and
agreement *would* pin it, provided the model's normalization was not set from this comparison
(provenance not established). **(3) the superradiance window** returns 7.14 pc / its recorded
6×10⁸–3×10⁹ M☉ — **and that third one is support and exposure in the same object**: the band is
populated and carries high measured spins,
and the model brings no defence there, the λ-quench margin computed at its own quartic and mass
being −83.7 to −85.8 decades across α_g = 0.1–0.5, so P-2026-034 stands or falls on the spin
measurements alone. Under the onset clock T_on = √(m·M_red/0.61) this mass sits at
**z_on = 4.03×10⁷ (log₁₀ 7.605)**, which is the value `include/background.h` carries as the derived
identity and which five of the six production configs set. *(The free-z_on optimizer lands at
log₁₀ z = 7.5517, which implies m = 1.75×10⁻²⁰ — 22%
**below**, a mass that misses all three checks above by ~28%. The grade stands on the three
independent uses, not on that landing.)*
The route "derived from ε via c(m) = (m/m₀)^{1/4} at c = 1" belongs to the
f_amp decomposition, not this one — in the standing decomposition ε = c·f̄·α_c the mass never
touches the census c, so **no roster-trial re-pricing propagates to m, z_on, or the hinge through
this route** (the hinge keeps only its α_c conditionality via c_s = √α_c). That curve is closed by
its own arithmetic in any case: it would force c = 1.005 while the census excludes
c = 1. Provenance walk].
The dark condensate fluid branch itself is already on the derived side of the ledger at the
structural level: exact `w = −1`, derived `H = m` onset/crossover, finite quartic floor, and the
topological winding/chirality assignment. The open residue is the residual magnitude and the
sign/correlation junctions, not the component's existence.
* **Field 2** — the electron-coupled scalar: charge-free, couples to the electron; its condensate
sources δm_e. (Lepton-sector, and **a separate field from the Majoron**: the one-scale corner
f = v_L is tie-dead on the condensate-friction ceiling, so the sector carries two L-breaking scales
and three dark fields. What stays open is *which* v_L corner — TeV-class or MeV — and CMB-S4 is the
selector ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §6). **The portal's un-derived core
is which Standard-Model scalar the dark-neutral bilinear |Ψ|² multiplies.** The standing operator
is the quadratic-canonical m_e(φ) = m_e0(1 + κφ²), and the recorded roster of dark-U(1)-invariant
couplings — |Ψ|², |Ψ|⁴, ∂_μΨ*∂^μΨ, J_μ — reaches δm_e only through |Ψ|², which is a total
singlet: Lorentz-scalar, dark-neutral, gauge-neutral, **and L-neutral**. What carries
leptophilia here is **data**: BBN kills the quark bilinear at ≥ 12σ through the D/H
quark→pion→deuteron channel; lepton number screens nothing, because the Majoron's current
couples to the phase and a phase-blind |Ψ|² operator cannot see it. The symmetry that does bite
runs the other way — it forces the portal **even** in the dark field, which is why the operator
is quadratic-canonical rather than linear. The Standard-Model side of that portal is the
headline result's one assumed step, and the block below states it.)

> **THE PORTAL'S STANDARD-MODEL SIDE — the assumed step, stated (#125).** The dark side is
> settled: the operator is even in that field and |Ψ|² is its leading invariant. A dimension-2
> dark singlet then has three couplings available, and they order by **dimension**, not by
> preference:
>
> | the SM factor it multiplies | total dimension | what it delivers | status |
> |---|---|---|---|
> | **H†H** | 4 — the only renormalizable one | a Higgs-vev shift, so **every** mass including the quarks | excluded at ε (a universal shift is +12–18σ on D/H); its coefficient is bounded λ_p ≲ 5×10⁻¹¹…1×10⁻⁹ across f = 100–500 TeV |
> | **L̄He**, the charged-lepton Yukawa (→ m_e ψ̄ψ after EWSB) | 6 | δm_e alone — **the standing choice** | assumed |
> | **(LH)(LH)**, the Weinberg operator | 7 | δm_ν alone; it cannot reach δm_e at any coefficient | not the deliverer |
>
> **Doing without the renormalizable one is affordable, and that is computed rather than asserted.**
> The standing dimension-6 lepton operator feeds back into H†H through one electron loop at
> λ_p ≤ 1.1×10⁻¹³ — from ~500× under the bound at its tightest corner (biggest cutoff, biggest f)
> to ~10⁶× under at the loosest — so the universal shift it induces reaches at most 2×10⁻³σ on D/H.
> Setting the
> renormalizable portal aside costs no tuning inside the effective theory. What it assumes is that
> the completion above f writes the lepton operator without the other two, which is the assumption
> λ_dyad's origin already carries.
>
> **And the choice that is actually being made is finer than the roster's.** Writing the dark
> bilinear into the lepton **doublet's normalization** — rather than into each mass operator
> separately — correlates the two: the charged mass carries one power of L and the Weinberg operator
> two, so δm_ν/m_ν = 2·δm_e/m_e exactly, one coefficient in place of two. Nothing selects between
> that correlated point and independent coefficients — a gauge singlet couples to every Yukawa
> operator with its own coefficient — and **nothing can**: inside the window the correlated point
> moves each neutrino mass by 2ε, 1.5 meV on Σm_ν, while the sky measures the unshifted present-day
> value, so the two readings are observationally identical. The pipeline runs the correlated point
> (`background.c`, m_ν ∝ m_e²). **Assumed** — docket #125, desk work with no external gate.

The amplitude — the model's one distinctive number — assembled from three factors, each graded by a
running instrument:

> **ε = c·f̄·α_c = 27α/5π = 1.2543%** (concordance joint 1.2403 ± 0.0079%), with
> - **c = 9/10** — a counting fraction (N−1)/N over the universal charged-fermion roster: 9 charged
> species plus the vacuum's own seat, the neutrinos sitting on the seat rather than in the count
> because their mass is medium-sourced rather than electroweak. **The value is data-selected, not
> framework-required:** the step that licenses a democratic count at all is open
> ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1, the two-census marriage), and what the
> value rests on independently is the ε-blind ensemble — c = 0.903 [0.867, 0.942], −0.08σ from 9/10.
> **That ensemble confirms and does not select.** At its width it sits +0.53σ from the
> neutrino-inclusive 12/13 and −0.38σ from the charge²-weighted 8/9, so it excludes neither. The
> binding pair is 9/10 against 8/9, separated by 0.0111, and discriminating hypotheses at that
> spacing requires a width well below it: 3σ requires σ_c ≤ 0.0037, a 10× sharpening and — since
> ensemble width falls as 1/√N — roughly 100× the data. That width is not in hand.
> What picks 9/10 over 12/13 is the tie-as-lock argument, not the measurement;
> - **f̄ = 2/π** — the winding time-average, the mean-absolute-sinusoid ⟨|cos|⟩, set by the
> winding's many-turn equidistribution; the coupling form is now data-selected (2026-07-16):
> mass-positivity kills the signed average (⟨cos⟩=0), leading-order (Yukawa, linear) picks
> mean-absolute over the quadratic/RMS readings, and the fit (0.625) + sim (0.635) confirm 2/π,
> rejecting RMS (0.707) at +13% — residual only "leading-order dominates";
> - **α_c = 3α = d·α** — **the dark condensate fluid's** condensate coupling (α is its
> Goldstone's — light *is* that Goldstone), the 3 being the spatial dimension d (second sound,
> geometry, and the induced loop-trace agree); the value a bet graded by the α_c MCMC.

> **Whose coupling is whose — the two fields behind the headline result, stated (2026-07-17).**
> ½α_c²M₂ hides that the dark-energy scale is a **cross of BOTH dark fields**, not one field's
> product. Substituting α_c = d·α and M₂ = α²·T_c collapses it to a closed form (verified identical
> to 4×10⁻¹⁹):
>
> > **ρ_Λ¼ = (d²/2)·α⁴·T_c = (9/2)·α⁴·T_c**, which on the kernel's τ gives **2.2599 meV against the observed 2.25 — a +0.44% OFFSET, i.e. ~1.8σ on the observational error** *(2026-07-28: the theory side carries no free parameter, so the 0.44% is a discrepancy rather than a tolerance; ρ_Λ¼ inherits ~0.25% from Ω_Λ's ~1%. The claim is that the chain lands on the right SCALE, not on the value — the quartic sits past perturbative control, so the digits are not a precision claim — head of this file)*
>
> | factor | owner | why |
> |---|---|---|
> | **α⁴** = α_c² × α² | **the dark condensate fluid** | α_c² is its **binding**; α² is the **electromagnetic coupling** — and α is the dark condensate fluid's own coupling because **light is its massless Goldstone** ([PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §4) |
> | **T_c** | **the electron-coupled scalar** | its condensation temperature, **177.10 keV** from the kernel's τ = ½ln2 |
> | **d²/2 = 9/2** | **geometry** | d = the spatial dimension (the same 3 as in α_c = 3α) |
>
> **Neither field produces the number alone**: the dark-energy scale is the dark condensate fluid's
> coupling raised to the fourth **weighing the electron-coupled scalar's condensation temperature**.
>
> > **The T_c row's owner is not settled, and the "cross of both fields" reading is the part that
> > depends on it.** This table assigns 177.10 keV to the electron-coupled scalar.
> > [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §6 assigns the headline result's τ·m_e to
> > the **SU(2) confinement scale** instead, and states that the electron-coupled scalar is neither
> > of that sector's two condensates.
> >
> > **The recorded chain leans to §6, on three independent points.** τ is *defined* as T_c/√σ — a
> > ratio to a confining string tension, which the electron-coupled scalar does not have; the one
> > dimensionful input is the **portal √σ_dark = m_e**, a statement about the confining sector; and
> > the referee registered for τ is a **lattice T_c/√σ for SU(2) with N_f = 3**. All three make T_c
> > the confining sector's transition, and §6 records that sector's diquark condensate as *being*
> > the dark condensate fluid. On that reading α⁴ and T_c both belong to the dark condensate
> > fluid's sector, and the dark-energy scale is **one sector's product, not a cross of two fields.**
> >
> > The arithmetic is identical either way — the two scales sit near the electron mass for separate
> > reasons, the portal in one case and the electron loop in the other — so nothing downstream of the
> > number moves. What moves is the structural claim in bold above, which should be read as
> > conditional until the assignment is ruled on.
>
> *(The decomposition is
> [PRTOE_build_2loop_Veff_spec.md](PRTOE_build_2loop_Veff_spec.md)'s, hunt 210–211; it is restated
> here because every reader-facing statement of the headline result wrote ½α_c²M₂ without saying
> which of the two condensates α_c belongs to — and the model has two.)*


## 1\. Genesis (the cycle's start)

Compact torus topology survives the bounce (topology holds what dynamics loses); the confined
reheated flow develops a fountain-effect / thermal-counterflow response and rolls up into a helical
vortex ring (blueshifted crunch radiation) → re-establishes the rotation. The compactness / Casimir
intuition explains why the spectrum is discrete and the axis survives, but it does **not** by
itself supply the bounce-sector `ρ_X(T)`.
Flat 3-torus registered as P-2026-013. **BKL and Tolman still obstruct the bounce rungs — this
layer is a phenomenological summary built from real mechanisms, not a derivation.** This is the
bounce/genesis flow, not the census-imprint scaling law, and the topology/Casimir reading is only
a structure helper, not the missing handover term.

## 2\. Radiation youth → dark matter (the first transition)

Above H ≈ m the ultralight field is frozen/radiation-like (w=1/3, the conformal-origin
phase); below, it oscillates as dust. The switch epoch:

> **T(H=m) = √(m·M_red / 0.61) = 9.46 keV** (g*=3.36) ↔ **coded z_rad_onset = 4×10⁷ → T = 9.39 keV.**

Match 1.007×. The onset is field 1's H=m clock — textbook ULDM — NOT a condensation temperature.
Code: `dcdf_z_rad_onset` (background.h, with the derived-identity comment). *(Five production
configs — `conv`, `conv_desi`, `dyad`, `lepton`, `nulink` — set this identity value. The `_fixed`
family, including the running evidence job, is frozen at 3.5619×10⁷ instead: 0.053 dex low, which
under this same clock corresponds to m = 1.75×10⁻²⁰ eV rather than 2.24×10⁻²⁰. The mass is pinned
independently by ξ, the Schive core radii and the superradiance window, so the identity is the
model's value and the frozen setting is a profiled offset — see
`ForJustin/07-zon-two-values.md`.)*

**Two jobs, one clock:** the ending regime reaches its floor (conformal
protection ends) while the starting regime crosses its threshold (dust/DM behavior begins). In
code this is literally one function: `dcdf_rho_rad`'s f(a) = x²/(1+x²) fades the radiation while
the dust part continues, amplitude fixed by continuity (no free knob).

## 3\. The background fluid (radiation → dust → de Sitter)

> **w(ρ) = −e^{−s}, s = ln(ρ/ρ_inf) clamped ≥ 0 ⟹ P = −ρ_inf exactly.**

So the background is ΛCDM-form: ρ = ρ_inf + C·a⁻³, algebraically (verified to 10⁻¹⁶).
w = −1 is EXACT for the constant floor — not a step artifact, not rampable. Code: `w_dcdf` /
`dcdf_s_of_rho` (background.h).

## 4\. The electron-coupled scalar turns on (field 2 condenses) [the standing high-scale configuration]

The electron-coupled scalar is a high-scale pseudo-Goldstone: **f ≈ 100–500 TeV (input)**,
quadratic-canonical operator m_e(φ) = m_e0(1 + κφ²) with **κ = ε/f² ≈ 1.4×10⁻³¹ eV⁻²** — ε = κf² =
1.2543% is the frozen zero-mode's delivery. The full operating point (roll time, fluctuation floor
2×10¹⁸ below ε, thermalization gates clearing by 10⁸–10⁹, λ_dyad radiatively stable) is closed-form
in [PRTOE_me_mechanism_math.md](PRTOE_me_mechanism_math.md) (the high-scale spec).
**T_c = 177.10 keV** (the lepton-mass relation's τ = ½ln2; lattice-gated on an SU(2), N_f = 3
value — the block at the top).
This is already a derivation ledger, not a narrative paragraph: the remaining open residue is the UV
operator choice in `PRTOE_me_mechanism_math.md` and the exact `T_c` pin within the standing band.
The high-scale portal rate law is already computed in the high-energy matching calculation; what is
not yet exposed is the crunch-sector bridge that would make it a bounce trigger.

**The ramp's timing, stated exactly.** The electron bath's thermal restoration crosses the
electron-coupled scalar's own bare curvature where

> **C_T(T) = −(8/π²)·J_F′(m_e/T)·κ·m_e·T³ = 2λ_dyad·f²**

(J_F the standard fermionic thermal function) — **a relation with no renormalization-scale
logarithm**. So (λ_dyad, f, T_c) is a **two-parameter family, not three separate inputs**: any
two fix the third. With the recorded λ_dyad the relation places **f ≈ 145 TeV**
(122–172 TeV across the quartic-normalization conventions), inside the adopted window; read the
other way, the window's 100–500 TeV range corresponds to T_c ≈ 130–940 keV.

**The perturbative cross-check, corrected.** The recorded T_c = m_e0·√(3(L−1)/2π²) ≈ 193 keV
and its [40, 900] keV envelope both used the *high-temperature expansion* of the thermal
function, which overstates the restoration by ~16× at this operating point (m_e/T_c ≈ 2.9 —
the electrons are Boltzmann-suppressed there). With the exact kernel the cross-check reads
**307–714 keV over L−1 ∈ [1, 10]** — a factor 2.3 in range where the recorded envelope spanned a
factor 22, and sitting *entirely above* the adopted 177.10 keV rather than bracketing it, by
**1.73× at its very bottom**. Stated plainly: the perturbative route does not corroborate the
adopted value at all — it excludes it; the adopted value's source is the confining chiral ratio,
not this route.

> **What that costs, and it is not only a comfort.** Intersecting the electron-coupled scalar's two
> internal determinations — this one and the timing relation's 130–940 keV over the registered f
> window — leaves **307–714 keV**, which **excludes 177.10 keV**. So the ramp ε(T) = ε(1 − T/T_c)
> is keyed on a temperature the field's own physics does not reach, while ε is that field's order
> parameter; §6 of [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) assigns 177.10 keV to the
> confining sector and rules the electron-coupled scalar is neither of that sector's condensates.
> **And the BBN safety argument does not survive the correction:** the ≤ 0.32σ whole-window swing
> is stated on the [70, 500] keV window, but **53% of the corrected band lies above 500 keV**
> (everything past L−1 = 4.1), where by that window's own definition the field reaches n/p
> freeze-out and helium moves — an effect that bound does not price. Re-keying the ramp onto the
> field's own band is therefore a **numerical** question as well as a structural one. *(The 250–530
> keV figure this replaces does not follow from the exact kernel over the stated range: it
> corresponds to L−1 ∈ [0.50, 4.78]. Recomputed from the same kernel that gives the file's own
> |J_F′| = 0.374 at m_e/T_c = 2.9; `scripts/audit_math_pass.py` carries the band.)*

*The predecessor configuration — the electron-CW VEV v = m_e0·[ε(L−1)/4π²]^(1/6) ≈ 175 keV — is
RETIRED (BBN-fatal at its recorded operating point; autopsy in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)); its formulas do not describe the standing
model.*

**BBN clearance [CLEARS at the adopted T_c — and that value is the condition]:** the deuterium
constraint's severity decomposes by process: weak rates n↔p (T \~ 500–1500 keV, \~75% of the m_e
lever), n-decay phase space (\~10%), e± heating (\~10%), the bottleneck itself (\~5%, B_d nuclear,
m_e-insensitive). The electron-coupled scalar's transition is taken at T_c = 177.10 keV, and BBN
itself bounds it to [70, 500] keV — the deuterium bottleneck below, the weak-rate window above —
with the adopted value interior by 2.5× and 2.8×, so **at that value the field never touches the
weak-rate window**; AND the field is LEPTONIC (quarks \~2-loop, \~10⁻⁹), whose full-BBN ceiling is
\~0.3–1σ, not the universal/hadronic 12σ. That makes `T_c` a safe melt threshold, but not yet a
bounce proof: the contracting branch still has to show that the same threshold feeds `ρ_X` or `Ḟ`
in the handover equation.

> **effective tension = (temporal exposure 0.05–0.25) × (leptonic 0.3–1σ) ≈ 0.02–0.25σ → QUIET.**

**Read that against the band above, because it is the same question twice.** The clearance is keyed
to 177.10 keV, which the confining chiral ratio supplies; the electron-coupled scalar's *own* two
internal determinations intersect at 307–714 keV, which overlaps the weak-rate window across most
of its range and puts 53% of itself past that window's 500 keV. So the clearance holds for the
temperature the ramp is keyed on and is **not** established for the field's own — which is why the
re-keying question above is numerical and not only structural.

"When D forms" ≠ "when m_e matters" — two different electron-scale clocks. Code: the
electron-coupled scalar's window `varconst_transition_redshift < z < varconst_z_high`
(`varying_z_high`, new 2026-07-10; ≤0 recovers the plain step). #40 (RG V_eff + BBN network)
CONFIRMS, not decides.

## 5\. Recombination → today [the fitted era]

m_e shifted by ε = 1.24% inside the window (H₀ fix; ΔlnZ = +2.635 Laplace, SH0ES-conditional, and
Laplace is where it stays — nested sampling waits for cluster time, so the estimate has no confirmer
in prospect and its margin over the decision threshold is inside its own systematic);
screening returns m_e → standard below z ≈ 50 [survival form S = exp[−(C²/C_ref²)^n_eff],
n_eff ≥ 35]. Optional rotation-shed `dcdf_conv_g` — the matter component draining into dark
radiation (S₈: minimizer picks g = 0.12, S₈ = 0.821 vs KiDS 0.814).
Corrected A2: the shed's apparent-w mirage is \~1% — OUT as a DESI driver; the S₈ job
survives (background ρ_m, not the w-mirage).

## 6\. The neutrino home

Ψ = Majoron (L-breaking Goldstone): tree coupling σNN → Majorana m_ν → **0νββ must occur**
(P-2026-020); **Σm_ν ≈ 61.4 meV, normal ordering** — the sum from the tie below, the *ordering*
selected by data through the P-2026-004 collision (ANN-2026-021), not by P-2026-012, which states
it does not fix the hierarchy (ANN-2026-025). The sum is not a discriminator: it sits 2.6 meV above
the m₁ = 0 floor against ~20 meV planned resolution. The tie:

> **ρ_inf¼ = m_ν,lightest = 2.25 meV** — a single lepton-number-breaking scale μ sets both the
> dark-energy floor (ρ_inf ∝ μ⁴) and the lightest neutrino mass (m_ν = μ). The tie is exact to a
> few percent, and it is AZK-safe: the neutrino mass comes from the frozen radial VEV, not from a
> coupling to the neutrino density (which would be unstable).

The scale μ is a dimension-1 lepton-number-breaking parameter, distinct from the (dimensionless)
varying-m_e amplitude ε, which is electromagnetic — the two are different quantities and are not
related by any bridge. The value μ = 2.25 meV is not itself derived from first principles; that is
the dark-energy-value problem ([PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md) §2). **The
tie's operator is now exhibited** (the tenth-channel seat term, with its UV form above v_L and
κ_m's size structural — [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md)); the seat constant b
(κ_m's exact value) remains gated on the constituent theory.

## 7\. NOW → THE END (the forward map)

> **Read 7a–7c with their verdict, which is below in the addendum and is adverse.** The full-cycle
> KP solve fired the internal falsifier: the clean Route-D prediction is dead, and what survives is
> a narrow imminent-turn corner needing a favorable alignment the priors do not favour.
> **P-2026-018 (w = −1 rigid) is the standing branch.** The
> sections below record the mechanism as it was worked out; the addendum records what happened to
> it.
>
> **Superseded in part, 2026-07-29: Route-D is running again — but the "single decider" retraction
> stands, for a reason that has nothing to do with whether a chain is on the box.** `cmp_prtoe_routeD`
> was relaunched and is live as of 2026-07-29 22:00, now with **two** chains rather than one,
> ~22 h in. Its R−1 reads 19331, which is a burn-in artefact and not a pathology — the two chains
> sit only 2–7 proposal-σ apart, and the huge number comes from within-chain scatter being 8–70×
> smaller than that separation while both chains are still descending rather than sampling. It is
> nonetheless stuck in a configuration deadlock: `learn_proposal_Rminus1_max_early` is 1000, so the
> proposal covariance cannot be relearned until R−1 falls, and R−1 falls slowly because it was never
> relearned. Expect nothing before 2026-08-01 and plan for ~08-09. **What does not change:** the
> clean Route-D prediction was killed by the full-cycle KP solve analytically, so no chain was ever
> the single decider — see the addendum, where that phrase has now actually been removed from the
> sentence carrying it.
>
> **Correction, 2026-07-28 (the state that prompted the retraction, kept for the record): there was
> no running Route-D chain, and the one that had run could not have
> decided anything.** This passage previously named it "the single decider". On the box,
> `cmp_prtoe_routeD` holds **exactly one** chain file — 11,508 steps, 363 accepted (3.2%
> acceptance), **last written 2026-07-20**, with a header-only progress file. The blocker is
> structural rather than temporal — *though not in the way this passage first stated it (corrected
> 2026-07-29).* It previously read: "the Gelman–Rubin statistic is a between-chain quantity, so a
> one-chain run yields no convergence diagnostic **however long it runs**." **That is false.** When
> only one process is running, the sampler splits the single chain into `Rminus1_single_split`
> segments (default 4) and computes R−1 *across those segments* — a within-chain split-R̂. Other
> single-chain runs on this box did record one (R−1 = 13.25 at N = 3744; R−1 = 40.36 at N = 832), so
> the statistic is produced, and is comparable across them.
>
> **The real objection is sharper, and it survives.** A split-R̂ compares segments of *one*
> trajectory, so it **cannot detect a chain confined to a single basin** — every segment shares the
> confinement. A between-chain R−1 can, because independently seeded chains would have to agree. The
> failure mode that actually matters here is precisely multi-modality, so a one-chain run supplies a
> number that is *blind to the thing being tested.* Deciding this fork from the model's own chains
> therefore still requires a multi-chain relaunch — **which has since been done** (2 ranks, launched
> 2026-07-28 22:51, healthy at 21–24% acceptance, burning in). The external adjudicator (DESI DR3) is
> unaffected and still decides the branch.

**7a. The sequestered floor — a route that does not work.** A Kaloper–Padilla vacuum-sequestering
attempt to fix the dark-energy value from the cosmic expansion history was checked and fails: it
predicts a dark-energy-to-matter ratio at least ~5× too small (and zero for an eternally expanding
universe). So the value is not fixed this way. The model's standing dark-energy predictions remain
**w = −1 exactly** and the neutrino tie (ρ_Λ¼ = m_ν,lightest ⟹ Σm_ν = 61.4 meV).

**7b. The thaw [the necessary consequence].** Observed Λ ⟹ turnaround within \~an e-fold ⟹
**m_J \~ (1–3)H₀** ⟹ the floor is thawing NOW:

> **1 + w_floor(a) = thaw · a³** (thawing growth), net apparent CPL (with the shed at g=0.12):
> **(w₀, wₐ) ≈ (−0.92…−0.86, −0.2…−0.5)** — thaw-side, NO true phantom ever.

Code: `dcdf_floor_thaw` (new 2026-07-10; ≤0 recovers w = −1 exactly). ρ_floor(a) =
ρ_inf·exp[thaw·(1−a³)]; E(a) = ρ_floor − ρ_inf added background-only (pattern of dcdf_rho_rad).

**7c. The branch [registered as P-2026-056, guards discharged]:**

> **P-2026-018 (w = −1 exact) XOR Route-D (thaw-now, w₀ ∈ [−0.92,−0.86], wₐ < 0, no phantom).**
> DESI DR3 adjudicates: thaw-side → Route-D (J1+why-now+DESI in one stroke, P-018 dies);
> rigid → P-018 (distinctive win; Route-D dies, J1 reverts to constitution);
> TRUE phantom in the DATA → both die. Guards: distance-space phrasing, KP solve, timestamp
> (J1-derivation precedes DESI-convergence), A2+A3 net (answered) — each stated with its
> resolution in [PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md)
> (P-2026-056), where the decision rule is registered.

**7d. The end (and the next start).**

**The turn, computed (expanding branch).** The recorded thaw law alone cannot deliver it:
ρ_DE(a) = ρ_Λ·exp[thaw(1 − a³)] falls toward zero **from above**, so the total density never
vanishes and expansion merely decelerates forever. A turnaround requires the sector's second
piece — the **negative bare vacuum** this narrative already carries — giving

> ρ_DE(a)/ρ_Λ = (1 + B)·exp[thaw(1 − a³)] − B,  B ≡ |ρ_bare|/ρ_Λ,obs,
> with today's equation of state pinning the product: 1 + w₀ = thaw·(1 + B).

The code path exists in `include/background.h` and `source/background.c`:

`ρ_floor(a) = ρ_∞·exp[thaw·(1 − a³)]`

with the background-only deviation

`E_th(a) = ρ_floor(a) − ρ_∞`.

Adding the negative bare vacuum gives the net late-time DE budget

`ρ_DE(a) = ρ_Λ·[(1 + B)·exp[thaw·(1 − a³)] − B]`,

where `B ≡ |ρ_bare|/ρ_Λ,obs`. The turn is the zero of that expression:

`ρ_DE(a_turn) = 0`

so

`a_turn = [1 − thaw⁻¹·ln(B/(1 + B))]^{1/3}`.

That is the actual mechanism: the thawing floor alone only falls toward zero from
above, but the added negative bare vacuum lets the total DE budget cross zero at
finite `a_turn`. The flat Friedmann equation then gives `H = 0` at that point; the
turning sign is the late-time branch reversal, not the bounce.

**The turnaround lands at a ≈ 2.0–2.8 (z ≈ −0.51 to −0.65), 16–26 Gyr from now** across
w₀ ∈ [−0.92, −0.86] and two orders of magnitude in B: the trade-off between thaw rate and
bare depth holds the answer nearly fixed, so the timing is a consequence of the structure
rather than a tuning of it. **The bare depth is invisible in the expansion history** — the
same trade-off makes the low-redshift trajectory B-independent to ~0.2% — so the turn itself
is not a measurement; what the sky grades is w₀. *Branch note: this is the expanding branch's
parametrization (the field rolls forward in time, it does not roll back up as a decreases);
the contracting branch and the bounce need the field equation solved in time — the bounce
sector's own debt. This is the late-time reversal only; it is not yet the contracting-branch
bounce.*

The `16–26 Gyr` range is the registered solution range for `w₀ ∈ [−0.92, −0.86]` and the
allowed `B` span; it is supported by the chain and the preregistered branch record, not by a
fresh standalone simulation in this session.

The thaw completes → expansion reverses → contraction blueshifts radiation (a⁻⁴ grows) →
thermal counterflow / heated-superfluid release reignites → T climbs back through **T_c** (the
SAME T_c of §4) → **the electron-coupled scalar's condensate MELTS** (m_e → standard for the
crunch) → charge survives in solitons/Q-balls [requires gravity-mediated K<0: fragmentation banks
the charge at T \~ 10¹⁰ GeV, 13 decades before any melt] → torus topology carries the axis across
the bounce (rotation resets, topology doesn't) → re-expansion cools through T_c → the condensate
RE-FORMS → §1.

Heated-superfluid release (thermal counterflow under a heat load) is the strongest
release-side clue in the corpus: it is the microphysical phrase for a heated superfluid
giving way and re-routing flow. But it still has to be tied into the cosmological
handover equations before it counts as the bounce itself.

The strongest surviving trigger branch is the high-scale electron-mass sector. The
gravitational portal only thermalizes at `T ~ M_Pl`, while `scripts/portal_bar.py`
leaves open a non-gravitational portal tied to the high-scale electron-mass sector that could bar
lower and fire at a sub-Planckian crunch. That makes it the first late-rung branch that
looks like a real trigger rather than another reservoir. The rate law is computed, but
the crunch-sector `ρ_X(T)` is not exposed yet, so the branch is still open rather than
closed.

So even this branch is trigger-shaped, not bridge-shaped: it can set the crunch
ceiling, but it still does not supply the handover term. The detailed retirements are
tracked in [`docs/PRTOE_FAILURES_LEDGER.md`](PRTOE_FAILURES_LEDGER.md).

The closest structural analogs are threshold-gated too: the `m_e` trigger is a sharp
topological switch, and the KMS / freeze-front material locks one face per thermal
period. So if the crunch-sector heated-superfluid release is the right clue, it probably needs a
sharp gate or front, not a smooth ramp, before it can become the bounce.

The "next regime" intuition is probably right in shape but not yet in species: the
corpus already has a radiation-like / normal-phase release grammar where the matter-part
sheds and dark radiation grows with opposite sign. That looks like the likely bridge if
the bounce closes, but it is still a phase of the same medium, not a newly named dark
radiation substance.

So the three sub-questions line up as follows:

- a sharp front / gate exists in the corpus already, via the `m_e` trigger and the
  KMS / freeze-front material;
- a late-time `shed` analogue exists already, via the dCDF matter-part draining into
  dark radiation;
- the heated-superfluid / thermal-counterflow threshold is still the strongest release-side clue,
  because it is the only named place where heating a superfluid forces retraction / flow re-routing.
  In the thermal program it shows up as a **residual thermal excitation** from the
  medium's one genesis injection, so the bounce hunt should read it as a real residual
  component of the same field, not as a separate species. No bounce-sector
  `ρ_X(T)` written from it has been found in the corpus; the explicit residual equations still
  sit in the late-time program. So this stays a load-bearing clue for the thermal
  residual program, not yet a bounce-sector source term.
The branch-change search is separate and still open: the corpus gives a historical
scalar-tensor template, but not an active crunch-sector `F(T)` to plug into the bounce.
That is the bridge ceiling: the only bridge-shaped equation in hand is the historical
varying-`F` / induced-gravity form, and it still lacks a live crunch-sector realization.

The other reusable shape is the thermal-threshold residual fraction: freeze at a threshold,
then keep a suppressed residual. That is the right silhouette for a crunch-side source
term, but the corpus prices it only in the neutrino / late-time residual sector. So the
bounce hunt has two templates and no live bridge yet.

There is one more general split in the corpus, "freeze-out third + release memory,"
but it belongs to the inflation / ergodic-mechanics material, not the crunch sector.
It is a real decomposition, just not a bounce bridge.

Likewise, the `T = m_e` localizable-zero burst in the expansion-energy ledger is a real
finite handover support, but it is still only a localization of the budget: it tells us
the handover can be finite, not why the contracting branch turns. So the burst is
another bridge-shaped template, not a live crunch-sector bridge.

**Thermal crossing and the bounce.** Contraction blueshifts radiation (`ρ_rad ∝ a⁻⁴`,
`T ∝ a⁻¹`), so the medium can reach the melt threshold `T_c` on the contracting branch.
That melt is a real local threshold; the classical turn is **open**. Finite `ρ_bounce`
stands as a no-singularity number. Checklist and reconstruction work:
[working_logs/bounce_derivation_workplan.md](working_logs/bounce_derivation_workplan.md),
[working_logs/bounce_reconstruction_rp.md](working_logs/bounce_reconstruction_rp.md).
Retirements: [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) only.

Support-side structure on the contracting branch (reservoirs, timing, release channels)
is discussed in the workplan; this spine does not re-list retired bounce-source claims.

The epoch ladder for late structure:

- BBN → nuclei
- recombination → atoms
- cosmic dawn → molecules / first stars
- structure formation → galaxies / dark solitons
- late collapse → neutron stars / magnetars / black holes
- gravitational-atom grammar → the late bound-state version of the same cooling ladder

For the current cosmic epoch, the same ladder read from today forward says:

- the most massive stars die first;
- the stellar UV budget declines;
- red giants, planetary nebulae, white dwarfs, neutron stars, magnetars, and black holes
  accumulate as the sky reddens and dims;
- the baryonic medium becomes more compact-object dominated;
- and that is the regime in which the next threshold clue is most likely to appear.

Keep that remnant set as the next-epoch survivor list:

- white dwarfs, with planetary nebulae and enriched gas shed on the way out;
- massive-star deaths as core-collapse supernovae, leaving neutron stars, magnetars, or black holes;
- the leftover gas and compact remnants are the objects most likely to matter once the bright
  stellar era is gone.

The "same room" reading should stay literal-but-causal, not literal-spatial:

- the remnant types do not need to merge into one object now;
- they need to end up in the same late compact-remnant epoch, with the same cooling and clustering
  rules;
- the final reunion is the crunch bath itself, where contraction and thermalization force the
  different survivor channels into one shared handover environment.

The four-piece map is:

| survivor | what it carries | likely bounce-role |
|---|---|---|
| white dwarf | cooled baryonic matter, the late low-mass endpoint | a settled matter reservoir and a cooling landmark |
| neutron star | nuclear-density matter plus neutrino/superfluid structure | the neutrino and superfluid timing side |
| magnetar | extreme magnetic energy storage | the release-side energy reservoir / trigger analogue |
| black hole | deepest gravitational lock, finite-density core, heat and entropy | the strongest reservoir/release ledger |

These are carrier-objects, not the handover term itself. The bridge still has to be a
sector-local `ρ_X(T)` or a genuine branch-changing `Ḟ(T)` that makes the shared late
remnant bath turn the crank on `H = 0`, `Ḣ > 0`.

Timing note: the next regime may reveal its carriers well before the reversal is
available. In other words, the epoch ladder can tell us what survives into the late
remnant inventory, while the actual bounce still waits for the terminal threshold in the
contracting branch. So the mechanism is likely not at the halfway marker; the carriers
arrive first, the reversal later.

So the "lights out" reading should stay literal but narrow:

- it does **not** mean starlight directly powers the dark-energy thaw;
- it does mean the source of abundant stellar radiation disappears as the current epoch burns out;
- and it does mean the late-rung reservoir/release objects become more important, not less.

So the bounce hunt should stay on the late-rung objects, not on the early thermometers.
At the current level of the corpus, the ranking is:

- black-hole cores: real reservoir / release ledger, still open
- magnetars: reservoir analogue only, no load-bearing term yet
- gravitational atoms / SMBH atoms: late-structure diagnostics, not the source

The late-time dCDF / thaw residual was checked and **not** promoted:
its `w = −1` floor is exact and useful for the dark-energy program, but it is the wrong epoch
and the wrong job for the contracting bounce. It can tune the late DE floor; it does not yet
name a bounce-sector `ρ_X(T)`. The failures ledger already retires the move that would reuse
that residual by fiat; the bounce still needs a sector-local source term or a genuine branch
change in its own equations.
That is the search ceiling reached so far: no crunch-sector-local term has emerged from the
obvious residual, reservoir, or branch-change templates.

That means the likely shape, if it closes, is multi-stage: thermalized cores,
radiation release, blueshift under contraction, and a last residual that tips the
handover. The equation is still missing, but the flavor is clearer.

**The condensate breathes; T_c is both the recombination-era turn-on and the
crunch-era melting point — one number, both jobs** (the two-jobs law, §2).
[Phenomenological at the bounce rungs: BKL, Tolman unresolved; the bounce itself remains
separately uncomputed.]

**BKL is worse than unresolved — the recorded equation of state is the wrong one to survive it
(2026-07-20, #117).** The standard route past a BKL approach is a stiff phase: shear energy density
scales as a⁻⁶, so anisotropy stops growing *relative* to the background only when w ≥ 1 (kination,
also a⁻⁶). **This model's recorded first regime is w = 1/3** — the phonon-gas/radiation-like phase
(UV_completion §step 3) — which scales as a⁻⁴ and therefore **loses to shear by two powers of a**.
Contracting through three decades of scale factor, the anisotropy-to-radiation ratio grows by 10⁶.
The one place kination appears in the corpus is the ALP rotation's *redshifting*, not a phase the
contracting branch is recorded to pass through. So the bounce sector does not merely owe a field
equation solved in time: **it owes an equation of state at the approach that the recorded regimes do
not currently supply**, and until one is named the BKL objection stands unopposed rather than open.
Tolman is untouched by this and remains separately unresolved.

**And the model's own sector cannot supply it — computed, not surveyed
(`scripts/bounce_bkl_stiff_check.py`).** The obvious place to look for a stiff phase is the
founding identity itself: a *rotating* condensate carries a conserved charge Q = a³r²θ̇, and at
fixed Q the rotation appears as a centrifugal term in an effective radial potential,
V_eff(r) = V(r) + Q²/2a⁶r². If the amplitude r were held fixed, the rotational energy would fall
as a⁻⁶ — exactly kination, exactly what BKL needs. So the question is whether r holds fixed on
approach, and that is decidable.

It does not. The field instead **tracks** the minimum of V_eff, and tracking in V ∝ rⁿ gives

  r ∝ a^(−6/(n+2)),  ρ ∝ a^(−6n/(n+2)),  hence **w = (n−2)/(n+2)**

— an exact result, confirmed by integrating the radial field equation through a contracting
background to five decimal places at n = 2, 4 and 6. It reproduces the recorded regimes rather
than contradicting them: n = 4 gives w = 1/3 (the quartic youth) and n = 2 gives w = 0. **And it
is strictly below 1 for every polynomial n**, approaching kination only as n → ∞. No polynomial
potential reaches the stiff condition by this route.

Freezing is the only escape, and it has a price that can be quoted. At the tracking minimum the
restoring curvature is V_eff″ = n(n+2)V/r² against H² = V(n+2)/6M_Pl², so
**V_eff″/H² = 6n·(M_Pl/r)²** — the field can only freeze once its amplitude is **trans-Planckian**
(r ≳ 3.5 M_Pl at n = 2, 4.9 at n = 4). The integration crosses that threshold and w does turn to
1.0000 above it, which confirms the mechanism and simultaneously prices it out: the model's
amplitudes are nowhere near M_Pl.

**The relation is not new to the corpus, which is worth saying.** w = (n−2)/(n+2) is exactly what
`cosmological_constant` §"why it stays unbuilt" already uses to grade a harmonic condensate mode as
w = 0 at n = 2. The two derivations were reached independently and for different purposes — one to
price an equipartition reading of the dark-energy floor, one to test a bounce — and they agree.
So the BKL result rests on a relation the corpus had already validated elsewhere, not on a new
claim introduced to settle this question.

**So the objection is not merely unanswered, it is unanswerable from this sector.** What remains
open is whether some *other* component — not the rotating condensate — supplies w ≥ 1 at the
approach; nothing in the recorded roster currently does.

**The contracting branch's own equation of state, walked on the recorded (m, λ).** The debt named
above — that the bounce needs the field equation solved in time, not just the expansion
parametrized — is discharged for the *approach*: on the recorded potential V = m²R² + λR⁴ the
contracting field passes through **w = 1/3** while quartic-dominated and **w = 0** once
mass-dominated, the same radiation-into-matter sequence as expansion run backward, and it never
stiffens. The quartic-to-mass crossover Ψ₀ = m/√λ is itself sub-Planckian (≈4×10⁻³ M_Pl), and
kination would need an amplitude of order M_Pl that contraction does not reach before the bounce
density. So solving the equation in time returns the *same* adverse verdict rather than a new
regime — the contracting branch is computed, and BKL stands against it. What stays genuinely open
is unchanged: whether the bounce itself introduces a stiff component, which is a question about the
bounce mechanism the model does not yet carry, not about the branch that leads into it.

## 8\. The two-jobs pattern — and where the code reflects it

Every transition is ONE clock with TWO jobs — the ending regime reaches its floor, the starting
regime crosses its threshold:

|transition|job 1 (floor reached)|job 2 (threshold crossed)|in code|
|-|-|-|-|
|H=m (z=4×10⁷)|conformal youth ends|DM (dust) begins|`dcdf_rho_rad` f(a): one function fades radiation as dust continues, continuity-matched|
|T_c (electron-coupled scalar)|thermal disorder dies|condensate/δm_e turns on|`varying_z_high` edge (2nd-order: no latent budget to hand off — a pure switch is CORRECT here)|
|ρ→ρ_inf (z\~0.7)|matter dilution bottoms|de Sitter begins|`w_dcdf(ρ)`: one barotropic function does both automatically|
|shed|matter-part drains|dark radiation grows|the SAME `conv` term, opposite signs, in two ODEs (background.c:2843-45) — the pattern literally|
|thaw/turnaround|the floor era ends|the turn begins|`dcdf_floor_thaw` (new)|

The conservation-pair transitions carry the two jobs as one term with two signs; the
second-order (continuous) transition carries them as one edge with no budget. **The code
reflects the law wherever the law demands it, and correctly does NOT fake a hand-off where
the physics has none.**

## 9\. Ledger (what this spine rests on)

**Recorded:** DM+DE unification (2→1); ε derived; onset = H=m identity (z = 4.03×10⁷, the mass
pinned independently by ξ, the Schive core radii and the superradiance window); **the
electron-coupled scalar's onset is T_c = 177.10 keV from the lepton-mass relation's τ = ½ln2** —
the value's source is the confining chiral ratio, not the electron loop, whose predecessor
*configuration* (the CW VEV at ≈ 175 keV) §4 retires
as BBN-fatal. What survives from that loop, and is used above, is the κ-independent restoration
*formula*, which supplies the ramp's timing and is why the transition sits at the electron scale for
any decay constant; AZK-safety; leptonic allowed ≠ generated.

**Falsified:** P-2026-004 (high Σm_ν); the sequestering route to the dark-energy value (§7a, and the
full-cycle KP solve in the addendum — the internal falsifier fired).

**Live falsifiers:** DESI DR3 (the branch), Σm_ν ≈ 61.4 meV, 0νββ, void/IGM m_e-step (P-007, J4).

**Settled since this ledger was last written** — each was carried here as open and each is closed
elsewhere in the corpus:
- *KP self-consistency* — resolved **in this file**: §7a reports the attempt fails, and the addendum
  reports the full-cycle solve firing the falsifier.
- *spurion identification* — done in [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md) §2: μ is a
  dimension-1 lepton-number-breaking parameter, distinct from the dimensionless varying-m_e
  amplitude.
- *low-scale seesaw* — **adjudicated** by the seesaw duty scan (same file).
- *leptophilia* — established in [PRTOE_dyad_gas.md](PRTOE_dyad_gas.md) §2, and **by data**: a
  universal quark-mass shift at ε lands at +12–18σ on D/H. What is settled is that the coupling is
  leptonic; the *portal* is not, and it is carried in the open list below.
- *the gate-0 confirm* — #40 (RG V_eff + BBN network) confirms rather than decides (§4).

**Still open:** the dark-energy *value* if Route-D dies (falls back to constitution — the
branch is DESI DR3's to decide); the seat constant b in the neutrino tie, gated on the
constituent-level build — which is itself gated on the band structure the hierarchy chain's §6c
needs, docket #146
([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §8, the open-surface table). **The portal's
selection rule is not an open debt — it is assumed**, and §0 now says so with its price: data
narrows the singlet's Standard-Model partner to the lepton bilinear and nothing else selects it,
while the one
fork with a signature moves an unmeasurable quantity. That is a permanent grade rather than a debt,
and it belongs beside c on the list of things the model counts on rather than derives.

**Standing:** open pending the named referees, DESI-capped; the branch is registered
(P-2026-056) with its guards discharged. Its adjudicating chain was **not running** as of
2026-07-28 (this sentence previously said it was); `cmp_prtoe_routeD` then held a single chain file,
last written 2026-07-20. It has since been **relaunched with two ranks** (2026-07-28 22:51, healthy
at 21–24% acceptance, still burning in). Note the earlier gloss here — that a one-chain run "cannot
yield a convergence statistic at all" — was **wrong and is corrected in §7**: a single chain does
yield a within-chain split-R̂; what it cannot do is detect confinement to one basin, which is the
failure mode at issue. **DESI DR3 remains the adjudicator and is unaffected.**

*(Every debt on this page names where it is closed or what it waits on. Bare "open" is not a
status: [`working_logs/_DOCKET_INDEX.md`](working_logs/_DOCKET_INDEX.md) resolves task numbers, and
where this page and a physics file disagree, the physics file is right.)*

---

## ADDENDUM (2026-07-10, later): §7 STATUS CHANGE — the internal falsifier FIRED

The full-cycle KP solve (full_cycle_kp.py, scratch-era, not retained) computed the fixed point over
the whole cycle (expansion + thawed contraction + Tolman boost): **it robustly wants a_turn = 0.70
(a PAST
turnaround, z=+0.43)** — excluded by observed acceleration; a future turn is 3× (a_turn=1.0) to
10× (1.5) short, Tolman boost null, and the "full-cycle-fixes-the-sign" claim was WRONG
(near-mirror contraction cancels). **So §7a–7c are DOWNGRADED:** the clean Route-D prediction is
dead; what survives is the IMMINENT-TURN CORNER (z_turn \~ −0.1..−0.3, needing \~3× from four
favorably-aligned rigorous-KP O(1)s [prior-adverse, tail] AND a strong thaw pulled by the data).
The two kill switches MERGE, and the Route-D MCMC (thaw free on the DESI joint stack) decides
**what is left** rather than the fork itself — the clean Route-D prediction was already killed
analytically by the full-cycle KP solve, with no chain involved. What the chain still settles is
whether the surviving imminent-turn corner lives: thaw pulled hard → corner lives; thaw \~ 0 →
Route-D dead twice over, **P-2026-018 (w = −1 rigid) stands as the distinctive branch, and J1
reverts to constitution/boundary-datum.** *(This sentence read "is the single decider" until
2026-07-29. The §7 header has carried a correction saying it "previously named it 'the single
decider'" since 2026-07-28 — but the correction was written at the head of §7 and never applied
to this line down in the addendum, so the retracted phrase stood for a day beneath its own
retraction.)*
§7d (the melt/re-form cycle closure) is unaffected as a phenomenological cycle picture. Held
open. *(The turn's
own timing follows from the surviving structure — the thaw plus the sector's negative bare
piece — and is later than this corner's z ≈ −0.1…−0.3, which rode the sequestering route:
see §7d.)*

---

## §10 — THE ATOM READING (the capstone, 2026-07-10 night)

**The universe is a single bound quantum state of the dark superfluid — one atom — and cosmology is
its internal atomic physics.** Formation: genesis = recombination (capture cascade; f_amp = the
branching ratio, computable-class). Structure: Landau's two components — the zero-entropy ground
state (floor/constitution/timeless; w=−1 exact \& ageless by theorem) and the entropic excitations
(light/matter/observers; Tolman's arrow). Spectroscopy: torus modes = the line spectrum (low-ℓ =
the first lines); the census = the selection rules; the CMB = the recombination photograph.
Chemistry: the electron-coupled scalar = one universal lepton rescaling ε, C²-gated, one
fingerprint across H₀/D-H/ν/21cm/radio. Present: mid-emission — Γ_par/H = √3 (IR scale) and
Γ_eff/H = √(3/2) with B = 1/√2 (Jeans growth rate, derived) = the linewidth
(why-now); symptoms {coupling dipole, mass defect = the thaw, recoil = the axis} = the falsifier
board. Biography: first excitation (Tolman arrow, finite past) → lengthening cascades → possible
ionization (binding energy un-computed). J1 = the ground-state eigenvalue: constitutional, at home.
**Status: the grammar is coherence (graded throughout);
the empirical content lives in the children and the symptom chart. The method was the subject.**


## §22 — THE THREADING DAY (2026-07-11, the second arc): sixteen roots, lawful deaths, the ladder, and the BBN witness

**The threading survey:** sixteen direct threads filed and graded (galactic/SMBH
atoms, the neutrino home, S₈, low-ℓ, the lepton-mass relation's invariance, the laboratory
analogues, the coincidence problem [why-now = √3·A_s·the floor — the √3 one-pager discharged: the
Friedmann factor,
value-independent; B = 1/√2 derived from Jeans dispersion, par-question closed
for the thaw rate], the purchased silences [direct+indirect],
GW [the vortex null Gμ ~ 3×10⁻²¹; the chirality family's third member], the Hubble standalone,
the radio lattice, the fingerprint capstone, IGMF helicity, LSS parity). **The protocol** (now
standing law): model every transition as smooth unless quantization protects a jump; adopt a
replacement only when it improves on what it replaces; and when a claim dies, record why — which
step failed, which coupling, and which downstream claims inherit the death — rather than letting
it lapse quietly. Debts are itemised where they are incurred. **The inheritance theorem:** no
orphan physics (L1) — every non-thread is a child of a threaded root; deaths are lawful (each
names its law — strong-CP and birefringence share
L1a, one clause, shared fate both ways).

**The master computes (the 40 debts factor to 8, in 4 clusters):** par/size (the α_c MCMC +
the lanes), topology (the AD route + the cavity), frame/UV (the Lorentz program + λ), data
(the chains + the epoch stamps). Sprint results: the toy cavity puts ℓ=2,3 BELOW the first
torus mode (T5's matched-circles risk resolved favorable); the thermal-leptogenesis surface is
EMPTY (×40-1000 under everywhere) → **the baryon asymmetry reverts to the native AD-direct route
(charge = abundance) with the frozen-era transfer (sphalerons at 130 GeV vs the field frozen till
9.4 keV) as the hard timing crux**; the λ trial chain failed its own bounce self-check
(informative).

**The λ-ceiling (a small recovery):** the winding-patch isocurvature (14.1% rms
if the onset is quartic) would be CMB-dead ×5-7 → the model REQUIRES λ ≤ (m/Ψ₀)² ≈ 2×10⁻⁹¹ —
a derived self-constraint; the axion-like reading (λ ~ m²/f²) lands at the ceiling within an O(1)
factor → **P-2026-031 (conditional): CDM isocurvature at ℓ ~ 170.** *(Amplitude caveat: the axion
quartic carries a coefficient ~1/6, so |λ| sits a factor ~6 below the naive (m/Ψ₀)² ceiling — the
isocurvature is then likely sub-%-level and below current Planck sensitivity, not at it; the exact
amplitude awaits the O(1) coefficient and the λ-sign.)* (+ a 45-90 km/s bulk-flow shadow).
MOND/RAR finally dead (m_amp → m; ≤59 AU ≪ kpc). The third
mass-top coincidence (CSW M_max ~ 10¹¹ M☉ at the ceiling; with α_g = 1 at 6×10⁹ and r_s = ξ
at 2×10¹⁰) — noted, m-correlated, not recorded.

**The scale ladder:** the Bohr skeleton E_b/(mc²) = ½α_eff² at every rung (the
universe rung SITS on its own skeleton: 2.28 vs 2.29×10⁻⁴); the corrected ordering (nucleon >
nucleus > UNIVERSE > atom > star > galaxy — the universe is the tightest GRAVITY-made
structure); **the hinge: ξ = 402 AU inside the solar-system rung — one substrate boundary in
the whole descent**; the double-ladder alignments graded per-rung (2 definitional, 3 loose —
no mechanism). **The ladder is RETIRED and the energy cascade CLOSED as malformed
(2026-07-28, `scripts/scale_ladder_virial_check.py`):** the per-rung grading did not go far
enough. Unpacking α_eff = v/c shows the "loose" rungs are also definitional — ½α_eff² = ½v²/c²
is the virial theorem, verified against GM/2rc² to machine precision — and the atomic rung is
the Rydberg. All five rungs are one textbook identity written five times, so there is nothing
for an energy cascade to be the dynamics of. **What survives is the hinge alone:** ξ = 402 AU
sits between the planetary system and the Oort cloud, one substrate boundary in the whole
descent — a statement about ξ, now filed with the medium's properties.

**THE WINDOWED BBN VERDICT:**
T_c (177.10 keV on the kernel's τ; 179 keV as the BBN pipeline codes it — the conclusion is
insensitive to the difference) is INSIDE the BBN window → the ε(epoch) stamps re-price everything:
**the Y_p improvement was an artifact of applying ε above T_c** — windowed, Y_p ≈ 0.24900 (+1.09σ
COUNTER vs Aver; +3.53σ vs EMPRESS — the disagreement between the two helium determinations
noted); D/H partly relieved (2.387 → **−2.9σ** vs Cooke on the full stated budget: obs ±0.030 ⊕
PRIMAT post-LUNA nuclear theory ±0.037; the 3.5% inter-code spread is named and unfolded, and
would soften it to −1.4…−2.2σ).
**Re-priced under the standing high-scale configuration + the committed genesis dilution
ζ = T_dark/T_γ ∈ [0.25, 0.35] (ΔN_eff = 0.06–0.24): D/H −2.5…−1.4σ on the quotable ±0.0476 budget
(−1.2…−0.7σ if the full inter-code spread is folded), Y_p +1.3…+2.0σ vs Aver
(EMPRESS +3.8…+4.4σ stands apart), joint
p = 0.02–0.08 quotable / 0.12–0.21 on the full spread. The residual helps deuterium and does not
heal it; the sector's verdict still turns on the code systematic. The σ's in the sentence above
are the window's own effect, before the residual —
[PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §8, recorded in
[PRTOE_bbn_witness.md](PRTOE_bbn_witness.md).** **The BBN synthesis: the sector is THE
TRANSITION'S WITNESS** — the only laboratory that watched the condensation live; the pattern
is RIGID (no dials); referees: the radio referee, the helium resolution, the T_c re-audit
(flagged-not-taken), the α_c MCMC posterior. The adverse landings are logged in public;
the λ-defense is on record.

## §23 — PROGRAM SYNC (2026-07-27): the cyclic sector, the lepton lock, and the primordial triangle

*Status addendum. Grades and referees follow the finish standard: every open item
names what would end it, in either direction. Retired alternatives live in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md); working records in
`working_logs/bounce_reconstruction_rp.md` and `working_logs/tilt_envelope_derivation.md`.*

### 23.1 The cyclic sector: the turning point requires the exit from the metric description

Two closures now bracket the crunch. At the fluid level, no admissible
negative-energy component exists in the recorded theory (measured-sign, budget,
and existence arguments — equal-scaling components are anchored by today's
measurements; transients and curvature terms fall short by 19–95 orders). At the
constraint level, the energy-balance derivation of the expansion equation keeps
its exact form with the quartic interaction included, and the medium's
short-distance corrections (∝ k⁴ξ²) vanish for homogeneous cosmology, activating
only at coherence-length gradients. **Consequence: the bounce proceeds through
the end of the metric description or not at all**, and the restart event is a
past boundary of the emergent spacetime by exhaustion
([PRTOE_white_holes.md](PRTOE_white_holes.md) §10).

The boundary's causal structure is written: the exit surface is spacelike for
order-unity density contrasts, collapsed regions bound it with absorbing
(permitted) timelike segments, and the re-emergence surface must be spacelike
everywhere — quantitatively, the non-metric interval must persist at least the
crossing-time spread, or a re-synchronization mechanism must be exhibited. The
anisotropic approach delivers 0–1 directional squeezes (the first squeeze is the
exit), planar to 2.5–3.5 orders, at Mach 14–16 relative to the medium's sound
speed. The medium's verified response: its repulsive self-interaction reverses
one-dimensional compressions across the full delivered speed range (energy
conserved to ≤0.3%), returning outflow on coherence-time scales; the excitation
bookkeeping at the boundary is written for the medium sector (the causal cone
ends because group velocities exceed the sound speed at coherence-scale
wavelengths; quasiparticle number is conserved; modes with kξ ≲ 2.5 cross as a
quench). **Open, with referees:** the re-expanding/contracting interface,
sequencing of neighboring regions, the Standard-Model sector's crossing, and the
nucleosynthesis budget (two live channels: spherical focusing — computing — and
the Standard-Model crossing). Grade: reconstruction/candidate throughout.

### 23.2 The charged-lepton mass structure: conservation plus quantization

The balance condition (Q = 2/3 ⟺ the charge-graded norm of the √mass vector
vanishes, the source of τ = ½ln2) carries a two-part candidate mechanism. The
uniform component is a **conserved charge** — computed exactly: its first moment
vanishes identically, so it is set once and cannot fluctuate. The charged pair
carries **exactly one quantum of energy as a definite classical amplitude** —
the ground-state occupancy principle (occupancy one: the ground state holds
exactly one quantum per coherence cell — the vacuum-energy counting) applied to
the lepton cell; integer-protected, hence compatible with the observed 6×10⁻⁶
exactness in a way no thermal average can be. The two exact numbers unify in one
object: the frozen quantum's amplitude gives the modulus (1/√2 ⟹ τ = ½ln2), its
transport around the three-generation cycle gives the phase (2/9), and the
closure forces its frequency to (2/9)·T_c = 39.36 keV — equal to the
independently recorded per-face drift. **Referees unchanged:** the SU(2),
N_f = 3 lattice campaign (five verdicts, including the three-source ground-state
geometry and the adjoint string-breaking distance), the registered deviation
lock, and m_τ at ≲1.4 ppm. Grade: candidate; the residual is the deposit
argument for the conserved amplitude's value.

### 23.3 The primordial amplitude and tilt: one triangle, one rate

The tilt's mechanism, at candidate grade: the census fluctuation is a conserved
charge sourcing curvature at a constant rate per e-fold, from the birth-scale
anchor to each mode's horizon crossing — amplitude ∝ ln(k_UV/k), hence
n_s = 1 − 2/ln = 0.9677 (+0.66σ) with the zero-parameter signature
α_s = −(1−n_s)²/2 = −5.2×10⁻⁴ (thirteenfold below current sensitivity; the
registered falsifier-in-waiting). The coherence is forced by the conservation
law: increments cannot be redrawn. The normalization dissolves into physics:
A_s = r²L*²β³/2π², with the conversion rate bounded two-sided by the registered
isocurvature band (r ∈ [0.8, 3.2]), and the imprint fraction β = γ/N₁ — the
scaling-network density γ ∈ [0.08, 0.20] (inside the standard band) times the
per-cell count N₁ = 4πk/α_c = 783 (the recorded winding-gas count, decomposing
exactly as the inverse screened coupling in loop units). **Four observables rest
on one rate without strain:** the amplitude, the tilt, the correlated
isocurvature residual (0.7–2.0%, the registered line's class), and the network
density. **Gates:** the substructure count per network cell under screened
damping (a specified computation), and the network density for the medium's
parameters. Grade: candidate; the surviving route is unique.

### 23.4 Scope refinement to 23.1 (same day)

The conditional in §23.1 — "the bounce proceeds through the end of the metric
description or not at all" — is sharpened by the light-sector scale separation
(recorded the same day; [PRTOE_white_holes.md](PRTOE_white_holes.md) §11): the
closures exclude a HOMOGENEOUS turning point, and the description that ends at
the coherence scale is the *hydrodynamic description of the dominant component*,
while the substrate carrying the geometry — and the Standard-Model fields, which
cross the interval as ordinary in-medium fields with energy conserved — remains
coherent throughout. The turn is a sub-coherence-scale inhomogeneous event
powered by the component's gradient stresses (the verified rebound's engine),
and the restart surface is the past boundary of the re-expanding hydrodynamic
description. One architecture, two consistent descriptions; every computed
number of §23.1 is unchanged. The hot-start budget resolves at candidate grade:
the Standard-Model bath rides the contraction as its own conserved reservoir.

### 23.5 The amplitude's normalization derived (2026-07-28)

The triangle of §23.3 carried one owed derivation: why the primordial
amplitude's per-vertex factor is the screened coupling over the standard loop
measure. That derivation now exists at candidate grade, in three parts, each
with its check.

**The channel.** Small-scale structure on the network's vortex lines is erased
by pairwise exchange through the screened interaction. Every rival channel is
priced out by standard physics: quadrupole sound emission carries the velocity
suppression the cutoff computation already measured; contact damping through
the particle-hole continuum has the right size but the wrong coupling
structure (it grows with the screening factor where the amplitude's factor
falls with it); reconnection is not perturbative; resonant mode conversion
operates only where the substructure reaches the core scale — the observable
window's ultraviolet edge, consistently with that edge's referee role.

**The count.** The exchange needs exactly one partner quantum per substructure
cell, and that count is the occupancy principle of the vacuum-energy sector
applied at the cascade's marginal scale: the mode holds its quantum or the
structure is not there, and a second quantum is an excitation the cascade
passes down — the same two-sided occupancy-one argument, inheriting its own grade
and its named referee (P-2026-048). The sky has also weighed the count
directly: a partner count N would enter the amplitude cubed, and the measured
amplitude against the closed form pins N = 1.003 ± 0.005.

**The measure.** Below the screening scale the exchange is contact-class, so
the emission carries the unit isotropic measure and no residual energy ratios
— the factor 1/4π with nothing adjustable.

Together: the per-vertex factor is the screened coupling over 4π by channel,
count, and measure, and the closed form's three vertices stand derived at
candidate grade. Live referees: the crossover number of P-2026-048, the
kernel-host condition of the hierarchy sector (its one owed number), and the
concordance value of the screening factor at the chains' convergence.
