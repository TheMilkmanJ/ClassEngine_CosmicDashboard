"""Two unrelated sectors constrain alpha_c. Do they agree, and does d = 3 survive them?

The corpus identifies the condensate coupling as alpha_c = 3 alpha = d.alpha with d = 3, giving
0.021892 at the infrared alpha. Two independent constraints bear on that value and have never
been compared:

  * the hierarchy anchor. Solving for the coupling that lands M exactly on 4 pi m_H gives
    alpha_c = 0.021316 (hierarchy 6g).
  * the epsilon-assembly's indirect band, from the background fit, registered independently at
    [0.0205, 0.0214] (quantum_trio, prediction registry).

The registry already records that the band "sits 2.3% below the claim". What it does not record
is where the anchor's value falls relative to the band -- or that the band excludes d = 3 at
EVERY scale, not merely at the recorded one, because alpha only strengthens toward the
ultraviolet and so 3.alpha(mu) never comes back down into the band.

Run: python3 scripts/alpha_c_band_convergence.py
"""
import math

ALPHA_0_INV = 137.035999084
D_RECORDED = 3.0
AC_RECORDED = D_RECORDED / ALPHA_0_INV
AC_ANCHOR = 0.021316                 # lands the anchor exactly on 4 pi m_H
BAND_LO, BAND_HI = 0.0205, 0.0214    # the epsilon-assembly's indirect band

print("=" * 76)
print("THE THREE VALUES")
print("=" * 76)
print(f"  alpha_c recorded  = d.alpha(0), d = 3      {AC_RECORDED:.6f}")
print(f"  alpha_c the anchor's exact landing needs   {AC_ANCHOR:.6f}")
print(f"  the indirect band                          [{BAND_LO}, {BAND_HI}]")

print()
print("=" * 76)
print("WHERE EACH FALLS AGAINST THE BAND")
print("=" * 76)
inside = BAND_LO <= AC_ANCHOR <= BAND_HI
pos = (AC_ANCHOR - BAND_LO) / (BAND_HI - BAND_LO)
print(f"  the anchor's value is {'INSIDE' if inside else 'OUTSIDE'} the band,"
      f" at {pos*100:.1f}% of its height")
print(f"  the recorded value is {'INSIDE' if BAND_LO <= AC_RECORDED <= BAND_HI else 'OUTSIDE'}"
      f" the band, {(AC_RECORDED/BAND_HI - 1)*100:.2f}% above its top"
      f"   (registry records 2.3%)")
print()
print(f"  so the two constraints agree with each other and disagree with d.alpha(0) in the")
print(f"  same direction: the anchor wants alpha_c {(1-AC_ANCHOR/AC_RECORDED)*100:.2f}% below the recorded value,")
print(f"  and the band's top is {(1-BAND_HI/AC_RECORDED)*100:.2f}% below it.")

print()
print("=" * 76)
print("THE BAND EXCLUDES d = 3 AT EVERY SCALE, NOT JUST AT alpha(0)")
print("=" * 76)
print("  alpha strengthens toward the ultraviolet, so alpha(mu) >= alpha(0) for all mu, and")
print("  3.alpha(mu) >= 3.alpha(0) with equality only in the infrared limit. The smallest")
print("  value the identification can ever take is therefore the one it already takes:")
print()
print(f"    min over mu of 3.alpha(mu) = 3.alpha(0) = {AC_RECORDED:.6f}")
print(f"    band top                                = {BAND_HI:.6f}")
print(f"    the minimum exceeds the band top by       {(AC_RECORDED/BAND_HI - 1)*100:.2f}%")
print()
print("  No choice of scale brings 3.alpha inside the band. The exclusion is of the")
print("  IDENTIFICATION, not of a particular evaluation of it -- which is the same shape as")
print("  the anchor's own bound, where 1/alpha = 140.74 lies past the infrared cap 137.036.")

print()
print("=" * 76)
print("WHAT d THE BAND PERMITS")
print("=" * 76)
d_lo, d_hi = BAND_LO * ALPHA_0_INV, BAND_HI * ALPHA_0_INV
d_anchor = AC_ANCHOR * ALPHA_0_INV
print(f"  writing alpha_c = d.alpha(0), the band maps to   d in [{d_lo:.4f}, {d_hi:.4f}]")
print(f"  the anchor's exact landing corresponds to        d  = {d_anchor:.4f}")
print(f"  the recorded value                               d  = {D_RECORDED:.4f}   EXCLUDED")
print()
print(f"  d = 3 misses the permitted interval by {(D_RECORDED/d_hi - 1)*100:.2f}%. Nothing simple sits inside")
print(f"  it: the interval's centre is {0.5*(d_lo+d_hi):.4f}, with e = {math.e:.4f} below it and 3 above.")

print()
print("=" * 76)
print("READING")
print("=" * 76)
print("  This does not touch alpha_c's VALUE, which both constraints put near 0.0213 -- within")
print("  2.6% of the recorded number and comfortably inside the band. What it bears on is the")
print("  IDENTIFICATION alpha_c = 3.alpha, which is section 6f's horn (a): the coupling being")
print("  genuinely electromagnetic. Two independent constraints now push the same way and")
print("  neither can be satisfied by choosing a different scale for alpha.")
print()
print("  Horn (b) -- alpha_c a medium constant that merely sits near 3.alpha(0) -- absorbs both")
print("  without strain, since a medium constant is free to be 0.0213. The convergence is")
print("  therefore evidence on the fork, and it points at (b).")
