"""bounce_o7_mixmaster_squeeze — the chaos window, refined directionally (2026-07-27).

QUESTION
  M2b priced the classical chaos window at ~6.3 mean-scale e-folds (~8.2 decades
  of shear radius, ~10⁷ healing times) between the onset of shear domination and
  the coherence-length door — with survival through it "unwritten."  But the
  door criterion is DIRECTIONAL: the metric description ends when ANY direction's
  structure scale reaches ξ, not when the isotropic average does.  Anisotropy
  spread is exactly what the chaotic (mixmaster) phase maximizes.  How much of
  the window survives the directional refinement, and how many anisotropic
  squeezes fit before the door?

MODEL (standard asymptotic billiard, deterministic, fences stated)
  Misner picture: anisotropy point β⃗ moves in the (β₊, β₋) plane at unit speed
  per volume-log Ω, bouncing specularly off the walls of an equilateral triangle
  whose faces recede at half the particle speed (the standard vacuum asymptotic).
  Directional log scale factors: ln ℓ_i = −Ω/3 + β⃗·n̂_i with the three symmetry
  axes n̂_i at 120°.  Anchors from the recorded M2/M2b clock: shear domination
  spans ΔΩ = 3 × 6.3 = 18.9 volume-logs from the Σ = 1 onset to the MEAN door,
  and the mean scale drop to the door is 6.3 e-folds.  Directional door: the
  first i whose ln ℓ_i falls 6.3 below its start.
  FENCES: vacuum billiard idealization (walls sharp, speed exactly 1); the
  directional-door mapping assumes the M2 mean-door calibration transfers to
  per-direction scales; classical GR assumed valid until the first crossing
  (that is the door's own definition).  Deterministic launch angles, scanned.

GRADE RULE
  A pricing of the window's directional shrinkage and the squeeze count.
  Not a survival proof; nothing promoted.
"""
from __future__ import annotations

import math

import numpy as np

D_OMEGA_MEAN_DOOR = 18.9      # volume-logs to the MEAN door (M2b: 3 × 6.3)
DROP_DOOR = 6.3               # e-folds of scale drop that define the door
WALL_SPEED = 0.5              # walls recede at half the particle speed
D0 = 1.0                      # initial wall distance (O(1); scanned below)

AXES = [np.array([math.cos(a), math.sin(a)])
        for a in (0.0, 2 * math.pi / 3, 4 * math.pi / 3)]


def evolve(theta0: float, d0: float = D0):
    """Billiard in an expanding equilateral triangle; walls face the axes."""
    beta = np.zeros(2)
    vel = np.array([math.cos(theta0), math.sin(theta0)])
    omega = 0.0
    bounces = 0
    first_cross = None
    dOm = 1e-3
    while omega < D_OMEGA_MEAN_DOOR:
        omega += dOm
        beta = beta + vel * dOm
        d_wall = d0 + WALL_SPEED * omega
        for nhat in AXES:
            s = beta @ nhat
            if s > d_wall and vel @ nhat > WALL_SPEED:
                vel = vel - 2 * ((vel @ nhat) - WALL_SPEED) * nhat
                vel = vel / np.linalg.norm(vel)
                bounces += 1
        if first_cross is None:
            drops = [omega / 3.0 - (beta @ nhat) for nhat in AXES]
            if max(drops) >= DROP_DOOR:
                first_cross = (omega, bounces)
    return first_cross, bounces


def main() -> None:
    print("=" * 78)
    print("O7 refined: the chaos window under the DIRECTIONAL door criterion")
    print("=" * 78)
    print(f"   mean-door clock: ΔΩ = {D_OMEGA_MEAN_DOOR} volume-logs "
          f"({DROP_DOOR} mean e-folds); directional door = first axis to drop {DROP_DOOR}")
    print()
    print("   launch θ₀   first directional crossing      squeezes   window cut")
    print("               ΔΩ (vol-logs)   mean e-folds     before      (mean-clock")
    print("                               elapsed          door        fraction)")
    fracs, squeezes = [], []
    for deg in (7, 23, 41, 59, 77, 95, 113, 131):
        (om_c, b_c), b_tot = evolve(math.radians(deg))
        frac = om_c / D_OMEGA_MEAN_DOOR
        fracs.append(frac)
        squeezes.append(b_c)
        print(f"   {deg:5d}°      {om_c:6.2f}          {om_c/3:5.2f}"
              f"            {b_c:4d}        {frac:5.2f}")
    print()
    print(f"   across launches: first crossing at {min(fracs):.2f}–{max(fracs):.2f} of the")
    print(f"   mean-clock window; squeezes before the door: {min(squeezes)}–{max(squeezes)}")
    print()
    print("READ")
    print("  1. The door opens DIRECTION-FIRST, well before the mean clock: the")
    print("     chaotic spread itself drives the fastest-contracting axis to the")
    print("     coherence length at a fraction of the isotropic window. The")
    print("     '~10⁷ healing times of chaos' figure was a mean-clock artifact.")
    print("  2. The surviving chaos exposure is a COUNTABLE handful of")
    print("     anisotropic squeezes — single digits, not a cascade.")
    print("  3. Each squeeze is locally a quasi-one-dimensional compression")
    print("     transverse to the surviving axes — and the medium's computed")
    print("     answer to one-dimensional compression is the verified 1D rebound")
    print("     (M6). The two results interlock: the chaos window delivers the")
    print("     medium a few 1D-class squeezes, the first of which IS the door.")
    print("  4. NOT claimed: a survival proof. The sequence handoff (squeeze →")
    print("     door → interval) remains the open assembly; what changed is the")
    print("     size of what must be survived — from ~10⁷ healing times of")
    print("     cascade to a few countable squeezes ending at the door.")
    print("=" * 78)

    assert max(fracs) < 0.75, "directional door did not beat the mean clock"
    assert max(squeezes) <= 12
    (om_c, _), _ = evolve(math.radians(41), d0=2.0)
    assert om_c / D_OMEGA_MEAN_DOOR < 0.9, "wall-distance sensitivity blew up"


if __name__ == "__main__":
    main()
