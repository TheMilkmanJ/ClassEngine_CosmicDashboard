# Census γ* / f — microphysics attempt (2026-07-31)

Code: `scripts/census_vos_microphysics.py`.  
Prior class exhibition: `census_scaling_mechanism.md`, `scripts/census_scaling_network.py`.  
Normalization target: `scripts/as_normalization_triangle.py` → **f(r=1) ≈ 2.21×10⁻⁴**.

## Goal

Derive the imprint cell fraction **f = k·ξ = γ\*** (at horizon exit) from the genesis
superfluid medium — **without** solving for friction parameters from A_s.

## What closed today (structural)

1. **Bare curvature–friction balance is not a scaling derivation.**  
   ξH ~ √(κ H ln / (4π α_B)) retains H (and m). Constant γ* requires the
   dimensionless VOS reduction, not a static force balance.

2. **κ ↔ ξ_h identity** on recorded (m, c_s):  
   κ = 2π/m, ξ_h = 1/(m c_s) ⇒ **κ = 2π c_s ξ_h**.

3. **Overdamped branch is forced by the smallness of f.**  
   Under the viable map A (k_mom = α_B², c_chop = 1): hitting f ≈ 2.21×10⁻⁴ needs  
   α_B ~ 2.21×10⁻⁴ and v* ~ 2.21×10⁻⁴ ≪ 1 — dense superfluid tangle, not
   relativistic strings (strengthens the class result in `census_scaling_mechanism.md`).

4. **Equal-coeff ansatz fails overdamping.**  
   c_chop = k_mom = α_B always gives v* ~ O(1). The momentum parameter must be
   **friction-suppressed** relative to chopping. That is a structural constraint on
   any future microphysical map.

5. **γ(β) minimum at radiation** still holds under the overdamped map (n_s ≈ 1 robust).

## What did **not** close

| claim | result |
|---|---|
| γ* from (α_c, ε, c_s, f̄, c) alone | **No.** Best numerical near-miss α_c²/2 at **+8.6%** — no force law forces the identification; coincidence risk (α_c ~ 0.022, target ~ 2×10⁻⁴). |
| α_B from phonon/normal fluid at imprint | **Not in corpus.** Would be a real derivation if computed. |
| Invert α_B from A_s then call A_s derived | **Forbidden** (kill condition). That is a measurement of dissipation. |

## Retyped residue

**One dimensionless mutual-friction (or VOS pair) number** for the genesis tangle.

- Under map A, A_s **measures** α_B ≈ 2.21×10⁻⁴.
- Deriving A_s end-to-end still requires deriving that number from medium content
  (normal-fluid fraction, phonon scattering, winding energetics) at imprint.

## Relation to A_s closed form

The closed form A_s = (α_c/4πk)³ remains **candidate grade** (channel + count + measure).
It is **consistent** with the r-triangle at r ~ 1 (f ~ 2.21×10⁻⁴). Consistency is not
a medium derivation of f.

## Grade (superseded 2026-07-31 evening)

**NUMERICAL NEAR-MISS ONLY** was the morning grade.  
**Superseded by** [`census_alpha_B_first_principles.md`](census_alpha_B_first_principles.md):

- α_B = ε² (portal second-order dissipation) — derived scale  
- Route T: c_chop = d_⊥ = 2 → **γ\* = ε²√2** within 1% of f_ref, A_s within 2% of measured  
- Grade: **CANDIDATE CLOSED** (named residual: defend d_⊥=2)

Do **not** claim γ* = α_c²/2. Do **not** claim zero free parameters.
