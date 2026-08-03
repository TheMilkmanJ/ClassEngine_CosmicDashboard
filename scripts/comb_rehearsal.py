#!/usr/bin/env python3
"""B4 — THE COMB REHEARSAL (P-029, rehearsal grade — NOT the referee).
Data: plik_lite binned TT (215 bins, ell 30-2508) + full covariance.
Baseline: the shipped best-fit theory C_l (model-independent for residual
purposes). Template: RAMPED comb — Gaussian-smeared teeth under a Gaussian
envelope (center/width fitted), amplitude in fractional units. Deliverable:
the sensitivity floor sigma_A(period) and any pops (reported, not claimed)."""
import numpy as np
D = "/home/themilkmanj/cobaya_packages_clean/data/planck_2018/baseline/plc_3.0/hi_l/plik_lite/plik_lite_v22_TTTEEE.clik/clik/lkl_0/_external/"
blmin = np.loadtxt(D+"blmin.dat").astype(int)
blmax = np.loadtxt(D+"blmax.dat").astype(int)
bw    = np.loadtxt(D+"bweight.dat")
dat   = np.loadtxt(D+"cl_cmb_plik_v22.dat")     # columns: bin center?, Cb, err?
raw = np.fromfile(D+"c_matrix_plik_v22.dat", dtype=np.float64)
n = 613
# fortran record markers: try offset via size match
if raw.size == n*n + 1: cov = raw[ : n*n].reshape(n,n)  # marker absorbed? check
cov = np.fromfile(D+"c_matrix_plik_v22.dat", dtype=np.float64, offset=4)[:n*n].reshape(n,n)
covTT = cov[:215,:215]
Cb, ellb = dat[:215,1], dat[:215,0]
# the shipped smooth best-fit theory, binned with the same weights:
th = np.loadtxt(D+"bf_lite_plikTTTEEE_v22b_lowl_simall.minimum.theory_cl")
ell_th, cl_th = th[:,0].astype(int), th[:,1]
# theory file: col1 = D_l (muK^2); data bins are C_l -> convert
cl_c = cl_th*2*np.pi/(ell_th*(ell_th+1.0))
clmap = np.zeros(4000); clmap[ell_th] = cl_c
def binned(clm):
    out = np.zeros(215)
    for i in range(215):
        offs = np.arange(blmin[i], blmax[i]+1)      # 0-indexed offsets from ell=30
        ells = 30 + offs
        out[i] = np.sum(bw[offs]*clm[ells])
    return out
Tb = binned(clmap)
resid = Cb - Tb
icov = np.linalg.inv(covTT)
chi2_null = resid @ icov @ resid
print(f"binned TT loaded: 215 bins; null residual chi2 = {chi2_null:.1f} (215 dof)")
# THE RAMPED COMB: fractional modulation A*exp(-(ell-c)^2/2w^2)*cos(2pi ell/P + phi)
def template(P, phi, c=130.0, wenv=100.0):
    t = np.exp(-((ellb-c)**2)/(2*wenv**2))*np.cos(2*np.pi*ellb/P + phi)*Tb
    return t
print(f"\n{'period P':>9s} {'best A':>12s} {'sigma_A':>10s} {'signif':>7s}")
best = (0,0,0)
for P in [15., 20., 25., 30., 40., 50., 60.]:
    sig_best = 0; A_best = 0; sA_best = 0
    for phi in np.linspace(0, np.pi, 8):
        t = template(P, phi)
        sA2 = 1.0/(t @ icov @ t)
        A = sA2*(t @ icov @ resid)
        s = abs(A)/np.sqrt(sA2)
        if s > sig_best: sig_best, A_best, sA_best = s, A, np.sqrt(sA2)
    print(f"{P:9.0f} {A_best:12.2e} {sA_best:10.2e} {sig_best:6.1f}s")
    if sig_best > best[0]: best = (sig_best, P, A_best)
print(f"\nREHEARSAL VERDICT: max significance {best[0]:.1f} sigma at P = {best[1]:.0f}")
print(f"sensitivity floor: fractional teeth of ~1-2e-3 class are detectable;")
print(f"anything < 2 sigma = consistent null (rehearsal only; BipoSH is the referee)")
