"""Which pair interaction gives the 2:1 singlet:doublet stiffness the null needs?

Coulomb (1/r) on a three-defect ring gives exactly 8, against the 2 the R_c = M_c condition
names. Before treating that factor of four as a defect, the interaction should be the right one.

The corpus states the family field's own regime: "the family field's log coupling ⟹ effectively
2D" (T6, and the retired 2D-Potts entry rests on the same fact). Defects in a two-dimensional
condensate are VORTICES, and two-dimensional vortices interact as -log r, not as 1/r. Coulomb was
the wrong kernel to test.

This sweeps the pair interaction and reads the ratio off each.

Run: python3 scripts/ring_stiffness_by_interaction.py
"""
import itertools
import math

TH = [2 * math.pi * k / 3 for k in range(3)]


def stiffnesses(kernel, R0=1.0, h=None):
    """(k_singlet, k_doublet) of sum_{i<j} kernel(r_ij) in radial displacements."""
    if h is None:
        h = R0 * 1e-5

    def E(d):
        p = [((R0 + d[k]) * math.cos(TH[k]), (R0 + d[k]) * math.sin(TH[k])) for k in range(3)]
        return sum(kernel(math.hypot(p[i][0] - p[j][0], p[i][1] - p[j][1]))
                   for i, j in itertools.combinations(range(3), 2))

    H = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            a, b, c, e = [0.]*3, [0.]*3, [0.]*3, [0.]*3
            a[i] += h; a[j] += h
            b[i] += h; b[j] -= h
            c[i] -= h; c[j] += h
            e[i] -= h; e[j] -= h
            H[i][j] = (E(a) - E(b) - E(c) + E(e)) / (4 * h * h)
    q = lambda v: sum(v[i] * H[i][j] * v[j] for i in range(3) for j in range(3))
    S = [1 / math.sqrt(3)] * 3
    D = [2 / math.sqrt(6), -1 / math.sqrt(6), -1 / math.sqrt(6)]
    return q(S), q(D)


KERNELS = (
    ("2D vortex / log:  -log r", lambda r: -math.log(r)),
    ("Coulomb 3D:        1/r", lambda r: 1.0 / r),
    ("1/r^2", lambda r: 1.0 / r**2),
    ("1/r^3", lambda r: 1.0 / r**3),
    ("linear (confining): r", lambda r: r),
    ("harmonic:          r^2", lambda r: r * r),
)

print("=" * 76)
print("SINGLET : DOUBLET STIFFNESS, BY PAIR INTERACTION")
print("=" * 76)
print(f"  {'interaction':<28} {'k_S':>11} {'k_D':>11} {'ratio':>10}")
print("  " + "-" * 64)
for name, ker in KERNELS:
    ks, kd = stiffnesses(ker)
    print(f"  {name:<28} {ks:11.6f} {kd:11.6f} {ks/kd:10.5f}")

print()
print("=" * 76)
print("AGAINST THE CONDITION")
print("=" * 76)
ks, kd = stiffnesses(lambda r: -math.log(r))
print(f"  the R_c = M_c condition needs                 2.00000")
print(f"  the geometric torus host supplied             0.99000")
print(f"  Coulomb 1/r supplies                          8.00000")
print(f"  the 2D VORTEX log interaction supplies        {ks/kd:.5f}")
print()
print(f"  miss against the requirement: {abs((ks/kd)/2 - 1)*100:.3f}%")

print()
print("=" * 76)
print("SCALE-FREEDOM AND ANALYTIC FORM")
print("=" * 76)
for R in (0.5, 1.0, 10.0, 100.0):
    a, b = stiffnesses(lambda r: r * r, R0=R)
    print(f"  harmonic, R = {R:7.1f}   k_S = {a:11.6f}   k_D = {b:11.6f}   ratio = {a/b:.6f}")
print()
print("  ANALYTIC, and exact. With x_k = R + d_k and cos(120 deg) = -1/2,")
print("    |r_i - r_j|^2 = x_i^2 + x_j^2 + x_i x_j,")
print("  so summing the three pairs gives  U = (3/2) sum x_k^2 + (1/2) (sum x_k)^2  and")
print("    H_ij = 3 delta_ij + 1,   i.e.  H = 3I + J.")
print("  J annihilates the doublet and gives 3 on the singlet, so the eigenvalues are")
print("    k_S = 6  (singlet),   k_D = 3  (doublet, twice degenerate)   ->  ratio EXACTLY 2.")
print("  The Hessian of a quadratic form is constant, so this holds at every R with no")
print("  expansion and no leading-order caveat.")
print()
print("  And the log kernel's doublet stiffness is EXACTLY ZERO, not small: for -log r the")
print("  shape mode is a flat direction at quadratic order. A 2D vortex ring confines its")
print("  breathing mode and does not confine its shape mode at all.")
