#!/usr/bin/env python3
"""
THE CRITICALITY CROSSOVER: can critically-amplified parity-odd scalar perturbations
source an OBSERVABLE chiral GW background (2nd-order induced GWs), beating the direct
CS signal (Pi~1e-7)? This is the one place criticality (a SCALAR-sector amplifier,
chi~1/c_s^2) can leak into the TENSOR sky.

Induced GW:      Omega_GW,ind h^2 ~ eps * P_zeta^2         (eps~1e-2..1e-1 efficiency)
Amplified power: P_zeta ~ chi^2 * P_zeta0   (chi amplifies delta; power ~ delta^2), capped <~0.1
Chiral part:     Omega_chiral ~ Pi_frac * Omega_GW,ind     (Pi_frac = parity-odd fraction)
Frequency:       f_today ~ H_crit / (2 pi (1+z_crit))      (horizon scale at the critical epoch)
The model's critical point is the DE FLOOR (z_crit ~ 0.5, late) -> what frequency does that land at?
"""
import numpy as np
H0_Hz = 2.3e-18          # H0 in Hz
P0     = 2.1e-9          # base scalar power (CMB)
eps    = 0.1             # induced-GW efficiency
Pcap   = 0.1            # perturbativity cap on P_zeta

# detector bands (approx central freq, Hz) and Omega_GW h^2 sensitivity
DET = {"CMB B-mode":(1e-17,1e-16),"PTA/NANOGrav":(1e-8,1e-9),"LISA":(1e-3,1e-13),"LIGO":(1e2,1e-9)}

def Hz_of_zcrit(z):     # induced-GW freq today from horizon scale at z_crit (matter/DE era)
    Hc = H0_Hz*np.sqrt(0.31*(1+z)**3+0.69)
    return Hc/(2*np.pi*(1+z))

def omega_ind(chi):
    P = min(Pcap, chi**2 * P0)
    return eps*P**2, P

print("="*72); print("CRITICALITY CROSSOVER: chiral scalar-induced GW vs the direct Pi~1e-7")
print("="*72)
print(f"\n  amplitude scan (chi = scalar amplification, chi~500 was the neutrino/DE number):")
print(f"  {'chi':>7}{'P_zeta':>12}{'Omega_ind h2':>15}{'x direct(1e-7)?':>18}")
print("  "+"-"*52)
for chi in [1,30,100,500,3000,1e4]:
    O,P = omega_ind(chi)
    beats = "YES" if O>1e-7 else "no"
    print(f"  {chi:>7.0f}{P:>12.2e}{O:>15.2e}{beats:>14}")
print(f"  (P_zeta capped at {Pcap} by perturbativity; chi^2 saturates fast)")

print(f"\n  FREQUENCY -- where does the model's critical point (DE floor) land?")
f_DE = Hz_of_zcrit(0.5)
print(f"  z_crit ~ 0.5 (DE floor)  ->  f_today ~ {f_DE:.2e} Hz")
print(f"  {'detector':>14}{'band f (Hz)':>14}{'sens Omega h2':>15}   reachable?")
print("  "+"-"*58)
for d,(f,s) in DET.items():
    off = f_DE/f
    reach = "band-match" if 0.1<off<10 else f"off by {f/f_DE:.0e}x in freq"
    print(f"  {d:>14}{f:>14.0e}{s:>15.0e}   {reach}")

# what z_crit would PTA need?
print(f"\n  For induced GW to reach the PTA band (f~1e-8 Hz), solve f(z_crit)=1e-8:")
zs=np.logspace(0,13,14000); fz=Hz_of_zcrit(zs); zc=zs[np.argmin(np.abs(fz-1e-8))]
print(f"     need z_crit ~ {zc:.1e}   (deep in the radiation era)")
print(f"     model's critical point is z~0.5 (the DE floor) -> off by ~{zc/0.5:.0e}x in redshift.")
print("="*72)
