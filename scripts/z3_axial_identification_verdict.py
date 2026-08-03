"""z3_axial_identification_verdict — the Z3-as-axial-charge candidate, killed by the corpus's own symmetry requirement (2026-07-28).

THE CANDIDATE (raised earlier the same day, scripts/mu5_selectivity_from_z3.py)
  #146's residue needs a species-selective chiral chemical potential on
  exactly one node pair, with the rest of the roster at mu5 = 0.  The
  Koide sector's Z3 grading assigns charges 0, +1, -1 to the three family
  modes, which matches that demand exactly and evades the count objection
  (graded charges sum to zero, so they cannot shift a species count).
  The identification was recorded at CANDIDATE grade with one condition
  named and one kill condition stated:

      "The single remaining identification is whether the Z3 family
       charge is the axial charge."
      "KILL: if the Z3 charge is shown to commute with chirality —
       grading families rather than handedness — the identification
       fails and the residue stands as recorded."

THE KILL FIRES, and it fires on a requirement the corpus imposes itself.

  1. The corpus requires the Z3 to be a GENUINE symmetry of the medium,
     not a relabelling.  basement_build_program.md: "only a real symmetry
     makes the three Fermi points one cone-sharing orbit", and the
     sector's single demand is "deliver a genuine Z3-symmetric protected
     node on three Fermi points".

  2. A cyclic Z3 permuting three Fermi points is orientation-preserving.
     Symmetry-related nodes in one orbit therefore carry the SAME
     topological (Berry monopole) charge: call it q.

  3. Nielsen-Ninomiya: the total topological charge over a compact
     momentum space vanishes.  Three nodes in one orbit give 3q = 0,
     hence q = 0.

  **The three Fermi points are topologically neutral.  There is no
  chirality on them for a Z3 charge to be.**  The Z3 grades the family
  index; chirality lives on the Dirac index; the two act on different
  labels and commute.  That is verbatim the recorded kill condition.

WHY THIS IS NOT A DISPROOF OF THE MECHANISM, ONLY OF THE IDENTIFICATION
  #146 still needs a species-selective mu5, and the structural match
  found earlier is still a real match — one mode at zero, two equal and
  opposite, neutrality identical, count objection evaded.  What dies is
  the claim that the corpus ALREADY SUPPLIES the selector through the Z3.
  It does not, and it cannot, because the same symmetry that makes the
  three seats one orbit is what forces their topological charge to zero.

  Note the shape of the obstruction, which is the useful part: the Z3
  cannot be both the thing that makes the family a single orbit AND the
  thing that distinguishes one node pair from the rest.  A symmetry that
  relates all three cannot select two of them.  Any surviving selector
  must break the Z3, and the Koide sector needs the Z3 exact.

THIS RUN
  states the argument as arithmetic and checks the two counting steps
  that carry it.
"""
from __future__ import annotations

Z3_CHARGES = (0, +1, -1)


def main() -> None:
    print("=" * 78)
    print("Is the Z3 family charge the axial charge? — the kill condition")
    print("=" * 78)

    print("\n(1) THE STRUCTURAL MATCH THAT RAISED THE CANDIDATE (unchanged):")
    print(f"      Z3 charges on the 3-cycle : {Z3_CHARGES}")
    print(f"      sum                       : {sum(Z3_CHARGES)}  -> neutrality identical")
    print(f"      modes at zero             : {sum(1 for q in Z3_CHARGES if q == 0)}")
    print(f"      modes equal and opposite  : {sum(1 for q in Z3_CHARGES if q != 0)}")
    print("      This is still exactly the configuration section 6c asks for.")

    print("\n(2) THE COUNTING STEP THAT KILLS IT:")
    print("      The corpus requires the Z3 to be a REAL symmetry making the")
    print("      three Fermi points ONE ORBIT (basement part 4). A cyclic")
    print("      permutation is orientation-preserving, so all three nodes")
    print("      carry the same Berry monopole charge q.")
    n_nodes = 3
    print(f"      Nielsen-Ninomiya: total charge over compact momentum space = 0")
    print(f"        {n_nodes} nodes x q = 0   ->   q = 0")
    print("      The three Fermi points are topologically NEUTRAL.")

    print("\n(3) THEREFORE:")
    print("      There is no chirality residing on the family seats for a Z3")
    print("      charge to be identified with. The Z3 grades the FAMILY index;")
    print("      chirality lives on the DIRAC index; they act on different")
    print("      labels and commute. That is the recorded kill condition,")
    print("      word for word.")

    print("\nVERDICT:")
    print("   THE IDENTIFICATION IS DEAD. The Z3 family charge is not the")
    print("   axial charge, and the corpus does not already supply #146's")
    print("   selector. The kill was pre-committed and it fired on the")
    print("   corpus's own requirement that the Z3 be a genuine symmetry.")
    print()
    print("   The obstruction generalises, and that is the part worth")
    print("   keeping: a symmetry that makes all three seats one orbit")
    print("   cannot also single out two of them. Any selector for the node")
    print("   pair must BREAK the Z3 — and the Koide sector needs the Z3")
    print("   exact, since it is what makes the three modes share one cone.")
    print("   So #146's selector and the Koide node's symmetry are in")
    print("   tension, and a candidate that supplies one must be checked")
    print("   against the other.")
    print("=" * 78)


if __name__ == "__main__":
    main()
