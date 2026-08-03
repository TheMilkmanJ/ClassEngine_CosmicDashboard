"""Does a = b have a structural source? The medium as a fourth node.

koide_quantum_law_null.py restated board task #1: the null is a = b (on-site stiffness equal to
bond stiffness) under the equal-quanta law, not a = 3b. a = b is a far more natural target -- one
constant in two places -- but "more natural" is not a derivation. This looks for the structure that
produces it.

THE OBSERVATION THAT STARTS IT. In H = (1/2) sum_k [a f_k^2 + b (f_k - f_{k+1})^2], the two terms
are not different in kind. The bond term penalises a face's amplitude against its NEIGHBOUR. The
on-site term penalises it against ZERO -- that is, against the background. So the on-site term is
already a bond: the bond to the medium. Written that way, a = b says nothing more than

    every bond has the same strength, and the medium is one of the nodes.

THE STRUCTURE. Take N faces plus the medium as one further node, all pairs coupled with a single
constant g (a complete graph K_{N+1}), and pin the medium's amplitude at the reference value 0
because it is the condensate the faces are excitations of:

    H = (g/2) [ sum_{i<j<=N} (f_i - f_j)^2  +  sum_{i<=N} (f_i - 0)^2 ]

This has no free ratio in it at all. What comes out is checked below -- including whether it picks
out a face count.

Run: python3 scripts/koide_democratic_graph_null.py
"""
import itertools
import math

print("=" * 78)
print("(1) THE DEMOCRATIC GRAPH'S STIFFNESS MATRIX")
print("=" * 78)


def stiffness_matrix(N, g=1.0, pin_medium=True):
    """Hessian of the K_{N+1} democratic energy in the N face amplitudes, medium pinned at 0."""
    H = [[0.0] * N for _ in range(N)]
    # face-face bonds
    for i, j in itertools.combinations(range(N), 2):
        H[i][i] += g; H[j][j] += g
        H[i][j] -= g; H[j][i] -= g
    # face-medium bonds (medium pinned, so only the diagonal survives)
    if pin_medium:
        for i in range(N):
            H[i][i] += g
    return H


def spectrum(N, **kw):
    """(eps_singlet, eps_other) using the exact circulant/complete-graph eigenvectors."""
    H = stiffness_matrix(N, **kw)
    s = [1 / math.sqrt(N)] * N
    eps_s = sum(s[i] * H[i][j] * s[j] for i in range(N) for j in range(N))
    # any zero-sum vector is a non-singlet eigenvector on the complete graph
    d = [0.0] * N
    d[0], d[1] = 1 / math.sqrt(2), -1 / math.sqrt(2)
    eps_d = sum(d[i] * H[i][j] * d[j] for i in range(N) for j in range(N))
    return eps_s, eps_d


print("  For N = 3 the matrix is, in units of g:")
for row in stiffness_matrix(3):
    print("     [" + "  ".join(f"{v:6.2f}" for v in row) + "]")
print()
print("  i.e. (N+1) I - J, whose eigenvalues are (N+1) - N = 1 on the singlet and (N+1) on")
print("  every zero-sum mode. In the (a, b) language this is a = b = g exactly -- the on-site")
print("  term IS the bond to the pinned medium, carrying the same g.")
print()
print(f"  {'N':>4} {'eps_singlet':>13} {'eps_other':>11} {'ratio':>9} {'a/b':>8}")
print("  " + "-" * 50)
for N in range(2, 8):
    es, ed = spectrum(N)
    print(f"  {N:>4} {es:13.5f} {ed:11.5f} {ed/es:9.5f} {1.0:8.4f}")
print()
print("  The ratio is N+1 and the a/b is 1 at every N: the structure fixes the RATIO by the")
print("  face count and fixes a = b unconditionally.")

