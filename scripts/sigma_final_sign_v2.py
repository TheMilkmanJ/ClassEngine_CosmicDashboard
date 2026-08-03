#!/usr/bin/env python3
"""SIGN SESSION v2 (ramped): ONLY the line features compress (Rydberg moves
lines; the thermal continuum re-equilibrates — its response is the Arnett
channel, counted separately). Template-space SCAN: the sign must survive the
honesty ranges of T, the blanketing edge/width, beta, and the filter proxies."""
import numpy as np
lam = np.linspace(2500, 9000, 4000)

def sed(T, edge, width, compress_lines):
    x = 1.4388e8/(lam*T)
    bb = 1.0/(lam**5*(np.expm1(np.clip(x, 1e-9, 500))))          # continuum: FIXED
    lam_line = lam*(1.0+compress_lines)                           # lines: compressed
    blanket = 1.0/(1.0 + np.exp(-(lam_line-edge)/width))
    return bb*blanket

def gf(c, w): return np.exp(-0.5*((lam-c)/w)**2)

eps = 0.0124
signs, dmus = [], []
for T in [8000., 10000., 12000.]:
  for edge in [3000., 3300., 3600.]:
    for width in [150., 250., 400.]:
      for beta in [2.5, 3.1, 3.7]:
        for (bc,bw,vc,vw) in [(4400,500,5500,450),(4350,450,5450,500)]:
          B, V = gf(bc,bw), gf(vc,vw)
          def mags(cl):
              f = sed(T, edge, width, cl)
              return (-2.5*np.log10(np.trapezoid(f*B*lam, lam)),
                      -2.5*np.log10(np.trapezoid(f*V*lam, lam)))
          mB0, mV0 = mags(0.0); mB1, mV1 = mags(eps)
          dmu = (mB1-mB0) - beta*((mB1-mV1)-(mB0-mV0))
          dmus.append(dmu); signs.append(np.sign(dmu))
dmus = np.array(dmus)
frac_neg = np.mean(np.array(signs) < 0)
print(f"template-space scan: {len(dmus)} configurations")
print(f"dmu range: [{dmus.min():+.4f}, {dmus.max():+.4f}] mag; median {np.median(dmus):+.4f}")
print(f"fraction with dmu < 0 (the ladder-reads-HIGH sense): {frac_neg*100:.0f}%")
print()
if frac_neg > 0.9:   print("SIGN ROBUST: sigma-final = +1 sense (ladder HIGH) across the scan")
elif frac_neg < 0.1: print("SIGN ROBUST: sigma-final = -1 sense (ladder DOWN) across the scan")
else:                print("SIGN NOT ROBUST at template grade: sigma-final stays 0 (armed-off);")
print("the real SN Ia spectral template + real filter curves = the named next fidelity")
