#!/usr/bin/env python3
"""Week-1 Page-curve instrument: 1D sonic horizon + Unruh T_H (NOT a Page curve).

Milestone A (honest first success), plan:
  docs/working_logs/_runs/quantum_null_hardening_20260803/PAGE_CURVE_IMPLEMENTATION_PLAN.md

What this script DOES:
  - Prescribe a stationary 1D acoustic background n(x), v(x) with a sonic horizon
  - Locate x_h where |v| = c_s; compute surface gravity κ and T_H = κ/(2π)
  - Print Bose occupation n_B(ω) = 1/(e^{ω/T_H}−1) for a mid-band of frequencies
  - Convergence check on κ under grid refinement; null profile (no horizon)

What this script does NOT do (do not over-claim):
  - No S_rad(v), no Page turn, no evaporative dynamics, no finite-core Hilbert space
  - No Bogoliubov scattering solve / greybody (Week 2+)
  - No self-consistent GP evolution (optional upgrade after Milestone A)
  - Toy 4v(1−v) ansatz is forbidden here (scaffold only)

Healing units: length ξ, time t_heal = ξ/c_s, ħ = k_B = 1.
Acoustic surface gravity (1D):
  κ = (1/2) ∂_x (c_s² − v²) |_{x_h}   ⇒   T_H = κ/(2π)
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# MVP defaults (healing units) — frozen for Week 1
# ---------------------------------------------------------------------------
L = 80.0  # domain length in ξ
N_DEFAULT = 2048
CORE_HINT = 3.0  # |x| <~ few ξ is the finite-core region (bookkeeping only)

OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
OUT_JSON = OUT_DIR / "page_curve" / "week1_sonic_horizon.json"


def bose_occupation(omega: float, T: float) -> float:
    """Thermal Bose occupation n_B(ω) = 1/(e^{ω/T}−1)."""
    if T <= 0.0:
        return 0.0
    if omega <= 0.0:
        raise ValueError("omega must be > 0")
    x = omega / T
    if x > 700.0:  # overflow guard
        return 0.0
    return 1.0 / (math.exp(x) - 1.0)


def profile_bh_tanh(
    x: np.ndarray,
    *,
    ell: float = 4.0,
    v_in: float = -1.5,
    v_out: float = -0.5,
    n_inf: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Stationary BH-like acoustic profile (prescribed; not evolved GP).

    Constant density ⇒ c_s = sqrt(n) = const (healing units g=m=1).
    Flow interpolates from supersonic interior (left) to subsonic exterior (right):
        v(x) = ½(v_in + v_out) + ½(v_out − v_in) tanh(x/ℓ)

    With defaults |v_in|=1.5 > 1, |v_out|=0.5 < 1, horizon at x=0 when c_s=1
    and (v_in + v_out)/2 = −1.
    """
    n = np.full_like(x, n_inf, dtype=float)
    c_s = np.sqrt(n)
    mid = 0.5 * (v_in + v_out)
    amp = 0.5 * (v_out - v_in)
    v = mid + amp * np.tanh(x / ell)
    return n, v, c_s


