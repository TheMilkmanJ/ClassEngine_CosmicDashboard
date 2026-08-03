"""f_bar's averaging window: the two readings are not equally supported by the corpus's own data.

THE RECORDED ABSENCE (winding_turn_budget.py's own closing words):

    "the two readings do not merely differ in precision, they differ in kind, and nothing recorded
     says which one the epsilon-assembly uses. That is the owed piece: not 'is equidistribution
     granted' but 'over what window is the average taken'."

THE TWO READINGS
  ACCUMULATED  -- f_bar is <|cos theta|> over the winding actually laid down. The turn budget gives
                  N = 3.82e5 turns, essentially all near T_sph, so f_bar = 2/pi to 2.6e-5%. On this
                  reading 2/pi is PREDICTED, with no freedom.
  INSTANTANEOUS -- below ~1.7 MeV the phase is frozen, so f_bar is not an average at all: it is
                  |cos theta_freeze|, one number with no reason to sit anywhere in particular.

THE DISCRIMINATOR. These make different predictions about a quantity the corpus has already
measured twice. The accumulated reading says f_bar must land on 2/pi. The instantaneous reading
says it lands wherever the phase froze, and |cos theta| for an equidistributed theta has a known
distribution -- so the probability of landing as close to 2/pi as observed is computable. That
turns a question of taste into a likelihood ratio.

Run: python3 scripts/fbar_window_discriminator.py
"""
import math

TWO_OVER_PI = 2 / math.pi
N_TURNS = 3.82e5                      # from winding_turn_budget.py
MEAS = (("fit-implied", 0.6253), ("winding-sim", 0.635))


def p_within(frac):
    """P(||cos theta| - 2/pi| <= frac * 2/pi) for theta equidistributed on [0, 2pi)."""
    lo = max(0.0, TWO_OVER_PI * (1 - frac))
    hi = min(1.0, TWO_OVER_PI * (1 + frac))
    # |cos| has CDF (2/pi) arcsin(x) on [0, 1]
    return (2 / math.pi) * (math.asin(hi) - math.asin(lo))


print("=" * 78)
print("(1) WHAT EACH READING PREDICTS")
print("=" * 78)
print(f"  ACCUMULATED:  N = {N_TURNS:.2e} turns  ->  f_bar = 2/pi to within"
      f" {100/(math.pi*N_TURNS):.2e}%")
print("                 2/pi is PREDICTED. No freedom, nothing to fit.")
print()
print("  INSTANTANEOUS: f_bar = |cos theta_freeze|, drawn once from the |cos| distribution,")
print("                 whose density is 2/(pi sqrt(1-x^2)) on [0,1] and whose MEAN is 2/pi --")
print("                 so 2/pi is the typical value but carries the full spread.")
sd = math.sqrt(0.5 - TWO_OVER_PI**2)
print(f"                 spread: sd(|cos|) = sqrt(1/2 - (2/pi)^2) = {sd:.4f}"
      f"  ({sd/TWO_OVER_PI*100:.1f}% of the mean)")

print()
print("=" * 78)
print("(2) THE CORPUS'S TWO MEASUREMENTS, AGAINST BOTH")
print("=" * 78)
print(f"  {'measurement':<16} {'value':>9} {'offset from 2/pi':>18} {'P(frozen lands this close)':>28}")
print("  " + "-" * 76)
ps = []
for name, val in MEAS:
    frac = abs(val / TWO_OVER_PI - 1)
    p = p_within(frac)
    ps.append(p)
    print(f"  {name:<16} {val:9.4f} {frac*100:17.2f}% {p*100:27.2f}%")
print()
print("  Under the accumulated reading each of these is a hit with probability ~1 (the")
print("  prediction is 2/pi and the measurements carry their own errors).")
print("  Under the instantaneous reading each is a coincidence at the quoted probability.")

print()
print("=" * 78)
print("(3) THE LIKELIHOOD RATIO")
print("=" * 78)
print("  ONLY ONE of the two measurements may be used, and it is not the tighter one.")
print("  The winding-sim SIMULATES the winding premise, so it is guaranteed to land on 2/pi")
print("  whatever the physical window is -- it tests the arithmetic of the average, not the")
print("  choice of window. Quoting its 0.25% as evidence against the frozen reading would be")
print("  circular. The fit-implied value is the only number drawn from data rather than from")
print("  the premise under test.")
print()
p_used = p_within(abs(MEAS[0][1] / TWO_OVER_PI - 1))
print(f"    fit-implied f_bar = {MEAS[0][1]}, offset {abs(MEAS[0][1]/TWO_OVER_PI-1)*100:.2f}%")
print(f"    P(a frozen phase lands this close to 2/pi) = {p_used*100:.2f}%")
print(f"    odds favouring the accumulated reading      = {1/p_used:.0f} : 1")
print()
print("  That is modest evidence, and it should be read as modest. A 1-in-53 coincidence is")
print("  not rare across a corpus with far more than 53 numbers in it, so the look-elsewhere")
print("  effect eats much of it. What it is NOT vulnerable to is fitting: the turn budget was")
print("  computed from theta_dot/H = 2.4e6 and theta_dot ~ T^3, both recorded for baryogenesis")
print("  and neither touched by the amplitude, so 3.82e5 turns was not chosen to make this work.")

print()
print("=" * 78)
print("(4) THE SENSITIVITY — HOW CLOSE WOULD IT HAVE TO BE TO SETTLE IT?")
print("=" * 78)
print(f"  {'offset from 2/pi':>18} {'P(frozen)':>12} {'odds':>12}")
print("  " + "-" * 46)
for frac in (0.10, 0.05, 0.02, 0.0181, 0.01, 0.003, 0.001):
    p = p_within(frac)
    print(f"  {frac*100:17.2f}% {p*100:11.3f}% {1/p:11.0f}:1")
print()
print("  The corpus's tightest reading sits at 1.81%. Halving the measurement error would")
print("  roughly double the odds; getting to 0.3% would put it past 300:1. So this is a")
print("  question the production chains can actually settle, and the quantity to watch is the")
print("  posterior width on epsilon, since f_bar is inferred through it.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  The window is the ACCUMULATED one, at evidence grade rather than by assertion. The")
print("  distinction matters beyond bookkeeping because the two readings differ in KIND:")
print()
print("    * accumulated -> f_bar = 2/pi is a theorem given the turn budget, the alpha_c")
print("      conflict stands at its full 2.08%, and branch (a) of that conflict is dead by")
print("      six orders. Nothing about f_bar is available to relieve the tension.")
print("    * instantaneous -> f_bar is a free parameter that happens to sit near 2/pi, the")
print("      2.08% conflict can be absorbed into it, and the amplitude's decomposition loses")
print("      one of its three derived factors.")
print()
print("  Recording which one is live therefore changes what the alpha_c conflict means, and")
print("  the evidence points at the reading that makes the conflict REAL. That is the")
print("  uncomfortable direction, which is the one worth trusting.")
print()
print("  STILL OWED. The operator form -- whether the shift in m_e is laid down as an integral")
print("  over the winding epoch or read off the phase at recombination -- is a statement about")
print("  the coupling that the corpus has not written down. The likelihood ratio argues for the")
print("  first; it does not derive it.")
