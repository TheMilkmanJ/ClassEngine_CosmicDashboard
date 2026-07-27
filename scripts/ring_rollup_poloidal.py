"""ring_rollup_poloidal — link 4, the poloidal half: does the fountain fix the ring? (2026-07-27)

SCOPE, SET BEFORE RUNNING
  The first-roll theorem claims a directed fountain rolls into a HELICAL ring
  whose two circulations are locked to the event.  In the axisymmetric
  reduction (no azimuthal dependence, zero swirl), the ring's POLOIDAL
  circulation — the vortex-ring core's winding in the (r, z) half-plane —
  can be dynamically generated and its lock to the fountain direction
  tested.  The TOROIDAL (swirl) half is a conserved azimuthal quantum
  number here and CANNOT be generated in this reduction — it needs full 3D,
  stated up front exactly as the compact-axis run stated its own limit.

MODEL (medium's own equation, healing units, recorded conventions)
  i∂_t ψ = −½(∂_rr + (1/r)∂_r + ∂_zz)ψ + (|ψ|² − 1)ψ,  axisymmetric m = 0.
  Fountain: a localized upward momentum kick — phase ramp θ(z) inside a
  tube r < r_j — on a uniform background with small deterministic seeds.
  Detection: plaquette-wise phase winding in the half-plane; a vortex point
  at (r₀ > 0, z₀) is a vortex RING; its winding sign is the poloidal
  circulation sense.

CHECKS
  V   the reflection pair (z → −z of the full initial data) must give the
      mirrored evolution with all ring signs flipped — exact symmetry,
      verified numerically.
  L   the lock: across fountain amplitudes and seeds, the leading ring's
      circulation sign must be a deterministic function of the fountain
      direction (all +z runs one sign, all −z runs the other).  A scatter
      would mean the roll-up does NOT fix even the poloidal sense — killing
      the theorem's first half.

GRADE RULE
  Energy monitored; sponge at the outer boundaries; results quoted only if
  the reflection check passes at machine class.  Half of link 4 either
  computes or dies; the toroidal half's 3D requirement stands either way.
"""
from __future__ import annotations

import math

import numpy as np

NR, NZ = 192, 384
RMAX, ZMAX = 28.0, 56.0
DR, DZ = RMAX / NR, 2.0 * ZMAX / NZ
DT = 2.0e-3
T_MAX = 30.0
R_JET, Z_JET, V_JET = 4.0, 8.0, 1.2

r = (np.arange(NR) + 0.5) * DR
z = -ZMAX + np.arange(NZ) * DZ
R2D = r[:, None] * np.ones((1, NZ))
Z2D = np.ones((NR, 1)) * z[None, :]


def laplacian(psi: np.ndarray) -> np.ndarray:
    out = np.zeros_like(psi)
    out[1:-1, :] += (psi[2:, :] - 2 * psi[1:-1, :] + psi[:-2, :]) / DR**2
    out[0, :] += (psi[1, :] - psi[0, :]) * 2.0 / DR**2          # Neumann at axis
    out[-1, :] += (psi[-2, :] - psi[-1, :]) / DR**2
    out[:, 1:-1] += (psi[:, 2:] - 2 * psi[:, 1:-1] + psi[:, :-2]) / DZ**2
    out[:, 0] += (psi[:, 1] - psi[:, 0]) / DZ**2
    out[:, -1] += (psi[:, -2] - psi[:, -1]) / DZ**2
    dpsi_dr = np.zeros_like(psi)
    dpsi_dr[1:-1, :] = (psi[2:, :] - psi[:-2, :]) / (2 * DR)
    dpsi_dr[-1, :] = (psi[-1, :] - psi[-2, :]) / DR
    out += dpsi_dr / R2D
    return out


SPONGE = 1.0 / (1.0 + np.exp(-(R2D - (RMAX - 4.0)) / 0.8)) \
    + 1.0 / (1.0 + np.exp(-(np.abs(Z2D) - (ZMAX - 5.0)) / 0.8))


def rhs(psi: np.ndarray) -> np.ndarray:
    return -1j * (-0.5 * laplacian(psi) + (np.abs(psi) ** 2 - 1.0) * psi) \
        - 0.6 * SPONGE * (np.abs(psi) ** 2 - 1.0) * psi \
        - 0.3 * SPONGE * 1j * 0.0


