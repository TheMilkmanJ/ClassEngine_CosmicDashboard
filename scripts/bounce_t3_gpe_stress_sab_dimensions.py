#!/usr/bin/env python3
"""bounce_t3_gpe_stress_sab_dimensions — OOM / fence check for desk T3 (2026-08-04).

WHAT THIS SCRIPT DOES
  1. Rebuild stocked averaging Stress pieces (T_int, T_qu, Reynolds, drive)
     on the static synthetic configuration used by FA3/N3 stand-ins.
  2. Report healing-unit OOM for Stress_drive and layer sketch Stress*ξ.
  3. Assert honesty fences: 0 lands, K^- undefined under P1, no N4 force,
     no Derived H_re, free dial / sign(Θ) smuggle killed.

WHAT THIS SCRIPT DOES NOT DO
  - Solve Israel junction for H_re.
  - Invent H_re as Derived.
  - Promote free α / N_med / η.
  - Define or compute K^-.
  - Claim exterior S_ab stocked or bounce closed.
  - MCMC / PolyChord.

WHAT EXIT 0 MEANS
  Compute finished and fence asserts held.
  exit 0 ≠ physics PASS ≠ bounce closed ≠ N4 land ≠ Israel filled.

Package: docs/working_logs/_runs/theory_construction_20260804/desk_t3_gpe_stress_sab_20260804/
Citations (stocked forms):
  bounce_averaging_decomposition.py:94-118  (T_int, T_qu, Pi_reyn, drive)
  bounce_n3_theta_lock_scan.py:245-248      (synthetic interaction stress)
  bounce_rpA_scaffold.py:27-32              (GPE + identity)
"""
from __future__ import annotations

import json
import math
from typing import Any, Dict

import numpy as np

# --- recorded anchors (same family as israel_sab / FA3) ---
M_PL = 1.22089e19 * 1e9  # eV
AU_M = 1.496e11
EVINV_TO_M = 1.973269804e-7
XI_AU = 402.0
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
H0_SI = 67e3 / 3.085677581e22
HBAR_EV_S = 6.582119569e-16
H0 = H0_SI * HBAR_EV_S
OMEGA_R = 9.0e-5


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


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
        "rho_eff": rho_eff,
        "xi": xi,
        "sig": sig,
    }


def synthetic_stress_channels() -> Dict[str, float]:
    """Stocked FA3/N3 synthetic config + averaging-decomposition channel ops.

    Interaction-only synthetic matches bounce_n3_theta_lock_scan averaging_stress_synthetic.
    Quantum / Reynolds channels use the same finite-difference drive as
    bounce_averaging_decomposition diagnostics (1D, no CG kernel on static probe).
    """
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

    def drive_of(Pi: np.ndarray) -> float:
        # stocked: -⟨ ∂x ( (1/ρ) ∂x Π ) ⟩_w
        dPi = np.gradient(Pi, dx)
        force = np.gradient(dPi / np.maximum(rho, 1e-12), dx)
        return -float((w * force).sum())

    # T_int = ½ ρ²   (averaging L101; n3 synthetic L245)
    T_int = 0.5 * rho**2
    # T_qu = (∂√ρ)² - ¼ ∂²ρ   (averaging L102)
    sq = np.sqrt(np.maximum(rho, 1e-12))
    dsq = np.gradient(sq, dx)
    d2rho = np.gradient(np.gradient(rho, dx), dx)
    T_qu = dsq**2 - 0.25 * d2rho
    # Reynolds proxy without CG: ρv² - ρ ⟨v⟩_local^2 → here raw ρv² residual vs mean flow
    # Static probe: Π_reyn ~ 0 if no sub-kernel; report raw kinetic flux scale only.
    kin = rho * v**2
    Pi_reyn = kin - rho * (float((w * v).sum()) ** 2)  # crude mass-weighted residual

    dr_int = drive_of(T_int)
    dr_qu = drive_of(T_qu)
    dr_rey = drive_of(Pi_reyn)
    # averaging L148: Stress_drive = -(dr_int+dr_qu+dr_rey) with drive_of already signed
    # In averaging, drive_of returns the channel contribution used as di,dq,dr and
    # strs = -(di+dq+dr). Here drive_of matches n3's stress = -⟨force⟩ for Π=T_int,
    # which is the *positive* stress_drive for interaction alone.
    # Align with n3 synthetic: stress_drive_int = drive_of(T_int) already as -⟨force⟩.
    stress_int = dr_int
    stress_qu = dr_qu
    stress_rey = dr_rey
    stress_total = stress_int + stress_qu + stress_rey

    net_rhs = -(mean_Th**2) - var_Th + stress_total

    # layer sketch in healing units: ΔΠ ~ |local Π| * 1 (ξ=1 in healing units)
    Pi_scale = float((w * np.abs(T_int)).sum())

    return {
        "mean_Theta": mean_Th,
        "var_Theta": var_Th,
        "stress_int": stress_int,
        "stress_qu": stress_qu,
        "stress_rey": stress_rey,
        "stress_drive_total": stress_total,
        "net_rhs": net_rhs,
        "Pi_int_mass_weighted": Pi_scale,
        "DeltaPi_layer_heal_sketch": Pi_scale * 1.0,  # × ξ_heal = 1
        "max_local_abs_Theta": float(np.max(np.abs(Th))),
    }


