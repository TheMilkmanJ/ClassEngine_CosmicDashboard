# PRTOE — THE MATH SPINE (genesis → now → end)

> **THE FLAGSHIP CLAIM, AND ITS GRADE.** The dark-energy scale is
> **ρ_Λ¼ = (9/2)·α⁴·τ·m_e** — α⁴ times a temperature tied to the electron. Every factor is sourced
> except τ = T_c/m_e, and τ is where the claim lives.
>
> **τ is sourced by the Koide sector, and nothing cosmological enters.** The circulant kernel fixes
> its own modulus through Parseval: Q = 2/3 forces |f₁/f₀| = 1/√2, hence
>
> > **τ = ½ln2 = 0.34657 ⟹ T_c = 177.10 keV ⟹ ρ_Λ¼ = 2.2599 meV against the observed 2.25 — +0.44%**
>
> descending from Q, a lepton-mass fact measured to ten parts per million, through an exact identity
> ([PRTOE_koide_relation.md](PRTOE_koide_relation.md)).
>
> **What the +0.44% claims, and what it does not.** It is an **existence** claim — that the chain
> lands on the observed scale with nothing cosmological in it — and **not a precision** claim. The
> composite quartic maps to λ = 26–46, the whole band above the control edge λ\* = 22.41, so the LHY
> correction is uncontrolled at this order on every reading: its formal size would be 5.4–9.8% on
> ρ_Λ¼, while the next term of the same series is already larger. The agreement is therefore good to
> the order the series can be trusted, and the two decimal places are not the claim.
>
> **Grade: candidate. Its price is one hypothesis** — that the charged-lepton √m are thermally
> populated, which is what Q = 2/3 asserts (variance of √m equals mean squared, the Boltzmann second
> moment, holding to 18 ppm). **Its referee is one number:** a lattice T_c/√σ for SU(2), N_f = 3 —
> **and it is one job, not two:** the same non-perturbative treatment that measures τ is what the
> radiative band needs, so the λ and τ gates open together.
> **A lattice return at 0.34657 crowns the kernel and the dark-energy prediction together; one at
> 0.34506 shows the model reading the sky back, and kills both.**


> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*2026-07-10. The full quantitative chain in one document: every epoch, its governing equation,
what is DERIVED vs INPUT vs STORY, and where it lives in the code. Cross-references:
PRTOE_me_mechanism_math.md (dyad detail), PRTOE_cyclic_torus_genesis.md (genesis narrative),
PRTOE_UV_completion.md, PRTOE_cosmological_constant.md (J1).*

**Status tags:** [DERIVED] falls out of prior pieces · [INPUT] boundary datum · [STORY] coherent
mechanism, not a derivation · [PENDING] computation named, not run.

---

## 0\. The objects

One dark superfluid, two components (the two-field split):

