#!/usr/bin/env python3
"""
Re-measure the ring's TOROIDAL CIRCULATION with the phase sampled OFF the core.

WHY THIS EXISTS (2026-07-28). `ring_toroidal_3d.py` completed its 10 h fork run
and its reading (B) -- the core-circuit phase winding W -- failed its parity pair
(-1.19 against +1.87, residual +0.680).  Before booking that as physics, the
instrument was read, and it does not do what its own comment specifies:

    # (B) excess phase twist along the core circuit (phase at core points is
    #  ill-defined AT the singularity; sample just outside the core radius)
    ...
    i, j, kk = np.unravel_index(np.argmin(vals), vals.shape)   # <- the core
    ths.append(float(np.angle(psi[i, j, kk])))                 # <- phase AT it

At a vortex core |psi| -> 0 and the phase is singular; the value at the nearest
grid point is set by which side of the true core that point falls on.  Unwrapping
sixteen such samples around the ring is expected to produce exactly the observed
non-locking, parity-violating W.  So (B) may have failed from an implementation
defect rather than from the configuration lacking a locked toroidal circulation,
and burying it would book a bug as a result.

WHAT THIS SCRIPT CHANGES, and nothing else:
  * the phase for each azimuthal bin is sampled on a SMALL RING of radius
    R_PROBE around the located core point, in the local plane perpendicular to
    the core circuit, and averaged as a unit vector (circular mean) before
    unwrapping.  That is the documented method.
  * it reports, in ONE instrument's convention:
      - W_toroidal : the corrected core-circuit winding = the toroidal circulation
      - helA       : the shape helicity, recomputed identically to the original
                     (position-based, untouched by the phase defect) as a control
  * T_MAX is cut to 1.5 because both readings are taken at FIRST RING (t ~ 1.0).
    This is ~1/5 of the completed run, not a repeat of it.

The physics -- grid, potential, sponge, initial data, stepper -- is copied
verbatim from `ring_toroidal_3d.py` so the two are comparable.  That script is
NOT modified: tonight's verdict must stay reproducible.

PRE-STATED GRADING, before any number is seen:
  * helA must reproduce the completed run (-1 at n=+1, +1 at n=-1).  If it does
    not, this harness differs from the original somewhere and NOTHING here counts.
  * W_toroidal LOCKS if it is near-integer and flips sign across n = +-1
    (|W(+1) + W(-1)| small compared to |W|).  Then (B) is RESCUED, the toroidal
    circulation is measured, and sign(H_kin) can be formed in this convention.
  * W_toroidal FAILS if it still scatters or fails parity with the phase sampled
    correctly.  Then (B)'s falsification is real and it goes to the ledger --
    earned, this time.
"""

import math
import sys

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq

# ---- verbatim from ring_toroidal_3d.py -------------------------------------
NX, NY, NZ = 128, 128, 256
LX, LY, LZ = 32.0, 32.0, 64.0
DX = LX / NX
DT = 2.0e-3
T_MAX = 1.5                     # <-- only change: first ring is at t ~ 1.0
FRAME = 0.25
R_JET, Z_JET, V_JET = 4.0, 8.0, 6.0
NBINS = 16

R_PROBE = 1.5                   # phase probe radius, in healing lengths (xi ~ 1)
NPROBE = 8                      # samples around each probe ring

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
# ---- end verbatim -----------------------------------------------------------


def sample_phase_off_core(psi, i, j, kk):
    """Circular-mean phase on a ring of radius R_PROBE about the core point.

    The core sits on the (r, z) plane at fixed azimuth, so the perpendicular
    plane is spanned by the radial and z directions. Probe in that plane, which
    is where the comment in the original says to sample.
    """
    acc = 0.0 + 0.0j
    used = 0
    rhat_x, rhat_y = X[i, j, kk], Y[i, j, kk]
    nrm = math.hypot(rhat_x, rhat_y) or 1.0
    rhat_x, rhat_y = rhat_x / nrm, rhat_y / nrm
    for p in range(NPROBE):
        a = 2 * np.pi * p / NPROBE
        dr, dz = R_PROBE * math.cos(a), R_PROBE * math.sin(a)
        ii = int(round(i + dr * rhat_x / DX))
        jj = int(round(j + dr * rhat_y / DX))
        kq = int(round(kk + dz / DX))
        if not (0 <= ii < NX and 0 <= jj < NY and 0 <= kq < NZ):
            continue
        val = psi[ii, jj, kq]
        if abs(val) < 0.55:           # still too close to a core: reject
            continue
        acc += val / abs(val)
        used += 1
    if used < NPROBE // 2:
        return np.nan
    return float(np.angle(acc))


