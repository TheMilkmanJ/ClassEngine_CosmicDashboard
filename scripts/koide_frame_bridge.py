"""The owed bridge between T6's stiffness frame and the ring-on-ring frame.

The failures ledger records the two frames and says the bridge between them is owed:

    "T6's reduction works in the sqrt(m) fluctuation field ... where eps_0 = a and eps_pm = a + 3b
     and the null reads eps_charged = 2 eps_neutral -- the DOUBLET twice as stiff, the inverse
     statement. The two are reconciled only through the canonical normalizations
     R_c = sqrt(3/2) R and M_c = sqrt3 M, and NO FILE STATES THAT BRIDGE."

This pays it. Three parts:

  (1) DERIVE the two normalizations from the Fourier transform on the three-site ring, and check
      that R_c = M_c, rho = 1/sqrt2, A = sqrt2 and Q = 2/3 are one statement.

  (2) TEST the ledger's proposed reconciliation. The claim is that the normalizations reconcile
      the frames. They cannot: both frames use the SAME canonical coordinates, so the factors
      sqrt3 and sqrt(3/2) cancel from every stiffness RATIO. Something else separates them.

  (3) NAME what actually separates them. R_c = M_c is a statement about AMPLITUDES. Turning it
      into a statement about STIFFNESSES needs an energy-delivery law, and the corpus uses
      several in different rooms. Each converts the same null into a different stiffness target.
      That is the bridge -- a physical choice, not a bookkeeping convention.

Then the consequence for the kernel sweep: which delivery law each kernel result answers to.

Run: python3 scripts/koide_frame_bridge.py
"""
import cmath
import itertools
import math

N = 3
TH = [2 * math.pi * k / N for k in range(N)]
Q_FENCE_TOP = 0.689433          # the corpus's one-sided fence on Q


# ----------------------------------------------------------------------------- part 1
def fourier(f):
    """f_q = (1/sqrtN) sum_k f_k exp(-2 pi i q k / N)."""
    return [sum(f[k] * cmath.exp(-2j * math.pi * q * k / N)
                for k in range(N)) / math.sqrt(N) for q in range(N)]


print("=" * 78)
print("(1) THE TWO NORMALIZATIONS, DERIVED")
print("=" * 78)

M, R, theta = 0.37, 0.91, 0.4213        # arbitrary, to expose any accidental agreement
prof = [M + R * math.cos(theta + TH[k]) for k in range(N)]
F = fourier(prof)

Mc, Rc = abs(F[0]), math.sqrt(abs(F[1]) ** 2 + abs(F[2]) ** 2)
print(f"  ring profile f_k = M + R cos(theta + 2 pi k/3),  M = {M}, R = {R}, theta = {theta}")
print()
print(f"  M_c = |f_0|                    = {Mc:.10f}")
print(f"  sqrt3 * M                      = {math.sqrt(3)*M:.10f}"
      f"   (miss {abs(Mc/(math.sqrt(3)*M)-1):.2e})")
print(f"  R_c = sqrt(|f_1|^2 + |f_2|^2)  = {Rc:.10f}")
print(f"  sqrt(3/2) * R                  = {math.sqrt(1.5)*R:.10f}"
      f"   (miss {abs(Rc/(math.sqrt(1.5)*R)-1):.2e})")
print()
print("  Both ledger normalizations confirmed from the transform itself, at arbitrary M, R,")
print("  theta. They are not conventions anyone chose; they are what the transform returns.")

print()
rho = abs(F[1]) / abs(F[0])
A = R / M
Qv = 1 / 3 + (2 / 3) * rho ** 2
print("  THE CHAIN, checked at this arbitrary point:")
print(f"    A     = R/M            = {A:.10f}")
print(f"    rho   = |f_1|/f_0      = {rho:.10f}")
print(f"    A / (2 rho)            = {A/(2*rho):.10f}      (so A = 2 rho identically)")
print(f"    R_c/M_c                = {Rc/Mc:.10f}")
print(f"    A / (sqrt2 * R_c/M_c)  = {A/(math.sqrt(2)*Rc/Mc):.10f}      (so R_c/M_c = A/sqrt2)")
print(f"    Q = 1/3 + (2/3) rho^2  = {Qv:.10f}")
print(f"    A^2 = 6Q - 2 check     = {math.sqrt(6*Qv-2)/A:.10f}      (ratio to A)")
print()
print("  At the null all four collapse to one statement:")
print("    R_c = M_c   <=>   rho = 1/sqrt2   <=>   A = sqrt2   <=>   Q = 2/3.")


