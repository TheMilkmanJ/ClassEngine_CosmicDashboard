#!/usr/bin/env python3
"""Savage-Dickey Bayes factor for the dyad vs nested LCDM (varying_me = 1).

B(dyad/LCDM) = pi(m_e=1) / p(m_e=1 | data), valid because LCDM is nested
in the dyad at varying_me = 1 (fluid background LCDM-identical by proof).

Run on a CONVERGED chain only (R-1 < 0.05). Reports both a weighted-KDE
and a Gaussian-approx density at the nested point, plus prior-sensitivity.
"""
import sys
import numpy as np

chain = sys.argv[1] if len(sys.argv) > 1 else "chains/dyad_mnu_mcmc.1.txt"
PRIOR_LO, PRIOR_HI = 0.98, 1.04
hdr = open(chain).readline().lstrip("#").split()
d = np.loadtxt(chain)
cut = d[int(0.3 * len(d)):]
w, me = cut[:, 0], cut[:, hdr.index("varying_me")]

mu = np.average(me, weights=w)
sig = np.sqrt(np.average((me - mu) ** 2, weights=w))
gauss = np.exp(-0.5 * ((1.0 - mu) / sig) ** 2) / (sig * np.sqrt(2 * np.pi))

# weighted KDE (Silverman bandwidth) at the nested point
n_eff = w.sum() ** 2 / (w ** 2).sum()
bw = 1.06 * sig * n_eff ** (-0.2)
kde = np.sum(w * np.exp(-0.5 * ((1.0 - me) / bw) ** 2)) / (w.sum() * bw * np.sqrt(2 * np.pi))

prior = 1.0 / (PRIOR_HI - PRIOR_LO)
print(f"chain: {chain}  rows={len(d)}  n_eff={n_eff:.0f}")
print(f"varying_me = {mu:.5f} +/- {sig:.5f}  ({abs(mu-1)/sig:.2f} sigma from nested point)")
for name, dens in [("gaussian", gauss), ("weighted-KDE", kde)]:
    B = prior / dens
    print(f"[{name:12s}] p(1|D)={dens:.4g}  B(dyad/LCDM)={B:.2f}  lnB={np.log(B):+.2f}")
print(f"prior-sensitivity: B scales linearly with prior width ({PRIOR_HI-PRIOR_LO}); "
      f"halve the prior -> lnB {np.log(prior/2/kde)+np.log(2):+.2f} -> {np.log(prior/kde)-np.log(2):+.2f}")
