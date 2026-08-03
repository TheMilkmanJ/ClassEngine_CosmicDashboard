#!/usr/bin/env python3
"""
The bar for turning zeta_pour from a bet into a prediction.

Logic (pour-partition chase): zeta_pour = 1 is EARNED only if the dark and SM
baths thermalized. The portal is gravitational -- "the standard gravitational
escape," Gamma/H ~ 3e-7 at the pour (PRTOE_DERIVATION_HUNT.md:299). Gravitational
2->2: Gamma ~ T^5/M_Pl^4, H ~ T^2/M_Pl, so Gamma/H = (T/M_Pl)^3. So there is a
threshold ceiling T* where Gamma/H = 1; if the CRUNCH ceiling (Tolman-blueshifted
max T of the contracting phase) clears T*, contraction thermalizes the two baths ->
zeta_pour = 1 forced -> zeta_late ~ 0.33 with no free knob. If not, zeta_pour is a
free initial condition inherited from the prior cycle -> the unsolved bounce.

This computes the bar and compares it to the model's own pour/reheat scale.
"""
M_PL   = 1.22e19          # GeV, Planck mass (gravitational rate uses the full M_Pl)
GH_POUR = 3e-7            # Gamma/H at the pour scale (DERIVATION_HUNT:299)
PSI0   = (0.7e17, 1.5e17)  # GeV, the reheat scale Psi_0 (PHYSICS_DOMAINS #70)

# Gamma/H = (T/M_Pl)^3.  Bar: Gamma/H = 1  ->  T* = M_Pl.
T_star  = M_PL
T_pour  = M_PL * GH_POUR ** (1/3)     # pour temperature implied by Gamma/H = 3e-7
gap     = T_star / T_pour             # = (3e-7)^(-1/3)

print("Bar for zeta_pour thermalization (gravitational portal, Gamma/H = (T/M_Pl)^3)")
print("=" * 74)
print(f"  BAR  T* where Gamma/H = 1        = M_Pl = {T_star:.2e} GeV")
print(f"  pour T implied by Gamma/H = 3e-7 = {T_pour:.2e} GeV")
print(f"     cross-check vs Psi_0 = {PSI0[0]:.1e}-{PSI0[1]:.1e} GeV : "
      f"{'CONSISTENT' if PSI0[0] <= T_pour <= 3*PSI0[1] else 'mismatch -- recheck'}")
print(f"  GAP  T*/T_pour = (3e-7)^(-1/3)   = {gap:.0f}x")
print()
for name, T in [("Psi_0 low",  PSI0[0]), ("Psi_0 high", PSI0[1]), ("bar T*=M_Pl", T_star)]:
    print(f"    Gamma/H at {name:12s} ({T:.2e} GeV) = {(T/M_PL)**3:.2e}")
print()
print("VERDICT:")
print(f"  The bar is the PLANCK temperature. The model's own pour/crunch ceiling")
print(f"  (Psi_0 ~ 1e17 GeV) sits ~{gap:.0f}x below it, at Gamma/H ~ 3e-7 -- the portal")
print(f"  does NOT fire there. Thermalization (hence zeta_pour = 1, hence a DERIVED")
print(f"  zeta ~ 0.33) requires the crunch to reach ~M_Pl -- i.e. a near-Planckian")
print(f"  bounce, ~{gap:.0f}x hotter than the stated reheat. Whether L_gen pushes the")
print(f"  ceiling that high is the whole question; at the model's stated scale it does not.")
print()
print("  Caveat: this is the GRAVITATIONAL portal (the corpus's quoted 3e-7 escape).")
print("  A non-gravitational portal (e.g. the high-f dyad, suppressed by f~1e5-1e6 GeV")
print("  rather than M_Pl) would bar LOWER and could fire at a sub-Planckian crunch --")
print("  a separate rate that is worth pricing before the branch is called closed.")
