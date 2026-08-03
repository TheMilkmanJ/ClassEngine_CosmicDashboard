#!/usr/bin/env python3
"""
*** WITHDRAWN 2026-07-29, THE SAME DAY IT WAS WRITTEN. DO NOT CITE. ***
*** SUPERSEDED BY scripts/delivery_law_two_parameters.py                          ***

This script reads eps_D/eps_S as a ratio of ENERGIES deposited per sector. It is a
ratio of STIFFNESSES. koide_frame_bridge.py writes amplitude^2 = g * T / eps and
koide_delivery_law_discriminator.py writes w ~ sqrt(eps) and <f^2> ~ 1/eps; both are
unambiguous and both predate this file. Fitting the four recorded numbers with a
quantity that is not the one they denote is protocol 42.

The two constructions agree at p = 0 and NOWHERE ELSE, so every conclusion below
that rests on the p = 1/2 or p = 1 entries is void: the corpus's sqrt2 is the sudden
quench (p = -1), the zero-point law gives 4 and is absent from the recorded set, and
"equal amplitude" is the null itself rather than a delivery law. The correct family
is two-parameter, eps_1/eps_0 = 2^(s/(1-p)), and Q = 2/3 singles out thermal
equipartition uniquely.

The file is kept, unrepaired, because the failures ledger records the error and this
is the object it refers to. Its controls all PASSED -- that is the point. They tested
whether the family fitted; none could test whether eps meant what it computed.

--- original header follows ---------------------------------------------------

#85: the four energy-delivery laws are ONE exponent, and one of the four is a
bookkeeping duplicate.

THE DOCKET. Four delivery laws are in use across the corpus, giving the
doublet-to-singlet energy ratio eps_D/eps_S in {2, sqrt2, 1, 1/2}, and nothing
selects among them. It is flagged HIGHEST-LEVERAGE because the null the Koide
sector hangs from is read through whichever law is right.

THE OBSERVATION. Those are not four mechanisms. The ring's normal modes are the
breathing singlet (k_S = 6, multiplicity 1) and the shape doublet (k_D = 3,
multiplicity 2), stiffness ratio exactly 2 and therefore frequency ratio sqrt2.
Write the energy deposited per MODE as

    eps_mode  ~  k^p

and let the sector energy be the per-mode value times the multiplicity. Then every
recorded law appears, at p = 0, 1/2, 1:

    p = 0    per sector : 2 * (k_D/k_S)^0    = 2        <- classical equipartition
    p = 1/2  per sector : 2 * (k_D/k_S)^0.5  = sqrt2    <- zero-point, (1/2) hbar omega
    p = 1    per sector : 2 * (k_D/k_S)^1    = 1        <- equal amplitude
    p = 1    per MODE   :     (k_D/k_S)^1    = 1/2      <- the SAME law, not summed

TWO CONSEQUENCES.

  (A) THERE ARE THREE LAWS, NOT FOUR. The 1 and the 1/2 are the same p = 1 physics
      quoted with and without the doublet's multiplicity. That is a bookkeeping
      convention, not a competing mechanism, and carrying it as a fourth option
      overstates the size of the fork.

  (B) THE DISCRIMINATING QUESTION IS A SINGLE EXPONENT: how does the deposited
      energy scale with mode stiffness? p = 0 means the deposit is classical and
      thermal (equal per degree of freedom); p = 1/2 means it is quantum and
      zero-point-like (equal quanta, (1/2) hbar omega per mode); p = 1 means every
      mode is left with the same AMPLITUDE. That is one physical question with three
      named answers, which is a far better-posed problem than four numbers.

WHERE THAT LEAVES THE FORK. scripts/koide_delivery_law_discriminator.py already put
the classical thermal reading under heavy pressure: at the corpus's own frequency it
distorts Q by 1025 ppm against a 6 ppm budget, and its own verdict was that "the
classical equipartition reading of the null is the one under pressure". That is
p = 0. So the live fork is p = 1/2 against p = 1 -- and the discriminator's named
survivor, the occupancy lock, is a cold quantum law, i.e. p = 1/2 territory.

PRE-STATED CONTROLS:
  D-A  the stiffnesses and their ratio must be the recorded ones (k_S/k_D = 2), and
       the frequency ratio must follow as sqrt2.
  D-B  all four recorded values must be reproduced by the single family, exactly.
  D-C  the 1 and the 1/2 must be shown to differ ONLY by the multiplicity factor,
       i.e. the same p.
  D-D  ANTI-CONTROL, and the one that matters: the family must NOT be able to fit
       arbitrary numbers at p in {0, 1/2, 1}. If it could, "they are one family"
       would be vacuous. Check that plausible other ratios (3, 1/3, 4) are NOT
       produced at any of the three exponents, in either convention.
"""

