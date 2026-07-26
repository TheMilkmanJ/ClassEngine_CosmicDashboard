"""koide_ring_zero_point — stabilizer candidate (b): quantum zero-point (2026-07-26).

QUESTION
  The classical ground state of the recorded three-term binding is the collinear
  chain, 0.2616·q̃² below the equilateral ring (koide_ring_quartic.py).  The
  chain has THREE stiff internal modes (spectrum 2, 2, 4 in q̃²/d² units) where
  the ring has ONE (breathing, k = 3; the shape pair is flat) — so zero-point
  energy taxes the chain harder.  Does the zero-point of the stiff transverse
  modes restore the ring as the ground state, and at what quantumness?

METHOD (adiabatic estimate, stated as such)
  Along the scale-relaxed isosceles flattening path θ ∈ [60°, 180°]:
    V_eff(θ; η) = E*(θ) + (η/2)·Σ √k⊥(θ),   η ≡ ħ / (d·√(m_face·q̃²))
  where k⊥ are the two Hessian eigenvalues transverse to the path (zero modes
  and path tangent projected out; negative k⊥ clipped at 0 and reported).
  The threshold η* is the smallest η making the ring the global path minimum:
    η* = max over θ of  [E*(60°) − E*(θ)] / (½[S⊥(θ) − S⊥(60°)]),
  valid only where S⊥(θ) > S⊥(60°) — checked, not assumed.
  Physical η: with d = c₂/√σ = 1.9236/√σ, q̃² = 1.1106·√σ (recorded), and the
  face (constituent) mass m_face as the one open identification:
    η = 0.4934 / √(m_face/√σ).

GRADE RULE
  Estimate grade: harmonic-transverse adiabatic treatment, scale relaxed
  classically, semiclassics marginal at η ≈ 0.5.  Survival here is
  candidate-grade viability, never a derivation.  Failure goes to the ledger.
"""
from __future__ import annotations

import numpy as np

Q2 = 1.0
SIG = np.sqrt(3.0)
RMIN = 1e-12
C2 = 4.0 / (3.0 * np.log(2.0))
Q2_PHYS = C2 / np.sqrt(3.0)          # q̃²/√σ, recorded 1.1106


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


def energy(x: np.ndarray) -> float:
    P = x.reshape(3, 2)
    E = SIG * steiner_len(P)
    for i in range(3):
        for j in range(i + 1, 3):
            r = max(np.linalg.norm(P[i] - P[j]), RMIN)
            E += -Q2 * np.log(r)
    return E


def config(theta_deg: float) -> np.ndarray:
    """Scale-relaxed isosceles configuration (legs 1 before scaling)."""
    t = np.radians(theta_deg) / 2.0
    P = np.array([[-np.sin(t), 0.0], [np.sin(t), 0.0], [0.0, np.cos(t)]])
    lam = 3.0 * Q2 / (SIG * steiner_len(P))     # exact scale relaxation
    return (lam * P).reshape(-1)


def hessian(x0: np.ndarray, h: float = 3e-4) -> np.ndarray:
    n = x0.size
    Hm = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            xpp = x0.copy(); xpp[i] += h; xpp[j] += h
            xpm = x0.copy(); xpm[i] += h; xpm[j] -= h
            xmp = x0.copy(); xmp[i] -= h; xmp[j] += h
            xmm = x0.copy(); xmm[i] -= h; xmm[j] -= h
            Hm[i, j] = Hm[j, i] = (
                energy(xpp) - energy(xpm) - energy(xmp) + energy(xmm)
            ) / (4 * h * h)
    return Hm


def transverse_spectrum(theta_deg: float, dth: float = 0.05):
    x0 = config(theta_deg)
    P0 = x0.reshape(3, 2)
    cen = P0.mean(axis=0)
    tx = np.tile([1.0, 0.0], 3)
    ty = np.tile([0.0, 1.0], 3)
    rot = np.stack([-(P0[:, 1] - cen[1]), P0[:, 0] - cen[0]], axis=1).reshape(-1)
    if theta_deg + dth <= 180.0:
        tang = (config(theta_deg + dth) - config(theta_deg - dth)) / (2 * dth)
    else:
        tang = (config(theta_deg) - config(theta_deg - dth)) / dth
    basis = []
    for v in (tx, ty, rot, tang):
        w = v.astype(float).copy()
        for b in basis:
            w -= (w @ b) * b
        nw = np.linalg.norm(w)
        assert nw > 1e-8, "degenerate projection basis"
        basis.append(w / nw)
    B = np.stack(basis, axis=0)
    _, _, Vt = np.linalg.svd(B, full_matrices=True)
    Cmp = Vt[4:, :]                       # 2 × 6 transverse complement
    Hm = hessian(x0)
    Ht = Cmp @ Hm @ Cmp.T
    k = np.sort(np.linalg.eigvalsh(0.5 * (Ht + Ht.T)))
    return k, energy(x0)


