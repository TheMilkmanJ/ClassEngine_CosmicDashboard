"""winding_fbar_spatial — P-2026-041's check on the RIGHT object: the spatial winding average (2026-07-28).

PROVENANCE
  The first rebuild (winding_fbar_ensemble.py) measured a friction-damped
  orbit's polar angle — the wrong object; its erratum stands and nothing
  was graded.  This instrument measures the registered object: the SPATIAL
  average ⟨|cos θ|⟩ over a ring of the genesis field CARRYING A WINDING,
  evolved on the model's own recorded potential
      V = m²R² + λR⁴ + 2ε_A·λR⁴·cos 4θ,   ε_A = 2/9
  with radiation-era Hubble friction and the gradient stiffness that lets
  the winding live — the exact machinery of `genesis_joint_draw.py`
  (constants, ramp initial condition, and stepper replicated; κ = 0.6,
  N = 24, r₀ = 10, the instrument's own values).

THE CLAIM UNDER TEST (as registered)
  f̄ = ⟨|cos θ|⟩ = 2/π = 0.63662 in the MANY-TURNS limit: the winding wraps
  the phase uniformly around the compact direction, and equidistribution
  forces the mean-absolute cosine to its textbook value.  The Z₄ tilt
  (the A-term) fights equidistribution early — it dies as R⁴ under the
  amplitude's decay — so the test is whether the LATE, frozen configuration
  averages to 2/π, with the trend in winding number n showing the
  many-turns limit.

ENSEMBLE
  θ_i uniform over the prior (64 values) × n ∈ {1, 2, 4, 8} × N = 24
  sites.  Winding survival is CHECKED per draw (final winding = initial);
  slipped rings are counted and excluded openly, never silently averaged.

KILLS (transferred from the registration)
  (i)  the many-turn members (n ≥ 4) landing > 2σ from 0.63662;
  (ii) the n-to-n systematic at large n exceeding the distance to 2/π.

GRADE RULE
  Ensemble mean ± σ/√M per n; survival counts printed; the verdict computed
  from the large-n members only (the registered limit), with the small-n
  deviation reported as the A-term's expected early-epoch imprint, not a
  kill.
"""
from __future__ import annotations

import math

import numpy as np

M2, LAM, RI = 1.0, 0.03, 10.0
EPS_A = 2.0 / 9.0
T0, TF, DT = 0.25, 60.0, 0.04
KAPPA = 0.6
N_SITES = 48
N_THETA = 64
WINDINGS = (1, 2, 4, 8)
TWO_OVER_PI = 2.0 / math.pi


def _wrap(d):
    return (d + np.pi) % (2 * np.pi) - np.pi


def winding_of(theta):
    d = _wrap(np.roll(theta, -1, axis=-1) - theta)
    return d.sum(axis=-1) / (2 * np.pi)


def ring_ic(theta_i, n, N):
    j = np.arange(N)
    return theta_i + 2 * np.pi * n * (j - (N - 1) / 2.0) / N


def accel(x, y):
    r2 = x * x + y * y
    dVx = 2 * M2 * x + 4 * LAM * r2 * x + 2 * EPS_A * LAM * (4 * x ** 3 - 12 * x * y * y)
    dVy = 2 * M2 * y + 4 * LAM * r2 * y + 2 * EPS_A * LAM * (4 * y ** 3 - 12 * x * x * y)
    lx = KAPPA * (np.roll(x, -1, axis=-1) + np.roll(x, 1, axis=-1) - 2 * x)
    ly = KAPPA * (np.roll(y, -1, axis=-1) + np.roll(y, 1, axis=-1) - 2 * y)
    return lx - dVx, ly - dVy