* **Field 1** — the dcdf fluid: charge/abundance carrier, DM+DE unified. Mass m = 2.24×10⁻²⁰ eV
[**MEASURED**, confirmed three independent ways: the coherence length ξ = ħ/(m c_s) returns
398 AU against the recorded 402; the Schive core radius returns 7.14 pc against the recorded 7.0 for
a 10⁹ M☉ halo; and the superradiance window lands on its recorded 6×10⁸–3×10⁹ M☉ — **that third one
is support and exposure in the same object**: the band is populated and carries high measured spins,
and the model brings no defence there, the λ-quench margin computed at its own quartic and mass
being −83.7 to −85.8 decades across α_g = 0.1–0.5, so P-2026-034 stands or falls on the spin
measurements alone. Under the onset
clock T_on = √(m·M_red/0.61) this mass sits at **z_on = 4.03×10⁷ (log₁₀ 7.605)**, which is the value
`include/background.h` carries as the derived identity and which five of the six production configs
set. *(An earlier confirmation recorded here — the free-z_on optimizer's landing at log₁₀ z = 7.5517
read as "m = 2.29×10⁻²⁰, 2% above" — was arithmetically inverted: 7.5517 implies 1.75×10⁻²⁰, 22%
**below**, and that mass misses all three checks above by ~28%. The grade stands on the three
independent uses, not on that reading.)*
The former "derived from ε via c(m) = (m/m₀)^{1/4} at c = 1" was a relic of the SUPERSEDED
f_amp decomposition — in the standing decomposition ε = c·f̄·α_c the mass never touches the
census c, so **no roster-trial re-pricing propagates to m, z_on, or the hinge through this
route** (the hinge keeps only its α_c conditionality via c_s = √α_c). And read backward, the
old curve is dead by its own arithmetic: it would force c = 1.005 while the census excludes
c = 1. Provenance walk].
* **Field 2** — the dyad field: charge-free, couples to the electron; its condensate sources
δm_e. (Lepton-sector, and **a separate field from the Majoron**: the one-scale corner f = v_L is
tie-dead on the condensate-friction ceiling, so the sector carries two L-breaking scales and three
dark fields. What stays open is *which* v_L corner — TeV-class or MeV — and CMB-S4 is the selector
([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §6). **The portal's un-derived core is which Standard-Model
scalar the dark-neutral bilinear |Ψ|² multiplies.** The standing operator is the
quadratic-canonical m_e(φ) = m_e0(1 + κφ²), and the recorded roster of dark-U(1)-invariant
couplings — |Ψ|², |Ψ|⁴, ∂_μΨ*∂^μΨ, J_μ — reaches δm_e only through |Ψ|², which is a total
singlet: Lorentz-scalar, dark-neutral, gauge-neutral, **and L-neutral**. So it multiplies
|Ψ|²·ψ̄ψ (the standing charged-lepton choice) and |Ψ|²·(LH)(LH)/Λ with independent
coefficients, and lepton number screens neither — the Majoron's current couples to the phase,
which a phase-blind |Ψ|² operator cannot see. What carries leptophilia here is **data**: BBN
kills the quark bilinear at ≥ 12σ through the D/H quark→pion→deuteron channel. The symmetry
argument that does bite is the reverse one — dark-U(1) forbids any coupling linear in Ψ.)

The amplitude — the model's one distinctive number — assembled from three factors, each graded by a
running instrument:

> **ε = c·f̄·α_c = 27α/5π = 1.2543%** (concordance joint 1.2403 ± 0.0079%), with
> - **c = 9/10** — a counting fraction (N−1)/N over the universal charged-fermion roster: 9 charged
> species plus the vacuum's own seat, the neutrinos sitting on the seat rather than in the count
> because their mass is medium-sourced rather than electroweak. **The value is data-selected, not
> framework-forced:** the step that licenses a democratic count at all is open
> ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1, the two-census marriage), and what the
> value rests on independently is the ε-blind ensemble — c = 0.903 [0.867, 0.942], −0.08σ from 9/10;
> - **f̄ = 2/π** — the winding time-average, the mean-absolute-sinusoid ⟨|cos|⟩, forced by the
> winding's many-turn equidistribution; the coupling form is now data-selected (2026-07-16):
> mass-positivity kills the signed average (⟨cos⟩=0), leading-order (Yukawa, linear) picks
> mean-absolute over the quadratic/RMS readings, and the fit (0.625) + sim (0.635) confirm 2/π,
> rejecting RMS (0.707) at +13% — residual only "leading-order dominates";
> - **α_c = 3α = d·α** — **the dCDF's** condensate coupling (α is its Goldstone's — light *is* that
> Goldstone), the 3 being the spatial dimension d (second sound,
> geometry, and the induced loop-trace agree); the value a bet graded by the α_c MCMC.

