"""Can the dark-energy floor keep d = 3 while alpha_c moves into the indirect band?

That was the cheapest of the three ways out of the three-way conflict: perhaps the floor's
d^2/2 is an independent geometry factor that merely shares a symbol with the coupling's d, in
which case alpha_c could drift down to satisfy the band while the floor kept its 9/2.

The test is algebraic, not empirical. The floor is recorded in two forms:

    E_b = (1/2) alpha_c^2 M_2        with M_2 = alpha^2 T_c        <- the primary form
    rho^(1/4) = (d^2/2) alpha^4 T_c                                 <- the substituted form

Substituting alpha_c = d.alpha into the first gives the second exactly. So the d^2 in the
second form is not a separate input: it is alpha_c^2/alpha^2. Whatever alpha_c is, the floor
carries its square.

Run: python3 scripts/d_escape_route_test.py
"""
import math

ALPHA = 1 / 137.035999084
T_C = 0.5 * math.log(2) * 0.51099895e6      # eV
M_2 = ALPHA**2 * T_C                        # eV
RHO_OBS = 2.25e-3                           # eV
BAND_LO, BAND_HI = 0.0205, 0.0214
AC_ANCHOR = 0.021316
AC_THEORY = 3.0 * ALPHA


def floor_from(alpha_c):
    """E_b = (1/2) alpha_c^2 M_2, in eV. The primary form -- no d anywhere."""
    return 0.5 * alpha_c**2 * M_2


print("=" * 76)
print("THE TWO FORMS ARE ONE FORM")
print("=" * 76)
d = 3.0
via_primary = floor_from(d * ALPHA)
via_substituted = (d * d / 2) * ALPHA**4 * T_C
print(f"  M_2 = alpha^2 T_c                       {M_2:.4f} eV   (recorded 9.43)")
print(f"  E_b = (1/2) alpha_c^2 M_2 at alpha_c=3a {via_primary*1e3:.6f} meV")
print(f"  (d^2/2) alpha^4 T_c at d = 3            {via_substituted*1e3:.6f} meV")
print(f"  difference                              {abs(via_primary-via_substituted)*1e3:.2e} meV")
print()
print("  Identical, because the second IS the first with alpha_c = d.alpha substituted.")
print("  The d^2 is alpha_c^2/alpha^2. There is no independent geometry factor to hold")
print("  fixed while the coupling moves — so the escape route is closed.")

print()
print("=" * 76)
print("WHAT THE FLOOR DEMANDS OF alpha_c DIRECTLY, WITH d NEVER MENTIONED")
print("=" * 76)
ac_obs = math.sqrt(2 * RHO_OBS / M_2)
print(f"  observed rho^(1/4) = {RHO_OBS*1e3:.3f} meV  ->  alpha_c = sqrt(2 rho / M_2) = {ac_obs:.6f}")
print(f"  the indirect band caps alpha_c at                                {BAND_HI:.6f}")
print(f"  the observation therefore exceeds the band by"
      f"                     {(ac_obs/BAND_HI - 1)*100:.2f}%")

print()
print("=" * 76)
print("THE FOUR VALUES OF alpha_c, IN TWO PAIRS")
print("=" * 76)
print(f"  {'source':<40} {'alpha_c':>10}  {'rho^(1/4) [meV]':>16}")
print("  " + "-" * 70)
for name, ac in (("the spatial dimension, d = 3", AC_THEORY),
                 ("the observed dark-energy density", ac_obs),
                 ("the indirect band, top", BAND_HI),
                 ("the hierarchy anchor's exact landing", AC_ANCHOR),
                 ("the indirect band, bottom", BAND_LO)):
    print(f"  {name:<40} {ac:10.6f}  {floor_from(ac)*1e3:16.4f}")
print()
print(f"  The first two agree to {abs(AC_THEORY/ac_obs - 1)*100:.2f}% — that agreement IS the floor's +0.44%,")
print(f"  since rho goes as alpha_c^2. The last two agree to {abs(BAND_HI/AC_ANCHOR - 1)*100:.2f}%. The two PAIRS")
print(f"  differ by {(AC_THEORY/AC_ANCHOR - 1)*100:.2f}%, and no choice of d reconciles them, because d is not")
print("  a free label — it is the ratio alpha_c/alpha itself.")

print()
print("=" * 76)
print("WHAT SURVIVES")
print("=" * 76)
print("  Of the three ways out, the middle one is now closed: the floor's d^2/2 and the")
print("  coupling's d are the same quantity by construction, not by a naming coincidence.")
print("  Two remain, and they are both empirical rather than algebraic:")
print()
print(f"    (a) the indirect band [{BAND_LO}, {BAND_HI}] is wrong, or applies to a different")
print("        quantity than the coupling the floor uses;")
print("    (c) the floor's agreement with observation is a coincidence — alpha_c really does")
print(f"        sit near {AC_ANCHOR:.4f}, and the floor's landing at {floor_from(AC_ANCHOR)*1e3:.3f} meV against 2.25 is")
print(f"        a {abs(floor_from(AC_ANCHOR)/RHO_OBS - 1)*100:.0f}% miss that the d = 3 arithmetic disguised.")
print()
print("  Those are decidable by measurement, and they point in opposite directions, so the")
print("  conflict is now a live fork rather than an unexplained tension.")