# ----------------------------------------------------------------------------- part 2
print()
print("=" * 78)
print("(2) DO THE NORMALIZATIONS RECONCILE THE FRAMES? NO -- THEY CANCEL")
print("=" * 78)
print("  Both frames grade the same three-site ring, and both quote stiffnesses of the SAME")
print("  two irreps. Write the quadratic energy in the raw amplitudes (M, R):")
print()
print("    H = (1/2)[eps_0 M_c^2 + eps_1 R_c^2] = (1/2)[3 eps_0 M^2 + (3/2) eps_1 R^2]")
print()
print("  so k_M = 3 eps_0 and k_R = (3/2) eps_1. The normalizations rescale each stiffness --")
print("  but by a FIXED factor, so in the ratio:")
print()
print("    k_R / k_M = (1/2) (eps_1 / eps_0)")
print()
print("  A frame that measures stiffness in canonical coordinates and one that measures it in")
print("  raw amplitudes differ by exactly 2, in a known direction. That is a factor 2, not the")
print("  factor 4 that separates eps_1/eps_0 = 2 from k_S/k_D = 2. The normalizations therefore")
print("  CANNOT be the reconciliation the ledger proposes; half the gap survives them and the")
print("  direction does not flip. The ledger row is corrected by this.")


# ----------------------------------------------------------------------------- part 3
print()
print("=" * 78)
print("(3) WHAT ACTUALLY SEPARATES THEM: THE ENERGY-DELIVERY LAW")
print("=" * 78)
print("  R_c = M_c constrains AMPLITUDES. Every stiffness statement in the corpus is that")
print("  constraint pushed through a law saying how energy sits in the modes. The singlet is")
print("  1 degree of freedom, the doublet is 2 -- so the laws disagree about the doublet by")
print("  factors of the mode count, and each yields a different target.")
print()
print(f"  {'delivery law':<34} {'energy per sector':<22} {'R_c = M_c  =>'}")
print("  " + "-" * 76)

# per-sector energy E and amplitude^2 as functions of the sector stiffness eps and dof count g:
#   thermal equipartition : e per dof = T          -> x^2 per dof = T/eps      -> X^2 = g T/eps
#   equal sector delivery : E per sector = E       -> X^2 = 2E/eps
#   doublet half singlet  : E_D = E_S/2            -> X^2 = 2E/eps with E halved
#   sudden quench 1/w^2   : e per dof ~ 1/eps      -> X^2 = g c/eps^2
LAWS = (
    ("thermal equipartition", "1/2 T per DOF", lambda g, e: g / e, "eps_1 = 2 eps_0", 2.0),
    ("equal sector delivery", "E each sector", lambda g, e: 1.0 / e, "eps_1 = eps_0", 1.0),
    ("doublet gets half the singlet", "E, E/2", lambda g, e: (1.0 if g == 1 else 0.5) / e,
     "eps_1 = eps_0 / 2", 0.5),
    ("sudden quench, 1/w^2 per mode", "~ 1/eps per DOF", lambda g, e: g / e ** 2,
     "eps_1 = sqrt2 eps_0", math.sqrt(2)),
)
for name, desc, amp2, target, ratio in LAWS:
    # solve amp2(1, eps0) == amp2(2, eps1) for eps1/eps0, numerically, to confirm the algebra
    lo, hi = 1e-3, 1e3
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if amp2(2, mid) > amp2(1, 1.0):
            lo = mid
        else:
            hi = mid
    got = math.sqrt(lo * hi)
    flag = "ok" if abs(got / ratio - 1) < 1e-6 else f"MISMATCH {got:.4f}"
    print(f"  {name:<34} {desc:<22} {target:<20} [{flag}]")

