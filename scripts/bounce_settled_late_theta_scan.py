#!/usr/bin/env python3
"""bounce_settled_late_theta_scan — F5 deepen: S1_settled under stocked FA3 0D only.

PACKAGE
  docs/working_logs/_runs/theory_construction_20260804/settled_late_theta_20260804/

MISSION (red F5 residual)
  Prior n3_gpe best-late row has late_tail10=+2.87 but late_tail20=−0.14
  and settled_std~1.25 — not a stable positive late ⟨Θ⟩.
  Re-define the lock metric as **settled** late, re-scan the stocked 0D
  ODE, and document whether ring-down always drives settled_mean → O(0.1)
  or below under the stocked form.

STOCKED FORM ONLY (FA3 / N1 reduced stress-channel)
  dn/dt = −n Θ
  dΘ/dt = −Θ² + κ(n−1) − γ Θ

S1_settled DEFINITION
  Integrate past re-entry cut (t_npeak+8) by settle_extra healing times.
  settled_mean = mean of last 20% of the full Θ history.
  settled_std  = std  of last 20% of the full Θ history.
  Quality cut (optional): settled_std < SETTLED_STD_MAX (default 0.2).

HARD RULES
  - FA3 0D form only — no invent force laws, no free dial beyond scan grid
  - No invent H_re · no bounce closed · leave MCMCs · no PolyChord
  - page_curve_claimed = false · production_3d = false (0D is not 3D)
  - exit 0 = compute finished; PASS/FAIL is physics grade in SUMMARY
  - Θ_lock ≈ 11.71 is a target, not an achievement

ANALYTIC ANCHOR
  Unique physical fixed point of the stocked ODE: (n, Θ) = (1, 0).
  Linearization: δn' = −Θ,  Θ' = κ δn − γ Θ  →  λ² + γλ + κ = 0.
  For γ > 0 the fixed point is asymptotically stable (ring-down rate γ/2).
  Therefore settled_mean → 0 as t → ∞ under the stocked form with γ > 0.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# anchors (disk / book; identical to FA3 / N3)
# ---------------------------------------------------------------------------
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
D_LOCK = 3
THETA_LOCK = D_LOCK / (C_S * math.sqrt(3.0))  # = 1/√α at d=3 ≈ 11.706
H_KIN_OVER_H_DOOR_UNIT = C_S / math.sqrt(3.0)  # |H_kin|/H_door at Θ=1
TH_CAP = 80.0
SETTLED_STD_MAX = 0.2  # quality cut for "settled" rows
DT_DEFAULT = 1e-3
PACKAGE = "settled_late_theta_20260804"
PRIOR = "n3_gpe_late_theta_20260804"
STOCKED_DEFAULT = (6.0, -2.0, 1.5, 0.15)  # (n0, Θ0, κ, γ)
PRIOR_BEST_LATE = (80.0, -8.0, 3.0, 0.02)  # F5 row


def hkin_over_hdoor(Theta: float, d: int = D_LOCK) -> float:
    """|H_kin(Θ)|/H_door with H_kin=Θ c_s/(d ξ), H_door=1/(√3 ξ)."""
    return abs(Theta) * C_S * math.sqrt(3.0) / float(d)


def late_windows(hist: np.ndarray) -> Dict[str, float]:
    a = np.asarray(hist, dtype=float)
    if a.size == 0:
        return {
            "late_tail10": float("nan"),
            "late_tail20": float("nan"),
            "late_last": float("nan"),
            "settled_mean": float("nan"),
            "settled_std": float("nan"),
        }
    n10 = max(1, a.size // 10)
    n20 = max(1, a.size // 5)
    tail = a[-n20:]
    return {
        "late_tail10": float(np.mean(a[-n10:])),
        "late_tail20": float(np.mean(tail)),
        "late_last": float(a[-1]),
        "settled_mean": float(np.mean(tail)),
        "settled_std": float(np.std(tail)),
    }


# ---------------------------------------------------------------------------
# stocked FA3 0D ODE (identical form to bounce_n3_gpe_late_theta.medium_rebound_0d)
# ---------------------------------------------------------------------------
def medium_rebound_0d(
    n0: float = 6.0,
    Theta0: float = -2.0,
    kappa: float = 1.5,
    gamma: float = 0.15,
    t_max: float = 200.0,
    dt: float = DT_DEFAULT,
    settle_extra: float = 40.0,
) -> Dict[str, float]:
    """Stocked reduced ODE with explicit settle extension.

    Re-entry cut: first t > t_npeak+8 with density overshoot.
    Then continue settle_extra more time units (healing).
    S1_settled = last-20% mean of the full trajectory (incl. settle).
    Also report re-entry-window tail10/tail20 for F5 comparison.
    """
    n, Th = float(n0), float(Theta0)
    n_peak, t_turn_n = n0, 0.0
    turned = False
    t_cross = float("nan")
    t = 0.0
    th_hist: List[float] = []
    n_hist: List[float] = []
    dth_at_cross = float("nan")
    th_max_pos = 0.0
    th_max_abs = abs(Th)
    hit_cap = False
    t_cut_reentry = t_max
    cut_set = False

    while t < t_max:
        dn = -n * Th
        dTh = -(Th * Th) + kappa * (n - 1.0) - gamma * Th
        n = max(n + dt * dn, 1e-8)
        Th = Th + dt * dTh
        if abs(Th) > TH_CAP:
            Th = math.copysign(TH_CAP, Th)
            hit_cap = True
        t += dt
        th_hist.append(Th)
        n_hist.append(n)
        if Th > th_max_pos:
            th_max_pos = Th
        if abs(Th) > th_max_abs:
            th_max_abs = abs(Th)
        if n > n_peak:
            n_peak = n
            t_turn_n = t
        if (
            not turned
            and len(th_hist) > 1
            and th_hist[-2] < 0.0 <= th_hist[-1]
            and n_peak > n0 * 1.005
        ):
            turned = True
            t_cross = t
            dth_at_cross = dTh
        if (not cut_set) and t > t_turn_n + 8.0 and n_peak > n0 * 1.005:
            t_cut_reentry = t
            cut_set = True
            if settle_extra <= 0.0:
                break
        if cut_set and t > t_cut_reentry + settle_extra:
            break
        if hit_cap and t > t_turn_n + 2.0:
            break

    th_a = np.asarray(th_hist, dtype=float)
    n_a = np.asarray(n_hist, dtype=float)

    # re-entry-window windows (F5 comparison — not S1_settled)
    if cut_set and settle_extra > 0.0:
        n_re = max(1, int(round(t_cut_reentry / dt)))
        n_re = min(n_re, th_a.size)
        re_hist = th_a[:n_re]
    else:
        re_hist = th_a
    re_lw = late_windows(re_hist)
    full_lw = late_windows(th_a)

    return {
        "n0": float(n0),
        "Theta0": float(Theta0),
        "kappa": float(kappa),
        "gamma": float(gamma),
        "dt": float(dt),
        "settle_extra": float(settle_extra),
        "turned": float(turned),
        "t_cross": float(t_cross) if turned else float("nan"),
        "dTheta_dt_cross": float(dth_at_cross) if turned else float("nan"),
        # re-entry-window (prior S1 primary; F5-sensitive)
        "late_tail10": float(re_lw["late_tail10"]),
        "late_tail20": float(re_lw["late_tail20"]),
        "late_Theta": float(re_lw["late_tail10"]),  # alias prior name
        # S1_settled (this package primary)
        "settled_mean": float(full_lw["settled_mean"]),
        "settled_std": float(full_lw["settled_std"]),
        "settled_last": float(full_lw["late_last"]),
        "S1_settled": float(full_lw["settled_mean"]),
        "quality_ok": float(
            math.isfinite(full_lw["settled_std"])
            and full_lw["settled_std"] < SETTLED_STD_MAX
        ),
        "overshoot": n_peak / max(n0, 1e-12),
        "n_peak": float(n_peak),
        "n_late": float(n_a[-1]) if n_a.size else float("nan"),
        "Theta_max_pos": float(th_max_pos),
        "Theta_max_abs": float(th_max_abs),
        "hit_cap": float(hit_cap),
        "t_end": float(t),
        "t_cut_reentry": float(t_cut_reentry) if cut_set else float(t),
        "Hkin_Hdoor_late": hkin_over_hdoor(re_lw["late_tail10"]),
        "Hkin_Hdoor_settled": hkin_over_hdoor(full_lw["settled_mean"]),
        "Hkin_Hdoor_peak": hkin_over_hdoor(th_max_pos),
    }


def row_physical(r: Dict[str, float]) -> bool:
    if r["hit_cap"] > 0.5:
        return False
    if r["overshoot"] > 100.0:
        return False
    if not math.isfinite(r["settled_mean"]):
        return False
    return True


def quality_cut(r: Dict[str, float], std_max: float = SETTLED_STD_MAX) -> bool:
    return row_physical(r) and math.isfinite(r["settled_std"]) and r["settled_std"] < std_max


# ---------------------------------------------------------------------------
# analytic ring-down (stocked form)
# ---------------------------------------------------------------------------
def analytic_fixed_point_report() -> Dict[str, Any]:
    """Document: unique physical FP (1,0); linear ring-down rate γ/2."""
    # Jacobian at (n,Θ)=(1,0):
    #   d(δn)/dt = −δΘ
    #   d(δΘ)/dt = κ δn − γ δΘ
    # char poly: λ² + γ λ + κ = 0
    # Re(λ) = −γ/2  (when γ≥0, κ>0)
    cases = []
    for kappa, gamma in ((1.5, 0.15), (3.0, 0.02), (1.5, 0.5), (5.0, 0.10)):
        disc = gamma * gamma - 4.0 * kappa
        rate = gamma / 2.0
        if disc < 0:
            omega = math.sqrt(kappa - rate * rate)
            regime = "underdamped"
        elif disc == 0:
            omega = 0.0
            regime = "critical"
        else:
            omega = 0.0
            regime = "overdamped"
        # time for e^{−(γ/2)t} to drop to 1% of amplitude
        t_1pct = (math.log(100.0) / rate) if rate > 0 else float("inf")
        cases.append(
            {
                "kappa": kappa,
                "gamma": gamma,
                "ringdown_rate_gamma_over_2": rate,
                "disc": disc,
                "regime": regime,
                "omega_osc": omega,
                "t_amplitude_1pct": t_1pct,
            }
        )
    return {
        "unique_physical_fixed_point": {"n": 1.0, "Theta": 0.0},
        "char_poly": "lambda^2 + gamma*lambda + kappa = 0",
        "asymptotic": (
            "For gamma>0 and kappa>0, FP is asymptotically stable with "
            "Re(lambda)=−gamma/2. Therefore settled_mean → 0 as t→∞ "
            "under the stocked form. No non-zero late attractor exists."
        ),
        "linear_cases": cases,
        "claim": (
            "Ring-down under stocked FA3 0D always drives settled_mean → 0 "
            "(hence O(0.1) or below after finite settle for legal γ>0). "
            "Finite-window residuals of O(0.1) are damped oscillations, "
            "not a stable positive late ⟨Θ⟩."
        ),
    }


# ---------------------------------------------------------------------------
# scan grid (stocked coefficients only; densify prior late-best corner)
# ---------------------------------------------------------------------------
def build_grid() -> List[Tuple[float, float, float, float]]:
    pts: List[Tuple[float, float, float, float]] = []

    # axis A: n0 × Θ0 at stocked (κ,γ)=(1.5,0.15)
    for n0 in (2.0, 3.0, 6.0, 11.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0):
        for Th0 in (-0.5, -1.0, -1.5, -2.0, -3.0, -4.0, -5.0, -6.0, -8.0):
            pts.append((n0, Th0, 1.5, 0.15))

    # axis B: κ × γ at stocked (n0,Θ0)=(6,−2)
    for kappa in (0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0):
        for gamma in (0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.30, 0.50):
            pts.append((6.0, -2.0, kappa, gamma))

    # axis C: high-compression corner (prior best late region)
    for n0 in (20.0, 30.0, 40.0, 50.0, 60.0, 80.0):
        for Th0 in (-3.0, -5.0, -6.0, -8.0):
            for kappa in (2.0, 3.0, 4.0, 5.0):
                for gamma in (0.02, 0.05, 0.08, 0.10, 0.15):
                    pts.append((n0, Th0, kappa, gamma))

    # axis D: mild / corpus FA3 points with κγ spread
    for n0, Th0 in ((3.0, -1.0), (6.0, -1.0), (6.0, -2.0), (11.0, -2.0), (11.0, -3.0)):
        for kappa in (1.0, 1.5, 2.0, 3.0):
            for gamma in (0.05, 0.10, 0.15, 0.30):
                pts.append((n0, Th0, kappa, gamma))

    # always include stocked default + prior F5 best-late
    pts.append(STOCKED_DEFAULT)
    pts.append(PRIOR_BEST_LATE)

    seen = set()
    unique: List[Tuple[float, float, float, float]] = []
    for p in pts:
        if p in seen:
            continue
        seen.add(p)
        unique.append(p)
    return unique


def scan_settled(
    settle_extra: float = 40.0,
    dt: float = DT_DEFAULT,
) -> Tuple[List[Dict[str, float]], Dict[str, Any]]:
    grid = build_grid()
    rows: List[Dict[str, float]] = []
    for n0, Th0, kappa, gamma in grid:
        rows.append(
            medium_rebound_0d(
                n0, Th0, kappa, gamma, settle_extra=settle_extra, dt=dt
            )
        )

    physical = [r for r in rows if row_physical(r)]
    quality = [r for r in physical if quality_cut(r)]
    turned = [r for r in physical if r["turned"] > 0.5]

    def _best(pool: List[Dict[str, float]], key: str) -> Optional[Dict[str, float]]:
        pool_f = [r for r in pool if math.isfinite(r[key])]
        if not pool_f:
            return None
        return max(pool_f, key=lambda r: r[key])

    best_settled_all = _best(physical, "settled_mean")
    best_settled_q = _best(quality, "settled_mean")
    best_late = _best(physical, "late_Theta")  # re-entry tail10 for F5 contrast

    max_settled_all = (
        best_settled_all["settled_mean"] if best_settled_all else float("-inf")
    )
    max_settled_q = (
        best_settled_q["settled_mean"] if best_settled_q else float("-inf")
    )
    max_late = best_late["late_Theta"] if best_late else float("-inf")

    # positive settled among quality
    pos_q = [r for r in quality if r["settled_mean"] > 0.0]
    max_pos_settled_q = (
        max(r["settled_mean"] for r in pos_q) if pos_q else float("-inf")
    )
    best_pos_q = _best(pos_q, "settled_mean")

    return rows, {
        "settle_extra": settle_extra,
        "dt": dt,
        "settled_std_max": SETTLED_STD_MAX,
        "n_rows": len(rows),
        "n_physical": len(physical),
        "n_quality": len(quality),
        "n_turned": len(turned),
        "n_blowup": len(rows) - len(physical),
        "max_settled_mean_all_physical": float(max_settled_all)
        if math.isfinite(max_settled_all)
        else None,
        "max_settled_mean_quality": float(max_settled_q)
        if math.isfinite(max_settled_q)
        else None,
        "max_positive_settled_quality": float(max_pos_settled_q)
        if math.isfinite(max_pos_settled_q)
        else None,
        "max_late_tail10_reentry": float(max_late) if math.isfinite(max_late) else None,
        "best_settled_all": best_settled_all,
        "best_settled_quality": best_settled_q,
        "best_positive_settled_quality": best_pos_q,
        "best_late_reentry": best_late,
        "settled_reaches_lock": bool(
            math.isfinite(max_settled_all) and max_settled_all >= THETA_LOCK
        ),
        "quality_settled_reaches_lock": bool(
            math.isfinite(max_settled_q) and max_settled_q >= THETA_LOCK
        ),
    }


def ringdown_ladder(
    n0: float, Th0: float, kappa: float, gamma: float, dt: float = DT_DEFAULT
) -> List[Dict[str, float]]:
    """settled_mean vs settle_extra for one IC — shows ring-down to 0."""
    out = []
    for se in (0.0, 10.0, 20.0, 40.0, 80.0, 160.0):
        r = medium_rebound_0d(n0, Th0, kappa, gamma, settle_extra=se, dt=dt, t_max=400.0)
        out.append(
            {
                "settle_extra": se,
                "t_end": r["t_end"],
                "late_tail10": r["late_tail10"],
                "late_tail20": r["late_tail20"],
                "settled_mean": r["settled_mean"],
                "settled_std": r["settled_std"],
                "n_late": r["n_late"],
                "quality_ok": r["quality_ok"],
            }
        )
    return out


def script_sha256() -> str:
    p = Path(__file__).resolve()
    return hashlib.sha256(p.read_bytes()).hexdigest()


def row_brief(r: Optional[Dict[str, float]]) -> Optional[Dict[str, float]]:
    if r is None:
        return None
    keys = (
        "n0",
        "Theta0",
        "kappa",
        "gamma",
        "late_tail10",
        "late_tail20",
        "settled_mean",
        "settled_std",
        "quality_ok",
        "Theta_max_pos",
        "turned",
        "t_end",
        "settle_extra",
        "dt",
        "Hkin_Hdoor_settled",
        "Hkin_Hdoor_late",
    )
    return {k: r[k] for k in keys if k in r}


def main() -> None:
    print("=" * 78)
    print("SETTLED LATE Θ SCAN — F5 deepen (FA3 0D form only)")
    print("=" * 78)
    print(f"  package                       = {PACKAGE}")
    print(f"  prior                         = {PRIOR}")
    print(f"  Θ_lock (d=3)                  = {THETA_LOCK:.12f}  [= 1/√α]")
    print(f"  c_s                           = {C_S:.12f}")
    print(f"  |H_kin(Θ=1)|/H_door           = {H_KIN_OVER_H_DOOR_UNIT:.12f}")
    print(f"  S1_settled                    = mean(last 20% of Θ hist after settle)")
    print(f"  quality cut                   = settled_std < {SETTLED_STD_MAX}")
    print(f"  dt                            = {DT_DEFAULT}")
    print(f"  script_sha256                 = {script_sha256()}")
    print()
    print("  FORM:  dn/dt = −n Θ ;  dΘ/dt = −Θ² + κ(n−1) − γ Θ")
    print("  NO invent H_re · no free dial · leave MCMCs · production_3d=false")
    print()

    # --- analytic ---
    print("-" * 78)
    print("[0] Analytic fixed point / ring-down (stocked form)")
    print("-" * 78)
    analytic = analytic_fixed_point_report()
    print(f"  unique physical FP            = (n,Θ) = (1, 0)")
    print(f"  char poly                     = {analytic['char_poly']}")
    print(f"  asymptotic claim              = {analytic['claim']}")
    for c in analytic["linear_cases"]:
        print(
            f"    κ={c['kappa']:.2f} γ={c['gamma']:.2f}  "
            f"rate=γ/2={c['ringdown_rate_gamma_over_2']:.4f}  "
            f"{c['regime']}  t_1%≈{c['t_amplitude_1pct']:.2f}"
        )
    print()

    # --- primary scan: settle_extra=40 ---
    print("-" * 78)
    print("[1] Full stocked 0D scan  settle_extra=40  (S1_settled primary)")
    print("-" * 78)
    rows40, s40 = scan_settled(settle_extra=40.0, dt=DT_DEFAULT)
    print(f"  n_rows / physical / quality   = {s40['n_rows']} / {s40['n_physical']} / {s40['n_quality']}")
    print(f"  n_turned / blowups            = {s40['n_turned']} / {s40['n_blowup']}")
    print(f"  max settled_mean (all phys)   = {s40['max_settled_mean_all_physical']}")
    print(f"  max settled_mean (quality)    = {s40['max_settled_mean_quality']}")
    print(f"  max positive settled (qual)   = {s40['max_positive_settled_quality']}")
    print(f"  max re-entry late_tail10      = {s40['max_late_tail10_reentry']}")
    print(f"  settled ≥ Θ_lock?             = {s40['settled_reaches_lock']}")
    print(f"  quality settled ≥ Θ_lock?     = {s40['quality_settled_reaches_lock']}")
    bq = s40["best_positive_settled_quality"] or s40["best_settled_quality"]
    ba = s40["best_settled_all"]
    bl = s40["best_late_reentry"]
    if bq:
        print(
            f"  ARGMAX quality S1_settled     = "
            f"(n0={bq['n0']}, Θ0={bq['Theta0']}, κ={bq['kappa']}, γ={bq['gamma']}) "
            f"→ settled={bq['settled_mean']:+.6f} std={bq['settled_std']:.6f} "
            f"tail10={bq['late_tail10']:+.4f} tail20={bq['late_tail20']:+.4f}"
        )
    if ba:
        print(
            f"  ARGMAX all-phys S1_settled    = "
            f"(n0={ba['n0']}, Θ0={ba['Theta0']}, κ={ba['kappa']}, γ={ba['gamma']}) "
            f"→ settled={ba['settled_mean']:+.6f} std={ba['settled_std']:.6f}"
        )
    if bl:
        print(
            f"  ARGMAX re-entry late_tail10   = "
            f"(n0={bl['n0']}, Θ0={bl['Theta0']}, κ={bl['kappa']}, γ={bl['gamma']}) "
            f"→ tail10={bl['late_tail10']:+.4f} tail20={bl['late_tail20']:+.4f} "
            f"settled@{s40['settle_extra']}={bl['settled_mean']:+.6f} "
            f"std={bl['settled_std']:.6f}"
        )
    print()

    # --- secondary: settle_extra=20 (prior phase-2 comparable) ---
    print("-" * 78)
    print("[2] Scan settle_extra=20  (prior phase-2 comparable)")
    print("-" * 78)
    rows20, s20 = scan_settled(settle_extra=20.0, dt=DT_DEFAULT)
    print(f"  n_physical / quality          = {s20['n_physical']} / {s20['n_quality']}")
    print(f"  max settled (all / quality)   = "
          f"{s20['max_settled_mean_all_physical']} / {s20['max_settled_mean_quality']}")
    print(f"  max positive settled (qual)   = {s20['max_positive_settled_quality']}")
    bq20 = s20["best_positive_settled_quality"] or s20["best_settled_quality"]
    if bq20:
        print(
            f"  ARGMAX quality S1_settled     = "
            f"(n0={bq20['n0']}, Θ0={bq20['Theta0']}, κ={bq20['kappa']}, γ={bq20['gamma']}) "
            f"→ settled={bq20['settled_mean']:+.6f} std={bq20['settled_std']:.6f}"
        )
    print()

    # --- stocked default + prior best-late ladders ---
    print("-" * 78)
    print("[3] Ring-down ladders (settled_mean vs settle_extra)")
    print("-" * 78)
    ladder_def = ringdown_ladder(*STOCKED_DEFAULT)
    ladder_f5 = ringdown_ladder(*PRIOR_BEST_LATE)
    print("  STOCKED DEFAULT (6, −2, 1.5, 0.15):")
    for row in ladder_def:
        print(
            f"    se={row['settle_extra']:5.0f}  t_end={row['t_end']:7.2f}  "
            f"tail10={row['late_tail10']:+8.5f}  tail20={row['late_tail20']:+8.5f}  "
            f"settled={row['settled_mean']:+8.5f}  std={row['settled_std']:8.5f}  "
            f"q={int(row['quality_ok'])}"
        )
    print("  PRIOR F5 BEST-LATE (80, −8, 3, 0.02):")
    for row in ladder_f5:
        print(
            f"    se={row['settle_extra']:5.0f}  t_end={row['t_end']:7.2f}  "
            f"tail10={row['late_tail10']:+8.5f}  tail20={row['late_tail20']:+8.5f}  "
            f"settled={row['settled_mean']:+8.5f}  std={row['settled_std']:8.5f}  "
            f"q={int(row['quality_ok'])}"
        )
    print()

    # stocked default at primary settle
    r_def = medium_rebound_0d(*STOCKED_DEFAULT, settle_extra=40.0, dt=DT_DEFAULT)
    r_f5 = medium_rebound_0d(*PRIOR_BEST_LATE, settle_extra=40.0, dt=DT_DEFAULT)
    r_def0 = medium_rebound_0d(*STOCKED_DEFAULT, settle_extra=0.0, dt=DT_DEFAULT)
    r_f50 = medium_rebound_0d(*PRIOR_BEST_LATE, settle_extra=0.0, dt=DT_DEFAULT)

    print("-" * 78)
    print("[4] Fixed-point stamp (stocked default + F5 row @ se=40)")
    print("-" * 78)
    print(
        f"  stocked se=0   tail10={r_def0['late_tail10']:+.6f}  "
        f"tail20={r_def0['late_tail20']:+.6f}  settled={r_def0['settled_mean']:+.6f}  "
        f"std={r_def0['settled_std']:.6f}"
    )
    print(
        f"  stocked se=40  tail10={r_def['late_tail10']:+.6f}  "
        f"tail20={r_def['late_tail20']:+.6f}  settled={r_def['settled_mean']:+.6f}  "
        f"std={r_def['settled_std']:.6f}  n_late={r_def['n_late']:.6f}"
    )
    print(
        f"  F5best se=0    tail10={r_f50['late_tail10']:+.6f}  "
        f"tail20={r_f50['late_tail20']:+.6f}  settled={r_f50['settled_mean']:+.6f}  "
        f"std={r_f50['settled_std']:.6f}"
    )
    print(
        f"  F5best se=40   tail10={r_f5['late_tail10']:+.6f}  "
        f"tail20={r_f5['late_tail20']:+.6f}  settled={r_f5['settled_mean']:+.6f}  "
        f"std={r_f5['settled_std']:.6f}  n_late={r_f5['n_late']:.6f}"
    )
    print()

    # top quality positive survivors se=40
    qual40 = [r for r in rows40 if quality_cut(r) and r["settled_mean"] > 0.0]
    qual40_sorted = sorted(qual40, key=lambda r: r["settled_mean"], reverse=True)
    print("-" * 78)
    print("[5] Top quality positive S1_settled survivors (se=40, std<0.2)")
    print("-" * 78)
    print(
        f"  {'n0':>6} {'Θ0':>6} {'κ':>5} {'γ':>5}  "
        f"{'settled':>10} {'std':>8} {'tail10':>9} {'tail20':>9} {'peak':>8}"
    )
    for r in qual40_sorted[:15]:
        print(
            f"  {r['n0']:6.1f} {r['Theta0']:6.1f} {r['kappa']:5.2f} {r['gamma']:5.2f}  "
            f"{r['settled_mean']:+10.6f} {r['settled_std']:8.5f} "
            f"{r['late_tail10']:+9.4f} {r['late_tail20']:+9.4f} {r['Theta_max_pos']:8.3f}"
        )
    if not qual40_sorted:
        print("  (none — no quality-positive settled rows)")
    print()

    # also top all-physical settled (may fail quality)
    phys40 = [r for r in rows40 if row_physical(r)]
    phys40_sorted = sorted(phys40, key=lambda r: r["settled_mean"], reverse=True)
    print("-" * 78)
    print("[6] Top all-physical S1_settled (se=40; may fail quality cut)")
    print("-" * 78)
    for r in phys40_sorted[:10]:
        print(
            f"  (n0={r['n0']}, Θ0={r['Theta0']}, κ={r['kappa']}, γ={r['gamma']}) "
            f"settled={r['settled_mean']:+.6f} std={r['settled_std']:.5f} "
            f"q={int(r['quality_ok'])} tail10={r['late_tail10']:+.4f} "
            f"tail20={r['late_tail20']:+.4f}"
        )
    print()

    # --- verdict ---
    max_s_q = s40["max_positive_settled_quality"]
    if max_s_q is None or not math.isfinite(max_s_q):
        # fall back to best quality (may be negative)
        max_s_q = s40["max_settled_mean_quality"]
    max_s_all = s40["max_settled_mean_all_physical"]
    # primary headline: max positive quality settled; else max quality
    if (
        s40["max_positive_settled_quality"] is not None
        and math.isfinite(s40["max_positive_settled_quality"])
    ):
        headline = s40["max_positive_settled_quality"]
        headline_row = s40["best_positive_settled_quality"]
        headline_label = "max_positive_quality_settled_se40"
    else:
        headline = s40["max_settled_mean_quality"]
        headline_row = s40["best_settled_quality"]
        headline_label = "max_quality_settled_se40_may_be_nonpositive"

    # secondary headline se=20
    if (
        s20["max_positive_settled_quality"] is not None
        and math.isfinite(s20["max_positive_settled_quality"])
    ):
        headline20 = s20["max_positive_settled_quality"]
        headline20_row = s20["best_positive_settled_quality"]
    else:
        headline20 = s20["max_settled_mean_quality"]
        headline20_row = s20["best_settled_quality"]

    lock = bool(
        headline is not None
        and math.isfinite(float(headline))
        and float(headline) >= THETA_LOCK
    )
    ratio = (float(headline) / THETA_LOCK) if headline is not None and math.isfinite(float(headline)) else float("nan")

    if lock:
        grade = "UNEXPECTED-SETTLED-LOCK"
        s1_status = "CLAIM-REVIEW-REQUIRED"
        complete = 0  # still require red / construction review
    else:
        grade = "OPEN-BLOCKED"
        s1_status = "MISSING_INPUT"
        complete = 0

    production_3d = False
    page_curve_claimed = False

    # ring-down always-to-O(0.1) evidence from ladders + analytic
    se160_def = ladder_def[-1]["settled_mean"]
    se160_f5 = ladder_f5[-1]["settled_mean"]
    ringdown_o01 = (
        abs(se160_def) < 0.1
        and abs(se160_f5) < 0.1
        and abs(float(max_s_all or 0.0)) < 1.0  # all-phys max still O(1) or less
    )

    print("=" * 78)
    print("VERDICT — S1_settled vs Θ_lock")
    print("=" * 78)
    print(f"  medium turn (stocked 0D)        = YES (if any turned>0)")
    print(f"  MAX S1_settled (quality, se=40) = {headline}")
    print(f"  MAX S1_settled (all phys, se40) = {max_s_all}")
    print(f"  MAX S1_settled (quality, se=20) = {headline20}")
    print(f"  stocked default settled se=40   = {r_def['settled_mean']:+.6f}  std={r_def['settled_std']:.6f}")
    print(f"  prior F5-row settled se=40      = {r_f5['settled_mean']:+.6f}  std={r_f5['settled_std']:.6f}")
    print(f"  prior F5-row tail10@se0         = {r_f50['late_tail10']:+.6f}  tail20={r_f50['late_tail20']:+.6f}")
    print(f"  Θ_lock required                 = {THETA_LOCK:.6f}")
    print(f"  ratio S1_settled / Θ_lock       = {ratio:.6e}")
    print(f"  |H_kin(settled)|/H_door         = {hkin_over_hdoor(float(headline or 0.0)):.6e}")
    print(f"  S1_settled ≥ Θ_lock?            = {lock}")
    print(f"  S1 status                       = {s1_status}")
    print(f"  package grade                   = {grade}")
    print(f"  production 3D COMPLETE?         = {production_3d}")
    print(f"  COMPLETE count                  = {complete}")
    print(f"  page_curve_claimed              = {page_curve_claimed}")
    print(f"  ring-down → O(0.1) or below?    = {ringdown_o01}  (ladders + analytic FP)")
    print()
    print("  READ:")
    print("  1. S1_settled = last-20% mean after settle_extra (not re-entry tail10).")
    print("  2. Quality cut settled_std < 0.2 rejects residual ring-down noise.")
    print("  3. Unique physical FP of stocked ODE is (n,Θ)=(1,0); γ>0 ⇒ Θ→0.")
    print("  4. Prior +2.87 was re-entry tail10 window-choice; F5 residual closed as")
    print("     documentation: no stable positive late ⟨Θ⟩ near lock under stocked form.")
    print("  5. κ,γ remain toy reduced coeffs — not Derived cosmological dials.")
    print("  6. No claim: bounce closed · H_re Derived · Θ_lock derived · page curve.")
    print("  7. exit 0 ≠ PASS. production_3d false (0D instrument).")

    top_survivors = [
        {
            "n0": r["n0"],
            "Theta0": r["Theta0"],
            "kappa": r["kappa"],
            "gamma": r["gamma"],
            "settled_mean": r["settled_mean"],
            "settled_std": r["settled_std"],
            "late_tail10": r["late_tail10"],
            "late_tail20": r["late_tail20"],
            "Theta_max_pos": r["Theta_max_pos"],
            "Hkin_Hdoor_settled": r["Hkin_Hdoor_settled"],
            "quality_ok": r["quality_ok"],
        }
        for r in qual40_sorted[:15]
    ]

    summary = {
        "package": PACKAGE,
        "prior": PRIOR,
        "form": "FA3_0D_only",
        "S1_definition": "settled_mean = mean(last 20% of Θ history after settle_extra)",
        "quality_cut": f"settled_std < {SETTLED_STD_MAX}",
        "Theta_lock": THETA_LOCK,
        "c_s": C_S,
        "H_kin_over_H_door_at_Theta1": H_KIN_OVER_H_DOOR_UNIT,
        "dt": DT_DEFAULT,
        "script_sha256": script_sha256(),
        "headline_label": headline_label,
        "max_S1_settled_quality_se40": headline,
        "max_S1_settled_all_physical_se40": max_s_all,
        "max_S1_settled_quality_se20": headline20,
        "argmax_quality_se40": row_brief(headline_row),
        "argmax_quality_se20": row_brief(headline20_row),
        "argmax_all_physical_se40": row_brief(ba),
        "stocked_default_se0": row_brief(r_def0),
        "stocked_default_se40": row_brief(r_def),
        "prior_F5_best_late_se0": row_brief(r_f50),
        "prior_F5_best_late_se40": row_brief(r_f5),
        "ratio_S1_settled_over_lock": ratio,
        "H_kin_over_H_door_at_max_settled": hkin_over_hdoor(float(headline or 0.0)),
        "Theta_lock_reached_S1_settled": lock,
        "S1_status": s1_status,
        "grade": grade,
        "COMPLETE": complete,
        "production_3d": production_3d,
        "page_curve_claimed": page_curve_claimed,
        "ringdown_drives_settled_to_O0.1_or_below": ringdown_o01,
        "analytic": analytic,
        "scan_se40": {
            "n_rows": s40["n_rows"],
            "n_physical": s40["n_physical"],
            "n_quality": s40["n_quality"],
            "n_turned": s40["n_turned"],
            "max_settled_mean_all_physical": s40["max_settled_mean_all_physical"],
            "max_settled_mean_quality": s40["max_settled_mean_quality"],
            "max_positive_settled_quality": s40["max_positive_settled_quality"],
            "max_late_tail10_reentry": s40["max_late_tail10_reentry"],
            "settled_reaches_lock": s40["settled_reaches_lock"],
            "best_positive_settled_quality": row_brief(
                s40["best_positive_settled_quality"]
            ),
            "best_settled_all": row_brief(s40["best_settled_all"]),
            "best_late_reentry": row_brief(s40["best_late_reentry"]),
        },
        "scan_se20": {
            "n_physical": s20["n_physical"],
            "n_quality": s20["n_quality"],
            "max_settled_mean_all_physical": s20["max_settled_mean_all_physical"],
            "max_settled_mean_quality": s20["max_settled_mean_quality"],
            "max_positive_settled_quality": s20["max_positive_settled_quality"],
            "best_positive_settled_quality": row_brief(
                s20["best_positive_settled_quality"]
            ),
        },
        "ringdown_ladder_stocked_default": ladder_def,
        "ringdown_ladder_prior_F5_best_late": ladder_f5,
        "top_quality_positive_survivors_se40": top_survivors,
        "note": (
            "S1_settled only. Re-entry late_tail10 is diagnostic (F5). "
            "Peak spikes and 0D caps are not lands. 0D ≠ production 3D. "
            "COMPLETE=0. exit0≠PASS."
        ),
    }

    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(summary, indent=2, default=str))
    print("SUMMARY_JSON_END")

    # honesty asserts
    assert summary["COMPLETE"] == 0
    assert summary["production_3d"] is False
    assert summary["page_curve_claimed"] is False
    assert r_def["turned"] > 0.5, "stocked 0D must still turn"
    # F5 residual stamp: prior best-late se0 tail10 vs tail20 opposite or inconsistent
    assert r_f50["late_tail10"] > 1.0, "prior F5 row must still show large tail10"
    assert r_f50["late_tail20"] < 0.0, "prior F5 row tail20 must stay negative (F5)"
    # asymptotic: long-settle stocked |settled| small
    assert abs(ladder_def[-1]["settled_mean"]) < 0.05
    if not lock:
        assert summary["S1_status"] == "MISSING_INPUT"
        assert summary["grade"] == "OPEN-BLOCKED"
    print()
    print("ASSERTS OK — S1_settled ≪ Θ_lock; F5 residual documented; not 3D COMPLETE.")
    print("=" * 78)
    # exit 0 = compute finished; grade is OPEN-BLOCKED above (exit0 ≠ PASS)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
