"""Why the phase is a SEPARATE debt: the democratic graph leaves it exactly flat.

PRTOE_koide_relation.md states the sector's debt as "one number and one relation: why Q = 2/3, and
why the closure 3 arg f_1 = Q holds at all." The democratic-graph mechanism
(koide_democratic_graph_null.py) supplies a candidate for the first -- it makes the Z3-graded norm
f_0^2 - |f_1|^2 - |f_2|^2 vanish, which is the constraint the whole sector hangs from.

The obvious next question is whether it also reaches the phase. It does not, and the reason is
worth having explicitly, because it says the two debts are not the same kind of thing and no
amount of work on stiffnesses will close the second.

THE REASON. The democratic graph's Hessian is (N+1) I - J, whose non-singlet eigenvalue is
(N+1)-fold... at N = 3, TWICE degenerate. Two degenerate modes span a plane, and any rotation in
that plane is a symmetry of the Hamiltonian. The Koide phase phi is exactly an angle in that
plane. So phi is a flat direction: the mechanism cannot fix it, by symmetry, not by omission.

WHAT THIS PREDICTS, WHICH IS NOT NOTHING. Q depends only on |f_1|/f_0 and not on phi, while the
individual masses depend on phi strongly. So the mechanism fixes exactly the phi-INDEPENDENT
content of the spectrum and leaves exactly the phi-DEPENDENT content free. That is a sharp
statement of its scope, and it is checked below rather than asserted.

WHAT WOULD BREAK THE DEGENERACY. In the circulant form H = a I + b P + b* P^2 the mode stiffnesses
are a + 2|b| cos(arg b + 2 pi q/3), so the q = 1 and q = 2 modes split if and only if arg b is
neither 0 nor pi. A REAL bond leaves them degenerate; a COMPLEX bond splits them. The phase debt is
therefore precisely the question of why the bond is complex and with what argument.

Run: python3 scripts/koide_phase_is_a_flat_direction.py
"""
import cmath
import math

N = 3
OM = cmath.exp(2j * math.pi / 3)


def circulant_eigs(a, b):
    """Stiffnesses of H = a I + b P + b* P^2 : eps_q = a + 2 Re(b omega^q)."""
    return [a + 2 * (b * OM**q).real for q in range(N)]


print("=" * 78)
print("(1) THE DEMOCRATIC GRAPH IN CIRCULANT FORM")
print("=" * 78)
print("  The graph's Hessian is (N+1) I - J. On the 3-cycle J = I + P + P^2, so")
print("      H = 4I - (I + P + P^2) = 3I - P - P^2,   i.e.  a = 3, b = -1  (REAL).")
eg = circulant_eigs(3.0, -1.0)
print()
print(f"  {'mode q':>8} {'eps_q':>10}")
print("  " + "-" * 20)
for q, e in enumerate(eg):
    print(f"  {q:>8} {e:10.6f}")
print()
print(f"  eps_1 - eps_2 = {eg[1]-eg[2]:.3e}   -- the doublet is EXACTLY degenerate")
print()
print("  NOTE THE CONVENTION TRAP. This (a, b) is the CIRCULANT pair and is not T6's (a, b),")
print("  which is (on-site, bond) in H = (1/2) sum [a f_k^2 + b (f_k - f_{k+1})^2]. The graph")
print("  gives on-site = bond = g, i.e. T6's a = b; in circulant form the same operator reads")
print("  a = 3g, b = -g. Two different pairs of letters for two different decompositions of one")
print("  matrix. Quoting 'a = b' across the two rooms without saying which is a live error.")

print()
print("=" * 78)
print("(2) THE PHASE IS A FLAT DIRECTION — CHECKED, NOT ASSERTED")
print("=" * 78)
print("  Build the ring profile f_k = M + R cos(phi + 2 pi k/3) at several phi, all with the")
print("  same M and R, and evaluate the graph energy E = (1/2) f^T H f. If phi is flat, E does")
print("  not move; and Q, which is what the mechanism predicts, must not move either.")
print()
M, R = 1.0, math.sqrt(2.0)          # A = R/M = sqrt2, the null


def profile(phi):
    return [M + R * math.cos(phi + 2 * math.pi * k / N) for k in range(N)]


def energy(f, a=3.0, b=-1.0):
    H = [[0.0] * N for _ in range(N)]
    for i in range(N):
        H[i][i] += a
        H[i][(i + 1) % N] += b
        H[i][(i - 1) % N] += b
    return 0.5 * sum(f[i] * H[i][j] * f[j] for i in range(N) for j in range(N))


def koide_Q(f):
    return sum(x * x for x in f) / sum(f) ** 2


print(f"  {'phi':>10} {'masses (f_k^2), normalised':>34} {'E':>12} {'Q':>12}")
print("  " + "-" * 74)
E0 = None
for phi in (0.0, 2/9, 0.4, math.pi/12, 1.0, 2.0):
    f = profile(phi)
    ms = [x * x for x in f]
    s = sum(ms)
    E = energy(f)
    if E0 is None:
        E0 = E
    print(f"  {phi:10.5f} {'  '.join(f'{m/s:.4f}' for m in ms):>34} {E:12.6f} {koide_Q(f):12.9f}")
print()
print(f"  E is constant to {max(abs(energy(profile(p))/E0 - 1) for p in (0.0, 2/9, 0.4, 1.0, 2.0)):.2e}"
      f" and Q to"
      f" {max(abs(koide_Q(profile(p))/koide_Q(profile(0.0)) - 1) for p in (0.0, 2/9, 0.4, 1.0, 2.0)):.2e}"
      " across the whole range,")
