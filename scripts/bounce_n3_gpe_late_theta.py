#!/usr/bin/env python3
"""bounce_n3_gpe_late_theta — production-class GPE late-Θ instrument (N3 deepen).

PACKAGE
  docs/working_logs/_runs/theory_construction_20260804/n3_gpe_late_theta_20260804/

MISSION
  Push stocked GPE / 1D / 2D / spherical instruments as hard as LEGAL
  (no invented force laws) and report LATE / SETTLED mean Θ — not peak
  spikes and not Madelung vacuum singularities — vs Θ_lock ≈ 11.71 and
  |H_kin|/H_door bookkeeping.

PRIOR
  n3_theta_3d_20260804: peak can hit ~11.7 but late Θ ≲ 1.8 ≪ lock
  (PEAK_VS_LATE.md). This package deepens the late metric and instrument
  grid without rebranding peak as lock.

STOCKED FORMS ONLY
  (0D)  dn/dt = −n Θ ;  dΘ/dt = −Θ² + κ(n−1) − γ Θ     [FA3/N1]
  (1D)  i ∂t ψ = −½ ∂xx ψ + (|ψ|² − 1) ψ               [M6 Cartesian]
  (sph) same GPE, spherical u=rψ, DST kinetic            [M6 dst scheme]
  (2D)  same GPE, pancake split-step                     [transverse_2d]
  (avg) coarse mass-weighted stress identity             [averaging]

HARD RULES
  - S1 lock metric = late / settled mass-weighted ⟨Θ⟩ only
  - NOT: 0D |Θ| caps, Madelung vacuum spikes, peak spikes
  - No invent H_re · no bounce closed · no free dial · leave MCMCs
  - No PolyChord · page_curve_claimed stays false
  - exit 0 = compute finished; PASS/FAIL is physics grade in SUMMARY
  - production 3D COMPLETE almost never — grade honesty required

Θ_lock (N1 / FA3 shear-door, d=3):
  Θ_lock = d / (c_s √3) ≈ 11.71
  |H_kin|/H_door = |Θ| · c_s / √3   (d=3; =1 at lock)
"""
from __future__ import annotations

import json
import math
import sys
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# anchors (disk / book)
# ---------------------------------------------------------------------------
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
D_LOCK = 3
THETA_LOCK = D_LOCK / (C_S * math.sqrt(3.0))  # ≈ 11.706
H_KIN_OVER_H_DOOR_UNIT = C_S / math.sqrt(3.0)  # |H_kin|/H_door at Θ=1, d=3
TH_CAP = 80.0  # 0D safety; rows that hit are unphysical


def hkin_over_hdoor(Theta: float, d: int = D_LOCK) -> float:
    """|H_kin(Θ)|/H_door with H_kin=Θ c_s/(d ξ), H_door=1/(√3 ξ)."""
    return abs(Theta) * C_S * math.sqrt(3.0) / float(d)


# ---------------------------------------------------------------------------
# late / settled window helpers
# ---------------------------------------------------------------------------
def late_windows(hist: np.ndarray) -> Dict[str, float]:
    """Multiple honest late readouts from a 1D history array."""
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
    # settled = last 20% mean; std measures residual drift
    tail = a[-n20:]
    return {
        "late_tail10": float(np.mean(a[-n10:])),
        "late_tail20": float(np.mean(tail)),
        "late_last": float(a[-1]),
        "settled_mean": float(np.mean(tail)),
        "settled_std": float(np.std(tail)),
    }


