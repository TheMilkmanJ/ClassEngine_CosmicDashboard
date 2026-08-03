#!/usr/bin/env python3
"""
#62: is the Theta-averaging forced, and by how much? Plus a correction to my own
morning entry, which quoted Theta's scatter as m_e's.

WHAT THE CORPUS ALREADY HAS (protocol 50 check, run before building). This is not a
blank page. `PRTOE_me_trigger.md` records that "developed speckle sits at <Theta> = 1/2
exactly by the Beta(d/2, d/2) law", and `_AUDIT_LEDGER.md` carries <Theta> = 1/2 in
developed speckle against Theta = 1.9e-6 laminar. So the one-point distribution of
Theta is KNOWN and stated, and the sd = 0.25 I quoted this morning is simply that
law's 3D standard deviation, not a new number.

MY MORNING ENTRY GOT THE INDUCED SCATTER WRONG. It read: "pointwise Theta (sd = 0.25
in 3D) would scatter m_e by 25% within a single absorber." That quotes THETA's scatter
as M_E's. Theta is a 0-to-1 coherence indicator; the mass shift it drives is

    delta m_e / m_e  =  eps * Theta,     eps = 27 alpha / 5 pi = 0.0125

so a Theta scatter of 0.25 induces an m_e scatter of eps * 0.25 = 3.14e-3, i.e.
0.31% OF m_e -- not 25%. (It is 50% of the MEAN SHIFT eps*<Theta> = eps/2, which is
probably where the confusion came from, but "scatter m_e by 25%" is not that either.)
Off by a factor ~80.

WHAT SURVIVES, AND IT IS THE USEFUL HALF. The averaging is still forced, and now by a
number rather than a feel:

    pointwise, one cell   :  3.14e-3
    averaged over N cells :  3.14e-3 / sqrt(N)
    at N = 1e9            :  9.9e-8

Astrophysical constraints on mu = m_p/m_e variation sit at the 1e-5 to 1e-7 level
depending on the system, so the pointwise value is excluded by four to five orders of
magnitude and the averaged one is not. Running it backwards: reaching 1e-7 needs
N > 9.8e8. THE CORPUS'S 1e9 CELLS IS, TO WITHIN A FACTOR OF 1.02, EXACTLY THE COUNT
THAT BRINGS SPECKLE SCATTER UNDER SPECTROSCOPIC BOUNDS. That is a much better statement
of "the averaging is forced" than the one I recorded, because it is quantitative and it
is falsifiable from the outside.

PRE-STATED CONTROLS:
  V-A  the Beta(d/2,d/2) mean and variance must be obtained by INTEGRATING the density,
       not by quoting moment formulae, and must give mean 1/2 and sd = 1/(2 sqrt(d+1)).
  V-B  at d = 3 that must be exactly 0.25, reproducing the corpus's recorded figure.
  V-C  the N-cell suppression must reproduce the recorded 7.9e-6 at N = 1e9.
  V-D  the induced m_e scatter must be computed, and my morning's "25%" must be shown
       WRONG by the factor it is wrong by.
  V-E  the count needed to reach 1e-7 must be computed and compared to the recorded 1e9.
  V-F  ANTI-CONTROL: the suppression must genuinely depend on N -- at small N the
       scatter must remain excluded.
  V-G  ANTI-CONTROL: sd = 0.25 must be specific to d = 3, or "in 3D" is decoration.
  V-H  ANTI-CONTROL: the laminar value 1.9e-6 must sit far below the speckle mean, or
       the two regimes are not distinguishable and the whole picture is vacuous.
"""

import math

TOL = 1e-12
ALPHA = 1.0 / 137.035999084
EPS = 27.0 * ALPHA / (5.0 * math.pi)
THETA_LAMINAR = 1.9e-6
N_CELLS = 1e9

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def beta_moments(a, b, n=200001):
    """
    Mean and variance of Beta(a,b) by integrating the density.

    NB the substitution x = sin^2 t is not cosmetic. For a = b = 1/2 (d = 1) the
    density diverges as x^(-1/2) at BOTH endpoints, and a plain Simpson rule on x
    returns sd = 0.410 against the true 0.354 -- a 16% error that looks like a
    physics result. Under x = sin^2 t the integrand becomes
    2 sin^(2a-1)t cos^(2b-1)t, which is smooth for every a, b >= 1/2.
    """
    hi = math.pi / 2.0
    h = hi / (n - 1)
    m0 = m1 = m2 = 0.0
    for i in range(n):
        t = i * h
        s, c = math.sin(t), math.cos(t)
        s = min(max(s, 1e-15), 1.0)
        c = min(max(c, 1e-15), 1.0)
        f = 2.0 * s ** (2.0 * a - 1.0) * c ** (2.0 * b - 1.0)
        x = math.sin(t) ** 2
        w = 1.0 if i in (0, n - 1) else (4.0 if i % 2 else 2.0)
        m0 += w * f
        m1 += w * f * x
        m2 += w * f * x * x
    mean = m1 / m0
    return mean, m2 / m0 - mean * mean


