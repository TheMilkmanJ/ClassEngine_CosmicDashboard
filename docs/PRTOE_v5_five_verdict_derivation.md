# The Five-Verdict Derivation (task #11) — working document

**Status: FRAMEWORK (2026-07-07). No verdict is issued in this revision.**
Per red-team turn 22 (binding): five separately-worked sections sharing
one framework, each verdict's chain visible from assumption to number —
built slowly, so a cold read can convict one step without acquitting the
other four. This document accumulates the derivation; verdicts are
stamped only when their section is complete.

## 0. What this calculation decides (the load)

One derivation — the nonlinear two-fluid sector of the dCDF medium with
the admissible (δK)² operator — carries five verdicts:

| # | verdict | decides |
|---|---|---|
| V1 | soliton core-mass slope vs Schive | fingerprint, or FDM-by-another-route |
| V2 | granule heating rate vs Eridanus II | small-scale discriminator lives or dies |
| V3 | granule spectrum reshaping by the normal component | whether V1/V2 can differ from FDM at all |
| V4 | structure-funded floor amplitude + Bianchi withdrawal | P-2026-003's conditional fingerprint |
| V5 | can the caustic structure support a Θ-type coupling | R1's life (consistency-construction → physics, or death) |

Red-team standing note (turn 10, adopted): V1–V3 are **three readouts of
one question** — does the nonlinear sector reduce to pure
Schrödinger–Poisson (FDM), or does the normal component (the one
ingredient FDM does not have) reshape the granule statistics? Identical
→ inherit FDM's heating bounds, cores die at the Eridanus II knife,
§4.2 degeneracy becomes permanent. Different → fingerprint and survival
in one stroke.

## 1. Recovered foundations (certificate-grade inputs, prior sessions)

These are the derived results this calculation stands on, with their
provenance; none is re-litigated here:

- **F1 (cert 3, exact):** the (δK)² operator is trace-only; gravitons
  are traceless; det(e^h)=1 ⇒ δK vanishes on tensors to all orders.
  c_T = 1 identically. The operator cannot see gravitational waves.
- **F2 (cert 2, scaling grade):** the induced particle mass is
  **epoch-independent** — the H² in the kinetic normalization cancels
  against the operator's. (Load-bearing for V1: without this, the
  soliton scale would drift with redshift and no Schive comparison
  would be possible.) Linear-scale leakage suppressed by powers of
  k/k_J: braiding 10⁻³ at k=0.2/Mpc, dispersion 10⁻⁶. GC dictionary:
  M₂ = 9.4 eV (X₀ cancels); braiding scales split — 0.87 kpc
  spatially, frozen temporally (accumulated μ−1 ≈ 4×10⁻²¹).
- **F3 (cert 1, Landau):** the ideal condensate's critical velocity is
  zero; every infall flow is supercritical and sheds excitations;
  caustics never form — they dissolve into de Broglie interference
  (~kpc at dwarf velocities: the granules SP simulations show).
  Stamped caveat: interference nodes are quantized vortex lines
  (shift-charge, O1) where the foliation degenerates — measure-zero
  EFT boundary, handled by the covariant completion.
- **F4 (boundary stamp):** the two-fluid correspondence is kinematic
  and compositional, NOT thermodynamic — the medium is collisionless
  and never thermalizes; no second sound, no counterflow degree of
  freedom. Any "heating" must be gravity-mediated.
- **F5 (EFT domain):** cutoff at the condensate scale — wavelengths
  below ~20 nm are outside the theory's definition. All five verdicts
  live at astrophysical scales, comfortably inside.
- **F6 (the price already posted):** the same excitation-shedding that
  dissolves caustics heats; ultra-faint-dwarf survival (Eridanus II's
  cold star cluster) bounds it — pure-FDM analyses give m ≳ 3×10⁻¹⁹ eV
  (contested relaxation modeling), which would shrink cores below a
  parsec. The fork is live and is exactly what V2/V3 must decide.

## 2. Shared framework (to be derived in full — the one set of equations
## all five verdicts read from)

**Target form:** the nonrelativistic reduction of
S = ∫√−g [M_pl²R/2 + P(X) + (m̄₂²/2)(δK)²] + S_m
about the condensate background, yielding:

1. a Schrödinger–Poisson sector for the coherent field ψ (condensate)
   with effective mass M (epoch-independent per F2) and NO quartic
   self-coupling at leading order (ideal condensate; c_s² = 0);
2. a kinetic sector for the incoherent excitations (the "normal"
   component): the a⁻⁶ pre-basin remnant PLUS the in-situ population
   shed by supercritical flow (F3) — its phase-space distribution
   f(x, k, t) sourced by a Landau-shedding emissivity to be derived;
3. the coupling between them: gravity only (F4), plus the kinematic
   composition constraint (both are pieces of one field — no
   independent counterflow).

Derivation steps owed (in order; each gets its own subsection when done):
- 2.1 DONE below.

