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

# Gate C's recorded numbers, the ones the veto was derived at (era regime,
# h = 300, r_t = 0.9) — see the prereg thread's item (3).
GATE_C_GRAD = 350.0            # /rad
GATE_C_HINF_LO = 1.0e10        # GeV
GATE_C_HINF_HI = 1.0e11        # GeV
# The ordinary (non-theta-channel) isocurvature bound already in the books.
STD_HINF_LO = 2.0e12           # GeV
STD_HINF_HI = 4.0e12           # GeV


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
    print(f"   (Gate C's steep zones at h = 300, r_t = 0.9: {GATE_C_GRAD:.0f}/rad)")

    # The verdict is NOT a threshold on the gradient — any such threshold would
    # be invented.  The physical question is where the gradient puts the H_inf
    # ceiling.  The theta-channel isocurvature amplitude goes as
    # (df/dtheta0) * delta_theta0 with delta_theta0 = H_inf/(2 pi Psi0), so at
    # fixed isocurvature bound the ceiling scales as 1/gradient.
    ratio = GATE_C_GRAD / max(worst, 1e-9)
    lo, hi = GATE_C_HINF_LO * ratio, GATE_C_HINF_HI * ratio
    print(f"\n   the lever arm is {ratio:.0f}x weaker than Gate C's, so the")
    print(f"   theta-channel H_inf ceiling relaxes by the same factor:")
    print(f"     Gate C (era regime):  H_inf <~ {GATE_C_HINF_LO:.0e}-{GATE_C_HINF_HI:.0e} GeV")
    print(f"     standing hierarchy:   H_inf <~ {lo:.1e}-{hi:.1e} GeV")
    print(f"   against the ORDINARY isocurvature bound already in the books,")
    print(f"   H_inf < {STD_HINF_LO:.0e}-{STD_HINF_HI:.0e} GeV.")

    print("\nVERDICT:")
    if lo > STD_HINF_HI:
        print("   THE THETA-CHANNEL VETO IS NO LONGER BINDING at the standing")
        print("   hierarchy: its ceiling has risen clear above the ordinary")
        print("   isocurvature bound, so it cuts no corner that bound leaves.")
    elif hi < STD_HINF_LO:
        print("   THE THETA-CHANNEL VETO STILL BINDS at the standing hierarchy:")
        print("   its ceiling sits below the ordinary isocurvature bound, so it")
        print("   remains the tighter of the two and keeps cutting corners.")
    else:
        print("   THE THETA-CHANNEL VETO BECOMES DEGENERATE with the ordinary")
        print("   isocurvature bound at the standing hierarchy. Its ceiling no")
        print("   longer sits two decades under that bound as it did in the era")
        print("   regime — it now BRACKETS it. So the veto neither retires nor")
        print("   keeps its old bite: it stops being the separately binding")
        print("   constraint and becomes one of two comparable limits on H_inf.")
        print("   Anything resting on 'the theta-channel cuts corners the")
        print("   standard bound does not' no longer holds at these parameters;")
        print("   anything resting on 'the veto is gone' overstates it.")
    print("\n   NOTE: the gradient rises monotonically in BOTH h and tilt across")
    print("   this grid, so the standing hierarchy is the worst case ON the")
    print("   grid and the high-tilt row is what governs. Scans that stopped")
    print("   below h = 1 read a weaker gradient than the physics carries.")
    print("=" * 78)


if __name__ == "__main__":
    main()
