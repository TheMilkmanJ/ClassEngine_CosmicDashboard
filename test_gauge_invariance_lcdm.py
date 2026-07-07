from classy import Class
import numpy as np

print("Running FALSIFIABLE TEST: Gauge Invariance (LCDM Baseline)")

common_params = {
    'omega_b': 0.0224,
    'omega_cdm': 0.12,
    'H0': 67.4,
    'output': 'tCl, mPk',
    'P_k_max_1/Mpc': 1.0,
    'z_max_pk': 0.0,
    'l_max_scalars': 2000
}

# 1. Synchronous Gauge
sync = Class()
sync.set(common_params)
sync.set({'gauge': 'synchronous'})
sync.compute()
cl_sync = sync.raw_cl(2000)
pk_sync = sync.pk(0.1, 0.0)
sigma8_sync = sync.sigma8()

# 2. Newtonian Gauge
newt = Class()
newt.set(common_params)
newt.set({'gauge': 'newtonian'})
newt.compute()
cl_newt = newt.raw_cl(2000)
pk_newt = newt.pk(0.1, 0.0)
sigma8_newt = newt.sigma8()

print("--- LCDM RESULTS ---")
print(f"Synchronous P(k=0.1): {pk_sync:.4e} | sigma8: {sigma8_sync:.6f}")
print(f"Newtonian P(k=0.1):   {pk_newt:.4e} | sigma8: {sigma8_newt:.6f}")

pk_diff = abs(pk_sync - pk_newt) / pk_sync
s8_diff = abs(sigma8_sync - sigma8_newt) / sigma8_sync
print(f"\nFractional Diff P(k): {pk_diff:.2e}")
print(f"Fractional Diff s8:   {s8_diff:.2e}")

# Compare CMB (l=500)
l = 500
tt_sync = cl_sync['tt'][l]
tt_newt = cl_newt['tt'][l]
cl_diff = abs(tt_sync - tt_newt) / tt_sync
print(f"\nFractional Diff C_l: {cl_diff:.2e}")

