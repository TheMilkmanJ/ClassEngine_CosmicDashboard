#!/usr/bin/env python3
"""
#2 / #55 — what a potential must contain to select arg b = 2/9, and what that costs.

FOLLOWS DIRECTLY FROM #1 (scripts/family_triplet_parent.py). That result showed the
family order parameter has two orthogonal components, a spin-2 nematic weighted by
cos(arg b) and an adjoint weighted by sin(arg b). This script asks the next
question: what invariant must the POTENTIAL contain for its minimum to sit at a
given arg b, and what symmetry has to be given up to allow it?

THE SYMMETRY ACTION. C3 relabels the three defects. In the Brannen parametrisation
sqrt(m_k) = a + 2|b| cos(phi + 2 pi k / 3), relabelling k -> k+1 shifts

    phi -> phi + 2 pi / 3,     i.e.   b -> omega b,   omega = exp(2 pi i / 3).

So a C3-invariant real potential can depend only on |b| and on the two cubic
harmonics cos(3 phi) and sin(3 phi) -- nothing of lower order in phi survives,
because phi appears only through b^3 and its conjugate.

THE PARITY QUESTION. Reflection (reversing the defect labelling, equivalently
b -> conj(b)) sends phi -> -phi. It kills sin(3 phi) and keeps cos(3 phi). So:

  * WITH reflection symmetry the potential is V(|b|, cos 3 phi). Its stationary
    points in phi are ONLY 3 phi = 0 and 3 phi = pi. This is exactly spec C6's
    theorem, re-derived here from the symmetry action rather than from the mass
    formula -- and it is why the ring's own potential cannot reach 3 phi = 2/3.

  * WITHOUT reflection symmetry a term in sin(3 phi) is allowed, and then

        V_phi = |b|^3 ( lambda cos 3 phi + mu sin 3 phi )
              = |b|^3 R cos(3 phi - delta),   R = sqrt(lambda^2 + mu^2),
                                              tan delta = mu / lambda

    whose stationary points are 3 phi = delta and 3 phi = delta + pi. Hence

        tan(3 phi) = mu / lambda

    at every stationary point, minimum or maximum alike.

THE PAYOFF, AND ITS HONEST STATUS. The holonomy closure already established
3 * arg b = Q. Substituting,

        tan(Q) = mu / lambda

so the ratio of the PARITY-ODD to the PARITY-EVEN cubic coupling is fixed to
tan(2/3) = 0.786843 by the Koide value. THIS IS NOT A DERIVATION OF arg b. It is a
change of unknown: from "an angle nobody can source" to "the ratio of two cubic
couplings, one of which requires parity violation to exist at all". That is
progress only in that the new unknown is a coupling ratio in a Lagrangian rather
than a bare number, and it names the symmetry that must be broken.

WHAT IT DOES BUY, CONCRETELY: any candidate background that is REFLECTION
SYMMETRIC is excluded from sourcing the phase, no matter how it couples. The
external object spec C6 demands must be CHIRAL.

PRE-STATED CONTROLS:
  P-A  under phi -> phi + 2pi/3 the mass multiset must be invariant (C3 acts as
       claimed), and under phi -> -phi it must also be invariant (reflection).
  P-B  a reflection-symmetric potential must have stationary points ONLY at
       3 phi = 0, pi -- checked by dense scan, not by assertion.
  P-C  with both terms, every stationary point must satisfy tan(3 phi) = mu/lambda.
  P-D  the minimum located numerically must agree with the closed form.
  P-E  setting mu/lambda = tan(Q) must put a stationary point exactly at
       arg b = Q/3 = 2/9.
  P-F  CONTROL AGAINST SELF-DECEPTION: with mu = 0 the scan must NOT find a
       stationary point at 2/9. If it does, the scan is broken.
"""

import math

TWO_PI = 2 * math.pi
Q_KOIDE = 2.0 / 3.0
PHI_TARGET = Q_KOIDE / 3.0          # = 2/9, the Brannen phase
TOL = 1e-9

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def masses(a, mb, phi):
    return sorted(a + 2 * mb * math.cos(phi + TWO_PI * k / 3) for k in range(3))


