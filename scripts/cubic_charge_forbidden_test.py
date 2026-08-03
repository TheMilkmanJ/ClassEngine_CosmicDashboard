"""Does electric charge forbid the Z3 cubic, and does that deliver A = sqrt2?

The null's sharpest form (T6): A = sqrt2 <=> R_c = M_c, the canonically normalized singlet
amplitude equal to the doublet's -- equivalently the field vector at 45 degrees to the democratic
direction. The corpus's standing fence says a natural Z3 cubic V ⊃ -g sum(phi^3) drives A -> 2,
not sqrt2, and instructs that such cubics not be cited as the landing mechanism.

THE IDEA under the charge-coupled/vanishing filter: sum(phi^3) carries three units of whatever
charge phi carries. If the family-field components are electrically charged, the term is forbidden
by U(1)_EM outright -- 3q = 0 has no solution for q = -1. The fence would then not apply to the
charged sector at all, and would apply to the neutral one, which is where A is observed to differ.

Three things to check, and the third is the kill.

Run: python3 scripts/cubic_charge_forbidden_test.py
"""
import math

DM21, DM31, M1 = 7.53e-5, 2.53e-3, 2.25e-3


def Q_nu(m1):
    m2, m3 = math.sqrt(m1*m1 + DM21), math.sqrt(m1*m1 + DM31)
    return (m1 + m2 + m3) / (math.sqrt(m1) + math.sqrt(m2) + math.sqrt(m3))**2


print("=" * 76)
print("(1) THE SELECTION RULE ON THE CUBIC")
print("=" * 76)
print("  sum(phi_i^3) carries 3q, where q is the charge of a family-field component.")
print(f"  {'q':>8}  {'3q':>8}  {'allowed by U(1)?':>18}")
print("  " + "-" * 42)
for lbl, q in (("charged lepton", -1.0), ("neutrino", 0.0), ("Z3 charge only", 1/3)):
    print(f"  {q:8.4f}  {3*q:8.4f}  {'YES' if abs(3*q) < 1e-12 else 'FORBIDDEN':>18}   ({lbl})")
print()
print("  So the cubic is forbidden outright for an electrically charged family field, and")
print("  allowed for a neutral one. That is a genuine selection rule, it is charge-coupled,")
print("  and it removes the corpus's own fence from the charged sector -- the fence was")
print("  derived for a term the charged sector cannot have.")

print()
print("=" * 76)
print("(2) BUT THE QUARTIC ALONE DOES NOT FIX THE RATIO")
print("=" * 76)
print("  With the cubic gone the natural potential is V = (lam/4)(sum phi^2 - v^2)^2, and in")
print("  canonical coordinates sum phi^2 = M_c^2 + R_c^2. Its minimum is the whole SPHERE")
print("  M_c^2 + R_c^2 = v^2 -- a flat direction, not a point.")
print()
print("  R_c = M_c is one point on that circle and nothing in the quartic prefers it. So")
print("  forbidding the cubic removes the wrong attractor without supplying the right one:")
print("  A becomes undetermined rather than sqrt2.")

print()
print("=" * 76)
print("(3) THE KILL — THE NEUTRINO SIDE IS WRONG")
print("=" * 76)
q_nu = Q_nu(M1)
A_nu = math.sqrt(6*q_nu - 2)
print("  The story predicts: charged sector has no cubic (A free of the A->2 pull), the")
print("  neutral sector has one (A driven to the cubic's minimum, A = 2).")
print()
print(f"    cubic minimum, recorded          A = 2")
print(f"    observed neutrino ring           A = sqrt(6 Q_nu - 2) = {A_nu:.4f}   (Q_nu = {q_nu:.4f})")
print(f"    miss                             {abs(A_nu/2 - 1)*100:.1f}%")
print()
print("  The neutrino triple is not at the cubic's minimum, so the neutral sector is not")
print("  behaving as the story requires. The prediction the mechanism makes on the side")
print("  where it is testable is wrong by a factor 2.3, and that is decisive.")

print()
print("=" * 76)
print("WHAT SURVIVES")
print("=" * 76)
print("  One piece, and it is worth keeping: the recorded fence -- 'a natural Z3 cubic drives")
print("  A -> 2, do not cite Z3-invariant cubics as the landing mechanism' -- was derived")
print("  without asking whether the charged sector may carry that term at all. It may not:")
print("  3q = 0 fails for q = -1. The fence stands for a neutral family field and does not")
print("  bind a charged one.")
print()
print("  That does not derive sqrt2. It removes one recorded obstacle from the charged")
print("  sector's path and leaves the flat direction unresolved, which is where the blank")
print("  now sits: what picks R_c = M_c on the quartic's circle.")
