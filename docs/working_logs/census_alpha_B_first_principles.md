# First-principles α_B → census γ* (2026-07-31)

Code: `scripts/census_alpha_B_first_principles.py`.  
Depends on: overdamped VOS structure in `census_vos_microphysics.py`,  
normalization triangle in `as_normalization_triangle.py`,  
ε stack (c·f̄·α_c).

## Result (headline)

| route | formula | γ* | vs f(r=1) | A_s(r=1,γ*) vs measured |
|---|---|---|---|---|
| **L** (floor) | ε² | 1.573×10⁻⁴ | **0.713×** | 0.360× |
| **T** (primary) | ε²√2 | 2.225×10⁻⁴ | **1.009×** | **1.017×** |

**Grade: CANDIDATE CLOSED** on Route T — no fit to A_s; one named O(1) (c_chop = d_⊥ = 2).

## The force law (what is derived vs named)

### Derived without free coefficients

1. **α_B = ε²**  
   The portal amplitude ε is the only small dimensionless coupling of the
   genesis winding medium to a dissipative channel. The reversible mass
   response is first order in ε (δm/m = ε|cos θ|). Dissipation — a rate —
   enters at second order: **α_B = ε²**.

2. **k_mom = α_B² = ε⁴**  
   Overdamped VOS structure (forced by small γ*; equal-coeff maps cannot
   overdamp): curvature momentum is friction-suppressed, k_mom ~ α_B².

3. **c_chop = O(1)**  
   Loop chopping / reconnections are topological, not portal-suppressed.
   They do not carry powers of ε.

4. **Radiation fixed point**  
   γ* = √[k_mom(k_mom + c_chop)] at β = 1/2, with v* ≪ 1 on both routes.

### Named O(1) — Route T

**c_chop = d_⊥ = 2**: the transverse plane of a line defect is two-dimensional,
so the phase space for loop production carries d_⊥ = 2.

Then

> **γ\* = ε² √2 = 2.225×10⁻⁴**

which is **+0.87%** on the r=1 triangle target from the closed form A_s, and
gives A_s(r=1) **+1.7%** on the measured 2.100×10⁻⁹.

Route L (c_chop = 1) is the coefficient-free floor: γ* = ε² at 0.71× target —
the right *scale*, wrong O(1).

## Rejected routes (computed)

| route | why dead |
|---|---|
| f_n = (T/T_c)⁴ at z ~ 10⁶ | ~10⁻¹²; **runs with z** → cannot hold γ* fixed across CMB decades |
| phonon ρ_n(ζ T_γ)/ρ_dm | α_B ≫ 1 — not the overdamped branch |
| (T/Ψ₀)² global-string radiation friction | ~10⁻⁴⁷ |
| γ* ≟ α_c²/2 with no force law | +8.6% numerical near-miss; coincidence risk |

## What this does *not* claim

- **n_s − 1 = −0.035** from α_B alone (still the modulation envelope / approach
  transient — see `tilt_envelope_derivation.md`).
- **d_⊥ = 2 is theorem-closed** — it is the natural transverse-plane factor;
  kill if reconnection microphysics returns a different O(1).
- **Zero free parameters for the whole model** — Track B inputs (portal
  √σ_dark=m_e, ξ_H, n-draw, c counting, …) remain.

## Kill conditions

1. Medium reconnection calculation returns c_chop far from 2, and no replacement
   O(1) restores γ* without fitting to A_s.
2. Closed-form A_s (independent channel) moves by ≫5% with Route T held fixed.
3. Promoting Route T while back-solving c_chop from A_s (forbidden inversion).

## Cross-links

- Class exhibition: `census_scaling_mechanism.md`
- Structure pass: `census_gamma_star_derivation.md`, `census_vos_microphysics.py`
- A_s closed form: `PRTOE_DERIVATION_HUNT.md` §7, MATH_SPINE §23.5
- ε stack: `PRTOE_THE_AMPLITUDE.md`, `_CANONICAL_VALUES.md`
