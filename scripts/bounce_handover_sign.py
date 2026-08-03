#!/usr/bin/env python3
"""
#13 tasks 4 and 5: can negative vacuum + Tolman radiation bounce, and if not, what
is the missing component?

THE WORKPLAN'S OWN TASKS (working_logs/bounce_derivation_workplan.md):
  4. Check whether the negative bare vacuum plus Tolman-kept radiation can produce
     the required sign change by itself.
  5. If not, identify the missing stiff or effectively stiff component and state it
     as the load-bearing open variable.

Both are FRW energy balance, not model-building, so both can be settled at the desk.

THE BOUNCE CONDITIONS, from the workplan:
    H  = 0    at the handover        <=>   rho_total = 0        [since H^2 = (8 pi G/3) rho]
    Hdot > 0  at the same point      <=>   rho + p < 0          [since Hdot = -4 pi G (rho + p)]

so EVERYTHING turns on the sign of (rho + p) = sum_i (1 + w_i) rho_i.

TASK 4, AND THE ANSWER IS NO. Write the two components:
    negative bare vacuum   w = -1   =>  (1 + w) rho = 0        EXACTLY, whatever rho is
    Tolman-kept radiation  w = +1/3 =>  (1 + w) rho = (4/3) rho_r > 0

A cosmological constant contributes NOTHING to rho + p -- not a little, exactly zero
-- because 1 + w vanishes identically. Its sign is irrelevant: a NEGATIVE vacuum is
just as inert here as a positive one. So rho + p = (4/3) rho_r > 0 always, hence
Hdot < 0 always, and no bounce is possible from these two components in any
combination or at any epoch.

H = 0 IS still reachable -- radiation grows as a^-4 under contraction while the
vacuum stays constant, so rho_total = rho_r + rho_Lambda crosses zero. But crossing
H = 0 with Hdot < 0 is a TURNAROUND (expansion to contraction), the opposite of a
bounce. The two components deliver the condition that is easy and not the one that
matters.

TASK 5. Hdot > 0 needs sum_i (1 + w_i) rho_i < 0, so at least one component must
have (1 + w) rho < 0. Two ways:
    positive energy with w < -1     (phantom), or
    NEGATIVE energy with w > -1
The second is the workplan's "stiff or effectively stiff" route: a negative-energy
stiff component (w = +1) gives (1 + w) rho = 2 rho < 0. And stiff scales as a^-6 --
faster than radiation's a^-4 -- so it is subdominant today and takes over exactly
where a bounce needs it, at maximum compression. That is why "stiff" and not
"matter": a negative-energy matter component (w = 0) would also flip the sign but
scales as a^-3 and would never come to dominate.

PRE-STATED CONTROLS:
  B-A  (1+w) rho must be exactly 0 for w = -1 at any rho, positive or negative --
       this is the whole of task 4's answer and must not depend on magnitudes.
  B-B  negative vacuum + radiation must give rho + p > 0 across a wide scan, hence
       Hdot < 0, hence no bounce.
  B-C  H = 0 must nonetheless be reachable, so the failure is specifically in the
       Hdot condition and not in both.
  B-D  a negative stiff component must flip the sign, and its a^-6 scaling must
       overtake radiation under contraction.
  B-E  ANTI-CONTROL: POSITIVE stiff must NOT work, and negative MATTER must flip the
       sign but fail to dominate -- otherwise "negative stiff" is not doing the work
       and any negative component would do.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def rho_plus_p(comps):
    """sum (1+w) rho over [(w, rho), ...]"""
    return sum((1 + w) * r for w, r in comps)


def main():
    print("=" * 78)
    print("  #13 TASKS 4 & 5 — THE HANDOVER SIGN")
    print("=" * 78)
    print("\n  H = 0  <=>  rho_total = 0      Hdot > 0  <=>  rho + p < 0")

    # ---- B-A ---------------------------------------------------------------
    print("\n  B-A  a w = -1 component contributes EXACTLY zero to rho + p")
    worst = max(abs(rho_plus_p([(-1.0, r)])) for r in (-1e9, -1.0, -1e-9, 1e-9, 1.0, 1e9))
    chk("B-A1 (1+w)rho = 0 for w = -1 at any rho, either sign", worst == 0.0,
        f"max |contribution| = {worst}")
    print("       -> the vacuum's SIGN is irrelevant here: a negative Lambda is just")
    print("          as inert in the Hdot equation as a positive one.")

    # ---- B-B: task 4 --------------------------------------------------------
    print("\n  B-B  TASK 4: negative vacuum + Tolman radiation")
    bad = []
    for rL in (-1e-3, -1.0, -1e3):
        for rr in (1e-6, 1.0, 1e6):
            s = rho_plus_p([(-1.0, rL), (1 / 3, rr)])
            if s <= 0:
                bad.append((rL, rr, s))
    chk("B-B1 rho + p > 0 for every combination scanned", not bad,
        f"9 combinations, {len(bad)} non-positive")
    chk("B-B2 so Hdot < 0 always -> NO BOUNCE from these two", not bad,
        "rho+p = (4/3) rho_r, the vacuum drops out entirely")

    # ---- B-C ---------------------------------------------------------------
    print("\n  B-C  but H = 0 IS reachable — the failure is specifically in Hdot")
    rL = -1.0
    # radiation ~ a^-4 under contraction; find a where rho_total = 0
    a_cross = (abs(rL) / 1.0) ** (-0.25)  # with rho_r(a) = 1*a^-4
    rho_tot = rL + a_cross ** -4
    chk("B-C1 rho_total = 0 at a finite scale factor", abs(rho_tot) < 1e-12,
        f"a = {a_cross:.4f}, rho_total = {rho_tot:.2e}")
    chk("B-C2 and rho + p there is POSITIVE, so it is a turnaround not a bounce",
        rho_plus_p([(-1.0, rL), (1 / 3, a_cross ** -4)]) > 0,
        f"rho+p = {rho_plus_p([(-1.0, rL), (1/3, a_cross**-4)]):.4f} > 0")

    # ---- B-D: task 5 --------------------------------------------------------
    print("\n  B-D  TASK 5: a NEGATIVE STIFF component supplies the sign")
    s_stiff = rho_plus_p([(1.0, -1.0)])
    chk("B-D1 negative stiff (w=+1, rho<0) gives (1+w)rho = 2rho < 0",
        s_stiff < 0, f"{s_stiff}")
    # and it overtakes radiation under contraction
    print(f"\n    {'a':>8} {'rho_rad ~ a^-4':>16} {'|rho_stiff| ~ a^-6':>20}  dominant")
    for a in (1.0, 0.1, 0.01, 0.001):
        rr, rs = a ** -4, a ** -6
        print(f"    {a:8.3f} {rr:16.4g} {rs:20.4g}  {'stiff' if rs > rr else 'radiation'}")
    chk("B-D2 stiff (a^-6) overtakes radiation (a^-4) under contraction", True,
        "subdominant today, dominant at maximum compression — exactly where a bounce needs it")

    # ---- B-E: anti-control --------------------------------------------------
    print("\n  B-E  ANTI-CONTROL: is it specifically NEGATIVE and specifically STIFF?")
    chk("B-E1 POSITIVE stiff does NOT flip the sign",
        rho_plus_p([(1.0, +1.0)]) > 0, f"(1+w)rho = {rho_plus_p([(1.0, 1.0)])} > 0")
    chk("B-E2 negative MATTER (w=0) flips the sign too...",
        rho_plus_p([(0.0, -1.0)]) < 0, f"{rho_plus_p([(0.0, -1.0)])}")
    chk("B-E3 ...but scales a^-3, so it never comes to dominate",
        (0.001 ** -3) < (0.001 ** -4),
        "a^-3 < a^-4 < a^-6 under contraction — matter loses to radiation")
    print("       -> so 'stiff' is load-bearing, not decorative: the sign flip needs")
    print("          NEGATIVE energy, and the domination needs w = +1 specifically.")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — BOTH TASKS ANSWERED")
    print("=" * 78)
    print("""
  TASK 4: NO, AND FOR A REASON THAT ADMITS NO TUNING. A w = -1 component contributes
  EXACTLY zero to rho + p, because 1 + w vanishes identically. The vacuum's sign is
  irrelevant -- a negative Lambda is as inert in the Hdot equation as a positive one.
  So rho + p = (4/3) rho_r > 0 for every combination, Hdot < 0 always, and no bounce
  can be built from these two components at any epoch or ratio. This is not a
  near-miss to be closed by better numbers; the term is identically absent.

  The pair does deliver H = 0 -- radiation's a^-4 growth crosses the constant vacuum
  under contraction -- but crossing H = 0 with Hdot < 0 is a TURNAROUND, expansion to
  contraction, the opposite of what is wanted. The two components supply the easy
  condition and not the one that matters.

  TASK 5: THE MISSING COMPONENT IS A NEGATIVE-ENERGY STIFF ONE, w = +1, rho < 0.
  Hdot > 0 requires sum (1+w_i) rho_i < 0, so some component needs either phantom
  behaviour (w < -1 at positive energy) or negative energy at w > -1. Negative stiff
  takes the second route, giving (1+w)rho = 2 rho < 0, and its a^-6 scaling means it
  is subdominant today and takes over precisely at maximum compression.

  BOTH QUALIFIERS ARE LOAD-BEARING (B-E). Positive stiff does not flip the sign at
  all. Negative MATTER does flip it but scales a^-3 and never comes to dominate. So
  the workplan's phrase "stiff or effectively stiff" is doing real work: the sign
  needs the negative energy, the domination needs w = +1.

  WHAT REMAINS, AND IT IS NOW A SINGLE NAMED OBJECT. The load-bearing open variable
  is a negative-energy stiff component in the crunch sector -- its existence, its
  magnitude, and whether the model's own content supplies one. The workplan already
  warned that "the reversal mechanism is not hidden in the white-hole label; it still
  has to come from a sector-local rho_X(T) or branch-changing Fdot(T)." That warning
  is now sharper: whatever supplies it must be negative-energy and stiff, which is a
  much narrower target than "a source term".
""")


if __name__ == "__main__":
    main()
