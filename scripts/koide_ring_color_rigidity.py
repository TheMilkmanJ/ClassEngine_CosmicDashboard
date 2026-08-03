"""koide_ring_color_rigidity — stabilizer candidate (c): color rigidity (2026-07-26).

QUESTION
  Does the ε^abc color structure of the three-adjoint ring impose any
  geometric rigidity — anything that disfavors the collinear chain relative
  to the equilateral ring?  Two computable sub-questions, both exact:
    1. Is the collinear geometry color-forbidden, or does the ε-singlet
       contraction survive the junction landing on the middle face?
    2. Can ANY pairwise color operator distinguish geometries — i.e. do the
       pair expectations ⟨T_i·T_j⟩ differ between pairs in the ε-singlet?

METHOD (exact, 27-dimensional)
  SU(2) adjoint generators (T^a)_{bc} = −i·ε_{abc} acting on each slot of
  C³⊗C³⊗C³.  The ε-singlet |s⟩ = (1/√6)·Σ ε_{abc}|a b c⟩.  Verified singlet
  (annihilated by the total charge), then all pairwise Casimir contractions
  and the pair-channel decomposition (3⊗3 = 1 ⊕ 3 ⊕ 5, T·T = −2, −1, +1)
  are computed exactly.

GRADE RULE
  Group theory is exact; anything dynamical beyond it (screening scales) is
  stated as a class fact with the deciding lattice quantity named, never a
  number invented.  Failures go to the ledger.
"""
from __future__ import annotations

import itertools

import numpy as np

EPS = np.zeros((3, 3, 3))
for a, b, c in itertools.permutations(range(3)):
    EPS[a, b, c] = (
        1.0 if (a, b, c) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1.0
    )

T = np.array([-1j * EPS[a] for a in range(3)])          # (T^a)_{bc} = −i ε_{abc}


def op_on_slot(M: np.ndarray, slot: int) -> np.ndarray:
    ops = [np.eye(3, dtype=complex)] * 3
    ops[slot] = M
    return np.kron(np.kron(ops[0], ops[1]), ops[2])


def main() -> None:
    print("=" * 78)
    print("Color rigidity of the ε^abc three-adjoint singlet — exact group theory")
    print("=" * 78)

    s = EPS.reshape(-1).astype(complex) / np.sqrt(6.0)
    assert abs(np.vdot(s, s) - 1.0) < 1e-14

    print("\nA. The ε contraction is a genuine singlet (total charge annihilates it)")
    worst = 0.0
    for a in range(3):
        Q = sum(op_on_slot(T[a], i) for i in range(3))
        worst = max(worst, float(np.linalg.norm(Q @ s)))
    print(f"   max |T_total^a |s⟩|  = {worst:.2e}   (exact singlet)")

    print("\nB. Pairwise contractions — the only geometry-sensitive color operators")
    pair_vals = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        val = sum(
            np.vdot(s, op_on_slot(T[a], i) @ op_on_slot(T[a], j) @ s)
            for a in range(3)
        )
        pair_vals[(i, j)] = val.real
        print(f"   ⟨s| T_{i+1}·T_{j+1} |s⟩ = {val.real:+.12f}  (imag {abs(val.imag):.1e})")
    spread = max(pair_vals.values()) - min(pair_vals.values())
    print(f"   spread across pairs = {spread:.2e}  →  SHAPE-BLIND: every pair")
    print("   identical (forced by the permutation antisymmetry of ε — any face")
    print("   ordering gives the same state up to sign, so no pairwise operator")
    print("   can prefer one geometry over another).")

    print("\nC. Pair channel: which representation each pair sits in")
    TT = sum(
        op_on_slot(T[a], 0) @ op_on_slot(T[a], 1) for a in range(3)
    )
    ev = np.sort(np.linalg.eigvalsh(
        (TT[:, :] + TT[:, :].conj().T) / 2.0
    ).real)
    print(f"   spectrum of T₁·T₂ on 3⊗3⊗1: {np.round(ev[::9], 6)} ...")
    print("   3⊗3 = 1 ⊕ 3 ⊕ 5 with T·T = −2, −1, +1. The ε-singlet pair value")
    print("   −1 = the ADJOINT channel: each pair binds into an adjoint to meet")
    print("   the third face — attractive, but NOT the deepest channel (−2).")
    print("   The chain geometry uses the very same contraction: the middle face")
    print("   couples the two end strings through the same f^abc = ε^abc vertex.")
    print("   Nothing in the algebra forbids it or taxes it.")

    print("\nD. What color CANNOT decide, and what would (class facts, no numbers)")
    print("   Adjoint sources in SU(2) are screened by gluons: the adjoint string")
    print("   is metastable and breaks at a finite distance set by the gluelump")
    print("   mass — a lattice number NOT in the corpus. The recorded spacing is")
    print("   d·√σ = c₂ ≈ 1.92. If the SU(2), N_f = 3 breaking distance is below")
    print("   that, the string-bound ring of the ADJOINT branch dissolves as a")
    print("   long-lived object regardless of geometry — a named exposure for")
    print("   that branch (the medium-vortex branch does not carry it).")

    print("\nVERDICT")
    print("  1. Candidate (c) FAILS as the ring's stabilizer: the collinear chain")
    print("     is color-allowed (same ε vertex), and every pairwise color")
    print("     operator is exactly equal across pairs — color is shape-blind at")
    print("     two-body order. There is no group-theoretic rigidity to invoke.")
    print("  2. Byproduct: the adjoint-branch screening exposure is now named —")
    print("     the deciding quantity is the SU(2), N_f = 3 adjoint string-breaking")
    print("     distance vs c₂ ≈ 1.92/√σ, one more question for the same lattice")
    print("     campaign (with T_c/√σ, F_π/√σ, w·√σ, and the three-source geometry).")
    print("  3. Standing after (a), (b), (c): zero-point (b) is the only surviving")
    print("     stabilizer, at estimate grade. Ledger rows: (a) and (c).")
    print("=" * 78)

    assert worst < 1e-12
    assert spread < 1e-12
    assert all(abs(v + 1.0) < 1e-12 for v in pair_vals.values())
    uniq = sorted(set(np.round(ev, 9)))
    assert np.allclose(uniq, [-2.0, -1.0, 1.0])


if __name__ == "__main__":
    main()
