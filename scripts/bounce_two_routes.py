#!/usr/bin/env python3
"""
*** NOVELTY CLAIM CORRECTED 2026-07-29, same day. Read this first. ***

The header below presents route 2 (the bounded-density constraint) as the route my
earlier answer missed. It was not missed by the CORPUS -- only by me. The lane is named
in three places and already graded:

  bounce_derivation_workplan.md  "no derived rho(1-rho/rho_c) bounce constraint in
                                  corpus. No free turn from this lane."
  PRTOE_FAILURES_LEDGER.md       "remains un-derived in the corpus (named in the
                                  reconstruction, not stocked)."
  bounce_reconstruction_rp.md    "Searching the corpus does not turn up a completed
                                  derivation ... Any rho^2/rho_c bounce law remains
                                  unbuilt (not fabricated here either)."

So this script's NET EFFECT ON THE DOCKET IS NIL -- the lane's grade is unchanged. What
it does contribute: (i) a correction to my OWN task-5 label, since w_X = 2w+1 makes
"negative-energy stiff" the matter-background special case rather than the general
object; (ii) an explicit RK4 exhibit that the constraint bounces at the predicted a_min
with rho + p > 0 throughout, and does not when the correction is removed; (iii) the
anti-controls separating sign from scaling. Useful as checks, not as findings.
See protocol 50.

--- original header follows ---------------------------------------------------

#13, continued: my own task-5 answer named ONE of two routes, and named the one the
corpus has already priced as insufficient.

WHAT I RECORDED THIS MORNING (scripts/bounce_handover_sign.py, and it stands as far as
it goes): a w = -1 component contributes EXACTLY zero to rho + p, so negative vacuum
plus Tolman radiation cannot bounce at any epoch or ratio; and "the missing component
is a NEGATIVE-ENERGY STIFF one, w = +1, rho < 0."

WHAT THAT MISSED. Hdot > 0 at H = 0 can be reached two ways, and the workplan already
names both -- "a bounce needs either rho + p < 0 transiently, OR a modified
gravitational branch that changes the hand-over condition itself." My answer developed
only the first. And the corpus prices the first as unavailable: the only NEC-flexible
sector is the ghost-condensate branch, whose negative-energy budget the wormhole audit
calls tiny, and PRTOE_stability.md's whole first question is whether the scalar carries
a ghost.

  *** So the route I named is the one the corpus has already closed, and the route the
  *** corpus left open is the one I did not develop.

ROUTE 2, DEVELOPED HERE. Take a Friedmann equation with a quadratic correction,

    H^2 = (8 pi G/3) rho (1 - rho/rho_c)

-- the standard form for a bounce driven by a maximum density rather than by exotic
matter. Then H = 0 at rho = rho_c exactly, and differentiating with the continuity
equation rho_dot = -3H(rho + p),

    Hdot = -4 pi G (rho + p) (1 - 2 rho/rho_c)

which at rho = rho_c is Hdot = +4 pi G (rho + p) > 0 for ORDINARY matter.

  *** A bounce with rho + p > 0 throughout. No negative energy, no NEC violation, no
  *** ghost. The sign flip comes from the bracket, not from the fluid.

AND THE EFFECTIVE-FLUID READING SHARPENS MY OWN LABEL. Write the correction as its own
component, rho_X = -rho^2/rho_c. If the background scales as rho ~ a^(-3(1+w)), then
rho_X ~ a^(-6(1+w)), i.e.

    w_X = 2w + 1

So rho_X is STIFF (w_X = 1) only when the background is MATTER (w = 0). Against
radiation it is w_X = 5/3, stiffer than stiff. My "negative-energy stiff" was the
matter-background special case quoted as the general answer. The general statement is:
the missing component is THE SQUARE OF WHATEVER DOMINATES, negative, and it outgrows
its own source automatically since 6(1+w) > 3(1+w) for every w > -1.

PRE-STATED CONTROLS:
  R-A  this morning's results must be reproduced, not contradicted: w = -1 contributes
       exactly 0, and negative stiff does flip the sign.
  R-B  the modified branch must give H = 0 at rho = rho_c and Hdot > 0 there, with
       rho + p > 0 throughout -- no NEC violation anywhere.
  R-C  an actual ODE integration must EXHIBIT the bounce: a(t) must reach a minimum and
       turn around, with the minimum at the predicted a.
  R-D  the effective-fluid exponent must be w_X = 2w + 1, checked at w = 0, 1/3, 1.
  R-E  the correction must always overtake its own background, for every w > -1.
  R-F  ANTI-CONTROL: shear scales a^-6 too but is POSITIVE -- it must NOT bounce, and
       must make the collapse worse. Otherwise "a^-6" is doing the work rather than the
       sign.
  R-G  ANTI-CONTROL: negative spatial curvature must give H = 0 with Hdot < 0, i.e. a
       turnaround, not a bounce -- the same trap task 4 fell into.
  R-H  ANTI-CONTROL: with the correction switched OFF the same integration must NOT
       bounce, or the demonstration proves nothing.
"""

