"""koide_ring_junction_core — can junction-core energetics restore the ring? (2026-07-26)

QUESTION
  koide_ring_quartic.py showed the classical ground state of the recorded
  three-term binding is a collinear chain, 0.2616·q̃² below the equilateral
  ring, with the equilateral point cubic-unstable.  Candidate stabilizer (a):
  a Y-junction core energy — the chain puts the junction ON the middle face
  (zero-length middle leg), so a junction-on-face penalty punishes the chain
  specifically.  Does that restore the equilateral ring?

STRUCTURE USED (derived by hand, asserted below; pure limit, q̃² = 1, σ = √3)
  Scale relaxation is exact: minimizing E(λ·shape) over λ gives string energy
  = 3q̃² always (virial identity of the log term), so
      E*(shape) = 3 + 3·ln(σ/3) + S(shape),
      S(shape)  = 3·ln L_Steiner − ln(r₁₂·r₁₃·r₂₃)   (scale invariant).
  Ring:  S = (3/2)ln3   → E* = 3.
  Chain: S = 2·ln2      → E* = 3 + ln(4/(3√3)) = 2.73838.
  The junction reaches the middle face exactly at apex angle 120° (the
  Fermat-point transition), so any junction-contact penalty acts only there
  and beyond.  The decisive question: is E* already below 3 on the
  junction-interior stretch 60° < θ < 120°?

GRADE RULE
  Prices candidate (a) at the thin-string classical layer.  Adverse results
  go to the failures ledger; nothing is promoted.
"""
from __future__ import annotations

import numpy as np

Q2 = 1.0
SIG = np.sqrt(3.0)
RMIN = 1e-12
C2 = 4.0 / (3.0 * np.log(2.0))     # d·√σ, the recorded spacing in string units
W_SQRT_SIG = (0.8, 1.1)            # flux-tube width band, w·√σ (recorded)


def steiner_len(P: np.ndarray) -> float:
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        u, v = P[j] - P[i], P[k] - P[i]
        nu, nv = np.linalg.norm(u), np.linalg.norm(v)
        if nu < RMIN or nv < RMIN:
            return float(nu + nv)
        if (u @ v) / (nu * nv) <= -0.5:
            return float(nu + nv)
    J = P.mean(axis=0)
    for _ in range(2000):
        r = np.linalg.norm(P - J, axis=1)
        w = 1.0 / np.maximum(r, RMIN)
        Jn = (P * w[:, None]).sum(axis=0) / w.sum()
        if np.linalg.norm(Jn - J) < 1e-14:
            J = Jn
            break
        J = Jn
    return float(np.linalg.norm(P - J, axis=1).sum())


def shape_S(P: np.ndarray) -> float:
    L = steiner_len(P)
    prod = 1.0
    for i in range(3):
        for j in range(i + 1, 3):
            prod *= max(np.linalg.norm(P[i] - P[j]), RMIN)
    return 3.0 * np.log(L) - np.log(prod)


def E_star(P: np.ndarray) -> float:
    return 3.0 + 3.0 * np.log(SIG / 3.0) + shape_S(P)


def isosceles(theta_deg: float) -> np.ndarray:
    t = np.radians(theta_deg) / 2.0
    return np.array([[-np.sin(t), 0.0], [np.sin(t), 0.0], [0.0, np.cos(t)]])


def apex_of_junction_contact() -> float:
    return 120.0


