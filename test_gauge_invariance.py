"""FALSIFIABLE TEST: gauge invariance of dCDF v5 (beta-free).

If the dCDF perturbation equations and Einstein couplings are correct,
observables must agree between synchronous and Newtonian gauges (up to
CLASS's own numerical gauge noise, ~1e-4 for LCDM at low ell).

v5 (2026-07-05): dcdf_beta removed from the model; this script no longer
passes it. Known v4-era defect being tracked: 0.26% TT deviation at
ell=10-12 on the newtonian branch (late ISW).
"""
from classy import Class
import numpy as np

common_params = {
    'use_dcdf': 'yes',
    'dcdf_rho_inf': 0.7,
    'xi_Neff': 0.2,
    'omega_b': 0.0224,
    'Omega_cdm': 0.0,
    'Omega_Lambda': 0.0,
    'Omega0_dcdf': 1.0 - 0.0224 / (0.674**2),
    'H0': 67.4,
    'output': 'tCl, mPk',
    'P_k_max_1/Mpc': 1.0,
    'z_max_pk': 0.0,
    'l_max_scalars': 2000,
}

cls = {}
pks = {}
s8s = {}
for gauge in ('synchronous', 'newtonian'):
    M = Class()
    M.set(common_params)
    M.set({'gauge': gauge})
    M.compute()
    cls[gauge] = M.raw_cl(2000)
    pks[gauge] = M.pk(0.1, 0.0)
    s8s[gauge] = M.sigma8()
    M.struct_cleanup()
    M.empty()

tt_s = cls['synchronous']['tt'][2:]
tt_n = cls['newtonian']['tt'][2:]
ell = cls['synchronous']['ell'][2:]
rel = np.abs(tt_n / tt_s - 1.0)

print("ell   rel.dev(TT)")
for l in range(2, 31):
    i = l - 2
    flag = "  <--" if rel[i] > 1e-3 else ""
    print(f"{l:4d}  {rel[i]:.2e}{flag}")

imax = int(np.argmax(rel))
print(f"\nmax |dCl_TT/Cl_TT| = {rel[imax]:.3e} at ell={ell[imax]}")
print(f"median             = {np.median(rel):.3e}")
print(f"sigma8: sync {s8s['synchronous']:.6f}  newt {s8s['newtonian']:.6f}  "
      f"rel {abs(s8s['newtonian']/s8s['synchronous']-1):.2e}")
print(f"P(k=0.1): sync {pks['synchronous']:.6e}  newt {pks['newtonian']:.6e}  "
      f"rel {abs(pks['newtonian']/pks['synchronous']-1):.2e}")

verdict = "PASS" if rel.max() < 1e-3 else "FAIL (defect present)"
print(f"\nVERDICT: {verdict}")
