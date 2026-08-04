# The m_e mechanism — consolidated mathematical formulation

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Amplitude grades: [PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md). Reasoning and dead ends: [PRTOE_me_trigger.md](exploratory/PRTOE_me_trigger.md).

Equations-only companion to the trigger doc. Every result is cross-referenced to its trigger-doc section. Assembled 2026-07-07; high-f operating point 2026-07-18.

**Audience grade.**

| item | grade |
|---|---|
| Form m_e(x) = m_e^lab [1 + ε S(x)], ε = 1.2543% | standing claim; ε stack **conditional** (see Amplitude) |
| Environmental variable Θ / Weyl gate | **derived / forced** (conformal portal → C²) |
| Transition sharpness | **forced** by MICROSCOPE + quasar (two-constraint) |
| Weyl not Ricci | **derived** (three independent reasons) |
| Amplitude ceiling ~1–2% (EM self-energy) | **derived** as bound; exact value from stack |
| High-f operator (dim-6 lepton) | **assumed** (data-narrowed, not symmetry-selected) — docket #125 |
| Electron-loop onset / low-f config | **dead** (BBN-fatal; failures ledger) |
| Canonical T_c | **177.10 keV derived** (Koide τ); κ-independent formula survives; 179 pipeline; 193 cross-check |
| ρ_Λ / CC residual | **existence not precision** where it lands |
| Θ-averaging / developed-speckle compliance | **retired** as route; laminar Θ branch survives |
| Conversion-channel linear perts | **implemented** when `dcdf_conv_g > 0` (CLASS; not this file) |

Do not cite the retired electron-loop onset as current. Body below keeps equations and numbers; grades above police how to read them.

---

## 0. The claim, in one line

The electron mass carries a fractional environmental shift
`m_e(x) = m_e^lab * [1 + eps * S(x)]`, where `S(x)` is a sharp/binary
"smoothness" indicator (1 in unstructured space, 0 in virialized structure)
and `eps = 1.2543%`. The CMB is imprinted at the bare value `m_e^lab*(1+eps)`;
all present-day (virialized) measurements see `m_e^lab`.

---

## 1. The environmental variable

The medium is a complex superfluid order parameter (Room 1):

 Psi(x) = |Psi(x)| * exp(i * ξ(x))

The coherence/smoothness indicator is built from the phase field. Define the
multi-stream (shell-crossing) bit via vorticity of the phase-gradient
velocity `v = grad(xi)`:

 Theta(x) = 1 if the medium is single-stream (smooth, curl-free, coherent)
 Theta(x) = 0 if multi-streamed / vortex-tangled (structured, decohered)

Key identity (exact): curl(grad(ξ)) = 0 for any smooth single-valued phase,
so Theta can only flip at genuine phase defects (vortices) -- structure.
[trigger-doc sec 3, 20]

Smooth observable proxy: the Weyl curvature invariant C², which is
identically zero in conformally-flat FRW and nonzero only where tidal
structure exists:

 S(x) = f(C²(x) / C_ref² ), f = a near-step (saturating) function

---

## 2. The coupling

 L_int = -eps * S(x) * m_e^lab * (psi_e-bar psi_e)

This is a direct, dimension-5 operator with S(x) the environmental modulator.
The operator is legal under the model's coupling law,
by the constitution's own consolidated clause (laws_and_rules, the L1 block):
the medium couples to ordinary matter only through gravity, and the second
field may couple non-gravitationally within its own sector — the lepton-mass
sector — while opening no interface to sectors it is not part of (no photon
coupling, no quark coupling). This operator satisfies all three tests:
 (1) it lives inside the permitted sector (it shifts a lepton mass);
 (2) its environmental switch reads curvature — gravity's own universal
 channel, the one interface everything already shares — so the modulation
 opens no new interface;
 (3) it treats every lepton alike (the doublet-universal structure of sec 10);
 the electron is singled out only by being the charged lepton present at
 recombination, not by hand. The identity-blindness rule polices couplings
 that pick species without a symmetry reason (the deleted per-species knobs
 were exactly that); a coupling that follows the lepton charge is not
 one of them.
Prior verdicts stand with the clause (the birefringence null, gate-0, the
EP posture, BBN). Sec 7's screening computation is a separate item from the
legality question, and it is delivered on all four of its items there. The form is forced:
geometry is 60 orders too weak (sec 32), so a direct operator is unavoidable.
[trigger-doc sec 23, 32, 34; laws_and_rules]

---

## 3. The functional form is forced sharp

Requirement A (MICROSCOPE, sec 26): the residual shift inside structure must
satisfy the Eotvos bound. Differential Ti/Pt sensitivity:

 d ln M_atom / d ln m_e = Z - E_bind/m_e, E_bind = 15.73 * Z^(7/3) eV
 (Ti: 2.517×10⁻⁴ ; Pt: 2.171×10⁻⁴ ; differential: 3.46×10⁻⁵)
 ⇒ residual |δ m_e/m_e| at Earth < 8.7×10⁻¹¹

Requirement B (quasar, sec 7/12): a smooth density-dependence gives absorber
differentials 1×10⁴ over bound → binarity forced.

Consequence: a gentle exponential fails -- the curvature gap between
recombination and dwarf cores is only ~22x (1.35 decades) but the required
suppression is 8.2 decades. Minimum power:

 S(x) = exp[ -(C²/C_ref²)^n ], n > 2.43 (forced, sec 27)