def main() -> None:
    print("=" * 78)
    print("Junction-core candidate: can a junction-on-face penalty restore the ring?")
    print("=" * 78)

    # anchors
    E_ring = E_star(isosceles(60.0))
    E_chain_closed = 3.0 + np.log(4.0 / (3.0 * np.sqrt(3.0)))
    E_120_closed = 3.0 + 3.0 * np.log(2.0) - 2.0 * np.log(3.0)
    print("\nA. Scale-relaxed identity and anchors (closed forms in q̃² units)")
    print(f"   E*(equilateral)          = {E_ring:+.6f}   (closed form: 3)")
    print(f"   E*(chain)                = {E_star(isosceles(180.0)):+.6f}"
          f"   (closed form: {E_chain_closed:+.6f})")
    print(f"   E*(120° isosceles)       = {E_star(isosceles(120.0)):+.6f}"
          f"   (closed form: 3 + 3ln2 − 2ln3 = {E_120_closed:+.6f})")

    print("\nB. The relaxed flattening path (junction interior until 120°)")
    print("   apex θ     E*(θ)      junction")
    prev = None
    monotone = True
    for th in (60, 70, 80, 90, 100, 110, 119.9, 120, 140, 160, 180):
        E = E_star(isosceles(float(th)))
        where = "interior" if th < 120 else "ON middle face"
        print(f"   {th:6.1f}°  {E:+.6f}   {where}")
        if prev is not None and E > prev + 1e-12:
            monotone = False
        prev = E
    print(f"   monotone decreasing along the path: {monotone}")

    drop_before_contact = E_ring - E_star(isosceles(119.9))
    print(f"\nC. The mechanism test")
    print(f"   energy drop BEFORE the junction ever touches a face:")
    print(f"     E*(60°) − E*(→120°) = {drop_before_contact:+.6f} q̃²")
    print("   A junction-contact penalty δ acts only at θ ≥ 120°. Even δ → ∞")
    print("   (an impenetrable wall at contact) leaves the minimum at the 120°")
    print(f"   isosceles, {E_ring - E_120_closed:+.4f} q̃² BELOW the equilateral ring.")
    print("   The equilateral point is a one-sided cubic inflection along this")
    print("   path — it is never the minimum for ANY δ ∈ [0, ∞].")

    print("\nD. Size vs mechanism, and the layer's own expansion parameter")
    need = np.log(3.0 * np.sqrt(3.0) / 4.0)
    q2_me = C2 / np.sqrt(3.0)
    print(f"   penalty size needed to beat the chain: {need:.4f} q̃²"
          f" = {need * q2_me:.3f} m_e  (natural core ~ √σ = m_e: available)")
    print(f"   BUT mechanism fails regardless of size (part C).")
    wlo, whi = (w / C2 for w in W_SQRT_SIG)
    print(f"   thin-string expansion parameter at the operating point:")
    print(f"     w/d = (w·√σ)/c₂ = {W_SQRT_SIG[0]}–{W_SQRT_SIG[1]} / {C2:.4f}"
          f" = {wlo:.2f}–{whi:.2f}")
    print("   The faces sit ~2 string-widths apart: the classical thin-string")
    print("   layer — the three-term balance AND this instability analysis —")
    print("   is uncontrolled at O(1) here.")

    print("\nVERDICT")
    print("  1. Candidate (a), junction-core energetics: FAILS at the thin-string")
    print("     layer. The needed size is natural, but the mechanism cannot work:")
    print("     a contact effect cannot cure an interior instability, and the")
    print("     energy is already 0.118 q̃² below the ring before contact.")
    print("  2. The stability debt escalates: at w/d ≈ 0.5 the ring-vs-chain")
    print("     question is genuinely undecidable at the classical layer. It is")
    print("     a beyond-thin-string question — the geometry of the three-source")
    print("     ground state (Y-junction-like vs collinear) is lattice-computable")
    print("     in the same SU(2) N_f = 3 campaign that referees T_c/√σ, F_π/√σ,")
    print("     and w·√σ.")
    print("  3. Candidates (b) zero-point of the soft pair and (c) color-structure")
    print("     rigidity remain open — and (b) is strengthened: soft modes at")
    print("     w/d ≈ 0.5 have O(1) quantum corrections.")
    print("  4. Nothing promoted; ledger follow-up owed on (a).")
    print("=" * 78)

    assert abs(E_ring - 3.0) < 1e-9
    assert abs(E_star(isosceles(180.0)) - E_chain_closed) < 1e-9
    # 120° sits exactly on the interior/vertex Steiner branch boundary, where
    # the Weiszfeld iteration converges slowly — 1e-6 is the honest tolerance.
    assert abs(E_star(isosceles(120.0)) - E_120_closed) < 1e-6
    assert monotone
    assert drop_before_contact > 0.1
    assert wlo > 0.4 and whi < 0.6


if __name__ == "__main__":
    main()
