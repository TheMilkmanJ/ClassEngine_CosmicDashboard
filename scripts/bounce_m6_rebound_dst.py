"""bounce_m6_rebound_dst — spherical rebound v3: the energy-clean scheme (2026-07-28).

HISTORY
  v1 (fixed-step) and v2 (adaptive CN/RK4 hybrid) both failed their own
  energy guards at focusing — every row unquotable (RP log §23 closed the
  O6 question on that basis, with the reopening condition "an energy-clean
  3D computation").  This is that computation's candidate: with u = rψ the
  spherical kinetic operator is a plain second derivative on a Dirichlet
  interval, which the sine transform diagonalizes EXACTLY — the kinetic
  step is unitary to machine precision, the potential step is a pointwise
  phase, and the linear background r is analytically invariant (∂_rr r = 0),
  so the split-step propagator has no secular energy drift mechanism.
  The timestep adapts to hold the nonlinear phase per step below φ_tol.

QUESTION, MODEL, GATES (unchanged from v2 — same physics, same honesty bar)
  i∂_t ψ = −½∇²ψ + (|ψ|²−1)ψ, spherical; u = rψ = r + w, w Dirichlet.
  IC: n = 1 + A·sech²(r/R), v = −v₀(r/R)e^{−(r/R)²/2}, R = 20ξ.
  Quotable ONLY if energy drift ≤ 2% and the refinement pair agrees on
  n_peak to ≤ 15%.  If clean rows land, the measured focusing F folds into
  the assembled timeline (task #5's recorded endpoint carries the bar
  F ≥ 10⁹; RP §22–23) — this run either reopens that endpoint or converts
  its caveat from "unresolved" to "measured".
"""
from __future__ import annotations

import math

import numpy as np
from scipy.fft import dst, idst

L = 200.0
N = 8000
DT_MAX = 2.0e-3
PHI_TOL = 0.05
T_MAX = 60.0
R_BLOB = 20.0
MAX_STEPS = 3_000_000

dr = L / N
r_in = np.arange(1, N) * dr                    # interior points
k = np.pi * np.arange(1, N) / L                # sine-mode wavenumbers


def initial(A: float, v0: float):
    n = 1.0 + A / np.cosh(r_in / R_BLOB) ** 2
    vel = -v0 * (r_in / R_BLOB) * np.exp(-((r_in / R_BLOB) ** 2) / 2.0)
    phase = np.concatenate(([0.0], np.cumsum(0.5 * (vel[1:] + vel[:-1]) * dr)))
    psi = np.sqrt(n) * np.exp(1j * phase)
    return r_in * psi                           # u on interior


def energy(u: np.ndarray) -> float:
    psi = np.empty(N + 1, dtype=complex)
    psi[1:N] = u / r_in
    psi[0] = psi[1]                             # regular at origin
    psi[N] = 1.0
    rfull = np.arange(N + 1) * dr
    dpsi = np.gradient(psi, dr)
    dens = 0.5 * np.abs(dpsi) ** 2 + 0.5 * (np.abs(psi) ** 2 - 1.0) ** 2
    return float(np.trapezoid(dens * rfull ** 2, dx=dr))