print("  while the individual mass fractions swing over the full spectrum. So the mechanism")
print("  determines Q and determines NOTHING about which masses realise it.")

print()
print("=" * 78)
print("(3) A COMPLEX BOND DOES NOT FIX IT EITHER")
print("=" * 78)
print("  The tempting next move is a complex hopping: in circulant form the charged stiffnesses")
print("  are a + 2|b| cos(arg b +- 2 pi/3), which do split once arg b is neither 0 nor pi.")
print()
print(f"  {'arg b':>10} {'eps_1':>11} {'eps_2':>11} {'split':>12}")
print("  " + "-" * 48)
for beta in (0.0, 2/9, math.pi/6, math.pi):
    e = circulant_eigs(3.0, -1.0 * cmath.exp(1j * beta))
    print(f"  {beta:10.5f} {e[1]:11.6f} {e[2]:11.6f} {abs(e[1]-e[2]):12.3e}")
print()
print("  But the splitting does NOT reach phi, because the ring field is REAL: f_2 = f_1*, so")
print("  |f_1| = |f_2| and only the SUM of the two stiffnesses enters the energy,")
print()
print("      E = eps_0 f_0^2 + (eps_1 + eps_2) |f_1|^2,   eps_1 + eps_2 = 2a - 2 Re b,")
print()
print("  which carries no phi at all. Checked directly:")


def E_circ(f, a, b):
    H = [[0j] * N for _ in range(N)]
    for i in range(N):
        H[i][i] += a
        H[i][(i + 1) % N] += b
        H[i][(i - 1) % N] += b.conjugate()
    return sum(f[i] * H[i][j] * f[j] for i in range(N) for j in range(N)).real


print()
print(f"  {'arg b':>10} {'E(phi=0)':>13} {'E(phi=2/9)':>13} {'E(phi=1)':>13} {'spread':>11}")
print("  " + "-" * 64)
for beta in (0.0, 2/9, math.pi/6, 1.3):
    bb = -1.0 * cmath.exp(1j * beta)
    Es = [E_circ(profile(p), 3.0, bb) for p in (0.0, 2/9, 1.0)]
    print(f"  {beta:10.5f} {Es[0]:13.6f} {Es[1]:13.6f} {Es[2]:13.6f} {max(Es)-min(Es):11.2e}")
print()
print("  So EVERY Z3-symmetric quadratic form leaves phi flat, complex bond or not. The phase")
print("  cannot be reached at quadratic order by anything.")

print()
print("=" * 78)
print("(4) THE CUBIC SEES phi — BUT ONLY THROUGH cos(3 phi)")
print("=" * 78)
print("  The lowest term that sees phi is the Z3-invariant cubic, and its phi-dependence is")
print("  exactly one harmonic:")
print()
print("      sum_k f_k^3 = 3 M^3 + (9/2) M R^2 + (3/4) R^3 cos(3 phi)")
print()
print(f"  {'phi':>9} {'direct':>16} {'closed form':>16} {'diff':>10}")
print("  " + "-" * 54)
for p in (0.0, 2/9, 1.0, 2.0):
    d = sum(x**3 for x in profile(p))
    c = 3*M**3 + 4.5*M*R*R + 0.75*R**3*math.cos(3*p)
    print(f"  {p:9.4f} {d:16.9f} {c:16.9f} {abs(d-c):10.1e}")
print()
print("  That is the 3-phi object the closure is about -- and it is also the trap. A single")
print("  cos(3 phi) is stationary only at 3 phi = 0 and 3 phi = pi, so a pure cubic selects")
print(f"  phi in {{0, +-2pi/3}} or {{pi/3, pi, -pi/3}}. The closure needs 3 phi = Q = {2/3:.6f},")
print(f"  which misses the nearer of the two by {2/3:.4f} rad. A cubic CANNOT deliver it.")
print()
print("  Nor can any higher order, without tuning. Z3 symmetry makes the potential invariant")
print("  under phi -> phi + 2pi/3, and reflection makes it even in phi, so ANY real symmetric")
print("  ring potential is a function V = F(cos 3 phi) alone. Its stationary points are")
print("  sin 3 phi = 0 -- the same two -- plus the roots of F'(cos 3 phi) = 0, which sit at")
print(f"  whatever the couplings are tuned to put them. Landing one on cos Q = {math.cos(2/3):.6f}")
print("  is fitting the answer, not deriving it.")

print()
print("=" * 78)
print("VERDICT — THE TWO DEBTS ARE DIFFERENT IN KIND")
print("=" * 78)
print("  The koide_relation file states the debt as 'one number and one relation'. They are now")
print("  cleanly separated, and their difficulty is not shared:")
print()
print("    THE NUMBER (why Q = 2/3): a statement about a RATIO OF MODULI. The democratic graph")
print("      supplies a candidate, and Q is phase-blind, so that candidate is complete on its")
print("      own terms -- it does not owe the phase as a missing piece.")
print()
print("    THE RELATION (why 3 arg f_1 = Q): unreachable from the ring's own real potential at")
print("      ANY order. Quadratic terms leave phi exactly flat; cubic and higher see it only")
print("      through cos(3 phi), whose natural stationary points are 0 and pi. Producing")
print("      3 phi = Q requires an EXTERNAL PHASE REFERENCE that carries the angle Q itself.")
print()
print("  That is why the corpus's route for it is thermal rather than potential-based: the KMS")
print("  construction supplies exactly such a reference, the Euclidean time circle, and reads")
print("  the angle as a twist per face. Whether that reference is legitimate is task #2's real")
print("  question. What is settled here is that nothing internal to the ring can answer it --")
print("  which retires every candidate built from the ring's own couplings, at every order.")
