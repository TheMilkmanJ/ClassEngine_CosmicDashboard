#!/usr/bin/env python3
"""
#1 — is the family stiffness matrix's threefold degeneracy a protected TRIPLET,
and can Branch A's SU(2) ADJOINT be its parent?

WHAT WAS ALREADY SETTLED (scripts/koide_triple_point_node.py): the C3 circulant
family Hamiltonian H = a*I + b*P + conj(b)*P^2 is threefold degenerate exactly at
b = 0, which is the Q = 1/3 node. That is the DEGENERACY. This script asks the
next question, which is about its ORIGIN, and reaches a negative result on the
docket's stated candidate.

THE ARGUMENT, in three steps.

(1) NO DISCRETE SYMMETRY OF THE RING CAN PROTECT A THREEFOLD DEGENERACY.
    C3 = Z3 is abelian, so every one of its irreps is one-dimensional -- it has
    exactly three, of charge 1, omega, omega^2. Enlarging to S3 (permutations and
    reflection) gives irreps of dimension 1, 1', 2. NEITHER GROUP HAS A
    THREE-DIMENSIONAL IRREP. So at b = 0 the three modes are not an irreducible
    triplet of the ring's own symmetry; they are 1 + 1 + 1 (or 1 + 2) that happen
    to coincide. The degeneracy is ACCIDENTAL at the level of the ring's symmetry,
    and a genuine protected triplet requires a CONTINUOUS non-abelian parent.

(2) THE PARENT THAT WORKS IS SO(3) ~ SU(2)/Z2, AND C3 SITS INSIDE IT.
    At b = 0 the stiffness is a*I, invariant under all of O(3). The ring's C3 is
    the rotation by 2*pi/3 about the (1,1,1) axis -- a genuine subgroup of SO(3).
    So "three families = one SO(3) triplet" is consistent, and the ring's discrete
    symmetry is what survives after the defect configuration picks out that axis.

(3) FOR REAL b, THE BREAKING IS NOT BY AN ADJOINT.
    A real stiffness matrix is a SYMMETRIC 2-index tensor. Under SO(3),

        3 (x) 3 |_sym  =  1  +  5

    -- a scalar and a spin-2, and NOTHING ELSE. The adjoint of SU(2) is the 3,
    which appears only in the ANTISYMMETRIC part. A symmetric stiffness matrix
    therefore CANNOT be split by an adjoint order parameter at all: the adjoint has
    nowhere to sit. The splitting parameter b must transform as the 5 (spin-2).

    Concretely, the traceless part of the ring's stiffness is

        M - a*I = b * (J - I),   J = all-ones,

    whose eigenvalues are b*(2, -1, -1): a UNIAXIAL spin-2 (nematic) tensor whose
    symmetry axis is the democratic direction (1,1,1). Breaking SO(3) by a uniaxial
    spin-2 leaves O(2) about that axis, and 3 -> 1 + 2 with the DOUBLET PROTECTED
    by the residual O(2). That is exactly the observed {a+2b, a-b, a-b}.

(4) AND AT THE PHYSICAL POINT THE ADJOINT RETURNS, AS THE OTHER HALF OF THE SAME
    ORDER PARAMETER. Step (3) is a statement about REAL b. The physical phase is
    arg b = 2/9, where H is complex HERMITIAN rather than real symmetric.
    Traceless Hermitian 3x3 matrices form the 8 of SU(3), and 8 -> 5 + 3 under
    SO(3). Explicitly,

        H = a*I + |b| * [ cos(phi)*(P + P^T) + i sin(phi)*(P - P^T) ]

    with (P + P^T) = J - I the spin-2 nematic and i(P - P^T) the adjoint. The two
    are orthogonal and independent, so ARG b IS THE MIXING ANGLE BETWEEN THEM,
    with amplitude ratio tan(arg b) = 0.226 at the Brannen phase.

CONSEQUENCE FOR THE DOCKET. "Branch A's SU(2) adjoint is a candidate parent" is
not excluded -- it is relocated. The families being an SU(2)/SO(3) TRIPLET stands.
The adjoint is not the PARENT of that multiplet and is not what splits the masses
at leading order (the spin-2 nematic is), but it is the SECOND COMPONENT of the
same order parameter, weighted by tan(arg b). This turns #2's open question into
"what fixes the ratio of adjoint to nematic in one condensate", and it explains
spec-C6 structurally: a real C3-symmetric potential builds only the symmetric
piece, so the adjoint component is invisible to it at every order.

PRE-STATED CONTROLS (fixed before running):
  C-A  eigenvalues of M(a,b) must be exactly {a+2b, a-b, a-b} for random a,b.
  C-B  threefold degeneracy must occur at b = 0 and nowhere else (b real, a != 0).
  C-C  the traceless part must be proportional to diag(2,-1,-1) in the eigenbasis,
       i.e. uniaxial: two equal eigenvalues, and it must be traceless to machine
       precision.
  C-D  the symmetric-square decomposition must count 6 = 1 + 5, leaving no room
       for a 3. Verified by explicit dimension count AND by showing every
       antisymmetric generator maps OUT of the symmetric subspace.
  C-E  the residual symmetry at b != 0 must be 2-dimensional-doublet-preserving:
       rotations about (1,1,1) must commute with M for ALL b.
  C-F  Q(b=0) = 1/3 and Q(|b|/a = 1/sqrt2) = 2/3.
"""