print()
print("  Four laws, four different stiffness targets from ONE null, spanning a factor 4.")
print("  The corpus uses at least three of them in different rooms, which is why the same")
print("  number 2 appears pointing in opposite directions. THE BRIDGE IS THE LAW, NOT THE")
print("  NORMALIZATION -- and the corpus has not fixed which law governs the freeze.")
print()
print("  T6's reduction reads sector powers off <|f_q|^2> = T/eps_q, which is the thermal row.")
print("  Its target is therefore eps_D/eps_S = 2 -- the DOUBLET stiffer. The ring-on-ring")
print("  entry's 'doublet receives half the singlet's energy' is the third row, target 1/2 --")
print("  the SINGLET stiffer. Same null, inverse targets, because the laws differ.")


# ----------------------------------------------------------------------------- part 4
print()
print("=" * 78)
print("(4) THE KERNEL SWEEP, RE-GRADED AGAINST EACH LAW")
print("=" * 78)


def sector_stiffness(kernel, R0=1.0):
    """(eps_singlet, eps_doublet) of sum_{i<j} kernel(r_ij) in radial displacements."""
    h = R0 * 1e-5

    def E(d):
        p = [((R0 + d[k]) * math.cos(TH[k]), (R0 + d[k]) * math.sin(TH[k])) for k in range(N)]
        return sum(kernel(math.hypot(p[i][0] - p[j][0], p[i][1] - p[j][1]))
                   for i, j in itertools.combinations(range(N), 2))

    H = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a, b, c, e = [0.] * N, [0.] * N, [0.] * N, [0.] * N
            a[i] += h; a[j] += h
            b[i] += h; b[j] -= h
            c[i] -= h; c[j] += h
            e[i] -= h; e[j] -= h
            H[i][j] = (E(a) - E(b) - E(c) + E(e)) / (4 * h * h)
    q = lambda v: sum(v[i] * H[i][j] * v[j] for i in range(N) for j in range(N))
    S = [1 / math.sqrt(3)] * N
    D = [2 / math.sqrt(6), -1 / math.sqrt(6), -1 / math.sqrt(6)]
    return q(S), q(D), H[0][1]


KERNELS = (
    ("2D vortex / log:  -log r", lambda r: -math.log(r)),
    ("Coulomb 3D:        1/r", lambda r: 1.0 / r),
    ("1/r^2", lambda r: 1.0 / r ** 2),
    ("1/r^3", lambda r: 1.0 / r ** 3),
    ("linear (confining): r", lambda r: r),
    ("harmonic:          r^2", lambda r: r * r),
)

print(f"  {'kernel':<28} {'eps_S':>9} {'eps_D':>9} {'eps_D/eps_S':>12} {'H_offdiag':>11}")
print("  " + "-" * 74)
ratios = {}
for name, ker in KERNELS:
    es, ed, off = sector_stiffness(ker)
    ratios[name] = ed / es
    print(f"  {name:<28} {es:9.5f} {ed:9.5f} {ed/es:12.6f} {off:11.5f}")

print()
print("  Five of the six put the doublet BELOW the singlet, the harmonic kernel highest at")
print("  exactly 1/2, tracking the positive off-diagonal Hessian element: on a ring with")
print("  cos 120 = -1/2 the pair separations grow super-additively in the radii, so breathing")
print("  pays in all three pairs at once while shape partly cancels. The sixth row breaks the")
print("  pattern and is the one to trust least, for the reason below.")
print()
print("  NOTE the linear kernel's blow-up: U = sum r_ij = 3 sqrt3 R exactly, linear in R, so its")
print("  breathing curvature is identically ZERO and the ratio is undefined, not large. That is")
print("  the tell that this sweep is unphysical as it stands -- NONE of these kernels holds the")
print("  ring at an equilibrium radius. A bare repulsion expands forever, a bare attraction")
print("  collapses. Stiffnesses read off a non-stationary point are curvatures, not restoring")
print("  frequencies, and the corpus's own frame supplies what is missing: kappa-confinement.")


# ----------------------------------------------------------------------------- part 5
print()
print("=" * 78)
print("(5) THE SAME SWEEP AT A REAL EQUILIBRIUM (the trap restored)")
print("=" * 78)
print("  Add the confining trap the ring-on-ring frame actually has, (kappa/2) sum x_k^2, and")
print("  fix kappa by demanding the symmetric ring be stationary. With s = sqrt3 R the pair")
print("  separation, the radial balance 3 sqrt3 u'(s) + 3 kappa R = 0 gives kappa = -3u'/s, and")
print("  the two sector stiffnesses come out in closed form:")
print()
print("      eps_S = 3 [ u'' - u'/s ]            eps_D = (3/4) [ u'' - 3u'/s ]")
print()
print("  so with the single dimensionless combination  t = u' / (s u'')  the whole geometry")
print("  collapses to one curve:")
print()
print("      eps_D / eps_S = (1/4) (1 - 3t) / (1 - t)")
print()


