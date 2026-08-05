#!/usr/bin/env python3
"""bounce_israel_junction_inventory — reconfirm stocked numbers + fence asserts (2026-08-04).

WHAT THIS SCRIPT DOES
  1. Reconfirm FA1/FA3/door anchors used by the Israel/junction inventory package.
  2. Assert domain fences: no Phase-II exterior H; obstruction A stands;
     magnitude lock C not closed at stocked Θ.
  3. Assert honesty flags: N_med not Derived; Israel S_ab not stocked;
     can_derive_H_re_without_declaration false; bounce not closed.
  4. Print a compact inventory stamp (counts only — no new physics).

WHAT EXIT 0 MEANS
  Compute finished and asserts held.
  exit 0 ≠ physics PASS ≠ bounce closed ≠ Derived H_re ≠ N4 land ≠ Israel filled.

HARD RULES
  - No invent H_re as Derived.
  - No N_med / η dials sold as Derived.
  - No Phase-II exterior H.
  - No PolyChord / MCMC.
  - Leave MCMCs alone.
"""
from __future__ import annotations

import json
import math
from typing import Dict

# --- recorded anchors (same family as bounce_fa3 / n2 / M2) ---
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
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
MEV = 1.0e6
GSTAR = 10.75


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_bounce() -> float:
    return M_EV**4 / LAM


def xi_eVinv() -> float:
    return XI_AU * AU_M / EVINV_TO_M


def H_friedmann(rho: float) -> float:
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
        "H_door": H,
        "rho": rho,
        "rho_eff": rho_eff,
        "R_H_over_xi": (1.0 / H) / xi,
        "xi": xi,
        "T_eff": rho_eff**0.25,
        "sig": sig,
    }


def H_kin_from_Theta_heal(Theta_heal: float, d: int, xi: float, c_s: float) -> float:
    return Theta_heal * c_s / (d * xi)


def eps(x: float) -> float:
    return x * math.sqrt(1.0 + x * x / 4.0)


def v_group(x: float) -> float:
    return (1.0 + x * x / 2.0) / math.sqrt(1.0 + x * x / 4.0)


def omega_over_H(x: float) -> float:
    return math.sqrt(3.0) * C_S * eps(x)


def find_xstar() -> float:
    lo, hi = 0.5, 10.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if omega_over_H(mid) < 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def rho_rad_T(T_eV: float, g: float = GSTAR) -> float:
    return (math.pi**2 / 30.0) * g * T_eV**4


