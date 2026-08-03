# PRTOE — Session Findings 2026-07-29 (the correction night)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](../PRTOE_READERS_GUIDE.md); claim
> conditionality maps in [PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md).*

Chronological record of an overnight session. Two things dominate it, and the second is the
uncomfortable one: **five dockets moved forward on structure**, and **five previously-recorded
conclusions of mine turned out to rest on unstated assumptions or wrong reasons** — two of them in
reader-facing documents. The corrections are recorded here at the same weight as the advances,
because the pattern connecting them is the useful output.

Audit: **1,255 → 1,295 closed-form checks, all passing.** Eight new instruments, all with
pre-stated controls, all clean.

---

## 1. The advances

### #1 — ANSWERED. The family degeneracy is accidental, and its parent is SO(3)
`scripts/family_triplet_parent.py` (27 controls, several exact to 0.00e+00).

C₃ is abelian, so every one of its irreps is one-dimensional; S₃ has only 1, 1′, 2. **Neither has a
three-dimensional irrep**, so the threefold degeneracy at b = 0 is *not* a protected multiplet of the
ring's own symmetry — it is the accidental degeneracy of a·𝟙. A genuine triplet needs a continuous
non-abelian parent, and **SO(3) ≅ SU(2)/ℤ₂ works**: the ring's C₃ is the 2π/3 rotation about the
democratic axis (1,1,1).

For **real** b the splitting is purely spin-2: 3 ⊗ 3|_sym = 1 ⊕ 5, the adjoint living entirely in the
antisymmetric part and orthogonal to every symmetric matrix. The traceless stiffness is b(J − 𝟙),
eigenvalues b(2,−1,−1) — a uniaxial nematic — breaking SO(3) → O(2), so 3 → 1 ⊕ 2 with the **doublet
protected by a residual continuous O(2)**, which is why the shape modes are *exactly* degenerate.

**Then the amendment, made before it was relied on.** The physical point has arg b = 2/9 ≠ 0, where
the Hamiltonian is complex **Hermitian**, not real symmetric. Traceless Hermitian 3×3 is the **8** of
SU(3), and 8 → 5 ⊕ 3 under SO(3):

> H = a𝟙 + |b|·[ **cos φ**·(P + Pᵀ) + i·**sin φ**·(P − Pᵀ) ]
> — the first piece the spin-2 nematic, the second the **adjoint**, orthogonal and independent.

So the docket's "SU(2) adjoint is a candidate parent" is **not excluded — it is relocated**, and
**arg b is the mixing angle between the two**, adjoint at 22.6% of the nematic. Recorded as spec C12.

### #2 — a hard exclusion, then a source that meets it
`scripts/arg_b_parity_odd_invariant.py` (11 controls) and `scripts/three_seeds_chirality_and_b.py`
(10 controls).

C₃ forces the potential's phase dependence into cos 3φ and sin 3φ alone. **Reflection kills the sin
term**, pinning the phase to 3φ = 0 or π — which re-derives spec C6's theorem from the *symmetry
action* rather than the mass formula, two independent routes to the same wall. Allowing the
parity-odd term gives tan(3·arg b) = μ/λ, so Koide requires μ/λ = tan(2/3) = 0.786843.

**The exclusion: a reflection-symmetric background cannot source the phase at any order with any
coupling** (anti-control confirmed). **The source must be chiral.** Recorded as C13.

The owner's three-seed idea then supplies exactly that, by counting alone (C14):

- **Identical seeds give b = 0 exactly** — 1 + ω + ω² = 0 — which is the Q = ⅓ node. **The masses
  split only because the seeds are different things.** Distinctness is what lifts the degeneracy;
  identical seeds leave it exact at any coupling strength.
- **Three distinct seeds are intrinsically chiral**: six assignments fall into two rotation-orbits of
  three (C₃ = A₃ has index 2 in S₃), exchanged by a transposition and connected by *no* rotation.
- **The cyclic order fixes the sign of arg b**, since reflection conjugates b — so which order the
  three creating objects sit in selects the sense of the family ordering.

Still owed: the **value** 2/9. Solving for the pattern gives g₁/g₀ = −0.3001 (gauge g₂ = 0) — a
constraint on the seeds, not a derivation.

### #81 — the neutral triple, and a load-bearing exclusion qualified
`scripts/neutrino_Q_sign_branch.py` (5 controls).

