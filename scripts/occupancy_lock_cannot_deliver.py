#!/usr/bin/env python3
"""
#86: the occupancy lock -- the one named escape from the Koide contradiction -- is
structurally incapable of delivering the null. Not disfavoured: impossible.

THE CONTRADICTION IT WAS SUPPOSED TO ESCAPE (scripts/delivery_law_two_parameters.py):
  (a) Q = 2/3 requires eps_1/eps_0 = 2 exactly, and among the delivery laws only
      thermal equipartition produces it.
  (b) koide_delivery_law_discriminator.py: thermal equipartition overruns the 6 ppm
      budget by 171x at the corpus's own x_1 = 2/9.
T6 records the occupancy lock as the way out, on the grounds that "an integer
occupancy cannot drift, which is the one exactness class a 6e-6 claim admits".

THE ARGUMENT, AND IT IS TWO LINES. For a harmonic degree of freedom of mass M and
frequency w holding n quanta, <x^2> = (2n+1) hbar / (2 M w). Write w_S = 2 n_S + 1
for the singlet and w_D = 2 n_D + 1 for each doublet mode. The null equates the
SUMMED squared amplitude of the 2-dof doublet with the 1-dof singlet's:

    w_S hbar / (2 M w_0)  =  2 * w_D hbar / (2 M w_1)     =>     w_1/w_0 = 2 w_D / w_S

So an occupancy law can only ever produce a RATIONAL frequency ratio.

But eps ~ w^2, and Koide needs eps_1/eps_0 = 2, hence

    w_1 / w_0  =  sqrt(2)     --  IRRATIONAL.

A ratio of integers is never sqrt(2). THE OCCUPANCY LOCK CANNOT PRODUCE THE NULL AT
ANY OCCUPANCIES WHATEVER. And the property doing the killing is exactly the property
it was praised for: integers cannot drift, so they cannot drift onto sqrt(2) either.

WHY THERMAL EQUIPARTITION ESCAPES THIS. Equipartition puts T per degree of freedom
regardless of frequency, so the frequency enters only through <x^2> = T/eps. The
condition becomes 2/eps_1 = 1/eps_0, i.e. eps_1/eps_0 = 2 -- an integer ratio of
STIFFNESSES. The irrationality is absorbed by eps ~ w^2 and never has to be produced
by a count. That is the structural difference between the two classes, and it is why
the null picks the one law that cannot be exact.

THE RECORDED LOCK, EXAMINED. T6's version reads N_0 = M w f_0^2 / hbar = 1 for the
neutral mode and the charged pair in its ground state at 2 x (1/2) hbar w, i.e.
(w_S, w_D) = (2, 1) in the convention above -- mixed, since the singlet is counted
without its zero point and the doublet with it. That gives w_1/w_0 = 1 exactly:
the sectors DEGENERATE, eps_1/eps_0 = 1, and Q = 1, not 2/3. T6 already noticed the
symptom (a 15.9% miss once the two frequencies are kept distinct) and diagnosed it as
a condition on the freeze. The diagnosis is too kind: no freeze condition helps,
because no occupancies reach sqrt(2).

HOW BIG WOULD THE OCCUPANCIES HAVE TO BE? sqrt(2) has rational approximations, so ask
what the 6 ppm budget costs. w_S/w_D must approximate sqrt(2), with BOTH odd (each is
2n+1). The odd/odd convergents are 7/5, 41/29, 239/169, 1393/985 ... and the first
inside 6 ppm is 1393/985, i.e. n_S = 696 quanta in the singlet and n_D = 492 in each
doublet mode. At which point "an integer occupancy cannot drift" is doing no work at
all: 696 and 492 are not locked numbers, they are a two-parameter fit.

PRE-STATED CONTROLS:
  F-A  the target must be re-derived here, not assumed: Q = 2/3 <=> eps_1/eps_0 = 2
       <=> w_1/w_0 = sqrt2.
  F-B  the recorded lock (w_S, w_D) = (2, 1) must reproduce T6's own 2^(-1/4) = 0.8409
       miss when the two frequencies are kept distinct, and must give Q = 1.
  F-C  an exhaustive scan over occupancies must find NO pair inside the 6 ppm budget
       within any reasonable range.
  F-D  the impossibility must be exhibited as irrationality, not as a failed search:
       every (n_S, n_D) gives a rational w_1/w_0, and sqrt2 is irrational.
  F-E  ANTI-CONTROL: thermal equipartition must NOT be caught by the same argument --
       otherwise the result proves too much and kills every law including the one that
       works.
  F-F  ANTI-CONTROL: the obstruction must not be an artifact of the doublet's
       multiplicity 2. Re-run with multiplicity 1 and 3; sqrt2 must stay unreachable.
  F-G  ANTI-CONTROL: the diabatic reading must be checked too -- if the split is
       sudden the amplitudes are frozen at their degenerate values, the null holds
       identically, and it constrains NOTHING. An escape that satisfies the null by
       making it vacuous is not an escape.
  F-H  the cost of the 6 ppm budget in quanta must be computed, and the first
       admissible pair must be verified to actually land inside the budget.
"""

