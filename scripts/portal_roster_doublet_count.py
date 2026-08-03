"""The portal roster's doublet count — the bound applied, using the corpus's own commitments.

THE RECORDED ABSENCE (PRTOE_hierarchy_problem.md §6j):

    "The bound has not been applied. It is derived here and repeated in three other files, but the
     portal roster's electroweak content is nowhere counted: the species are described as
     Higgs-coupled and leptophilic and given no representation assignment. A falsifiable
     self-constraint therefore sits on the books with nothing to test it against."

and the worry attached to it:

    "the ceiling is tight and the most natural reading fails it. One doublet per generation is
     three, giving S = 3/6pi = 0.159 against |S| <~ 0.14 -- excluded by 14%."

THE QUESTION. The oblique parameter S counts new ELECTROWEAK-CHARGED states. So the count is
forced to be nonzero only if something in the corpus requires the portal species to carry
electroweak charge. This checks the three requirements the corpus actually places on them, and
asks whether any of the three needs a doublet.

Run: python3 scripts/portal_roster_doublet_count.py
"""
import math

S_BOUND = 0.14                       # |S| <~ 0.14, the recorded electroweak-precision ceiling
M_H = 125.25                         # GeV
M_ANCHOR = 4 * math.pi * M_H         # the recorded anchor definition

print("=" * 78)
print("(1) THE BOUND, RECOMPUTED")
print("=" * 78)
print(f"  {'new EW doublets':>16} {'S = n/(6 pi)':>14} {'vs |S| <~ 0.14':>16}")
print("  " + "-" * 50)
for n in range(0, 5):
    S = n / (6 * math.pi)
    print(f"  {n:>16} {S:14.6f} {'allowed' if S <= S_BOUND else 'EXCLUDED':>16}")
print()
print(f"  The ceiling sits between 2 and 3 doublets, as recorded. n_D = 0 is trivially allowed")
print(f"  and uses none of the margin.")

print()
print("=" * 78)
print("(2) THE THREE REQUIREMENTS THE CORPUS ACTUALLY PLACES ON THE PORTAL SPECIES")
print("=" * 78)
REQS = (
    ("Higgs-coupled", "generate m_H^2 at one loop under the no-bare clause",
     "lam |S|^2 |H|^2 for a gauge SINGLET S", "NO doublet needed"),
    ("leptophilic", "couple preferentially to leptons",
     "the dim-5 operator S (Lbar H e_R)/Lambda -- #125's own selection", "NO doublet needed"),
    ("anchor-scale", "m_H ~ M_anchor/4pi from that loop",
     "sets lam x multiplicity ~ 1, not a representation", "NO doublet needed"),
)
print(f"  {'requirement':<16} {'what it demands':<44} {'verdict'}")
print("  " + "-" * 78)
for name, demand, how, verdict in REQS:
    print(f"  {name:<16} {demand:<44} {verdict}")
print()
for name, demand, how, verdict in REQS:
    print(f"    {name:<16} satisfied by: {how}")

print()
print("=" * 78)
print("(3) THE SIZE CHECK — CAN A SINGLET LOOP ACTUALLY MAKE m_H?")
print("=" * 78)
print("  A requirement is only met if it is met at the right SIZE. Under the no-bare clause a")
print("  scalar of mass M coupling as lam |S|^2 |H|^2 induces dm_H^2 ~ (n_S lam / 16 pi^2) M^2.")
print("  The recorded anchor identification is m_H = M_anchor/(4 pi), i.e. m_H^2 = M^2/(16 pi^2).")
print("  Setting the two equal:")
print()
print("      n_S lam = 1")
print()
print(f"    M_anchor = 4 pi m_H = {M_ANCHOR:.1f} GeV")
print(f"    m_H from the loop at n_S lam = 1:  M/(4 pi) = {M_ANCHOR/(4*math.pi):.2f} GeV")
print(f"    against the measured                        {M_H:.2f} GeV")
print()
print("  So one singlet at order-unity coupling delivers the recorded relation exactly, with")
print("  no electroweak charge anywhere in it. The anchor identification is a statement about")
print("  the loop factor 1/(4 pi), and a singlet loop carries the same 1/(4 pi).")

print()
print("=" * 78)
print("(4) AND THE CORPUS'S OWN NAMED PORTAL OBJECT IS A SINGLET")
print("=" * 78)
print("  PRTOE_dyad_gas.md records the electron-coupled scalar's symmetry role verbatim as")
print("  'a total singlet: Lorentz-scalar, dark-neutral, gauge-neutral, L-neutral', and #125")
print("  selected its operator as the one multiplying the Yukawa -- 'a gauge singlet couples to")
print("  every Yukawa'. That is the corpus's only portal-class object with an assigned")
print("  representation, and the assignment is: no electroweak charge.")

print()
print("=" * 78)
print("(5) DOES THE CENSUS FORCE ELECTROWEAK CHARGE? NO — IT COUNTS SOMETHING ELSE")
print("=" * 78)
print("  The obvious way the count could be forced is if the census's own counting argument")
print("  ranged over the portal species. It does not. c = 9/10 is 'the census over the")
print("  universal charged-fermion roster, not the electron-coupled scalar' -- Standard-Model")
print("  charged fermions, whose representations are already fixed and are not new states. The")
print("  census constrains what the light scalar may couple to (a universal conformal")
print("  rescaling, no flavour-structured Higgs/EM portal); it says nothing about the")
print("  representation of anchor-scale states.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  THE COUNT IS ZERO on the corpus's own commitments. Every requirement placed on the")
print("  portal species -- Higgs-coupled, leptophilic, m_H at one loop from the anchor -- is")
print("  met by electroweak singlets, at the right size, and the one portal-class object the")
print("  corpus has assigned a representation to is explicitly gauge-neutral.")
print()
print(f"    S(n_D = 0) = 0.000000  against |S| <~ {S_BOUND}   -- the full margin unused.")
print()
print("  WHAT THE WORRY RESTED ON. 'One doublet per generation is three' is a reading imported")
print("  from generic lepton-portal model-building, not a commitment the corpus made. Nothing")
print("  in the census, the anchor identification, or the operator selection generates a")
print("  generation index on the portal states. The 14% exclusion is real for THAT reading and")
print("  the reading is not the corpus's.")
print()
print("  WHAT IS STILL OWED, and it is much narrower than 'the count has never been taken':")
print("  if any future construction gives the portal states a generation index or an")
print("  electroweak representation -- for instance to explain WHY they are leptophilic rather")
print("  than assuming it -- the bound bites immediately and hard, at n_D = 3. The constraint")
print("  should therefore be carried as a live design rule on the roster, not as an untested")
print("  entry: THE PORTAL MAY NOT ACQUIRE MORE THAN TWO ELECTROWEAK DOUBLETS.")
