#!/usr/bin/env python3
"""
#85, RE-OPENED AND CORRECTED. The delivery laws are NOT one exponent, and the
identification recorded earlier today was a coincidence fit against the wrong
quantity.

WHAT WENT WRONG, STATED FIRST. scripts/delivery_law_is_one_exponent.py read
eps_D/eps_S as a ratio of ENERGIES deposited per sector, and reproduced the four
recorded values {2, sqrt2, 1, 1/2} as 2*(k_D/k_S)^p at p in {0, 1/2, 1} on the
ring's normal-mode stiffnesses k_S = 6, k_D = 3.

But the corpus's eps is a STIFFNESS, not an energy. koide_frame_bridge.py writes
amplitude^2 = g * T / eps and koide_delivery_law_discriminator.py writes
w ~ sqrt(eps) and <f^2> ~ 1/eps. Both are unambiguous. So the earlier script fitted
four numbers with a quantity that is not the one the numbers denote -- protocol 42,
the proxy-is-not-the-quantity error, committed while the same session was writing
that trap up.

THE CORPUS'S ACTUAL ALGEBRA. The null R_c = M_c equates the SUMMED squared
amplitude of the 2-dof doublet with that of the 1-dof singlet. Write the deposited
energy per degree of freedom as e ~ eps^p, and let s record how the sector's total
is counted (s = 1 per-dof, s = 0 per-sector, s = -1 the "doublet gets half"
convention). Then amplitude^2 per sector is

    X^2  =  g^s * e / eps  ~  g^s * eps^(p-1)

and the null 2^s * eps_1^(p-1) = eps_0^(p-1) solves to

    eps_1 / eps_0  =  2^( s / (1 - p) )              [THE FAMILY]

TWO PARAMETERS, NOT ONE. All four recorded laws sit in this family, but at four
different (s, p):

    thermal equipartition   e = T/2 per dof      (s, p) = ( 1,  0)  ->  2
    sudden quench, 1/w^2    e ~ 1/eps per dof    (s, p) = ( 1, -1)  ->  sqrt2
    equal sector delivery   E per sector         (s, p) = ( 0,  *)  ->  1
    doublet gets half       E, E/2 per sector    (s, p) = (-1,  0)  ->  1/2

so the earlier claim that they are "one exponent with a bookkeeping duplicate" is
withdrawn. In particular sqrt2 is NOT the zero-point law: it is the sudden quench,
p = -1. The zero-point law is p = +1/2, and it gives 4, a value the recorded set of
four does not contain.

AND THE RESULT THAT MATTERS, WHICH THE ERROR WAS HIDING. Q = 2/3 requires rho^2 =
1/2, i.e. eps_1/eps_0 = 2 exactly, i.e. s/(1-p) = 1, i.e. s = 1 - p. That is a LINE
in (s, p), and only ONE of the four recorded laws lies on it. If s is restricted to
the two ways a sector total can actually be counted -- per degree of freedom (s = 1)
or per sector (s = 0) -- then s = 0 has no solution at any p, and s = 1 forces p = 0
uniquely. THERMAL EQUIPARTITION IS THE ONLY ADMISSIBLE DELIVERY LAW THAT YIELDS
KOIDE.

That converts the docket. It was "four laws and nothing selects among them". It is
now "the null selects thermal equipartition uniquely, and the discriminator has
already shown thermal equipartition cannot hold at 6 ppm at the corpus's own
frequency". Those two statements are in tension, and the tension is INSIDE the Koide
derivation rather than upstream of it.

PRE-STATED CONTROLS:
  E-A  the four recorded ratios must come back out of the bridge's OWN amplitude^2
       functions, solved numerically -- not out of my re-derivation.
  E-B  the closed form 2^(s/(1-p)) must reproduce all four at the stated (s, p).
  E-C  the family must be genuinely TWO-parameter: no single s with p varying, and
       no single p with s varying, can produce all four.
  E-D  the earlier construction must be shown to disagree with this one away from
       p = 0 -- if they agreed everywhere the earlier result would merely be a
       reparametrisation, not an error.
  E-E  the zero-point law (p = 1/2, s = 1) must give 4, outside the recorded set.
  E-F  Q = 2/3 must single out ratio 2, and the recorded ratios sqrt2, 1, 1/2, 4
       must all miss it by margins far outside 6 ppm.
  E-G  ANTI-CONTROL: p = 1 at s = 1 must be structurally EXCLUDED, not merely
       disfavoured -- at p = 1 amplitude^2 is eps-independent, so the null degenerates
       to 2 = 1 and converts into no stiffness statement at all. If this came out as
       a finite ratio the family would be hiding a singularity.
  E-H  ANTI-CONTROL: the family must not fit arbitrary targets at the four recorded
       (s, p) pairs -- check 3, 1/3, 5 are not produced.
"""