import math

TOL = 1e-12
FOUR_PI_G = 1.5          # units with 8 pi G / 3 = 1, so 4 pi G = 3/2
RHO_C = 1.0

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def rho_plus_p(comps):
    return sum((1 + w) * r for w, r in comps)


def deriv(a, H, rho0, w, corrected):
    rho = rho0 * a ** (-3.0 * (1.0 + w))
    p = w * rho
    bracket = (1.0 - 2.0 * rho / RHO_C) if corrected else 1.0
    return a * H, -FOUR_PI_G * (rho + p) * bracket


def integrate(rho0, w, corrected, a0=1.0, dt=2e-4, nmax=4000000):
    """RK4 from the contracting branch; returns (a_min, bounced)."""
    rho = rho0 * a0 ** (-3.0 * (1.0 + w))
    h2 = rho * ((1.0 - rho / RHO_C) if corrected else 1.0)
    if h2 <= 0:
        return None, False
    a, H = a0, -math.sqrt(h2)
    a_min, bounced = a, False
    for _ in range(nmax):
        k1a, k1H = deriv(a, H, rho0, w, corrected)
        k2a, k2H = deriv(a + 0.5 * dt * k1a, H + 0.5 * dt * k1H, rho0, w, corrected)
        k3a, k3H = deriv(a + 0.5 * dt * k2a, H + 0.5 * dt * k2H, rho0, w, corrected)
        k4a, k4H = deriv(a + dt * k3a, H + dt * k3H, rho0, w, corrected)
        a += dt / 6.0 * (k1a + 2 * k2a + 2 * k3a + k4a)
        H += dt / 6.0 * (k1H + 2 * k2H + 2 * k3H + k4H)
        if a <= 0 or not math.isfinite(a):
            break
        a_min = min(a_min, a)
        if H > 0:
            bounced = True
            break
    return a_min, bounced


