import time
from classy import Class

cosmo = Class()
params = {
    'output': 'tCl, pCl, lCl, mPk',
    'l_max_scalars': 2500,
    'P_k_max_h/Mpc': 1.,
    'z_pk': '0.0',
    'A_s': 2.1e-09,
    'n_s': 0.965,
    'h': 0.758,
    'omega_b': 0.0224,
    'omega_cdm': 0.1200,
    'tau_reio': 0.0544,
    'varying_fundamental_constants': 'instantaneous',
    'varying_alpha': 1.05,
    'use_dcdf': 'yes',
    'Omega0_dcdf': 0.95,
    'dcdf_rho_inf': 0.7,
    'dcdf_beta': 5e-5,
    'non_linear': 'none',
}
cosmo.set(params)

t0 = time.time()
try:
    cosmo.compute()
    t1 = time.time()
    print(f"Compute SUCCESS in {t1-t0:.2f} seconds.")
except Exception as e:
    t1 = time.time()
    print(f"Compute FAILED in {t1-t0:.2f} seconds. Error: {e}")
