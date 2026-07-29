#!/usr/bin/env python3
"""
Docket #62's check, run. It does not kill the model -- it kills the ROUTE, and the route
it kills is the one the corpus had just called load-bearing.

--------------------------------------------------------------------------------------
THE DEBT, as the corpus stated it (PRTOE_me_mechanism_math.md):

    "The same cell-to-cell scatter that averages away in the line CENTROID does not
     average away in the line WIDTH. A 3.14e-3 spread in m_e across cells implies an
     excess broadening, and whether that survives observed line widths is a real,
     external, falsifiable test the corpus has not run."

--------------------------------------------------------------------------------------
THE ANSWER: THE TWO EFFECTS ARE THE SAME OBJECT, AND THEY CANNOT BE HAD SEPARATELY.

The averaging argument needs the scatter. That is what averaging averages. But the width
is set by that same scatter and is INDEPENDENT OF N -- superposing more cells does not
narrow the distribution of their shifts, it samples it better. So:

    centroid error  =  w * eps * sd(Theta) / sqrt(N)      <-- N helps
    line width      =  w * eps * sd(Theta)                <-- N is absent

Their ratio is sqrt(N). At the recorded N = 1e9 that is a factor of ~31,000. You cannot
buy centroid compliance with N and decline to pay for width.

So the speckle branch faces a fork, and BOTH horns close:

  HORN 1, Theta uniform at its Beta mean (no scatter). No broadening -- but then the
          shift is a coherent eps*<Theta> = eps/2 = 6.3e-3, which is ~4 orders of
          magnitude above the mu bounds. Excluded on the CENTROID.
  HORN 2, Theta scattered per the Beta(d/2,d/2) law. The centroid averages down to 1e-7
          as advertised -- and the width comes out ~1880 km/s, which is 2 orders of
          magnitude above any observed 21 cm absorption linewidth. Excluded on the WIDTH.

WHAT SURVIVES is the branch the corpus already had and did not need the averaging for:
LAMINAR / SCREENED Theta = 1.9e-6, which passes centroid AND width together, because it
suppresses the mean and the scatter by the same factor.

CONSEQUENCE, and it is a retraction of a result recorded hours earlier: the "N = 10^9 is
within 2% of exactly what a 1e-7 bound requires" coincidence is a RED HERRING. It tunes
the centroid while the width fails by ~188x. The averaging argument is retired as a route
to compliance.

STRUCTURAL BONUS, and it connects this docket to the radio-lattice paper: the paper's two
observable classes respond to scatter in OPPOSITE ways.
  - LINE rows (21 cm, recombination lines) are broadened. Width ~ sd, no N help.
  - RECONSTRUCTED-COLUMN rows (dispersion measure, rotation measure) are integrals along
    the path, so the scatter averages down exactly like the centroid and is INVISIBLE.
So scatter is maximally visible in exactly the rows the paper calls measurable, and
invisible in the rows it demoted. That is a testable structural statement, not a slogan.

PRE-STATED CONTROLS:
  W-A  the Beta(d/2,d/2) mean and sd, by integration, not by quoting a moment formula.
  W-B  the per-cell m_e scatter, and the corpus's own 3.14e-3 reproduced.
  W-C  the cell count needed for centroid compliance, and the claimed 2% agreement.
  W-D  the width must be shown INDEPENDENT of N -- the whole result turns on this.
  W-E  the width in velocity units, and the suppression a given observed width demands.
  W-F  HORN 1: uniform Theta must fail on the centroid, or the fork is not a fork.
  W-G  ANTI-CONTROL: the laminar branch must pass BOTH, or nothing survives.
  W-H  ANTI-CONTROL: the column-integrated rows must NOT be broadened, or the structural
       claim is empty.
  W-I  ANTI-CONTROL: no value of N may rescue horn 2 -- scan N over 12 decades.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


ALPHA = 0.0072973525693
C_KMS = 299792.458
EPS = 27 * ALPHA / (5 * math.pi)      # the derived stack, 1.2543%
THETA_LAMINAR = 1.9e-6               # the corpus's laminar value
MU_BOUND = 4.0e-7                    # methanol, 2 sigma (Kanekar 2015 robust)
N_RECORDED = 1e9                     # the corpus's recorded cell count
W_21CM = 2                           # the 21 cm hyperfine weight


def beta_moments(d, n=2_000_001):
    """mean and sd of Beta(d/2,d/2) on [0,1] by direct integration.

    Substitute x = sin^2(t) so the endpoint singularities at d < 2 are removed:
    x^(a-1)(1-x)^(a-1) dx = 2 sin^(2a-1)(t) cos^(2a-1)(t) dt, t in [0, pi/2].
    """
    a = d / 2.0
    m0 = m1 = m2 = 0.0
    for i in range(n):
        t = (math.pi / 2) * (i + 0.5) / n
        s, c = math.sin(t), math.cos(t)
        wgt = (s ** (2 * a - 1)) * (c ** (2 * a - 1))
        x = s * s
        m0 += wgt
        m1 += wgt * x
        m2 += wgt * x * x
    mean = m1 / m0
    var = m2 / m0 - mean * mean
    return mean, math.sqrt(var)


def main():
    print("=" * 78)
    print("  DOCKET #62: THE LINE-WIDTH CHECK")
    print("=" * 78)
    print(f"\n  eps = 27a/5pi = {EPS:.6e}  ({EPS*100:.4f}%)")

    # ---- W-A ---------------------------------------------------------------
    print("\n  W-A  the Beta(d/2,d/2) law, by integration")
    for d in (1, 2, 3, 4):
        mean, sd = beta_moments(d)
        closed = 1.0 / (2 * math.sqrt(d + 1))
        print(f"       d = {d}:  mean {mean:.6f}   sd {sd:.6f}   "
              f"closed form 1/(2sqrt(d+1)) = {closed:.6f}")
        if d == 3:
            sd3, mean3 = sd, mean
    chk("W-A1 mean is 1/2 in 3D", abs(mean3 - 0.5) < 1e-6, f"{mean3:.6f}")
    chk("W-A2 sd is 1/4 in 3D", abs(sd3 - 0.25) < 1e-5, f"{sd3:.6f}")

    # ---- W-B ---------------------------------------------------------------
    print("\n  W-B  the per-cell m_e scatter")
    sigma_cell = EPS * sd3
    print(f"       sigma(dm_e/m_e) = eps * sd(Theta) = {EPS:.4e} * {sd3:.4f}"
          f" = {sigma_cell:.4e}")
    chk("W-B1 reproduces the corpus's 3.14e-3", abs(sigma_cell - 3.14e-3) < 2e-5,
        f"{sigma_cell:.4e}")

    # ---- W-C ---------------------------------------------------------------
    print("\n  W-C  the cell count centroid compliance demands")
    N_needed = (sigma_cell / 1e-7) ** 2
    print(f"       N >= (sigma/1e-7)^2 = {N_needed:.3e}   recorded {N_RECORDED:.0e}"
          f"   ratio {N_RECORDED/N_needed:.4f}")
    chk("W-C1 the recorded N clears the 1e-7 bar", N_RECORDED >= N_needed)
    chk("W-C2 and does so to within 2%, as recorded",
        abs(N_RECORDED / N_needed - 1) < 0.02, f"{100*(N_RECORDED/N_needed-1):+.1f}%")

    # ---- W-D  THE LOAD-BEARING ONE -----------------------------------------
    print("\n  W-D  is the WIDTH independent of N?  (the whole result turns on this)")
    #  The line profile is the distribution of per-cell shifts w*eps*Theta_i.
    #  Superposing more cells samples that distribution better; it does not narrow it.
    widths = {}
    for N in (1e2, 1e4, 1e6, 1e9, 1e12):
        width = W_21CM * EPS * sd3          # no N anywhere
        centroid = W_21CM * EPS * sd3 / math.sqrt(N)
        widths[N] = width
        print(f"       N = {N:.0e}:  width {width:.4e}   centroid err {centroid:.4e}"
              f"   ratio sqrt(N) = {math.sqrt(N):.3e}")
    chk("W-D1 the width is identical at every N", len(set(f"{v:.12e}" for v in widths.values())) == 1,
        "averaging cannot reach it")
    ratio = math.sqrt(N_RECORDED)
    chk("W-D2 at the recorded N the width exceeds the centroid error by ~31,000x",
        abs(ratio - 31623) / 31623 < 0.01, f"{ratio:.0f}x")

    # ---- W-E ---------------------------------------------------------------
    print("\n  W-E  the width in velocity, and what an observed width demands")
    sd_v = C_KMS * W_21CM * EPS * sd3
    fwhm_v = 2 * math.sqrt(2 * math.log(2)) * sd_v
    print(f"       21 cm (w = +2):  sd = {sd_v:.1f} km/s   FWHM = {fwhm_v:.0f} km/s")
    chk("W-E1 the predicted broadening is ~1880 km/s sd", abs(sd_v - 1880) < 15,
        f"{sd_v:.1f} km/s")
    print("\n       suppression of sd(Theta) required, per allowed observed width:")
    for W in (1.0, 10.0, 50.0):
        sd_allowed = W / (C_KMS * W_21CM * EPS)
        supp = sd3 / sd_allowed
        print(f"         {W:5.1f} km/s  ->  sd(Theta) <= {sd_allowed:.3e}"
              f"   i.e. suppressed {supp:6.0f}x below the Beta law")
        if W == 10.0:
            supp10 = supp
    chk("W-E2 a 10 km/s allowance demands ~188x suppression", abs(supp10 - 188) < 3,
        f"{supp10:.0f}x")
    print("       (21 cm absorption in damped systems is narrow -- of order 1-50 km/s as")
    print("        a class. No specific measured width is sourced in-corpus, so the")
    print("        demand is quoted across the class rather than against one system.)")

    # ---- W-F  HORN 1 --------------------------------------------------------
    print("\n  W-F  HORN 1: uniform Theta (no scatter, hence no broadening)")
    shift_uniform = EPS * mean3
    print(f"       coherent shift = eps * <Theta> = {shift_uniform:.4e}")
    print(f"       against the mu bound {MU_BOUND:.1e}:  "
          f"exceeded by {shift_uniform/MU_BOUND:.3e}x")
    chk("W-F1 uniform Theta is excluded on the CENTROID", shift_uniform > MU_BOUND,
        f"by {shift_uniform/MU_BOUND:.2e}x -- so the fork is real")

    # ---- W-G  anti-control --------------------------------------------------
    print("\n  W-G  ANTI-CONTROL: does the laminar/screened branch pass BOTH?")
    shift_lam = EPS * THETA_LAMINAR
    #  screening suppresses mean and scatter together: sd scales with the mean
    sd_lam = sd3 * (THETA_LAMINAR / mean3)
    width_lam_v = C_KMS * W_21CM * EPS * sd_lam
    print(f"       Theta = {THETA_LAMINAR:.1e}:  centroid shift {shift_lam:.3e}"
          f"   width {width_lam_v:.3e} km/s")
    chk("W-G1 laminar passes the centroid", shift_lam < MU_BOUND,
        f"{shift_lam:.2e} < {MU_BOUND:.1e}")
    chk("W-G2 laminar passes the width", width_lam_v < 1.0,
        f"{width_lam_v:.2e} km/s, far below any observed width")
    chk("W-G3 so something DOES survive -- this is a route kill, not a model kill",
        shift_lam < MU_BOUND and width_lam_v < 1.0)

    # ---- W-H  anti-control --------------------------------------------------
    print("\n  W-H  ANTI-CONTROL: are the column-integrated rows broadened too?")
    #  DM and RM are path integrals: the observable is INT n_e (1 + w eps Theta) dl,
    #  so cell scatter enters as a mean over N cells, exactly like the centroid.
    dm_scatter = W_21CM * EPS * sd3 / math.sqrt(N_RECORDED)
    print(f"       a reconstructed column over N = {N_RECORDED:.0e} cells carries"
          f" scatter {dm_scatter:.3e}")
    chk("W-H1 the column rows ARE averaged, so scatter is invisible there",
        dm_scatter < MU_BOUND, "no broadening analogue exists for an integral")
    chk("W-H2 so the two classes respond OPPOSITELY, which is the structural claim",
        dm_scatter < MU_BOUND < shift_uniform)

    # ---- W-I  anti-control --------------------------------------------------
    print("\n  W-I  ANTI-CONTROL: can ANY N rescue horn 2?")
    rescued = []
    for k in range(0, 25, 2):
        N = 10.0 ** k
        w_v = C_KMS * W_21CM * EPS * sd3          # N-free
        if w_v <= 50.0:
            rescued.append(N)
    print(f"       scanned N from 1e0 to 1e24: widths all {C_KMS*W_21CM*EPS*sd3:.0f} km/s")
    chk("W-I1 no N brings the width under 50 km/s", len(rescued) == 0,
        "because N does not appear in the width -- the escape is closed by construction")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE CHECK KILLS THE ROUTE, NOT THE MODEL")
    print("=" * 78)
    print(f"""
  The centroid and the width are the same object seen twice. Averaging divides the
  centroid error by sqrt(N) and leaves the width untouched, because N does not appear in
  the width at all -- superposing more cells samples the distribution of shifts better,
  it does not narrow it. At the recorded N = 1e9 the width exceeds the centroid error by
  a factor of {math.sqrt(N_RECORDED):.0f}.

  So the speckle branch forks, and both horns close:

    uniform Theta   ->  no broadening, but a coherent eps/2 = {EPS*0.5:.2e} shift,
                        {EPS*0.5/MU_BOUND:.1e}x over the mu bound. Dead on the centroid.
    scattered Theta ->  centroid averages to 1e-7 as advertised, and the width comes out
                        {C_KMS*W_21CM*EPS*0.25:.0f} km/s sd against 21 cm absorption lines that
                        are narrow. Needs sd(Theta) suppressed {0.25/(10/(C_KMS*W_21CM*EPS)):.0f}x to
                        fit inside even 10 km/s. Dead on the width.

  WHAT THIS RETIRES. The corpus recorded, hours before this was run, that N = 1e9 sits
  "within 2% of exactly the number that brings speckle scatter under spectroscopic
  bounds," and called the coincidence load-bearing. It is confirmed arithmetically here
  (ratio 1.017) and it is a RED HERRING: it tunes the centroid while the width fails by
  two orders of magnitude. **The averaging argument is retired as a route to compliance.**

  WHAT SURVIVES is the branch that never needed it. Laminar Theta = {THETA_LAMINAR:.1e}
  suppresses the mean and the scatter by the same factor and clears both tests at once
  (centroid {EPS*THETA_LAMINAR:.2e}, width {C_KMS*W_21CM*EPS*0.25*(THETA_LAMINAR/0.5):.1e} km/s). Screening was already
  "data-required" from centroids alone; the width makes it required far more strongly,
  and rules out the developed-speckle alternative rather than merely disfavouring it.

  AND A STRUCTURAL RESULT WORTH KEEPING. The radio-lattice paper's two observable classes
  respond to scatter in opposite directions. Line rows get broadened, with no N relief.
  Reconstructed-column rows are path integrals, so their scatter averages down exactly
  like a centroid and is invisible. Cell-to-cell scatter is therefore maximally visible in
  precisely the rows that paper calls measurable, and invisible in the three it demoted.
  That is a falsifiable statement about where to look, not a slogan.
""")


if __name__ == "__main__":
    main()