import math

TOL = 1e-12
Q_TARGET = 2.0 / 3.0
EXACTNESS = 6e-6

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# ---- the bridge's own amplitude^2 functions, transcribed verbatim ---------------
# from scripts/koide_frame_bridge.py, part 3. g = dof count, e = sector stiffness.
BRIDGE_LAWS = (
    ("thermal equipartition",        lambda g, e: g / e,                        2.0),
    ("equal sector delivery",        lambda g, e: 1.0 / e,                      1.0),
    ("doublet gets half the singlet", lambda g, e: (1.0 if g == 1 else 0.5) / e, 0.5),
    ("sudden quench, 1/w^2 per mode", lambda g, e: g / e ** 2,                   math.sqrt(2)),
)

# the same four in the (s, p) family
FAMILY = (
    ("thermal equipartition",         1, 0.0,  2.0),
    ("equal sector delivery",         0, 0.0,  1.0),
    ("doublet gets half the singlet", -1, 0.0, 0.5),
    ("sudden quench, 1/w^2 per mode",  1, -1.0, math.sqrt(2)),
)


def solve_ratio(amp2):
    """solve amp2(2, eps1) == amp2(1, 1.0) for eps1 -- the bridge's own method."""
    lo, hi = 1e-6, 1e6
    ref = amp2(1, 1.0)
    inc = amp2(2, hi) > amp2(2, lo)
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if (amp2(2, mid) > ref) == inc:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def family_ratio(s, p):
    return 2.0 ** (s / (1.0 - p))


def Q_of_ratio(r):
    """classical limit of the discriminator's Q: rho^2 = 1/r, Q = 1/3 + (2/3) rho^2."""
    return 1.0 / 3.0 + (2.0 / 3.0) / r


