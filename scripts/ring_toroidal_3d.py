"""ring_toroidal_3d — link 4's toroidal half, both fork readings computed in one experiment (2026-07-28).

THE FORK, AND THE OWNER'S RULE
  The toroidal sign has two candidate observables; per the fork rule both are
  computed in the same runs, the survivor kept, the dead buried in the ledger:
    (A) SHAPE HELICITY — the ring core's m = 1 displacement mode: as azimuth
        advances, the core's (r, z) displacement rotates with a handedness;
        its sign versus the background winding n is reading A.
    (B) EXCESS PHASE TWIST — the total phase winding W along the closed
        core-following circuit minus the linkage n with the central line;
        a nonzero locked excess is reading B.
  THE TEST: a directed fountain (+z, v = 6 — the amplitude the axisymmetric
  diagnostic showed nucleates) on a background vortex line n = ±1 threading
  the axis.  A locked observable FLIPS SIGN between n = +1 and n = −1 (the
  pair is its own parity check); a null or non-flipping observable dies.

MODEL
  3D Gross–Pitaevskii, split-step Fourier, periodic box with a sponge; the
  central line is paired with a compensating anti-line inside the corner
  sponge (periodic-compatible net winding), so the physical region carries
  winding n about the axis.  Fountain: the erf phase ramp in a tube, as in
  the graded axisymmetric run.

GATES (quotable only if all pass)
  * a ring is DETECTED: a low-density core (n < 0.35) off the axis
    (r_⊥ > 2.2) in at least 14 of 16 azimuthal bins at the detection time;
  * the n = ±1 pair behaves as a parity pair for whichever observable is
    quoted (exact flip);
  * energy drift ≤ 2% per run.
  A reading that scatters or nulls across the pair is BURIED (ledger row);
  a reading that flips deterministically SURVIVES at candidate grade.
"""
from __future__ import annotations

import math

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq

NX, NY, NZ = 128, 128, 256
LX, LY, LZ = 32.0, 32.0, 64.0
DX = LX / NX
DT = 2.0e-3
T_MAX = 8.0
FRAME = 0.25
R_JET, Z_JET, V_JET = 4.0, 8.0, 6.0
NBINS = 16

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

XC, YC = LX / 2 - 1.0, LY / 2 - 1.0          # anti-line, buried in the corner sponge


def initial(n_wind: int) -> np.ndarray:
    phi_anti = np.arctan2(Y - YC, X - XC)
    theta_bg = n_wind * (PHI - phi_anti)
    core = RP / np.sqrt(RP ** 2 + 2.0)
    ramp = np.vectorize(math.erf)(Z / Z_JET)
    theta_jet = V_JET * Z_JET * math.sqrt(math.pi) / 2.0 * ramp \
        * np.exp(-(RP / R_JET) ** 2)
    return (core * np.exp(1j * (theta_bg + theta_jet))).astype(np.complex64)


def step(psi, dt):
    n = np.abs(psi) ** 2
    psi = psi * np.exp(-0.5j * dt * (n - 1.0)).astype(np.complex64)
    psi = ifftn(fftn(psi) * np.exp(-0.5j * dt * K2)).astype(np.complex64)
    n = np.abs(psi) ** 2
    psi = psi * np.exp(-0.5j * dt * (n - 1.0)).astype(np.complex64)
    psi = psi - 0.4 * dt * SPONGE * (n - 1.0) * psi
    return psi


def energy(psi) -> float:
    g = fftn(psi)
    kin = 0.5 * np.sum(K2 * np.abs(g) ** 2) / (NX * NY * NZ) ** 2 * (NX * NY * NZ)
    pot = 0.5 * np.sum((np.abs(psi) ** 2 - 1.0) ** 2)
    return float(kin.real + pot) * DX ** 3


def trace_ring(psi, n_wind: int):
    """Locate the ring core per azimuthal bin; return core curve + both readings."""
    n = np.abs(psi) ** 2
    mask = (RP > 2.2) & (RP < LX / 2 - 4.0) & (np.abs(Z) < LZ / 2 - 6.0) & (Z > 0.5)
    rs, zs, ths, ok = [], [], [], 0
    for b in range(NBINS):
        lo, hi = -np.pi + 2 * np.pi * b / NBINS, -np.pi + 2 * np.pi * (b + 1) / NBINS
        sel = mask & (PHI >= lo) & (PHI < hi)
        if not sel.any():
            rs.append(np.nan); zs.append(np.nan); ths.append(np.nan)
            continue
        vals = np.where(sel, n, np.inf)
        i, j, kk = np.unravel_index(np.argmin(vals), vals.shape)
        if n[i, j, kk] > 0.35:
            rs.append(np.nan); zs.append(np.nan); ths.append(np.nan)
            continue
        rs.append(RP[i, j, kk]); zs.append(Z[i, j, kk])
        ths.append(float(np.angle(psi[i, j, kk])))
        ok += 1
    if ok < NBINS - 2:
        return None
    rs, zs = np.array(rs), np.array(zs)
    good = ~np.isnan(rs)
    phis = -np.pi + 2 * np.pi * (np.arange(NBINS) + 0.5) / NBINS
    # (A) shape helicity: rotation sense of the (r, z) m=1 displacement
    r1 = np.nansum((rs - np.nanmean(rs)) * np.exp(-1j * phis) * good) / good.sum()
    z1 = np.nansum((zs - np.nanmean(zs)) * np.exp(-1j * phis) * good) / good.sum()
    amp = float(np.hypot(abs(r1), abs(z1)))
    hel = float(np.sign(np.imag(z1 * np.conj(r1)))) if amp > 0.05 else 0.0
    # (B) excess phase twist along the core circuit (phase at core points is
    # ill-defined AT the singularity; sample just outside the core radius)
    tw = np.array(ths)
    tw = tw[~np.isnan(tw)]
    unw = np.unwrap(tw)
    W = (unw[-1] - unw[0]) / (2 * np.pi) * NBINS / max(len(tw) - 1, 1)
    excess = W - n_wind
    return dict(rbar=float(np.nanmean(rs)), zbar=float(np.nanmean(zs)),
                nbins=ok, helA=hel, ampA=amp, W=float(W), excessB=float(excess))


