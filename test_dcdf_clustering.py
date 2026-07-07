from classy import Class
import numpy as np

print("Testing dCDF vs LCDM Clustering...")

# 1. LCDM Baseline
lcdm = Class()
lcdm.set({
    'omega_b': 0.0224,
    'omega_cdm': 0.12,
    'H0': 67.4,
    'output': 'mPk',
    'P_k_max_1/Mpc': 1.0,
    'z_max_pk': 0.0
})
lcdm.compute()
pk_lcdm = lcdm.pk(0.1, 0.0)
sigma8_lcdm = lcdm.sigma8()

# 2. dCDF Model
dcdf = Class()
dcdf.set({
    'use_dcdf': 'yes',
    'dcdf_rho_inf': 0.7,
    'dcdf_beta': 1e-7,
    'xi_Neff': 0.2,
    'omega_b': 0.0224,
    'Omega_cdm': 0.0,
    'Omega_Lambda': 0.0,
    'Omega0_dcdf': 1.0 - 0.0224 / (0.674**2), # Replace CDM + Lambda
    'H0': 67.4,
    'output': 'mPk',
    'P_k_max_1/Mpc': 1.0,
    'z_max_pk': 0.0
})
dcdf.compute()
pk_dcdf = dcdf.pk(0.1, 0.0)
sigma8_dcdf = dcdf.sigma8()

print(f"\n--- LCDM Baseline ---")
print(f"P(k=0.1): {pk_lcdm:.2e}")
print(f"sigma8:   {sigma8_lcdm:.4f}")

print(f"\n--- dCDF Model ---")
print(f"P(k=0.1): {pk_dcdf:.2e}")
print(f"sigma8:   {sigma8_dcdf:.4f}")

ratio = pk_dcdf / pk_lcdm
print(f"\nPower Spectrum Ratio (dCDF / LCDM) at k=0.1: {ratio:.4f}")
if ratio > 0.1:
    print("SUCCESS: dCDF is clustering like dark matter!")
else:
    print("FAILURE: dCDF is not clustering (ratio too small, likely baryon-only clustering).")
