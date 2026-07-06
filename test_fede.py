import os
import numpy as np
from classy import Class

c = Class()
c.set({
    'h': 0.674, 'Omega_b': 0.05, 'Omega_cdm': 0.25,
    'A_s': 2.1e-9, 'n_s': 0.965,
    'use_prtoe': 'yes',
    'm_prtoe': 2.0,
    'phi_c_prtoe': 0.15,
    'Omega0_prtoe': 0.7,
    'Omega_Lambda': 0.0,
    'root': os.environ.get('PRTOE_CLASS_ROOT', './'),
})
print("Computing...")
c.compute()
bg = c.get_background()
z = bg['z']
f_ede = bg['(.)rho_fld'] / bg['(.)rho_crit']
mask = (z > 100) & (z < 5000)
max_f = np.max(f_ede[mask])
print(f"Max f_EDE = {max_f*100:.6f}%")
