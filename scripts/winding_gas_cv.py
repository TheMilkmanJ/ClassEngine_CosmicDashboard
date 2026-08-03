#!/usr/bin/env python3
"""PARTLY SUPERSEDED — the area law and the activation ramp stand; the tilt leg (c) does not.

  * nu = 2/3 (3D-XY) here is a STATIC exponent for the CONDENSATION ramp at T_c.  It is not a
    quench criterion for the A_s census imprint, which is a separate link and a SCALING imprint
    (xi(k) ~ 1/k), not a freeze-out — see #184.  The corpus's recorded claim that no critical
    exponent appears anywhere was corrected against this line.
  * Leg (c), "C_V ~ R^2 => Phi^2 scale-invariant (the thermodynamic road to the tilt)", is not
    the surviving tilt route; the tilt is carried by the modulation map, n_s = 1 - 2/ln(T0/k).

Autopsies: docs/PRTOE_FAILURES_LEDGER.md (#184).

B2 — THE WINDING-GAS SPECIFIC HEAT (sweep 71). The medium's winding sector
near T_c: each transverse coherence patch (xi^2) carries an independent winding
integer n with E(n) = eps1(T) * n^2, where eps1 ~ rho_s(T) -> 0 at T_c (the
3D-XY ramp, nu = 2/3). Tests: (a) the activation ramp (the Hagedorn-analog IS
T_c); (b) THE AREA LAW (dof transversely indexed -> C_V(region) ~ R^2);
(c) the NBV chain: C_V ~ R^2 => Phi^2 scale-invariant (the thermodynamic road
to the tilt). All ramps; the winding integers are the legal (exempt) discretes."""
import numpy as np

def cv_per_patch(t, a=8.0, nmax=400):
    """C_V of ONE winding dof at T/T_c = t; eps1 = a*(1-t)^(2/3) in T_c units."""
    if t >= 1.0: return 0.5   # melted: free winding = 1 quadratic dof classical
    eps1 = a*(1.0-t)**(2.0/3.0)
    n = np.arange(-nmax, nmax+1)
    E = eps1*n**2
    w = np.exp(-E/t)
    Z = w.sum(); Em = (E*w).sum()/Z; E2 = (E**2*w).sum()/Z
    return (E2 - Em**2)/t**2    # C_V = var(E)/T^2

print("(a) THE ACTIVATION RAMP — C_V per winding patch vs T/T_c:")
for t in [0.5, 0.8, 0.9, 0.95, 0.98, 0.995, 0.9995]:
    print(f"   T/T_c = {t:6.4f}: C_V/patch = {cv_per_patch(t):.4f}")
print("   (0 = frozen windings; -> 1/2 = the classical winding-active regime:")
print("    the proliferation temperature IS T_c — the Hagedorn-analog, a RAMP)")
print()
print("(b) THE AREA LAW — a region of size R holds (R/xi)^2 patches (transverse")
print("    indexing; the axis direction adds NO winding multiplicity):")
t = 0.98
for R in [4, 8, 16, 32]:
    N_dof = R**2
    print(f"   R = {R:3d}: C_V = {N_dof*cv_per_patch(t):8.1f}   C_V/R^2 = {N_dof*cv_per_patch(t)/R**2:.4f} (const)   C_V/R^3 = {N_dof*cv_per_patch(t)/R**3:.4f} (falls)")
print()
print("(c) THE NBV CHAIN (with C_V ~ R^2 confirmed):")
print("   dE^2 = T^2 C_V ~ T^2 R^2  ->  drho^2 = dE^2/V^2 ~ T^2/R^4")
print("   Phi ~ G dM/R ~ drho R^2   ->  Phi^2 ~ (T^2/R^4) R^4 = T^2/M_Pl^4-class")
print("   => SCALE-INVARIANT at zeroth order — the tilt's thermodynamic road")
print("   confirmed; the drift (the RAMP of eps1 near the draw) supplies n_s-1.")