def main():
    print("=" * 78)
    print("  #85 CORRECTED — THE DELIVERY LAWS ARE A TWO-PARAMETER FAMILY")
    print("=" * 78)

    # ---- E-A ----------------------------------------------------------------
    print("\n  E-A  the four ratios, solved from the BRIDGE'S OWN amplitude^2 functions")
    print(f"\n    {'law':<32} {'solved eps_1/eps_0':>18} {'recorded':>10}")
    ok = True
    for name, amp2, rec in BRIDGE_LAWS:
        got = solve_ratio(amp2)
        good = abs(got - rec) < 1e-6
        ok &= good
        print(f"    {name:<32} {got:18.9f} {rec:10.6f}  {'' if good else '  <-- MISMATCH'}")
    chk("E-A1 all four bridge laws reproduce their recorded ratios", ok)

    # ---- E-B ----------------------------------------------------------------
    print("\n  E-B  the closed form  eps_1/eps_0 = 2^(s/(1-p))")
    print(f"\n    {'law':<32} {'s':>3} {'p':>6} {'2^(s/(1-p))':>14} {'recorded':>10}")
    ok = True
    for name, s, p, rec in FAMILY:
        got = family_ratio(s, p)
        good = abs(got - rec) < TOL
        ok &= good
        print(f"    {name:<32} {s:3d} {p:6.1f} {got:14.9f} {rec:10.6f}"
              f"  {'' if good else '  <-- MISMATCH'}")
    chk("E-B1 closed form reproduces all four exactly", ok)

    # ---- E-C ----------------------------------------------------------------
    print("\n  E-C  is it genuinely two-parameter?")
    targets = sorted(r for _, _, _, r in FAMILY)
    # (i) fix s, vary p: can any single s reach all four?
    reach_fixed_s = {}
    for s in (-1, 0, 1):
        hit = set()
        for r in targets:
            if s == 0:
                if abs(r - 1.0) < TOL:
                    hit.add(round(r, 9))
                continue
            # r = 2^(s/(1-p))  ->  1-p = s*ln2/ln r
            if r <= 0 or abs(math.log(r)) < TOL:
                continue
            hit.add(round(r, 9))
        reach_fixed_s[s] = hit
    chk("E-C1 no single s reaches all four (s=0 reaches only 1)",
        len(reach_fixed_s[0]) == 1,
        f"s=0 can only ever give 2^0 = 1, whatever p is")
    # (ii) fix p, vary s: s is a COUNTING label, so it is not a free real number
    hits_p0 = {round(family_ratio(s, 0.0), 9) for s in (-1, 0, 1)}
    chk("E-C2 fixing p = 0 and varying the counting s gives {1/2, 1, 2} but not sqrt2",
        hits_p0 == {0.5, 1.0, 2.0} and round(math.sqrt(2), 9) not in hits_p0,
        f"{sorted(hits_p0)}")
    chk("E-C3 so sqrt2 requires p != 0 AND 2 requires s != 0 — both parameters load-bearing",
        abs(family_ratio(1, -1.0) - math.sqrt(2)) < TOL and abs(family_ratio(0, -1.0) - 1) < TOL)

    # ---- E-D ----------------------------------------------------------------
    print("\n  E-D  the earlier construction vs this one — where do they part?")
    print("       earlier: ratio = 2*(k_D/k_S)^p = 2^(1-p)   [an ENERGY ratio]")
    print("       correct: ratio = 2^(s/(1-p)) at s = 1      [a STIFFNESS ratio]")
    print(f"\n    {'p':>6} {'earlier 2^(1-p)':>16} {'correct 2^(1/(1-p))':>21}   agree?")
    agree_at, differ_at = [], []
    for p in (-1.0, -0.5, 0.0, 0.5, 0.75):
        old = 2.0 ** (1.0 - p)
        new = family_ratio(1, p)
        same = abs(old - new) < 1e-9
        (agree_at if same else differ_at).append(p)
        print(f"    {p:6.2f} {old:16.9f} {new:21.9f}   {'yes' if same else 'NO'}")
    chk("E-D1 the two constructions agree ONLY at p = 0", agree_at == [0.0],
        f"agree at {agree_at}, differ at {differ_at}")
    chk("E-D2 so the earlier p = 1/2 -> sqrt2 identification was a coincidence",
        abs(2.0 ** (1.0 - 0.5) - math.sqrt(2)) < TOL and abs(family_ratio(1, 0.5) - 4.0) < TOL,
        "earlier gives sqrt2 at p=1/2; the corpus's algebra gives 4 there")
    chk("E-D3 and the corpus's sqrt2 is the SUDDEN QUENCH, p = -1, not zero-point",
        abs(family_ratio(1, -1.0) - math.sqrt(2)) < TOL)

    # ---- E-E ----------------------------------------------------------------
    print("\n  E-E  where does the zero-point law actually land?")
    zp = family_ratio(1, 0.5)
    print(f"       e per dof = (1/2) hbar w ~ eps^(1/2)  =>  s = 1, p = 1/2")
    print(f"       eps_1/eps_0 = {zp:.9f}")
    chk("E-E1 zero-point delivery gives 4", abs(zp - 4.0) < TOL)
    chk("E-E2 which is NOT in the recorded set {2, sqrt2, 1, 1/2}",
        all(abs(zp - r) > 1e-6 for _, _, _, r in FAMILY),
        "so the recorded four were never exhaustive — T6 already calls the lock 'a fifth law'")

    # ---- E-F ----------------------------------------------------------------
    print("\n  E-F  which ratio does Q = 2/3 actually require?")
    print(f"\n    {'ratio':>12} {'Q (classical)':>16} {'ppm from 2/3':>16}")
    hits = []
    for label, r in (("2", 2.0), ("sqrt2", math.sqrt(2)), ("1", 1.0), ("1/2", 0.5), ("4", 4.0)):
        q = Q_of_ratio(r)
        ppm = abs(q / Q_TARGET - 1) * 1e6
        if ppm < EXACTNESS * 1e6:
            hits.append(label)
        print(f"    {label:>12} {q:16.9f} {ppm:16.1f}")
    chk("E-F1 exactly one recorded ratio gives Q = 2/3, and it is 2", hits == ["2"], f"{hits}")
    chk("E-F2 the Koide condition is the LINE s = 1 - p", abs(family_ratio(0.5, 0.5) - 2.0) < TOL,
        "e.g. (s,p) = (1/2,1/2) also gives 2 — but s is a counting label, not a free real")
    chk("E-F3 with s in {0,1}: s=0 impossible at any p, s=1 forces p=0 uniquely",
        abs(family_ratio(0, 0.3) - 1.0) < TOL and abs(family_ratio(1, 0.0) - 2.0) < TOL
        and all(abs(family_ratio(1, p) - 2.0) > 1e-9 for p in (-1.0, -0.5, 0.25, 0.5)),
        "-> thermal equipartition is the unique admissible law yielding Koide")

    # ---- E-G: anti-control --------------------------------------------------
    print("\n  E-G  ANTI-CONTROL: is p = 1 excluded structurally, or just disfavoured?")
    # amplitude^2 ~ g^s eps^(p-1); at p = 1 the eps dependence vanishes identically
    a_lo = 2 ** 1 * (0.001 ** (1.0 - 1.0))
    a_hi = 2 ** 1 * (1000.0 ** (1.0 - 1.0))
    chk("E-G1 at p = 1 the doublet's amplitude^2 is eps-INDEPENDENT",
        abs(a_lo - a_hi) < TOL and abs(a_lo - 2.0) < TOL,
        f"X^2(eps=1e-3) = {a_lo}, X^2(eps=1e3) = {a_hi}")
    chk("E-G2 so the null degenerates to 2 = 1 and fixes NO stiffness ratio",
        abs(a_lo - 1.0) > TOL, "the equation is inconsistent, not solvable")
    # tested in logs: the ratio itself overflows a float long before p reaches 1,
    # which is the point, but a control should demonstrate that rather than crash on it.
    log2_ratio = [1.0 / (1.0 - p) for p in (0.9, 0.99, 0.999, 0.9999)]
    chk("E-G3 and the closed form diverges there, as it must",
        all(b > a for a, b in zip(log2_ratio, log2_ratio[1:])) and log2_ratio[-1] > 9e3,
        f"log2(ratio) = {', '.join(f'{v:.0f}' for v in log2_ratio)} as p -> 1: a "
        "singularity, not a fourth data point")
    print("       -> 'equal amplitude' is the NULL ITSELF, not a delivery law. A law that")
    print("          leaves every mode at the same amplitude satisfies R_c = M_c for any")
    print("          stiffness whatever, so it carries no information. The earlier script's")
    print("          'p = 1 <-> equal amplitude <-> ratio 1' row was three errors in one.")

    # ---- E-H: anti-control --------------------------------------------------
    print("\n  E-H  ANTI-CONTROL: does the family fit arbitrary targets?")
    produced = {round(family_ratio(s, p), 9) for _, s, p, _ in FAMILY}
    bad = [t for t in (3.0, 1.0 / 3.0, 5.0) if round(t, 9) in produced]
    chk("E-H1 3, 1/3, 5 are NOT produced at the four recorded (s,p)", not bad,
        f"produced = {sorted(produced)}")

    # ---- E-I ----------------------------------------------------------------
    print("\n  E-I  which stiffness pair IS eps_0, eps_1? (C3's question, re-asked correctly)")
    # the two pairs C3 warns must not be conflated:
    k_S, k_D = 6.0, 3.0                       # radial Hessian normal-mode stiffnesses
    radial = k_D / k_S
    b_over_a = math.sqrt(2.0) / 2.0           # A = 2|b|/a = sqrt2 at the Koide point
    e0, e1 = 1.0 + 2.0 * b_over_a, 1.0 - b_over_a   # circulant amplitude stiffnesses
    circulant = e1 / e0
    print(f"       radial Hessian     k_D/k_S             = {radial:.6f}")
    print(f"       circulant at Koide (a-b)/(a+2b)        = {circulant:.6f}"
          f"   [inverse {1/circulant:.4f}]")
    print(f"       what the null REQUIRES for Q = 2/3     = 2.000000")
    chk("E-I1 the required 2 is NOT the radial ratio", abs(radial - 2.0) > 1e-6,
        f"radial gives {radial:.6f} — that is law 3, which yields Q = 5/3")
    chk("E-I2 nor the circulant ratio at the Koide point", abs(circulant - 2.0) > 1e-6,
        f"circulant gives {circulant:.6f}")
    chk("E-I3 and the two differ from each other, as C3 says", abs(radial - circulant) > 1e-6,
        f"{radial:.6f} vs {circulant:.6f}")
    print("       -> so the delivery law's eps is a THIRD stiffness pair, distinct from both.")
    print("          C3's warning is EXTENDED, not resolved. The earlier claim that the law")
    print("          'is a radial-sector statement' is withdrawn: identifying eps with the")
    print("          radial pair forces eps_D/eps_S = 1/2, i.e. law 3, i.e. Q = 5/3.")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE EARLIER #85 FINDING IS WITHDRAWN AND REPLACED")
    print("=" * 78)
    print("""
  WITHDRAWN. "The four delivery laws are one exponent p in {0, 1/2, 1}, with the 1/2
  a bookkeeping duplicate." That read eps_D/eps_S as an energy ratio; the corpus's
  eps is a stiffness, fixed by <f^2> ~ 1/eps and w ~ sqrt(eps) in two separate
  scripts. The two constructions agree at p = 0 and nowhere else (E-D), so the match
  at sqrt2 and 1 was a coincidence of small powers of 2. Protocol 42.

  ALSO WITHDRAWN: the three labels. sqrt2 is the SUDDEN QUENCH (e ~ 1/eps, p = -1),
  not the zero-point law; the zero-point law gives 4 and is absent from the recorded
  four. And "equal amplitude" is not a delivery law at all -- it is the null itself,
  and imposes nothing (E-G).

  REPLACED BY, and this is stronger than what it replaces:

    eps_1/eps_0 = 2^( s / (1 - p) ),   e ~ eps^p per dof,  s the counting label

  a TWO-parameter family holding all four recorded laws at four distinct (s, p), plus
  the zero-point law at (1, 1/2) -> 4. Both parameters are load-bearing: sqrt2 needs
  p != 0, and 2 needs s != 0 (E-C).

  AND THE DOCKET'S QUESTION IS ANSWERED, NOT NARROWED. Q = 2/3 needs rho^2 = 1/2,
  hence eps_1/eps_0 = 2 EXACTLY, hence s = 1 - p. Of the five laws on the table only
  thermal equipartition lies on that line, and the next-nearest, sqrt2, misses 2/3 by
  2.07e5 ppm against a 6 ppm budget (E-F). With s restricted to the two ways a sector
  total can be counted, s = 0 fails at every p and s = 1 forces p = 0 alone.

  SO THE FORK WAS NEVER FOUR-WAY. The null selects thermal equipartition uniquely --
  and koide_delivery_law_discriminator.py has already shown thermal equipartition
  overruns the 6 ppm budget by 171x at the corpus's own x_1 = 2/9. Those two results
  are in DIRECT tension, and the tension sits inside the Koide derivation rather than
  upstream of it. The occupancy lock is not one option among four; it is the only
  named escape from a contradiction.

  WHAT THIS COSTS AND WHAT IT DOES NOT. It does not touch Q = 2/3 itself, which is
  measured. It does not touch the ring's mode structure. It does mean the docket's
  "highest-leverage, four laws in different rooms" framing overstated the freedom:
  four of the five were already excluded by the null, and nobody had checked.
""")


if __name__ == "__main__":
    main()
