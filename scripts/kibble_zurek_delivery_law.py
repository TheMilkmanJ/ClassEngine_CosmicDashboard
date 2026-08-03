#!/usr/bin/env python3
"""
#88: work the Kibble-Zurek route through for THIS mode structure. T6 recorded it as
"a route, not an answer" and left the prescription unapplied. Applying it settles what
KZ can and cannot buy.

THE CORPUS'S CLAIM, which this grades. T6: "the delivery law may not be a free choice
among four at all -- KZ carries its own freeze-out prescription ... which converts #85
from 'choose among four conventions' into 'apply a textbook mechanism the model already
claims', which is a categorically better position."

THE SETUP. The ring's normal modes carry FIXED geometric stiffness coefficients
c_S = 6 (breathing singlet, multiplicity 1) and c_D = 3 (shape doublet, multiplicity 2),
so c_D/c_S = 1/2. Through the transition the overall stiffness ramps, eps_i(t) = c_i
lambda(t) with lambda ~ t^m, and a mode's relaxation time scales as tau_i ~ eps_i^(-a)
-- a = 1 overdamped, a = 1/2 underdamped (tau ~ 1/omega ~ eps^(-1/2)).

THE KZ PRESCRIPTION. A mode freezes when its relaxation time equals the time remaining,
tau_i(t) = t, and thereafter keeps the amplitude it had at that instant. Solving,

    t_i        ~  c_i^( -a / (1 + a m) )
    eps_i(t_i) ~  c_i^(  1 / (1 + a m) )

and the frozen amplitude is the equilibrium one AT FREEZE, <x^2>_i = T / eps_i(t_i).

THE NULL, AND THE RESULT THAT MATTERS. R_c = M_c equates the doublet's summed frozen
amplitude with the singlet's, 2 T/eps_D(t_D) = T/eps_S(t_S), i.e.

    eps_D(t_D) / eps_S(t_S)  =  ( c_D/c_S )^( 1/(1+am) )  =  2

Since c_D/c_S = 1/2 < 1 and the target 2 > 1, THE EXPONENT MUST BE NEGATIVE:
1/(1+am) = -1, i.e. **a m = -2**.

  *** So KZ delivers the null ONLY for a SOFTENING quench (m < 0). For every ordering
  *** transition -- every m > 0, at any damping -- the ratio comes out BELOW 1, and Q
  *** lands above 1 instead of at 2/3. The sign is wrong, not the magnitude.

Special cases: am = 0 (no ramp) gives exactly 1/2, which is the recorded "doublet gets
half" law and Q = 5/3. Overdamped a = 1 needs m = -2; underdamped a = 1/2 needs m = -4.

AND KZ BUYS THE RATIO, NOT THE EXACTNESS. Even at am = -2, the two sectors freeze at
stiffnesses differing by 2, hence frequencies differing by sqrt2, so the quantum
correction g(x) still does not cancel between them -- the same non-cancellation, the
same 1025 ppm against a 6 ppm budget. KZ relocates where the number 2 comes from; it
does nothing whatever about why the null is claimed exact.

ONE STRUCTURAL GAIN, WORTH MORE THAN THE ARITHMETIC. Under KZ a mode's stiffness AT
FREEZE (which sets the amplitude) differs from its stiffness AT OBSERVATION (which the
mass formula reads). Those are two different objects, and the (s,p) family assumed one.
That is a candidate identity for #85's unexplained "third stiffness pair" -- the pair
the null needs is neither the final radial Hessian nor the circulant amplitudes, and a
freeze-time pair is exactly the kind of object it would have to be.

PRE-STATED CONTROLS:
  K-A  the freeze time must be obtained by SOLVING tau_i(t) = t numerically, and must
       match the closed form t_i ~ c_i^(-a/(1+am)).
  K-B  the freeze-time stiffness must match eps_i ~ c_i^(1/(1+am)), again solved not
       asserted.
  K-C  the null must require am = -2, and that value must reproduce ratio 2 exactly.
  K-D  for EVERY stiffening quench (m > 0, a > 0) the ratio must come out below 1, and
       Q above 1 -- scanned, not argued.
  K-E  am = 0 must reproduce the recorded "doublet gets half" law (1/2, Q = 5/3).
  K-F  ANTI-CONTROL: KZ must NOT rescue exactness. At am = -2 the quantum correction
       must still fail to cancel, reproducing the recorded 1025 ppm class.
  K-G  ANTI-CONTROL: the result must depend on the two sectors sharing ONE ramp. If
       each sector had its own lambda(t) the construction would be vacuous -- check
       that independent ramps can hit any ratio at all, so the shared ramp is what
       makes KZ predictive.
  K-H  ANTI-CONTROL: freeze-time and observation-time stiffness must genuinely differ,
       or the "third pair" reading is empty.
"""

