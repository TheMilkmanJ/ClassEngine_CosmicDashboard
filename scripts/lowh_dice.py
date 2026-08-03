"""lowh_dice — task #36: the release dice across the physical hierarchy (2026-07-27).

HIERARCHY CORRECTED 2026-07-28: the physical point is h₀ ≈ 1.0, not the
0.1 this docstring first assumed.  The authority is the misalignment
abundance closure in `genesis_solver_B1.py` (release at H = m, which
returns the corpus's canonical onset 1 + z = 4.03×10⁷): Ψ₀ = 5.03×10¹⁶
GeV, so h₀ = λΨ₀²/m² = 1.01.  The grid below spans {0.03, 0.1, 0.3,
1.0}, so the physical point IS covered — read the h = 1.0 rows as the
standing ones.  At h = 1.0: P(f_amp > 0.2) = 71–100% by tilt, medians
0.42–0.76, and zero quiet draws.  The no-quiet-branch conclusion holds
at every h on the grid; the tight-ensemble conclusion belongs to the
h ≤ 0.3 rows only.

REFINED 2026-07-28 (`scripts/quiet_branch_fine_search.py`): re-run at 56
angles per tilt — 4x this grid's resolution — the quiet branch is still
empty, so the absence is a property of the map and not of the sampling.
But state the margin, because "zero draws" hides it: the closest
approach falls steeply with tilt, 20.4x -> 5.9x -> 1.6x the quiet
threshold across r_t = 0.3, 0.6, 0.9.  At the steepest tilt the nearest
draw is f_amp = 0.031 against a 0.02 threshold.  The defensible claim is
"no quiet draw, by 1.6x at the worst tilt on the grid" — not that the
branch cannot be reached.

WHAT THIS RUNS
  Room 1's summit dice, rebuilt to its own conventions and pointed at the
  regime the standing era actually selects (h₀ ≈ 1.0 from the abundance
  closure, seven decades below the era-bound target).

  The instrument (room's spec, ~lines 364-412): seamless integration of the
  complex field through frozen era → release → late oscillations in the
  radiation background; V/m²Ψ₀² = |x|² + h(|x|⁴ + r_t·Re(x⁴)) (Z₄ tilt at
  quartic level, diluting as the quartic redshifts — the room's "tilt
  diluting" clause); frozen release at t₀ = 0.01/√h from rest at R = 1,
  angle θ₀; dense θ₀ dice over the fundamental domain [0.05, π/4 − 0.05]
  (14 angles); per-universe readout f_rot = the late-time charge fraction
  (a³-weighted; U(1) restores once the tilt dies, so comoving charge
  conserves), f_amp = 1 − f_rot, ε = √f_amp.

VALIDATION LEG (runs first; gates everything)
  h = 300, r_t = 0.6 — the room's own booked row: median f_amp ≈ 0.55,
  range ≈ [0.07, 0.93], P(f_amp > 0.2) = 86%. The rebuild must land the
  median within ±0.15 and the exceedance within ±15 points, or nothing
  downstream is quoted (conventions differ → fix before grading).

THE PHYSICAL GRID
  h ∈ {0.03, 0.1, 0.3, 1} × r_t ∈ {0.3, 0.6, 0.9}, 14 angles each.
  THE QUESTION: does any ringing survive at h₀ ~ 0.1 — and does the quiet
  branch (f_rot > 0.98) exist at all where the torque is a 10% correction?
  STAKES (A4a/A5a binding): the granule ε-meter is the only ε readout.
  Expectation stated before running (the fork discipline): rest-release
  with weak quartic torque ⟹ little libration→rotation conversion ⟹
  f_amp high everywhere and the dice nearly deterministic. If instead the
  frozen-era drift or a resonance converts efficiently at low h, that is
  the finding — report exactly what lands.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import solve_ivp

ANGLES = [0.05 + i * (math.pi / 4 - 0.10) / 13.0 for i in range(14)]
T_LATE = 1500.0
AVG_FROM = 1000.0


def rhs(t, y, h, rt):
    u, v, du, dv = y
    H = 0.5 / t
    r2 = u * u + v * v
    # complex EOM ẍ + 3Hẋ + ∂V/∂x* = 0, and ∂V/∂x* = ½(∂V/∂u + i∂V/∂v):
    # the ½ makes the mass-term oscillator ω = 1 exactly (the rotor/librator
    # calibration asserts it — v1 omitted the ½, ω = √2, rotor limit 0.89,
    # caught by the calibration's own assert before anything was quoted).
    # dV/du with V = r² + h(r⁴ + rt·Re(x⁴)); Re(x⁴) = u⁴ − 6u²v² + v⁴
    Vu = 2 * u + h * (4 * r2 * u + rt * (4 * u ** 3 - 12 * u * v * v))
    Vv = 2 * v + h * (4 * r2 * v + rt * (4 * v ** 3 - 12 * u * u * v))
    return [du, dv, -3 * H * du - 0.5 * Vu, -3 * H * dv - 0.5 * Vv]


def universe(theta0: float, h: float, rt: float) -> float:
    """Returns f_rot (late-time charge fraction) for one draw."""
    t0 = 0.01 / math.sqrt(h)
    y0 = [math.cos(theta0), math.sin(theta0), 0.0, 0.0]
    sol = solve_ivp(rhs, (t0, T_LATE), y0, args=(h, rt), method="DOP853",
                    rtol=1e-9, atol=1e-12, dense_output=False,
                    t_eval=np.linspace(AVG_FROM, T_LATE, 4000))
    u, v, du, dv = sol.y
    Q = np.abs(u * dv - v * du)                  # |Im(x* ẋ)|
    E = du ** 2 + dv ** 2 + u ** 2 + v ** 2      # mass-dominated late energy
    f_rot = float(np.mean(2.0 * Q / np.maximum(E, 1e-300)))
    return min(max(f_rot, 0.0), 1.0)


def calibrate() -> None:
    """Pure-rotor and pure-librator limits must return 1 and 0."""
    t0, tl = 50.0, 300.0
    sol = solve_ivp(rhs, (t0, tl), [1e-3, 0, 0, 1e-3], args=(0.0, 0.0),
                    method="DOP853", rtol=1e-10, atol=1e-14,
                    t_eval=np.linspace(tl - 50, tl, 500))
    u, v, du, dv = sol.y
    fr = np.mean(2 * np.abs(u * dv - v * du) / (du**2 + dv**2 + u**2 + v**2))
    assert abs(fr - 1.0) < 0.02, f"rotor limit failed: {fr}"
    sol = solve_ivp(rhs, (t0, tl), [1e-3, 0, 0, 0], args=(0.0, 0.0),
                    method="DOP853", rtol=1e-10, atol=1e-14,
                    t_eval=np.linspace(tl - 50, tl, 500))
    u, v, du, dv = sol.y
    fr = np.mean(2 * np.abs(u * dv - v * du) / (du**2 + dv**2 + u**2 + v**2))
    assert fr < 0.02, f"librator limit failed: {fr}"
    print("   calibration: rotor → 1.00, librator → 0.00 ✓")


def row(h: float, rt: float):
    fas = []
    for th in ANGLES:
        fr = universe(th, h, rt)
        fas.append(1.0 - fr)
    fas_a = np.array(fas)
    return (float(np.median(fas_a)), float(fas_a.min()), float(fas_a.max()),
            float(np.mean(fas_a > 0.2)), fas)


def main() -> None:
    print("=" * 78)
    print("The dice at the physical hierarchy — low-h regime, validation-gated")
    print("=" * 78)
    calibrate()

    print("\nVALIDATION (h = 300, r_t = 0.6; booked: median 0.55, "
          "range [0.07, 0.93], P = 86%):")
    med, lo, hi, p, _ = row(300.0, 0.6)
    ok = abs(med - 0.55) <= 0.15 and abs(p - 0.86) <= 0.15
    print(f"   rebuild: median {med:.2f}, range [{lo:.2f}, {hi:.2f}], "
          f"P(f_amp>0.2) = {100*p:.0f}%   → {'GATE PASSES' if ok else 'GATE FAILS — nothing below is quoted'}")
    if not ok:
        print("   (convention mismatch with the room's instrument; fix first.)")
        return

    print("\nTHE PHYSICAL GRID (f_amp per row; quiet branch = any f_rot > 0.98"
          " ⟺ f_amp < 0.02):")
    print("   h      r_t   median   min    max    P(>0.2)  quiet draws")
    quiet_total = 0
    for h in (0.03, 0.1, 0.3, 1.0):
        for rt in (0.3, 0.6, 0.9):
            med, lo, hi, p, fas = row(h, rt)
            nq = sum(1 for f in fas if f < 0.02)
            quiet_total += nq
            print(f"   {h:<5}  {rt:.1f}   {med:.3f}   {lo:.3f}  {hi:.3f}"
                  f"   {100*p:3.0f}%     {nq}/14")

    print("\nVERDICT:")
    if quiet_total == 0:
        print("   NO DRAW REACHES THE QUIET BRANCH at the physical hierarchy —")
        print("   every draw rings, at every tilt, and the granule ε-meter")
        print("   keeps its readout. This survives a 4× angular refinement")
        print("   (quiet_branch_fine_search.py), so it is a property of the")
        print("   map rather than of the sampling. It is a MEASURED MARGIN,")
        print("   not a structural floor: the margin narrows steeply with")
        print("   tilt and reaches 1.6× the threshold at r_t = 0.9. Report")
        print("   the f_amp levels exactly; ε = √f_amp per row above.")
    else:
        print(f"   {quiet_total} quiet draws found at low h — the conversion")
        print("   mechanism survives where the weak-torque expectation said it")
        print("   could not. The expectation was wrong; report exactly, and the")
        print("   quiet-branch probability at the physical h becomes the number.")
    print("=" * 78)


if __name__ == "__main__":
    main()
