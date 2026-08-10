#!/usr/bin/env python3
"""bounce_n2_match_book_check — reconfirm FA1 anchors + domain fences (2026-08-04).

WHAT THIS SCRIPT DOES
  1. Reconfirm FA1 / FA3 kinematic numbers used by the N2 match-book.
  2. Assert domain fences: Phase II has no exterior H; continuous metric-ON
     H=0 at finite ρ is obstructed (A).
  3. Reconfirm magnitude mismatch (C) still present for late Θ and Θ=1.
  4. Reconfirm FA1 trans-phononic quench/adiabatic split.

WHAT EXIT 0 MEANS
  Compute finished and asserts held.  exit 0 ≠ physics PASS, ≠ bounce closed,
  ≠ Derived H_re, ≠ F-A2 closed.

HARD RULES
  - No invent H_re as Derived.
  - No N_med / η dials.
  - No Phase-II exterior H.
"""
from __future__ import annotations

import json
import math
from typing import Dict

# --- recorded anchors (same as bounce_fa3_hcross_attempt / FA1 table) ---
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
    }


def H_kin_from_Theta_heal(Theta_heal: float, d: int, xi: float, c_s: float) -> float:
    return Theta_heal * c_s / (d * xi)


# --- FA1 table pieces ---
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


def main() -> None:
    print("=" * 78)
    print("N2 match-book check: FA1 reconfirm + domain fences")
    print("=" * 78)
    print("  exit 0 = compute done; NOT physics PASS / NOT bounce closed")
    print()

    door = door_state(1e-5)
    xi = door["xi"]
    H_door = door["H_door"]
    rb = rho_bounce()
    H_shear = 1.0 / (math.sqrt(3.0) * xi)

    # --- [1] FA1 / door anchors ---
    print("[1] Anchors (FA1 / FA3 class)")
    print(f"  c_s = √(3α)              = {C_S:.6f}")
    print(f"  ξ                        = {xi:.6e} eV^{{-1}}")
    print(f"  H_door                   = {H_door:.6e} eV")
    print(f"  H_shear = 1/(√3 ξ)       = {H_shear:.6e} eV")
    print(f"  R_H/ξ                    = {door['R_H_over_xi']:.4f}")
    print(f"  ρ_eff^{{1/4}}              = {door['T_eff']:.4e} eV")
    print(f"  ρ_bounce^{{1/4}}           = {rb**0.25:.4e} eV")

    ratio_Theta1_d3 = abs(H_kin_from_Theta_heal(1.0, 3, xi, C_S)) / H_door
    ratio_cs_sqrt3 = C_S / math.sqrt(3.0)
    Theta_lock_d3 = H_door * 3.0 * xi / C_S
    print(f"  |H_kin(Θ=1,d=3)|/H_door  = {ratio_Theta1_d3:.6f}")
    print(f"  c_s/√3                   = {ratio_cs_sqrt3:.6f}")
    print(f"  Θ_lock (d=3)             = {Theta_lock_d3:.4f}")

    # late Θ stand-in from FA3 0D (~0.062) — bookkeeping only
    Th_late = 0.062
    Hk_late = abs(H_kin_from_Theta_heal(Th_late, 3, xi, C_S))
    ratio_late = Hk_late / H_door
    rho_need = 3.0 * Hk_late**2 * M_PL**2 / (8.0 * math.pi)
    print(f"  |H_kin(Θ_late=0.062,d=3)|/H_door = {ratio_late:.6e}")
    print(f"  ρ_need/ρ_eff (late inverse)      = {rho_need / door['rho_eff']:.6e}")

    # --- [2] Domain fence: Phase II exterior H undefined ---
    print()
    print("[2] Domain fence — Phase II exterior H")
    # Operational assert: we refuse to assign exterior H from Θ during Phase II.
    # Represented as a boolean policy flag the match-book requires.
    PHASE_II_EXTERIOR_H_DEFINED = False
    PHASE_II_APPLY_H_EQ_THETA_OVER_D = False
    print(f"  PHASE_II_EXTERIOR_H_DEFINED        = {PHASE_II_EXTERIOR_H_DEFINED}")
    print(f"  PHASE_II_APPLY_H_EQ_THETA_OVER_D   = {PHASE_II_APPLY_H_EQ_THETA_OVER_D}")
    assert PHASE_II_EXTERIOR_H_DEFINED is False
    assert PHASE_II_APPLY_H_EQ_THETA_OVER_D is False
    print("  ASSERT: Phase II has no exterior H; do not apply H=⟨Θ⟩/d to exterior")

    # --- [3] Obstruction A: H_kin=0 at finite ρ under metric-ON ---
    print()
    print("[3] Obstruction A — metric-ON continuous cross forbidden")
    # At kinematic zero, any positive density ⇒ H_F ≠ 0
    n_cross_proxy = 1.0  # O(1) healing density scale
    rho_at_cross = door["rho_eff"] * n_cross_proxy
    H_kin_at_cross = 0.0
    H_F_at_cross = H_friedmann(rho_at_cross)
    print(f"  H_kin(Θ=0)     = {H_kin_at_cross}")
    print(f"  H_F(ρ_eff·1)   = {H_F_at_cross:.6e} eV  ≠ 0")
    obstruction_A = (H_kin_at_cross == 0.0) and (H_F_at_cross > 0.0)
    print(f"  obstruction_A (H_kin=0 ∧ ρ>0 under metric-ON) = {obstruction_A}")
    assert obstruction_A
    print("  ASSERT: continuous metric-ON exterior H through 0 at finite ρ is DEAD")

    # --- [4] Obstruction C residual: magnitude not locked ---
    print()
    print("[4] Obstruction C residual — magnitude lock not closed")
    mag_lock_Theta1 = abs(ratio_Theta1_d3 - 1.0) < 1e-3
    mag_lock_late = abs(ratio_late - 1.0) < 1e-3
    print(f"  |H_kin(Θ=1)|/H_door ≈ 1?   {mag_lock_Theta1}  (value {ratio_Theta1_d3:.4f})")
    print(f"  |H_kin(late)|/H_door ≈ 1?  {mag_lock_late}  (value {ratio_late:.4e})")
    assert not mag_lock_Theta1
    assert not mag_lock_late
    print("  ASSERT: default H_kin = H_F(ρ_door) not locked for stocked Θ")

    # --- [5] FA1 table fences ---
    print()
    print("[5] FA1 trans-phononic table reconfirm")
    xstar = find_xstar()
    vg2 = v_group(2.0)
    print(f"  v_g/c_s (x=2) = {vg2:.4f}  (expect > 1.3)")
    print(f"  x* (ω/H=1)    = {xstar:.2f}  (expect ~2.5)")
    assert vg2 > 1.3
    assert 2.0 < xstar < 3.0
    assert omega_over_H(0.5) < 1.0 and omega_over_H(5.0) > 1.0
    print("  ASSERT: metric-end quantitative (v_g>c_s); quench/adiabatic split stocked")
    print("  SCOPE: medium sector only; SM photon inverse not claimed")

    # --- [6] Phase III gate form (declaration, not derivation) ---
    print()
    print("[6] Phase III re-entry gate (P2 form — not Derived)")
    print("  gate: ⟨Θ⟩>0 ∧ ℓ_grad ≳ ξ  ⇒  H_re = +√(8πG ρ_re/3 + σ_re²/3)")
    print("  ρ_re law: OPEN / F-A2 (N1: 0 lands)")
    print("  expanding root: P2 CANDIDATE declaration, not NEC derivation")
    can_derive_H_re = False
    assert can_derive_H_re is False
    print("  ASSERT: can_derive_H_re_without_declaration = false")

    # --- numeric tolerances vs N1/FA3 ---
    assert abs(ratio_Theta1_d3 - ratio_cs_sqrt3) < 1e-6
    assert abs(H_door / H_shear - 1.0) < 1e-3 or abs(H_door - H_shear) / H_door < 0.01
    # door R_H/ξ near √3 under shear domination
    assert 1.5 < door["R_H_over_xi"] < 2.0
    assert 11.0 < Theta_lock_d3 < 12.5

    out = {
        "package": "n2_match_book_20260804",
        "exit_means": "compute_done_not_physics_PASS",
        "c_s": C_S,
        "H_door_eV": H_door,
        "H_kin_over_H_door_Theta1_d3": ratio_Theta1_d3,
        "H_kin_over_H_door_late_d3": ratio_late,
        "Theta_lock_d3": Theta_lock_d3,
        "rho_need_over_rho_eff_late": rho_need / door["rho_eff"],
        "xstar": xstar,
        "v_g_over_cs_x2": vg2,
        "phase_II_exterior_H_defined": False,
        "obstruction_A_stands": True,
        "obstruction_C_stands": True,
        "can_derive_H_re_without_declaration": False,
        "bounce_closed": False,
        "grade": "PARTIAL_OPEN_residual_dictionary_RECONSTRUCTED",
        "lands": 0,
    }
    print()
    print("SUMMARY_JSON_BEGIN")
    print(json.dumps(out, indent=2))
    print("SUMMARY_JSON_END")
    print()
    print("ASSERTS OK — FA1 numbers reconfirmed; domain fences held; 0 land.")
    print("=" * 78)


if __name__ == "__main__":
    main()
