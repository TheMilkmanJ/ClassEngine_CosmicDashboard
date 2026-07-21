#!/usr/bin/env python3
"""
The real realignment: minimise the Planck chi^2 over the FOUR background parameters
(H0, omega_b, z_reio, dcdf_rho_inf) together, with the derived physics fixed. The
1D H0 slice showed H0 alone cannot move theta_s without breaking the peak heights
(the dcdf-is-everything closure welds H0 to the dark density); this lets omega_b
and rho_inf compensate. Verdict: does the high-l chi^2 reach LCDM's ~584, or stick?

Run:  /usr/bin/python3.12 scripts/cmb_realign_4d.py
"""
import numpy as np
from cobaya.model import get_model
from scipy.optimize import minimize

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
print("building the Planck model ...", flush=True)
model = get_model(info)
names = list(model.likelihood)
i_hi = names.index('planck_2018_highl_plik.TTTEEE_lite')

neval = [0]; best = [None]
def chi2(x):
    H0, ob, zr, rho = x
    if not (64 < H0 < 78 and 0.020 < ob < 0.025 and 4 < zr < 12 and 0.50 < rho < 0.80):
        return 1e7
    neval[0] += 1
    try:
        chis = -2*np.array(model.logposterior({'H0': H0, 'omega_b': ob,
               'z_reio': zr, 'dcdf_rho_inf': rho}).loglikes)
        c = chis.sum()
    except Exception:
        return 1e7
    if best[0] is None or c < best[0][0]:
        best[0] = (c, chis[i_hi], (H0, ob, zr, rho))
        print(f"  [{neval[0]:3d}] NEW BEST chi2={c:8.1f}  high-l={chis[i_hi]:7.1f}  "
              f"H0={H0:.2f} ob={ob:.5f} zr={zr:.2f} rho={rho:.4f}", flush=True)
    return c

x0 = np.array([69.613, 0.022757, 8.363414, 0.701221])
print(f"start (fiducial): chi2={chi2(x0):.1f}\n", flush=True)
res = minimize(chi2, x0, method='Nelder-Mead',
               options={'maxiter': 120, 'xatol': 0.003, 'fatol': 0.4, 'adaptive': True})

print("\n" + "="*62)
print("4D REALIGNMENT VERDICT (physics fixed; H0, omega_b, z_reio, rho_inf fit)")
print("="*62)
c, hi, x = best[0]
print(f"  best-fit H0={x[0]:.2f}, omega_b={x[1]:.5f}, z_reio={x[2]:.2f}, rho_inf={x[3]:.4f}")
print(f"  high-l chi2 = {hi:.1f}   (fiducial 782, LCDM 584)")
print(f"  TOTAL Planck chi2 = {c:.1f}   (fiducial 1215, LCDM 1012)")
print(f"  Delta vs LCDM = {c-1012.2:+.1f}   ({neval[0]} evals)")
if c - 1012.2 < 30:
    print("  -> the comb REALIGNS: the model fits the CMB at its own best-fit, and the")
    print("     +200 was the un-refit theta_s. The closure is viable.")
elif hi - 584 < 60:
    print("  -> high-l largely recovers; a modest residual remains (worth locating).")
else:
    print("  -> a real residual STICKS after the fit: the closure cannot match the CMB")
    print("     as well as LCDM at fixed derived physics. A genuine, important tension.")