def main() -> None:
    print("=" * 78)
    print("Israel / junction inventory reconfirm — stocked numbers + fences")
    print("=" * 78)
    print("  exit 0 = compute done; NOT physics PASS / NOT bounce closed / NOT N4 land")
    print()

    door = door_state(1e-5)
    xi = door["xi"]
    H_door = door["H_door"]
    rb = rho_bounce()
    H_shear = 1.0 / (math.sqrt(3.0) * xi)

    # --- [1] Anchors ---
    print("[1] Stocked door / acoustic anchors")
    print(f"  c_s = √(3α)              = {C_S:.6f}")
    print(f"  ξ                        = {xi:.6e} eV^{{-1}}")
    print(f"  H_door                   = {H_door:.6e} eV")
    print(f"  H_shear = 1/(√3 ξ)       = {H_shear:.6e} eV")
    print(f"  R_H/ξ                    = {door['R_H_over_xi']:.4f}")
    print(f"  ρ_eff^{{1/4}}              = {door['T_eff']:.4e} eV")
    print(f"  ρ_bounce^{{1/4}}           = {rb**0.25:.4e} eV")

    ratio_Theta1_d3 = abs(H_kin_from_Theta_heal(1.0, 3, xi, C_S)) / H_door
    ratio_cs_sqrt3 = C_S / math.sqrt(3.0)
    # Single board definition: at d=3, Θ_lock = d/(c_s√3) = 1/√α (analytic; not via numeric H_door)
    Theta_lock_d3 = 3.0 / (C_S * math.sqrt(3.0))
    Theta_lock_via_Hdoor = H_door * 3.0 * xi / C_S  # diagnostic only — shear door ≈ 1/(√3 ξ)
    print(f"  |H_kin(Θ=1,d=3)|/H_door  = {ratio_Theta1_d3:.6f}")
    print(f"  c_s/√3                   = {ratio_cs_sqrt3:.6f}")
    print(f"  Θ_lock (d=3, analytic)   = {Theta_lock_d3:.12f}  [=1/√α]")
    print(f"  Θ_lock via H_door (diag) = {Theta_lock_via_Hdoor:.12f}  (not board value)")

    Th_late = 0.062
    Hk_late = abs(H_kin_from_Theta_heal(Th_late, 3, xi, C_S))
    ratio_late = Hk_late / H_door
    print(f"  |H_kin(Θ_late=0.062,d=3)|/H_door = {ratio_late:.6e}")

    # --- [2] Phase II fence ---
    print()
    print("[2] Domain fence — Phase II exterior H")
    PHASE_II_EXTERIOR_H_DEFINED = False
    PHASE_II_APPLY_H_EQ_THETA_OVER_D = False
    print(f"  PHASE_II_EXTERIOR_H_DEFINED      = {PHASE_II_EXTERIOR_H_DEFINED}")
    print(f"  PHASE_II_APPLY_H_EQ_THETA_OVER_D = {PHASE_II_APPLY_H_EQ_THETA_OVER_D}")
    assert PHASE_II_EXTERIOR_H_DEFINED is False
    assert PHASE_II_APPLY_H_EQ_THETA_OVER_D is False
    print("  ASSERT: Phase II has no exterior H")

    # --- [3] Obstruction A ---
    print()
    print("[3] Obstruction A — continuous metric-ON H through 0 DEAD")
    H_kin_at_cross = 0.0
    H_F_at_cross = H_friedmann(door["rho_eff"])
    obstruction_A = (H_kin_at_cross == 0.0) and (H_F_at_cross > 0.0)
    print(f"  H_kin(Θ=0)   = {H_kin_at_cross}")
    print(f"  H_F(ρ_eff)   = {H_F_at_cross:.6e} eV ≠ 0")
    print(f"  obstruction_A = {obstruction_A}")
    assert obstruction_A
    print("  ASSERT: continuous metric-ON exterior H through 0 at finite ρ is DEAD")

    # --- [4] Obstruction C residual ---
    print()
    print("[4] Obstruction C residual — magnitude lock not closed")
    mag_lock_Theta1 = abs(ratio_Theta1_d3 - 1.0) < 1e-3
    mag_lock_late = abs(ratio_late - 1.0) < 1e-3
    print(f"  |H_kin(Θ=1)|/H_door ≈ 1?  {mag_lock_Theta1}  (value {ratio_Theta1_d3:.4f})")
    print(f"  |H_kin(late)|/H_door ≈ 1? {mag_lock_late}  (value {ratio_late:.4e})")
    assert not mag_lock_Theta1
    assert not mag_lock_late
    print("  ASSERT: magnitude lock C stands open")

    # --- [5] FA1 reconfirm ---
    print()
    print("[5] FA1 medium table reconfirm")
    xstar = find_xstar()
    vg2 = v_group(2.0)
    print(f"  v_g/c_s (x=2) = {vg2:.4f}")
    print(f"  x* (ω/H=1)    = {xstar:.2f}")
    assert vg2 > 1.3
    assert 2.0 < xstar < 3.0
    print("  ASSERT: metric-end quantitative; medium sector only")

    # --- [6] Fabrication fence: N_med not Derived ---
    print()
    print("[6] Fabrication fence — N_med not Derived")
    N_MED_IS_DERIVED = False
    ETA_IS_DERIVED = False
    # sensitivity number only (fabricated path) — must not be asserted as identity
    rho_mev = rho_rad_T(MEV)
    N_med_needed = 0.25 * math.log(rho_mev / max(door["rho_eff"], 1e-300))
    ratio_vs_1cs = N_med_needed / (1.0 / C_S)
    print(f"  N_med_needed (exit→1 MeV, η=1, FABRICATED path) = {N_med_needed:.3f}")
    print(f"  N_med / (1/c_s) at operating point               = {ratio_vs_1cs:.3f}")
    print(f"  N_MED_IS_DERIVED = {N_MED_IS_DERIVED}")
    print(f"  ETA_IS_DERIVED   = {ETA_IS_DERIVED}")
    assert N_MED_IS_DERIVED is False
    assert ETA_IS_DERIVED is False
    # coincidence is near but NOT identity (retired): observation only — do not pin as test invariant
    print(f"  OBSERVE (not assert identity): 0.8 < N_med/(1/c_s)={ratio_vs_1cs:.4f} < 1.0 → {0.8 < ratio_vs_1cs < 1.0}")
    print("  NOTE: N_med remains fabricated knob; 1/c_s coincidence not identity")

    # --- [7] Israel / N4 honesty flags ---
    # VACUOUS (documentation stamps — cannot fail as physics tests; inventory product is CORPUS_INVENTORY.md)
    # REAL asserts that can fail: obstruction_A, mag_lock open, FA1 vg2/xstar, ratio vs c_s/√3, H_door/H_shear
    print()
    print("[7] Israel / N4 honesty flags (VACUOUS documentation stamps — see CORPUS_INVENTORY for earned 0)")
    ISRAEL_S_AB_STOCKED = False  # VACUOUS stamp; real claim is inventory count=0 in CORPUS_INVENTORY
    ISRAEL_K_AB_STOCKED = False  # VACUOUS
    N4_FORCE_BRANCH_DERIVED = False  # VACUOUS
    can_derive_H_re = False  # VACUOUS here; FA3 script reconfirm is real
    bounce_closed = False  # VACUOUS
    lands = 0  # VACUOUS
    print(f"  ISRAEL_S_AB_STOCKED           = {ISRAEL_S_AB_STOCKED}  [VACUOUS stamp]")
    print(f"  ISRAEL_K_AB_STOCKED           = {ISRAEL_K_AB_STOCKED}  [VACUOUS stamp]")
    print(f"  N4_FORCE_BRANCH_DERIVED       = {N4_FORCE_BRANCH_DERIVED}  [VACUOUS stamp]")
    print(f"  can_derive_H_re_w/o_decl.     = {can_derive_H_re}  [VACUOUS stamp]")
    print(f"  bounce_closed                 = {bounce_closed}  [VACUOUS stamp]")
    print(f"  lands                         = {lands}  [VACUOUS stamp]")
    print("  NOTE: exit0 on this block proves nothing about Israel physics; inventory is the product")

    # --- [8] Inventory count stamp (documentation only) ---
    print()
    print("[8] Inventory class counts (documentation stamp — not new physics)")
    # Counts mirror CORPUS_INVENTORY.md §10 — VACUOUS if hardcoded; real claim is the md inventory
    counts = {
        "paid_exterior_door": 7,
        "acoustic_map_and_nogo": 5,
        "fa1_paid": 5,
        "medium_fluid": 5,
        "boundary_constraints": 7,
        "phase_III_declaration_forms": 3,
        "fabricated_m2_labeled": 5,
        "israel_S_ab_equations": 0,  # VACUOUS hardcoded; earned in CORPUS_INVENTORY.md
    }
    for k, v in counts.items():
        print(f"  {k:32s} = {v}")
    print("  NOTE: israel_S_ab_equations=0 is documentation stamp, not a physics test")

    # --- numeric tolerances vs FA3/N2 ---
    assert abs(ratio_Theta1_d3 - ratio_cs_sqrt3) < 1e-6
    assert abs(H_door / H_shear - 1.0) < 1e-2
    assert 1.5 < door["R_H_over_xi"] < 2.0
    assert 11.0 < Theta_lock_d3 < 12.5

    out = {
        "package": "israel_junction_content_20260804",
        "exit_means": "compute_done_not_physics_PASS",
        "c_s": C_S,
        "H_door_eV": H_door,
        "H_kin_over_H_door_Theta1_d3": ratio_Theta1_d3,
        "H_kin_over_H_door_late_d3": ratio_late,
        "Theta_lock_d3": Theta_lock_d3,
        "xstar": xstar,
        "v_g_over_cs_x2": vg2,
        "N_med_needed_fabricated_path": N_med_needed,
        "N_med_over_1_over_cs_OP": ratio_vs_1cs,
        "phase_II_exterior_H_defined": False,
        "obstruction_A_stands": True,
        "obstruction_C_stands": True,
        "N_med_is_Derived": False,
        "israel_S_ab_stocked": False,
        "israel_K_ab_stocked": False,
        "N4_force_branch_derived": False,
        "can_derive_H_re_without_declaration": False,
        "bounce_closed": False,
        "grade": "MISSING_INPUT_N4_inventory_PAID_0_lands",
        "lands": 0,
        "inventory_counts": counts,
    }
    print()
    print("SUMMARY_JSON_BEGIN")
    print(json.dumps(out, indent=2))
    print("SUMMARY_JSON_END")
    print()
    print("ASSERTS OK — stocked numbers reconfirmed; fences held; Israel empty; 0 land.")
    print("=" * 78)


if __name__ == "__main__":
    main()
