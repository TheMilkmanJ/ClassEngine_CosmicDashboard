#!/usr/bin/env python3
"""
#2 — I graded this morning's Y-junction work against a RETRACTED input, and used a
SUPERSEDED energy functional. Both corrections here, and the docket's real state.

WHAT I DID THIS MORNING (scripts/y_junction_ck_from_alpha.py). Minimised a two-term
functional E(d) = sqrt3 sigma d + 3 q^2/d, got c_K = 3^(1/4) q, converted the target
into q^2 = 2.136318, and reported that "the recorded alpha_dark ~ 3.2 does not
reproduce in any convention". I then recorded that as #2's blocking item.

BOTH HALVES OF THAT ARE WRONG, AND THE CORPUS SAYS SO ALREADY.

  (1) alpha_dark ~ 3.2 WAS RETRACTED ON 2026-07-18, eleven days earlier. T6:
      "the repulsive-balance alpha_dark ~ 3.2 consistency line is RETRACTED -- wrong
      sign in the gauge channel". I graded a live docket against a dead number. This
      is the re-grade rule in its purest form: I checked the number and not its status.

  (2) The two-term functional is the retracted one. The exact colour algebra forces
      the gauge channel ATTRACTIVE, so "+3q^2/d" has the wrong sign. The live
      functional is three-term, with the repulsion coming from the MEDIUM as a vortex
      log rather than from the gauge sector as a Coulomb term:

          E(d) = sqrt3 sigma d  -  3 qt^2 ln d  -  3 alpha_d / d

THE COLOUR ALGEBRA, WHICH IS WHAT DECIDES THE SIGN. Three adjoints contracted into the
epsilon^abc singlet satisfy sum_i T_i = 0. Squaring, 3 C_2(adj) + 6 (T_i . T_j) = 0, so
for SU(2) where C_2(adj) = 2,

    T_i . T_j = -1        ATTRACTIVE, exactly.

So a pure-gauge ring cannot exist: string tension and singlet-channel Coulomb both pull
inward and the configuration collapses. A pure-medium ring has no tie to sqrt(sigma).
Only the hybrid equilibrates -- the corpus's "forced combination" theorem.

WHAT THE LIVE CHAIN ACTUALLY DEMANDS. At the target c_K = d sqrt(sigma) = 4/(3 ln 2),
the equilibrium condition in the pure-medium limit gives

    qt^2 / sqrt(sigma) = c_K / sqrt3 = 1.110586

and with the vortex convention qt^2 = 2 pi F^2 t at t sqrt(sigma) = 1 this converts to

    F_dark / sqrt(sigma) = 0.420428

which is the corpus's recorded 0.4204. So the chain does NOT dangle on an unfixed
convention -- the convention is pinned, the demand is exact, and the referee is a
lattice campaign (SU(2), N_f = 3) that must deliver T_c/sqrt(sigma), F_pi/sqrt(sigma)
and w sqrt(sigma) together.

  *** #2 IS NOT BLOCKED ON alpha_dark'S CONVENTION. It is blocked on external compute,
  *** and it has been in that state since 2026-07-18.

PRE-STATED CONTROLS:
  Y-A  the colour algebra must give T_i . T_j = -1 for SU(2) adjoints in the singlet,
       derived from sum T_i = 0 rather than quoted.
  Y-B  a pure-gauge ring must have NO equilibrium -- the derivative must be one-signed.
  Y-C  a pure-medium ring must have no equilibrium either, so the hybrid is forced.
  Y-D  the three-term functional's minimum must reproduce qt^2/sqrt(sigma) = 1.110586
       at the target, and ~1.6 at alpha_d = 1 -- both recorded numbers.
  Y-E  the stability window on alpha_d must be computed, not quoted.
  Y-F  the vortex convention must reproduce F_dark/sqrt(sigma) = 0.4204 exactly, and
       the recorded band 0.40-0.47 from w sqrt(sigma) in [0.8, 1.1].
  Y-G  ANTI-CONTROL: this morning's two-term functional must be shown to give a
       DIFFERENT answer, so the two are not a reparametrisation of each other.
  Y-H  ANTI-CONTROL: the minimum must be a genuine minimum (second derivative > 0) at
       the target, or the equilibrium is spurious.
"""

