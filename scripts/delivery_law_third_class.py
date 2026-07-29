#!/usr/bin/env python3
"""
#87: does a third class of delivery law exist -- one whose frequency dependence enters
through eps ~ w^2 rather than through a count, AND which is exact at 6 ppm?

YES, AND THE QUESTION COLLAPSES TO ONE LINE FIRST.

THE REDUCTION. For a harmonic mode of stiffness eps = M w^2 holding total energy e,
<x^2> = e/eps. The null equates the 2-dof doublet's summed amplitude with the 1-dof
singlet's:

    2 * e(eps_1)/eps_1  =  e(eps_0)/eps_0

and Q = 2/3 requires eps_1/eps_0 = 2 exactly (delivery_law_two_parameters.py). Put the
two together and the 2s cancel:

    ****  e(2 eps_0)  =  e(eps_0)  ****

THAT IS THE WHOLE REQUIREMENT. The delivery law must deposit the SAME energy per
degree of freedom into a mode of stiffness eps_0 and one of stiffness 2 eps_0 -- i.e.
be FLAT across a factor sqrt2 in frequency. Everything else -- the (s, p) family, the
four recorded laws, the occupancy lock -- is downstream of this single statement.

Three consequences fall out immediately:

  * Among power laws e ~ eps^p, flatness forces p = 0. That re-derives the earlier
    uniqueness result as a corollary of something simpler.
  * The occupancy lock fails because integer counts make e DISCRETE in a way that
    cannot be flattened (#86). Continuous (coherent) excitation is not excluded by
    that argument -- but then nothing fixes the amplitudes.
  * And the search for a "third class" is now a well-posed question about ONE function:
    which physically motivated e(w) is flat between w_0 and sqrt2 w_0?

THERMAL EQUILIBRIUM IS NOT AN ARBITRARY CHOICE -- IT IS THE BEST FLAT LAW THERE IS.
The exact harmonic result is e = (hbar w/2) coth(hbar w/2kT) = kT + (hbar w)^2/(12 kT)
- ..., and the LINEAR term in w is absent: equilibrium cancels it. A non-equilibrium
flat law -- "every mode gets E_0" -- still carries the mode's own zero point, giving
e = E_0 + hbar w/2, whose error is FIRST order. The cost difference is large: thermal
needs n_bar ~ 80 quanta to hold 6 ppm, a driven law needs ~34,500.

But strictly increasing is strictly increasing: g(x) rises monotonically, so
g(sqrt2 x_0) = g(x_0) has no solution at finite x. Thermal is exact only in the limit.

SO AN EXACT THIRD CLASS MUST BE NON-MONOTONIC, AND THERE IS A CLEAN ONE.
If the deposition spectrum is symmetric in log w about a peak w_p, then

    e(w_0) = e(w_1)   <=>   ln w_p = (ln w_0 + ln w_1)/2   <=>   w_p = sqrt(w_0 w_1)

the GEOMETRIC MEAN -- which for w_1 = sqrt2 w_0 is w_p = 2^(1/4) w_0. This is exact,
and exact for ANY WIDTH: the condition fixes only where the spectrum sits, not how
broad it is. That is a symmetry statement rather than a numerical coincidence, and it
is the strongest candidate the classification produces.

A second exact route: a TWO-TEMPERATURE freeze. With the sectors decoupling at
different times, e_S = kT_S g(x_S) and e_D = kT_D g(x_D), and the free ratio T_D/T_S
can be set to make them equal exactly. Also one condition.

WHAT THIS COSTS, STATED PLAINLY. Both exact routes need ONE number tied to the ring
(the peak location, or the temperature ratio). Neither is derived here. The result is
a CLASSIFICATION -- "a third class exists and here is exactly what it must satisfy" --
not a mechanism.

PRE-STATED CONTROLS:
  G-A  the reduction must be re-derived, and must reproduce the (s,p) family's verdict
       as a corollary: among power laws only p = 0 is flat.
  G-B  the thermal law must be shown strictly increasing, hence never exactly flat, and
       must reproduce the recorded 1025 ppm at x_1 = 2/9 and the x_1 <= 0.0170 ceiling.
  G-C  thermal's leading correction must be O(x^2) -- the linear term must cancel.
  G-D  a driven flat law plus zero point must be O(x), and the quanta needed for 6 ppm
       must be computed and be far larger than thermal's.
  G-E  a log-symmetric deposition spectrum centred on the geometric mean must give
       EXACT flatness, at several widths.
  G-F  the two-temperature route must have an exact solution; solve for T_D/T_S.
  G-G  ANTI-CONTROL: a log-symmetric spectrum NOT centred on the geometric mean must
       FAIL -- otherwise the centring condition is doing no work.
  G-H  ANTI-CONTROL: the condition must be width-independent but NOT frequency-
       independent, i.e. it must genuinely tie the spectrum to the ring.
  G-I  ANTI-CONTROL: the reduction must not be vacuous -- laws known to fail must fail
       it, and reproduce their recorded wrong stiffness ratios.
"""

