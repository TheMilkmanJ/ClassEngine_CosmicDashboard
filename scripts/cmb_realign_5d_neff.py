#!/usr/bin/env python3
"""
The deuterium<->high-l link test: repeat the 4D Planck realignment with the model's
own dark-radiation knob xi_Neff FREED (it is nailed to 0 in every headline chain).
xi_Neff is DeltaN_eff added straight onto 3.044 (source/input.c:2528). The model
predicts a committed window DeltaN_eff in [0.06, 0.24] from the genesis dilution.

The question JP posed: is there ONE piece between Genesis and Recombination that
both the deuterium abundance and the high-l peaks hang on? If freeing xi_Neff pulls
the CMB-preferred omega_b DOWN toward the deuterium-optimal 0.02237 while the high-l
chi^2 stays fit, that piece is the below-T_c dark radiation, and it links both.
If the fit drives xi_Neff -> 0, the CMB does not want it and the link is broken.

Run:  /usr/bin/python3.12 scripts/cmb_realign_5d_neff.py
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
        'xi_Neff': {'prior': {'min': 0.0, 'max': 0.35}},   # <-- FREED (was 0.0)
        'A_s': 2.088058e-09, 'n_s': 0.9641, 'varying_me': 1.012543,
        'm_ncdm': 0.0654,
        'Omega0_dcdf': {'value': 'lambda omega_b, H0: 1.0 - omega_b/(H0/100.0)**2',
                        'derived': False},
        'YHe': {'value': 'lambda omega_b, varying_me: 0.2471 + 0.0096*np.log(omega_b/0.02236)'
                         ' + 0.00176009*((varying_me-1)*100) + (-5.105e-05)*((varying_me-1)*100)**2',
                'derived': False},
        'A_planck': 1.0,
    },
}
print("building the Planck model (xi_Neff freed) ...", flush=True)
model = get_model(info)
names = list(model.likelihood)
i_hi = names.index('planck_2018_highl_plik.TTTEEE_lite')

neval = [0]; best = [None]
def chi2(x):
    H0, ob, zr, rho, xi = x
    if not (64 < H0 < 78 and 0.020 < ob < 0.025 and 4 < zr < 12
            and 0.50 < rho < 0.80 and 0.0 <= xi < 0.35):
        return 1e7
    neval[0] += 1
    try:
        chis = -2*np.array(model.logposterior({'H0': H0, 'omega_b': ob, 'z_reio': zr,
               'dcdf_rho_inf': rho, 'xi_Neff': xi}).loglikes)
        c = chis.sum()
    except Exception:
        return 1e7
    if best[0] is None or c < best[0][0]:
        best[0] = (c, chis[i_hi], (H0, ob, zr, rho, xi))
        print(f"  [{neval[0]:3d}] NEW BEST chi2={c:8.1f}  high-l={chis[i_hi]:7.1f}  "
              f"H0={H0:.2f} ob={ob:.5f} zr={zr:.2f} rho={rho:.4f} xi={xi:.4f}", flush=True)
    return c

# warm-start near the 4D min, xi_Neff seeded mid-window so it is not born on the boundary
x0 = np.array([70.80, 0.02290, 8.20, 0.7000, 0.120])
print(f"start: chi2={chi2(x0):.1f}\n", flush=True)
res = minimize(chi2, x0, method='Nelder-Mead',
               options={'maxiter': 180, 'xatol': 0.003, 'fatol': 0.4, 'adaptive': True})

print("\n" + "="*66)
print("5D REALIGNMENT VERDICT (physics fixed; H0, omega_b, z_reio, rho_inf, xi_Neff)")
print("="*66)
c, hi, x = best[0]
print(f"  best-fit H0={x[0]:.2f}, omega_b={x[1]:.5f}, z_reio={x[2]:.2f}, "
      f"rho_inf={x[3]:.4f}, xi_Neff={x[4]:.4f}")
print(f"  high-l chi2 = {hi:.1f}   (4D-min 595, LCDM 584)")
print(f"  TOTAL Planck chi2 = {c:.1f}   (4D-min 1025, LCDM 1012)")
print(f"  Delta vs LCDM = {c-1012.2:+.1f}   ({neval[0]} evals)")
print()
print(f"  omega_b moved 0.02290 -> {x[1]:.5f}  (deuterium-optimal 0.02237)")
if x[4] > 0.03 and x[1] < 0.02275:
    print("  -> the CMB WANTS the dark radiation AND it pulls omega_b toward deuterium.")
    print("     The below-T_c dark radiation is the shared piece: it eases both.")
elif x[4] < 0.03:
    print("  -> the fit drives xi_Neff -> 0: the CMB does NOT want the dark radiation.")
    print("     high-l and deuterium are not linked through DeltaN_eff at the CMB.")
else:
    print("  -> xi_Neff wanted, but omega_b did not move to deuterium: a partial link.")
