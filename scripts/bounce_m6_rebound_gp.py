"""bounce_m6_rebound_gp — spherical rebound, ADAPTIVE integrator (v2, 2026-07-27).

HISTORY
  v1 (2026-07-26) FAILED its energy guard: fixed-step split-step lost the
  nonlinear phase once the implosion focused (dt·n_peak ≫ 1), violating energy
  conservation up to ~20×.  Its numbers were artifacts and were never quoted.
  v2 rebuilds the integrator: the timestep adapts to hold the nonlinear phase
  per step below φ_tol at the instantaneous density maximum (dt quantized to
  dt_max/2^k so the Crank–Nicolson operator rebuilds only on level changes),
  with an energy monitor and a grid/tolerance refinement pair for convergence.

QUESTION (unchanged)
  Does the medium's own repulsive field equation turn a spherical implosion
  around, with how much geometric focusing amplification (the honest version
  of the compression free parameter), on what timescale, with what energy
  partition?  Spherical focusing is the open question the verified 1D run
  could not address.

MODEL
  Healing units: i ∂_t ψ = −½∇²ψ + (|ψ|² − 1)ψ, u = rψ, Dirichlet u(0) = 0,
  u(L) = L.  IC: n = 1 + A·sech²(r/R), v = −v₀(r/R)e^{−(r/R)²/2}, R = 20ξ.
  FENCES: nonrelativistic; no emergent-gravity backreaction inside the
  interval (the metric-exit hypothesis, explicit); spherical symmetry.
  t_heal = ξ/c_s ≈ 15.7 days at the recorded ξ = 402 AU, c_s = √(3α).

GRADE RULE
  Numbers are quoted ONLY if energy is conserved to ≤2% and the refinement
  pair agrees on n_peak to ≤15%.  Otherwise the run reports itself unconverged.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.linalg import solve_banded

L = 200.0
N = 8000
DT_MAX = 2.0e-3
PHI_TOL = 0.05
T_MAX = 60.0
R_BLOB = 20.0
PROBE = 60.0
MAX_STEPS = 1_500_000

XI_SEC = 402.0 * 1.496e11 / (math.sqrt(3.0 / 137.036) * 2.99792458e8)


def cn_factors(dr: float, n: int, dt: float):
    alpha = 1j * dt / (4.0 * dr * dr)
    ab = np.zeros((3, n), dtype=complex)
    ab[0, 1:] = -alpha
    ab[1, :] = 1.0 + 2.0 * alpha
    ab[2, :-1] = -alpha
    return ab, alpha


def rhs_apply(u, alpha, u_left, u_right):
    out = (1.0 - 2.0 * alpha) * u
    out[1:] += alpha * u[:-1]
    out[:-1] += alpha * u[1:]
    out[0] += alpha * u_left
    out[-1] += alpha * u_right
    return out


def energies(r, psi, dr):
    n = np.abs(psi) ** 2
    sq = np.sqrt(np.maximum(n, 1e-300))
    dpsi = np.gradient(psi, dr)
    dsq = np.gradient(sq, dr)
    j = np.imag(np.conj(psi) * dpsi)
    v = j / np.maximum(n, 1e-12)
    w = 4.0 * math.pi * r * r * dr
    return (0.5 * np.sum(n * v * v * w),
            0.5 * np.sum(dsq * dsq * w),
            0.5 * np.sum((n - 1.0) ** 2 * w))


def run(A, v0, n_grid=N, phi_tol=PHI_TOL):
    dr = L / n_grid
    r = np.arange(1, n_grid) * dr
    nprof = 1.0 + A / np.cosh(r / R_BLOB) ** 2
    v = -v0 * (r / R_BLOB) * np.exp(-0.5 * (r / R_BLOB) ** 2)
    theta = np.concatenate([[0.0], np.cumsum(0.5 * (v[1:] + v[:-1]) * dr)])
    u = r * np.sqrt(nprof) * np.exp(1j * theta)
    ip = int(PROBE / dr) - 1

    level = 0
    ab, alpha = cn_factors(dr, n_grid - 1, DT_MAX)
    e0 = sum(energies(r, u / r, dr))
    t = 0.0
    steps = 0
    nmax_hist, t_hist = [], []
    t_peak, n_peak = 0.0, 0.0
    flux_late = []
    next_sample = 0.0
    while t < T_MAX and steps < MAX_STEPS:
        dens = np.abs(u / r) ** 2
        nm = float(dens.max())
        want = 0 if nm <= 1.0 else max(0, math.ceil(math.log2(DT_MAX * (nm - 1.0) / phi_tol)) if DT_MAX * (nm - 1.0) > phi_tol else 0)
        if want != level:
            level = want
            ab, alpha = cn_factors(dr, n_grid - 1, DT_MAX / 2 ** level)
        dt = DT_MAX / 2 ** level
        u = u * np.exp(-0.5j * dt * (dens - 1.0))
        u = solve_banded((1, 1), ab, rhs_apply(u, alpha, 0.0, L))
        dens = np.abs(u / r) ** 2
        u = u * np.exp(-0.5j * dt * (dens - 1.0))
        t += dt
        steps += 1
        if t >= next_sample:
            next_sample += 0.25
            nm = float(dens.max())
            nmax_hist.append(nm)
            t_hist.append(t)
            if nm > n_peak:
                n_peak, t_peak = nm, t
            if t > t_peak + 5.0 and nm < 0.2 * n_peak and t > 10.0:
                break
            if t > t_peak + 3.0:
                psi = u / r
                dpsi = np.gradient(psi, dr)
                flux_late.append(float(np.imag(np.conj(psi[ip]) * dpsi[ip]) * r[ip] ** 2))
    psi = u / r
    e_fl, e_qp, e_in = energies(r, psi, dr)
    econs = abs((e_fl + e_qp + e_in) - e0) / e0
    return {
        "A": A, "v0": v0, "n_init": 1.0 + A, "n_peak": n_peak, "t_peak": t_peak,
        "t_end": t, "n_end": float(np.abs(psi).max() ** 2), "steps": steps,
        "econs": econs, "e0": e0, "e_flow": e_fl, "e_qp": e_qp, "e_int": e_in,
        "outflux": float(np.mean(flux_late)) if flux_late else 0.0,
    }


def main() -> None:
    print("=" * 78)
    print("M6 v2 — spherical rebound with the adaptive integrator")
    print("=" * 78)
    print(f"   φ_tol = {PHI_TOL}, dt adaptive from {DT_MAX} downward; "
          f"t_heal ≈ {XI_SEC/86400:.1f} days")
    print()
    print("   A    v₀   n_init→n_peak (focus ×)   t_peak[t_heal|days]  E-cons   steps    outflux")
    results = []
    for A, v0 in ((5.0, 1.0), (20.0, 1.0), (50.0, 1.0), (20.0, 3.0)):
        res = run(A, v0)
        results.append(res)
        print(f"   {A:3.0f}  {v0:3.0f}   {res['n_init']:5.1f} → {res['n_peak']:8.1f}"
              f" (×{res['n_peak']/res['n_init']:6.2f})   {res['t_peak']:5.1f} | "
              f"{res['t_peak']*XI_SEC/86400:6.1f}   {100*res['econs']:5.2f}%  "
              f"{res['steps']:7d}   {'+' if res['outflux']>0 else '−'}")
    print("\n   Convergence pair (A=20, v₀=1): refine grid ×1.5 and φ_tol ×0.5")
    ref = run(20.0, 1.0, n_grid=12000, phi_tol=0.025)
    base = results[1]
    dev = abs(ref["n_peak"] - base["n_peak"]) / base["n_peak"]
    print(f"   base n_peak = {base['n_peak']:.1f}, refined = {ref['n_peak']:.1f} "
          f"→ deviation {100*dev:.1f}%  (E-cons refined: {100*ref['econs']:.2f}%)")
    print("\n   Energy partition at end (fraction of initial excess):")
    for res in results:
        tot = res["e_flow"] + res["e_qp"] + res["e_int"]
        print(f"   A={res['A']:3.0f} v₀={res['v0']:.0f}:  flow {res['e_flow']/tot:.2f}  "
              f"quantum-pressure {res['e_qp']/tot:.2f}  interaction {res['e_int']/tot:.2f}")

    converged = all(r["econs"] < 0.02 for r in results) and ref["econs"] < 0.02 and dev < 0.15
    print("\nVERDICT")
    if converged:
        print("  CONVERGED (energy ≤2% everywhere, refinement pair ≤15%).")
        print("  1. The spherical implosion TURNS in every case — the dynamical")
        print("     re-entry survives the geometry that broke the v1 integrator.")
        print("  2. The geometric focusing amplification n_peak/n_init is the")
        print("     table's third column — the honest, computed version of the")
        print("     compression free parameter, now with conserved energy.")
        print("  3. Post-turn probe flux and the partition are as tabulated;")
        print("     cosmological matching (F-A1/F-A3) remains the open assembly.")
    else:
        print("  NOT CONVERGED — the run reports itself unusable; no numbers")
        print("  from this script may be quoted. See the guard values above.")
    print("=" * 78)

    assert converged, "unconverged — do not quote"
    for res in results:
        assert res["n_peak"] < res["n_init"] * 400.0
        assert res["n_end"] < 0.5 * res["n_peak"]


if __name__ == "__main__":
    main()
