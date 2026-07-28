"""The indirect band's provenance, recovered from git history -- and why it cannot grade anything.

An earlier sweep of the working tree found the band [0.0205, 0.0214] only as prose and concluded
its derivation was absent. The sweep was incomplete: it did not search the history. It is there.

Commit a48b2a1e, 2026-07-11 20:25, registering P-2026-040:

    "Registered while the zon chain's center is still watch-only and the indirect band
     [0.0205, 0.0214] sits 2.3% BELOW the claim -- this is a bet against a running
     instrument, not a fit."
    "(i) zon-converged alpha_c more than 2 sigma from 0.02189 (the chain is at 2.6% width
     and tightening -- the verdict is weeks away at most)"

So the band is a posterior interval from `cmp_prtoe_zon`, read at registration time. The
question is what state that chain was in when it was read.

Run: python3 scripts/alpha_c_band_provenance_found.py
"""
import math

BAND_LO, BAND_HI = 0.0205, 0.0214
R_AT_READ = 93.100635        # cmp_prtoe_zon.progress, 2026-07-11T20:03:29 -- the row before registration
R_NEXT = 40.362246           # 2026-07-12T01:10:29, the last row that chain ever wrote
R_DISP_BEST = 11.869753      # cmp_prtoe_zon_disp's best, 2026-07-22
R_STOP = 0.05                # the chains' own Rminus1_stop

print("=" * 76)
print("WHAT THE CHAIN WAS DOING WHEN THE BAND WAS READ")
print("=" * 76)
print("  band registered      2026-07-11 20:25  (commit a48b2a1e)")
print(f"  zon progress row     2026-07-11 20:03  R-1 = {R_AT_READ:.2f}")
print(f"  the chains' target                     R-1 = {R_STOP}")
print(f"  ratio                                  {R_AT_READ/R_STOP:.0f}x")
print()
print(f"  the next and final row that chain wrote, 2026-07-12 01:10: R-1 = {R_NEXT:.2f}")
print(f"  its successor cmp_prtoe_zon_disp reached R-1 = {R_DISP_BEST:.2f} at best, then stopped")
print("  and was archived as collapsed. Neither is running.")
print()
print("  A posterior interval read at R-1 = 93 is not a measurement of anything. It is the")
print("  spread of a chain that has not found the distribution yet, and such a spread is")
print("  typically far too NARROW rather than too wide, since the chain has not yet explored.")

print()
print("=" * 76)
print("WHAT THE BAND WAS TAKEN TO SHOW, AND WHAT SURVIVES")
print("=" * 76)
ALPHA = 1/137.035999084
AC3 = 3*ALPHA
print(f"  the registry's reading: the band sits {(1 - BAND_HI/AC3)*100:.1f}% below 3.alpha, so P-2026-040")
print("  is a bet against a running instrument rather than a fit. That framing is sound --")
print("  registering against an unconverged chain is legitimate PRE-REGISTRATION.")
print()
print("  What is not sound is using the same band as a CONSTRAINT, which later work did:")
print("    - 'd = 3 is excluded at every scale' rested on the band's top being below 3.alpha;")
print("    - the three-way conflict on d counted the band as one of its three constraints.")
print("  Both inherit R-1 = 93 and neither survives it.")

print()
print("=" * 76)
print("THE d PICTURE WITH THE BAND WITHDRAWN")
print("=" * 76)
T_C = 0.5*math.log(2)*0.51099895e6
M_2 = ALPHA**2 * T_C
rho = lambda d: (d*d/2)*ALPHA**4*T_C
d_rho = 3.0*math.sqrt(2.25e-3/rho(3.0))
d_anchor = 0.021316*137.035999084
print(f"  {'constraint':<40} {'d':>9}")
print("  " + "-" * 52)
print(f"  {'the spatial dimension (theory)':<40} {3.0:9.4f}")
print(f"  {'the observed dark-energy density':<40} {d_rho:9.4f}")
print(f"  {'the hierarchy anchor exact landing':<40} {d_anchor:9.4f}")
print(f"  {'the indirect band':<40} {'WITHDRAWN':>9}")
print()
print(f"  Theory and observation agree to {abs(d_rho/3.0 - 1)*100:.2f}% -- which is the floor's recorded")
print(f"  +0.44%, since rho goes as d^2. The anchor sits {(1 - d_anchor/3.0)*100:.2f}% below both.")
print()
print("  So there is no three-way conflict. There is the single exposure section 6f already")
print("  named: the anchor's exact landing wants a coupling weaker than the infrared limit,")
print("  and cannot have it at any scale. Removing the band does not weaken the corpus --")
print("  it removes an apparent second constraint that was never entitled to the name, and")
print("  leaves the picture simpler and better than the three-way reading described.")
