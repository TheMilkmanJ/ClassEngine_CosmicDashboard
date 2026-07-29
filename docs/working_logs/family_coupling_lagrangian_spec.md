# The family-coupling Lagrangian — a specification, not a build (2026-07-28)

**Why this file exists.** Two live dockets are blocked on the same un-built object, and a third
now joins them:

- **#55** — derive c_w, the winding-response quadratic coefficient. Blocked: *"'leading-order
  dominates' is generic but not proved from the **un-built** family-coupling Lagrangian."*
- **#2 / the three-seed candidate** — what sets arg b. Blocked: no coupling of any external object
  to the ring is written anywhere, so the seeds' doublet-space vector has no components.
- **#1** — is the family stiffness matrix threefold degenerate before pinning? Answerable
  immediately once a Lagrangian exists; unanswerable without one.

> **⚠ THE FRAMING ABOVE OVER-CLAIMED THE BLOCKING — corrected 2026-07-29, one day later.** Two of
> those three were answered **without building anything**, using representation theory and counting:
>
> - **#1 is answered.** The degeneracy is *not* symmetry-protected — C₃ is abelian and S₃ has only
>   1, 1′, 2, so neither has a three-dimensional irrep; the node is the accidental degeneracy of a·𝟙.
>   The parent that works is SO(3) ≅ SU(2)/ℤ₂, and arg b is the **spin-2 / adjoint mixing angle**
>   (C12). "Unanswerable without a Lagrangian" was simply wrong.
> - **#2 is substantially advanced.** The phase-selecting term must be **parity-odd**, so the source
>   must be chiral (C13) — a hard exclusion — and three *distinct* seeds supply exactly that, with
>   identical seeds giving b = 0 exactly (C14). None of that needed a written coupling.
>
> **The lesson is worth more than the correction.** A specification of what an object must satisfy is
> also a specification of what its *consequences* must satisfy — and those can often be extracted by
> symmetry before the object exists. Assembling this list was not merely preparation for a build; it
> was most of the work. **Do not assume a docket is gated on construction just because it mentions an
> un-built object.**
>
> **What the Lagrangian is still genuinely needed for**, and this is now the honest short list:
> **(a)** c_w — that needs the *response function* coupling winding to mass, a different object from
> the family quadratic form (which C₃ + hermiticity already fix completely, at three real parameters);
> **(b)** the **value** of arg b, as opposed to its structure — the seeds' relative couplings are
> unknown, and C14 only converts the phase into a constraint on them; **(c)** whether the negative
> square-root branch the neutral triple appears to need is dynamically admissible.

Nobody has collected what the object must satisfy. The constraints are unusually tight and mostly
came from *closed* work, so this is assembly, not speculation. **A candidate Lagrangian can be
checked against this list before any effort is spent on its consequences.**

---

## What it must reproduce (each already established elsewhere)

**C1 — C₃ symmetry.** Three defects on a ring, equilibrium at 120°. The Lagrangian must be invariant
under cyclic relabelling f_j → f_{j+1}, equivalently f_j → ω^j f_j with ω = e^{2πi/3}.

**C2 — pair-harmonic defect interaction.** The defects interact as **r², not log and not 1/r**
(settled separately). This is not a modelling choice available to the builder; it is fixed.

**C3 — the normal-mode stiffnesses.** Three defects give 3 degrees of freedom, decomposing under C₃
into **one singlet + two degenerate doublet** modes with

> **k_S = 6, k_D = 3 — ratio exactly 2.**

Any candidate reproduces this ratio or contradicts recorded work.