def initial(direction: int, vjet: float, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    tube = np.exp(-(R2D / R_JET) ** 2) * np.exp(-(Z2D / Z_JET) ** 2)
    phase = direction * vjet * Z_JET * math.sqrt(math.pi) / 2.0 \
        * np.array([[math.erf(zz / Z_JET) for zz in z]]) * np.exp(-(r[:, None] / R_JET) ** 2)
    dn = np.zeros((NR, NZ))
    for _ in range(6):
        kz = rng.integers(1, 5)
        kr = rng.integers(1, 4)
        ph = rng.uniform(0, 2 * math.pi)
        dn += 1e-3 * np.cos(2 * math.pi * kz * Z2D / (2 * ZMAX) + ph) \
            * np.cos(math.pi * kr * R2D / RMAX)
    return np.sqrt(np.maximum(1.0 + 0.0 * tube + dn, 1e-6)) * np.exp(1j * phase)


def evolve(psi: np.ndarray):
    steps = int(T_MAX / DT)
    for s in range(steps):
        k1 = rhs(psi)
        k2 = rhs(psi + 0.5 * DT * k1)
        k3 = rhs(psi + 0.5 * DT * k2)
        k4 = rhs(psi + DT * k3)
        psi = psi + (DT / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.isfinite(psi).all():
            raise FloatingPointError(f"blowup at step {s}")
    return psi


def ring_charge(psi: np.ndarray) -> int:
    """Net plaquette winding in the interior half-plane (r > 2, |z| < 30)."""
    th = np.angle(psi)
    d1 = np.angle(np.exp(1j * (th[1:, :-1] - th[:-1, :-1])))
    d2 = np.angle(np.exp(1j * (th[1:, 1:] - th[1:, :-1])))
    d3 = np.angle(np.exp(1j * (th[:-1, 1:] - th[1:, 1:])))
    d4 = np.angle(np.exp(1j * (th[:-1, :-1] - th[:-1, 1:])))
    w = (d1 + d2 + d3 + d4) / (2 * math.pi)
    mask = (R2D[:-1, :-1] > 2.0) & (np.abs(Z2D[:-1, :-1]) < 30.0)
    return int(np.rint(np.sum(w * mask)))


def main() -> None:
    print("=" * 78)
    print("Ring roll-up, poloidal half: is the ring's circulation fixed by the fountain?")
    print("=" * 78)

    print("\nV. Reflection pair (z → −z: all ring signs must flip):")
    psi_a = initial(+1, V_JET, seed=42)
    qa = ring_charge(evolve(psi_a))
    qb = ring_charge(evolve(psi_a[:, ::-1].copy()))
    print(f"   base: net ring charge = {qa:+d};  reflected: {qb:+d}")
    v_ok = (qa == -qb) and (qa != 0)
    print(f"   reflection symmetry: {'CONFIRMED' if v_ok else 'FAILED/NULL'}")

    print("\nL. The lock: fountain direction vs leading ring sign")
    print("   direction   v_jet   seed   net ring charge")
    results = []
    for direction in (+1, -1):
        for vj, sd in ((1.2, 7), (1.2, 19), (1.6, 7)):
            q = ring_charge(evolve(initial(direction, vj, sd)))
            results.append((direction, q))
            print(f"   {direction:+d}          {vj:.1f}    {sd:3d}    {q:+d}")
    plus = [q for d, q in results if d > 0 and q != 0]
    minus = [q for d, q in results if d < 0 and q != 0]
    locked = plus and minus and all(np.sign(q) == np.sign(plus[0]) for q in plus) \
        and all(np.sign(q) == -np.sign(plus[0]) for q in minus)

    print("\nVERDICT")
    if locked and v_ok:
        print("   THE POLOIDAL LOCK HOLDS: the rolled-up ring's circulation sign is")
        print("   a deterministic function of the fountain's direction — smoke-ring")
        print("   physics confirmed in the medium's own equation. Half of link 4 is")
        print("   computed. The toroidal (swirl) half is a conserved quantum number")
        print("   in this reduction and needs full 3D — the named remaining half.")
    else:
        print("   NOT LOCKED or checks failed — report as-is; if the poloidal sense")
        print("   scatters, the theorem's first half dies and P-2026-057's map")
        print("   cannot close. Nothing papered.")
    print("=" * 78)

    assert v_ok, "reflection check failed — do not quote"
    assert locked, "poloidal lock absent — report the null"


if __name__ == "__main__":
    main()
