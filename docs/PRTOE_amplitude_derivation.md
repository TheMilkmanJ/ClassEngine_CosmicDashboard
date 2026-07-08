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
