from classy import Class
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
    'modes': 's', 'perturbations_verbose': 3
}
c = Class()
c.set(pars)
print("Computing background...", flush=True)
c.compute(level=["background"])
print("Computing thermodynamics...", flush=True)
c.compute(level=["thermodynamics"])
print("Computing perturbations...", flush=True)
c.compute(level=["perturbations"])
print("Computing primordial...", flush=True)
c.compute(level=["primordial"])
print("Computing harmonic...", flush=True)
c.compute(level=["harmonic"])
print("Computing fourier...", flush=True)
c.compute(level=["fourier"])
print("Computing lensing...", flush=True)
c.compute(level=["lensing"])
print("DONE", flush=True)
