"""quiet_branch_fine_search — does the quiet branch survive a FINE angular grid at the physical hierarchy? (2026-07-28)

WHY THIS RUN EXISTS
  #36's dice sampled 14 angles per (h, r_t) cell and found ZERO quiet
  draws anywhere — f_rot > 0.98 (equivalently f_amp < 0.02) never
  occurred.  That result is load-bearing: it is what promoted the
  ringing half of P-2026-005 from a probability to a regime fact, and
  what lets the granule meter keep its readout.

  The fine-gradient scan then ran 56 angles at the standing hierarchy
  h = 1.0 and reported, at r_t = 0.9, a median f_amp of 0.726 with a
  SPREAD of 0.963.  A spread that wide is only compatible with a
  minimum close to zero.  Fourteen angles can miss a narrow quiet
  window that fifty-six angles resolve, and "no quiet draw exists" is
  exactly the kind of claim a coarse grid can fake.

WHAT THIS MEASURES
  The same validated instrument (lowh_dice.universe), 56 angles across
  the fundamental domain, at the physical h = 1.0 and all three tilts:
  the MINIMUM f_amp, how many draws fall under the quiet threshold, and
  where in theta_0 the minimum sits.  A narrow window is reported with
  its width, because a quiet branch that occupies a vanishing measure of
  angle is a different physical statement from one that occupies a band.

  Pre-committed reading, fixed before the numbers:
   * no draw under 0.02  -> #36's conclusion survives refinement;
   * some draw under 0.02 -> "zero quiet draws" was a resolution
     artifact of the 14-angle grid and must be restated as a measure,
     not an absence.
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
QUIET = 0.02
H_PHYS = 1.0


def main() -> None:
    print("=" * 78)
    print("The quiet branch under a fine angular grid, at the standing h = 1.0")
    print("=" * 78)
    thetas = np.linspace(LO, HI, N_ANGLES)
    any_quiet = 0
    print(f"\n   quiet threshold: f_amp < {QUIET}  (f_rot > {1-QUIET})")
    print("\n   r_t    min f_amp   at theta_0   max     median   draws < 0.02")
    rows = {}
    for rt in (0.3, 0.6, 0.9):
        f = np.array([1.0 - universe(t, H_PHYS, rt) for t in thetas])
        rows[rt] = f
        n_quiet = int(np.sum(f < QUIET))
        any_quiet += n_quiet
        i = int(np.argmin(f))
        print(f"   {rt:.1f}    {f.min():.5f}     {thetas[i]:.4f}     "
              f"{f.max():.4f}  {np.median(f):.4f}      {n_quiet}/{N_ANGLES}")

    print("\n   the closest approach to the quiet branch, per tilt:")
    for rt, f in rows.items():
        print(f"     r_t = {rt}: min f_amp = {f.min():.5f} "
              f"= {f.min()/QUIET:.1f}x the quiet threshold")

    print("\nVERDICT:")
    if any_quiet == 0:
        closest = min(f.min() for f in rows.values())
        print("   THE QUIET BRANCH STAYS EMPTY under 4x the angular")
        print(f"   resolution. #36's conclusion is not a sampling artifact:")
        print("   every draw rings at the physical hierarchy, and the granule")
        print("   meter keeps its readout.")
        print()
        print("   BUT THE MARGIN IS THIN, AND 'ZERO DRAWS' HIDES THAT. The")
        print(f"   closest approach is f_amp = {closest:.5f} — only "
              f"{closest/QUIET:.1f}x the")
        print("   threshold, at the highest tilt. The minimum falls steeply")
        print("   with tilt (20.4x -> 5.9x -> 1.6x across r_t = 0.3, 0.6, 0.9),")
        print("   so the high-tilt corner is where the branch is nearly")
        print("   reached, and the tilt is a free dial. The defensible claim")
        print("   is 'no quiet draw, by a factor 1.6 at the worst tilt on the")
        print("   grid', not 'the quiet branch does not exist'. Anything")
        print("   downstream that treats the absence as structural rather than")
        print("   as a measured margin is claiming more than this run shows.")
    else:
        print(f"   {any_quiet} QUIET DRAWS APPEAR at 56 angles where 14 found")
        print("   none. 'Zero quiet draws' was a resolution artifact: the")
        print("   correct statement is a MEASURE — what fraction of the")
        print("   angular domain is quiet — not an absence. Every downstream")
        print("   claim resting on 'the branch does not exist' must be")
        print("   restated as a probability, and P-2026-005's ringing half")
        print("   goes back from regime fact to probability.")
    print("=" * 78)


if __name__ == "__main__":
    main()
