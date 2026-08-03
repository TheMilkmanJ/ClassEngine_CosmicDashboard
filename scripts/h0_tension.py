#!/usr/bin/env python3
"""
The H0 tension figure: where the model sits in the early-vs-late H0 landscape.
A forest plot of the determinations, with the model's varying-me value shown
bridging the CMB (early) and distance-ladder (late) camps. No CLASS, no chain --
literature determinations plus the model's derived-stack H0.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (label, H0, sigma, kind)  kind: 'early' (CMB/sound-horizon), 'late' (ladder), 'model'
rows = [
    ("Planck 2018 (CMB, ΛCDM)",          67.36, 0.54, "early"),
    ("ACT+WMAP (CMB)",                    67.6,  1.1,  "early"),
    ("BBN + BAO (early, no CMB)",         67.4,  1.1,  "early"),
    ("TRGB (CCHP, Freedman+21)",          69.8,  1.7,  "late"),
    ("SH0ES Cepheid (Riess+22)",          73.04, 1.04, "late"),
    ("Lensing time delays (TDCOSMO)",     73.3,  1.8,  "late"),
    ("PRTOE (varying-mₑ)",                69.61, 0.6,  "model"),
]
col = {"early": "#2c3e50", "late": "#c0392b", "model": "#27ae60"}

fig, ax = plt.subplots(figsize=(8.4, 5.2))
# Planck and SH0ES reference bands
ax.axvspan(67.36-0.54, 67.36+0.54, color="#2c3e50", alpha=0.10, zorder=0)
ax.axvspan(73.04-1.04, 73.04+1.04, color="#c0392b", alpha=0.10, zorder=0)

y = np.arange(len(rows))[::-1]
for yi, (lab, h0, s, kind) in zip(y, rows):
    ax.errorbar(h0, yi, xerr=s, fmt='o', ms=9 if kind=="model" else 7,
                color=col[kind], capsize=4, lw=2, zorder=3,
                markeredgecolor='k' if kind=="model" else col[kind],
                markeredgewidth=1.5 if kind=="model" else 0)
    ax.text(h0, yi+0.28, f"{h0:.2f}", ha='center', va='bottom', fontsize=8.5, color=col[kind])

ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows], fontsize=10)
ax.set_xlabel(r"$H_0\ \ [\mathrm{km\,s^{-1}\,Mpc^{-1}}]$", fontsize=11)
ax.set_title("The H₀ landscape — varying-mₑ closes 40% of the early–late gap", fontsize=12)
ax.set_xlim(65.5, 76); ax.grid(axis='x', alpha=0.25)
# camp labels
ax.text(67.36, len(rows)-0.4, "early (sound horizon)", color="#2c3e50",
        ha='center', fontsize=9, style='italic')
ax.text(73.04, len(rows)-0.4, "late (distance ladder)", color="#c0392b",
        ha='center', fontsize=9, style='italic')
fig.tight_layout()
fig.savefig("chains/h0_tension.png", dpi=130)
print("saved chains/h0_tension.png")

# the honest number: how far the model closes the gap
planck, shoes, model = 67.36, 73.04, 69.61
frac = (model - planck)/(shoes - planck)*100
print(f"  Planck {planck}, SH0ES {shoes}, PRTOE {model}")
print(f"  the model moves the CMB value UP by {model-planck:.2f} km/s/Mpc via varying-me,")
print(f"  closing {frac:.0f}% of the {shoes-planck:.1f} km/s/Mpc early-late gap.")
print(f"  tension vs SH0ES: {(shoes-model)/np.hypot(1.04,0.6):.1f} sigma (was "
      f"{(shoes-planck)/np.hypot(1.04,0.54):.1f} sigma Planck-vs-SH0ES).")
