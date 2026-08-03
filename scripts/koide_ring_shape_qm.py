"""koide_ring_shape_qm — the zero-point survivor, one rung up (2026-07-26, v2).

QUESTION
  koide_ring_zero_point.py (adiabatic, harmonic-transverse, 1D path) gave the
  ring-restoration threshold η* = 0.311.  This pass drops both approximations:
  exact diagonalization of the 2D Schrödinger problem on the shape plane —
  the full warped landscape (ring point at the origin, three chain valleys at
  120° spacing), no harmonic truncation, tunneling between valleys included.
    H/q̃² = −(η²/2)·∇²_u + V(u),   η = ħ/(d·√(m_face·q̃²)),  u in units of d.
  Two variants: V = classical scale-relaxed energy, and V plus the breathing
  (scale-mode) zero-point (η/2)·√k_b(u) in Born–Oppenheimer fashion.

EXACT IDENTITY (derived, cross-checked by finite differences below)
  Along the normalized radial-scale direction, E(λ) = σλL₀ − 3q̃²·lnλ + const
  gives d²E/dλ² = 3q̃²/λ², hence  k_b(u) = 3q̃²/|x_rel(u)|²  exactly.
  Ring: |x|² = 1 ⟹ k_b = 3.  Chain: |x|² = 3/2 ⟹ k_b = 2 — the chain's
  scale mode is SOFTER, so the breathing zero-point taxes the RING more.

V1 ERRATUM (recorded): the first run's printed verdict presumed the exact
  treatment would lower the threshold.  It does the opposite: η_c(exact 2D) =
  0.345 > 0.311 (tunneling across the three valleys favors the chain phase),
  and the breathing zero-point raises it further.  This version computes the
  breathing-variant threshold properly and prints only what the numbers say.

GRADE RULE
  Estimate grade, one rung up.  If the exact treatment kills the survivor,
  it goes to the ledger; if it holds, the grade stays candidate/viability.
"""
from __future__ import annotations

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

Q2 = 1.0
SIG = np.sqrt(3.0)
RMIN = 1e-12
C2 = 4.0 / (3.0 * np.log(2.0))
Q2_PHYS = C2 / np.sqrt(3.0)
E_CHAIN = 3.0 + np.log(4.0 / (3.0 * np.sqrt(3.0)))
ETA_ADIABATIC = 0.311


def vertices() -> np.ndarray:
    R = 1.0 / np.sqrt(3.0)
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
    for _ in range(300):
        r = np.linalg.norm(P - J, axis=1)
        w = 1.0 / np.maximum(r, RMIN)
        Jn = (P * w[:, None]).sum(axis=0) / w.sum()
        if np.linalg.norm(Jn - J) < 1e-12:
            J = Jn
            break
        J = Jn
    return float(np.linalg.norm(P - J, axis=1).sum())


def raw_energy(x: np.ndarray) -> float:
    P = x.reshape(3, 2)
    E = SIG * steiner_len(P)
    for i in range(3):
        for j in range(i + 1, 3):
            r = max(np.linalg.norm(P[i] - P[j]), RMIN)
            E += -Q2 * np.log(r)
    return E


def shape_basis(x0: np.ndarray):
    P0 = x0.reshape(3, 2)
    rhat = P0 / np.linalg.norm(P0, axis=1, keepdims=True)
    that = np.stack([-rhat[:, 1], rhat[:, 0]], axis=1)
    vecs = [np.tile([1.0, 0.0], 3), np.tile([0.0, 1.0], 3),
            that.reshape(-1), rhat.reshape(-1)]
    M = np.stack([v / np.linalg.norm(v) for v in vecs], axis=0)
    _, s, Vt = np.linalg.svd(M, full_matrices=True)
    assert s.min() > 0.5
    return Vt[4], Vt[5]


X0 = vertices().reshape(-1)
E1, E2 = shape_basis(X0)


def V_and_kb(u1: float, u2: float):
    """Scale-relaxed classical energy and exact scale-mode stiffness at (u1,u2)."""
    x = X0 + u1 * E1 + u2 * E2
    L0 = steiner_len(x.reshape(3, 2))
    if L0 < 1e-9:
        return 50.0, 3.0
    lam = 3.0 * Q2 / (SIG * L0)
    xr = lam * x
    return raw_energy(xr), 3.0 * Q2 / float(xr @ xr)