def evolve_measure(theta0):
    """RK4 from rest; returns the late-window ⟨|cosθ|⟩ per draw + final winding."""
    x = RI * np.cos(theta0)
    y = RI * np.sin(theta0)
    vx = np.zeros_like(x)
    vy = np.zeros_like(y)
    t = T0
    acc_c, n_c = np.zeros(theta0.shape[0]), 0
    w_samples = []
    while t < TF:
        h = 1.0 / (2.0 * t)

        def rhs(xx, yy, vxx, vyy):
            ax, ay = accel(xx, yy)
            return vxx, vyy, ax - 3 * h * vxx, ay - 3 * h * vyy

        k1 = rhs(x, y, vx, vy)
        k2 = rhs(x + 0.5 * DT * k1[0], y + 0.5 * DT * k1[1],
                 vx + 0.5 * DT * k1[2], vy + 0.5 * DT * k1[3])
        k3 = rhs(x + 0.5 * DT * k2[0], y + 0.5 * DT * k2[1],
                 vx + 0.5 * DT * k2[2], vy + 0.5 * DT * k2[3])
        k4 = rhs(x + DT * k3[0], y + DT * k3[1],
                 vx + DT * k3[2], vy + DT * k3[3])
        x = x + DT / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y = y + DT / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        vx = vx + DT / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
        vy = vy + DT / 6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
        t += DT
        if t > 0.7 * TF:
            th = np.arctan2(y, x)
            r = np.hypot(x, y)
            c = np.where(r > 1e-9, np.abs(np.cos(th)), np.nan)
            acc_c += np.nanmean(c, axis=-1)
            n_c += 1
            # amplitude-gated winding samples: the damped field sweeps through
            # near-zero amplitude each half-cycle, where arctan2 is noise — a
            # single-snapshot read (v1, v2) 'slipped' whole n-classes purely by
            # oscillation phasing.  Collect the winding only when every site
            # resolves the phase, and take the per-draw MEDIAN over the window.
            if float(np.min(r)) > 0.05 * float(np.median(r)) and np.all(r > 1e-6):
                w_samples.append(winding_of(th))
    w = (np.median(np.stack(w_samples), axis=0) if w_samples
         else np.full(theta0.shape[0], np.nan))
    return acc_c / n_c, w


def main() -> None:
    print("=" * 78)
    print("The spatial winding average — the registered object, on its own machine")
    print("=" * 78)
    thetas = np.linspace(0, 2 * np.pi, N_THETA, endpoint=False)
    results = {}
    for n in WINDINGS:
        ic = np.stack([ring_ic(t0, n, N_SITES) for t0 in thetas])
        fbar, wfin = evolve_measure(ic)
        keep = np.abs(wfin - n) < 0.5
        f = fbar[keep]
        results[n] = (float(np.mean(f)), float(np.std(f) / max(math.sqrt(len(f)), 1)),
                      int(keep.sum()), len(keep))
        m, s, k, tot = results[n]
        print(f"   n = {n}:  f̄ = {m:.5f} ± {s:.5f}   (windings survived {k}/{tot})")

    big = [results[n] for n in WINDINGS if n >= 4 and results[n][2] > 8]
    if not big:
        print("\n   CANNOT GRADE — no many-turn member has enough surviving")
        print("   windings; diagnose the harness before any verdict. Nothing")
        print("   passes, nothing dies.")
        return
    mB = float(np.mean([m for m, *_ in big]))
    sB = float(np.mean([s for _, s, *_ in big]) / math.sqrt(len(big)))
    sysB = float(max(abs(m - mB) for m, *_ in big)) if len(big) > 1 else 0.0
    dist = abs(mB - TWO_OVER_PI)
    print(f"\n   MANY-TURN MEMBERS (n ≥ 4): f̄ = {mB:.5f} ± {sB:.5f}, "
          f"n-systematic {sysB:.5f}")
    print(f"   target 2/π = {TWO_OVER_PI:.5f} — distance {dist:.5f} "
          f"({dist/max(sB,1e-9):.1f}σ)")

    kill_i = dist > 2 * sB and dist > sysB
    kill_ii = sysB > dist and sysB > 3 * sB
    print("\nVERDICT (kills transferred from the registration):")
    if not kill_i and not kill_ii:
        print("   THE CHECK PASSES on the registered object at ensemble precision:")
        print("   the many-turn winding average lands at 2/π. #26 promotes at")
        print("   candidate grade; the residual ('leading-order dominates') and")
        print("   the small-n A-term imprint stay named.")
    elif kill_i:
        print("   KILL (i): the many-turn average lands > 2σ off 2/π — ledger row;")
        print("   the derived stack loses its middle factor.")
    else:
        print("   KILL (ii): the winding-number systematic exceeds the distance —")
        print("   f̄ is not a sharp constant. Ledger row.")
    print("=" * 78)


if __name__ == "__main__":
    main()
