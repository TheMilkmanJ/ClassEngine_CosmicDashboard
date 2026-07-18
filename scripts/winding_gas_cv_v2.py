#!/usr/bin/env python3
"""B2 v2 (sweep 72) — the two ramps the operator's bet demanded:
(1) xi(t) DIVERGES at T_c: xi = xi0*(1-t)^(-nu) -> the patch census N(R,t) =
    (R/xi)^2 COLLAPSES toward the draw — the count is dynamical, not static.
(2) THE COUPLED FIELD: adjacent winding mismatches cost vortex-line energy ->
    the transverse winding field is a 2D Gaussian height model, J ~ rho_s(t).
    Solvable: modes E_k = (J/2)k^2|n_k|^2; the census fluctuation of a region
    acquires a LOG (height fields are log-correlated) over independent-patch
    shot noise — the candidate origin of the banked 1/ln tilt structure."""
import numpy as np
nu = 2.0/3.0

print("(1) THE CENSUS COLLAPSE — patches merge as the draw approaches:")
print(f"   {'t=T/T_c':>8s} {'xi/xi0':>8s} {'N(R=1000 xi0)':>14s}")
for t in [0.5, 0.8, 0.9, 0.95, 0.98, 0.99]:
    xi = (1-t)**(-nu)
    print(f"   {t:8.3f} {xi:8.2f} {1e6/xi**2:14.0f}")
print("   -> N(t) is a RAMP; the census the sky remembers = N at the LOCK moment;")
print("   the 781-per-dimension question becomes: WHERE ON THIS CURVE DID IT FREEZE?")
print()
print("(2) THE COUPLED HEIGHT FIELD (Gaussian model, exact by modes):")
# var of the mean winding over a region R: (T/J) * sum over k of |W(kR)|^2/k^2
# on the transverse plane, UV cutoff at the patch scale, IR at the system L.
def var_mean_winding(R, L=4096.0, TJ=1.0, nk=6000):
    k = np.logspace(np.log10(2*np.pi/L), np.log10(2*np.pi), nk)
    # 2D isotropic: d^2k -> k dk/(2pi); window: top-hat disc |W|^2 ~ (2 J1(kR)/(kR))^2
    from scipy.special import j1
    W2 = (2*j1(k*R)/(k*R))**2
    integrand = TJ*W2/k**2 * k/(2*np.pi)
    return np.trapezoid(integrand, k)
from scipy.special import j1
print(f"   {'R':>6s} {'var(nbar)':>10s} {'xR^2':>10s} {'vs 1/R^2 (indep)':>18s}")
base = None
for R in [8., 16., 32., 64., 128.]:
    v = var_mean_winding(R)
    if base is None: base = v*R**2
    print(f"   {R:6.0f} {v:10.5f} {v*R**2:10.4f}   indep-model would give {base/R**2:.5f}")
print("   -> var x R^2 GROWS with ln(L/R)-class structure (log-correlated),")
print("   NOT constant (independent shot noise): the census carries a LOG.")
print()
print("(3) THE TILT CANDIDATE: a log-enhanced census makes the spectrum's")
print("   deviation from scale-invariance ~ 1/ln — THE BANKED FORM's class")
print("   (n_s - 1 = -2/ln): the roughening log as the tilt's microphysics.")
print("   [CANDIDATE mechanism, sharpened: coefficient '-2' read as the two transverse")
print("   dims of a 2D Gaussian height field; log argument R/a = (M_Pl/T_on^2)/(1/T_on)")
print("   = M_Pl/T_on -- scale arithmetic checks. NOT closed: the log-derivative step")
print("   (tilt = exactly -2/ln, not just ~1/ln) is the owed variance->spectrum session.]")
