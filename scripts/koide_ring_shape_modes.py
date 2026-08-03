"""koide_ring_shape_modes — the virial/stiffness test of the sector balance (2026-07-26).

QUESTION
  Does the recorded three-term ring binding  E = √3·σ·d − 3q̃²·ln d − 3α_d/d
  carry the sector balance f₀² = |f₁|² + |f₂|² in its own stiffness spectrum?
  Thermal sector power balances iff  k_E = 2·k_A  (shape pair vs breathing),
  since <a²> = T/k per mode and the charged sector holds two modes.

METHOD
  Three unit point faces at the vertices of an equilateral triangle (d = 1).
  Strings: Steiner/Fermat Y-junction, tension σ, junction fully relaxed
  (Weiszfeld).  Pairwise log repulsion q̃²; pairwise Coulomb attraction α_d
  (the gauge channel is attractive: T_i·T_j = −1, exact).  Radial equilibrium
  fixes  √3·σ = 3(q̃² − α_d).  The 6×6 Hessian is taken by central second
  differences; zero modes (2 translations + 1 rotation) are identified; the
  internal spectrum is k_A (breathing, Z₃-neutral) + k_E (doubly degenerate
  shape pair, Z₃-charged).

HAND-COMPUTED PREDICTION (to be verified, d = 1 units)
  k_A = 3q̃² − 6α_d          (breathing; matches d-direction E''(d))
  k_E = −(3/2)·α_d           (trace identity over the C₃v irreps)
  i.e. the shape pair is FLAT in the Coulomb-free limit and UNSTABLE for
  any α_d > 0.  The balance k_E = 2k_A is then unreachable everywhere.

GRADE RULE
  A fail retires the direction (ledger).  Byproducts are reported with their
  caveats: classical point faces, quadratic order, relaxed Y-junction.
  Nothing is promoted.
"""
from __future__ import annotations

import numpy as np

D = 1.0
H = 3e-4          # finite-difference step
WTOL = 1e-14      # Weiszfeld tolerance


def vertices() -> np.ndarray:
    R = D / np.sqrt(3.0)
    ang = np.array([np.pi / 2, np.pi / 2 + 2 * np.pi / 3, np.pi / 2 + 4 * np.pi / 3])
    return np.stack([R * np.cos(ang), R * np.sin(ang)], axis=1)


def fermat(P: np.ndarray) -> np.ndarray:
    J = P.mean(axis=0)
    for _ in range(500):
        r = np.linalg.norm(P - J, axis=1)
        w = 1.0 / np.maximum(r, 1e-300)
        Jn = (P * w[:, None]).sum(axis=0) / w.sum()
        if np.linalg.norm(Jn - J) < WTOL:
            return Jn
        J = Jn
    return J


def energy(x: np.ndarray, q2: float, ad: float, sig: float) -> float:
    P = x.reshape(3, 2)
    J = fermat(P)
    Es = sig * np.linalg.norm(P - J, axis=1).sum()
    El = Ec = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            r = np.linalg.norm(P[i] - P[j])
            El += -q2 * np.log(r)
            Ec += -ad / r
    return Es + El + Ec


def hessian(x0: np.ndarray, q2: float, ad: float, sig: float) -> np.ndarray:
    n = x0.size
    Hm = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            xpp = x0.copy(); xpp[i] += H; xpp[j] += H
            xpm = x0.copy(); xpm[i] += H; xpm[j] -= H
            xmp = x0.copy(); xmp[i] -= H; xmp[j] += H
            xmm = x0.copy(); xmm[i] -= H; xmm[j] -= H
            Hm[i, j] = Hm[j, i] = (
                energy(xpp, q2, ad, sig) - energy(xpm, q2, ad, sig)
                - energy(xmp, q2, ad, sig) + energy(xmm, q2, ad, sig)
            ) / (4 * H * H)
    return Hm