> **Whose coupling is whose — the flagship's two fields, stated (2026-07-17).** ½α_c²M₂ hides that
> the dark-energy scale is a **cross of BOTH dark fields**, not one field's product. Substituting
> α_c = d·α and M₂ = α²·T_c collapses it to a closed form (verified identical to 4×10⁻¹⁹):
>
> > **ρ_Λ¼ = (d²/2)·α⁴·T_c = (9/2)·α⁴·T_c**, which on the kernel's τ gives **2.2599 meV against the observed 2.25 — +0.44%** *(an existence claim; the quartic sits past perturbative control, so the digits are not a precision claim — head of this file)*
>
> | factor | owner | why |
> |---|---|---|
> | **α⁴** = α_c² × α² | **the dCDF** | α_c² is its **binding**; α² is the **EM handshake** — and α is the dCDF's own coupling because **light is its massless Goldstone** ([PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) §4) |
> | **T_c** | **the dyad** | its condensation temperature, **177.10 keV** from the kernel's τ = ½ln2 |
> | **d²/2 = 9/2** | **geometry** | d = the spatial dimension (the same 3 as in α_c = 3α) |
>
> **Neither field produces the number alone**: the dark-energy scale is the dCDF's coupling raised
> to the fourth **weighing the dyad's condensation temperature**.
>
> > **The T_c row's owner is not settled, and the "cross of both fields" reading is the part that
> > depends on it.** This table assigns 177.10 keV to the dyad.
> > [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §6 assigns the flagship's τ·m_e to the
> > **SU(2) confinement scale** instead, and states that the dyad is neither of that sector's two
> > condensates.
> >
> > **The recorded chain leans to §6, on three independent points.** τ is *defined* as T_c/√σ — a
> > ratio to a confining string tension, which the dyad does not have; the one dimensionful input is
> > the **portal √σ_dark = m_e**, a statement about the confining sector; and the referee registered
> > for τ is a **lattice T_c/√σ for SU(2) with N_f = 3**. All three make T_c the confining sector's
> > transition, and §6 records that sector's diquark condensate as *being* the dCDF. On that reading
> > α⁴ and T_c both belong to the dCDF's sector, and the dark-energy scale is **one sector's product,
> > not a cross of two fields.**
> >
> > The arithmetic is identical either way — the two scales sit near the electron mass for separate
> > reasons, the portal in one case and the electron loop in the other — so nothing downstream of the
> > number moves. What moves is the structural claim in bold above, which should be read as
> > conditional until the assignment is ruled on.
>
> *(The decomposition is
> [PRTOE_build_2loop_Veff_spec.md](PRTOE_build_2loop_Veff_spec.md)'s, hunt 210–211; it is restated
> here because every reader-facing statement of the flagship wrote ½α_c²M₂ without saying which of
> the two condensates α_c belongs to — and the model has two.)*


## 1\. Genesis (the cycle's start) [STORY]

Torus topology survives the bounce (topology holds what dynamics loses); the confined heat
fountain (blueshifted crunch radiation) rolls up into a helical vortex ring → re-seeds the twist.
Flat 3-torus registered as P-2026-013. **BKL and Tolman stand against the bounce rungs — this
layer is a story built from real mechanisms, not a derivation.**

## 2\. Radiation youth → dark matter (the first transition) [DERIVED identity]

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

## 3\. The background fluid (radiation → dust → de Sitter) [DERIVED form; ρ_inf INPUT]

> **w(ρ) = −e^{−s}, s = ln(ρ/ρ_inf) clamped ≥ 0 ⟹ P = −ρ_inf exactly.**

So the background is ΛCDM-form: ρ = ρ_inf + C·a⁻³, algebraically (verified to 10⁻¹⁶).
w = −1 is EXACT for the constant floor — not a step artifact, not rampable. Code: `w_dcdf` /
`dcdf_s_of_rho` (background.h).

## 4\. The dyad turn-on (field 2 condenses) [the standing high-f configuration]

The dyad is a high-scale pseudo-Goldstone: **f ≈ 100–500 TeV (input)**, quadratic-canonical
operator m_e(φ) = m_e0(1 + κφ²) with **κ = ε/f² ≈ 1.4×10⁻³¹ eV⁻²** — ε = κf² = 1.2543% is the
frozen zero-mode's delivery. The full operating point (roll time, fluctuation floor 2×10¹⁸
below ε, thermalization gates clearing by 10⁸–10⁹, λ_dyad radiatively stable) is closed-form in
[PRTOE_me_mechanism_math.md](PRTOE_me_mechanism_math.md) (the high-f spec). **T_c = 177.10 keV**
(the Koide kernel's τ = ½ln2; lattice-gated on an SU(2), N_f = 3 value — the block at the top).

**The ramp's timing, stated exactly.** The electron bath's thermal restoration crosses the
dyad's own bare curvature where

> **C_T(T) = −(8/π²)·J_F′(m_e/T)·κ·m_e·T³ = 2λ_dyad·f²**

(J_F the standard fermionic thermal function) — **a relation with no renormalization-scale
logarithm**. So (λ_dyad, f, T_c) is a **two-parameter family, not three separate inputs**: any
two fix the third. With the recorded λ_dyad the relation places **f ≈ 145 TeV**
(122–172 TeV across the quartic-normalization conventions), inside the adopted window; read the other way, the window's 100–500 TeV range corresponds to T_c ≈ 130–940 keV.

**The perturbative cross-check, corrected.** The recorded T_c = m_e0·√(3(L−1)/2π²) ≈ 193 keV
and its [40, 900] keV envelope both used the *high-temperature expansion* of the thermal
function, which overstates the restoration by ~16× at this operating point (m_e/T_c ≈ 2.9 —
the electrons are Boltzmann-suppressed there). With the exact kernel the cross-check reads
**307–714 keV over L−1 ∈ [1, 10]** — a factor 2.3 in range where the recorded envelope spanned a
factor 22, and sitting *entirely above* the adopted 177.10 keV rather than bracketing it, by
**1.73× at its very bottom**. Stated plainly: the perturbative route does not corroborate the
adopted value at all — it excludes it; the adopted value's source is the confining chiral ratio,
not this route.

> **What that costs, and it is not only a comfort.** Intersecting the dyad's two internal
> determinations — this one and the timing relation's 130–940 keV over the registered f window —
> leaves **307–714 keV**, which **excludes 177.10 keV**. So the ramp ε(T) = ε(1 − T/T_c) is keyed
> on a temperature the dyad's own physics does not reach, while ε is the dyad's order parameter;
> §6 of [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) assigns 177.10 keV to the confining
> sector and rules the dyad is neither of that sector's condensates. **And the BBN safety argument
> does not survive the correction:** the ≤ 0.32σ whole-fence swing is stated on the fence [70, 500]
> keV, but **53% of the corrected band lies above 500 keV** (everything past L−1 = 4.1), where by
> the fence's own definition the dyad reaches n/p freeze-out and helium moves — an effect that
> bound does not price. Re-keying the ramp onto the dyad's own band is therefore a **numerical**
> question as well as a structural one. *(The 250–530 keV figure this replaces does not follow from
> the exact kernel over the stated range: it corresponds to L−1 ∈ [0.50, 4.78]. Recomputed from the
> same kernel that gives the file's own |J_F′| = 0.374 at m_e/T_c = 2.9;
> `scripts/audit_math_pass.py` carries the band.)*

*The predecessor configuration —
the electron-CW VEV v = m_e0·[ε(L−1)/4π²]^(1/6) ≈ 175 keV — is RETIRED (BBN-fatal at its
recorded operating point; autopsy in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md));
its formulas do not describe the standing model.*

