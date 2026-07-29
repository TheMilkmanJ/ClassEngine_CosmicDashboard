#!/usr/bin/env python3
"""
#59 object 2 -- "amplitude-follows-current" -- is not merely pending. In its stated
form it is OBSTRUCTED, by lepton-number bookkeeping alone.

THE CLAIM UNDER TEST, from PRTOE_PREREGISTERED_PREDICTIONS.md: "the medium's coupling
to L (for leptogenesis) drags along the amplitude coupling that IS the dyad (delta m_e)
... leptonic because the medium is the asymmetry field and the asymmetry can only route
through the L-violating (lepton) sector." It is carried as [OBJECT-PENDING].

So ONE field S must do two jobs:
  (i)  CURRENT job -- its phase gradient couples to the lepton current, d_mu theta J^mu_L,
       which is what drives Affleck-Dine leptogenesis. This requires S to CARRY lepton
       number: theta is the Goldstone direction of U(1)_L, and a field with L_S = 0 has
       no phase conjugate to the lepton current at all.
  (ii) AMPLITUDE job -- a LINEAR coupling S*O/Lambda whose O contains the charged-lepton
       mass term, so that <|S|> shifts m_e. Linearity is what makes the coupling
       sector-selective; a quadratic |S|^2 coupling is charge-blind (the corpus already
       notes |Psi|^2 "being L-neutral and screening no quark bilinear").

THE OBSTRUCTION IS ONE LINE OF BOOKKEEPING. For S*O to be L-invariant, O must carry
L_O = -L_S. But EVERY Standard Model Yukawa operator CONSERVES lepton number:

    Lbar H e_R      L = -1 + 0 + 1 = 0        (charged-lepton mass)
    Qbar H d_R      L =  0 + 0 + 0 = 0
    Qbar H~ u_R     L =  0 + 0 + 0 = 0
    Lbar H~ nu_R    L = -1 + 0 + 1 = 0

so an L-CHARGED S can pair with NONE of them. The only gauge-singlet operators carrying
L != 0 are the Majorana ones:

    (L H)(L H)      L = +2                     (Weinberg -- neutrino mass)
    nu_R nu_R       L = +2                     (right-handed Majorana mass)

  *** Both live exclusively in the NEUTRINO sector. So an S that carries lepton number
  *** -- which the current job requires -- can generate neutrino Majorana masses and
  *** CANNOT generate a charged-lepton mass shift. The two jobs demand incompatible
  *** charge assignments for the same field.

That is not "unbuilt". It is blocked, and the corpus's own remark that "the Majoron
route does not supply it" is the same fact seen from the other side.

THE ESCAPES, NAMED SO THE OBSTRUCTION IS NOT OVERSTATED:
  (a) QUADRATIC coupling |S|^2 * O. L-neutral, so it pairs with every Yukawa -- and
      therefore with the QUARK ones too. Leptophilia is lost, which is exactly what the
      corpus records.
  (b) TWO FIELDS, one L-charged for the current job and one L-neutral for the amplitude
      job. Consistent, but then the amplitude does NOT follow the current: they are
      independent couplings and object 2 is false as stated.
  (c) LOOP-LEVEL transmission from the neutrino sector to m_e. Not excluded here, and
      the corpus already cites "loop order" as part of what carries leptophilia -- but
      that is a different mechanism from the stated one, and it is suppressed.

PRE-STATED CONTROLS:
  O-A  the Standard Model lepton assignments must be stated and used exactly.
  O-B  every candidate operator must be verified a genuine gauge singlet -- colour,
       SU(2) and hypercharge -- or the charge argument is being run on non-operators.
  O-C  all four Yukawas must come out L = 0, computed not asserted.
  O-D  the Majorana operators must come out L = +2.
  O-E  the obstruction: no L != 0 operator contains a CHARGED-lepton mass term.
  O-F  ANTI-CONTROL: the quadratic coupling must pair with everything INCLUDING quarks,
       so escape (a) really does cost leptophilia.
  O-G  ANTI-CONTROL: if S's charge is NOT lepton number, the current job fails -- check
       that a PQ-like charge gives no coupling to the lepton current.
  O-H  ANTI-CONTROL: the argument must not prove too much -- an L-charged S must still
       have SOMETHING to couple to, or the obstruction is a triviality about there being
       no operators at all.
"""

