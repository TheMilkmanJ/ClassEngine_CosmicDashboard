# The census imprint's scaling mechanism — exhibited, not asserted (#168)

*The A_s imprint (THE_CHAIN link 5) was re-typed to a **scaling** ratio: the coherence length holds
a fixed fraction of each mode's own scale, ξ/ℓ_H = k_*ξ = (2π²A_s)^⅓ = 3.45×10⁻³, across every
decade the CMB resolves. The class was settled by the tilt (a frozen comoving cell is white noise,
n_s = 4, excluded); the standing debt was the **dynamics that enforces the self-similarity** — "the
corpus asserts the scaling class without exhibiting the dynamics that enforces it" (DERIVATION_HUNT
§7). This log exhibits that dynamics. Code: `scripts/census_scaling_network.py` (self-checking; four
closed forms anchored in the harness).*

## The mechanism: a defect-network scaling attractor

ξ/ℓ_H constant across decades is the textbook signature of a **defect-network scaling regime** — a
network of topological defects in an expanding background flows, from generic initial conditions, to
a self-similar state in which the correlation length tracks the horizon at a fixed ratio. The PRTOE
genesis is a rotating superfluid threaded with windings and vortices, so its census cells are the
cells of a **genesis vortex tangle**, and the self-similarity the imprint needs is the tangle's own
scaling attractor. This is not a new postulate: it is the generic late-time behaviour of a defect
network, imported to the link that already reads A_s as a shot-noise census of cells.

**Exhibited (the attractor is dynamically real).** Integrating the velocity-dependent one-scale (VOS)
equations for ξ and the RMS velocity v in a radiation background,

  dξ/dt = Hξ(1+v²) + ½ c̃ v ,  dv/dt = (1−v²)[k_v/ξ − 2Hv] ,  H = β/t ,

trajectories launched from *both* sides (ξ/t = 0.03 and 4.0) close onto one ratio — the gap shrinks
from 0.36 to 0.02 over the integrated range — matching the analytic fixed point ξ = γ*t. The approach
is a slow power law: with v → v*, the ξ/t transient decays as t^(a−1), a = β(1+v*²) < 1, so
γ* is an attractor but reached only after many decades. That slowness is itself a known feature of
defect networks, and it is a candidate source for the tilt (below). The self-similarity the corpus
asserted is therefore a genuine dynamical attractor, not an assumption.

## The value 3.45×10⁻³ is a physical discriminant

γ* is set by the network's velocity. A **relativistic** (Nambu–Goto) network scales at
γ ~ O(0.1–0.3) — of order one coherence cell per horizon — which is a factor ~10⁷ too *few* cells to
carry A_s (the observed ratio wants (ℓ_H/ξ)³ ≈ 2.4×10⁷ cells per horizon). Hitting γ = 3.45×10⁻³
requires the strongly **overdamped** branch: a network drift velocity v ~ 1.5×10⁻², i.e. a dense
tangle held small by strong dissipation. That is exactly a **superfluid vortex tangle under mutual
friction**, not a relativistic string network — so the smallness of 3.45×10⁻³ is not an embarrassment
to be tuned away; it is a reading that points straight at the model's own superfluid genesis medium.

## The tilt: n_s ≈ 1 is robust; the red −0.035 is sub-leading

Exact scaling gives n_s = 1 by construction (ξ ∝ 1/k makes Δ²_ζ ∝ k³ξ³ flat). Whether the drift of
γ* reddens it depends on how γ* responds to the background: and γ*(β) has a **minimum at radiation**
(β = ½), where dγ*/dβ ≈ 0 — precisely where the CMB modes imprint. So the equation-of-state drift is
suppressed there, and the network predicts **n_s ≈ 1 robustly** (near-scale-invariance for free, not
tuned). The observed red n_s − 1 = −0.035 is then a **sub-leading correction**, of order the
departure from exact scaling; its candidates, none yet computed, are (a) the slow
approach-to-scaling transient (the t^(a−1) residual, which is red), (b) a mild scale-dependence of the
imprint transfer R, and (c) the exit from radiation. This is the honest residual: the mechanism fixes
n_s ≈ 1; the last −0.035 is open.

*(A recorded exponent, placed correctly: `scripts/winding_gas_cv*.py` carry ν = 2/3 (3D-XY), but for
the condensation transition at T_c — a different link. The census imprint's dynamical half — the
scaling attractor, its velocity, and what sets γ* — is the object here, and z / (ξ₀, τ₀) remain the
microphysics the value derivation owes.)*

## Grade

**Class exhibited; value and medium-derivation open.** #168 moves from *"asserted, never exhibited"*
to a demonstrated mechanism: ξ/ℓ_H = const is a real dynamical attractor of the genesis vortex
tangle, its smallness selects the overdamped/superfluid branch (the model's own medium), and it
delivers n_s ≈ 1 robustly. What remains is genuine model-building, not assertion: (a) the exact value
γ* = 3.45×10⁻³ from the tangle's microphysics (winding energetics, the mutual-friction coefficient),
first-principles from the PRTOE medium rather than a generic VOS ansatz; and (b) the sub-leading tilt.
Not gated on any run.

## Sources

[Kibble 1976] (defect formation and the one-scale picture); [Martins–Shellard 1996, 2002]
(the velocity-dependent one-scale model; network scaling as an attractor); [Vinen 1957] /
[Volovik 2003] (superfluid vortex-tangle dynamics under mutual friction — the overdamped branch).
Internal: [PRTOE_THE_CHAIN.md](../PRTOE_THE_CHAIN.md) link 5,
[PRTOE_THE_AMPLITUDE.md](../PRTOE_THE_AMPLITUDE.md) §5,
[PRTOE_DERIVATION_HUNT.md](../PRTOE_DERIVATION_HUNT.md) §7.
