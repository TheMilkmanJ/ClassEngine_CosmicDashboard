#!/usr/bin/env python3
"""
BBN money-plot: the model's primordial helium Y_p and deuterium D/H vs the baryon
density, against the measured values. At BBN the condensate is not yet formed, so
m_e = 1 (the deuterium heal by varying-m_e is excluded at 12 sigma, data-required)
-- the model's BBN is therefore standard BBN, and the figure shows it does not
break the light-element abundances. The relations are the ones the model's config
carries (the BBN prior in cmp_prtoe_fixed.yaml). No CLASS, no chain.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def Yp(ob):   return 0.2471 + 0.0096*np.log(ob/0.02236)           # m_e = 1 at BBN
def DH(ob):   return 2.53e-5*np.exp(-1.6*np.log(ob/0.02236))       # m_e = 1 at BBN

Yp_obs, Yp_err = 0.2449, 0.0040        # Aver+ 2015
DH_obs, DH_err = 2.527e-5, 0.030e-5    # Cooke+ 2018
ob_planck, ob_p_err = 0.02237, 0.00015 # Planck 2018 (= deuterium-optimal)
ob_model = 0.02280                     # the model's CMB-fitted omega_b (theta_s realignment)

ob = np.linspace(0.020, 0.025, 400)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# --- helium ---
a1.plot(ob, Yp(ob), color="#c0392b", lw=2, label="BBN (m_e = 1)")
a1.axhspan(Yp_obs-Yp_err, Yp_obs+Yp_err, color="grey", alpha=0.25, label="measured (Aver+ 15)")
a1.axhline(Yp_obs, color="grey", lw=1)
a1.set_ylabel(r"$Y_p$ (helium mass fraction)")
a1.set_title("BBN light-element abundances — model vs measured")
a1.legend(frameon=False, fontsize=9); a1.grid(alpha=0.2)

# --- deuterium (x1e5) ---
a2.plot(ob, DH(ob)*1e5, color="#2c3e50", lw=2, label="BBN (m_e = 1)")
a2.axhspan((DH_obs-DH_err)*1e5, (DH_obs+DH_err)*1e5, color="grey", alpha=0.25,
           label="measured (Cooke+ 18)")
a2.axhline(DH_obs*1e5, color="grey", lw=1)
a2.set_ylabel(r"$10^5\times$ D/H"); a2.set_xlabel(r"$\omega_b=\Omega_b h^2$")
a2.legend(frameon=False, fontsize=9); a2.grid(alpha=0.2)

for ax in (a1, a2):
    ax.axvspan(ob_planck-ob_p_err, ob_planck+ob_p_err, color="#2980b9", alpha=0.12)
    ax.axvline(ob_planck, color="#2980b9", lw=1, ls=':')
    ax.axvline(ob_model,  color="#27ae60", lw=1.5, ls='--')
a1.text(ob_planck, a1.get_ylim()[1], "Planck ω_b\n(D-optimal)", color="#2980b9", fontsize=8,
        ha='center', va='bottom')
a1.text(ob_model, a1.get_ylim()[1], "model ω_b\n(CMB fit)", color="#27ae60", fontsize=8,
        ha='center', va='bottom')
fig.tight_layout(); fig.savefig("chains/bbn_abundances.png", dpi=130)
print("saved chains/bbn_abundances.png")

# --- the honest numbers: the CMB pulls omega_b up, deuterium pulls it down ------
for lbl, ob0 in [("Planck / D-optimal omega_b", ob_planck), ("model CMB-fit omega_b", ob_model)]:
    sy = (Yp(ob0)-Yp_obs)/Yp_err
    sd = (DH(ob0)-DH_obs)/DH_err
    print(f"  {lbl} = {ob0:.5f}:  Y_p = {Yp(ob0):.4f} ({sy:+.1f} sigma),"
          f"  D/H = {DH(ob0)*1e5:.3f}e-5 ({sd:+.1f} sigma)")
print("  The varying-me theta_s realignment prefers omega_b ~ 0.0228, where D/H is ~ -2.5")
print("  sigma; the BBN prior pulls back toward 0.0224, so the joint fit compromises at a")
print("  mild D/H tension. It is a genuine cost of the H0 mechanism, not a dyad effect --")
print("  the dyad is L-neutral and reaches the deuteron only at two loops (~2e4x too weak).")
print("  Li-7 is a separate sector (the lithium problem: standard BBN over-predicts")
print("  Li-7/H ~5e-10 vs observed ~1.6e-10; the model's Li row handles it apart).")