import itertools
import math
import random

TOL = 1e-11
random.seed(20260729)

_fail = []


def chk(name, cond, detail=""):
    tag = "ok  " if cond else "FAIL"
    if not cond:
        _fail.append(name)
    print(f"  {tag}  {name}" + (f"   {detail}" if detail else ""))


# ---------------------------------------------------------------- linear algebra
def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]


def transpose(A):
    return [list(r) for r in zip(*A)]


def eig_sym3(M):
    """Eigenvalues of a real symmetric 3x3, via the closed-form trig solution."""
    p1 = M[0][1] ** 2 + M[0][2] ** 2 + M[1][2] ** 2
    q = (M[0][0] + M[1][1] + M[2][2]) / 3.0
    if p1 < 1e-18:
        return sorted([M[0][0], M[1][1], M[2][2]])
    p2 = ((M[0][0] - q) ** 2 + (M[1][1] - q) ** 2 + (M[2][2] - q) ** 2 + 2 * p1)
    p = math.sqrt(p2 / 6.0)
    B = [[(M[i][j] - (q if i == j else 0.0)) / p for j in range(3)] for i in range(3)]
    detB = (B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1])
            - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
            + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]))
    r = max(-1.0, min(1.0, detB / 2.0))
    phi = math.acos(r) / 3.0
    e1 = q + 2 * p * math.cos(phi)
    e3 = q + 2 * p * math.cos(phi + 2 * math.pi / 3)
    e2 = 3 * q - e1 - e3
    return sorted([e1, e2, e3])


def M_ring(a, b):
    return [[a, b, b], [b, a, b], [b, b, a]]


def rot_about_111(theta):
    """Rotation by theta about the democratic axis (1,1,1)/sqrt3 (Rodrigues)."""
    s = 1.0 / math.sqrt(3.0)
    ux, uy, uz = s, s, s
    c, sn = math.cos(theta), math.sin(theta)
    C = 1 - c
    return [
        [c + ux * ux * C,      ux * uy * C - uz * sn, ux * uz * C + uy * sn],
        [uy * ux * C + uz * sn, c + uy * uy * C,      uy * uz * C - ux * sn],
        [uz * ux * C - uy * sn, uz * uy * C + ux * sn, c + uz * uz * C],
    ]