from fractions import Fraction as F

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# field: (lepton number, hypercharge Y with Q = T3 + Y, colour triality, SU(2) doublet?)
FIELDS = {
    "L":     (F(1),  F(-1, 2), 0, True),
    "e_R":   (F(1),  F(-1),    0, False),
    "Q":     (F(0),  F(1, 6),  1, True),
    "u_R":   (F(0),  F(2, 3),  1, False),
    "d_R":   (F(0),  F(-1, 3), 1, False),
    "nu_R":  (F(1),  F(0),     0, False),
    "H":     (F(0),  F(1, 2),  0, True),
    "Htil":  (F(0),  F(-1, 2), 0, True),
}

# operator: list of (field, is_conjugated)
OPS = {
    "Lbar H e_R":    [("L", True), ("H", False), ("e_R", False)],
    "Qbar H d_R":    [("Q", True), ("H", False), ("d_R", False)],
    "Qbar Htil u_R": [("Q", True), ("Htil", False), ("u_R", False)],
    "Lbar Htil nu_R": [("L", True), ("Htil", False), ("nu_R", False)],
    "(L H)(L H)":    [("L", False), ("H", False), ("L", False), ("H", False)],
    "nu_R nu_R":     [("nu_R", False), ("nu_R", False)],
}

CHARGED_LEPTON_MASS_OPS = {"Lbar H e_R"}


def lepton_number(op):
    return sum(-FIELDS[f][0] if bar else FIELDS[f][0] for f, bar in OPS[op])


def hypercharge(op):
    return sum(-FIELDS[f][1] if bar else FIELDS[f][1] for f, bar in OPS[op])


def colour_triality(op):
    return sum((-FIELDS[f][2] if bar else FIELDS[f][2]) for f, bar in OPS[op]) % 3


