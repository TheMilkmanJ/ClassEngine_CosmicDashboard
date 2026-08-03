"""bounce_task4_handoff_joints — the squeeze-to-interval handoff, as three joints (2026-07-27).

WHAT THIS IS AND IS NOT
  The handoff is NOT a new mechanism — it is the set of consistency joints
  between three already-computed results: the directional chaos door
  (bounce_o7_mixmaster_squeeze.py), the verified 1D medium rebound
  (bounce_m6_rebound_1d.py), and the achronal re-entry condition (M4).
  Each joint below is arithmetic on recorded anchors.  What the joints do
  not cover is listed at the end, not smoothed over.

J1  DELIVERY: what inflow does the squeeze hand the medium at the door?
    The billiard's velocity at first crossing gives the fast axis's
    contraction rate relative to the mean: H_fast/H_mean = 3·(1/3 − v⃗·n̂).
    The recorded mean door rate is H_mean·ξ = 1/√3 (M2).  The delivered
    inflow speed at the coherence scale is v = H_fast·ξ, i.e.
    Mach = v/c_s = (H_fast/H_mean)/(√3·c_s).  Compared against the rebound
    toy's tested envelope (inflow up to Mach 3).

J2  CAUSAL CONSISTENCY: the interval's natural duration is the rebound turn
    time (~1 t_heal, 1D verified).  M4 requires the interval to hold at
    least δ·R_H/6 = 0.0427·δ t_heal for door contrast δ.  Self-consistency
    window: δ ≲ t_turn/0.0427 ≈ 23.  Larger contrasts (collapsed cores) are
    the separately-recorded absorbing-boundary ledger, not this joint.

J3  PLANARITY: the quasi-1D geometry of the rebound toy is justified only if
    the squeeze is strongly anisotropic at crossing.  The billiard's three
    axis drops at first crossing give the transverse-to-fast scale ratios
    directly.

GRADE RULE
  Joints computed from recorded anchors; open items named; nothing promoted.
"""
from __future__ import annotations

import math

import numpy as np

D_OMEGA_MEAN_DOOR = 18.9
DROP_DOOR = 6.3
WALL_SPEED = 0.5
D0 = 1.0
C_S = math.sqrt(3.0 / 137.036)
T_TURN_1D = 1.0                # verified 1D rebound turn time, t_heal units
HOLD_COEFF = 0.0427            # M4: hold >= this * delta, t_heal units

AXES = [np.array([math.cos(a), math.sin(a)])
        for a in (0.0, 2 * math.pi / 3, 4 * math.pi / 3)]


def evolve_to_crossing(theta0: float, d0: float = D0):
    beta = np.zeros(2)
    vel = np.array([math.cos(theta0), math.sin(theta0)])
    omega = 0.0
    dOm = 1e-3
    while omega < D_OMEGA_MEAN_DOOR:
        omega += dOm
        beta = beta + vel * dOm
        d_wall = d0 + WALL_SPEED * omega
        for nhat in AXES:
            if beta @ nhat > d_wall and vel @ nhat > WALL_SPEED:
                vel = vel - 2 * ((vel @ nhat) - WALL_SPEED) * nhat
                vel = vel / np.linalg.norm(vel)
        drops = np.array([omega / 3.0 - (beta @ nhat) for nhat in AXES])
        if drops.max() >= DROP_DOOR:
            i_fast = int(np.argmax(drops))
            rate_fast = 1.0 / 3.0 - float(vel @ AXES[i_fast])
            return drops, rate_fast
    raise RuntimeError("no crossing before mean door")


def main() -> None:
    print("=" * 78)
    print("Task 4 — the squeeze-to-interval handoff: three joints, computed")
    print("=" * 78)

    print("\nJ1+J3 per launch angle: delivery Mach and planarity at first crossing")
    print("   θ₀      H_fast/H_mean   Mach = v/c_s   axis ratios ℓ_mid/ℓ_fast, ℓ_slow/ℓ_fast")
    machs, ratios = [], []
    for deg in (7, 23, 41, 59, 77, 95, 113, 131):
        drops, rate = evolve_to_crossing(math.radians(deg))
        hf = 3.0 * rate
        mach = hf / (math.sqrt(3.0) * C_S)
        d_sorted = np.sort(drops)[::-1]
        r_mid = math.exp(d_sorted[0] - d_sorted[1])
        r_slow = math.exp(d_sorted[0] - d_sorted[2])
        machs.append(mach)
        ratios.append((r_mid, r_slow))
        print(f"   {deg:4d}°      {hf:6.2f}        {mach:6.1f}          "
              f"{r_mid:8.1f}, {r_slow:10.1f}")

    print(f"\nJ1 verdict: delivered inflow Mach {min(machs):.1f}–{max(machs):.1f}."
          f"  The rebound toy's tested")
    print("   envelope reaches Mach 3 — the delivery EXCEEDS the tested range by")
    print("   ~5×. The toy's mechanism (repulsive-interaction rebound) has no")
    print("   known velocity ceiling, but the honest statement is: the verified")
    print("   response covers the low end of the delivered window; the high end")
    print("   needs the toy extended. NOT covered ≠ contradicted — a gap, named.")

    delta_max = T_TURN_1D / HOLD_COEFF
    print(f"\nJ2 verdict: rebound duration ~{T_TURN_1D:.0f} t_heal vs required hold")
    print(f"   0.0427·δ t_heal ⟹ causally self-consistent for door contrasts")
    print(f"   δ ≲ {delta_max:.0f}. Smooth-door contrasts (order unity to tens) fit inside;")
    print("   collapsed-core contrasts are the separate absorbing-boundary ledger.")

    print(f"\nJ3 verdict: transverse axes are {min(r[0] for r in ratios):.0f}–"
          f"{max(r[1] for r in ratios):.0f}× larger than the fast axis at")
    print("   crossing — the compression is planar to 2.5–3.5 orders of magnitude.")
    print("   The quasi-1D geometry of the rebound toy is justified at the door.")

    print("\nOPEN, NAMED (the joints do not cover):")
    print("   * transverse dynamics during the rebound (the toy holds them static);")
    print("   * the wall between a rebounding pocket and a still-contracting")
    print("     metric-on exterior (M4's boundary problem, unresolved);")
    print("   * whether one pocket's outflow re-steepens its neighbors (cascade")
    print("     sequencing — unwritten);")
    print("   * the Standard-Model sector's crossing (task #14).")
    print("\nGRADE: the handoff is now three computed joints + four named opens.")
    print("   Consistent where tested; one delivery-envelope gap to close in the")
    print("   toy. Nothing promoted.")
    print("=" * 78)

    assert 3.0 < min(machs) and max(machs) < 30.0
    assert delta_max > 20.0
    assert all(r[0] > 5.0 for r in ratios)


if __name__ == "__main__":
    main()
