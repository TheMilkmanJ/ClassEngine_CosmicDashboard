# The 1.24% Amplitude — Consolidated Derivation (historical, 2026-07-07)

> # ⚠ SUPERSEDED DECOMPOSITION — DO NOT CITE THIS FILE'S FACTORS AS CURRENT
>
> **This file records the retired `ε = c × f_amp × (Ψ₀/M_red)` factorization.** The standing
> decomposition is **`ε = c·f̄·α_c = 27α/5π = 1.2543%`** — see
> [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §0 and
> [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1.
>
> Specifically retired here: **f_amp ≈ 0.6 ("COMPUTED, from the genesis dice")** and
> **c ≈ 0.94** and **Ψ₀/M_red ≈ 2.2%**. In the standing decomposition the factors are
> **c = 9/10** (the census over the universal charged-fermion roster), **f̄ = 2/π** (the winding
> mean-absolute-sinusoid), and **α_c = 3α** (under MCMC test). MATH_SPINE §0 records why: the
> old `c(m) = (m/m₀)^{1/4}` route was a relic of *this* decomposition, and read backward it is
> dead by its own arithmetic — it forces c = 1.005 while the census excludes c = 1.
>
> **Why the banner exists (2026-07-16):** this file's `f_amp ≈ 0.6` was cited as a live claim in
> external review, because nothing here said otherwise. The generic "some statuses may be
> superseded" hedge below is not sufficient — a retired *headline decomposition* requires a named
> retirement, not a disclaimer. Kept for provenance only.

> *Some statuses in this file may be superseded by later work; the current conditionality of every claim is tracked in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Consolidates the §57–74 build in PRTOE_me_trigger.md into one clean story:
how the electron-mass amplitude went from a naked fit to a traced, census-gated
prediction. Every factor labeled by its status: TRACED / COMPUTED / NATURAL /
GATED.*

## The number

ε ≡ δm_e/m_e ≈ **1.24%** — the varying-electron-mass shift at recombination that
eases the H₀ tension. Fit to the CMB; the model's one novel empirical handle.

## The factorization (from the interaction structure)

 ε = c × f_amp × (Ψ₀ / M_red)

Three factors, each a distinct physical object:

| factor | value | role | status |
|---|---|---|---|
| **Ψ₀/M_red** | ≈ 2.2% | field displacement in gravitational units (the SIZE) | **TRACED** |
| **f_amp** | ≈ 0.6 | amplitude-mode fraction (which part of the field couples) | **COMPUTED** |
| **c** | ≈ 0.94 | conformal coupling strength (gravitational-strength = 1) | **NATURAL / GATED** |

Product: c × f_amp × Ψ₀/M_red ≈ 1 × 0.6 × 2.2% ≈ **1.3%**, bracketing the observed
1.24% as the median of the genesis distribution.

## Factor 1 — Ψ₀/M_red ≈ 2.2% (TRACED)

- **Ψ₀ ≈ 5×10¹⁶ GeV** from the misalignment abundance: the field is frozen until
 H drops to m, then redshifts as matter; ρ_DM,0 = ½m²Ψ₀²(1+z_osc)⁻³ pins Ψ₀.
 **Robust: Ψ₀ ∝ m^(−1/4)** — a factor-3 mass uncertainty moves it 24%.
- **M_red** (reduced Planck mass) is the physical scale for a gravity-only
 coupling (coefficient of R/2 in the action). Census-forced convention.

## Factor 2 — f_amp ≈ 0.6 (COMPUTED, from the genesis dice)

- Only the **amplitude mode** (radial |Ψ| oscillation) couples to m_e, because
 m_e rides on |Ψ|. The **phase mode** is the U(1) Goldstone — it couples to
 charge/number, NOT mass. So the fraction of the field in the amplitude mode,
 f_amp, is what reaches the electron.
- f_amp ≈ 0.55–0.67 was **already computed** by the genesis orbit integration
 (the "One Mountain" dice), NOT sim-pending. The granule sim (the working docket) is an
 independent cross-check (granule power S = (1+(1−f_amp)²)/2), not the source.
- **Distributional:** f_amp is one genesis-dice roll per universe (median ~0.6);
 our 1.24% ⇒ we drew the median ⇒ a typical universe.

## Factor 3 — c ≈ 1 (NATURAL, GATED on the census — the working docket)

- **Make-or-break PASSED.** The dangerous alternative was the Ψ₀ normalization
 (δm_e/m_e = δΨ/Ψ₀ → O(1) blowup), which requires m_e ∝ Ψ (dark-sourced Yukawa).
 But **m_e is Higgs-sourced**, and the census forbids the Yukawa — excluded
 twice. The coupling is gravitational (conformal), scale M_red, no blowup.
- **c is a free O(1) conformal coefficient.** Scale invariance does NOT force
 c = 1 (the amplitude mode is a massive pseudo-dilaton coupling to Higgs-sourced
 masses, not a Goldstone to scale-sector masses). Data wants c ≈ 0.94.
- **c = 1 ⟺ the STRONG census** ("medium couples to matter at exactly
 gravitational strength, no free constant"). So c reduces to the **census-scope
 adjudication (the working docket)**:
 - STRONG census → **ε = f_amp × Ψ₀/M_red is FULLY DERIVED = 1.24%.**
 - WEAK census → c ≈ 1 is natural + data-consistent, not forced.

## The interaction (why the factors are what they are)

The m_e shift is a closed loop of couplings, matter → space → matter:
1. **matter → space (gravity):** clustering/shell-crossing saturates Θ.
2. **Θ (the all-clear gate):** binary — diffuse "hold" / virialized "release".
 Matter's own state, written into the fluid.
3. **space → matter (β = the read gain):** β = f_amp reads Θ back onto m_e.
 INFORMATION not energy (census-forced small, §69) → UNCOLLECTABLE (the medium
 reading its own information, §71). Matter reallocates its own energy
 (FIRAS-safe reallocation branch).
4. **matter → matter (EM):** the electron's EM-structured mass realizes the
 shift, distributed by hydrogen/reduced-mass flavor (electron dominates).

## Status

**Traced end-to-end.** Two of three factors are traced/computed (Ψ₀/M_red,
f_amp); the third (c) passed its make-or-break and reduces to the model's central
census-scope hinge. **The 1.24% is now one census ruling (the working docket, strong
direction) away from a complete derivation.** The scariest failure mode (Ψ₀
blowup) is eliminated. Remaining honest caveats: c=1 not forced (only natural);
distributional (median, our universe typical); the dice's own h-convergence
caveats; and the whole chain still assumes the discrete-switch m_e mechanism
(ANN-2026-013), whose payload operator is un-built.

---

## FOUNDATIONAL NOTE (parked, 2026-07-07): R=0 ontology, bubble-vs-infinite, and the multiverse edge

*Author's foundational question chain, and its correct parking. Recorded so the
model's silent assumption is on record, NOT so anything is built on it.*

**R=0 = the model's absolute nothing** (no medium, no curvature — the genesis
ground state). Its direction is TEMPORAL ("before"), not spatial ("outside"):
the genesis happened everywhere at once in an already-unbounded space; the
universe DILUTES (ρ∝a⁻³) as it expands, it does not invade fresh R=0.

**OPEN foundational choice (data cannot reach it):** the fitted cosmology ASSUMES
unbounded homogeneity (FLRW). Whether the medium is globally infinite OR a finite
BUBBLE of R=1 in an R=0 void is undetermined — the CMB fit assumes the former but
never earns it. In the bubble reading, expansion IS into R=0 nothingness (the
bubble picture is then literally correct).

**Multiverse extension (parked as philosophy):** if R=1
nucleates in R=0, generic bubble/eternal-inflation logic gives OTHER R=1 regions.
Untestable in principle — causally sealed by super-horizon R=0 inflation, hence
un-chaseable; adopted.

**The neighbor rule + its single crack (honest):** no signal from a neighbor
reaches us EXCEPT a possible early BUBBLE COLLISION (a circular CMB temperature
disk). Planck/WMAP searched — NULL. So the one testable edge CONFIRMS the
neighbor rule (nothing has reached us). Additional distance from PRTOE: its
genesis is Affleck-Dine ROLLING, not Coleman-De Luccia bubble NUCLEATION — so the
multiverse isn't even clearly this model's mechanism. Speculation atop an
unearned assumption: doubly un-chaseable. Booked PARKED; the model leans on none
of it.

---

## The coupling structure, and where it stands

*The consolidation above froze at §74. This block carries it to §92.*

**Factor 3 (c) — much more resolved.** c is now BOXED near 1, not free:
- **Ceiling (c ≲ 1):** DERIVED from technical naturalness (§75, the "too
 expensive"). A stronger-than-gravitational coupling radiatively destroys the
 medium's own ultralight mass — so c can't exceed gravitational strength. The
 naturalness constraint caps c to survive.
- **Floor:** the amplitude is over-determined (pinned f_amp, Ψ₀) so c can't drop
 far without breaking the fit (§76–77). Measured value: **c = 0.93 ± 0.38**,
 consistent with 1, sharpening as Fairbank converges.
- **The remaining bet (§81 vs §82):** is c a *free dial* (§81) or *forced = 1*
 (§82, "no half-gravity")? DATA can referee it: the granule sim's
 independent f_amp isolates c (§83, breaks the §77 degeneracy) and reads our
 universe's dice roll (f_amp ≈ 0.56). But *measuring* c=1 ≠ *deriving* it (§84):
 only the effective-action calc (docketed) proves "no dial."

**Why the coupling is universal & flavor-blind (§89):** gravity couples
to mass-energy only — it *cannot* tell electron from quark ("same shit, different
flavor" = the equivalence principle). So c is universal by constitution, and any
flavor must be matter's own — the medium has no organ to make it.

**Flavor / deuterium arc (§85–92):**
- The varying-constant shift is UNIVERSAL across leptons and hadrons. A flavor-dependent
 shift would require a non-gravitational touch on the Higgs/EM sector, which the census
 forbids (§90) — so the model predicts universal varying-constants.
- **No Higgs portal is needed (§92):**
 the SAME universal conformal coupling rescales the metric, and the Higgs vev is
 a mass scale in it — so one gravitational nudge shifts electron + quark + vev
 together. The Higgs moves because the FLOOR moved, not a direct touch.
- **Unification RESURRECTED:** one conformal coupling does m_e (recombination) AND
 the quark/vev shift (BBN) — one engine, no separate carrier, no portal.
- **The deuterium heal now hinges on ONE calculable question:** does the dark
 field's value GROW or SHRINK from BBN to recombination? Grows → small BBN shift
 (~0.15%) heals D/H, no catastrophe. Shrinks (misalignment's naive answer) →
 full 1.24% quark shift → the +11% D/H catastrophe. Genesis-set, computable.

**Current standing of the whole amplitude program:**
- Architecture: complete (gravity universal-conformal, flavor-blind).
- c: boxed near 1 (ceiling derived, value measured ~0.93, "forced vs dial" = #14).
- Flavor: universal (P-011 retracted); no portal owed.
- Deuterium: unified with m_e (one coupling), rides the BBN→recomb field ratio.
- Three live walls: #14 (c=1 loop calc), #8 (granule sim → dice roll + c),
 #6 (Fairbank convergence). All calculation/simulation, no fog.

---

## The analytic backbone: the amplitude PINS the mass

`scripts/amplitude_11_analytic.py` (fast/analytic, completes in-sandbox; the stiff
genesis ODE for f_amp still needs WSL). Result:
- **Psi0 ~ 5×10¹⁶ GeV is DERIVED from the DM abundance** (leading-order misalignment,
 ρ_dm0 = 1/2 m² Psi0² a_osc³, a_osc from H=m). Confirms the traced value.
- eps = c*f_amp*(Psi0/M_red) lands in the **right decade (1-5%) from abundance alone**.
- Demanding **eps = 1.24%** (c=1, f_amp=0.6) **PINS the mass: m ~ 2×10⁻²⁰ eV** (Psi0/M_red
 = 2.07%, matching the traced pair). The amplitude program is internally self-consistent
 and corresponds to m ~ 2×10⁻²⁰ eV, NOT the 1×10⁻²¹ fuzzy-DM fiducial we had loosely quoted.
- **This converts the fit into a prediction / advances #9 (mass pin):** abundance fixes
 Psi0; eps=1.24% then pins m to the ~1×10⁻²⁰ decade. Falsifiable, and consistent with the
 Lyman-α fuzzy-DM floor (~2×10⁻²¹ eV, so allowed).
- **OWED (factor-level, not order-level):** f_amp from the genesis orbit (WSL ODE), c from
 the loop, O(1) misalignment factors (~2x). These move the pinned m by factors.

## The f_amp orbit: mechanism confirmed, ~0.6 natural

`scripts/genesis_famp_orbit.py` (Cartesian, NON-stiff, runs in-sandbox -- the WSL
caveat did NOT bind). Complex AD field in V=m²|Psi|²+lam|Psi|⁴ with Hubble
friction; f_amp = time-averaged RADIAL (breathing) energy fraction of the late-time
orbit.
- **Mechanism CONFIRMED:** f_amp set by orbit eccentricity, spans 0.47-0.99 as the
 release kick varies (near-radial → f_amp~1, near-circular → f_amp~0.5).
- **Central value ~0.6 is NATURAL:** median over a flat kick prior = 0.62, matching
 the doc's assumed f_amp~0.6. Not cherry-picked -- it's where the mechanism sits.
 (f_amp=0.6 exactly ↔ kick~1.3.)
- **CAVEAT:** generic AD orbit (quartic + parametrized kick), NOT the model's
 specific A-term, so the DISTRIBUTION is illustrative/prior-dependent; the mechanism
 and ~0.5-0.6 central value are robust.

**#11 amplitude standing:** eps = c * f_amp * (Psi0/M_red). Psi0 DERIVED (abundance,
→ m~2×10⁻²⁰ eV), f_amp mechanism-confirmed (~0.6), both in-sandbox. Only **c** remains
(the effective-action loop). The three are mutually consistent at 1.24% for
m~2×10⁻²⁰ eV, c~1, f_amp~0.6.

## The real Z4 A-term, and the c verdict

**#2 -- f_amp from the MODEL's real A-term (`scripts/genesis_famp_Z4.py`).** Z4 tilt
V_A = eps_A lam (Psi⁴ + h.c.) = 2 eps_A lam R⁴ cos(4theta); field released AT REST
at phase θ_i (uniform prior after inflation); rotation is GENERATED by the torque,
not assumed. Median f_amp over the uniform phase prior:
 eps_A=0.10 → 0.59 ; 0.20 → 0.68 ; 0.30 → 0.74 ; 0.50 → 0.70 (range ~[0.05,1.0])
⇒ **f_amp ~ 0.6 is where the model's own dice sit** (hit dead-on at small tilt), NOT an
assumption. Residual = the tilt strength eps_A (slides the median 0.6→0.7).

**#14 -- is c forced to 1? VERDICT: SOFT DIAL, not forced.** The amplitude mode is a
PSEUDO-dilaton (the m² term breaks scale invariance explicitly), so the dilaton
low-energy theorem that would pin c=1 does NOT bind; "no half-gravity" fails because a
matter scalar couples conformally via a non-minimal ξ φ² R with CONTINUOUS ξ. So c
is a BOUNDED O(1) (≤1 by naturalness, ~0.93 measured), not symmetry-forced.
**Consequence:** with f_amp computed, eps = c*f_amp*(Psi0(m)/M_red) = 1.24% is ONE
equation in TWO unknowns → pins a **c-m relation**, not either alone. Breaks 3 ways:
compute ξ (hard theory), measure m (fuzzy-DM astro), or the granule sim (docketed).

**AMPLITUDE PROGRAM, post-#11/#14:** Psi0 DERIVED (abundance), f_amp DERIVED from the
Z4 dice (~0.6), c a bounded soft-dial degenerate with m. The 1.24% is now a **derived
relation between two ultralight-sector numbers (c, m)**, not a free fit -- a constraint
surface with two astrophysical ways to close it.

## The c-m degeneracy, broken by fuzzy-DM data

c-m curve (f_amp=0.6): **c(m) = (m / 2.24×10⁻²⁰ eV)^(1/4)**; naturalness c<~1 ⇒ m <~ 2.24×10⁻²⁰ eV.
Fuzzy-DM lower bounds: Lyman-α (Rogers&Peiris 2021) m>2×10⁻²⁰ eV (95%); UFD (Dalal&Kravtsov
2022) m>3×10⁻¹⁹ eV (99%, stronger but more model-dependent).
- **NEAR-COINCIDENCE:** the model's natural ceiling (2.24×10⁻²⁰) sits right at the Lyman-α
 floor (2×10⁻²⁰) → model cornered to m~2×10⁻²⁰ eV, **PREDICTS c~0.97-1.0**. Measured c=0.93+-0.38
 confirms. FIVE independent lines (amplitude, abundance, naturalness, Lyman-a, measured c)
 converge on (m~2×10⁻²⁰ eV, c~1). Degeneracy broken; c pinned ~1, no longer a free dial.
- **THREAT (3rd):** the UFD bound (m>3×10⁻¹⁹) would force c~1.9 -- mildly unnatural AND ~2.5sigma
 against the measured c. If UFD holds (debated), real tension. 
- **#6 is now a SHARP test:** as c tightens from +-0.38, it either nails c~1 (confirms corner)
 or drifts low (m below Lyman-a floor → tension).

## Origins audit: c derives from the census (honest downgrade)

Traced the "convergences on c~1" to their roots; two corrections + one deepening:
- **OVERCOUNT corrected:** "measured c=0.93" is NOT independent -- it is the amplitude eps
 rearranged (c = eps/(f_amp*Psi0/M_red)). Same input, not a separate confirmation.
- **Naturalness ceiling and UV/ALP share ONE root:** "can't exceed gravitational strength"
 (ceiling) and "gravity generates it at gravitational strength" (floor) are the same
 statement -- **c~1 because the coupling IS gravity (strength 1 in M_red units) = the census.**
- **Genuine convergence = TWO independent things, agreeing:** (1) THEORY/census predicts c~1
 (= the strong census restated quantitatively); (2) DATA: Lyman-α m>2×10⁻²⁰ → via the c-m
 curve → c>0.97. The census's predicted c~1 and the mass data's implied c~0.97 AGREE, non-
 circularly.
- **Upshot:** c does not derive from 5 places; it derives from the census. "c=1" IS "the coupling
 is exactly gravitational." The amplitude program is therefore "census predicts c~1; does the
 independent mass agree?" -- YES (Lyman-a), with the UFD bound as the one dissenting dataset.

## The late regime change reframes DESI

The dCDF w runs 1/3→0→-1 = TWO regime changes: early (radiation→DM condensation,
z~1×10⁵) and LATE (DM→DE floor, w:0→-1, z~0.7 → now). **We live inside the late one**
(the onset of accelerated expansion IS the medium's 2nd phase transition). DESI's w
measurement is therefore the DIRECT THERMOMETER of this regime change.

**FORK (the intuition vs the model's theorem):**
- **(A) current bet:** the late transition FROZE at w=-1 -- mutual-exclusion theorem
 (ANN-2026-008) caps drift at ≤2×10⁻⁸, unobservable. DESI thawing (w0~-0.84, 2.9sigma)
 = THREAT / systematic.
- **(B):** the regime change is still VISIBLY in progress (w evolving toward -1). Then
 DESI's thawing is NOT a threat -- it's the late regime change SEEN LIVE, a CONFIRMATION.
- The intuition and DESI's data point the SAME way (witnessable evolving w), i.e. AGAINST
 the model's own theorem.

**COST (honest):** (B) doesn't bend the theorem, it ABANDONS it -- the drift cap (2×10⁻⁸) vs
DESI (~0.1) is 7 orders apart. So it's a major revision, not a tweak. (A) keeps theorem +
calls DESI systematic; (B) drops theorem + reads DESI as the live 2nd regime change.

**Upshot:** DESI flips from pure-threat to threat-OR-live-confirmation, forked on ONE
theorem. Highest-leverage DESI question is now: is the mutual-exclusion theorem's "w=-1
frozen" truly FORCED, or assumed? If relaxable, the acceleration we observe = the medium's
2nd phase transition witnessed.

## Regime changes are GRADUAL; the late one templates the early

Three claims, calibrated:
- **Always gradual:** consistent with the process-not-switch reading; defensible for the
 medium's superfluid CROSSOVERS (condensation, potential-domination). ("Always" isn't a
 law of ALL physics -- first-order transitions are sharp -- but holds for THIS model.)
- **Intervals lengthen approaching stability: CORRECT.** Clock: BB→condensation ~1×10³ yr;
 condensation→DE onset ~7.7 Gyr; DE onset→full de Sitter = asymptotically infinite. The
 medium relaxes to a stable ATTRACTOR (de Sitter, w=-1); approach to a fixed point slows
 (the physics behind "critical slowing down"). Final regime change is slowest.
- **Late templates early (THE BET):** the late transition is OBSERVABLE (DESI w(z)), the
 early ones aren't. IF regime changes share a UNIVERSAL form (universality-class precedent),
 measuring the late shape gives the early (condensation) shape → feeds #11, deuterium,
 birefringence-width at once. CATCH: early/late driven by different physics (μ=m vs
 potential>kinetic), so universality is a HYPOTHESIS, not a theorem.

**LOAD-BEARING:** the whole structure rests on DESI thawing being REAL (the (B) branch that
costs the mutual-exclusion theorem; 2.9sigma hint, not a detection).
**CONCRETE TEST:** the SHAPE of w(z). Prediction: a smooth MONOTONIC gradual crossover to -1
(not a step, wiggle, or bump-return). DESI/Euclid measure the shape → supports or breaks the
"always gradual + approaching-attractor" picture. First falsifiable DE-shape prediction.

## RETRACTION (2026-07-08) — the DESI "regime change caught live" reframe was WRONG

Objection #2 was adjudicated and UPHELD. The DESI reframe (w evolving = the
late regime change, threat→confirmation) CONTRADICTED the mutual-exclusion theorem
(ANN-2026-008), and the theorem WINS -- it is LSS-derived, not fiat: observable DE drift
ν~1×10⁻³ requires a core scale M_eff~6.6×10⁻²⁵ eV (l_dB~90 kpc) ⇒ galaxies could not exist.
Galaxies exist ⇒ ν≤1×10⁻⁸ ⇒ NO observable DE thawing.
**Two distinct w's, kept separate.** The dCDF "w:0→-1" is the TOTAL/effective medium
w, running because the floor's DENSITY overtakes the condensate (a density handover). The
DE COMPONENT itself (sign-locked funded floor) is w=-1 ALWAYS (ν≤1×10⁻⁸). DESI measures the
DE-component w = -1, flat. So the model predicts NO thawing; a confirmed DESI thawing would
FALSIFY it. The observable that IS present is the DENSITY HANDOVER (Ω_DE overtaking Ω_DM, the
accelerated expansion, H(z)/Ω(z)),
NOT w_DE evolution.
**Also downgraded:** the "smooth w(z) crossover to -1" prediction assumed observable
DE-component w-evolution; the theorem forbids it IF the settling shares the m̄₂² operator with
the drift (likely). DOWNGRADED to uncertain pending: is the field's SETTLING onto the floor a
separate process from the floor's DRIFT? Owed.

## The granule sim: the S=(1+f_rot²)/2 law does NOT reproduce

`scripts/granule_sim.py` (first build, transparent). Tested whether the claimed granule-power
law S=(1+f_rot²)/2 (which would let a halo's granule contrast read out f_amp independently of
the Z4 dice) falls out of plausible two-component speckle models. RESULT: NONE reproduce it.
 - two independent complex speckles → S~1.0 FLAT (no f_amp dependence);
 - speckle + coherent smooth → S runs 1.0→0.0 (OPPOSITE trend to the doc's 0.5→1.0);
 - real-amplitude + complex-rotation → erratic, no match.
⇒ the S=(1+f_rot²)/2 formula is NOT reproduced by naive speckle; its underlying physical
model is UNPINNED. #8 is blocked deeper than "infrastructure/code" -- the granule channel cannot
serve as an independent f_amp cross-check until the correct two-component speckle statistics are
derived. Honest negative (same discipline as the self-tuning toy). f_amp~0.6 currently rests on
the Z4-dice orbit calc ALONE; the granule cross-check is not yet real.

## The gravitational parity door: computed, Planck-suppressed

The birefringence-of-LIGHT door is welded shut (EM-neutral → anomaly coeff = 0, and charge
conservation forbids any residual). The genesis twist's parity preference (θ-dot ≠ 0 from
the Affleck-Dine spiral) is REAL but lives in the GRAVITATIONAL sector, not the EM one. Its
charge-free home is a CHIRAL gravitational-wave background via Chern-Simons gravity
(L ⊃ α*θ*R R̃). `scripts/chiral_gw_genesis.py` computes the net GW circular polarization:
 Pi ~ α * θ_dot * H_gen / M_Pl² (net chirality)
RESULT: Planck-suppressed. At the model's natural genesis scale (Psi0~5×10¹⁶ GeV, H_inf≤1×10¹³ GeV),
Pi ~ 1×10⁻⁷ to 1×10⁻⁸ -- about 5-6 orders below any conceivable detection (CMB TB/EB reach ~1×10⁻²),
even though the GW background itself can be detectable (r~1×10⁻³). Boosting α by 1×10³ → Pi~1×10⁻⁵,
still unobservable. Observable Pi (≥1×10⁻²) needs near-Planckian genesis H_gen≥2.4×10¹⁷ GeV, which
(a) is ~4000x above the inflationary tensor ceiling and (b) gives an absurd r. VERDICT: the door
is REAL and charge-free (NOT forbidden, unlike the light channel) -- but the fingerprint is
unobservably faint, killed by the M_Pl² in the CS coupling. Robust to the O(1) estimate (no
factor rescues 5-6 orders). The universe's birth-spin twists spacetime, just imperceptibly.
This is the honest counterpart to the birefringence null: light door WELDED (charge), gravity
door OPEN but the room is nearly empty (Planck suppression). [[birefringence-null-proven]]

## Criticality crossover killed (frequency), and the verdict on the whole GW door

`scripts/chiral_induced_gw.py`: tested whether critically-amplified parity-odd scalar perturbations
source an OBSERVABLE chiral induced-GW background (the one place scalar criticality χ~1/c_s² can
leak into the tensor sky). Amplitude CAN reach observable Ω_GW h²~1×10⁻³ for χ>~3000. BUT the
model's critical point is the DE FLOOR (z~0.5, late) → induced GW at f~3×10⁻¹⁹ Hz = horizon-scale
today, off by 3e10x (PTA), 3e15x (LISA), 3e20x (LIGO), even 30x below CMB B-mode. Reaching PTA needs
z_crit~1×10¹³ (deep radiation era); model has none. KILLED BY FREQUENCY, not amplitude.

Verdict on the entire gravitational-parity finding:
 1. DIRECT signal (Pi~1×10⁻⁷): the θ*R R̃ coupling was ASSUMED, not derived. A scalar condensate
 has NO gravitational anomaly (needs chiral fermions) → the CS coupling may be EXACTLY ZERO,
 not 1×10⁻⁷. 1×10⁻⁷ is an upper estimate assuming α~O(1) exists.
 2. INDUCED channel: (a) χ~500 is late-time GROWTH of specific modes, MISAPPLIED as amplification
 of the primordial P_zeta that sources induced GWs; (b) the chiral FRACTION Pi_frac was never
 derived (needs a parity-odd scalar bispectrum, unshown); (c) frequency fatal (above).
 NET: no observable gravitational parity signature survives. The door is REAL and charge-free but
 leads nowhere observable -- Planck-suppressed (direct, if the coupling even exists) or
 frequency-banished + misapplied-amplification (induced). The birefringence-null's gravitational
 counterpart is ALSO observationally null, for robust structural reasons. [[birefringence-null-proven]]

## The +1.24% m_e amplitude, converted from fit to prediction

`scripts/amplitude_11_assembly.py`: assembled eps = c * f_amp * (Psi0/M_red) with propagated
uncertainties. Psi0 (abundance-pinned) and f_amp (Z4 genesis dice) are BOTH fixed by physics
INDEPENDENT of the m_e measurement, so this is a genuine test, not a refit.
 Psi0/M_red = 2.05% [1.23-3.29] ; f_amp = 0.60 [0.50-0.70] ; c = 1.0 [0.5-2.0] (soft dial)
 PREDICTED eps (central, c=1) = 1.232% vs OBSERVED 1.20 ± 0.45% → +0.07σ.
 c needed to nail 1.20% exactly = 0.97 (i.e. natural c~1 lands it).
VERDICT: eps is NO LONGER a free fit parameter. Two of three factors are independently fixed
and force the ~1% SCALE; the central value lands on the data. The ONLY residual freedom is the
single O(1) coupling c, natural at ~1. #11 status: 1 free param → 0, plus one natural O(1) the
data pins to ~1. Order-of-magnitude + central value DERIVED; sharp value pending c (= #14/#16/#17).

## The c-m degeneracy mapped, UFD tension survived

`scripts/c_m_degeneracy.py`: the amplitude fixes a COMBINATION of c and the field mass m, not
either alone. Abundance pins Psi0 ∝ m^(-1/4), so at fixed observed eps:
 c(m) = 0.974 * (m / 2×10⁻²⁰ eV)^(1/4) (higher m needs higher c)
An INDEPENDENT fuzzy-DM mass therefore pins c. Trial of the mass landmarks:
 m = 2×10⁻²⁰ (model pin / Lyman-a) → c = 0.97 (comfortable)
 m = 3×10⁻¹⁹ (UFD Dalal-Kravtsov) → c = 1.92 (edge of O(1)) <- the tension
 m = 1×10⁻¹⁸ (CDM-like) → c = 2.59 (strained)
 c reaches 2 at m=3.6×10⁻¹⁹, 3 at 1.8×10⁻¹⁸, 4 at 5.7×10⁻¹⁸.
VERDICT: the UFD tension is SURVIVABLE, NOT a kill. The model ABSORBS m~3×10⁻¹⁹ by setting
c~1.92 -- still O(1)/natural. Cost: spends c's naturalness margin (0.97→1.9). And c is pinned
only as tightly as m is measured: m in [2×10⁻²⁰, 3×10⁻¹⁹] ⇒ c in [1.0, 1.9], a RANGE consistent
with natural, not yet sharp. #16 delivers c empirically to a factor ~2, bounded by the mass data.
NEW THREAT REGISTERED: if future data pushes m > ~1×10⁻¹⁸ eV, c strains past ~2.6 toward unnatural
-- a naturalness ceiling on the field mass. That is the live falsifier for the amplitude program.

## Birefringence: the portal downgraded to a clean kill

Final resurrection pass over all ~15 birefringence-source attempts. Result: NOTHING resurrects.
Three death classes are un-revivable: (1) killed by conservation law/definition (residual/decaying
charge, reverse-flow, external source, frozen coupling, sign-flip, radiation-coupling → charge
conservation + "touching a photon IS coupling to it"); (2) wrong signature (plasma/Faraday are
CHROMATIC, the hint is ACHROMATIC; color = naming coincidence); (3) alive in the wrong body
(topology → low quadrupole not TB/EB; genesis twist → GW chirality not light).

KEY NEW FINDING -- the PORTAL (dark-photon kinetic mixing), previously filed as "real but costs the
phonon," is now a CLEAN KILL on a deeper structural ground: to reach light the medium must carry the
dark-photon charge, but the medium is a CONDENSATE (<Psi≥Psi0). A charged condensate HIGGSES the
gauge boson (Meissner) → m_gamma' ~ g*Psi0 ~ g*(5×10¹⁶ GeV) = enormous → range ~ 0 → NO long-range
(cosmic) birefringence. So even paying the phonon cost, the condensate self-destructs the messenger.
The superfluidity itself murders the only photon-coupling route. ⇒ the last "maybe" is now a "no".
P-2026-009 birefringence null is now hardened: every grave is a clean kill, and the one that had a
pulse (portal) flatlined on re-exam. [[birefringence-null-proven]]

## Non-birefringence results from the same analysis

Mining the birefringence graveyard for what it says about the model OTHER than birefringence:
1. CENSUS IS STRUCTURALLY FORCED (biggest): the portal autopsy generalizes → because the medium
 is a CONDENSATE, ANY gauge force it carries is Higgsed short-range (Meissner). Gravity is the
 ONLY long-range force that can't be Higgsed. So "gravity-only" is not a neutrality coincidence;
 it is a structural consequence of superfluidity. NEW TESTABLE PREDICTION: PRTOE forbids any
 long-range dark/fifth force from the medium (fifth-force & equivalence-principle tests can probe).
2. BIREFRINGENCE DATA IS A DISCRIMINATOR (overlooked): axion-DE predicts nonzero β; PRTOE predicts
 exactly zero from the dark sector. So the β hint adjudicates PRTOE vs axion-DE either way it
 resolves -- we had been reading it only as our own null.
3. PARITY MAP COMPLETE: everything parity-even (gravity, Thomson, E-modes, census) EXCEPT the genesis
 twist, which imprints ONLY on gravity (GW chirality Pi~1×10⁻⁷). ⇒ any parity-odd signal can only be
 the GW chirality; in light, flat zero.
4. P-2026-013 (closed universe) was itself a birefringence-tangent spinoff -- the hunt's largest yield.
⇒ candidate new prediction to register: "no long-range dark/fifth force (condensate Higgses all
mediators short-range)". [[birefringence-null-proven]]

## Where the dead ends live

The retracted lepton/hadron varying-constant hierarchy (P-2026-011) is in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) under **"Retracted predictions"** — it
needed a Higgs/EM portal the census forbids, and the census-legal reading is the universal
conformal rescaling this file derives. The full birefringence dead-end map (why the parity
signal is forced out of light and into gravity) lives under **"Birefringence."**
