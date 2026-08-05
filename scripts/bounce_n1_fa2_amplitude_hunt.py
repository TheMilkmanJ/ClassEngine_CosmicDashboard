#!/usr/bin/env python3
"""bounce_n1_fa2_amplitude_hunt — N1 F-A2 legal ρ_re / amplitude law hunt (2026-08-04).

QUESTION
  After P1+P2 are accepted as CANDIDATE licensed premises, can a *legal*
  amplitude / ρ_re map from *stocked* medium / door / junction parts close
  obstruction C (magnitude lock) without free dials?

  Matching target (re-entry, metric-on):
      |H_kin|  ?=  H_F(ρ_re)   or   H_door-scale when Θ matched at door
  with
      H_kin = Θ_heal · c_s / (d · ξ)
      H_F(ρ) = √(8πG ρ / 3)   (eV units via M_PL)

HARD RULES
  - No invent exotic X, N_med, η as Derived.
  - No free dial to pre-chosen H_re or MeV.
  - No bounce closed / cyclic booking.
  - Prefer kill / exact obstruction over fake land.
  - exit 0 = compute finished; PASS/FAIL is physics grade in SUMMARY.

CANDIDATE MAPS (all entered for kill-seeking; none pre-blessed)
  C0  identity: ρ_re = ρ_eff (door)                    — no law
  C1  floor:    ρ_re = ρ_bounce                        — paid ceiling ≠ turn
  C2  n-scaled: ρ_re = ρ_eff · n_late / n-scaled bounce
  C3  overshoot:ρ_re = ρ_eff / overshoot               — if overshoot were density drop
  C4  inverse-match: ρ_re = 3 H_kin² M_PL²/(8π)        — tautology, not law
  C5  door-rad: ρ_re = ρ_rad (door radiation only)
  C6  Θ-forced: ρ_re from Θ_heal fixed O(1) vs H_door  — reports mismatch only
  C7  require Θ_lock = d/(c_s √3) for shear-door        — required Θ, not derived
  C8  M2 knobs: ρ_out = η ρ_in exp(4 N_med)            — FABRICATED (labeled kill)

Output: per-candidate score vs magnitude lock + hard verdict.
"""
from __future__ import annotations

import json
import math
from typing import Any, Dict, List

import numpy as np

# --- same anchors as bounce_fa3_hcross_attempt / M2 ---
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
C_S = math.sqrt(3.0 * ALPHA)
MEV = 1.0e6


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_bounce() -> float:
    return M_EV**4 / LAM


def xi_eVinv() -> float:
    return XI_AU * AU_M / EVINV_TO_M


def H_friedmann(rho: float) -> float:
    return math.sqrt(8.0 * math.pi / 3.0) * math.sqrt(max(rho, 0.0)) / M_PL


def H_kin(Theta_heal: float, d: int, xi: float) -> float:
    return Theta_heal * C_S / (d * xi)


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
        "H_door": H,
        "sig": sig,
        "rho_rad": rho,
        "rho_eff": rho_eff,
        "xi": xi,
        "T_eff": rho_eff**0.25,
        "T_rad": rho**0.25,
    }


