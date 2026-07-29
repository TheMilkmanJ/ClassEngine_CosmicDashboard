#!/usr/bin/env python3
"""
#51's third horn, verified: no Dirac cone exists in the Standard Model roster.

THE CLAIM (PRTOE_hierarchy_problem.md). The chiral chemical potential mu_5 = theta-dot/2
= 29.85 eV is derived, but it is "undetermined by construction" because at the shell
scale there is nothing for it to act on. Two legs carry that:

  (i)  at Lambda_shell = 5.4e17 GeV electroweak symmetry is unbroken, so the screened
       abelian charge is HYPERCHARGE, not electric charge -- and over the roster
       sum(Y^2) = 10, not sum(Q^2) = 16. The corpus validates the 10 by noting the
       Standard Model's own hypercharge beta coefficient (2/3) sum_f Y^2 +
       (1/3) sum_scalar Y^2 returns 41/6 on it exactly.
  (ii) NO SPECIES IS VECTOR-LIKE. Every left-handed field is an SU(2) doublet and every
       right-handed one a singlet, so no opposite-chirality Weyl pair shares a
       representation. "There is no Dirac cone in the 48 for a chiral chemical
       potential to sit on."

Both legs are finite arithmetic over a fixed roster, so both can be checked rather
than trusted. That is what this does. Leg (ii) in particular is an OBSTRUCTION
rather than a shortage of candidates, which is a much stronger statement than "none
was found" -- and it is worth having verified, because the whole docket's status
("dissolves rather than is answered") rests on it.

PRE-STATED CONTROLS:
  H-A  the one-generation hypercharge sum must be 10/3, and the three-generation
       total exactly 10, with the state counting (colour x weak) explicit.
  H-B  the Standard Model hypercharge beta coefficient must come out 41/6 EXACTLY
       from that sum plus the Higgs doublet -- this is the independent validation
       the corpus cites, and it fails loudly if sum(Y^2) is wrong.
  H-C  sum(Q^2) must be 16, so the two numbers really are different and the
       broken/unbroken distinction is doing work.
  H-D  NO left-handed field shares a gauge representation with any right-handed one
       -- checked exhaustively over the roster, which is what "chiral gauge theory"
       means operationally and what forbids a Dirac cone.
  H-E  ANTI-CONTROL: adding a vector-like pair (a hypothetical heavy Dirac fermion)
       must MAKE the check fail. If it does not, H-D is not testing anything.
"""

from fractions import Fraction as F

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# (name, chirality, SU(3) dim, SU(2) dim, hypercharge Y)  -- Q = T3 + Y convention
ROSTER = [
    ("Q_L  quark doublet", "L", 3, 2, F(1, 6)),
    ("u_R  up singlet",    "R", 3, 1, F(2, 3)),
    ("d_R  down singlet",  "R", 3, 1, F(-1, 3)),
    ("L    lepton doublet", "L", 1, 2, F(-1, 2)),
    ("e_R  electron singlet", "R", 1, 1, F(-1)),
]
N_GEN = 3