print()
print("=" * 78)
print("(2) THE NULL ON THIS STRUCTURE PICKS OUT A FACE COUNT")
print("=" * 78)
print("  Under the equal-quanta law <x^2> ~ 1/w, and w ~ sqrt(eps), so with N-1 non-singlet")
print("  modes sharing the doublet-analogue role:")
print()
print("      R^2 / f_0^2 = (N - 1) * w_0/w_other = (N - 1) / sqrt(N + 1)")
print()
print("  and the null R = f_0 requires (N-1)^2 = N+1, i.e. N^2 - 3N = 0, i.e. N = 0 or N = 3.")
print()
print(f"  {'N':>4} {'(N-1)/sqrt(N+1)':>18} {'R/f_0':>10} {'null?':>8}")
print("  " + "-" * 46)
for N in range(2, 9):
    es, ed = spectrum(N)
    ratio = (N - 1) * math.sqrt(es / ed)          # (N-1) * w_0/w_other, built from the spectrum
    print(f"  {N:>4} {ratio:18.10f} {math.sqrt(ratio):10.6f}"
          f" {'YES' if abs(ratio - 1) < 1e-12 else '':>8}")
print()
print("  Verified from the computed spectrum, not from the closed form. N = 3 alone, exactly.")

print()
print("=" * 78)
print("(3) AND THE KOIDE RATIO IT PRODUCES")
print("=" * 78)
print("  Q = sum(m)/ (sum sqrt(m))^2 = sum f_k^2 / (sum f_k)^2. By Parseval with f_0 the")
print("  uniform component and R^2 the rest, sum f_k^2 = f_0^2 + R^2 and sum f_k = sqrt(N) f_0,")
print("  so")
print()
print("      Q(N) = (1 + R^2/f_0^2) / N = (1 + (N-1)/sqrt(N+1)) / N")
print()
print(f"  {'N':>4} {'Q(N)':>14} {'2/N':>12} {'null (Q = 2/N)?':>18}")
print("  " + "-" * 52)
for N in range(2, 9):
    es, ed = spectrum(N)
    r2 = (N - 1) * math.sqrt(es / ed)
    Q = (1 + r2) / N
    hit = abs(Q - 2.0 / N) < 1e-12
    print(f"  {N:>4} {Q:14.10f} {2.0/N:12.8f} {'YES' if hit else '':>18}")
print()
es, ed = spectrum(3)
r2 = 2 * math.sqrt(es / ed)
Q3 = (1 + r2) / 3
print(f"  At N = 3:  Q = {Q3:.15f}")
print(f"             2/3 = {2/3:.15f}")
print(f"             difference = {abs(Q3 - 2/3):.3e}")
print()
print("  Two facts meeting, and they are independent of each other:")
print("    * the null R = f_0 forces Q = 2/N, by Parseval alone, for any N;")
print("    * the democratic graph with equal quanta delivers R = f_0 only at N = 3.")
print("  So on this structure Q = 2/3 is not fitted -- it is the only place the two agree.")

print()
print("=" * 78)
print("(4) THE REST OF THE CHAIN, CARRIED THROUGH")
print("=" * 78)
rho2 = 0.5 * r2                     # rho^2 = |f_1|^2/f_0^2, and R^2 = 2|f_1|^2 at N = 3
A = math.sqrt(6 * Q3 - 2)
tau = -math.log(A / 2)
print(f"    rho^2 = {rho2:.15f}   (1/2 = {0.5:.15f})")
print(f"    A     = sqrt(6Q - 2) = {A:.15f}   (sqrt2 = {math.sqrt(2):.15f})")
print(f"    tau   = -ln(A/2)     = {tau:.15f}   (ln2/2 = {math.log(2)/2:.15f})")
print(f"    T_c   = tau * m_e    = {tau*0.51099895e6/1e3:.6f} keV   (177.099 keV)")
print()
print("  and the frequency condition the cold law needs comes out of the same spectrum:")
print(f"    w_other/w_0 = sqrt(eps_other/eps_singlet) = {math.sqrt(ed/es):.15f}   (needs 2)")