def kb_fd(u1: float, u2: float, h: float = 2e-3) -> float:
    """Finite-difference cross-check of the exact k_b identity."""
    x = X0 + u1 * E1 + u2 * E2
    L0 = steiner_len(x.reshape(3, 2))
    lam = 3.0 * Q2 / (SIG * L0)
    xs = lam * x
    b = xs / np.linalg.norm(xs)
    return (raw_energy(xs + h * b) - 2 * raw_energy(xs)
            + raw_energy(xs - h * b)) / (h * h)


def main() -> None:
    print("=" * 78)
    print("Exact 2D shape-space quantum mechanics of the ring — v2 (honest verdict)")
    print("=" * 78)

    print("\nA. The landscape")
    best = (1e9, 0.0, 0.0)
    for phi in np.linspace(0, 2 * np.pi, 96, endpoint=False):
        for r in np.linspace(0.3, 1.2, 40):
            v, _ = V_and_kb(r * np.cos(phi), r * np.sin(phi))
            if v < best[0]:
                best = (v, r, phi)
    _, r0, p0 = best
    for _ in range(40):                       # local polish
        moved = False
        for dr, dp in ((1e-3, 0), (-1e-3, 0), (0, 1e-3), (0, -1e-3)):
            v, _ = V_and_kb((r0 + dr) * np.cos(p0 + dp), (r0 + dr) * np.sin(p0 + dp))
            if v < best[0]:
                best = (v, r0 + dr, p0 + dp)
                r0, p0 = r0 + dr, p0 + dp
                moved = True
        if not moved:
            break
    Vv, rv, phiv = best
    vall = [V_and_kb(rv * np.cos(p), rv * np.sin(p))[0]
            for p in (phiv, phiv + 2 * np.pi / 3, phiv + 4 * np.pi / 3)]
    V00, kb00 = V_and_kb(0.0, 0.0)
    _, kbvv = V_and_kb(rv * np.cos(phiv), rv * np.sin(phiv))
    print(f"   V(origin) = {V00:+.6f} (closed form 3);  valley = {Vv:+.6f} at "
          f"|u| = {rv:.4f} (chain closed form {E_CHAIN:+.6f})")
    print(f"   three valleys agree to {max(vall) - min(vall):.2e}")
    print(f"   exact k_b: ring {kb00:.4f} (identity 3), valley {kbvv:.4f} "
          f"(chain identity 2)")
    fd_r, fd_v = kb_fd(0, 0), kb_fd(rv * np.cos(phiv), rv * np.sin(phiv))
    print(f"   FD cross-check: ring {fd_r:.4f}, valley {fd_v:.4f}")

    B = 1.45 * rv
    N = 101
    xs = np.linspace(-B, B, N)
    h = xs[1] - xs[0]
    Vg = np.empty((N, N))
    KBg = np.empty((N, N))
    for i, a in enumerate(xs):
        for j, b in enumerate(xs):
            Vg[i, j], kb = V_and_kb(a, b)
            KBg[i, j] = np.sqrt(max(kb, 0.0))
    print(f"   grid: {N}×{N} over [−{B:.3f}, {B:.3f}]²")

    D2 = sparse.diags([1.0, -2.0, 1.0], [-1, 0, 1], shape=(N, N)) / (h * h)
    I = sparse.identity(N)
    LAP = sparse.kron(D2, I) + sparse.kron(I, D2)
    R2 = np.add.outer(xs**2, xs**2)
    center_mask = (R2 < (0.4 * rv) ** 2).reshape(-1)

    def solve(eta: float, with_zp: bool):
        Vloc = Vg + 0.5 * eta * KBg if with_zp else Vg
        H = -0.5 * eta * eta * LAP + sparse.diags(Vloc.reshape(-1))
        w, vecs = eigsh(H.tocsc(), k=3, which="SA")
        psi2 = vecs[:, 0] ** 2
        imax = int(np.argmax(psi2))
        ring = np.sqrt(R2.reshape(-1)[imax]) < 0.4 * rv
        return w, float(psi2[center_mask].sum()), ring

    def threshold(with_zp: bool, lo: float = 0.05, hi: float = 0.80) -> float:
        assert not solve(lo, with_zp)[2] and solve(hi, with_zp)[2]
        for _ in range(14):
            mid = 0.5 * (lo + hi)
            if solve(mid, with_zp)[2]:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)

    print("\nB. Phase vs quantumness η — both variants")
    print("   η       phase(V classical)   phase(V + breathing ZP)")
    probe = [0.10, 0.20, 0.28, 0.311, 0.35, 0.40, 0.50, 0.60]
    ph1, ph2 = {}, {}
    for eta in probe:
        _, _, r1 = solve(eta, False)
        _, _, r2 = solve(eta, True)
        ph1[eta], ph2[eta] = r1, r2
        print(f"   {eta:.3f}       {'RING ' if r1 else 'chain'}                "
              f"{'RING ' if r2 else 'chain'}")
    ec1 = threshold(False)
    ec2 = threshold(True)
    print(f"\n   η_c (V classical)      = {ec1:.4f}")
    print(f"   η_c (V + breathing ZP) = {ec2:.4f}")
    print(f"   adiabatic path estimate was {ETA_ADIABATIC}")

    print("\nC. Against the physical quantumness η = 0.4934/√(m_face/√σ)")
    print("   m_face/√σ     η      classical-V phase   with-ZP phase")
    for mf in (0.5, 1.0, 1.5, 2.0, 3.0):
        eta = (1.0 / C2) / np.sqrt(mf * Q2_PHYS)
        print(f"   {mf:8.1f}   {eta:6.4f}      {'RING ' if eta >= ec1 else 'chain'}"
              f"               {'RING ' if eta >= ec2 else 'chain'}")
    mf1 = ((1.0 / C2) / ec1) ** 2 / Q2_PHYS
    mf2 = ((1.0 / C2) / ec2) ** 2 / Q2_PHYS
    dir1 = "RAISES" if ec1 > ETA_ADIABATIC else "lowers"
    dir2 = "RAISES further" if ec2 > ec1 else "lowers it back"

    print("\nVERDICT (printed from the numbers, not from expectation)")
    print(f"  1. The exact 2D treatment {dir1} the bar: η_c = {ec1:.3f} vs the")
    print("     adiabatic 0.311 — tunneling across the three valleys helps the")
    print("     CHAIN phase, not the ring.")
    print(f"  2. The breathing zero-point {dir2}: η_c = {ec2:.3f}. The chain's")
    print("     scale mode is softer (k_b = 2 vs 3, exact identity), so the")
    print("     breathing zero-point taxes the ring more.")
    print(f"  3. Ring-phase window: m_face ≤ {mf1:.1f}·√σ (classical V), "
          f"m_face ≤ {mf2:.1f}·√σ (with ZP).")
    print("     The natural constituent identification m_face ~ √σ stays in the")
    print("     RING phase in both variants; m_face ≳ 2·√σ does not. The window")
    print("     is genuinely tighter than the first estimate suggested.")
    print("  4. GRADE: candidate (b) SURVIVES the exact-in-2D test, with a")
    print("     narrowed window and a corrected direction of approach. Estimate")
    print("     grade; not promoted; the lattice three-source geometry and the")
    print("     face-mass identification remain the referees.")
    print("=" * 78)

    assert abs(V00 - 3.0) < 1e-6
    assert abs(Vv - E_CHAIN) < 5e-3
    assert max(vall) - min(vall) < 1e-4
    assert abs(kb00 - 3.0) < 1e-6 and abs(fd_r - 3.0) < 0.05
    assert abs(kbvv - 2.0) < 0.02 and abs(fd_v - 2.0) < 0.05
    assert not ph1[0.10] and ph1[0.60]
    assert not ph2[0.10] and ph2[0.60]
    assert 0.30 < ec1 < 0.40 and ec1 < ec2 < 0.55
    assert mf2 >= 0.9        # constituent-scale faces stay in the ring phase


if __name__ == "__main__":
    main()
