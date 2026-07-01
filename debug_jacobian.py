#!/usr/bin/env python3
"""
Minimal reproduction of singular Jacobian issue
"""
import sys
sys.path.insert(0, '.')

from classy import Class

# Minimal PRTOE config that triggers singular Jacobian
params = {
    'use_prtoe': 'yes',
    'xi_prtoe': 5e-6,
    'zeta_prtoe': 1.0,
    'lambda_prtoe': 0.1,
    'm_prtoe': 0.1,
    'phi_0_prtoe': 0.1,
    'prtoe_beta': 1e-6,
    
    'H0': 67.0,
    'Omega_b': 0.05,
    'Omega_cdm': 0.27,
    'Omega_lambda': 0.68,
    
    # Try to compute power spectrum - this triggers perturbations
    'output': 'mPk',
    'P_k_max_1/Mpc': 0.1,  # Very small k to avoid stiffness
    'z_max_pk': 100,
}

print("Attempting to initialize CLASS with minimal PRTOE + mPk...")
print("This should trigger the singular Jacobian error if it exists.")
print("")

try:
    cosmo = Class()
    cosmo.set(params)
    print("Computing...")
    cosmo.compute()
    print("✅ SUCCESS!")
except Exception as e:
    error_str = str(e)
    if "singular" in error_str.lower() or "ludcmp" in error_str.lower():
        print("❌ SINGULAR JACOBIAN CONFIRMED")
        print(f"\nError:\n{error_str[:500]}")
    else:
        print(f"❌ Different error:\n{error_str[:500]}")