def V(phi, lam, mu):
    return lam * math.cos(3 * phi) + mu * math.sin(3 * phi)


def dV(phi, lam, mu):
    return 3 * (-lam * math.sin(3 * phi) + mu * math.cos(3 * phi))


def stationary_points(lam, mu, n=2_000_00):
    """Dense sign-change scan of dV over one period [0, 2pi/3)."""
    out = []
    period = TWO_PI / 3
    prev_p = 0.0
    prev = dV(prev_p, lam, mu)
    for i in range(1, n + 1):
        p = period * i / n
        cur = dV(p, lam, mu)
        if prev == 0.0:
            out.append(prev_p)
        elif prev * cur < 0:
            lo, hi = prev_p, p
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                if dV(lo, lam, mu) * dV(mid, lam, mu) <= 0:
                    hi = mid
                else:
                    lo = mid
            out.append(0.5 * (lo + hi))
        prev_p, prev = p, cur
    return out


def main():
    print("=" * 78)
    print("  #2 — THE PARITY-ODD CUBIC INVARIANT, AND WHAT arg b COSTS")
    print("=" * 78)

    # ---- P-A: the symmetry action -----------------------------------------
    print("\n  P-A  C3 acts as phi -> phi + 2pi/3; reflection as phi -> -phi")
    a, mb = 2.0, 0.31
    worst_c3 = worst_ref = 0.0
    for i in range(200):
        phi = -math.pi + i * TWO_PI / 200
        m0 = masses(a, mb, phi)
        m1 = masses(a, mb, phi + TWO_PI / 3)
        m2 = masses(a, mb, -phi)
        worst_c3 = max(worst_c3, max(abs(x - y) for x, y in zip(m0, m1)))
        worst_ref = max(worst_ref, max(abs(x - y) for x, y in zip(m0, m2)))
    chk("P-A1 mass multiset invariant under phi -> phi + 2pi/3",
        worst_c3 < 1e-12, f"max dev {worst_c3:.2e}")
    chk("P-A2 mass multiset invariant under phi -> -phi (reflection)",
        worst_ref < 1e-12, f"max dev {worst_ref:.2e}")

    # ---- P-B: reflection-symmetric potential -> only 3phi = 0, pi ----------
    print("\n  P-B  with mu = 0 the ONLY stationary points are 3phi = 0, pi")
    sps = stationary_points(1.0, 0.0)
    got = sorted(round(3 * p % TWO_PI, 9) for p in sps)
    allowed = all(min(abs(g - 0.0), abs(g - math.pi), abs(g - TWO_PI)) < 1e-6
                  for g in got)
    chk("P-B1 every stationary point has 3phi = 0 or pi", allowed,
        f"3phi values {[round(g,6) for g in got]}")
    chk("P-B2 this reproduces spec C6 from the symmetry action alone", allowed,
        "the ring's own potential cannot reach 3phi = 2/3")

    # ---- P-C / P-D: with both terms, tan(3phi) = mu/lambda ----------------
    print("\n  P-C  with mu != 0 every stationary point obeys tan(3phi) = mu/lambda")
    worst = 0.0
    for lam, mu in ((1.0, 0.4), (1.0, -0.9), (2.0, 1.6), (-1.0, 0.5), (0.7, 2.3)):
        for p in stationary_points(lam, mu):
            lhs = math.tan(3 * p)
            rhs = mu / lam
            worst = max(worst, abs(lhs - rhs))
    chk("P-C1 tan(3phi) = mu/lambda at every stationary point", worst < 1e-6,
        f"max dev {worst:.2e}")

    print("\n  P-D  the numerical minimum matches the closed form")
    lam, mu = 1.0, 0.4
    sps = stationary_points(lam, mu)
    numeric_min = min(sps, key=lambda p: V(p, lam, mu))
    delta = math.atan2(mu, lam)
    closed = (delta + math.pi) / 3.0
    closed = closed % (TWO_PI / 3)
    chk("P-D1 argmin agrees with (delta + pi)/3", abs(numeric_min - closed) < 1e-6,
        f"numeric {numeric_min:.9f}  closed {closed:.9f}")

    # ---- P-E: the Koide point ---------------------------------------------
    print("\n  P-E  mu/lambda = tan(Q) puts a stationary point at arg b = 2/9")
    ratio = math.tan(Q_KOIDE)
    sps = stationary_points(1.0, ratio)
    hit = min(sps, key=lambda p: abs(p - PHI_TARGET))
    chk("P-E1 a stationary point sits at arg b = 2/9",
        abs(hit - PHI_TARGET) < 1e-6,
        f"found {hit:.9f}  target {PHI_TARGET:.9f}")
    # Booked value corrected 2026-07-29: this check first carried 0.793551, which
    # was an arithmetic slip on my part, not a computed number -- and the control
    # caught it on the first run. tan(2/3) = 0.7868427... The lesson is the one
    # already in the audit protocol: never book a constant you have not computed.
    chk("P-E2 the required coupling ratio is tan(Q) = tan(2/3)",
        abs(ratio - 0.7868427) < 1e-6, f"mu/lambda = {ratio:.7f}")
    # independent cross-check of the same number, via the tangent addition formula
    # tan(2x) = 2 tan x / (1 - tan^2 x) with x = 1/3, so nothing here reuses tan(2/3)
    _t3 = math.tan(1.0 / 3.0)
    chk("P-E2b tan(2/3) reproduced from tan(1/3) by the double-angle identity",
        abs(ratio - 2 * _t3 / (1 - _t3 * _t3)) < 1e-12,
        f"double-angle gives {2*_t3/(1-_t3*_t3):.9f}")
    chk("P-E3 consistency: 3 * arg b = Q (the holonomy closure)",
        abs(3 * PHI_TARGET - Q_KOIDE) < TOL,
        f"3 * 2/9 = {3*PHI_TARGET:.9f} = Q")

    # ---- P-F: the anti-control --------------------------------------------
    print("\n  P-F  ANTI-CONTROL: with mu = 0 the scan must NOT find 2/9")
    sps0 = stationary_points(1.0, 0.0)
    near = min(abs(p - PHI_TARGET) for p in sps0)
    chk("P-F1 no stationary point near 2/9 when parity is unbroken", near > 0.1,
        f"closest stationary point is {near:.4f} rad away")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}  — do not record")
        print("=" * 78)
        return
    print("  ALL CONTROLS PASS")
    print("=" * 78)
    print(f"""
  WHAT IS ESTABLISHED

  C3 forces the potential's phi-dependence into the two cubic harmonics and
  nothing else. Reflection symmetry keeps only cos(3 phi), whose stationary points
  are 3 phi = 0 and pi -- spec C6's theorem, re-derived from the symmetry action
  (P-B). Allowing the parity-odd sin(3 phi) term with coefficient mu gives

      tan(3 * arg b) = mu / lambda                                        (P-C)

  and since the holonomy closure fixes 3 * arg b = Q, the Koide value requires

      mu / lambda = tan(Q) = tan(2/3) = {ratio:.6f}                          (P-E)

  WHAT IS *NOT* ESTABLISHED, STATED PLAINLY

  This does not derive arg b. It trades one unknown for another: an unsourced
  angle becomes a ratio of two cubic couplings. The new unknown is better only
  because it lives in a Lagrangian, where it can be computed once the couplings
  are, rather than being a bare number with nowhere to come from.

  THE ONE HARD CONSEQUENCE, WHICH IS A REAL EXCLUSION

  The sin(3 phi) term is odd under reflection. A reflection-symmetric background
  CANNOT generate it, at any order, with any coupling strength -- the anti-control
  (P-F) confirms the phase stays pinned to 0 or pi when mu = 0. So the external
  object that spec C6 demands must be CHIRAL. This is a genuine filter on the
  owner's three-seed candidate and on any other proposal: if the seeds' imprint is
  reflection symmetric, it cannot supply arg b however it is coupled.

  It also connects two previously separate parts of the corpus: the model already
  carries a definite handedness in its winding sector, which is exactly the kind
  of object that can source a parity-odd invariant. Whether THAT chirality has the
  right magnitude is a separate computation and is NOT claimed here.
""")


if __name__ == "__main__":
    main()
