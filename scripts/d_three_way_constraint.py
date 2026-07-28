"""d carries two jobs. Can one value do both?

The math spine defines d once and uses it twice:

    alpha_c = d.alpha           the condensate coupling, d = 3 "the spatial dimension"
    rho_Lambda^(1/4) = (d^2/2).alpha^4.T_c = (9/2).alpha^4.T_c    the dark-energy floor

and states explicitly that the second d is "the same 3 as in alpha_c = 3 alpha". So d is a
single quantity constrained from two directions, and protocol check 23 applies: the set is
over-determined and its closure has never been tested.

Three constraints now bear on it:
    the epsilon-assembly's indirect band on alpha_c    ->  d in [2.809, 2.933]
    the hierarchy anchor's exact landing on 4 pi m_H   ->  d = 2.921
    the observed dark-energy density, 2.25 meV        ->  d = ?

Run: python3 scripts/d_three_way_constraint.py
"""
import math

ALPHA_INV = 137.035999084
ALPHA = 1 / ALPHA_INV
ME = 0.51099895e6                 # eV
TAU = 0.5 * math.log(2)
T_C = TAU * ME                    # eV
RHO_OBS = 2.25e-3                 # eV, the observed dark-energy scale
BAND_LO, BAND_HI = 0.0205, 0.0214
AC_ANCHOR = 0.021316


def rho_of(d):
    """rho_Lambda^(1/4) in eV for a given d."""
    return (d * d / 2) * ALPHA**4 * T_C


print("=" * 76)
print("THE CHAIN, AT d = 3")
print("=" * 76)
print(f"  tau = ln2/2                {TAU:.7f}")
print(f"  T_c = tau.m_e              {T_C/1e3:.3f} keV")
print(f"  rho_Lambda^(1/4) at d = 3  {rho_of(3.0)*1e3:.4f} meV")
print(f"  observed                   {RHO_OBS*1e3:.4f} meV"
      f"   ->  {(rho_of(3.0)/RHO_OBS - 1)*100:+.2f}%   (recorded +0.44%)")

print()
print("=" * 76)
print("WHAT EACH CONSTRAINT DEMANDS OF d")
print("=" * 76)
d_band_lo, d_band_hi = BAND_LO * ALPHA_INV, BAND_HI * ALPHA_INV
d_anchor = AC_ANCHOR * ALPHA_INV
d_rho = 3.0 * math.sqrt(RHO_OBS / rho_of(3.0))
print(f"  {'constraint':<44} {'d':>10}   {'in band?':>9}")
print("  " + "-" * 68)
rows = (("the indirect band on alpha_c (interval)", None, None),
        ("the hierarchy anchor's exact landing", d_anchor, None),
        ("the observed dark-energy density 2.25 meV", d_rho, None),
        ("the spatial dimension (theory)", 3.0, None))
print(f"  {'the indirect band on alpha_c':<44} [{d_band_lo:.4f}, {d_band_hi:.4f}]")
for name, d, _ in rows[1:]:
    ok = "yes" if d_band_lo <= d <= d_band_hi else "NO"
    print(f"  {name:<44} {d:10.4f}   {ok:>9}")

print()
print("=" * 76)
print("SO THE SET DOES NOT CLOSE")
print("=" * 76)
print(f"  band top                                   {d_band_hi:.4f}")
print(f"  d the observed dark energy requires        {d_rho:.4f}"
      f"   -> {(d_rho/d_band_hi - 1)*100:+.2f}% above the band")
print(f"  d the theory supplies (spatial dimension)  {3.0:.4f}"
      f"   -> {(3.0/d_band_hi - 1)*100:+.2f}% above the band")
print(f"  d the hierarchy anchor wants               {d_anchor:.4f}"
      f"   -> inside, at {(d_anchor-d_band_lo)/(d_band_hi-d_band_lo)*100:.0f}% of its height")
print()
print("  The band agrees with the hierarchy anchor and disagrees with BOTH the geometric")
print("  d = 3 and the d the observed dark-energy density requires — and those two agree with")
print(f"  each other to {abs(d_rho/3.0 - 1)*100:.2f}%, which is what the floor's +0.44% landing means.")

print()
print("=" * 76)
print("WHAT MOVING d INTO THE BAND COSTS THE DARK-ENERGY FLOOR")
print("=" * 76)
print(f"  {'d':>8}  {'rho^(1/4) [meV]':>17}  {'vs observed':>12}")
print("  " + "-" * 42)
for label, d in (("3 (theory)", 3.0), ("2.9934 (obs)", d_rho),
                 ("2.9326 (band top)", d_band_hi), ("2.9211 (anchor)", d_anchor),
                 ("2.8092 (band bottom)", d_band_lo)):
    print(f"  {label:>20}  {rho_of(d)*1e3:12.4f}  {(rho_of(d)/RHO_OBS-1)*100:+11.2f}%")

print()
print("=" * 76)
print("READING")
print("=" * 76)
print("  The convergence found earlier -- the anchor and the band both wanting alpha_c below")
print("  3.alpha(0) -- reads as evidence for a free medium constant only while d is free.")
print("  It is not: the spine ties the same d to the dark-energy floor through d^2/2, and")
print("  there d = 3 is what buys the +0.44% landing. Letting alpha_c drift down to satisfy")
print(f"  the band drags the floor with it, to {(rho_of(d_band_hi)/RHO_OBS-1)*100:+.1f}% at the band's top and"
      f" {(rho_of(d_band_lo)/RHO_OBS-1)*100:+.1f}% at its bottom.")
print()
print("  So the three constraints are mutually exclusive at about the 2% level, and the")
print("  choice is between them rather than between the fork's two horns. Either the")
print("  indirect band is wrong, or the dark-energy floor's d^2/2 does not carry the same d")
print("  as the coupling, or the +0.44% landing is a coincidence that a corrected d spoils.")
print("  Nothing recorded decides which, and the second option is the cheapest to test:")
print("  it asks only whether the geometry factor and the coupling factor were ever one")
print("  quantity, which is a statement about the derivation rather than about any datum.")
