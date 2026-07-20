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

## Part 2 — the constituent count (2026-07-20: the relation is fixed, the value is one input short)

The two normalisations agree. The QG file's 1/G = N/(12πε²) with ε the cutoff length is identical
to 1/G = N·Λ²/12π with Λ = 1/ε — the same equation. So there is nothing to reconcile, and the
induced-gravity demand gives one clean relation:

  **N = 12π·(M_Pl/Λ)²**

between the constituent count N and their scale Λ. It does **not** pin either alone — and that is
structural, not a gap in the work: the QG file's whole area-law argument turns on N and ε cancelling
between 1/G = N/(12πε²) and S = N·A/(48πε²), so the induced-gravity sector is by construction blind
to N and Λ separately and sees only the combination. One further input — the actual roster size, or
the exact constituent scale — closes it; the area law cannot.

Evaluated on the recorded band Λ ∈ [1, 2] M_Pl, the relation gives **N ∈ [9.4, 37.7]** — an O(10–40)
count, tied to the scale rather than free. But which *level* N lives at is not settled, and part 3a
below shows it matters: read as the constituent count this is a few tens of preons at 1–2 M_Pl; read
as the emergent-species count it is a different object at a different scale. The relation is firm;
its interpretation is the open question, flagged here so N ∈ [9,38] is not quoted as a settled
constituent number.

## Part 3a — the Pauli count verified, and the level question it exposes (2026-07-20)

Lock (i)→(ii), the finiteness condition that forces three generations, is str[k₁] = 0 — a supertrace
over species, fermions +1 per Weyl, the twelve gauge bosons −4 each. Reproduced exactly: the
Standard Model's 45 Weyl fermions against −48 from the gauge sector give **−3**; adding the three
right-handed neutrinos the model needs anyway makes it **48 − 48 = 0**. So the balance is real and it
selects exactly SM + 3ν_R — three generations, three ν_R, no light steriles (P-2026-045).

**But this supertrace runs over the EMERGENT species — 48 Weyl fermions and 12 gauge bosons — while
part 2's N ∈ [9,38] is a count of the M_Pl constituents.** Two different levels, and the induced-
gravity relation does not by itself say which one the Sakharov–Visser N in 1/G = N/(12πε²) belongs
to. The QG file calls it "the species count" and leaves the level open. This is not cosmetic:

- If N is the **constituent** count, part 2 stands: a few tens of preons at 1–2 M_Pl.
- If N is the **emergent** count (~60 unweighted, or the Sakharov–Visser-weighted version of the same
  48 + 12), then the relation N = 12π(M_Pl/Λ)² inverts to Λ = M_Pl√(12π/N) ≈ **0.79 M_Pl at N = 60**
  — *sub-Planckian*, in tension with the recorded "constituents at 1–2 M_Pl."

So the level of the induced-gravity N is a genuine structural fork, and the two readings give
different constituent scales. Resolving it — does the 1/G loop run on the preons or on the emergent
fields, and with which weights — is the first properly-physical question of the constituent
specification, and it is not gated on any run. (The Sakharov–Visser weighting is not the +1/−4 Pauli
weighting, so the emergent-N that enters 1/G is not literally 60; pinning that weighted count is part
of the same question.)

## Parts 3+ — genuinely open, and this is where the model-building lives

- **The emit mechanism.** How a roster at ~M_Pl emits α_Y(M_Pl) = 0.0180 and the non-abelian
  handouts (52.4, 49.4) — i.e. the constituents' own gauge structure. This is preon/GUT-class
  model-building, not a desk computation.
- **The equation of state**, from which the response-function identity descends — the object α_c's
  derivation owes (that one medium response sets both the photon coupling and the compressibility).
- **The seat constant b** (κ_m's exact value), which the tenth channel's m₁ = κ_m·ρ_inf¼ owes.
- **The 2.9 near-lock's closure** — whether the basement's own threshold corrections close the
  non-abelian gap at M_Pl and turn the near-lock exact. A bonus round, not a lock.

*Honest state: the target is verified coherent (part 1), the constituent count has a suggestive
value pending one convention (part 2), and the specification of the constituents themselves —
the actual UV completion — remains open and is genuine model-building. No part of it is gated on a
run; it is gated on physics not yet done.*
