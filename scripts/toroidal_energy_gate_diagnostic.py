"""Is the toroidal run's energy drift the SPONGE, or is it integrator error?

Owner decision #6 asks whether ring_toroidal_3d.py's third quotability gate -- energy drift <= 2%
per run -- can be met at all, given the integrator carries an explicit dissipative term
`psi -= 0.4 dt SPONGE (n-1) psi` whose job is to absorb the fountain's radiation at the box edge.

THE PRECEDENT THAT MAKES THIS WORTH MEASURING. The adaptive spherical rebound run
(bounce_reconstruction_rp.md sec.23) failed the SAME 2% bar with energy errors of 22-1817%, and was
recorded as "numerically unresolved by this method at this resolution" -- the verdict fell back to
the honest endpoint. So the corpus takes this bar seriously and has buried a run on it before.
Re-scoping it for the toroidal run therefore needs evidence, not an argument, and the evidence has
to distinguish two causes that share one symptom:

    (a) UNCONTROLLED INTEGRATOR ERROR -- the split-step is under-resolved. Gate failure is real,
        the numbers are not trustworthy, and the spherical precedent applies directly.
    (b) DESIGNED DISSIPATION -- the sponge is removing energy on purpose. Gate failure is an
        artifact of measuring a closed-system quantity on an open system, and the parity test
        (a RELATIVE comparison across n = +-1) is untouched by it.

These are separable by one experiment: run the same initial condition with the sponge on and with
the sponge off, and compare the drift. If (b), sponge-off conserves and sponge-on drifts.

Run at reduced resolution (64x64x128) so the diagnostic costs minutes rather than hours; the
QUESTION -- which term removes the energy -- does not depend on grid size, and the per-step drift
rate is reported so the comparison is like-for-like.

Run: python3 scripts/toroidal_energy_gate_diagnostic.py
"""
import math
import time

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq

NX, NY, NZ = 64, 64, 128            # the production run is 128x128x256
LX, LY, LZ = 32.0, 32.0, 64.0
DX = LX / NX
DT = 2.0e-3
STEPS = 200
R_JET, Z_JET, V_JET = 4.0, 8.0, 6.0

x = (np.arange(NX) - NX // 2) * DX
y = (np.arange(NY) - NY // 2) * DX
z = (np.arange(NZ) - NZ // 2) * DX
X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
RP = np.sqrt(X ** 2 + Y ** 2)
PHI = np.arctan2(Y, X)

kx = 2 * np.pi * fftfreq(NX, DX)
ky = 2 * np.pi * fftfreq(NY, DX)
kz = 2 * np.pi * fftfreq(NZ, DX)
KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing="ij")
K2 = KX ** 2 + KY ** 2 + KZ ** 2

edge = 1.0 / (1.0 + np.exp(-(RP - (LX / 2 - 3.0)) / 0.7)) \
    + 1.0 / (1.0 + np.exp(-(np.abs(Z) - (LZ / 2 - 4.0)) / 0.7))
SPONGE = np.clip(edge, 0.0, 2.0)

XC, YC = LX / 2 - 1.0, LY / 2 - 1.0


def initial(n_wind=1):
    phi_anti = np.arctan2(Y - YC, X - XC)
    theta_bg = n_wind * (PHI - phi_anti)
    core = RP / np.sqrt(RP ** 2 + 2.0)
    ramp = np.vectorize(math.erf)(Z / Z_JET)
    theta_jet = V_JET * Z_JET * math.sqrt(math.pi) / 2.0 * ramp * np.exp(-(RP / R_JET) ** 2)
    return (core * np.exp(1j * (theta_bg + theta_jet))).astype(np.complex64)


def step(psi, dt, sponge_on):
    n = np.abs(psi) ** 2
    psi = psi * np.exp(-0.5j * dt * (n - 1.0)).astype(np.complex64)
    psi = ifftn(fftn(psi) * np.exp(-0.5j * dt * K2)).astype(np.complex64)
    n = np.abs(psi) ** 2
    psi = psi * np.exp(-0.5j * dt * (n - 1.0)).astype(np.complex64)
    if sponge_on:
        psi = psi - 0.4 * dt * SPONGE * (n - 1.0) * psi
    return psi


def energy(psi):
    g = fftn(psi)
    kin = 0.5 * np.sum(K2 * np.abs(g) ** 2) / (NX * NY * NZ)
    pot = 0.5 * np.sum((np.abs(psi) ** 2 - 1.0) ** 2)
    return float(kin.real + pot) * DX ** 3


print("=" * 78)
print("THE SAME INITIAL CONDITION, SPONGE ON AND SPONGE OFF")
print("=" * 78)
print(f"  grid {NX}x{NY}x{NZ} (production is 128x128x256), dt = {DT}, {STEPS} steps"
      f" -> t = {STEPS*DT}")
print()
print(f"  {'configuration':<22} {'E(0)':>13} {'E(end)':>13} {'drift':>10} {'per step':>12}")
print("  " + "-" * 74)
res = {}
for label, on in (("sponge ON (as run)", True), ("sponge OFF", False)):
    psi = initial()
    e0 = energy(psi)
    t0 = time.time()
    for _ in range(STEPS):
        psi = step(psi, DT, on)
    e1 = energy(psi)
    d = abs(e1 - e0) / abs(e0)
    res[label] = d
    print(f"  {label:<22} {e0:13.5f} {e1:13.5f} {d*100:9.4f}% {d/STEPS*100:11.6f}%")
    print(f"  {'':22} ({time.time()-t0:.0f} s)")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
on_d, off_d = res["sponge ON (as run)"], res["sponge OFF"]
print(f"  drift with the sponge     {on_d*100:9.4f}%")
print(f"  drift without it          {off_d*100:9.4f}%")
if off_d > 0:
    print(f"  ratio                     {on_d/off_d:9.1f}x")
print()
if off_d < 0.02 and on_d > 5 * max(off_d, 1e-12):
    print("  CAUSE (b): DESIGNED DISSIPATION. With the absorbing term removed the integrator")
    print("  conserves energy to within the gate, and switching it on reproduces the drift. The")
    print("  2% bar is therefore measuring the sponge, not the numerics, and it cannot be met by")
    print("  any run that uses an absorbing boundary -- which this instrument does by design,")
    print("  because a periodic box without one reflects the fountain's radiation back onto the")
    print("  ring it is trying to measure.")
    print()
    print("  This is NOT the spherical rebound run's situation. There the energy error was the")
    print("  integrator failing at 22-1817% with no dissipative term to blame, and burying the")
    print("  result was correct. Here the same symptom has a different cause, and the")
    print("  distinguishing measurement is the one above.")
    print()
    print("  RECOMMENDATION unchanged and now evidenced: re-scope gate (iii) to the physical")
    print("  region interior to the sponge, which is what it was written to protect. The parity")
    print("  test across n = +-1 is a RELATIVE comparison and a common dissipation cancels from")
    print("  it, so the fork's actual content survives either ruling.")
elif off_d >= 0.02:
    print("  CAUSE (a): the integrator does NOT conserve energy even with the sponge removed.")
    print("  The gate is measuring real numerical error and the spherical precedent applies")
    print("  directly: the run should be treated as unresolved at this resolution, and the")
    print("  recommendation in owner item 6 is WITHDRAWN.")
else:
    print("  INCONCLUSIVE at this resolution and step count -- neither cause is cleanly")
    print("  separated. Report as-is; do not rule on it from this evidence.")
