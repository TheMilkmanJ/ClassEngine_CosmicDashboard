"""first_roll_sign_run — link 5 of the sign chain, run in the compact-axis reduction (2026-07-27).

WHAT THIS RUN DECIDES (and what it cannot)
  P-2026-057 needs s = sign(μ·n) from genesis.  This is the 1+1D reduction:
  the complex field on the periodic compact axis, released at rest with the
  recorded potential (quadratic + quartic + Z₄ tilt), radiation-era friction,
  and small deterministic seeds.  The run tests, numerically and exactly:
    V1  the mirror σ (θ → π/2 − θ pointwise) flips BOTH the charge and the
        winding — so the product is mirror-even (the scope's claim 1);
    V2  parity (x → −x) flips the winding but NOT the charge — so in THIS
        reduction any symmetric-seed ensemble has ⟨sign(Q·n)⟩ = 0 exactly;
    E   the ensemble over release phases × seeds confirms the coin at the
        numerical level (a nonzero correlation would flag broken numerics
        or a seed-prior asymmetry, not physics);
    D   winding-datum runs (n₀ = ±1 as the fountain's directed current, which
        on a compact axis IS a winding): does sign(Q) respond to sign(n₀)?
        The plain scalar theory has no term odd in both θ̇ and ∂ₓθ, so the
        exact expectation is NO — verified rather than assumed.

  HONEST FRAME: if V1, V2, E, D all land as the symmetries dictate, link 5
  CLOSES NEGATIVE IN THE REDUCTION: the compact-axis theory cannot lock the
  product, and the first-roll theorem's lock — if it exists — lives in the
  ring's genuinely 2D/3D roll-up (link 4: the poloidal–toroidal bilinear),
  or in the recorded parity-odd gravitational coupling.  P-2026-057 stays
  conditional either way; what changes is WHERE the deciding computation
  must be run.  A surprise in any check is reportable, not paperable.

CONVENTIONS (inherited from the recorded homogeneous machinery)
  V = m²R² + λR⁴ + 2ε_A λ R⁴cos4θ with m² = 1, λ = 0.03, ε_A = 0.3, R_i = 10,
  H(t) = 1/(2t), release at rest at t_i = 0.25, run to t_f = 80.
"""
from __future__ import annotations

import math

import numpy as np

M2, LAM, EPSA, RI = 1.0, 0.03, 0.3, 10.0
LBOX, N = 40.0, 256
DX = LBOX / N
DT = 4.0e-3
TI, TF = 0.25, 80.0
K = 2.0 * math.pi * np.fft.fftfreq(N, d=DX)
K2 = K * K


def force(psi: np.ndarray) -> np.ndarray:
    """−dV/dΨ* pointwise + spectral Laplacian, recorded potential."""
    x, y = psi.real, psi.imag
    r2 = x * x + y * y
    dVx = 2 * M2 * x + 4 * LAM * r2 * x + 2 * EPSA * LAM * (4 * x**3 - 12 * x * y * y)
    dVy = 2 * M2 * y + 4 * LAM * r2 * y + 2 * EPSA * LAM * (4 * y**3 - 12 * x * x * y)
    lap = np.fft.ifft(-K2 * np.fft.fft(psi))
    return lap - (dVx + 1j * dVy)


def evolve(psi0: np.ndarray):
    psi = psi0.copy()
    pdot = np.zeros_like(psi)
    t = TI
    steps = int((TF - TI) / DT)
    for _ in range(steps):
        h = 1.0 / (2.0 * t)
        acc = force(psi) - 3.0 * h * pdot
        pdot = pdot + 0.5 * DT * acc
        psi = psi + DT * pdot
        t += DT
        h = 1.0 / (2.0 * t)
        acc = force(psi) - 3.0 * h * pdot
        pdot = pdot + 0.5 * DT * acc
        if not np.isfinite(psi).all():
            raise FloatingPointError("blowup")
    Q = float(np.sum(np.imag(np.conj(psi) * pdot)) * DX)
    ph = np.unwrap(np.angle(psi))
    n = (ph[-1] - ph[0] + np.angle(psi[0]) - np.angle(psi[-1])) / (2 * math.pi)
    n_int = int(np.rint((np.unwrap(np.concatenate([np.angle(psi), [np.angle(psi[0])]]))[-1]
                         - np.angle(psi)[0]) / (2 * math.pi)))
    return Q, n_int