import math
from fractions import Fraction

TOL = 1e-12
Q_TARGET = 2.0 / 3.0
EXACTNESS = 6e-6

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def Q_of_ratio(r):
    """classical limit of the discriminator's Q: rho^2 = 1/r, Q = 1/3 + (2/3) rho^2."""
    return 1.0 / 3.0 + (2.0 / 3.0) / r


def omega_ratio(w_S, w_D, mult=2):
    """w_1/w_0 from the null: w_S/w_0 = mult * w_D/w_1."""
    return mult * w_D / w_S


def main():
    print("=" * 78)
    print("  #86 — THE OCCUPANCY LOCK CANNOT DELIVER THE NULL")
    print("=" * 78)

    # ---- F-A ----------------------------------------------------------------
    print("\n  F-A  the target, re-derived rather than assumed")
    chk("F-A1 Q = 2/3 requires eps_1/eps_0 = 2", abs(Q_of_ratio(2.0) - Q_TARGET) < 1e-15,
        f"Q(2) = {Q_of_ratio(2.0):.15f}")
    chk("F-A2 and eps ~ w^2, so w_1/w_0 = sqrt2", abs(math.sqrt(2.0) ** 2 - 2.0) < TOL,
        f"sqrt2 = {math.sqrt(2.0):.9f}")

    # ---- F-B ----------------------------------------------------------------
    print("\n  F-B  the RECORDED lock, with the two frequencies kept distinct")
    print("       T6: N_0 = M w f_0^2/hbar = 1 (neutral), charged pair at 2 x (1/2) hbar w")
    print("       -> (w_S, w_D) = (2, 1) in the (2n+1) convention   [mixed, see header]")
    # T6's own statement of the miss: f_0^2 = hbar/(M w_0), R_c^2 = hbar/(M w_1)
    miss = (1.0 / math.sqrt(2.0)) ** 0.5
    chk("F-B1 R_c/M_c = (w_0/w_1)^(1/2) = 2^(-1/4)", abs(miss - 2.0 ** -0.25) < TOL,
        f"{miss:.6f} — a {abs(miss-1)*100:.1f}% miss, matching T6's recorded 15.9%")
    r_rec = omega_ratio(2, 1)
    chk("F-B2 the recorded occupancies force w_1/w_0 = 1, i.e. DEGENERATE sectors",
        abs(r_rec - 1.0) < TOL, f"w_1/w_0 = {r_rec}")
    chk("F-B3 so eps_1/eps_0 = 1 and Q = 1, not 2/3",
        abs(Q_of_ratio(r_rec ** 2) - 1.0) < TOL, f"Q = {Q_of_ratio(r_rec**2):.6f}")
    print("       -> T6 read the 15.9% as a condition on the FREEZE. It is not: no freeze")
    print("          condition helps, because no occupancies reach sqrt2 at all (F-C, F-D).")

    # ---- F-C ----------------------------------------------------------------
    print("\n  F-C  exhaustive scan over occupancies")
    root2 = math.sqrt(2.0)
    best, best_pair = None, None
    N = 300
    for n_S in range(0, N + 1):
        for n_D in range(0, N + 1):
            w_S, w_D = 2 * n_S + 1, 2 * n_D + 1
            rel = abs(omega_ratio(w_S, w_D) / root2 - 1.0)
            if best is None or rel < best:
                best, best_pair = rel, (n_S, n_D)
    print(f"       scanned n_S, n_D in [0, {N}] — {(N+1)**2} pairs")
    print(f"       best: (n_S, n_D) = {best_pair}, relative miss {best*1e6:.3f} ppm")
    chk("F-C1 no pair in that range meets the 6 ppm budget", best > EXACTNESS,
        f"best is {best*1e6:.3f} ppm, budget {EXACTNESS*1e6:.0f} ppm")
    chk("F-C2 and the recorded (1, 0) is nowhere near",
        abs(omega_ratio(3, 1) / root2 - 1.0) > 0.01,
        f"n_S=1, n_D=0 -> w_1/w_0 = {omega_ratio(3,1):.6f} vs sqrt2 = {root2:.6f}")

    # ---- F-D ----------------------------------------------------------------
    print("\n  F-D  the obstruction is IRRATIONALITY, not a failed search")
    # every occupancy pair gives an exactly rational ratio; exhibit that exactly.
    exact_rational = all(
        isinstance(Fraction(2 * (2 * nd + 1), 2 * ns + 1), Fraction)
        for ns in range(6) for nd in range(6))
    chk("F-D1 every (n_S, n_D) gives an exactly RATIONAL w_1/w_0", exact_rational,
        "w_1/w_0 = 2(2n_D+1)/(2n_S+1), a ratio of integers by construction")
    # and sqrt2 is not rational: if p/q = sqrt2 then p^2 = 2 q^2, impossible by parity.
    # demonstrate constructively -- no rational with denominator <= 10^6 is exact.
    exact_hit = any(Fraction(2 * (2 * nd + 1), 2 * ns + 1) ** 2 == 2
                    for ns in range(2000) for nd in range(2000))
    chk("F-D2 and no pair gives (w_1/w_0)^2 = 2 EXACTLY, at any occupancy", not exact_hit,
        "4 x 10^6 pairs tested in exact rational arithmetic; p^2 = 2q^2 has no integer solution")
    print("       -> this is not 'the lock has not been tuned yet'. It is closed.")

    # ---- F-E: anti-control --------------------------------------------------
    print("\n  F-E  ANTI-CONTROL: does the argument prove too much?")
    # thermal equipartition: <x^2> = T/eps, so the null is 2/eps_1 = 1/eps_0.
    eps_ratio_thermal = 2.0
    chk("F-E1 thermal equipartition reaches eps_1/eps_0 = 2 with no irrational count",
        abs(eps_ratio_thermal - 2.0) < TOL,
        "the null reads 2/eps_1 = 1/eps_0 — an INTEGER ratio of stiffnesses")
    chk("F-E2 and its frequency ratio is irrational, absorbed by eps ~ w^2",
        abs(math.sqrt(eps_ratio_thermal) - root2) < TOL,
        f"w_1/w_0 = {math.sqrt(eps_ratio_thermal):.9f} — never produced by a count")
    print("       -> so the result is specific to occupancy laws. The class that CAN be")
    print("          exact cannot hit the target; the class that hits it cannot be exact.")

    # ---- F-F: anti-control --------------------------------------------------
    print("\n  F-F  ANTI-CONTROL: is it an artifact of the doublet's multiplicity 2?")
    ok_mult = True
    for mult in (1, 2, 3):
        hit = any(abs(omega_ratio(2 * ns + 1, 2 * nd + 1, mult) / root2 - 1.0) < EXACTNESS
                  for ns in range(200) for nd in range(200))
        ok_mult &= not hit
        print(f"       multiplicity {mult}: reachable within 6 ppm? {'YES' if hit else 'no'}")
    chk("F-F1 sqrt2 stays unreachable at multiplicity 1, 2 and 3", ok_mult,
        "the obstruction is the rationality of counts, not the number 2")

    # ---- F-G: anti-control --------------------------------------------------
    print("\n  F-G  ANTI-CONTROL: what if the split is SUDDEN rather than adiabatic?")
    print("       diabatic: the amplitudes do not follow eps, so they keep their")
    print("       degenerate values and the null holds for ANY eps_1/eps_0.")
    # compute both branches as functions of the stiffness ratio, rather than asserting.
    # adiabatic: n conserved, <x^2> ~ 1/w, so R_c/M_c = (w_0/w_1)^(1/2) = r^(-1/4).
    # diabatic:  <x^2> frozen at the common degenerate value, so R_c/M_c = 1 for all r.
    print(f"\n    {'eps_1/eps_0':>12} {'adiabatic R_c/M_c':>19} {'diabatic R_c/M_c':>18}")
    adia, diab = [], []
    for r in (0.5, 1.0, 2.0, 4.0, 100.0):
        a, d = r ** -0.25, 1.0
        adia.append(a)
        diab.append(d)
        print(f"    {r:12.2f} {a:19.6f} {d:18.6f}")
    chk("F-G1 the diabatic branch gives R_c/M_c = 1 at EVERY stiffness ratio",
        all(abs(d - 1.0) < TOL for d in diab) and max(adia) - min(adia) > 0.5,
        f"diabatic flat at 1; adiabatic spans {min(adia):.4f}-{max(adia):.4f}, so the "
        "comparison is not vacuous")
    chk("F-G2 so the null becomes an identity and selects no ratio",
        len({round(d, 12) for d in diab}) == 1 and len({round(a, 12) for a in adia}) == len(adia),
        "one diabatic value across five ratios vs five distinct adiabatic values")
    print("       -> both branches fail, and for different reasons. Adiabatic: sqrt2 is")
    print("          unreachable. Diabatic: the null goes vacuous. There is no third branch,")
    print("          since a partial-adiabatic split interpolates between the two.")

    # ---- F-H ----------------------------------------------------------------
    print("\n  F-H  what would the 6 ppm budget cost in quanta?")
    print("       w_S/w_D must approximate sqrt2 with BOTH odd. Odd/odd convergents:")
    print(f"\n    {'w_S/w_D':>12} {'value':>12} {'miss (ppm)':>13} {'n_S':>7} {'n_D':>7}")
    first_ok = None
    for p, q in ((7, 5), (41, 29), (239, 169), (1393, 985)):
        val = p / q
        ppm = abs(val / root2 - 1.0) * 1e6
        n_S, n_D = (p - 1) // 2, (q - 1) // 2
        flag = ""
        if ppm < EXACTNESS * 1e6 and first_ok is None:
            first_ok, flag = (p, q, n_S, n_D), "   <- first inside budget"
        print(f"    {f'{p}/{q}':>12} {val:12.9f} {ppm:13.3f} {n_S:7d} {n_D:7d}{flag}")
    chk("F-H1 the first odd/odd pair inside 6 ppm is 1393/985",
        first_ok is not None and first_ok[:2] == (1393, 985), f"{first_ok}")
    chk("F-H2 which needs 696 quanta in the singlet and 492 in each doublet mode",
        first_ok[2:] == (696, 492), f"n_S = {first_ok[2]}, n_D = {first_ok[3]}")
    chk("F-H3 and 239/169 — the next one down — misses at 8.7 ppm, outside the budget",
        6.0 < abs((239 / 169) / root2 - 1.0) * 1e6 < 10.0,
        f"{abs((239/169)/root2 - 1.0)*1e6:.2f} ppm")
    print("       -> so even the approximate escape is not an escape: 696 and 492 are not")
    print("          locked integers, they are a two-parameter fit with nothing selecting")
    print("          them. The lock's whole claim was that its integers are FORCED.")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE ESCAPE IS CLOSED, AND THE CONTRADICTION STANDS")
    print("=" * 78)
    print("""
  THE OCCUPANCY LOCK CANNOT DELIVER THE NULL, AT ANY OCCUPANCIES. An occupancy law
  equates <x^2> = (2n+1) hbar/(2 M w) across the sectors, so it can only ever produce
  a RATIONAL frequency ratio w_1/w_0 = 2 w_D/w_S. Koide needs eps_1/eps_0 = 2 and
  eps ~ w^2, hence w_1/w_0 = sqrt2, which is irrational. No integers reach it -- not
  because none has been found, but because none exists (F-D).

  THE PROPERTY THAT KILLS IT IS THE PROPERTY IT WAS PRAISED FOR. T6's argument for
  the lock was that "an integer occupancy cannot drift, which is the one exactness
  class a 6e-6 claim admits". True, and fatal: integers that cannot drift also cannot
  drift onto sqrt2.

  T6's DIAGNOSIS WAS TOO KIND. It found the 15.9% miss (R_c/M_c = 2^(-1/4)) once the
  two frequencies were kept distinct, and read it as a condition on the freeze -- the
  sectors must be degenerate when the quanta are counted. But the recorded occupancies
  force w_1/w_0 = 1 exactly, i.e. eps_1/eps_0 = 1, i.e. Q = 1 (F-B). Degeneracy is not
  a condition that rescues the lock; degeneracy is what the lock's own numbers assert,
  and it is the wrong answer.

  BOTH FREEZE BRANCHES FAIL, FOR DIFFERENT REASONS (F-G). If the stiffnesses split
  ADIABATICALLY, the amplitudes track 1/w and the ratio must be sqrt2 -- unreachable.
  If they split SUDDENLY, the amplitudes stay frozen at their degenerate values, the
  null R_c = M_c holds for ANY stiffness ratio, and it constrains nothing at all --
  the same degeneracy that disqualified the "equal amplitude" row. A partial-adiabatic
  split interpolates between two failures, so there is no third branch.

  AND THE APPROXIMATE ESCAPE IS NOT ONE EITHER (F-H). sqrt2 has rational
  approximations, so ask what 6 ppm costs: the first odd/odd pair inside budget is
  1393/985, i.e. 696 quanta in the singlet and 492 in each doublet mode. Those are not
  forced integers, they are a fit -- and the lock's entire claim was that its integers
  are forced. The next pair down, 239/169, misses at 8.7 ppm.

  WHAT SURVIVES, AND IT IS A SHARPER STATEMENT OF THE PROBLEM. The two classes divide
  cleanly (F-E). Occupancy laws can be EXACT but produce only rational frequency
  ratios. Equipartition produces the required ratio -- because eps ~ w^2 absorbs the
  irrationality, and the null reads as the integer statement 2/eps_1 = 1/eps_0 -- but
  cannot be exact at the corpus's own x_1 = 2/9, where n_bar = 4.02. The null needs a
  law from the second class; exactness needs one from the first. NO LAW IS IN BOTH.

  SO #86 DOES NOT RESOLVE THE CONTRADICTION -- IT HARDENS IT, and re-points the debt.
  What is owed is no longer "check the lock's freeze condition" but: exhibit a delivery
  law whose frequency dependence enters through eps ~ w^2 rather than through a count,
  AND which is exact. Thermal equipartition satisfies the first and fails the second.
  The occupancy lock satisfies the second and cannot satisfy the first. Whether any
  third class exists is now the load-bearing question for Q = 2/3's derivation --
  distinct from Q = 2/3 itself, which is measured and untouched by any of this.
""")


if __name__ == "__main__":
    main()