def profile_subsonic_null(
    x: np.ndarray,
    *,
    v0: float = -0.3,
    n_inf: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Subsonic everywhere — control null: no sonic horizon, no Hawking T_H."""
    n = np.full_like(x, n_inf, dtype=float)
    c_s = np.sqrt(n)
    v = np.full_like(x, v0, dtype=float)
    return n, v, c_s


def analytic_kappa_tanh(
    *,
    ell: float = 4.0,
    v_in: float = -1.5,
    v_out: float = -0.5,
    n_inf: float = 1.0,
) -> dict:
    """Exact κ for the tanh profile at the sonic point (analytic).

    c_s = sqrt(n_inf). Horizon where |v| = c_s and v < 0 for leftward BH flow:
        v(x) = mid + amp * tanh(x/ℓ)
        mid + amp * t = −c_s  (assuming c_s > 0)
    For defaults mid=−1, amp=0.5, c_s=1 → tanh(x_h/ℓ)=0 → x_h=0.
    κ = (1/2) ∂_x (c_s² − v²) |_{x_h} = −v ∂_x v |_{x_h}
    """
    c_s = math.sqrt(n_inf)
    mid = 0.5 * (v_in + v_out)
    amp = 0.5 * (v_out - v_in)
    # solve mid + amp * tanh(x_h/ell) = -c_s
    arg = (-c_s - mid) / amp
    if abs(arg) > 1.0 + 1e-12:
        return {"found": False, "reason": "no real horizon for this (v_in,v_out,c_s)"}
    arg = max(-1.0, min(1.0, arg))
    x_h = ell * math.atanh(arg) if abs(arg) < 1.0 else (math.copysign(1e9, arg))
    sech2 = 1.0 - arg * arg
    dv_dx = (amp / ell) * sech2
    v_h = -c_s
    kappa = -v_h * dv_dx  # = c_s * dv_dx when v_h = -c_s
    # equivalent: 0.5 * d/dx(c_s^2 - v^2) = -v dv/dx
    return {
        "found": True,
        "x_h": x_h,
        "v_h": v_h,
        "c_s": c_s,
        "kappa": kappa,
        "T_H": kappa / (2.0 * math.pi),
        "ell": ell,
        "v_in": v_in,
        "v_out": v_out,
        "dv_dx": dv_dx,
    }


def find_horizon(
    x: np.ndarray,
    v: np.ndarray,
    c_s: np.ndarray,
) -> dict:
    """Locate outermost BH-like sonic point: |v|=c_s with |v| larger inside (left)."""
    f = np.abs(v) - c_s
    # sign change of f: interior f>0 (supersonic), exterior f<0 (subsonic)
    hits: list[dict] = []

    def _record(i: int, x_h: float, v_h: float, c_h: float, df: float) -> None:
        hits.append(
            {
                "i": i,
                "x_h": x_h,
                "v_h": v_h,
                "c_s_h": c_h,
                # BH-like: f decreases through zero (supersonic → subsonic L→R)
                # and inflow to the left (v_h < 0)
                "bh_like": df < 0.0 and v_h < 0.0,
            }
        )

    for i in range(len(x) - 1):
        if f[i] == 0.0:
            # exact grid hit: slope from neighbors when possible
            if i > 0:
                df = float(f[i + 1] - f[i - 1])
            else:
                df = float(f[i + 1] - f[i])
            _record(i, float(x[i]), float(v[i]), float(c_s[i]), df)
        elif f[i] * f[i + 1] < 0.0:
            t = float(f[i] / (f[i] - f[i + 1]))
            x_h = float(x[i] + t * (x[i + 1] - x[i]))
            v_h = float(v[i] + t * (v[i + 1] - v[i]))
            c_h = float(c_s[i] + t * (c_s[i + 1] - c_s[i]))
            df = float(f[i + 1] - f[i])
            _record(i, x_h, v_h, c_h, df)
    # last point exact zero
    if f[-1] == 0.0:
        _record(len(x) - 1, float(x[-1]), float(v[-1]), float(c_s[-1]), float(f[-1] - f[-2]))

    bh = [h for h in hits if h.get("bh_like")]
    if not bh:
        return {"found": False, "hits": hits}
    # outermost (largest x_h)
    h = max(bh, key=lambda z: z["x_h"])
    return {"found": True, **h}


def surface_gravity_fd(
    x: np.ndarray,
    v: np.ndarray,
    c_s: np.ndarray,
    x_h: float,
) -> float:
    """κ = (1/2) ∂_x (c_s² − v²) at x_h via centered finite difference + interp."""
    g = c_s**2 - v**2
    dg = np.gradient(g, x)
    return float(0.5 * np.interp(x_h, x, dg))


def kappa_on_grid(N: int, ell: float = 4.0) -> dict:
    """Build grid profile, find horizon, measure κ."""
    dx = L / N
    x = np.linspace(-L / 2, L / 2, N, endpoint=False)
    n, v, c_s = profile_bh_tanh(x, ell=ell)
    h = find_horizon(x, v, c_s)
    if not h["found"]:
        return {"N": N, "dx": dx, "found": False}
    kappa = surface_gravity_fd(x, v, c_s, h["x_h"])
    return {
        "N": N,
        "dx": dx,
        "found": True,
        "x_h": h["x_h"],
        "v_h": h["v_h"],
        "c_s_h": h["c_s_h"],
        "kappa": kappa,
        "T_H": kappa / (2.0 * math.pi),
        "ell": ell,
    }


def midband_frequencies(T_H: float, kappa: float) -> list[float]:
    """Pre-registered mid-band: ω ∈ [0.05, 2] κ (plan §1.3), plus thermal peak ~κ."""
    # sample relative to κ so table is profile-independent in shape
    fracs = [0.05, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0]
    omegas = [f * kappa for f in fracs]
    # also add a few absolute points near T_H if distinct
    return omegas


def main() -> None:
    print("=" * 78)
    print("WEEK1 ONLY — thermal bookkeeping; Page curve NOT computed;")
    print("S_rad(v) NOT claimed. Milestone A instrument: sonic horizon + T_H.")
    print("=" * 78)
    print()
    print("Units: healing (ξ, t_heal=ξ/c_s), ħ=k_B=1, g=m=1 ⇒ c_s=√n")
    print(f"Domain: x ∈ [{-L/2}, {L/2}] ξ, N default={N_DEFAULT}")
    print("Background: prescribed stationary tanh flow (not self-consistent GP)")
    print()

    # --- Analytic target ---
    ell = 4.0
    ana = analytic_kappa_tanh(ell=ell)
    assert ana["found"], "analytic horizon missing for default profile"
    print("--- Analytic tanh profile (exact) ---")
    print(f"  ell        = {ell:.4f} ξ")
    print(f"  v_in/v_out = {ana['v_in']:.3f} / {ana['v_out']:.3f}")
    print(f"  x_h        = {ana['x_h']:.6f} ξ")
    print(f"  v_h, c_s   = {ana['v_h']:.6f}, {ana['c_s']:.6f}")
    print(f"  dv/dx|xh   = {ana['dv_dx']:.6f}")
    print(f"  κ          = {ana['kappa']:.6f}  (1/t_heal)")
    print(f"  T_H=κ/2π   = {ana['T_H']:.6f}")
    print()

    # --- Grid measurement + convergence ---
    print("--- Grid measurement (finite difference) ---")
    print(f"  {'N':>6} {'dx':>10} {'x_h':>12} {'κ':>12} {'T_H':>12} {'|κ-κ_an|/κ_an':>14}")
    grid_rows = []
    for N in (512, 1024, 2048, 4096):
        r = kappa_on_grid(N, ell=ell)
        assert r["found"], f"horizon not found on N={N}"
        rel = abs(r["kappa"] - ana["kappa"]) / ana["kappa"]
        grid_rows.append({**r, "rel_err_kappa": rel})
        print(
            f"  {N:6d} {r['dx']:10.5f} {r['x_h']:12.6f} {r['kappa']:12.6f} "
            f"{r['T_H']:12.6f} {100*rel:13.4f}%"
        )
    # Exit criterion: κ stable to <5% (plan Week 1 day 2); vs analytic even tighter
    best = grid_rows[-1]
    assert best["rel_err_kappa"] < 0.05, "κ grid error ≥ 5% — instrument FAIL"
    assert best["kappa"] > 0.0, "κ must be positive for BH-like horizon"
    # N→2N stability between last two
    rel_refine = abs(grid_rows[-1]["kappa"] - grid_rows[-2]["kappa"]) / grid_rows[-1]["kappa"]
    print(f"  refinement |κ_N−κ_{{N/2}}|/κ_N = {100*rel_refine:.4f}%  "
          f"{'PASS' if rel_refine < 0.05 else 'FAIL'} (<5%)")
    print()

    # --- Null: subsonic ---
    print("--- Null control: subsonic everywhere ---")
    x = np.linspace(-L / 2, L / 2, N_DEFAULT, endpoint=False)
    n0, v0, c0 = profile_subsonic_null(x)
    h0 = find_horizon(x, v0, c0)
    print(f"  max |v|/c_s = {float(np.max(np.abs(v0) / c0)):.4f}")
    print(f"  horizon found? {h0['found']}  "
          f"{'PASS (none expected)' if not h0['found'] else 'FAIL'}")
    assert not h0["found"], "subsonic null must not produce a horizon"
    print()

    # --- Thermal occupation table (demonstration bookkeeping) ---
    T_H = ana["T_H"]
    kappa = ana["kappa"]
    omegas = midband_frequencies(T_H, kappa)
    print("--- Mode frequencies vs thermal occupation n_B(ω)=1/(e^{ω/T_H}−1) ---")
    print("  (Unruh/Hawking thermal bookkeeping on T_H=κ/2π; NOT a scattering solve)")
    print(f"  {'ω/κ':>8} {'ω':>12} {'ω/T_H':>10} {'n_B(ω)':>14}")
    table = []
    for w in omegas:
        nb = bose_occupation(w, T_H)
        row = {
            "omega_over_kappa": w / kappa,
            "omega": w,
            "omega_over_T_H": w / T_H,
            "n_B": nb,
        }
        table.append(row)
        print(
            f"  {w/kappa:8.3f} {w:12.6f} {w/T_H:10.4f} {nb:14.6e}"
        )
    print()
    # sanity: n_B decreases with ω; high-ω occupation small
    assert table[0]["n_B"] > table[-1]["n_B"]
    assert bose_occupation(kappa, T_H) > 0.0

    # Wien / peak check of energy density ~ ω n_B(ω) for 1D-ish demo
    w_peak = max(omegas, key=lambda w: w * bose_occupation(w, T_H))
    print(f"  max of ω n_B(ω) among sampled mid-band bins at ω/κ = {w_peak/kappa:.3f}")
    print(f"  (thermal peak scale ~ O(κ) ~ O(2π T_H); expected order-of-magnitude only)")
    print()

    # --- Explicit non-claims ---
    print("--- Explicit non-claims (Week 1 fence) ---")
    print("  * S_rad(v)          : NOT computed")
    print("  * Page time / turn  : NOT computed")
    print("  * Greybody Γ(ω)     : NOT computed (n_B is pure thermal reference)")
    print("  * Bogoliubov β_ω    : NOT extracted from mode equation")
    print("  * Finite-core DM    : NOT evolved")
    print("  * GP self-consistency: NOT run (prescribed acoustic metric OK for Week 1)")
    print()

    # --- Write JSON artifact ---
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "milestone": "A_week1_sonic_horizon_thermal_bookkeeping",
        "claim_grade": "instrument_partial",
        "page_curve_claimed": False,
        "S_rad_v_claimed": False,
        "units": "healing (xi, t_heal), hbar=kB=1",
        "profile": {
            "type": "tanh_stationary_acoustic",
            "ell": ell,
            "v_in": ana["v_in"],
            "v_out": ana["v_out"],
            "n_inf": 1.0,
            "L": L,
        },
        "analytic": {
            "x_h": ana["x_h"],
            "kappa": ana["kappa"],
            "T_H": ana["T_H"],
        },
        "grid_convergence": grid_rows,
        "null_subsonic_horizon_found": False,
        "thermal_table": table,
        "acceptance": {
            "horizon_found": True,
            "kappa_positive": True,
            "kappa_vs_analytic_rel_err": best["rel_err_kappa"],
            "kappa_refine_rel": rel_refine,
            "kappa_stable_lt_5pct": bool(rel_refine < 0.05 and best["rel_err_kappa"] < 0.05),
            "thermal_fit_from_modes": False,  # Week 1: bookkeeping only; no mode solve
            "note": (
                "T_H reported from κ/2π; n_B(ω) is the ideal Bose reference, "
                "not a fitted spectrum from Bogoliubov scattering (Week 2)."
            ),
        },
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2))
    print(f"wrote {OUT_JSON}")
    print()
    print("=" * 78)
    print("WEEK1 RESULT: PASS — sonic horizon instrumented; κ, T_H, n_B table OK.")
    print("Page curve remains OPEN. S_rad(v) remains NOT claimed.")
    print("=" * 78)


if __name__ == "__main__":
    main()
