#!/usr/bin/env python3
"""bounce_israel_sab_dimensions — dim/numeric check of CANDIDATE S_ab atoms (2026-08-04).

WHAT THIS SCRIPT DOES
  1. Reconfirm stocked door/medium anchors (same family as FA3 / N2 / Israel inventory).
  2. Evaluate dimension-legal surface-density atoms from stocked quantities only.
  3. Compare medium scales to gravitational door scale M_Pl^2 H_door.
  4. Assert honesty fences: 0 lands, no N4 force, C4/dial killed, obstruction A, no Derived H_re.

WHAT THIS SCRIPT DOES NOT DO
  - Solve Israel junction for H_re.
  - Invent H_re as Derived.
  - Promote free α / N_med / η.
  - Claim bounce closed or S_ab stocked.
  - MCMC / PolyChord.

WHAT EXIT 0 MEANS
  Compute finished and fence asserts held.
  exit 0 ≠ physics PASS ≠ bounce closed ≠ N4 land ≠ Israel filled.

Package: docs/working_logs/_runs/theory_construction_20260804/israel_sab_construction_20260804/
"""
from __future__ import annotations

import json
import math
from typing import Any, Dict

# --- recorded anchors (same family as bounce_fa3 / n2 / israel inventory) ---
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
# 8πG in natural units with M_Pl: G = 1/M_Pl^2
# Israel rough scale: σ ~ M_Pl^2 ΔH  (since [K]~H, 8πG σ ~ [K])


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_bounce() -> float:
    return M_EV**4 / LAM


def xi_eVinv() -> float:
    return XI_AU * AU_M / EVINV_TO_M


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
        "rho_rad": rho,
        "rho_eff": rho_eff,
        "R_H_over_xi": (1.0 / H) / xi,
        "xi": xi,
        "sig": sig,
    }


def H_kin(Theta_heal: float, d: int, xi: float, c_s: float) -> float:
    return Theta_heal * c_s / (d * xi)