**BBN clearance [CLEARS at the adopted T_c — and that value is the condition]:** the deuterium
constraint's severity decomposes by process: weak rates n↔p (T \~ 500–1500 keV, \~75% of the m_e
lever), n-decay phase space (\~10%), e± heating (\~10%), the bottleneck itself (\~5%, B_d nuclear,
m_e-insensitive). The dyad's transition is taken at T_c = 177.10 keV, and BBN itself fences it to
[70, 500] keV — the deuterium bottleneck below, the weak-rate window above — with the adopted value
interior by 2.5× and 2.8×, so **at that value the dyad never touches the weak-rate window**; AND the
dyad is LEPTONIC (quarks \~2-loop, \~10⁻⁹), whose full-BBN ceiling is \~0.3–1σ, not the universal/
hadronic 12σ:

> **effective tension = (temporal exposure 0.05–0.25) × (leptonic 0.3–1σ) ≈ 0.02–0.25σ → QUIET.**

**Read that against the band above, because it is the same question twice.** The clearance is keyed
to 177.10 keV, which the confining chiral ratio supplies; the dyad's *own* two internal
determinations intersect at 307–714 keV, which overlaps the weak-rate window across most of its
range and puts 53% of itself past the fence's 500 keV. So the clearance holds for the temperature
the ramp is keyed on and is **not** established for the dyad's own — which is why the re-keying
question above is numerical and not only structural.

"When D forms" ≠ "when m_e matters" — two different electron-scale clocks. Code: the dyad window
`varconst_transition_redshift < z < varconst_z_high` (`varying_z_high`, new 2026-07-10; ≤0
recovers the plain step). #40 (RG V_eff + BBN network) CONFIRMS, not decides.

## 5\. Recombination → today [the fitted era]

