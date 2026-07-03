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
print("Starting LCDM compute...")
c_lcdm.compute()
print("DONE LCDM")
