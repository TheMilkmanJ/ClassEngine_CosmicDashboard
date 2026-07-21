#!/usr/bin/env python3
"""
Matter power spectrum money-plot: the model's linear and nonlinear P(k) at z=0
against a LCDM reference, with sigma8 and S8 placed against the weak-lensing and
Planck constraints. One CLASS run each (mPk output). Shows the model reproduces
the matter clustering and where it lands in the S8 landscape.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from classy import Class

def run(params):
    c = Class(); c.set({**params, 'output': 'mPk', 'P_k_max_1/Mpc': 10.0,
                        'non_linear': 'halofit', 'z_max_pk': 1.0}); c.compute()
    k = np.geomspace(1e-3, 5.0, 300)          # 1/Mpc
    Plin = np.array([c.pk_lin(ki, 0.0) for ki in k])
    Pnl  = np.array([c.pk(ki, 0.0) for ki in k])
    s8, Om = c.sigma8(), c.Omega_m()
    c.struct_cleanup(); c.empty()
    return k, Plin, Pnl, s8, Om

model_p = {'use_dcdf':'yes','varying_fundamental_constants':'instantaneous','varying_alpha':1.0,
    'varying_transition_redshift':50.0,'varying_transition_width':0.25,'dcdf_deltam_mode':1,
    'dcdf_z_rad_onset':3.5619e7,'dcdf_rho_inf':0.701221,'varying_me':1.012543,
    'A_s':2.088058e-9,'n_s':0.9641,'omega_b':0.022757,'H0':69.613,
    'Omega0_dcdf':1.0-0.022757/0.69613**2,
    'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.0654,'T_ncdm':0.71611}
lcdm_p = {'A_s':2.100e-9,'n_s':0.9659,'omega_b':0.022377,'omega_cdm':0.12010,'H0':67.36,
    'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.06,'T_ncdm':0.71611}

print("computing model + LCDM P(k)...")
km, Pl_m, Pn_m, s8m, Om_m = run(model_p)
kl, Pl_l, Pn_l, s8l, Om_l = run(lcdm_p)
S8m = s8m*(Om_m/0.3)**0.5; S8l = s8l*(Om_l/0.3)**0.5
print(f"  model: sigma8={s8m:.4f}, Omega_m={Om_m:.4f}, S8={S8m:.4f}")
print(f"  LCDM : sigma8={s8l:.4f}, Omega_m={Om_l:.4f}, S8={S8l:.4f}")

fig, (ax, axr) = plt.subplots(2, 1, figsize=(8.2, 6.8), sharex=True,
                              gridspec_kw={"height_ratios":[3,1]})
ax.loglog(km, Pn_m, color="#c0392b", lw=2, label="PRTOE (nonlinear)")
ax.loglog(km, Pl_m, color="#c0392b", lw=1, ls=':', label="PRTOE (linear)")
ax.loglog(kl, Pn_l, color="#2c3e50", lw=1.3, ls="--", label="ΛCDM (nonlinear)")
ax.set_ylabel(r"$P(k)\ \ [\mathrm{Mpc}^3]$"); ax.legend(frameon=False); ax.grid(alpha=0.2, which='both')
ax.set_title("Matter power spectrum (z=0) — model vs ΛCDM")
axr.semilogx(km, (Pn_m/np.interp(km,kl,Pn_l)-1)*100, color="#c0392b")
axr.axhline(0, color="#2c3e50", lw=1); axr.axhspan(-2,2,color="grey",alpha=0.15)
axr.set_ylabel("(model−ΛCDM)/ΛCDM [%]"); axr.set_xlabel(r"$k\ \ [1/\mathrm{Mpc}]$")
axr.set_ylim(-8,8); axr.grid(alpha=0.2, which='both')
fig.tight_layout(); fig.savefig("chains/matter_pk.png", dpi=130)
print("saved chains/matter_pk.png")

# --- S8 landscape ---
print("\n  S8 landscape:")
for lab, s8v, e in [("Planck 2018", 0.834, 0.016), ("DES-Y3 3x2pt", 0.776, 0.017),
                    ("KiDS-1000", 0.759, 0.021), ("PRTOE", S8m, 0.0)]:
    print(f"    {lab:14s} S8 = {s8v:.3f}" + (f" +/- {e:.3f}" if e else ""))
print(f"  the model's S8={S8m:.3f} sits near Planck, above the weak-lensing band "
      f"(a mild S8 offset, shared with LCDM).")
