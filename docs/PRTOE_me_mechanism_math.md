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
and `eps ~ 1.24%`. The CMB is imprinted at the bare value `m_e^lab*(1+eps)`;
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

## 2. The coupling [OPEN legality / FORCED form]

 L_int = -eps * S(x) * m_e^lab * (psi_e-bar psi_e)

This is a direct, dimension-5, Planck-suppressed moduli/dilaton-class
operator with S(x) the environmental modulator. Legality under the coupling
census: OPEN (narrow reading → legal; broad → forbidden). Form: FORCED
(geometry is 60 orders too weak, sec 32, so a direct
operator is unavoidable). [trigger-doc sec 23, 32, 34]

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

## 4. The amplitude [BOUNDED, coefficient OPEN]

Ceiling (sec 31): only the ELECTROMAGNETIC part of m_e can respond to an
EM-binding environment. Split:

 m_e = m_bare(Higgs-Yukawa, ~99%) + delta_m_EM(self-energy, ~1%)
 delta_m_EM/m_e = (3 α / 4pi) * ln(Λ²/m_e²) ~ 1-2% (O(α))

So eps ≤ (EM self-energy fraction) ~ 1-2%. The observed 1.24% sits AT the
ceiling. Size DERIVED; exact value needs Λ (cutoff, ~18 MeV -- not yet
motivated) and the modulation fraction. [sec 28, 31]

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

Only the direct coupling has S+V; its sole missing property is L, and
MICROSCOPE-safety within L is already delivered by the sec-27 sharp
screening. ⇒ the whole roof reduces to the census-scope question. [sec 34]

---

## 7. The EP escape (fifth-force gate) [RESOLUTION DIRECTION, computation OPEN]

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

OWED COMPUTATION (make-or-break):
 (i) eps = 1.24% at recombination (Theta~0, smooth), AND
 (ii) saturated-Theta screening: grad(φ) < MICROSCOPE at Earth AND
 clears the reopened chameleon/Casimir/EP bounds, AND
 (iii) virialization delivers freezing (Theta static by medium EOM), AND
 (iv) quasar delta_mu/μ ~ 0 (all virialized absorbers Theta-saturated).
Screening machinery is cousin to the abandoned v1-v3 sector → must earn
its place fresh (graveyard Rule 3), inherits nothing.

---

## 8. Observable signature [DERIVED, testable]

Under a single m_e amendment, ALL EM-binding observables shift in LOCKED
correlation (sec 29):

 binding energies (Rydberg ~ m_e): +1.24%
 atomic sizes (Bohr radius ~ 1/m_e): -1.24%
 transition frequencies: +1.24%
 21-cm hyperfine (~m_e²/m_p): ~+2.5%

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
 - census-scope legality (a/b) -- reproduce the census derivation [2,6]
 - exact amplitude coefficient (cutoff + modulation fraction) [4]
 - the EP-screening computation (grad φ < MICROSCOPE; chameleon bounds) [7]
 - virialization-delivers-freezing, from the medium's EOM [7]
 - the two-field sims (docketed): confirm S=(1+f_rot²)/2, ψ/χ layering [trigger-doc]

The empirical fit (m_e = 1.0124, fits the CMB) is UNTOUCHED by all of the
above -- this document concerns the MECHANISM's legality/derivation, not
the data.

## 10. The leptonic origin -- why m_e and not m_q [MECHANISM DERIVED, magnitude OPEN] (2026-07-09)

BBN (docketed) REQUIRES the coupling be leptonic: a universal mass shift is 12-16σ
dead via the D/H quark→pion→deuteron channel (dln(D/H)/dln m_q ~ 15 vs dln m_e ~ 0.5,
a 30x ratio). Why the coupling picks the electron:

NO-GO (it is not a symmetry): L-bar H e and Q-bar H d both need a gauge-SINGLET scalar;
a singlet couples to every Yukawa operator with INDEPENDENT coefficients → no gauge
symmetry forces leptonic. Froggatt-Nielsen also fails -- the light quarks (u,d) carry
FN charges comparable to the electron's, so a generic flavon shifts m_q and re-triggers
BBN. Leptophilia is neither a gauge nor a generic-flavor consequence.

MECHANISM (uses P-2026-012: DE floor scale = lightest m_ν, so the medium lives in the
lepton-mass sector). Neutrino mass rides the lepton DOUBLET L (Weinberg (LH)(LH)/Λ);
quarks have no such operator, so the medium has no reason to couple to Q. Minimal
coupling = a field-dependent kinetic renormalization of L:

 Z_L(Psi) = 1 + Psi/f_L [dim-5: (Psi/f_L) * L-bar iD-slash L]

