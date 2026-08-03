#!/usr/bin/env python3
"""#188 — plot the model's CMB TT spectrum vs LCDM (reads the saved .dat files)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

m = np.loadtxt("chains/cmb_model_baseline.dat")      # ell D_TT D_TE D_EE
l  = np.loadtxt("chains/cmb_lcdm_reference.dat")     # ell D_TT
ell, Dtt = m[:,0], m[:,1]
elll, Dl = l[:,0], l[:,1]
Dl_i = np.interp(ell, elll, Dl)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True,
                               gridspec_kw={"height_ratios": [3, 1]})
ax1.plot(ell, Dtt, lw=1.8, color="#c0392b", label="PRTOE (dcdf dark sector, varying-mₑ)")
ax1.plot(ell, Dl_i, lw=1.2, color="#2c3e50", ls="--", label="ΛCDM (Planck 2018)")
ax1.set_ylabel(r"$D_\ell^{TT}=\ell(\ell+1)C_\ell/2\pi\ \ [\mu K^2]$")
ax1.set_title("PRTOE vs ΛCDM — CMB temperature power spectrum (fiducial derived stack)")
ax1.legend(frameon=False); ax1.set_xlim(2, 2500); ax1.set_ylim(0, 6500)
for lp in (221, 537, 814, 1128):
    ax1.axvline(lp, color="grey", lw=0.5, alpha=0.4)

frac = (Dtt - Dl_i)/Dl_i * 100
ax2.plot(ell, frac, lw=1.0, color="#c0392b")
ax2.axhline(0, color="#2c3e50", lw=0.8, ls="--")
ax2.fill_between(ell, -1, 1, color="grey", alpha=0.15, label="±1%")
ax2.set_ylabel("(model−ΛCDM)/ΛCDM [%]"); ax2.set_xlabel(r"multipole $\ell$")
ax2.set_ylim(-5, 5); ax2.legend(frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig("chains/cmb_baseline.png", dpi=130)
print("saved chains/cmb_baseline.png")
print(f"first-peak: model {np.interp(220,ell,Dtt):.0f} vs LCDM {np.interp(220,ell,Dl_i):.0f} muK^2")
