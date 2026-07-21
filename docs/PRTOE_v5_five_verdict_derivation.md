# The Five-Verdict Derivation (the working docket) — working document

> *Some statuses in this file may be superseded by later work; the current conditionality of every claim is tracked in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


**Status: COMPLETE (2026-07-07) — all five verdicts STAMPED (§3), the V4 step-walk
run and CLEARED (§4, the reviewer's registration recorded verbatim).** Binding: five
separately-worked sections sharing one framework, each verdict's chain visible from
assumption to number — built so a cold read can convict one step without acquitting the
other four. The header's original working rule (verdicts stamped only when their section
completes) was honored: every stamp below carries its chain.

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

Standing note: V1–V3 are **three readouts of
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
- **F4 (boundary stamp):** in this leading-order small-scale reduction
 the two-fluid correspondence is kinematic and compositional, NOT
 thermodynamic — the coherent condensate ψ and its shed normal
 component are pieces of ONE field, gravity-coupled, with the quartic
 collision channel 1/X₀-suppressed, so no independent thermodynamic
 counterflow or collisional second-sound exchange operates between
 them and any granule "heating" must be gravity-mediated (this is the
 scope that lets V1–V3 inherit the FDM/DK bounds). "Collisionless" is
 that microscopic-collision statement; it does NOT deny the medium's
 own thermal modes elsewhere — the velocity-ladder second sound
 (√α·c, the entropy wave — [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md)
 §1) and the real counterflow of other regimes: the fountain-effect
 thermal counterflow while T ≠ 0
 ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md)),
 the ψ–χ two-condensate counterflow with its independent vortex
 tangles (Room 5), and the Vinen-class mutual-friction turbulence of
 granulated halos (the two-fluid factor p²+q² that funds V5's ε-meter).
- **F5 (EFT domain):** cutoff at the condensate scale — wavelengths
 below ~20 nm are outside the theory's definition. All five verdicts
 live at astrophysical scales, comfortably inside.
- **F6 (the price already posted):** the same excitation-shedding that
 dissolves caustics heats; ultra-faint-dwarf survival (Eridanus II's
 cold star cluster) bounds it — pure-FDM analyses give m ≳ 3×10⁻¹⁹ eV
 (contested relaxation modeling), which would shrink cores below a
 parsec. The fork is live and is exactly what V2/V3 must decide.

## 2. Shared framework (the one set of equations all five verdicts read from)

**Target form:** the nonrelativistic reduction of
S = ∫√−g [M_pl²R/2 + P(X) + (m̄₂²/2)(δK)²] + S_m
about the condensate background, yielding:

1. a Schrödinger–Poisson sector for the coherent field ψ (condensate)
 with effective mass M (epoch-independent per F2) and NO quartic
 self-coupling at leading order (ideal condensate; c_s² = 0);
2. a kinetic sector for the incoherent excitations (the "normal"
 component): the a⁻⁶ pre-basin remnant PLUS the in-situ population
 shed by supercritical flow (F3) — its phase-space distribution
 f(x, k, t) sourced by a Landau-shedding emissivity (§2.2: ε ~ ρ M_eff v⁴/ħ);
3. the coupling between them: gravity only (F4), plus the kinematic
 composition constraint (both are pieces of one field — no
 independent counterflow).

The derivation steps, in order, each with its own subsection:
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

 **M_eff = M₂²/m̄₂** (X₀ cancels — the FOURTH time this model's
 algebra has protected an observable from its one tuned parameter).

**Step 5 — numbers and consistency checks** (script:
`derivation_battery.py` lineage, run 2026-07-07; scratch-era, not retained):
- With M₂ = 9.4 eV: M_eff = 88.4 eV²/m̄₂. The astrophysically
 interesting window maps to **m̄₂ ∈ 10¹¹–10¹⁵ GeV** — the
 intermediate/GUT band (M_eff = 2×10⁻²¹ eV ↔ m̄₂ = 4.4×10¹³ GeV).
 The completion operator's coefficient sits at a natural UV scale;
 it did not have to.
- λ_dB(M_eff = 2×10⁻²¹ eV, v = 10 km/s) = 0.60 kpc — matches cert 1's
 "~kpc granules at dwarf speeds" independently.
- Quantum-pressure Jeans scale at today's mean density: 299/Mpc at
 2×10⁻²¹ eV (67/Mpc even at 10⁻²² eV) — the S₈-mute claim
 (k_J ≥ 5.5/Mpc) holds with two orders of margin.

**Addendum (2026-07-07 evening) — the X₀-free form: the whisper
answered.** Define the field in clock units, ξ = φ/√(2X₀) (the
condensate ticks at unit rate: ξ̇₀ = 1). The action collapses to

 **P = ½M₂⁴((∂ξ)² − 1)² + (m̄₂²/2)(δK)²**

— X₀ is eliminated, not hidden: the theory has exactly TWO scales,
M₂ (potential depth, 9.4 eV) and m̄₂ (stiffness, GUT band). The four
X₀ cancellations were the artifact of writing a clock in the wrong
field units. This is the canonical ghost-condensate form
(independently confirming the dictionary), and it makes the
hinge MANIFEST: M₂ is the potential's own depth — visibly pinned,
not a dial. The model's true variables: a unit-tick khronon and two
scales.

**What 2.1 hands the verdicts:** V1 reads M_eff = M₂²/m̄₂ (one free
number m̄₂ ⇒ the entire FDM-equivalent phenomenology, epoch-fixed);
V3 reads Step 1's structural fact (granules are pure completion);
V5 will read Step 2's δK-to-π map when the caustic-bit question is
posed in these variables.
- 2.2 DONE below.

### 2.2 The shedding rate (2026-07-07)

**Step 1 — where shedding can and cannot happen.** Landau with
ω = k²/2M_eff: a flow of speed v may emit modes with k < 2M_eff v —
the critical velocity is zero (cert 1/F3). But Galilean invariance
protects HOMOGENEOUS superflow: with no momentum sink, uniform flow
cannot shed. Shedding requires flow gradients; the would-be caustic —
where gradients diverge — is where it happens. (This is why the
background cosmology never sheds: the Hubble flow is locally uniform;
the medium granulates only inside collapsing structure. V4's
structure-gating is this fact restated.)

**Step 2 — the rate.** At a forming caustic, compression is halted by
the k⁴ quantum pressure at the de Broglie scale l_dB = 2πħ/(M_eff v);
the coherent stream self-interferes and converts over the transit
time of that region:

 **t_shed ~ ħ/(M_eff v²)** ; emissivity ε ~ ρv²/t_shed = ρ M_eff v⁴/ħ.

Heavier ripple-particles granulate faster (ε ∝ M_eff).

**Step 3 — the regime boundary (a correction the numbers forced).**
The rate law splits halos into two regimes, and the split IS the
known phenomenology:
- **Granular regime (R ≫ l_dB):** t_shed ≪ t_dyn (MW at 2×10⁻²¹ eV:
 t_shed ~ 10⁴ yr vs t_dyn 250 Myr; even dwarfs at that mass: 9 vs
 100 Myr) — virialized halos complete granulation within a fraction
 of a dynamical time. SP simulations observe this; here it is a
 derived rate.
- **Coherence-patch regime (R ≲ l_dB):** at 10⁻²² eV a dwarf (R ~ 3
 kpc) sits INSIDE one de Broglie patch (l_dB ~ 12 kpc) — granulation
 cannot complete and the object is a single coherent lump: the
 soliton core. The same rate law yields the granule field, the
 soliton regime, AND the boundary between them (R ~ l_dB), with no
 additional input.

**Step 4 — structural pre-load for V1–V3 (flagged here, stamped only
in their own sections).** In halos today: c_s²(halo) ≲ 10⁻²² (the §2
residual), quartic self-interactions suppressed by 1/X₀, pre-basin
normal remnant diluted to irrelevance (a⁻⁶ since z ~ 10⁵). The
leading-order nonlinear sector is therefore EXACTLY Schrödinger–
Poisson with mass M_eff — the same equations the FDM literature
simulates. Unless the listed subleading terms intervene at observable
level, the core-mass relation (V1), granule statistics (V3), and
heating rates (V2) transfer from that literature with m → M_eff. The
honest possible outcome that V1–V3 must confront: FDM-by-another-
route, with the model's distinctive content living only in V4 (the
funded floor — FDM has no such operator) and V5 (the caustic bit).
- 2.3 DONE below.

