#!/usr/bin/env python3
"""
Does the neutrino triple's Q = 0.585 ceiling survive a NEGATIVE square root?

THE RECORDED CLAIM. PRTOE_koide_relation.md carries a load-bearing exclusion:

    "the neutrino triple cannot sit on the cone for any lightest mass -- Q_nu rises
     monotonically to only 0.585 as m1 -> 0, short of 2/3 by 12.2% -- so whatever
     pins the cone acts in the charged sector specifically"

and that, together with an exactness argument, is used to "condemn every candidate
tried so far as one class". It is doing real work.

THE UNSTATED ASSUMPTION. Koide's ratio is

    Q = (sum m_i) / (sum sqrt(m_i))^2

and the DENOMINATOR depends on the signs chosen for the square roots. The recorded
ceiling is computed with all three roots positive. But the ring parametrisation the
rest of the corpus uses,

    sqrt(m_k) = a + 2|b| cos(phi + 2 pi k / 3),

produces NEGATIVE values of sqrt(m_k) whenever 2|b| > a -- and nothing in it forbids
that, because only m_k = (sqrt m_k)^2 is observable. A negative root makes the
denominator SMALLER and therefore Q LARGER, so the ceiling is not obviously a
ceiling at all. Brannen's neutrino extension turns on exactly this.

WHAT THIS SCRIPT DOES. Recomputes Q_nu over the whole allowed range of the lightest
mass, for BOTH sign branches, using measured oscillation splittings. It then asks
whether the ring form with the charged sector's own A = sqrt2 can reproduce the
measured splitting RATIO, which is the sharper test because that ratio is a pure
number independent of the overall mass scale.

WHAT IT DOES NOT DO. It does not claim the negative branch is physical. It asks
whether the recorded exclusion depends on an assumption that was never stated, which
is a question about the argument rather than about neutrinos.

PRE-STATED CONTROLS:
  N-A  the all-positive branch must reproduce the recorded ceiling 0.585 as m1 -> 0,
       or this script is not measuring the same quantity the corpus measured.
  N-B  Q must be scale-invariant: multiplying all three masses by any factor leaves
       it unchanged. If not, the formula is wrong.
  N-C  the charged-lepton triple must return Q = 2/3 to the accuracy the corpus
       claims (~1e-5), as an end-to-end check of the same code path.
  N-D  the splitting ratio computed from the ring form must be independent of the
       overall scale a, since it is a ratio.
"""

import math

# PDG 2024 / NuFIT, normal ordering. Stated as inputs, not derived here.
DM21 = 7.53e-5          # eV^2
DM31 = 2.453e-3         # eV^2
RATIO_MEAS = DM31 / DM21

# charged leptons, PDG (MeV)
M_E, M_MU, M_TAU = 0.51099895, 105.6583755, 1776.86

TOL = 1e-12
_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def Q_of(masses, signs=(1, 1, 1)):
    """Koide ratio with explicit square-root signs."""
    s = sum(sg * math.sqrt(m) for sg, m in zip(signs, masses))
    if abs(s) < 1e-300:
        return float("nan")
    return sum(masses) / (s * s)


def nu_masses(m1):
    """Normal ordering: m1 free, m2 and m3 fixed by the measured splittings."""
    return (m1, math.sqrt(m1 * m1 + DM21), math.sqrt(m1 * m1 + DM31))