> **⚠ C3 AND C7 ARE DIFFERENT OBJECTS — do not try to satisfy both with one ratio.** Added
> 2026-07-28 after nearly filing a false conflict. Running the instrument
> (`scripts/coulomb_ring_stiffness_ratio.py`) shows k_S and k_D are **Hessian eigenvalues in RADIAL
> displacements** — the breathing mode (1,1,1) against the shape modes (2,−1,−1) and (0,1,−1). They
> are **not** the circulant amplitude stiffnesses ε₀ = a + 2b and ε₁ = a − b that carry |b|/a.
>
> The trap is that ε₀/ε₁ = 2 would force **b/a = 1/4**, while Koide (C7) forces **|b|/a = 1/√2** — a
> 2.83× "conflict" that is entirely an artefact of identifying two different mode decompositions.
> A candidate must reproduce k_S/k_D = 2 **in the radial sector** and |b|/a = 1/√2 **in the amplitude
> sector**, and these are independent requirements on the same Lagrangian, not a contradiction.
>
> The instrument also reproduces the table's other rows (Coulomb → 8.0), so the definitions above are
> the operative ones.

**C4 — the quadratic sector is PHASE-BLIND, and must be.** The ring amplitudes are real
(f₂ = f₁*), so only the sum enters the energy:

> E = ε₀·f₀² + (ε₁ + ε₂)·|f₁|²,  with ε₁ + ε₂ = 2a − 2·Re b

which carries **no φ**. Verified to 9×10⁻¹⁵ at every arg b tested. A candidate whose quadratic part
depends on the phase is wrong — not incomplete, wrong.

**C5 — the cubic sees the phase, and only through cos 3φ.**

> Σ_k (√m_k)³ = 3M³ + (9/2)M R² + (¾) R³·cos 3φ

One harmonic, no other φ-dependence. Together with C4 this is a **theorem**: φ → φ + 2π/3 symmetry
plus evenness forces any real symmetric ring potential to be a function of cos 3φ alone, whose
stationary points are only 3φ = 0 and 3φ = π.

**C6 — therefore the phase CANNOT come from the Lagrangian's own potential.** The needed value is
3φ = Q = 0.6667, missing the nearer stationary point by 0.667 rad. So the Lagrangian must **admit an
external phase reference** — a coupling slot for something outside the ring. It does not have to
*supply* the phase; it must have somewhere for the phase to enter.

**C7 — the closure and Parseval, both exact, both automatic.**
> 3·arg f₁ = Q  and  Q = ⅓ + (2/3)|f₁/f₀|² = ⅓ + A²/6, A = 2|b|/a

Parseval is an identity (Q is just the variance of the √m about their mean), so a candidate cannot
violate it; the closure is the one dynamical relation and must be derivable, not imposed.

**C8 — the mass response must have an EVEN part in the rectified amplitude.** Writing the fractional
mass shift against the winding projection x = ε·cos θ,

> δm/m = |x| + c_w·x² + O(x³)

**c_w = 0 for any response that is odd in u = |x|** — `tanh u` and `u/√(1+u²)` both saturate and both
give exactly zero. Data brackets c_w in **[−2, 0]** (−1.80 fit-implied; −0.84 ± 0.52 ensemble). So the
Lagrangian must generate a response with a genuine even part, and land in that band.

**C9 — leading-order dominance must be a consequence, not an assumption.** The expansion parameter
is ε itself: the quadratic term is ~~0.83%~~ **0.985%** of leading and the cubic 0.0105%. A candidate
should make that fall out rather than be asserted. *(Quadratic corrected 2026-07-29 — the recorded
0.83% used the cubic's moment ratio 2/3 where the quadratic's π/4 belongs; the cubic is right. The
constraint is unaffected. Working in C16 below.)*

**C10 — family universality must be protected structurally.** Families differ in mass and mixing
only; their gauge charges are identical to high precision. The construction protects this if charges
are **topological** (winding numbers — integers, immune to continuous shape deformation) while masses
are energetic. A candidate that lets shape deformations move charges is excluded by precision data.

**C11 — the winding average.** ⟨|cos|⟩ = 2/π under equidistribution, with the turn budget securing
equidistribution to ~10⁻⁴%. The rectification (mass-positivity taking |x| rather than x) must come
from the Lagrangian, not be imposed by hand.

