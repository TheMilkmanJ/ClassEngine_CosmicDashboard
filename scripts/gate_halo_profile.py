#!/usr/bin/env python3
"""Entry-83 follow-up: the gate's spatial profile through a real halo.

Frame: the dCDF halo already does the rotation curve (the model HAS dark matter).
Route A's observable is the RESIDUAL: a(r) = c^2 * f_lep * eps0 * |dg/dr| — an extra
inward, composition-tagged pull where the gate g(C(r)) turns. Questions: (1) where is
the gate radius r_gate (g = 1/2)? (2) how wide is the ring? (3) peak a vs a0? (4) the
integrated v^2 boost; (5) does any fence-allowed (C_ref, s) put the ring where data
exist (outer HI curves ~10-80 kpc; MW streams/dwarfs ~20-300 kpc)?

Environment model (flagged assumptions): MW-class NFW halo (M_vir = 1e12 Msun,
c = 10, R_vir = 250 kpc) + mean-matter background floor; the gate variable C is
proxied by local total-matter overdensity Delta(r). Gate: g(C) = 1/(1 + (C/C_ref)^s)
— smooth, steepness s; ON (g -> 1) in voids, OFF in dense regions.

RAMP DISCIPLINE: continuous r-grids, (C_ref, s) scanned as bands, outputs as curves;
no single-point verdicts. Reading-B conditional like the whole gate family.
"""
import numpy as np

c_light = 2.998e8
eps0    = 0.0124
m_e_u   = 0.000549
f_star  = 0.5 * m_e_u / 1.0
f_gas   = 1.0 * m_e_u / 1.008
a0      = 1.2e-10
kpc     = 3.086e19
Msun    = 1.989e30

# --- MW-class NFW + background ------------------------------------------------
Mvir, conc, Rvir = 1e12 * Msun, 10.0, 250 * kpc
rs = Rvir / conc
rho_crit = 8.6e-27                      # kg/m^3
rho_m    = 0.31 * rho_crit              # mean matter density
delta_c  = (200/3) * conc**3 / (np.log(1+conc) - conc/(1+conc))

def rho_nfw(r):
    x = r / rs
    return delta_c * rho_crit / (x * (1 + x)**2)

r = np.logspace(np.log10(5), np.log10(3000), 600) * kpc     # 5 kpc - 3 Mpc
Delta = rho_nfw(r) / rho_m + 1.0                            # overdensity + floor

print(f"environment: Delta at 10/50/100/250/500/1000/2000 kpc = ", end="")
for rk in [10, 50, 100, 250, 500, 1000, 2000]:
    print(f"{np.interp(rk*kpc, r, Delta):8.1f}", end=" ")
print("\n")

print(f"{'C_ref':>6} {'s':>3} | {'r_gate [kpc]':>12} | {'ring FWHM [kpc]':>15} | "
      f"{'peak a_star':>11} | {'peak/a0':>8} | {'v2 boost (km/s)^2 @peak':>22}")
print("-" * 100)
for C_ref in [3, 10, 30, 100, 300, 1000]:
    for s in [2, 4, 8]:
        g = 1.0 / (1.0 + (Delta / C_ref)**s)
        dgdr = np.gradient(g, r)
        a_star = c_light**2 * f_star * eps0 * np.abs(dgdr)
        ipk = np.argmax(a_star)
        # gate radius: g crosses 1/2
        if g[0] < 0.5 < g[-1]:
            r_gate = np.interp(0.5, g, r) / kpc
        else:
            r_gate = float('nan')
        # ring FWHM in radius
        half = a_star > a_star[ipk] / 2
        fwhm = (r[half][-1] - r[half][0]) / kpc if half.sum() > 1 else 0.0
        v2boost = r[ipk] * a_star[ipk] / 1e6                  # (km/s)^2
        print(f"{C_ref:6d} {s:3d} | {r_gate:12.1f} | {fwhm:15.1f} | "
              f"{a_star[ipk]:11.3e} | {a_star[ipk]/a0:8.2f} | {v2boost:22.1f}")

print()
print("invariant: total integral  ∫a dr = c^2 f_lep eps0 =",
      f"{c_light**2*f_star*eps0:.3e} m^2/s^2 (stars) = ({np.sqrt(c_light**2*f_star*eps0)/1e3:.0f} km/s)^2 ;",
      f"gas x{f_gas/f_star:.2f}")
print("composition split: a_gas/a_star =", f"{f_gas/f_star:.2f}", "everywhere on the ring")
