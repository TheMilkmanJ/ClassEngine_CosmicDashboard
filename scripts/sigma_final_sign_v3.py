#!/usr/bin/env python3
"""sigma-final v3 — FEATURE-RESOLVED (the appeal, one notch below real templates):
the peak SN Ia spectrum built as continuum x blanketing + the NAMED absorption
features (Ca II H&K, Si II 4130, Fe blends, S II 5450, Si II 5750, Si II 6150)
at literature-typical depths/widths. The Rydberg compression moves ONLY the
features (lines); continuum fixed. Bessell-approximate B/V. Scan retained."""
import numpy as np
lam = np.linspace(2800, 8000, 6000)
FEATURES = [  # (center A, depth, width A) — peak-epoch SN Ia, literature-typical
    (3750, 0.45, 120), (4130, 0.30, 90), (4900, 0.35, 220),
    (5450, 0.20, 90),  (5750, 0.22, 80), (6150, 0.45, 140)]
def sed(T, edge, wB, compress):
    x = 1.4388e8/(lam*T)
    bb = 1.0/(lam**5*np.expm1(np.clip(x,1e-9,500)))
    blank = 1.0/(1.0+np.exp(-(lam*(1+compress)-edge)/wB))   # line-forest edge: compresses
    f = bb*blank
    for c0, d, w in FEATURES:
        c = c0/(1+compress)     # features emitted BLUER by eps
        f = f*(1.0 - d*np.exp(-0.5*((lam-c)/w)**2))
    return f
def bessell(center, width, edgew=150):
    lo, hi = center-width/2, center+width/2
    return 1/(1+np.exp(-(lam-lo)/edgew))*1/(1+np.exp((lam-hi)/edgew))
B, V = bessell(4400, 980), bessell(5500, 890)
eps = 0.0124
res = []
for T in [8500., 10000., 11500.]:
  for edge in [3100., 3400.]:
    for beta in [2.7, 3.1, 3.5]:
      def mags(cl):
          f = sed(T, edge, 250., cl)
          return (-2.5*np.log10(np.trapezoid(f*B*lam,lam)),
                  -2.5*np.log10(np.trapezoid(f*V*lam,lam)))
      b0,v0 = mags(0.0); b1,v1 = mags(eps)
      dmu = (b1-b0) - beta*((b1-v1)-(b0-v0))
      res.append(dmu)
res = np.array(res)
print(f"feature-resolved scan ({len(res)} configs): dmu in [{res.min():+.4f}, {res.max():+.4f}], median {np.median(res):+.4f}")
print(f"fraction dmu > 0 (sigma = -1 sense): {np.mean(res>0)*100:.0f}%")
print("VERDICT:", "sigma-final = -1 CONFIRMED at feature-resolved grade" if np.mean(res>0)>0.9
      else ("sigma-final = +1 at this grade" if np.mean(res>0)<0.1 else "NOT ROBUST — stays armed-off"))