def main():
    print("=" * 78)
    print("  #51 THIRD HORN — NO DIRAC CONE IN THE STANDARD MODEL ROSTER")
    print("=" * 78)

    # ---- H-A: the hypercharge sum ------------------------------------------
    print("\n  H-A  sum(Y^2) over one generation, states counted explicitly")
    print(f"\n    {'field':<24} {'states':>7} {'Y':>8} {'states*Y^2':>12}")
    tot = F(0)
    for nm, chi, c, w, Y in ROSTER:
        n = c * w
        contrib = n * Y * Y
        tot += contrib
        print(f"    {nm:<24} {n:7d} {str(Y):>8} {str(contrib):>12}")
    print(f"    {'':<24} {'':>7} {'TOTAL':>8} {str(tot):>12}")
    chk("H-A1 one generation gives 10/3", tot == F(10, 3), f"{tot}")
    tot3 = tot * N_GEN
    chk("H-A2 three generations give exactly 10", tot3 == 10, f"{tot3}")

    # ---- H-B: the independent validation -----------------------------------
    print("\n  H-B  the SM hypercharge beta coefficient validates it")
    # Higgs doublet: 2 complex states, Y = 1/2
    higgs = 2 * F(1, 2) ** 2
    b_Y = F(2, 3) * tot3 + F(1, 3) * higgs
    chk("H-B1 Higgs doublet contributes sum(Y^2) = 1/2", higgs == F(1, 2), f"{higgs}")
    chk("H-B2 (2/3)*10 + (1/3)*(1/2) = 41/6 EXACTLY", b_Y == F(41, 6),
        f"{b_Y}  = {float(b_Y):.6f}")
    print("       -> this is the Standard Model's own one-loop b_Y. It reproduces only")
    print("          if sum(Y^2) = 10, so the 10 is validated, not asserted.")

    # ---- H-C: Q^2 is a different number ------------------------------------
    print("\n  H-C  the broken-phase charge gives a DIFFERENT number")
    # electric charges: Q = T3 + Y.  doublets split into T3 = +-1/2
    qsum = F(0)
    for nm, chi, c, w, Y in ROSTER:
        if w == 2:
            for t3 in (F(1, 2), F(-1, 2)):
                qsum += c * (t3 + Y) ** 2
        else:
            qsum += c * Y ** 2
    qsum3 = qsum * N_GEN
    chk("H-C1 sum(Q^2) over three generations = 16", qsum3 == 16, f"{qsum3}")
    chk("H-C2 so 10 != 16 — the phase distinction is load-bearing", tot3 != qsum3,
        f"unbroken {tot3} vs broken {qsum3}")

    # ---- H-D: no vector-like pair ------------------------------------------
    print("\n  H-D  NO left-handed field shares a representation with a right-handed one")
    Ls = [(c, w, Y, nm) for nm, chi, c, w, Y in ROSTER if chi == "L"]
    Rs = [(c, w, Y, nm) for nm, chi, c, w, Y in ROSTER if chi == "R"]
    matches = [(a[3], b[3]) for a in Ls for b in Rs if a[:3] == b[:3]]
    chk("H-D1 exhaustive check finds no (SU3, SU2, Y) match", not matches,
        f"{len(Ls)} LH x {len(Rs)} RH = {len(Ls)*len(Rs)} pairs, "
        f"{len(matches)} matching")
    print("       -> every LH field is an SU(2) DOUBLET and every RH field a SINGLET,")
    print("          so the weak rep alone already forbids a match. This is an")
    print("          OBSTRUCTION, not a shortage of candidates.")

    # ---- H-E: the anti-control ---------------------------------------------
    print("\n  H-E  ANTI-CONTROL: does the check actually detect a Dirac cone?")
    fake = ROSTER + [("X_L  hypothetical", "L", 1, 1, F(-1))]   # pairs with e_R
    Ls2 = [(c, w, Y) for nm, chi, c, w, Y in fake if chi == "L"]
    Rs2 = [(c, w, Y) for nm, chi, c, w, Y in fake if chi == "R"]
    m2 = [(a, b) for a in Ls2 for b in Rs2 if a == b]
    chk("H-E1 adding a vector-like partner for e_R IS detected", len(m2) == 1,
        f"found {len(m2)} match — so H-D is a real test, not a tautology")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE THIRD HORN'S TWO LEGS BOTH HOLD")
    print("=" * 78)
    print("""
  LEG (i): sum(Y^2) = 10 over the three-generation roster, exactly, and it is
  INDEPENDENTLY VALIDATED — feeding it through the Standard Model's own one-loop
  hypercharge beta coefficient, (2/3) sum_f Y^2 + (1/3) sum_scalar Y^2, returns
  41/6 exactly. That is a number the Standard Model fixes without reference to this
  model, so the 10 is checked rather than asserted. The broken-phase sum(Q^2) = 16
  is a genuinely different number, so which phase the shell sits in matters.

  LEG (ii): no left-handed field shares a gauge representation with any
  right-handed one — verified exhaustively over all 2 x 3 = 6 LH/RH pairings. The
  weak representation alone forbids it: every LH field is an SU(2) doublet, every
  RH field a singlet. So there is no Dirac cone anywhere in the roster for a chiral
  chemical potential to sit on. The anti-control confirms the test bites: adding one
  hypothetical vector-like partner for e_R is detected immediately.

  WHAT THIS SETTLES FOR THE DOCKET. The third horn is not a gap in the search — it
  is an obstruction, and "undetermined by construction" is the right grade. mu_5 =
  29.85 eV is derived and has nothing to act on at the shell scale, and no further
  work inside this construction can produce the number it asks to be compared
  against. The docket's own framing — "a question that dissolves is not the same as
  one that is answered" — is verified rather than trusted.

  WHAT IS NOT TOUCHED: whether the shell really sits at 5.4e17 GeV (that is
  section 6c's, not this), and section 6f's separate question about alpha's value
  eighteen orders from its defining scale.
""")


if __name__ == "__main__":
    main()
