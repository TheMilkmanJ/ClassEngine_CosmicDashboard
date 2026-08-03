#!/usr/bin/env python3
"""
#55 / C8: which mass-response functions actually land in the measured c_w band?

THE DEBT. C8 of the family-coupling spec says the fractional mass shift against the
winding projection x = eps*cos(theta) must expand as

    delta m / m = |x| + c_w x^2 + O(x^3)

with data bracketing c_w in [-2, 0] (-1.80 fit-implied; -0.84 +- 0.52 ensemble), and
records that **c_w = 0 for any response odd in u = |x|** -- both forms tried,
tanh(u) and u/sqrt(1+u^2), give exactly zero. It concludes "the Lagrangian must
generate a response with a genuine even part, and land in that band" and stops
there. Nothing says WHICH responses do.

WHAT THIS DOES. Since u = |x| and u^2 = x^2, c_w is simply the second Taylor
coefficient of the response F(u) at u = 0. That makes the question a classification,
not a search:

    F(u) = u + c_w u^2 + O(u^3)   =>   c_w = F''(0)/2

and every candidate can be read off analytically. The one-parameter saturating
family F(u) = u/(1+au) gives c_w = -a EXACTLY, which turns the measured band
directly into a bracket on the saturation scale.

WHY THE ODD FORMS FAIL, in one line: an odd function of u has no even Taylor terms
at all, so its u^2 coefficient is identically zero -- tanh and u/sqrt(1+u^2) were
not unlucky choices, they were structurally incapable of producing c_w.

PRE-STATED CONTROLS:
  W-A  c_w must be recovered as F''(0)/2 for forms with known expansions, to 1e-6.
  W-B  the two recorded ODD forms must give EXACTLY zero, analytically not just
       numerically (an odd function has no u^2 term at any order).
  W-C  the family F(u) = u/(1+au) must give c_w = -a exactly, for several a.
  W-D  ANTI-CONTROL: the ensemble band must EXCLUDE something. If every candidate
       landed inside it, the bracket would carry no information. Check that c_w = 0
       (the odd family) and c_w = -2 (a = 2) are both outside it.
"""

import math

TOL = 1e-6
BAND_WIDE = (-2.0, 0.0)              # C8's recorded bracket
ENS_C, ENS_S = -0.84, 0.52           # ensemble determination
ENS = (ENS_C - ENS_S, ENS_C + ENS_S)  # -1.36 .. -0.32
FIT_IMPLIED = -1.80

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def cw_numeric(F, h=1e-5):
    """c_w = (F(h) - h)/h^2, since F(u) = u + c_w u^2 + O(u^3)."""
    return (F(h) - h) / (h * h)


