#!/usr/bin/env python3
"""Price the two BBN supersessions by measurement, not by proportionality argument.

WHAT IS BEING PRICED. The booked BBN numbers were produced at eps = 1.24% and T_c = 179 keV.
Both inputs have since moved: T_c was re-pinned to the kernel-sourced 177.10 keV, and the
derived amendment is eps = 1.2543%. Neither has been re-run through the network.

HOW IT WAS PRICED BEFORE. PRTOE_CODE_MANIFEST.md priced the T_c move by assuming D/H's window
contribution is proportional to the ramp stamp at the deuterium bottleneck: the stamp moves
0.6089 -> 0.6047 (0.69%), so the window's +0.645% becomes +0.641%, so D/H moves 0.002 sigma.
That is an argument, not a measurement -- it assumes strict proportionality to the bottleneck
stamp and ignores the rest of the network's response.

WHY IT CANNOT BE PRICED BY A SINGLE PAIR OF RUNS. PRyM is bit-for-bit deterministic but its
D/H output is not smooth in its inputs at the ~0.1% level (see prym_omega_b_elasticity.py).
Both supersessions are themselves ~0.007% effects on D/H -- more than ten times BELOW that
non-smoothness. Differencing two runs therefore measures the solver, not the physics:

  single-pair T_c 0.179 -> 0.17710 : -0.034 sigma      } both are ~10x too large, and are
  single-pair eps 1.24 -> 1.2543   : +0.038 sigma      } the non-smoothness, not the step

THE METHOD. Scan each input over a range wide enough that the true response clears the
non-smoothness, fit a slope, then evaluate the actual (tiny) step from the fitted slope. The
fit residuals independently re-measure the non-smoothness: 0.064% and 0.121% of D/H here,
consistent with the ~0.1% found on the omega_b axis.

RECORDED SCANS (`prym_ramped_splice.py <shift> <T_c> 1.0`, numba on, PRyM pivot omega_b):

  T_c scan, eps fixed 1.24%        eps scan, T_c fixed 0.179
  T_c/MeV    D/H x1e5              eps/%      D/H x1e5
  0.150      2.470831              0.00       2.454439
  0.165      2.472999              0.60       2.467205
  0.179      2.472118              1.24       2.472118
  0.193      2.472825              1.90       2.481448
  0.210      2.477419              2.50       2.484393

THE RESULT.

  T_c: slope +0.0898 +/- 0.0328 (D/H per MeV); step -0.00190 MeV -> -0.0036 +/- 0.0013 sigma
  eps: slope +0.0118 +/- 0.0015 (D/H per % m_e); step +0.0143 pp -> +0.0035 +/- 0.0004 sigma

Both confirm the booked prices (0.002 and 0.004 sigma) at the same order; the eps price is
reproduced almost exactly. And the two moves carry OPPOSITE signs and near-equal magnitude, so
applying both together is a net **-0.00005 sigma, zero to within +/-0.0014** (the error dominated
by the T_c slope, a 36% measurement of an already negligible number). The supersessions are free,
and now by measurement rather than by proportionality argument.

Usage:
  python3 scripts/prym_supersession_pricing.py            # refit the recorded scans
  python3 scripts/prym_supersession_pricing.py --rerun    # re-run PRyM (10 runs, ~10 min)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SPLICE = ROOT / "scripts" / "prym_ramped_splice.py"

WIDTH = 0.047634        # the standing two-term D/H width
DH_STANDING = 2.387     # the standing prediction, for converting % -> sigma

AS_RUN_TC, NEW_TC = 0.179, 0.17710        # MeV
AS_RUN_EPS, NEW_EPS = 1.24, 1.2543        # % of m_e

TC_SCAN = [(0.150, 2.470831), (0.165, 2.472999), (0.179, 2.472118),
           (0.193, 2.472825), (0.210, 2.477419)]
EPS_SCAN = [(0.00, 2.454439), (0.60, 2.467205), (1.24, 2.472118),
            (1.90, 2.481448), (2.50, 2.484393)]


def run(shift, tc):
    r = subprocess.run([sys.executable, str(SPLICE), str(shift), str(tc), "1.0"],
                       capture_output=True, text=True)
    line = [ln for ln in r.stdout.splitlines() if ln.startswith("RAMPED")]
    if not line:
        raise SystemExit(f"no RAMPED line for shift={shift} T_c={tc}:\n{r.stderr[-800:]}")
    return float(line[0].split()[8])


def price(points, step, label, unit):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    p, cov = np.polyfit(x, y, 1, cov=True)
    slope, sig = float(p[0]), float(np.sqrt(cov[0, 0]))
    resid = y - np.polyval(p, x)
    sd = float(resid.std(ddof=2))
    d, e = slope * step, sig * abs(step)
    print(f"\n  {label}")
    print(f"    slope            : {slope:+.5f} +/- {sig:.5f}  D/H per {unit}")
    print(f"    fit residual sd  : {sd:.5f}  ({100*sd/DH_STANDING:.3f}% of D/H "
          f"-- the solver's non-smoothness, re-measured)")
    print(f"    step             : {step:+.5f} {unit}")
    print(f"    price            : {100*d/DH_STANDING:+.4f}% of D/H = "
          f"**{d/WIDTH:+.4f} sigma** (+/- {e/WIDTH:.4f})")
    return d / WIDTH


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rerun", action="store_true")
    args = ap.parse_args()

    tc_pts, eps_pts = TC_SCAN, EPS_SCAN
    if args.rerun:
        print("re-running T_c scan ...", flush=True)
        tc_pts = [(t, run(1.0 + AS_RUN_EPS / 100.0, t)) for t, _ in TC_SCAN]
        print("re-running eps scan ...", flush=True)
        eps_pts = [(e, run(1.0 + e / 100.0, AS_RUN_TC)) for e, _ in EPS_SCAN]
        for lab, pts in (("T_c", tc_pts), ("eps", eps_pts)):
            print(f"  {lab}: " + " ".join(f"({a:g},{b:.6f})" for a, b in pts))

    print("=" * 74)
    print("BBN SUPERSESSION PRICING — measured over wide baselines, not differenced")
    print("=" * 74)

    s_tc = price(tc_pts, NEW_TC - AS_RUN_TC, f"T_c  {AS_RUN_TC} -> {NEW_TC} MeV", "MeV")
    s_eps = price(eps_pts, NEW_EPS - AS_RUN_EPS,
                  f"eps  {AS_RUN_EPS}% -> {NEW_EPS}%", "% m_e")

    print(f"\n  BOTH APPLIED TOGETHER: {s_tc + s_eps:+.6f} sigma "
          f"-- the two moves nearly cancel.")
    print(f"  Against the standing width +/-{WIDTH:.4f}, that is "
          f"1 part in {int(abs(1/(s_tc+s_eps))) if abs(s_tc+s_eps)>1e-9 else float('inf')}.")
    print("\n  For contrast, differencing single pairs (what the non-smoothness returns):")
    print(f"    T_c: {(2.470512-2.472118)/WIDTH:+.4f} sigma      "
          f"eps: {(2.473914-2.472118)/WIDTH:+.4f} sigma")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