**C12 — the family-splitting order parameter is a UNIAXIAL SPIN-2 (nematic), and an adjoint is
excluded.** Added 2026-07-29 from #1; verified in `scripts/family_triplet_parent.py` (27 controls,
several exact to 0.00e+00). *(Count corrected 2026-07-29 — recorded as 15 by the control-count sweep
below, which found this and two others wrong.)*

The threefold degeneracy at b = 0 is real but **not protected by the ring's own symmetry**: C₃ is
abelian so all its irreps are one-dimensional, and S₃ has only 1, 1′ and 2. Neither has a
three-dimensional irrep, so the degenerate triple at the node is not an irreducible multiplet of the
ring — it is the accidental degeneracy of a·𝟙. A genuinely protected triplet requires a continuous
non-abelian parent, and **SO(3) ≅ SU(2)/ℤ₂ works**: the ring's C₃ is exactly the 2π/3 rotation about
the democratic axis (1,1,1), a subgroup of SO(3). So "three families = one SO(3) triplet, with C₃ the
residue after the configuration picks that axis" is consistent.

**But the object that breaks it cannot be an adjoint.** A stiffness matrix is a real *symmetric*
2-tensor, and under SO(3)

> **3 ⊗ 3 |_sym = 1 ⊕ 5** — a scalar and a spin-2, and nothing else.

The adjoint is the **3**, which lives entirely in the *antisymmetric* part and is orthogonal to every
symmetric matrix (verified: maximum overlap exactly 0). **An adjoint order parameter has nowhere to
sit in a stiffness matrix, at any order, for any coupling.** What does the splitting is the 5: the
ring's traceless stiffness is b·(J − 𝟙), eigenvalues b·(2, −1, −1), symmetry axis (1,1,1) — a
textbook uniaxial nematic. It breaks SO(3) → O(2) about that axis, giving 3 → 1 ⊕ 2, and the
**doublet degeneracy is protected by the residual continuous O(2)**, not merely by C₃ — which is why
the two shape modes are *exactly* degenerate rather than approximately so. Rotations about (1,1,1)
commute with the stiffness for every b (verified to 0.00e+00).

> **AMENDED within the hour, before this was relied on.** The paragraph above is a true statement
> about a **real** stiffness matrix — i.e. about **real b**. The physical point has arg b = 2/9 ≠ 0,
> where the family Hamiltonian H = a𝟙 + bP + b̄Pᵀ is complex **Hermitian**, not real symmetric.
> Traceless Hermitian 3×3 matrices are the **8** of SU(3), and **8 → 5 ⊕ 3** under SO(3). Written out:
>
> > H = a𝟙 + |b|·[ **cos φ**·(P + Pᵀ) + i·**sin φ**·(P − Pᵀ) ]
> > with (P + Pᵀ) = J − 𝟙 the **spin-2 nematic** and i(P − Pᵀ) the **adjoint**.
>
> The two pieces are orthogonal and independent (verified, overlap exactly 0). So the adjoint is
> **not excluded — it is relocated**, and **arg b is precisely the mixing angle between the spin-2 and
> adjoint components of one order parameter**, their amplitude ratio being tan(arg b) = 0.226 at the
> Brannen phase.

**What a candidate must now do.** Supply a family order parameter with **both** components: a spin-2
(rank-2 symmetric traceless) piece aligned with the democratic direction, which does the leading-order
splitting, **and** an adjoint piece whose weight relative to it is tan(arg b). The adjoint is not the
parent of the triplet and does not drive the splitting, but it cannot be omitted — with φ = 0 the
doublet stays exactly degenerate and there are only **two** distinct masses, not three.

**Why this matters for C6.** It supplies the structural reason the ring's own potential cannot fix the
phase. A real C₃-symmetric potential builds only the **symmetric** piece; the adjoint component is
**imaginary-antisymmetric** and is therefore invisible to that potential *at every order*. C6 was
established as a theorem about stationary points of cos 3φ; this says the same thing in
representation-theoretic terms, and explains it rather than merely establishing it.

**And note the relation to C4.** A real symmetric 2-tensor is automatically phase-blind in the
quadratic sector, so C4 is not an extra assumption but a consequence of the nematic component's
representation — which is also why C4 holds *exactly* (9×10⁻¹⁵) rather than approximately.

