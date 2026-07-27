"""rectification_ramp_integral — #104 stage 6: the careful pass's magnitude piece, run through the real shutoff (2026-07-27).

WHAT STAGE 5 LEFT
  The AC junction at the sphaleron era winds at θ̇/H = 2.4×10⁶; the naive
  rectified transmission R ~ H/θ̇ = 4.1×10⁻⁷ sits a factor ~122 below the
  need (~5×10⁻⁵ from the reservoir's 1.9×10⁴ headroom), inside the
  pre-committed "within 10²" boundary — neither pass nor fail.  The spec
  said: the sphaleron-window integration and the mechanism's own O(1)s
  are exactly the size of the gap.

THE PIECE THIS COMPUTES (well-posed, recorded inputs, no mechanism choice)
  The net transfer of a SYMMETRIC sinusoidal junction is an oscillatory
  integral against the sphaleron weight's envelope.  For a smooth
  (Hubble-scale) envelope the boundary suppression is H/θ̇ — the naive
  number.  But the actual envelope is the lattice-measured shutoff:
  Γ_sph ∝ exp(+0.83·T/GeV) through the crossover (d'Onofrio–Rummukainen–
  Tranberg, arXiv:1404.3565; slope 0.83 ± 0.01 /GeV, freeze-out
  T* = 131.7 GeV where Γ = H), an e-width w = 1/0.83 = 1.2 GeV — a
  FRACTIONAL width δ = w/T* = 0.92%.  A stationary-envelope integral
  suppresses by the phase wound across the ENVELOPE's own width:
      R = 1/ΔΦ_ramp = H/(θ̇·δ)  — an enhancement of 1/δ ≈ 109 over naive.
  This script does it numerically, not by the asymptotic formula: the
  full weighted integral over the window with three envelope models
  (pure exponential ramp; Γ/(Γ+H) interpolation; integrated-processing
  1−exp(−Γ/H)), a scan over the genesis phase φ (the draw), and the
  φ-averages (⟨|·|⟩ → the 2/π grammar's third appearance — the spec's
  own watch).

WHAT IT DOES NOT DO (honest scope)
  The junction's current-phase relation is taken sinusoidal (the DC-
  Josephson template as recorded); a skewed relation adds harmonics and
  O(1)s.  The SIGN (which φ the genesis drew, and the handedness lock)
  remains T14 link 5's object, untouched here.  This is the magnitude's
  careful pass: does the recorded shutoff close the 122?
"""
from __future__ import annotations

import math
import numpy as np

M_EV = 2.24e-20
T_ON_EV = 9.5e3
T_SPH_GEV = 131.7
SLOPE_PER_GEV = 0.83
M_PL_GEV = 1.22e19
G_STAR = 106.75
NEED = 5.0e-5


def H_gev(T):
    return 1.66 * math.sqrt(G_STAR) * T * T / M_PL_GEV


def theta_dot_ev(T_gev):
    return M_EV * (T_gev * 1e9 / T_ON_EV) ** 3


