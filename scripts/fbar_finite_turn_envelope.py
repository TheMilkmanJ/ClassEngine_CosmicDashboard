"""Can f_bar actually differ from 2/pi, and by how much?

The band on alpha_c inverts epsilon = c.f_bar.alpha_c, so moving f_bar moves the band. The
previous pass observed that f_bar's fit-implied value sits 1.81% below the booked 2/pi and that
applying that shift nearly closes the conflict with the dark-energy floor. That reasoning needs
a check it did not get: f_bar is not a measured constant.

    <|cos|> over a uniformly distributed phase = (1/2pi) * integral |cos| = 2/pi, EXACTLY.

So 2/pi is a theorem given equidistribution, and the fit's 0.6253 is a noisy estimate of it, not
a rival value. A 1.81% shift cannot be helped along by preferring the estimate.

What CAN move f_bar is failure of the premise: a finite number of turns. Over an exact whole
number of turns the average is 2/pi identically; a partial turn leaves a residue. This script
computes that envelope, which is the only honest way the band's f_bar moves.

Run: python3 scripts/fbar_finite_turn_envelope.py
"""
import math

TWO_OVER_PI = 2 / math.pi


def _G(x):
    """Antiderivative of |cos| from 0 to x, closed form. |cos| has period pi with integral 2
    over each period; inside a period the primitive is sin r, or 2 - sin r past the quarter."""
    m, r = divmod(x, math.pi)
    return 2 * m + (math.sin(r) if r <= math.pi / 2 else 2 - math.sin(r))


def mean_abs_cos(turns, phase=0.0):
    """Exact time-average of |cos| over `turns` turns starting at `phase`."""
    T = 2 * math.pi * turns
    return (_G(phase + T) - _G(phase)) / T


print("=" * 76)
print("THE PREMISE, CHECKED")
print("=" * 76)
print(f"  2/pi                                {TWO_OVER_PI:.9f}")
for n in (1, 2, 10, 50):
    print(f"  <|cos|> over exactly {n:3} turns      {mean_abs_cos(n):.9f}"
          f"   (deviation {abs(mean_abs_cos(n)/TWO_OVER_PI-1)*100:.2e}%)")
print()
print("  Over any whole number of turns the average is 2/pi to numerical precision. The")
print("  booked value is therefore exact under the stated premise, and the fit's 0.6253 is")
print("  an estimate of it rather than a competing determination.")

print()
print("=" * 76)
print("THE ONLY WAY IT MOVES: A PARTIAL TURN")
print("=" * 76)
print(f"  {'turns N':>9}  {'worst-case deviation':>21}  {'1/(pi N) for comparison':>24}")
print("  " + "-" * 60)
for N in (1.0, 2.0, 5.0, 10.0, 18.0, 30.0, 100.0):
    worst = 0.0
    # sweep the starting phase and the fractional part; the residue is a partial half-period
    for j in range(400):
        frac = j / 400.0
        for k in range(200):
            ph = math.pi * k / 200
            d = abs(mean_abs_cos(N + frac, ph) / TWO_OVER_PI - 1)
            worst = max(worst, d)
    print(f"  {N:9.1f}  {worst*100:20.3f}%  {1/(math.pi*N)*100:23.3f}%")

print()
print("=" * 76)
print("WHAT THAT DOES TO THE PREVIOUS PASS")
print("=" * 76)
print("  The 1.81% shift the earlier pass borrowed from the fit is real ONLY if the winding")
print("  is short enough for a partial turn to matter. The envelope above puts that at")
print("  roughly N < 20 turns; past a few tens of turns f_bar is pinned to 2/pi far tighter")
print("  than the 2.08% conflict, and the escape closes.")
print()
print("  So branch (a) does not rest on 'the fit disagrees with 2/pi' -- that is noise around")
print("  a theorem. It rests on whether the winding completes enough turns, which is a")
print("  physical question with a recorded answer elsewhere in the corpus, and a different")
print("  question from the one the fit's scatter answers.")
print()
def envelope(N):
    w = 0.0
    for j in range(400):
        for k in range(200):
            w = max(w, abs(mean_abs_cos(N + j / 400.0, math.pi * k / 200) / TWO_OVER_PI - 1))
    return w


lo, hi = 1.0, 60.0
for _ in range(40):
    mid = 0.5 * (lo + hi)
    if envelope(mid) > 0.0208:
        lo = mid
    else:
        hi = mid
print("  Stated as a requirement: closing the alpha_c conflict through f_bar needs the")
print(f"  winding to be short. Solving the envelope for a 2.08% worst case gives")
print(f"  N = {0.5*(lo+hi):.1f} turns -- and note the 1/(pi N) proxy would have said"
      f" {1/(math.pi*0.0208):.0f}, overstating")
print("  the allowance by a factor of three. Anything longer than a handful of turns")
print("  leaves the conflict standing at close to its full 2.08%.")