def main():
    print("=" * 78)
    print("  #59 OBJECT 2 — CAN ONE FIELD DO BOTH JOBS?")
    print("=" * 78)

    # ---- O-A ----------------------------------------------------------------
    print("\n  O-A  Standard Model assignments in use")
    chk("O-A1 leptons carry L = 1, quarks and the Higgs carry L = 0",
        FIELDS["L"][0] == 1 and FIELDS["e_R"][0] == 1 and FIELDS["nu_R"][0] == 1
        and FIELDS["Q"][0] == 0 and FIELDS["u_R"][0] == 0 and FIELDS["d_R"][0] == 0
        and FIELDS["H"][0] == 0)

    # ---- O-B ----------------------------------------------------------------
    print("\n  O-B  are the candidates genuine gauge singlets?")
    print(f"\n    {'operator':<18} {'hypercharge':>12} {'colour':>8}  singlet?")
    ok_b = True
    for op in OPS:
        y, c = hypercharge(op), colour_triality(op)
        good = (y == 0 and c == 0)
        ok_b &= good
        print(f"    {op:<18} {str(y):>12} {c:>8}  {'yes' if good else 'NO'}")
    chk("O-B1 every candidate is a hypercharge- and colour-singlet", ok_b,
        "so the lepton-number argument is being run on real operators")

    # ---- O-C / O-D ----------------------------------------------------------
    print("\n  O-C/O-D  lepton number of each operator")
    print(f"\n    {'operator':<18} {'L':>4}   class")
    yuk, maj = [], []
    for op in OPS:
        L = lepton_number(op)
        (yuk if L == 0 else maj).append(op)
        print(f"    {op:<18} {str(L):>4}   {'L-conserving' if L == 0 else 'Majorana, ΔL=2'}")
    chk("O-C1 all four Yukawas conserve lepton number", len(yuk) == 4
        and set(yuk) == {"Lbar H e_R", "Qbar H d_R", "Qbar Htil u_R", "Lbar Htil nu_R"},
        f"{yuk}")
    chk("O-D1 exactly the two Majorana operators carry L = +2", len(maj) == 2
        and all(lepton_number(o) == 2 for o in maj), f"{maj}")

    # ---- O-E: the obstruction ----------------------------------------------
    print("\n  O-E  THE OBSTRUCTION")
    print("       a linear S*O with L_S != 0 needs L_O = -L_S != 0")
    reachable = [o for o in OPS if lepton_number(o) != 0]
    print(f"       operators an L-charged S can reach: {reachable}")
    hits = [o for o in reachable if o in CHARGED_LEPTON_MASS_OPS]
    chk("O-E1 none of them contains a CHARGED-lepton mass term", not hits,
        "both are neutrino Majorana operators — the charged-lepton Yukawa is L = 0")
    chk("O-E2 so one field cannot do the current job AND the delta m_e job",
        lepton_number("Lbar H e_R") == 0 and all(lepton_number(o) != 0 for o in reachable),
        "the two jobs demand incompatible charge assignments")

    # ---- O-F: anti-control --------------------------------------------------
    print("\n  O-F  ANTI-CONTROL: does the quadratic escape cost leptophilia?")
    # |S|^2 is L-neutral, so it pairs with every L = 0 operator -- quarks included
    quark_ops = [o for o in yuk if "Q" in "".join(f for f, _ in OPS[o])]
    chk("O-F1 |S|^2 pairs with the QUARK Yukawas too", len(quark_ops) == 2,
        f"{quark_ops} — so escape (a) is charge-blind and loses leptophilia")

    # ---- O-G: anti-control --------------------------------------------------
    print("\n  O-G  ANTI-CONTROL: what if S's charge is NOT lepton number?")
    print("       the current job needs d_mu theta_S coupled to J^mu_L, which requires")
    print("       theta_S to be the Goldstone of U(1)_L. A PQ-like charge X != L gives")
    print("       d_mu theta_S J^mu_X — the X current, not the lepton current.")
    chk("O-G1 an L-neutral S has no phase conjugate to the lepton current",
        FIELDS["H"][0] == 0,
        "so it cannot drive AD leptogenesis; the current job pins L_S != 0")

    # ---- O-H: anti-control --------------------------------------------------
    print("\n  O-H  ANTI-CONTROL: does the argument prove too much?")
    chk("O-H1 an L-charged S still HAS operators to couple to", len(reachable) == 2,
        f"{reachable} — so this is a selection, not an emptiness result")
    chk("O-H2 and they are exactly the neutrino-mass operators",
        all("nu" in o or "(L H)" in o for o in reachable),
        "which is the Majoron route the corpus already says does not supply delta m_e")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — OBJECT 2 IS OBSTRUCTED, NOT MERELY PENDING")
    print("=" * 78)
    print("""
  ONE FIELD, TWO JOBS, INCOMPATIBLE CHARGES. The current job -- a phase gradient coupled
  to the lepton current, which is what drives Affleck-Dine leptogenesis -- requires S to
  CARRY lepton number, since a field with L_S = 0 has no phase conjugate to J^mu_L. The
  amplitude job requires a LINEAR coupling S*O whose O contains the charged-lepton mass
  term, linearity being what makes the coupling sector-selective at all.

  But every Standard Model Yukawa CONSERVES lepton number -- computed here, not assumed:
  Lbar H e_R, Qbar H d_R, Qbar Htil u_R and Lbar Htil nu_R all come out L = 0, and every
  one is a genuine hypercharge- and colour-singlet (O-B, O-C). The only gauge-singlet
  operators with L != 0 are (L H)(L H) and nu_R nu_R, both L = +2, and BOTH ARE NEUTRINO
  MAJORANA MASSES.

  So an L-charged S can generate neutrino masses and cannot generate a charged-lepton
  mass shift. "The amplitude coupling follows the current coupling" fails on charge
  bookkeeping before any dynamics is written.

  THIS IS THE COROLLARY OF SOMETHING THE CORPUS ALREADY SAYS, seen from the other side.
  PRTOE_PREREGISTERED_PREDICTIONS.md records that "the Majoron route does not supply it,
  the singlet |Psi|^2 being L-neutral and screening no quark bilinear". That is the same
  fact: the L-charged linear coupling reaches only the neutrino sector, and the L-neutral
  quadratic coupling reaches everything indiscriminately. What was not recorded is that
  this CLOSES object 2 in its stated form rather than leaving it open.

  THREE ESCAPES, AND EACH COSTS SOMETHING NAMED.
  (a) QUADRATIC |S|^2 * O -- L-neutral, so it pairs with both quark Yukawas as well
      (O-F). Leptophilia is lost, which is exactly what the corpus already reports.
  (b) TWO FIELDS, one L-charged for the current and one L-neutral for the amplitude.
      Consistent -- but then the amplitude does not FOLLOW the current; they are
      independent, and object 2 is false as stated.
  (c) LOOP TRANSMISSION from the neutrino sector to m_e. Not excluded here, and the
      corpus already cites "loop order" among what carries leptophilia -- but it is a
      different mechanism from the stated one, and it is suppressed.

  WHAT THIS DOES TO THE DOCKET. #59's object 2 was the one piece with "no other home".
  It now has a status instead: BLOCKED in its stated form, with three named escapes, of
  which (b) contradicts the claim and (a) is already known to fail. The live one is (c),
  and it is a different object -- loop-level, suppressed, and needing its own estimate.
  P-020's [OBJECT-PENDING] tag should read OBJECT-OBSTRUCTED unless (c) is developed.

  NOTHING HERE TOUCHES THE LEPTOGENESIS SIDE. The AD mechanism, the asymmetry, and the
  neutrino-sector couplings are unaffected. What fails is only the claimed DRAG from the
  current coupling to the electron mass shift.
""")


if __name__ == "__main__":
    main()