def evolve(A: float, v0: float, n_grid: int = N, dt_max: float = DT_MAX):
    global dr, r_in, k
    dr_l = L / n_grid
    r_l = np.arange(1, n_grid) * dr_l
    k_l = np.pi * np.arange(1, n_grid) / L

    n0 = 1.0 + A / np.cosh(r_l / R_BLOB) ** 2
    vel = -v0 * (r_l / R_BLOB) * np.exp(-((r_l / R_BLOB) ** 2) / 2.0)
    phase = np.concatenate(([0.0], np.cumsum(0.5 * (vel[1:] + vel[:-1]) * dr_l)))
    u = r_l * np.sqrt(n0) * np.exp(1j * phase)

    def E(uv):
        psi = uv / r_l
        dpsi = np.gradient(np.concatenate(([psi[0]], psi, [1.0])), dr_l)[1:-1]
        dens = 0.5 * np.abs(dpsi) ** 2 + 0.5 * (np.abs(psi) ** 2 - 1.0) ** 2
        return float(np.trapezoid(dens * r_l ** 2, dx=dr_l))

    e0 = E(u)
    n_peak, t_peak = 1.0 + A, 0.0
    t, steps = 0.0, 0
    while t < T_MAX and steps < MAX_STEPS:
        psi2 = np.abs(u / r_l) ** 2
        vmax = float(np.max(np.abs(psi2 - 1.0)))
        dt = min(dt_max, PHI_TOL / max(vmax, 1e-12))
        # Strang: half potential, full kinetic (exact in sine basis), half potential
        # scipy.fft.idst is the NORMALIZED inverse — no extra division.  (v3's
        # first launch divided by 2N again, shrinking the field each step; the
        # energy guard flagged 100% drift at once and nothing was quoted.)
        w = u * np.exp(-0.5j * dt * (psi2 - 1.0)) - r_l
        wh = dst(w.real, type=1) + 1j * dst(w.imag, type=1)
        wh *= np.exp(-0.5j * dt * k_l ** 2)
        w = idst(wh.real, type=1) + 1j * idst(wh.imag, type=1)
        u = w + r_l
        psi2 = np.abs(u / r_l) ** 2
        u *= np.exp(-0.5j * dt * (psi2 - 1.0))
        t += dt
        steps += 1
        m = float(np.max(np.abs(u / r_l) ** 2))
        if m > n_peak:
            n_peak, t_peak = m, t
    drift = abs(E(u) - e0) / abs(e0)
    return n_peak, t_peak, drift, steps, t


def main() -> None:
    print("=" * 78)
    print("Spherical rebound v3 — split-step sine-transform (energy-clean scheme)")
    print("=" * 78)
    print(f"\n   grid N = {N}, L = {L}, φ_tol = {PHI_TOL}; gates: energy ≤2%, pair ≤15%")
    print("\n   A    v₀   n_init → n_peak (focus ×)   t_peak   E-drift    steps")
    rows = {}
    for A, v0 in ((5, 1.0), (20, 1.0), (50, 1.0), (20, 3.0)):
        npk, tpk, drift, steps, t_end = evolve(A, v0)
        focus = npk / (1.0 + A)
        rows[(A, v0)] = (npk, focus, drift)
        flag = "QUOTABLE" if drift <= 0.02 else "unquotable"
        print(f"   {A:3d}  {v0:3.0f}   {1+A:5.1f} → {npk:9.1f} (×{focus:8.2f})"
              f"   {tpk:6.1f}   {100*drift:7.3f}%   {steps}  [{flag}]")

    print("\n   refinement pair (A=20, v₀=1): grid ×1.5, dt_max ×0.5")
    npk_r, tpk_r, drift_r, steps_r, _ = evolve(20, 1.0, n_grid=12000,
                                               dt_max=DT_MAX / 2)
    base = rows[(20, 1.0)][0]
    pair = abs(npk_r - base) / base
    print(f"   refined: n_peak = {npk_r:.1f} (base {base:.1f}) — pair Δ = "
          f"{100*pair:.1f}%, E-drift {100*drift_r:.3f}%")

    clean = [f for (a, v), (npk, f, d) in rows.items() if d <= 0.02]
    print("\nVERDICT")
    if clean and pair <= 0.15 and drift_r <= 0.02:
        fmax = max(clean)
        print(f"   ENERGY-CLEAN ROWS LANDED — measured spherical focusing up to")
        print(f"   ×{fmax:.1f} at the quotability gates. Against the assembled")
        print(f"   timeline's bar (F ≥ 1e9 for O6 by compression): "
              f"{'BAR CLEARED — REOPEN §23' if fmax >= 1e9 else f'short by ×{1e9/fmax:.1e} — the §23 endpoint stands, its caveat upgraded from unresolved to MEASURED'}")
    else:
        print("   gates not met — report as-is; nothing quoted.")
    print("=" * 78)


if __name__ == "__main__":
    main()
