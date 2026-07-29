#!/usr/bin/env python3
"""
#81: pi/12 is NOT an independent angle -- it is the root-zero-crossing at A = sqrt2.

WHAT WAS RECORDED, AND IS WRONG. Yesterday's #81 entry closed with: "the new debt is
pi/12 itself... note pi/12 is a PURE geometric angle carrying no Q, so whatever
supplies it is a different KIND of object from the one that supplies 2/9." That
framing treats pi/12 as a new unknown requiring a new mechanism. It is not.

THE IDENTIFICATION. With the ring form sqrt(m_k) = a[1 + A cos(phi + 2 pi k/3)], the
k = 1 root vanishes when

    1 + A cos(phi + 2 pi/3) = 0   =>   cos(phi + 2 pi/3) = -1/A

At the KOIDE amplitude A = sqrt2 this is cos(...) = -1/sqrt2, so phi + 2pi/3 = 3pi/4
and

    phi_cross = 3 pi/4 - 2 pi/3 = 9 pi/12 - 8 pi/12 = pi/12      (EXACT)

So pi/12 is not a free geometric angle. It is fixed by A alone -- and A is fixed by
Koide through A^2 = 6(Q - 1/3), i.e. by the SAME invariant that fixes 2/9 via the
holonomy closure 3 arg b = Q. There is no second kind of object.

WHAT THE STRUCTURE THEN LOOKS LIKE. The zero-crossing partitions the phase line:

    phi < pi/12   all three roots positive        <- the CHARGED sector, at 2/9
    phi = pi/12   middle root exactly zero
    phi > pi/12   middle root negative            <- the NEUTRAL sector, at 2/9 + pi/12

and the two sectors sit on OPPOSITE SIDES of the crossing, displaced by exactly the
crossing phase. That also explains, rather than merely accommodates, why the neutral
fit needs the (-,+,+) branch: it is on the far side of the crossing by construction.

WHAT IS STILL OWED, HONESTLY. This derives pi/12 from A. It does NOT explain why the
neutral phase should be phi_e + phi_cross rather than any other combination -- that
displacement rule is still an input, and it is now the whole of the remaining debt
for #81. The debt is one relation smaller and sharper than recorded.

PRE-STATED CONTROLS:
  P-A  phi_cross = arccos(-1/A) - 2pi/3 must equal pi/12 to machine precision at
       A = sqrt2, and the middle root must be exactly 0 there.
  P-B  the charged phase 2/9 must sit BELOW the crossing (all roots positive) and the
       neutral phase 2/9 + pi/12 ABOVE it (middle root negative).
  P-C  the crossing must MOVE with A -- otherwise "derived from A" is vacuous and
       pi/12 would be a coincidence of this particular A.
  P-D  ANTI-CONTROL: at A = 1 (no Koide) the crossing must NOT be pi/12; and the
       value pi/12 must be reachable ONLY at A = sqrt2 among sampled amplitudes.
"""

import math

TOL = 1e-12
A_KOIDE = math.sqrt(2.0)
PHI_E = 2 / 9
PI12 = math.pi / 12

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def roots(phi, A=A_KOIDE):
    return [1 + A * math.cos(phi + 2 * math.pi * k / 3) for k in range(3)]


def phi_cross(A):
    """Phase at which the k=1 root vanishes. Defined only for A >= 1."""
    if A < 1:
        return None
    return math.acos(-1.0 / A) - 2 * math.pi / 3


