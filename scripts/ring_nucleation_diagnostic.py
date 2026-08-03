"""ring_nucleation_diagnostic — why does the fountain not register a ring? (2026-07-28)

PURPOSE (diagnosis, not the test)
  Two runs of the poloidal sign-lock experiment returned zero net ring
  charge (jets 1.2 and 2.5).  Before redesigning anything, this diagnostic
  answers WHERE the failure lives, with a time-resolved winding census:
    zone A: r < 2            (the main detector's axis exclusion)
    zone B: 2 ≤ r ≤ R−4, |z| < Z−5   (the main detector's window)
    zone C: the sponge margins        (structure dying at the boundary)
  plus the minimum-density point each frame (a nucleation precursor track),
  at half resolution and short horizon so it answers in minutes.

READINGS IT SEPARATES
  * rings in zone A only  → detector-window fix (include the axis region)
  * rings appear then vanish between frames → lifetime/annihilation issue
  * transient windings in B early, gone by the old single-shot detection
    time → detection-timing fix
  * no winding anywhere at any time, both amplitudes → the smooth jet
    genuinely does not roll up in this reduction; nucleation redesign
    (density piston) or 3D relocation — the owner's three readings sharpen.

GRADE RULE
  Diagnostic only; nothing here grades the lock.  Findings feed the fix.
"""
from __future__ import annotations

import math

import numpy as np

NR, NZ = 96, 192
RMAX, ZMAX = 28.0, 56.0
DR, DZ = RMAX / NR, 2.0 * ZMAX / NZ
DT = 4.0e-3
T_MAX = 25.0
R_JET, Z_JET = 4.0, 8.0

r = (np.arange(NR) + 0.5) * DR
z = -ZMAX + np.arange(NZ) * DZ
R2D = r[:, None] * np.ones((1, NZ))
Z2D = np.ones((NR, 1)) * z[None, :]

SPONGE = 1.0 / (1.0 + np.exp(-(R2D - (RMAX - 4.0)) / 0.8)) \
    + 1.0 / (1.0 + np.exp(-(np.abs(Z2D) - (ZMAX - 5.0)) / 0.8))


def laplacian(psi):
    out = np.zeros_like(psi)
    out[1:-1, :] += (psi[2:, :] - 2 * psi[1:-1, :] + psi[:-2, :]) / DR**2
    out[0, :] += (psi[1, :] - psi[0, :]) * 2.0 / DR**2
    out[-1, :] += (psi[-2, :] - psi[-1, :]) / DR**2
    out[:, 1:-1] += (psi[:, 2:] - 2 * psi[:, 1:-1] + psi[:, :-2]) / DZ**2
    out[:, 0] += (psi[:, 1] - psi[:, 0]) / DZ**2
    out[:, -1] += (psi[:, -2] - psi[:, -1]) / DZ**2
    dpsi = np.zeros_like(psi)
    dpsi[1:-1, :] = (psi[2:, :] - psi[:-2, :]) / (2 * DR)
    dpsi[-1, :] = (psi[-1, :] - psi[-2, :]) / DR
    out += dpsi / R2D
    return out


def rhs(psi):
    return -1j * (-0.5 * laplacian(psi) + (np.abs(psi) ** 2 - 1.0) * psi) \
        - 0.6 * SPONGE * (np.abs(psi) ** 2 - 1.0) * psi


def initial(vjet: float) -> np.ndarray:
    phase = vjet * Z_JET * math.sqrt(math.pi) / 2.0 \
        * np.array([[math.erf(zz / Z_JET) for zz in z]]) \
        * np.exp(-(r[:, None] / R_JET) ** 2)
    return np.exp(1j * phase).astype(complex) * 1.0


def winding_field(psi):
    th = np.angle(psi)
    d1 = np.angle(np.exp(1j * (th[1:, :-1] - th[:-1, :-1])))
    d2 = np.angle(np.exp(1j * (th[1:, 1:] - th[1:, :-1])))
    d3 = np.angle(np.exp(1j * (th[:-1, 1:] - th[1:, 1:])))
    d4 = np.angle(np.exp(1j * (th[:-1, :-1] - th[:-1, 1:])))
    return (d1 + d2 + d3 + d4) / (2 * math.pi)


def census(psi):
    w = winding_field(psi)
    rr, zz = R2D[:-1, :-1], Z2D[:-1, :-1]
    zoneA = (rr <= 2.0)
    zoneB = (rr > 2.0) & (rr < RMAX - 4.0) & (np.abs(zz) < ZMAX - 5.0)
    zoneC = ~zoneA & ~zoneB
    n = np.abs(psi) ** 2
    i, j = np.unravel_index(np.argmin(n), n.shape)
    return (int(np.rint(np.abs(w[zoneA]).sum())),
            int(np.rint(np.abs(w[zoneB]).sum())),
            int(np.rint(np.abs(w[zoneC]).sum())),
            float(n.min()), float(R2D[i, j]), float(Z2D[i, j]))


def run(vjet: float) -> None:
    print(f"\n── jet v = {vjet} (+z), half-res diagnostic")
    print("   t     |w|:axis  window  sponge   n_min   at (r, z)")
    psi = initial(vjet)
    steps = int(T_MAX / DT)
    per = int(1.0 / DT)
    found = False
    for s in range(steps + 1):
        if s % per == 0:
            a, b, c, nmin, rm, zm = census(psi)
            if a + b + c > 0 or s % (5 * per) == 0:
                print(f"   {s*DT:5.1f}   {a:5d}   {b:5d}   {c:5d}"
                      f"   {nmin:6.3f}  ({rm:5.1f}, {zm:6.1f})")
            found = found or (a + b + c > 0)
        if s == steps:
            break
        k1 = rhs(psi)
        k2 = rhs(psi + 0.5 * DT * k1)
        k3 = rhs(psi + 0.5 * DT * k2)
        k4 = rhs(psi + DT * k3)
        psi = psi + (DT / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        if not np.isfinite(psi).all():
            print(f"   BLOWUP at t = {s*DT:.2f}")
            return
    print(f"   any winding ever: {'YES' if found else 'NO'}")


def main() -> None:
    print("=" * 70)
    print("Nucleation diagnostic: where (if anywhere) do windings appear?")
    print("=" * 70)
    for vjet in (2.5, 4.0, 6.0):
        run(vjet)
    print("\nDone — findings feed the sign-lock fix; nothing here grades the lock.")


if __name__ == "__main__":
    main()
