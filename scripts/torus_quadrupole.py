#!/usr/bin/env python3
"""
TORUS TEST: does a flat 3-torus suppress the CMB quadrupole by the observed amount, at a box
size consistent with the 'no matched circles' bound? A finite box of side L has NO modes with
k < k_min = 2*pi/L -> the largest-scale power is cut. Sachs-Wolfe estimate:
   C_l  ∝  ∫ dk/k [j_l(k D)]^2 ,   D = comoving distance to last scattering (~14000 Mpc)
Infinite universe: integral from 0 (analytic = 1/(2 l(l+1))). Torus: integral from k_min=2pi/L.
Suppression(l) = C_l(torus)/C_l(infinite).  Leading-order (SW-only, isotropic-cutoff) estimate.
"""
import numpy as np
from scipy.special import spherical_jn
from scipy.integrate import quad

D = 14000.0  # comoving distance to last scattering, Mpc

def C_full(l):   # analytic infinite-universe SW: ∫_0^inf dx/x j_l^2 = 1/(2 l(l+1))
    return 1.0/(2*l*(l+1))
def C_cut(l, L): # torus: cut off below x_min = k_min*D = 2pi*D/L
    xmin = 2*np.pi*D/L
    return quad(lambda x: spherical_jn(l,x)**2/x, xmin, 400, limit=400)[0]

# sanity: numeric full vs analytic
num_full = quad(lambda x: spherical_jn(2,x)**2/x, 1e-4, 400, limit=400)[0]
print("="*62); print("FLAT 3-TORUS: quadrupole suppression vs box size"); print("="*62)
print(f"\n  sanity: numeric C_2(full)={num_full:.4f} vs analytic {C_full(2):.4f} "
      f"({'MATCH' if abs(num_full-C_full(2))<0.005 else 'CHECK'})")
print(f"  observable-universe diameter ~ 2D = {2*D:.0f} Mpc (matched-circle bound: L > ~2D)\n")
print(f"  {'L/D':>6}{'L (Mpc)':>10}{'x_min':>8}{'C2 supp.':>10}{'C3 supp.':>10}  note")
print("  "+"-"*58)
for LD in [10, 6, 4, 3, 2.5, 2.0, 1.5]:
    L=LD*D; xmin=2*np.pi*D/L
    s2=C_cut(2,L)/C_full(2); s3=C_cut(3,L)/C_full(3)
    note = "< matched-circle bound" if LD<2 else ("~ bound (edge)" if LD<2.6 else "allowed")
    print(f"  {LD:>6.1f}{L:>10.0f}{xmin:>8.2f}{s2:>10.2f}{s3:>10.2f}  {note}")
print("\n  "+"-"*58)
print("  observed quadrupole ~0.2-0.5 of LCDM (low, but ~2sigma cosmic-variance).")
print("  -> box L giving that suppression: read the C2 column for supp ~0.2-0.5.")
print("="*62)
