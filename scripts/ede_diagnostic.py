#!/usr/bin/env python3
"""f_EDE(z) diagnostic from a CLASS background.dat: reports the PRTOE energy
fraction through the z_eq -> recombination window and where it peaks.
Usage: python scripts/ede_diagnostic.py output/v3_x03_g1.0_00_background.dat"""
import sys, numpy as np

if len(sys.argv) != 2:
    raise SystemExit(__doc__)
path = sys.argv[1]
with open(path) as f:
    header = [l for l in f if l.startswith('#')][-1]
cols = [c.strip() for c in header.lstrip('#').split('  ') if c.strip()]
data = np.loadtxt(path)
def col(frag):
    idx = [i for i, c in enumerate(cols) if frag in c]
    if not idx: raise SystemExit(f"column '{frag}' not found; have: {cols}")
    return data[:, idx[0]]
z = col('z')
rho_de = col('rho_prtoe') if any('rho_prtoe' in c for c in cols) else col('rho_scf')
rho_crit = col('rho_crit') if any('rho_crit' in c for c in cols) else None
if rho_crit is None:
    H = col('H [1/Mpc]'); rho_crit = H**2
f = rho_de / rho_crit
win = (z > 500) & (z < 30000)
i = np.argmax(f[win])
print(f"max f_EDE = {100*f[win][i]:.3f}% at z = {z[win][i]:.0f}")
for zz in (3400, 1100, 0):
    j = np.argmin(np.abs(z - zz))
    print(f"  f_EDE(z={zz}) = {100*f[j]:.4f}%")
