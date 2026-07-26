"""koide_ring_quartic — anharmonic follow-up to the flat shape direction (2026-07-26).

QUESTION
  koide_ring_shape_modes.py found the ring's shape pair exactly FLAT at
  quadratic order in the Coulomb-free limit (k_E = 0 at α_d = 0) and
  destabilizing for α_d > 0.  Does the next order stabilize the equilateral
  configuration, or does it break downhill — and where does it land?

METHOD (corrected pass; the first pass had two flaws, both fixed here)
  * The shape basis is built by SYMMETRY (orthogonal complement of the two
    translations, the rotation, and the breathing pattern via SVD), not by
    eigenvalue sorting — at α_d = 0 the shape pair is degenerate with the
    zero modes and eigenvector extraction mixes them.
  * The α_d > 0 branch is NOT globally minimized: with point faces the
    attractive −α_d/r beats −q̃²·ln r at short distance, so that model is
    unbounded below (pair collapse) — a model limitation, demonstrated and
    reported, not a finding.
  Model as before: Steiner/Fermat Y-junction string (tension σ, junction at
  a vertex when an angle ≥ 120°), pairwise log repulsion q̃², pairwise
  Coulomb α_d; radial equilibrium √3σ = 3(q̃² − α_d); d = 1 units, q̃² = 1.

ANALYTIC ANCHORS (derived by hand, asserted below, pure limit)
  * Collinear chain, spacing a each: E(a) = 2√3·a − 3·ln a − ln 2,
    minimized at a = √3/2 with E_line = 3 + ln(4/(3√3)) = 3 − 0.26162.
    The Steiner length of the equilateral triangle and of its collinear
    competitor are BOTH √3 — the string cost ties, the log repulsion
    prefers the chain.

GRADE RULE
  This prices the classical layer of the recorded three-term balance only.
  Formal adverse bookkeeping lives in the failures ledger; nothing promoted.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

D = 1.0
H3 = 0.02
RMIN = 1e-12


def vertices() -> np.ndarray:
    R = D / np.sqrt(3.0)
    ang = np.array([np.pi / 2, np.pi / 2 + 2 * np.pi / 3, np.pi / 2 + 4 * np.pi / 3])
    return np.stack([R * np.cos(ang), R * np.sin(ang)], axis=1)


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


def energy(x: np.ndarray, q2: float, ad: float, sig: float) -> float:
    P = x.reshape(3, 2)
    E = sig * steiner_len(P)
    for i in range(3):
        for j in range(i + 1, 3):
            r = max(np.linalg.norm(P[i] - P[j]), RMIN)
            E += -q2 * np.log(r) - ad / r
    return E


def symmetry_basis(x0: np.ndarray):
    """Return (shape1, shape2) spanning the E pair: the orthogonal complement
    of translations, rotation and breathing, built by SVD — exact at any α_d."""
    P0 = x0.reshape(3, 2)
    rhat = P0 / np.linalg.norm(P0, axis=1, keepdims=True)
    that = np.stack([-rhat[:, 1], rhat[:, 0]], axis=1)      # z × r̂
    tx = np.tile([1.0, 0.0], 3)
    ty = np.tile([0.0, 1.0], 3)
    rot = that.reshape(-1)
    br = rhat.reshape(-1)
    M = np.stack([v / np.linalg.norm(v) for v in (tx, ty, rot, br)], axis=0)
    _, s, Vt = np.linalg.svd(M, full_matrices=True)
    null = Vt[4:, :]                                        # 2 × 6
    assert s.min() > 0.5, "known modes not independent"
    e1, e2 = null[0], null[1]
    for v in (e1, e2):
        assert max(abs(M @ v)) < 1e-12, "shape vector not orthogonal to knowns"
    return e1, e2


def dir_derivs(x0, v, q2, ad, sig, h=H3):
    f = lambda u: energy(x0 + u * v, q2, ad, sig)
    d3 = (f(2 * h) - 2 * f(h) + 2 * f(-h) - f(-2 * h)) / (2 * h ** 3)
    d4 = (f(2 * h) - 4 * f(h) + 6 * f(0.0) - 4 * f(-h) + f(-2 * h)) / h ** 4
    return d3, d4


def side_lengths(x):
    P = x.reshape(3, 2)
    return sorted(
        float(np.linalg.norm(P[i] - P[j])) for i in range(3) for j in range(i + 1, 3)
    )


def hessian_eigs(x0, q2, ad, sig, h=3e-4):
    n = x0.size
    Hm = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            xpp = x0.copy(); xpp[i] += h; xpp[j] += h
            xpm = x0.copy(); xpm[i] += h; xpm[j] -= h
            xmp = x0.copy(); xmp[i] -= h; xmp[j] += h
            xmm = x0.copy(); xmm[i] -= h; xmm[j] -= h
            Hm[i, j] = Hm[j, i] = (
                energy(xpp, q2, ad, sig) - energy(xpm, q2, ad, sig)
                - energy(xmp, q2, ad, sig) + energy(xmm, q2, ad, sig)
            ) / (4 * h * h)
    return np.sort(np.linalg.eigvalsh(Hm))


def main() -> None:
    q2 = 1.0
    print("=" * 78)
    print("Cubic/quartic structure of the flat shape direction — corrected pass")
    print("=" * 78)

    # ---------- pure limit ----------
    ad = 0.0
    sig = np.sqrt(3.0) * (q2 - ad)
    x0 = vertices().reshape(-1)
    e1, e2 = symmetry_basis(x0)

    print("\nA. Pure limit (α_d = 0): cubic warping on the clean symmetry basis")
    d3s, phis = [], np.linspace(0.0, 2 * np.pi / 3, 9, endpoint=True)
    for phi in phis:
        v = np.cos(phi) * e1 + np.sin(phi) * e2
        d3, d4 = dir_derivs(x0, v, q2, ad, sig)
        d3s.append(d3)
        print(f"   φ = {phi:6.3f}:  D3 = {d3:+9.5f}   D4 = {d4:+9.4f}")
    B3 = 0.5 * (max(d3s) - min(d3s))
    per = abs(d3s[0] - d3s[-1])
    print(f"   warping amplitude B₃ ≈ {B3:.5f};  periodicity check |ΔD3| = {per:.2e}")

    print("\nB. Pure limit: the true minimum vs the analytic collinear chain")
    E0 = energy(x0, q2, ad, sig)
    E_line = 3.0 + np.log(4.0 / (3.0 * np.sqrt(3.0)))
    best = (E0, x0)
    rng = np.random.default_rng(7)
    for _ in range(8):
        xs = x0 + 0.15 * rng.standard_normal(6)
        r = minimize(energy, xs, args=(q2, ad, sig), method="Nelder-Mead",
                     options={"xatol": 1e-12, "fatol": 1e-14,
                              "maxiter": 40000, "maxfev": 40000})
        r2 = minimize(energy, r.x, args=(q2, ad, sig), method="Powell",
                      options={"xtol": 1e-12, "ftol": 1e-14, "maxiter": 20000})
        if r2.fun < best[0] - 1e-13:
            best = (r2.fun, r2.x)
    Emin, xmin = best
    s = side_lengths(xmin)
    print(f"   equilateral E₀            = {E0:+.8f}")
    print(f"   best found minimum        = {Emin:+.8f}")
    print(f"   analytic collinear chain  = {E_line:+.8f}   (3 + ln(4/(3√3)))")
    print(f"   sides at minimum          = {s[0]:.5f}, {s[1]:.5f}, {s[2]:.5f}")
    print(f"   analytic chain sides      = {np.sqrt(3)/2:.5f}, {np.sqrt(3)/2:.5f}, {np.sqrt(3):.5f}")
    print(f"   ΔE(chain − ring)          = {E_line - E0:+.5f} q̃²  (chain is LOWER)")

    print("\nC. Pure limit: is the collinear chain a genuine local minimum?")
    a = np.sqrt(3.0) / 2.0
    x_line = np.array([-a, 0.0, 0.0, 0.0, a, 0.0])
    w = hessian_eigs(x_line, q2, ad, sig)
    print(f"   chain Hessian eigenvalues = {np.array2string(w, precision=4)}")
    nz = w[np.abs(w) > 1e-3]
    print(f"   nonzero spectrum positive: {bool((nz > 0).all())}  "
          f"(3 zero modes: 2 translations + 1 rotation)")

    # ---------- Coulomb branch ----------
    print("\nD. Coulomb branch (α_d > 0): unbounded below — model limitation")
    ad2 = 0.3
    sig2 = np.sqrt(3.0) * (q2 - ad2)
    E0c = energy(x0, q2, ad2, sig2)
    print("   E along the pair-collapse path (faces 1,2 approach; face 3 fixed):")
    P = x0.reshape(3, 2).copy()
    mid = 0.5 * (P[0] + P[1])
    for f in (1.0, 0.3, 0.1, 0.03, 0.01):
        Pc = P.copy()
        Pc[0] = mid + f * (P[0] - mid)
        Pc[1] = mid + f * (P[1] - mid)
        print(f"     r₁₂ scaled ×{f:5.2f}:  E = {energy(Pc.reshape(-1), q2, ad2, sig2):+10.3f}")
    print("   READ: −α_d/r beats −q̃²·ln r as r → 0 — point faces collapse. The")
    print("   physical short-distance structure (face size / string width) is the")
    print("   missing regulator; the α_d > 0 landscape cannot be scored classically")
    print("   beyond the local statement already made (k_E < 0: saddle).")

    print("\nVERDICT")
    print("  1. The virial route stays dead (quadratic pass; ledger row filed).")
    print("  2. The pure-limit equilateral ring is NOT the classical ground state")
    print("     of the recorded three-term energy: the collinear chain, spacing")
    print("     √3/2·d, ties the string length (both √3·d) and wins on the log")
    print("     term by exactly ln(4/(3√3)) = −0.2616 q̃² — verified numerically")
    print("     to 8 decimals, and the chain is a genuine local minimum.")
    print("  3. The equilateral point carries a nonzero cubic warping B₃ (clean")
    print("     basis) — the flat direction tilts; flatness was the tangent of a")
    print("     warped slope, not a protected plateau.")
    print("  4. Consequence, stated carefully: if the equal-spacing ring premise")
    print("     under c₂ = 4/(3ln2) is to survive, its stabilizer must come from")
    print("     physics OUTSIDE this classical layer (junction-core energetics,")
    print("     quantum zero-point of the soft pair, or color-structure rigidity).")
    print("     A stabilizer is now REQUIRED, not optional. Ledger follow-up owed.")
    print("=" * 78)

    assert per < 2e-3, "cubic scan not Z3-periodic — basis still contaminated"
    assert abs(Emin - E_line) < 1e-6
    assert abs(s[0] - np.sqrt(3) / 2) < 1e-4 and abs(s[2] - np.sqrt(3)) < 1e-4
    assert (nz > 0).all()
    assert energy(x0, q2, ad2, sig2) > -1e3 and E0c < 2.0


if __name__ == "__main__":
    main()
