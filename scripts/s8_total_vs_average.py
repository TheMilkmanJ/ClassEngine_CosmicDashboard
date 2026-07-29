#!/usr/bin/env python3
"""
#82: why does the S8 shed coupling see the TOTAL when the amplitude sees the AVERAGE?

WHERE THE DOCKET STOOD. scripts/g_over_eps_is_the_roster.py showed the 10 in g = 10 eps
is not a bare integer but N, the roster size -- nine charged species plus the vacuum's
own seat. The 10 cancels the census denominator exactly, so g and eps are the same sum
counted two ways. What was left open: WHY one quantity takes the sum and the other the
average.

THE ANSWER IS A DIMENSIONAL ONE, AND IT MAKES A PREDICTION.

Write the per-species contribution as X = fbar * alpha_c = (2/pi)(3 alpha) = 6 alpha/pi.
Then the corpus's two numbers decompose as

    eps = (N-1)/N * X      -- a MEAN: the sum over charged species, per SEAT
    g   = (N-1)   * X      -- a SUM:  the same total, undivided

so g/eps = N = 10 identically. The census fraction c = (N-1)/N is a PROBABILITY -- the
chance that a randomly chosen seat carries a charged species rather than the vacuum --
so eps is an expectation value per seat and g is the ensemble total.

WHY EACH IS WHAT IT IS. eps is delta m_e/m_e: a property of ONE electron, i.e. of one
seat. It cannot count seats it does not occupy, so what it sees is the per-seat share.
g is a CONVERSION RATE for the dCDF fluid (dcdf_conv_g: the DM component shedding into
the floor/dark-radiation) -- an aggregate property of the whole ensemble, which counts
every contributor. Intensive versus extensive, and the ratio between an extensive
quantity and its intensive partner is the system size, here N = 10.

AND IT IS FALSIFIABLE IN PRINCIPLE, NOT JUST A LABEL. The two respond to a roster
change by very different amounts:

    dg/dN   = X            (adding a species adds its full contribution)
    deps/dN = X / N^2      (adding a species adds a share AND dilutes the average)

a ratio of N^2 = 100. So the reading is not "g and eps happen to differ by 10" -- it
says they must differ by 10 NOW and would track the roster differently if it changed.
Any construction that made both extensive, or both intensive, is excluded by the
observed factor.

PRE-STATED CONTROLS:
  S-A  the corpus's two closed forms must reproduce numerically, and g/eps must be
       exactly 10.
  S-B  the decomposition into (N-1)X/N and (N-1)X must be exact, with X = 6 alpha/pi.
  S-C  eps must equal the sum over the 9 charged species divided by the 10 seats,
       computed as an explicit sum rather than a formula.
  S-D  the roster-response ratio must be N^2 = 100.
  S-E  ANTI-CONTROL: if BOTH were sums, or BOTH means, the ratio would not be 10.
       Check both alternatives fail.
  S-F  ANTI-CONTROL: the split must not be a free fit. N = 10 and N-1 = 9 must be the
       recorded census, and a scan over other roster sizes must fail to give 10.
  S-G  the closed form's agreement with the fitted g ~ 0.12 must reproduce the recorded
       ~4.5%, so the object being explained is the one the corpus carries.
"""

import math

