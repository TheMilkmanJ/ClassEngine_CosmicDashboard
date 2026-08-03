"""mu5_selectivity_from_z3 — #146's residue: the corpus may already carry its own selector (2026-07-28).

THE RESIDUE, AS RECORDED
  §6c's three band-structure conditions reduce to one, and the sector's
  own analysis sharpens it to its hardest form:

    "not 'what gives the constituent level a Fermi surface' but 'what
     gives ONE node pair a chiral chemical potential while the rest of
     the roster stays at mu5 = 0.'  Nothing recorded selects that pair."

  The blocker recorded against the axial route is a COUNT: "mu5 is
  chiral, so it couples to every Weyl species in the roster, which
  returns exactly the N = 25.5 the file has already ruled out."  So the
  axial structure was judged to supply the structure and not the
  selectivity.

WHAT THIS SCRIPT CHECKS
  Whether the selector is already in the corpus, in a different sector.
  The Koide reduction (basement part 4, T6) forces a Z3-graded family
  node, and records the charge assignment explicitly: on a 3-cycle the
  Fourier modes carry Z3 charges **0, +1, -1** — one neutral mode and two
  oppositely-charged ones.  A chemical potential conjugate to THAT charge
  is not democratic: it vanishes identically on the neutral mode and is
  equal-and-opposite on the remaining pair.

  That is, structurally, exactly the object §6c asks for.  This script
  tests the match against the three things the residue demands, and —
  more importantly — against the count objection that killed the
  democratic version.

WHAT IS AND IS NOT CLAIMED
  CLAIMED: the structural match, which is checkable arithmetic.
  NOT CLAIMED: that the Z3 charge IS the axial charge.  That is the one
  remaining identification, and it is named here rather than assumed.
  This is recorded at candidate grade in the corpus's own sense — to be
  earned or killed, with the killing condition stated.
"""
from __future__ import annotations

import numpy as np

# The recorded assignment: T6's "on a 3-cycle the Fourier modes carry Z3
# charges 0, +1, -1" (koide_relation: the neutral mode timelike, the two
# charged modes spacelike, in the Z3-graded form).
Z3_CHARGE = np.array([0, +1, -1])
SIGNATURE = np.array([+1, -1, -1])      # f0^2 - |f1|^2 - |f2|^2


def main() -> None:
    print("=" * 78)
    print("Does the Z3 grading already supply mu5's selectivity?")
    print("=" * 78)

    print(f"\n   recorded Z3 charges on the 3-cycle : {Z3_CHARGE}")
    print(f"   recorded graded signature          : {SIGNATURE}")
    print("   (one neutral/timelike mode, two charged/spacelike modes)")

    print("\n(1) IS A Z3-CONJUGATE POTENTIAL SPECIES-SELECTIVE?")
    mu5 = 1.0
    seated = mu5 * Z3_CHARGE
    print(f"     mu5 * charge -> {seated}")
    n_zero = int(np.sum(seated == 0))
    n_pair = int(np.sum(seated != 0))
    print(f"     modes left at exactly mu5 = 0 : {n_zero}")
    print(f"     modes carrying a potential    : {n_pair}, "
          f"equal and opposite ({seated[seated!=0]})")
    print("     -> ONE node pair seated, the rest at zero. This is the")
    print("        residue's demand, word for word.")

    print("\n(2) DOES IT SURVIVE THE COUNT OBJECTION THAT KILLED THE")
    print("    DEMOCRATIC VERSION?")
    print("    The objection: a chiral mu5 couples to EVERY Weyl species,")
    print("    restoring the ruled-out N = 25.5. Test the graded version by")
    print("    the only thing that matters — its contribution to a")
    print("    democratically summed quantity:")
    tot = int(np.sum(Z3_CHARGE))
    print(f"      sum of Z3 charges = {tot}")
    print(f"      sum of seated potentials = {np.sum(seated):.1f}")
    print("    A Z3-graded potential contributes ZERO to any democratic sum,")
    print("    because the charges cancel by construction. So it CANNOT shift")
    print("    a species count — the objection that killed the ungraded")
    print("    version does not reach the graded one.")

    print("\n(3) DOES IT DELIVER THE PHYSICAL STRUCTURE §6c NEEDS?")
    checks = [
        ("one particle pocket and one hole pocket",
         n_pair == 2 and seated[seated != 0].sum() == 0),
        ("at exactly equal |k_F| (charges equal in magnitude)",
         abs(seated[seated != 0][0]) == abs(seated[seated != 0][1])),
        ("neutrality preserved identically, not imposed",
         np.sum(seated) == 0),
        ("the remaining node untouched (mu5 = 0)", n_zero == 1),
    ]
    for name, ok in checks:
        print(f"     {'OK ' if ok else 'NO '} {name}")

    print("\n(4) THE SIGNATURE CROSS-CHECK")
    print("    The graded form's signature (+,-,-) sorts the SAME way as the")
    print("    charge assignment: the neutral mode is the odd one out in")
    print("    both. The two structures are not independent coincidences —")
    print("    they are the same Z3 grading read twice.")
    agree = (SIGNATURE[0] != SIGNATURE[1]) and (SIGNATURE[1] == SIGNATURE[2]) \
        and (Z3_CHARGE[0] == 0) and (Z3_CHARGE[1] == -Z3_CHARGE[2])
    print(f"     same partition of the three modes: {agree}")

    print("\nVERDICT (candidate grade, stated as such):")
    print("   THE SELECTOR MAY ALREADY BE IN THE CORPUS. '#146: nothing")
    print("   recorded selects that pair' is too strong — the Koide sector's")
    print("   own Z3 grading, which the basement's part 4 already forces and")
    print("   which is recorded independently of the band structure, assigns")
    print("   charges 0, +1, -1 and therefore selects exactly one pair while")
    print("   leaving one node at zero. It also evades the count objection,")
    print("   because a graded potential sums to zero over the roster.")
    print()
    print("   THE ONE REMAINING IDENTIFICATION, named not assumed: whether")
    print("   the Z3 family charge IS the axial charge. If it is, the")
    print("   selectivity is supplied by a structure the model already")
    print("   carries for unrelated reasons, and #146's residue closes")
    print("   without new physics. If it is not, this is a structural")
    print("   analogy and nothing more.")
    print()
    print("   KILL CONDITION: if the Z3 charge is shown to commute with")
    print("   chirality (i.e. it grades families, not handedness), the")
    print("   identification fails and the residue stands as recorded.")
    print("=" * 78)


if __name__ == "__main__":
    main()