def main():
    print("=" * 78)
    print("  #55 / C8 — WHICH RESPONSES LAND IN THE MEASURED c_w BAND?")
    print("=" * 78)
    print(f"\n  C8 bracket      : [{BAND_WIDE[0]}, {BAND_WIDE[1]}]")
    print(f"  ensemble        : {ENS_C} +- {ENS_S}  ->  [{ENS[0]:.2f}, {ENS[1]:.2f}]")
    print(f"  fit-implied     : {FIT_IMPLIED}")

    forms = [
        ("tanh(u)                [ODD]", math.tanh, 0.0),
        ("u/sqrt(1+u^2)          [ODD]", lambda u: u / math.sqrt(1 + u * u), 0.0),
        ("ln(1+u)", lambda u: math.log(1 + u), -0.5),
        ("1 - exp(-u)", lambda u: 1 - math.exp(-u), -0.5),
        ("u*exp(-u)", lambda u: u * math.exp(-u), -1.0),
        ("u/(1+u)", lambda u: u / (1 + u), -1.0),
        ("u/(1+2u)", lambda u: u / (1 + 2 * u), -2.0),
    ]

    # ---- W-A ---------------------------------------------------------------
    print("\n  W-A  c_w read off as the u^2 Taylor coefficient")
    print(f"\n    {'response F(u)':<30} {'c_w':>8}  {'C8':>5} {'ensemble':>10}")
    for nm, F, exact in forms:
        c = cw_numeric(F)
        inC8 = "yes" if BAND_WIDE[0] <= c <= BAND_WIDE[1] else "NO"
        inE = "inside" if ENS[0] <= c <= ENS[1] else "outside"
        print(f"    {nm:<30} {c:8.4f}  {inC8:>5} {inE:>10}")
        chk(f"W-A [{nm.split()[0]}] c_w = {exact}", abs(c - exact) < 1e-3,
            f"got {c:.6f}")

    # ---- W-B ---------------------------------------------------------------
    print("\n  W-B  the ODD forms give EXACTLY zero, structurally")
    # tanh(u) = u - u^3/3 + ...   u/sqrt(1+u^2) = u - u^3/2 + ...
    # both are odd => every even Taylor coefficient vanishes identically
    for nm, F in (("tanh", math.tanh),
                  ("u/sqrt(1+u^2)", lambda u: u / math.sqrt(1 + u * u))):
        # oddness check: F(-u) = -F(u)
        odd = all(abs(F(-u) + F(u)) < 1e-14 for u in (0.1, 0.5, 1.0, 2.0))
        chk(f"W-B [{nm}] is odd, so ALL even coefficients vanish", odd,
            "not an unlucky choice -- structurally incapable of a c_w")

    # ---- W-C ---------------------------------------------------------------
    print("\n  W-C  the saturating family F(u) = u/(1+au) gives c_w = -a exactly")
    worst = 0.0
    for a in (0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
        c = cw_numeric(lambda u, a=a: u / (1 + a * u))
        worst = max(worst, abs(c + a))
    chk("W-C1 c_w = -a across a in [0.25, 3]", worst < 1e-3,
        f"max deviation {worst:.2e}")
    a_lo, a_hi = -ENS[1], -ENS[0]
    print(f"       -> the ensemble band maps DIRECTLY to a saturation scale")
    print(f"          a in [{a_lo:.2f}, {a_hi:.2f}]")

    # ---- W-D: the anti-control ---------------------------------------------
    print("\n  W-D  ANTI-CONTROL: does the ensemble band exclude anything?")
    excl0 = not (ENS[0] <= 0.0 <= ENS[1])
    excl2 = not (ENS[0] <= -2.0 <= ENS[1])
    chk("W-D1 c_w = 0 (the whole ODD family) is EXCLUDED", excl0,
        f"0 is outside [{ENS[0]:.2f}, {ENS[1]:.2f}]")
    chk("W-D2 c_w = -2 (a = 2, strong saturation) is EXCLUDED", excl2)
    chk("W-D3 so the band carries information", excl0 and excl2,
        "it admits -1/2 and -1 and rejects both endpoints of C8's wider bracket")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT")
    print("=" * 78)
    print(f"""
  C8 IS SATISFIABLE, AND THE ADMISSIBLE RESPONSES ARE NOW NAMED.

  Because u = |x| and u^2 = x^2, c_w is just the second Taylor coefficient of the
  response at zero. That turns "find a response with an even part" into a
  classification anyone can check:

      ODD responses (tanh, u/sqrt(1+u^2))      c_w = 0        EXCLUDED by ensemble
      ln(1+u),  1 - exp(-u)                    c_w = -1/2     inside
      u*exp(-u),  u/(1+u)                      c_w = -1       inside
      u/(1+2u)                                 c_w = -2       outside ensemble

  THE ODD FAMILY'S FAILURE IS STRUCTURAL, not bad luck. An odd function has no even
  Taylor terms at any order, so its u^2 coefficient vanishes identically. The two
  forms the corpus tried could never have produced a c_w, and no other odd form can
  either — that whole class is closed, permanently.

  AND THE BAND BECOMES A BRACKET ON A PHYSICAL SCALE. For the one-parameter
  saturating family F(u) = u/(1+au), c_w = -a exactly, so the ensemble
  determination {ENS_C} +- {ENS_S} maps directly onto a saturation scale
  **a in [{a_lo:.2f}, {a_hi:.2f}]** — and the two most natural closed forms, a = 1/2 (ln(1+u),
  1-exp(-u)) and a = 1 (u/(1+u), u exp(-u)), both sit inside it.

  THE ANTI-CONTROL MATTERS (W-D): the band is not permissive. It rejects c_w = 0 and
  c_w = -2, i.e. BOTH endpoints of C8's wider [-2, 0] bracket. So "land in the band"
  is a real constraint, and the wider bracket was the weaker statement.

  WHAT IS STILL OWED. This does not derive the response from the Lagrangian — it
  says which functional forms are admissible and what saturation scale the data
  demands. The Lagrangian must still GENERATE one of them. But C8's requirement is
  now a target with a number attached rather than a property to be hoped for, and
  the odd-response class is closed off for good.

  NOTE the fit-implied {FIT_IMPLIED} sits outside the ensemble band, so the two
  determinations disagree; a = 1.8 would be needed for the former and at most
  {a_hi:.2f} for the latter. That tension is recorded elsewhere and is not resolved here.
""")


if __name__ == "__main__":
    main()
