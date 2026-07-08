#!/usr/bin/env python3
"""
THE GRAVITATIONAL DOOR: does the genesis twist leave a chiral-GW fingerprint?
Charge-free. Mechanism: the rolling pseudoscalar theta (Affleck-Dine spiral)
couples parity-odd to gravity via Chern-Simons gravity  L ⊃ alpha * theta * R R̃
(R R̃ = gravitational Pontryagin density). When theta-dot != 0, left- and right-
handed gravitons propagate differently -> the primordial GW background acquires a
NET CIRCULAR POLARIZATION Pi (Stokes V / intensity). This is the honest, EM-charge-
free home for the birth-twist parity preference.

Order-of-magnitude (defensible): the CS term competes with Einstein-Hilbert (~M_Pl^2).
The parity-odd correction to the L/R graviton dispersion at horizon crossing (k/a ~ H):
    Pi  ~  alpha * theta_dot * H_gen / M_Pl^2       (dimensionless)
AND you can only MEASURE that chirality if there's a GW background to carry it:
    r   ~  (H_inf / M_Pl)^2   (tensor-to-scalar; needs r >~ 1e-3 for any hope)
So observability needs BOTH  Pi  large  AND  r  detectable.
"""
import numpy as np
M_Pl = 2.4e18       # reduced Planck mass, GeV
GeV_per_eV = 1e-9

# observability thresholds (generous / futuristic)
PI_OBS  = 1e-2      # net GW circular pol detectable by CMB B-mode parity (TB/EB) at best
R_OBS   = 1e-3      # tensor-to-scalar floor for a detectable primordial GW background

def Pi(alpha, tdot, Hgen):   # net chirality
    return alpha * tdot * Hgen / M_Pl**2
def r_ts(Hinf):
    # correct: A_s ~ 2.1e-9, H_inf = pi*M_Pl*sqrt(A_s*r/2) -> r = (Hinf/2.44e14 GeV)^2
    return (Hinf/2.44e14)**2

print("="*72)
print("CHIRAL-GW FINGERPRINT OF THE GENESIS TWIST  (charge-free, CS gravity)")
print("="*72)

# genesis scenarios: (name, H_gen GeV, theta_dot GeV, alpha)
# theta_dot ~ m_field at genesis; alpha ~ O(1) natural unless UV-enhanced
scen = [
  ("Planckian genesis (extreme)",      1e18,  1e18,  1.0),
  ("GUT/high-inflation (r~max)",        6e13,  6e13,  1.0),
  ("model-natural (Psi0~5e16 scale)",   1e13,  5e16,  1.0),   # H_inf<=1e13, tdot~field scale
  ("model-natural, alpha boosted 1e3",  1e13,  5e16,  1e3),
  ("low-scale genesis",                 1e8,   1e10,  1.0),
]
print(f"\n  {'scenario':<34}{'Pi (chirality)':>16}{'r (GW ampl)':>14}  verdict")
print("  " + "-"*70)
for name,Hg,td,al in scen:
    p = Pi(al,td,Hg); r = r_ts(Hg)
    obs = "OBSERVABLE" if (p>=PI_OBS and r>=R_OBS) else ("no GW bkg" if r<R_OBS else "too faint")
    print(f"  {name:<34}{p:>16.2e}{r:>14.2e}  {obs}")

print("\n  " + "-"*70)
# what would it TAKE? solve Pi=PI_OBS for H_gen assuming tdot~H_gen, alpha=1
# Pi = H_gen^2/M_Pl^2 = PI_OBS  -> H_gen = M_Pl*sqrt(PI_OBS)
Hcrit = M_Pl*np.sqrt(PI_OBS)
print(f"  For Pi >= {PI_OBS:.0e} with theta_dot~H_gen, alpha=1:")
print(f"     need H_gen >= {Hcrit:.2e} GeV  =  {Hcrit/M_Pl:.3f} M_Pl")
print(f"  But inflation requires H_inf <~ 6e13 GeV (tensor bound r<0.03).")
print(f"  Gap: need genesis ~{Hcrit/6e13:.0e}x ABOVE the observational ceiling on H_inf.")
print("="*72)