def main() -> None:
    print("=" * 78)
    print("Israel S_ab dimension / numeric atoms — no fake land")
    print("=" * 78)
    print("  exit 0 = compute done; NOT physics PASS / NOT S_ab stocked / NOT N4")
    print()

    door = door_state(1e-5)
    xi = door["xi"]
    H_door = door["H_door"]
    H_shear = 1.0 / (math.sqrt(3.0) * xi)
    rb = rho_bounce()
    rho_eff = door["rho_eff"]
    rho_rad = door["rho_rad"]

    print("[1] Stocked anchors")
    print(f"  c_s                       = {C_S:.6f}")
    print(f"  ξ                         = {xi:.6e} eV^{{-1}}")
    print(f"  H_door                    = {H_door:.6e} eV")
    print(f"  H_shear                   = {H_shear:.6e} eV")
    print(f"  R_H/ξ                     = {door['R_H_over_xi']:.4f}")
    print(f"  ρ_eff                     = {rho_eff:.6e} eV^4")
    print(f"  ρ_rad                     = {rho_rad:.6e} eV^4")
    print(f"  ρ_bounce                  = {rb:.6e} eV^4")
    print(f"  ρ_bounce^{{1/4}}            = {rb**0.25:.4e} eV")
    print(f"  m                         = {M_EV:.4e} eV")
    print(f"  M_Pl                      = {M_PL:.6e} eV")

    # --- [2] Dimension-legal surface density atoms [σ_s] = eV^3 ---
    print()
    print("[2] Candidate σ_s atoms (eV^3) — numeric only, not Derived land")

    # C1: ρ_eff * ξ
    sig_C1 = rho_eff * xi
    # C1b: ρ_rad * ξ
    sig_C1b = rho_rad * xi
    # C2: ρ_bounce * ξ
    sig_C2 = rb * xi
    # C3: (1/2) m c_s^2 / ξ^2   (task5 quench * ξ)
    sig_C3 = 0.5 * M_EV * (C_S**2) / (xi**2)
    # C6: M_Pl^2 * H_door   (pure gravity scale; wrong-object for medium law)
    sig_C6 = (M_PL**2) * H_door
    # C6b: M_Pl^2 / ξ
    sig_C6b = (M_PL**2) / xi
    # C7: M_Pl^2 * |Θ|_phys with Θ_heal = 1 and late 0.062, d absorbed into phys map
    # Θ_phys = Θ_heal * c_s / ξ  (healing time t0 = ξ/c_s)
    Theta_phys_1 = 1.0 * C_S / xi
    Theta_phys_late = 0.062 * C_S / xi
    sig_C7_1 = (M_PL**2) * abs(Theta_phys_1)
    sig_C7_late = (M_PL**2) * abs(Theta_phys_late)
    # related: M_Pl^2 * |H_kin(Θ=1,d=3)|
    Hk1 = abs(H_kin(1.0, 3, xi, C_S))
    sig_from_Hkin1 = (M_PL**2) * Hk1

    atoms = {
        "C1_rho_eff_xi": sig_C1,
        "C1b_rho_rad_xi": sig_C1b,
        "C2_rho_bounce_xi": sig_C2,
        "C3_quench_half_m_cs2_over_xi2": sig_C3,
        "C6_Mpl2_H_door": sig_C6,
        "C6b_Mpl2_over_xi": sig_C6b,
        "C7_Mpl2_Theta_phys_heal1": sig_C7_1,
        "C7_Mpl2_Theta_phys_late": sig_C7_late,
        "ref_Mpl2_Hkin_Theta1_d3": sig_from_Hkin1,
    }
    for k, v in atoms.items():
        print(f"  σ[{k:36s}] = {v:.6e} eV^3")

    # ratios to gravitational scale
    print()
    print("[3] Ratios to gravitational door scale σ_G = M_Pl^2 H_door")
    for k, v in atoms.items():
        if k.startswith("C6"):
            continue
        ratio = v / sig_C6 if sig_C6 > 0 else float("nan")
        print(f"  {k:36s} / σ_G = {ratio:.6e}")

    # dim checks (all should be eV^3 — we only construct legal ones)
    print()
    print("[4] Dimension legality (all listed atoms constructed as eV^3)")
    print("  Aρξ  ρ*ξ          OK")
    print("  Amcξ m c_s^2/ξ^2  OK")
    print("  AGH  M_Pl^2 H     OK")
    print("  AΘ   M_Pl^2 Θ_phys OK")
    illegal_Mpl_over_xi = M_PL / xi  # eV^2 — wrong for σ_s
    print(f"  illegal M_Pl/ξ   = {illegal_Mpl_over_xi:.6e} eV^2  (NOT a σ_s)")

    # --- [5] Force-branch / land fences ---
    print()
    print("[5] Force-branch and land fences (documentation + real A check)")
    # Real obstruction A reconfirm
    H_kin_cross = 0.0
    H_F = math.sqrt(8.0 * math.pi / 3.0) * math.sqrt(max(rho_eff, 0.0)) / M_PL
    obstruction_A = (H_kin_cross == 0.0) and (H_F > 0.0)
    print(f"  obstruction_A (H_kin=0, H_F>0 at ρ_eff) = {obstruction_A}")
    assert obstruction_A

    # VACUOUS stamps that mirror package conclusions (cannot fail as physics tests;
    # earned content is CANDIDATE_SAB.md force-branch §3)
    n_candidates = 12
    n_lands = 0
    n_survivor_schemas = 5
    n4_force_from_any_candidate = False  # VACUOUS stamp; earned in CANDIDATE_SAB.md §3
    c4_tautology_killed = True
    free_dial_killed = True
    israel_S_ab_stocked = False
    can_derive_H_re = False
    bounce_closed = False
    N_MED_IS_DERIVED = False

    print(f"  n_candidates                      = {n_candidates}")
    print(f"  n_survivor_schemas                = {n_survivor_schemas}")
    print(f"  n_lands                           = {n_lands}  [VACUOUS stamp]")
    print(f"  n4_force_from_any_candidate       = {n4_force_from_any_candidate}  [VACUOUS; see CANDIDATE_SAB §3]")
    print(f"  c4_tautology_killed               = {c4_tautology_killed}")
    print(f"  free_dial_killed                  = {free_dial_killed}")
    print(f"  israel_S_ab_stocked               = {israel_S_ab_stocked}  [VACUOUS; inventory still 0]")
    print(f"  can_derive_H_re_w/o_declaration   = {can_derive_H_re}  [VACUOUS stamp]")
    print(f"  bounce_closed                     = {bounce_closed}  [VACUOUS stamp]")
    print(f"  N_MED_IS_DERIVED                  = {N_MED_IS_DERIVED}")
    print("  NOTE: exit0 on vacuous stamps ≠ Israel physics PASS; package md is the product")

    assert n_lands == 0
    assert n4_force_from_any_candidate is False
    assert c4_tautology_killed is True
    assert free_dial_killed is True
    assert israel_S_ab_stocked is False
    assert can_derive_H_re is False
    assert bounce_closed is False
    assert N_MED_IS_DERIVED is False

    # numeric sanity vs inventory
    ratio_cs = C_S / math.sqrt(3.0)
    ratio_Hkin = Hk1 / H_door
    assert abs(ratio_Hkin - ratio_cs) < 1e-6
    assert abs(H_door / H_shear - 1.0) < 1e-2
    assert 1.5 < door["R_H_over_xi"] < 2.0
    # quench << gravity (honesty: not a gravitational Israel jump scale)
    assert sig_C3 / sig_C6 < 1e-10
    print()
    print("[6] Sanity")
    print(f"  |H_kin(Θ=1,d=3)|/H_door = {ratio_Hkin:.6f} (= c_s/√3)")
    print(f"  σ_C3/σ_G (quench/gravity) = {sig_C3/sig_C6:.6e}  << 1  (expected)")
    print("  ASSERT: quench surface ≪ gravitational door scale (not a hard GR jump)")

    out: Dict[str, Any] = {
        "package": "israel_sab_construction_20260804",
        "exit_means": "compute_done_not_physics_PASS",
        "c_s": C_S,
        "xi_eVinv": xi,
        "H_door_eV": H_door,
        "rho_eff_eV4": rho_eff,
        "rho_bounce_eV4": rb,
        "sigma_atoms_eV3": atoms,
        "sigma_G_Mpl2_H_door_eV3": sig_C6,
        "sigma_C3_over_sigma_G": sig_C3 / sig_C6,
        "n_candidates": n_candidates,
        "n_survivor_schemas": n_survivor_schemas,
        "n_lands": n_lands,
        "n4_force_from_any_candidate": n4_force_from_any_candidate,
        "c4_tautology_killed": c4_tautology_killed,
        "free_dial_killed": free_dial_killed,
        "obstruction_A_stands": True,
        "israel_S_ab_stocked": False,
        "can_derive_H_re_without_declaration": False,
        "bounce_closed": False,
        "N_med_is_Derived": False,
        "grade": "CANDIDATE_maps_0_lands_N4_still_MISSING_INPUT",
        "survivors": ["C1", "C3", "C7", "C8", "C9"],
    }
    print()
    print("SUMMARY_JSON_BEGIN")
    print(json.dumps(out, indent=2))
    print("SUMMARY_JSON_END")
    print()
    print("ASSERTS OK — dims evaluated; fences held; 0 land; N4 not forced.")
    print("=" * 78)


if __name__ == "__main__":
    main()
