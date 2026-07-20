# Stability — the whole certificate set, in one place

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*A referee asks four questions of any dark-sector model before reading anything else: does the
scalar carry a ghost, does it carry a gradient instability, does it move gravitational waves off the
speed of light, and does it violate the equivalence principle. This page answers all four for the
configuration that is actually running.*

*It has to answer them **twice**, because the model has two sectors with completely different
stability stories: a condensate whose health is inherited from a canonical UV completion, and a
dark-energy floor operator whose health had to be earned on explicit certificates. The corpus also
holds a third certificate set belonging to a **superseded** object, and citing that one — the
obvious thing to do, since it is the most detailed — would describe conditions this model does not
have.*

## The short answer

The medium is a **canonical complex scalar** — Ψ with the minimal potential
V = m²|Ψ|² + λ|Ψ|⁴ — whose working description below the amplitude gap is the phase EFT of a
condensate at finite chemical potential (Son, hep-ph/0204199; see
[PRTOE_PHYSICS_DOMAINS.md](PRTOE_PHYSICS_DOMAINS.md) room 10). **Ghost-freedom is not a condition
this model satisfies; it is a property it inherits.** A canonical kinetic term has no
higher-derivative sector to produce an Ostrogradsky mode, and a phase EFT derived from a healthy UV
completion carries that health down with it. The sound speed of the phonon is the Bogoliubov speed,
positive throughout the condensed phase.

And gravity is unmodified: the medium's only coupling is geometry, so **c_T = 1 exactly**, with no
tuning and no cancellation. The GW170817 constraint that killed a generation of scalar-tensor models
is not a constraint this one has to survive — it never had a term that could violate it.

**That covers the condensate. It does not cover the dark-energy floor, which is where this model's
stability question is actually interesting** — see the next section.

## The floor operator, where the question is not trivial

The dark-energy floor is carried by a **(δK)² operator** — background-orthogonal, built on the
extrinsic curvature, and in the ghost-condensate family (Arkani-Hamed et al., hep-th/0312099). It
is a genuine higher-derivative term, it replaced a (□φ)² floor that BBN killed, and it operates
**about c_s = 0** — precisely the point where the gradient term vanishes and the higher-derivative
structure is what does the stabilising. **Nothing here is inherited; the operator had to earn
admission, and the corpus records it earning admission on three explicit certificates:**

- **Tensor silence, exactly.** δK vanishes on tensor modes to all orders because det(e^h) = 1, so
  **α_T = 0** identically. Not a bound, not a cancellation — the operator has no tensor coupling to
  suppress, which is why c_T = 1 survives the floor as well as the condensate.
- **Braiding frozen.** The scalar–tensor mixing (α_B face) is temporally frozen, μ − 1 ~ 4×10⁻²¹.
- **Foliation health.** Landau critical velocity v_c = 0, which dissolves caustics into interference
  rather than letting the preferred slicing develop the pathology this operator class is known for.

**One thing that is *not* in the model, and is worth naming because it recurs as a proposed repair.**
A second, independent (δg⁰⁰)² operator would resurrect an observability claim the corpus killed —
and the corpus is explicit that this is **a model extension, not a repair**: it breaks the one-term
taxonomy and would owe its own three certificates. Within the minimal model the kill is final. If a
reader sees the DE floor's observability argued back to life, the first question is whether a second
operator was quietly added.

**So the honest one-line summary is not "stability is trivial here".** It is: the condensate's health
is inherited from a canonical UV completion and needs no certificate; the floor's health is *earned*,
by three checks that are stated and were done.

## The certificates that belong to a different object

`PRTOE_v4_dCDF_derivation.md` §9.4–9.5 carries a genuine, explicit no-ghost / no-gradient proof:

- **No-gradient.** With x = w_kin/w₁ ∈ [0, 1], the sound speed is c_s² = w₁·x(1 − (1−x)/Δ), a
  downward parabola whose critical point x⋆ = (1 − Δ)/2 falls outside the physical range whenever
  **Δ ≥ 1**. c_s² is then monotonic in x with its minimum at the boundary, c_s² = 0, attained only
  as s → +∞. So Δ ≥ 1 is *sufficient* for c_s² ≥ 0 everywhere — global, not asymptotic.
- **No-ghost.** For k-essence, c_s² = P_X/(P_X + 2X·P_XX), and no-ghost requires
  ∂ρ/∂X = P_X + 2X·P_XX > 0 — which is the same condition that makes ρ an invertible function of X,
  i.e. the condition that lets "w(ρ)" mean anything at all. With the s ↔ X map built monotonic, both
  ∂ρ/∂X > 0 and P_X ≥ 0 hold together.

**These certify the v4 dCDF's P(X) branch, and that object is superseded.** The file says so at its
head. The derivation remains correct and is worth keeping — a P(X) sector *would* need exactly these
checks, and they were done properly rather than asserted by analogy. But **they are not this model's
stability argument**, and quoting them as though they were would suggest the current configuration
needs conditions it does not have.

## Equivalence principle and screening

The EP question is real, because a light scalar coupled to matter generically produces a fifth force.
This model's answer is structural rather than a screening mechanism bolted on: the census forbids a
direct coupling, so the medium reaches matter only through geometry, and composition-independence
follows from the same blindness. MICROSCOPE's η = (−1.5 ± 2.7)×10⁻¹⁵ is cleared, and the sector is
held to it permanently — a measured EP violation falsifies the census outright.

**The screening margin is a prediction, not a null, and that distinction is the interesting part.**
The Vainshtein estimate clears the Hui–Nicolis argument with roughly five orders in hand, which the
corpus is careful to record as a **band rather than a zero**: a solar-system residual at or below
10⁻⁵ of current bounds. The model therefore does not say "no fifth force ever"; it says where the
residual sits, which is a thing an experiment can go and fail to find. Homes:
[PRTOE_classical_gravity.md](PRTOE_classical_gravity.md),
[PRTOE_interaction_map.md](PRTOE_interaction_map.md),
[PRTOE_direct_detection.md](PRTOE_direct_detection.md),
[PRTOE_PHYSICS_DOMAINS.md](PRTOE_PHYSICS_DOMAINS.md).

## Lorentz violation

Priced rather than assumed absent: [PRTOE_LV_pricing.md](PRTOE_LV_pricing.md).

## What is *not* certified here, stated so it is not mistaken for silence

- **λ_dyad's radiative stability** is a separate question from ghost/gradient stability — it asks
  whether the quartic survives quantum corrections, not whether the kinetic term is healthy. Tracked
  in its own place ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §4).
- **The conversion channel's perturbation treatment** is an open theory item and is the one
  stability-adjacent gap the model genuinely carries. The dark fluid's own perturbation sector is
  built and integrated (see [PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md)); the channel that
  converts between sectors is what lacks a full treatment.
- **The full-cycle behaviour past the turn** is STORY grade, not certified
  ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7 and its addendum).