import math

K_S, K_D = 6.0, 3.0
N_S, N_D = 1, 2
TOL = 1e-12

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def ratio(p, per_sector=True):
    r = (K_D / K_S) ** p
    return (N_D / N_S) * r if per_sector else r


def main():
    print("=" * 78)
    print("  #85 — THE FOUR DELIVERY LAWS ARE ONE EXPONENT")
    print("=" * 78)

    # ---- D-A ---------------------------------------------------------------
    print("\n  D-A  the recorded mode structure")
    chk("D-A1 k_S/k_D = 2 exactly", abs(K_S / K_D - 2) < TOL, f"{K_S}/{K_D}")
    chk("D-A2 so omega_S/omega_D = sqrt2",
        abs(math.sqrt(K_S) / math.sqrt(K_D) - math.sqrt(2)) < TOL)
    chk("D-A3 multiplicities: singlet 1, doublet 2", (N_S, N_D) == (1, 2))

    # ---- D-B ---------------------------------------------------------------
    print("\n  D-B  every recorded law is eps_mode ~ k^p")
    cases = [("p=0   classical equipartition (per DOF)", 0.0, True, 2.0),
             ("p=1/2 zero-point, (1/2)hbar omega per mode", 0.5, True, math.sqrt(2)),
             ("p=1   equal amplitude, per sector", 1.0, True, 1.0),
             ("p=1   equal amplitude, per MODE", 1.0, False, 0.5)]
    print(f"\n    {'law':<44} {'predicted':>10} {'recorded':>10}")
    for nm, p, sec, rec in cases:
        got = ratio(p, sec)
        print(f"    {nm:<44} {got:10.6f} {rec:10.6f}")
        chk(f"D-B [{nm.split()[0]}{'' if sec else ' per-mode'}] reproduces {rec:.4f}",
            abs(got - rec) < 1e-9)

    # ---- D-C ---------------------------------------------------------------
    print("\n  D-C  the 1 and the 1/2 are the SAME law")
    chk("D-C1 they share p = 1", True, "identical exponent")
    chk("D-C2 and differ by exactly the doublet multiplicity",
        abs(ratio(1.0, True) / ratio(1.0, False) - N_D) < TOL,
        f"{ratio(1.0,True):.6f} / {ratio(1.0,False):.6f} = {N_D}")
    print("       -> so the fork has THREE branches, not four; carrying the 1/2 as a")
    print("          separate mechanism overstates it.")

    # ---- D-D: the anti-control ---------------------------------------------
    print("\n  D-D  ANTI-CONTROL: can the family fit arbitrary numbers?")
    strays = [3.0, 1.0 / 3.0, 4.0, 0.75]
    hits = []
    for target in strays:
        for p in (0.0, 0.5, 1.0):
            for sec in (True, False):
                if abs(ratio(p, sec) - target) < 1e-9:
                    hits.append((target, p, sec))
    chk("D-D1 none of {3, 1/3, 4, 0.75} is produced at p in {0, 1/2, 1}",
        not hits, f"stray hits: {hits}")
    print("       -> the family is constrained: it lands on the four recorded values")
    print("          and not on nearby plausible ones, so the unification is not vacuous.")
    # what p WOULD be needed for a stray, to show they are off-lattice
    for target in (3.0, 1.0 / 3.0):
        p_need = math.log(target / (N_D / N_S)) / math.log(K_D / K_S)
        print(f"          (ratio {target:.4f} would need p = {p_need:+.4f} — not in the set)")

    # ---- D-E: WHICH sector does the law act on? ----------------------------
    # The spec (C3) warns explicitly that the RADIAL Hessian stiffnesses
    # (k_S = 6, k_D = 3, ratio 2) and the CIRCULANT AMPLITUDE stiffnesses
    # (eps_0 = a+2b, eps_1 = a-b) are different objects and must not be identified.
    # The family above was built on the radial pair. Does the choice matter, and
    # does it tell us which sector the delivery law is a statement about?
    print("\n  D-E  which sector is the delivery law a statement about?")
    r = 1 / math.sqrt(2)                 # |b|/a at the Koide point
    e0, e1 = 1 + 2 * r, 1 - r            # amplitude stiffnesses (a = 1)
    chk("D-E1 the two sectors have genuinely different ratios",
        abs((e0 / e1) - 8.242640687) < 1e-6 and abs(K_S / K_D - 2) < TOL,
        f"radial 2.000 vs amplitude {e0/e1:.4f}")
    # do the recorded values survive in the amplitude sector?
    amp = {p: (N_D / N_S) * (e1 / e0) ** p for p in (0.0, 0.5, 1.0)}
    rec = {0.0: 2.0, 0.5: math.sqrt(2), 1.0: 1.0}
    ok_amp = all(abs(amp[p] - rec[p]) < 1e-6 for p in rec)
    chk("D-E2 the amplitude sector does NOT reproduce the recorded values",
        not ok_amp,
        f"p=1/2 gives {amp[0.5]:.4f} (recorded sqrt2), p=1 gives {amp[1.0]:.4f} (recorded 1)")
    chk("D-E3 the radial sector DOES, exactly",
        all(abs((N_D / N_S) * (K_D / K_S) ** p - rec[p]) < 1e-9 for p in rec))
    print("       -> so the recorded laws are RADIAL-sector statements. That is not an")
    print("          assumption here; it is forced, because no other sector reproduces")
    print("          the numbers the corpus already carries. (Note p = 0 cannot")
    print("          discriminate — k^0 = 1 in any sector — so the discrimination rests")
    print("          entirely on the p = 1/2 and p = 1 entries.)")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT")
    print("=" * 78)
    print("""
  THE FORK IS SMALLER AND BETTER POSED THAN RECORDED.

  All four "competing laws" are eps_mode ~ k^p on the ring's own mode structure,
  at p = 0, 1/2, 1 — with the 1 and the 1/2 being the SAME p = 1 law quoted with
  and without the doublet's multiplicity. So there are THREE mechanisms, not four,
  and one entry on the list was a bookkeeping duplicate.

  THE WHOLE QUESTION IS ONE EXPONENT: how does deposited energy scale with mode
  stiffness?
      p = 0    classical and thermal — equal energy per degree of freedom
      p = 1/2  quantum and cold — equal QUANTA, (1/2) hbar omega per mode
      p = 1    equal AMPLITUDE — every mode left with the same <|f|^2>

  AND ONE BRANCH IS ALREADY UNDER PRESSURE. The delivery-law discriminator showed
  the classical thermal reading distorts Q by 1025 ppm against a 6 ppm budget, and
  concluded the classical equipartition reading is the one under pressure. That is
  p = 0. The live fork is therefore p = 1/2 against p = 1, and the discriminator's
  named survivor — the occupancy lock, a cold quantum law — sits at p = 1/2.

  WHAT THIS DOES NOT DO. It does not derive p. Kibble–Zurek would fix it (the quench
  determines which spectrum is frozen in) and so would the ring-BEC bench, and
  neither is attempted here. But the target has changed shape: from "choose among
  four numbers" to "determine one exponent, with one branch already disfavoured".
""")


if __name__ == "__main__":
    main()
