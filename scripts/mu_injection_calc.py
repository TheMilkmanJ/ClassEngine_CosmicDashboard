#!/usr/bin/env python3
"""B5 — the mu-distortion calculator (sweep 46/strike-10 machinery, packaged).
mu(z_inject, efficiency): the visibility RAMP (never a wall), the dark-sector
budget ceiling, the branch verdicts. The draw-branch discriminator's tool."""
import numpy as np

Z_DC = 1.98e6   # the blackbody-visibility scale
Z_EQ = 3400.0

def visibility(z):
    return np.exp(-(z/Z_DC)**2.5)

def mu(z_inject, efficiency=1.0):
    """mu from a dark-sector latent-heat injection at z_inject."""
    budget = Z_EQ/z_inject          # the sector's whole share of radiation
    return 1.4*efficiency*budget*visibility(z_inject)

if __name__ == "__main__":
    print(f"{'z_inject':>10s} {'budget':>9s} {'visib.':>9s} {'mu(eff=1)':>10s}  vs FIRAS 9e-5 / PIXIE 1e-8 / PRISM 1e-9")
    for z in [3e5, 6e5, 1.2e6, 2e6, 3e6, 5.6e6, 1e7]:
        b, v, m = Z_EQ/z, visibility(z), mu(z)
        flag = "FIRAS-DEAD" if m > 9e-5 else ("PIXIE-visible" if m > 1e-8 else ("PRISM-visible" if m > 1e-9 else "silent"))
        print(f"{z:10.1e} {b:9.2e} {v:9.2e} {m:10.2e}  {flag}")
    print("\nbranch verdicts (the sweep-46/strike-10 discriminator, now a tool):")
    print(f"  xi-branch  (z=1.2e6): eff must be < {9e-5/mu(1.2e6):.3f} (FIRAS) ; PIXIE sees eff > {1e-8/mu(1.2e6):.1e}")
    print(f"  1/m-branch (z=5.6e6): mu(eff=1) = {mu(5.6e6):.1e} — below PIXIE, PRISM-reachable")
