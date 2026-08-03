#!/usr/bin/env python3
"""
#82 — what is the factor 10 in g = 10*eps?

THE DOCKET. "g = 10 eps = 54 alpha/pi awaits its mechanism -- the S8 rotation-shed
coupling's closed form is firewalled, not derived." The closed form matches the
minimiser's fitted g ~ 0.12 at about 4.5%, and is deliberately NOT used in the fit.
What has never been said is what the 10 IS.

WHAT THE CORPUS ALREADY FIXES. The amplitude is a product of three factors, each
with its own referee (PRTOE_MATH_SPINE.md):

    eps = c * fbar * alpha_c = (9/10) * (2/pi) * (3 alpha) = 27 alpha / (5 pi)

and the first factor is a census, stated there explicitly:

    "c = 9/10 -- a counting fraction (N-1)/N over the universal charged-fermion
     roster: 9 charged species plus the vacuum's own seat, the neutrinos sitting on
     the seat rather than in the count"

So N = 10: nine charged species plus one vacuum seat, and c is the fraction of
seats that are charged species.

THE OBSERVATION. Substituting,

    g = 10 * eps = 10 * (9/10) * fbar * alpha_c = 9 * fbar * alpha_c
                 = (N - 1) * fbar * alpha_c

The 10 cancels the census denominator EXACTLY. So the two quantities are not two
independent numbers with a coincidental ratio -- they are the SAME sum, counted two
ways:

    eps = the PER-SEAT AVERAGE   (total over 9 species, divided by all 10 seats)
    g   = the UNNORMALISED TOTAL (the same 9 species, not divided at all)

and therefore g / eps = N, the roster size, rather than a free integer.

WHAT THIS IS AND IS NOT. It is NOT a derivation of g. The empirical content is a
fit, g ~ 0.12, and 10*eps = 0.12543 sits 4.5% away; nothing here closes that. What
it does is REPLACE the question. "Why 10?" was unanswerable because 10 looked like a
bare integer. "Why does the S8 rotation-shed coupling see the TOTAL when the
electron-mass shift sees the AVERAGE?" is a question about normalisation --
answerable in principle from how each observable sums over the roster, and of the
same kind as questions the corpus already settles.

PRE-STATED CONTROLS:
  G-A  the three factors must reproduce eps = 27 alpha/(5 pi) exactly.
  G-B  10*eps must equal 54 alpha/pi exactly.
  G-C  the cancellation must be exact: 10 * (9/10) = 9 = N - 1.
  G-D  ANTI-CONTROL, and the important one: the reading must be FALSIFIABLE. If the
       census had a different N, g = N*eps would give a different number. Check that
       N = 10 is the only roster size consistent with the recorded closed form
       g = 54 alpha/pi -- otherwise "10 = N" is unconstrained and means nothing.
  G-E  state the residual against the fit honestly rather than burying it.
"""

import math

