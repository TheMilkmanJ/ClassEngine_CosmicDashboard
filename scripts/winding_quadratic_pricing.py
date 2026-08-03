#!/usr/bin/env python3
"""
#55: what can be said about c_w WITHOUT the un-built family-coupling Lagrangian.

The docket asks to derive c_w, the winding-response quadratic coefficient in

    dm/m = |x| + c_w x^2 + O(x^3),      x = eps cos(theta)

from the family-coupling Lagrangian.  The corpus records that Lagrangian as
UN-BUILT, so the derivation is not available and this script does not attempt
one.  What IS available at the desk, and is done here:

  (1) the expansion's own convergence -- is the series even trustworthy at the
      values being quoted?  (a control on the whole framing)
  (2) whether the two recorded determinations of c_w actually conflict
  (3) what c_w equals for the natural SATURATING response forms -- a PRICING of
      the plausible range, explicitly NOT a derivation and not to be quoted as one
  (4) the size of the neglected cubic term, so "leading-order dominates" has a
      number rather than an adjective

Pre-stated control: an exactly-linear response (mass strictly proportional to the
rectified amplitude) must return c_w = 0.  Any method that does not reproduce
that is broken.
"""

import math

TWO_OVER_PI = 2.0 / math.pi
EPS = 0.012543  # the recorded amplitude, 1.2543%

# the two recorded determinations
CW_FIT = -1.80              # fit-implied, no stated uncertainty
CW_ENS, CW_ENS_ERR = -0.84, 0.52  # winding ensemble (n >= 4)


def fbar_eff(c_w, eps=EPS):
    """f_bar_eff = 2/pi + c_w * eps / 2."""
    return TWO_OVER_PI + c_w * eps / 2.0


