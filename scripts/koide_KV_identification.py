"""The K ~ R^2, V ~ M^2 identification: what the democratic graph supplies, and what it does not.

THE DEBT, as both files state it:
  PRTOE_koide_relation.md: "What is owed, and it is one thing: the identification K ~ R^2, V ~ M^2 --
  that the sqrt(m) spectrum's fluctuation IS the family field's kinetic energy and its background IS
  the potential -- is a property of the family-field potential, and that potential is not built."
  T6: "What remains owed is now ONE identification, not a mechanism-shaped hole ... Item 1 stays
  OPEN; it is one notch from closed, not several."

WHY IT MATTERS: under that identification the null becomes an equation of state. With K ~ R^2 and
V ~ M^2 the field's w = (K - V)/(K + V) is fixed by A = R/M alone, and the corpus's recorded
one-parameter compression (Q = 1 - w, A^2 = (1-w)/w) follows. So A = sqrt2 and w = 1/3 are the same
statement, and whichever is derived hands the other over.

WHAT THIS ASKS: the identification names two energies -- a background one and a fluctuation one --
and asserts which is which. The democratic construction has exactly two energy terms. Do they line
up, and does that amount to supplying the identification or merely to restating it?

Run: python3 scripts/koide_KV_identification.py
"""
import math

print("=" * 78)
print("(1) THE IDENTIFICATION MAKES A = sqrt2 AND w = 1/3 ONE STATEMENT")
print("=" * 78)
print("  With K ~ R^2 and V ~ M^2 (raw amplitudes), w = (K - V)/(K + V) = (A^2 - 1)/(A^2 + 1).")
print()
print(f"  {'A':>10} {'A^2':>8} {'w':>12} {'Q = 1 - w':>12} {'A^2 vs (1-w)/w':>16}")
print("  " + "-" * 62)
for A in (1.0, 1.2, math.sqrt(2), 1.5, 2.0):
    w = (A*A - 1) / (A*A + 1)
    chk = (1 - w) / w if w else float("inf")
    print(f"  {A:10.6f} {A*A:8.4f} {w:12.8f} {1-w:12.8f} {chk:16.8f}")
print()
w0 = (2 - 1) / (2 + 1)
print(f"  At A = sqrt2 exactly:  w = {w0:.12f} = 1/3,  Q = 1 - w = {1-w0:.12f} = 2/3")
print(f"  and the recorded compression A^2 = (1-w)/w returns {(1-w0)/w0:.12f} = 2.")
print()
print("  So the identification is a two-way bridge: derive A = sqrt2 and w = 1/3 follows;")
print("  derive w = 1/3 and A = sqrt2 follows. The corpus has recorded this; it is restated")
print("  here only to fix what the debt is actually buying.")

print()
print("=" * 78)
print("(2) THE GRAPH HAS EXACTLY TWO ENERGY TERMS, AND THEY ARE OF THE TWO NAMED KINDS")
print("=" * 78)
print("  The democratic construction's energy is")
print()
print("      H = (g/2) [ sum_{i<j} (f_i - f_j)^2   +   sum_i (f_i - 0)^2 ]")
print("                   ^^^^^^^^^^^^^^^^^^^^         ^^^^^^^^^^^^^^^^^")
print("                   generations differ           displacement from")
print("                   from EACH OTHER              the CONDENSATE")
print()
print("  Those are not two arbitrary terms. One measures internal relative structure; the other")
print("  measures displacement against the background the generations are excitations of. That")
print("  is precisely the kinetic/potential split the identification names -- 'fluctuation' and")
print("  'background' are the graph's two bond types, not labels imposed on one expression.")
print()
print("  And the two terms are diagonal in exactly the two sectors:")
print("    the CONDENSATE bond contributes to BOTH modes (it is a diagonal a on every site);")
print("    the INTER-GENERATION bonds contribute ONLY to the non-uniform modes (lambda_0 = 0).")
_lam = (0.0, 3.0, 3.0)
for q, nm in ((0, "uniform (M)"), (1, "shape (R)")):
    print(f"      {nm:<14} eps_q = a + b*lambda_{q} = a + {_lam[q]:.0f}b"
          f"   -> at a = b:  {1 + _lam[q]:.0f} a")
