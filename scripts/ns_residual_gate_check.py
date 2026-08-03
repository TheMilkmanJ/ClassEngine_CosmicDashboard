"""ns_residual_gate_check — task #9, gate (2): the mechanism's residual vs the registered line (2026-07-28).

THE GATE
  The tilt mechanism's built-in residual is correlated isocurvature at
  S/ζ = 1/(r·L), L = ln(k_UV/k) = 2/(1−n_s) at the pivot.  P-2026-031
  registers a percent-level isocurvature contribution (peaking near ℓ ≈ 170;
  kill: a CMB bound tightening below the predicted level).  Gate (2) of the
  tilt's promotion asks whether the mechanism's residual lands inside the
  registered class over the construction's own surviving band r ∈ [0.8, 2.3].

GRADE RULE
  Pure arithmetic on recorded numbers.  PASS: the residual sits in the
  percent class across the surviving band (consistency — the mechanism's
  residual IS the registered line's amplitude class, one object read twice).
  FAIL: the residual leaving the class inside the surviving band.
"""
from __future__ import annotations

import math

NS = 0.9677
R_BAND = (0.8, 2.3)


def main() -> None:
    L = 2.0 / (1.0 - NS)
    print("=" * 78)
    print("The tilt's residual against the registered isocurvature line")
    print("=" * 78)
    print(f"\n   L = 2/(1−n_s) = {L:.1f} e-folds at the pivot")
    print("   r      S/ζ = 1/(rL)")
    for r in (R_BAND[0], 1.0, 1.5, R_BAND[1]):
        print(f"   {r:4.1f}   {100.0/(r*L):5.2f}%")
    lo, hi = 100.0 / (R_BAND[1] * L), 100.0 / (R_BAND[0] * L)
    print(f"\n   over the surviving band: S/ζ ∈ [{lo:.2f}%, {hi:.2f}%] — the")
    print("   percent class, which is P-2026-031's registered amplitude class.")
    print("   The mechanism's residual and the registered line are one object")
    print("   read twice; no tension anywhere inside the surviving band (the")
    print("   r ≲ 0.1 tension zone lies outside it).")
    print("\nVERDICT: gate (2) PASSES — consistency, not promotion. The tilt's")
    print("   remaining gate is the rate normalization (task #15's weight-zero")
    print("   exhibit); P-2026-031's own referee (a future CMB bound at ℓ ≈ 170)")
    print("   is unchanged and external.")
    print("=" * 78)

    assert 0.5 < lo < hi < 2.5
    assert abs(L - 61.9) < 0.5


if __name__ == "__main__":
    main()