def trapped_sectors(u, up, upp, R0=1.0):
    """(eps_S, eps_D) for pair kernel u with a trap fixed by equilibrium at radius R0."""
    s = math.sqrt(3) * R0
    kappa = -3.0 * up(s) / s
    return 3.0 * (upp(s) - up(s) / s), 0.75 * (upp(s) - 3.0 * up(s) / s), kappa, s


def numeric_sectors(kernel, R0=1.0):
    """Same thing by brute-force Hessian, as an independent check of the closed form."""
    s = math.sqrt(3) * R0
    h = 1e-5
    up_num = (kernel(s + h) - kernel(s - h)) / (2 * h)
    kappa = -3.0 * up_num / s

    def E(d):
        p = [((R0 + d[k]) * math.cos(TH[k]), (R0 + d[k]) * math.sin(TH[k])) for k in range(N)]
        pair = sum(kernel(math.hypot(p[i][0] - p[j][0], p[i][1] - p[j][1]))
                   for i, j in itertools.combinations(range(N), 2))
        return pair + 0.5 * kappa * sum((R0 + d[k]) ** 2 for k in range(N))

    H = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a, b, c, e = [0.] * N, [0.] * N, [0.] * N, [0.] * N
            a[i] += h; a[j] += h
            b[i] += h; b[j] -= h
            c[i] -= h; c[j] += h
            e[i] -= h; e[j] -= h
            H[i][j] = (E(a) - E(b) - E(c) + E(e)) / (4 * h * h)
    q = lambda v: sum(v[i] * H[i][j] * v[j] for i in range(N) for j in range(N))
    S = [1 / math.sqrt(3)] * N
    D = [2 / math.sqrt(6), -1 / math.sqrt(6), -1 / math.sqrt(6)]
    return q(S), q(D)


TRAPPED = (
    ("-log r", lambda r: -math.log(r), lambda r: -1 / r, lambda r: 1 / r ** 2, None),
    ("1/r    (Coulomb)", lambda r: 1 / r, lambda r: -1 / r ** 2, lambda r: 2 / r ** 3, -1.0),
    ("1/r^2", lambda r: r ** -2, lambda r: -2 * r ** -3, lambda r: 6 * r ** -4, -2.0),
    ("1/r^3", lambda r: r ** -3, lambda r: -3 * r ** -4, lambda r: 12 * r ** -5, -3.0),
    ("r      (linear)", lambda r: r, lambda r: 1.0, lambda r: 0.0, 1.0),
    ("-r     (linear attractive)", lambda r: -r, lambda r: -1.0, lambda r: 0.0, None),
)

print(f"  {'kernel':<28} {'eps_S':>9} {'eps_D':>9} {'eps_D/eps_S':>12} {'stable?':>9} {'check':>9}")
print("  " + "-" * 80)
for name, u, up, upp, p in TRAPPED:
    eS, eD, kappa, s = trapped_sectors(u, up, upp)
    nS, nD = numeric_sectors(u)
    agree = max(abs(eS - nS), abs(eD - nD)) < 1e-4 * max(1.0, abs(eS))
    stable = eS > 1e-12 and eD > 1e-12
    rat = eD / eS if abs(eS) > 1e-12 else float("inf")
    print(f"  {name:<28} {eS:9.5f} {eD:9.5f} {rat:12.6f} {'yes' if stable else 'NO':>9}"
          f" {'ok' if agree else 'MISMATCH':>9}")

print()
print("  The closed form agrees with the brute-force Hessian in every row. For a power law")
print("  u = r^p one has t = 1/(p-1), so the curve becomes an exact rational function of p:")
print()
print("      eps_D / eps_S = (p - 4) / (4 (p - 2))")
print()
print(f"  {'p':>8} {'closed form':>14} {'(p-4)/(4(p-2))':>18}")
print("  " + "-" * 44)
for p in (-3.0, -2.0, -1.0, 1.0, 3.0, 5.0):
    eS, eD, _, _ = trapped_sectors(lambda r, p=p: r ** p,
                                   lambda r, p=p: p * r ** (p - 1),
                                   lambda r, p=p: p * (p - 1) * r ** (p - 2))
    print(f"  {p:8.1f} {eD/eS:14.6f} {(p-4)/(4*(p-2)):18.6f}")