ALPHA = 1 / 137.035999084
TOL = 1e-12
_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def main():
    print("=" * 78)
    print("  #82 — THE FACTOR 10 IN g = 10*eps IS THE ROSTER SIZE N")
    print("=" * 78)

    N = 10                      # 9 charged species + the vacuum's own seat
    c = (N - 1) / N             # the democratic counting fraction
    fbar = 2 / math.pi          # the winding average
    alpha_c = 3 * ALPHA         # the composite coupling

    eps = c * fbar * alpha_c
    g = 10 * eps

    print(f"\n  N        = {N}   (9 charged species + 1 vacuum seat)")
    print(f"  c        = (N-1)/N = {c}")
    print(f"  fbar     = 2/pi = {fbar:.9f}")
    print(f"  alpha_c  = 3 alpha = {alpha_c:.9f}")
    print(f"  eps      = {eps:.9f}  ({100*eps:.4f} %)")
    print(f"  g = 10*eps = {g:.9f}")

    print("\n  G-A  the three factors reproduce eps = 27 alpha / (5 pi)")
    chk("G-A1 eps = 27a/(5pi)", abs(eps - 27 * ALPHA / (5 * math.pi)) < TOL,
        f"{eps:.12f} vs {27*ALPHA/(5*math.pi):.12f}")

    print("\n  G-B  and 10*eps = 54 alpha / pi")
    chk("G-B1 g = 54a/pi", abs(g - 54 * ALPHA / math.pi) < TOL,
        f"{g:.12f} vs {54*ALPHA/math.pi:.12f}")

    print("\n  G-C  the cancellation is exact: the 10 kills the census denominator")
    chk("G-C1 10 * c = N - 1 = 9", abs(10 * c - (N - 1)) < TOL, f"10*c = {10*c}")
    chk("G-C2 so g = (N-1) * fbar * alpha_c", abs(g - (N - 1) * fbar * alpha_c) < TOL,
        "g is the UNNORMALISED total; eps is the per-seat average")
    chk("G-C3 and g/eps = N exactly", abs(g / eps - N) < 1e-9, f"g/eps = {g/eps:.12f}")

    # ---- G-D: is "10 = N" falsifiable, or does any N work? -----------------
    print("\n  G-D  ANTI-CONTROL: is N = 10 forced, or would any roster do?")
    target = 54 * ALPHA / math.pi
    hits = []
    for n in range(2, 41):
        cc = (n - 1) / n
        gg = n * cc * fbar * alpha_c        # = (n-1)*fbar*alpha_c
        if abs(gg - target) < 1e-9:
            hits.append(n)
    chk("G-D1 exactly one roster size reproduces g = 54a/pi", hits == [N],
        f"solutions: {hits}")
    print("       -> so 'the 10 is N' is a constrained claim, not a relabelling:")
    print("          a different roster would give a different g, and does.")
    # show the neighbours, to make the constraint visible
    for n in (9, 10, 11):
        gg = (n - 1) * fbar * alpha_c
        print(f"          N = {n:2d}  ->  g = {gg:.6f}   ({100*(gg-target)/target:+.1f}% vs recorded)")

    # ---- G-E: the honest residual -----------------------------------------
    print("\n  G-E  the residual against the fit, stated not buried")
    g_fit = 0.12
    chk("G-E1 the closed form sits 4-5% above the minimiser's fitted g",
        0.03 < abs(g - g_fit) / g_fit < 0.06,
        f"closed form {g:.5f} vs fitted {g_fit:.3f}  ->  {100*(g-g_fit)/g_fit:+.1f}%")

    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  ALL CONTROLS PASS")
    print("=" * 78)
    print(f"""
  THE FACTOR 10 IS NOT A BARE INTEGER. It is N, the roster size the census already
  fixes -- nine charged species plus the vacuum's own seat. Substituting,

      eps = c * fbar * alpha_c        = (N-1)/N * fbar * alpha_c   -- PER-SEAT AVERAGE
      g   = 10 * eps = (N-1) * fbar * alpha_c                      -- UNNORMALISED TOTAL

  so g/eps = N exactly, and the 10 is the same 10 that sits in the denominator of
  c = 9/10. The two quantities are one sum counted two ways.

  IT IS FALSIFIABLE, WHICH IS WHY IT IS WORTH RECORDING (G-D). Exactly one roster
  size reproduces the recorded g = 54 alpha/pi; N = 9 and N = 11 both miss, so the
  identification is constrained rather than a relabelling.

  WHAT IS STILL OWED, AND IT IS A DIFFERENT QUESTION NOW. Not "why 10?" -- that is
  answered, the 10 is N. The open question is:

      WHY DOES THE S8 ROTATION-SHED COUPLING SEE THE TOTAL WHEN THE ELECTRON-MASS
      SHIFT SEES THE AVERAGE?

  That is a question about how each observable sums over the roster -- normalisation,
  not numerology -- and it is the same kind of question the corpus settles elsewhere.

  AND THE RESIDUAL STANDS. The closed form is {g:.5f} against the minimiser's fitted
  {g_fit:.3f}, i.e. {100*(g-g_fit)/g_fit:+.1f}%. Nothing here closes that gap, and the
  closed form remains FIREWALLED from the fit. This sharpens the debt; it does not
  discharge it.
""")


if __name__ == "__main__":
    main()
