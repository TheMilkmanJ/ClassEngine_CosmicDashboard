#!/usr/bin/env python3
"""
The real Planck chi^2 at the derived stack — a SINGLE point evaluation (no MCMC,
no PolyChord). Loads the Planck 2018 likelihoods via cobaya, computes the model's
C_l at the fixed derived parameters, and reads off chi^2 = -2 lnL per likelihood.
Then the same for LCDM at Planck's best-fit, for the honest comparison.

Run:  /usr/bin/python3.12 scripts/cmb_chi2.py
"""
import sys
import numpy as np
from cobaya.model import get_model

PKG = "/home/themilkmanj/cobaya_packages_clean"

# ---- the model's classy extra_args (the dcdf / varying-const machinery) -------
model_extra = {
    'use_dcdf': 'yes',
    'varying_fundamental_constants': 'instantaneous',
    'varying_alpha': 1.0,
    'varying_transition_redshift': 50.0,
    'varying_transition_width': 0.25,
    'dcdf_deltam_mode': 1,
    'dcdf_z_rad_onset': 3.5619e7,
    'non_linear': 'halofit',
    'N_ur': 2.0328, 'N_ncdm': 1, 'T_ncdm': 0.71611,
    'lensing': 'yes', 'l_max_scalars': 3000,
}
planck = {
    'planck_2018_lowl.TT': None,
    'planck_2018_lowl.EE': None,
    'planck_2018_highl_plik.TTTEEE_lite': None,
    'planck_2018_lensing.clik': None,
}

def chi2_of(info, point, label):
    print(f"\n>>> building {label} ...")
    model = get_model(info)
    lp = model.logposterior(point)
    names = list(model.likelihood)
    print(f"--- {label}: chi^2 = -2 lnL per Planck likelihood ---")
    tot = 0.0
    for n, ll in zip(names, lp.loglikes):
        print(f"    {n:38s}  chi2 = {-2*ll:9.2f}")
        tot += -2*ll
    print(f"    {'TOTAL Planck chi2':38s}  chi2 = {tot:9.2f}")
    return tot

# ============================================================ the model
model_info = {
    'packages_path': PKG,
    'theory': {'classy': {'extra_args': dict(model_extra), 'stop_at_error': True}},
    'likelihood': dict(planck),
    'params': {
        'omega_b': 0.022757,
        'H0': 69.613,
        'A_s': 2.088058e-09,        # derived census amplitude
        'n_s': 0.9641,              # derived census tilt
        'z_reio': 8.363414,
        'varying_me': 1.012543,     # 1 + 27 alpha/5 pi
        'dcdf_rho_inf': 0.701221,
        'm_ncdm': 0.0654,
        'xi_Neff': 0.0,
        'Omega0_dcdf': {'value': 'lambda omega_b, H0: 1.0 - omega_b/(H0/100.0)**2',
                        'derived': False},
        'YHe': {'value': 'lambda omega_b, varying_me: 0.2471 + 0.0096*np.log(omega_b/0.02236)'
                         ' + 0.00176009*((varying_me-1)*100) + (-5.105e-05)*((varying_me-1)*100)**2',
                'derived': False},
        'A_planck': 1.0,
    },
}

# ============================================================ LCDM reference
lcdm_info = {
    'packages_path': PKG,
    'theory': {'classy': {'extra_args': {'non_linear': 'halofit', 'N_ur': 2.0328,
              'N_ncdm': 1, 'T_ncdm': 0.71611, 'lensing': 'yes', 'l_max_scalars': 3000},
              'stop_at_error': True}},
    'likelihood': dict(planck),
    'params': {
        'omega_b': 0.022377, 'omega_cdm': 0.12010, 'H0': 67.36,
        'A_s': 2.100e-9, 'n_s': 0.9659, 'tau_reio': 0.0544,
        'm_ncdm': 0.06, 'A_planck': 1.0,
    },
}

try:
    c_model = chi2_of(model_info, {}, "PRTOE (derived stack)")
except Exception as e:
    print("MODEL chi2 FAILED:", repr(e)); c_model = None
try:
    c_lcdm = chi2_of(lcdm_info, {}, "LCDM (Planck 2018 best-fit)")
except Exception as e:
    print("LCDM chi2 FAILED:", repr(e)); c_lcdm = None

print("\n" + "="*64)
print("VERDICT — the real Planck chi^2, at the fixed points (not fitted)")
print("="*64)
if c_model is not None and c_lcdm is not None:
    print(f"  PRTOE derived stack : chi2 = {c_model:.1f}")
    print(f"  LCDM Planck best-fit: chi2 = {c_lcdm:.1f}")
    print(f"  Delta chi2 (model - LCDM) = {c_model - c_lcdm:+.1f}")
    print("  (LCDM is AT its best fit; PRTOE is at its DERIVED stack, NOT refit --")
    print("   so a modest positive Delta is expected and is the honest headroom the")
    print("   full MCMC recovers. A blow-up would mean the derived stack misses.)")
else:
    print("  (one side failed to evaluate; see errors above)")
