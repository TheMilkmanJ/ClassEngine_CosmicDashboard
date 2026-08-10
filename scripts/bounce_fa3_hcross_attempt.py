#!/usr/bin/env python3
"""bounce_fa3_hcross_attempt — smallest honest compute toward F-A3 / O2 (2026-08-03).

QUESTION
  Can exterior H_re be *derived* from medium stress + junction, without the
  F-A3 hand declaration  ⟨Θ⟩>0 ∧ ℓ_grad≳ξ  ⇒  H_re = +√(8πG ρ_re/3)  ?

CANDIDATE CONTINUOUS MAP (the only natural one from acoustic emergence)
  On the preferred-frame condensate rest slice, the acoustic FRW expansion
  is the fluid expansion scalar:
      H_kin = ⟨Θ⟩_phys / d     (d=3 isotropic 3D; d=1 in verified 1D toys)
  Physical units: Θ_phys = Θ_heal / t_0 ,  t_0 = ℏ/(m c_s²) = ξ/c_s
  so  H_kin = Θ_heal · c_s / (d · ξ).

CHECKS
  (1) Medium layer: does ⟨Θ⟩ cross 0 with d⟨Θ⟩/dt > 0 from stress drive?
      (already known from scaffold 0D + averaging; re-confirmed here)
  (2) Unit conversion: is |H_kin| at O(1) healing Θ comparable to door H?
  (3) Friedmann consistency: can H_kin = 0 coexist with ρ_re > 0 under
      H² = 8πGρ/3 when the metric is ON?
  (4) Magnitude lock at re-entry: does |Θ_late|·c_s/(d ξ) equal
      √(8πG ρ_re/3) for any legal ρ_re (door ρ_eff, ρ_bounce, overshoot)?

HARD RULES
  - Do not invent exotic X or N_med compression to close the sign.
  - Prefer kill / exact obstruction over fake derivation.
  - No cyclic cosmology claim.
"""
from __future__ import annotations

import math
from typing import Dict, List, Tuple

import numpy as np

# --- recorded anchors (same as bounce_rpA_scaffold / M2) ---
M_PL = 1.22089e19 * 1e9  # eV
AU_M = 1.496e11
EVINV_TO_M = 1.973269804e-7
XI_AU = 402.0
M_EV = 2.24e-20
LAM = 2e-91
H0_SI = 67e3 / 3.085677581e22
HBAR_EV_S = 6.582119569e-16
H0 = H0_SI * HBAR_EV_S
OMEGA_R = 9.0e-5
GSTAR = 10.75
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)  # recorded √(3α)


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_bounce() -> float:
    return M_EV**4 / LAM


def xi_eVinv() -> float:
    return XI_AU * AU_M / EVINV_TO_M


def H_friedmann(rho: float) -> float:
    """|H| from flat FRW constraint (eV units)."""
    return math.sqrt(8.0 * math.pi / 3.0) * math.sqrt(max(rho, 0.0)) / M_PL


def door_state(Sigma0: float = 1e-5) -> Dict[str, float]:
    sig0 = Sigma0 * H0
    rho_r0 = OMEGA_R * rho_c()
    xi = xi_eVinv()
    a_loc = (sig0 * xi) ** (1.0 / 3.0)
    sig = sig0 / a_loc**3
    rho = rho_r0 / a_loc**4
    H2 = (8.0 * math.pi / 3.0) * rho / M_PL**2 + sig**2 / 3.0
    H = math.sqrt(max(H2, 1e-300))
    rho_eff = 3.0 * H**2 * M_PL**2 / (8.0 * math.pi)
    return {
        "a_loc": a_loc,
        "H_door": H,  # contracting magnitude
        "sig": sig,
        "rho": rho,
        "rho_eff": rho_eff,
        "R_H_over_xi": (1.0 / H) / xi,
        "xi": xi,
        "T_eff": rho_eff**0.25,
    }


