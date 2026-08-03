# c_chop = d_⊥ = 2 — transverse reconnection kinematics (2026-07-31)

Code: `scripts/census_c_chop_transverse.py`.  
Prior: `census_alpha_B_first_principles.md` (Route T γ\*=ε²√2, named residual d_⊥=2),  
`census_vos_microphysics.py`, `census_scaling_network.py`.

## Result (headline)

| object | status | value |
|---|---|---|
| d_⊥ | **DERIVED** | d − 1 = 2 (codim-2 line defect in R³) |
| p, α, f_ℓ | **DERIVED** on overdamped one-scale branch | all = 1 |
| C_geom = d_⊥ | **CANDIDATE** | non-double-counting transverse DOF count |
| **c_chop** | **CANDIDATE** | **2** (primary); sensitivity π/2 |
| γ\* (Route T) | consistent | ε²√2 = 2.225×10⁻⁴ (+0.87% f_ref, A_s +1.7% meas) |

**Grade: CANDIDATE** — residual defended and narrowed, not theorem-closed to percent level.

## What closed

### 1. d_⊥ = 2 is forced (theorem half)

A vortex is a line defect. In spatial dimension d = 3 (the same d that enters
α_c = d·α), its codimension is 2, so the transverse space is two-dimensional:

> **d_⊥ = d − 1 = 2**

Loop production / reconnection is the approach of two segments *in that
transverse plane*. The integer count of independent transverse directions is
d_⊥. This is embedding geometry, not a fit.

The solid-angle ratio Ω(S¹)/Ω(S²) = 2π/4π = 1/2 is a *reduction* of bare 3D
direction measure — it does **not** by itself produce an enhancement factor 2.
The factor 2 is the **dimension** of the transverse plane, not a solid-angle
ratio. (Script §1 records this explicitly so the two readings cannot be
confused.)

### 2. Microscopic → VOS map

Corpus VOS convention (Martins–Shellard; `census_scaling_network.py`):

```
ρ̇|_chop = − c_chop  μ v / ξ³
ξ̇|_chop = ½ c_chop v
```

One-scale reconnection counting gives

> **c_chop = C_geom · p · α · f_ℓ**

with α = ⟨ℓ_loop⟩/ξ and f_ℓ the fraction of reconnections that remove a loop
from the long-string network.

### 3. p = α = f_ℓ = 1 on the overdamped PRTOE branch

| factor | value | why forced |
|---|---|---|
| p | 1 | continuum superfluid vortices reconnect when cores meet (topological; geometric, not portal-suppressed — already used to set c_chop = O(1) rather than O(εⁿ)) |
| α | 1 | overdamped one-scale: the network has a single length ξ; α ≪ 1 is the relativistic small-loop cascade, absent on this branch |
| f_ℓ | 1 | one-scale self-similarity (order-unity loop fraction; no second population) |

Therefore **c_chop = C_geom**.

### 4. C_geom = d_⊥ (candidate identification)

First-principles estimates computed in the script (no A_s input):

| estimate | C_geom | γ\*/f_ref | A_s/meas | role |
|---|---|---|---|---|
| bare unit | 1 | 0.713 | 0.360 | Route L floor |
| ⟨\|sin θ\|⟩ = π/4 | 0.785 | 0.632 | 0.250 | orientation only (incomplete) |
| d_⊥ · ⟨\|sin θ\|⟩ = π/2 | 1.571 | 0.894 | 0.708 | sensitivity (double-counts angles) |
| **d_⊥** | **2** | **1.009** | **1.017** | **primary** |

**Why primary is d_⊥, not π/2:**

- VOS already feeds the RMS segment speed v into ξ̇ = ½ c v. Orientation is
  inside that average. Multiplying by ⟨\|sin θ\|⟩ again **double-counts** angles.
- d_⊥ counts independent transverse approach channels once, matches the unique
  integer geometric invariant of the embedding, and is the non-double-counting
  closure.

Then

> **c_chop = 2,  γ\* = ε² √2 = 2.225×10⁻⁴**

with no fit to A_s (A_s is referee only).

## Robustness

Natural kinematic interval from the first-principles set:

> **c_chop ∈ [π/2, d_⊥] ≈ [1.57, 2]**

| endpoint | γ\*/f_ref | A_s/meas |
|---|---|---|
| π/2 | 0.894 | 0.708 |
| 2 | 1.009 | 1.017 |

γ\* stays inside ~11% of the r=1 target across the whole interval. A_s (∝ f³)
moves by up to ~30% — so percent-level A_s is a successful consistency test of
the primary closure, not an independent derivation of it.

Wider O(1) box [1.5, 2.5]: γ\*/f_ref ∈ [0.87, 1.13]. Route T structure is
robust at O(1); it is not robust at the percent level under arbitrary O(1)
rescaling (and is not claimed to be).

## External consistency (not an input)

Relativistic Nambu–Goto VOS calibrations give c̃ ≈ 0.23 with characteristic
loop-size parameter α_NG ~ 0.1, so the geometric efficiency c̃/α_NG ~ 2.3 ≈ d_⊥.
Overdamped one-scale forces α → 1, hence c_chop → c̃/α ~ d_⊥. This is a
literature cross-check only; the PRTOE prediction does not consume NG numbers.

## What this does *not* claim

- **Percent-level theorem** that κ = 1 in c_chop = κ d_⊥. The identification
  C_geom = d_⊥ is the natural unit choice (non-double-counting); a medium
  reconnection simulation could return κ = π/4 or similar.
- **n_s − 1 = −0.035** from this coefficient.
- **Zero free parameters** of the whole model (Track B inputs remain).
- **Back-solving c_chop from A_s** (forbidden; script records the inversion
  c_from_f_ref ≈ 1.97 only as a kill-log consistency check — primary d_⊥ = 2
  sits 1.75% from it).

## Kill conditions

1. Medium reconnection calculation returns c_chop far outside [1.5, 2.5], and no
   replacement O(1) restores γ\* without fitting to A_s.
2. Proof that d_⊥ does not enter the chopping phase space.
3. Promoting Route T while back-solving c_chop from A_s.

## Residual retype (A1)

**Before:** named residual = “defend d_⊥ = 2”.

**After:**

- d_⊥ = 2 is **defended** (codimension theorem + d = 3).
- p = α = f_ℓ = 1 are **forced** on the overdamped one-scale branch.
- Residual narrowed to: **C_geom = d_⊥ versus a nearby phase-space average
  (π/2)**. Primary chooses d_⊥ by non-double-counting; sensitivity is 11% on γ\*.

A1 overall remains **CANDIDATE CLOSED** (force law + one natural geometric
identification; residual no longer an undefended integer).

## Cross-links

- Force law α_B = ε², k_mom = ε⁴: `census_alpha_B_first_principles.md`
- Overdamped structure: `census_vos_microphysics.py`, `census_gamma_star_derivation.md`
- Attractor class: `census_scaling_mechanism.md`
- Board: `_E2E_DERIVATION_BOARD.md` A1
- A_s closed form: `PRTOE_DERIVATION_HUNT.md` §7, MATH_SPINE §23.5
