import sys
sys.path.insert(0, '/home/themilkmanj/prtoe_class')
from classy import Class

cosmo = Class()
params = {
    'omega_b': 0.0224, 'H0': 74.8, 'A_s': 2.1115e-09, 'n_s': 0.965, 'z_reio': 8.0,

    'use_dcdf': 'yes', 'dcdf_rho_inf': 0.7, 'Omega0_dcdf': 0.96, 'xi_Neff': 0.3,
    'm_ncdm': 0.06, 'varying_alpha': 1.05, 'dcdf_beta': 3.3e-05,
    'varying_fundamental_constants': 'instantaneous',
    'N_ur': 2.0328, 'N_ncdm': 1, 'T_ncdm': 0.71611,
    'omega_cdm': 1e-5,
    'output': 'tCl, pCl, lCl, mPk', 'l_max_scalars': 2500
}
cosmo.set(params)
cosmo.compute()
print("CLASS compute finished!")
