#!/usr/bin/env python3
"""Entry-85 RAMPED RE-RUN (the author's catch: the host split was a binary).

v1's step: hosts classified void/not-void (g = 1 or 0), dilution = f_lo - f_hi.
v2's ramp: each host population carries a CONTINUOUS distribution of large-scale
(few-Mpc-smoothed) overdensity Delta; the gate g(Delta) = 1/(1 + (Delta/C_ref)^s)
is smooth and fourth-fence-parked (C_ref ~ few or below); the dilution is
    <g>_low-mass - <g>_high-mass
with <g> = the population average of the gate value.

Population model (flagged): ln Delta ~ Normal(mu, sigma);
  low-mass hosts:  median Delta scanned 1.0-2.5 (field/void-leaning)
  high-mass hosts: median Delta scanned 3-10   (wall/node-leaning)
  sigma scanned 0.6-1.2 (environment spread)
Gate: C_ref scanned 0.5-5 (the fourth fence's allowed band), s in [2, 8].

Output: the predicted-step surface vs the observed 0.05-0.08 mag band — as bands.
"""
import numpy as np

rng = np.random.default_rng(7)
N = 40000
obs_lo, obs_hi = 0.05, 0.08

def mean_gate(median, sigma, C_ref, s):
    d = np.exp(rng.normal(np.log(median), sigma, N))
    return (1.0 / (1.0 + (d / C_ref)**s)).mean()

off_band  = np.linspace(0.05, 0.12, 6)
med_lo_b  = [1.0, 1.5, 2.5]
med_hi_b  = [3.0, 5.0, 10.0]
sig_b     = [0.6, 0.9, 1.2]
Cref_b    = [0.5, 1.0, 2.0, 5.0]
s_b       = [2, 4, 8]

steps = []
rows = []
for Cref in Cref_b:
    for s in s_b:
        for sig in sig_b:
            for mlo in med_lo_b:
                for mhi in med_hi_b:
                    glo = mean_gate(mlo, sig, Cref, s)
                    ghi = mean_gate(mhi, sig, Cref, s)
                    dil = glo - ghi
                    for off in off_band:
                        steps.append(off * dil)
                    rows.append((Cref, s, sig, mlo, mhi, glo, ghi, dil))

steps = np.array(steps)
print(f"configurations: {len(rows)}  step evaluations: {steps.size}")
print(f"predicted step: min {steps.min():.4f}  median {np.median(steps):.4f}  "
      f"max {steps.max():.4f} mag")
print(f"fraction reaching the observed floor (>= {obs_lo}): {(steps >= obs_lo).mean():.3f}")
print(f"fraction inside the observed band [{obs_lo}, {obs_hi}]: "
      f"{((steps >= obs_lo) & (steps <= obs_hi)).mean():.3f}")

print("\ndilution <g>_lo - <g>_hi across the gate/population bands:")
dils = np.array([r[7] for r in rows])
print(f"  min {dils.min():.3f}  median {np.median(dils):.3f}  max {dils.max():.3f}")
print(f"  (v1's binary gave 0.09-0.35 over its scanned corner)")

print("\nthe corners that reach the observed band (Cref, s, sigma, med_lo, med_hi, dil):")
count = 0
for (Cref, s, sig, mlo, mhi, glo, ghi, dil) in rows:
    if 0.09 * dil >= obs_lo and count < 10:   # reachable at mid-band offset 0.09
        print(f"  Cref={Cref:4.1f} s={s} sig={sig:.1f} mlo={mlo:.1f} mhi={mhi:4.1f} "
              f"<g>lo={glo:.2f} <g>hi={ghi:.2f} dil={dil:.3f}")
        count += 1
if count == 0:
    print("  NONE at mid-band offset (0.09 mag)")
    # what offset would the best dilution need?
    print(f"  best dilution {dils.max():.3f} needs offset >= {obs_lo/dils.max():.3f} mag")