i.e. a near-threshold/step. Both independent constraints force the same
sharpness → two-constraint pillar. Once suppressed at the dwarf core,
Earth (17 decades higher C²) is automatically suppressed. [sec 26, 27]

C_ref is not a free scale: the transition is set by a topological event
(first shell-crossing / first vortex), not a tuned curvature value. [sec 27]

---

## 4. The amplitude

Ceiling (sec 31): only the electromagnetic part of m_e can respond to an
EM-binding environment. Split:

 m_e = m_bare(Higgs-Yukawa, ~99%) + delta_m_EM(self-energy, ~1%)
 delta_m_EM/m_e = (3 α / 4pi) * ln(Λ²/m_e²) ~ 1-2% (O(α))

So eps ≤ (EM self-energy fraction) ~ 1-2%. The standing 1.2543% sits at the
ceiling. The size is derived here as a bound; the exact value comes from the standing
stack eps = c*fbar*alpha_c = 27*alpha/(5*pi), which uses no cutoff at all --
it, not this section's Lambda-and-modulation route, sets the value. **Stack grade: conditional**
(f̄ derived, c assumed, α_c bet). [sec 28, 31]

Why m_e and not α: varying-α killed by quasars (45-100x); m_e evades
those bounds -- the surviving EM-binding knob, selected by data. [sec 7, 29]

---

## 5. Which curvature piece, and why

The trigger couples to Weyl (tidal/radiative), not Ricci (local/binding):
 R1. Ricci fails directionally -- large at both high-z background and in
 halos, cannot distinguish smooth-dense from clumped. [sec 25]
 R2. Weyl = 0 identically in smooth FRW (conformal flatness) -- exactly the
 "bare in smooth space" requirement. [sec 23]
 R3. The switch fires on a decoherence event; decoherence is driven by a
 force's radiative/far piece; Weyl is gravity's radiative piece; Ricci
 (binding piece) cannot trigger a decoherence event. [sec 30]

Near/far force split (general): every long-range force = near piece (binds)
+ far/radiative piece (carries info away = decoheres). EM: Coulomb binds,
photons decohere. Gravity: Ricci binds, Weyl decoheres. [sec 30]

---

## 6. The amplitude-channel constraint (why the roof is one question)

A viable channel must be simultaneously strong [S] (O(α), not curvature-
suppressed), legal [L] (census + MICROSCOPE), varying [V] (smooth vs
structured). Scored:

 curvature : L,V not S (60 orders weak, R/m_e²~1×10⁻⁶⁹)
 direct coupling : S,V not L (census scope, open)
 khronon/frame : S,L not V (spatially uniform)
 intrinsic dm_EM : S,L not V (present everywhere equally)

Only the direct coupling has S+V — and its L is now delivered: the coupling
law's consolidated clause legalizes sector-internal coupling (sec 2), and
MICROSCOPE-safety within L is delivered by the sec-27 sharp screening.
⇒ the roof is closed; the channel constraint is satisfied on all three
properties. [sec 34; laws_and_rules]

---

## 7. The EP escape (fifth-force gate)

Smooth dilaton: needs β~0.012, MICROSCOPE allows β<~1×10⁻⁴ → 2 orders
over → dead.

Escape: the field is the sharp/saturated Theta (sec 27 sharpness), not a
smooth dilaton. Inside the virialized MW halo Theta is at its ceiling →
grad(Theta) ~ 0 (flat top) → grad(φ) exponentially suppressed → no
fifth force. Chameleon-class screening; screening agent = Theta saturation
(forced, not tuned). Freezing agent = virialization (medium's own dynamics,
static in a virialized halo).

Screening-test corroboration (sec 37, computed): atomic clocks are a genuine
third independent leg -- they kill the continuous version via temporal physics
(a continuous 1% coupling gives ~1×10⁻⁴ clock modulation, ruled out), while the
saturated form predicts a null (observed). Caveat: clocks force the screening-
consequence, not the sharp-form-cause uniquely. White-dwarf spectroscopy =
consistency-check (saturated → lab value, confirmed ~1×10⁻⁵). Continuous version
now killed by two independent experiments (quasar spatial + clocks temporal).

