#!/usr/bin/env python3
"""
#8 GRANULE SIM (first build, transparent). Ultralight-DM in a halo is wave-like
-> self-interference -> speckle -> density granules. The doc claims the granule
power (density-contrast variance) reads out f_amp via
    S = (1 + f_rot^2)/2 ,  f_rot = 1 - f_amp
so a measured halo granule contrast -> f_amp (independent of the Z4 dice).

This tests whether that law falls out of plausible two-component speckle models.
S := var(rho)/mean(rho)^2 , rho=|psi|^2.  Speckle via random-phase plane-wave sum.
Run: python3 scripts/granule_sim.py
"""
import numpy as np
rng=np.random.default_rng(0)
N=200000  # samples (each a point in a big speckle field)

def speckle(n):
    # complex Gaussian speckle: sum of many random-phase modes -> circular Gaussian
    return (rng.standard_normal(n)+1j*rng.standard_normal(n))/np.sqrt(2)  # <|.|^2>=1

def S_of(rho): 
    m=rho.mean(); return rho.var()/m**2

print("="*66); print("#8 granule sim: does S = (1+f_rot^2)/2 fall out of speckle?"); print("="*66)
print(f"\n  {'f_amp':>6} {'f_rot':>6} {'DOC S':>8} | {'A:2 speckle':>11} {'B:speckle+coh':>13} {'C:real+cplx':>11}")
print("  " + "-"*64)
for fa in [1.0,0.8,0.6,0.4,0.2,0.0]:
    fr=1-fa
    doc=(1+fr**2)/2
    # Model A: two INDEPENDENT complex speckles, fractions fa, fr
    psiA=np.sqrt(fa)*speckle(N)+np.sqrt(fr)*speckle(N)
    SA=S_of(np.abs(psiA)**2)
    # Model B: amplitude=speckle (fa), rotation=coherent smooth constant (fr)
    psiB=np.sqrt(fa)*speckle(N)+np.sqrt(fr)*np.ones(N)
    SB=S_of(np.abs(psiB)**2)
    # Model C: amplitude=REAL Gaussian (fa), rotation=complex speckle (fr)
    amp=rng.standard_normal(N)          # real, <amp^2>=1
    psiC_rho=fa*amp**2+fr*np.abs(speckle(N))**2
    SC=S_of(psiC_rho)
    print(f"  {fa:>6.1f} {fr:>6.1f} {doc:>8.3f} | {SA:>11.3f} {SB:>13.3f} {SC:>11.3f}")
print("\n" + "-"*66)
print("READ: if any column tracks 'DOC S', that model underlies the granule law.")
print("If none do, the S=(1+f_rot^2)/2 formula needs its speckle model pinned down")
print("before the halo granule contrast can be read as f_amp. (Honest test.)")