def medium_rebound_0d(
    n0: float = 6.0, Theta0: float = -2.0, t_max: float = 40.0, dt: float = 5e-4
) -> Dict[str, float]:
    """Same 0D toy as scaffold — returns turn diagnostics + Θ history stats."""
    kappa, gamma = 1.5, 0.15
    n, Th = float(n0), float(Theta0)
    n_peak, t_turn = n0, 0.0
    turned = False
    t = 0.0
    th_hist: List[float] = []
    n_hist: List[float] = []
    t_hist: List[float] = []
    dth_at_cross = float("nan")
    th_at_cross = float("nan")
    n_at_cross = float("nan")
    while t < t_max:
        dn = -n * Th
        dTh = -(Th * Th) + kappa * (n - 1.0) - gamma * Th
        n = max(n + dt * dn, 1e-8)
        Th = Th + dt * dTh
        if abs(Th) > 50.0:
            Th = math.copysign(50.0, Th)
        t += dt
        th_hist.append(Th)
        n_hist.append(n)
        t_hist.append(t)
        if n > n_peak:
            n_peak = n
            t_turn = t
        # detect first upward zero-cross of Θ after compression start
        if (
            not turned
            and len(th_hist) > 1
            and th_hist[-2] < 0.0 <= th_hist[-1]
            and n_peak > n0 * 1.005
        ):
            turned = True
            th_at_cross = Th
            n_at_cross = n
            dth_at_cross = dTh
        if turned and t > t_turn + 8.0:
            break
    # late mean Θ (last 10%)
    late = th_hist[-max(1, len(th_hist) // 10) :]
    late_n = n_hist[-max(1, len(n_hist) // 10) :]
    return {
        "n0": n0,
        "Theta0": Theta0,
        "n_peak": n_peak,
        "overshoot": n_peak / max(n0, 1e-12),
        "t_turn": t_turn,
        "turned": 1.0 if turned else 0.0,
        "Theta_cross": th_at_cross,
        "n_cross": n_at_cross,
        "dTheta_dt_cross": dth_at_cross,
        "Theta_final": Th,
        "late_Theta": float(np.mean(late)),
        "late_n": float(np.mean(late_n)),
        "n_final": n,
    }


def averaging_stress_synthetic() -> Dict[str, float]:
    """Spatial stress drive on synthetic double-bump (scaffold copy)."""
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
    }


def H_kin_from_Theta_heal(Theta_heal: float, d: int, xi: float, c_s: float) -> float:
    """H_kin = Θ_heal * c_s / (d * ξ)  in eV (since ξ in eV^{-1})."""
    return Theta_heal * c_s / (d * xi)


def main() -> None:
    print("=" * 78)
    print("F-A3 / O2 attempt: derive exterior H-cross from medium stress+junction")
    print("=" * 78)

    door = door_state(1e-5)
    xi = door["xi"]
    rb = rho_bounce()
    H_door = door["H_door"]
    H_from_rho_eff = H_friedmann(door["rho_eff"])
    H_from_rho_b = H_friedmann(rb)
    H_from_rho_rad = H_friedmann(door["rho"])

    print("\n[0] Anchors")
    print(f"  c_s = √(3α)           = {C_S:.6f}")
    print(f"  ξ                     = {xi:.6e} eV^{{-1}}  ({XI_AU} AU)")
    print(f"  H_door (shear clock)  = {H_door:.6e} eV")
    print(f"  R_H/ξ                 = {door['R_H_over_xi']:.4f}  (√3 target)")
    print(f"  ρ_eff^{{1/4}} (door)     = {door['T_eff']:.4e} eV")
    print(f"  ρ_bounce^{{1/4}}         = {rb**0.25:.4e} eV")
    print(f"  |H_F(ρ_eff)|          = {H_from_rho_eff:.6e} eV")
    print(f"  |H_F(ρ_bounce)|       = {H_from_rho_b:.6e} eV")
    print(f"  |H_F(ρ_rad door)|     = {H_from_rho_rad:.6e} eV")
    # shear contribution: H_door vs H_F(ρ) — H_door includes shear
    print(f"  H_door / H_F(ρ_eff)   = {H_door / H_from_rho_eff:.4f}  (expect ~1 if ρ_eff from total H)")

    # conversion prefactor: H_kin / Θ_heal = c_s/(d ξ)
    print("\n[1] Kinematic map prefactor  H_kin = Θ_heal · c_s / (d · ξ)")
    for d in (1, 3):
        pref = C_S / (d * xi)
        print(
            f"  d={d}:  H_kin/Θ_heal = {pref:.6e} eV"
            f"   |H_kin(Θ=1)|/H_door = {abs(pref) / H_door:.4e}"
        )

    # medium turn
    print("\n[2] Medium ⟨Θ⟩ turn (0D toy stand-in for M6)")
    cases = [(3.0, -1.0), (6.0, -2.0), (11.0, -2.0)]
    rebounds = []
    for n0, Th0 in cases:
        r = medium_rebound_0d(n0, Th0)
        rebounds.append(r)
        print(
            f"  n0={n0:5.1f} Θ0={Th0:5.1f} → turn={'YES' if r['turned']>0.5 else 'no'}"
            f"  n_cross={r['n_cross']:.3f}  dΘ/dt|cross={r['dTheta_dt_cross']:+.4f}"
            f"  late_Θ={r['late_Theta']:+.4f}  overshoot×{r['overshoot']:.2f}"
        )

    av = averaging_stress_synthetic()
    print(
        f"  synthetic stress_drive={av['stress_drive']:+.4e}"
        f"  net_rhs={av['net_rhs']:+.4e}"
        f"  (need stress>0 channel for turn under averaging identity)"
    )

    # Primary rebound for numbers
    r6 = rebounds[1]
    assert r6["turned"] > 0.5, "0D toy must turn for analysis"
    assert r6["dTheta_dt_cross"] > 0.0, "turn must have Ḣ_kin > 0 at cross"

    print("\n[3] Continuous kinematic cross (medium layer only)")
    print("  Candidate: H_kin(t) := Θ_heal(t) · c_s / (d · ξ)")
    print("  At medium Θ: − → 0 → + with dΘ/dt>0:")
    print(f"    ⇒ H_kin crosses 0 with Ḣ_kin = (c_s/(d ξ))·dΘ/dt > 0  (by algebra)")
    print("  This is NOT yet exterior FRW H — only fluid/acoustic expansion.")

    print("\n[4] Friedmann consistency at the kinematic zero-cross")
    # At Θ=0, H_kin=0. Density at cross is finite.
    n_x = r6["n_cross"]
    # map n to energy density: two legal candidates
    # (a) scale door ρ_eff by n (healing n~1 is background)
    # (b) use ρ_bounce · n  (core ceiling scale)
    rho_x_door = door["rho_eff"] * n_x  # provisional: n in units of background
    rho_x_bounce = rb * n_x
    H_F_door_x = H_friedmann(rho_x_door)
    H_F_b_x = H_friedmann(rho_x_bounce)
    print(f"  at Θ_cross≈0: n_cross={n_x:.4f} (finite)")
    print(f"  H_kin(cross) = 0  exactly (by map)")
    print(f"  |H_F(ρ_eff·n)| = {H_F_door_x:.6e} eV  ≠ 0")
    print(f"  |H_F(ρ_b·n)|   = {H_F_b_x:.6e} eV  ≠ 0")
    print("  OBSTRUCTION A (metric-ON continuous cross):")
    print("    H_kin=0 ∧ ρ>0  violates  H² = 8πGρ/3  (and shear-corrected form).")
    print("    Exterior FRW cannot pass through H=0 at finite density without")
    print("    either ρ_tot→0, modified constraint, or surface stress / metric-off.")

    print("\n[5] Magnitude lock at late medium (re-entry candidate epoch)")
    # When Θ>0 late, compare |H_kin| to |H_F(ρ)|
    Th_late = r6["late_Theta"]
    n_late = r6["late_n"]
    rows = []
    for d in (1, 3):
        Hk = H_kin_from_Theta_heal(Th_late, d, xi, C_S)
        for label, rho in (
            ("ρ_eff·n_late", door["rho_eff"] * max(n_late, 1e-12)),
            ("ρ_eff (door)", door["rho_eff"]),
            ("ρ_bounce·n", rb * max(n_late, 1e-12)),
            ("ρ_bounce", rb),
            ("ρ_rad door", door["rho"]),
        ):
            Hf = H_friedmann(rho)
            ratio = abs(Hk) / Hf if Hf > 0 else float("inf")
            rows.append((d, label, Hk, Hf, ratio))
            print(
                f"  d={d}  H_kin(lateΘ={Th_late:+.3f})={Hk:+.4e}"
                f"  vs H_F({label})={Hf:.4e}  |H_kin|/H_F={ratio:.4e}"
            )

    # Best-case: is there ANY legal ρ such that H_F(ρ)=|H_kin|?
    # ρ_match = 3 H_kin² M_PL² / (8π)
    print("\n[6] ρ required to match |H_kin(late)| under Friedmann")
    for d in (1, 3):
        Hk = abs(H_kin_from_Theta_heal(Th_late, d, xi, C_S))
        rho_need = 3.0 * Hk**2 * M_PL**2 / (8.0 * math.pi)
        print(
            f"  d={d}: |H_kin|={Hk:.4e} ⇒ ρ_need^{{1/4}}={rho_need**0.25:.4e} eV"
            f"   ρ_need/ρ_eff={rho_need/door['rho_eff']:.4e}"
            f"   ρ_need/ρ_b={rho_need/rb:.4e}"
        )

    # Door-entry kinematics: at door, contracting H should match Θ_in
    print("\n[7] Door entry: invert H_door → Θ_heal implied by kinematic map")
    for d in (1, 3):
        # H_door is positive magnitude of contraction; medium Θ0 should be negative
        Th_imp = -H_door * d * xi / C_S
        print(
            f"  d={d}: Θ_heal(door) implied = {Th_imp:.4e}"
            f"   (0D toys use O(1); ratio toy/implied ~ {abs(-2.0/Th_imp):.4e})"
        )
    # Note: 0D toys are dimensionless medium physics, not cosmologically normalized.

    # Shear-dom analytic: H_door = 1/(√3 ξ) when shear dominates
    H_shear = 1.0 / (math.sqrt(3.0) * xi)
    print(f"\n  analytic shear-dom H = 1/(√3 ξ) = {H_shear:.6e}  (vs door {H_door:.6e})")

    # What Θ makes H_kin match H_door at entry?
    print("\n[8] Θ that would match H_door magnitude under H_kin (entry bookkeeping)")
    for d in (1, 3):
        Th_match = H_door * d * xi / C_S
        print(f"  d={d}: |Θ_heal| = H_door·d·ξ/c_s = {Th_match:.6e}")

    # Cross-check: ratio of kinematic prefactor to door scale
    print("\n[9] Order-of-magnitude: |H_kin(Θ=O(1))| / H_door")
    for d in (1, 3):
        ratio = (C_S / (d * xi)) / H_door
        print(
            f"  d={d}: {ratio:.6e}  = c_s/(d) * √3   if H=1/(√3ξ) → "
            f"{C_S * math.sqrt(3.0) / d:.6e}"
        )
    # c_s * √3 / 3 = c_s/√3 ≈ 0.148/1.732 ≈ 0.085 for d=3
    # So O(1) healing Θ gives H_kin ~ 0.085 H_door — not Planck-suppressed,
    # but NOT equal to H_door either. Closing requires Θ_heal ~ d/(c_s√3) ~ 3/0.148/1.73
    # ≈ 12 for d=3 — large for verified 1D overshoot O(1).

    print("\n[10] Verdict assembly")
    # Decision tree
    medium_turn = all(r["turned"] > 0.5 for r in rebounds)
    dth_pos = r6["dTheta_dt_cross"] > 0
    # magnitude mismatch: for d=3, |H_kin|/H_F(ρ_eff) should be ~1 for lock
    Hk3 = abs(H_kin_from_Theta_heal(Th_late, 3, xi, C_S))
    mag_ratio_eff = Hk3 / H_from_rho_eff
    mag_ratio_doorH = Hk3 / H_door

    can_derive = False  # set only if all locks pass without declaration
    # Criteria for YES:
    #  - continuous H_kin cross with Ḣ>0  (yes at medium layer)
    #  - Friedmann consistent at cross (NO — obstruction A)
    #  - magnitude lock at re-entry without knobs (NO — ratios ≪ 1 for late Θ~0
    #    and for O(1) Θ still O(0.1) of door, not ρ-matched)

    print(f"  medium_turn (0D cases)     = {medium_turn}")
    print(f"  dΘ/dt>0 at cross           = {dth_pos}")
    print(f"  |H_kin(late,d=3)|/H_door   = {mag_ratio_doorH:.4e}")
    print(f"  |H_kin(late,d=3)|/H_F(ρeff)= {mag_ratio_eff:.4e}")
    print(f"  Friedmann OK at H_kin=0?   = False (ρ finite)")
    print(f"  can_derive H_re w/o decl.? = {can_derive}")

    print("\n" + "=" * 78)
    print("EXACT OBSTRUCTION (F-A3 cannot close from stocked parts)")
    print("=" * 78)
    print(
        """
  Two stacked obstructions; either alone blocks derived exterior H-cross:

  (A) CONSTRAINT CONFLICT AT THE ZERO
      Identifying exterior H with fluid expansion (H = ⟨Θ⟩_phys/d) makes the
      medium turn into a continuous H:−→0→+ with Ḣ>0 algebraically.
      But at the zero-cross, density remains finite (n_cross ~ O(1–10) in
      healing units; door ρ_eff or ρ_bounce scale). Flat FRW
          H² = 8πG ρ/3   (+ σ²/3)
      then requires H≠0. Metric-ON continuous exterior H-cross at finite ρ
      is inconsistent without a modified constraint or a surface layer.

  (B) METRIC-OFF RE-ENTRY IS BRANCH CHOICE, NOT DERIVATION
      RP-A escapes (A) by dissolving the metric at ξ (Phase II). During the
      non-metric interval Friedmann does not apply, so Θ may cross freely.
      Re-attaching exterior FRW only *after* ⟨Θ⟩>0 selects the expanding
      square-root branch:
          H_re = +√(8πG ρ_re/3)
      That is exactly F-A3's declaration. The medium stress derives the
      *fluid* turn; it does not compute the *exterior* H(t) trajectory
      through zero, because exterior H does not exist in Phase II.

  (C) MAGNITUDE LOCK (secondary, even if sign were granted)
      H_kin(Θ_heal=O(1), d=3) / H_door ≈ c_s/√3 ≈ 0.085
      Late 0D Θ after damping is ≪1, so |H_kin| ≪ H_F(ρ_eff).
      Matching |H_kin|=H_F(ρ) would force either huge Θ_heal ≳ d/(c_s√3)≈12
      (not produced by verified 1D O(1) overshoot) or ρ_re suppressed by
      ~10²–many relative to door ρ_eff — no legal junction fixes this
      without new amplitude law (F-A2 open).

  PASS path not reached. O2 stays PARTIAL. No cyclic cosmology.
"""
    )

    # Machine-readable summary line
    print("SUMMARY_JSON_BEGIN")
    import json

    out = {
        "can_derive_H_re_without_declaration": False,
        "medium_Theta_turn": bool(medium_turn),
        "dTheta_dt_at_cross": r6["dTheta_dt_cross"],
        "n_cross": r6["n_cross"],
        "c_s": C_S,
        "H_door_eV": H_door,
        "H_F_rho_eff_eV": H_from_rho_eff,
        "H_kin_over_H_door_Theta1_d3": C_S / math.sqrt(3.0),
        "H_kin_late_d3_over_H_door": mag_ratio_doorH,
        "H_kin_late_d3_over_HF_eff": mag_ratio_eff,
        "obstruction": "A_friedmann_at_H0_finite_rho + B_metric_off_branch_declaration + C_magnitude_lock",
        "grade_O2": "PARTIAL",
        "cyclic_cosmology": False,
    }
    print(json.dumps(out, indent=2))
    print("SUMMARY_JSON_END")

    # asserts: honesty of the obstruction
    assert medium_turn and dth_pos
    assert H_F_door_x > 0 and H_F_b_x > 0
    assert mag_ratio_eff < 1.0 or Th_late == 0.0  # late damped: tiny ratio
    assert abs(C_S / math.sqrt(3.0) - (C_S / (3 * xi)) / H_shear) < 1e-9
    print("\nASSERTS OK — obstruction stands; no false F-A3 closure.")


if __name__ == "__main__":
    main()