**C13 — the phase-selecting term must be PARITY-ODD, so the external object of C6 must be CHIRAL.**
Added 2026-07-29 from #2; verified in `scripts/arg_b_parity_odd_invariant.py` (11 controls, all pass,
including an anti-control and an independent double-angle cross-check).

C₃ relabelling acts on the Brannen phase as φ → φ + 2π/3, so a real C₃-invariant potential can depend
on φ **only** through cos 3φ and sin 3φ — nothing of lower order survives, since φ enters only via b³.
Reflection (reversing the labelling, b → b̄) sends φ → −φ, keeping cos 3φ and killing sin 3φ. Hence:

- **With reflection symmetry:** V = V(|b|, cos 3φ), whose stationary points in φ are *only* 3φ = 0 and
  3φ = π. This is **spec C6's theorem re-derived from the symmetry action** rather than from the mass
  formula — two independent routes to the same wall.
- **Without it:** a term μ·sin 3φ is allowed, and every stationary point obeys

> **tan(3·arg b) = μ / λ**

Combined with the holonomy closure 3·arg b = Q, the Koide value requires

> **μ / λ = tan Q = tan(2/3) = 0.786843**

**What this does NOT do, stated plainly: it does not derive arg b.** It trades an unsourced angle for
a ratio of two cubic couplings. That is progress only because the new unknown lives in a Lagrangian,
where it can be computed once the couplings are, instead of being a bare number with nowhere to come
from.

> **But it yields one hard exclusion, and that is the value here.** The sin 3φ term is odd under
> reflection, so a **reflection-symmetric background cannot generate it at any order with any coupling
> strength** — confirmed by anti-control, the phase stays pinned to 0 or π whenever μ = 0. **The
> external object C6 demands must be chiral.**
>
> **⚠ A LINK TO SAKHAROV THAT DOES NOT HOLD — checked 2026-07-29 and recorded so it is not drawn
> later.** Docket #69 needs a CP-violating ingredient, and it is tempting to read C13's parity-odd
> requirement as supplying it: arg b ≠ 0 makes the family Hamiltonian complex, and a complex phase in
> a mass matrix is the standard flavour-physics source of CP violation. **It does not follow, for two
> separate reasons.** First, the reflection here acts on the *family labels* — reversing the cyclic
> order of three ring sites — which is a discrete relabelling, not spacetime P, and still less CP.
> Second and decisively, **the spectrum is real for every arg b**: the eigenvalues a + 2|b|cos(φ +
> 2πk/3) are real by construction, verified across the range, so arg b is a *shape parameter of a real
> spectrum*, not a phase that survives into observables. A Jarlskog-type invariant needs the
> **mismatch of two matrices**, and only one is in play here. The chirality C13 demands is real and
> useful; it is **not** the Sakharov ingredient, and #69 gains nothing from it. This is a real filter on the owner's three-seed
> candidate: *if the seeds' imprint is reflection symmetric, it cannot supply arg b however it is
> coupled.* It also points at the model's own winding sector, which already carries a definite
> handedness — whether that chirality has the right *magnitude* is a separate computation and is not
> claimed.

**C14 — three DISTINCT seeds supply exactly the chiral source C13 demands, and distinctness is what
lifts the degeneracy at all.** Added 2026-07-29 from the owner's three-seed idea; verified in
`scripts/three_seeds_chirality_and_b.py` (10 controls including an anti-control).

Let the three seeds couple to the three ring sites with strengths g₀, g₁, g₂. Then b is the k = 1
discrete-Fourier component of that pattern, b ∼ Σⱼ gⱼ ω⁻ʲ — not an assumption, just what "the C₃
harmonic of a pattern on three sites" means. Three consequences, in order of strength:

1. **Identical seeds give b = 0 exactly.** Since 1 + ω + ω² = 0, equal couplings cancel — and b = 0
   is the threefold-degenerate node at Q = ⅓. **The masses split only because the seeds are
   different things.** "Three separate things used for creating everything" is load-bearing here:
   identical seeds would leave the degeneracy exact, and no amount of coupling strength would break
   it.
