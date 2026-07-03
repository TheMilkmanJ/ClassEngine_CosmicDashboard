from classy import Class
import time
pars = {
    'omega_b': 0.02275,
    'omega_cdm': 0.12,
    'H0': 67.4,
    'A_s': 2.111534442254061e-09,
    'n_s': 0.965,
    'z_reio': 8.0,
    'xi_prtoe': 1e-8,
    'zeta_prtoe': 0.1,
    'V0_prtoe': 0.6857,
    'lambda_prtoe': 0.05,
    'm_prtoe': 0.05,
    'beta_prtoe': 1.0e-6,
    'use_prtoe': 'yes',
    'output': 'mPk',
    'modes': 's',
    'background_verbose': 3
}
c = Class()
c.set(pars)
print("Computing...", flush=True)
c.compute()
print("Done compute. Calling luminosity_distance...", flush=True)
d = c.luminosity_distance(0.5)
print(f"Distance: {d}", flush=True)