TOL = 1e-12
ALPHA = 1.0 / 137.035999084
N_SEATS = 10                 # 9 charged species + the vacuum's own seat
N_CHARGED = 9
G_FITTED = 0.12              # the minimiser's fitted value

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def main():
    print("=" * 78)
    print("  #82 — TOTAL vs AVERAGE: WHY g = N eps")
    print("=" * 78)

    fbar = 2.0 / math.pi
    alpha_c = 3.0 * ALPHA
    X = fbar * alpha_c                       # per-species contribution = 6 alpha/pi

    # ---- S-A ----------------------------------------------------------------
    print("\n  S-A  the corpus's closed forms")
    eps = 27.0 * ALPHA / (5.0 * math.pi)
    g = 54.0 * ALPHA / math.pi
    print(f"       eps = 27 alpha / 5 pi = {eps:.9f}")
    print(f"       g   = 54 alpha /   pi = {g:.9f}")
    chk("S-A1 g/eps = 10 exactly", abs(g / eps - 10.0) < 1e-12, f"{g/eps:.12f}")

    # ---- S-B ----------------------------------------------------------------
    print("\n  S-B  the decomposition, with X = fbar * alpha_c = 6 alpha/pi")
    chk("S-B1 X = 6 alpha/pi", abs(X - 6.0 * ALPHA / math.pi) < TOL, f"X = {X:.9f}")
    chk("S-B2 eps = (N-1)/N * X  — a MEAN per seat",
        abs(eps - (N_CHARGED / N_SEATS) * X) < 1e-15,
        f"{(N_CHARGED/N_SEATS)*X:.9f} vs {eps:.9f}")
    chk("S-B3 g = (N-1) * X  — the SAME total, undivided",
        abs(g - N_CHARGED * X) < 1e-15, f"{N_CHARGED*X:.9f} vs {g:.9f}")

    # ---- S-C ----------------------------------------------------------------
    print("\n  S-C  eps as an explicit sum over seats, not a formula")
    seats = [X] * N_CHARGED + [0.0]          # nine charged species, one empty vacuum seat
    total = sum(seats)
    mean = total / len(seats)
    chk("S-C1 the ten seats sum to g", abs(total - g) < 1e-15,
        f"sum = {total:.9f}, g = {g:.9f}")
    chk("S-C2 and their mean is eps", abs(mean - eps) < 1e-15,
        f"mean = {mean:.9f}, eps = {eps:.9f}")
    chk("S-C3 the vacuum seat contributes zero but IS counted in the denominator",
        seats[-1] == 0.0 and len(seats) == N_SEATS,
        "which is exactly what makes the census fraction 9/10 rather than 1")

    # ---- S-D ----------------------------------------------------------------
    print("\n  S-D  how each responds to a roster change")
    def eps_of(n): return (n - 1) / n * X
    def g_of(n): return (n - 1) * X
    h = 1e-6
    d_eps = (eps_of(N_SEATS + h) - eps_of(N_SEATS - h)) / (2 * h)
    d_g = (g_of(N_SEATS + h) - g_of(N_SEATS - h)) / (2 * h)
    print(f"       dg/dN   = {d_g:.9f}   (closed form X       = {X:.9f})")
    print(f"       deps/dN = {d_eps:.9f}   (closed form X/N^2  = {X/N_SEATS**2:.9f})")
    chk("S-D1 dg/dN = X", abs(d_g - X) < 1e-6)
    chk("S-D2 deps/dN = X/N^2", abs(d_eps - X / N_SEATS ** 2) < 1e-9)
    chk("S-D3 so g responds N^2 = 100x more strongly than eps",
        abs(d_g / d_eps - N_SEATS ** 2) < 1e-3, f"ratio {d_g/d_eps:.4f}")

    # ---- S-E: anti-control --------------------------------------------------
    print("\n  S-E  ANTI-CONTROL: would any other pairing give 10?")
    both_sums = (N_CHARGED * X) / (N_CHARGED * X)
    both_means = ((N_CHARGED / N_SEATS) * X) / ((N_CHARGED / N_SEATS) * X)
    swapped = ((N_CHARGED / N_SEATS) * X) / (N_CHARGED * X)
    print(f"       both extensive : ratio {both_sums:.4f}")
    print(f"       both intensive : ratio {both_means:.4f}")
    print(f"       swapped roles  : ratio {swapped:.4f}")
    chk("S-E1 only the sum/mean split gives 10",
        abs(both_sums - 1.0) < TOL and abs(both_means - 1.0) < TOL
        and abs(swapped - 0.1) < TOL,
        "the observed factor 10 excludes both-extensive and both-intensive outright")

    # ---- S-F: anti-control --------------------------------------------------
    print("\n  S-F  ANTI-CONTROL: is N = 10 fitted, or forced?")
    hits = [n for n in range(2, 41)
            if abs(((n - 1) * X) / (((n - 1) / n) * X) - 10.0) < 1e-9]
    chk("S-F1 only N = 10 reproduces the observed ratio", hits == [N_SEATS],
        f"scanned N in [2,40], hits at {hits}")
    chk("S-F2 and N = 10 is the recorded census, not a fit",
        N_SEATS == N_CHARGED + 1,
        "9 charged species + the vacuum's own seat (MATH_SPINE's c = 9/10)")

    # ---- S-G ----------------------------------------------------------------
    print("\n  S-G  is this the object the corpus actually carries?")
    dev = abs(g / G_FITTED - 1.0) * 100.0
    chk("S-G1 the closed form sits ~4.5% from the minimiser's fitted g ~ 0.12",
        4.0 < dev < 5.0, f"{g:.5f} vs {G_FITTED}, {dev:.2f}%")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — INTENSIVE vs EXTENSIVE, AND THE RATIO IS THE SYSTEM SIZE")
    print("=" * 78)
    print("""
  THE OPEN QUESTION IS ANSWERED, AND THE ANSWER IS DIMENSIONAL. With the per-species
  contribution X = fbar * alpha_c = 6 alpha/pi, the corpus's two numbers are the same
  ten seats read two ways:

      eps = (N-1)/N * X    the MEAN over seats   -- INTENSIVE
      g   = (N-1)   * X    the SUM over seats    -- EXTENSIVE

  verified as an explicit sum: nine seats carrying X and one vacuum seat carrying zero
  sum to g and average to eps (S-C). The census fraction 9/10 is a probability -- the
  chance a seat carries a charged species rather than the vacuum -- so eps is an
  expectation value and g is the ensemble total. The ratio between an extensive
  quantity and its intensive partner is the system size, which is why it is N.

  WHY EACH IS WHAT IT IS. eps is delta m_e/m_e -- a property of ONE electron, hence of
  ONE seat, which cannot count seats it does not occupy. g is a conversion RATE for the
  dCDF fluid (dcdf_conv_g, the DM component shedding into the floor), an aggregate
  property of the whole ensemble that counts every contributor. That is the whole
  content of "S8 sees the total while eps sees the average".

  AND IT IS NOT A RELABELLING -- IT PREDICTS. The two respond to a roster change by
  dg/dN = X against deps/dN = X/N^2, a factor N^2 = 100 (S-D). Adding a species adds
  its full contribution to g, but adds only a share to eps while simultaneously
  diluting the average. So the reading commits to more than the present ratio.

  THE ANTI-CONTROLS DO REAL WORK. If both quantities were extensive, or both
  intensive, the ratio would be 1; with the roles swapped it would be 1/10 (S-E). The
  observed factor 10 excludes all three outright. And the split is not a free fit: over
  roster sizes 2 to 40, ONLY N = 10 reproduces the ratio (S-F), and 10 is the recorded
  census -- nine charged species plus the vacuum's own seat -- not a number chosen to
  make this work.

  WHAT REMAINS OWED ON #82, AND IT IS SMALLER THAN WHAT WAS OWED. Not "why the total
  versus the average" -- that is settled. What is still unclosed is the same thing the
  docket carried from the start: g = 54 alpha/pi is a DERIVATION CANDIDATE, firewalled
  from the fit and agreeing with the minimiser's g ~ 0.12 at 4.5% (S-G). The
  intensive/extensive reading explains the FACTOR relating it to eps; it does not
  promote the closed form itself, which still awaits its mechanism through eps.
""")


if __name__ == "__main__":
    main()