m_e shifted by ε = 1.24% inside the window (H₀ fix; ΔlnZ = +2.635 Laplace, SHOES-conditional, and
Laplace is where it stays — nested sampling waits for cluster time, so the estimate has no confirmer
in prospect and its margin over the win line is inside its own systematic);
screening returns m_e → standard below z ≈ 50 [survival form S = exp[−(C²/C_ref²)^n_eff], n_eff ≥ 35].
Optional rotation-shed `dcdf_conv_g` (S₈: minimizer picks g = 0.12, S₈ = 0.821 vs KiDS 0.814).
Corrected A2: the shed's apparent-w mirage is \~1% — OUT as a DESI driver; the S₈ job
survives (background ρ_m, not the w-mirage).

## 6\. The neutrino home [relation DERIVED-candidate; value INPUT]

Ψ = Majoron (L-breaking Goldstone): tree coupling σNN → Majorana m_ν → **0νββ must occur**
(P-2026-020); **Σm_ν ≈ 61 meV, normal ordering** — the sum from the tie below, the *ordering*
selected by data through the P-2026-004 collision (ANN-2026-021), not by P-2026-012, which states
it does not fix the hierarchy (ANN-2026-025). The sum is not a discriminator: it sits 2.6 meV above
the m₁ = 0 floor against ~20 meV planned resolution. The tie:

> **ρ_inf¼ = m_ν,lightest = 2.25 meV** — a single lepton-number-breaking scale μ sets both the
> dark-energy floor (ρ_inf ∝ μ⁴) and the lightest neutrino mass (m_ν = μ). The tie is exact to a few
> percent, and it is AZK-safe: the neutrino mass comes from the frozen radial VEV, not from a coupling to
> the neutrino density (which would be unstable).

