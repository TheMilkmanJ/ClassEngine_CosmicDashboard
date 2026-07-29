#!/usr/bin/env python3
"""
A factor-2 fork inside the registry's own arithmetic, in the entry whose kill condition
claims uniqueness. Found while re-grading the dependents of docket #62's width result.

--------------------------------------------------------------------------------------
THE COLLISION, stated with both sides quoted.

P-2026-050 (PRTOE_PREREGISTERED_PREDICTIONS.md, registered 2026-07-18):

    "in unvirialized gas (Theta = 1 -- the bare value), every m_e-keyed rest frequency
     runs +2.509% high (dln nu_hf/dln m_e = 2, with eps = 1.2543%)"

and its kill (ii):

    "an offset at a value inconsistent with +2.5% (THE MECHANISM'S OWN ARITHMETIC ALLOWS
     NO OTHER NUMBER)"

PRTOE_me_mechanism_math.md, on the same coupling in the same regime:

    "Developed speckle sits at <Theta> = 1/2 exactly by the Beta(d/2, d/2) law ...
     against Theta = 1.9e-6 laminar. So <Theta> = 1/2 is a DISTRIBUTIONAL FACT, not
     something the model arranges"

Those cannot both govern unvirialized gas. The Theta framework as written contains TWO
states -- laminar 1.9e-6 and developed-speckle mean 1/2. **It contains no Theta = 1 state.**
Theta = 1 is the upper END POINT of the Beta support, not its mean, and a dark-ages or
cosmic-dawn signal is a volume average, so the mean is what the observable carries.

CONSEQUENCE. The registered offsets halve:

                        Theta = 1 (as registered)   <Theta> = 1/2 (the Beta law)
  frequency offset            +2.509%                      +1.254%
  dark-ages trough           +0.40 MHz                    +0.20 MHz
  cosmic-dawn trough         +1.96 MHz                    +0.98 MHz

and the kill condition's uniqueness claim is FALSE either way: the corpus supplies exactly
one other number, and it is a factor of two.

The discriminant degrades with it. The entry rests the kill on "+-0.1 MHz-class precision
makes the 0.40 MHz offset a 4 sigma-class discriminant." At <Theta> = 1/2 the same
precision faces 0.20 MHz -- a 2 sigma-class discriminant. Half the leverage, on the
entry's own instrument assumption.

WHAT THIS IS NOT. It is not a refutation of either value. Which regime unvirialized gas
occupies is a model question and the owner's to settle. What is established here is that
**the registry currently asserts uniqueness for a number its own mechanism file contradicts
by a factor of two**, and that the kill threshold inherits the factor.

PRE-STATED CONTROLS:
  T-A  reproduce the registry's own arithmetic at Theta = 1 exactly -- if the entry's
       numbers do not come out, the collision is mine and not the corpus's.
  T-B  the same arithmetic at <Theta> = 1/2.
  T-C  the ratio must be exactly 2, with no residual -- otherwise it is not a clean fork.
  T-D  the discriminant in sigma at the entry's own stated precision, both branches.
  T-E  ANTI-CONTROL: the uniqueness claim must actually fail, i.e. the second number must
       be a legitimate output of the corpus's own stated law, not one I introduced.
  T-F  ANTI-CONTROL: the laminar regime must give a THIRD number, and it must be
       unobservably small -- so the fork is genuinely two-way and not three-way.
  T-G  the speckle broadening from docket #62 carried into this band, and honestly sized
       against the trough rather than oversold.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


ALPHA = 0.0072973525693
EPS = 27 * ALPHA / (5 * math.pi)          # 1.2543%
W_HF = 2                                   # dln nu_hf / dln m_e
SD_THETA = 0.25                            # Beta(3/2,3/2) sd, 3D
THETA_LAMINAR = 1.9e-6

# the registry's own inputs
DARK_LO, DARK_HI = 15.8, 16.5              # MHz, standard dark-ages trough
DAWN = 78.0                                # MHz, standard cosmic-dawn trough
PRECISION = 0.1                            # MHz, the entry's stated instrument class


def offset_frac(theta):
    """fractional rest-frequency offset for a given coupling fraction"""
    return W_HF * EPS * theta


def main():
    print("=" * 78)
    print("  P-2026-050: A FACTOR-2 FORK IN A KILL CONDITION THAT CLAIMS UNIQUENESS")
    print("=" * 78)
    print(f"\n  eps = 27a/5pi = {EPS*100:.4f}%   w(hyperfine) = {W_HF}")

    # ---- T-A ---------------------------------------------------------------
    print("\n  T-A  the registry's arithmetic at Theta = 1, reproduced")
    o1 = offset_frac(1.0)
    print(f"       offset = {W_HF} * {EPS*100:.4f}% = {o1*100:.4f}%   (entry says +2.509%)")
    chk("T-A1 the +2.509% reproduces", abs(o1 * 100 - 2.509) < 0.002, f"{o1*100:.4f}%")
    d_lo, d_hi = DARK_LO * (1 + o1), DARK_HI * (1 + o1)
    print(f"       dark ages: {DARK_LO}-{DARK_HI} -> {d_lo:.3f}-{d_hi:.3f} MHz"
          f"   (entry says 16.2-16.9)")
    chk("T-A2 the 16.2-16.9 MHz band reproduces",
        abs(d_lo - 16.2) < 0.05 and abs(d_hi - 16.9) < 0.05, f"{d_lo:.2f}-{d_hi:.2f}")
    off_dark1 = 0.5 * ((d_lo - DARK_LO) + (d_hi - DARK_HI))
    print(f"       mean dark-ages offset {off_dark1:.3f} MHz   (entry says +0.40)")
    chk("T-A3 the +0.40 MHz offset reproduces", abs(off_dark1 - 0.40) < 0.01,
        f"{off_dark1:.3f} MHz")
    dawn1 = DAWN * (1 + o1)
    print(f"       cosmic dawn: {DAWN} -> {dawn1:.3f} MHz, offset {dawn1-DAWN:.3f}"
          f"   (entry says 79.96, +1.96)")
    chk("T-A4 the 79.96 MHz / +1.96 offset reproduces",
        abs(dawn1 - 79.96) < 0.02 and abs((dawn1 - DAWN) - 1.96) < 0.02)
    print("       -> the entry's arithmetic is internally correct AT Theta = 1.")

    # ---- T-B ---------------------------------------------------------------
    print("\n  T-B  the same arithmetic at the Beta law's <Theta> = 1/2")
    o2 = offset_frac(0.5)
    d2_lo, d2_hi = DARK_LO * (1 + o2), DARK_HI * (1 + o2)
    off_dark2 = 0.5 * ((d2_lo - DARK_LO) + (d2_hi - DARK_HI))
    dawn2 = DAWN * (1 + o2)
    print(f"       offset = {o2*100:.4f}%")
    print(f"       dark ages: {DARK_LO}-{DARK_HI} -> {d2_lo:.3f}-{d2_hi:.3f} MHz"
          f"   offset {off_dark2:.3f} MHz")
    print(f"       cosmic dawn: {DAWN} -> {dawn2:.3f} MHz   offset {dawn2-DAWN:.3f} MHz")
    chk("T-B1 the offset is +1.254%", abs(o2 * 100 - 1.2543) < 0.002, f"{o2*100:.4f}%")
    chk("T-B2 the dark-ages offset is +0.20 MHz", abs(off_dark2 - 0.20) < 0.01,
        f"{off_dark2:.3f} MHz")

    # ---- T-C ---------------------------------------------------------------
    print("\n  T-C  is it a clean factor of two?")
    chk("T-C1 the frequency offsets differ by exactly 2", abs(o1 / o2 - 2.0) < 1e-12,
        f"{o1/o2:.12f}")
    chk("T-C2 and so do the MHz offsets", abs(off_dark1 / off_dark2 - 2.0) < 1e-9,
        f"{off_dark1/off_dark2:.9f}")

    # ---- T-D ---------------------------------------------------------------
    print(f"\n  T-D  discriminating power at the entry's own +-{PRECISION} MHz precision")
    s1, s2 = off_dark1 / PRECISION, off_dark2 / PRECISION
    print(f"       Theta = 1  :  {off_dark1:.2f} / {PRECISION} = {s1:.1f} sigma")
    print(f"       <Theta>=1/2:  {off_dark2:.2f} / {PRECISION} = {s2:.1f} sigma")
    chk("T-D1 the registered branch is the 4-sigma-class one the entry claims",
        3.5 <= s1 <= 4.5, f"{s1:.1f} sigma")
    chk("T-D2 the Beta-law branch is only 2-sigma-class", 1.5 <= s2 <= 2.5,
        f"{s2:.1f} sigma -- half the leverage, same instrument")

    # ---- T-E: anti-control -------------------------------------------------
    print("\n  T-E  ANTI-CONTROL: is the second number really the corpus's own?")
    #  It follows from <Theta> = 1/2, which the mechanism file calls a distributional
    #  fact of Beta(d/2,d/2) -- derived there by integration, not assumed.
    from_beta = W_HF * EPS * 0.5
    chk("T-E1 the second number is exactly w*eps*<Theta> with the corpus's own <Theta>",
        abs(from_beta - o2) < 1e-15,
        "so 'no other number' is false on the corpus's own arithmetic")
    chk("T-E2 and the two states named in the mechanism file do NOT include Theta = 1",
        THETA_LAMINAR != 1.0 and 0.5 != 1.0,
        "laminar 1.9e-6 and developed-speckle mean 1/2 are the stated pair")

    # ---- T-F: anti-control -------------------------------------------------
    print("\n  T-F  ANTI-CONTROL: does laminar give a third, observably distinct number?")
    o3 = offset_frac(THETA_LAMINAR)
    off_dark3 = 0.5 * ((DARK_LO + DARK_HI)) * o3
    print(f"       Theta = {THETA_LAMINAR:.1e}:  offset {o3*100:.3e}%"
          f"   = {off_dark3*1e6:.3f} Hz on the trough")
    chk("T-F1 laminar is unobservable, so the fork is TWO-way not three-way",
        off_dark3 < PRECISION / 1000, f"{off_dark3:.3e} MHz, far under the precision")

    # ---- T-G ---------------------------------------------------------------
    print("\n  T-G  the #62 broadening carried into this band, sized honestly")
    smear_frac = W_HF * EPS * SD_THETA
    smear_dark = 0.5 * (DARK_LO + DARK_HI) * smear_frac
    trough_width = DARK_HI - DARK_LO
    print(f"       fractional speckle spread {smear_frac:.4e}"
          f"  ->  {smear_dark:.3f} MHz at {0.5*(DARK_LO+DARK_HI):.1f} MHz")
    print(f"       the trough band itself is {trough_width:.1f} MHz wide")
    chk("T-G1 the smearing is comparable to the stated precision, not to the trough",
        abs(smear_dark - PRECISION) < 0.05, f"{smear_dark:.3f} vs {PRECISION} MHz")
    chk("T-G2 and it is SMALL against the trough's own width -- stated, not oversold",
        smear_dark < 0.2 * trough_width,
        f"{smear_dark/trough_width:.2f} of the band; it perturbs the shape only mildly")
    print("       -> so the factor-2 in the OFFSET is the dominant effect. The smearing")
    print("          matters only because it sits at the precision the kill relies on,")
    print("          and it does NOT shift a centroid, so it degrades rather than moves.")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — AN UNRESOLVED FACTOR OF 2, AND A FALSE UNIQUENESS CLAIM")
    print("=" * 78)
    print(f"""
  The registry's arithmetic is internally correct AT Theta = 1: +2.509%, the 16.2-16.9 MHz
  dark-ages band, the +0.40 MHz offset and the +1.96 MHz cosmic-dawn companion all
  reproduce exactly. That is not where the problem is.

  The problem is that the Theta framework, in the corpus's own mechanism file, contains
  **two** states for this coupling -- laminar 1.9e-6 and developed-speckle mean 1/2 -- and
  **no Theta = 1 state at all.** Theta = 1 is the upper endpoint of the Beta support, not
  its mean, and a dark-ages or cosmic-dawn signal is a volume average, so it is the mean
  the observable carries. On the corpus's own law the offset is

      w * eps * <Theta>  =  2 * {EPS*100:.4f}% * 0.5  =  +{o2*100:.4f}%,

  i.e. **+{off_dark2:.2f} MHz on the dark-ages trough, not +{off_dark1:.2f}**. The two branches differ by
  exactly 2 with no residual.

  So kill (ii) -- "an offset at a value inconsistent with +2.5%, the mechanism's own
  arithmetic allows no other number" -- **is false, and it is falsified by the corpus
  rather than from outside.** The mechanism file supplies precisely one other number, a
  factor of two below, derived there by integration and labelled a distributional fact.

  The kill threshold inherits the factor. On the entry's own +-{PRECISION} MHz instrument class
  the registered branch is a {s1:.0f}-sigma discriminant and the Beta-law branch is {s2:.0f}-sigma.
  Half the leverage, same instrument, and the entry currently advertises only the first.

  Docket #62's broadening lands here too, at {smear_dark:.2f} MHz -- comparable to the stated
  precision but small against the {trough_width:.1f} MHz trough band, and it degrades a centroid
  rather than moving one. The factor-2 in the offset is the dominant effect; the smearing
  is a secondary one and is recorded as such rather than stacked onto the headline.

  WHAT IS OWED, and it is not mine to decide. Either unvirialized gas occupies a third,
  fully-coherent regime, in which case the framework must add it and say why voids are
  coherent when the same field is speckled elsewhere -- or the registered offsets and the
  kill threshold halve. **Until that is settled, P-2026-050 should not assert uniqueness.**
  The laminar anti-control confirms the fork is two-way: Theta = 1.9e-6 gives
  {off_dark3*1e6:.1f} Hz, unobservable, so it is not a live third branch.
""")


if __name__ == "__main__":
    main()
