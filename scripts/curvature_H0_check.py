#!/usr/bin/env python3
"""
QUICK CHECK: does a CLOSED universe (Omega_k<0) raise or lower H0, at fixed CMB acoustic scale?
The CMB pins theta_* = r_s / D_M(z*) very tightly. Hold r_s fixed (same early physics) and the
physical matter density omega_m = Om*h^2 fixed (peak heights) -> D_M(z*) is fixed. Then vary
Omega_k and solve for the H0 that keeps D_M fixed. That is the geometric degeneracy direction --
the thing that decides Justin's bet (closed -> H0 UP, toward SHOES) vs vanilla (closed -> H0 down).
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

c = 299792.458   # km/s
zstar = 1089.9

def E(z, Om, Ok):
    return np.sqrt(Om*(1+z)**3 + Ok*(1+z)**2 + (1-Om-Ok))

def I_comov(Om, Ok):
    return quad(lambda z: 1.0/E(z,Om,Ok), 0, zstar, limit=200)[0]

def D_M(H0, Om, Ok):   # comoving angular-diameter distance to z*, Mpc
    I = I_comov(Om, Ok)
    if abs(Ok) < 1e-9:  return (c/H0)*I
    if Ok < 0:  s=np.sqrt(-Ok); return (c/H0)/s*np.sin(s*I)
    s=np.sqrt(Ok);            return (c/H0)/s*np.sinh(s*I)

# baseline: flat PRTOE point
H0b, Omb = 69.9, 0.30
wm = Omb*(H0b/100)**2                 # fixed physical matter density
Dtar = D_M(H0b, Omb, 0.0)             # fixed by CMB (r_s & theta_* fixed)

def H0_at(Ok):                        # solve D_M = Dtar with Om = wm/h^2
    f = lambda H0: D_M(H0, wm/(H0/100)**2, Ok) - Dtar
    return brentq(f, 40, 130)

print("="*60); print("Does closing the universe raise or lower H0?"); print("="*60)
print(f"\n  baseline (flat): H0 = {H0b}, Om = {Omb}, omega_m = {wm:.4f}")
print(f"  held fixed: CMB D_M(z*) = {Dtar:.1f} Mpc  and  omega_m\n")
print(f"  {'Omega_k':>9}{'geometry':>9}{'-> H0':>9}{'vs SHOES(73)':>14}")
print("  "+"-"*42)
for Ok in [0.02, 0.0, -0.005, -0.01, -0.02, -0.03, -0.04, -0.05]:
    H0 = H0_at(Ok)
    geo = "open" if Ok>0 else ("flat" if Ok==0 else "closed")
    print(f"  {Ok:>9.3f}{geo:>9}{H0:>9.2f}{abs(73-H0):>10.1f} away")
print("\n  "+"-"*42)
# sanity anchor: Planck-alone closed ~ Ok=-0.044 should give low H0 (~54)
print(f"  sanity: Ok=-0.044 -> H0={H0_at(-0.044):.1f}  (Planck-alone lands ~54: {'MATCH' if abs(H0_at(-0.044)-54)<4 else 'CHECK'})")
print("="*60)
print("READ: sign of dH0/dOmega_k tells whose bet the geometry favors.")