2. **Three distinct seeds are intrinsically chiral, by counting alone.** The six assignments of three
   distinct labels to three sites fall into **two rotation-orbits of three** (C₃ = A₃ has index 2 in
   S₃), exchanged by a transposition and connected by *no* rotation. So the arrangement carries a
   handedness before any dynamics is written — which is precisely what **C13** showed the phase
   needs and what the ring's own potential cannot supply.
3. **The cyclic order fixes the SIGN of arg b.** Reflection conjugates b, so the two orbits give
   +arg b and −arg b. Which cyclic order the three creating objects sit in selects the sign of the
   Brannen phase, and therefore the sense of the family ordering. A qualitative idea with a
   quantitative consequence.

> **What is still owed, and it is the hard part.** None of this derives the *value* 2/9. The phase
> follows from the relative coupling strengths, which are unknown. Solving for the pattern that would
> reproduce it gives **g₁/g₀ = −0.3001** in the gauge g₂ = 0 — a **constraint on the seeds**, not a
> derivation of the phase. Why the dark condensate, the dyad and the boundary should couple in that
> ratio is untouched, and it is the same debt as deriving c_K, which the keystone c_K·τ = Q would
> settle at a stroke.
>
> **⚠ THAT LAST FRAMING WAS TOO GENEROUS — corrected the same day** (`scripts/seed_couplings_are_the_masses.py`,
> 8 controls incl. an anti-control). Calling g₁/g₀ = −0.3001 "a constraint on the seeds" implies it is
> a *separate* thing that could be discharged on its own. It is not. The map from three real seed
> couplings to (G₀, b) is an **exact bijection** — 3 reals ↔ 1 real + 1 complex, round-tripping to
> 10⁻¹⁵ — and its inverse is
>
> > gⱼ = ⅓[G₀ + 2|b|·cos(arg b + 2πj/3)]
>
> which is **the same functional form as the mass formula**. Hence **gⱼ ∝ √mⱼ**: fed the measured
> leptons, the three seeds couple as **1 : 14.379 : 58.969**.
>
> **So specifying the couplings IS specifying the masses.** The seed picture is a change of variables
> carrying exactly the information the spectrum already carries — it reduces the unknown count by
> **zero**, and "why do the three creating objects couple in that ratio?" is literally the same
> question as "why do the leptons have those masses?". The −0.3001 is the Koide relation in another
> basis.
>
> *Not vacuous:* four seeds on three sites **would** genuinely reduce (kernel dimension 1). The
> no-reduction result is specific to the three-on-three case, which is the configuration actually
> proposed.
>
> **What survives is still worth having** — three facts the spectrum alone does not state: identical
> seeds give b = 0 *exactly* (distinctness is why any splitting exists); three distinct seeds are
> intrinsically chiral, supplying precisely the parity-odd source C13 proved is required; and the
> cyclic order fixes the *sign* of arg b. Those answer *why there is a splitting* and *what kind of
> object can source the phase*. They do not answer *what its value is*.
>
> **Net effect on the search: a narrowing.** The value cannot come from the seed couplings, because
> they carry no information the masses do not. It must come from outside the family sector — which is
> the keystone. **"Derive c_K from first principles" is now the *only* remaining route, not one of
> two.**

### Coherence check — C12/C13 reproduce an existing result from the other direction

Run 2026-07-29 against `scripts/koide_phase_is_a_flat_direction.py`, written a day earlier from the
democratic-graph side. It concluded:

> *"Two degenerate modes span a plane, and any rotation in that plane is a symmetry of the
> Hamiltonian. The Koide phase φ is exactly an angle in that plane. So φ is a flat direction: the
> mechanism cannot fix it, by symmetry, not by omission… A REAL bond leaves them degenerate; a
> COMPLEX bond splits them."*

