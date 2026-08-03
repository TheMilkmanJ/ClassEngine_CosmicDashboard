#!/usr/bin/env python3
"""
Verify the radio-lattice paper's Table I from the underlying scalings, in exact
rational arithmetic. Both columns, and the ratio row the paper quotes.

WHY THIS EXISTS. The paper's whole discriminating claim is that the m_e and alpha
weight vectors are not proportional. That claim lives entirely in one table, and the
table was written by hand. Nothing in the corpus checked it. A wrong entry would not
show up as a build error, a bad citation or a failed control -- it would ship.

THE SCALINGS, each standard and each cited in the paper:

  21 cm hyperfine   nu_hf ~ alpha^2 (m_e/m_p) g_p R_inf,  R_inf ~ alpha^2 m_e
                          => nu_hf ~ alpha^4 m_e^2 / m_p
  RRL               nu ~ R_inf ~ alpha^2 m_e
  dispersion delay  t ~ e^2/m_e ~ alpha/m_e   (Gaussian: e^2 = alpha hbar c)
                    the INFERRED column divides out the laboratory constant, so the
                    reconstructed DM inherits the ratio true/lab
  synchrotron       nu_c ~ eB/m_e ~ alpha^(1/2) B / m_e   at FIXED field
  Faraday RM        RM ~ e^3/m_e^2 ~ alpha^(3/2) / m_e^2

PRE-STATED CONTROLS:
  T-A  each m_e weight must come out as the paper's Table I column, in exact fractions.
  T-B  each alpha weight likewise.
  T-C  the paper's quoted ratio row w_alpha/w_me = 2, 2, -1, -1/2, -3/4 must reproduce.
  T-D  the qualitative claim must hold: every alpha weight strictly positive, while the
       m_e weights change sign across the set.
  T-E  the vectors must NOT be proportional -- that is the paper's discriminator, so it
       has to be checked and not assumed.
  T-F  ANTI-CONTROL: a deliberately mis-entered weight must break T-C or T-E, otherwise
       those checks are not sensitive to the thing they are guarding.
  T-G  the sum of squared m_e weights must be 11, and the 21cm/Faraday pair 8 -- the two
       numbers the sensitivity section quotes as sigma/sqrt(11) and sigma/sqrt(8).
"""

from fractions import Fraction as F

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# exponents of (alpha, m_e) in each observable, from the scalings in the docstring
SCALING = {
    "21 cm hyperfine":        (F(4),     F(2)),    # alpha^4 m_e^2 / m_p
    "radio recombination":    (F(2),     F(1)),    # alpha^2 m_e
    "dispersion measure":     (F(1),     F(-1)),   # alpha / m_e
    "synchrotron nu_c":       (F(1, 2),  F(-1)),   # alpha^(1/2) / m_e
    "Faraday rotation":       (F(3, 2),  F(-2)),   # alpha^(3/2) / m_e^2
}

# the paper's Table I, transcribed
PAPER_ME    = [F(2), F(1), F(-1), F(-1), F(-2)]
PAPER_ALPHA = [F(4), F(2), F(1),  F(1, 2), F(3, 2)]
PAPER_RATIO = [F(2), F(2), F(-1), F(-1, 2), F(-3, 4)]


