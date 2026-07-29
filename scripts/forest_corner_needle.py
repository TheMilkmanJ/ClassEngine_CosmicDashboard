#!/usr/bin/env python3
"""
#28's desk half: can the full-mass-step corner (C_ref ~ 2) thread the forest's needle?

The gate is the survival form  S(D) = exp[-(D^2/C_ref^2)^n],  n > 2.43 forced
(me_mechanism_math sec 26/27), acting on eps_0 = 27a/5pi = 1.2543%.

The Lyman-alpha forest cannot see a UNIFORM offset -- that is degenerate with the
absorber's redshift.  What it sees is the DIFFERENTIAL across its own density
contrast.  The corpus records that a smooth (gentle-exponential) density dependence
gives "absorber differentials 1e4 over bound", which forces binarity.  That statement
back-derives the bound itself, with no external number needed:

    bound = D_smooth(n=1) / 1e4

We then ask where the steep gate's differential sits against that same bound, as a
function of C_ref -- and in particular at the corner C_ref ~ 2 that the full SN mass
step requires.

Pre-stated control: as C_ref -> 0 or C_ref -> infinity the differential must vanish
(gate fully off, or fully on, across the whole forest).  A method that does not
reproduce that is broken.
"""

import math

ALPHA = 1.0 / 137.035999084
EPS0_PCT = 27.0 * ALPHA / (5.0 * math.pi) * 100.0  # 1.2543 %

N_STEEP = 2.43  # forced minimum
N_SMOOTH = 1.0  # the "gentle exponential" that fails

# The forest's own density contrast at z ~ 2-3.  The transmission-weighted Lyman-alpha
# forest is dominated by near-mean gas; this is a deliberately CONSERVATIVE contrast
# (a wider one only strengthens every conclusion below).
D_LO, D_HI = 0.5, 2.0


def S(D, c_ref, n):
    """Survival factor: eps -> eps_0 * S.  S=1 unscreened, S=0 screened."""
    return math.exp(-((D * D) / (c_ref * c_ref)) ** n)


def differential(c_ref, n, d_lo=D_LO, d_hi=D_HI):
    """Predicted forest differential in percent of m_e."""
    return EPS0_PCT * (S(d_lo, c_ref, n) - S(d_hi, c_ref, n))


def main():
    print("=" * 74)
    print("  #28: the full-step corner against the forest's flatness fence")
    print("=" * 74)
    print(f"  eps_0 = 27a/5pi = {EPS0_PCT:.4f}%   forest contrast D = {D_LO} -> {D_HI}")
    print(f"  gate  S(D) = exp[-(D^2/C_ref^2)^n],  n_steep = {N_STEEP} (forced)")
    print()

    # --- pre-stated control: the differential must vanish at both extremes -----
    lo_end = differential(1e-3, N_STEEP)
    hi_end = differential(1e3, N_STEEP)
    print("  CONTROL (stated before looking):")
    print(f"    C_ref -> 0    differential = {lo_end:.3e} %   (gate off everywhere)")
    print(f"    C_ref -> inf  differential = {hi_end:.3e} %   (gate on everywhere)")
    ok = abs(lo_end) < 1e-12 and abs(hi_end) < 1e-12
    print(f"    both vanish: {'PASS' if ok else 'FAIL'}")
    print()

    # --- back-derive the bound from the corpus's own 1e4 statement -------------
    # The smooth gate's WORST differential over C_ref is what "1e4 over bound" refers to.
    best_c, d_smooth_max = None, 0.0
    c = 0.05
    while c < 50.0:
        d = differential(c, N_SMOOTH)
        if d > d_smooth_max:
            d_smooth_max, best_c = d, c
        c *= 1.002
    bound = d_smooth_max / 1e4
    print("  BOUND, back-derived from the corpus's own statement")
    print('  ("a smooth density-dependence gives absorber differentials 1e4 over bound"):')
    print(f"    smooth gate (n=1) peak differential = {d_smooth_max:.4f}%  at C_ref = {best_c:.3f}")
    print(f"    => implied forest bound            = {bound:.3e}%  = {bound*1e4:.3f} x 1e-4 %")
    print()

    # --- the steep gate across C_ref ------------------------------------------
    print("  THE STEEP GATE'S FOREST DIFFERENTIAL vs the same bound:")
    print(f"    {'C_ref':>8} {'S(0.5)':>9} {'S(2.0)':>9} {'differential':>14} {'/bound':>12}")
    for c_ref in (0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 30.0):
        d = differential(c_ref, N_STEEP)
        flag = "   <-- the corner" if abs(c_ref - 2.0) < 1e-9 else ""
        print(f"    {c_ref:8.2f} {S(D_LO,c_ref,N_STEEP):9.5f} {S(D_HI,c_ref,N_STEEP):9.5f}"
              f" {d:13.5f}% {d/bound:11.1f}x{flag}")
    print()

    corner = differential(2.0, N_STEEP)
    print("  VERDICT AT THE CORNER (C_ref = 2):")
    print(f"    predicted forest differential = {corner:.5f}%")
    print(f"    exceeds the back-derived bound by {corner/bound:,.0f}x")
    print()

    # --- what C_ref would actually be needed for flatness? --------------------
    print("  WHERE THE FOREST WOULD ACTUALLY BE FLAT (differential <= bound):")
    lo_ok = hi_ok = None
    c = 1e-3
    while c < 1e3:
        if differential(c, N_STEEP) <= bound:
            if lo_ok is None or c < 1.0:
                lo_ok = c if lo_ok is None else lo_ok
        c *= 1.01
    # scan explicitly for the two allowed wings
    c, wing_lo = 1e-3, None
    while c < 2.0:
        if differential(c, N_STEEP) <= bound:
            wing_lo = c
        c *= 1.005
    c, wing_hi = 1e3, None
    while c > 2.0:
        if differential(c, N_STEEP) <= bound:
            wing_hi = c
        c /= 1.005
    print(f"    screened wing:   C_ref <= {wing_lo:.4f}   (whole forest screened, eps off)")
    print(f"    unscreened wing: C_ref >= {wing_hi:.4f}   (whole forest unscreened, uniform offset)")
    print(f"    the corner C_ref = 2.0 sits BETWEEN these wings -> forest is NOT flat there")
    print()
    print("  Reading: the corner does not thread the needle on these numbers.  It is not")
    print("  killed here either -- the forest contrast used is an assumption, and the SN")
    print("  host large-scale density range is NOT stated anywhere in the corpus, so the")
    print("  needle's other side cannot be checked.  THAT is the desk debt #28 is carrying:")
    print("  the fence is invoked ('the SN host-density range') without its number.")
    print("=" * 74)


if __name__ == "__main__":
    main()