That is **C12 arrived at independently**. "Any rotation in that plane is a symmetry" is the residual
continuous O(2); "a real bond leaves them degenerate, a complex bond splits them" is the
nematic/adjoint decomposition seen from the eigenvalue side. **Two routes, same structure, neither
using the other** — which is the strongest kind of agreement available here.

**What C12–C14 add over it:** the residual O(2) is identified as what survives SO(3) broken by a
*uniaxial spin-2 nematic* along the democratic axis; the complex part of b is identified as the
*adjoint* component, making arg b a mixing angle rather than an unexplained argument; the flatness is
sharpened into a **parity** statement (C13), which is what converts "the mechanism cannot fix it" into
the usable exclusion *the source must be chiral*; and C14 then supplies a source that qualifies.

**One apparent disagreement, checked and resolved.** The earlier script says the q = 1 and q = 2
modes are degenerate iff arg b ∈ {0, π}; C-G8 says *some* pair coincides at arg b = 0 mod π/3. Both
are correct and they are different statements — verified by direct computation: at φ = 0 and π the
coinciding pair is (q1, q2), at φ = π/3 it is (q0, q2), at φ = 2π/3 it is (q0, q1). The specific pair
rotates with the phase; the existence of *a* degenerate pair recurs every π/3.

---

## What a candidate would immediately buy

- **#1 answers itself.** Threefold degeneracy before pinning is read straight off the stiffness
  matrix.
- **#55 closes** if the response's even part lands in [−2, 0].
- **The three-seed candidate becomes computable**: with a coupling slot (C6), the seeds' imprints
  have components, their doublet-space two-vector has an orientation, and that orientation is either
  **2/9** or one of two pre-registered wrong answers.
- **And if the phase comes out right, Koide inverts**: Q = 3·arg b = 2/3 ⟹ A² = 6(Q − ⅓) = 2 ⟹
  **A = √2 becomes an output.**

## What this file is not

Not a build, and not a hint at one. Assembling constraints is cheap; satisfying C2–C5 and C8
simultaneously is the actual work, and nothing here suggests it is easy — C4 and C5 in particular
are a theorem saying where the answer *cannot* come from, which narrows the search without pointing
into it. **The value here is that a candidate can now be killed in an afternoon instead of after a
month of consequences.**

### ~~C3's open question answered: the delivery law is a RADIAL-sector statement~~ — WITHDRAWN SAME DAY (2026-07-29)

> **This subsection was wrong and is retained struck through, per the ledger convention.** The
> claim was that `scripts/delivery_law_is_one_exponent.py` showed the four recorded delivery laws
> {2, √2, 1, ½} to be one family ε_mode ∝ k^p at p ∈ {0, ½, 1}, reproducing all four "exactly in the
> radial sector and in no other", with the ½ a per-mode duplicate of the 1 and the live fork p = ½
> against p = 1. **Every clause of that is withdrawn.** It read ε as an *energy per mode*; the
> corpus's ε is a **stiffness**, fixed independently in two scripts by ⟨f²⟩ ∝ 1/ε and ω ∝ √ε.
> Fitting four numbers with a quantity that is not the one they denote is protocol 42 — committed in
> the same session that wrote protocol 42 up. Replaced by the entry below.

### C15 — the delivery laws are a TWO-parameter family, and the null already picked one (2026-07-29)

C3 carries a warning that the **radial** Hessian stiffnesses (k_S = 6, k_D = 3) and the **circulant
amplitude** stiffnesses (ε₀ = a + 2b, ε₁ = a − b) are different objects that must not be identified —
added after a false 2.83× conflict was nearly filed. It did not say which stiffness pair the
energy-delivery law (#85) acts on. `scripts/delivery_law_two_parameters.py` (20 controls, two of them
anti-control blocks) settles the law and **extends** C3's warning rather than resolving it.

**The corpus's actual algebra.** The null R_c = M_c equates the summed squared amplitude of the 2-dof
doublet with that of the 1-dof singlet. Writing the deposited energy per degree of freedom as
e ∝ ε^p, and letting s record how a sector's total is counted, the sector amplitude is X² ∝ g^s·ε^(p−1)
and the null solves to

