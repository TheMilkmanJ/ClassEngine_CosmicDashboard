"""If the family Z3 is broken by the electron's doping, is the residual electron-localised?

The emergent-Z3 reading says the family symmetry is exact in the infrared and broken at the
pairing shell by whatever dopes one node pair -- and the charge weighting says that pair is the
electron's. If so the breaking is not democratic: it should show up preferentially on the seat
that carries it.

That is a prediction beyond the one residual the reading was built to explain, so it is worth
testing. Take the zero-parameter node (A = sqrt2, phi = 2/9 exactly), fit only the overall scale,
and ask where the residuals sit.

The answer depends on the spurion's form, and this script reports both readings rather than
choosing: an ADDITIVE perturbation on sqrt(m) and a MULTIPLICATIVE one are different hypotheses
and they rank the seats differently.

Run: python3 scripts/z3_spurion_localisation.py
"""
import math

ME, MMU, MTAU = 0.51099895000, 105.6583755, 1776.86
TWOPI3 = 2 * math.pi / 3
A0, P0 = math.sqrt(2.0), 2.0 / 9
SEAT = (("tau", 0, MTAU), ("e", 1, ME), ("mu", 2, MMU))

s_meas = {n: math.sqrt(m) for n, _, m in SEAT}
a_fit = sum(s_meas.values()) / 3.0                      # the one free parameter
pred = {n: a_fit * (1 + A0 * math.cos(P0 + TWOPI3 * k)) for n, k, _ in SEAT}

print("=" * 76)
print("THE ZERO-PARAMETER NODE AGAINST THE MEASURED SEATS")
print("=" * 76)
print(f"  a (the only fitted quantity) = {a_fit:.9f} MeV^1/2")
print()
print(f"  {'seat':<6} {'sqrt(m) measured':>18} {'predicted':>16} {'residual':>14} {'relative':>12}")
print("  " + "-" * 72)
res_abs, res_rel = {}, {}
for n, _, _m in SEAT:
    d = s_meas[n] - pred[n]
    res_abs[n] = d
    res_rel[n] = d / pred[n]
    print(f"  {n:<6} {s_meas[n]:18.9f} {pred[n]:16.9f} {d:+14.3e} {d/pred[n]*1e6:+11.2f} ppm")
print()
print(f"  residuals sum to {sum(res_abs.values()):+.2e} -- identically zero, since a is their mean,")
print("  so only two of the three are independent and no seat can be off on its own.")

print()
print("=" * 76)
print("WHERE THE BREAKING SITS, ON EACH READING")
print("=" * 76)
lo_a = sorted(res_abs, key=lambda n: -abs(res_abs[n]))
lo_r = sorted(res_rel, key=lambda n: -abs(res_rel[n]))
print(f"  ADDITIVE on sqrt(m) -- largest first:   {', '.join(f'{n} ({res_abs[n]:+.2e})' for n in lo_a)}")
print(f"  MULTIPLICATIVE      -- largest first:   {', '.join(f'{n} ({res_rel[n]*1e6:+.1f} ppm)' for n in lo_r)}")
print()
print(f"  The two orderings disagree: absolutely the tau carries most, relatively the electron")
print(f"  does, by {abs(res_rel['e']/res_rel['mu']):.1f}x over the muon and {abs(res_rel['e']/res_rel['tau']):.0f}x over the tau. That is not evidence")
print("  either way -- it is arithmetic. The electron's seat ratio is the smallest of the three")
print(f"  ({pred['e']/a_fit:.4f} against {pred['tau']/a_fit:.4f}), so any absolute perturbation looks largest there")
print("  in relative terms whatever its origin.")

print()
print("=" * 76)
print("SO THE TEST DOES NOT BITE, AND THIS IS WHAT WOULD MAKE IT")
print("=" * 76)
print("  The prediction 'the breaking is electron-localised' is only testable once the spurion's")
print("  form is fixed, because the two natural forms rank the seats oppositely. What the emergent")
print("  reading owes is therefore not a size but a FORM: does the doping perturb sqrt(m)")
print("  additively (a shift of the seat) or multiplicatively (a rescaling of the hopping)?")
print()
print("  Those are distinguishable. An additive spurion breaks the circulant structure itself and")
print("  would show up as a departure from the Parseval identity Q = 1/3 + A^2/6; a multiplicative")
print("  one preserves the circulant and moves only A and phi. The Parseval identity is exact on")
print("  the measured masses by construction, so it cannot discriminate either -- but a FOURTH")
print("  measured mass would, and the sector has none.")
print()
print("  Recording the negative result: the emergent-Z3 reading makes no further prediction that")
print("  the three charged-lepton masses can test. It stands or falls on the spurion, and three")
print("  numbers with one fitted scale leave two residuals, which is exactly the freedom two")
print("  unknowns (A and phi) already use up.")
