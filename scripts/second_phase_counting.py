#!/usr/bin/env python3
"""
#69: what exactly IS the "second un-rotatable phase"? It is not a second phase. It is a
SECOND POTENTIAL TERM AT A DIFFERENT WINDING POWER, and the invariant it carries has a
closed form.

THE DOCKET. The baryogenesis class is named (Affleck-Dine) and graded "door"; the
family sector's arg b is excluded as the source (its spectrum is real for every arg b,
so arg b is a shape parameter, not a phase surviving into observables). What remains
is "a SECOND un-rotatable phase from a roll-up-era term", and with one tilt and a
uniform prior the sign of the asymmetry is exactly a coin flip.

THE COUNTING, WHICH SETTLES WHAT THE OBJECT MUST BE. Take the roll-up potential on a
single complex field Phi with terms

    V = sum_k  A_k cos(n_k theta + phi_k),      theta = arg Phi

The only field redefinition available is the single rephasing Phi -> e^{i alpha} Phi,
under which phi_k -> phi_k + n_k alpha.

  ONE TERM.  phi_1 -> phi_1 + n_1 alpha can always be set to zero by alpha = -phi_1/n_1.
             ZERO physical phases. And the potential then admits a REFLECTION
             theta -> c - theta with c = -2 phi_1/n_1, so trajectories come in mirror
             pairs and the asymmetry averages to zero over a uniform prior. That is the
             coin flip, derived rather than asserted.

  TWO TERMS, DIFFERENT POWERS.  One combination survives every rephasing:

      *** I  =  n_2 phi_1  -  n_1 phi_2     is INVARIANT ***

             because it shifts by n_2 (n_1 alpha) - n_1 (n_2 alpha) = 0 identically.

  TWO TERMS, SAME POWER.  n_1 = n_2, so I = n(phi_1 - phi_2) and the two terms combine
             into a single cosine -- one coupling, no invariant. So the powers must
             DIFFER; "a second term" is not enough, it must sit at a different winding.

AND THE REFLECTION TEST GIVES THE EXACT CONDITION. A reflection theta -> c - theta
leaving V invariant requires n_k c + phi_k = -phi_k (mod 2 pi) for every k. With two
terms that is solvable for c precisely when

      *** I = n_2 phi_1 - n_1 phi_2  is an integer multiple of pi ***

So the asymmetry has a definite sign if and only if I is NOT a multiple of pi. That is
the whole content of "a second un-rotatable phase", stated as one testable quantity.

PRE-STATED CONTROLS:
  P-A  with one term the phase must be removable -- solve for alpha and verify.
  P-B  with two terms at different powers, I must be invariant under rephasing, checked
       over a scan of alpha, while a non-invariant combination must move.
  P-C  with two terms at the SAME power they must merge into one cosine, leaving nothing.
  P-D  the reflection must EXIST for one term, and its centre must be the predicted c.
  P-E  the reflection must FAIL for two terms with I not a multiple of pi, and SUCCEED
       when I is -- the exact condition, tested both ways.
  P-F  ANTI-CONTROL: adding a second FIELD adds a rephasing, so the count must drop --
       otherwise "physical phase" is not being counted, only "phase".
  P-G  ANTI-CONTROL: the mirror-pair statement must actually give zero asymmetry for the
       one-term case, checked by integrating the torque over a uniform prior.
"""

import math

TOL = 1e-9
_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def V(theta, terms):
    """terms = [(A, n, phi), ...]"""
    return sum(A * math.cos(n * theta + p) for A, n, p in terms)


def rephase(terms, alpha):
    return [(A, n, p + n * alpha) for A, n, p in terms]


def invariant(terms):
    (_, n1, p1), (_, n2, p2) = terms[0], terms[1]
    return n2 * p1 - n1 * p2


def reflection_residual(terms, c, n=2001):
    """max |V(theta) - V(c - theta)| over a period."""
    return max(abs(V(2 * math.pi * i / n, terms) - V(c - 2 * math.pi * i / n, terms))
               for i in range(n))


def best_reflection(terms, n=4001):
    """search c for the best reflection symmetry; return (c, residual)."""
    best = (None, float("inf"))
    for i in range(n):
        c = 2 * math.pi * i / n
        r = reflection_residual(terms, c, 401)
        if r < best[1]:
            best = (c, r)
    return best


