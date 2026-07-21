#!/usr/bin/env python3
"""
SNe Ia Hubble-diagram money-plot: the model's distance modulus mu(z) against the
Pantheon+ SH0ES supernovae. The SNe fix the SHAPE of mu(z) (the acceleration);
the absolute offset is the M_B / H0 calibration (fit here as one nuisance, since
without the Cepheid anchor the model does not set the absolute rung). Background-
only CLASS, real data. Shows the model reproduces the acceleration.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from classy import Class

DAT = "/home/themilkmanj/cobaya_packages_clean/data/sn_data/PantheonPlus/Pantheon+SH0ES.dat"
d = np.genfromtxt(DAT, names=True, dtype=None, encoding=None)
keep = (d['IS_CALIBRATOR'] == 0) & (d['zHD'] > 0.01)
z, mu, sig = d['zHD'][keep], d['MU_SH0ES'][keep], d['MU_SH0ES_ERR_DIAG'][keep]
print(f"Pantheon+ Hubble-flow SNe (non-calibrator, z>0.01): {z.size}")

def mu_model(params):
    c = Class(); c.set({**params, 'output': ''}); c.compute()
    zz = np.geomspace(0.01, 2.3, 300)
    dL = np.array([c.luminosity_distance(zi) for zi in zz])   # Mpc
    c.struct_cleanup(); c.empty()
    return zz, 5*np.log10(dL) + 25

model_p = {'use_dcdf':'yes','varying_fundamental_constants':'instantaneous','varying_alpha':1.0,
    'varying_transition_redshift':50.0,'varying_transition_width':0.25,'dcdf_deltam_mode':1,
    'dcdf_z_rad_onset':3.5619e7,'dcdf_rho_inf':0.701221,'varying_me':1.012543,
    'omega_b':0.022757,'H0':69.613,'Omega0_dcdf':1.0-0.022757/0.69613**2,
    'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.0654,'T_ncdm':0.71611}
lcdm_p = {'omega_b':0.022377,'omega_cdm':0.12010,'H0':67.36,
    'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.06,'T_ncdm':0.71611}

print("computing model + LCDM luminosity distances...")
zz, mm = mu_model(model_p)
_, ml = mu_model(lcdm_p)
mu_m_at = np.interp(z, zz, mm)                      # model mu at the SN redshifts
# fit the single offset (M_B/H0 nuisance) by inverse-variance weighting
dM = np.sum((mu - mu_m_at)/sig**2) / np.sum(1/sig**2)
chi2 = np.sum(((mu - mu_m_at - dM)/sig)**2)
print(f"  fitted offset dM = {dM:+.3f} mag; shape chi2 = {chi2:.1f} / {z.size} SNe (diag)")

fig, (ax, axr) = plt.subplots(2, 1, figsize=(8.2, 6.8), sharex=True,
                              gridspec_kw={"height_ratios":[3,1]})
ax.errorbar(z, mu, yerr=sig, fmt='.', ms=2, color="#95a5a6", alpha=0.35, elinewidth=0.4,
            label=f"Pantheon+ ({z.size} SNe)", zorder=1)
ax.plot(zz, mm+dM, color="#c0392b", lw=2, label="PRTOE", zorder=4)
ax.plot(zz, ml+dM, color="#2c3e50", lw=1.2, ls="--", label="ΛCDM", zorder=3)
ax.set_xscale('log'); ax.set_ylabel(r"distance modulus $\mu$")
ax.set_title("SNe Ia Hubble diagram — model vs Pantheon+"); ax.legend(frameon=False); ax.grid(alpha=0.2)

# binned residuals to the model
res = mu - mu_m_at - dM
bins = np.geomspace(z.min(), z.max(), 14)
bc = np.sqrt(bins[:-1]*bins[1:])
bm, be = [], []
for lo, hi in zip(bins[:-1], bins[1:]):
    m = (z>=lo)&(z<hi)
    if m.sum() > 2:
        w = 1/sig[m]**2
        bm.append(np.sum(res[m]*w)/w.sum()); be.append(1/np.sqrt(w.sum()))
    else:
        bm.append(np.nan); be.append(np.nan)
axr.errorbar(bc, bm, yerr=be, fmt='o', ms=5, color="#c0392b", capsize=3)
axr.axhline(0, color="#2c3e50", lw=1); axr.axhspan(-0.05,0.05,color="grey",alpha=0.15)
axr.set_xscale('log'); axr.set_ylabel(r"$\Delta\mu$ (binned)"); axr.set_xlabel("redshift z")
axr.set_ylim(-0.2,0.2); axr.grid(alpha=0.2)
fig.tight_layout(); fig.savefig("chains/sn_hubble.png", dpi=130)
print("saved chains/sn_hubble.png")
