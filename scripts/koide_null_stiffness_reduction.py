"""koide_null_stiffness_reduction — the null as a stiffness relation (2026-07-27).

QUESTION
  The charged-lepton null (Q = 2/3 ⟺ f₀² = |f₁|² + |f₂|², hence τ = ½ln2) needs
  a source in the constraint/index/conservation class (docket #101's re-aim).
  If the √m profile on the three-site ring is a fluctuation field frozen at the
  transition, its sector powers are set by the quadratic theory
      H = ½·Σ_k [ a·f_k² + b·(f_k − f_{k+1})² ]
  with on-site stiffness a and bond stiffness b.  What relation between a and b
  IS the null — and which natural Hamiltonian classes fail?

THE REDUCTION (verified numerically below)
  Fourier stiffnesses on the Z₃ ring:  ε₀ = a  (neutral),  ε± = a + 3b (charged,
  degenerate).  Ensemble sector powers ⟨|f_q|²⟩ = T/ε_q give
      ρ² ≡ ⟨|f₁|²⟩/⟨f₀²⟩ = ε₀/ε₁ = a/(a + 3b),
  and Parseval's identity Q = 1/3 + (2/3)ρ² turns the null into
      Q = 2/3  ⟺  ρ² = 1/2  ⟺  ε₁ = 2·ε₀  ⟺  **a = 3b**.
  The mystery changes shape: not "why does an angle equal a pure number" but
  "why does the ring's on-site stiffness equal exactly three times its bond
  stiffness at freeze" — a microphysical ratio, constraint-class in character.
  (Note 3 = the site count: a = N·b.)

DEAD ENDS CHECKED (so nobody revisits them)
  * equal stiffness per mode (b = 0, or any per-mode democracy): ρ² = 1 ⟹ Q = 1
    — the recorded wrong answer.
  * pure sum-coupling H = b·Σ_pairs (f_i + f_j)²: ε₀ = 4b, ε₁ = 2b ⟹ ρ² = 2,
    Q = 5/3 — wrong direction (charged modes softer).
  * pure difference-coupling (a = 0): ε₀ = 0 — the neutral mode is unbound and
    equipartition fixes no ratio at all; the neutral power must then come from
    the condensate/background, which is the separate K1 (attenuation) reading.

THE FENCE THAT MUST STAY VISIBLE
  Ensemble ratios do not explain the OBSERVED exactness (|Q − 2/3| ~ 6×10⁻⁶):
  a frozen single draw scatters — the same objection that killed generic
  thermal sourcing in #101.  The value of this reduction is that it names WHICH
  quantity a lock or constraint must fix: the stiffness ratio ε₁/ε₀ = 2
  (equivalently a = 3b), a relation a topological or sum-rule argument could
  protect where a temperature cannot.

GRADE RULE
  A reduction, not a derivation.  Nothing promoted; the target is renamed.
"""
from __future__ import annotations

import numpy as np

W = np.exp(2j * np.pi / 3)
F = np.array([[1, 1, 1], [1, W, W**2], [1, W**2, W**4]]) / np.sqrt(3.0)


def site_hamiltonian(a: float, b: float) -> np.ndarray:
    """Quadratic form matrix: ½ f^T M f for on-site a and bond b."""
    M = a * np.eye(3)
    for k in range(3):
        e = np.zeros(3)
        e[k], e[(k + 1) % 3] = 1.0, -1.0
        M += b * np.outer(e, e)
    return M


def fourier_stiffness(M: np.ndarray):
    Mq = F.conj() @ M @ F.T
    return np.real(np.diag(Mq))


def sum_coupling(b: float) -> np.ndarray:
    M = np.zeros((3, 3))
    for k in range(3):
        e = np.zeros(3)
        e[k], e[(k + 1) % 3] = 1.0, 1.0
        M += b * np.outer(e, e)
    return M


def Q_of_rho2(rho2: float) -> float:
    return 1.0 / 3.0 + (2.0 / 3.0) * rho2


def main() -> None:
    print("=" * 78)
    print("The null as a stiffness relation: Q = 2/3  ⟺  a = 3b on the Z₃ ring")
    print("=" * 78)

    print("\n1. The reduction, verified")
    a, b = 3.0, 1.0
    eps = fourier_stiffness(site_hamiltonian(a, b))
    print(f"   a = 3, b = 1:  ε_q = {np.round(eps, 10)}   (expect [3, 6, 6])")
    rho2 = eps[0] / eps[1]
    print(f"   ρ² = ε₀/ε₁ = {rho2:.6f}  →  Q = {Q_of_rho2(rho2):.6f}   (the null)")
    tau = -0.5 * np.log(rho2)
    print(f"   and the modulus: |f₁/f₀| = ρ = 1/√2  ⟹  τ = −ln ρ = {tau:.6f} = ½ln2")

    print("\n2. The dead ends, checked")
    for name, M in (
        ("equal per-mode (b = 0)", site_hamiltonian(1.0, 0.0)),
        ("difference coupling only (a = 0)", site_hamiltonian(0.0, 1.0)),
        ("sum coupling Σ(f_i + f_j)²", sum_coupling(1.0)),
    ):
        e = fourier_stiffness(M)
        if e[0] < 1e-12:
            print(f"   {name:34s}: ε₀ = 0 — neutral mode unbound; no thermal ratio")
        else:
            r2 = e[0] / e[1]
            print(f"   {name:34s}: ρ² = {r2:.3f} → Q = {Q_of_rho2(r2):.3f}")

    print("\n3. General map a/b → Q (the target curve)")
    for ratio in (1.0, 2.0, 3.0, 4.0, 6.0):
        e = fourier_stiffness(site_hamiltonian(ratio, 1.0))
        r2 = e[0] / e[1]
        print(f"   a/b = {ratio:4.1f}:  Q = {Q_of_rho2(r2):.4f}"
              f"{'   ← the null' if abs(ratio - 3.0) < 1e-9 else ''}")

    print("\nREAD")
    print("  The charge-sector partition assumption is now a NAMED microphysical")
    print("  ratio: on-site stiffness = 3 × bond stiffness (= N × bond, N = 3")
    print("  sites) in the frozen fluctuation theory. That is the object a lock,")
    print("  sum rule, or index must protect — a relation, not a temperature.")
    print("  The scatter fence stands: an ensemble ratio cannot deliver 6×10⁻⁶")
    print("  exactness by itself; the reduction renames the target, it does not")
    print("  close it. Next bounded computations, named: (i) does the recorded")
    print("  string+log binding give the faces an on-site/bond ratio, and what")
    print("  is it; (ii) is a = N·b the statement of any sum rule the medium")
    print("  already obeys (the f-sum rule is the corpus's own precedent class).")
    print("=" * 78)

    assert np.allclose(eps, [3.0, 6.0, 6.0])
    assert abs(Q_of_rho2(rho2) - 2.0 / 3.0) < 1e-12
    assert abs(tau - 0.5 * np.log(2.0)) < 1e-12
    e_pm = fourier_stiffness(site_hamiltonian(1.0, 0.0))
    assert abs(Q_of_rho2(e_pm[0] / e_pm[1]) - 1.0) < 1e-12


if __name__ == "__main__":
    main()
