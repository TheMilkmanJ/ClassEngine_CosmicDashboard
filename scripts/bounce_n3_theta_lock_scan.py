#!/usr/bin/env python3
"""bounce_n3_theta_lock_scan — N3 A_Θ-3D + S1 Θ_lock hunt (2026-08-04).

QUESTION
  Can legal medium stress produce ⟨Θ⟩ turn AND raise Θ_heal toward
  Θ_lock ≈ 11.7 needed for magnitude lock (N1 obstruction C), beyond
  0D O(1) toys?  Is S1 payable under GPE-legal instruments already stocked?

HARD RULES
  - Reuse stocked 0D / 1D / averaging instruments only.
  - Scan n0, Theta0, kappa, gamma within corpus-reasonable ranges.
  - Do NOT invent force laws that aren't GPE-legal.
  - S1 lock metric = LATE / coarse mass-weighted ⟨Θ⟩ at re-entry candidate,
    NOT Madelung vacuum spikes and NOT 0D integrator |Θ| caps.
  - No claim that Θ_lock is derived if late/mean never reaches it.
  - Toy turn YES ≠ production 3D COMPLETE.
  - No invent H_re · no bounce closed · leave MCMCs · no PolyChord.
  - exit 0 = compute finished; PASS/FAIL is physics grade in SUMMARY.

INSTRUMENTS
  (0D)  medium_rebound ODE (FA3 / N1 / scaffold):
            dn/dt = −n Θ
            dΘ/dt = −Θ² + κ(n−1) − γ Θ
  (1D)  Cartesian GPE split-step (M6 scheme): mass-weighted ⟨Θ⟩=⟨∂_x v⟩
  (avg) synthetic double-bump stress channel (FA3)

Θ_lock (N1 / FA3 shear-door bookkeeping, d=3):
    Θ_lock = d / (c_s √3) ≈ 11.71
"""
from __future__ import annotations

import json
import math
from typing import Any, Dict, List, Tuple

import numpy as np

ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
D_LOCK = 3
THETA_LOCK = D_LOCK / (C_S * math.sqrt(3.0))  # ≈ 11.71
TH_CAP = 80.0  # 0D integrator safety; rows that hit cap are unphysical