def main() -> None:
    print("=" * 78)
    print("The rectification's magnitude through the real shutoff — #104 stage 6")
    print("=" * 78)

    H_star = H_gev(T_SPH_GEV)
    td_star = theta_dot_ev(T_SPH_GEV) / 1e9          # GeV
    naive = H_star / td_star
    delta = 1.0 / (SLOPE_PER_GEV * T_SPH_GEV)
    print(f"\n   recorded: θ̇(T*) = {td_star*1e9:.3g} eV, H(T*) = {H_star*1e9:.3g} eV,"
          f" θ̇/H = {td_star/H_star:.3g}")
    print(f"   naive rectified R = H/θ̇ = {naive:.3g}  (the stage-5 boundary number)")
    print(f"   shutoff ramp: slope {SLOPE_PER_GEV}/GeV → e-width {1/SLOPE_PER_GEV:.2f} GeV,"
          f" fractional δ = {100*delta:.2f}%")
    print(f"   asymptotic prediction: R = H/(θ̇δ) = {naive/delta:.3g}"
          f"   (enhancement 1/δ = {1/delta:.0f})")

    # numerical: work in x = T/GeV over the window [T*−15w, T_high]; phase
    # Δθ(x) = ∫ θ̇ dt = ∫_x^{x_hi} θ̇/(H·x') dx' (dt = −dT/(HT), radiation)
    w = 1.0 / SLOPE_PER_GEV
    x_lo, x_hi = T_SPH_GEV - 15 * w, T_SPH_GEV + 60 * w
    N = 4_000_000
    x = np.linspace(x_lo, x_hi, N)
    dx = x[1] - x[0]
    td = M_EV * (x * 1e9 / T_ON_EV) ** 3 / 1e9
    Hx = 1.66 * math.sqrt(G_STAR) * x * x / M_PL_GEV
    dphase = td / (Hx * x)                       # dΔθ/dT, 1/GeV
    phase = np.cumsum(dphase[::-1])[::-1] * dx   # Δθ measured from x_hi down
    gam_ratio = np.exp(SLOPE_PER_GEV * (x - T_SPH_GEV))   # Γ/H at T (Γ=H at T*)

    envelopes = {
        "exponential ramp (Γ/H, capped 1)": np.minimum(gam_ratio, 1.0),
        "interpolation Γ/(Γ+H)": gam_ratio / (gam_ratio + 1.0),
        "processing 1−exp(−Γ/H)": 1.0 - np.exp(-np.minimum(gam_ratio, 50.0)),
    }
    print("\n   numerical R(φ) over the genesis-phase draw (normalized by the")
    print("   DC-equivalent ∫f_sph dT — the transfer a non-winding junction gives):")
    print(f"   {'envelope':<34} ⟨|R|⟩_φ      max_φ|R|    ⟨|R|⟩/naive")
    results = {}
    for name, f in envelopes.items():
        dc = float(np.sum(f) * dx)
        vals = []
        for phi in np.linspace(0, 2 * math.pi, 24, endpoint=False):
            osc = float(np.sum(f * np.sin(phase + phi)) * dx)
            vals.append(abs(osc) / dc)
        vals = np.array(vals)
        results[name] = (float(vals.mean()), float(vals.max()))
        print(f"   {name:<34} {vals.mean():.3g}   {vals.max():.3g}   "
              f"{vals.mean()/naive:8.0f}×")

    mean_R = results["interpolation Γ/(Γ+H)"][0]
    print(f"\n   the 2/π watch: ⟨|cos φ|⟩ = 2/π = {2/math.pi:.3f}; measured "
          f"⟨|R|⟩/max|R| = {mean_R/results['interpolation Γ/(Γ+H)'][1]:.3f}")
    print(f"\n   against the need ({NEED:.1e}):")
    for name, (mR, xR) in results.items():
        print(f"   {name:<34} ⟨|R|⟩/need = {mR/NEED:.2f}")

    # v2 DIAGNOSIS (the run's own result refused v1's asymptotic): the
    # measured R matched neither H/(θ̇δ) (v1's prediction — a NORMALIZATION
    # ERROR: 1/(Ωw) is per-ramp, the need is per-WINDOW) nor pure physics —
    # it matched the artificial hard edge at x_hi (boundary term
    # 1/Φ'(x_hi) over the window). Demonstrated here: hard-edge R scales
    # with the cutoff's own 1/Φ'; a smooth taper collapses the transfer by
    # orders. The physical envelope is smooth everywhere (the lattice ramp
    # is analytic; the crossover matching is C¹-smooth on GeV widths; the
    # genesis onset sits at enormous Φ'), so the SYMMETRIC junction's net
    # transfer is boundary-artifact-free and ADIABATICALLY NULL.
    print("\n   v2 — edge-artifact demonstration (hard cutoff vs smooth taper):")
    f_base = gam_ratio / (gam_ratio + 1.0)
    for frac, label in ((0.5, "hard edge at x_hi/2"), (1.0, "hard edge at x_hi")):
        n_cut = int(N * frac) - 1
        dc = float(np.sum(f_base[:n_cut]) * dx)
        osc = float(np.sum(f_base[:n_cut] * np.sin(phase[:n_cut])) * dx)
        pred = 1.0 / (dphase[n_cut] * dc)
        print(f"     {label:<22} |R| = {abs(osc)/dc:.3g}   "
              f"(edge prediction 1/(Φ'·window) = {pred:.3g})")
    taper = np.ones(N)
    t_w = 10 * w
    mask = x > (x_hi - 3 * t_w)
    taper[mask] = np.exp(-((x[mask] - (x_hi - 3 * t_w)) / t_w) ** 2)
    f_t = f_base * taper
    dc_t = float(np.sum(f_t) * dx)
    osc_t = float(np.sum(f_t * np.sin(phase)) * dx)
    print(f"     smooth taper (10w)     |R| = {abs(osc_t)/dc_t:.3g}   "
          f"(the adiabatic collapse)")

    m1_ev = 2.25e-3
    watch = m1_ev / (td_star * 1e9)
    print(f"\n   THE WATCH (flagged, not asserted): the junction's own symmetry")
    print(f"   breaker is the seat term's Majorana insertion m₁ = 2.25 meV —")
    print(f"   the object that makes the junction a DIODE (φ₀/anomalous-junction")
    print(f"   class), and m₁/θ̇(T*) = {watch:.3g} against the need {NEED:.1e}")
    print(f"   (ratio {watch/NEED:.2f}) — coincidence grade until the diode's")
    print(f"   efficiency is DERIVED from the seat term; owning computation:")
    print(f"   the φ₀-junction response, T14 link 5's rectifier, same object.")

    print("\nVERDICT (v2, the honest one):")
    print("   THE SYMMETRIC JUNCTION IS ADIABATICALLY DEAD: with the envelope")
    print("   smooth everywhere — and every physical feature is — the monotonic")
    print("   winding transfers exponentially little; the naive H/θ̇ was itself")
    print("   a hard-boundary artifact, and v1's ramp enhancement was a")
    print("   normalization error caught by this run. Stage 5's 'factor 122")
    print("   boundary' verdict is superseded in the DEAD direction for the")
    print("   symmetric channel: the magnitude rides ENTIRELY on the junction's")
    print("   symmetry-breaking (diode) structure — which is T14 link 5's one")
    print("   object, now carrying all four consumers with a named scale watch")
    print("   (m₁/θ̇ = 0.75× the need) to earn or kill.")
    print("=" * 78)


if __name__ == "__main__":
    main()
