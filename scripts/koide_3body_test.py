#!/usr/bin/env python3
"""
JP's 3-body / masslessness test for the Koide amplitude A = R/M (Q = 2/3 <=> A = √2).
The three charged leptons are an equilateral (120°, Lagrange-like) config; JP's read:
"2 massive orbiting 1 (near-)massless," 2/3 out of that. Tests:
  (1) does A = √2 hold, and what is its clean characterization?
  (2) is the family really "2 heavy + 1 near-massless"?
  (3) does imposing one EXACTLY massless reproduce the leptons (i.e. DERIVE √2)?
"""
import numpy as np

m  = np.array([0.51099895, 105.6583755, 1776.86])   # e, mu, tau  (MeV, PDG)
sm = np.sqrt(m)
M  = sm.mean()                     # ring centre-offset = <√m>
dev = sm/M - 1.0                   # = A cos(phi_k)
var = np.var(sm/M)                 # population variance of √m/M  (= A^2/2)
A   = np.sqrt(2*var)
Q   = (1 + A**2/2)/3

print("Koide ring, straight from the leptons")
print("="*62)
print(f"  M = <√m>            = {M:.4f} √MeV")
print(f"  √m/M                = [{sm[0]/M:.4f}, {sm[1]/M:.4f}, {sm[2]/M:.4f}]")
print(f"  A = √(2·Var(√m/M))  = {A:.5f}      (√2 = {np.sqrt(2):.5f})")
print(f"  Q = (1 + A²/2)/3    = {Q:.5f}      (target 2/3 = {2/3:.5f})")
print(f"  ==> A=√2  <=>  Var(√m/M) = 1  <=>  sigma(√m) = <√m>   (CV = {np.std(sm)/np.mean(sm):.5f})")
print()

# (2) is the electron near the massless point?
phi_e        = np.degrees(np.arccos(dev[0]/A))
phi_massless = np.degrees(np.arccos(-1/A))
print(f"  electron phase  φ_e      = {phi_e:.2f}°")
print(f"  massless point (√m=0) at φ = {phi_massless:.2f}°")
print(f"  ==> electron sits {abs(phi_e-phi_massless):.2f}° from massless: NEAR, not AT.")
print()

# (3) impose one EXACTLY massless (A=√2, φ=135°): does it reproduce m_tau/m_mu?
ph  = np.radians(135.0) + np.radians([0, 120, 240])
sml = 1 + np.sqrt(2)*np.cos(ph)
mml = np.sort(sml**2)
print(f"  IF one lepton were EXACTLY massless (A=√2, φ=135°):")
print(f"     √m/M = [{sml[0]:.3f}, {sml[1]:.3f}, {sml[2]:.3f}]  ->  heavy ratio = {mml[2]/mml[1]:.2f}")
print(f"     actual m_tau/m_mu = {m[2]/m[1]:.2f}   ->  off by {100*abs(mml[2]/mml[1]-m[2]/m[1])/(m[2]/m[1]):.0f}%")
print()
print("VERDICT")
print("-"*62)
print("  A=√2 is real and to 5 digits, and it has a clean meaning: the spread of")
print("  √m equals its mean (CV=1, a 'critical' spread). The family IS 2 heavy + 1")
print("  near-massless -- the electron is 2.3° off the massless point, so JP's picture")
print("  is right. BUT √2 is the ring's CV=1 eccentricity, a SEPARATE fact from the")
print("  phase θ that places the electron near-massless; imposing EXACT masslessness")
print("  misses m_tau/m_mu by ~20%. So the 3-body reading REFRAMES √2 (as σ=μ) and")
print("  confirms the near-massless electron, but does not yet DERIVE √2 or locate M.")
print("  The sharpened target: what forces the spread of √m to equal its mean?")