### 2.1 The effective particle, derived (2026-07-07)

**Step 1 — fluctuation Lagrangian.** Expand φ = φ₀(t) + π about the
condensate (X₀ = ½φ̇₀², P_X(X₀) = 0). Then
δX = φ̇₀π̇ + ½π̇² − (∇π)²/2a², and to quadratic order

  L₂ ⊃ ½P₂(δX)² → P₂X₀ π̇².

The would-be gradient term P_X·(−(∇π)²/2a²) **vanishes identically at
the extremum** — this is c_s² = 0 seen in fluctuation variables, and
it carries a structural consequence stated now because V3 leans on it:
*every bit of spatial stiffness in this medium belongs to the (δK)²
operator; none of it to the fluid.* The granule physics is entirely
the completion's.

**Step 2 — the operator's gradient energy.** For the perturbed
constant-φ foliation, δK = −∇²π/(a²φ̇₀) at leading order, so

  (m̄₂²/2)(δK)² = (m̄₂²/4X₀) (∇²π)²/a⁴.

**Step 3 — canonical normalization and dispersion.** With
π_c = √(2P₂X₀) π:

  L₂ = ½π̇_c² − [m̄₂²/(8P₂X₀²)] (∇²π_c)²/a⁴
  ⟹ ω = [m̄₂/(2√P₂ X₀)] k² ≡ k²/(2M_eff),
  **M_eff = √P₂ X₀ / m̄₂.**

Manifestly **epoch-independent** (P₂, X₀, m̄₂ are constants of the
action) — F2's covariant H²-cancellation appears automatically in
these variables; the two derivations agree.

**Step 4 — the basin-entry identity collapses it.** The atlas identity
ρ(basin entry) = 2P₂X₀² = 2M₂⁴ gives M₂⁴ = P₂X₀², hence

  **M_eff = M₂²/m̄₂**   (X₀ cancels — the FOURTH time this model's
  algebra has protected an observable from its one tuned parameter).

**Step 5 — numbers and consistency checks** (script:
`derivation_battery.py` lineage, run 2026-07-07):
- With M₂ = 9.4 eV: M_eff = 88.4 eV²/m̄₂. The astrophysically
  interesting window maps to **m̄₂ ∈ 10¹¹–10¹⁵ GeV** — the
  intermediate/GUT band (M_eff = 2×10⁻²¹ eV ↔ m̄₂ = 4.4×10¹³ GeV).
  The completion operator's coefficient sits at a natural UV scale;
  it did not have to.
- λ_dB(M_eff = 2×10⁻²¹ eV, v = 10 km/s) = 0.60 kpc — matches cert 1's
  "~kpc granules at dwarf speeds" independently.
- Quantum-pressure Jeans scale at today's mean density: 299/Mpc at
  2×10⁻²¹ eV (67/Mpc even at 10⁻²² eV) — the S8-mute claim
  (k_J ≥ 5.5/Mpc) holds with two orders of margin.

**What 2.1 hands the verdicts:** V1 reads M_eff = M₂²/m̄₂ (one free
number m̄₂ ⇒ the entire FDM-equivalent phenomenology, epoch-fixed);
V3 reads Step 1's structural fact (granules are pure completion);
V5 will read Step 2's δK-to-π map when the caustic-bit question is
posed in these variables.
- 2.2 The shedding emissivity: rate of energy transfer from coherent
  infall to incoherent excitations at a would-be caustic (Landau
  criterion with v_c = 0); this is the NEW object no FDM paper has.
- 2.3 The granule statistics: interference speckle field of ψ (standard
  SP) perturbed by the incoherent bath — the V3 kernel.
- 2.4 ⟨(δK)²⟩ from the nonlinear velocity field: the funded-floor
  source integral over Δ²(k, z) — the V4 kernel — and the Bianchi
  bookkeeping for the withdrawal.
- 2.5 The caustic-bit operator: is Θ(shell-crossed) expressible in the
  EFT's variables (vortex-line density / interference contrast), or
  does it require information the medium does not carry? — the V5
  kernel. Sharpened form: R1 needs a field-local object that is ~0 in
  laminar regions and ~1 (saturated, environment-independent) inside
  any multistreamed region, stable over Gyr. Candidate: the vortex-line
  density per de Broglie volume (quantized, hence naturally step-like);
  the derivation must show saturation, or R1 dies by the same
  continuous-coupling knife that forced binarity in the first place.

## 3. Verdict sections (empty until their derivations are complete)

### V1 — core-mass slope: NOT YET DERIVED
### V2 — heating vs Eridanus II: NOT YET DERIVED
### V3 — granule reshaping: NOT YET DERIVED
### V4 — funded-floor amplitude + withdrawal: NOT YET DERIVED
### V5 — the caustic bit: NOT YET DERIVED

*Backdrop transferring unconditionally: Lyman-α. External judges: the
red team reads each section cold, per-verdict, when stamped.*