print()
print("=" * 78)
print("(6) THE CHARGE-COUPLED FILTER, PASSED WITHOUT BEING ASKED TO")
print("=" * 78)
print("  A mechanism for the charged-lepton null has to say why the NEUTRINO triple does not")
print("  obey it -- Q_nu = 0.458, nowhere near 2/3. This structure answers that without a new")
print("  assumption, because the face-medium bond is a coupling to the screening background,")
print("  and screening weights carriers by q^2. A neutral face has NO medium bond.")
print()
print("  Set the medium bond to zero (the neutral case) and keep the face-face bonds:")
for lbl, pin in (("charged faces (medium bond on)", True), ("neutral faces (medium bond off)", False)):
    es, ed = spectrum(3, pin_medium=pin)
    tag = f"eps_singlet = {es:.5f}   eps_other = {ed:.5f}"
    print(f"    {lbl:<34} {tag}")
print()
es0, ed0 = spectrum(3, pin_medium=False)
print(f"  The neutral case gives eps_singlet = {es0:.1f} EXACTLY -- the uniform mode is unbound,")
print("  because with no medium to measure against, shifting all three faces together costs")
print("  nothing. That is a zero mode, not a small stiffness.")
print()
print("  So for neutral faces the ratio eps_other/eps_singlet is not large, it is UNDEFINED,")
print("  and the mechanism makes no prediction for Q at all -- the uniform amplitude must be")
print("  set by something outside this Hamiltonian. Which is exactly the observed situation:")
print("  the null is a charged-sector statement, and Q_nu is free.")
print()
print("  This matters because it was not put in by hand. The same q^2 screening weight that")
print("  the basement's species selection uses, applied here, switches the mechanism off for")
print("  neutral faces and on for charged ones. The charge-coupled filter and this structure")
print("  were built from different materials and agree.")
print()
print("  It also predicts the sign of the effect on any OTHER neutral triple: no null, ever,")
print("  for a species with no medium bond. That is falsifiable in principle and it is the")
print("  cheapest way to attack this mechanism.")

print()
print("=" * 78)
print("(5) WHAT IS DERIVED, AND WHAT IS ASSUMED")
print("=" * 78)
print("  ASSUMED — four premises, each stated so it can be attacked:")
print("    (P1) the three faces and the medium are the nodes of one graph;")
print("    (P2) every pair is coupled with the SAME constant (democratic, no free ratio);")
print("    (P3) the medium is pinned at the reference amplitude, being the condensate the")
print("         faces are excitations of;")
print("    (P4) the modes carry EQUAL QUANTA, not equal energy.")
print()
print("  DERIVED — from those four and nothing else:")
print("    a = b, hence eps_charged/eps_neutral = 4, hence R_c = M_c, hence Q = 2/3,")
print("    hence A = sqrt2 and tau = ln2/2 and T_c = 177.099 keV. Exact, with no")
print("    temperature, no ensemble average, and no tuned ratio anywhere.")
print()
print("  AND — the face count is not an input to the null. Given (P1)-(P4), R = f_0 holds at")
print("  N = 3 and at no other N. The three faces and the value 2/3 are the same fact.")
print()
print("  THE HONEST WEAKNESS. (P4) is the live one. Equal quanta is what makes the (2n+1)")
print("  factor cancel and the result exact, and nothing here derives it -- it is the branch")
print("  the delivery-law fork left open, now carrying the whole chain. (P2) is the second:")
print("  'democratic' is the corpus's idiom for this ring and is not free. Neither is smuggled")
print("  in; both are named.")
print()
print("  WHAT IT IS NOT. This is not the occupancy lock. The lock asserted a specific integer")
print("  occupancy (N_0 = 1) for one mode; this asserts only that the two sectors agree with")
print("  each other, whatever the number is. That is strictly weaker and does the same work,")
print("  which is the argument for preferring it.")