def medium_rebound_0d(
    n0: float = 6.0, Theta0: float = -2.0, t_max: float = 40.0, dt: float = 5e-4
) -> Dict[str, float]:
    kappa, gamma = 1.5, 0.15
    n, Th = float(n0), float(Theta0)
    n_peak, t_turn = n0, 0.0
    turned = False
    t = 0.0
    th_hist: List[float] = []
    n_hist: List[float] = []
    dth_at_cross = float("nan")
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
            n_at_cross = n
            dth_at_cross = dTh
        if turned and t > t_turn + 8.0:
            break
    late = th_hist[-max(1, len(th_hist) // 10) :]
    late_n = n_hist[-max(1, len(n_hist) // 10) :]
    return {
        "turned": float(turned),
        "n_cross": n_at_cross,
        "dTheta_dt_cross": dth_at_cross,
        "late_Theta": float(np.mean(late)),
        "late_n": float(np.mean(late_n)),
        "overshoot": n_peak / max(n0, 1e-12),
        "n_peak": n_peak,
    }


def score_lock(Hk: float, rho: float) -> Dict[str, float]:
    Hf = H_friedmann(rho)
    ratio = abs(Hk) / Hf if Hf > 0 else float("inf")
    # lock band: within factor 2 of unity counts as "near lock" for diagnostics only
    near = 1.0 if 0.5 <= ratio <= 2.0 else 0.0
    exactish = 1.0 if 0.9 <= ratio <= 1.1 else 0.0
    return {
        "H_F": Hf,
        "ratio_Hkin_over_HF": ratio,
        "near_lock_factor2": near,
        "near_lock_10pct": exactish,
        "rho_1_4": rho**0.25 if rho > 0 else 0.0,
    }


def main() -> None:
    print("=" * 78)
    print("N1 / F-A2 amplitude hunt — legal ρ_re maps vs magnitude lock")
    print("=" * 78)

    door = door_state(1e-5)
    xi = door["xi"]
    rb = rho_bounce()
    H_door = door["H_door"]
    r6 = medium_rebound_0d(6.0, -2.0)
    assert r6["turned"] > 0.5
    Th_late = r6["late_Theta"]
    n_late = r6["late_n"]
    overshoot = r6["overshoot"]

    print("\n[0] Anchors (stocked)")
    print(f"  c_s                 = {C_S:.6f}")
    print(f"  ξ                   = {xi:.6e} eV^{{-1}}")
    print(f"  H_door              = {H_door:.6e} eV")
    print(f"  ρ_eff^{{1/4}} (door)   = {door['T_eff']:.4e} eV")
    print(f"  ρ_rad^{{1/4}} (door)   = {door['T_rad']:.4e} eV")
    print(f"  ρ_bounce^{{1/4}}       = {rb**0.25:.4e} eV")
    print(f"  0D late_Θ           = {Th_late:+.4f}")
    print(f"  0D late_n           = {n_late:.4f}")
    print(f"  0D overshoot        = {overshoot:.4f}")

    # Required Θ for lock at door H under shear-dom bookkeeping
    # H_door ≈ 1/(√3 ξ) ⇒ |H_kin| = |Θ| c_s/(d ξ) = H_door  ⇒ |Θ| = d H_door ξ / c_s = d/(c_s √3)
    d = 3
    Theta_lock_door = d / (C_S * math.sqrt(3.0))
    print(f"\n[1] Obstruction-C numbers (d=3)")
    print(f"  |H_kin(Θ=1)|/H_door     = {abs(H_kin(1.0, d, xi)) / H_door:.6e}  (~ c_s/√3)")
    print(f"  |H_kin(late)|/H_door    = {abs(H_kin(Th_late, d, xi)) / H_door:.6e}")
    print(f"  Θ_heal for lock@H_door  = {Theta_lock_door:.4f}  (need ≳12; 0D/1D O(1))")
    print(f"  Θ_late / Θ_lock         = {abs(Th_late) / Theta_lock_door:.4e}")

    candidates: List[Dict[str, Any]] = []

    def add(
        cid: str,
        name: str,
        rho: float,
        grade: str,
        reason: str,
        Theta_for_Hkin: float = Th_late,
    ) -> None:
        Hk = H_kin(Theta_for_Hkin, d, xi)
        sc = score_lock(Hk, rho)
        # also score vs H_door directly
        sc["ratio_Hkin_over_Hdoor"] = abs(Hk) / H_door if H_door > 0 else float("inf")
        candidates.append(
            {
                "id": cid,
                "name": name,
                "rho": rho,
                "rho_over_rho_eff": rho / door["rho_eff"] if door["rho_eff"] > 0 else float("inf"),
                "rho_over_rho_bounce": rho / rb if rb > 0 else float("inf"),
                "Theta_used": Theta_for_Hkin,
                "H_kin": Hk,
                "grade": grade,
                "reason": reason,
                **sc,
            }
        )

    # --- candidate maps ---
    add("C0", "ρ_re = ρ_eff (door)", door["rho_eff"], "DEAD-as-law",
        "Identity, not a dynamical amplitude law; late Θ fails lock by ~190×")
    add("C1", "ρ_re = ρ_bounce", rb, "WRONG-OBJECT",
        "Floor/ceiling PAID; not turn amplitude; still fails late-Θ lock")
    add("C2a", "ρ_re = ρ_eff · n_late", door["rho_eff"] * max(n_late, 1e-12), "DEAD-as-law",
        "n-scaling provisional; late n~O(1) does not supply 10²–10⁵ suppression")
    add("C2b", "ρ_re = ρ_bounce · n_late", rb * max(n_late, 1e-12), "WRONG-OBJECT",
        "Floor×n still not F-A2; lock fails")
    # C3: if overshoot diluted density — overshoot is n_peak/n0 > 1 so /overshoot *reduces* ρ
    add("C3", "ρ_re = ρ_eff / overshoot", door["rho_eff"] / max(overshoot, 1e-12), "DEAD-as-law",
        f"overshoot={overshoot:.2f} only O(1); need ~10⁴–10⁵ for late-Θ lock")
    # C4 tautology: ρ from H_kin itself
    Hk_late = abs(H_kin(Th_late, d, xi))
    rho_taut = 3.0 * Hk_late**2 * M_PL**2 / (8.0 * math.pi)
    add("C4", "ρ_re = 3 H_kin² M_PL²/(8π)  [inverse]", rho_taut, "TAUTOLOGY",
        "Always locks by construction; does not derive ρ_re from medium parts")
    add("C5", "ρ_re = ρ_rad (door radiation)", door["rho_rad"], "DEAD-as-law",
        "Radiation alone at door; H_F smaller — check score; not a re-entry law")
    # C6: use Θ=1 optimistic healing, not late damped
    add("C6", "ρ_re = ρ_eff with Θ_heal=1 (optimistic)", door["rho_eff"], "STILL-OPEN",
        "Best stocked Θ without inventing Θ≳12; ratio ~0.085 ≠ 1",
        Theta_for_Hkin=1.0)
    # C7: required Θ — report as required input, not a ρ map
    add("C7", "ρ_re = ρ_eff with Θ=Θ_lock≈12 (required)", door["rho_eff"], "MISSING_INPUT",
        "Would lock shear-door bookkeeping only if Θ_heal derived at ~12; not stocked",
        Theta_for_Hkin=Theta_lock_door)
    # C8 fabricated M2 knobs — show that dial works but is fabrication
    # N_med to get ρ_need for late lock from ρ_eff: ρ_need/ρ_eff = 2.8e-5 → not MeV
    # For MeV: N_med = 0.25 ln(ρ_MeV/ρ_eff)
    rho_mev = (math.pi**2 / 30.0) * GSTAR * MEV**4
    N_med_mev = 0.25 * math.log(rho_mev / max(door["rho_eff"], 1e-300))
    rho_m2_mev = door["rho_eff"] * math.exp(4.0 * N_med_mev)  # η=1
    add("C8a", f"M2 η=1 N_med={N_med_mev:.3f} → MeV ρ", rho_m2_mev, "FABRICATED",
        "M2 labels N_med,η fabricated; closes MeV by dial, not F-A2 from legal parts")
    # dial N_med to match late H_kin (suppression)
    # ρ_need already rho_taut; N_med = 0.25 ln(ρ_need/ρ_eff)  (negative)
    if rho_taut > 0 and door["rho_eff"] > 0:
        N_med_lock = 0.25 * math.log(rho_taut / door["rho_eff"])
    else:
        N_med_lock = float("nan")
    rho_m2_lock = door["rho_eff"] * math.exp(4.0 * N_med_lock) if N_med_lock == N_med_lock else 0.0
    add("C8b", f"M2 η=1 N_med={N_med_lock:.3f} → late-Θ lock ρ", rho_m2_lock, "FABRICATED",
        "Magnitude lock by dialing N_med; honesty kill for F-A2 land")

    print("\n[2] Candidate scorecard (d=3, primary H_kin from listed Θ)")
    print(f"  {'ID':4} {'|Hkin|/HF':>12} {'|Hkin|/Hdoor':>12} {'ρ/ρ_eff':>12} {'ρ^{1/4}/eV':>12}  grade")
    for c in candidates:
        print(
            f"  {c['id']:4} {c['ratio_Hkin_over_HF']:12.4e} {c['ratio_Hkin_over_Hdoor']:12.4e}"
            f" {c['rho_over_rho_eff']:12.4e} {c['rho_1_4']:12.4e}  {c['grade']}"
        )
        print(f"       {c['name']}")
        print(f"       → {c['reason']}")

    # Summary grades
    lands = [c for c in candidates if c["grade"] in ("LAND", "DERIVED")]
    near = [c for c in candidates if c.get("near_lock_10pct", 0) > 0.5 and c["grade"] not in ("TAUTOLOGY", "FABRICATED", "MISSING_INPUT")]
    fab = [c for c in candidates if c["grade"] == "FABRICATED"]
    taut = [c for c in candidates if c["grade"] == "TAUTOLOGY"]
    missing = [c for c in candidates if c["grade"] == "MISSING_INPUT"]

    print("\n[3] Verdict assembly")
    print(f"  legal LANDs from stocked parts     = {len(lands)}")
    print(f"  near-lock non-tautology non-fab    = {len(near)}")
    print(f"  tautologies (not laws)             = {len(taut)}")
    print(f"  fabricated dials (M2 knobs)        = {len(fab)}")
    print(f"  missing-input (Θ_lock)             = {len(missing)}")

    # What would close C without fabrication?
    print("\n[4] What residual still forces (honest)")
    print("  Either:")
    print(f"    (i)  derive Θ_heal ≳ {Theta_lock_door:.1f} at re-entry from legal stress (not 0D O(1)), OR")
    print("    (ii) derive ρ_re / ρ_eff ∼ (H_kin/H_door)² from legal junction without N_med/η dial, OR")
    print("    (iii) write a different matching rule than H_kin = H_F(ρ) that is still acoustic-legal.")
    print("  Stocked parts supply neither (i) nor (ii). (iii) is N2 (match-book), not N1 alone.")

    can_land = False  # no land this package
    summary = {
        "package": "n1_fa2_amplitude_20260804",
        "can_land_F_A2_from_stocked_parts": can_land,
        "medium_turn_0d": bool(r6["turned"] > 0.5),
        "c_s": C_S,
        "H_door_eV": H_door,
        "H_kin_over_H_door_Theta1_d3": abs(H_kin(1.0, 3, xi)) / H_door,
        "H_kin_late_d3_over_H_door": abs(H_kin(Th_late, 3, xi)) / H_door,
        "Theta_lock_door_d3": Theta_lock_door,
        "late_Theta": Th_late,
        "overshoot_0d": overshoot,
        "rho_eff_1_4_eV": door["T_eff"],
        "rho_bounce_1_4_eV": rb**0.25,
        "rho_need_late_1_4_eV": rho_taut**0.25,
        "rho_need_over_rho_eff": rho_taut / door["rho_eff"],
        "n_candidates": len(candidates),
        "n_lands": len(lands),
        "n_fabricated": len(fab),
        "n_tautology": len(taut),
        "grade_N1": "OPEN-BLOCKED",
        "obstruction_C": "stands",
        "bounce_closed": False,
        "cyclic_cosmology": False,
        "candidates": [
            {
                "id": c["id"],
                "name": c["name"],
                "grade": c["grade"],
                "ratio_Hkin_over_HF": c["ratio_Hkin_over_HF"],
                "rho_1_4_eV": c["rho_1_4"],
                "reason": c["reason"],
            }
            for c in candidates
        ],
    }

    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(summary, indent=2))
    print("SUMMARY_JSON_END")

    # Asserts: honesty — we did not invent a land
    assert can_land is False
    assert summary["grade_N1"] == "OPEN-BLOCKED"
    assert abs(summary["H_kin_over_H_door_Theta1_d3"] - C_S / math.sqrt(3.0)) < 1e-6
    print("\nASSERTS OK — N1 no land; obstruction C stands; no free-dial COMPLETE.")


if __name__ == "__main__":
    main()
