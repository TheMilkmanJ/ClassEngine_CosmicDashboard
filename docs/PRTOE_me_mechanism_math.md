# The m_e Mechanism: Consolidated Mathematical Formulation

> *Some statuses in this file may be superseded by later work; the current conditionality of every claim is tracked in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Assembled 2026-07-07. This is the EQUATIONS-ONLY companion to
`PRTOE_me_trigger.md` (which holds the reasoning and the dead ends).
Every result here is cross-referenced to its trigger-doc
section. Status tags: [DERIVED] solid, [BOUNDED] size/ceiling fixed but not
exact, [OPEN] owed, [FORCED] required by multiple independent constraints.*

---

## 0. The claim, in one line

The electron mass carries a fractional environmental shift
`m_e(x) = m_e^lab * [1 + eps * S(x)]`, where `S(x)` is a sharp/binary
"smoothness" indicator (1 in unstructured space, 0 in virialized structure)
and `eps = 1.2543%`. The CMB is imprinted at the bare value `m_e^lab*(1+eps)`;
all present-day (virialized) measurements see `m_e^lab`.

---

## 1. The environmental variable [DERIVED]

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
IDENTICALLY ZERO in conformally-flat FRW and nonzero only where tidal
structure exists:

 S(x) = f(C²(x) / C_ref² ), f = a near-step (saturating) function

---

## 2. The coupling [LEGAL under the coupling law / FORCED form]

 L_int = -eps * S(x) * m_e^lab * (psi_e-bar psi_e)

This is a direct, dimension-5 operator with S(x) the environmental modulator.
**Legality: CLOSED — the operator is legal under the model's coupling law,**
by the constitution's own consolidated clause (laws_and_rules, the L1 block):
the medium couples to ordinary matter only through gravity, and the second
field may couple non-gravitationally WITHIN its own sector — the lepton-mass
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
 were exactly that crime); a coupling that follows the lepton charge is not
 one of them.
Prior verdicts stand with the clause (the birefringence null, gate-0, the
EP posture, BBN). Sec 7's screening computation is a separate item from the
legality question, and it is delivered on all four of its items there. Form: FORCED (geometry is 60 orders
too weak, sec 32, so a direct operator is unavoidable). [trigger-doc sec 23,
32, 34; laws_and_rules]

---

## 3. The functional form is FORCED SHARP [DERIVED / FORCED by 2 constraints]

Requirement A (MICROSCOPE, sec 26): the residual shift inside structure must
satisfy the Eotvos bound. Differential Ti/Pt sensitivity:

 d ln M_atom / d ln m_e = Z - E_bind/m_e, E_bind = 15.73 * Z^(7/3) eV
 (Ti: 2.517×10⁻⁴ ; Pt: 2.171×10⁻⁴ ; differential: 3.46×10⁻⁵)
 ⇒ residual |δ m_e/m_e| at Earth < 8.7×10⁻¹¹

Requirement B (quasar, sec 7/12): a smooth density-dependence gives absorber
differentials 1×10⁴ over bound → binarity FORCED.

Consequence: a gentle exponential fails -- the curvature gap between
recombination and dwarf cores is only ~22x (1.35 decades) but the required
suppression is 8.2 decades. Minimum power:

 S(x) = exp[ -(C²/C_ref²)^n ], n > 2.43 [FORCED, sec 27]

i.e. a near-threshold/step. Both independent constraints force the same
sharpness → two-constraint pillar. Once suppressed at the dwarf core,
Earth (17 decades higher C²) is automatically suppressed. [sec 26, 27]

C_ref is NOT a free scale: the transition is set by a topological event
(first shell-crossing / first vortex), not a tuned curvature value. [sec 27]

---

## 4. The amplitude [BOUNDED here; the coefficient is derived by the standing stack]

Ceiling (sec 31): only the ELECTROMAGNETIC part of m_e can respond to an
EM-binding environment. Split:

 m_e = m_bare(Higgs-Yukawa, ~99%) + delta_m_EM(self-energy, ~1%)
 delta_m_EM/m_e = (3 α / 4pi) * ln(Λ²/m_e²) ~ 1-2% (O(α))