def main():
    print("=" * 78)
    print("  NEUTRINO Q — DOES THE 0.585 CEILING SURVIVE A NEGATIVE ROOT?")
    print("=" * 78)
    print(f"\n  inputs: dm21 = {DM21:.4g} eV^2, dm31 = {DM31:.4g} eV^2,"
          f" ratio = {RATIO_MEAS:.3f}")

    # ---- N-C: end-to-end check on the charged leptons ---------------------
    print("\n  N-C  the same code path returns Q = 2/3 for the charged leptons")
    qc = Q_of((M_E, M_MU, M_TAU))
    chk("N-C1 charged-lepton Q = 2/3 to ~1e-5", abs(qc - 2 / 3) < 2e-5,
        f"Q = {qc:.9f}, deviation {abs(qc-2/3):.2e}")

    # ---- N-B: scale invariance --------------------------------------------
    print("\n  N-B  Q is scale-invariant")
    q1 = Q_of((1.0, 4.0, 9.0))
    q2 = Q_of((1.0e6, 4.0e6, 9.0e6))
    chk("N-B1 Q unchanged under a common rescaling", abs(q1 - q2) < 1e-12,
        f"{q1:.12f} vs {q2:.12f}")

    # ---- N-A: reproduce the recorded ceiling ------------------------------
    print("\n  N-A  the all-positive branch reproduces the recorded 0.585 ceiling")
    print(f"\n    {'m1 (eV)':>12} {'Q (+++)':>12} {'Q (+-+)':>12} {'Q (-++)':>12}")
    rows = []
    for m1 in (0.0, 1e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1):
        ms = nu_masses(m1)
        qp = Q_of(ms, (1, 1, 1))
        qm = Q_of(ms, (1, -1, 1))
        qn = Q_of(ms, (-1, 1, 1))
        rows.append((m1, qp, qm, qn))
        print(f"    {m1:12.5g} {qp:12.6f} {qm:12.6f} {qn:12.6f}")
    q_at_zero = rows[0][1]
    chk("N-A1 all-positive Q -> 0.585 as m1 -> 0", abs(q_at_zero - 0.585) < 0.002,
        f"Q(m1=0) = {q_at_zero:.6f}  (corpus records 0.585)")
    mono = all(rows[i][1] >= rows[i + 1][1] - 1e-9 for i in range(len(rows) - 1))
    chk("N-A2 and it is monotonic downward in m1, as recorded", mono,
        "so 0.585 is the ceiling ON THAT BRANCH")

    # ---- the sign branches ------------------------------------------------
    print("\n  THE SIGN BRANCHES")
    hit = []
    for sgn, lbl in (((1, -1, 1), "(+,-,+)"), ((-1, 1, 1), "(-,+,+)"),
                     ((1, 1, -1), "(+,+,-)")):
        # scan m1 for a crossing of 2/3
        prev = None
        found = None
        for i in range(2001):
            m1 = i * 1e-4
            q = Q_of(nu_masses(m1), sgn)
            if prev is not None and (prev - 2 / 3) * (q - 2 / 3) < 0:
                found = m1
                break
            prev = q
        hit.append((lbl, found))
        if found is not None:
            print(f"    branch {lbl}: crosses Q = 2/3 at m1 ~ {found:.5f} eV")
        else:
            print(f"    branch {lbl}: never reaches Q = 2/3 in m1 < 0.2 eV")

    reachable = [l for l, f in hit if f is not None]

    # ---- the sharper test: the splitting ratio ----------------------------
    print("\n  THE SHARPER TEST — the splitting RATIO is scale-free")
    print("  Ring form sqrt(m_k) = a[1 + A cos(phi + 2 pi k/3)], A = sqrt2 (the charged")
    print("  sector's own value). The dm31/dm21 ratio then depends on phi alone.")

    def ratio_of(phi, A=math.sqrt(2.0), a=1.0):
        # r_k are the SQUARE ROOTS of the masses, so the masses are r_k^2 and the
        # SQUARED-mass splittings that oscillation experiments measure are
        # m_j^2 - m_i^2 = r_j^4 - r_i^4. The first version of this function
        # returned r_j^2 - r_i^2, i.e. a difference of MASSES called dm^2 -- the
        # proxy-is-not-the-quantity error of protocol 42, committed here in new
        # code while the same trap was being written up elsewhere. Caught because a
        # hand-computed cross-check disagreed with it.
        r = [a * (1 + A * math.cos(phi + 2 * math.pi * k / 3)) for k in range(3)]
        m = sorted(x * x for x in r)              # masses
        d21 = m[1] ** 2 - m[0] ** 2               # squared-mass splittings
        d31 = m[2] ** 2 - m[0] ** 2
        return d31 / d21 if d21 else float("nan")

    chk("N-D1 the ratio is independent of the scale a",
        abs(ratio_of(0.4, a=1.0) - ratio_of(0.4, a=97.3)) < 1e-9,
        f"{ratio_of(0.4, a=1.0):.6f} vs {ratio_of(0.4, a=97.3):.6f}")

    print(f"\n    measured dm31/dm21 = {RATIO_MEAS:.3f}")
    print(f"    {'phi':>22} {'ratio':>12} {'off by':>10}")
    for phi, lbl in ((2 / 9, "2/9 (charged sector)"),
                     (2 / 9 + math.pi / 12, "2/9 + pi/12"),
                     (2 / 9 - math.pi / 12, "2/9 - pi/12"),
                     (math.pi / 12, "pi/12")):
        r = ratio_of(phi)
        print(f"    {lbl:>22} {r:12.3f} {100*(r-RATIO_MEAS)/RATIO_MEAS:9.1f}%")

    # best-fit phi
    best, bphi = None, None
    for i in range(400001):
        phi = i * math.pi / 3 / 400000
        r = ratio_of(phi)
        if r == r and r > 0:
            d = abs(r - RATIO_MEAS)
            if best is None or d < best:
                best, bphi = d, phi
    print(f"\n    best-fit phi over [0, pi/3): {bphi:.6f}  -> ratio {ratio_of(bphi):.3f}"
          f"  (measured {RATIO_MEAS:.3f})")
    print(f"    compare 2/9 + pi/12 = {2/9 + math.pi/12:.6f}"
          f"   difference {abs(bphi - (2/9 + math.pi/12)):.6f}")

    # ---- the absolute scale, which oscillations alone cannot give ----------
    print("\n  THE ABSOLUTE MASS SCALE — fixed once the phase is")
    print("  With A and phi both fixed, the three masses are determined up to ONE")
    print("  overall scale, and dm21 sets that scale. So sum(m_nu) is a PREDICTION.")
    phi_b = 2 / 9 + math.pi / 12
    r = [1 + math.sqrt(2.0) * math.cos(phi_b + 2 * math.pi * k / 3) for k in range(3)]
    m_rel = sorted(x * x for x in r)
    d21_rel = m_rel[1] ** 2 - m_rel[0] ** 2
    scale = math.sqrt(DM21 / d21_rel)          # eV per unit of m_rel
    m_abs = [m * scale for m in m_rel]
    print(f"\n    square roots  : {[round(x, 6) for x in r]}")
    print(f"      (note the NEGATIVE root -- this is the (-,+,+) sign branch)")
    print(f"    m1 = {m_abs[0]:.6g} eV")
    print(f"    m2 = {m_abs[1]:.6g} eV")
    print(f"    m3 = {m_abs[2]:.6g} eV")
    print(f"    SUM m_nu = {sum(m_abs):.5f} eV")
    d31_pred = (m_abs[2] ** 2 - m_abs[0] ** 2)
    print(f"\n    check: dm21 = {(m_abs[1]**2 - m_abs[0]**2):.4g} eV^2 "
          f"(input {DM21:.4g})")
    print(f"           dm31 = {d31_pred:.4g} eV^2 (measured {DM31:.4g}, "
          f"off {100*(d31_pred-DM31)/DM31:+.1f}%)")
    print(f"\n    Cosmological bound on sum(m_nu) is ~0.12 eV (Planck+BAO); this")
    print(f"    prediction sits at {sum(m_abs):.3f} eV, i.e. COMFORTABLY BELOW it and")
    print(f"    within reach of the model's own m_ncdm posterior.")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  WHAT THIS SETTLES, AND WHAT IT DOES NOT")
    print("=" * 78)
    print(f"""
  THE RECORDED CEILING IS REAL, BUT IT IS BRANCH-SPECIFIC. With all three square
  roots positive, Q_nu does rise monotonically to {q_at_zero:.3f} as m1 -> 0 and never
  reaches 2/3 -- the corpus's number is reproduced exactly (N-A). What was never
  stated is that this is a statement about ONE SIGN BRANCH.

  Allowing a negative root -- which the ring parametrisation produces on its own
  whenever 2|b| > a, and which is unobservable since only m = (sqrt m)^2 enters --
  changes the denominator and therefore Q. Branches reaching 2/3: {reachable if reachable else 'none'}.

  SO THE EXCLUSION NEEDS ITS ASSUMPTION STATED. "The neutrino triple cannot sit on
  the cone for any lightest mass" is true only for the all-positive branch. Whether
  the negative branch is PHYSICALLY admissible is a separate question this script
  does not settle -- but the argument as written does not address it, and it is
  used to condemn a whole class of mechanisms.

  ON THE SPLITTING RATIO, which is the scale-free test. The measured
  dm31/dm21 = {RATIO_MEAS:.1f} is emphatically NOT reproduced by the charged sector's own
  phase 2/9, which gives 283 -- off by 768%. So the neutrinos do not share the
  charged phase, and any claim that they do has to confront that number.

  BUT A SHIFT OF pi/12 REPRODUCES IT TO 0.5%. phi = 2/9 + pi/12 gives 32.43 against
  the measured 32.58, and the free best fit over [0, pi/3) lands at 0.483376 against
  2/9 + pi/12 = 0.484022 -- a difference of 0.00065, i.e. 0.13%. THIS IS BRANNEN'S
  PUBLISHED NEUTRINO EXTENSION (2006) AND IS NOT NEW HERE; it is recorded because
  the corpus did not carry it and because it bears directly on the exclusion above.

  THE TWO RESULTS LOCK TOGETHER, WHICH IS THE PART WORTH NOTICING. That fit needs a
  NEGATIVE square root (the roots come out 2.2518, -0.1958, 0.9440), i.e. it lives on
  the (-,+,+) branch -- the same branch that crosses Q = 2/3, and it crosses at
  m1 ~ 0.00040 eV while this configuration independently predicts m1 = 0.000374 eV.
  Two different routes to the same sign branch and the same lightest mass.

  AND IT PREDICTS THE ABSOLUTE SCALE, which oscillations alone cannot give:
  sum(m_nu) = 0.0585 eV, normal ordering, essentially the minimal NO value. That is
  comfortably below the ~0.12 eV cosmological bound and inside the range the model's
  own m_ncdm posterior can speak to.

  WHAT IS NOW OWED. The pi/12 itself. The charged sector's phase is 2/9 = Q/3 via the
  holonomy closure; nothing yet says why the neutral triple should sit a further
  pi/12 around the ring. That is a new, sharply posed debt -- and note pi/12 is a
  PURE geometric angle with no Q in it, so whatever supplies it is a different kind
  of object from the one that supplies 2/9.

  A NEAR-MISS, CHECKED AND DELIBERATELY NOT CHASED. Multiplying through by three,

      3 * arg b_nu = 3*(2/9 + pi/12) = Q + pi/4      (exact, difference 0.0)

  and PRTOE_koide_relation.md separately records a Lorentzian metric on family space
  "whose light cone opens at exactly 45 degrees about the democratic direction". It
  is tempting to read the neutral triple's holonomy as the charged one displaced by
  the cone's opening angle.

  DO NOT. The identity is trivial arithmetic -- 3 * pi/12 = pi/4 -- so "shifted by
  pi/12 in phi" and "shifted by pi/4 in 3 phi" are the same sentence, and no content
  is added by writing it the second way. The only real claim would be that THIS pi/4
  is THAT cone angle, and there is no argument for it: the holonomy is an angle in
  the family PHASE, while the cone angle is an aperture of a metric on family
  SPACE. Different spaces, coincident numbers. Recorded here so the coincidence is
  not rediscovered later and mistaken for a mechanism -- the same discipline the
  delivery-law discriminator applied when it noted 3.119 is not pi.
""")
    print("=" * 78)


if __name__ == "__main__":
    main()
