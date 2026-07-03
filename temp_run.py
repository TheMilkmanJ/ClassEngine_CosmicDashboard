
from classy import Class
c = Class()
c.set({'omega_b': 0.02275, 'omega_cdm': 0.12, 'H0': 67.4, 'A_s': 2.111534442254061e-09, 'n_s': 0.965, 'z_reio': 8.0, 'xi_prtoe': 1.0119e-07, 'zeta_prtoe': 0.01, 'V0_prtoe': 0.6857, 'lambda_prtoe': 0.05, 'm_prtoe': 0.05, 'beta_prtoe': 1e-06, 'use_prtoe': 'yes', 'output': 'mPk', 'modes': 's'})
c.compute()
print(c.luminosity_distance(0.5))
