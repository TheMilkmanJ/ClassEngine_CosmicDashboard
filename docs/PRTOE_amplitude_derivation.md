# The 1.24% Amplitude — Consolidated Derivation (the showcase room, 2026-07-07)

*Consolidates the §57–74 build in PRTOE_me_trigger.md into one clean story:
how the electron-mass amplitude went from a naked fit to a traced, census-gated
prediction. Every factor labeled by its status: TRACED / COMPUTED / NATURAL /
GATED.*

## The number

ε ≡ δm_e/m_e ≈ **1.24%** — the varying-electron-mass shift at recombination that
eases the H0 tension. Fit to the CMB; the model's one novel empirical handle.

## The factorization (from the transaction structure)

    ε  =  c  ×  f_amp  ×  (Ψ₀ / M_red)

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
  (the "One Mountain" dice), NOT sim-pending. The granule sim (task #8) is an
  independent cross-check (granule power S = (1+(1−f_amp)²)/2), not the source.
- **Distributional:** f_amp is one genesis-dice roll per universe (median ~0.6);
  our 1.24% ⇒ we drew the median ⇒ a typical universe.

## Factor 3 — c ≈ 1 (NATURAL, GATED on the census — task #5)

- **Make-or-break PASSED.** The dangerous alternative was the Ψ₀ normalization
  (δm_e/m_e = δΨ/Ψ₀ → O(1) blowup), which requires m_e ∝ Ψ (dark-sourced Yukawa).
  But **m_e is Higgs-sourced**, and the census forbids the Yukawa — excluded
  twice. The coupling is gravitational (conformal), scale M_red, no blowup.
- **c is a free O(1) conformal coefficient.** Scale invariance does NOT force
  c = 1 (the amplitude mode is a massive pseudo-dilaton coupling to Higgs-sourced
  masses, not a Goldstone to scale-sector masses). Data wants c ≈ 0.94.
- **c = 1 ⟺ the STRONG census** ("medium couples to matter at exactly
  gravitational strength, no free constant"). So c reduces to the **census-scope
  adjudication (task #5)**:
  - STRONG census → **ε = f_amp × Ψ₀/M_red is FULLY DERIVED = 1.24%.**
  - WEAK census → c ≈ 1 is natural + data-consistent, not forced.

## The transaction (why the factors are what they are)

The m_e shift is a closed loop of couplings, matter → space → matter:
1. **matter → space (gravity):** clustering/shell-crossing saturates Θ.
2. **Θ (the all-clear gate):** binary — diffuse "hold" / virialized "release".
   Matter's own state, written into the fluid.
3. **space → matter (β = the read gain):** β = f_amp reads Θ back onto m_e.
   INFORMATION not energy (census-forced small, §69) → UNCOLLECTABLE (the bank
   collecting its own information, §71). Matter reallocates its own energy
   (FIRAS-safe reallocation branch).
4. **matter → matter (EM):** the electron's EM-structured mass realizes the
   shift, distributed by hydrogen/reduced-mass flavor (electron dominates).

## Status

**Traced end-to-end.** Two of three factors are traced/computed (Ψ₀/M_red,
f_amp); the third (c) passed its make-or-break and reduces to the model's central
census-scope hinge. **The 1.24% is now one census ruling (task #5, strong
direction) away from a complete derivation.** The scariest failure mode (Ψ₀
blowup) is eliminated. Remaining honest caveats: c=1 not forced (only natural);
distributional (median, our universe typical); the dice's own h-convergence
caveats; and the whole chain still assumes the discrete-switch m_e mechanism
(ANN-2026-013), whose payload operator is un-built.

---

## FOUNDATIONAL NOTE (parked, 2026-07-07): R=0 ontology, bubble-vs-infinite, and the multiverse edge

*Operator's foundational question chain, and its correct parking. Recorded so the
model's silent assumption is on record, NOT so anything is built on it.*

**R=0 = the model's absolute nothing** (no medium, no curvature — the genesis
ground state). Its direction is TEMPORAL ("before"), not spatial ("outside"):
the genesis happened everywhere at once in an already-unbounded space; the
universe DILUTES (ρ∝a⁻³) as it expands, it does not invade fresh R=0.

**OPEN foundational choice (data cannot reach it):** the fitted cosmology ASSUMES
unbounded homogeneity (FLRW). Whether the medium is globally infinite OR a finite
BUBBLE of R=1 in an R=0 void is undetermined — the CMB fit assumes the former but
never earns it. In the bubble reading, expansion IS into R=0 nothingness (the
operator's picture is then literally correct).

**Multiverse extension (operator, correctly PARKED as philosophy):** if R=1
nucleates in R=0, generic bubble/eternal-inflation logic gives OTHER R=1 regions.
Untestable in principle — causally sealed by super-horizon R=0 inflation. The
operator flagged this un-chaseable; adopted.

**The neighbor rule + its single crack (honest):** no signal from a neighbor
reaches us EXCEPT a possible early BUBBLE COLLISION (a circular CMB temperature
disk). Planck/WMAP searched — NULL. So the one testable edge CONFIRMS the
neighbor rule (nothing has reached us). Additional distance from PRTOE: its
genesis is Affleck-Dine ROLLING, not Coleman-De Luccia bubble NUCLEATION — so the
multiverse isn't even clearly this model's mechanism. Speculation atop an
unearned assumption: doubly un-chaseable. Booked PARKED; the model leans on none
of it.

---

## SESSION UPDATE — §75–92 (2026-07-08): the coupling structure, and where it stands

*The consolidation above froze at §74. This block carries it to §92.*

**Factor 3 (c) — much more resolved.** c is now BOXED near 1, not free:
- **Ceiling (c ≲ 1):** DERIVED from technical naturalness (§75, operator's "too
  expensive"). A stronger-than-gravitational coupling radiatively destroys the
  medium's own ultralight mass — so c can't exceed gravitational strength. The
  ledger caps c to survive.
- **Floor:** the amplitude is over-determined (pinned f_amp, Ψ₀) so c can't drop
  far without breaking the fit (§76–77). Measured value: **c = 0.93 ± 0.38**,
  consistent with 1, sharpening as Fairbank converges.
- **The remaining bet (§81 vs §82):** is c a *free dial* (§81) or *forced = 1*
  (§82, operator — "no half-gravity")? DATA can referee it: the granule sim's
  independent f_amp isolates c (§83, breaks the §77 degeneracy) and reads our
  universe's dice roll (f_amp ≈ 0.56). But *measuring* c=1 ≠ *deriving* it (§84):
  only the effective-action calc (#14) proves "no dial."

**Why the coupling is universal & flavor-blind (§89, operator):** gravity couples
to mass-energy only — it *cannot* tell electron from quark ("same shit, different
flavor" = the equivalence principle). So c is universal by constitution, and any
flavor must be matter's own — the medium has no organ to make it.

**Flavor / deuterium arc (§85–92) — resolved, with retractions:**
- The lepton/hadron flavor (P-2026-011) needs a NON-gravitational touch on the
  Higgs/EM sector — a portal the census forbids (§90). **P-011 RETRACTED**
  (ANN-2026-015); the model predicts UNIVERSAL varying-constants.
- **No Higgs portal is actually needed (§92, operator's correction to my §90):**
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

## SESSION UPDATE — #11 analytic backbone (2026-07-08): the amplitude PINS the mass

`scripts/amplitude_11_analytic.py` (fast/analytic, completes in-sandbox; the stiff
genesis ODE for f_amp still needs WSL). Result:
- **Psi0 ~ 5e16 GeV is DERIVED from the DM abundance** (leading-order misalignment,
  rho_dm0 = 1/2 m^2 Psi0^2 a_osc^3, a_osc from H=m). Confirms the traced value.
- eps = c*f_amp*(Psi0/M_red) lands in the **right decade (1-5%) from abundance alone**.
- Demanding **eps = 1.24%** (c=1, f_amp=0.6) **PINS the mass: m ~ 2e-20 eV** (Psi0/M_red
  = 2.07%, matching the traced pair). The amplitude program is internally self-consistent
  and corresponds to m ~ 2e-20 eV, NOT the 1e-21 fuzzy-DM fiducial we had loosely quoted.
- **This converts the fit into a prediction / advances #9 (mass pin):** abundance fixes
  Psi0; eps=1.24% then pins m to the ~1e-20 decade. Falsifiable, and consistent with the
  Lyman-alpha fuzzy-DM floor (~2e-21 eV, so allowed).
- **OWED (factor-level, not order-level):** f_amp from the genesis orbit (WSL ODE), c from
  the #14 loop, O(1) misalignment factors (~2x). These move the pinned m by factors.

## SESSION UPDATE — #11 f_amp orbit (2026-07-08): mechanism confirmed, ~0.6 natural

`scripts/genesis_famp_orbit.py` (Cartesian, NON-stiff, runs in-sandbox -- the WSL
caveat did NOT bind). Complex AD field in V=m^2|Psi|^2+lam|Psi|^4 with Hubble
friction; f_amp = time-averaged RADIAL (breathing) energy fraction of the late-time
orbit.
- **Mechanism CONFIRMED:** f_amp set by orbit eccentricity, spans 0.47-0.99 as the
  release kick varies (near-radial -> f_amp~1, near-circular -> f_amp~0.5).
- **Central value ~0.6 is NATURAL:** median over a flat kick prior = 0.62, matching
  the doc's assumed f_amp~0.6. Not cherry-picked -- it's where the mechanism sits.
  (f_amp=0.6 exactly <-> kick~1.3.)
- **CAVEAT:** generic AD orbit (quartic + parametrized kick), NOT the model's
  specific A-term, so the DISTRIBUTION is illustrative/prior-dependent; the mechanism
  and ~0.5-0.6 central value are robust.

**#11 amplitude standing:** eps = c * f_amp * (Psi0/M_red). Psi0 DERIVED (abundance,
-> m~2e-20 eV), f_amp mechanism-confirmed (~0.6), both in-sandbox. Only **c** remains
(the #14 effective-action loop). The three are mutually consistent at 1.24% for
m~2e-20 eV, c~1, f_amp~0.6.

## SESSION UPDATE — #2 (real Z4 A-term) + #14 (c verdict), 2026-07-08

**#2 -- f_amp from the MODEL's real A-term (`scripts/genesis_famp_Z4.py`).** Z4 tilt
V_A = eps_A lam (Psi^4 + h.c.) = 2 eps_A lam R^4 cos(4theta); field released AT REST
at phase theta_i (uniform prior after inflation); rotation is GENERATED by the torque,
not assumed. Median f_amp over the uniform phase prior:
  eps_A=0.10 -> 0.59 ;  0.20 -> 0.68 ;  0.30 -> 0.74 ;  0.50 -> 0.70  (range ~[0.05,1.0])
=> **f_amp ~ 0.6 is where the model's own dice sit** (hit dead-on at small tilt), NOT an
assumption. Residual = the tilt strength eps_A (slides the median 0.6->0.7).

**#14 -- is c forced to 1? VERDICT: SOFT DIAL, not forced.** The amplitude mode is a
PSEUDO-dilaton (the m^2 term breaks scale invariance explicitly), so the dilaton
low-energy theorem that would pin c=1 does NOT bind; "no half-gravity" fails because a
matter scalar couples conformally via a non-minimal xi phi^2 R with CONTINUOUS xi. So c
is a BOUNDED O(1) (<=1 by naturalness, ~0.93 measured), not symmetry-forced.
**Consequence:** with f_amp computed, eps = c*f_amp*(Psi0(m)/M_red) = 1.24% is ONE
equation in TWO unknowns -> pins a **c-m relation**, not either alone. Breaks 3 ways:
compute xi (hard theory), measure m (fuzzy-DM astro), or the granule sim (#8).

**AMPLITUDE PROGRAM, post-#11/#14:** Psi0 DERIVED (abundance), f_amp DERIVED from the
Z4 dice (~0.6), c a bounded soft-dial degenerate with m. The 1.24% is now a **derived
relation between two ultralight-sector numbers (c, m)**, not a free fit -- a constraint
surface with two astrophysical ways to close it.

## SESSION UPDATE — c-m degeneracy BROKEN by fuzzy-DM data (2026-07-08)

c-m curve (f_amp=0.6): **c(m) = (m / 2.24e-20 eV)^(1/4)**; naturalness c<~1 => m <~ 2.24e-20 eV.
Fuzzy-DM lower bounds: Lyman-alpha (Rogers&Peiris 2021) m>2e-20 eV (95%); UFD (Dalal&Kravtsov
2022) m>3e-19 eV (99%, stronger but more model-dependent).
- **NEAR-COINCIDENCE:** the model's natural ceiling (2.24e-20) sits right at the Lyman-alpha
  floor (2e-20) -> model cornered to m~2e-20 eV, **PREDICTS c~0.97-1.0**. Measured c=0.93+-0.38
  confirms. FIVE independent lines (amplitude, abundance, naturalness, Lyman-a, measured c)
  converge on (m~2e-20 eV, c~1). Degeneracy broken; c pinned ~1, no longer a free dial.
- **THREAT (3rd):** the UFD bound (m>3e-19) would force c~1.9 -- mildly unnatural AND ~2.5sigma
  against the measured c. If UFD holds (debated), real tension. 
- **#6 is now a SHARP test:** as c tightens from +-0.38, it either nails c~1 (confirms corner)
  or drifts low (m below Lyman-a floor -> tension).

## SESSION UPDATE — origins audit: c derives from the CENSUS (honest downgrade, 2026-07-08)

Traced the "convergences on c~1" to their roots; two corrections + one deepening:
- **OVERCOUNT corrected:** "measured c=0.93" is NOT independent -- it is the amplitude eps
  rearranged (c = eps/(f_amp*Psi0/M_red)). Same input, not a separate confirmation.
- **Naturalness ceiling and UV/ALP share ONE root:** "can't exceed gravitational strength"
  (ceiling) and "gravity generates it at gravitational strength" (floor) are the same
  statement -- **c~1 because the coupling IS gravity (strength 1 in M_red units) = the census.**
- **Genuine convergence = TWO independent things, agreeing:** (1) THEORY/census predicts c~1
  (= the strong census restated quantitatively); (2) DATA: Lyman-alpha m>2e-20 -> via the c-m
  curve -> c>0.97. The census's predicted c~1 and the mass data's implied c~0.97 AGREE, non-
  circularly.
- **Upshot:** c does not derive from 5 places; it derives from the census. "c=1" IS "the coupling
  is exactly gravitational." The amplitude program is therefore "census predicts c~1; does the
  independent mass agree?" -- YES (Lyman-a), with the UFD bound as the one dissenting dataset.
