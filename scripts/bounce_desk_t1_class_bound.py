#!/usr/bin/env python3
"""bounce_desk_t1_class_bound — T1 CLASS bound for settled ⟨Θ⟩ vs Θ_lock.

PACKAGE
  docs/working_logs/_runs/theory_construction_20260804/desk_t1_settled_theta_class_20260804/

MISSION
  Formalize the CLASS argument under the stocked FA3 0D ODE
      dn/dt = −n Θ
      dΘ/dt = −Θ² + κ(n−1) − γ Θ   (γ > 0)
  and document whether stocked GPE 1D / spherical forms change the
  conclusion for settled mean.

CLASS (exact identity from continuity alone — any κ, γ, any IC):
  Θ = − d(ln n)/dt
  ⇒  ⟨Θ⟩_[t1,t2] = [ln n(t1) − ln n(t2)] / (t2 − t1)
  To hold ⟨Θ⟩ = Θ_lock ≈ 11.706 over a window of length Δt requires
      n(t1)/n(t2) = exp(Θ_lock · Δt)
  For Δt ~ 10 (S1_settled last-20% of se≈40 runs): ~10^50 density drop
  inside the window. Grid extension / free κ,γ cannot evade this.

GPE extension (stocked continuity, not re-run of full grids):
  ∂t n + ∇·(n v) = 0  and  Θ = ∇·v  ⇒ for mass-conserving domains
  ⟨Θ⟩_n = − (1/M) d/dt ∫ n ln n
  so window-mean mass-weighted ⟨Θ⟩ is a mass-weighted log-density drop.
  Stocked 1D/2D/sph late/settled numbers (prior packages) remain ≪ lock;
  production_3d stays false.

HARD RULES
  - No invent H_re · no free dial as land · leave MCMCs · no PolyChord
  - page_curve_claimed = false · production_3d = false
  - exit 0 = compute finished; PASS/FAIL is physics grade in SUMMARY
  - COMPLETE = 0 (CLASS-BOUND is partial, not S1 land)
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# anchors (disk / book; identical to FA3 / N3 / settled_late_theta)
# ---------------------------------------------------------------------------
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
D_LOCK = 3
THETA_LOCK = D_LOCK / (C_S * math.sqrt(3.0))  # = 1/√α at d=3
H_KIN_OVER_H_DOOR_UNIT = C_S / math.sqrt(3.0)
TH_CAP = 80.0
DT_DEFAULT = 1e-3
PACKAGE = "desk_t1_settled_theta_class_20260804"
PRIOR_SETTLED = "settled_late_theta_20260804"
PRIOR_GPE = "n3_gpe_late_theta_20260804"
STOCKED_DEFAULT = (6.0, -2.0, 1.5, 0.15)
PRIOR_F5 = (80.0, -8.0, 3.0, 0.02)
ARGMAX_QUALITY = (3.0, -1.0, 1.0, 0.05)
ARGMAX_ALLPHYS = (6.0, -2.0, 1.0, 0.02)

# Prior package stamps (not re-scanned here; identity proof does not need them)
PRIOR_MAX_QUALITY_SETTLED = 0.04358232247341028
PRIOR_MAX_ALLPHYS_SETTLED = 0.10560011708111182
PRIOR_GPE_MAX_LATE = 2.870069874888626
PRIOR_GPE_MAX_SETTLED_0D = 0.1143
PRIOR_GPE_1D_LATE = 0.0265
PRIOR_GPE_1D_SETTLED = 0.0015
PRIOR_GPE_2D_LATE = 0.0346
PRIOR_GPE_2D_SETTLED = 0.0391
PRIOR_GPE_SPH_NOTE = "unclean energy; late O(10^-2) negative; not S1-quotable"


def script_sha256() -> str:
    p = Path(__file__).resolve()
    return hashlib.sha256(p.read_bytes()).hexdigest()


def n_drop_ratio(Theta_mean: float, delta_t: float) -> float:
    """Exact identity: n(t1)/n(t2) = exp(⟨Θ⟩ Δt) under ṅ = −nΘ."""
    return math.exp(float(Theta_mean) * float(delta_t))


def class_bound_table(Theta_lock: float = THETA_LOCK) -> List[Dict[str, float]]:
    """n-drop required for window-mean Θ = Θ_lock at several Δt."""
    rows = []
    for dt in (1.0, 5.0, 8.0, 9.7, 10.0, 20.0, 40.0):
        ratio = n_drop_ratio(Theta_lock, dt)
        rows.append(
            {
                "delta_t": float(dt),
                "Theta_lock": float(Theta_lock),
                "ln_n_drop": float(Theta_lock * dt),
                "n_ratio_n1_over_n2": float(ratio),
                "log10_n_ratio": float(math.log10(ratio)),
            }
        )
    return rows


def medium_rebound_0d_with_n(
    n0: float,
    Theta0: float,
    kappa: float,
    gamma: float,
    settle_extra: float = 40.0,
    t_max: float = 200.0,
    dt: float = DT_DEFAULT,
) -> Dict[str, Any]:
    """Stocked FA3 0D; record n and Θ so the log-density identity can be checked."""
    n, Th = float(n0), float(Theta0)
    n_peak, t_turn_n = n0, 0.0
    turned = False
    t = 0.0
    th_hist: List[float] = []
    n_hist: List[float] = []
    t_hist: List[float] = []
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
        t_hist.append(t)
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
        if (not cut_set) and t > t_turn_n + 8.0 and n_peak > n0 * 1.005:
            t_cut_reentry = t
            cut_set = True
            if settle_extra <= 0.0:
                break
        if cut_set and t >= t_cut_reentry + settle_extra:
            break

    th_a = np.asarray(th_hist, dtype=float)
    n_a = np.asarray(n_hist, dtype=float)
    t_a = np.asarray(t_hist, dtype=float)
    if th_a.size == 0:
        return {"ok": False}

    n20 = max(1, th_a.size // 5)
    n10 = max(1, th_a.size // 10)
    # last-20% window endpoints
    i1 = th_a.size - n20
    i2 = th_a.size - 1
    t1, t2 = float(t_a[i1]), float(t_a[i2])
    delta_t = t2 - t1
    n1, n2 = float(n_a[i1]), float(n_a[i2])
    th_mean = float(np.mean(th_a[i1 : i2 + 1]))
    th_std = float(np.std(th_a[i1 : i2 + 1]))
    # identity prediction from log n
    if n1 > 0 and n2 > 0 and delta_t > 0:
        th_from_logn = (math.log(n1) - math.log(n2)) / delta_t
        n_ratio = n1 / n2
    else:
        th_from_logn = float("nan")
        n_ratio = float("nan")
    rel_err = (
        abs(th_mean - th_from_logn) / max(abs(th_mean), abs(th_from_logn), 1e-12)
        if math.isfinite(th_from_logn)
        else float("nan")
    )

    # what n-drop would be needed for lock over this actual window
    if delta_t > 0:
        n_ratio_for_lock = n_drop_ratio(THETA_LOCK, delta_t)
        log10_for_lock = math.log10(n_ratio_for_lock)
    else:
        n_ratio_for_lock = float("nan")
        log10_for_lock = float("nan")

    return {
        "ok": True,
        "n0": float(n0),
        "Theta0": float(Theta0),
        "kappa": float(kappa),
        "gamma": float(gamma),
        "settle_extra": float(settle_extra),
        "dt": float(dt),
        "t_end": float(t_a[-1]),
        "turned": float(turned),
        "hit_cap": float(hit_cap),
        "window": "last_20pct_of_full_history",
        "t1": t1,
        "t2": t2,
        "delta_t": float(delta_t),
        "n1": n1,
        "n2": n2,
        "n_ratio_n1_over_n2": float(n_ratio),
        "settled_mean_Theta": th_mean,
        "settled_std_Theta": th_std,
        "Theta_from_logn_identity": float(th_from_logn),
        "identity_rel_err": float(rel_err),
        "late_tail10": float(np.mean(th_a[-n10:])),
        "late_tail20": float(np.mean(th_a[-n20:])),
        "n_ratio_required_for_lock": float(n_ratio_for_lock),
        "log10_n_ratio_required_for_lock": float(log10_for_lock),
        "quality_ok": float(th_std < 0.2),
        "Hkin_Hdoor_settled": abs(th_mean) * H_KIN_OVER_H_DOOR_UNIT,
    }


def verify_identity_rows() -> List[Dict[str, Any]]:
    """Check log-density identity on prior headline rows (se=40)."""
    specs = [
        ("argmax_quality_se40", *ARGMAX_QUALITY),
        ("stocked_default_se40", *STOCKED_DEFAULT),
        ("prior_F5_best_late_se40", *PRIOR_F5),
        ("argmax_all_physical_se40", *ARGMAX_ALLPHYS),
    ]
    out = []
    for label, n0, Th0, kappa, gamma in specs:
        r = medium_rebound_0d_with_n(n0, Th0, kappa, gamma, settle_extra=40.0)
        r["label"] = label
        out.append(r)
    return out


def analytic_class_statement() -> Dict[str, Any]:
    """Form-only statements (no scan)."""
    return {
        "stocked_0d": {
            "equations": ["dn/dt = -n*Theta", "dTheta/dt = -Theta^2 + kappa*(n-1) - gamma*Theta"],
            "identity": "Theta = -d(ln n)/dt  (exact, any kappa,gamma,IC)",
            "window_mean": "mean_Theta[t1,t2] = (ln n(t1) - ln n(t2)) / (t2-t1)",
            "unique_physical_FP": {"n": 1.0, "Theta": 0.0},
            "local_stability": "gamma>0, kappa>0 ⇒ Re(lambda)=-gamma/2 (underdamped branch of legal grid)",
            "class_bound": (
                "Any finite window with mean_Theta = Theta_lock requires "
                "n(t1)/n(t2) = exp(Theta_lock * Delta_t). For Delta_t~10 this is ~10^50. "
                "Free kappa,gamma and grid densification cannot evade the identity."
            ),
            "settled_attractor": (
                "Under stocked form with gamma>0, trajectories approach (1,0); "
                "finite-window positive residuals are leftover density drift, not a nonzero late attractor."
            ),
        },
        "stocked_gpe": {
            "continuity": "partial_t n + div(n v) = 0",
            "Theta_definition": "Theta = div v  (Madelung / continuum expansion)",
            "mass_weighted_identity": (
                "On mass-conserving domains, d/dt ∫ n ln n = -∫ n Theta "
                "⇒ mass-weighted <Theta>_n = -(1/M) d/dt ∫ n ln n. "
                "Window-mean mass-weighted expansion is a mass-weighted log-density drop."
            ),
            "does_gpe_change_class": (
                "NO for settled mean under stocked 1D/2D/sph instruments: "
                "prior late/settled ≪ lock (1D late 0.0265, 2D late 0.035, sph unclean O(0.01)); "
                "continuity still prices any large positive window-mean expansion as huge "
                "mass-weighted log-n drop. production_3d remains false / not stocked."
            ),
            "prior_stamps": {
                "1d_late": PRIOR_GPE_1D_LATE,
                "1d_settled": PRIOR_GPE_1D_SETTLED,
                "2d_late": PRIOR_GPE_2D_LATE,
                "2d_settled": PRIOR_GPE_2D_SETTLED,
                "0d_max_late": PRIOR_GPE_MAX_LATE,
                "0d_max_settled": PRIOR_GPE_MAX_SETTLED_0D,
                "spherical": PRIOR_GPE_SPH_NOTE,
            },
        },
        "what_breaks_class": {
            "not_free_dial": "kappa,gamma rescaling does not break continuity identity",
            "new_instruments": [
                "Continuity-breaking medium source/sink (dn/dt ≠ -n Theta) with named legal form",
                "Lock metric redefinition (N2 match-book) so S1 is not window-mean expansion",
                "Named multi-component law where lock Θ is not the expanding medium's own expansion",
                "Production full-3D instrument only if it still obeys continuity: class bound survives; "
                "if it does not obey continuity, that non-conserving form must be stocked and named first",
            ],
            "not_claimed_here": "No new instrument invented in this package",
        },
    }


def main() -> int:
    print("=" * 72)
    print("DESK T1 — CLASS bound: settled ⟨Θ⟩ vs Θ_lock under stocked continuity")
    print(f"package: {PACKAGE}")
    print(f"priors:  {PRIOR_SETTLED} · {PRIOR_GPE}")
    print("=" * 72)
    print(f"  α                      = {ALPHA:.12g}")
    print(f"  c_s = √(3α)            = {C_S:.12g}")
    print(f"  Θ_lock (d=3)           = {THETA_LOCK:.12g}  [= 1/√α]")
    print(f"  |H_kin|/H_door (Θ=1)   = {H_KIN_OVER_H_DOOR_UNIT:.12g}")
    print(f"  script_sha256          = {script_sha256()}")
    print()

    # --- analytic n-drop table ---
    print("[A] CLASS n-drop bound: ⟨Θ⟩=Θ_lock over window Δt ⇒ n1/n2 = exp(Θ_lock Δt)")
    bound_rows = class_bound_table()
    print(f"  {'Δt':>8} {'ΘΔt':>12} {'n1/n2':>14} {'log10(n1/n2)':>14}")
    for r in bound_rows:
        print(
            f"  {r['delta_t']:8.1f} {r['ln_n_drop']:12.4f} "
            f"{r['n_ratio_n1_over_n2']:14.4e} {r['log10_n_ratio']:14.4f}"
        )
    # headline ~10^50 at Δt=10
    r10 = next(r for r in bound_rows if abs(r["delta_t"] - 10.0) < 1e-12)
    r97 = next(r for r in bound_rows if abs(r["delta_t"] - 9.7) < 1e-12)
    print()
    print(f"  HEADLINE bound @ Δt=10:  n1/n2 = {r10['n_ratio_n1_over_n2']:.6e}  (~10^{r10['log10_n_ratio']:.2f})")
    print(f"  RED window ~9.7:      n1/n2 = {r97['n_ratio_n1_over_n2']:.6e}  (~10^{r97['log10_n_ratio']:.2f})")
    print("  ⇒ settled ⟨Θ⟩ cannot reach Θ_lock without ~10^50 density drop in-window.")
    print()

    # --- numeric identity check ---
    print("[B] Numeric identity check on prior headline 0D rows (se=40, last 20%)")
    id_rows = verify_identity_rows()
    print(
        f"  {'label':<28} {'⟨Θ⟩':>10} {'Θ_from_ln':>10} {'rel_err':>10} "
        f"{'Δt':>8} {'n1/n2':>10} {'log10_need':>10}"
    )
    max_rel_err = 0.0
    for r in id_rows:
        assert r["ok"]
        max_rel_err = max(max_rel_err, r["identity_rel_err"])
        print(
            f"  {r['label']:<28} {r['settled_mean_Theta']:+10.6f} "
            f"{r['Theta_from_logn_identity']:+10.6f} {r['identity_rel_err']:10.3e} "
            f"{r['delta_t']:8.4f} {r['n_ratio_n1_over_n2']:10.4f} "
            f"{r['log10_n_ratio_required_for_lock']:10.2f}"
        )
    # Euler dt=1e-3: quality/stocked rows ~0.1%; F5 high-amp ring ~1% (same identity)
    assert max_rel_err < 1.5e-2, f"identity rel_err too large: {max_rel_err}"
    print(
        f"  max identity rel_err = {max_rel_err:.3e}  "
        f"(Euler dt=1e-3; assert < 1.5e-2; F5 largest)"
    )
    print()

    # --- quality residual as density drift ---
    aq = next(r for r in id_rows if r["label"] == "argmax_quality_se40")
    print("[C] Quality residual is density drift, not late attractor")
    print(f"  argmax quality settled_mean = {aq['settled_mean_Theta']:+.6f}")
    print(f"  n1/n2 over settled window   = {aq['n_ratio_n1_over_n2']:.6f}")
    pct = (1.0 - 1.0 / aq["n_ratio_n1_over_n2"]) * 100.0 if aq["n_ratio_n1_over_n2"] > 0 else float("nan")
    print(f"  ≈ n falls by {pct:.1f}% across the 'settled' window")
    print(f"  n-drop for lock on same Δt  = 10^{aq['log10_n_ratio_required_for_lock']:.2f}")
    print(f"  prior package max quality   = {PRIOR_MAX_QUALITY_SETTLED:+.6f}  (stamp; this run {aq['settled_mean_Theta']:+.6f})")
    # settle_mean should match prior to ~1e-5
    assert abs(aq["settled_mean_Theta"] - PRIOR_MAX_QUALITY_SETTLED) < 1e-5
    print()

    # --- GPE class scan (documentation from priors; continuity identity) ---
    analytic = analytic_class_statement()
    print("[D] Stocked GPE 1D / spherical — does class conclusion change for settled mean?")
    print("  Continuity: ∂t n + ∇·(n v)=0 ⇒ mass-weighted ⟨Θ⟩ = −(1/M) d/dt ∫ n ln n")
    print("  Prior stamps (n3_gpe_late_theta; not re-run):")
    print(f"    1D clean late / settled   = {PRIOR_GPE_1D_LATE:+.4f} / {PRIOR_GPE_1D_SETTLED:+.4f}  ≪ 11.71")
    print(f"    2D Θ_xx late / settled    = {PRIOR_GPE_2D_LATE:+.4f} / {PRIOR_GPE_2D_SETTLED:+.4f}  ≪ 11.71")
    print(f"    spherical light           = {PRIOR_GPE_SPH_NOTE}")
    print(f"    0D max late / settled     = {PRIOR_GPE_MAX_LATE:+.4f} / {PRIOR_GPE_MAX_SETTLED_0D:+.4f}")
    print("  VERDICT: stocked GPE forms do NOT change the class conclusion for settled mean.")
    print("  production_3d = false (still not stocked).")
    print()

    print("[E] What NEW instrument would break the class (not free dial)")
    for item in analytic["what_breaks_class"]["new_instruments"]:
        print(f"  · {item}")
    print(f"  · NOT: free κ,γ dial ({analytic['what_breaks_class']['not_free_dial']})")
    print()

    # --- grade ---
    grade = "OPEN-BLOCKED"
    partial = "CLASS-BOUND"
    complete = 0
    print("[F] Grade")
    print(f"  CLASS 0D continuity bound     = {partial} (formalized + numeric-checked)")
    print(f"  S1_settled ≳ Θ_lock           = MISSING_INPUT (still)")
    print(f"  package grade                 = {grade}")
    print(f"  COMPLETE                      = {complete}")
    print(f"  production_3d                 = False")
    print(f"  page_curve_claimed            = False")
    print("  exit 0 ≠ PASS")
    print()

    summary: Dict[str, Any] = {
        "package": PACKAGE,
        "prior_settled": PRIOR_SETTLED,
        "prior_gpe": PRIOR_GPE,
        "Theta_lock": THETA_LOCK,
        "c_s": C_S,
        "alpha": ALPHA,
        "H_kin_over_H_door_at_Theta1": H_KIN_OVER_H_DOOR_UNIT,
        "script_sha256": script_sha256(),
        "dt": DT_DEFAULT,
        "class_bound_table": bound_rows,
        "headline_bound_delta_t_10": {
            "delta_t": 10.0,
            "n_ratio_n1_over_n2": r10["n_ratio_n1_over_n2"],
            "log10_n_ratio": r10["log10_n_ratio"],
            "note": "~10^50 density drop required for settled mean = Theta_lock",
        },
        "headline_bound_delta_t_9_7": {
            "delta_t": 9.7,
            "n_ratio_n1_over_n2": r97["n_ratio_n1_over_n2"],
            "log10_n_ratio": r97["log10_n_ratio"],
        },
        "identity_checks_se40": id_rows,
        "max_identity_rel_err": max_rel_err,
        "prior_max_quality_settled": PRIOR_MAX_QUALITY_SETTLED,
        "this_run_argmax_quality_settled": aq["settled_mean_Theta"],
        "argmax_quality_n_ratio_window": aq["n_ratio_n1_over_n2"],
        "argmax_quality_pct_n_drop": pct,
        "analytic": analytic,
        "gpe_class_conclusion_changed": False,
        "gpe_note": (
            "Stocked 1D/2D/sph mass-weighted late/settled remain ≪ lock; "
            "continuity prices large window-mean expansion as log-density drop. "
            "production_3d=false."
        ),
        "Theta_lock_reached_S1_settled": False,
        "S1_status": "MISSING_INPUT",
        "class_partial": partial,
        "grade": grade,
        "COMPLETE": complete,
        "production_3d": False,
        "page_curve_claimed": False,
        "note": (
            "CLASS-BOUND under stocked continuity (0D exact; GPE mass-weighted analog). "
            "Not S1 land. Not production 3D. exit0≠PASS. COMPLETE=0."
        ),
    }

    print("SUMMARY_JSON")
    print(json.dumps(summary, indent=2, sort_keys=False))
    print()
    print("ASSERTS OK — CLASS n-drop bound formalized; S1 still MISSING_INPUT; COMPLETE=0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