A flavour-blind operator is ∝ 𝟙 in the family basis, i.e. pure k = 0, so it splits nothing; any
state-selective result needs a k ≠ 0 component. Against data: the neutrinos do **not** share the
charged phase (φ = 2/9 predicts Δm²₃₁/Δm²₂₁ = 283 against a measured 32.58), but **φ = 2/9 + π/12
gives 32.43**, within 0.5%, with a free best fit 0.13% away. *This is Brannen's published extension
(2006), not new here* — recorded because the corpus did not carry it.

**And it qualifies an exclusion used to condemn a whole class of mechanisms.** The recorded ceiling
"Q_ν rises to only 0.585, short of 2/3 by 12.2%" is **reproduced exactly here as a control** — but it
assumes all three square roots positive. Q = Σm ⁄ (Σ√m)² depends on those signs, and the ring form
generates a negative root whenever 2|b| > a. **On the (−,+,+) branch Q_ν crosses 2/3 at
m₁ ≈ 0.00040 eV** — and the π/12 fit requires that negative root and independently predicts
m₁ = 0.000374 eV. Two routes, one branch, one lightest mass.

**The exclusion does not collapse**: its second leg (Thomas–Fermi weights by charge², so a neutral
cone is worth 2·N_c·q² = 0) is untouched by any of this, and the corpus already noted the two
arguments do not use each other. What changed is that the Q_ν leg can no longer be claimed without
saying which branch it is about. Qualified in three places: the Koide relation doc, the derivation
hunt, and the owner queue.

**A prediction that follows:** Σm_ν = **0.0585 eV**, normal ordering — essentially the minimal NO
value, under the ~0.12 eV bound, inside what the live chains' `m_ncdm` posterior can speak to.
**New debt: π/12 itself**, a pure geometric angle carrying no Q, so a different *kind* of object from
whatever supplies 2/9.

### #85 — one open question retired, and it was not a discovery
`scripts/occupancy_frequency_keystone_identity.py`.

The delivery-law discriminator flagged a contradiction between two arcs: unit occupancy needs
ħω/kT_c = ln2 while the corpus records ω₁/T_c = 2/9, ratio 9ln2/2 = 3.119162. That ratio is exactly
**9τ = 6/c_K** — and **τ cancels out of it** (verified over a wide range, max deviation 0.00e+00). So
it is the keystone c_K·τ = Q with the modulus divided out, implied the moment ω₁/T_c was identified
with arg b = Q/3. **Carry it as an instance of the c_K debt, not as its own question.** Evidence
against neither arc; deriving c_K settles it automatically.

### #55 — the spec's own framing was over-claimed
It opened by saying three dockets were blocked on the un-built Lagrangian, including that **#1 is
"unanswerable without one."** Two of the three were answered without building anything.

**The lesson, which is worth more than the correction:** a specification of what an object must
satisfy is also a specification of what its *consequences* must satisfy, and those can often be
extracted by symmetry before the object exists. **Do not assume a docket is gated on construction
just because it names an un-built object.** The honest remaining need is c_w's response function.

---

## 2. The corrections — five of my own, two reader-facing

### (a) The learn-deadlock mechanism — WITHDRAWN (protocol 47, failures ledger)
Recorded cause: cobaya refuses to re-learn while R−1 exceeds its threshold, so "the mechanism that
would fix the proposal is gated behind the problem it would fix", *and more wall-clock could not
repair it*. Reached the reader-facing risk page **and the Fairbank letter**.

**That gate was never reached.** Isolating the archived run's MPI section shows ranks 1 and 2
announcing *"Ready to check convergence… (waiting for the rest…)"* and rank 0 never arriving.
"All chains are ready" never appears; **no convergence statistic was ever computed**. Learning is a
**collective checkpoint** at `learn_every` = 40·d per rank — 520 at d = 13, against ranks holding
467/1684/658. Two ranks blocked for hours on a third that was **53 samples short**.

**Why it survived:** it explained every symptom and named a real code path. But the evidence was
entirely an *absence*, and an absence is consistent with every mechanism that would produce it.
**Ranking candidates by plausibility is not diagnosis.** Six words settle it — "waiting for the rest".

### (b) "A single chain yields no R−1" — FALSE, and the corpus contradicted itself
With one process cobaya splits the chain into `Rminus1_single_split` segments (default 4) and
computes a within-chain split-R̂. Two dead chains here recorded exactly that (13.25 and 40.36). The
run log asserted the impossibility **two bullets above** quoting one of those numbers. Five instances
swept; `PRTOE_REFEREE_CALENDAR.md` had it right all along.