# ---------------------------------------------------------------------------
# [A] 0D reduced stress-channel ODE (stocked FA3/N1)
# ---------------------------------------------------------------------------
def medium_rebound_0d(
    n0: float = 6.0,
    Theta0: float = -2.0,
    kappa: float = 1.5,
    gamma: float = 0.15,
    t_max: float = 40.0,
    dt: float = 1e-3,
    settle_extra: float = 0.0,
) -> Dict[str, float]:
    """Stocked reduced ODE.

    Primary late (S1 re-entry-candidate style, prior-comparable):
      integrate to max(t_npeak+8, …) then mean of last 10% of Θ history.
    Settled (honesty): continue settle_extra healing times past that cut and
      report mean of final 20% — often ≪ re-entry-window late.
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
    t_cut_reentry = t_max  # updated once density peaks
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
        # prior-comparable re-entry window end
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

    # re-entry-window late: last 10% of history up to re-entry cut
    if cut_set and settle_extra > 0.0:
        # reconstruct index near t_cut_reentry
        n_re = max(1, int(round(t_cut_reentry / dt)))
        n_re = min(n_re, th_a.size)
        re_hist = th_a[:n_re]
    else:
        re_hist = th_a
    n10 = max(1, re_hist.size // 10)
    late_reentry = float(np.mean(re_hist[-n10:])) if re_hist.size else float("nan")

    lw = late_windows(th_a)  # full trajectory incl. settle_extra
    s1_late = late_reentry  # primary S1 re-entry-candidate metric

    return {
        "n0": float(n0),
        "Theta0": float(Theta0),
        "kappa": float(kappa),
        "gamma": float(gamma),
        "turned": float(turned),
        "t_cross": float(t_cross) if turned else float("nan"),
        "dTheta_dt_cross": float(dth_at_cross) if turned else float("nan"),
        "late_Theta": float(s1_late),
        "late_tail10": float(s1_late),
        "late_tail20": float(np.mean(re_hist[-max(1, re_hist.size // 5) :]))
        if re_hist.size
        else float("nan"),
        "late_last": float(re_hist[-1]) if re_hist.size else float("nan"),
        "settled_mean": lw["settled_mean"],
        "settled_std": lw["settled_std"],
        "settled_last": lw["late_last"],
        "overshoot": n_peak / max(n0, 1e-12),
        "n_peak": float(n_peak),
        "n_late": float(n_a[-1]) if n_a.size else float("nan"),
        "Theta_max_pos": float(th_max_pos),
        "Theta_max_abs": float(th_max_abs),
        "hit_cap": float(hit_cap),
        "t_end": float(t),
        "t_cut_reentry": float(t_cut_reentry) if cut_set else float(t),
        "Hkin_Hdoor_late": hkin_over_hdoor(s1_late),
        "Hkin_Hdoor_settled": hkin_over_hdoor(lw["settled_mean"]),
        "Hkin_Hdoor_peak": hkin_over_hdoor(th_max_pos),
    }


def row_physical_0d(r: Dict[str, float]) -> bool:
    if r["hit_cap"] > 0.5:
        return False
    if r["overshoot"] > 100.0:
        return False
    if not math.isfinite(r["late_Theta"]):
        return False
    return True


def scan_0d_deep() -> Tuple[List[Dict[str, float]], Dict[str, Any]]:
    """Denser legal grid than n3_theta_lock_scan; still stocked ODE only.

    Phase 1: re-entry-window late (prior-comparable, settle_extra=0).
    Phase 2: re-run top late rows with settle_extra=20 for settled honesty.
    """
    rows: List[Dict[str, float]] = []

    # axis A: n0 × Θ0 at stocked (κ,γ)
    for n0 in (2.0, 3.0, 6.0, 11.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0):
        for Th0 in (-0.5, -1.0, -1.5, -2.0, -3.0, -4.0, -5.0, -6.0, -8.0):
            rows.append(medium_rebound_0d(n0, Th0, 1.5, 0.15))

    # axis B: κ × γ at stocked (6,−2)
    for kappa in (0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0):
        for gamma in (0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.30, 0.50):
            rows.append(medium_rebound_0d(6.0, -2.0, kappa, gamma))

    # axis C: high-compression corner densification (prior best late region)
    for n0 in (20.0, 30.0, 40.0, 50.0, 60.0, 80.0):
        for Th0 in (-3.0, -5.0, -6.0, -8.0):
            for kappa in (2.0, 3.0, 4.0, 5.0):
                for gamma in (0.02, 0.05, 0.08, 0.10, 0.15):
                    rows.append(medium_rebound_0d(n0, Th0, kappa, gamma))

    # axis D: mild/corpus FA3 points with κγ spread
    for n0, Th0 in ((3.0, -1.0), (6.0, -1.0), (6.0, -2.0), (11.0, -2.0), (11.0, -3.0)):
        for kappa in (1.0, 1.5, 2.0, 3.0):
            for gamma in (0.05, 0.10, 0.15, 0.30):
                rows.append(medium_rebound_0d(n0, Th0, kappa, gamma))

    # dedupe
    seen = set()
    unique: List[Dict[str, float]] = []
    for r in rows:
        key = (r["n0"], r["Theta0"], r["kappa"], r["gamma"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(r)

    physical = [r for r in unique if row_physical_0d(r)]
    blowups = [r for r in unique if not row_physical_0d(r)]
    turned = [r for r in physical if r["turned"] > 0.5]
    max_late = max((r["late_Theta"] for r in physical), default=float("-inf"))
    max_pos = max((r["Theta_max_pos"] for r in physical), default=0.0)
    best_late = max(physical, key=lambda r: r["late_Theta"]) if physical else None
    best_peak = max(physical, key=lambda r: r["Theta_max_pos"]) if physical else None

    # Phase 2: settle honesty on top late survivors + stocked default
    settle_targets = sorted(physical, key=lambda r: r["late_Theta"], reverse=True)[:20]
    settle_targets.append(medium_rebound_0d(6.0, -2.0, 1.5, 0.15))
    settled_rows: List[Dict[str, float]] = []
    for r in settle_targets:
        rs = medium_rebound_0d(
            r["n0"], r["Theta0"], r["kappa"], r["gamma"], settle_extra=20.0
        )
        if row_physical_0d(rs):
            settled_rows.append(rs)
            # attach settled onto matching unique row
            for u in unique:
                if (
                    u["n0"] == rs["n0"]
                    and u["Theta0"] == rs["Theta0"]
                    and u["kappa"] == rs["kappa"]
                    and u["gamma"] == rs["gamma"]
                ):
                    u["settled_mean"] = rs["settled_mean"]
                    u["settled_std"] = rs["settled_std"]
                    u["settled_last"] = rs["settled_last"]
                    u["Hkin_Hdoor_settled"] = rs["Hkin_Hdoor_settled"]
                    break

    max_settled = max(
        (r["settled_mean"] for r in settled_rows if math.isfinite(r["settled_mean"])),
        default=float("-inf"),
    )
    best_settled = (
        max(settled_rows, key=lambda r: r["settled_mean"]) if settled_rows else None
    )

    peak_hits = [r for r in physical if r["Theta_max_pos"] >= THETA_LOCK]
    late_among_peak = (
        max(r["late_Theta"] for r in peak_hits) if peak_hits else float("nan")
    )

    return unique, {
        "n_rows": len(unique),
        "n_physical": len(physical),
        "n_blowup_rejected": len(blowups),
        "n_turned": len(turned),
        "max_late_Theta": float(max_late) if math.isfinite(max_late) else 0.0,
        "max_settled_mean": float(max_settled) if math.isfinite(max_settled) else 0.0,
        "max_Theta_pos_physical": float(max_pos),
        "best_late": best_late,
        "best_settled": best_settled,
        "best_peak": best_peak,
        "n_peak_ge_lock": len(peak_hits),
        "max_late_among_peak_hits": (
            float(late_among_peak) if math.isfinite(late_among_peak) else None
        ),
        "n_settled_probed": len(settled_rows),
        "late_reaches_lock": bool(max_late >= THETA_LOCK),
        "settled_reaches_lock": bool(
            math.isfinite(max_settled) and max_settled >= THETA_LOCK
        ),
        "peak_reaches_lock": bool(max_pos >= THETA_LOCK),
    }


# ---------------------------------------------------------------------------
# [B] 1D Cartesian GPE (M6 stocked form) — late mass-weighted ⟨Θ⟩
# ---------------------------------------------------------------------------
def gpe_1d_late_theta(
    A: float,
    v0: float,
    R: float = 8.0,
    L: float = 80.0,
    N: int = 768,
    DT: float = 1.25e-3,
    T_MAX: float = 16.0,
) -> Dict[str, float]:
    """Repulsive GPE; S1 readout = late mass-weighted ⟨∂x v⟩."""
    dx = L / N
    x = np.linspace(-L / 2, L / 2, N, endpoint=False)
    k2 = 0.5 * (2.0 * math.pi * np.fft.fftfreq(N, d=dx)) ** 2
    n0 = 1.0 + A * np.exp(-((x / R) ** 2))
    v = -v0 * (x / R) * np.exp(-0.5 * (x / R) ** 2)
    phase = np.cumsum(v) * dx
    psi = np.sqrt(n0) * np.exp(1j * phase)

    def energy(psi_):
        nn = np.abs(psi_) ** 2
        dpsi = np.gradient(psi_, dx)
        return float(
            0.5 * np.sum(np.abs(dpsi) ** 2) * dx
            + 0.5 * np.sum((nn - 1.0) ** 2) * dx
        )

    def theta_stats(psi_):
        nn = np.abs(psi_) ** 2
        dpsi = np.gradient(psi_, dx)
        J = np.imag(np.conj(psi_) * dpsi)
        vf = J / np.maximum(nn, 1e-12)
        Th = np.gradient(vf, dx)
        w = nn / max(float(nn.sum()), 1e-30)
        mean_th = float((w * Th).sum())
        support = nn > 0.05
        max_th_support = float(Th[support].max()) if np.any(support) else float(Th.max())
        max_th_raw = float(Th.max())
        return mean_th, max_th_support, max_th_raw, float(nn.max())

    e0 = energy(psi)
    steps = int(T_MAX / DT)
    sample = max(1, int(0.1 / DT))
    mean_hist: List[float] = []
    max_sup_hist: List[float] = []
    max_raw_hist: List[float] = []
    nmax_hist: List[float] = []
    t_hist: List[float] = []
    for s in range(steps):
        nn = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (nn - 1.0))
        psi = np.fft.ifft(np.exp(-1j * DT * k2) * np.fft.fft(psi))
        nn = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (nn - 1.0))
        if s % sample == 0:
            m, ms, mr, nmax = theta_stats(psi)
            mean_hist.append(m)
            max_sup_hist.append(ms)
            max_raw_hist.append(mr)
            nmax_hist.append(nmax)
            t_hist.append(s * DT)

    e1 = energy(psi)
    mean_a = np.asarray(mean_hist)
    max_sup_a = np.asarray(max_sup_hist)
    max_raw_a = np.asarray(max_raw_hist)
    nmax_a = np.asarray(nmax_hist)
    kpk = int(np.argmax(nmax_a))
    lw = late_windows(mean_a)
    turned = float(nmax_a[-1]) < 0.95 * float(nmax_a[kpk])
    mean_turn = any(
        mean_a[i - 1] < 0.0 <= mean_a[i] for i in range(1, len(mean_a))
    )
    # post-peak late mean Θ (after density peak)
    post = mean_a[kpk:] if kpk < len(mean_a) else mean_a
    post_late = float(np.mean(post[max(1, len(post) // 2) :])) if len(post) else float(
        "nan"
    )
    s1_late = lw["late_tail10"]

    return {
        "A": float(A),
        "v0": float(v0),
        "R": float(R),
        "n_init": 1.0 + A,
        "n_peak": float(nmax_a[kpk]),
        "overshoot": float(nmax_a[kpk]) / max(1.0 + A, 1e-12),
        "turned_density": float(turned),
        "mean_Theta_turn": float(mean_turn),
        "mean_Theta_max": float(mean_a.max()) if mean_a.size else float("nan"),
        "mean_Theta_min": float(mean_a.min()) if mean_a.size else float("nan"),
        "mean_Theta_late": float(s1_late),
        "late_tail20": lw["late_tail20"],
        "settled_mean": lw["settled_mean"],
        "settled_std": lw["settled_std"],
        "post_peak_late": float(post_late),
        "support_Theta_max": float(max_sup_a.max()) if max_sup_a.size else float("nan"),
        "support_Theta_late": float(np.mean(max_sup_a[-max(1, len(max_sup_a)//10):]))
        if max_sup_a.size
        else float("nan"),
        "raw_local_Theta_max": float(max_raw_a.max()) if max_raw_a.size else float("nan"),
        "dE_frac": abs(e1 - e0) / max(e0, 1e-12),
        "Hkin_Hdoor_late": hkin_over_hdoor(s1_late),
        "Hkin_Hdoor_mean_max": hkin_over_hdoor(
            float(mean_a.max()) if mean_a.size else 0.0
        ),
        "T_MAX": float(T_MAX),
    }


def scan_1d_deep() -> Tuple[List[Dict[str, float]], Dict[str, Any]]:
    """Harder 1D GPE sweep: more (A,v0,R), longer late window than prior N3."""
    cases: List[Tuple[float, float, float]] = []
    # corpus M6 + high-A / high-v0 push (still stocked repulsive GPE)
    for A, v0 in (
        (2.0, 0.5),
        (5.0, 1.0),
        (10.0, 1.0),
        (5.0, 2.0),
        (20.0, 1.0),
        (5.0, 3.0),
        (30.0, 1.0),
        (50.0, 1.0),
        (20.0, 3.0),
        (10.0, 2.0),
    ):
        cases.append((A, v0, 8.0))
    # R variation (width)
    for R in (4.0, 12.0):
        cases.append((10.0, 1.0, R))
        cases.append((20.0, 1.0, R))

    rows = [gpe_1d_late_theta(A, v0, R=R) for A, v0, R in cases]
    clean = [r for r in rows if r["dE_frac"] < 0.05]
    max_mean = max((r["mean_Theta_max"] for r in clean), default=0.0)
    max_late = max((r["mean_Theta_late"] for r in clean), default=0.0)
    max_settled = max((r["settled_mean"] for r in clean), default=0.0)
    max_raw = max((r["raw_local_Theta_max"] for r in clean), default=0.0)
    best_late = max(clean, key=lambda r: r["mean_Theta_late"]) if clean else None
    return rows, {
        "n_rows": len(rows),
        "n_clean": len(clean),
        "max_mean_Theta": float(max_mean),
        "max_late_mean_Theta": float(max_late),
        "max_settled_mean": float(max_settled),
        "max_support_Theta": max(
            (r["support_Theta_max"] for r in clean), default=0.0
        ),
        "max_raw_local_Theta": float(max_raw),
        "max_overshoot": max((r["overshoot"] for r in clean), default=0.0),
        "best_late": best_late,
        "mean_reaches_lock": bool(max_mean >= THETA_LOCK),
        "late_mean_reaches_lock": bool(max_late >= THETA_LOCK),
        "settled_reaches_lock": bool(max_settled >= THETA_LOCK),
        "support_local_note": "support/raw local Θ = Madelung diagnostic, not S1",
    }


# ---------------------------------------------------------------------------
# [C] Spherical GPE light probe (M6 DST form) — mass-weighted ∇·v
# ---------------------------------------------------------------------------
def gpe_sph_late_theta(
    A: float,
    v0: float,
    L: float = 80.0,
    N: int = 1000,
    R_BLOB: float = 16.0,
    DT_MAX: float = 3.0e-3,
    PHI_TOL: float = 0.12,
    T_MAX: float = 24.0,
    MAX_STEPS: int = 80_000,
) -> Dict[str, float]:
    """Spherical repulsive GPE via DST kinetic (stocked bounce_m6_rebound_dst).

    Readout: mass-weighted Θ_3d = ⟨∂r vr + 2 vr/r⟩ with volume weight r².
    Coarser than production M6 focusing table — Θ instrument, not MeV F.
    Kinetic step evolves w = u − r (Dirichlet deviation), matching stocked v3.
    """
    from scipy.fft import dst, idst

    dr = L / N
    r = np.arange(1, N) * dr
    k = np.pi * np.arange(1, N) / L

    nprof = 1.0 + A / np.cosh(r / R_BLOB) ** 2
    vel = -v0 * (r / R_BLOB) * np.exp(-0.5 * (r / R_BLOB) ** 2)
    phase = np.concatenate(([0.0], np.cumsum(0.5 * (vel[1:] + vel[:-1]) * dr)))
    u = r * np.sqrt(nprof) * np.exp(1j * phase)

    def energy(u_):
        psi = u_ / r
        dpsi = np.gradient(psi, dr)
        dens = 0.5 * np.abs(dpsi) ** 2 + 0.5 * (np.abs(psi) ** 2 - 1.0) ** 2
        return float(np.trapezoid(dens * r**2, dx=dr))

    def theta_mean(u_):
        psi = u_ / r
        nn = np.abs(psi) ** 2
        dpsi = np.gradient(psi, dr)
        J = np.imag(np.conj(psi) * dpsi)
        vr = J / np.maximum(nn, 1e-12)
        dvr = np.gradient(vr, dr)
        Th = dvr + 2.0 * vr / np.maximum(r, dr)
        wt = nn * r**2
        wsum = float(np.sum(wt))
        if wsum <= 0:
            return 0.0, float(nn.max())
        return float(np.sum(wt * Th) / wsum), float(nn.max())

    e0 = energy(u)
    t = 0.0
    steps = 0
    mean_hist: List[float] = []
    nmax_hist: List[float] = []
    next_sample = 0.0
    n_peak = 0.0
    t_peak = 0.0

    while t < T_MAX and steps < MAX_STEPS:
        psi2 = np.abs(u / r) ** 2
        vmax = float(np.max(np.abs(psi2 - 1.0)))
        dt = min(DT_MAX, PHI_TOL / max(vmax, 1e-12))
        # Strang: half potential, full kinetic on w=u-r (stocked dst), half pot
        w = u * np.exp(-0.5j * dt * (psi2 - 1.0)) - r
        wh = dst(w.real, type=1) + 1j * dst(w.imag, type=1)
        wh *= np.exp(-0.5j * dt * k**2)
        w = idst(wh.real, type=1) + 1j * idst(wh.imag, type=1)
        u = w + r
        psi2 = np.abs(u / r) ** 2
        u = u * np.exp(-0.5j * dt * (psi2 - 1.0))
        t += dt
        steps += 1
        nm = float(np.max(np.abs(u / r) ** 2))
        if nm > n_peak:
            n_peak, t_peak = nm, t
        if t >= next_sample:
            next_sample += 0.25
            mth, nm2 = theta_mean(u)
            mean_hist.append(mth)
            nmax_hist.append(nm2)
            if t > t_peak + 8.0 and nm2 < 0.25 * max(n_peak, 1e-12) and t > 12.0:
                break

    e1 = energy(u)
    mean_a = np.asarray(mean_hist) if mean_hist else np.array([0.0])
    nmax_a = np.asarray(nmax_hist) if nmax_hist else np.array([1.0 + A])
    kpk = int(np.argmax(nmax_a))
    lw = late_windows(mean_a)
    turned = float(nmax_a[-1]) < 0.95 * float(nmax_a[kpk])
    s1 = lw["late_tail10"]
    return {
        "A": float(A),
        "v0": float(v0),
        "n_init": 1.0 + A,
        "n_peak": float(n_peak),
        "overshoot": float(n_peak) / max(1.0 + A, 1e-12),
        "t_peak": float(t_peak),
        "t_end": float(t),
        "steps": float(steps),
        "turned_density": float(turned),
        "mean_Theta_max": float(mean_a.max()),
        "mean_Theta_min": float(mean_a.min()),
        "mean_Theta_late": float(s1),
        "settled_mean": lw["settled_mean"],
        "settled_std": lw["settled_std"],
        "dE_frac": abs(e1 - e0) / max(abs(e0), 1e-12),
        "Hkin_Hdoor_late": hkin_over_hdoor(s1),
        "N_grid": float(N),
        "note": "spherical symmetry ≠ full 3D production",
    }


def scan_sph_light() -> Tuple[List[Dict[str, float]], Dict[str, Any]]:
    # light set — full M6 production focusing is separate; this is Θ late only
    cases = [
        (5.0, 1.0),
        (20.0, 1.0),
    ]
    rows: List[Dict[str, float]] = []
    for A, v0 in cases:
        try:
            rows.append(gpe_sph_late_theta(A, v0))
        except Exception as exc:  # noqa: BLE001 — instrument must continue
            rows.append(
                {
                    "A": float(A),
                    "v0": float(v0),
                    "n_init": 1.0 + A,
                    "n_peak": float("nan"),
                    "overshoot": float("nan"),
                    "t_peak": float("nan"),
                    "t_end": float("nan"),
                    "steps": 0.0,
                    "turned_density": 0.0,
                    "mean_Theta_max": float("nan"),
                    "mean_Theta_min": float("nan"),
                    "mean_Theta_late": float("nan"),
                    "settled_mean": float("nan"),
                    "settled_std": float("nan"),
                    "dE_frac": 1.0,
                    "Hkin_Hdoor_late": float("nan"),
                    "N_grid": 2400.0,
                    "note": f"FAILED: {exc}",
                }
            )
    clean = [
        r
        for r in rows
        if math.isfinite(r.get("dE_frac", 1.0))
        and r["dE_frac"] < 0.05
        and math.isfinite(r.get("mean_Theta_late", float("nan")))
    ]
    max_late = max((r["mean_Theta_late"] for r in clean), default=0.0)
    max_mean = max((r["mean_Theta_max"] for r in clean), default=0.0)
    return rows, {
        "n_rows": len(rows),
        "n_clean": len(clean),
        "max_late_mean_Theta": float(max_late),
        "max_mean_Theta": float(max_mean),
        "late_reaches_lock": bool(max_late >= THETA_LOCK),
        "production_3d": False,
        "symmetry": "spherical (not full 3D)",
    }


# ---------------------------------------------------------------------------
# [D] 2D pancake late ⟨Θ_xx⟩ (stocked transverse form, reduced grid)
# ---------------------------------------------------------------------------
def gpe_2d_late_theta(
    Lx: float = 160.0,
    Ly: float = 40.0,
    Nx: int = 384,
    Ny: int = 96,
    DT: float = 3.0e-3,
    T_MAX: float = 14.0,
    V: float = 2.0,
    V2: float = 0.6,
    seed: int = 11,
) -> Dict[str, float]:
    """2D GPE pancake; late mass-weighted ⟨∂x vx⟩, ⟨∂y vy⟩."""
    from numpy.fft import fft2, ifft2, fftfreq

    dx, dy = Lx / Nx, Ly / Ny
    x = np.arange(Nx) * dx
    y = np.arange(Ny) * dy
    X, Y = np.meshgrid(x, y, indexing="ij")
    kx = 2 * np.pi * fftfreq(Nx, dx)
    ky = 2 * np.pi * fftfreq(Ny, dy)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    K2 = KX**2 + KY**2

    def wrapx(d):
        return (d + Lx / 2.0) % Lx - Lx / 2.0

    rng = np.random.default_rng(seed)
    X_A, W_SEED, D_SEED = 40.0, 5.0, 0.25
    theta = (V * Lx / (4 * math.pi)) * np.cos(4 * math.pi * (X - X_A) / Lx) + (
        V2 * Lx / (2 * math.pi)
    ) * np.cos(2 * math.pi * (X - X_A) / Lx)
    rho = (
        1.0
        + D_SEED * np.exp(-(wrapx(X - X_A) / W_SEED) ** 2)
        + D_SEED * np.exp(-(wrapx(X - (X_A + Lx / 2)) / W_SEED) ** 2)
    )
    for _ in range(8):
        kxn = rng.integers(1, 5)
        kyn = rng.integers(1, 5)
        ph1, ph2 = rng.uniform(0, 2 * math.pi, 2)
        rho += 1e-3 * np.cos(2 * math.pi * kxn * X / Lx + ph1) * np.cos(
            2 * math.pi * kyn * Y / Ly + ph2
        )
    rho = np.maximum(rho, 1e-8)
    psi = np.sqrt(rho) * np.exp(1j * theta)

    def energy(psi_):
        nn = np.abs(psi_) ** 2
        px = ifft2(1j * KX * fft2(psi_))
        py = ifft2(1j * KY * fft2(psi_))
        return float(
            0.5 * np.sum(np.abs(px) ** 2 + np.abs(py) ** 2) * dx * dy
            + 0.5 * np.sum((nn - 1.0) ** 2) * dx * dy
        )

    def axis_theta(psi_):
        nn = np.abs(psi_) ** 2
        px = ifft2(1j * KX * fft2(psi_))
        py = ifft2(1j * KY * fft2(psi_))
        Jx = np.imag(np.conj(psi_) * px)
        Jy = np.imag(np.conj(psi_) * py)
        vx = Jx / np.maximum(nn, 1e-12)
        vy = Jy / np.maximum(nn, 1e-12)
        # derivatives via FFT
        dvx_dx = np.real(ifft2(1j * KX * fft2(vx)))
        dvy_dy = np.real(ifft2(1j * KY * fft2(vy)))
        w = nn / max(float(nn.sum()), 1e-30)
        Th_xx = float(np.sum(w * dvx_dx))
        Th_yy = float(np.sum(w * dvy_dy))
        return Th_xx, Th_yy, float(nn.max())

    e0 = energy(psi)
    steps = int(T_MAX / DT)
    sample = max(1, int(0.25 / DT))
    thx_hist: List[float] = []
    thy_hist: List[float] = []
    nmax_hist: List[float] = []
    for s in range(steps):
        nn = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (nn - 1.0))
        psi = ifft2(np.exp(-0.5j * DT * K2) * fft2(psi))
        nn = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (nn - 1.0))
        if s % sample == 0:
            tx, ty, nm = axis_theta(psi)
            thx_hist.append(tx)
            thy_hist.append(ty)
            nmax_hist.append(nm)

    e1 = energy(psi)
    thx = np.asarray(thx_hist)
    thy = np.asarray(thy_hist)
    lwx = late_windows(thx)
    lwy = late_windows(thy)
    return {
        "mean_Theta_xx_max": float(thx.max()) if thx.size else float("nan"),
        "mean_Theta_xx_min": float(thx.min()) if thx.size else float("nan"),
        "mean_Theta_xx_late": lwx["late_tail10"],
        "settled_Theta_xx": lwx["settled_mean"],
        "mean_Theta_yy_max": float(np.max(np.abs(thy))) if thy.size else float("nan"),
        "mean_Theta_yy_late": lwy["late_tail10"],
        "n_peak": float(max(nmax_hist)) if nmax_hist else float("nan"),
        "dE_frac": abs(e1 - e0) / max(abs(e0), 1e-12),
        "Hkin_Hdoor_xx_late": hkin_over_hdoor(lwx["late_tail10"]),
        "Nx": float(Nx),
        "Ny": float(Ny),
        "note": "2D pancake; not isotropic 3D production",
    }


# ---------------------------------------------------------------------------
# [E] synthetic averaging stress (static FA3 stand-in) + CG dynamic probe
# ---------------------------------------------------------------------------
def averaging_stress_static() -> Dict[str, float]:
    L, N = 80.0, 1024
    x = np.linspace(0, L, N, endpoint=False)
    dx = L / N
    rho = (
        1.0
        + 2.0 * np.exp(-((x - 20.0) / 4.0) ** 2)
        + 2.0 * np.exp(-((x - 60.0) / 4.0) ** 2)
    )
    v = 0.5 * (
        (x - 20.0) / 4.0 * np.exp(-0.5 * ((x - 20.0) / 4.0) ** 2)
        + (x - 60.0) / 4.0 * np.exp(-0.5 * ((x - 60.0) / 4.0) ** 2)
    )
    w = rho / rho.sum()
    Th = np.gradient(v, dx)
    mean_Th = float((w * Th).sum())
    var_Th = float((w * (Th - mean_Th) ** 2).sum())
    Pi = 0.5 * rho**2
    dPi = np.gradient(Pi, dx)
    force = np.gradient(dPi / np.maximum(rho, 1e-12), dx)
    stress = -float((w * force).sum())
    return {
        "mean_Theta": mean_Th,
        "var_Theta": var_Th,
        "stress_drive": stress,
        "net_rhs": -(mean_Th**2) - var_Th + stress,
        "max_local_abs_Theta": float(np.max(np.abs(Th))),
    }


def averaging_dynamic_late(
    L: float = 160.0,
    N: int = 1280,
    DT: float = 2.0e-3,
    T_MAX: float = 20.0,
) -> Dict[str, float]:
    """Coarse-grained ⟨Θ⟩ late from stocked averaging IC (V=2,V2=0.6)."""
    x = np.arange(N) * (L / N)
    dx = L / N
    k = 2.0 * np.pi * np.fft.fftfreq(N, dx)
    X_A, V, V2, W_SEED, D_SEED = 40.0, 2.0, 0.6, 5.0, 0.25

    def wrap(d):
        return (d + L / 2.0) % L - L / 2.0

    theta = (V * L / (4 * math.pi)) * np.cos(4 * math.pi * (x - X_A) / L) + (
        V2 * L / (2 * math.pi)
    ) * np.cos(2 * math.pi * (x - X_A) / L)
    rho = (
        1.0
        + D_SEED * np.exp(-(wrap(x - X_A) / W_SEED) ** 2)
        + D_SEED * np.exp(-(wrap(x - (X_A + L / 2)) / W_SEED) ** 2)
    )
    psi = np.sqrt(rho) * np.exp(1j * theta)

    SIG_CG = 2.0
    KERNEL = np.exp(-0.5 * (SIG_CG * k) ** 2)

    def smooth(f):
        return np.real(np.fft.ifft(KERNEL * np.fft.fft(f)))

    def mean_theta(psi_):
        rho_ = np.abs(psi_) ** 2
        px = np.fft.ifft(1j * k * np.fft.fft(psi_))
        J = np.imag(np.conj(psi_) * px)
        rho_c = smooth(rho_)
        J_c = smooth(J)
        v_c = J_c / np.maximum(rho_c, 1e-6)
        th = (np.roll(v_c, -1) - np.roll(v_c, 1)) / (2 * dx)
        w = rho_c / rho_c.sum()
        return float((w * th).sum()), float(rho_.max())

    def energy(psi_):
        nn = np.abs(psi_) ** 2
        dpsi = np.gradient(psi_, dx)
        return float(
            0.5 * np.sum(np.abs(dpsi) ** 2) * dx
            + 0.5 * np.sum((nn - 1.0) ** 2) * dx
        )

    e0 = energy(psi)
    k2 = 0.5 * k**2
    steps = int(T_MAX / DT)
    sample = max(1, int(0.05 / DT))
    mean_hist: List[float] = []
    nmax_hist: List[float] = []
    for s in range(steps):
        nn = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (nn - 1.0))
        psi = np.fft.ifft(np.exp(-1j * DT * k2) * np.fft.fft(psi))
        nn = np.abs(psi) ** 2
        psi *= np.exp(-0.5j * DT * (nn - 1.0))
        if s % sample == 0:
            m, nm = mean_theta(psi)
            mean_hist.append(m)
            nmax_hist.append(nm)

    e1 = energy(psi)
    mean_a = np.asarray(mean_hist)
    lw = late_windows(mean_a)
    return {
        "mean_Theta_max": float(mean_a.max()) if mean_a.size else float("nan"),
        "mean_Theta_min": float(mean_a.min()) if mean_a.size else float("nan"),
        "mean_Theta_late": lw["late_tail10"],
        "settled_mean": lw["settled_mean"],
        "settled_std": lw["settled_std"],
        "n_peak": float(max(nmax_hist)) if nmax_hist else float("nan"),
        "dE_frac": abs(e1 - e0) / max(abs(e0), 1e-12),
        "Hkin_Hdoor_late": hkin_over_hdoor(lw["late_tail10"]),
        "turned_mean": bool(
            any(mean_a[i - 1] < 0.0 <= mean_a[i] for i in range(1, len(mean_a)))
        ),
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 78)
    print("N3 deepen — GPE late-Θ production-class instrument")
    print("package: n3_gpe_late_theta_20260804")
    print("=" * 78)
    print(f"  c_s                       = {C_S:.6f}")
    print(f"  Θ_lock (d=3)              = {THETA_LOCK:.4f}  [= d/(c_s √3)]")
    print(f"  |H_kin(Θ=1)/H_door|       = {H_KIN_OVER_H_DOOR_UNIT:.6f}  (= c_s/√3)")
    print(f"  need late ⟨Θ_heal⟩ ≳ {THETA_LOCK:.2f} for door-magnitude lock (S1)")
    print()
    print("  LOCK METRIC: late / settled mass-weighted ⟨Θ⟩")
    print("  NOT: peaks · 0D |Θ| caps · Madelung vacuum spikes")
    print("  FENCES: stocked GPE/ODE only · no invent H_re · no bounce closed")
    print("  exit 0 ≠ physics PASS · production 3D COMPLETE almost never")

    # ---- [A] 0D ----
    print("\n" + "-" * 78)
    print("[A] 0D reduced stress-channel DEEP scan (stocked FA3/N1 ODE)")
    print("-" * 78)
    rows0, s0 = scan_0d_deep()
    print(f"  scanned unique rows       = {s0['n_rows']}")
    print(
        f"  physical (no cap/blow)    = {s0['n_physical']}"
        f"  (rejected {s0['n_blowup_rejected']})"
    )
    print(f"  turned (Θ:−→0→+)          = {s0['n_turned']}")
    print(f"  max late_Θ (S1 primary)   = {s0['max_late_Theta']:+.4f}")
    print(f"  max settled_mean          = {s0['max_settled_mean']:+.4f}")
    print(f"  max Θ_pos (physical peak) = {s0['max_Theta_pos_physical']:+.4f}")
    print(f"  peak≥lock hits            = {s0['n_peak_ge_lock']}")
    print(f"  max late among peak-hits  = {s0['max_late_among_peak_hits']}")
    bl, bs, bp = s0["best_late"], s0["best_settled"], s0["best_peak"]
    if bl is not None:
        print(
            f"  best late: n0={bl['n0']:.1f} Θ0={bl['Theta0']:.1f}"
            f" κ={bl['kappa']:.2f} γ={bl['gamma']:.2f}"
            f" → late={bl['late_Theta']:+.4f}"
            f" settled={bl['settled_mean']:+.4f}"
            f" peak={bl['Theta_max_pos']:+.4f}"
            f" |H|/H_d={bl['Hkin_Hdoor_late']:.4e}"
        )
    if bs is not None and bs is not bl:
        print(
            f"  best settled: n0={bs['n0']:.1f} Θ0={bs['Theta0']:.1f}"
            f" κ={bs['kappa']:.2f} γ={bs['gamma']:.2f}"
            f" → settled={bs['settled_mean']:+.4f} late={bs['late_Theta']:+.4f}"
        )
    if bp is not None:
        print(
            f"  best peak: n0={bp['n0']:.1f} Θ0={bp['Theta0']:.1f}"
            f" κ={bp['kappa']:.2f} γ={bp['gamma']:.2f}"
            f" → peak={bp['Theta_max_pos']:+.4f} late={bp['late_Theta']:+.4f}"
            f"  (peak≠S1)"
        )
    print(
        f"  late≥lock? {s0['late_reaches_lock']}"
        f"  settled≥lock? {s0['settled_reaches_lock']}"
        f"  peak≥lock? {s0['peak_reaches_lock']}"
    )

    r_def = medium_rebound_0d(6.0, -2.0, 1.5, 0.15)
    print(
        f"  stocked default (6,-2,1.5,0.15): late={r_def['late_Theta']:+.4f}"
        f" settled={r_def['settled_mean']:+.4f}"
        f" peak={r_def['Theta_max_pos']:+.4f}"
        f" |H|/H_d={r_def['Hkin_Hdoor_late']:.4e}"
        f" turned={r_def['turned']>0.5}"
    )

    print("\n  sample high-compression late table (physical only, top by late):")
    phys = [r for r in rows0 if row_physical_0d(r)]
    top = sorted(phys, key=lambda r: r["late_Theta"], reverse=True)[:12]
    print(
        f"  {'n0':>6} {'Θ0':>6} {'κ':>5} {'γ':>5} {'late':>8} {'settled':>8}"
        f" {'peak':>8} {'|H|/Hd':>10} {'×n':>6}"
    )
    for r in top:
        print(
            f"  {r['n0']:6.1f} {r['Theta0']:6.1f} {r['kappa']:5.2f} {r['gamma']:5.2f}"
            f" {r['late_Theta']:+8.4f} {r['settled_mean']:+8.4f}"
            f" {r['Theta_max_pos']:+8.4f} {r['Hkin_Hdoor_late']:10.3e}"
            f" {r['overshoot']:6.2f}"
        )

    # ---- [B] 1D GPE ----
    print("\n" + "-" * 78)
    print("[B] 1D Cartesian GPE late ⟨Θ⟩ deep sweep (M6 stocked form)")
    print("-" * 78)
    sys.stdout.flush()
    rows1, s1 = scan_1d_deep()
    print(f"  cases run                 = {s1['n_rows']}  (clean dE<5%: {s1['n_clean']})")
    print(f"  max ⟨Θ⟩_mean (any time)   = {s1['max_mean_Theta']:+.4f}")
    print(f"  max ⟨Θ⟩_mean late         = {s1['max_late_mean_Theta']:+.4f}")
    print(f"  max settled_mean          = {s1['max_settled_mean']:+.4f}")
    print(f"  max support-local Θ       = {s1['max_support_Theta']:+.4f}  (ρ>0.05)")
    print(
        f"  max raw local Θ           = {s1['max_raw_local_Theta']:+.4f}"
        f"  (VACUUM SPIKE — not S1)"
    )
    print(f"  max overshoot             = {s1['max_overshoot']:.3f}")
    print(
        f"  late≥lock? {s1['late_mean_reaches_lock']}"
        f"  settled≥lock? {s1['settled_reaches_lock']}"
        f"  mean-peak≥lock? {s1['mean_reaches_lock']}"
    )
    bl1 = s1["best_late"]
    if bl1 is not None:
        print(
            f"  best late 1D: A={bl1['A']:.1f} v0={bl1['v0']:.1f} R={bl1['R']:.1f}"
            f" → late={bl1['mean_Theta_late']:+.4f}"
            f" settled={bl1['settled_mean']:+.4f}"
            f" mean_max={bl1['mean_Theta_max']:+.4f}"
            f" |H|/Hd={bl1['Hkin_Hdoor_late']:.4e}"
        )

    print(
        f"\n  {'A':>5} {'v0':>5} {'R':>5} {'n_pk':>8} {'×':>6}"
        f" {'⟨Θ⟩max':>8} {'⟨Θ⟩late':>8} {'settled':>8} {'raw max':>9}"
        f" {'turn':>5} {'dE%':>6}"
    )
    for r in rows1:
        print(
            f"  {r['A']:5.1f} {r['v0']:5.1f} {r['R']:5.1f} {r['n_peak']:8.2f}"
            f" {r['overshoot']:6.2f} {r['mean_Theta_max']:+8.4f}"
            f" {r['mean_Theta_late']:+8.4f} {r['settled_mean']:+8.4f}"
            f" {r['raw_local_Theta_max']:+9.1f}"
            f" {'Y' if r['turned_density']>0.5 else 'n':>5}"
            f" {100*r['dE_frac']:6.2f}"
        )

    # ---- [C] spherical ----
    print("\n" + "-" * 78)
    print("[C] Spherical GPE late ⟨Θ_3d⟩ light probe (DST; not full-3D production)")
    print("-" * 78)
    sys.stdout.flush()
    rows_s, ss = scan_sph_light()
    print(f"  cases run                 = {ss['n_rows']}  (clean: {ss['n_clean']})")
    print(f"  max ⟨Θ⟩_mean late         = {ss['max_late_mean_Theta']:+.4f}")
    print(f"  max ⟨Θ⟩_mean any          = {ss['max_mean_Theta']:+.4f}")
    print(f"  late≥lock? {ss['late_reaches_lock']}")
    print(f"  production_3d             = {ss['production_3d']}  ({ss['symmetry']})")
    print(
        f"\n  {'A':>5} {'v0':>5} {'n_pk':>10} {'×':>7} {'⟨Θ⟩max':>8}"
        f" {'⟨Θ⟩late':>8} {'settled':>8} {'turn':>5} {'dE%':>7} {'steps':>8}"
    )
    for r in rows_s:
        note = str(r.get("note", ""))
        if "FAILED" in note:
            print(f"  {r['A']:5.1f} {r['v0']:5.1f}  FAIL: {note}")
            continue
        npk = r.get("n_peak", float("nan"))
        npk_s = f"{npk:10.2f}" if math.isfinite(npk) else f"{'nan':>10}"
        print(
            f"  {r['A']:5.1f} {r['v0']:5.1f}{npk_s}"
            f" {r['overshoot']:7.2f} {r['mean_Theta_max']:+8.4f}"
            f" {r['mean_Theta_late']:+8.4f} {r['settled_mean']:+8.4f}"
            f" {'Y' if r['turned_density']>0.5 else 'n':>5}"
            f" {100*r['dE_frac']:7.2f} {int(r['steps']):8d}"
        )

    # ---- [D] 2D ----
    print("\n" + "-" * 78)
    print("[D] 2D pancake late ⟨Θ_xx⟩ / ⟨Θ_yy⟩ (stocked transverse class)")
    print("-" * 78)
    r2 = gpe_2d_late_theta()
    print(f"  ⟨Θ_xx⟩ max                = {r2['mean_Theta_xx_max']:+.4e}")
    print(f"  ⟨Θ_xx⟩ late               = {r2['mean_Theta_xx_late']:+.4e}")
    print(f"  ⟨Θ_xx⟩ settled            = {r2['settled_Theta_xx']:+.4e}")
    print(f"  ⟨Θ_yy⟩ |max|              = {r2['mean_Theta_yy_max']:+.4e}")
    print(f"  ⟨Θ_yy⟩ late               = {r2['mean_Theta_yy_late']:+.4e}")
    print(f"  |H_kin|/H_door (Θ_xx late)= {r2['Hkin_Hdoor_xx_late']:.4e}")
    print(f"  dE_frac                   = {100*r2['dE_frac']:.3f}%")
    print(f"  note                      = {r2['note']}")

    # ---- [E] averaging ----
    print("\n" + "-" * 78)
    print("[E] Averaging stress channel (static + dynamic CG)")
    print("-" * 78)
    av = averaging_stress_static()
    print(f"  static mean_Θ             = {av['mean_Theta']:+.4e}")
    print(f"  static stress_drive       = {av['stress_drive']:+.4e}")
    print(f"  static net_rhs            = {av['net_rhs']:+.4e}")
    print(f"  static max |local Θ|      = {av['max_local_abs_Theta']:.4f}")
    avd = averaging_dynamic_late()
    print(f"  dynamic CG ⟨Θ⟩ max        = {avd['mean_Theta_max']:+.4e}")
    print(f"  dynamic CG ⟨Θ⟩ late       = {avd['mean_Theta_late']:+.4e}")
    print(f"  dynamic CG settled        = {avd['settled_mean']:+.4e}")
    print(f"  dynamic CG turned?        = {avd['turned_mean']}")
    print(f"  dynamic |H|/H_d late      = {avd['Hkin_Hdoor_late']:.4e}")
    print(f"  dynamic dE%               = {100*avd['dE_frac']:.3f}")

    # ---- VERDICT ----
    print("\n" + "=" * 78)
    print("VERDICT — late Θ vs Θ_lock / production grade")
    print("=" * 78)

    candidates = [
        s0["max_late_Theta"],
        s0["max_settled_mean"],
        s1["max_late_mean_Theta"],
        s1["max_settled_mean"],
        ss["max_late_mean_Theta"],
        r2["mean_Theta_xx_late"],
        r2["settled_Theta_xx"],
        avd["mean_Theta_late"],
        avd["settled_mean"],
    ]
    max_late = max(float(c) for c in candidates if math.isfinite(float(c)))
    max_mean_peak = max(
        s0["max_Theta_pos_physical"],
        s1["max_mean_Theta"],
        ss["max_mean_Theta"],
        abs(r2["mean_Theta_xx_max"]) if math.isfinite(r2["mean_Theta_xx_max"]) else 0.0,
    )
    lock_late = max_late >= THETA_LOCK
    ratio_late = max_late / THETA_LOCK
    ratio_h = hkin_over_hdoor(max_late)

    turn_paid = s0["n_turned"] > 0 and any(
        r.get("turned_density", 0) > 0.5 for r in rows1 if r["dE_frac"] < 0.05
    )

    if lock_late:
        grade = "UNEXPECTED-LATE-LOCK"
        s1_status = "CLAIM-REVIEW-REQUIRED"
    else:
        grade = "OPEN-BLOCKED"
        s1_status = "MISSING_INPUT"

    production_3d = False  # none of these instruments are full 3D production
    complete = 0

    print(f"  medium turn (toy/M6 class)      = {'YES' if turn_paid else 'NO'}")
    print(f"  MAX LATE/SETTLED ⟨Θ⟩ (S1)       = {max_late:+.4f}")
    print(f"  max peak 0D / 1D-mean           = {max_mean_peak:+.4f}")
    print(f"  raw 1D local max (NOT S1)       = {s1['max_raw_local_Theta']:+.1f}")
    print(f"  Θ_lock required                 = {THETA_LOCK:.4f}")
    print(f"  ratio late / Θ_lock             = {ratio_late:.4e}")
    print(f"  |H_kin(late)|/H_door (d=3)      = {ratio_h:.4e}")
    print(f"  |H_kin(Θ=1)|/H_door             = {H_KIN_OVER_H_DOOR_UNIT:.4e}")
    print(f"  late Θ_lock reached (S1)?       = {lock_late}")
    print(f"  S1 status                       = {s1_status}")
    print(f"  package grade                   = {grade}")
    print(f"  production 3D COMPLETE?         = {production_3d}")
    print(f"  COMPLETE count                  = {complete}")
    print()
    print("  LAYER LATE Θ SUMMARY:")
    print(f"    0D late max                   = {s0['max_late_Theta']:+.4f}")
    print(f"    0D settled max                = {s0['max_settled_mean']:+.4f}")
    print(f"    1D GPE late max               = {s1['max_late_mean_Theta']:+.4f}")
    print(f"    spherical late max            = {ss['max_late_mean_Theta']:+.4f}")
    print(f"    2D Θ_xx late                  = {r2['mean_Theta_xx_late']:+.4e}")
    print(f"    avg CG late                   = {avd['mean_Theta_late']:+.4e}")
    print()
    print("  READ:")
    print("  1. Stocked legal instruments still produce medium turn (toy/M6).")
    print("  2. Late/settled ⟨Θ⟩ remains ≪ Θ_lock under deeper legal sweeps.")
    print("  3. Peak can approach or hit lock in extreme 0D corners; late does not.")
    print("  4. Madelung vacuum spikes and 0D caps are NOT S1 lands.")
    print("  5. κ,γ remain toy reduced coeffs — not Derived cosmological dials.")
    print("  6. Spherical/2D/1D are NOT production full-3D A_Θ-3D COMPLETE.")
    print("  7. S1 stays MISSING_INPUT; N1 magnitude lock via Θ stays OPEN-BLOCKED.")
    print("  8. No claim: bounce closed · H_re Derived · Θ_lock derived · page curve.")

    # survivors: rows with late_Θ > 0.5 (interesting but not lock)
    survivors_0d = [
        {
            "n0": r["n0"],
            "Theta0": r["Theta0"],
            "kappa": r["kappa"],
            "gamma": r["gamma"],
            "late_Theta": r["late_Theta"],
            "settled_mean": r["settled_mean"],
            "Theta_max_pos": r["Theta_max_pos"],
            "Hkin_Hdoor_late": r["Hkin_Hdoor_late"],
        }
        for r in sorted(phys, key=lambda z: z["late_Theta"], reverse=True)[:15]
    ]

    summary = {
        "package": "n3_gpe_late_theta_20260804",
        "prior": "n3_theta_3d_20260804",
        "Theta_lock": THETA_LOCK,
        "c_s": C_S,
        "H_kin_over_H_door_at_Theta1": H_KIN_OVER_H_DOOR_UNIT,
        "max_late_Theta_S1": max_late,
        "max_peak_0d_or_1d_mean": max_mean_peak,
        "max_raw_local_NOT_S1": s1["max_raw_local_Theta"],
        "ratio_late_over_lock": ratio_late,
        "H_kin_over_H_door_at_max_late": ratio_h,
        "Theta_lock_reached_S1_late": lock_late,
        "turn_paid_toy": turn_paid,
        "S1_status": s1_status,
        "grade": grade,
        "COMPLETE": complete,
        "production_3d": production_3d,
        "page_curve_claimed": False,
        "layer": {
            "0d": {
                "n_rows": s0["n_rows"],
                "n_physical": s0["n_physical"],
                "n_turned": s0["n_turned"],
                "max_late_Theta": s0["max_late_Theta"],
                "max_settled_mean": s0["max_settled_mean"],
                "max_Theta_pos_physical": s0["max_Theta_pos_physical"],
                "n_peak_ge_lock": s0["n_peak_ge_lock"],
                "max_late_among_peak_hits": s0["max_late_among_peak_hits"],
                "late_reaches_lock": s0["late_reaches_lock"],
                "best_late": s0["best_late"],
            },
            "1d_gpe": {
                "n_rows": s1["n_rows"],
                "n_clean": s1["n_clean"],
                "max_mean_Theta": s1["max_mean_Theta"],
                "max_late_mean_Theta": s1["max_late_mean_Theta"],
                "max_settled_mean": s1["max_settled_mean"],
                "max_raw_local_Theta": s1["max_raw_local_Theta"],
                "late_mean_reaches_lock": s1["late_mean_reaches_lock"],
                "best_late": s1["best_late"],
            },
            "spherical": {
                "n_rows": ss["n_rows"],
                "n_clean": ss["n_clean"],
                "max_late_mean_Theta": ss["max_late_mean_Theta"],
                "max_mean_Theta": ss["max_mean_Theta"],
                "late_reaches_lock": ss["late_reaches_lock"],
                "production_3d": False,
            },
            "2d_pancake": r2,
            "averaging_static": av,
            "averaging_dynamic": avd,
            "default_0d": {
                "late_Theta": r_def["late_Theta"],
                "settled_mean": r_def["settled_mean"],
                "Theta_max_pos": r_def["Theta_max_pos"],
                "Hkin_Hdoor_late": r_def["Hkin_Hdoor_late"],
            },
        },
        "top_0d_late_survivors": survivors_0d,
        "note": (
            "S1 = late/settled mass-weighted ⟨Θ⟩ only. Peak spikes, Madelung "
            "vacuum local Θ, and 0D integrator caps are not lands. Full-3D "
            "production A_Θ-3D is not stocked; COMPLETE=0."
        ),
    }

    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(summary, indent=2, default=str))
    print("SUMMARY_JSON_END")

    # hard asserts — honesty
    assert r_def["turned"] > 0.5, "stocked 0D must still turn"
    assert summary["COMPLETE"] == 0
    assert summary["production_3d"] is False
    assert summary["page_curve_claimed"] is False
    if not lock_late:
        assert summary["S1_status"] == "MISSING_INPUT"
        assert summary["grade"] == "OPEN-BLOCKED"
    print("\nASSERTS OK — late Θ_lock not landed; S1 MISSING_INPUT; not 3D COMPLETE.")
    print("=" * 78)


if __name__ == "__main__":
    main()
