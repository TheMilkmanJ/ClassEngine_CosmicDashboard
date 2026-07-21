# The basement build — a program, not a session

*The medium's UV completion: specify the constituents (the induced-gravity demand forces them to
1–2 M_Pl) and the equation of state, from which flow the response-function identity that α_c's
derivation owes and the seat constant b the tenth channel owes. This is the corpus's real
chokepoint — several open debts converge here, and no MCMC or telescope reaches it. It is a research
program; this file tracks its parts, closed and open, honestly.*

## The target — six locks any basement must hit simultaneously (from [PRTOE_light.md](../PRTOE_light.md) §6)

1. Pauli finiteness (the condition itself)
2. three Fermi points (the generation count, via the Pauli balance)
3. a Z₃ family structure (the cyclic symmetry the Koide parametrisation uses)
4. 1/α₁ ÷ 1/α₂ = 0.673 at M_Pl (equivalently, the basement's sin²θ_W is fixed by the runs)
5. the bare handout α_Y(M_Pl) = 0.0180 (GUT-normalised 1/α₁ = 33.3)
6. Koide's amplitude A = √2

## Part 1 — is the target self-consistent? (2026-07-20: YES)

Before anyone specifies a structure, the six locks must not contradict each other; an over-constrained
target would kill the route without any model-building. Checked against the §5 handout table
(1/α at M_Pl, GUT-normalised: strong 52.4, weak 49.4, U(1) 33.3):

| lock | check | result |
|---|---|---|
| (iv) ratio | 1/α₁ ÷ 1/α₂ = 33.3/49.4 = **0.674** | matches booked 0.673 |
| (v) handout | α_Y = (3/5)/33.3 = **0.0180** | matches booked 0.0180 |
| (vi) Koide | A = √2 = 1.41421 vs measured 1.4142005 | matches to 0.0009% |

Locks (iv) and (v) are **not independent** — both descend from the single U(1) entry 33.3 in the
handout table, so hitting one hits the other. The structural triad (i)(ii)(iii) is likewise one
mechanism in three faces: the Pauli balance that gives finiteness is what fixes the Fermi-point
count at three, which is what the Z₃ family symmetry organises. So the six nominal locks are really
**three independent demands** — the U(1) handout, the Pauli/generation/Z₃ chain, and Koide's A —
and none contradicts another. **The target is self-consistent; the route is not dead by
over-constraint.**

*One consequence, stated correctly so it is not misread as a fourth check:* these couplings give
sin²θ_W(M_Pl) = α_Y/(α₂+α_Y) = **0.471**. That is *above* the unification value 3/8 = 0.375, not
near it — a direct restatement of the abelian coupling being the outlier (α₁ > α₂ at M_Pl), not an
independent success. It carries no information beyond lock (iv).

## Part 2 — the constituent count from induced gravity: the route the framework rejects (RETRACTED)

A first pass here derived N = 12π·(M_Pl/Λ)² from 1/G = N/(12πε²) and read off **N ∈ [9,38]**
constituents on the 1–2 M_Pl band. **That is wrong, and the model's own content is what kills it.**
The Sakharov quadratic form 1/G = N/(12πε²) is proportional to str[k₁]·Λ² — and **str[k₁] = 0 is
exactly the Pauli finiteness condition** (part 3a). The QG file (§5.4) states it plainly: *"This
framework's own content sets that coefficient to zero … every attempt to compute Newton's constant
along Sakharov's route was computing a term the vacuum annihilates."* So the cutoff-and-count
relation is the route the framework abandons; it cannot pin the constituent count, and
**N ∈ [9,38] is retracted.**

The physical 1/G is cutoff-free — the Pauli form **1/G = −(1/2π)·str[k₁·m²·ln(m²/µ²)]**, fixed by the
**mass spectrum** of the vacuum's content, not by a cutoff times a count (QG §5.5). So the
induced-gravity demand constrains the constituents through their *masses*, via the log term; pinning
the constituent count from it is a mass-spectrum computation, not a one-line relation, and it is the
correct first payable step here. The "constituents at 1–2 M_Pl" band must rest on that mass-spectrum
reading rather than on the quadratic route — re-deriving it from the log term is what part 3b (open)
owes. *The lesson: the induced-gravity sector does not hand over a constituent count for free; the
same finiteness that makes the model gravitationally interesting removes the cheap way to count its
constituents.*

## Part 3a — the Pauli count verified, and its double duty (2026-07-20)

Lock (i)→(ii), the finiteness condition that forces three generations, is str[k₁] = 0 — a supertrace
over species, fermions +1 per Weyl, the twelve gauge bosons −4 each. Reproduced exactly: the
Standard Model's 45 Weyl fermions against −48 from the gauge sector give **−3**; adding the three
right-handed neutrinos the model needs anyway makes it **48 − 48 = 0**. So the balance is real and it
selects exactly SM + 3ν_R — three generations, three ν_R, no light steriles (P-2026-045).

**The finding: str[k₁] = 0 does two jobs at once, and the second one is what retracts part 2.** The
same supertrace that forces three generations is the coefficient of the Sakharov *quadratic* 1/G
(∝ str[k₁]·Λ²), so setting it to zero simultaneously (a) fixes the generation count and (b)
annihilates the cutoff term in Newton's constant. This is precisely why the framework is "in Pauli's
scheme, not Sakharov's" (QG §5.4): with the quadratic term gone, 1/G is cutoff-free and fixed by the
mass spectrum. So finiteness and induced gravity are **one condition, not two** — and the
constituent-count-from-cutoff of part 2 never had a foundation, because the very str[k₁] = 0 that
gives three generations removes the Λ² term that count was read from. The honest structural content
is the identification itself: *the condition that makes the roster finite is the condition that makes
its gravity cutoff-free.*

## Part 3b — the constituent count from the mass spectrum (OPEN, replaces the retracted part 2)

What actually pins the constituents, then, is the cutoff-free relation
1/G = −(1/2π)·str[k₁·m²·ln(m²/µ²)]: Newton's constant is a weighted sum over the constituents' own
*masses*, so requiring it to reproduce M_Pl constrains the constituent mass spectrum, not a bare
count against a cutoff.

**One firm consequence, and it explains the recorded band.** Because str[k₁] = 0, a *degenerate*
constituent spectrum gives 1/G = 0: if every constituent shared one mass M, then m²·ln(m²/µ²) is a
common factor and str[k₁·m²·ln] = (m²·ln)·str[k₁] = 0 — gravity would not be induced at all. So
**finiteness forbids a degenerate spectrum**: the same condition that makes the roster finite and
fixes three generations requires the constituents to sit at *different* masses, and 1/G is set by
the *spread* of m²·ln across the balanced species, not by their common scale. The order of the
required spread is O(M_Pl) — which is why the constituents occupy a *band* (the recorded 1–2 M_Pl)
rather than a single mass. That band is therefore a structural consequence, not an input. *(A
two-mass toy with the species count near 12π puts the fermion/boson split at ~7% of M_Pl, but that
figure rests on the retracted count and a degenerate-within-sector approximation, so only the
qualitative statement — non-degenerate, spread O(M_Pl) — is firm; the exact spread needs the actual
roster and its weights.)*

Reading off how many constituents the spectrum needs, and their actual masses, is the remaining
step — genuine model-building, not gated on any run.

## Parts 3+ — genuinely open, and this is where the model-building lives

- **The emit mechanism.** How a roster at ~M_Pl emits α_Y(M_Pl) = 0.0180 and the non-abelian
  handouts (52.4, 49.4) — i.e. the constituents' own gauge structure. This is preon/GUT-class
  model-building, not a desk computation.
- **The equation of state**, from which the response-function identity descends — the object α_c's
  derivation owes (that one medium response sets both the photon coupling and the compressibility).
- **The seat constant b** (κ_m's exact value), which the tenth channel's m₁ = κ_m·ρ_inf¼ owes.
- **The 2.9 near-lock's closure** — whether the basement's own threshold corrections close the
  non-abelian gap at M_Pl and turn the near-lock exact. A bonus round, not a lock.

## Part 4 — the Koide sector's demand collapses to ONE node (2026-07-20)

The Koide-facing locks are not independent targets; the mass sector's own reduction (T6, the
kernel/holonomy pass) shows they are faces of a single object. In the Z₃ kernel the Koide amplitude
and the Brannen phase are the **radius** and the **winding** of one graded cone:

- **A = √2 (lock vi) is the cone's radius.** Q = 2/3 ⟺ the family √m-vector is null on the
  Z₃-graded form f₀² − |f₁|² − |f₂|² (signature +,−,−). "A = √2" is not a fitted amplitude; it is the
  statement that the vector sits on the cone — §6's "the relation lives entirely in the amplitude",
  read structurally. And 2/3 is not a tuned fraction: for *any* null vector Σm = 2f₀² while
  (Σ√m)² = 3f₀², so Q = 2/3 identically. The object to explain is the null, not the number.
- **The phase 2/9 is the cone's holonomy, not a seventh lock.** 3·θ_B = Q — verified a genuine
  relation, not an identity (it fails every non-lepton triple) — winds the phase around the three
  seats: θ_B = Q/3, the per-generation share. The Brannen phase is the winding of the same cone the
  amplitude is the radius of.
- **The three seats are the three Fermi points (lock ii), organised by the Z₃ (lock iii).** The
  generation index is the Fermi-point label; the Z₃ is what makes the three one orbit, so they share
  one cone.
- **The null has the *shape* of lock (i)'s balance, but the node permits it rather than forcing it.**
  A Fermi point is a *protected gapless* node — the str[k₁] = 0 balance (part 3a) — and the Koide
  null f₀² − |f₁|² − |f₂|² = 0 is that same signed balance read in family space, one neutral node
  against two charged. But gaplessness alone is *not* the null: the gapless node (b = 0) sits at
  Q = 1/3, while the null lives at *finite* hopping |b|/a = 1/√2 (Q = 2/3), which the C₃ symmetry
  permits but does not force (worked below). So "why the radius is exactly √2" is not "why the node
  is gapless" — it is why the medium seats the hopping at that one finite ratio, the quantity the
  node leaves open.

**The consequence for the build.** The six locks are really **two objects**: the *family node* —
locks (i),(ii),(iii),(vi) plus the Brannen phase, all faces of one Z₃-protected gapless
three-Fermi-point node with a null cone — and the *gauge handout*, locks (iv),(v), the U(1) outlier's
emit mechanism (part 3+). The Koide sector no longer hands the basement four separate demands; it
hands it **one**: deliver a genuine Z₃-symmetric protected node on three Fermi points.

**What "one node" actually buys — worked explicitly (`scripts/koide_triple_point_node.py`).** The
node is *literal*: the Koide √m are the eigenvalues of a C₃ (circulant) hopping Hamiltonian
H = a·I + b·P + b*·P², with the node at b = 0 (threefold degenerate, Q = 1/3) and the leptons seated
at |b|/a = 1/√2 (Q = 2/3) — the circulant reproduces the three √m to 10⁻⁸. So the node reduces the
*entire* sector to a **single complex hopping b**: exactly two dimensionless numbers, |b|/a and
arg(b). But the node **permits** the null; it does not **force** it. Koide's two facts *fix* those
two numbers — |b|/a = 1/√2 gives A = √2, arg(b) gives the phase 2/9 — while the C₃ symmetry alone
predicts neither value. So the radius (√2) and winding (2/9) do **not** fall out for free; they are
the two parameters the node leaves open, and pinning them needs the medium (what sets the hopping
relative to the offset). One honest hint the calculation surfaces: A = √2 is **96% of the positivity
wall** A_max = −1/cos θ_min, where the lightest branch (the electron, √m ≈ 0.04 μ) nears zero — so the
leptons sit at *near-maximal* splitting, and "the electron branch saturating the positivity bound"
is the leading candidate selector for |b|/a = 1/√2, not yet exact. The gain is real regardless: the
whole Koide mystery is now **one complex number** (the family hopping), its two parts your √2 and
2/9, and the node explains why there are exactly those two — the residual is maximally sharpened, not
closed.

**What this does not yet do (the honest residual).** It does not build the node. Two steps remain,
both UV: (a) promoting the Z₃ from the parametrization *scaffold* §6 calls it to a genuine protected
symmetry of the medium — only a real symmetry makes the three Fermi points one cone-sharing orbit;
and (b) the bridge from the medium's momentum-space Fermi points to the family-space √m cone — the
identification (ii) asserts but does not derive. Both are the same model-building the rest of this
program owes; the gain is that they now discharge four locks and the phase at once, not one.

## Honest state

*The target is verified coherent (part 1); the constituent count is NOT pinned by the cheap
cutoff route (part 2, retracted) but constrained through the mass spectrum (part 3b), which forbids a
degenerate spectrum and forces the recorded O(M_Pl) band; the Koide-facing locks reduce to one
protected Z₃ node (part 4); and the specification of the constituents themselves — the actual UV
completion, that node and the gauge handout — remains open and is genuine model-building. No part of
it is gated on a run; it is gated on physics not yet done.*