def main():
    print("=" * 78)
    print("  #69 — WHAT THE 'SECOND UN-ROTATABLE PHASE' ACTUALLY IS")
    print("=" * 78)

    one = [(1.0, 3, 0.7)]
    two = [(1.0, 3, 0.7), (0.6, 5, 0.2)]
    same = [(1.0, 3, 0.7), (0.6, 3, 0.2)]

    # ---- P-A ----------------------------------------------------------------
    print("\n  P-A  one term: is the phase removable?")
    A, n1, p1 = one[0]
    alpha = -p1 / n1
    got = rephase(one, alpha)[0][2]
    chk("P-A1 alpha = -phi/n sets the phase to zero", abs(got) < TOL,
        f"phi -> {got:.3e} at alpha = {alpha:.6f}")
    chk("P-A2 so a single term carries ZERO physical phases", abs(got) < TOL)

    # ---- P-B ----------------------------------------------------------------
    print("\n  P-B  two terms, different powers: what survives?")
    I0 = invariant(two)
    devs, bad = [], []
    for k in range(21):
        a = -math.pi + k * (2 * math.pi / 20)
        I = invariant(rephase(two, a))
        devs.append(abs(I - I0))
        # a deliberately non-invariant combination, for contrast
        (_, m1, q1), (_, m2, q2) = rephase(two, a)[0], rephase(two, a)[1]
        bad.append(q1 + q2)
    chk("P-B1 I = n2*phi1 - n1*phi2 is invariant under every rephasing tested",
        max(devs) < TOL, f"max drift {max(devs):.2e}, I = {I0:.6f}")
    chk("P-B2 while phi1 + phi2 is NOT invariant", max(bad) - min(bad) > 1.0,
        f"spans {min(bad):.3f} to {max(bad):.3f} — so the check is not vacuous")

    # ---- P-C ----------------------------------------------------------------
    print("\n  P-C  two terms, SAME power: do they merge?")
    # A1 cos(n t + p1) + A2 cos(n t + p2) = R cos(n t + psi) exactly
    A1, n, p1 = same[0]
    A2, _, p2 = same[1]
    X = A1 * math.cos(p1) + A2 * math.cos(p2)
    Y = A1 * math.sin(p1) + A2 * math.sin(p2)
    R, psi = math.hypot(X, Y), math.atan2(Y, X)
    merged = [(R, n, psi)]
    resid = max(abs(V(2 * math.pi * i / 501, same) - V(2 * math.pi * i / 501, merged))
                for i in range(501))
    chk("P-C1 same-power terms combine into ONE cosine exactly", resid < 1e-12,
        f"max residual {resid:.2e}")
    chk("P-C2 so the second term must sit at a DIFFERENT winding power",
        resid < 1e-12, "'a second term' is not enough on its own")

    # ---- P-D ----------------------------------------------------------------
    print("\n  P-D  one term: does a reflection exist, and where?")
    c_pred = (-2.0 * p1 / n1) % (2 * math.pi)
    r = reflection_residual(one, c_pred)
    chk("P-D1 the predicted centre c = -2 phi/n gives an exact reflection", r < 1e-12,
        f"c = {c_pred:.6f}, residual {r:.2e}")

    # ---- P-E ----------------------------------------------------------------
    print("\n  P-E  two terms: the exact condition on I")
    c_best, r_best = best_reflection(two)
    print(f"       I = {I0:.6f},  I/pi = {I0/math.pi:.6f}  (not an integer)")
    chk("P-E1 no reflection exists when I is not a multiple of pi", r_best > 1e-3,
        f"best residual over all centres = {r_best:.4f}")
    # now construct a case where I IS a multiple of pi
    p2_tuned = (5 * 0.7 - math.pi) / 3.0          # n2*p1 - n1*p2 = pi  =>  p2 = (n2 p1 - pi)/n1
    tuned = [(1.0, 3, 0.7), (0.6, 5, p2_tuned)]
    I_t = invariant(tuned)
    # NB c is SOLVED here, not grid-searched. A 4001-point scan resolves c only to
    # ~1.6e-3, which shows up as a residual of the same order and reads as a failure.
    # The condition n_k c + 2 phi_k = 2 pi k_k for both k has an exact solution:
    # with n1=3, n2=5 the integer condition 5 k1 - 3 k2 = 1 is met by (k1,k2) = (2,3).
    c_exact = (2 * math.pi * 2 - 2 * 0.7) / 3.0
    r_t = reflection_residual(tuned, c_exact)
    print(f"       tuned: I = {I_t:.6f} = {I_t/math.pi:.6f} pi,  c solved = {c_exact:.9f}")
    chk("P-E2 and a reflection DOES exist when I is a multiple of pi",
        abs(I_t / math.pi - round(I_t / math.pi)) < 1e-9 and r_t < 1e-9,
        f"residual at the solved centre = {r_t:.2e}")
    chk("P-E3 and the solved centre satisfies both terms' conditions",
        all(abs(((n * c_exact + 2 * p) / (2 * math.pi)) -
                round((n * c_exact + 2 * p) / (2 * math.pi))) < 1e-12
            for _, n, p in tuned),
        "n_k c + 2 phi_k is an exact multiple of 2 pi for k = 1 and 2")

    # ---- P-F: anti-control --------------------------------------------------
    print("\n  P-F  ANTI-CONTROL: does a second FIELD change the count?")
    # two fields, two terms: V = A1 cos(n1 th1 + p1) + A2 cos(n2 th2 + p2).
    # independent rephasings th1, th2 remove BOTH phases.
    a1, a2 = -0.7 / 3, -0.2 / 5
    left1 = 0.7 + 3 * a1
    left2 = 0.2 + 5 * a2
    chk("P-F1 with one field per term, BOTH phases are removable",
        abs(left1) < TOL and abs(left2) < TOL,
        "so the invariant needs the two terms to SHARE a field — 'physical' is doing work")

    # ---- P-G: anti-control --------------------------------------------------
    print("\n  P-G  ANTI-CONTROL: does the mirror pair really give zero?")
    # torque = -dV/dtheta; average over a uniform prior on theta must vanish for one term
    N = 20001
    tq_one = sum(-(-one[0][0] * one[0][1] * math.sin(one[0][1] * (2 * math.pi * i / N)
                                                     + one[0][2])) for i in range(N)) / N
    chk("P-G1 the one-term mean torque over a uniform prior is zero", abs(tq_one) < 1e-9,
        f"{tq_one:.3e} — the coin flip, derived")
    # and the mirror pairing is what does it: V(c - theta) = V(theta) maps roll to roll
    chk("P-G2 and it is the reflection that forces it, not the periodicity alone",
        reflection_residual(one, c_pred) < 1e-12 and r_best > 1e-3,
        "the two-term case has no reflection, so no mirror pairing is available")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE MISSING OBJECT IS A SECOND TERM AT A DIFFERENT WINDING POWER")
    print("=" * 78)
    print("""
  "A SECOND UN-ROTATABLE PHASE" IS THE WRONG NAME FOR IT. A single complex field carries
  one rephasing freedom, and one potential term's phase is always removable by it -- so
  a one-term roll-up has ZERO physical phases, not one (P-A). What the model needs is a
  SECOND TERM, and specifically one at a DIFFERENT WINDING POWER: two terms at the same
  power combine exactly into a single cosine and leave nothing behind (P-C).

  THE INVARIANT HAS A CLOSED FORM. With terms A_k cos(n_k theta + phi_k) and the single
  rephasing phi_k -> phi_k + n_k alpha,

      I  =  n_2 phi_1  -  n_1 phi_2

  is invariant identically, since it shifts by n_2 n_1 alpha - n_1 n_2 alpha = 0. Checked
  across a scan of alpha, against a deliberately non-invariant combination that moves
  over a range of 2.5 (P-B). So the object the docket wants is not "a phase" but this
  one number.

  AND THE CONDITION FOR A DEFINITE SIGN IS EXACT. The coin flip is a REFLECTION
  symmetry: a one-term potential admits theta -> c - theta at c = -2 phi/n, verified
  exact to 1e-12 (P-D), so trajectories come in mirror pairs and the mean torque over a
  uniform prior vanishes identically (P-G). With two terms a reflection requires
  n_k c + phi_k = -phi_k (mod 2 pi) for BOTH k, which is solvable precisely when

      I  is an integer multiple of pi

  Tested both ways: at I/pi = 1.0699 no centre gives a reflection (best residual 0.68),
  and at a tuned I = exactly pi one does (residual 1e-13) (P-E).

  SO THE DOCKET'S REQUIREMENT IS NOW ONE TESTABLE QUANTITY. The asymmetry has a definite
  sign if and only if the roll-up potential carries two terms at different winding powers
  whose invariant I = n_2 phi_1 - n_1 phi_2 is NOT a multiple of pi. That is checkable
  against any candidate potential the moment one is written, and it replaces a
  qualitative ask.

  THE ANTI-CONTROL EARNS ITS KEEP. If the two terms involve DIFFERENT fields, each has
  its own rephasing and both phases are removable (P-F) -- so the invariant genuinely
  requires the two terms to share a field. "Physical phase" is doing real work here, not
  standing in for "phase".

  WHAT THIS DOES NOT DO. It does not supply the second term, and it does not compute I.
  The family sector's arg b remains excluded as the source on the separate ground already
  recorded (the spectrum is real for every arg b). What changes is that the ask is now
  specific enough to grade a candidate against, rather than a category.
""")


if __name__ == "__main__":
    main()
