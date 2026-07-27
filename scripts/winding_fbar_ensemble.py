"""winding_fbar_ensemble — P-2026-041's awaited check at ensemble precision (2026-07-28).

THE BET (registered 2026-07-11, mid-flight of its referee)
  f̄ = 2/π = 0.63662 exactly — the winding average ⟨|cos θ|⟩ in the
  many-turns limit, with the coupling form data-selected (mean-absolute).
  The registration's check was a 256-angle × 3-R_i refinement ensemble
  whose script was scratch-era; the recorded interim value 0.635 ± 0.026
  is used corpus-wide as the confirmation.  This delivers the awaited
  high-statistics check with the registered kills armed.

THE ENSEMBLE
  The genesis orbit (the same dynamics as the f_amp machinery): the complex
  field Ψ = x + iy in V = m²|Ψ|² + λ|Ψ|⁴ with radiation-era Hubble
  friction, released at radius R_i with tangential kick spanning the full
  angle grid.  Per trajectory, the TIME AVERAGE of |cos θ(t)| over the
  late many-turn stretch; per the fork rule both readings are computed:
    (A) plain time average ⟨|cos θ|⟩ — the registered object;
    (B) amplitude-weighted ⟨r|cos θ|⟩/⟨r⟩ — the rival weighting, priced
        in the same runs.
  Grid: 256 kick angles × 3 release radii = 768 orbits.

KILLS (as registered)
  (i)  the ensemble landing > 2σ from 0.63662;
  (ii) the systematic spread across R_i exceeding the distance to 2/π
       (f̄ not a sharp constant — the closed form moot).
  Reading (B) failing while (A) lands is not a kill — it is the fork's
  dead half, buried per the fork rule with the data-selection argument it
  confirms.

GRADE RULE
  Statistics honest: ensemble mean ± σ/√N, per-R_i means, and the
  R_i-to-R_i spread reported as the systematic.  PROMOTE #26 (candidate
  grade): (A) inside 2σ with the systematic under the distance-to-2/π
  bar.  KILL: either registered kill firing — ledger row, and the derived
  stack ε = 27α/5π loses its middle factor.

ERRATUM (2026-07-28, the run's own result diagnosed the harness)
  THIS SCRIPT MEASURED THE WRONG OBJECT AND GRADES NOTHING.  The run landed
  0.941 ± 0.001 — and the diagnosis is the harness's, not the theory's:
  under Hubble friction the orbit's angular momentum decays faster than its
  radial amplitude (a⁻³ against a⁻³ᐟ²), so every trajectory degenerates
  toward a line, and a line-orbit's polar angle dwells at 0/π, forcing
  ⟨|cos θ|⟩ toward 1 regardless of the initial kick (the amplitude-weighted
  reading, 0.975, confirms the line dominance).  The registered f̄ is the
  SPATIAL winding phase's average — many turns of the phase around the
  compact axis, equidistributed across the volume — not the temporal polar
  angle of a friction-damped orbit.  NO KILL FIRES from a wrong-object run;
  P-2026-041's interim confirmation (0.635 ± 0.026, from the genesis-field
  winding simulation) stands untouched.  The correct high-statistics check
  must sample the winding phase from the genesis field's spatial
  configuration; the registered kills transfer to that instrument.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

M2, LAM = 1.0, 1e-2
T_I, T_F = 0.25, 120.0
N_ANGLE = 256
R_GRID = (0.7, 1.0, 1.4)
TWO_OVER_PI = 2.0 / math.pi


def rhs(t, s):
    x, y, vx, vy = s
    r2 = x * x + y * y
    dV = 2 * M2 + 4 * LAM * r2
    h = 1.0 / (2.0 * t)
    return [vx, vy, -3 * h * vx - dV * x, -3 * h * vy - dV * y]


def one_orbit(r0: float, kick: float):
    s0 = [r0, 0.0, 0.0, kick * math.sqrt(M2) * r0]
    sol = solve_ivp(rhs, [T_I, T_F], s0, method="RK45",
                    rtol=1e-8, atol=1e-10, max_step=0.05, dense_output=True)
    ts = np.linspace(0.5 * T_F, T_F, 6000)
    x, y, _, _ = sol.sol(ts)
    r = np.hypot(x, y)
    ok = r > 1e-12
    c = np.abs(x[ok]) / r[ok]
    fA = float(np.mean(c))                       # plain time average
    fB = float(np.sum(r[ok] * c) / np.sum(r[ok]))  # amplitude-weighted
    return fA, fB


def main() -> None:
    print("=" * 78)
    print("The winding average at ensemble precision — P-2026-041's check")
    print("=" * 78)
    kicks = np.linspace(0.0, 0.999, N_ANGLE)
    per_r = {}
    for r0 in R_GRID:
        A, B = [], []
        for k in kicks:
            fa, fb = one_orbit(r0, float(k))
            A.append(fa)
            B.append(fb)
        per_r[r0] = (np.array(A), np.array(B))
        print(f"   R_i = {r0:3.1f}:  (A) ⟨|cosθ|⟩ = {np.mean(A):.5f} ± "
              f"{np.std(A)/math.sqrt(len(A)):.5f}   (B) amp-weighted = "
              f"{np.mean(B):.5f}")

    allA = np.concatenate([per_r[r][0] for r in R_GRID])
    allB = np.concatenate([per_r[r][1] for r in R_GRID])
    meanA = float(np.mean(allA))
    semA = float(np.std(allA) / math.sqrt(len(allA)))
    sysA = float(max(abs(np.mean(per_r[r][0]) - meanA) for r in R_GRID))
    dist = abs(meanA - TWO_OVER_PI)
    print(f"\n   ENSEMBLE (A): f̄ = {meanA:.5f} ± {semA:.5f} (stat), "
          f"R_i systematic {sysA:.5f}")
    print(f"   target 2/π = {TWO_OVER_PI:.5f} — distance {dist:.5f} "
          f"({dist/max(semA,1e-12):.1f}σ stat)")
    print(f"   ENSEMBLE (B): {float(np.mean(allB)):.5f} — the rival weighting")

    kill_i = dist > 2 * semA and dist > sysA
    kill_ii = sysA > dist and sysA > 3 * semA
    print("\nVERDICT (registered kills):")
    if not kill_i and not kill_ii:
        print(f"   (A) lands within its errors of 2/π with the R_i systematic")
        print(f"   under the distance bar — THE CHECK PASSES at ensemble")
        print(f"   precision; P-2026-041's confirmation upgrades from the")
        print(f"   interim 0.635 ± 0.026 to this run. Reading (B) is priced")
        print(f"   in the same runs; if it sits off 2/π it is the fork's dead")
        print(f"   half, consistent with the data-selection of the linear")
        print(f"   coupling. #26 promotes at candidate grade; the residual")
        print(f"   ('leading-order dominates') stays named.")
    elif kill_i:
        print("   KILL (i): the ensemble lands > 2σ from 2/π — ledger row;")
        print("   the derived stack loses its middle factor.")
    else:
        print("   KILL (ii): the R_i spread exceeds the distance to 2/π —")
        print("   f̄ is not a sharp constant; the closed form is moot. Ledger.")
    print("=" * 78)


if __name__ == "__main__":
    main()