print()
print("  So the uniform mode is held ONLY by the condensate bond, and the shape modes are held")
print("  by the condensate bond plus three times the inter-generation bond. The split is clean")
print("  in one direction and not in the other, and that asymmetry is the whole content below.")

print()
print("=" * 78)
print("(3) WHERE IT FALLS SHORT — AND THE SHORTFALL IS EXACT")
print("=" * 78)
print("  If the identification were simply 'condensate bond = V, inter-generation bonds = K',")
print("  then at a = b the two energies at the null (M_c = R_c, i.e. equal canonical amplitudes)")
print("  would stand in the ratio:")
print()
a = 1.0
Mc2 = Rc2 = 1.0                              # the null, in canonical amplitudes
E_uniform = 0.5 * (a + 0*a) * Mc2            # eps_0 = a
E_shape = 0.5 * (a + 3*a) * Rc2              # eps_1 = a + 3b = 4a
print(f"    E(uniform sector) = (1/2) eps_0 M_c^2 = {E_uniform:.6f}   (eps_0 = a)")
print(f"    E(shape sector)   = (1/2) eps_1 R_c^2 = {E_shape:.6f}   (eps_1 = 4a)")
print(f"    ratio K/V would be {E_shape/E_uniform:.6f}")
w_bad = (E_shape/E_uniform - 1) / (E_shape/E_uniform + 1)
print(f"    -> w = {w_bad:.6f}, not 1/3")
print()
print("  So the sector ENERGIES do not give w = 1/3. What does is the identification as the")
print("  corpus actually writes it -- on the raw AMPLITUDES, K ~ R^2 and V ~ M^2, not on the")
print("  sector energies. In raw amplitudes the null is R^2 = 2 M^2 and w = 1/3 immediately:")
R2, M2 = 2.0, 1.0
print(f"    R^2/M^2 = {R2/M2:.4f}  ->  w = (R^2 - M^2)/(R^2 + M^2) = {(R2-M2)/(R2+M2):.12f}")
print()
print("  The distinction is not pedantic. An energy carries its stiffness; an amplitude does")
print("  not. The identification asserts that the field's kinetic and potential energies are")
print("  proportional to R^2 and M^2 WITH THE SAME COEFFICIENT -- and the graph says the two")
print("  sectors have stiffnesses differing by exactly 4. Those cannot both be true unless the")
print("  cosmological K and V are read off the amplitudes before the ring's stiffnesses are")
print("  applied, i.e. at the moment the amplitudes are set rather than in the settled ring.")

print()
print("=" * 78)
print("VERDICT — THE DEBT IS SHARPENED, NOT PAID")
print("=" * 78)
print("  WHAT THE GRAPH SUPPLIES: the two objects the identification names. Before this, 'the")
print("  background' and 'the fluctuation' were two aspects of one unbuilt potential; the")
print("  construction exhibits them as two BOND TYPES -- displacement against the condensate,")
print("  and generations differing from each other -- with the uniform mode held by the first")
print("  alone. The identification is no longer between a spectrum and an unbuilt Lagrangian;")
print("  it is between a spectrum and two terms that exist.")
print()
print("  WHAT IT DOES NOT SUPPLY: the equal-coefficient clause. K ~ R^2 and V ~ M^2 with a")
print("  COMMON constant is what delivers w = 1/3, and the graph's two sectors carry stiffnesses")
print(f"  in the ratio {E_shape/E_uniform:.0f}. Reading K and V off the amplitudes rather than the")
print("  energies is therefore a real additional claim, and it is a claim about WHEN the")
print("  equation of state is read -- at the pour, when amplitudes are set, or later in the")
print("  settled ring.")
print()
print("  THAT IS THE SAME FORK AS EVERYTHING ELSE IN THIS ARC. The assembly-order question")
print("  (task #1) asks when the stiffnesses split relative to when the energy arrives. This")
print("  asks when the equation of state is read relative to the same split. **One ordering")
print("  answers both**, which is worth more than either answer alone: pour while degenerate,")
print("  read w there, then split -- and at degeneracy the stiffnesses are equal, so the")
print("  equal-coefficient clause the identification needs holds exactly, for the same reason")
print("  every delivery law agreed there.")
print()
print("  That last sentence is a candidate, not a result. It is written down because it is")
print("  checkable and because it would close the identification if it survives.")