### 2.3 Granule statistics — and the caustic bit found (2026-07-07)

**Step 1 — the speckle law.** A granulated halo is many random-phase
SP modes: ψ is a Gaussian random field, so ρ = |ψ|² is EXPONENTIALLY
distributed — order-unity density contrast is structural, not
incidental (P(ρ > 3ρ̄) = 5%). Granule size l_dB, coherence time
l_dB/σ_v. Per 2.2's pre-load this transfers from the FDM literature
with m → M_eff; no reshaping by the (dead) remnant. Quasiparticle
masses (V2's heating flywheel): ~10⁶ M☉ lumps in dwarfs at
2×10⁻²¹ eV; ~30 M☉ at the solar radius.

**Step 2 — THE V5 GEM: the caustic bit exists as mathematics.**
The nodal lines of a Gaussian random wave are quantized vortex
filaments with UNIVERSAL statistics (Berry & Dennis, Proc. R. Soc. A
456, 2059 (2000), doi:10.1098/rspa.2000.0602 — cite-verified
2026-07-07; 3D tangle statistics: Taylor & Dennis, arXiv:1410.0383):
line length per volume L_v = O(1)/l_dB². Therefore the
dimensionless object

 **Θ ≡ L_v · l_dB²**

is the same O(1) number in EVERY granulated region — independent of
halo mass, density, epoch, or environment — and exactly ZERO in
laminar flow (an unbroken ψ has no nodal tangle). This is precisely
the saturated, environment-independent, binary attribute R1's forced
binarity demanded (the "can the caustic structure support a
Θ-type coupling" question): granulation happened ⇒ Θ ≈ 1 universally;
never-crossed ⇒ Θ = 0. The quasar wall's uniformity requirement is
met BY the universality of random-wave vortex statistics — not by
tuning. **The local operator 2.5 supplies:** Θ_loc = Q/(Q+K), with
Q = |∇√ρ|² and K = ρ|∇S|² — built from both of the readings the
construction had to choose between (phase-gradient variance and
vortex-core density), and verified numerically at 512² (a 0.496
plateau against 1.9×10⁻⁶ laminar). The statistical object and the
coupling construction are both in hand; R1's life turns on its sims.
- 2.4 DONE below. - 2.5 DONE below.

### 2.4 The funded floor, locked to the core scale (2026-07-07)

**Step 1 — the source.** δρ_floor = (m̄₂²/2)⟨(δK)²⟩ with δK the
structure-induced expansion fluctuation. Volume-weighted census:
quasi-linear velocity-divergence variance ⟨θ²⟩ ~ (H f σ)² ~ O(1)H₀²,
plus virialized interiors ((σ_v/R)² ~ 10²H₀² over volume fraction
~mass/Δ_vir ~ 2×10⁻³ → ~0.5H₀²). Total: **⟨(δK)²⟩ = αH₀², α ≈ 2**
(order-of-magnitude grade; grows ∝ growth² — P-2026-003's time-shape).

**Step 2 — the lock.** The SAME m̄₂² sets both the floor funding and
(via 2.1) M_eff = M₂²/m̄₂. Substituting:

 **ν ≡ δρ_floor/ρ_c = (4πα/3)·(M₂²/(M_eff·M_Pl))²**

— a zero-free-parameter relation between the drift amplitude and the
core scale. Numbers (α = 2): M_eff = 2.9×10⁻¹⁹ eV → ν = 5×10⁻¹⁵;
2×10⁻²¹ → 1.1×10⁻¹⁰; 8.8×10⁻²³ → 5.6×10⁻⁸.

**Step 3 — THE MUTUAL-EXCLUSION THEOREM (and a correction).** A
DESI-visible drift (ν ~ 10⁻³) requires m̄₂ = 1.3×10¹⁷ GeV ⇒
M_eff = 6.6×10⁻²⁵ eV ⇒ l_dB(200 km/s) ≈ 91 kpc — galaxies could not
exist. **Observable drift and observable cores are mutually exclusive;
LSS kills the deep hierarchy outright.** This SUPERSEDES the earlier
scaling-grade claim that the deep end (x₀ ~ e⁻⁴³) was "DESI-scale" —
that estimate did not carry the m̄₂–M_eff lock. Consequences: the
two-sided x₀ window's lower (chalk) wall is replaced by a brick one
(LSS); P-2026-003's fingerprint resolves to its "absent/below
detection" branch — the mechanism stands, sign-locked phantom, at
ν ≤ 10⁻⁸ in the structure-allowed range: invisible to any foreseeable
w-measurement. **Step 4 — withdrawal:** fractional growth drag
~ ν/Ω_m ≤ 10⁻⁸ — clears RSD by ~7 orders; rider (i) trivially
satisfied. An honest self-kill of our own conditional fingerprint,
by our own locked relation.

### 2.5 The local caustic-bit operator — constructed and verified (2026-07-07)

**Step 1 — construction.** Madelung variables (ρ, S). Define the
local, dimensionless, bounded scalar

 **Θ_loc = Q/(Q+K)**, Q = |∇√ρ|², K = ρ|∇S|² (common 1/L² units)

— the pointwise fraction of gradient energy carried by amplitude
structure vs flow. Laminar flow: Q/K ~ (l_dB/R)² → Θ_loc ≈ 0.
Speckle: circular-Gaussian equipartition puts amplitude and phase
gradients at the same scale → Θ_loc saturates at a universal O(1)
value set by Gaussian statistics alone (Berry-class universality —
scale-free by construction of the ratio).

**Step 2 — numerical verification (512², random-wave fields).**
Granulated: mean Θ_loc = 0.496 (median 0.493). Universality check
(k ×3.3, modes ÷4): 0.459 — same plateau, different speckle. Laminar
control: **1.9×10⁻⁶**. Six orders of separation, saturation confirmed,
environment-independence confirmed at the few-percent level.

**Step 3 — verdict input and caveats.** The caustic bit IS expressible
as a local operator in the EFT's own variables: R1's forced binarity
has a mechanism (couple m_e to Θ_loc; every lab/absorber sits at the
plateau, every laminar region at zero — the quasar uniformity is a
property of Gaussian statistics, not tuning). Caveats stamped:
(i) m_e(Θ_loc) is a NON-POLYNOMIAL coupling (ratio of gradients) —
EFT-exotic, UV story owed, same debt-class as κ_v; (ii) transitional
environments (collapsing but not yet granulated) take intermediate
values — all currently measured environments are deep-plateau;
(iii) the plateau's few-percent spread (0.46–0.50) propagates to a
few-×10⁻⁴ spread in m_e across environments — safely below the 10⁻⁷
molecular bounds? NO: 3×10⁻⁴ ≫ 10⁻⁷ IF absorber speckle statistics
differ systematically from lab-region statistics. FLAGGED as the
remaining quantitative kill-test for R1: the plateau's universality
must hold at the 10⁻⁵ level between halo environments, which the
512² test cannot resolve. R1 survives the EXISTENCE test; it now owes
a PRECISION test.

## 3. The five verdicts — STAMPED (2026-07-07; grades marked)

### V1 — core-mass slope: NO FINGERPRINT (inherited; derivation grade)
Chain: 2.1 (M_eff = M₂²/m̄₂, epoch-independent) + 2.2 Step 4 (leading-
order nonlinear sector = SP exactly; c_s² residual ≤ 10⁻²², quartics
1/X₀-suppressed, remnant dead). The soliton/core physics is
Schrödinger–Poisson with mass M_eff: **the core-mass relation is
Schive's, unmodified.** dCDF at the core scale is FDM-by-another-route;
the §4.2 discipline extends to the small-scale sector.

### V2 — heating vs Eridanus II: KNIFE INHERITED (fork on contested literature)
Chain: 2.3's granule masses (~10⁶ M☉ lumps in dwarfs) + V1's
FDM-equivalence ⇒ the ultra-faint-dwarf heating bounds apply to M_eff
verbatim. If the Dalal–Kravtsov-class analyses hold: M_eff ≥ 3×10⁻¹⁹
eV ⇒ m̄₂ ≤ 3×10¹¹ GeV ⇒ cores < 1 pc ⇒ **the small-scale
discriminator is dead and the model reverts to the pure dyad
(§4.2 permanent).** If their relaxation modeling fails scrutiny
(contested), a window at M_eff ~ 1–3×10⁻²¹ eV with 60–200 pc cores
survives. The verdict is the fork itself, stated without preference.

### V3 — granule reshaping: NONE (derivation grade)
Chain: the pre-basin remnant is diluted by a⁻⁶ since z ~ 10⁵ (7×10⁻⁵
of its BBN value by recombination; nothing today); the in-situ
"normal component" IS the granule field (2.2); interactions
1/X₀-suppressed. **The granule spectrum is pure SP speckle —
exponential statistics, identical to FDM.** The one ingredient FDM
lacks contributes nothing observable here; V1–V3 close as a package:
no small-scale fingerprint distinguishes dCDF from FDM at mass M_eff.

### V4 — funded floor: MUTUAL-EXCLUSION THEOREM; fingerprint ABSENT (locked relation derived)
Chain: 2.4 in full. ν = (4πα/3)(M₂²/(M_eff M_Pl))² — cores and
observable drift are mutually exclusive; LSS bricks the deep end;
ν ≤ 10⁻⁸ in the allowed range; withdrawal clears RSD by 7 orders.
**P-2026-003 resolves to its "absent" branch by derivation** —
registered in ANN-2026-008. The earlier "deep end is DESI-scale"
scaling claim is corrected on the record.

### V5 — the caustic bit: EXISTENCE PASSED, precision test DISCHARGED by theorem (constructed + numerically verified)
Chain: 2.3 Step 2 (Θ universal by random-wave theory) + 2.5 in full
(Θ_loc constructed; plateau vs 1.9×10⁻⁶ laminar). **R1 survives its
internal test**: the medium's caustic structure supports a Θ-type coupling.

**The plateau universality is now settled analytically** ([scripts/r1_caustic_sim.py](../scripts/r1_caustic_sim.py),
[working_logs/PRTOE_R1_caustic_precision.md](working_logs/PRTOE_R1_caustic_precision.md)). In this
medium the critical velocity is zero, so classical caustics wave-regularise into de Broglie speckle
threaded by a vortex tangle — the caustic bit is a random-wave *statistics* question, not a
ray-tracing one. For developed circular-Gaussian speckle Θ_loc = Q/(Q+K) is **Beta(d/2, d/2)-
distributed, so its mean is exactly ½** — independent of the power spectrum, σ_v, density, epoch,
dimension, and even anisotropy. Confirmed: the partition identity Q+K = |∇ψ|² to 9×10⁻¹⁶, the 3D
pointwise variance 0.06253 against 1/16, the vortex density 0.082 against Berry–Dennis 1/4π = 0.0796,
and an environment sweep that returns ½ everywhere. **The earlier "0.496/0.459 spread" was a
finite-developedness artefact** — cutting the speckle-cell count pulls ⟨Θ⟩ to 0.481 at ~4 cells and
it climbs to ½ by ~50–100 cells — not an environmental effect.

So the plateau meets the 10⁻⁵ requirement in the developed limit **by theorem, not resolution**,
under two structural conditions where any residual kill-test now lives: (a) the coupling responds to
a volume/line-of-sight **average** of Θ over many de Broglie cells (a realistic absorber column,
N_cells ~ 10⁹, sits below 10⁻⁵ with orders of margin; a *pointwise* coupling would scatter m_e by
the O(1) Beta variance and is excluded), and (b) the measured environments are deep-developed, not
soliton-core or strongly laminar (⟨Θ⟩ ≈ ½ − 0.155·f in the residual-laminar fraction f). What stays
owed is only the non-polynomial coupling's UV story; the direct central-limit narrowing to 10⁻⁵ is
written into the sim's deferred production run (~6×10⁸ cells), but the exactness that delivers it is
the Beta law, which is settled.

*Lyman-α transfers unconditionally as backdrop. All five stamped;
the review reads cold, per-verdict, per the standing conditions.*

## 4. V4 STEP-WALK (the reserve — every O(1) skeleton exposed)

The reviewer reserved V4 pending a step-walk of the m̄₂–M_eff lock and
the α coefficient. Here is the walk, with the conventions and the one
undercount surfaced by us before the walk was read.

**Step A — the lock's two powers (structural, not adjustable).**
(A1) The operator is, by definition, (m̄₂²/2)(δK)² — its contribution
to any coherent expansion-fluctuation energy is ∝ m̄₂². Not a choice;
the operator's name. (A2) The dispersion (2.1 Steps 2–3): the same
coefficient supplies the ONLY gradient term, giving
ω = [m̄₂/(2√P₂X₀)]k², hence M_eff = √P₂X₀/m̄₂ ∝ 1/m̄₂. Power fixed by
the operator being the sole k⁴ source at a P_X = 0 extremum. (A3)
Therefore ν ∝ m̄₂² = (M₂²/M_eff)² — the mutual exclusion needs only
these two powers. **Any un-kill requires changing a power, i.e.
changing the theory.**

**Step B — the O(1) skeletons, exposed.** (B1) Basin-entry convention:
ρ_entry at x = 1 including the quadratic term is 3.5·P₂X₀², not 2 —
the identity's "2" is the linear-term convention. Skeleton: ×1.75 in
M₂⁴'s definition. (B2) δK foliation normalization: the δK = −∇²π/(a²φ̇₀)
leading form may carry a √2 vs the covariant treatment — skeleton: ×2
in ν. (B3) α: the quasi-linear + halo-scale census gives α ≈ 2; we
stress it to 100. Worst-case stack: ×175 ⇒ ν(quasi-linear) ≤ 1.9×10⁻⁸.

**Step C — the undercount we surface ourselves.** The 2.4 first pass
counted δK at halo scale (σ_v/R). Inside granulated regions the
medium's own flow varies at l_dB, giving δK ~ M_eff v²/2πħ — 240 H₀
in dwarfs, ~10⁵ H₀ in MW interiors. A naive m̄₂²(δK)² with these
values exceeds halo energy budgets by orders — which is a
NORMALIZATION DIAGNOSIS, not a discovery: for on-shell granule modes
the operator term is part of the mode energy, capped by equipartition
at the granule kinetic energy ρv². Cap: ρ_halo v² ~ 10⁻¹⁵ eV⁴;
cosmic-averaged ≤ 7×10⁻⁸ ρ_c; and — decisive for the verdict — this
piece is LOCALIZED: it rides with halos as a ~4×10⁻⁷ fractional
halo-mass correction. Localized energy is halo mass, not smooth
dark energy: it cannot masquerade as w-drift at all.

**Step D — conclusion of the walk.** Under every prefactor stack the
smooth component is ≤ 2×10⁻⁸ ρ_c and the large local piece is not
drift. Un-killing the fingerprint needs ν ~ 10⁻³: a factor ≥ 5×10⁴
beyond the worst-case stack, unreachable by prefactors, reachable
only by breaking Step A's powers. **The mutual-exclusion theorem and
the ABSENT resolution of P-2026-003 stand with ≥ 4 orders of margin.**
The reviewer's conviction or acquittal follows this section.

**Step E — THE TRUE HINGE (found on review; the walk's
verdict: CLEARED).** The substitution ν = (4πα/3)(m̄₂/M_Pl)² shows ν
depends on m̄₂ ALONE while M_eff = M₂²/m̄₂ depends on m̄₂ AND M₂ — so
Step A's "two powers" were a symptom, not the cause: the mutual
exclusion is enforced by exactly one fact, **M₂ is PINNED**
(M₂⁴ = X₀²P₂ — in k-essence the (δg⁰⁰)² coefficient is a background
quantity ~X²P_XX fixed by the completion, and the one-term taxonomy
admits only (δK)² as the added free operator). If M₂ were free, drift
and cores would coexist with no power broken. The reviewer
interrogated the pin and could not open it. **Registered precisely,
in the reviewer's words: the kill holds under M₂-pinned (single added
operator); it is un-killable ONLY by a second independent (δg⁰⁰)²
term — a MODEL EXTENSION that breaks the one-term taxonomy and owes
its own three certificates (α_T, foliation, α_B). Within the
corroborated minimal model, the kill is final.** The turns-12/19
premature credit and the un-locked scaling that misled both sides are
corrected on the shared record: the math caught a shared error.
