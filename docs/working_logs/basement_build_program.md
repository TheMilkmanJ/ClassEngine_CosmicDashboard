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
constituent count. That is the honest content: the induced-gravity demand does not leave N free, it
ties it to the scale, and on the recorded scale band the roster is a few tens of constituents. For
comparison, the Standard Model carries ~100 degrees of freedom, so a basement in this band is
**more minimal than the SM** — a real constraint on what the constituent roster can be, and a check
any proposed structure must pass. The "1–2 M_Pl constituents" band and this count are two faces of
the one relation, not independent facts.

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