Canonical normalization of L rescales every lepton coupling by Z_L^(-1/2):

 charged lepton (one L): m_e ∝ Z_L^(-1/2) ⇒ dm_e/m_e = -1/2 (dPsi/f_L)
 neutrino (two L's): m_ν ∝ Z_L^(-1) ⇒ dm_nu/m_ν = -(dPsi/f_L)

Consequences:
 - BBN-safe by DISCONNECTION (not a dodge): Psi couples to L only; the quark/pion/
 deuteron channel is simply not connected.
 - WHY THE ELECTRON: Z_L shifts all charged leptons equally (e,μ,τ); only electrons
 survive at recombination (μ,τ decayed) → the electron is the charged lepton
 PRESENT, not a chosen flavor. No flavon needed.
 - L1-CLEAN: the medium's SUBSTANCE (lepton-mass sector), not its gravitational
 INTERFACE (identity-blind coupling). Interface-vs-substance (laws doc) → no census
 violation. The "L1 wants universal" tension of the prior session is DISSOLVED.

LOCKED PREDICTION (of the kinetic-Z_L coupling specifically):
 dm_nu/m_ν = 2 * dm_e/m_e = 2.48% at recombination.
 The factor 2 is operator counting (two L's vs one), no free knob. It DISCRIMINATES
 mechanisms: a direct Yukawa (Psi/f) L-bar H e shifts m_e with NO neutrino link
 (ratio 0). CMB consequence of dm_nu ~ 1.5 meV on Σm_ν (~0.06x sensitivity) --
 safe, currently unfalsifiable, a consistency consequence not yet a handle.

MAGNITUDE + SELF-CONSISTENCY (computed 2026-07-09):
 (a) f_L is DERIVED, not free. From ρ_dm(rec)=Om*ρ_c*(1+z)³ and ρ~m² Psi²:
 Psi_rec = √(ρ)/m = 5.8×10¹⁸ eV (~6×10⁻¹⁰ Mpl); f_L = Psi_rec/(2*dm_e) = 2.3×10²⁰ eV
 = 2.3×10¹¹ GeV. An INTERMEDIATE / seesaw-adjacent scale, fixed by (abundance, mass,
 amplitude) -- it adds NO new free parameter. [CLOSED]
 (b) The coupling PROFILE is forced to be CONDENSATION-TRIGGERED, not smooth in Psi.
 A smooth linear Z_L=1+Psi/f_L gives dm_e ∝ Psi ∝ a⁻³/2, hence dm_e(z=2) ~ 1.8×10⁻⁶
 -- AT the quasar bound (|dm_e/m_e|<~1×10⁻⁶ at z~1-3). The model AVOIDS this with the
 z=50 STEP (dm_e=0 below z=50; the condensate/transition reading, see [28]). So the
 explicit coupling must switch AT condensation (a step in Z_L), which both matches
 the code and dodges quasars. This ties [10] to the [28] reconciliation. [RESOLVED
 to "condensation-step", not smooth.]
 (c) The loop, worked (2026-07-09). Minimal potential V(Psi)=ρ_inf + 1/2 m² Psi²
 (DM oscillation early, DE floor late). It CLOSES TO CONSISTENCY: the DM→DE
 transition lands at z~0.7 (1/2 m² Psi² = ρ_inf), the right epoch (observed
 ~0.3, same order) for the model's own m + abundance; and ρ_inf^(1/4)=2.3 meV =
 m_ν,light [P-2026-012]. BUT it bottoms out at the CC PROBLEM: why ρ_inf=(m_ν)⁴
 is P-2026-012's POSIT, not derived. So the docketed last residual is the cosmological-
 constant question -- no longer a PRTOE-specific gap, the universal one. [REDUCED to CC]
 (d) kinetic-Z_L vs direct-Yukawa: RESOLVED (2026-07-09). The medium lives in the lepton
 sector via NEUTRINO mass, which rides L (Weinberg, two L's) → the natural coupling
 is TO L = the kinetic Z_L. A Yukawa (Psi/f)L-bar H e touches the charged-lepton
 Yukawa only, no route to m_ν = unmotivated. So the neutrino-sector home SELECTS
 kinetic → dm_nu = 2 dm_e is the LOCKED prediction, not one of two options. [CLOSED]

CAVEAT (2026-07-10) -- the deeper gap this section does NOT close. "The
medium is made of the neutrino sector" strictly implies a coupling to the WEINBERG operator
(→ dm_nu only). Reaching dm_e requires coupling to L's KINETIC term (Z_L), which is an
ADDITIONAL step beyond "makes neutrino mass" -- and THAT step is the leptophilia postulate
itself (dm_e is the charged-lepton Higgs-Yukawa L-bar H e = quark-structured, a no-go).
So the census refinement "couple to what you're made of" (laws doc, 2026-07-10) RENAMES the
leptophilia gap "substance" but does not close it: it legalizes a dm_nu coupling; the dyad
is dm_e. The un-derived core is precisely "why couple to L's kinetic term (reaching dm_e)
rather than only the Weinberg operator (reaching only dm_nu)." The mechanism here is a
coherent, motivated SKETCH; the explicit dm_e coupling from a neutrino-sector medium stays
[OBJECT-PENDING], prior unfavorable. The assessment did not move.

LEDGER UPDATE to Section 9: the EP-screening computation [7] is now RESOLVED (2026-07-09):
the composition-dependent Vainshtein-screened Delta_a/a = 8×10⁻²¹..8e-19, 3-5 orders below
MICROSCOPE (screened regime, cubic galileon); EP gate CLEARS, favorable-prior, sole
caveat a non-standard eps_V^(1/2) power (numerical galileon solve would fully discharge).
So varying-m_e is single-gated on DESI. And the leptonic-origin MECHANISM (this section)
moves item [2]'s "census-scope legality" from OPEN toward RESOLVED via interface/substance
-- the coupling is legal as substance; magnitude (a,b) remains the open frontier.

---

## ELECTRON-CW DYAD ONSET + FINITE-T (2026-07-10, gate-0 session)

On the charge-free dyad field (field 2, two-field split), the electron Coleman-Weinberg backreaction
sets the dyad's condensation scale — the onset becomes DERIVED, not a free input.

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
Majoron. Scripts: electron_cw_Tc.py, finite_T_Tc.py, leptophilia.py.

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
| restoration temperature T_c = m_e0·√(3(L−1)/2π²) | **κ-independent** (κ cancels between the vacuum and thermal terms) | the ramp's T_γ-keyed timing survives at any f; value log-ambiguous [40, 900] keV, BBN-stability fence [179, 369], the RG-resummation docket owns the re-pin |
| roll time 1/m_φ | 2.4×10⁻¹¹ s | the ramp is dynamically unimpeded (instant vs BBN minutes) |
| thermal fluctuation term κ⟨δφ²⟩_T at n/p freeze-out | ~5.7×10⁻²¹ | **2×10¹⁸ below ε** — the OFF-window is honest at high f |
| thermalization channels | Γ ∝ κ², all gates clear by 10⁸–10⁹ | ε rides first order in κ (the zero mode); the two orders are the configuration's whole point |

**The sequence:** above T_c the electron-plasma thermal mass holds the symmetric point (ε OFF —
including through n/p freeze-out); at T_c the tilt flips tachyonic and the field rolls to the bare
minimum at f (fast); ε ramps in with the order parameter and sits at 1.2543% thereafter, gated off
only inside high-Weyl structure (below). **The named fork inherited from the un-merger:** whether
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
exponent in the transition zone is n_eff ≈ ν²/2 (ν = the seed threshold in σ units; the exact
erfc slope runs slightly steeper: ν = 2.2σ gives 2.81, ν = 3σ gives 4.92) — so **ν ≳ 2.1σ
delivers n_eff > 2.43**, meeting §3's MICROSCOPE/quasar-forced bound from the event statistics
alone, for any but sub-2σ seeding. **The seed-count exponent, bounded (conditional
on seed identity):** if the decoherence seeds are the winding field's own fluctuations, the
n_s-subdominance ceiling (Δ² ≲ 2.3×10⁻⁶ per log, ~62 logs) pins the field's total σ ≈ 0.012 —
so any O(0.1–1) shell-crossing threshold sits at ν ≈ 8–84σ, giving **n_eff ≈ ν²/2 ≈ 35–3500**:
the gate is a hard step for every practical purpose, and §3's forced n > 2.43 is over-satisfied
by 1–3 orders. The bound closes the exponent at conditional grade; an unconditional value needs
the C²-to-threshold map. Grade: **gate variable derived-structural (conditional on the census
coupling form); gate form derived at class level (survival/exponential-power — the power form
retired); the exponent bounded hard-step (conditional on winding-seed identity); C_ref
input.**
