#!/usr/bin/env python3
"""
Realign the comb: with the derived physics (A_s, n_s, varying_me) held FIXED, scan
H0 (the theta_s knob) and watch the Planck high-l chi^2 move. If theta_s is the
whole story, there is an H0 where the high-l penalty collapses toward LCDM's ~584.

Run:  /usr/bin/python3.12 scripts/cmb_realign.py
"""
import numpy as np
from cobaya.model import get_model

PKG = "/home/themilkmanj/cobaya_packages_clean"
model_extra = {
    'use_dcdf': 'yes', 'varying_fundamental_constants': 'instantaneous',
    'varying_alpha': 1.0, 'varying_transition_redshift': 50.0,
    'varying_transition_width': 0.25, 'dcdf_deltam_mode': 1,
    'dcdf_z_rad_onset': 3.5619e7, 'non_linear': 'halofit',
    'N_ur': 2.0328, 'N_ncdm': 1, 'T_ncdm': 0.71611,
    'lensing': 'yes', 'l_max_scalars': 3000,
}
info = {
    'packages_path': PKG,
    'theory': {'classy': {'extra_args': dict(model_extra), 'stop_at_error': True}},
    'likelihood': {'planck_2018_lowl.TT': None, 'planck_2018_lowl.EE': None,
                   'planck_2018_highl_plik.TTTEEE_lite': None,
                   'planck_2018_lensing.clik': None},
    'params': {
        'H0': {'prior': {'min': 64.0, 'max': 78.0}},
        'omega_b': {'prior': {'min': 0.020, 'max': 0.025}},
        'z_reio': {'prior': {'min': 4.0, 'max': 12.0}},
        'dcdf_rho_inf': {'prior': {'min': 0.50, 'max': 0.80}},
        'A_s': 2.088058e-09, 'n_s': 0.9641, 'varying_me': 1.012543,
        'm_ncdm': 0.0654, 'xi_Neff': 0.0,
        'Omega0_dcdf': {'value': 'lambda omega_b, H0: 1.0 - omega_b/(H0/100.0)**2',
                        'derived': False},
        'YHe': {'value': 'lambda omega_b, varying_me: 0.2471 + 0.0096*np.log(omega_b/0.02236)'
                         ' + 0.00176009*((varying_me-1)*100) + (-5.105e-05)*((varying_me-1)*100)**2',
                'derived': False},
        'A_planck': 1.0,
    },
}

print("building the Planck model (loads clik once) ...")
model = get_model(info)
names = list(model.likelihood)
i_hi = names.index('planck_2018_highl_plik.TTTEEE_lite')

def evaluate(H0, ob=0.022757, zr=8.363414, rho=0.701221):
    lp = model.logposterior({'H0': H0, 'omega_b': ob, 'z_reio': zr, 'dcdf_rho_inf': rho})
    return -2*np.array(lp.loglikes)

print("\nscanning H0 (omega_b, z_reio, rho_inf fixed at fiducial):")
print(f"  {'H0':>6s} {'lowlTT':>7s} {'lowlEE':>7s} {'highl':>8s} {'lens':>6s} {'TOTAL':>8s}")
best = None
for H0 in [68.0, 69.0, 69.613, 70.0, 71.0, 72.0, 73.0, 74.0]:
    try:
        chis = evaluate(H0); tot = chis.sum()
        print(f"  {H0:6.2f} {chis[names.index('planck_2018_lowl.TT')]:7.1f}"
              f" {chis[names.index('planck_2018_lowl.EE')]:7.1f} {chis[i_hi]:8.1f}"
              f" {chis[names.index('planck_2018_lensing.clik')]:6.1f} {tot:8.1f}")
        if best is None or tot < best[1]:
            best = (H0, tot, chis[i_hi])
    except Exception as e:
        print(f"  {H0:6.2f}  eval failed: {e}")

print("\n" + "="*60)
print("REALIGNMENT RESULT (H0 scan, physics fixed)")
print("="*60)
if best:
    try:
        from classy import Class
        c = Class(); c.set({'use_dcdf':'yes','varying_fundamental_constants':'instantaneous',
            'varying_alpha':1.0,'varying_transition_redshift':50.0,'varying_transition_width':0.25,
            'dcdf_deltam_mode':1,'dcdf_z_rad_onset':3.5619e7,'dcdf_rho_inf':0.701221,
            'varying_me':1.012543,'omega_b':0.022757,'H0':best[0],
            'Omega0_dcdf':1.0-0.022757/(best[0]/100.0)**2,
            'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.0654,'T_ncdm':0.71611,'output':''})
        c.compute(); th = c.get_current_derived_parameters(['100*theta_s'])['100*theta_s']
        c.struct_cleanup(); c.empty()
    except Exception as e:
        th = float('nan')
    print(f"  best H0 in scan       = {best[0]:.2f}")
    print(f"  100*theta_s there     = {th:.5f}   (Planck 1.04109)")
    print(f"  high-l chi2 there     = {best[2]:.1f}   (fiducial was 782, LCDM 584)")
    print(f"  TOTAL Planck chi2     = {best[1]:.1f}   (fiducial was 1215, LCDM 1012)")
    print("  (H0 alone, other 3 background params at fiducial -- a 1D slice, not the")
    print("   full 4D minimum; that only goes lower.)")