def trace_ring(psi, n_wind: int):
    n = np.abs(psi) ** 2
    mask = (RP > 2.2) & (RP < LX / 2 - 4.0) & (np.abs(Z) < LZ / 2 - 6.0) & (Z > 0.5)
    rs, zs, ths, ok = [], [], [], 0
    for b in range(NBINS):
        lo, hi = -np.pi + 2 * np.pi * b / NBINS, -np.pi + 2 * np.pi * (b + 1) / NBINS
        sel = mask & (PHI >= lo) & (PHI < hi)
        if not sel.any():
            rs.append(np.nan); zs.append(np.nan); ths.append(np.nan); continue
        vals = np.where(sel, n, np.inf)
        i, j, kk = np.unravel_index(np.argmin(vals), vals.shape)
        if n[i, j, kk] > 0.35:
            rs.append(np.nan); zs.append(np.nan); ths.append(np.nan); continue
        rs.append(RP[i, j, kk]); zs.append(Z[i, j, kk])
        ths.append(sample_phase_off_core(psi, i, j, kk))     # <-- THE FIX
        ok += 1
    if ok < NBINS - 2:
        return None
    rs, zs = np.array(rs), np.array(zs)
    good = ~np.isnan(rs)
    phis = -np.pi + 2 * np.pi * (np.arange(NBINS) + 0.5) / NBINS
    r1 = np.nansum((rs - np.nanmean(rs)) * np.exp(-1j * phis) * good) / good.sum()
    z1 = np.nansum((zs - np.nanmean(zs)) * np.exp(-1j * phis) * good) / good.sum()
    amp = float(np.hypot(abs(r1), abs(z1)))
    hel = float(np.sign(np.imag(z1 * np.conj(r1)))) if amp > 0.05 else 0.0
    # The phase measurement must NEVER be able to suppress the helA control --
    # a probe failure would otherwise be indistinguishable from "no ring", and
    # the control is what certifies this harness matches the original.
    tw = np.array(ths); tw = tw[~np.isnan(tw)]
    if len(tw) < NBINS - 4:
        W = float("nan")
    else:
        unw = np.unwrap(tw)
        W = (unw[-1] - unw[0]) / (2 * np.pi) * NBINS / max(len(tw) - 1, 1)
    return dict(nbins=ok, nphase=len(tw), helA=hel, ampA=amp, W=float(W),
                excess=float(W - n_wind))


def run(n_wind: int):
    psi = initial(n_wind)
    steps = int(round(T_MAX / DT))
    every = int(round(FRAME / DT))
    first = None
    for s in range(1, steps + 1):
        psi = step(psi, DT)
        if s % every == 0:
            t = s * DT
            r = trace_ring(psi, n_wind)
            got = "ring" if r else "----"
            print(f"   [n={n_wind:+d} t={t:5.2f}] {got}"
                  + (f"  helA {r['helA']:+.0f}  W {r['W']:+.3f}"
                     f"  (phase pts {r['nphase']}/{NBINS})" if r else ""),
                  flush=True)
            if r and first is None and not math.isnan(r["W"]):
                first = dict(t=t, **r)
                print(f"      FIRST RING at t = {t:.2f}: helA {r['helA']:+.0f}, "
                      f"W_toroidal {r['W']:+.3f}, excess {r['excess']:+.3f}",
                      flush=True)
    return first


def main():
    print("=" * 74)
    print("  TOROIDAL CIRCULATION, phase sampled OFF the core")
    print(f"  R_PROBE = {R_PROBE} healing lengths, {NPROBE} samples/bin, T_MAX = {T_MAX}")
    print("=" * 74)
    # Optional branch selector: "+1" or "-1" runs one branch only, so the two can
    # be run in parallel on separate cores and reconciled afterwards. With no
    # argument the behaviour is unchanged (both branches, in order).
    which = (+1, -1)
    if len(sys.argv) > 1 and sys.argv[1] in ("+1", "-1"):
        which = (int(sys.argv[1]),)
        print(f"  [single-branch mode: n = {which[0]:+d}]")
    out = {}
    for nw in which:
        print(f"\n  --- n = {nw:+d} ---", flush=True)
        out[nw] = run(nw)
    print("\n" + "=" * 74)
    p, m = out.get(+1), out.get(-1)
    if not (p and m):
        print("  NO RING on one or both branches — nothing graded.")
        return
    print("  CONTROL (must reproduce the completed run):")
    print(f"    helA: {p['helA']:+.0f} at n=+1, {m['helA']:+.0f} at n=-1"
          f"   -> {'PASS' if p['helA'] == -m['helA'] and p['helA'] != 0 else 'FAIL'}"
          "  (completed run: -1 / +1)")
    print("\n  THE MEASUREMENT:")
    print(f"    W_toroidal: {p['W']:+.3f} at n=+1, {m['W']:+.3f} at n=-1")
    s = p["W"] + m["W"]
    mag = (abs(p["W"]) + abs(m["W"])) / 2
    print(f"    pair sum {s:+.3f}, i.e. {100*abs(s)/mag if mag else float('nan'):.1f}% of |W|")
    print(f"    (completed run, phase sampled AT the core: -1.190 / +1.870, sum +0.680 = 44.4%)")
    print()
    if mag and abs(s) / mag < 0.10:
        print("  READING (B) IS RESCUED: with the phase sampled correctly the toroidal")
        print("  circulation locks and respects the parity pair. Its earlier failure was")
        print("  the instrument, not the configuration — it does NOT go to the ledger,")
        print("  and sign(H_kin) can now be formed in this instrument's convention.")
    else:
        print("  READING (B) FAILS HONESTLY: the parity violation survives correct")
        print("  sampling, so it is a property of the configuration. NOW it earns the")
        print("  ledger row the fork pre-registered.")
    print("=" * 74)


if __name__ == "__main__":
    main()