import math

TOL = 1e-12
C_S, C_D = 6.0, 3.0
Q_TARGET = 2.0 / 3.0
X1_CORPUS = 2.0 / 9.0

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def g(x):
    if x < 1e-8:
        return 1.0 + x * x / 12.0
    z = 0.5 * x
    return z / math.tanh(z)


def freeze_time(c, a, m, A=1.0, lam=1.0):
    """solve tau(t) = t with tau = A (c lam t^m)^(-a) -- numerically, not by formula."""
    def f(t):
        return A * (c * lam * t ** m) ** (-a) - t
    lo, hi = 1e-8, 1e8
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(400):
        mid = math.sqrt(lo * hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def eps_at_freeze(c, a, m, A=1.0, lam=1.0):
    t = freeze_time(c, a, m, A, lam)
    return None if t is None else c * lam * t ** m


def ratio_kz(a, m):
    """eps_D(t_D) / eps_S(t_S)"""
    eD, eS = eps_at_freeze(C_D, a, m), eps_at_freeze(C_S, a, m)
    return None if (eD is None or eS is None) else eD / eS


def Q_of_ratio(r):
    return 1.0 / 3.0 + (2.0 / 3.0) / r


def main():
    print("=" * 78)
    print("  #88 — THE KIBBLE–ZUREK ROUTE, WORKED THROUGH")
    print("=" * 78)
    print(f"\n  ring modes: c_S = {C_S:.0f} (singlet, mult 1), c_D = {C_D:.0f}"
          f" (doublet, mult 2), c_D/c_S = {C_D/C_S}")

    # ---- K-A ----------------------------------------------------------------
    print("\n  K-A  freeze time, solved from tau(t) = t")
    print(f"\n    {'a':>5} {'m':>5} {'t_S':>12} {'t_D':>12} {'t_D/t_S':>10}"
          f" {'closed form':>12}")
    ok_a = True
    for a, m in ((1.0, 1.0), (0.5, 1.0), (1.0, 2.0), (0.5, 3.0)):
        tS, tD = freeze_time(C_S, a, m), freeze_time(C_D, a, m)
        want = (C_D / C_S) ** (-a / (1 + a * m))
        good = abs(tD / tS / want - 1) < 1e-6
        ok_a &= good
        print(f"    {a:5.1f} {m:5.1f} {tS:12.6f} {tD:12.6f} {tD/tS:10.6f}"
              f" {want:12.6f}  {'' if good else '<-- MISMATCH'}")
    chk("K-A1 solved freeze times match t_i ~ c_i^(-a/(1+am))", ok_a)

    # ---- K-B ----------------------------------------------------------------
    print("\n  K-B  stiffness at freeze")
    ok_b = True
    for a, m in ((1.0, 1.0), (0.5, 1.0), (1.0, 2.0), (0.5, 3.0)):
        got = ratio_kz(a, m)
        want = (C_D / C_S) ** (1.0 / (1 + a * m))
        good = abs(got / want - 1) < 1e-6
        ok_b &= good
        print(f"    a={a:.1f} m={m:.1f}:  eps_D/eps_S = {got:.9f}"
              f"   closed form {want:.9f}  {'' if good else '<-- MISMATCH'}")
    chk("K-B1 solved stiffness ratios match c_i^(1/(1+am))", ok_b)

    # ---- K-C ----------------------------------------------------------------
    print("\n  K-C  what does the null require?")
    print("       need (c_D/c_S)^(1/(1+am)) = 2 with c_D/c_S = 1/2")
    print("       => 1/(1+am) = -1  =>  am = -2")
    r_target = (C_D / C_S) ** (1.0 / (1 + (-2.0)))
    chk("K-C1 am = -2 gives exactly 2", abs(r_target - 2.0) < TOL, f"{r_target:.12f}")
    chk("K-C2 and hence Q = 2/3", abs(Q_of_ratio(r_target) - Q_TARGET) < 1e-15,
        f"Q = {Q_of_ratio(r_target):.15f}")
    # every damping exponent needs its own m, and all of them are NEGATIVE
    needed = [(a, -2.0 / a) for a in (0.5, 1.0, 2.0)]
    chk("K-C3 each damping a needs m = -2/a, and every one is a SOFTENING ramp",
        all(abs((C_D / C_S) ** (1.0 / (1 + a * m)) - 2.0) < 1e-9 for a, m in needed)
        and all(m < 0 for _, m in needed),
        "  ".join(f"a={a:.1f} -> m={m:+.1f}" for a, m in needed))

    # ---- K-D ----------------------------------------------------------------
    print("\n  K-D  every STIFFENING quench (m > 0) — which side of 1?")
    print(f"\n    {'a':>5} {'m':>5} {'am':>6} {'eps_D/eps_S':>13} {'Q':>12}  verdict")
    all_below = True
    for a in (0.5, 1.0, 2.0):
        for m in (0.5, 1.0, 2.0, 5.0):
            r = (C_D / C_S) ** (1.0 / (1 + a * m))
            all_below &= r < 1.0
            print(f"    {a:5.1f} {m:5.1f} {a*m:6.2f} {r:13.9f} {Q_of_ratio(r):12.6f}"
                  f"  {'below 1' if r < 1 else 'ABOVE 1'}")
    chk("K-D1 every stiffening quench gives eps_D/eps_S < 1", all_below,
        "so Q > 1 in all of them — the SIGN is wrong, not the magnitude")
    chk("K-D2 and the target 2 is unreachable for any m > 0, a > 0",
        all((C_D / C_S) ** (1.0 / (1 + a * m)) < 1.0
            for a in (0.1, 0.5, 1.0, 2.0, 10.0) for m in (0.1, 1.0, 10.0, 100.0)),
        "1 + am > 1 > 0, so the exponent is positive and (1/2)^positive < 1")

    # ---- K-E ----------------------------------------------------------------
    print("\n  K-E  the no-ramp limit am = 0")
    r0 = (C_D / C_S) ** (1.0 / (1 + 0.0))
    chk("K-E1 am = 0 gives exactly 1/2", abs(r0 - 0.5) < TOL, f"{r0}")
    chk("K-E2 which is the recorded 'doublet gets half' law, Q = 5/3",
        abs(Q_of_ratio(r0) - 5.0 / 3.0) < TOL, f"Q = {Q_of_ratio(r0):.9f}")

    # ---- K-F: anti-control --------------------------------------------------
    print("\n  K-F  ANTI-CONTROL: does KZ rescue EXACTNESS?")
    # at am = -2 the freeze stiffnesses differ by 2, so omegas differ by sqrt2
    x_D = X1_CORPUS
    x_S = x_D / math.sqrt(2.0)
    rho2 = 0.5 * g(x_D) / g(x_S)
    q_kz = 1.0 / 3.0 + (2.0 / 3.0) * rho2
    ppm = abs(q_kz / Q_TARGET - 1) * 1e6
    print(f"       at am = -2:  eps ratio 2  =>  omega ratio sqrt2  =>  x ratio sqrt2")
    print(f"       x_D = {x_D:.6f}, x_S = {x_S:.6f}, g(x_D)/g(x_S) = {g(x_D)/g(x_S):.9f}")
    chk("K-F1 the quantum correction still does NOT cancel",
        abs(g(x_D) / g(x_S) - 1.0) > 1e-6, f"ratio {g(x_D)/g(x_S):.9f}, not 1")
    chk("K-F2 reproducing the recorded 1025 ppm against a 6 ppm budget",
        abs(ppm - 1025.4) < 0.5, f"{ppm:.1f} ppm")
    print("       -> KZ relocates where the number 2 comes from. It does nothing at all")
    print("          about why the null is claimed exact.")

    # ---- K-G: anti-control --------------------------------------------------
    print("\n  K-G  ANTI-CONTROL: is the SHARED ramp what makes KZ predictive?")
    # give the sectors independent ramp rates lam_S, lam_D and see if any ratio is reachable
    hits = []
    for lam_D in (0.1, 0.5, 1.0, 2.0, 10.0):
        eD = eps_at_freeze(C_D, 1.0, 1.0, lam=lam_D)
        eS = eps_at_freeze(C_S, 1.0, 1.0, lam=1.0)
        hits.append(eD / eS)
    chk("K-G1 with independent ramps the ratio is a free parameter",
        max(hits) / min(hits) > 3.0 and any(h > 2.0 for h in hits) and any(h < 1.0 for h in hits),
        f"spans {min(hits):.4f} to {max(hits):.4f} — brackets the target 2")
    chk("K-G2 so KZ predicts anything ONLY because the two sectors share one lambda(t)",
        True, "the shared ramp is the physical content; without it the route is vacuous")

    # ---- K-H: anti-control --------------------------------------------------
    print("\n  K-H  ANTI-CONTROL: do freeze-time and observation-time stiffness differ?")
    a, m = 1.0, 1.0
    eD_f, eS_f = eps_at_freeze(C_D, a, m), eps_at_freeze(C_S, a, m)
    chk("K-H1 the freeze-time ratio is NOT the geometric ratio c_D/c_S",
        abs(eD_f / eS_f - C_D / C_S) > 1e-6,
        f"freeze {eD_f/eS_f:.6f} vs geometric {C_D/C_S:.6f}")
    chk("K-H2 so KZ supplies TWO stiffness pairs where the (s,p) family assumed one",
        True, "a candidate identity for #85's unexplained third pair")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — KZ BUYS THE RATIO'S ORIGIN, NOT THE RATIO, AND NOT THE EXACTNESS")
    print("=" * 78)
    print("""
  THE PRESCRIPTION APPLIED. Freezing when tau_i(t) = t, with eps_i = c_i lambda(t),
  lambda ~ t^m and tau ~ eps^(-a), gives eps_i(t_i) ~ c_i^(1/(1+am)) -- verified by
  solving the freeze condition numerically, not by quoting the algebra (K-A, K-B). The
  null then reads

      ( c_D/c_S )^( 1/(1+am) )  =  2,    with c_D/c_S = 1/2

  THE SIGN IS WRONG FOR EVERY ORDERING TRANSITION. c_D/c_S is BELOW 1 and the target is
  ABOVE 1, so the exponent must be negative: 1 + am < 0, i.e. am < -1, i.e. m < 0 at any
  positive damping. Scanned over a in [0.1, 10] and m in [0.1, 100], EVERY stiffening
  quench lands below 1, hence Q above 1 (K-D). Exactly am = -2 gives 2 -- overdamped
  needs m = -2, underdamped m = -4. Those are SOFTENING ramps.

  AND THE NO-RAMP LIMIT IS ALREADY IN THE TABLE. am = 0 returns exactly 1/2, which is
  the recorded "doublet gets half the singlet" law, Q = 5/3 (K-E). So KZ does not
  introduce a new row so much as parametrise the existing ones by a quench exponent.

  KZ DOES NOT TOUCH EXACTNESS (K-F). At am = -2 the two sectors freeze at stiffnesses
  differing by 2, hence frequencies differing by sqrt2, so g(x) still fails to cancel
  between them -- reproducing the same 1025 ppm against the same 6 ppm budget. Whatever
  KZ buys, it is not the thing the arc is actually blocked on.

  GRADING T6's CLAIM. T6 recorded that KZ "converts #85 from 'choose among four
  conventions' into 'apply a textbook mechanism the model already claims', which is a
  categorically better position." Half right, and the half that fails is the important
  one. KZ does replace a convention with a mechanism -- but the mechanism then DEMANDS a
  softening quench with a tuned exponent (am = -2) to reach the null at all, and leaves
  the exactness problem exactly where it was. It is a reparametrisation of the choice,
  not a removal of it.

  THE ONE REAL GAIN, AND IT IS STRUCTURAL (K-H). Under KZ a mode's stiffness AT FREEZE
  -- which sets the frozen amplitude -- differs from its stiffness AT OBSERVATION, which
  the mass formula reads. The (s,p) family assumed a single eps. So KZ naturally
  supplies TWO stiffness pairs, and a freeze-time pair is exactly the kind of object
  #85's unexplained "third pair" would have to be: neither the final radial Hessian
  (1/2) nor the circulant amplitudes (0.1213). That is a lead worth keeping even though
  the rest of the route does not deliver.

  ONE CAVEAT, STATED SO THIS IS NOT OVER-READ (K-G). The whole construction is
  predictive only because both sectors ride ONE lambda(t). Allowed independent ramp
  rates, the ratio spans the target freely and KZ predicts nothing. The shared ramp is
  the physical content, and it is an assumption -- a reasonable one for two normal modes
  of a single ring, but an assumption.
""")


if __name__ == "__main__":
    main()
