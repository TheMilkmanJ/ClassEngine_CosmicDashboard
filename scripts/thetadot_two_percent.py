#!/usr/bin/env python3
"""
#51's residual: the "two-percent disagreement between two recorded values of theta-dot".

PRTOE_hierarchy_problem.md sec 6f rules:
  "The ratio route -- thetadot/H = 2.4e6 with T_sph = 131.7 GeV and g* = 106.75 --
   gives thetadot = 58.5 eV and mu_5 = 29.3 eV; the failures ledger carries
   thetadot = 59.7 eV directly, which would require g* = 111.1 and has no stated
   derivation.  THE DERIVED VALUE HAS THE BETTER PROVENANCE, each of its inputs
   being sourced."

But the_transfer_integral_spec.md stage 5 states a derivation for 59.7:
   thetadot = m * (T_sph/T_on)^3   (deep-frozen condensate, theta-dot ~ a^-3)

So the question is which number is the derived one and which is the artifact.

Pre-stated control: H(T_sph) must reproduce the recorded 2.44e-5 eV from the
standard radiation-era formula at g* = 106.75.  If it does not, nothing below is
trustworthy.
"""

import math

# ---- recorded inputs -------------------------------------------------------
M_PL = 1.220890e28        # eV, Planck mass
T_SPH = 131.7e9           # eV, sphaleron freeze-out (dORT)
GSTAR = 106.75            # SM relativistic dof at T_sph
M_FIELD = 2.24e-20        # eV, the fluid's mass
RATIO_RECORDED = 2.4e6    # thetadot/H as recorded (TWO significant figures)
THETADOT_LEDGER = 59.7    # eV, the failures-ledger / stage-5 value
THETADOT_RATIO = 58.5     # eV, the hierarchy file's "ratio route" value


def hubble(T, gstar):
    return 1.66 * math.sqrt(gstar) * T * T / M_PL


def main():
    print("=" * 74)
    print("  #51 residual: which theta-dot is derived and which is an artifact?")
    print("=" * 74)

    H = hubble(T_SPH, GSTAR)
    print(f"\n  CONTROL: H(T_sph) = 1.66*sqrt(g*)*T^2/M_Pl = {H:.4e} eV")
    print(f"           recorded value 2.44e-5 eV -> "
          f"{'PASS' if abs(H - 2.44e-5)/2.44e-5 < 0.01 else 'FAIL'}")

    # ---- route 1: back-multiply the recorded ratio -------------------------
    td_from_ratio = RATIO_RECORDED * H
    print(f"\n  ROUTE 1 (the hierarchy file's 'ratio route'):")
    print(f"    thetadot = (thetadot/H) * H = {RATIO_RECORDED:.1e} * {H:.4e} "
          f"= {td_from_ratio:.2f} eV   (file says 58.5)")

    # ---- route 2: the direct scaling ---------------------------------------
    print(f"\n  ROUTE 2 (stage 5's direct scaling, thetadot = m*(T_sph/T_on)^3):")
    print(f"    {'T_on (keV)':>12} {'thetadot (eV)':>15} {'thetadot/H':>13}")
    for T_on_keV in (9.41, 9.46, 9.50, 9.56):
        T_on = T_on_keV * 1e3
        td = M_FIELD * (T_SPH / T_on) ** 3
        mark = "   <-- reproduces 59.7" if abs(td - THETADOT_LEDGER) < 0.1 else ""
        print(f"    {T_on_keV:12.2f} {td:15.2f} {td/H:13.4e}{mark}")

    # ---- the resolution -----------------------------------------------------
    exact_ratio = THETADOT_LEDGER / H
    print(f"\n  THE RESOLUTION:")
    print(f"    the EXACT ratio implied by thetadot = {THETADOT_LEDGER} eV is "
          f"{exact_ratio:.4e}")
    print(f"    the spec records that as '{RATIO_RECORDED:.1e}' -- TRUNCATED at two")
    print(f"    figures, not rounded (2.45 rounds up to 2.5, so this is a floor)")
    print(f"    back-multiplying the truncated ratio loses "
          f"{100*(exact_ratio-RATIO_RECORDED)/exact_ratio:.2f}%")
    print(f"    and {THETADOT_LEDGER} * (1 - {100*(exact_ratio-RATIO_RECORDED)/exact_ratio:.4f}/100)"
          f" = {THETADOT_LEDGER*RATIO_RECORDED/exact_ratio:.2f} eV = the '58.5'")

    # ---- the g* claim, checked ---------------------------------------------
    # the file says 59.7 "would require g* = 111.1"
    gstar_needed = (THETADOT_LEDGER / (RATIO_RECORDED * 1.66 * T_SPH**2 / M_PL)) ** 2
    print(f"\n  THE FILE'S g* CLAIM, CHECKED:")
    print(f"    holding thetadot/H = {RATIO_RECORDED:.1e} FIXED and forcing "
          f"thetadot = {THETADOT_LEDGER}:")
    print(f"      g* would have to be {gstar_needed:.1f}   (the file says 111.1)")
    print(f"    -- but that inference assumes the ratio is exact.  It is quoted to")
    print(f"       two figures, so it cannot carry a 2% inference at all.")

    print("\n" + "=" * 74)
    print("""  VERDICT: the file's provenance ruling is INVERTED.

    59.7 eV is the derived number: thetadot = m*(T_sph/T_on)^3 with m, T_sph and
    T_on = 9.5 keV all recorded (the_transfer_integral_spec.md stage 5).  It does
    NOT require g* = 111.1 and it does NOT lack a stated derivation.

    58.5 eV is the artifact: it is 59.7 back-multiplied out of a ratio that was
    only ever quoted to two significant figures.  The '2% disagreement' is the
    rounding error of 2.4e6 against the exact 2.448e6, and nothing else.

    The sentence 'the derived value has the better provenance, each of its inputs
    being sourced' is true -- of the OTHER number.

  Consequence for mu_5 = thetadot/2:  29.85 eV, not 29.3 eV.
""")
    print(f"  Also worth naming: T_on is carried at 9.41, 9.46 and 9.5 keV in")
    print(f"  different files, a {100*(9.5-9.41)/9.41:.1f}% spread that propagates as")
    print(f"  {100*((9.5/9.41)**3-1):.1f}% in thetadot (cubed).  That is the real")
    print(f"  uncertainty here, and it is larger than the 'disagreement' being ruled on.")
    print("=" * 74)


if __name__ == "__main__":
    main()
