"""lowh_gradient_scan — the owed fine-gradient tilt scan, run where the physics now lives (2026-07-27).

THE OWED ITEM (room 1's owed block, second clause)
  Gate C found chaos gradients ~350/rad in steep zones at h = 300,
  r_t = 0.9 (vs ~0.26/rad coarse at r_t = 0.3) and vetoed high-tilt +
  high-H_inf corners through the θ-channel isocurvature: steep df/dθ₀
  amplifies inflationary angle fluctuations into an isocurvature mode.
  The owed fine-gradient scan across tilts was never run.

WHAT THIS RUNS
  The same validated instrument (lowh_dice), dense-θ₀ (56 angles), at
  h = 0.1, 0.3 and 1.0 — all three tilts — measuring max|df_amp/dθ₀| by
  central differences.  The h = 1.0 rows are the STANDING ones: the
  physical hierarchy is h₀ = λΨ₀²/m² = 1.01 from the misalignment
  abundance closure (`genesis_solver_B1.py`, release at H = m, which
  reproduces this corpus's canonical onset 1 + z = 4.03×10⁷).  The two
  lower rows bracket it from below and show the trend.
  Expectation on record: the steep zones are a large-h chaos feature;
  at h₀ of order unity the map θ₀ → f_amp should be smooth with gradients
  O(1)/rad, retiring the isocurvature veto's bite at the standing
  parameters.  If steep zones survive here, the veto stays live —
  report exactly.  The verdict is graded on the h = 1.0 rows.
"""
from __future__ import annotations

import math
import sys
import pathlib

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lowh_dice import universe  # noqa: E402

N_ANGLES = 56
LO, HI = 0.05, math.pi / 4 - 0.05


def scan(h: float, rt: float):
    thetas = np.linspace(LO, HI, N_ANGLES)
    f = np.array([1.0 - universe(t, h, rt) for t in thetas])
    grad = np.gradient(f, thetas)
    return thetas, f, grad


def main() -> None:
    print("=" * 78)
    print("Fine-gradient tilt scan at the physical hierarchy (56 angles)")
    print("=" * 78)
    print("\n   h     r_t   max|df/dθ₀| [/rad]   median f_amp   spread")
    worst = 0.0
    for h in (0.1, 0.3, 1.0):
        for rt in (0.3, 0.6, 0.9):
            th, f, g = scan(h, rt)
            mg = float(np.max(np.abs(g)))
            if h == 1.0:                    # graded on the standing rows only
                worst = max(worst, mg)
            print(f"   {h:<4}  {rt:.1f}   {mg:10.2f}           "
                  f"{np.median(f):.3f}         {f.max()-f.min():.3f}")
    print(f"\n   worst gradient at the standing hierarchy h = 1.0: {worst:.2f}/rad")
    print("   (Gate C's steep zones at h = 300, r_t = 0.9: ~350/rad)")

    print("\nVERDICT:")
    if worst < 5.0:
        print("   The steep zones are GONE at the standing hierarchy — the map")
        print(f"   θ₀ → f_amp is smooth (max {worst:.1f}/rad, a factor")
        print(f"   ~{350.0/max(worst,1e-9):.0f} below Gate C's steep zones). The")
        print("   θ-channel isocurvature amplification that vetoed high-tilt +")
        print("   high-H_inf corners has no lever arm at h₀ ≈ 1: the veto is")
        print("   retired at the standing parameters (it remains a true fact")
        print("   about the era-parameter regime it was found in). The owed")
        print("   fine-gradient scan is PAID in its physical form.")
    else:
        print(f"   Steep structure SURVIVES at low h (max {worst:.1f}/rad) —")
        print("   the veto keeps its bite; map the zones and report exactly.")
    print("=" * 78)


if __name__ == "__main__":
    main()