def main():
    print("=" * 76)
    print("  #55: pricing c_w without the Lagrangian that would derive it")
    print("=" * 76)

    # ---- (0) control -------------------------------------------------------
    print("\n  CONTROL (stated before anything else):")
    print(f"    exactly-linear response -> c_w = 0 -> f_bar_eff = {fbar_eff(0):.6f}")
    print(f"    2/pi                                        = {TWO_OVER_PI:.6f}")
    ok = abs(fbar_eff(0) - TWO_OVER_PI) < 1e-15
    print(f"    identical: {'PASS' if ok else 'FAIL'}")

    # ---- (1) convergence ---------------------------------------------------
    print("\n  (1) IS THE EXPANSION TRUSTWORTHY AT THESE VALUES?")
    print("      the series is in |c_w x|, and |x| <= eps, so the worst-case ratio of")
    print("      the quadratic term to the linear one is |c_w| * eps:")
    print(f"      {'c_w':>8} {'|c_w|*eps':>12} {'verdict':>14}")
    for c in (CW_ENS, CW_FIT, -3.0, -10.0, -80.0):
        r = abs(c) * EPS
        v = "safe" if r < 0.05 else ("marginal" if r < 0.2 else "SERIES BREAKS")
        print(f"      {c:8.2f} {r:12.4f} {v:>14}")
    print("      -> at both recorded values the quadratic term is a few percent of the")
    print("         linear one.  The expansion is not the weak point.")

    # ---- (2) do the two determinations conflict? ---------------------------
    print("\n  (2) DO THE TWO RECORDED VALUES CONFLICT?")
    sigma = abs(CW_FIT - CW_ENS) / CW_ENS_ERR
    print(f"      fit-implied      c_w = {CW_FIT:.2f}   (no stated uncertainty)")
    print(f"      winding ensemble c_w = {CW_ENS:.2f} +/- {CW_ENS_ERR:.2f}")
    print(f"      separation = {sigma:.2f} sigma  (corpus records 1.9)")
    print("      -> a real tension but not a contradiction, and it CANNOT be resolved")
    print("         by more precision on the ensemble alone: the fit-implied value")
    print("         carries no error bar, so the gap has only one measured side.")

    # ---- (3) natural saturating forms --------------------------------------
    print("\n  (3) WHAT c_w DO THE NATURAL SATURATING FORMS GIVE?")
    print("      PRICING ONLY -- these are candidate response shapes, not derivations.")
    print("      Each is expanded about |x| = 0 and its x^2 coefficient read off.")
    print(f"      {'response dm/m':<26} {'c_w':>8} {'cubic':>9} {'vs ensemble':>13}")
    print("      " + "-" * 60)
    forms = [
        ("|x|                  (linear)", 0.0, 0.0),
        ("1 - exp(-|x|)", -0.5, 1.0 / 6.0),
        ("ln(1 + |x|)", -0.5, 1.0 / 3.0),
        ("|x| / (1 + |x|)", -1.0, 1.0),
        ("tanh(|x|)", 0.0, -1.0 / 3.0),
        ("|x| / sqrt(1 + x^2)", 0.0, -0.5),
        ("|x| / (1 + 2|x|)", -2.0, 4.0),
    ]
    for name, cw, cub in forms:
        n = abs(cw - CW_ENS) / CW_ENS_ERR
        print(f"      {name:<26} {cw:8.3f} {cub:9.3f} {n:11.2f}s")
    print("      -> the simple one-scale saturating forms cluster on c_w in [-1, -1/2],")
    print("         which sits inside the ensemble's band and BELOW the fit-implied")
    print("         -1.80.  Forms reaching -1.80 need a saturation scale ~2x sharper")
    print("         than the amplitude itself.  Recorded as a shape constraint, not a value.")

    # ---- (4) the neglected cubic -------------------------------------------
    print("\n  (4) HOW BIG IS THE TERM BEING NEGLECTED?")
    # <|cos|> = 2/pi, <cos^2> = 1/2, <|cos|^3> = 4/(3pi)
    m1, m2, m3 = TWO_OVER_PI, 0.5, 4.0 / (3.0 * math.pi)
    print(f"      moments: <|cos|> = {m1:.6f}, <cos^2> = {m2:.4f}, <|cos|^3> = {m3:.6f}")
    print(f"      {'term':<12} {'contribution to <dm/m>/eps':>30} {'rel. to leading':>18}")
    lead = m1
    quad = CW_ENS * EPS * m2
    cub = 1.0 * EPS**2 * m3  # unit cubic coefficient
    print(f"      {'linear':<12} {lead:30.8f} {'1':>18}")
    print(f"      {'quadratic':<12} {quad:30.8f} {abs(quad/lead):18.2e}")
    print(f"      {'cubic (c=1)':<12} {cub:30.8f} {abs(cub/lead):18.2e}")
    print(f"      -> 'leading-order dominates' is worth {abs(quad/lead)*100:.2f}% at the")
    print(f"         quadratic order and {abs(cub/lead)*100:.5f}% at the cubic.  The cubic is")
    print("         irrelevant; the whole residual is the x^2 term, as the docket assumes.")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 76)
    print(f"""  VERDICT ON #55

  The derivation asked for is NOT AVAILABLE and this script does not fake one.
  The corpus states plainly that the family-coupling Lagrangian is un-built, and
  c_w is a property of that Lagrangian.  #55 is therefore model-building, not
  desk work, and belongs with the other un-built-mechanism dockets.

  What the desk can hand the eventual derivation, so it starts with a target:

    * the expansion is safe -- |c_w|*eps is a few percent at every value in play,
      so no result here is threatened by the series itself;
    * the two determinations sit {sigma:.1f} sigma apart and the gap has only ONE
      measured side, so sharpening the ensemble cannot close it;
    * simple one-scale saturating responses give c_w in [-1, -1/2]; reaching the
      fit-implied -1.80 requires a saturation scale about twice as sharp as the
      amplitude.  A derived Lagrangian landing outside [-2, 0] would be in
      tension with BOTH determinations at once, which is a usable kill;
    * the cubic term is {abs(cub/lead)*100:.5f}% -- the residual is the x^2 term and
      nothing else, so the derivation only has to produce one number.
""")
    print("=" * 76)


if __name__ == "__main__":
    main()
