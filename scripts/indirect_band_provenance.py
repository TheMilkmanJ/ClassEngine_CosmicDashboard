"""What does the indirect band on alpha_c actually measure?

P-2026-040 registers the band [0.0205, 0.0214] as an instrument against the alpha_c = 3 alpha
bet, and PRTOE_quantum_trio calls it one of "three instruments, one coupling, none able to cheat
for the others". But the band is not a direct reading of the coupling. It comes from the
zero-dial assembly

    epsilon = c . f_bar . alpha_c,    with c = 9/10 and f_bar = 2/pi

inverted on a measured epsilon. So the band's alpha_c carries two further model quantities that
the dark-energy floor's alpha_c does not: the democratic count c and the winding average f_bar.
Any error in either moves the band by the same fraction, and the conflict with the floor is
2.08% -- the size of an error the corpus already records in f_bar.

Run: python3 scripts/indirect_band_provenance.py
"""
import math

ALPHA = 1 / 137.035999084
C_DEMO = 0.9
F_2PI = 2 / math.pi
F_FIT = 0.6253          # the fit-implied winding average, recorded
F_SIM = 0.635           # the simulation's, recorded
F_RMS = math.sqrt(0.5)  # the rejected RMS reading
BAND_LO, BAND_HI = 0.0205, 0.0214
T_C = 0.5 * math.log(2) * 0.51099895e6
M_2 = ALPHA**2 * T_C
AC_FLOOR = math.sqrt(2 * 2.25e-3 / M_2)      # what the observed dark energy demands

print("=" * 76)
print("THE ASSEMBLY, AND WHAT THE BAND IS AN INVERSION OF")
print("=" * 76)
eps_at_3a = C_DEMO * F_2PI * 3 * ALPHA
print(f"  epsilon = c . f_bar . alpha_c   with c = {C_DEMO}, f_bar = 2/pi = {F_2PI:.6f}")
print(f"  at alpha_c = 3 alpha:  epsilon = {eps_at_3a*100:.4f}%   (registry records 1.254%)")
print(f"  the conversion factor c.f_bar   = {C_DEMO*F_2PI:.6f}")
print()
print(f"  so the band [{BAND_LO}, {BAND_HI}] on alpha_c is the band")
print(f"     [{BAND_LO*C_DEMO*F_2PI*100:.4f}%, {BAND_HI*C_DEMO*F_2PI*100:.4f}%] on epsilon, divided by c.f_bar.")
print()
print("  The floor's alpha_c comes from E_b = (1/2) alpha_c^2 M_2 and involves neither c nor")
print("  f_bar. The two instruments are therefore not independent in the way the trio's")
print("  'none able to cheat for the others' suggests: the band inherits two model numbers")
print("  the floor does not, and an error in either shifts it by the same fraction.")

print()
print("=" * 76)
print("HOW BIG AN ERROR WOULD IT TAKE, AND IS ONE ALREADY ON RECORD?")
print("=" * 76)
gap = AC_FLOOR / BAND_HI - 1
print(f"  the observed dark-energy floor demands alpha_c = {AC_FLOOR:.6f}")
print(f"  the band's top is                                {BAND_HI:.6f}")
print(f"  the conflict is                                  {gap*100:.2f}%")
print()
print("  The corpus records f_bar's alternatives explicitly:")
print(f"    {'reading':<34} {'f_bar':>9} {'vs 2/pi':>9}")
print("  " + "-" * 55)
for name, f in (("2/pi, the booked value", F_2PI), ("the fit-implied value", F_FIT),
                ("the simulation's value", F_SIM), ("RMS, rejected", F_RMS)):
    print(f"    {name:<34} {f:9.5f} {(f/F_2PI-1)*100:+8.2f}%")

print()
print("=" * 76)
print("WHAT EACH READING DOES TO THE BAND")
print("=" * 76)
print(f"  {'f_bar used':<34} {'band top':>10} {'vs the floor':>14}")
print("  " + "-" * 62)
for name, f in (("2/pi, the booked value", F_2PI), ("the fit-implied 0.6253", F_FIT),
                ("the simulation's 0.635", F_SIM)):
    top = BAND_HI * F_2PI / f          # epsilon fixed, alpha_c = eps/(c f_bar)
    print(f"  {name:<34} {top:10.6f} {(AC_FLOOR/top-1)*100:+13.2f}%")
print()
print(f"  Holding the measured epsilon fixed and swapping the booked 2/pi for the fit-implied")
print(f"  0.6253 -- a shift of {(F_2PI/F_FIT-1)*100:.2f}%, which the corpus itself carries -- moves the band's top")
print(f"  from {BAND_HI:.6f} to {BAND_HI*F_2PI/F_FIT:.6f} and cuts the conflict from {gap*100:.2f}% to"
      f" {(AC_FLOOR/(BAND_HI*F_2PI/F_FIT)-1)*100:.2f}%.")

print()
print("=" * 76)
print("READING")
print("=" * 76)
print("  This does not show the band is wrong. It shows the band is not the independent")
print("  instrument the triangulation treats it as, and that the discrepancy it reports")
print("  against the floor is the same size as an uncertainty already recorded in one of")
print("  its own inputs. Branch (a) of the fork -- 'the indirect band is wrong, or measures")
print("  a different quantity' -- therefore has a concrete and cheap form: the band measures")
print("  epsilon/(c.f_bar), and f_bar is known to about 2%.")
print()
print("  What would settle it is a determination of f_bar to better than 1%, or an alpha_c")
print("  reading that does not route through the assembly at all. The dispersion chain and")
print("  the isocurvature phase speed, the trio's other two doors, are both of that second")
print("  kind -- neither carries c or f_bar -- so the triangulation still has two clean legs.")