The four deliveries, paid under the survival-form gate (S = exp[−(C²/C_ref²)^n_eff],
n_eff ≥ 35, threshold event-set):
 (i) recombination sits ≥22× below the threshold scale in C²,
 so 1 − S = (1/22)^35 ≈ 10⁻⁴⁷: the bare value rides to ~47 decimal places
 (the amplitude itself is the high-f operating point's own record).
 (ii) the laboratory checklist: every terrestrial environment
 sits ~25 orders above the structure-class edge (curvature penetrates
 vacuum chambers, so the chameleon-trap tests do not apply); MICROSCOPE is
 out of range by kinematics; the mm–cm band is torsion-balance territory,
 already fenced.
 (iii) freezing is structural: the switch is a function of the
 local Weyl invariant, not a field with its own relaxation; virialized
 tidal fields evolve on Gyr timescales and the step is pinned at
 S = exp(−10^10)-class or deeper, so no fluctuation of any ordinary size
 moves it. No separate relaxation dynamics exists to fail.
 (iv) molecular-hydrogen absorbers require dense shielded gas,
 which exists only deep inside virialized structure: the predicted
 delta_mu/mu is zero to the same exponential depth, against observed nulls
 of ~10⁻⁵–10⁻⁶. Stated edge: pristine unvirialized gas carries the bare
 value but forms no H₂ — the mu-probe cannot reach the unscreened phase;
 the void-side falsifiers are the 21-cm channels (P-2026-043, P-2026-050).
Graveyard Rule 3 satisfied: nothing here inherits from the abandoned v1–v3
machinery — the survival form was derived independently this cycle (the
event-set/first-passage structure), and these four results follow from it
and the recorded curvature ladder alone.

---

## 8. Observable signature

Under a single m_e amendment, all EM-binding observables shift in locked
correlation (sec 29):

 binding energies (Rydberg ~ m_e): +1.2543%
 atomic sizes (Bohr radius ~ 1/m_e): −1.2543%
 transition frequencies: +1.2543%
 21-cm hyperfine (~m_e²/m_p): +2.51%

Discriminator: the dark-ages/cosmic-dawn 21-cm sky (unvirialized IGM,
Theta~1, bare value) vs the standard (virialized) sky. A specific
correlated pattern across all EM-binding observables, not a single-line
shift. [sec 8, 29] REACH/SKA-low class instruments.

Forecast numbers (chain-free, from dln nu_hf/dln m_e = 2 and eps = 1.2543%):
 the bare-value hyperfine frequency runs +2.509% high in unvirialized gas.
 - The clean channel — the dark-ages absorption trough (z ~ 85-90, linear
   physics only, no stars): standard 15.8-16.5 MHz -> model 16.2-16.9 MHz,
   a +0.40 MHz offset that cannot be absorbed into astrophysics. Instrument
   class: lunar farside (LuSEE-Night / FarView). This is the mechanism's
   sharpest astrophysics-free falsifier outside the CMB.
 - the cosmic-dawn trough (EDGES band): 78.0 -> 79.96 MHz (+1.96 MHz) —
   degenerate with star-formation timing; consistency channel only, stated
   as such.

---

## 9. What is derived vs open

Derived or forced:
 - the environmental variable (Theta, vorticity-based, exact identity) [1]
 - the coupling form is forced (geometry 60 orders too weak) [2]
 - the transition is forced sharp by 2 independent constraints [3]
 - Weyl not Ricci, 3 independent reasons [5]
 - the amplitude size/ceiling (EM self-energy fraction, ~1-2%) [4]
 - the roof reduces to one question (census scope) [6]
 - the locked-correlation observable signature [8]

Open / graded:
 (census-scope legality: closed — the coupling law's consolidated clause; sec 2, 6)
 (the amplitude coefficient: stack 27*alpha/(5*pi) — **conditional**: f̄ derived, c assumed, α_c bet [4])
 (the sec-7 screening computation: delivered — all four items, see sec 7)
 - the two-field sims (sim-gated): confirm S=(1+f_rot²)/2, ψ/χ layering [trigger-doc]

The empirical fit (m_e = 1.012543, fits the CMB) is untouched by all of the
above -- this document concerns the mechanism's legality/derivation, not
the data. H₀/ΔlnZ from that fit remain **provisional**.

## 10. The leptonic origin -- why m_e and not m_q (2026-07-09)

BBN (the data ruling — the windowed program) requires the coupling be leptonic: a universal
mass shift is 12-16σ dead via the D/H quark→pion→deuteron channel (dln(D/H)/dln m_q ~ 15 vs
dln m_e ~ 0.5, a 30x ratio). Why the coupling picks the electron:

No-go (it is not a symmetry): L-bar H e and Q-bar H d both need a gauge-singlet scalar;
a singlet couples to every Yukawa operator with independent coefficients → no gauge
symmetry forces leptonic. Froggatt-Nielsen also fails -- the light quarks (u,d) carry
FN charges comparable to the electron's, so a generic flavon shifts m_q and re-triggers
BBN. Leptophilia is neither a gauge nor a generic-flavor consequence.

What is actually on offer (the operator roster, #125). The portal must be **even** in the
electron-coupled scalar, so what multiplies a Standard-Model operator is the dimension-2
singlet |Ψ|². Three couplings are available, ordered by dimension:

 |Ψ|² H†H [dim 4, renormalizable] → shifts the Higgs vev → every mass, quarks included
 |Ψ|² L̄He [dim 6, → m_e ψ̄ψ after EWSB] → δm_e alone — the standing choice
 |Ψ|² (LH)(LH) [dim 7] → δm_ν alone; cannot reach δm_e at any coefficient

The renormalizable one is the one the model must do without: a universal shift at ε is
+12–18σ on D/H, which bounds λ_p ≲ 5×10⁻¹¹…1×10⁻⁹ across f = 100–500 TeV. **That exclusion
is affordable and the statement is computed**: the standing dim-6 lepton operator feeds
H†H back through one electron loop at λ_p ≤ ε·y_e² ≈ 1.1×10⁻¹³ (Λ_UV = 4πf; 6.8×10⁻¹⁶ at
Λ_UV = f) — from ~500× under the bound at its tightest corner to ~10⁶× under at the loosest —
so the induced universal shift reaches at
most 2×10⁻³σ on D/H. No tuning is spent inside the effective theory; what is assumed is
that the completion above f writes the lepton operator and not the other two.

Why the electron, and it survives the roster change: the operator shifts all charged
leptons equally (e, μ, τ); only electrons are present at recombination (μ, τ decayed), so
the electron is the charged lepton present, not a chosen flavour. No flavon needed.

The finer fork — one coefficient or two. Writing |Ψ|² into the lepton doublet's
normalization rather than into each mass operator separately correlates them: the charged
mass carries one power of L and the Weinberg operator two, so

 δm_ν/m_ν = 2 · δm_e/m_e = 2.51% inside the window

with the factor 2 pure operator counting. Independent coefficients leave δm_ν free instead.
**Nothing selects between them and nothing can**: the correlated point moves Σm_ν by 1.5 meV
inside a window whose exit restores the present-day value the sky measures — observationally
identical to the free case. The pipeline runs the correlated point (`background.c`, m_ν ∝ m_e²).
(assumed; docket #125)
Magnitude + self-consistency (computed 2026-07-09, re-keyed to the standing operator):
 (a) The coupling profile is forced to be condensation-triggered, not smooth in the field.
 A profile that tracks the field's own redshift gives dm_e(z=2) ~ 1.8×10⁻⁶ -- at the
 quasar bound (|dm_e/m_e| <~ 1×10⁻⁶ at z~1-3). The model avoids this with the z=50
 step (dm_e=0 below z=50; the condensate/transition reading, see [28]). So the shift
 must switch at condensation and be gated thereafter, which both matches the code and
 dodges quasars. This ties [10] to the [28] reconciliation (resolved to a
 condensation-step, not smooth).
 (b) The loop, worked (2026-07-09). Minimal potential V(Psi)=ρ_inf + 1/2 m² Psi²
 (DM oscillation early, DE floor late). It closes to consistency: the DM→DE
 transition lands at z~0.7 (1/2 m² Psi² = ρ_inf), the right epoch (observed
 ~0.3, same order) for the model's own m + abundance; and ρ_inf^(1/4) = 2.25 meV =
 m_ν,light [P-2026-012]. But it bottoms out at the CC problem: why ρ_inf=(m_ν)⁴
 is P-2026-012's posit, not derived. So the last residual is the
 cosmological-constant question -- not a PRTOE-specific gap but the universal one
 (reduced to the cosmological-constant question).

The delivering operator is not selected by
any symmetry the model carries: a gauge singlet couples to every Yukawa operator with an
independent coefficient, which is this section's own no-go read forwards. Data does the
excluding -- H†H and the quark bilinear at ε are both +12–18σ dead on D/H, and the Weinberg
operator reaches no charged mass at all -- so what remains standing is the lepton bilinear by
elimination, with the doublet-normalization correlation an assumption on top of it. The portal
is data-narrowed and assumed, not derived, and its one
discriminating observable is unreachable. Docket #125.

The EP-screening computation [7] is resolved (2026-07-09):
the composition-dependent Vainshtein-screened Delta_a/a = 8×10⁻²¹..8e-19, 3-5 orders below
MICROSCOPE (screened regime, cubic galileon); EP gate clears, favorable-prior, sole
caveat a non-standard eps_V^(1/2) power (numerical galileon solve would fully discharge).
So varying-m_e is single-gated on DESI. And the leptonic-origin mechanism (this section)
resolves item [2]'s "census-scope legality" via interface/substance -- the coupling is legal
as substance. What stays open is not the legality but the *selection*: which legal operator
delivers δm_e, which is assumed above (#125), and the CC value the loop reduces to.

---

## The electron-loop onset — the predecessor configuration

> This section describes the retired operating point, in which the electron's
> Coleman–Weinberg backreaction drove the electron-coupled scalar's condensation. That
> configuration is BBN-fatal at its own numbers and no longer describes the model
> ([PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)); the standing configuration is the
> high-f operating point above. What survives from the work below is the κ-independent
> transition-temperature formula, which still supplies the ramp's timing. The rest is kept for
> the record and must not be cited as current.

On the charge-free scalar, the electron Coleman–Weinberg backreaction was taken to set the
condensation scale, making the onset derived rather than a free input.

Zero-T (the VEV / reduction). m_e(φ)=m_e0(1+κφ²); the electron loop gives
V_CW(φ)=−(1/16π²)m_e(φ)⁴[ln(m_e(φ)²/μ²)−3/2], whose φ² term is a tachyonic induced mass
m_φ²(0)=−(κ/2π²)m_e0⁴(L−1) (radiative SSB). Self-consistent VEV
**v = m_e0·[ε(L−1)/4π²]^(1/6) ≈ 175 keV** (150/175/196 keV for L−1=2/5/10) — the CW minimum imposed
together with the delivered shift κv² = ε (full 1.2543%), which fixes κm_e0² = ε(m_e0/v)² ≈ 0.108;
robust under the 1/6-power. So the onset falls out of m_e0 + the scalar's amplitude alone = a
genuine reduction (the onset is no longer free). Un-swamped because field 2 carries no charge →
no TeV soft mass.

Finite-T (the coin-flip). Thermal mass Δm_φ²(T)=+(κm_e0²/3)T² (electron plasma, symmetry-
restoring); symmetry restored above T_c where it cancels the tachyonic curvature. κ cancels →
**T_c = m_e0·√(3(L−1)/2π²), coupling-independent, ~electron-scale.** Leading-log is unreliable
here (μ~T_c → L−1→0 iterates unstably), so T_c is log-ambiguous ~40–450 keV, central ~70–160 keV —
**straddling the deuterium bottleneck (~70 keV).** Structural: onset and D/H are both
electron-scale → "derived" and "marginal" are one fact. Resolver: RG-improved V_eff + BBN
network (the working docket).
Caveat — T_c is marginal. The condensation temperature is electron-scale but genuinely
marginal: the perturbative (Coleman–Weinberg) treatment is scale-ambiguous, and a careful
analysis shows T_c is not perturbatively well-defined — the condensation is a strong-coupling
effect. Treated non-perturbatively (as a gap equation for a composite scalar), T_c *is*
well-defined and lands at the electron scale, but its precise value then rests on the medium's
strong binding, which the model does not yet supply from first principles. This is the same
marginality that limits the dark-energy value (see the cosmological-constant document).

Leptophilia (allowed ≠ generated). Ψ (lepton-sector Majoron) generates |Ψ|²q̄q only at ~2-loop
EW/EM ~(α/4π)² ~ 3×10⁻⁷ → quark fractional shift ~1×10⁻⁹ → effectively exact leptophilia.
Caveat: the Majoron forces the neutrino coupling (σNN), not the charged-lepton Yukawa — so the
scalar's leptophilia rests on a lepton-specific portal / the P-020 leptogenesis route, not bare
Majoron. Scripts (scratch-era, not retained): electron_cw_Tc.py, finite_T_Tc.py, leptophilia.py.

---

## The high-f operating point — the standing configuration's mechanism (2026-07-18)

The operator: m_e(φ) = m_e0(1 + κφ²), quadratic-canonical (dark-U(1) forbids the
linear coupling). At the standing decay constant f ≈ 3×10¹⁴ eV (window 10¹⁴–5×10¹⁴):
**κ = ε/f² = 1.4×10⁻³¹ eV⁻²**, and the frozen zero mode delivers the full amplitude exactly:
**ε = κ⟨φ⟩² = κf² = 1.2543%.**

The potential (two pieces, one new small input): V = V_L(φ) + V_CW(φ). The bare L-breaking
Mexican hat parks the VEV at f — its quartic is **λ_dyad = |m²_CW(0)|/2f² ≈ 1.3×10⁻³⁸**, a named
small input whose **radiative stability is verified**: the electron loop's own induced quartic
((6/16π²)κ²m_e0⁴(L−1)) is only 1–4% of λ_dyad across the L-band, so loop corrections do not
destabilize the input — it is technically natural. A derivation of its *value* belongs to the
L-breaking sector's own dynamics (corner-dependent); until built, this is an input with its
naturalness statement, not a hidden fit. The electron loop supplies
the small tilt that does the *timing*:

| quantity | value at f = 3×10¹⁴ eV | note |
|---|---|---|
| CW-induced mass — √[(κ/2π²)m_e0⁴(L−1)] | 3.1–6.9×10⁻⁵ eV (L−1 = 2–10) | **coincides with the constraint-window mass 2.8×10⁻⁵ eV — the allowed line is the CW locus**, an unarranged consistency |
| restoration temperature T_c = m_e0·√(3(L−1)/2π²) | **κ-independent** (κ cancels between the vacuum and thermal terms) | the ramp's T_γ-keyed timing survives at any f; value log-ambiguous [40, 900] keV. **The BBN-stability fence, stated on the derived anchor T_c = 177.10 keV, is [70, 500] keV** — bounded below by the deuterium bottleneck (~70 keV, beneath which the ramp's stamp at the bottleneck is zero and the sector stops witnessing the transition) and above by the weak-rate window (~500 keV, above which the electron-coupled scalar reaches n/p freeze-out and helium moves). 177.10 keV is interior on both sides, 2.5× and 2.8×. **The fence's conclusion is insensitive to where inside it T_c sits: the whole-range swing is at most 0.32σ on D/H** (2-term width; 0.27σ on the 3-term), against a row whose code systematic alone spans ~1.1σ — the kernel's own 1.1% move costs 0.0022σ, one part in 449. The RG-resummation docket retains the re-pin; the fence no longer waits on it |
| roll time 1/m_φ | 2.4×10⁻¹¹ s | the ramp is dynamically unimpeded (instant vs BBN minutes) |
| thermal fluctuation term κ⟨δφ²⟩_T at n/p freeze-out | ~5.7×10⁻²¹ | **2×10¹⁸ below ε** — the off-window is honest at high f |
| thermalization channels | Γ ∝ κ², all gates clear by 10⁸–10⁹ | ε rides first order in κ (the zero mode); the two orders are the configuration's whole point |

The sequence: above T_c the electron-plasma thermal mass holds the symmetric point (ε off —
including through n/p freeze-out); at T_c the tilt flips tachyonic and the field rolls to the bare
minimum at f (fast); ε ramps in with the order parameter and sits at 1.2543% thereafter, gated off
only inside high-Weyl structure (below). The ramp, computed with the exact thermal kernel:
ε(T)/ε₀ = 1 − [T³|J_F′(m_e/T)|] / [T_c³|J_F′(m_e/T_c)|] — half amplitude at T ≈ 152 keV
(0.86 T_c), 90% by T ≈ 113 keV (0.64 T_c), full below ~100 keV. The transition is second order
(a quadratic thermal correction on a quartic potential), so the order-parameter birth is
continuous — what the depth law requires, and what the BBN engine codes. The named fork
inherited from the un-merger: whether f = v_L (one L-breaking scale — the seesaw scan re-runs at
~100 TeV, where y ≈ 1.6×10⁻⁵ is natural and the Majoron–ν channel is safer) or f ≠ v_L (two
scales; the spec stays agnostic). This section is spec-grade: every number above is closed-form
from (ε, f, m_e, L−1); the open items are λ_dyad's origin, the T_c re-pin, and the v_L fork.

## The gate — the variable derived, the form graded (2026-07-18)

Why the gate reads Weyl curvature and not density — structural, from the census's own coupling
form. The census-legal coupling is a universal **conformal (metric) rescaling**: the
electron-coupled scalar enters through Ω²(φ)·g_μν. A conformally-coupled channel responds to the
metric's **conformal class only** — and the local, covariant measure of departure from conformal
flatness is precisely the Weyl tensor. FRW is conformally flat (C ≡ 0): the channel is fully open
in the homogeneous cosmos — which is exactly where the model operates (the ε-ramp, recombination,
the dark ages). Inside formed structure C² ≠ 0 obstructs the conformal channel. **So the gate
variable is C² by the coupling's own geometry — a conformal portal cannot key on density, and no
chameleon-class density gate is available to it even in principle.** *(This is also why the
laboratory checklist clears the vacuum-chamber trap: curvature penetrates chambers.)*

The two recorded rooms — the exponential f = exp(−C²/C_ref²) (reading B) and the power form
1/(1 + (C/C_ref)^p) (the candle-room module, p = 4) — with **every current use robust to the
choice**: at the ~24 orders above the edge that any terrestrial environment sits, both are zero
for every purpose on the record. C_ref is **event-set, not tuned** (the first
shell-crossing/vortex — §3 above; this addendum inherits that).

The obstruction functional — the form derived at class level; the two rooms reconciled. The
gate's microphysics is an **event** (§1/§3: the transition fires at the first
shell-crossing/vortex; C_ref is event-set). A suppression that fires at a first event is a
**survival probability**, and survival is theorem-shaped: S = exp[−N̄(C²)], with N̄ the expected
count of decoherence seeds inside the portal's coherence volume at Weyl level C²
(weakest-link/first-passage structure — the form class is not a fit choice). The two rooms then
read as two claims about the hazard N̄:

- exp[−(C²/C_ref²)^n] ⟺ N̄ = (C²/C_ref²)^n — **polynomial seed growth**: what any local,
  extensive, monotone seeding mechanism produces (phase-space volume above threshold). This is
  the mechanism's class.
- 1/(1 + (C/C_ref)^p) ⟺ N̄ = ln[1 + (C/C_ref)^p] — the seed count would have to grow only
  **logarithmically** in the load at large C², a log-slope collapsing as 1/ln C². No local
  seeding does that. The candle-room form is a numerical stand-in, not a mechanism — **retired
  as a candidate for the functional** (harmless in every deployed use: all bounds were taken in
  the deep-suppression regime, where both forms are zero).

The forced sharpness is produced, not imposed: if the seeds are threshold crossings of the
medium's Gaussian-statistics fluctuations with an amplitude-linear threshold map, the effective
exponent in the transition zone is n_eff ≈ ν²/2 (ν = the seed threshold in σ units). The exact
slope is closed-form, not an approximation — with φ the standard-normal density and Q its upper
tail,

> **n_eff(ν) = ½·ν·φ(ν)/Q(ν)**, running slightly steeper than ν²/2: ν = 2.2 gives 2.81, ν = 3
> gives 4.92, and §3's forced **n > 2.43 is met for ν > 2.027**.

So the gate is a hard step **whenever σ < 0.493·δ_c** — whenever the medium is in its linear
regime at the threshold scale. **The seed-count exponent — the sharpness is unconditional**, and
no seed identity is required to say so: any medium fluctuating well below its own crossing
threshold gives a step, and the bound fails only for a medium fluctuating at order the threshold
itself, already nonlinear everywhere, which the model's structure excludes.

The C²-to-threshold map, reduced to one number. The exponent's *value* is what the sharpness
argument leaves open, and the reduction is sharper than "needs a map". The recorded hazard carries
its own normalization — N̄ = (C²/C_ref²)ⁿ means **N̄(C_ref) = 1** — while the seed statistics give
N̄ = N_cell·Q(ν), with N_cell the number of independent seed cells inside the portal's coherence
volume. The two together *fix* ν at the reference curvature instead of leaving it free:

> **Q(ν_ref) = 1/N_cell**, and **n = ½·ν_ref·φ(ν_ref)·N_cell**

(the amplitude-linear map is σ ∝ C, so ν ∝ 1/C and d ln ν/d ln C² = −½ — which is where both the
½ and the large-ν limit n → ν²/2 come from). Hence **n ≈ ln N_cell**, less an offset that grows
only logarithmically (1.2 at N_cell = 10, 2.1 at 10⁶, 3.0 at 10⁴⁰), and the whole map collapses
to a single number, the cell count **N_cell = (ξ_portal/ℓ_seed)³**. §3's forced n > 2.43 becomes
**N_cell > 46.9**, i.e. **ξ_portal/ℓ_seed > 3.61** — the bound fails only if the coherence volume
holds fewer than ~47 independent seed cells, fewer than a condensate can hold and still be one.
The logarithm is also why the exponent's exact value has never mattered downstream: a hundred
decades of cell count buy two decades of n.

The one owed object, named: ℓ_seed — the seed's own correlation length inside the portal's
coherence volume. Nothing else is owed, and in particular (σ, δ_c) is *not* a second independent
route to n: the normalization above already determines σ(C_ref) = δ_c/ν_ref from the cell count,
so an externally sourced σ over-determines the gate rather than evaluating it. Read that way the
winding field's own ceiling (σ ≈ 0.012 from the n_s subdominance condition, against a unit
threshold) would demand N_cell = 10¹⁵¹⁰, which overshoots even a Planck-seeded coherence volume
(10¹⁴⁶ cells at ξ = 398 AU) by some 1360 orders. That route is sound as the *bound* it was written
for — σ ≪ δ_c forces ν ≫ 1 forces a step — and is not available as a valuation. In summary: the gate
variable is derived-structural (conditional on the census coupling form); the gate form is
derived at class level (survival/exponential-power — the power form retired); the exponent is a
hard step unconditionally, its value reduced to the closed form n(N_cell) with ℓ_seed the single
owed number; C_ref is an input.

## The Θ-averaging is forced, and by how much (2026-07-29)

`scripts/theta_averaging_forced.py`, 10 controls including three anti-controls. This also **corrects a
figure recorded earlier the same day**, which quoted Θ's scatter as m_e's.

**What was already held.** Developed speckle sits at **⟨Θ⟩ = ½ exactly by the Beta(d/2, d/2) law**
(`PRTOE_me_trigger.md`), against Θ = 1.9×10⁻⁶ laminar. Re-derived here by integrating the density
rather than quoting moment formulae: mean ½ and **sd = 1/(2√(d+1))** at every d, hence exactly
**0.25 in three dimensions**. So ⟨Θ⟩ = ½ is a *distributional fact*, not something the model arranges,
and the 0.25 is that law's own spread.

> **⚠ Correction.** An entry recorded earlier today read *"pointwise Θ (sd = 0.25 in 3D) would scatter
> m_e by 25% within a single absorber."* That quotes **Θ's** scatter as **m_e's**. Θ is a 0-to-1
> coherence indicator and the shift it drives is ε·Θ, so a Θ scatter of 0.25 induces an m_e scatter of
> ε × 0.25 = **3.14×10⁻³ — 0.31% of m_e, not 25%.** Off by a factor 80. (It is 50% of the *mean shift*
> ε⟨Θ⟩, which is the nearest true statement to what was written, and still not it.)

**The averaging is nonetheless forced, and now by a number rather than a feel.**

| | scatter in δm_e/m_e |
|---|---|
| pointwise, one cell | 3.14×10⁻³ |
| averaged over N cells | 3.14×10⁻³/√N |
| at the recorded N = 10⁹ | **9.9×10⁻⁸** |

Astrophysical constraints on μ = m_p/m_e variation sit in the 10⁻⁵–10⁻⁷ range depending on the
system, so the pointwise value is excluded by four to five orders of magnitude and the averaged one is
not.

> **Run backwards, the cell count is not arbitrary.** Reaching 10⁻⁷ requires N > 9.83×10⁸, and the
> corpus records 10⁹ — a ratio of **1.017**. The recorded cell count is, to within 2%, exactly the
> number that brings speckle scatter under spectroscopic bounds. The anti-control confirms this is
> load-bearing: N = 1, 10², 10⁴ and 10⁶ all stay excluded, and only ~10⁹ clears.

**So the debt is better stated and smaller than it was.** Not *"why does the coupling average"* as an
open mechanism question — the observable **is** an average, because an absorption line forms across
the whole column and each cell contributes its own m_e. What the model owes is a **check**, not a
smoothing mechanism:

> The same cell-to-cell scatter that averages away in the line **centroid** does not average away in
> the line **width**. A 3.14×10⁻³ spread in m_e across cells implies an excess broadening, and whether
> that survives observed line widths is a real, external, falsifiable test the corpus has not run.

That is the honest next object for this docket — a residual that can be named, quantified, and handed
to data.

---

## The width check, run (2026-07-29) — and it retires the averaging argument

The check named immediately above has been carried out. `scripts/speckle_width_check.py`,
16 controls including four anti-controls, all passing.

**The centroid and the width are the same object seen twice, and they cannot be had separately.**
Averaging divides the centroid error by √N. It leaves the width untouched, because **N does not
appear in the width at all** — superposing more cells samples the distribution of per-cell shifts
better, it does not narrow it:

| | scales as |
|---|---|
| centroid error | w·ε·sd(Θ)/√N — **N helps** |
| line width | w·ε·sd(Θ) — **N is absent** |

Their ratio is √N. At the recorded N = 10⁹ that is a factor of **31 623**.

### The fork, and both horns close

| branch | centroid | width | verdict |
|---|---|---|---|
| Θ uniform at its mean ½ | coherent shift ε/2 = 6.27×10⁻³, **1.6×10⁴×** over the μ bound | none | **dead on the centroid** |
| Θ scattered per Beta(3/2,3/2) | averages to 9.9×10⁻⁸ as advertised | **1880 km/s** (sd); FWHM 4427 km/s | **dead on the width** |
| Θ laminar = 1.9×10⁻⁶ | 2.38×10⁻⁸ | 7.1×10⁻³ km/s | **passes both** |

For the scattered branch to fit inside even a 10 km/s allowance, sd(Θ) would have to be suppressed
**188×** below the Beta law (1880× at 1 km/s, 38× at 50 km/s). 21 cm absorption in damped systems is
narrow — of order 1–50 km/s as a class. No specific measured width is sourced in-corpus, so the
demand is quoted across the class rather than against one system.

> **The N = 10⁹ coincidence is a red herring.** It was recorded hours earlier that the cell count
> sits "within 2% of exactly the number that brings speckle scatter under spectroscopic bounds," and
> called load-bearing. The 2% reproduces here exactly (ratio 1.017) — and it tunes the **centroid**
> while the **width** fails by two orders of magnitude. **The averaging argument is retired as a route
> to compliance.** The anti-control is decisive: scanning N across 24 decades never brings the width
> under 50 km/s, because N is not in the expression.

**What survives is the branch that never needed the averaging.** Laminar Θ suppresses the mean and
the scatter by the same factor and clears both tests at once. Environmental screening was already
data-required from centroids alone; the width makes it required far more strongly, and **rules out
the developed-speckle alternative rather than merely disfavouring it.**

### A structural result worth keeping

The two observable classes of the radio-lattice construction respond to cell-to-cell scatter in
**opposite** directions:

- **Line rows** (21 cm hyperfine, recombination lines) are **broadened**, with no relief from N.
- **Reconstructed-column rows** (dispersion measure, rotation measure) are path integrals, so their
  scatter averages down exactly like a centroid and is **invisible** — 2.0×10⁻⁷ at N = 10⁹.

So scatter is maximally visible in precisely the rows that construction calls measurable, and
invisible in the three it demoted. That is a falsifiable statement about where to look.

---

## The width check corrected — the coupling is κ_Θ, not ε (2026-07-29, same day)

Everything above about the width used **ε·sd(Θ)** for the induced mass scatter. **Wrong.** The
coupling recorded in `docs/exploratory/PRTOE_me_trigger.md` §5 is

> m_e = m_bare(1 + κ_Θ·Θ),  **κ_Θ = −2ε/(1+ε) = −2.478%**

so the per-cell scatter is **|κ_Θ|·sd(Θ) = 6.19×10⁻³**, not 3.14×10⁻³. Every width figure above is
low by **2/(1+ε) = 1.975×**. The 21 cm broadening is **3714 km/s**, not 1880.

**And the endpoints are the reverse of what was assumed here.** Θ is multi-stream occupancy:

| | Θ | m_e |
|---|---|---|
| single-stream — voids, pre-collapse | **0** | **bare** (the full ε) |
| multi-stream — halos, folded filaments | **½** | **laboratory**, since 1 + κ_Θ/2 = 1/(1+ε) exactly |

That identity holds to machine precision because κ_Θ was defined to make it hold, and the corpus's
own residual-laminar slope, 0.384%·f, reproduces from the same κ_Θ — two independent confirmations.

### What this does to the argument

**The core claim survives untouched:** averaging divides a centroid error by √N and leaves a width
alone, because N is absent from the width. Correcting the coupling makes the tension *worse*, not
better.

**But it relocates it, and that matters more than the size.** Developed speckle lives in
**multi-stream** gas — halos and folded filaments — which is exactly where 21 cm and methanol
absorbers are observed. The broadening therefore lands on the very systems supplying the tightest
constraints, not on some unobserved diffuse phase.

**The escape is real and it is not the sightline.** Sightline averaging protects a centroid only.
What protects the width is averaging *within each absorbing atom's own sampling volume*: if that
volume spans many granules, every atom sees the same effective Θ and the line stays narrow. The
demand is **≳1.4×10⁵ granules per sampling volume** to fit inside 10 km/s (1.4×10⁷ for 1 km/s,
5.5×10³ for 50 km/s). That is a concrete constraint on the granule scale, and a **different** one
from the sightline cell count recorded earlier.

`scripts/theta_coupling_resolved.py`, 13 controls including two anti-controls. All pass.

---

## Claims ledger & discipline (2026-08-03) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Form m_e(x) = m_e^lab[1+ε S(x)]; ε = 1.2543% | **complete-conditional** | audience table; THE_AMPLITUDE | ε stack conditional |
| 2 | Environmental Θ / Weyl gate forced (conformal portal → C²) | **derived / forced** | §1–2 | — |
| 3 | Transition sharpness forced by MICROSCOPE + quasar | **derived** | audience table | Two-constraint |
| 4 | Weyl not Ricci (three independent reasons) | **derived** | audience table | — |
| 5 | High-f operator (dim-6 lepton) assumed, not symmetry-selected | **OPEN** / assumption | docket #125 | Data-narrowed |
| 6 | T_c = 177.10 keV derived (Koide τ); κ-independent formula | **derived-conditional** | audience table | Lattice crowns τ |
| 7 | Electron-loop onset / low-f config | **failed / retired** | Failures ledger | BBN-fatal |
| 8 | Θ-averaging / developed-speckle route | **retired**; laminar Θ survives | closing; theta_coupling_resolved | Width demand on granules |
| 9 | Conversion-channel linear perts | **implemented** when dcdf_conv_g>0 | CLASS; not this file | — |

**Non-claims:** not free per-window ε; retired electron-loop onset not current.

**Triage:** elevate-in-place. Physics ceiling: math form forced; operator/stack residual OPEN.
