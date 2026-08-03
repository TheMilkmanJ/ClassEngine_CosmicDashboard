"""Where does the indirect band come from, and does it agree with the corpus's own epsilon?

An earlier pass asserted the band [0.0205, 0.0214] on alpha_c is the zero-dial assembly
epsilon = c.f_bar.alpha_c inverted on a measured epsilon. That assertion does not survive
arithmetic, and this script is the check that should have been run first.

The corpus records two epsilon-side numbers:
    the assembly's prediction at alpha_c = 3 alpha   ->  epsilon = 1.2543%
    the dyad posterior                                ->  epsilon ~ 1.24%

and separately the band [0.0205, 0.0214] on alpha_c. If the band were the posterior inverted,
the posterior would land inside it. It does not.

Run: python3 scripts/band_vs_epsilon_posterior.py
"""
import math

ALPHA = 1 / 137.035999084
C_DEMO, F_BAR = 0.9, 2 / math.pi
CF = C_DEMO * F_BAR
EPS_POST = 0.0124                 # the dyad posterior, recorded as ~1.24%
BAND_LO, BAND_HI = 0.0205, 0.0214
T_C = 0.5 * math.log(2) * 0.51099895e6
M_2 = ALPHA**2 * T_C
AC_FLOOR = math.sqrt(2 * 2.25e-3 / M_2)
AC_ANCHOR = 0.021316

print("=" * 76)
print("THE ASSEMBLY, BOTH WAYS")
print("=" * 76)
print(f"  c.f_bar = {CF:.7f}")
print(f"  forward:  alpha_c = 3 alpha = {3*ALPHA:.6f}  ->  epsilon = {CF*3*ALPHA*100:.4f}%"
      f"   (registry: 1.254%)")
print(f"  inverse:  epsilon = {EPS_POST*100:.2f}% (the dyad posterior)  ->  alpha_c ="
      f" {EPS_POST/CF:.6f}")
print()
print(f"  the band is                                          [{BAND_LO}, {BAND_HI}]")
print(f"  the posterior's alpha_c is                            {EPS_POST/CF:.6f}"
      f"   {'INSIDE' if BAND_LO <= EPS_POST/CF <= BAND_HI else 'OUTSIDE'}")
print(f"  the band expressed back on epsilon is                [{BAND_LO*CF*100:.4f}%,"
      f" {BAND_HI*CF*100:.4f}%]")
print(f"  the posterior sits above that interval by             "
      f"{(EPS_POST/(BAND_HI*CF) - 1)*100:.2f}%")
print()
print("  So the band is NOT the posterior inverted through the assembly. Whatever it is,")
print("  its derivation is not recorded: it appears in four forward-facing places and one")
print("  ledger entry, every one of which cites it and none of which derives it.")

print()
print("=" * 76)
print("TWO NUMBERS ABOUT ONE COUPLING, AND THEY DISAGREE")
print("=" * 76)
ac_post = EPS_POST / CF
print(f"  {'source':<44} {'alpha_c':>10}  {'vs the floor':>13}")
print("  " + "-" * 72)
for name, ac in (("the dark-energy floor's demand", AC_FLOOR),
                 ("the epsilon posterior, through the assembly", ac_post),
                 ("d = 3, the registered bet", 3 * ALPHA),
                 ("the indirect band, top", BAND_HI),
                 ("the hierarchy anchor's exact landing", AC_ANCHOR)):
    print(f"  {name:<44} {ac:10.6f}  {(AC_FLOOR/ac - 1)*100:+12.2f}%")
print()
print(f"  the two epsilon-side numbers differ by {(ac_post/BAND_HI - 1)*100:.2f}%, and it is the BAND,")
print("  not the posterior, that P-2026-040 grades the alpha_c bet against.")

print()
print("=" * 76)
print("WHY THE CONVERSION ITSELF IS CLEAN")
print("=" * 76)
print("  epsilon -> alpha_c does route through c.f_bar, so it inherits f_bar. But f_bar is")
print("  pinned: on the accumulated winding of 3.8e5 turns it sits within 2.6e-5 % of 2/pi,")
print("  so the conversion contributes nothing to the 1.1% gap. The disagreement between")
print("  the posterior and the band is therefore real and not an artefact of the assembly.")
print()
print("  That gives branch (a) a sharp form. It is not 'the band might be wrong' but")
print("  'the corpus holds two epsilon-side determinations that differ by 1.1%, and only")
print(f"  one of them is used as the instrument'. The posterior's alpha_c = {ac_post:.6f} sits")
print(f"  {abs(AC_FLOOR/ac_post - 1)*100:.2f}% from the floor's demand, against the band's {(AC_FLOOR/BAND_HI - 1)*100:.2f}% -- so which")
print("  number is the instrument decides how large the conflict is, and that is a question")
print("  about a recorded derivation rather than about new data.")