# ---------------------------------------------------------------------------
# 0D toy (stocked)
# ---------------------------------------------------------------------------
def medium_rebound_0d(
    n0: float = 6.0,
    Theta0: float = -2.0,
    kappa: float = 1.5,
    gamma: float = 0.15,
    t_max: float = 40.0,
    dt: float = 5e-4,
) -> Dict[str, float]:
    n, Th = float(n0), float(Theta0)
    n_peak, t_turn = n0, 0.0
    turned = False
    t = 0.0
    th_hist: List[float] = []
    dth_at_cross = float("nan")
    th_max_pos = 0.0
    th_max_abs = abs(Th)
    hit_cap = False
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
        if Th > th_max_pos:
            th_max_pos = Th
        if abs(Th) > th_max_abs:
            th_max_abs = abs(Th)
        if n > n_peak:
            n_peak = n
            t_turn = t
        if (
            not turned
            and len(th_hist) > 1
            and th_hist[-2] < 0.0 <= th_hist[-1]
            and n_peak > n0 * 1.005
        ):
            turned = True
            dth_at_cross = dTh
        if turned and t > t_turn + 8.0:
            break
    late = th_hist[-max(1, len(th_hist) // 10) :]
    return {
        "n0": float(n0),
        "Theta0": float(Theta0),
        "kappa": float(kappa),
        "gamma": float(gamma),
        "turned": float(turned),
        "dTheta_dt_cross": float(dth_at_cross) if turned else float("nan"),
        "late_Theta": float(np.mean(late)),
        "overshoot": n_peak / max(n0, 1e-12),
        "n_peak": float(n_peak),
        "Theta_max_pos": float(th_max_pos),
        "Theta_max_abs": float(th_max_abs),
        "hit_cap": float(hit_cap),
        "t_end": float(t),
    }


def row_physical_0d(r: Dict[str, float]) -> bool:
    """Reject integrator blow-ups. S1 uses late Θ, not cap hits."""
    if r["hit_cap"] > 0.5:
        return False
    if r["overshoot"] > 100.0:
        return False
    if not math.isfinite(r["late_Theta"]):
        return False
    return True


# ---------------------------------------------------------------------------
# 1D GPE probe (stocked M6 scheme; measure Θ)
# ---------------------------------------------------------------------------
def gpe_1d_theta_probe(
    A: float,
    v0: float,
    R: float = 8.0,
    L: float = 80.0,
    N: int = 1024,
    DT: float = 1.0e-3,
    T_MAX: float = 16.0,
) -> Dict[str, float]:
    """1D repulsive GPE; mass-weighted ⟨Θ⟩ is the lock-relevant readout.

    Local max Θ near vacuum cores is Madelung-singular diagnostic only
    (cf. bounce_averaging_decomposition v1 note) — not S1.
    """
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
        # density floor for velocity: avoids vacuum Madelung spikes in mean
        vf = J / np.maximum(nn, 1e-12)
        Th = np.gradient(vf, dx)
        w = nn / max(float(nn.sum()), 1e-30)
        mean_th = float((w * Th).sum())
        # local max only on support ρ > 0.05 (reject vacuum spikes for diagnostic
        # "support-local"; raw local still recorded separately)
        support = nn > 0.05
        if np.any(support):
            max_th_support = float(Th[support].max())
        else:
            max_th_support = float(Th.max())
        max_th_raw = float(Th.max())
        return mean_th, max_th_support, max_th_raw, float(nn.max())

    e0 = energy(psi)
    steps = int(T_MAX / DT)
    sample = max(1, int(0.1 / DT))
    mean_hist: List[float] = []
    max_sup_hist: List[float] = []
    max_raw_hist: List[float] = []
    nmax_hist: List[float] = []
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
    e1 = energy(psi)
    mean_a = np.asarray(mean_hist)
    max_sup_a = np.asarray(max_sup_hist)
    max_raw_a = np.asarray(max_raw_hist)
    nmax_a = np.asarray(nmax_hist)
    kpk = int(np.argmax(nmax_a))
    late_frac = max(1, len(mean_a) // 10)
    late_mean = float(np.mean(mean_a[-late_frac:]))
    late_sup = float(np.mean(max_sup_a[-late_frac:]))
    turned = float(nmax_a[-1]) < 0.95 * float(nmax_a[kpk])
    mean_turn = False
    for i in range(1, len(mean_a)):
        if mean_a[i - 1] < 0.0 <= mean_a[i]:
            mean_turn = True
            break
    return {
        "A": float(A),
        "v0": float(v0),
        "n_init": 1.0 + A,
        "n_peak": float(nmax_a[kpk]),
        "overshoot": float(nmax_a[kpk]) / max(1.0 + A, 1e-12),
        "turned_density": float(turned),
        "mean_Theta_turn": float(mean_turn),
        "mean_Theta_max": float(mean_a.max()),
        "mean_Theta_min": float(mean_a.min()),
        "mean_Theta_late": late_mean,
        "support_Theta_max": float(max_sup_a.max()),
        "support_Theta_late": late_sup,
        "raw_local_Theta_max": float(max_raw_a.max()),
        "dE_frac": abs(e1 - e0) / max(e0, 1e-12),
    }


# ---------------------------------------------------------------------------
# synthetic averaging stress (stocked FA3)
# ---------------------------------------------------------------------------
def averaging_stress_synthetic() -> Dict[str, float]:
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


# ---------------------------------------------------------------------------
# scans
# ---------------------------------------------------------------------------
def scan_0d() -> Tuple[List[Dict[str, float]], Dict[str, Any]]:
    n0_grid = [2.0, 3.0, 6.0, 11.0, 20.0, 50.0]
    Th0_grid = [-0.5, -1.0, -2.0, -3.0, -5.0]
    kappa_grid = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    gamma_grid = [0.05, 0.10, 0.15, 0.30, 0.50]

    rows: List[Dict[str, float]] = []
    for n0 in n0_grid:
        for Th0 in Th0_grid:
            rows.append(medium_rebound_0d(n0, Th0, 1.5, 0.15))
    for kappa in kappa_grid:
        for gamma in gamma_grid:
            rows.append(medium_rebound_0d(6.0, -2.0, kappa, gamma))
    for n0 in (11.0, 20.0, 50.0):
        for kappa in (3.0, 5.0):
            for gamma in (0.05, 0.15):
                for Th0 in (-2.0, -5.0):
                    rows.append(medium_rebound_0d(n0, Th0, kappa, gamma))

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
    max_over = max((r["overshoot"] for r in physical), default=0.0)
    best_late = max(turned, key=lambda r: r["late_Theta"]) if turned else None
    best_peak = max(physical, key=lambda r: r["Theta_max_pos"]) if physical else None

    return unique, {
        "n_rows": len(unique),
        "n_physical": len(physical),
        "n_blowup_rejected": len(blowups),
        "n_turned": len(turned),
        "max_late_Theta": float(max_late) if math.isfinite(max_late) else 0.0,
        "max_Theta_pos_physical": float(max_pos),
        "max_overshoot_physical": float(max_over),
        "best_late": best_late,
        "best_peak": best_peak,
        "late_reaches_lock": bool(max_late >= THETA_LOCK),
        "peak_reaches_lock": bool(max_pos >= THETA_LOCK),
    }


def scan_1d() -> Tuple[List[Dict[str, float]], Dict[str, Any]]:
    cases = [
        (2.0, 0.5),
        (5.0, 1.0),
        (10.0, 1.0),
        (5.0, 2.0),
        (20.0, 1.0),
        (5.0, 3.0),
    ]
    rows = [gpe_1d_theta_probe(A, v0) for A, v0 in cases]
    clean = [r for r in rows if r["dE_frac"] < 0.05]
    max_mean = max((r["mean_Theta_max"] for r in clean), default=0.0)
    max_late_mean = max((r["mean_Theta_late"] for r in clean), default=0.0)
    max_sup = max((r["support_Theta_max"] for r in clean), default=0.0)
    max_raw = max((r["raw_local_Theta_max"] for r in clean), default=0.0)
    max_over = max((r["overshoot"] for r in clean), default=0.0)
    return rows, {
        "n_rows": len(rows),
        "n_clean": len(clean),
        "max_mean_Theta": max_mean,
        "max_late_mean_Theta": max_late_mean,
        "max_support_Theta": max_sup,
        "max_raw_local_Theta": max_raw,
        "max_overshoot": max_over,
        # S1 lock only on mass-weighted mean (late preferred); support/raw = diagnostic
        "mean_reaches_lock": bool(max_mean >= THETA_LOCK),
        "late_mean_reaches_lock": bool(max_late_mean >= THETA_LOCK),
        "support_local_note": "support/raw local Θ are Madelung diagnostics, not S1",
    }


def main() -> None:
    print("=" * 78)
    print("N3 / S1 — Θ_lock hunt under legal 0D + 1D GPE instruments")
    print("=" * 78)
    print(f"  c_s              = {C_S:.6f}")
    print(f"  Θ_lock (d=3)     = {THETA_LOCK:.4f}   [= d/(c_s √3)]")
    print(f"  |H_kin(Θ=1)/H_d| = {C_S / math.sqrt(3.0):.6f}  (= c_s/√3)")
    print(f"  need late ⟨Θ_heal⟩ ≳ {THETA_LOCK:.2f} for door-magnitude lock (N1 S1)")
    print()
    print("  LOCK METRIC: late / mass-weighted ⟨Θ⟩ (re-entry candidate)")
    print("  NOT: 0D |Θ| integrator caps · Madelung vacuum local spikes")
    print("  FENCES: no invent force laws · no free H_re · no bounce closed")
    print("  exit 0 ≠ physics PASS · toy turn ≠ 3D production COMPLETE")

    # ---- 0D ----
    print("\n" + "-" * 78)
    print("[A] 0D reduced stress-channel scan (FA3/N1 ODE)")
    print("-" * 78)
    rows0, s0 = scan_0d()
    print(f"  scanned unique rows     = {s0['n_rows']}")
    print(f"  physical (no cap/blow)  = {s0['n_physical']}  "
          f"(rejected {s0['n_blowup_rejected']})")
    print(f"  turned (Θ:−→0→+)        = {s0['n_turned']}")
    print(f"  max late_Θ (physical)   = {s0['max_late_Theta']:+.4f}")
    print(f"  max Θ_pos (physical)    = {s0['max_Theta_pos_physical']:+.4f}")
    print(f"  max overshoot physical  = {s0['max_overshoot_physical']:.3f}")
    bl, bp = s0["best_late"], s0["best_peak"]
    if bl is not None:
        print(
            f"  best late: n0={bl['n0']:.1f} Θ0={bl['Theta0']:.1f}"
            f" κ={bl['kappa']:.2f} γ={bl['gamma']:.2f}"
            f" → late_Θ={bl['late_Theta']:+.4f} ×n={bl['overshoot']:.2f}"
        )
    if bp is not None:
        print(
            f"  best peak: n0={bp['n0']:.1f} Θ0={bp['Theta0']:.1f}"
            f" κ={bp['kappa']:.2f} γ={bp['gamma']:.2f}"
            f" → Θ_max_pos={bp['Theta_max_pos']:+.4f}"
            f" late_Θ={bp['late_Theta']:+.4f}"
        )
    print(
        f"  late ≥ Θ_lock? {s0['late_reaches_lock']}"
        f"   peak(phys) ≥ Θ_lock? {s0['peak_reaches_lock']}"
    )

    r_def = medium_rebound_0d(6.0, -2.0, 1.5, 0.15)
    print(
        f"  stocked default (6,-2,1.5,0.15): late_Θ={r_def['late_Theta']:+.4f}"
        f"  Θ_max_pos={r_def['Theta_max_pos']:+.4f}"
        f"  overshoot={r_def['overshoot']:.2f}  turned={r_def['turned']>0.5}"
    )

    print("\n  sample (κ=1.5, γ=0.15) n0 × Θ0  [* = rejected blowup]:")
    print(f"  {'n0':>6} {'Θ0':>6} {'turn':>5} {'lateΘ':>8} {'Θmax+':>8} {'×n':>8} {'ok':>4}")
    for n0 in (3.0, 6.0, 11.0, 20.0, 50.0):
        for Th0 in (-1.0, -2.0, -5.0):
            r = medium_rebound_0d(n0, Th0, 1.5, 0.15)
            ok = row_physical_0d(r)
            print(
                f"  {n0:6.1f} {Th0:6.1f} {'Y' if r['turned']>0.5 else 'n':>5}"
                f" {r['late_Theta']:+8.4f} {r['Theta_max_pos']:+8.4f}"
                f" {r['overshoot']:8.2f} {'Y' if ok else '*':>4}"
            )

    print("\n  κ–γ sensitivity at (n0=6, Θ0=-2):")
    print(f"  {'κ':>5} {'γ':>5} {'turn':>5} {'lateΘ':>8} {'Θmax+':>8} {'×n':>6} {'ok':>4}")
    for kappa in (0.5, 1.5, 3.0, 5.0):
        for gamma in (0.05, 0.15, 0.50):
            r = medium_rebound_0d(6.0, -2.0, kappa, gamma)
            ok = row_physical_0d(r)
            print(
                f"  {kappa:5.2f} {gamma:5.2f} {'Y' if r['turned']>0.5 else 'n':>5}"
                f" {r['late_Theta']:+8.4f} {r['Theta_max_pos']:+8.4f}"
                f" {r['overshoot']:6.2f} {'Y' if ok else '*':>4}"
            )

    # ---- 1D GPE ----
    print("\n" + "-" * 78)
    print("[B] 1D GPE Θ probe (M6-legal; mass-weighted ⟨Θ⟩ is lock metric)")
    print("-" * 78)
    rows1, s1 = scan_1d()
    print(f"  cases run               = {s1['n_rows']}  (clean dE<5%: {s1['n_clean']})")
    print(f"  max ⟨Θ⟩_mean (any time) = {s1['max_mean_Theta']:+.4f}")
    print(f"  max ⟨Θ⟩_mean late       = {s1['max_late_mean_Theta']:+.4f}")
    print(f"  max support-local Θ     = {s1['max_support_Theta']:+.4f}  (ρ>0.05)")
    print(f"  max raw local Θ         = {s1['max_raw_local_Theta']:+.4f}  "
          f"(VACUUM SPIKE — not S1)")
    print(f"  max overshoot n_pk/n_i  = {s1['max_overshoot']:.3f}")
    print(
        f"  mean≥lock? {s1['mean_reaches_lock']}"
        f"  late_mean≥lock? {s1['late_mean_reaches_lock']}"
        f"  (support/raw local ignored for S1)"
    )
    print(
        f"\n  {'A':>5} {'v0':>5} {'n_pk':>8} {'×':>6} {'⟨Θ⟩max':>8} "
        f"{'⟨Θ⟩late':>8} {'Θsup max':>9} {'raw max':>9} {'turn':>5} {'dE%':>6}"
    )
    for r in rows1:
        print(
            f"  {r['A']:5.1f} {r['v0']:5.1f} {r['n_peak']:8.2f}"
            f" {r['overshoot']:6.2f} {r['mean_Theta_max']:+8.4f}"
            f" {r['mean_Theta_late']:+8.4f} {r['support_Theta_max']:+9.4f}"
            f" {r['raw_local_Theta_max']:+9.1f}"
            f" {'Y' if r['turned_density']>0.5 else 'n':>5}"
            f" {100*r['dE_frac']:6.2f}"
        )

    # ---- synthetic averaging ----
    print("\n" + "-" * 78)
    print("[C] Synthetic averaging stress channel (FA3 stand-in)")
    print("-" * 78)
    av = averaging_stress_synthetic()
    print(f"  mean_Θ           = {av['mean_Theta']:+.4e}")
    print(f"  var_Θ            = {av['var_Theta']:+.4e}")
    print(f"  stress_drive     = {av['stress_drive']:+.4e}")
    print(f"  net_rhs          = {av['net_rhs']:+.4e}")
    print(f"  max |local Θ|    = {av['max_local_abs_Theta']:.4f}")
    print("  (static snapshot — stress can fund turn; not Θ_lock)")

    # ---- corpus priors ----
    print("\n" + "-" * 78)
    print("[D] Corpus priors (not re-run; inventory)")
    print("-" * 78)
    print("  M6 1D: density turn YES; overshoot O(1); no late Θ≳12")
    print("  M6 hypersonic: turn YES at Mach~15; O(1) amplification")
    print("  M6 spherical (gp/dst): focusing measured; short of MeV F≥1e9")
    print("  transverse 2D: ⟨Θ_xx⟩ ~0.03–0.08; Θ_yy ≪ 1e-4")
    print("  averaging decomp: identity holds; stress funds turn; Θ O(1)")
    print("  NO production full-3D GPE instrument stocked for Θ_lock")

    # ---- verdict: S1 uses late/mean only ----
    print("\n" + "=" * 78)
    print("VERDICT — S1 / N3 Θ_lock")
    print("=" * 78)

    # lock-relevant maxima (late/mean only for S1; 0D peak diagnostic)
    max_late = max(s0["max_late_Theta"], s1["max_late_mean_Theta"])
    max_mean_peak = max(s0["max_Theta_pos_physical"], s1["max_mean_Theta"])
    lock_late = s0["late_reaches_lock"] or s1["late_mean_reaches_lock"]
    # peak diagnostic: 0D physical peak or 1D *mean* — NOT support/raw spikes
    lock_peak_diag = s0["peak_reaches_lock"] or s1["mean_reaches_lock"]
    # S1 demands late re-entry Θ, not a transient peak
    lock_reached_S1 = lock_late
    turn_paid_toy = s0["n_turned"] > 0 and any(
        r["turned_density"] > 0.5 for r in rows1
    )

    if lock_reached_S1:
        grade = "UNEXPECTED-LATE-LOCK"
        s1_status = "CLAIM-REVIEW-REQUIRED"
    else:
        grade = "OPEN-BLOCKED"
        s1_status = "MISSING_INPUT"

    print(f"  medium turn (0D/1D toys)        = {'YES' if turn_paid_toy else 'NO'}")
    print(f"  max late ⟨Θ⟩ (S1 lock metric)   = {max_late:+.4f}")
    print(f"  max peak 0D-phys / 1D-mean      = {max_mean_peak:+.4f}")
    print(f"  raw/support local max (NOT S1)  = {s1['max_raw_local_Theta']:+.1f}")
    print(f"  Θ_lock required                 = {THETA_LOCK:.4f}")
    print(f"  ratio late / Θ_lock             = {max_late / THETA_LOCK:.4e}")
    print(f"  ratio peak_mean / Θ_lock        = {max_mean_peak / THETA_LOCK:.4e}")
    print(f"  late Θ_lock reached (S1)?       = {lock_reached_S1}")
    print(f"  0D-peak or 1D-mean ≥ lock?      = {lock_peak_diag}")
    print(f"  S1 status                       = {s1_status}")
    print(f"  package grade                   = {grade}")
    print(f"  production 3D COMPLETE?         = False")
    print()
    print("  READ:")
    print("  1. Legal stress (0D reduced + 1D GPE) DOES produce ⟨Θ⟩ turn")
    print("     under stocked repulsive GPE form — toy layer PAID.")
    print("  2. Late healing ⟨Θ⟩ remains ≪ Θ_lock across legal physical")
    print("     scans: stocked default late_Θ~0.062; best late O(1) only.")
    print("  3. 0D physical peak can approach ~11 in extreme κ/γ/n0 corners")
    print("     but late_Θ there is O(1) or negative — peak ≠ re-entry lock.")
    print("  4. Madelung vacuum/support local spikes (Θ ≫ 1) are harness")
    print("     singularities (averaging decomp v1); not Derived lock.")
    print("  5. 0D |Θ| cap hits / overshoot≫100 are numerical blowups;")
    print("     rejected — not GPE-legal re-entry amplitudes.")
    print("  6. κ,γ are toy reduced coeffs, not Derived cosmological dials.")
    print("  7. Production 3D A_Θ-3D instrument is NOT stocked.")
    print("  8. S1 stays MISSING_INPUT / OPEN-BLOCKED for magnitude lock.")
    print("  9. No claim: Θ_lock derived · bounce closed · H_re Derived.")

    summary = {
        "package": "n3_theta_3d_20260804",
        "Theta_lock": THETA_LOCK,
        "c_s": C_S,
        "max_late_Theta_lock_metric": max_late,
        "max_peak_0d_phys_or_1d_mean": max_mean_peak,
        "max_raw_local_NOT_S1": s1["max_raw_local_Theta"],
        "ratio_late_over_lock": max_late / THETA_LOCK,
        "ratio_peak_mean_over_lock": max_mean_peak / THETA_LOCK,
        "Theta_lock_reached_S1_late": lock_reached_S1,
        "peak_0d_or_mean_ge_lock": lock_peak_diag,
        "turn_paid_toy": turn_paid_toy,
        "S1_status": s1_status,
        "grade": grade,
        "scan_0d": {
            "n_rows": s0["n_rows"],
            "n_physical": s0["n_physical"],
            "n_blowup_rejected": s0["n_blowup_rejected"],
            "n_turned": s0["n_turned"],
            "max_late_Theta": s0["max_late_Theta"],
            "max_Theta_pos_physical": s0["max_Theta_pos_physical"],
            "max_overshoot_physical": s0["max_overshoot_physical"],
            "late_reaches_lock": s0["late_reaches_lock"],
            "peak_reaches_lock": s0["peak_reaches_lock"],
        },
        "scan_1d": {
            "n_rows": s1["n_rows"],
            "n_clean": s1["n_clean"],
            "max_mean_Theta": s1["max_mean_Theta"],
            "max_late_mean_Theta": s1["max_late_mean_Theta"],
            "max_support_Theta": s1["max_support_Theta"],
            "max_raw_local_Theta": s1["max_raw_local_Theta"],
            "max_overshoot": s1["max_overshoot"],
            "mean_reaches_lock": s1["mean_reaches_lock"],
            "late_mean_reaches_lock": s1["late_mean_reaches_lock"],
        },
        "averaging_synthetic": av,
        "default_0d": {
            "late_Theta": r_def["late_Theta"],
            "Theta_max_pos": r_def["Theta_max_pos"],
            "overshoot": r_def["overshoot"],
        },
        "COMPLETE": 0,
        "production_3d": False,
        "note": (
            "S1 lock metric = late/mean ⟨Θ⟩; vacuum spikes and 0D caps "
            "are not lands. N3 production 3D not stocked."
        ),
    }
    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(summary, indent=2, default=str))
    print("SUMMARY_JSON_END")

    assert r_def["turned"] > 0.5, "stocked 0D must still turn"
    assert summary["COMPLETE"] == 0
    assert summary["production_3d"] is False
    if not lock_reached_S1:
        assert summary["S1_status"] == "MISSING_INPUT"
        assert summary["grade"] == "OPEN-BLOCKED"
    print("\nASSERTS OK — no late Θ_lock land; S1 MISSING_INPUT; not 3D COMPLETE.")
    print("=" * 78)


if __name__ == "__main__":
    main()