> **ε₁/ε₀ = 2^( s / (1 − p) )**

| delivery law | energy | s | p | ε₁/ε₀ |
|---|---|---|---|---|
| thermal equipartition | ½T per dof | 1 | 0 | **2** |
| sudden quench, 1/ω² | ∝ 1/ε per dof | 1 | −1 | **√2** |
| equal sector delivery | E per sector | 0 | — | **1** |
| doublet gets half | E, E/2 per sector | −1 | 0 | **½** |
| *zero-point, ½ħω* | ∝ √ε per dof | 1 | ½ | **4** |

**Two parameters, not one.** Both are load-bearing: √2 requires p ≠ 0, and 2 requires s ≠ 0. And the
recorded four were never exhaustive — the zero-point law lands on **4**, which is not among them.
(T6 already called the occupancy lock "a fifth law"; this says where the fifth sits.)

**Three corrections to the labels.** √2 is the **sudden quench** (p = −1), *not* the zero-point law.
The zero-point law gives 4. And **"equal amplitude" is not a delivery law at all** — it is the null
itself: at p = 1 the amplitude becomes ε-independent, the null degenerates to 2 = 1, and it fixes no
stiffness ratio whatever. That row was three errors in one.

> **AND THE DOCKET'S QUESTION IS ANSWERED, NOT NARROWED.** Q = ⅔ needs ρ² = ½, hence ε₁/ε₀ = **2
> exactly**, hence s = 1 − p. Only thermal equipartition lies on that line; the next-nearest, √2,
> misses ⅔ by **207,107 ppm** against a 6 ppm budget. With s restricted to the two ways a sector total
> can actually be counted, s = 0 fails at every p and **s = 1 forces p = 0 uniquely**.

**So the fork was never four-way, and the real result is a tension.** The null selects thermal
equipartition *uniquely* — and `koide_delivery_law_discriminator.py` has already shown thermal
equipartition overruns the 6 ppm budget by **171×** at the corpus's own x₁ = 2/9. Those two results
are in direct conflict, and the conflict sits **inside** the Koide derivation rather than upstream of
it. The occupancy lock is not one option among four; it is the only named escape from a contradiction.

**C3's warning is extended.** The required ε₁/ε₀ = 2 matches **neither** existing pair: the radial
Hessian gives k_D/k_S = **½** (which is law 3, yielding Q = 5/3, not ⅔), and the circulant amplitude
stiffnesses at the Koide point give **0.1213** (the 8.2426 inverted). So the delivery law's ε is a
**third** stiffness pair, distinct from both — and *which* pair it is remains open.

### C8 turned into a bracket: which responses are admissible (2026-07-29)

C8 requires a mass response with a genuine even part and records that both forms tried — `tanh u` and
`u/√(1+u²)` — give exactly c_w = 0. It stops at *"the Lagrangian must generate a response with a
genuine even part, and land in that band"*, without saying which responses do.
`scripts/cw_response_bracket.py` (13 controls, incl. anti-control) settles that.

Since u = |x| and u² = x², **c_w is simply the second Taylor coefficient of the response at zero** —
which makes this a classification, not a search:

| response F(u) | c_w | C8 [−2,0] | ensemble [−1.36,−0.32] |
|---|---|---|---|
| `tanh u`, `u/√(1+u²)` — **odd** | **0** | yes | **outside** |
| `ln(1+u)`, `1 − e^(−u)` | **−½** | yes | inside |
| `u·e^(−u)`, `u/(1+u)` | **−1** | yes | inside |
| `u/(1+2u)` | **−2** | yes | **outside** |

**The odd family's failure is structural, not bad luck.** An odd function has no even Taylor terms at
any order, so its u² coefficient vanishes identically. The two forms tried could never have produced
a c_w, **and no other odd form can either — that class is closed permanently.**

