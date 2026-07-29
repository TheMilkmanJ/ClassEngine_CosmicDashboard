#!/usr/bin/env python3
"""
Owner-queue item 4: "the junction quartet misses closure by nine, and #39's target
may be the wrong number."

THE CLAIM ON THE BOOKS.  Baryogenesis records four numbers:

    omega_J    ~ 5.7 keV      (junction plasma frequency at T_sph)
    j          ~ 6 meV        (= omega_J^2 / Gamma_phi)
    Gamma_phi/thetadot ~ 1e7  (the overdamping ratio)
    R          ~ 5e-5         (the needed rectified transmission)

Since R = j/(2 thetadot), omega_J cancels and four numbers constrain three
unknowns.  The queue reports the system missing closure by 9.03 -- or
equivalently omega_J low by 3.004 -- and warns that #39's 5.7 keV target may be
wrong, with 1.90 keV the "internally consistent" value.

THE SUSPICION TESTED HERE.  Protocol entry 40 was written this same day about a
factor inferred from a rounded intermediate.  "Gamma_phi/thetadot ~ 1e7" is quoted
to an ORDER OF MAGNITUDE.  So before accepting a factor-9 physics discrepancy,
compute the ratio from its own sourced inputs and see what it actually is.

Pre-stated control: Gamma_phi must reproduce the recorded 5.4e9 eV from
G_F^2 T^5 at T_sph before any conclusion is drawn from it.
"""

import math

# ---- sourced inputs --------------------------------------------------------
G_F = 1.1663787e-5      # GeV^-2, Fermi constant (PDG)
T_SPH_GEV = 131.7       # GeV, sphaleron freeze-out (dORT)
THETADOT = 59.68        # eV, = m*(T_sph/T_on)^3  (corrected value, this session)
OMEGA_J_KEV = 5.7       # keV, the recorded #39 target
R_NEEDED = 5e-5         # the reservoir-implied transmission

# ---- recorded shorthand, as the owner queue quotes it ----------------------
RATIO_QUOTED = 1e7      # "Gamma_phi/thetadot ~ 1e7"
J_QUOTED = 6e-3         # eV, "j ~ 6 meV"


def main():
    print("=" * 76)
    print("  Does the junction quartet actually miss closure?")
    print("=" * 76)

    # ---- control ----------------------------------------------------------
    gamma_gev = G_F**2 * T_SPH_GEV**5
    gamma_ev = gamma_gev * 1e9
    print(f"\n  CONTROL: Gamma_phi = G_F^2 T^5 at T_sph")
    print(f"    = ({G_F:.6e})^2 * ({T_SPH_GEV})^5 = {gamma_gev:.4f} GeV = {gamma_ev:.4e} eV")
    print(f"    recorded value 5.4e9 eV -> "
          f"{'PASS' if abs(gamma_ev-5.4e9)/5.4e9 < 0.02 else 'FAIL'}")

    # ---- the ratio, computed rather than quoted ---------------------------
    ratio = gamma_ev / THETADOT
    print(f"\n  THE OVERDAMPING RATIO, COMPUTED FROM ITS OWN INPUTS:")
    print(f"    Gamma_phi/thetadot = {gamma_ev:.4e} / {THETADOT} = {ratio:.4e}")
    print(f"    the owner queue quotes this as ~{RATIO_QUOTED:.0e}")
    print(f"    RATIO OF THE TWO: {ratio/RATIO_QUOTED:.3f}")
    print(f"    -- and the queue's reported shortfall is 9.03.")
    print(f"    The transfer-integral spec itself states 'overdamped by 9e7',")
    print(f"    so the 9 was present in the source and dropped in the shorthand.")

    # ---- does the quartet close on the computed ratio? --------------------
    print(f"\n  CLOSURE TEST, using the COMPUTED ratio:")
    omega_j = OMEGA_J_KEV * 1e3
    j = omega_j**2 / gamma_ev
    R = j / (2 * THETADOT)
    R_direct = omega_j**2 / (2 * gamma_ev * THETADOT)
    print(f"    j = omega_J^2/Gamma_phi = {omega_j:.0f}^2 / {gamma_ev:.4e}"
          f" = {j:.4e} eV = {j*1e3:.3f} meV")
    print(f"      recorded j ~ {J_QUOTED*1e3:.0f} meV -> "
          f"{'MATCH' if abs(j-J_QUOTED)/J_QUOTED < 0.05 else 'MISMATCH'}")
    print(f"    R = j/(2*thetadot) = {R:.4e}")
    print(f"    R = omega_J^2/(2*Gamma_phi*thetadot) = {R_direct:.4e}  (same, as it must be)")
    print(f"      needed R ~ {R_NEEDED:.0e} -> "
          f"{'MATCH' if abs(R-R_NEEDED)/R_NEEDED < 0.05 else 'MISMATCH'}")

    # ---- what omega_J does the need actually require? ---------------------
    omega_req = math.sqrt(R_NEEDED * 2 * gamma_ev * THETADOT)
    print(f"\n  WHAT omega_J DOES THE NEED REQUIRE?")
    print(f"    omega_J = sqrt(R * 2 * Gamma_phi * thetadot) = {omega_req:.1f} eV"
          f" = {omega_req/1e3:.3f} keV")
    print(f"    #39's stated target: {OMEGA_J_KEV} keV")
    print(f"    agreement: {100*abs(omega_req/1e3-OMEGA_J_KEV)/OMEGA_J_KEV:.1f}% -- the target is RIGHT")

    # ---- the queue's alternative --------------------------------------
    print(f"\n  THE QUEUE'S PROPOSED 'internally consistent' 1.90 keV:")
    om_alt = 1.90e3
    R_alt = om_alt**2 / (2 * gamma_ev * THETADOT)
    print(f"    would give R = {R_alt:.4e}, i.e. {R_NEEDED/R_alt:.2f}x SHORT of the need")
    print(f"    -- that value is what you get by imposing the ROUNDED ratio 1e7;")
    print(f"       it is an artifact of the shorthand, not a physical alternative.")

    print("\n" + "=" * 76)
    print(f"""  VERDICT: THE QUARTET CLOSES.  There is no factor-9 discrepancy.

  Gamma_phi/thetadot is {ratio/1e7:.2f}e7, NOT 1e7.  The transfer-integral spec records it
  correctly ("overdamped by 9e7"); the owner-queue summary compressed it to an
  order of magnitude, and the missing 9.03 is exactly that compression.  With the
  computed ratio, all four numbers agree simultaneously:

      omega_J = {OMEGA_J_KEV} keV  ->  j = {j*1e3:.2f} meV  ->  R = {R:.3e}  vs needed {R_NEEDED:.0e}

  CONSEQUENCES:
    * owner-queue item 4 dissolves -- nothing needs to move, no ruling required;
    * #39's target of 5.7 keV is CORRECT and should be graded against;
    * the 1.90 keV alternative is an artifact of the rounded ratio and should NOT
      be adopted -- a derivation landing there would be 9x short of the need.

  This is protocol 40's failure mode for the second time in one day: a factor
  inferred from a quantity quoted to one figure, then attributed to physics.
""")
    print("=" * 76)


if __name__ == "__main__":
    main()