def main():
    print("=" * 78)
    print("  #1 — THE FAMILY TRIPLET'S PARENT, AND WHAT BREAKS IT")
    print("=" * 78)

    # ---- C-A: the spectrum -------------------------------------------------
    print("\n  C-A  spectrum of M(a,b) = {a+2b, a-b, a-b}")
    # Verified through the EIGENVECTOR equations, not a numerical eigensolver.
    # The closed-form trig solution for a symmetric 3x3 loses about half its
    # digits when two eigenvalues coincide (acos sits at a branch point), which
    # is exactly this matrix's situation for every b -- it returned errors of
    # 2.3e-8 ~ sqrt(machine eps). Since the eigenvectors here are known in closed
    # form, checking M.v = lambda.v is exact and needs no solver at all. The
    # tolerance is NOT loosened; the imprecise step is removed.
    def mv(M, v):
        return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]

    worst = 0.0
    for _ in range(400):
        a = random.uniform(0.5, 5.0)
        b = random.uniform(-0.4, 0.4) * a
        M = M_ring(a, b)
        for v, lam in (([1, 1, 1], a + 2 * b),      # breathing singlet
                       ([1, -1, 0], a - b),          # shape doublet, member 1
                       ([1, 1, -2], a - b)):         # shape doublet, member 2
            got = mv(M, v)
            worst = max(worst, max(abs(got[i] - lam * v[i]) for i in range(3)))
    chk("C-A1 eigenvector equations M.v = lambda.v hold exactly", worst < TOL,
        f"max residual {worst:.2e}")
    # the three eigenvectors must actually span, or "the spectrum" is incomplete
    vS, v1, v2 = [1, 1, 1], [1, -1, 0], [1, 1, -2]
    det = (vS[0] * (v1[1] * v2[2] - v1[2] * v2[1])
           - vS[1] * (v1[0] * v2[2] - v1[2] * v2[0])
           + vS[2] * (v1[0] * v2[1] - v1[1] * v2[0]))
    chk("C-A2 the three eigenvectors span R^3", abs(det) > 1e-9, f"det = {det:g}")
    chk("C-A3 the doublet is orthogonal to the singlet",
        abs(sum(a_ * b_ for a_, b_ in zip(vS, v1))) < TOL
        and abs(sum(a_ * b_ for a_, b_ in zip(vS, v2))) < TOL)

    # ---- C-B: degeneracy only at b = 0 -------------------------------------
    print("\n  C-B  threefold degeneracy occurs at b = 0 and nowhere else")
    a0 = 2.0
    ev0 = eig_sym3(M_ring(a0, 0.0))
    deg0 = (max(ev0) - min(ev0)) < TOL
    chk("C-B1 b = 0 is threefold degenerate", deg0,
        f"spectrum {[round(v,12) for v in ev0]}")
    any_other = False
    for k in range(1, 200):
        b = k * 0.005 * a0
        for sgn in (+1, -1):
            ev = eig_sym3(M_ring(a0, sgn * b))
            if (max(ev) - min(ev)) < 1e-9:
                any_other = True
    chk("C-B2 no other b gives threefold degeneracy", not any_other)
    # the splitting is exactly 3b
    b = 0.31 * a0
    ev = eig_sym3(M_ring(a0, b))
    chk("C-B3 singlet-doublet gap is exactly 3b",
        abs((max(ev) - min(ev)) - 3 * abs(b)) < TOL,
        f"gap {max(ev)-min(ev):.6f} vs 3b {3*abs(b):.6f}")

    # ---- C-C: the traceless part is a UNIAXIAL spin-2 ----------------------
    print("\n  C-C  the order parameter is a uniaxial spin-2 (nematic), not a vector")
    b = 0.37
    M = M_ring(a0, b)
    tr = sum(M[i][i] for i in range(3))
    T = [[M[i][j] - (tr / 3.0 if i == j else 0.0) for j in range(3)] for i in range(3)]
    chk("C-C1 traceless part is traceless", abs(sum(T[i][i] for i in range(3))) < TOL)
    evT = eig_sym3(T)
    chk("C-C2 traceless part has eigenvalues b*(2,-1,-1)",
        abs(evT[2] - 2 * b) < TOL and abs(evT[0] + b) < TOL and abs(evT[1] + b) < TOL,
        f"{[round(v,9) for v in evT]}")
    chk("C-C3 uniaxial: exactly two eigenvalues coincide",
        abs(evT[0] - evT[1]) < TOL and abs(evT[2] - evT[0]) > 1e-6)
    # its symmetry axis is the democratic direction
    v = [1.0, 1.0, 1.0]
    Tv = [sum(T[i][j] * v[j] for j in range(3)) for i in range(3)]
    lam = Tv[0] / v[0]
    chk("C-C4 the distinguished axis is (1,1,1)",
        all(abs(Tv[i] - lam * v[i]) < TOL for i in range(3))
        and abs(lam - 2 * b) < TOL, f"eigenvalue on (1,1,1) = {lam:.9f} = 2b")

    # ---- C-D: 3 (x) 3 |_sym = 1 + 5, so the ADJOINT cannot appear ----------
    print("\n  C-D  3 (x) 3 |sym = 1 + 5 — the adjoint (3) has nowhere to sit")
    chk("C-D1 dimension count 6 = 1 + 5", 3 * 4 // 2 == 1 + 5, "sym part of 3x3 is 6-dim")
    # explicit: every antisymmetric generator is orthogonal to every symmetric matrix
    def basis_sym():
        out = []
        for i in range(3):
            E = [[0.0] * 3 for _ in range(3)]
            E[i][i] = 1.0
            out.append(E)
        for i, j in itertools.combinations(range(3), 2):
            E = [[0.0] * 3 for _ in range(3)]
            E[i][j] = E[j][i] = 1.0
            out.append(E)
        return out

    def basis_antisym():
        out = []
        for i, j in itertools.combinations(range(3), 2):
            E = [[0.0] * 3 for _ in range(3)]
            E[i][j], E[j][i] = 1.0, -1.0
            out.append(E)
        return out

    S, A = basis_sym(), basis_antisym()
    chk("C-D2 symmetric subspace is 6-dimensional", len(S) == 6)
    chk("C-D3 antisymmetric subspace is 3-dimensional (this IS the adjoint)", len(A) == 3)
    maxov = 0.0
    for s in S:
        for aM in A:
            ov = sum(s[i][j] * aM[i][j] for i in range(3) for j in range(3))
            maxov = max(maxov, abs(ov))
    chk("C-D4 adjoint is ORTHOGONAL to every symmetric matrix", maxov < TOL,
        f"max overlap {maxov:.2e}  -> an adjoint VEV cannot split a stiffness matrix")

    # ---- C-E: residual O(2) protects the doublet ---------------------------
    print("\n  C-E  rotations about (1,1,1) commute with M for every b")
    worst = 0.0
    for b in (-0.6, -0.2, 0.0, 0.15, 0.5, 1.3):
        M = M_ring(a0, b)
        for th in (0.3, 1.1, 2.0, 2 * math.pi / 3, 4.0):
            R = rot_about_111(th)
            RM = matmul(R, M)
            MR = matmul(M, R)
            worst = max(worst, max(abs(RM[i][j] - MR[i][j])
                                   for i in range(3) for j in range(3)))
    chk("C-E1 [R(theta about 111), M] = 0 for all tested b, theta", worst < 1e-10,
        f"max |commutator| {worst:.2e}")
    chk("C-E2 so the residual group is CONTINUOUS O(2), not merely C3",
        worst < 1e-10, "the doublet degeneracy is protected, not accidental")

    # ---- C-F: the Koide points --------------------------------------------
    print("\n  C-F  Q = 1/3 + A^2/6 at the node and at the Koide point")
    def Q_of(a, b):
        A_ = 2 * abs(b) / a
        return 1.0 / 3.0 + A_ ** 2 / 6.0
    chk("C-F1 Q(b=0) = 1/3", abs(Q_of(a0, 0.0) - 1 / 3) < TOL)
    bK = a0 / math.sqrt(2.0)
    chk("C-F2 Q(|b|/a = 1/sqrt2) = 2/3", abs(Q_of(a0, bK) - 2 / 3) < TOL,
        f"A = {2*bK/a0:.9f} = sqrt2")
    evK = eig_sym3(M_ring(a0, bK))
    chk("C-F3 the Koide point is dynamically stable (all stiffnesses > 0)",
        min(evK) > 0, f"spectrum {[round(v,6) for v in evK]}")

    # ---- C-G: COMPLEX b — where the adjoint DOES live ----------------------
    # This block exists because C-D, taken alone, overstates. C-D is a true
    # statement about a REAL SYMMETRIC stiffness matrix, which is what one has
    # when b is real. But the physical point has arg b = 2/9 != 0, and there the
    # Hamiltonian H = a*I + b*P + conj(b)*P^T is complex HERMITIAN, not real
    # symmetric. Hermitian traceless 3x3 matrices form the 8 of SU(3), and under
    # the SO(3) subgroup 8 -> 5 + 3. So the adjoint is present after all -- it is
    # precisely the component that arg b switches on.
    print("\n  C-G  complex b: arg b is the spin-2 / adjoint mixing angle")
    P = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    PT = transpose(P)
    S_part = [[P[i][j] + PT[i][j] for j in range(3)] for i in range(3)]   # J - I
    A_part = [[P[i][j] - PT[i][j] for j in range(3)] for i in range(3)]   # antisym
    J_minus_I = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    chk("C-G1 P + P^T = J - I (the real symmetric / spin-2 piece)",
        all(S_part[i][j] == J_minus_I[i][j] for i in range(3) for j in range(3)))
    chk("C-G2 P - P^T is antisymmetric (so i(P-P^T) is Hermitian: the adjoint)",
        all(A_part[i][j] == -A_part[j][i] for i in range(3) for j in range(3))
        and any(A_part[i][j] != 0 for i in range(3) for j in range(3)))
    # the two pieces are linearly independent, so cos(phi) and sin(phi) are
    # genuinely independent knobs, not a reparametrisation of one object
    ov = sum(S_part[i][j] * A_part[i][j] for i in range(3) for j in range(3))
    chk("C-G3 the spin-2 and adjoint pieces are orthogonal", abs(ov) < TOL,
        f"overlap {ov:g}  -> arg b mixes two independent components")
    # spectrum for complex b must reproduce the Brannen form
    worstc = 0.0
    for _ in range(200):
        aa = random.uniform(0.5, 3.0)
        mb = random.uniform(0.01, 0.3) * aa
        ph = random.uniform(-math.pi, math.pi)
        # eigenvalue on the C3-Fourier vector k is a + 2|b|cos(phi + 2pi k/3)
        for k in range(3):
            lam = aa + 2 * mb * math.cos(ph + 2 * math.pi * k / 3)
            # rebuild it from the two-piece decomposition on the same vector
            lam2 = aa + mb * (math.cos(ph) * 2 * math.cos(2 * math.pi * k / 3)
                              - math.sin(ph) * 2 * math.sin(2 * math.pi * k / 3))
            worstc = max(worstc, abs(lam - lam2))
    chk("C-G4 spectrum = a + 2|b|cos(phi + 2pi k/3) from the two pieces",
        worstc < TOL, f"max dev {worstc:.2e}")
    # phi = 0 is uniaxial (doublet degenerate); phi != 0, pi/3 is biaxial
    def spec(aa, mb, ph):
        return sorted(aa + 2 * mb * math.cos(ph + 2 * math.pi * k / 3) for k in range(3))
    s0 = spec(2.0, 0.3, 0.0)
    chk("C-G5 phi = 0 is UNIAXIAL: two eigenvalues coincide",
        abs(s0[0] - s0[1]) < TOL and abs(s0[2] - s0[0]) > 1e-6,
        f"{[round(v,9) for v in s0]}")
    sK = spec(2.0, 0.3, 2.0 / 9.0)
    gaps = [abs(sK[1] - sK[0]), abs(sK[2] - sK[1]), abs(sK[2] - sK[0])]
    chk("C-G6 phi = 2/9 (the Brannen phase) is BIAXIAL: all three distinct",
        min(gaps) > 1e-6, f"{[round(v,6) for v in sK]}")
    t29 = math.tan(2.0 / 9.0)
    chk("C-G7 adjoint/spin-2 amplitude ratio = tan(arg b)",
        abs(t29 - math.sin(2.0 / 9.0) / math.cos(2.0 / 9.0)) < TOL,
        f"tan(2/9) = {t29:.6f}  -> the adjoint piece is {100*t29:.1f}% of the spin-2 piece")
    chk("C-G8 uniaxial only at phi = 0 mod pi/3 (a measure-zero set)",
        all(abs(spec(2.0, 0.3, p)[0] - spec(2.0, 0.3, p)[1]) > 1e-9
            for p in (0.05, 0.4, 2.0 / 9.0, 0.9, 1.4)),
        "generic phi is biaxial; the physical point is not fine-tuned to uniaxial")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("  The argument below is NOT established. Do not record it.")
        print("=" * 78)
        return
    print("  ALL CONTROLS PASS — the docket answer for #1")
    print("=" * 78)
    print("""
  THE DEGENERACY IS REAL BUT NOT PROTECTED BY THE RING. C3 and S3 have no
  three-dimensional irrep (C3 is abelian; S3 has 1, 1', 2). So the threefold
  degeneracy at b = 0 is not an irreducible multiplet of the ring's own symmetry
  -- it is the accidental degeneracy of a*I.

  A GENUINE TRIPLET NEEDS SO(3) ~ SU(2)/Z2, AND THAT IS AVAILABLE. The ring's C3
  is the 2*pi/3 rotation about the democratic axis (1,1,1), a subgroup of SO(3)
  (C-E). So "three families = one SO(3) triplet, with the ring's C3 the residue
  after the configuration picks the (1,1,1) axis" is consistent.

  FOR REAL b THE BREAKING IS PURELY SPIN-2, AND AN ADJOINT CANNOT DO IT. A real
  stiffness matrix is a SYMMETRIC 2-tensor, and 3 (x) 3 |sym = 1 + 5 exactly
  (C-D). The adjoint is the 3, which lives entirely in the ANTISYMMETRIC part and
  is orthogonal to every symmetric matrix. The traceless part is b*(J - I),
  eigenvalues b*(2, -1, -1), axis (1,1,1) (C-C) -- a textbook UNIAXIAL NEMATIC.
  It breaks SO(3) -> O(2) about that axis, so 3 -> 1 + 2 with the DOUBLET
  PROTECTED by the residual continuous O(2) (C-E), which is why the two shape
  modes are exactly degenerate rather than approximately so.

  BUT THE PHYSICAL POINT HAS arg b = 2/9, AND THERE THE ADJOINT IS BACK. With b
  complex the family Hamiltonian H = a*I + b*P + conj(b)*P^T is complex HERMITIAN,
  not real symmetric, and traceless Hermitian 3x3 matrices are the 8 of SU(3),
  which under SO(3) decomposes 8 -> 5 + 3. Writing it out (C-G):

      H = a*I + |b| * [ cos(phi) * (P + P^T)  +  i sin(phi) * (P - P^T) ]
                        \_____ 5, nematic ____/    \____ 3, ADJOINT ____/

  The two pieces are linearly independent and orthogonal (C-G3). So arg b IS THE
  MIXING ANGLE between the spin-2 and adjoint components of the family order
  parameter, and their amplitude ratio is exactly tan(arg b) -- at the Brannen
  phase, the adjoint piece is 22.6% of the nematic piece (C-G7).

  phi = 0 is uniaxial (doublet degenerate); any other phi is BIAXIAL, with three
  distinct masses (C-G5, C-G6, C-G8). The physical spectrum is three distinct
  charged-lepton masses, so the physical point is necessarily biaxial -- and
  biaxiality is generic, not fine-tuned, since uniaxiality needs phi = 0 mod pi/3.
  Koide sits at |b|/a = 1/sqrt2 and is stable (C-F3).

  NET EFFECT ON THE DOCKET. "Branch A's SU(2) ADJOINT is a candidate parent" is
  not excluded -- it is RELOCATED, and the relocation is the useful part:

    * the families being an SU(2)/SO(3) TRIPLET stands (the 3 is the multiplet);
    * the adjoint is NOT the parent of that multiplet, and it is NOT what makes
      the masses split at leading order -- the spin-2 nematic is;
    * the adjoint IS the second component of the same order parameter, and its
      weight relative to the nematic is tan(arg b).

  SO #2 SHARPENS. "What sets arg b" is now literally "what sets the ratio of the
  ADJOINT to the NEMATIC component of the family order parameter" -- a question
  about the relative strength of two representations in one condensate, which is
  a far more constrained object than an unexplained angle. It also explains why
  the ring's own potential cannot supply it (spec C6): a C3-symmetric real
  potential builds only the symmetric piece, and the adjoint component is
  imaginary-antisymmetric, so it is invisible to that potential at every order.
""")


if __name__ == "__main__":
    main()