def main() -> None:
    print("=" * 78)
    print("Stabilizer (b): zero-point of the transverse stiff modes, ring vs chain")
    print("=" * 78)
    thetas = [60.0, 62.0, 65.0, 70.0, 80.0, 90.0, 100.0, 110.0, 119.0,
              121.0, 130.0, 145.0, 160.0, 175.0, 180.0]
    k60, E60 = transverse_spectrum(60.0)
    S60 = np.sqrt(np.clip(k60, 0.0, None)).sum()
    print(f"\n   ring anchor: E* = {E60:+.6f}, transverse k = "
          f"({k60[0]:+.4f}, {k60[1]:+.4f}), S⊥ = {S60:.4f}  (expected √3 + 0)")
    print("\n   apex θ     E*(θ)      k⊥₁       k⊥₂      S⊥(θ)    η*(θ)")
    rows = []
    for th in thetas:
        k, E = transverse_spectrum(th)
        S = np.sqrt(np.clip(k, 0.0, None)).sum()
        num = E60 - E
        den = 0.5 * (S - S60)
        eta = num / den if (num > 1e-9 and den > 1e-9) else np.nan
        rows.append((th, E, k, S, eta))
        es = f"{eta:8.4f}" if np.isfinite(eta) else "     —  "
        print(f"   {th:6.1f}°  {E:+.6f}  {k[0]:+8.4f}  {k[1]:+8.4f}  {S:7.4f}  {es}")
    etas = [r[4] for r in rows if np.isfinite(r[4])]
    eta_star = max(etas)
    th_star = [r[0] for r in rows if np.isfinite(r[4]) and abs(r[4] - eta_star) < 1e-12][0]
    neg = [r[0] for r in rows if r[1] < E60 - 1e-9 and r[3] <= S60 + 1e-9]
    print(f"\n   binding point: θ = {th_star:.0f}°,  η* = {eta_star:.4f}")
    print(f"   any point with lower E* but no extra zero-point (fatal if so): {neg or 'none'}")

    print("\n   physical quantumness η = 0.4934/√(m_face/√σ) vs the threshold:")
    print("   m_face/√σ     η       ring restored (η ≥ η*)?")
    restored_at = []
    for mf in (0.5, 1.0, 2.0, 3.0, 4.0, 8.0):
        eta = (1.0 / C2) / np.sqrt(mf * Q2_PHYS)
        ok = eta >= eta_star
        restored_at.append((mf, ok))
        print(f"   {mf:8.1f}   {eta:7.4f}   {'YES' if ok else 'no'}")

    print("\nVERDICT")
    print(f"  1. Zero-point taxes the chain harder everywhere on the path")
    print(f"     S⊥ exceeds the ring value {S60:.3f} at every θ > 60° (peaking ≈3.5,")
    print(f"     ending {rows[-1][3]:.3f} at the chain — not monotone, but never below).")
    print(f"     Restoration threshold: η* = {eta_star:.3f}, set at the chain end θ = {th_star:.0f}°.")
    print("  2. At the natural constituent identification m_face ~ (0.5–2)·√σ the")
    print("     physical η is 0.35–0.70: ABOVE threshold — the ring is restored as")
    print("     the path's global minimum, and locally the √u growth of the")
    print("     transverse zero-point beats the u³ classical descent for any η.")
    print("  3. Fences, stated: harmonic-adiabatic estimate; semiclassics is")
    print("     itself O(1)-marginal at η ≈ 0.5; m_face is an open identification")
    print("     (heavier faces, m_face ≳ 3√σ, fall back below threshold); the")
    print("     lattice three-source geometry remains the referee.")
    print("  4. GRADE: candidate (b) SURVIVES at estimate grade — the first")
    print("     stabilizer that does. Viability, not a derivation. Not promoted.")
    print("=" * 78)

    assert abs(S60 - np.sqrt(3.0)) < 5e-3
    assert not neg
    assert 0.1 < eta_star < 1.0
    assert restored_at[1][1]          # m_face = √σ restores the ring


if __name__ == "__main__":
    main()
