#!/usr/bin/env python3
"""Entry-84 follow-up: does the mass-step candidacy survive the fourth fence?

The fourth fence forces the gate to swing at void/supercluster boundaries — a
WEB-SCALE field. Consequences for the SN channel:
  (i)  the ejecta-screening trap dissolves (the medium's state is set on web scales,
       not by local baryon density — otherwise every photosphere is screened and the
       channel was stillborn);
  (ii) the predicted offset tracks the host's WEB environment (void-side vs wall/node),
       NOT host mass directly;
  (iii) the observed HOST-MASS step must then be the environment step diluted through
       the mass-environment correlation:
           step_pred(mass) = offset_full * [f_void(low-mass hosts) - f_void(high-mass hosts)]
       where f_void = the SN-weighted fraction of hosts on the unscreened (void) side.

RAMP DISCIPLINE: all inputs scanned as bands (offset_full from the sign-session's
color-channel class; f_void from the galaxy-environment literature ranges); output =
the predicted-step surface vs the observed 0.05-0.08 mag band; no point verdicts.
"""
import numpy as np

obs_lo, obs_hi = 0.05, 0.08          # observed mass step band [mag]

off_grid   = np.linspace(0.05, 0.12, 8)     # full unscreened offset [mag] (ς-session class)
f_lo_grid  = np.linspace(0.10, 0.50, 9)     # void-side fraction, LOW-mass hosts
f_hi_grid  = np.linspace(0.01, 0.15, 8)     # void-side fraction, HIGH-mass hosts

print("predicted step [mag] = offset_full * (f_void_low - f_void_high)")
print(f"observed band: [{obs_lo}, {obs_hi}] mag\n")
print(f"{'offset':>7} | " + " ".join(f"fL={f:4.2f}" for f in f_lo_grid))
hits = 0; total = 0
best = []
for off in off_grid:
    row = []
    for fL in f_lo_grid:
        # marginalize the high-mass fraction over its band (mean of the surface slice)
        steps = off * (fL - f_hi_grid)
        m = steps.mean()
        row.append(m)
        inband = ((steps >= obs_lo) & (steps <= obs_hi)).mean()
        hits += (steps >= obs_lo).sum(); total += steps.size
        if inband > 0:
            best.append((off, fL, inband))
    print(f"{off:7.3f} | " + " ".join(f"{v:7.4f}" for v in row))

frac_reach = hits / total
print(f"\nfraction of the scanned band reaching the observed floor (0.05): {frac_reach:.2f}")
if best:
    print("corners touching the observed band (offset, f_void_low, in-band frac):")
    for off, fL, ib in best[:8]:
        print(f"  offset={off:.3f}  f_void_low={fL:.2f}  in-band={ib:.2f}")
    o_min = min(b[0] for b in best); fL_min = min(b[1] for b in best)
    print(f"  -> the candidacy needs offset >= {o_min:.3f} mag AND f_void_low >= {fL_min:.2f}")
print("""
DISCRIMINATORS THE TRANSFORMATION SHARPENS (named, falsifiable):
 1. At FIXED host mass, standardization residuals must correlate with web
    environment (void-centric distance / local large-scale density).
 2. Controlling for environment must SHRINK the mass step (the mass step is
    the shadow, environment the caster).
 3. Cluster SNe (all screened) must show NO internal mass step.
""")