def main():
    print("=" * 78)
    print("  RADIO-LATTICE TABLE I — VERIFIED FROM THE SCALINGS")
    print("=" * 78)
    rows = list(SCALING.items())

    print(f"\n    {'observable':<24} {'w(m_e)':>8} {'paper':>7} {'w(alpha)':>10} {'paper':>7}")
    ok_me = ok_al = True
    for i, (name, (a_exp, m_exp)) in enumerate(rows):
        ok_me &= (m_exp == PAPER_ME[i])
        ok_al &= (a_exp == PAPER_ALPHA[i])
        print(f"    {name:<24} {str(m_exp):>8} {str(PAPER_ME[i]):>7}"
              f" {str(a_exp):>10} {str(PAPER_ALPHA[i]):>7}")

    chk("T-A1 every m_e weight matches Table I exactly", ok_me)
    chk("T-B1 every alpha weight matches Table I exactly", ok_al)

    # ---- T-C ----------------------------------------------------------------
    print("\n  T-C  the quoted ratio row")
    ratios = [a / m for (_, (a, m)) in rows]
    print("       computed:", ", ".join(str(r) for r in ratios))
    print("       paper:   ", ", ".join(str(r) for r in PAPER_RATIO))
    chk("T-C1 w_alpha/w_me reproduces 2, 2, -1, -1/2, -3/4", ratios == PAPER_RATIO)

    # ---- T-D ----------------------------------------------------------------
    print("\n  T-D  the qualitative claim")
    al = [a for (_, (a, _)) in rows]
    me = [m for (_, (_, m)) in rows]
    chk("T-D1 every alpha weight is strictly positive", all(x > 0 for x in al),
        "so a shift in alpha moves all five the same way")
    chk("T-D2 the m_e weights change sign across the set",
        any(x > 0 for x in me) and any(x < 0 for x in me),
        f"{sum(1 for x in me if x>0)} up, {sum(1 for x in me if x<0)} down")

    # ---- T-E ----------------------------------------------------------------
    print("\n  T-E  are the two vectors proportional? (the discriminator)")
    chk("T-E1 no single constant maps one column onto the other",
        len(set(ratios)) > 1,
        f"{len(set(ratios))} distinct ratios among 5 rows — proportionality would give 1")

    # ---- T-F: anti-control --------------------------------------------------
    print("\n  T-F  ANTI-CONTROL: would a mis-entered weight be caught?")
    bad = list(PAPER_ALPHA); bad[3] = F(1)        # synchrotron 1/2 -> 1, a plausible slip
    bad_ratio = [b / m for b, m in zip(bad, PAPER_ME)]
    chk("T-F1 a wrong synchrotron alpha-weight breaks the ratio row",
        bad_ratio != PAPER_RATIO,
        "so T-C is sensitive to the entry it guards")
    prop = [F(2)] * 5                              # a deliberately proportional column
    chk("T-F2 and a proportional column would be caught by T-E",
        len(set(p / m for p, m in zip([2 * x for x in PAPER_ME], PAPER_ME))) == 1,
        "a genuinely proportional pair collapses to one ratio, which T-E rejects")

    # ---- T-G ----------------------------------------------------------------
    print("\n  T-G  the sensitivity normalisations")
    s_all = sum(m * m for m in me)
    s_pair = PAPER_ME[0] ** 2 + PAPER_ME[4] ** 2   # 21 cm and Faraday
    chk("T-G1 sum of squared m_e weights is 11", s_all == 11, f"{s_all}")
    chk("T-G2 the 21cm/Faraday pair gives 8", s_pair == 8,
        f"{s_pair} — the sigma/sqrt(8) the paper now forecasts")

    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — TABLE I IS CORRECT IN BOTH COLUMNS")
    print("=" * 78)
    print("""
  All ten entries reproduce from the standard scalings in exact rational arithmetic,
  as does the ratio row the paper quotes, and both normalisations the sensitivity
  section depends on (11 for all five bands, 8 for the 21 cm / Faraday pair).

  The discriminating claim holds and is now checked rather than asserted: every alpha
  weight is positive, so a varying fine-structure constant moves all five observables
  the same way, while the m_e weights split two up and three down. The columns are not
  proportional -- the five rows give FOUR distinct ratios (the two line rows share 2,
  since both scale as R_inf times a power of alpha), where proportionality would give
  exactly one. The anti-control confirms the check bites: changing the synchrotron
  alpha-weight from 1/2 to 1, an easy slip, breaks the ratio row immediately.

  This was the paper's one substantive claim with no computational backing. It has one
  now.
""")


if __name__ == "__main__":
    main()
