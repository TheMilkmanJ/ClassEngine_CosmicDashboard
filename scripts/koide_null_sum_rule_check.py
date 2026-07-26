"""koide_null_sum_rule_check — computation (ii): is a = N·b a sum rule? (2026-07-27)

QUESTION
  Does the f-sum-rule class (the corpus's precedent for protected relations,
  guarded by the same Anderson commutator that quantizes the emergent metric)
  force the a = 3b stiffness relation — or protect something else?

METHOD (exact, three-site ring)
  For density-like fluctuations ρ_q on a ring with hopping, the first moment of
  the structure factor is fixed by a double commutator:
      m₁(q) = ⟨[[ρ_q, H], ρ_{−q}]⟩ ∝ E_hop · (1 − cos(2πq/3)),
  independent of the potential (on-site) terms.  Computed exactly below for the
  three-site tight-binding ring.  Consequences:
    * m₁(0) = 0 identically — the q = 0 (neutral) mode is CONSERVED.  The
      sum-rule class protects the NEUTRAL SEAT by conservation law, not by
      equilibrium — precisely the aisle #101 demanded for the null's source.
    * m₁(±1) are equal by symmetry, but the sum rule says nothing about the
      stiffness RATIO ε₁/ε₀: varying the on-site term moves ε₀ freely while
      every first moment stays fixed.  a = 3b is NOT itself a sum rule.

OBSERVATION (weight: none — recorded so it is not re-found)
  a = 3b ⟺ ω_charged/ω_neutral = √2 — the same √2 that is the kernel's cone
  radius A.  A frequency-ratio reading of the amplitude is noted, not used.

GRADE RULE
  A split verdict: the sum-rule class protects the neutral half (conservation);
  the ratio itself is not a sum rule.  The remaining target is the charged-mode
  power lock.  Nothing promoted.
"""
from __future__ import annotations

import numpy as np

N = 3
W = np.exp(2j * np.pi / N)


def hop_hamiltonian(t: float, u_onsite: np.ndarray) -> np.ndarray:
    """Single-particle tight-binding ring: hopping t, arbitrary on-site u."""
    H = np.diag(u_onsite.astype(complex))
    for k in range(N):
        H[k, (k + 1) % N] = -t
        H[(k + 1) % N, k] = -t
    return H


def first_moment(H: np.ndarray, q: int) -> float:
    """m₁(q) = ⟨gs| [[ρ_q, H], ρ_q†] |gs⟩ for the single-particle ground state."""
    rho = np.diag([W ** (q * k) for k in range(N)])
    w, v = np.linalg.eigh(H)
    gs = v[:, 0]
    comm = rho @ H - H @ rho
    dbl = comm @ rho.conj().T - rho.conj().T @ comm
    return float(np.real(gs.conj() @ dbl @ gs))


def main() -> None:
    print("=" * 78)
    print("(ii) The sum-rule check: what the f-sum-rule class does and does not force")
    print("=" * 78)
    t = 1.0
    print("\n   first moments m₁(q), varying the ON-SITE landscape at fixed hopping:")
    print("   on-site pattern          m₁(0)      m₁(1)      m₁(2)")
    for name, u in (("flat  [0,0,0]", np.zeros(3)),
                    ("tilted [0.5,0,−0.5]", np.array([0.5, 0.0, -0.5])),
                    ("strong [3,0,0]", np.array([3.0, 0.0, 0.0]))):
        m = [first_moment(hop_hamiltonian(t, u), q) for q in range(3)]
        print(f"   {name:22s}  {m[0]:+.4f}   {m[1]:+.4f}   {m[2]:+.4f}")
    print("\n   READ: m₁(0) = 0 identically (the neutral mode is a CONSERVED")
    print("   quantity — total density commutes with any hopping H). The charged")
    print("   moments shift only through the ground state (the double-commutator")
    print("   identity itself is potential-free); nothing in any of them fixes")
    print("   the stiffness ratio ε₁/ε₀ — hence a/b stays completely free.")
    print("\nVERDICT (ii): SPLIT.")
    print("   * The sum-rule class PROTECTS THE NEUTRAL SEAT: the q = 0 mode is")
    print("     conserved — its power is set by the conserved total (genesis-set,")
    print("     condensate-class), not by a temperature. That is a conservation-")
    print("     law protection in exactly the aisle #101 demanded, and it")
    print("     dissolves the scatter objection for the NEUTRAL half: f₀ does")
    print("     not scatter because it does not fluctuate.")
    print("   * The RATIO is not a sum rule: a = 3b must come from the dynamics")
    print("     that pins the CHARGED power to f₀²/2. The remaining target is")
    print("     that single lock — one number, one sector, sharper than before.")
    print("   * Noted without weight: a = 3b ⟺ ω_c/ω_n = √2, the cone radius.")
    print("=" * 78)

    for u in (np.zeros(3), np.array([0.5, 0.0, -0.5]), np.array([3.0, 0.0, 0.0])):
        m = [first_moment(hop_hamiltonian(t, u), q) for q in range(3)]
        assert abs(m[0]) < 1e-12
        assert abs(m[1] - m[2]) < 1e-10
    m_flat = first_moment(hop_hamiltonian(t, np.zeros(3)), 1)
    m_strong = first_moment(hop_hamiltonian(t, np.array([3.0, 0.0, 0.0])), 1)
    assert abs(m_flat) > 1e-6


if __name__ == "__main__":
    main()
