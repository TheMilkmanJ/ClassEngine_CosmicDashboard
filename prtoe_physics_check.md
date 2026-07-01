# PRTOE Perturbation Physics Check

## What does PRTOE actually do?

### Background (✅ Working)
- Friedmann: H² = (ρ_matter + ρ_prtoe + ρ_rad) / 3M_pl²
- Field equation: φ̈ + 3Hφ̇ + V'(φ) = 0
- Scalar field couples through F(φ) = 1 + ξ·φ²·A(φ)
- This modifies H(z) ✓

### Perturbations (❌ Singular Jacobian)
For perturbations, PRTOE should affect:

1. **Matter perturbations δ_m**
   - Standard continuity/Euler equations
   - Modified by effective gravitational constant G_eff = G·F(φ)
   - This is what the Chameleon screening addresses

2. **Scalar field perturbations δφ**
   - Second-order wave equation with mass/friction terms
   - Should couple to matter via metric perturbations

3. **Metric perturbations (Φ, Ψ)**
   - Modified Einstein constraints from PRTOE energy-momentum tensor
   - These determine slip parameter η = Ψ - Φ

## The Critical Question:

**Does δφ directly couple to δ_m?**

If YES (scenario A):
- Matter feels the scalar field directly
- Need full coupled system: (δ_m, θ_m, δφ, δ̇φ, Φ, Ψ)
- This is what we're trying to implement
- Singular Jacobian suggests this system is malformed

If NO (scenario B):
- Matter only feels PRTOE through modified metric (G_eff)
- δφ evolves independently
- Matter perturbations use standard equations with G_eff instead of G
- CLASS doesn't need to know about δφ at all!

## Which is physically correct?

Looking at our equations:
- We have F(φ) = 1 + ξ·φ²·A(φ) modifying Friedmann
- We have slip: Φ + Ψ = ξ·F·dφ·δφ

This suggests **Scenario A** - full coupling. But if the coupling is
weak (ξ ~ 1e-6), then in practice **Scenario B** is approximately correct.

## Hypothesis:

The singular Jacobian happens because we're trying to evolve δφ
coupled to matter perturbations, but CLASS's standard perturbation
solver assumes a much simpler structure (just fluids + metric).

Adding a new scalar field with its own dynamics breaks CLASS's
assumptions about the system structure.