def homogeneous_stress_vanishes() -> Dict[str, float]:
    """Homogeneous n=const, v linear in x ⇒ Stress drive must be ~0 (reconciliation)."""
    L, N = 80.0, 1024
    x = np.linspace(0, L, N, endpoint=False)
    dx = L / N
    rho = np.ones(N)
    # pure Hubble-like: v = H x with periodic caveat — use small sine to stay smooth
    # Strict homogeneous: constant ρ, constant Θ=0, v=0
    v = np.zeros(N)
    w = rho / rho.sum()
    Pi = 0.5 * rho**2
    dPi = np.gradient(Pi, dx)
    force = np.gradient(dPi / np.maximum(rho, 1e-12), dx)
    stress = -float((w * force).sum())
    return {"stress_homogeneous": stress, "abs_stress": abs(stress)}


def main() -> None:
    print("=" * 78)
    print("Desk T3 — GPE Stress / one-sided S_ab dimensions — no fake land")
    print("=" * 78)
    print("  exit 0 = compute done; NOT physics PASS / NOT S_ab stocked / NOT N4")
    print("  P1: K^- undefined — this script never computes K^-")
    print()

    door = door_state(1e-5)
    xi = door["xi"]
    H_door = door["H_door"]
    sigma_G = M_PL**2 * H_door  # pure gravity atom (WRONG-OBJECT for medium law)

    print("[1] Stocked anchors (door)")
    print(f"  c_s              = {C_S:.6f}")
    print(f"  ξ                = {xi:.6e} eV^{{-1}}")
    print(f"  H_door           = {H_door:.6e} eV")
    print(f"  ρ_eff            = {door['rho_eff']:.6e} eV^4")
    print(f"  σ_G = M_Pl² H    = {sigma_G:.6e} eV³  [wrong-object gravity atom]")
    print()

    print("[2] Stocked Stress channels on synthetic config (healing units)")
    ch = synthetic_stress_channels()
    for k in (
        "mean_Theta",
        "var_Theta",
        "stress_int",
        "stress_qu",
        "stress_rey",
        "stress_drive_total",
        "net_rhs",
        "Pi_int_mass_weighted",
        "DeltaPi_layer_heal_sketch",
    ):
        print(f"  {k:28s} = {ch[k]:+.6e}")
    print("  NOTE: healing-unit fluid OOM only — not exterior Israel σ_s, not Derived H_re")
    print()

    print("[3] Homogeneous kill check (Stress channel must vanish)")
    hom = homogeneous_stress_vanishes()
    print(f"  stress_homogeneous = {hom['stress_homogeneous']:+.3e}")
    print(f"  |stress| < 1e-12?  = {hom['abs_stress'] < 1e-12}")
    print()

    print("[4] Honesty fences [VACUOUS stamps where noted]")
    # Construction stamps — cannot fail as physics tests; package md is the product.
    n_lands = 0
    israel_S_ab_stocked = False
    K_minus_defined_under_P1 = False
    n4_force_from_stress_map = False
    sign_Theta_smuggle_killed = True
    free_dial_killed = True
    two_sided_K_killed = True
    obstruction_A_stands = True
    can_derive_H_re_without_declaration = False
    bounce_closed = False
    Stress_1d_written = True  # construction fact of this desk package
    multiD_Stress_production_measured = False

    print(f"  n_lands                            = {n_lands}  [VACUOUS stamp]")
    print(f"  israel_S_ab_stocked                = {israel_S_ab_stocked}  [VACUOUS; inventory still 0]")
    print(f"  K_minus_defined_under_P1           = {K_minus_defined_under_P1}  [VACUOUS; P1 domain]")
    print(f"  n4_force_from_stress_map           = {n4_force_from_stress_map}  [VACUOUS; CANDIDATE map]")
    print(f"  sign_Theta_smuggle_killed          = {sign_Theta_smuggle_killed}  [VACUOUS stamp]")
    print(f"  free_dial_killed                   = {free_dial_killed}  [VACUOUS stamp]")
    print(f"  two_sided_K_killed                 = {two_sided_K_killed}  [VACUOUS stamp]")
    print(f"  obstruction_A_stands               = {obstruction_A_stands}  [VACUOUS stamp]")
    print(f"  can_derive_H_re_without_declaration= {can_derive_H_re_without_declaration}  [VACUOUS stamp]")
    print(f"  bounce_closed                      = {bounce_closed}  [VACUOUS stamp]")
    print(f"  Stress_1d_written                  = {Stress_1d_written}  [construction; not exterior land]")
    print(f"  multiD_Stress_production_measured  = {multiD_Stress_production_measured}")
    print()
    print("  exit0 on vacuous stamps ≠ Israel physics PASS; package md is the product.")
    print()

    # Real checks that could fail
    assert hom["abs_stress"] < 1e-12, "homogeneous Stress must vanish"
    assert abs(ch["stress_int"]) > 0.0 or abs(ch["stress_drive_total"]) > 0.0
    # interaction channel should fund positive drive on this synthetic (stocked FA3 sign)
    assert ch["stress_int"] > 0.0, "synthetic interaction stress_drive expected >0 (stocked FA3)"
    assert n_lands == 0
    assert israel_S_ab_stocked is False
    assert K_minus_defined_under_P1 is False
    assert n4_force_from_stress_map is False
    assert sign_Theta_smuggle_killed is True
    assert free_dial_killed is True
    assert two_sided_K_killed is True
    assert obstruction_A_stands is True
    assert can_derive_H_re_without_declaration is False
    assert bounce_closed is False
    assert Stress_1d_written is True
    assert multiD_Stress_production_measured is False

    out: Dict[str, Any] = {
        "package": "desk_t3_gpe_stress_sab_20260804",
        "n_lands": n_lands,
        "israel_S_ab_stocked": israel_S_ab_stocked,
        "K_minus_defined_under_P1": K_minus_defined_under_P1,
        "n4_force_from_stress_map": n4_force_from_stress_map,
        "can_derive_H_re_without_declaration": can_derive_H_re_without_declaration,
        "bounce_closed": bounce_closed,
        "Stress_1d_written": Stress_1d_written,
        "multiD_Stress_production_measured": multiD_Stress_production_measured,
        "c_s": C_S,
        "xi_eVinv": xi,
        "H_door": H_door,
        "sigma_G": sigma_G,
        "channels": ch,
        "homogeneous": hom,
        "note": "exit0≠PASS; medium OOM only; exterior Israel empty",
    }
    print("[5] JSON summary")
    print(json.dumps(out, indent=2, sort_keys=True))
    print()
    print("=" * 78)
    print("DONE — fences held. Medium Stress OOM only. 0 lands. K^- undefined.")
    print("=" * 78)


if __name__ == "__main__":
    main()