def main():
    print("=" * 78)
    print("  #62 — IS THE AVERAGING FORCED, AND BY HOW MUCH?")
    print("=" * 78)
    print(f"\n  eps = 27 alpha / 5 pi = {EPS:.9f}")

    # ---- V-A ----------------------------------------------------------------
    print("\n  V-A  the Beta(d/2, d/2) law, integrated")
    print(f"\n    {'d':>3} {'mean':>12} {'sd':>12} {'1/(2 sqrt(d+1))':>18}")
    ok_a = True
    sds = {}
    for d in (1, 2, 3, 5):
        mean, var = beta_moments(d / 2.0, d / 2.0)
        sd = math.sqrt(var)
        sds[d] = sd
        closed = 1.0 / (2.0 * math.sqrt(d + 1.0))
        good = abs(mean - 0.5) < 1e-6 and abs(sd - closed) < 1e-5
        ok_a &= good
        print(f"    {d:3d} {mean:12.9f} {sd:12.9f} {closed:18.9f}"
              f"  {'' if good else '<-- MISMATCH'}")
    chk("V-A1 mean is 1/2 and sd = 1/(2 sqrt(d+1)) at every d", ok_a,
        "so <Theta> = 1/2 is a distributional fact, not something to be arranged")

    # ---- V-B ----------------------------------------------------------------
    print("\n  V-B  the 3D value")
    chk("V-B1 sd = 0.25 exactly in d = 3", abs(sds[3] - 0.25) < 1e-5,
        f"{sds[3]:.9f} — the corpus's recorded figure, and it is the Beta law's, not new")

    # ---- V-C ----------------------------------------------------------------
    print("\n  V-C  suppression over N cells")
    sup = 0.25 / math.sqrt(N_CELLS)
    chk("V-C1 0.25/sqrt(1e9) reproduces the recorded 7.9e-6", abs(sup - 7.9e-6) < 5e-8,
        f"{sup:.4e}")

    # ---- V-D ----------------------------------------------------------------
    print("\n  V-D  what scatter does that induce in m_e?")
    scat_pointwise = EPS * 0.25
    mean_shift = EPS * 0.5
    print(f"       delta m_e/m_e = eps * Theta, so a Theta scatter of 0.25 gives")
    print(f"         scatter in m_e            = {scat_pointwise:.4e}  ({scat_pointwise*100:.3f}% of m_e)")
    print(f"         mean shift  eps*<Theta>   = {mean_shift:.4e}")
    print(f"         scatter as % of the shift = {scat_pointwise/mean_shift*100:.1f}%")
    chk("V-D1 the induced m_e scatter is 0.31%, NOT 25%",
        abs(scat_pointwise - 3.136e-3) < 1e-5 and abs(scat_pointwise - 0.25) > 0.2,
        f"my morning entry was off by a factor {0.25/scat_pointwise:.0f}")
    chk("V-D2 the 25% figure is THETA's scatter, quoted as m_e's",
        abs(0.25 - sds[3]) < 1e-5, "0.25 is sd(Theta); sd(delta m/m) = eps * 0.25")

    # ---- V-E ----------------------------------------------------------------
    print("\n  V-E  how many cells does a 1e-7 bound require?")
    target = 1e-7
    n_needed = (scat_pointwise / target) ** 2
    print(f"       need scatter/sqrt(N) < {target:.0e}  =>  N > {n_needed:.3e}")
    print(f"       the corpus records                        N = {N_CELLS:.0e}")
    chk("V-E1 the recorded cell count is within a small factor of what 1e-7 needs",
        0.5 < N_CELLS / n_needed < 2.0,
        f"ratio {N_CELLS/n_needed:.3f} — the count is not arbitrary")
    chk("V-E2 and the averaged scatter lands just under 1e-7",
        scat_pointwise / math.sqrt(N_CELLS) < 1.05e-7,
        f"{scat_pointwise/math.sqrt(N_CELLS):.3e}")

    # ---- V-F: anti-control --------------------------------------------------
    print("\n  V-F  ANTI-CONTROL: does the suppression really need N?")
    print(f"\n    {'N':>12} {'scatter':>14}  verdict vs 1e-7")
    ok_f = True
    for n in (1, 1e2, 1e4, 1e6, 1e9):
        s = scat_pointwise / math.sqrt(n)
        good = (s > target) if n < 1e8 else (s < 1.05 * target)
        ok_f &= good
        print(f"    {n:12.0e} {s:14.3e}  {'excluded' if s > target else 'allowed'}")
    chk("V-F1 small N stays excluded; only N ~ 1e9 clears the bound", ok_f,
        "so the cell count is load-bearing, not decorative")

    # ---- V-G: anti-control --------------------------------------------------
    print("\n  V-G  ANTI-CONTROL: is 0.25 specific to three dimensions?")
    chk("V-G1 d = 1 and d = 2 give different sds",
        abs(sds[1] - 0.25) > 0.05 and abs(sds[2] - 0.25) > 0.02,
        f"d=1: {sds[1]:.4f}, d=2: {sds[2]:.4f}, d=3: {sds[3]:.4f}")

    # ---- V-H: anti-control --------------------------------------------------
    print("\n  V-H  ANTI-CONTROL: are the two regimes actually distinguishable?")
    chk("V-H1 the laminar value sits far below the speckle mean",
        THETA_LAMINAR / 0.5 < 1e-5,
        f"{THETA_LAMINAR:.1e} vs 0.5 — a factor {0.5/THETA_LAMINAR:.1e}")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE AVERAGING IS FORCED, AND MY OWN FIGURE WAS WRONG")
    print("=" * 78)
    print("""
  FIRST, THE CORRECTION. My morning entry on #62 read: "pointwise Theta (sd = 0.25 in
  3D) would scatter m_e by 25% within a single absorber." That quotes THETA's scatter as
  M_E's. Theta is a 0-to-1 coherence indicator and the shift it drives is eps * Theta,
  so a Theta scatter of 0.25 induces an m_e scatter of eps * 0.25 = 3.14e-3 -- 0.31% of
  m_e, not 25%. Off by a factor 80. (It is 50% of the MEAN SHIFT, which is the nearest
  true statement to what I wrote, and still not what I wrote.)

  SECOND, WHAT THE CORPUS ALREADY HELD. The sd = 0.25 is not a new number: developed
  speckle sits at <Theta> = 1/2 exactly by the Beta(d/2, d/2) law, which this script
  re-derives by integrating the density -- mean 1/2 and sd = 1/(2 sqrt(d+1)) at every d,
  giving exactly 0.25 in three dimensions (V-A, V-B). So <Theta> = 1/2 is a
  DISTRIBUTIONAL FACT rather than something the model has to arrange, and the 0.25 is
  that law's own spread.

  THIRD, AND THIS IS THE PART WORTH KEEPING. The averaging is forced, and now by a
  number instead of a feel. Pointwise the induced scatter is 3.14e-3; averaged over N
  cells it falls as 1/sqrt(N); at the recorded N = 1e9 it is 9.9e-8. Astrophysical
  constraints on mu = m_p/m_e variation sit in the 1e-5 to 1e-7 range, so the pointwise
  value is excluded by four to five orders of magnitude while the averaged one is not.

  RUN BACKWARDS, THE CELL COUNT IS NOT ARBITRARY. Reaching 1e-7 requires N > 9.8e8, and
  the corpus records 1e9 -- a ratio of 1.02 (V-E). THE RECORDED CELL COUNT IS, TO WITHIN
  2%, EXACTLY THE NUMBER THAT BRINGS SPECKLE SCATTER UNDER SPECTROSCOPIC BOUNDS. The
  anti-control confirms this is load-bearing: N = 1, 1e2, 1e4 and 1e6 all stay excluded,
  and only ~1e9 clears (V-F).

  SO #62'S DEBT IS BETTER STATED THAN IT WAS, AND SMALLER. Not "why does the coupling
  average" as an open mechanism question -- the observable IS an average, because an
  absorption line is formed across the whole column and each cell contributes its own
  m_e. What the model owes is not a smoothing mechanism but a CHECK: the same cell-to-
  cell scatter that averages away in the line CENTROID does not average away in the line
  WIDTH. A 3.14e-3 spread in m_e across cells implies an excess broadening, and whether
  that survives observed line widths is a real, external, falsifiable test that the
  corpus has not run.

  That is the honest next object for this docket, and it is sharper than what it
  replaces: a residual I can name, quantify, and hand to data.
""")


if __name__ == "__main__":
    main()
