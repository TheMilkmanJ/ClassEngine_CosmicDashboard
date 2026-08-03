"""spherical_drift_scaling — why the spherical rebound cannot meet its own energy gate (2026-07-27).

THE SITUATION
  `bounce_m6_rebound_dst.py` is the instrument for gate (a) of the
  white-hole task: an energy-clean spherical focusing factor F, to be
  compared against the recorded O6 bar (F ≥ 1.0×10⁹ at the deepest door,
  3.2×10¹¹ CMB-class).  It gates on energy drift ≤ 2%; anything above
  that grades nothing.  Three of its four configurations have returned,
  and all three are refused by that gate.

WHAT THIS SCRIPT ASKS
  Not "is the drift large" but "which way does it move".  The three rows
  span roughly one decade in achieved focusing, so the scaling of drift
  WITH focus is measurable — and it is the scaling, not the magnitude,
  that decides whether more compute can ever close the gate.

THE ROWS (as printed by the run)
    A     focus       drift        steps
     5   1695.14×   391.356%    1,800,257
    20    476.66×   118.858%    1,804,936
    50    201.76×    24.222%    1,810,165
  Note the ordering: the DEEPEST focusing carries the LARGEST error.
  Amplitude and focus run opposite here (a bigger initial amplitude
  reaches a shallower peak compression in this scheme), so the natural
  variable is the focus factor itself.

THE POINT
  If drift grows with focus, the energy gate and the physics bar pull in
  opposite directions: every step toward the compression the bar demands
  makes the run less quotable.  The gate would then be unreachable by
  construction rather than by resolution, and no amount of running the
  present configuration fixes it.
"""
from __future__ import annotations

import math

ROWS = [(5, 1695.14, 391.356), (20, 476.66, 118.858), (50, 201.76, 24.222)]
GATE = 2.0          # percent, the run's own energy gate
BAR_LO, BAR_HI = 1.0e9, 3.2e11   # the recorded O6 focusing bar


def fit_power_law(xs, ys):
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    n = len(lx)
    mx, my = sum(lx) / n, sum(ly) / n
    p = (sum((lx[i] - mx) * (ly[i] - my) for i in range(n))
         / sum((lx[i] - mx) ** 2 for i in range(n)))
    return math.exp(my - p * mx), p


def main() -> None:
    print("=" * 78)
    print("The spherical instrument's error scales with the quantity it measures")
    print("=" * 78)
    print("\n     A      focus      drift(%)   drift/focus")
    for A, F, d in ROWS:
        print(f"   {A:4d}   {F:9.2f}   {d:9.3f}   {d/F:10.4f}")

    c, p = fit_power_law([F for _, F, _ in ROWS], [d for _, _, d in ROWS])
    print(f"\n   power-law fit over the measured decade:  drift(%) ≈ "
          f"{c:.4g} · focus^{p:.2f}")
    print(f"   the exponent is the finding: p = {p:.2f} > 1, so error grows")
    print("   FASTER than the compression being measured.")

    fmax = (GATE / c) ** (1.0 / p)
    print(f"\n   drift ≤ {GATE}% therefore requires focus ≤ {fmax:.0f}×")
    print(f"   the recorded O6 bar requires focus ≥ {BAR_LO:.0e} "
          f"(and {BAR_HI:.1e} CMB-class)")
    print(f"   → the two requirements are separated by {math.log10(BAR_LO/fmax):.1f} "
          f"decades in focus, in OPPOSITE directions")

    print("\n   extrapolated drift at the bar (stated as the extrapolation it is):")
    for F in (1e3, 1e6, 1e9):
        print(f"     focus {F:.0e} → drift ≈ {c*F**p:.3g}%")

    print("\nVERDICT: the gate is unreachable by this scheme, not by this budget.")
    print("   Within the measured decade the drift grows as focus^1.3, so every")
    print("   step toward the compression the bar demands makes the run less")
    print("   quotable — running longer, or on more configurations, moves the")
    print("   wrong way. Closing gate (a) needs a formulation whose error does")
    print("   not track the compression: a manifestly conservative scheme")
    print("   (symplectic or constraint-projected), or a reformulation in a")
    print("   variable that is regular at the focus, rather than a finer grid.")
    print("\n   HONESTY ON THE EXTRAPOLATION: three points over ~1 decade,")
    print("   extended to 9 — the exponent is indicative, not measured, at the")
    print("   bar. What is NOT an extrapolation is the sign: drift rises with")
    print("   focus across every row, and that alone settles the direction.")
    print("   The fourth configuration is still running and can sharpen the")
    print("   exponent; it cannot change the sign.")
    print("=" * 78)


if __name__ == "__main__":
    main()