import math

TOL = 1e-12
Q_TARGET = 2.0 / 3.0
EXACTNESS = 6e-6
X1_CORPUS = 2.0 / 9.0

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def g(x):
    """(x/2) coth(x/2) — the exact harmonic energy in units of kT."""
    if x < 1e-8:
        return 1.0 + x * x / 12.0
    z = 0.5 * x
    return z / math.tanh(z)


def eps_ratio_from(e_of_eps, eps0=1.0):
    """solve 2 e(eps1)/eps1 = e(eps0)/eps0 for eps1/eps0."""
    target = e_of_eps(eps0) / eps0
    lo, hi = 1e-6, 1e6
    inc = (2 * e_of_eps(hi) / hi) > (2 * e_of_eps(lo) / lo)
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if ((2 * e_of_eps(mid) / mid) > target) == inc:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi) / eps0


def Q_of_ratio(r):
    return 1.0 / 3.0 + (2.0 / 3.0) / r


def main():
    print("=" * 78)
    print("  #87 — DOES A THIRD CLASS EXIST? THE QUESTION REDUCES TO ONE CONDITION")
    print("=" * 78)

    root2 = math.sqrt(2.0)

    # ---- G-A ----------------------------------------------------------------
    print("\n  G-A  the reduction:  null + (Q = 2/3)  <=>  e(2 eps_0) = e(eps_0)")
    # flat law -> ratio 2, by the solver, not by the algebra
    r_flat = eps_ratio_from(lambda e: 1.0)
    chk("G-A1 a FLAT e gives eps_1/eps_0 = 2", abs(r_flat - 2.0) < 1e-6, f"{r_flat:.9f}")
    chk("G-A2 which is exactly what Q = 2/3 needs",
        abs(Q_of_ratio(r_flat) - Q_TARGET) < 1e-7, f"Q = {Q_of_ratio(r_flat):.9f}")
    # among power laws, only p = 0 is flat
    print(f"\n    {'p':>6} {'e(2eps)/e(eps)':>16} {'eps_1/eps_0':>13} {'Q':>12}")
    flat_ps = []
    for p in (-1.0, -0.5, 0.0, 0.5, 1.0):
        ratio_e = 2.0 ** p
        r = eps_ratio_from(lambda e, p=p: e ** p)
        if abs(ratio_e - 1.0) < TOL:
            flat_ps.append(p)
        print(f"    {p:6.1f} {ratio_e:16.9f} {r:13.9f} {Q_of_ratio(r):12.9f}")
    chk("G-A3 among power laws e ~ eps^p, ONLY p = 0 is flat", flat_ps == [0.0],
        f"flat at p in {flat_ps} — re-derives the (s,p) family's uniqueness verdict")
    print("       NB the p = 1 row's 1e6 is the solver's upper BOUND, not a value: at")
    print("          p = 1 the amplitude is eps-independent and the null has no solution")
    print("          at all (#85's E-G). Read that row as a singularity — see G-I.")

    # ---- G-B ----------------------------------------------------------------
    print("\n  G-B  the thermal law is strictly increasing, so never exactly flat")
    xs = [0.01, 0.1, 0.5, 1.0, 2.0, 5.0]
    gs = [g(x) for x in xs]
    chk("G-B1 g(x) is strictly increasing", all(b > a for a, b in zip(gs, gs[1:])),
        f"g: {', '.join(f'{v:.4f}' for v in gs)}")
    chk("G-B2 so g(sqrt2 x) = g(x) has no solution at finite x",
        all(g(root2 * x) > g(x) for x in xs),
        "thermal equipartition is exact only in the limit x -> 0")
    # reproduce the recorded numbers
    x0 = X1_CORPUS / root2
    rho2 = 0.5 * g(X1_CORPUS) / g(x0)
    q_corpus = 1.0 / 3.0 + (2.0 / 3.0) * rho2
    chk("G-B3 at the corpus's x_1 = 2/9 the miss is the recorded 1025 ppm",
        abs(abs(q_corpus / Q_TARGET - 1) * 1e6 - 1025.4) < 0.5,
        f"{abs(q_corpus/Q_TARGET - 1)*1e6:.1f} ppm")
    lo, hi = 1e-6, 10.0
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        q = 1.0 / 3.0 + (2.0 / 3.0) * (0.5 * g(mid) / g(mid / root2))
        if abs(q / Q_TARGET - 1) > EXACTNESS:
            hi = mid
        else:
            lo = mid
    x_max = math.sqrt(lo * hi)
    chk("G-B4 and the 6 ppm ceiling is the recorded x_1 <= 0.0170", abs(x_max - 0.016971) < 1e-4,
        f"x_1 <= {x_max:.6f}, i.e. n_bar >= {1/(math.exp(x_max)-1):.1f}")

    # ---- G-C ----------------------------------------------------------------
    print("\n  G-C  why thermal is the BEST flat law: its linear term cancels")
    # e/kT = g(x) = 1 + x^2/12 - x^4/720 + ...  -- no O(x) term
    lin = (g(1e-6) - g(0.0)) / 1e-6
    chk("G-C1 dg/dx -> 0 as x -> 0, so there is no O(x) term", abs(lin) < 1e-5,
        f"slope at origin = {lin:.3e}")
    quad = (g(1e-3) - 1.0) / (1e-3 ** 2)
    chk("G-C2 and the leading term is x^2/12", abs(quad - 1.0 / 12.0) < 1e-6,
        f"coefficient {quad:.9f} vs 1/12 = {1/12:.9f}")

    # ---- G-D ----------------------------------------------------------------
    print("\n  G-D  a DRIVEN flat law still carries the mode's zero point — O(x)")
    print("       e = E_0 + hbar w/2, so e(w_1)/e(w_0) = (u + sqrt2)/(u + 1),"
          " u = E_0/(hbar w_0/2)")
    u_need = (root2 - 1.0) / EXACTNESS - 1.0
    n_need = u_need / 2.0
    chk("G-D1 6 ppm needs u = (sqrt2-1)/delta - 1", abs(u_need - 69034.2) < 1.0,
        f"u = {u_need:.1f}")
    chk("G-D2 i.e. about 34,500 quanta per mode", abs(n_need - 34517.1) < 1.0,
        f"n = E_0/(hbar w_0) = {n_need:.1f}")
    n_thermal = 1.0 / (math.exp(x_max) - 1.0)
    chk("G-D3 against thermal's ~58 for the same budget — a factor ~591",
        n_need / n_thermal > 100,
        f"driven {n_need:.0f} vs thermal {n_thermal:.1f}, ratio {n_need/n_thermal:.0f}x")
    print("       -> equilibrium is not one flat law among many. It is the one whose")
    print("          leading frequency correction cancels, and it is ~591x cheaper.")

    # ---- G-E ----------------------------------------------------------------
    print("\n  G-E  an EXACT third class: a log-symmetric deposition spectrum")
    w0, w1 = 1.0, root2
    w_geo = math.sqrt(w0 * w1)
    print(f"       w_0 = {w0}, w_1 = sqrt2 = {w1:.6f}, geometric mean = {w_geo:.9f}"
          f" = 2^(1/4) = {2**0.25:.9f}")
    chk("G-E1 the geometric mean is 2^(1/4) w_0", abs(w_geo - 2 ** 0.25) < TOL)

    def lognormal(w, wp, sigma):
        return math.exp(-((math.log(w) - math.log(wp)) ** 2) / (2 * sigma ** 2))

    print(f"\n    {'sigma':>8} {'e(w_0)':>14} {'e(w_1)':>14} {'|ratio-1|':>12}")
    worst = 0.0
    for sig in (0.05, 0.2, 0.5, 1.0, 3.0):
        a, b = lognormal(w0, w_geo, sig), lognormal(w1, w_geo, sig)
        d = abs(b / a - 1.0)
        worst = max(worst, d)
        print(f"    {sig:8.2f} {a:14.9f} {b:14.9f} {d:12.3e}")
    chk("G-E2 flat EXACTLY at every width tested", worst < 1e-12,
        f"worst deviation {worst:.3e} — the condition fixes WHERE, not HOW BROAD")
    r_ln = eps_ratio_from(lambda e: lognormal(math.sqrt(e), w_geo, 0.4))
    chk("G-E3 and it delivers eps_1/eps_0 = 2 through the null solver",
        abs(r_ln - 2.0) < 1e-5, f"{r_ln:.9f}")

    # ---- G-F ----------------------------------------------------------------
    print("\n  G-F  a second exact route: a TWO-TEMPERATURE freeze")
    # e_S = T_S g(hbar w_0/T_S), e_D = T_D g(hbar w_1/T_D); solve e_D = e_S for T_D/T_S
    T_S = 1.0
    x0c = X1_CORPUS / root2                     # hbar w_0 / T_c
    e_S = T_S * g(x0c)
    lo, hi = 1e-3, 1e3
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if mid * g(X1_CORPUS / mid) > e_S:
            hi = mid
        else:
            lo = mid
    T_D = math.sqrt(lo * hi)
    chk("G-F1 an exact solution exists for T_D/T_S", abs(T_D * g(X1_CORPUS / T_D) - e_S) < 1e-12,
        f"T_D/T_S = {T_D:.6f}")
    chk("G-F2 and it is not 1 — the sectors must be at different temperatures",
        abs(T_D - 1.0) > 1e-4, f"a {abs(T_D-1)*100:.3f}% temperature split")

    # ---- G-G: anti-control --------------------------------------------------
    print("\n  G-G  ANTI-CONTROL: does the geometric-mean centring do any work?")
    off = []
    for wp in (1.0, 1.1, w_geo, 1.3, root2):
        a, b = lognormal(w0, wp, 0.4), lognormal(w1, wp, 0.4)
        off.append((wp, abs(b / a - 1.0)))
        print(f"       w_p = {wp:.6f}:  |e(w_1)/e(w_0) - 1| = {abs(b/a - 1.0):.6e}")
    good = [wp for wp, d in off if d < EXACTNESS]
    chk("G-G1 ONLY the geometric mean is flat", len(good) == 1 and abs(good[0] - w_geo) < TOL,
        f"flat at {[f'{v:.6f}' for v in good]}")

    # ---- G-H: anti-control --------------------------------------------------
    print("\n  G-H  ANTI-CONTROL: width-independent, but frequency-DEPENDENT?")
    # the peak must move with w_0 -- otherwise the condition ties nothing to the ring
    peaks = [math.sqrt(w * (root2 * w)) for w in (0.5, 1.0, 2.0, 7.3)]
    chk("G-H1 the required peak moves with w_0", len(set(round(p, 9) for p in peaks)) == 4,
        f"peaks {', '.join(f'{p:.4f}' for p in peaks)} for w_0 = 0.5, 1, 2, 7.3")
    chk("G-H2 always at the same RATIO 2^(1/4) to w_0",
        all(abs(p / (w * 2 ** 0.25) - 1) < TOL
            for p, w in zip(peaks, (0.5, 1.0, 2.0, 7.3))),
        "so it is one condition tying the spectrum to the ring, not a free function")

    # ---- G-I: anti-control --------------------------------------------------
    print("\n  G-I  ANTI-CONTROL: is the reduction vacuous?")
    known = (("zero-point, e ~ sqrt(eps)", lambda e: e ** 0.5, 4.0),
             ("sudden quench, e ~ 1/eps", lambda e: 1.0 / e, math.sqrt(2)),
             ("equal amplitude, e ~ eps", lambda e: e, None))
    ok_known = True
    for name, law, expect in known:
        flat = abs(law(2.0) / law(1.0) - 1.0) < TOL
        ok_known &= not flat
        if expect is not None:
            r = eps_ratio_from(law)
            hit = abs(r - expect) < 1e-5
            ok_known &= hit
            print(f"       {name:<28} flat? no   eps_1/eps_0 = {r:.6f}"
                  f" (recorded {expect:.6f}) {'ok' if hit else 'MISMATCH'}")
        else:
            print(f"       {name:<28} flat? no   (degenerate: no solution, see #85)")
    chk("G-I1 laws known to fail DO fail the flatness test, and reproduce their"
        " recorded ratios", ok_known)

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — A THIRD CLASS EXISTS, AND IT IS EXACTLY CHARACTERISED")
    print("=" * 78)
    print("""
  THE WHOLE DOCKET REDUCES TO ONE CONDITION. Combining the null (2 e(eps_1)/eps_1 =
  e(eps_0)/eps_0) with Q = 2/3's requirement eps_1/eps_0 = 2, the 2s cancel and what
  remains is

      e(2 eps_0) = e(eps_0)

  -- the delivery law must be FLAT across a factor sqrt2 in frequency. Every earlier
  result is downstream: among power laws only p = 0 is flat (G-A3), which re-derives
  the (s,p) family's uniqueness verdict from something simpler; and the occupancy lock
  fails because integer counts cannot be flattened (#86).

  THERMAL EQUILIBRIUM IS NOT AN ARBITRARY CHOICE. It is the flat law whose LINEAR
  frequency correction cancels: e = kT + (hbar w)^2/(12 kT), no O(w) term (G-C). A
  driven law that deposits E_0 per mode is equally "flat" in its deposit but still
  carries the mode's own zero point, giving a FIRST-order error -- and needing ~34,500
  quanta per mode against thermal's ~58 for the same 6 ppm (G-D). Thermal is roughly
  591x cheaper. That reframes the contradiction: equilibrium was already the best
  available answer, which is why it being 171x over budget hurts.

  BUT STRICTLY INCREASING IS STRICTLY INCREASING (G-B). g(x) rises monotonically, so
  g(sqrt2 x) = g(x) has no finite-x solution. Thermal is exact only in the limit. AN
  EXACT LAW MUST THEREFORE BE NON-MONOTONIC IN w -- and that is the whole content of
  "a third class".

  TWO EXACT ROUTES, AND BOTH COST EXACTLY ONE NUMBER.

  (1) A DEPOSITION SPECTRUM SYMMETRIC IN log w, centred on the GEOMETRIC MEAN of the
      two sector frequencies: w_p = sqrt(w_0 w_1) = 2^(1/4) w_0. This is exact, and
      exact AT ANY WIDTH (G-E) -- the condition fixes where the spectrum sits, not how
      broad it is, so it is not fine-tuned in sigma. It is a symmetry statement, not a
      numerical coincidence. The anti-control confirms the centring is load-bearing:
      no other peak location is flat (G-G), and the required peak moves with w_0 while
      holding the ratio 2^(1/4), so it genuinely ties the spectrum to the ring (G-H).

  (2) A TWO-TEMPERATURE FREEZE, the sectors decoupling at different times. The free
      ratio T_D/T_S has an exact solution (G-F). Also one condition.

  WHAT THIS IS, AND WHAT IT IS NOT. It is a CLASSIFICATION: the third class exists, is
  non-empty, and is characterised completely by a single flatness condition, with two
  named realisations and their exact requirements. It is NOT a mechanism -- neither
  the peak location nor the temperature ratio is derived here, and each is one number
  the corpus does not currently supply.

  THE DEBT AFTER THIS. Not "does a third class exist" (yes) and not "what must it
  satisfy" (e(2 eps_0) = e(eps_0)), but: does anything in the model put a deposition
  peak at 2^(1/4) w_0, or split the two sectors' freeze temperatures? Route (1) is the
  more constrained of the two and therefore the more falsifiable -- a spectrum peak is
  a physical object with its own consequences, while a temperature ratio is a free
  parameter wearing a mechanism's clothes.
""")


if __name__ == "__main__":
    main()