So eps ≤ (EM self-energy fraction) ~ 1-2%. The standing 1.2543% sits AT the
ceiling. Size DERIVED here as a bound; the exact value comes from the standing
stack eps = c*fbar*alpha_c = 27*alpha/(5*pi), which uses no cutoff at all --
this section's Lambda-and-modulation route is superseded by it. [sec 28, 31]

Why m_e and not α: varying-α killed by quasars (45-100x); m_e evades
those bounds -- the surviving EM-binding knob, selected by data. [sec 7, 29]

---

## 5. Which curvature piece, and why [DERIVED, 3 independent reasons]

The trigger couples to WEYL (tidal/radiative), not RICCI (local/binding):
 R1. Ricci fails directionally -- large at BOTH high-z background AND in
 halos, cannot distinguish smooth-dense from clumped. [sec 25]
 R2. Weyl = 0 identically in smooth FRW (conformal flatness) -- exactly the
 "bare in smooth space" requirement. [sec 23]
 R3. The switch fires on a DECOHERENCE event; decoherence is driven by a
 force's RADIATIVE/far piece; Weyl IS gravity's radiative piece; Ricci
 (binding piece) cannot trigger a decoherence event. [sec 30]

Near/far force split (general): every long-range force = near piece (binds)
+ far/radiative piece (carries info away = decoheres). EM: Coulomb binds,
photons decohere. Gravity: Ricci binds, Weyl decoheres. [sec 30]

---

## 6. The amplitude-channel constraint (why the roof is one question) [DERIVED]

A viable channel must be simultaneously STRONG [S] (O(α), not curvature-
suppressed), LEGAL [L] (census + MICROSCOPE), VARYING [V] (smooth vs
structured). Scored:

 curvature : L,V not S (60 orders weak, R/m_e²~1×10⁻⁶⁹)
 direct coupling : S,V not L (census scope, OPEN)
 khronon/frame : S,L not V (spatially uniform)
 intrinsic dm_EM : S,L not V (present everywhere equally)

Only the direct coupling has S+V — and its L is now delivered: the coupling
law's consolidated clause legalizes sector-internal coupling (sec 2), and
MICROSCOPE-safety within L is delivered by the sec-27 sharp screening.
⇒ the roof is CLOSED; the channel constraint is satisfied on all three
properties. [sec 34; laws_and_rules]

---

## 7. The EP escape (fifth-force gate) [RESOLVED — all four deliveries below]

Smooth dilaton: needs β~0.012, MICROSCOPE allows β<~1×10⁻⁴ → 2 orders
over → DEAD.

Escape: the field is the SHARP/SATURATED Theta (sec 27 sharpness), not a
smooth dilaton. Inside the virialized MW halo Theta is at its ceiling →
grad(Theta) ~ 0 (flat top) → grad(φ) exponentially suppressed → no
fifth force. Chameleon-class screening; screening agent = Theta saturation
(forced, not tuned). Freezing agent = VIRIALIZATION (medium's own dynamics,
static in a virialized halo).

Screening-test corroboration (sec 37, computed): atomic clocks are a GENUINE
third independent leg -- they kill the continuous version via temporal physics
(a continuous 1% coupling gives ~1×10⁻⁴ clock modulation, ruled out), while the
saturated form predicts a null (observed). Caveat: clocks force the screening-
CONSEQUENCE, not the sharp-form-CAUSE uniquely. White-dwarf spectroscopy =
consistency-check (saturated → lab value, confirmed ~1×10⁻⁵). Continuous version
now killed by TWO independent experiments (quasar spatial + clocks temporal).