# ----------------------------------------------------------------------------- part 6
print()
print("=" * 78)
print("(6) CAN A RING REACH THE THERMAL NULL AT ALL?")
print("=" * 78)
print("  Solve (1/4)(1 - 3t)/(1 - t) = 2 for the target eps_D/eps_S = 2:")
t_star = 7.0 / 5.0
print(f"      1 - 3t = 8(1 - t)  ->  5t = 7  ->  t* = {t_star:.6f} = 7/5")
print(f"      check: (1/4)(1 - 3t*)/(1 - t*) = {0.25*(1-3*t_star)/(1-t_star):.10f}")
print()
print("  So the null is reachable in principle -- but only on ONE branch, and the branch is the")
print("  whole result. Stability needs eps_S > 0 AND eps_D > 0, i.e. u''(1 - t) > 0 and")
print("  u''(1 - 3t) > 0. Two disjoint windows:")
print()
print(f"  {'branch':<26} {'t window':<18} {'eps_D/eps_S range':<22} {'null t* = 7/5?'}")
print("  " + "-" * 80)


def ratio_of_t(t):
    return 0.25 * (1 - 3 * t) / (1 - t)


lo_branch = [ratio_of_t(t) for t in (-1e6, -10.0, -1.0, 0.0, 0.3333 - 1e-6)]
hi_branch = [ratio_of_t(t) for t in (1 + 1e-6, 1.2, t_star, 2.0, 10.0, 1e6)]
print(f"  {chr(34) + 'convex  u_rr > 0' + chr(34):<26} {'t < 1/3':<18} "
      f"{f'[{min(lo_branch):.3f}, {max(lo_branch):.3f})':<22} "
      f"{'NO -- t* is outside'}")
print(f"  {chr(34) + 'concave u_rr < 0' + chr(34):<26} {'t > 1':<18} "
      f"{f'({min(hi_branch):.3f}, inf)':<22} "
      f"{'YES'}")
print()
print("  Every ordinary kernel lives on the convex branch: a power law has t = 1/(p-1), and the")
print("  log has t = -1, all of them t < 1/3, all of them capped at eps_D/eps_S < 3/4. That is")
print("  the ceiling the earlier sweep was bumping into, and 2 is above it by a factor 2.7.")
print()
print("  The null's branch requires u' < 0 AND u'' < 0 -- a repulsion that STRENGTHENS with")
print("  separation. No power law does this (u' < 0 forces p < 0, which forces u'' > 0), and")
print("  neither does the log. It is not a kernel anyone would write down from a medium; it is")
print("  the signature of a confining string, and even then t must sit at 7/5 exactly, which is")
print("  one tuned number and not a derivation.")
print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  1. The ledger's bridge is PAID and CORRECTED. The normalizations M_c = sqrt3 M and")
print("     R_c = sqrt(3/2) R are right, but they cancel from stiffness ratios and cannot be")
print("     the reconciliation -- they contribute a factor 2 in a fixed direction, not the")
print("     factor 4 with a flip. What separates the frames is the ENERGY-DELIVERY LAW.")
print()
print("  2. The kernel sweep's exact 2 answers the 'doublet gets half the singlet' law and is")
print("     correct there. T6's a = 3b is written in the THERMAL law and needs the inverse.")
print("     Both readings stand; neither refutes the other; the corpus has not fixed the law.")
print()
print("  3. T6's 'a = 3b does not live in ring geometry' is upgraded from a bracket to a")
print("     mechanism: on the stable convex branch the geometric ring's ceiling is")
print("     eps_D/eps_S < 3/4, and the thermal null needs 2. The route is closed by a branch,")
print("     and the only opening left is a kernel no medium supplies.")
print()
print("  4. NEW AND OWED, replacing the old blank: fix the delivery law at freeze. Until it is")
print("     fixed, no stiffness computation can be graded, and the same number will keep")
print("     arriving with opposite signs.")
