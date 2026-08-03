#!/usr/bin/env python3
"""Entry 87b: the RAMPED re-run of the Kelvin-weight checks (process error 23 —
v1 asserted point ratios). All suppressions computed as continuous curves; the
question inverted per ramp discipline: not "is it dead at the model's point?" but
"where on the curve WOULD the vector sector matter, and does the model own
anything there?"
"""
import numpy as np
AU=1.496e11; Gpc=3.086e25
xi=402*AU; L=27.6*Gpc; NEED=76.0     # |delta str| the sign flip requires

print("CURVE 1 — core-localized line modes: weight vs winding n (5..40)")
for n in [5,10,19,25,40]:
    print(f"  n={n:3d}: delivered/needed = {n*np.pi*xi**2/L**2/NEED:.2e}")
print("  -> flat in n to within x8 across the whole Widnall band; 24-25 orders short everywhere\n")

print("CURVE 2 — worldsheet-reduced treatment ((1+1)D heat kernel on the line):")
for n in [5,19,40]:
    print(f"  n={n:3d}: ~ n/(L*K)^2 = {n/( (L/xi)**2 ):.2e}  ({np.log10(NEED*(L/xi)**2/n):.1f} orders short)")
print()

print("CURVE 3 — lattice (Tkachenko) route: contribution vs inter-line spacing b")
print(f"  {'b':>12} | (xi/b)^2      | verdict")
for b_val,name in [(L/np.sqrt(19),'the model (n=19 global)'),(1*Gpc,'1 Gpc'),(3.086e22,'1 Mpc'),
                   (3.086e19,'1 kpc'),(9*xi,'~9*xi (where O(1) arrives)')]:
    s=(xi/b_val)**2
    print(f"  {b_val/AU:12.3e} AU | {s:.2e} | {'REACHES the needed weight' if s*NEED>=1 else 'short'}")
b_crit = xi*np.sqrt(NEED)
print(f"  O(76) requires b <= xi*sqrt(1/76)... exact: b = {xi/np.sqrt(NEED)/AU:.0f} AU —")
print(f"  a vortex line every ~46 AU filling ALL of space. The model stocks: n~19 global")
print(f"  lines (b ~ 6 Gpc) and halo-bound lattices (environment-fenced). The gap between")
print(f"  what is owned and what is needed: {np.log10((L/np.sqrt(19))/(xi/np.sqrt(NEED))):.1f} orders in spacing,")
print(f"  ~{2*np.log10((L/np.sqrt(19))/(xi/np.sqrt(NEED))):.0f} orders in weight — smooth, no treatment crosses it.")
