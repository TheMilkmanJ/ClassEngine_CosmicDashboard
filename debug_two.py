from classy import Class
c_lcdm = Class()
c_lcdm.set({
    'omega_b': 0.02275,
    'omega_cdm': 0.12,
    'H0': 67.4,
    'A_s': 2.111534442254061e-09,
    'n_s': 0.965,
    'z_reio': 8.0,
    'output': 'mPk',
    'modes': 's'
})
c_lcdm.compute()
print("LCDM DONE")

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
    'modes': 's'
}
c = Class()
c.set(pars)
c.compute()
print("PRTOE DONE")