def main():
    print("=" * 78)
    print("  #81 — pi/12 IS THE ROOT ZERO-CROSSING AT THE KOIDE AMPLITUDE")
    print("=" * 78)

    # ---- P-A ---------------------------------------------------------------
    print("\n  P-A  the crossing at A = sqrt2 is exactly pi/12")
    pc = phi_cross(A_KOIDE)
    chk("P-A1 arccos(-1/sqrt2) - 2pi/3 = pi/12", abs(pc - PI12) < TOL,
        f"{pc:.15f} vs {PI12:.15f}   diff {abs(pc-PI12):.2e}")
    chk("P-A2 and it is 3pi/4 - 2pi/3 in closed form",
        abs(pc - (3 * math.pi / 4 - 2 * math.pi / 3)) < TOL,
        "9pi/12 - 8pi/12")
    chk("P-A3 the middle root is exactly zero there",
        abs(roots(PI12)[1]) < 1e-15, f"root = {roots(PI12)[1]:.2e}")

    # ---- P-B ---------------------------------------------------------------
    print("\n  P-B  the two sectors sit on opposite sides of the crossing")
    re_, rn = roots(PHI_E), roots(PHI_E + PI12)
    chk("P-B1 charged phase 2/9 is BELOW the crossing", PHI_E < PI12,
        f"{PHI_E:.6f} < {PI12:.6f}")
    chk("P-B2 ... so all three charged roots are positive", all(r > 0 for r in re_),
        f"{[round(r,6) for r in re_]}  (middle only +{re_[1]:.4f})")
    chk("P-B3 neutral phase 2/9 + pi/12 is ABOVE the crossing", PHI_E + PI12 > PI12)
    chk("P-B4 ... so its middle root is NEGATIVE — the (-,+,+) branch",
        rn[1] < 0, f"{[round(r,6) for r in rn]}")
    print("       -> the branch Brannen's neutral fit requires is not an extra")
    print("          assumption: it follows from sitting past the crossing.")

    # ---- P-C ---------------------------------------------------------------
    print("\n  P-C  the crossing MOVES with A (so 'derived from A' has content)")
    tbl = [(1.0, phi_cross(1.0)), (1.2, phi_cross(1.2)), (A_KOIDE, phi_cross(A_KOIDE)),
           (1.6, phi_cross(1.6)), (2.0, phi_cross(2.0))]
    print(f"\n    {'A':>8} {'phi_cross':>12}")
    for A, p in tbl:
        mark = "   <- Koide, = pi/12" if abs(A - A_KOIDE) < 1e-12 else ""
        print(f"    {A:8.5f} {p:12.8f}{mark}")
    spread = max(p for _a, p in tbl) - min(p for _a, p in tbl)
    chk("P-C1 phi_cross varies appreciably over A", spread > 0.5,
        f"range {spread:.4f} rad")

    # ---- P-D: anti-control -------------------------------------------------
    print("\n  P-D  ANTI-CONTROL: is pi/12 special to A = sqrt2?")
    chk("P-D1 at A = 1 the crossing is NOT pi/12",
        abs(phi_cross(1.0) - PI12) > 0.1,
        f"A=1 gives {phi_cross(1.0):.6f}")
    # Solve phi_cross(A) = pi/12. NB phi_cross DECREASES with A (see the P-C table:
    # 1.047 -> 0.462 -> 0.262 -> 0.152 -> 0.000), so the bisection branch is the
    # reverse of the naive one. The first version had it backwards and converged on
    # the bracket endpoint; the control caught it. Second time tonight for this
    # exact slip -- monotonic direction is worth checking against a table, not assumed.
    lo, hi = 1.0, 2.0                       # phi_cross(1) = pi/3 > pi/12 > phi_cross(2) = 0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if phi_cross(mid) > PI12:
            lo = mid                        # still above target -> need larger A
        else:
            hi = mid
    A_sol = 0.5 * (lo + hi)
    chk("P-D2 the ONLY amplitude giving pi/12 is A = sqrt2",
        abs(A_sol - A_KOIDE) < 1e-9,
        f"solved A = {A_sol:.12f} vs sqrt2 = {A_KOIDE:.12f}")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — A RECORDED DEBT DISSOLVES")
    print("=" * 78)
    print("""
  pi/12 IS NOT AN INDEPENDENT ANGLE. It is arccos(-1/A) - 2pi/3 evaluated at the
  Koide amplitude A = sqrt2, i.e. the phase at which the middle root of the ring
  spectrum crosses zero. Exact, to 1e-16, and A = sqrt2 is the UNIQUE amplitude
  producing it (P-D2).

  SO YESTERDAY'S FRAMING WAS WRONG AND IS WITHDRAWN. #81 recorded "pi/12 is a PURE
  geometric angle carrying no Q, so whatever supplies it is a different KIND of
  object from the one that supplies 2/9." It is the SAME object: A is fixed by
  Koide through A^2 = 6(Q - 1/3), the same invariant that fixes 2/9 through the
  holonomy closure. No second mechanism is required, and none should be sought.

  AND IT EXPLAINS THE SIGN BRANCH RATHER THAN ASSUMING IT. The crossing partitions
  the phase line: below it all three roots are positive (the charged sector, at
  2/9, with its middle root only +0.040 — barely inside); above it the middle root
  is negative (the neutral sector, at 2/9 + pi/12). The (-,+,+) branch that
  Brannen's neutral fit needs is not an extra assumption — it is where you land by
  sitting past the crossing.

  WHAT REMAINS, AND IT IS NOW THE WHOLE OF #81's DEBT: why the neutral phase should
  be phi_e + phi_cross rather than any other combination. That displacement rule is
  still an input. But it is ONE relation between two quantities both already fixed
  by Koide, not a new angle needing a new kind of object.
""")


if __name__ == "__main__":
    main()