**And the band becomes a bracket on a physical scale.** For the saturating family F(u) = u/(1+au),
c_w = −a *exactly*, so the ensemble determination −0.84 ± 0.52 maps directly onto a **saturation
scale a ∈ [0.32, 1.36]** — with the two most natural closed forms, a = ½ and a = 1, both inside it.

> **The anti-control matters:** the band is not permissive. It rejects c_w = 0 *and* c_w = −2, i.e.
> **both endpoints of C8's own [−2, 0] bracket**. "Land in the band" is a real constraint, and the
> wider bracket was the weaker statement.

**Still owed:** the Lagrangian must *generate* one of these, not merely be compatible with it. But
C8 is now a target with a number attached. *(Noted: the fit-implied −1.80 lies outside the ensemble
band — a = 1.8 against at most 1.36 — so the two determinations disagree. Recorded, not resolved.)*

### C16 — C8's even part is a RESUMMATION, not an operator (2026-07-29)

`scripts/cw_response_from_backreaction.py`, 15 controls, two anti-control blocks. C8 required *"the
Lagrangian must generate a response with a genuine even part"*, and the bracket entry above turned
that into c_w ∈ [−1.36, −0.32] without saying where the form comes from. It comes from resummation.

**The construction.** Take the bare response to the winding projection as **linear**, F₀(u) = u —
which is all C8's leading term asserts. Let the medium back-react in proportion to the response it is
already carrying, with strength a. Self-consistency gives a fixed point:

> F = F₀ − a·F₀·F  ⟹  **F = F₀/(1 + a·F₀) = u/(1 + a·u)**,  with **c_w = −a exactly**

the standard geometric (Dyson) resummation — solved here by bisection rather than quoted.

> **So the even part is not a new operator.** It is what resumming the *linear* coupling against the
> medium's back-reaction produces, and **c_w is the back-reaction strength**. A Lagrangian carrying
> only the linear coupling, plus a medium that responds to it, already generates an admissible c_w.
> The band becomes a band on that strength: **a ∈ [0.32, 1.36]** — order unity, which is what a
> medium not weakly coupled to its own response should give.

**It explains the odd-response failure structurally.** `tanh u` and `u/√(1+u²)` are saturating forms
imposed by hand, and **neither is of resummed type** — fitting a at u = 0.5 leaves a **33%** error by
u = 1.5. A back-reaction on a linear bare response *always* gives the rational form, so the c_w = 0
class was never something the mechanism could have produced.

**And it predicts rather than fits.** The geometric series fixes every higher coefficient from one
number: **c₃ = c_w², c₄ = −|c_w|³**. The corpus currently carries the cubic with an *assumed* unit
coefficient, so nothing is being tuned to. At the fit-implied c_w = −1.80 the predicted cubic is 3.24×
larger than unit and leading-order dominance still holds comfortably — the mechanism does not collide
with C9.

**What is still owed.** This supplies the **form** and the meaning of c_w; it does not supply the
**value**. Deriving a — the medium's back-reaction strength on its own winding response — is the
remaining object, now a single number inside a named mechanism rather than an unspecified "response
with an even part".

> ### ⚠ C9's quadratic percentage is mis-booked (found in passing, 2026-07-29)
>
> `_AUDIT_LEDGER.md` derives C9's two figures from the winding moments ⟨|cos|⟩ = 2/π, ⟨cos²⟩ = ½,
> ⟨|cos|³⟩ = 4/3π. The **cubic reproduces exactly**: ε²·⟨|cos|³⟩/⟨|cos|⟩ = ε²·(2/3) = **0.0105%** as
> recorded. The **quadratic does not**: ε·⟨cos²⟩/⟨|cos|⟩ = ε·(π/4) = **0.985%**, against a recorded
> **0.83%** — off by 18.7%.
>
> The recorded figure is what you get using **2/3 — the cubic's moment ratio — in the quadratic's
> place**: 2/3·ε = 0.836%. **C9's conclusion is unaffected**, since both are far below 1 and
> leading-order dominance holds either way. A booking correction, not a retraction — but the spec and
> the ledger both quote 0.83% as a computed result, and it is 0.985%.
