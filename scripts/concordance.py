#!/usr/bin/env python3
"""THE CONCORDANCE TABLE (first pass): joint solve across the model's shared
families — multiple determinations of one quantity -> weighted center + strain.
Legal by construction (the CODATA move: no freedom added; scatter becomes a test).
Uncertainties are honest current grades (estimate-level where flagged [E])."""
import numpy as np

FAMILIES = {
  "k (the settlement coupling)": [
      ("sweep-19 grid",        1.360,   0.010 ),   # [E] grid granularity
      ("closed form",          1.36461, 0.004 ),   # [E] convention residue ~0.3%
      ("from measured A_s",    1.3602,  0.0064),   # Planck A_s 1.4% -> /3
  ],
  "f_bar (the winding average)": [
      ("fit-implied eps/(c a)",0.6253,  0.008 ),   # [E] eps posterior width
      ("simulation",           0.635,   0.026 ),
      ("2/pi claim",           0.63662, 0.0    ),  # exact IF true; test, not datum
  ],
  "eps (the dyad, %)": [
      ("production fit",       1.232,   0.010 ),   # [E]
      ("derived stack 27a/5pi",1.2543,  0.013 ),   # [E] ~1% from c,f_bar spreads
  ],
  "n_s (the tilt)": [
      ("formula @ T_on",       0.9641,  0.0012),   # [E] bath-band smear
      ("formula @ T_lock",     0.9661,  0.0012),   # [E]
      ("Planck",               0.9649,  0.0042),
  ],
  "omega_0 (km/s/Mpc)": [
      ("P-028 input, decayed", 0.67,    0.13  ),   # [E] the 0.5 input's ~20%
      ("kinematic line (eps=1)",0.77,   0.08  ),   # [E] pre-spin-up ceiling
  ],
}

print(f"{'family':32s} {'joint':>9s} {'+/-':>7s} {'strain(sig)':>11s}  verdict")
for name, dets in FAMILIES.items():
    vals = np.array([v for _,v,e in dets])
    errs = np.array([max(e,1e-9) for _,v,e in dets])
    w = 1/errs**2
    joint = np.sum(w*vals)/np.sum(w)
    jerr  = 1/np.sqrt(np.sum(w))
    # strain: max pairwise tension in sigma
    strain = 0
    for i in range(len(vals)):
        for j in range(i+1,len(vals)):
            s = abs(vals[i]-vals[j])/np.sqrt(errs[i]**2+errs[j]**2+1e-18)
            strain = max(strain,s)
    verdict = "TIGHT" if strain < 1.5 else ("WATCH" if strain < 3 else "STRAINED")
    print(f"{name:32s} {joint:9.4f} {jerr:7.4f} {strain:11.1f}  {verdict}")
print()
print("Notes: 2/pi entered as exact -> dominates f_bar's joint; remove it and the")
print("joint is 0.626+/-0.008 — the 2/pi test is then 1.3 sigma. The eps family is")
print("the network's largest strain (fit vs stack); zon's alpha_c verdict owns it.")