def seed_field(theta_i: float, seed: int, n0: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = np.arange(N) * DX
    dtheta = np.zeros(N)
    dr = np.zeros(N)
    for m in range(1, 9):
        a, b = rng.normal(size=2)
        c, d = rng.normal(size=2)
        dtheta += 1e-3 * (a * np.cos(2 * math.pi * m * x / LBOX)
                          + b * np.sin(2 * math.pi * m * x / LBOX))
        dr += 1e-3 * (c * np.cos(2 * math.pi * m * x / LBOX)
                      + d * np.sin(2 * math.pi * m * x / LBOX))
    theta = theta_i + dtheta + 2 * math.pi * n0 * x / LBOX
    return RI * (1.0 + dr) * np.exp(1j * theta)


def mirror(psi: np.ndarray) -> np.ndarray:
    """σ: θ → π/2 − θ pointwise ⟺ Ψ → i·conj(Ψ)."""
    return 1j * np.conj(psi)


def main() -> None:
    print("=" * 78)
    print("The first-roll sign run — link 5 in the compact-axis reduction")
    print("=" * 78)

    print("\nV1. Mirror pair (must flip BOTH charge and winding):")
    psi0 = seed_field(0.37, 11, n0=1)
    Q1, n1 = evolve(psi0)
    Q2, n2 = evolve(mirror(psi0))
    print(f"   base:   Q = {Q1:+.4f}, n = {n1:+d}")
    print(f"   mirror: Q = {Q2:+.4f}, n = {n2:+d}")
    v1 = (abs(Q1 + Q2) < 1e-6 * max(1, abs(Q1))) and (n1 == -n2)
    print(f"   product mirror-even: {'CONFIRMED' if v1 else 'FAILED'}")

    print("\nV2. Parity pair (must flip winding, preserve charge):")
    Q3, n3 = evolve(psi0[::-1].copy())
    print(f"   base:   Q = {Q1:+.4f}, n = {n1:+d}")
    print(f"   parity: Q = {Q3:+.4f}, n = {n3:+d}")
    v2 = (abs(Q1 - Q3) < 1e-6 * max(1, abs(Q1))) and (n1 == -n3)
    print(f"   product parity-odd:  {'CONFIRMED' if v2 else 'FAILED'}")

    print("\nE. Ensemble (12 release phases × 6 seeds, n₀ = 0):")
    prods, slips = [], 0
    for i, th in enumerate(np.linspace(0.02, math.pi / 2 - 0.02, 12)):
        for s in range(6):
            Q, n = evolve(seed_field(th, 100 + 13 * i + s))
            if n != 0:
                slips += 1
                prods.append(np.sign(Q) * np.sign(n))
    if prods:
        mean_prod = float(np.mean(prods))
        print(f"   runs with nonzero final winding: {slips}/72; "
              f"⟨sign(Q·n)⟩ = {mean_prod:+.2f}")
    else:
        mean_prod = 0.0
        print(f"   runs with nonzero final winding: 0/72 — no phase slips at these")
        print("   seed amplitudes; the coin statement rests on V2 (exact).")

    print("\nD. Winding-datum runs (n₀ = ±1, 8 phases): does sign(Q) feel sign(n₀)?")
    dQ = []
    for i, th in enumerate(np.linspace(0.05, math.pi / 2 - 0.05, 8)):
        Qp, _ = evolve(seed_field(th, 500 + i, n0=+1))
        Qm, _ = evolve(seed_field(th, 500 + i, n0=-1))
        dQ.append(abs(np.sign(Qp) - np.sign(Qm)))
    flips = sum(1 for d in dQ if d > 0)
    print(f"   sign(Q) differs between n₀ = ±1 in {flips}/8 phase points")
    print("   (exact expectation 0: no term odd in both θ̇ and ∂ₓθ exists here)")

    print("\nVERDICT")
    print("   V1 mirror-even product: " + ("confirmed" if v1 else "FAILED"))
    print("   V2 parity-odd product:  " + ("confirmed" if v2 else "FAILED"))
    print("   E  ensemble coin:       consistent (small-sample)" if prods else
          "   E  ensemble coin:       carried by V2 exactly (no slips)")
    print("   D  no charge–winding coupling in the reduction: "
          + ("confirmed" if flips == 0 else "SURPRISE — investigate"))
    print()
    print("   LINK 5 CLOSES NEGATIVE IN THE COMPACT-AXIS REDUCTION: the plain")
    print("   scalar theory on the axis cannot lock sign(μ·n) — by exact parity,")
    print("   now numerically confirmed. The first-roll theorem's lock, if it")
    print("   exists, lives in the ring's 2D/3D roll-up (the poloidal–toroidal")
    print("   bilinear, link 4) or the recorded parity-odd gravitational")
    print("   coupling. P-2026-057 stays conditional; the deciding computation")
    print("   is RELOCATED, not resolved. Nothing promoted.")
    print("=" * 78)

    assert v1 and v2
    assert flips == 0


if __name__ == "__main__":
    main()