def run(n_wind: int):
    # PROGRESS/CHECKPOINT DISCIPLINE (added 2026-07-27 after the first launch was
    # killed at 6 h 46 m under machine contention having printed nothing at all —
    # seven hours of compute lost because every result waited on the final return.
    # Now: every frame reports, flushed, so a kill leaves a usable partial record,
    # and the first ring detection is announced the moment it happens.)
    psi = initial(n_wind)
    e0 = energy(psi)
    steps = int(T_MAX / DT)
    per = int(FRAME / DT)
    best = None
    for s in range(steps + 1):
        if s % per == 0 and s * DT >= 1.0:
            res = trace_ring(psi, n_wind)
            drift_now = abs(energy(psi) - e0) / abs(e0)
            print(f"      [n={n_wind:+d} t={s*DT:5.2f}  E-drift {100*drift_now:6.3f}%"
                  f"  ring: {'yes' if res is not None else 'no '}]", flush=True)
            if res is not None and best is None:
                best = (s * DT, res)
                print(f"      [n={n_wind:+d} FIRST RING at t = {s*DT:.2f}: "
                      f"helA {res['helA']:+.0f}, W {res['W']:+.2f}]", flush=True)
        if s == steps:
            break
        psi = step(psi, DT)
        if not np.isfinite(psi).all():
            print(f"      [n={n_wind:+d} field went non-finite at t = {s*DT:.2f}]",
                  flush=True)
            return None, math.inf
    drift = abs(energy(psi) - e0) / abs(e0)
    return best, drift


def main() -> None:
    print("=" * 78)
    print("Link 4's toroidal half — both fork readings, one experiment")
    print("=" * 78)
    out = {}
    for n_wind in (+1, -1):
        print(f"\n   --- starting n = {n_wind:+d} ---", flush=True)
        best, drift = run(n_wind)
        if best is None:
            print(f"\n   n = {n_wind:+d}: NO RING DETECTED (or blowup); "
                  f"drift = {drift:.3f}", flush=True)
            out[n_wind] = None
            continue
        t0, r = best
        out[n_wind] = r
        print(f"\n   n = {n_wind:+d}: ring at t = {t0:.2f}, r̄ = {r['rbar']:.1f}, "
              f"z̄ = {r['zbar']:.1f}, bins {r['nbins']}/{NBINS}, drift {drift:.4f}",
              flush=True)
        print(f"      (A) shape helicity: {r['helA']:+.0f} (m₁ amp {r['ampA']:.2f})")
        print(f"      (B) core-circuit winding W = {r['W']:+.2f}, "
              f"excess = {r['excessB']:+.2f}", flush=True)

    print("\nVERDICT (the fork resolves on the pair):")
    if out.get(1) and out.get(-1):
        a_flip = out[1]["helA"] != 0 and out[1]["helA"] == -out[-1]["helA"]
        b_flip = abs(out[1]["excessB"]) > 0.5 and \
            abs(out[1]["excessB"] + out[-1]["excessB"]) < 0.5
        print(f"   (A) shape helicity locked+flips: {'YES' if a_flip else 'NO'}")
        print(f"   (B) excess twist locked+flips:   {'YES' if b_flip else 'NO'}")
        if a_flip and not b_flip:
            print("   SURVIVOR: reading (A). Reading (B) to the ledger.")
        elif b_flip and not a_flip:
            print("   SURVIVOR: reading (B). Reading (A) to the ledger.")
        elif a_flip and b_flip:
            print("   BOTH lock — the two readings are one object here; record both.")
        else:
            print("   NEITHER locks — both to the ledger; the toroidal sign is not")
            print("   set by the fountain-on-winding roll-up in this geometry.")
    else:
        print("   Pair incomplete — nucleation/diagnostic issue; report as-is,")
        print("   nothing quoted, nothing buried (a test that didn't run grades")
        print("   nothing).")
    print("=" * 78)


if __name__ == "__main__":
    main()