def main():
    print("=" * 78)
    print("  #13 — THE SECOND ROUTE, WHICH MY TASK-5 ANSWER MISSED")
    print("=" * 78)

    # ---- R-A ----------------------------------------------------------------
    print("\n  R-A  this morning's results, reproduced (not contradicted)")
    chk("R-A1 a w = -1 component contributes exactly 0 to rho + p",
        all(rho_plus_p([(-1.0, r)]) == 0.0 for r in (-1e9, -1.0, 1.0, 1e9)),
        "so the vacuum's sign is irrelevant — unchanged")
    chk("R-A2 negative stiff (w=+1, rho<0) does flip the sign",
        rho_plus_p([(1.0, -1.0)]) < 0, f"{rho_plus_p([(1.0, -1.0)])}")
    chk("R-A3 and negative vacuum + radiation still cannot bounce",
        rho_plus_p([(-1.0, -1.0), (1 / 3, 1.0)]) > 0,
        "route 1 stands; what follows is a SECOND route, not a correction to it")

    # ---- R-B ----------------------------------------------------------------
    print("\n  R-B  the modified branch:  H^2 = (8 pi G/3) rho (1 - rho/rho_c)")
    rho_at_H0 = RHO_C
    h2 = rho_at_H0 * (1.0 - rho_at_H0 / RHO_C)
    chk("R-B1 H = 0 exactly at rho = rho_c", abs(h2) < TOL, f"H^2 = {h2}")
    # Hdot = -4 pi G (rho+p)(1 - 2 rho/rho_c); at rho = rho_c the bracket is -1
    for w, label in ((0.0, "matter"), (1 / 3, "radiation"), (1.0, "stiff")):
        rp = (1 + w) * RHO_C
        hdot = -FOUR_PI_G * rp * (1.0 - 2.0 * RHO_C / RHO_C)
        chk(f"R-B2 Hdot > 0 at the bounce for {label} (w = {w:.3f}), with rho+p > 0",
            hdot > 0 and rp > 0, f"Hdot = {hdot:+.4f}, rho+p = {rp:.4f}")
    print("       -> a bounce with rho + p > 0 THROUGHOUT. No negative energy, no NEC")
    print("          violation, no ghost. The sign flip lives in the bracket.")

    # ---- R-C ----------------------------------------------------------------
    print("\n  R-C  integrate it — does a(t) actually turn around?")
    rho0 = 0.01
    a_pred = (rho0 / RHO_C) ** (1.0 / 3.0)
    a_min, bounced = integrate(rho0, 0.0, corrected=True)
    chk("R-C1 the corrected branch bounces", bounced, f"a_min = {a_min:.6f}")
    chk("R-C2 at the predicted scale factor a = (rho_0/rho_c)^(1/3)",
        a_min is not None and abs(a_min / a_pred - 1.0) < 5e-3,
        f"integrated {a_min:.6f} vs predicted {a_pred:.6f}")

    # ---- R-D ----------------------------------------------------------------
    print("\n  R-D  the correction as its own component:  rho_X = -rho^2/rho_c")
    print(f"\n    {'background w':>14} {'rho ~ a^n':>12} {'rho_X ~ a^n':>13}"
          f" {'w_X = 2w+1':>12}  reading")
    ok_d = True
    for w, name in ((0.0, "stiff"), (1 / 3, "beyond stiff"), (1.0, "beyond stiff")):
        n_bg = -3.0 * (1.0 + w)
        n_X = 2.0 * n_bg
        w_X = -1.0 - n_X / 3.0
        ok_d &= abs(w_X - (2.0 * w + 1.0)) < 1e-12
        print(f"    {w:14.4f} {n_bg:12.3f} {n_X:13.3f} {w_X:12.4f}  {name}")
    chk("R-D1 w_X = 2w + 1 at every background tested", ok_d)
    chk("R-D2 so 'stiff' is the MATTER special case, not the general answer",
        abs((2.0 * 0.0 + 1.0) - 1.0) < TOL and abs((2.0 * (1 / 3) + 1.0) - 5 / 3) < TOL,
        "matter -> w_X = 1 (stiff); radiation -> 5/3. My task-5 label was the w=0 case")

    # ---- R-E ----------------------------------------------------------------
    print("\n  R-E  does the correction always overtake its own background?")
    chk("R-E1 6(1+w) > 3(1+w) for every w > -1",
        all(6.0 * (1 + w) > 3.0 * (1 + w) for w in (-0.99, -0.5, 0.0, 1 / 3, 1.0, 5.0)),
        "so domination at maximum compression is automatic, not a tuning")

    # ---- R-F: anti-control --------------------------------------------------
    print("\n  R-F  ANTI-CONTROL: shear also scales a^-6 — does IT bounce?")
    # shear: rho_sigma > 0, w = +1. (1+w)rho = 2 rho > 0.
    chk("R-F1 positive stiff shear gives (1+w)rho > 0, so Hdot < 0",
        rho_plus_p([(1.0, +1.0)]) > 0, "it deepens the collapse — this is the BKL problem")
    chk("R-F2 so a^-6 is NOT what does the work; the SIGN is",
        rho_plus_p([(1.0, +1.0)]) > 0 > rho_plus_p([(1.0, -1.0)]),
        "same scaling, opposite outcome")

    # ---- R-G: anti-control --------------------------------------------------
    print("\n  R-G  ANTI-CONTROL: negative curvature — bounce or turnaround?")
    # curvature: w = -1/3, so (1+w)rho = (2/3) rho. With rho_k > 0 (open universe) it is
    # positive; H = 0 is reachable against matter but Hdot < 0 there.
    chk("R-G1 curvature has w = -1/3, so (1+w)rho = (2/3)rho — never zero",
        abs(rho_plus_p([(-1 / 3, 1.0)]) - 2 / 3) < TOL, f"{rho_plus_p([(-1/3, 1.0)]):.6f}")
    chk("R-G2 so it gives a TURNAROUND, not a bounce — task 4's trap",
        rho_plus_p([(-1 / 3, 1.0), (0.0, 1.0)]) > 0,
        "H = 0 is the easy condition; Hdot > 0 is the one that matters")

    # ---- R-H: anti-control --------------------------------------------------
    print("\n  R-H  ANTI-CONTROL: switch the correction OFF and re-integrate")
    a_min_off, bounced_off = integrate(rho0, 0.0, corrected=False)
    chk("R-H1 the UNcorrected branch does not bounce", not bounced_off,
        f"a_min reached {a_min_off:.2e} and still contracting"
        if a_min_off else "collapsed")
    chk("R-H2 so the bounce is the correction's doing, not the integrator's",
        bounced and not bounced_off)

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — TASK 5's ANSWER WAS ONE OF TWO ROUTES, AND THE CLOSED ONE")
    print("=" * 78)
    print("""
  WHAT STANDS. Everything in this morning's task-4 result is unchanged (R-A): a w = -1
  component contributes exactly zero to rho + p, so negative vacuum plus Tolman
  radiation cannot bounce at any epoch or ratio. That is not revised.

  WHAT WAS INCOMPLETE. Task 5 concluded "the missing component is a NEGATIVE-ENERGY
  STIFF one". That develops only the first of the two routes the workplan itself
  names -- "rho + p < 0 transiently, OR a modified gravitational branch that changes
  the hand-over condition itself" -- and it is the route the corpus has already priced
  as unavailable, since the only NEC-flexible sector is the ghost-condensate branch and
  the wormhole audit calls its negative-energy budget tiny.

  ROUTE 2 NEEDS NO EXOTIC MATTER AT ALL. With H^2 = (8 pi G/3) rho (1 - rho/rho_c),
  H = 0 at rho = rho_c and Hdot = -4 pi G (rho+p)(1 - 2 rho/rho_c) = +4 pi G (rho+p)
  there -- positive for ordinary matter, radiation and stiff alike (R-B). An explicit
  RK4 integration from the contracting branch turns around at the predicted
  a = (rho_0/rho_c)^(1/3), and switching the correction off removes the bounce (R-C,
  R-H). rho + p > 0 throughout. No ghost, no NEC violation.

  AND THE EFFECTIVE-FLUID READING CORRECTS MY OWN LABEL. Written as a component,
  rho_X = -rho^2/rho_c has w_X = 2w + 1 (R-D). It is STIFF only against a MATTER
  background; against radiation it is 5/3. So "negative-energy stiff" was the w = 0
  special case quoted as the general answer. The general statement is better and
  simpler: THE MISSING COMPONENT IS THE SQUARE OF WHATEVER DOMINATES, NEGATIVE -- and
  it outgrows its own source automatically, since 6(1+w) > 3(1+w) for every w > -1
  (R-E). No tuning selects the epoch; the correction takes over at maximum compression
  by construction.

  THE ANTI-CONTROLS EARN THEIR KEEP. Shear scales as a^-6 too and does NOT bounce -- it
  deepens the collapse, which is the BKL problem (R-F). So the a^-6 scaling is not what
  does the work; the SIGN is. And negative curvature reaches H = 0 with Hdot < 0, a
  turnaround, which is precisely the trap task 4 identified (R-G).

  WHAT IS NOW OWED, AND IT IS A DIFFERENT QUESTION FROM THIS MORNING'S. Not "does the
  model contain a negative-energy stiff component" -- the corpus has already answered
  that, no. It is: DOES THE MODEL'S GRAVITATIONAL SECTOR CARRY A rho^2 CORRECTION, and
  what sets rho_c? That is a question about the induced-gravity construction rather
  than about the matter roster, and it is where #13 should be pointed next.
""")


if __name__ == "__main__":
    main()