import math

TOL = 1e-12
C_K = 4.0 / (3.0 * math.log(2.0))          # 1.923593
SIGMA = 1.0                                 # units with sqrt(sigma) = 1
ROOT3 = math.sqrt(3.0)

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def dE_hybrid(d, qt2, alpha_d):
    """d/dd of  sqrt3 sigma d - 3 qt^2 ln d - 3 alpha_d / d"""
    return ROOT3 * SIGMA - 3.0 * qt2 / d + 3.0 * alpha_d / (d * d)


def d2E_hybrid(d, qt2, alpha_d):
    return 3.0 * qt2 / (d * d) - 6.0 * alpha_d / (d ** 3)


def main():
    print("=" * 78)
    print("  #2 — THE CORRECTED Y-JUNCTION FUNCTIONAL, AND A RETRACTED INPUT")
    print("=" * 78)
    print(f"\n  target  c_K = 4/(3 ln2) = {C_K:.9f}   (units: sqrt(sigma) = 1, so d = c_K)")

    # ---- Y-A ----------------------------------------------------------------
    print("\n  Y-A  the colour algebra fixes the gauge channel's SIGN")
    C2_adj = 2.0                              # SU(2) adjoint Casimir
    # sum_i T_i = 0  =>  3 C2 + 6 (T_i . T_j) = 0
    TiTj = -3.0 * C2_adj / 6.0
    chk("Y-A1 three SU(2) adjoints in the singlet give T_i . T_j = -1",
        abs(TiTj + 1.0) < TOL, f"{TiTj:+.6f} — ATTRACTIVE, from sum T_i = 0")
    chk("Y-A2 so a repulsive gauge Coulomb term has the wrong sign", TiTj < 0,
        "this is what retracted alpha_dark ~ 3.2 on 2026-07-18")

    # ---- Y-B ----------------------------------------------------------------
    print("\n  Y-B  a PURE-GAUGE ring: E = sqrt3 sigma d - 3 alpha_d/d")
    # dE/dd = sqrt3 sigma + 3 alpha_d/d^2 > 0 always
    slopes = [ROOT3 * SIGMA + 3.0 * 1.0 / (d * d) for d in (0.1, 1.0, 5.0, 50.0)]
    chk("Y-B1 the derivative is positive at every spacing", all(s > 0 for s in slopes),
        "monotonic — the minimum is at d = 0, i.e. COLLAPSE, no equilibrium")

    # ---- Y-C ----------------------------------------------------------------
    print("\n  Y-C  a PURE-MEDIUM ring: no tension term, E = -3 qt^2 ln d")
    slopes_m = [-3.0 * 1.0 / d for d in (0.1, 1.0, 5.0, 50.0)]
    chk("Y-C1 the derivative is negative at every spacing", all(s < 0 for s in slopes_m),
        "monotonic the other way — d -> infinity, no scale tie to sqrt(sigma)")
    chk("Y-C2 so ONLY the hybrid equilibrates — the forced-combination theorem", True,
        "gauge alone collapses, medium alone disperses")

    # ---- Y-D ----------------------------------------------------------------
    print("\n  Y-D  the hybrid's equilibrium at the target spacing")
    print(f"\n    {'alpha_d':>9} {'qt^2/sqrt(sigma)':>18} {'recorded':>12}")
    ok_d = True
    for a_d, rec in ((0.0, 1.1105872), (1.0, 1.6304475)):
        # solve dE/dd = 0 at d = C_K for qt^2
        qt2 = (ROOT3 * SIGMA * C_K * C_K + 3.0 * a_d) / (3.0 * C_K)
        good = abs(qt2 - rec) < 1e-5
        ok_d &= good
        print(f"    {a_d:9.1f} {qt2:18.9f} {rec:12.6f}  {'' if good else '<-- MISMATCH'}")
    chk("Y-D1 pure limit gives qt^2/sqrt(sigma) = c_K/sqrt3 = 1.1105872",
        abs((ROOT3 * C_K * C_K) / (3.0 * C_K) - C_K / ROOT3) < TOL
        and abs(C_K / ROOT3 - 1.1105872) < 1e-6, f"{C_K/ROOT3:.9f}")
    chk("Y-D2 and ~1.63 at alpha_d = 1, matching the recorded '~1.6'", ok_d)

    # ---- Y-E ----------------------------------------------------------------
    print("\n  Y-E  the stability window on alpha_d, computed")
    # minimum requires d2E/dd2 > 0 at d = C_K, with qt^2 fixed by equilibrium there
    lo, hi = 0.0, 100.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        qt2 = (ROOT3 * SIGMA * C_K * C_K + 3.0 * mid) / (3.0 * C_K)
        if d2E_hybrid(C_K, qt2, mid) > 0:
            lo = mid
        else:
            hi = mid
    a_max = 0.5 * (lo + hi)
    exact = C_K * C_K / ROOT3
    chk("Y-E1 the equilibrium is a minimum only for alpha_d below", abs(a_max - exact) < 1e-6,
        f"alpha_d < {a_max:.6f}  (closed form c_K^2/sqrt3 = {exact:.6f})")
    chk("Y-E2 consistent with the corpus's recorded 'alpha_d <~ 2.2'",
        2.0 < a_max < 2.3,
        f"exact value is {a_max:.4f}; the recorded 2.2 is the rounded statement")

    # ---- Y-F ----------------------------------------------------------------
    print("\n  Y-F  the vortex convention: qt^2 = 2 pi F^2 t")
    qt2_target = C_K / ROOT3
    F_over_rootsigma = math.sqrt(qt2_target / (2.0 * math.pi))
    chk("Y-F1 at t sqrt(sigma) = 1 the demand is F_dark/sqrt(sigma) = 0.4204",
        abs(F_over_rootsigma - 0.4204) < 5e-5, f"{F_over_rootsigma:.6f}")
    print(f"\n    {'w sqrt(sigma)':>14} {'F_dark/sqrt(sigma)':>20}")
    band = []
    for w in (0.8, 1.1):
        F = math.sqrt(qt2_target / (2.0 * math.pi * w))
        band.append(F)
        print(f"    {w:14.2f} {F:20.6f}")
    chk("Y-F2 the flux-tube width band gives 0.40-0.47, as recorded",
        abs(min(band) - 0.401) < 2e-3 and abs(max(band) - 0.470) < 2e-3,
        f"[{min(band):.4f}, {max(band):.4f}]")

    # ---- Y-G: anti-control --------------------------------------------------
    print("\n  Y-G  ANTI-CONTROL: is this morning's functional a reparametrisation?")
    # two-term: E = sqrt3 sigma d + 3 q^2/d  =>  d = 3^(1/4) q / sqrt(sigma)
    q2_two_term = (C_K / (3.0 ** 0.25)) ** 2
    chk("Y-G1 the two-term functional gives q^2 = 2.136318", abs(q2_two_term - 2.136318) < 1e-5,
        f"{q2_two_term:.6f} — this morning's number, reproduced")
    chk("Y-G2 which is NOT the three-term functional's 1.110586",
        abs(q2_two_term - qt2_target) > 0.5,
        f"{q2_two_term:.6f} vs {qt2_target:.6f} — a factor {q2_two_term/qt2_target:.4f}")
    chk("Y-G3 so they are different physics, not different variables",
        abs(q2_two_term / qt2_target - C_K) < 1e-9,
        f"the ratio is EXACTLY c_K = {C_K:.6f}, since c_K^2/sqrt3 over c_K/sqrt3 = c_K")
    # and a number that will look like a coincidence: the two-term q^2 and the stability
    # ceiling on alpha_d are the SAME expression, c_K^2/sqrt3. Not a second fact.
    chk("Y-G4 this morning's 2.136318 IS the stability ceiling c_K^2/sqrt3, not a coincidence",
        abs(q2_two_term - a_max) < 1e-6,
        f"{q2_two_term:.6f} = {a_max:.6f} — same expression reached two ways; "
        "recorded so it is not chased as a discovery")

    # ---- Y-H: anti-control --------------------------------------------------
    print("\n  Y-H  ANTI-CONTROL: is the equilibrium a genuine minimum?")
    qt2 = C_K / ROOT3
    d2 = d2E_hybrid(C_K, qt2, 0.0)
    chk("Y-H1 second derivative positive at the target, in the pure limit", d2 > 0,
        f"d2E/dd2 = {d2:+.6f}")
    chk("Y-H2 and the first derivative vanishes there", abs(dE_hybrid(C_K, qt2, 0.0)) < 1e-12,
        f"dE/dd = {dE_hybrid(C_K, qt2, 0.0):+.3e}")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THIS MORNING'S #2 FINDING IS WITHDRAWN; THE DOCKET IS ELSEWHERE")
    print("=" * 78)
    print("""
  WITHDRAWN, TWICE OVER. This morning I minimised a two-term functional with a
  REPULSIVE gauge Coulomb term, obtained c_K = 3^(1/4) q and q^2 = 2.136318, and
  reported that the recorded alpha_dark ~ 3.2 "does not reproduce in any convention",
  recording that as #2's blocking item.

  (1) THE NUMBER WAS ALREADY DEAD. alpha_dark ~ 3.2 was retracted on 2026-07-18 --
  "wrong sign in the gauge channel" -- eleven days before I graded against it. I
  checked the number and not its status, which is exactly the failure the re-grade
  rule exists for.

  (2) THE FUNCTIONAL WAS THE RETRACTED ONE. The exact colour algebra settles the sign:
  three SU(2) adjoints in the epsilon^abc singlet satisfy sum T_i = 0, hence
  T_i . T_j = -1, ATTRACTIVE (Y-A). So a repulsive gauge Coulomb term cannot appear.
  A pure-gauge ring collapses (derivative one-signed, Y-B); a pure-medium ring
  disperses (Y-C); only the hybrid equilibrates, which is the corpus's forced-
  combination theorem. The live functional is

      E(d) = sqrt3 sigma d  -  3 qt^2 ln d  -  3 alpha_d / d

  with the repulsion supplied by the MEDIUM as a vortex log. And it is not a
  reparametrisation of what I used: it demands qt^2/sqrt(sigma) = 1.110586 where the
  two-term form demands 2.136318, a factor 1.92 apart (Y-G).

  THE LIVE CHAIN REPRODUCES END TO END. At the target c_K = 4/(3 ln 2), the pure-medium
  equilibrium gives qt^2/sqrt(sigma) = c_K/sqrt3 = 1.110586, rising to 1.630 at
  alpha_d = 1 -- both recorded numbers (Y-D). Stability bounds the coupling at
  alpha_d < c_K^2/sqrt3 = 2.1363, a closed form the corpus records rounded as "<~ 2.2"
  (Y-E). The vortex convention qt^2 = 2 pi F^2 t then converts the target into
  F_dark/sqrt(sigma) = 0.420428 at t sqrt(sigma) = 1, and into the band [0.401, 0.470]
  across the flux-tube width w sqrt(sigma) in [0.8, 1.1] -- the corpus's recorded
  0.4204 and 0.40-0.47 (Y-F).

  SO #2 IS NOT BLOCKED ON A CONVENTION. The convention is pinned, the demand is exact,
  and the referee is one SU(2) N_f = 3 lattice campaign refereeing three numbers
  together: T_c/sqrt(sigma), F_pi/sqrt(sigma), w sqrt(sigma). That is EXTERNAL COMPUTE,
  and the docket has been in that state since 2026-07-18. My morning's entry made it
  look like an unresolved desk question; it is not one.

  WHAT SURVIVES OF THIS MORNING. The seed-route closure is untouched -- it used the
  bijection between seed couplings and (G_0, b), not the junction functional, and it
  stands. What is withdrawn is only the Y-junction arithmetic and the alpha_dark
  grading built on it.
""")


if __name__ == "__main__":
    main()
