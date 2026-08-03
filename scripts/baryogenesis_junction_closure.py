"""The junction rectifier's four recorded numbers are over-determined. Do they close?

PRTOE_baryogenesis.md records, for the driven overdamped junction at T_sph:

    omega_J ~ 5.7 keV          the junction plasma frequency (task #39's target)
    j = omega_J^2/Gamma_phi ~ 6 meV
    Gamma_phi/theta_dot ~ 1e7  the overdamping ratio
    R = omega_J^2/(2 Gamma_phi theta_dot)   the rectified ratio
    R needed ~ 5e-5            "the naive ratio R = H/theta_dot = 4.1e-7 sits against the
                                needed ~5e-5, a factor 122"

Four constraints on three unknowns (omega_J, Gamma_phi, theta_dot), so one relation is a
consistency check rather than a definition. This script performs it.

Note the algebra first: substituting Gamma_phi = omega_J^2/j into R collapses it to

    R = j / (2 theta_dot)

so R does not depend on omega_J at all once j is fixed -- omega_J enters only through
Gamma_phi, and cancels.

Run: python3 scripts/baryogenesis_junction_closure.py
"""
import math

OMEGA_J = 5.7e3          # eV
J_REL = 6e-3             # eV
RATIO = 1e7              # Gamma_phi / theta_dot
R_NEEDED = 5.0e-5
R_NAIVE = 4.1e-7         # = H/theta_dot, recorded

print("=" * 76)
print("THE RECORDED NUMBERS")
print("=" * 76)
print(f"  omega_J             {OMEGA_J:.4g} eV   (5.7 keV)")
print(f"  j = omega_J^2/G_phi {J_REL:.4g} eV   (6 meV)")
print(f"  G_phi/theta_dot     {RATIO:.4g}")
print(f"  R needed            {R_NEEDED:.4g}")
print(f"  R naive = H/th_dot  {R_NAIVE:.4g}   -> factor {R_NEEDED/R_NAIVE:.0f} short"
      f"  (recorded: 122)")

print()
print("=" * 76)
print("TAKE THREE, PREDICT THE FOURTH -- ALL FOUR WAYS")
print("=" * 76)
# (a) omega_J, j, ratio -> R
G_a = OMEGA_J**2 / J_REL
th_a = G_a / RATIO
R_a = J_REL / (2 * th_a)
print(f"  (a) from omega_J, j, ratio:")
print(f"        Gamma_phi = {G_a:.4g} eV,  theta_dot = {th_a:.4g} eV")
print(f"        R = {R_a:.4g}   against the needed {R_NEEDED:.4g}"
      f"   -> short by x{R_NEEDED/R_a:.2f}")

# (b) j, ratio, R -> omega_J
th_b = J_REL / (2 * R_NEEDED)
G_b = RATIO * th_b
om_b = math.sqrt(J_REL * G_b)
print(f"  (b) from j, ratio, R:")
print(f"        theta_dot = {th_b:.4g} eV,  Gamma_phi = {G_b:.4g} eV")
print(f"        omega_J = {om_b:.4g} eV = {om_b/1e3:.3f} keV"
f"   against the recorded 5.7 keV -> low by x{OMEGA_J/om_b:.3f}")

# (c) omega_J, j, R -> ratio
th_c = J_REL / (2 * R_NEEDED)
G_c = OMEGA_J**2 / J_REL
print(f"  (c) from omega_J, j, R:")
print(f"        Gamma_phi/theta_dot = {G_c/th_c:.4g}"
      f"   against the recorded 1e7 -> high by x{(G_c/th_c)/RATIO:.2f}")

# (d) omega_J, ratio, R -> j.  R = j/(2 th) and th = (omega_J^2/j)/ratio  =>  j^2 = 2 R omega_J^2/ratio
j_d = math.sqrt(2 * R_NEEDED * OMEGA_J**2 / RATIO)
print(f"  (d) from omega_J, ratio, R:")
print(f"        j = {j_d:.4g} eV = {j_d*1e3:.2f} meV"
      f"   against the recorded 6 meV -> high by x{j_d/J_REL:.3f}")

print()
print("=" * 76)
print("THE MISS IS ONE NUMBER, SEEN FOUR WAYS")
print("=" * 76)
print(f"  R short by            x{R_NEEDED/R_a:.3f}")
print(f"  omega_J low by        x{OMEGA_J/om_b:.3f}   (= sqrt of the R miss)")
print(f"  ratio high by         x{(G_c/th_c)/RATIO:.3f}")
print(f"  j high by             x{j_d/J_REL:.3f}   (= sqrt of the R miss)")
print()
print("  So the quartet misses closure by a clean factor of about 9 in R, equivalently")
print("  3 in omega_J. Which of the three inputs carries it is NOT determined by anything")
print("  recorded: moving omega_J to 1.9 keV closes it, and so does moving the overdamping")
print("  ratio to 9e7, and so does moving j to 18 meV. All three are quoted to one")
print("  significant figure with a leading tilde.")
print()
print("  What this costs task #39. Its target is stated as 'derive omega_J, needs ~5.7 keV'")
print(f"  with a pre-committed kill two orders below. On the recorded j and ratio the")
print(f"  internally consistent value is {om_b/1e3:.2f} keV, so a derivation landing there would read")
print("  as a 3x miss while actually closing the transmission the section needs. The kill")
print("  threshold is untouched either way -- a factor 3 is well inside two orders -- but the")
print("  target itself is only as firm as the least certain member of the trio.")