The scale μ is a dimension-1 lepton-number-breaking parameter, distinct from the (dimensionless)
varying-m_e amplitude ε, which is electromagnetic — the two are different quantities and are not related
by any bridge. The value μ = 2.25 meV is not itself derived from first principles; that is the
dark-energy-value problem ([PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md) §2). **The tie's operator is now exhibited** (the tenth-channel seat
term, with its UV form above v_L and κ_m's size structural —
[PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md)); the seat constant b (κ_m's exact value)
remains basement-gated.

## 7\. NOW → THE END (the forward map)

> **Read 7a–7c with their verdict, which is below in the addendum and is adverse.** The full-cycle
> KP solve fired the internal falsifier: the clean Route-D prediction is dead, and what survives is
> a narrow imminent-turn corner needing a favorable alignment the priors do not favour. The running
> Route-D chain is the single decider. **P-2026-018 (w = −1 rigid) is the standing branch.** The
> sections below record the mechanism as it was worked out; the addendum records what happened to
> it.

**7a. The sequestered floor — a route that does not work.** A Kaloper–Padilla vacuum-sequestering attempt
to fix the dark-energy value from the cosmic expansion history was checked and fails: it predicts a
dark-energy-to-matter ratio at least ~5× too small (and zero for an eternally expanding universe). So the
value is not fixed this way. The model's standing dark-energy predictions remain **w = −1 exactly** and
the neutrino tie (ρ_Λ¼ = m_ν,lightest ⟹ Σm_ν = 61.4 meV).

**7b. The thaw [the forced consequence].** Observed Λ ⟹ turnaround within \~an e-fold ⟹
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

**The turnaround lands at a ≈ 2.0–2.8 (z ≈ −0.51 to −0.65), 16–26 Gyr from now** across
w₀ ∈ [−0.92, −0.86] and two orders of magnitude in B: the trade-off between thaw rate and
bare depth holds the answer nearly fixed, so the timing is a consequence of the structure
rather than a tuning of it. **The bare depth is invisible in the expansion history** — the
same trade-off makes the low-redshift trajectory B-independent to ~0.2% — so the turn itself
is not a measurement; what the sky grades is w₀. *Branch note: this is the expanding branch's
parametrization (the field rolls forward in time, it does not roll back up as a decreases);
the contracting branch and the bounce need the field equation solved in time — the bounce
sector's own debt.*

The thaw completes → expansion reverses → contraction
blueshifts radiation (a⁻⁴ grows) → the heat fountain reignites → T climbs back through **T_c**
(the SAME T_c of §4) → **the dyad condensate MELTS** (m_e → standard for the crunch) →
charge survives in solitons/Q-balls [requires gravity-mediated K<0: fragmentation
banks the charge at T \~ 10¹⁰ GeV, 13 decades before any melt] → torus topology carries the axis
across the bounce (rotation resets, topology doesn't) → re-expansion cools through T_c → the
condensate RE-FORMS → §1. **The condensate breathes; T_c is both the recombination-era turn-on
and the crunch-era melting point — one number, both jobs** (the two-jobs law, §2).
[STORY at the bounce rungs: BKL, Tolman unresolved.]

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

## 8\. The two-jobs pattern — and where the code reflects it

Every transition is ONE clock with TWO jobs — the ending regime reaches its floor, the starting
regime crosses its threshold:

|transition|job 1 (floor reached)|job 2 (threshold crossed)|in code|
|-|-|-|-|
|H=m (z=4×10⁷)|conformal youth ends|DM (dust) begins|`dcdf_rho_rad` f(a): one function fades radiation as dust continues, continuity-matched|
|T_c (dyad)|thermal disorder dies|condensate/δm_e turns on|`varying_z_high` edge (2nd-order: no latent budget to hand off — a pure switch is CORRECT here)|
|ρ→ρ_inf (z\~0.7)|matter dilution bottoms|de Sitter begins|`w_dcdf(ρ)`: one barotropic function does both automatically|
|shed|matter-part drains|dark radiation grows|the SAME `conv` term, opposite signs, in two ODEs (background.c:2843-45) — the pattern literally|
|thaw/turnaround|the floor era ends|the turn begins|`dcdf_floor_thaw` (new)|

The conservation-pair transitions carry the two jobs as one term with two signs; the
second-order (continuous) transition carries them as one edge with no budget. **The code
reflects the law wherever the law demands it, and correctly does NOT fake a hand-off where
the physics has none.**

## 9\. Ledger (what this spine rests on)

**Recorded:** DM+DE unification (2→1); ε derived; onset = H=m identity (z = 4.03×10⁷, the mass
pinned independently by ξ, the Schive core radii and the superradiance window); **the dyad onset is
T_c = 177.10 keV from the Koide kernel's τ = ½ln2** — the value's source is the confining chiral
ratio, not the electron loop, whose predecessor *configuration* (the CW VEV at ≈ 175 keV) §4 retires
as BBN-fatal. What survives from that loop, and is used above, is the κ-independent restoration
*formula*, which supplies the ramp's timing and is why the transition sits at the electron scale for
any decay constant; AZK-safety; leptonic allowed ≠ generated.

**Falsified:** P-2026-004 (high Σm_ν); the sequestering route to the dark-energy value (§7a, and the
full-cycle KP solve in the addendum — the internal falsifier fired).

**Live falsifiers:** DESI DR3 (the branch), Σm_ν ≈ 60 meV, 0νββ, void/IGM m_e-step (P-007, J4).

**Settled since this ledger was last written** — each was carried here as owed and each is closed
elsewhere in the corpus:
- *KP self-consistency* — resolved **in this file**: §7a reports the attempt fails, and the addendum
  reports the full-cycle solve firing the falsifier.
- *spurion identification* — done in [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md) §2: μ is a
  dimension-1 lepton-number-breaking parameter, distinct from the dimensionless varying-m_e amplitude.
- *low-scale seesaw* — **adjudicated** by the seesaw duty scan (same file).
- *leptophilia* — established in [PRTOE_dyad_gas.md](PRTOE_dyad_gas.md) §2, and **by data**: a
  universal quark-mass shift at ε lands at +12–18σ on D/H. What is settled is that the coupling is
  leptonic; the *portal* is not, and it is carried in the owed list below.
- *the gate-0 confirm* — #40 (RG V_eff + BBN network) confirms rather than decides (§4).

**Genuinely owed:** the dark-energy *value* if Route-D dies (falls back to constitution — the
branch is DESI DR3's to decide); the seat constant b in the neutrino tie, gated on the basement
build — which is itself gated on the band structure the hierarchy chain's §6c needs, docket #146
([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §8, the open-surface table); **the portal's
selection rule** — which Standard-Model scalar the singlet |Ψ|² multiplies (§0), desk work with no
external gate, docket #125.

**Standing:** provisional pending the named referees, DESI-capped; the branch is registered
(P-2026-056) with its guards discharged, and its adjudicating chain is running.

*(Every debt on this page names where it is closed or what it waits on. Bare "owed" is not a
status: [`working_logs/_DOCKET_INDEX.md`](working_logs/_DOCKET_INDEX.md) resolves task numbers, and
where this page and a physics file disagree, the physics file is right.)*

---

## ADDENDUM (2026-07-10, later): §7 STATUS CHANGE — the internal falsifier FIRED

The full-cycle KP solve (full_cycle_kp.py, scratch-era, not retained) computed the fixed point over the whole
cycle (expansion + thawed contraction + Tolman boost): **it robustly wants a_turn = 0.70 (a PAST
turnaround, z=+0.43)** — excluded by observed acceleration; a future turn is 3× (a_turn=1.0) to
10× (1.5) short, Tolman boost null, and the "full-cycle-fixes-the-sign" claim was WRONG
(near-mirror contraction cancels). **So §7a–7c are DOWNGRADED:** the clean Route-D prediction is
dead; what survives is the IMMINENT-TURN CORNER (z_turn \~ −0.1..−0.3, needing \~3× from four
favorably-aligned rigorous-KP O(1)s [prior-adverse, tail] AND a strong thaw pulled by the data).
The two kill switches MERGE: the running Route-D MCMC (thaw free on the DESI joint stack) is the
single decider — thaw pulled hard → corner lives; thaw \~ 0 → Route-D dead twice over, **P-2026-018
(w = −1 rigid) stands as the distinctive branch, and J1 reverts to constitution/boundary-datum.**
§7d (the melt/re-form cycle closure) is unaffected as STORY. Held provisional. *(The turn's
own timing follows from the surviving structure — the thaw plus the sector's negative bare
piece — and is later than this corner's z ≈ −0.1…−0.3, which rode the sequestering route:
see §7d.)*

---

## §10 — THE ATOM READING (the capstone, 2026-07-10 night)

**The universe is a single bound quantum state of the spacefluid — one atom — and cosmology is
its internal atomic physics.** Formation: genesis = recombination (capture cascade; f_amp = the
branching ratio, computable-class). Structure: Landau's two components — the zero-entropy ground
state (floor/constitution/timeless; w=−1 exact \& ageless by theorem) and the entropic excitations
(light/matter/observers; Tolman's arrow). Spectroscopy: torus modes = the line spectrum (low-ℓ =
the first lines); the census = the selection rules; the CMB = the recombination photograph.
Chemistry: the dyad = one universal lepton rescaling ε (Koide-multiplicative), C²-gated, one
fingerprint across H₀/D-H/ν/21cm/radio. Present: mid-emission — Γ_par/H = √3 (IR scale) and
Γ_eff/H = √(3/2) with B = 1/√2 (Jeans growth rate, derived) = the linewidth
(why-now); symptoms {coupling dipole, mass defect = the thaw, recoil = the axis} = the falsifier
board. Biography: first excitation (Tolman arrow, finite past) → lengthening cascades → possible
ionization (binding energy un-computed). J1 = the ground-state eigenvalue: constitutional, at home.
**Status: the grammar is coherence (graded throughout);
the empirical content lives in the children and the symptom chart. The method was the subject.**


## §22 — THE THREADING DAY (2026-07-11, the second arc): sixteen roots, lawful deaths, the ladder, and the BBN witness

**The threading survey:** sixteen direct threads filed and graded (galactic/SMBH
atoms, the neutrino home, S₈, low-ℓ, Koide's invariance, the lab cousins, the coincidence
problem [why-now = √3·A_s·the floor — the √3 one-pager discharged: the Friedmann factor,
value-independent; B = 1/√2 derived from Jeans dispersion, par-question closed
for the thaw rate], the purchased silences [direct+indirect],
GW [the vortex null Gμ ~ 3×10⁻²¹; the chirality family's third member], the Hubble standalone,
the radio lattice, the fingerprint capstone, IGMF helicity, LSS parity). **The protocol** (now
standing law): model every transition as smooth unless quantization protects a jump; adopt a
replacement only when it improves on what it replaces; and when a claim dies, record why — which
step failed, which coupling, and which downstream claims inherit the death — rather than letting
it lapse quietly. Debts are itemised where they are incurred. **The inheritance theorem:** no orphan physics (L1) — every non-thread is a child
of a threaded root; deaths are lawful (each names its law — strong-CP and birefringence share
L1a, one clause, shared fate both ways).

**The master computes (the 40 debts factor to 8, in 4 clusters):** par/size (the α_c MCMC +
the lanes), topology (the AD route + the cavity), frame/UV (the Lorentz program + λ), data
(the chains + the epoch stamps). Sprint results: the toy cavity puts ℓ=2,3 BELOW the first
torus mode (T5's matched-circles risk resolved favorable); the thermal-leptogenesis surface is
EMPTY (×40-1000 under everywhere) → **the baryon asymmetry reverts to the native AD-direct route (charge =
abundance) with the frozen-era transfer (sphalerons at 130 GeV vs the field frozen till
9.4 keV) as the hard timing crux**; the λ candidate chain failed its own bounce self-check
(informative).

**The λ-ceiling (a small recovery):** the winding-patch isocurvature (14.1% rms
if the onset is quartic) would be CMB-dead ×5-7 → the model REQUIRES λ ≤ (m/Ψ₀)² ≈ 2×10⁻⁹¹ —
a derived self-constraint; the axion-like reading (λ ~ m²/f²) lands at the ceiling within an O(1)
factor → **P-2026-031 (candidate): CDM isocurvature at ℓ ~ 170.** *(Amplitude caveat: the axion
quartic carries a coefficient ~1/6, so |λ| sits a factor ~6 below the naive (m/Ψ₀)² ceiling — the
isocurvature is then likely sub-%-level and below current Planck sensitivity, not at it; the exact
amplitude awaits the O(1) coefficient and the λ-sign.)* (+ a 45-90 km/s bulk-flow shadow). MOND/RAR finally dead (m_amp → m; ≤59 AU ≪ kpc). The third
mass-top coincidence (CSW M_max ~ 10¹¹ M☉ at the ceiling; with α_g = 1 at 6×10⁹ and r_s = ξ
at 2×10¹⁰) — noted, m-correlated, not recorded.

**The scale ladder:** the Bohr skeleton E_b/(mc²) = ½α_eff² at every rung (the
universe rung SITS on its own skeleton: 2.28 vs 2.29×10⁻⁴); the corrected ordering (nucleon >
nucleus > UNIVERSE > atom > star > galaxy — the universe is the tightest GRAVITY-made
structure); **the hinge: ξ = 402 AU inside the solar-system rung — one substrate boundary in
the whole descent**; the double-ladder alignments graded per-rung (2 definitional, 3 loose —
no mechanism, honestly tagged); the energy cascade owed as the dynamical half.

**THE WINDOWED BBN VERDICT:**
T_c (177.10 keV on the kernel's τ; 179 keV in the superseded reading — the conclusion is
insensitive to the difference) is INSIDE the BBN window → the ε(epoch) stamps re-price everything: **the Y_p
medicine was an artifact of applying ε above T_c** — windowed, Y_p ≈ 0.24900 (+1.09σ
COUNTER vs Aver; +3.53σ vs EMPRESS — the helium civil war noted); D/H partially refunded
(2.387 → **−2.9σ** vs Cooke on the full stated budget: obs ±0.030 ⊕ PRIMAT post-LUNA nuclear theory ±0.037; the 3.5% inter-code spread is named and unfolded, and would soften it to −1.4…−2.2σ).
**Re-priced under the standing high-f configuration + the committed genesis dilution ζ = T_dark/T_γ ∈ [0.25, 0.35]
(ΔN_eff = 0.06–0.24): D/H −2.5…−1.4σ on the quotable ±0.0476 budget (−1.2…−0.7σ if the full
inter-code spread is folded), Y_p +1.3…+2.0σ vs Aver (EMPRESS +3.8…+4.4σ stands apart), joint
p = 0.02–0.08 quotable / 0.12–0.21 on the full spread. The residual helps deuterium and does not
heal it; the sector's verdict still turns on the code systematic. The σ's in the sentence above
are the window's own effect, before the residual —
[PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §8, books in
[PRTOE_bbn_witness.md](PRTOE_bbn_witness.md).** **The BBN synthesis: the sector is THE
TRANSITION'S WITNESS** — the only laboratory that watched the condensation live; the pattern
is RIGID (no dials); referees: the radio referee, the helium resolution, the T_c re-audit
(flagged-not-taken), the α_c MCMC posterior. The adverse landings are logged in public;
the λ-defense is on record.
