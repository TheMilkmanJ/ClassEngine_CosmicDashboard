from classy import Class
import numpy as np

cosmo = Class()
params = {
    'Omega_b': 0.05,
    'Omega_cdm': 0.25,
    'use_prtoe': 'yes',
    'Omega0_prtoe': 0.70,
    'h': 0.67,
    'Omega_Lambda': 0.0,
    'output': 'tCl, mPk',
    'P_k_max_h/Mpc': 1.0,
    'z_max_pk': 10.0
}
try:
    cosmo.set(params)
    cosmo.compute()
    bg = cosmo.get_background()
    print("SUCCESS: Code ran with V4 fluid model!")
    print(f"Computed age: {cosmo.age()} Gyr")
    
    # Let's check fluid density
    keys = bg.keys()
    if '(.)rho_fld' in keys:
        rho_fld = bg['(.)rho_fld'][-1]
        print(f"Final rho_fld: {rho_fld}")
    else:
        print("Fluid density not in background output!")
        print("Keys:", keys)
except Exception as e:
    print("FAILED:", e)
