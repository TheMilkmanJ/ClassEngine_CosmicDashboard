#!/usr/bin/env python3
"""
Why is the high-l chi^2 high? Diagnose the model-vs-LCDM TT residual SHAPE.
  - if the peaks DRIFT (misalign, growing with l) -> acoustic scale theta_s is off
    -> the peaks are in the wrong place -> FIXABLE by refitting H0 / varying_me.
  - if the peaks sit at the right l but wrong HEIGHT -> amplitude/omega_b/damping.
Also computes 100*theta_s for both from CLASS (the smoking gun: Planck pins it to
1.04109 +/- 0.0003, ~0.03%).
"""
import numpy as np

m = np.loadtxt("chains/cmb_model_baseline.dat"); ell, Dm = m[:,0], m[:,1]
l = np.loadtxt("chains/cmb_lcdm_reference.dat");  Dl = np.interp(ell, l[:,0], l[:,1])

def peaks(x, y, lo=180):
    out = []
    mm = x >= lo
    xx, yy = x[mm], y[mm]
    for i in range(2, len(yy)-2):
        if yy[i] >= yy[i-1] and yy[i] >= yy[i+1] and yy[i] > yy[i-2] and yy[i] > yy[i+2]:
            out.append(int(xx[i]))
    # dedupe nearby
    ded = []
    for p in out:
        if not ded or p - ded[-1] > 60:
            ded.append(p)
    return ded

pm, pl = peaks(ell, Dm), peaks(ell, Dl)
print("="*66)
print("PEAK POSITIONS — model vs LCDM (does the acoustic scale drift?)")
print("="*66)
print(f"  {'peak':4s} {'model l':>8s} {'LCDM l':>8s} {'drift dl':>9s} {'dl/l %':>8s}")
n = min(len(pm), len(pl))
drifts = []
for i in range(n):
    dl = pm[i] - pl[i]
    drifts.append(dl/pl[i])
    print(f"  {i+1:4d} {pm[i]:8d} {pl[i]:8d} {dl:+9d} {dl/pl[i]*100:+8.2f}")
print(f"\n  mean fractional drift dl/l = {np.mean(drifts)*100:+.2f}%")
if abs(np.mean(drifts)) > 0.05/100 and np.std(drifts) < abs(np.mean(drifts)):
    print("  -> peaks drift by a ~CONSTANT FRACTION: this is an ACOUSTIC-SCALE (theta_s)")
    print("     mismatch. The peaks are in the wrong PLACE, not the wrong height.")
    print("     theta_s ~ shifts all peaks by l -> n*pi/theta_s, so a fixed % drift")
    print("     = a fixed % theta_s error. That is FIXABLE by moving H0 (or the")
    print("     recombination via varying_me) to restore theta_s.")

# --- residual shape: oscillating (misalignment) vs smooth (amplitude/tilt) -----
res = (Dm - Dl)/Dl
band = (ell >= 200) & (ell <= 2000)
# a peak-misalignment residual oscillates and correlates with the SLOPE of D_l
slope = np.gradient(Dl)
corr = np.corrcoef(res[band], slope[band])[0,1]
print("\n" + "="*66)
print("RESIDUAL SHAPE (200 < l < 2000)")
print("="*66)
print(f"  RMS fractional residual = {np.std(res[band])*100:.2f}%")
print(f"  corr(residual, dD/dl)   = {corr:+.2f}")
print("  a large |corr| means the residual tracks the peak SLOPE = a horizontal")
print("  (l) SHIFT of the peaks = theta_s misalignment (fixable), not a vertical")
print("  height error (which would not correlate with the slope).")

# --- theta_s for both, from CLASS (the definitive number) ---------------------
print("\n" + "="*66)
print("100*theta_s from CLASS (Planck pins it to 1.04109, ~0.03%)")
print("="*66)
try:
    from classy import Class
    def theta_s(params, label):
        c = Class(); c.set(params); c.compute()
        d = c.get_current_derived_parameters(['100*theta_s'])
        val = d['100*theta_s']; c.struct_cleanup(); c.empty()
        print(f"  {label:26s} 100*theta_s = {val:.5f}")
        return val
    base = {'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.0654,'T_ncdm':0.71611,'output':''}
    tm = theta_s({**base,'use_dcdf':'yes','varying_fundamental_constants':'instantaneous',
                  'varying_alpha':1.0,'varying_transition_redshift':50.0,
                  'varying_transition_width':0.25,'dcdf_deltam_mode':1,
                  'dcdf_z_rad_onset':3.5619e7,'dcdf_rho_inf':0.701221,'varying_me':1.012543,
                  'omega_b':0.022757,'H0':69.613,
                  'Omega0_dcdf':1.0-0.022757/0.69613**2}, "PRTOE (derived stack)")
    tl = theta_s({'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.06,'T_ncdm':0.71611,'output':'',
                  'omega_b':0.022377,'omega_cdm':0.12010,'H0':67.36}, "LCDM (Planck)")
    print(f"\n  difference: {(tm/tl-1)*100:+.2f}%  (Planck's error on theta_s is ~0.03%)")
    if abs(tm/tl-1) > 0.0005:
        print("  -> theta_s is off by MORE than Planck's precision: this is the high-l")
        print("     killer, and it is a background-parameter fix (H0/varying_me), not a")
        print("     shape failure. Refit those and the high-l chi2 should collapse.")
except Exception as e:
    print("  (CLASS theta_s check skipped:", e, ")")