def modes(q2: float, ad: float):
    sig = np.sqrt(3.0) * (q2 - ad)          # radial equilibrium at d = 1
    P0 = vertices()
    x0 = P0.reshape(-1)

    # equilibrium check (central gradient)
    g = np.zeros(6)
    for i in range(6):
        xp = x0.copy(); xp[i] += H
        xm = x0.copy(); xm[i] -= H
        g[i] = (energy(xp, q2, ad, sig) - energy(xm, q2, ad, sig)) / (2 * H)
    assert np.abs(g).max() < 5e-7, f"not at equilibrium: |g|max = {np.abs(g).max():.2e}"

    Hm = hessian(x0, q2, ad, sig)
    w, V = np.linalg.eigh(Hm)

    # breathing pattern (unit-normalized radial displacement)
    b = (P0 / np.linalg.norm(P0, axis=1, keepdims=True)).reshape(-1)
    b /= np.linalg.norm(b)

    # classify: three |λ| ≈ 0 zero modes; breathing by overlap; shape pair = rest
    idx = np.argsort(np.abs(w))
    zero = list(idx[:3])
    rest = [i for i in range(6) if i not in zero]
    ov = [abs(V[:, i] @ b) for i in rest]
    ia = rest[int(np.argmax(ov))]
    ie = [i for i in rest if i != ia]
    kA = w[ia]
    kE = 0.5 * (w[ie[0]] + w[ie[1]])
    assert abs(w[ie[0]] - w[ie[1]]) < 2e-3, "shape pair not degenerate"
    assert max(abs(w[i]) for i in zero) < 2e-3, "zero modes not flat"
    return kA, kE


def main() -> None:
    q2 = 1.0
    print("=" * 78)
    print("Stiffness spectrum of the three-term ring — sector-balance test")
    print("=" * 78)
    print()
    print("  balance target: k_E = 2·k_A  (equal thermal power per charge sector)")
    print()
    print("   α_d/q̃²     k_A (num)   k_A (hand)   k_E (num)   k_E (hand)   k_E/k_A")
    ok_A = ok_E = True
    for x in (0.0, 0.15, 0.3, 0.6, 0.9):
        kA, kE = modes(q2, x * q2)
        hA, hE = 3 * q2 - 6 * x * q2, -1.5 * x * q2
        ratio = kE / kA if abs(kA) > 1e-12 else float("nan")
        print(f"   {x:6.2f}   {kA:10.5f}  {hA:10.5f}  {kE:10.5f}  {hE:10.5f}  {ratio:9.4f}")
        ok_A &= abs(kA - hA) < 2e-3
        ok_E &= abs(kE - hE) < 2e-3
    print()
    print(f"  hand formulas verified: k_A = 3q̃²−6α_d [{ok_A}],  k_E = −(3/2)α_d [{ok_E}]")
    print()
    print("VERDICT")
    print("  1. Sector balance needs k_E = 2k_A > 0. Computed: k_E = −(3/2)α_d ≤ 0")
    print("     everywhere — the shape sector is FLAT at α_d = 0 and UNSTABLE for")
    print("     α_d > 0. The balance is unreachable by structure, not by tuning.")
    print("     → the stiffness/virial route to the null FAILS. Ledger row owed.")
    print("  2. BYPRODUCT (adverse, caveated): the equilateral ring is marginal /")
    print("     unstable against shape distortion at quadratic order. The recorded")
    print("     stability window (α_d ≲ 2.2) tested the breathing direction only.")
    print("     Caveats: classical point faces, quadratic order, relaxed junction.")
    print("  3. The Coulomb-free flat direction (k_E = 0 exactly) is a zero mode")
    print("     of the recorded binding — noted as structure, not promoted.")
    print("=" * 78)

    assert ok_A and ok_E
    kA0, kE0 = modes(q2, 0.0)
    assert abs(kE0) < 2e-3 and kA0 > 2.9


if __name__ == "__main__":
    main()
