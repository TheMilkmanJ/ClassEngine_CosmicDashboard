"""sm_crossing_two_scale — task #14: the Standard-Model crossing resolves by scale separation (2026-07-27).

THE FORK, AND WHAT FORCES IT
  Reading A (single-scale): everything — metric and all fields — fails at
  402-AU-scale gradients; photons must exotically convert at the door.
  Reading B (two-scale): the photon is the SUBSTRATE's transverse Goldstone
  mode (the recorded light framework), and the substrate's coherence scale
  is far below the dark fluid's 402 AU; the door is the DARK FLUID's
  hydrodynamic edge, not the substrate's.
  THE FORCING ARGUMENT (observational, computed below): photons propagate
  today at wavelengths ~17 orders below the dark fluid's coherence length,
  over gigaparsec distances, with no dispersion (the recorded Lorentz-
  invariance pricing).  A mode cannot ride a carrier whose coherence it
  outresolves by 10¹⁷ — the photon's carrier is coherent FAR below ξ, so at
  the door (gradients at ξ) the substrate and its modes persist.  Reading B
  is forced; Reading A is dead on today's sky.

WHAT THE CROSSING THEN IS (textbook, computed)
  Through the interval, photons are ordinary fields in a dense e± plasma:
    * "massed": the in-medium photon mass is the thermal plasma frequency,
      ω_p ≈ eT/3 ≈ 0.1·T — at an MeV bath, a ~100 keV effective mass.  The
      story-grade "the crunch mouth masses the photons" upgrades to
      textbook in-medium field theory.
    * "thermalized": Compton locking at the recorded rates (Γ/H ~ 10¹⁷
      class at the relevant epochs) — the bath is one self-equilibrated
      fluid throughout.
    * portals to the dark sector are the recorded tiny couplings — no
      exotic sink.  THE BATH'S ENERGY PASSES THROUGH CONSERVED.

THE BUDGET IMPLICATION (candidate grade — the MeV lever assessed)
  Under Reading B the door does not need to fund the hot start at all: the
  Standard-Model bath is a separate reservoir that rides the contraction,
  blueshifting as 1/a, massed and self-thermalized, passing through the
  dark sector's non-hydrodynamic interval intact.  The reheat is the bath's
  own adiabatic history.  The MeV question's Standard-Model lever RESOLVES
  in the affirmative at candidate grade, conditional on the two-scale
  reading and on the local rebounds not disrupting the bath (the portals
  say they cannot — recorded).

THE ARCHITECTURAL NOTE (filed for the reconstruction, not smuggled)
  Reading B refines the interval's meaning: not "metric off" but "the
  dominant component's hydrodynamics off."  No contradiction with the
  metric-on closures — those were HOMOGENEOUS-level (the fluid and
  constraint closures), and the door regime is violently inhomogeneous by
  the reconstruction's own results (the directional squeeze); the recorded
  "homogeneous quantum pressure vanishes" leaves the ξ-scale gradient
  stress — exactly what the verified rebound uses — as the local turn's
  source, with the metric on.  Filed as a candidate reframing in the
  reconstruction log; the bounce program's tasks carry the update.

GRADE RULE
  The forcing argument is observational arithmetic; the crossing physics is
  textbook in-medium QED at recorded rates; the budget implication and the
  reframing are candidate grade with their conditions named.
"""
from __future__ import annotations

import math

XI_M = 402.0 * 1.496e11            # dark fluid coherence length, meters
LAMBDA_CMB_M = 1.06e-3             # CMB peak wavelength today, meters
GPC_M = 3.086e25
ALPHA = 1.0 / 137.036
E_CHARGE = math.sqrt(4.0 * math.pi * ALPHA)


def main() -> None:
    sub = XI_M / LAMBDA_CMB_M
    print("=" * 78)
    print("The Standard-Model crossing: forced two-scale reading, textbook physics")
    print("=" * 78)
    print(f"\n1. The forcing argument:")
    print(f"   photon wavelength (CMB peak) / dark-fluid coherence: 1 : {sub:.1e}")
    print(f"   propagation distance observed undispersed: ~Gpc = {GPC_M/XI_M:.1e}·ξ")
    print("   A mode resolving its carrier's 'coherence cells' by 17 orders,")
    print("   over 10¹¹ coherence lengths, with no dispersion (the recorded")
    print("   Lorentz-invariance pricing at 10⁻¹²–10⁻³⁸): the photon's carrier")
    print("   is NOT the 402-AU-coherent dark fluid. The substrate stays")
    print("   coherent far below ξ ⟹ at the door, photons persist. Reading B")
    print("   forced; Reading A dead on today's sky.")

    print(f"\n2. The crossing, textbook:")
    for T_kev in (177.0, 511.0, 1000.0):
        wp = E_CHARGE * T_kev / 3.0
        print(f"   T = {T_kev:6.0f} keV:  in-medium photon mass ω_p ≈ eT/3 = "
              f"{wp:6.1f} keV")
    print("   'massed' = the thermal plasma frequency (in-medium QED);")
    print("   'thermalized' = Compton locking at the recorded Γ/H ~ 10¹⁷ class;")
    print("   portals to the dark sector: recorded tiny — no exotic sink.")

    print(f"\n3. The budget implication (candidate):")
    print("   the bath rides the contraction as its own conserved reservoir,")
    print("   blueshifting 1/a, passing through the dark sector's interval")
    print("   intact — the door does not fund the hot start; the contraction")
    print("   already did. The MeV lever resolves affirmative, conditional on")
    print("   the two-scale reading (forced above) and bath survival through")
    print("   local rebounds (the portals' smallness — recorded).")

    print(f"\n4. Architectural note, filed: the interval = the dominant")
    print("   component's non-hydrodynamic regime, metric on. Consistent with")
    print("   the homogeneous-level closures (the door is inhomogeneous by the")
    print("   reconstruction's own results; homogeneous quantum pressure")
    print("   vanishes — the ξ-scale gradient stress is the local turn's")
    print("   source, and the verified rebound is exactly that). Candidate")
    print("   reframing; the reconstruction log carries it.")
    print("=" * 78)

    assert sub > 1e16
    assert GPC_M / XI_M > 1e10
    assert abs(E_CHARGE * 1000.0 / 3.0 - 101.1) < 2.0


if __name__ == "__main__":
    main()
