#!/usr/bin/env python3
"""Task #33: the response-function session — one medium, two legal channels, two limits.

ROUTE A (the epsilon channel, mean-field limit): the gate curve's spatial gradient at
galaxy edges acts on matter's LEPTONIC mass fraction:
    a_anom(L) = c^2 * f_lep * eps0 / L      (L = the gate's spatial gradient scale)
Sign: eps is ON (heavier leptons) where C is LOW (outskirts/voids) -> grad(eps) points
outward -> F = -grad(m c^2) points INWARD: extra centripetal pull at the edge.
Census-legal by construction (it IS the model's one coupling); screened regime evades
MICROSCOPE (no gradient where saturated). Composition tag: f_lep = Z*m_e/(A*m_u) differs
between H gas (Z/A=1) and evolved stars (Z/A~0.5) -> a ~2x composition split, which
MOND does not have. RAMP: a(L) as a continuous curve; no chosen L.

ROUTE B (the gravity channel, two-body limit): the depletion/polarization cloud around
a mass in the condensate; overlap of two clouds corrects the pair's mutual binding.
Census cap (P-2026-014: no fifth force): the response is GRAVITATIONAL polarization only:
    relative correction  A_rel ~ 4*pi*G*rho_dm*xi^2 / c_s^2   (saturating above the hinge)
    ramped in separation: g(d) = d^2/(d^2 + xi^2)  (smooth 0->1 across the hinge)
with xi = 402 AU (the ladder's hinge), c_s = sqrt(alpha_c)*c (the recorded sound speed).

THE DEGENERACY CHECK (the author's order): are the two routes secretly one number?
"""
import numpy as np

c      = 2.998e8
G      = 6.674e-11
eps0   = 0.0124
alpha_c= 0.021892
c_s    = np.sqrt(alpha_c) * c            # the medium's sound speed
xi     = 402 * 1.496e11                  # the hinge, m
kpc    = 3.086e19
a0     = 1.2e-10                         # the MOND/wide-binary acceleration scale
m_e_u  = 0.000549                        # electron mass, u
rho_dm = 6.8e-22                         # local DM density kg/m^3 (0.018 Msun/pc^3 class)

print("=" * 74)
print("ROUTE A — the epsilon-gradient (lepton channel), ramped in gradient scale L")
print("=" * 74)
print("composition: f_lep(H gas, Z/A=1) vs f_lep(stellar, Z/A~0.5)")
f_gas  = 1.0 * m_e_u / 1.008             # hydrogen
f_star = 0.5 * m_e_u / 1.0               # evolved-mix class
print(f"  f_lep gas = {f_gas:.3e}   f_lep stars = {f_star:.3e}   ratio = {f_gas/f_star:.2f}")
print(f"{'L [kpc]':>8} | a_gas [m/s^2] | a_stars [m/s^2] | a_gas/a0")
for L in np.logspace(np.log10(5), np.log10(500), 11):
    a_gas  = c**2 * f_gas  * eps0 / (L * kpc)
    a_star = c**2 * f_star * eps0 / (L * kpc)
    print(f"{L:8.1f} | {a_gas:12.3e} | {a_star:14.3e} | {a_gas/a0:8.2f}")
L_a0_gas  = c**2 * f_gas  * eps0 / a0 / kpc
L_a0_star = c**2 * f_star * eps0 / a0 / kpc
print(f"\n  a0 is reached at L = {L_a0_star:.0f} kpc (stars) .. {L_a0_gas:.0f} kpc (gas)")
print("  SIGN: inward at the edge (eps rises outward, F = -grad(mc^2)) — RAR-friendly")

print()
print("=" * 74)
print("ROUTE B — the depletion overlap (gravity channel), ramped across the hinge")
print("=" * 74)
A_rel = 4 * np.pi * G * rho_dm * xi**2 / c_s**2
print(f"  census-capped amplitude: A_rel = 4piG rho_dm xi^2/c_s^2 = {A_rel:.3e}")
print(f"{'d [AU]':>8} | d/xi     | g(d) ramp | F correction (rel)")
for d_au in [50, 100, 200, 402, 800, 2000, 5000, 20000]:
    d = d_au * 1.496e11
    g = d**2 / (d**2 + xi**2)
    print(f"{d_au:8.0f} | {d/xi:8.3f} | {g:9.4f} | {A_rel*g:.3e}")
print(f"  wide-binary anomaly claims need ~2e-1; the census cap delivers {A_rel:.1e}")
print(f"  shortfall: {np.log10(0.2/A_rel):.1f} orders — the unloaded-gun class")

print()
print("=" * 74)
print("THE DEGENERACY CHECK — are A and B one number in disguise?")
print("=" * 74)
a_B_char = A_rel * G * 2e30 / (2000 * 1.496e11)**2   # B's absolute size at a solar pair, 2000 AU
a_A_char = c**2 * f_star * eps0 / (80 * kpc)
print(f"  route A characteristic acceleration (80 kpc): {a_A_char:.3e} m/s^2")
print(f"  route B characteristic acceleration (2000 AU): {a_B_char:.3e} m/s^2")
print(f"  ratio A/B = {a_A_char/a_B_char:.3e}")
print("  channels: A = lepton (composition-tagged), B = gravity (composition-blind)")