**The real objection survives and is sharper:** a split-R̂ compares segments of one trajectory and so
**cannot detect confinement to a single basin**. Route-D's gate was not waiting on an impossible
number but on one **blind to the question** — which is worse, since it could have returned something
reassuring.

### (c) Rank separation overstated 75× — ESS ignored
`scripts/rank_separation_ess.py`. The diagnostic divided by raw sample count, treating autocorrelated
samples as independent. Measured τ_int ≈ 23–68. Re-grading the archived model chain:
**23,855 → 2,102 (matching lengths) → 317 (honest ESS)**. The reference re-grades **12.6 → 1.6**, i.e.
*consistent with a single basin*. The conclusion sharpens rather than reverses: reference 1.6 versus
model 317 is a cleaner contrast than 10.5 versus 23,855, where both looked broken.

### (d) The acceptance-rate *reason* was wrong though the conclusion was right (protocol 45)
The `.progress` column named `acceptance_rate` reads ≈0.97 — it is rows ÷ Σweights, pinned near unity
under oversampling. The launchlog's step counters give the true 9.3%. My recorded reason ("chain
files store only accepted points") is **false**, since weights do record rejections. **A right answer
resting on a wrong reason survives every check that tests the answer.**

### (e) Checks that cannot fail (protocol 46)
`scripts/audit_selfcheck_tautology_scan.py`: 161 of 1,236 call sites flagged (13%), meaning **87% are
substantive recomputations**. One was mislabelled in a way that mattered — a "g candidate identity"
that reduces to (10·27/5)/54 = 1 for any α, reading as evidence for a claim #82 records as *still
owed*. Relabelled `[transcription only]`.

**Refined within the hour:** T3 conflates *pinning an external measurement* (correct — you cannot
recompute a measurement) with *pinning something derivable* (the only real weakness). **13% is an
upper bound on soft checks, not a defect rate.**

---

## 3. What the controls caught in my own new work

Five specifications failed their own controls tonight and were fixed before anything relied on them:
a mis-booked tan(2/3) = 0.7936 (actually 0.786843); a closed-form eigensolver losing half its digits
at a degenerate pair; a control asserting tight-prior nuisances should come out *constrained* when
the prior **is** the constraint; a bisection assuming the wrong monotonic direction; and **Δm
computed and called Δm²** — protocol 42, committed in new code while writing up that same trap.

**This is the controls working, not a tally of slips.** The pattern across §2 and §3 is one thing:
*the failure modes that survive longest are the ones that keep passing.*

---

## 4. Coherence check — an independent confirmation

`scripts/koide_phase_is_a_flat_direction.py`, written a day earlier from the democratic-graph side,
concluded that the two degenerate modes span a plane, any rotation in it is a symmetry, and "a REAL
bond leaves them degenerate; a COMPLEX bond splits them." **That is C12 reached independently.** Two
routes, same structure, neither using the other.

One apparent disagreement was chased rather than assumed away: that script says the q = 1, 2 modes
are degenerate iff arg b ∈ {0, π}; C-G8 says *some* pair coincides at arg b = 0 mod π/3. Both correct
— the coinciding pair rotates with the phase (at 0 and π it is (q1,q2), at π/3 it is (q0,q2), at
2π/3 it is (q0,q1)).

---

## 5. Chain state at close of session

- **Reference (ΛCDM)** — healthy, ~9.2% acceptance. Its `.progress` had been stale 4.5 h, which is
  *expected*: progress rows are written only at `learn_every` = 40·d **per rank**. Diagnose liveness
  from `.N.txt` mtimes, never from `.progress`.
- **Model (re-tuned)** — the repair worked: acceptance **5.3–6.2% → 31.2–31.9%**, and rank-count
  spread **1217 → single digits**, which is the condition that prevents the collective block. First
  collective checkpoint due at 520/rank.
- **Route-D** — relaunched 22:51 with **two ranks**, healthy at 21–24%, no "waiting for the rest".
  #21 had still been describing it as one-chain and dead.
- **#84 remains ungraded**, and its pre-registration was sharpened at 00:12:05 with **zero sample
  files on disk** (attested). Bands are in *naive* units deliberately — they were fixed before any
  post-fix sample existed and are not being moved now that a better estimator exists. Grade against
  them as written; report the honest ESS figure alongside.