THE FOUR DELIVERIES (the make-or-break computation, paid under the
survival-form gate — S = exp[−(C²/C_ref²)^n_eff], n_eff ≥ 35, threshold
event-set):
 (i) DELIVERED — recombination sits ≥22× below the threshold scale in C²,
 so 1 − S = (1/22)^35 ≈ 10⁻⁴⁷: the bare value rides to ~47 decimal places
 (the amplitude itself is the high-f operating point's own record).
 (ii) DELIVERED — the laboratory checklist: every terrestrial environment
 sits ~25 orders above the structure-class edge (curvature penetrates
 vacuum chambers, so the chameleon-trap tests do not apply); MICROSCOPE is
 out of range by kinematics; the mm–cm band is torsion-balance territory,
 already fenced.
 (iii) DELIVERED — freezing is structural: the switch is a function of the
 local Weyl invariant, not a field with its own relaxation; virialized
 tidal fields evolve on Gyr timescales and the step is pinned at
 S = exp(−10^10)-class or deeper, so no fluctuation of any ordinary size
 moves it. No separate relaxation dynamics exists to fail.
 (iv) DELIVERED — molecular-hydrogen absorbers require dense shielded gas,
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

## 8. Observable signature [DERIVED, testable]

Under a single m_e amendment, ALL EM-binding observables shift in LOCKED
correlation (sec 29):

 binding energies (Rydberg ~ m_e): +1.2543%
 atomic sizes (Bohr radius ~ 1/m_e): −1.2543%
 transition frequencies: +1.2543%
 21-cm hyperfine (~m_e²/m_p): +2.51%

Discriminator: the dark-ages/cosmic-dawn 21-cm sky (unvirialized IGM,
Theta~1, BARE value) vs the standard (virialized) sky. A specific
CORRELATED pattern across all EM-binding observables, not a single-line
shift. [sec 8, 29] REACH/SKA-low class instruments.

FORECAST NUMBERS (chain-free, from dln nu_hf/dln m_e = 2 and eps = 1.2543%):
 the bare-value hyperfine frequency runs +2.509% high in unvirialized gas.
 - THE CLEAN CHANNEL — the dark-ages absorption trough (z ~ 85-90, linear
   physics only, no stars): standard 15.8-16.5 MHz -> model 16.2-16.9 MHz,
   a +0.40 MHz offset that CANNOT be absorbed into astrophysics. Instrument
   class: lunar farside (LuSEE-Night / FarView). This is the mechanism's
   sharpest astrophysics-free falsifier outside the CMB.
 - the cosmic-dawn trough (EDGES band): 78.0 -> 79.96 MHz (+1.96 MHz) —
   degenerate with star-formation timing; consistency channel only, stated
   as such.

---

## 9. What is DERIVED vs OPEN (honest accounting)

DERIVED / FORCED:
 - the environmental variable (Theta, vorticity-based, exact identity) [1]
 - the coupling FORM is forced (geometry 60 orders too weak) [2]
 - the transition is FORCED sharp by 2 independent constraints [3]
 - Weyl not Ricci, 3 independent reasons [5]
 - the amplitude SIZE/CEILING (EM self-energy fraction, ~1-2%) [4]
 - the roof reduces to ONE question (census scope) [6]
 - the locked-correlation observable signature [8]

OPEN:
 (census-scope legality: CLOSED — the coupling law's consolidated clause; sec 2, 6)
 (the amplitude coefficient: DERIVED by the standing stack 27*alpha/(5*pi), no cutoff [4])
 (the sec-7 screening computation: DELIVERED — all four items, see sec 7)
 - the two-field sims (sim-gated): confirm S=(1+f_rot²)/2, ψ/χ layering [trigger-doc]

The empirical fit (m_e = 1.012543, fits the CMB) is UNTOUCHED by all of the
above -- this document concerns the MECHANISM's legality/derivation, not
the data.

## 10. The leptonic origin -- why m_e and not m_q [DATA-NARROWED, the operator ASSUMED] (2026-07-09)

BBN (the data ruling — the windowed program) REQUIRES the coupling be leptonic: a universal mass shift is 12-16σ
dead via the D/H quark→pion→deuteron channel (dln(D/H)/dln m_q ~ 15 vs dln m_e ~ 0.5,
a 30x ratio). Why the coupling picks the electron:

NO-GO (it is not a symmetry): L-bar H e and Q-bar H d both need a gauge-SINGLET scalar;
a singlet couples to every Yukawa operator with INDEPENDENT coefficients → no gauge
symmetry forces leptonic. Froggatt-Nielsen also fails -- the light quarks (u,d) carry
FN charges comparable to the electron's, so a generic flavon shifts m_q and re-triggers
BBN. Leptophilia is neither a gauge nor a generic-flavor consequence.

WHAT IS ACTUALLY ON OFFER (the operator roster, #125). The portal must be **even** in the
dyad field, so what multiplies a Standard-Model operator is the dimension-2 singlet |Ψ|².
Three couplings are available, ordered by dimension:

 |Ψ|² H†H [dim 4, renormalizable] → shifts the Higgs vev → EVERY mass, quarks included
 |Ψ|² L̄He [dim 6, → m_e ψ̄ψ after EWSB] → δm_e alone — THE STANDING CHOICE
 |Ψ|² (LH)(LH) [dim 7] → δm_ν alone; cannot reach δm_e at any coefficient

The renormalizable one is the one the model must do without: a universal shift at ε is
+12–18σ on D/H, which bounds λ_p ≲ 5×10⁻¹¹…1×10⁻⁹ across f = 100–500 TeV. **That exclusion
is affordable and the statement is computed**: the standing dim-6 lepton operator feeds
H†H back through one electron loop at λ_p ≤ ε·y_e² ≈ 1.1×10⁻¹³ (Λ_UV = 4πf; 6.8×10⁻¹⁶ at
Λ_UV = f) — from ~500× under the bound at its tightest corner to ~10⁶× under at the loosest —
so the induced universal shift reaches at
most 2×10⁻³σ on D/H. No tuning is spent inside the effective theory; what is assumed is
that the completion above f writes the lepton operator and not the other two.

WHY THE ELECTRON, and it survives the roster change: the operator shifts all charged
leptons equally (e, μ, τ); only electrons are present at recombination (μ, τ decayed), so
the electron is the charged lepton PRESENT, not a chosen flavour. No flavon needed.

THE FINER FORK — one coefficient or two. Writing |Ψ|² into the lepton DOUBLET's
normalization rather than into each mass operator separately correlates them: the charged
mass carries one power of L and the Weinberg operator two, so

 δm_ν/m_ν = 2 · δm_e/m_e = 2.51% inside the window

with the factor 2 pure operator counting. Independent coefficients leave δm_ν free instead.
**Nothing selects between them and nothing can**: the correlated point moves Σm_ν by 1.5 meV
inside a window whose exit restores the present-day value the sky measures — observationally
identical to the free case. The pipeline runs the correlated point (`background.c`, m_ν ∝ m_e²).
[ASSUMED — docket #125]
MAGNITUDE + SELF-CONSISTENCY (computed 2026-07-09, re-keyed to the standing operator):
 (a) The coupling PROFILE is forced to be CONDENSATION-TRIGGERED, not smooth in the field.
 A profile that tracks the field's own redshift gives dm_e(z=2) ~ 1.8×10⁻⁶ -- AT the
 quasar bound (|dm_e/m_e| <~ 1×10⁻⁶ at z~1-3). The model AVOIDS this with the z=50
 STEP (dm_e=0 below z=50; the condensate/transition reading, see [28]). So the shift
 must switch AT condensation and be gated thereafter, which both matches the code and
 dodges quasars. This ties [10] to the [28] reconciliation. [RESOLVED to
 "condensation-step", not smooth.]
 (b) The loop, worked (2026-07-09). Minimal potential V(Psi)=ρ_inf + 1/2 m² Psi²
 (DM oscillation early, DE floor late). It CLOSES TO CONSISTENCY: the DM→DE
 transition lands at z~0.7 (1/2 m² Psi² = ρ_inf), the right epoch (observed
 ~0.3, same order) for the model's own m + abundance; and ρ_inf^(1/4) = 2.25 meV =
 m_ν,light [P-2026-012]. BUT it bottoms out at the CC PROBLEM: why ρ_inf=(m_ν)⁴
 is P-2026-012's POSIT, not derived. So the last residual is the cosmological-
 constant question -- no longer a PRTOE-specific gap, the universal one. [REDUCED to CC]

WHAT THIS SECTION DOES NOT CLOSE, stated exactly. The delivering operator is not selected by
any symmetry the model carries: a gauge singlet couples to every Yukawa operator with an
INDEPENDENT coefficient, which is this section's own no-go read forwards. Data does the
excluding -- H†H and the quark bilinear at ε are both +12–18σ dead on D/H, and the Weinberg
operator reaches no charged mass at all -- so what remains standing is the lepton bilinear by
elimination, with the doublet-normalization correlation an assumption on top of it. That is
the honest grade: **the portal is data-narrowed and assumed, not derived**, and its one
discriminating observable is unreachable. Docket #125.

LEDGER UPDATE to Section 9: the EP-screening computation [7] is now RESOLVED (2026-07-09):
the composition-dependent Vainshtein-screened Delta_a/a = 8×10⁻²¹..8e-19, 3-5 orders below
MICROSCOPE (screened regime, cubic galileon); EP gate CLEARS, favorable-prior, sole
caveat a non-standard eps_V^(1/2) power (numerical galileon solve would fully discharge).
So varying-m_e is single-gated on DESI. And the leptonic-origin MECHANISM (this section)
moves item [2]'s "census-scope legality" from OPEN toward RESOLVED via interface/substance
-- the coupling is legal as substance. What stays open is not the legality but the *selection*:
which legal operator delivers δm_e, graded assumed above (#125), and the CC value the loop reduces to.

---

## THE ELECTRON-LOOP ONSET — the predecessor configuration [RETIRED]

> **This section describes the retired operating point**, in which the electron's
> Coleman–Weinberg backreaction drove the dyad's condensation. That configuration is
> BBN-fatal at its own numbers and no longer describes the model
> ([PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)); the standing configuration is the
> high-f operating point above. What survives from the work below is the κ-independent
> transition-temperature formula, which still supplies the ramp's timing. The rest is kept for
> the record and must not be cited as current.

On the charge-free dyad field, the electron Coleman–Weinberg backreaction was taken to set the
condensation scale, making the onset derived rather than a free input.

**Zero-T (the VEV / reduction).** m_e(φ)=m_e0(1+κφ²); the electron loop gives
V_CW(φ)=−(1/16π²)m_e(φ)⁴[ln(m_e(φ)²/μ²)−3/2], whose φ² term is a TACHYONIC induced mass
m_φ²(0)=−(κ/2π²)m_e0⁴(L−1) (radiative SSB). Self-consistent VEV
**v = m_e0·[ε(L−1)/4π²]^(1/6) ≈ 175 keV** (150/175/196 keV for L−1=2/5/10) — the CW minimum imposed
together with the delivered shift κv² = ε (full 1.2543%), which fixes κm_e0² = ε(m_e0/v)² ≈ 0.108;
robust under the 1/6-power. So the onset falls out of m_e0 + the dyad amplitude ALONE = a genuine
reduction (the onset is no longer free). Un-swamped because field 2 carries no charge → no TeV soft mass.

**Finite-T (the coin-flip).** Thermal mass Δm_φ²(T)=+(κm_e0²/3)T² (electron plasma, symmetry-
restoring); symmetry restored above T_c where it cancels the tachyonic curvature. κ CANCELS →
**T_c = m_e0·√(3(L−1)/2π²), coupling-independent, ~electron-scale.** Leading-log is UNRELIABLE
here (μ~T_c → L−1→0 iterates unstably), so T_c is log-ambiguous ~40–450 keV, central ~70–160 keV —
**STRADDLING the deuterium bottleneck (~70 keV).** Structural: onset AND D/H are both electron-scale
→ "derived" and "marginal" are one fact. Resolver: RG-improved V_eff + BBN network (the working docket).
**Caveat — T_c is marginal.** The condensation temperature is electron-scale but genuinely marginal:
the perturbative (Coleman–Weinberg) treatment is scale-ambiguous, and a careful analysis shows T_c is not
perturbatively well-defined — the condensation is a strong-coupling effect. Treated non-perturbatively
(as a gap equation for a composite dyad), T_c *is* well-defined and lands at the electron scale, but its
precise value then rests on the medium's strong binding, which the model does not yet supply from first
principles. This is the same marginality that limits the dark-energy value (see the cosmological-constant
document).

**Leptophilia (allowed ≠ generated).** Ψ (lepton-sector Majoron) generates |Ψ|²q̄q only at ~2-loop
EW/EM ~(α/4π)² ~ 3×10⁻⁷ → quark fractional shift ~1×10⁻⁹ → effectively exact leptophilia. CAVEAT
: the Majoron forces the NEUTRINO coupling (σNN), NOT the charged-lepton Yukawa — so
the dyad's leptophilia rests on a lepton-specific portal / the P-020 leptogenesis route, not bare
Majoron. Scripts (scratch-era, not retained): electron_cw_Tc.py, finite_T_Tc.py, leptophilia.py.

---

## THE HIGH-f OPERATING POINT — the standing configuration's mechanism (2026-07-18)

**The operator (unchanged):** m_e(φ) = m_e0(1 + κφ²), quadratic-canonical (dark-U(1) forbids the
linear coupling). At the standing decay constant f ≈ 3×10¹⁴ eV (window 10¹⁴–5×10¹⁴):
**κ = ε/f² = 1.4×10⁻³¹ eV⁻²**, and the frozen zero mode delivers the full amplitude exactly:
**ε = κ⟨φ⟩² = κf² = 1.2543%.**

**The potential (two pieces, one new small input):** V = V_L(φ) + V_CW(φ). The bare L-breaking
Mexican hat parks the VEV at f — its quartic is **λ_dyad = |m²_CW(0)|/2f² ≈ 1.3×10⁻³⁸**, a named
small input whose **radiative stability is verified**: the electron loop's own induced quartic
((6/16π²)κ²m_e0⁴(L−1)) is only 1–4% of λ_dyad across the L-band, so loop corrections do not
destabilize the input — it is technically natural. A derivation of its *value* belongs to the
L-breaking sector's own dynamics (corner-dependent); until built, this is an input with its
naturalness statement, not a hidden fit. (The predecessor configuration had no bare potential
and its VEV formula died with it.) The electron loop supplies
the small tilt that does the *timing*:

| quantity | value at f = 3×10¹⁴ eV | note |
|---|---|---|
| CW-induced mass — √[(κ/2π²)m_e0⁴(L−1)] | 3.1–6.9×10⁻⁵ eV (L−1 = 2–10) | **coincides with the constraint-window mass 2.8×10⁻⁵ eV — the allowed line IS the CW locus**, an unarranged consistency |
| restoration temperature T_c = m_e0·√(3(L−1)/2π²) | **κ-independent** (κ cancels between the vacuum and thermal terms) | the ramp's T_γ-keyed timing survives at any f; value log-ambiguous [40, 900] keV. **The BBN-stability fence, stated on the derived anchor T_c = 177.10 keV, is [70, 500] keV** — bounded below by the deuterium bottleneck (~70 keV, beneath which the ramp's stamp at the bottleneck is zero and the sector stops witnessing the transition) and above by the weak-rate window (~500 keV, above which the dyad reaches n/p freeze-out and helium moves). 177.10 keV is interior on both sides, 2.5× and 2.8×. **The fence's conclusion is insensitive to where inside it T_c sits: the whole-range swing is at most 0.32σ on D/H** (2-term width; 0.27σ on the 3-term), against a row whose code systematic alone spans ~1.1σ — the kernel's own 1.1% move costs 0.0022σ, one part in 449. The RG-resummation docket retains the re-pin; the fence no longer waits on it |
| roll time 1/m_φ | 2.4×10⁻¹¹ s | the ramp is dynamically unimpeded (instant vs BBN minutes) |
| thermal fluctuation term κ⟨δφ²⟩_T at n/p freeze-out | ~5.7×10⁻²¹ | **2×10¹⁸ below ε** — the OFF-window is honest at high f |
| thermalization channels | Γ ∝ κ², all gates clear by 10⁸–10⁹ | ε rides first order in κ (the zero mode); the two orders are the configuration's whole point |

**The sequence:** above T_c the electron-plasma thermal mass holds the symmetric point (ε OFF —
including through n/p freeze-out); at T_c the tilt flips tachyonic and the field rolls to the bare
minimum at f (fast); ε ramps in with the order parameter and sits at 1.2543% thereafter, gated off
only inside high-Weyl structure (below). **The ramp, computed with the exact thermal kernel:**
ε(T)/ε₀ = 1 − [T³|J_F′(m_e/T)|] / [T_c³|J_F′(m_e/T_c)|] — half amplitude at T ≈ 152 keV
(0.86 T_c), 90% by T ≈ 113 keV (0.64 T_c), full below ~100 keV. The transition is second order
(a quadratic thermal correction on a quartic potential), so the order-parameter birth is
continuous — what the depth law requires, and what the BBN engine codes. **The named fork inherited from the un-merger:** whether
f = v_L (one L-breaking scale — the seesaw scan re-runs at ~100 TeV, where y ≈ 1.6×10⁻⁵ is natural
and the Majoron–ν channel is safer) or f ≠ v_L (two scales; the spec stays agnostic). Grade of this
section: **spec** — every number above is closed-form from (ε, f, m_e, L−1); the open items are
λ_dyad's origin, the T_c re-pin, and the v_L fork.

## THE GATE — the variable derived, the form graded (2026-07-18)

**Why the gate reads Weyl curvature and not density — structural, from the census's own coupling
form.** The census-legal coupling is a universal **conformal (metric) rescaling**: the dyad enters
through Ω²(φ)·g_μν. A conformally-coupled channel responds to the metric's **conformal class
only** — and the local, covariant measure of departure from conformal flatness is precisely the
Weyl tensor. FRW is conformally flat (C ≡ 0): the channel is fully open in the homogeneous cosmos
— which is exactly where the model operates (the ε-ramp, recombination, the dark ages). Inside
formed structure C² ≠ 0 obstructs the conformal channel. **So the gate variable is C² by the
coupling's own geometry — a conformal portal cannot key on density, and no chameleon-class
density gate is available to it even in principle.** *(This is also why the laboratory checklist
clears the vacuum-chamber trap: curvature penetrates chambers.)*

**The two recorded rooms** — the exponential f = exp(−C²/C_ref²) (reading B) and the power form
1/(1 + (C/C_ref)^p) (the candle-room module, p = 4) — with **every current use robust to the
choice**: at the ~24 orders above the edge that any terrestrial environment sits, both are zero
for every purpose in the books. C_ref is **event-set, not tuned** (the first
shell-crossing/vortex — §3 above; this addendum inherits that).

**The obstruction functional — the form derived at class level; the two rooms reconciled.** The
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

**The forced sharpness is produced, not imposed:** if the seeds are threshold crossings of the
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

**The C²-to-threshold map, reduced to one number.** The exponent's *value* is what the sharpness
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

**The one owed object, named: ℓ_seed** — the seed's own correlation length inside the portal's
coherence volume. Nothing else is owed, and in particular (σ, δ_c) is *not* a second independent
route to n: the normalization above already determines σ(C_ref) = δ_c/ν_ref from the cell count,
so an externally sourced σ over-determines the gate rather than evaluating it. Read that way the
winding field's own ceiling (σ ≈ 0.012 from the n_s subdominance condition, against a unit
threshold) would demand N_cell = 10¹⁵¹⁰, which overshoots even a Planck-seeded coherence volume
(10¹⁴⁶ cells at ξ = 398 AU) by some 1360 orders. That route is sound as the *bound* it was written
for — σ ≪ δ_c forces ν ≫ 1 forces a step — and is not available as a valuation. Grade: **gate
variable derived-structural (conditional on the census coupling form); gate form derived at class
level (survival/exponential-power — the power form retired); the exponent hard-step
unconditionally, its value reduced to the closed form n(N_cell) with ℓ_seed the single owed
number; C_ref input.**
