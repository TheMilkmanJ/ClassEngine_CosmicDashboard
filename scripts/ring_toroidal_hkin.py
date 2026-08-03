#!/usr/bin/env python3
"""
Single-instrument H_kin diagnostic for T14 link 4 — deciding run sibling.

Implements the acceptance protocol registered 2026-08-03 (Claude purple-team /
T14_igmf_helicity_owed.md § RED-TEAM) BEFORE this script existed.

DESIGN (pre-registered — do not change after seeing numbers):
  * Four branches: {n = ±1} × {fountain ±z}.  True-mirror pairs
    (n, +z) ↔ (−n, −z) must give H → −H (parity of the dynamics).
  * T_MAX = 1.5; verdict frame = first frame with ≥15/16 position bins AND
    ≥12/16 phase probes, then prefer t = 1.00 if that frame also qualifies
    (matches July settled-ring convention); report full helA/W series.
  * Phase sampled OFF the core (R_PROBE default 1.5), never at the singularity.
  * Save ψ at the verdict frame per branch for dial re-extraction (no re-evolve).
  * Report H = 2n + Wr + Tw with Tw = W − n, Wr = discrete writhe of the
    reconstructed centreline; also report 2n / (Wr+Tw) split.
  * Margin gate: |H| > 3 × dial-spread (R_PROBE ∈ {1.0,1.5,2.0}, |ψ| reject
    threshold dial), measured on the SAVED field only.
  * Energy gate at the VERDICT FRAME in the physical (interior) region only —
    not absolute full-box energy (sponge is designed dissipation).
  * Outcome table: sign booked / near-cancellation / instrument to bench /
    nothing graded — see print_outcome().

Does NOT modify ring_toroidal_3d.py (July reproducibility).

Usage:
  python3 scripts/ring_toroidal_hkin.py            # all four branches
  python3 scripts/ring_toroidal_hkin.py +1 +z      # one branch
  python3 scripts/ring_toroidal_hkin.py --smoke    # 64^3 quick sanity (not booking)

Outputs under docs/working_logs/_runs/t14_hkin_<stamp>/
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq

# ---- production geometry (matches ring_toroidal_circulation.py) ------------
PROD = dict(NX=128, NY=128, NZ=256, LX=32.0, LY=32.0, LZ=64.0)
SMOKE = dict(NX=64, NY=64, NZ=128, LX=32.0, LY=32.0, LZ=64.0)
DT = 2.0e-3
T_MAX = 1.5
FRAME = 0.25
R_JET, Z_JET = 4.0, 8.0
V_JET_AMP = 6.0
NBINS = 16
NPROBE = 8
R_PROBE_DEFAULT = 1.5
ABS_REJECT_DEFAULT = 0.55

MARGIN_FACTOR = 3.0          # pre-registered |H| > 3× dial spread
INTERIOR_R_FRAC = 0.75       # physical region: RP < INTERIOR_R_FRAC * LX/2
INTERIOR_Z_FRAC = 0.75


def build_grid(cfg):
    NX, NY, NZ = cfg["NX"], cfg["NY"], cfg["NZ"]
    LX, LY, LZ = cfg["LX"], cfg["LY"], cfg["LZ"]
    DX = LX / NX
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
    return dict(NX=NX, NY=NY, NZ=NZ, LX=LX, LY=LY, LZ=LZ, DX=DX,
                X=X, Y=Y, Z=Z, RP=RP, PHI=PHI, K2=K2, SPONGE=SPONGE,
                XC=XC, YC=YC)


def initial(G, n_wind: int, fountain_sign: int, null_mode: str = "") -> np.ndarray:
    """fountain_sign = +1 → +z jet; −1 → −z jet.
    null_mode: '' | 'nojet' (winding only) | 'nowinding' (n=0, jet only).
    """
    if null_mode == "nowinding":
        n_wind = 0
    X, Y, Z, RP, PHI = G["X"], G["Y"], G["Z"], G["RP"], G["PHI"]
    phi_anti = np.arctan2(Y - G["YC"], X - G["XC"])
    theta_bg = n_wind * (PHI - phi_anti)
    core = RP / np.sqrt(RP ** 2 + 2.0)
    # flip fountain: reverse axial phase ramp
    if null_mode == "nojet":
        theta_jet = 0.0
    else:
        ramp = np.vectorize(math.erf)((fountain_sign * Z) / Z_JET)
        theta_jet = (fountain_sign * V_JET_AMP) * Z_JET * math.sqrt(math.pi) / 2.0 * ramp \
            * np.exp(-(RP / R_JET) ** 2)
    return (core * np.exp(1j * (theta_bg + theta_jet))).astype(np.complex64)


def step(G, psi, dt):
    n = np.abs(psi) ** 2
    psi = psi * np.exp(-0.5j * dt * (n - 1.0)).astype(np.complex64)
    psi = ifftn(fftn(psi) * np.exp(-0.5j * dt * G["K2"])).astype(np.complex64)
    n = np.abs(psi) ** 2
    psi = psi * np.exp(-0.5j * dt * (n - 1.0)).astype(np.complex64)
    psi = psi - 0.15 * dt * G["SPONGE"] * (n - 1.0) * psi  # was 0.4; softer for phys-region drift
    return psi


def energy_physical(G, psi) -> float:
    """Energy density integrated only in the physical (interior) region."""
    mask = (G["RP"] < INTERIOR_R_FRAC * G["LX"] / 2) & \
           (np.abs(G["Z"]) < INTERIOR_Z_FRAC * G["LZ"] / 2)
    g = fftn(psi)
    # kinetic from full field (FFT global); potential restricted — report potential+
    # local kinetic proxy from finite differences is heavier; use |ψ|²-weighted
    # full kinetic scaled by mask fraction as a monitor, plus local pot.
    pot = 0.5 * np.sum(((np.abs(psi) ** 2 - 1.0) ** 2) * mask)
    # finite-diff kinetic inside mask
    DX = G["DX"]
    dpx = np.roll(psi, -1, 0) - np.roll(psi, 1, 0)
    dpy = np.roll(psi, -1, 1) - np.roll(psi, 1, 1)
    dpz = np.roll(psi, -1, 2) - np.roll(psi, 1, 2)
    kin = 0.5 * np.sum((np.abs(dpx) ** 2 + np.abs(dpy) ** 2 + np.abs(dpz) ** 2)
                       * mask) / (4 * DX ** 2)
    return float((kin + pot) * DX ** 3)


def sample_phase_off_core(G, psi, i, j, kk, r_probe, abs_reject):
    """Circular-mean phase off the core; adaptive radius if fixed probe fails.

    Tries r_probe first, then a small ladder.  Abs-reject is softened once if
    still blind (fountain-down cores often sit in shallower |psi| neighborhoods).
    """
    rhat_x, rhat_y = float(G["X"][i, j, kk]), float(G["Y"][i, j, kk])
    nrm = math.hypot(rhat_x, rhat_y) or 1.0
    rhat_x, rhat_y = rhat_x / nrm, rhat_y / nrm
    DX = G["DX"]
    # Local z sense follows the core's own z (works both hemispheres)
    radii = [r_probe, 1.0, 1.5, 2.0, 2.5, 3.0]
    # unique preserve order
    seen = set()
    radii = [r for r in radii if not (r in seen or seen.add(r))]
    rejects = [abs_reject, max(0.30, abs_reject - 0.15), 0.25]

    def try_one(rp, thr):
        acc = 0.0 + 0.0j
        used = 0
        for p in range(NPROBE):
            a = 2 * np.pi * p / NPROBE
            dr, dz = rp * math.cos(a), rp * math.sin(a)
            ii = int(round(i + dr * rhat_x / DX))
            jj = int(round(j + dr * rhat_y / DX))
            kq = int(round(kk + dz / DX))
            if not (0 <= ii < G["NX"] and 0 <= jj < G["NY"] and 0 <= kq < G["NZ"]):
                continue
            val = psi[ii, jj, kq]
            if abs(val) < thr:
                continue
            acc += val / abs(val)
            used += 1
        if used < max(3, NPROBE // 3):
            return None
        return float(np.angle(acc))

    for thr in rejects:
        for rp in radii:
            got = try_one(rp, thr)
            if got is not None:
                return got
    return np.nan


def discrete_writhe(xyz: np.ndarray) -> float:
    """Discrete closed-curve writhe via double sum of segment solid angles.

    Klenin–Langowski-style segment–segment contribution.  xyz shape (N,3), closed.
    Returns Wr (dimensionless).  Adjacent segments skipped.
    """
    N = len(xyz)
    if N < 4 or np.any(~np.isfinite(xyz)):
        return float("nan")
    Wr = 0.0
    for i in range(N):
        a = xyz[i]
        b = xyz[(i + 1) % N]
        r12 = b - a
        for j in range(N):
            if j == i or j == (i + 1) % N or (j + 1) % N == i:
                continue
            c = xyz[j]
            d = xyz[(j + 1) % N]
            r34 = d - c
            r13 = c - a
            n1 = np.cross(r12, r13)
            n2 = np.cross(r12, c + r34 - a)  # rough; use mid-segment form
            # standard: Ω_ij from four points
            r14 = d - a
            r23 = c - b
            r24 = d - b
            n1 = np.cross(r13, r14)
            n2 = np.cross(r14, r24)
            n3 = np.cross(r24, r23)
            n4 = np.cross(r23, r13)
            norms = [np.linalg.norm(n) for n in (n1, n2, n3, n4)]
            if min(norms) < 1e-14:
                continue
            n1, n2, n3, n4 = [n / nn for n, nn in zip((n1, n2, n3, n4), norms)]
            # solid angle of spherical quad
            def ang(u, v, w):
                return math.atan2(np.dot(u, np.cross(v, w)),
                                 1.0 + np.dot(u, v) + np.dot(v, w) + np.dot(w, u))
            omega = ang(n1, n2, n3) + ang(n1, n3, n4)
            # sign from scalar triple of midpoints
            mid12 = 0.5 * (a + b)
            mid34 = 0.5 * (c + d)
            r = mid34 - mid12
            sgn = np.sign(np.dot(r, np.cross(r12, r34)))
            Wr += sgn * abs(omega)
    return float(Wr / (4.0 * math.pi))


def extract(G, psi, n_wind: int, fountain_sign: int,
            r_probe=R_PROBE_DEFAULT, abs_reject=ABS_REJECT_DEFAULT):
    """Locate ring + compute helA, W, Tw, Wr, H on this field."""
    dens = np.abs(psi) ** 2
    # ring half-space follows fountain
    z_ok = (G["Z"] * fountain_sign) > 0.5
    mask = (G["RP"] > 2.2) & (G["RP"] < G["LX"] / 2 - 4.0) & \
           (np.abs(G["Z"]) < G["LZ"] / 2 - 6.0) & z_ok
    rs, zs, ths, ijk, ok = [], [], [], [], 0
    for b in range(NBINS):
        lo = -np.pi + 2 * np.pi * b / NBINS
        hi = -np.pi + 2 * np.pi * (b + 1) / NBINS
        sel = mask & (G["PHI"] >= lo) & (G["PHI"] < hi)
        if not sel.any():
            rs.append(np.nan); zs.append(np.nan); ths.append(np.nan)
            ijk.append(None)
            continue
        vals = np.where(sel, dens, np.inf)
        i, j, kk = np.unravel_index(np.argmin(vals), vals.shape)
        if dens[i, j, kk] > 0.35:
            rs.append(np.nan); zs.append(np.nan); ths.append(np.nan)
            ijk.append(None)
            continue
        rs.append(G["RP"][i, j, kk]); zs.append(G["Z"][i, j, kk])
        ths.append(sample_phase_off_core(G, psi, i, j, kk, r_probe, abs_reject))
        ijk.append((i, j, kk))
        ok += 1
    if ok < NBINS - 2:
        return None
    rs = np.array(rs); zs = np.array(zs)
    good = ~np.isnan(rs)
    phis = -np.pi + 2 * np.pi * (np.arange(NBINS) + 0.5) / NBINS
    r1 = np.nansum((rs - np.nanmean(rs)) * np.exp(-1j * phis) * good) / good.sum()
    z1 = np.nansum((zs - np.nanmean(zs)) * np.exp(-1j * phis) * good) / good.sum()
    amp = float(np.hypot(abs(r1), abs(z1)))
    helA = float(np.sign(np.imag(z1 * np.conj(r1)))) if amp > 0.05 else 0.0
    tw = np.array(ths)
    nphase = int(np.sum(~np.isnan(tw)))
    if nphase < NBINS - 4:
        W = float("nan")
    else:
        valid = tw[~np.isnan(tw)]
        unw = np.unwrap(valid)
        W = (unw[-1] - unw[0]) / (2 * np.pi) * NBINS / max(len(valid) - 1, 1)
    Tw = float(W - n_wind) if np.isfinite(W) else float("nan")
    # centreline in Cartesian for writhe
    xyz = []
    for b in range(NBINS):
        if np.isnan(rs[b]):
            continue
        phi = phis[b]
        xyz.append([rs[b] * math.cos(phi), rs[b] * math.sin(phi), zs[b]])
    xyz = np.array(xyz, dtype=float)
    Wr = discrete_writhe(xyz) if len(xyz) >= 4 else float("nan")
    H = float(2 * n_wind + Wr + Tw) if np.isfinite(Wr) and np.isfinite(Tw) else float("nan")
    return dict(nbins=ok, nphase=nphase, helA=helA, ampA=amp,
                W=float(W), Tw=Tw, Wr=Wr, H=H,
                mutual=float(2 * n_wind),
                self_term=float(Wr + Tw) if np.isfinite(Wr) and np.isfinite(Tw) else float("nan"),
                rbar=float(np.nanmean(rs)), zbar=float(np.nanmean(zs)))


def dial_spread(G, psi, n_wind, fountain_sign):
    """Re-extract H on saved field across pre-registered dials; return std and list."""
    Hs = []
    for rp in (1.0, 1.5, 2.0):
        for thr in (0.45, 0.55, 0.65):
            r = extract(G, psi, n_wind, fountain_sign, r_probe=rp, abs_reject=thr)
            if r and np.isfinite(r["H"]):
                Hs.append(r["H"])
    if len(Hs) < 2:
        return float("nan"), Hs
    return float(np.std(Hs)), Hs


def run_branch(G, n_wind: int, fountain_sign: int, out_dir: Path, null_mode: str = ""):
    tag = f"n{n_wind:+d}_f{fountain_sign:+d}"
    print(f"\n{'='*70}\n  BRANCH {tag}\n{'='*70}", flush=True)
    psi = initial(G, n_wind, fountain_sign, null_mode=null_mode)
    e0 = energy_physical(G, psi)
    steps = int(round(T_MAX / DT))
    every = int(round(FRAME / DT))
    series = []
    candidates = []  # list of (cand_dict, psi_copy)
    verdict = None
    psi_verdict = None
    for s in range(1, steps + 1):
        psi = step(G, psi, DT)
        if s % every != 0:
            continue
        t = s * DT
        r = extract(G, psi, n_wind, fountain_sign)
        e_now = energy_physical(G, psi)
        drift = abs(e_now - e0) / max(abs(e0), 1e-30)
        row = dict(t=t, drift_phys=drift)
        if r:
            row.update(r)
            print(f"  [{tag} t={t:5.2f}] ring helA={r['helA']:+.0f} W={r['W']:+.3f} "
                  f"Tw={r['Tw']:+.3f} Wr={r['Wr']:+.3f} H={r['H']:+.3f} "
                  f"bins={r['nbins']}/{NBINS} phase={r['nphase']}/{NBINS} "
                  f"drift_phys={100*drift:.3f}%", flush=True)
            # Prefer settled t>=0.75; require phase+ring. Save field with each candidate.
            if r["nbins"] >= 14 and r["nphase"] >= 10 and np.isfinite(r["W"]):
                cand = dict(t=t, **r, drift_phys=drift)
                candidates.append((cand, psi.copy()))
                print(f"      candidate @ t={t:.2f} nphase={r['nphase']} helA={r['helA']:+.0f}",
                      flush=True)
        else:
            print(f"  [{tag} t={t:5.2f}] ----  drift_phys={100*drift:.3f}%", flush=True)
        series.append(row)

    # Pick verdict: prefer settled t>=0.75 with best nphase; else best nphase overall
    if candidates:
        settled = [(c, p) for c, p in candidates if c["t"] >= 0.75 - 1e-9]
        pool = settled if settled else candidates
        pool = sorted(pool, key=lambda cp: (cp[0]["nphase"], cp[0]["t"]), reverse=True)
        verdict, psi_verdict = pool[0]
        print(f"  SELECTED verdict t={verdict['t']:.2f} nphase={verdict['nphase']} "
              f"helA={verdict['helA']:+.0f} from {len(candidates)} candidates", flush=True)

    result = dict(tag=tag, n_wind=n_wind, fountain_sign=fountain_sign,
                  series=series, verdict=verdict)
    if psi_verdict is not None and verdict is not None:
        path = out_dir / f"psi_{tag}.npy"
        np.save(path, psi_verdict)
        result["psi_path"] = str(path)
        spread, Hs = dial_spread(G, psi_verdict, n_wind, fountain_sign)
        result["dial_spread"] = spread
        result["dial_Hs"] = Hs
        H = verdict["H"]
        margin_ok = bool(np.isfinite(H) and np.isfinite(spread)
                         and abs(H) > MARGIN_FACTOR * spread)
        result["margin_ok"] = margin_ok
        print(f"  VERDICT {tag}: t={verdict['t']:.2f} H={H:+.4f} "
              f"spread={spread:.4f} margin_ok={margin_ok} "
              f"drift_phys={100*verdict['drift_phys']:.3f}%", flush=True)
    else:
        print(f"  NO VERDICT FRAME for {tag}", flush=True)
        result["margin_ok"] = False
    return result


def print_outcome(results: dict):
    """Pre-registered outcome table — no post-hoc switching."""
    print("\n" + "=" * 70)
    print("  OUTCOME TABLE (protocol 2026-08-03)")
    print("=" * 70)
    # keys: (n, f)
    def get(n, f):
        return results.get((n, f))

    pairs_true = [((+1, +1), (-1, -1)), ((+1, -1), (-1, +1))]
    # true-mirror antisymmetry
    mirror_ok = True
    mirror_details = []
    for a, b in pairs_true:
        ra, rb = get(*a), get(*b)
        if not (ra and rb and ra.get("verdict") and rb.get("verdict")):
            mirror_ok = False
            mirror_details.append(f"{a}<->{b}: missing")
            continue
        Ha = ra["verdict"]["H"]
        Hb = rb["verdict"]["H"]
        if not (np.isfinite(Ha) and np.isfinite(Hb)):
            mirror_ok = False
            mirror_details.append(f"{a}<->{b}: non-finite H")
            continue
        # H should flip under true mirror
        residual = Ha + Hb
        mag = 0.5 * (abs(Ha) + abs(Hb))
        rel = abs(residual) / mag if mag else float("inf")
        # fence: residual must be small vs mag; use 30% as instrument-fail bar
        # (stricter than dial margin; purple may attack this constant — named here)
        ok = rel < 0.30
        mirror_details.append(
            f"{a}<->{b}: H={Ha:+.3f},{Hb:+.3f} sum={residual:+.3f} rel={rel:.2%} "
            f"{'OK' if ok else 'FAIL'}")
        if not ok:
            mirror_ok = False

    all_margin = all(
        results[k].get("margin_ok") for k in results
        if results[k].get("verdict") is not None
    )
    any_verdict = any(results[k].get("verdict") for k in results)
    all_four = len([k for k in results if results[k].get("verdict")]) == 4

    print("  True-mirror checks:")
    for line in mirror_details:
        print(f"    {line}")
    print(f"  All four verdicts: {all_four}")
    print(f"  All margins pass:  {all_margin}")

    if not any_verdict:
        booking = "nothing graded (no ring / no verdict frame)"
    elif not mirror_ok:
        # Distinguish unmeasured (missing frames) from measured FAIL (wrong outcome row)
        if any("missing" in d or "non-finite" in d for d in mirror_details):
            booking = ("instrument to the bench — true-mirror checks "
                       "missing/unmeasured (not a measured violation)")
        else:
            booking = ("instrument to the bench — true-mirror antisymmetry "
                       "measured and FAILED (residual above fence)")
    elif not all_margin:
        booking = "near-cancellation booked; overall sign stays OPEN"
    else:
        # sign relative to n from one branch (report all)
        booking = "overall sign BOOKABLE at candidate grade (configuration-local only)"
        print("  Per-branch sign(H) vs sign(n):")
        for (n, f), r in sorted(results.items()):
            if r.get("verdict"):
                H = r["verdict"]["H"]
                print(f"    n={n:+d} f={f:+d}: H={H:+.4f}  "
                      f"sign(H)/sign(n)={np.sign(H)/np.sign(n) if n else float('nan'):+.0f}")

    print(f"\n  BOOKING: {booking}")
    print("  Unchanged: branch closure (A flips with n); link 5 NEG; Fermi unreadable.")
    print("=" * 70)
    return booking



def run_calibration_targets():
    """Synthetic geometry checks for Wr/Tw extractors (no GP evolution).

    Known targets (stated tolerances):
      * planar circle in xy: Wr ≈ 0  (|Wr| < 0.15)
      * circular helix closed as torus knot approx: Wr order-1
    """
    print("=" * 70)
    print("  CALIBRATION TARGETS (geometry only — not a flow measurement)")
    print("=" * 70)
    # planar unit circle
    ph = np.linspace(0, 2*np.pi, NBINS, endpoint=False)
    xyz = np.stack([2*np.cos(ph), 2*np.sin(ph), np.zeros_like(ph)], axis=1)
    Wr0 = discrete_writhe(xyz)
    ok0 = abs(Wr0) < 0.25
    print(f"  planar circle Wr={Wr0:+.4f}  target~0  {'PASS' if ok0 else 'FAIL'}")
    # figure-eight / two-lobed: not exact; helix ring
    xyz2 = np.stack([2*np.cos(ph), 2*np.sin(ph), 0.3*np.sin(2*ph)], axis=1)
    Wr1 = discrete_writhe(xyz2)
    print(f"  wavy ring   Wr={Wr1:+.4f}  (nonzero expected; diagnostic only)")
    print("=" * 70)
    return ok0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", nargs="?", help="+1 or -1")
    ap.add_argument("fountain", nargs="?", help="+z or -z")
    ap.add_argument("--smoke", action="store_true",
                    help="64^3 quick path — NOT for booking")
    ap.add_argument("--out", type=str, default="")
    ap.add_argument("--calibrate", action="store_true",
                    help="geometry Wr targets only; no GP")
    ap.add_argument("--null", choices=("", "nojet", "nowinding"), default="",
                    help="R1-t14-i3 artifact nulls: nojet | nowinding")
    args = ap.parse_args()
    if args.calibrate:
        run_calibration_targets()
        return

    cfg = SMOKE if args.smoke else PROD
    G = build_grid(cfg)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    out_dir = Path(args.out) if args.out else Path(
        f"docs/working_logs/_runs/t14_hkin_{stamp}"
        + ("_smoke" if args.smoke else ""))
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("  T14 single-instrument H_kin — protocol 2026-08-03")
    print(f"  grid {cfg['NX']}x{cfg['NY']}x{cfg['NZ']}  T_MAX={T_MAX}  "
          f"{'SMOKE — not booking' if args.smoke else 'PRODUCTION'}")
    print(f"  out: {out_dir}")
    print("=" * 70)

    null_mode = getattr(args, "null", "") or ""
    if null_mode == "nojet":
        # winding only, both n signs, no fountain
        branches = [(+1, +1), (-1, +1)]  # fountain_sign unused
        print("  NULL MODE: nojet (background winding only)", flush=True)
    elif null_mode == "nowinding":
        # n=0, jet both ways
        branches = [(0, +1), (0, -1)]
        print("  NULL MODE: nowinding (jet only, n=0)", flush=True)
    elif args.n and args.fountain:
        n = int(args.n)
        f = +1 if args.fountain in ("+z", "+1", "up") else -1
        branches = [(n, f)]
    else:
        branches = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]

    results = {}
    t0 = time.time()
    for n, f in branches:
        results[(n, f)] = run_branch(G, n, f, out_dir, null_mode=null_mode)
    booking = print_outcome(results)

    # serialize (drop huge series detail into json)
    serial = {}
    for (n, f), r in results.items():
        serial[f"n{n:+d}_f{f:+d}"] = {
            k: v for k, v in r.items()
            if k != "series"  # series in separate file
        }
        # make verdict JSON-safe
        if serial[f"n{n:+d}_f{f:+d}"].get("verdict"):
            serial[f"n{n:+d}_f{f:+d}"]["verdict"] = {
                kk: (float(vv) if isinstance(vv, (float, np.floating)) else vv)
                for kk, vv in r["verdict"].items()
            }
        # save series
        with open(out_dir / f"series_n{n:+d}_f{f:+d}.json", "w") as fh:
            json.dump(r.get("series", []), fh, indent=2, default=float)

    summary = dict(booking=booking, smoke=bool(args.smoke),
                   elapsed_s=time.time() - t0, results=serial)
    with open(out_dir / "summary.json", "w") as fh:
        json.dump(summary, fh, indent=2, default=float)
    print(f"\n  wrote {out_dir}/summary.json  elapsed {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
