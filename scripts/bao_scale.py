#!/usr/bin/env python3
"""
BAO money-plot: the model's isotropic BAO distance D_V/r_d vs redshift, against the
galaxy-survey measurements and a LCDM reference. Background-only CLASS (fast), no
chain. Shows the model reproduces the standard-ruler distance-redshift relation.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from classy import Class

C_KMS = 299792.458

def distances(params):
    c = Class(); c.set({**params, 'output': ''}); c.compute()
    rd = c.rs_drag()
    def DV_over_rd(z):
        DA = c.angular_distance(z)          # Mpc
        DM = DA*(1+z)                        # comoving angular-diameter distance
        DH = 1.0/c.Hubble(z)                # c/H(z) in Mpc (classy Hubble is 1/Mpc)
        DV = (z*DM*DM*DH)**(1.0/3.0)
        return DV/rd
    zz = np.linspace(0.05, 2.5, 120)
    out = np.array([DV_over_rd(z) for z in zz])
    c.struct_cleanup(); c.empty()
    return zz, out, rd

model_p = {'use_dcdf':'yes','varying_fundamental_constants':'instantaneous','varying_alpha':1.0,
    'varying_transition_redshift':50.0,'varying_transition_width':0.25,'dcdf_deltam_mode':1,
    'dcdf_z_rad_onset':3.5619e7,'dcdf_rho_inf':0.701221,'varying_me':1.012543,
    'omega_b':0.022757,'H0':69.613,'Omega0_dcdf':1.0-0.022757/0.69613**2,
    'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.0654,'T_ncdm':0.71611}
lcdm_p = {'omega_b':0.022377,'omega_cdm':0.12010,'H0':67.36,
    'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.06,'T_ncdm':0.71611}

print("computing model and LCDM BAO distances (background only)...")
zm, dvm, rdm = distances(model_p)
zl, dvl, rdl = distances(lcdm_p)
print(f"  r_drag: model {rdm:.2f} Mpc, LCDM {rdl:.2f} Mpc")

# measured D_V/r_d (label, z, value, sigma)
bao = [
    ("6dFGS",       0.106, 3.047, 0.137),
    ("SDSS MGS",    0.15,  4.514, 0.140),
    ("BOSS DR12",   0.38,  9.99,  0.12),
    ("BOSS DR12",   0.51,  12.72, 0.13),
    ("BOSS DR12",   0.61,  14.94, 0.17),
    ("eBOSS QSO",   1.48,  26.07, 0.42),
]

fig, (ax, axr) = plt.subplots(2, 1, figsize=(8, 6.6), sharex=True,
                              gridspec_kw={"height_ratios":[3,1]})
ax.plot(zm, dvm, color="#c0392b", lw=2, label=f"PRTOE (r_d={rdm:.1f} Mpc)")
ax.plot(zl, dvl, color="#2c3e50", lw=1.3, ls="--", label=f"ΛCDM (r_d={rdl:.1f} Mpc)")
seen=set()
for lab, z, v, s in bao:
    ax.errorbar(z, v, yerr=s, fmt='o', ms=6, color="#27ae60", capsize=3, zorder=5,
                label=("BAO surveys" if "BAO surveys" not in seen else None))
    seen.add("BAO surveys")
ax.set_ylabel(r"$D_V/r_d$"); ax.legend(frameon=False, fontsize=9)
ax.set_title("BAO standard-ruler distance — model vs galaxy surveys"); ax.grid(alpha=0.2)

# residual of the data vs the model curve, in sigma
for lab, z, v, s in bao:
    axr.errorbar(z, (v-np.interp(z,zm,dvm))/s, yerr=1, fmt='o', ms=5, color="#27ae60", capsize=2)
axr.axhline(0, color="#c0392b", lw=1); axr.axhspan(-1,1,color="grey",alpha=0.15)
axr.set_ylabel("(data−model)/σ"); axr.set_xlabel("redshift z"); axr.set_ylim(-3,3); axr.grid(alpha=0.2)
fig.tight_layout(); fig.savefig("chains/bao_scale.png", dpi=130)
print("saved chains/bao_scale.png")
chi2 = sum(((v-np.interp(z,zm,dvm))/s)**2 for _,z,v,s in bao)
print(f"  BAO chi2 (data vs model curve, {len(bao)} points) = {chi2:.1f}")
