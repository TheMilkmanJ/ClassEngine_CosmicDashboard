#!/usr/bin/env python3
"""bounce_o6_mev_gap — O6 MeV residual: stocked keV door/floor vs MeV BBN arithmetic.

PACKAGE
  docs/working_logs/_runs/theory_construction_20260804/o6_mev_residual_20260804/

MISSION (N5 residual after bounce_residual_demand P1+P2)
  Reconfirm ONLY stocked keV↔MeV gap arithmetic. Score legal/priced channels
  against the MeV bar. Kill free N_med/η as land. Record sign conflict with
  S2 late-lock dial (MeV wants N_med>0; late lock wants N_med<0).

HARD RULES
  - NO FABRICATIONS · no free N_med/η as Derived · no invent MeV from keV by dial
  - exit 0 ≠ PASS · bounce not closed by O6 alone · leave MCMCs
  - Arithmetic reconfirm only; does not invent a hot-start engine
  - N_med = 1/c_s is coincidence (M2b), not identity

STOCKED ANCHORS
  m = 2.24e-20 eV, λ = 2e-91 → ρ_bounce = m^4/λ → ^(1/4) ≈ 1.06 keV
  M2 door (Σ0=1e-5 CMB-class): T_eff ≈ 2.83 keV, T_rad ≈ 146 eV
  BBN weak-equilibrium bar: T ≳ 1 MeV (g_* = 10.75 radiation density)

Output: gap factors, channel scorecard, lands=0, grade OPEN-BLOCKED.
"""
from __future__ import annotations

import json
import math
from typing import Any, Dict, List

# --- same anchors as bounce_m2 / bounce_s2 / rho_bounce ---
M_PL = 1.22089e19 * 1e9  # eV
AU_M = 1.496e11
EVINV_TO_M = 1.973269804e-7
XI_AU = 402.0
M_EV = 2.24e-20
LAM = 2e-91
H0_SI = 67e3 / 3.085677581e22
HBAR = 6.582119569e-16
H0 = H0_SI * HBAR
OMEGA_R = 9.0e-5
GSTAR = 10.75
MEV = 1.0e6  # eV — BBN weak-equilibrium bar
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)
M_E = 0.51099895e6  # eV
TAU_TC = 0.5 * math.log(2.0)  # T_c / m_e kernel
OVERSHOOT_1D = 1.34  # verified 0D/1D class overshoot (N1/M6 books)
FOCUS_INSTRUMENT_CEILING = 25.0  # spherical drift scaling: focus ≤ 25× at 2% energy bar
FOCUS_BAR_O6 = 1.0e9  # reconstruction bar for volume focus (order-of-magnitude)


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_bounce() -> float:
    return M_EV**4 / LAM


def rho_rad_T(T: float, g: float = GSTAR) -> float:
    return (math.pi**2 / 30.0) * g * T**4


def door(Sigma0: float = 1e-5) -> Dict[str, float]:
    """M2 CMB-class shear door at a_loc where R_σ = ξ."""
    sig0 = Sigma0 * H0
    xi = XI_AU * AU_M / EVINV_TO_M
    a_loc = (sig0 * xi) ** (1.0 / 3.0)
    rho = OMEGA_R * rho_c() / a_loc**4
    sig = sig0 / a_loc**3
    H2 = (8.0 * math.pi / 3.0) * rho / M_PL**2 + sig**2 / 3.0
    H = math.sqrt(max(H2, 1e-300))
    rho_eff = 3.0 * H**2 * M_PL**2 / (8.0 * math.pi)
    return {
        "rho_eff": rho_eff,
        "rho_rad": rho,
        "T_eff": rho_eff**0.25,
        "T_rad": rho**0.25,
        "a_loc": a_loc,
        "xi": xi,
        "H": H,
        "shear_frac": (sig**2 / 3.0) / H2,
    }


def score_channel(
    name: str,
    T_proxy_eV: float,
    rho_proxy: float,
    rho_need: float,
    T_need: float,
    grade: str,
    note: str,
) -> Dict[str, Any]:
    """Score a stocked/priced channel vs MeV bar. No free dial."""
    gap_T = T_need / max(T_proxy_eV, 1e-300)
    gap_rho = rho_need / max(rho_proxy, 1e-300)
    lands = grade in ("LAND", "DERIVED", "PASS")
    return {
        "name": name,
        "T_proxy_eV": T_proxy_eV,
        "gap_T_to_MeV": gap_T,
        "gap_rho_to_MeV": gap_rho,
        "grade": grade,
        "note": note,
        "land": bool(lands),
    }


def main() -> None:
    d = door()
    rb = rho_bounce()
    rm = rho_rad_T(MEV)
    T_b = rb**0.25
    T_eff = d["T_eff"]
    T_rad = d["T_rad"]

    gap_T_eff = MEV / T_eff
    gap_T_b = MEV / T_b
    gap_T_rad = MEV / T_rad
    gap_rho_eff = rm / d["rho_eff"]
    gap_rho_b = rm / rb
    gap_rho_rad = rm / d["rho_rad"]

    # Fabricated M2 compression (η=1) — reported as FABRICATED only
    N_med_mev = 0.25 * math.log(rm / max(d["rho_eff"], 1e-300))
    # S2 late-lock: S_need ≈ 2.8e-5 → N_med = 0.25 ln S (NEGATIVE)
    S_need_late = 2.80e-5  # stocked from FA3/S2 late |H_kin|/H_door
    N_med_late = 0.25 * math.log(S_need_late)
    S_need_th1 = (C_S / math.sqrt(3.0)) ** 2
    N_med_th1 = 0.25 * math.log(S_need_th1)

    # Electron-family gates (clock candidate only)
    T_c = TAU_TC * M_E
    N_med_Tc = 0.25 * math.log(rho_rad_T(T_c) / d["rho_eff"])
    N_med_me = 0.25 * math.log(rho_rad_T(M_E) / d["rho_eff"])

    # Quench channel (task5 priced)
    mc2 = M_EV * C_S**2
    inv_xi = M_EV * C_S
    rho_quench = 0.5 * mc2 * inv_xi**3

    # Linear / volume focus need if compression alone funds MeV from door ρ_eff
    vol_focus_need = gap_rho_eff
    lin_focus_need = vol_focus_need ** (1.0 / 3.0)

    print("=" * 70)
    print("O6 MeV residual — stocked gap arithmetic only")
    print("=" * 70)
    print("\n[0] Stocked anchors")
    print(f"  m                    = {M_EV:.3e} eV")
    print(f"  λ                    = {LAM:.1e}")
    print(f"  ρ_bounce^{{1/4}}        = {T_b:.4e} eV  ({T_b/1e3:.4f} keV)")
    print(f"  ρ_eff^{{1/4}} (door)    = {T_eff:.4e} eV  ({T_eff/1e3:.4f} keV)")
    print(f"  ρ_rad^{{1/4}} (door)    = {T_rad:.4e} eV  ({T_rad:.1f} eV)")
    print(f"  shear_frac (door)    = {d['shear_frac']:.6f}")
    print(f"  MeV bar T            = {MEV:.0e} eV")
    print(f"  ρ_MeV (g_*={GSTAR})   = {rm:.4e} eV^4  (ρ^{{1/4}}={rm**0.25:.4e} eV)")
    print(f"  c_s                  = {C_S:.6f}   1/c_s = {1.0/C_S:.4f}")

    print("\n[1] Gap factors (MeV over stocked scales)")
    print(f"  T_MeV / T_eff        = {gap_T_eff:.4e}  ({math.log10(gap_T_eff):.2f} dex)")
    print(f"  T_MeV / T_bounce     = {gap_T_b:.4e}  ({math.log10(gap_T_b):.2f} dex)")
    print(f"  T_MeV / T_rad(door)  = {gap_T_rad:.4e}  ({math.log10(gap_T_rad):.2f} dex)")
    print(f"  ρ_MeV / ρ_eff        = {gap_rho_eff:.4e}  ({math.log10(gap_rho_eff):.2f} dex)")
    print(f"  ρ_MeV / ρ_bounce     = {gap_rho_b:.4e}  ({math.log10(gap_rho_b):.2f} dex)")
    print(f"  ρ_MeV / ρ_rad(door)  = {gap_rho_rad:.4e}  ({math.log10(gap_rho_rad):.2f} dex)")

    print("\n[2] Fabricated N_med / η path (reported; NOT a land)")
    print(f"  N_med (door→1 MeV, η=1) = {N_med_mev:.4f}   [FABRICATED]")
    print(f"  1/c_s                     = {1.0/C_S:.4f}   [NOT identity]")
    print(f"  N_med / (1/c_s)           = {N_med_mev/(1.0/C_S):.4f}")
    print(f"  N_med late-lock (S2)      = {N_med_late:.4f}   [NEGATIVE — S={S_need_late:.2e}]")
    print(f"  N_med Θ=1 lock            = {N_med_th1:.4f}   [NEGATIVE — S={S_need_th1:.3e}]")
    print("  SIGN CONFLICT: MeV dial wants N_med>0; F-A2 late lock wants N_med<0.")
    print("  One free N_med cannot honestly serve both O6 and obstruction-C close.")

    print("\n[3] Electron-family clock (candidate only; under MeV bar)")
    print(f"  T_c = τ m_e               = {T_c:.4e} eV  ({T_c/1e3:.1f} keV)")
    print(f"  N_med to T_c              = {N_med_Tc:.4f}  → T under MeV by ×{MEV/T_c:.2f}")
    print(f"  N_med to m_e              = {N_med_me:.4f}  → T under MeV by ×{MEV/M_E:.2f}")
    print("  VERDICT: clock candidate only; no corpus mechanism selects the gate.")

    # Channel scorecard
    channels: List[Dict[str, Any]] = []
    channels.append(
        score_channel(
            "C0 door ρ_eff (legal M2)",
            T_eff,
            d["rho_eff"],
            rm,
            MEV,
            "FAIL-scale",
            "keV-class total effective density; gap ρ ~5.5e10",
        )
    )
    channels.append(
        score_channel(
            "C1 floor ρ_bounce (PAID)",
            T_b,
            rb,
            rm,
            MEV,
            "WRONG-OBJECT+FAIL-scale",
            "CSW ceiling PAID; not heat bath; gap ρ ~2.8e12; H4 no help",
        )
    )
    channels.append(
        score_channel(
            "C2 door ρ_rad only",
            T_rad,
            d["rho_rad"],
            rm,
            MEV,
            "FAIL-scale",
            "radiation piece alone colder (~146 eV); worse O6",
        )
    )
    channels.append(
        score_channel(
            "C3 1D overshoot O(1)",
            T_eff * OVERSHOOT_1D**0.25,
            d["rho_eff"] * OVERSHOOT_1D,
            rm,
            MEV,
            "FAIL-scale",
            f"overshoot~{OVERSHOOT_1D} verified; still ~{gap_rho_eff/OVERSHOOT_1D:.1e} short in ρ",
        )
    )
    channels.append(
        score_channel(
            "C4 quench injection (priced)",
            rho_quench**0.25 if rho_quench > 0 else 0.0,
            rho_quench,
            rm,
            MEV,
            "DEAD",
            f"ρ_quench~{rho_quench:.1e} eV^4; ~{d['rho_eff']/rho_quench:.0e}× under door itself",
        )
    )
    channels.append(
        score_channel(
            "C5 electron gate T_c",
            T_c,
            rho_rad_T(T_c),
            rm,
            MEV,
            "CANDIDATE-clock-only",
            f"T_c~{T_c/1e3:.0f} keV; under MeV ×{MEV/T_c:.1f} in T; gate unselected",
        )
    )
    channels.append(
        score_channel(
            "C6 electron gate m_e",
            M_E,
            rho_rad_T(M_E),
            rm,
            MEV,
            "CANDIDATE-clock-only",
            f"m_e=511 keV; under MeV ×{MEV/M_E:.2f} in T; not BBN bar",
        )
    )
    channels.append(
        score_channel(
            "C7 spherical F instrument ceiling",
            T_eff * FOCUS_INSTRUMENT_CEILING**0.25,
            d["rho_eff"] * FOCUS_INSTRUMENT_CEILING,
            rm,
            MEV,
            "INSTRUMENT-CEILING",
            f"energy-clean focus ≲{FOCUS_INSTRUMENT_CEILING}×; O6 needs ~{vol_focus_need:.1e}× in ρ "
            f"(~{lin_focus_need:.0f} linear); ~{vol_focus_need/FOCUS_INSTRUMENT_CEILING:.0e}× short",
        )
    )
    channels.append(
        score_channel(
            "C8 free N_med/η dial to MeV",
            MEV,
            rm,
            rm,
            MEV,
            "FABRICATED",
            f"N_med={N_med_mev:.3f} η=1 closes by dial; killed as Derived; sign-conflicts S2",
        )
    )
    channels.append(
        score_channel(
            "C9 N_med=1/c_s as identity",
            T_eff * math.exp(C_S ** (-1)),  # wrong use if treated as T multiplier — score as label only
            d["rho_eff"] * math.exp(4.0 / C_S),
            rm,
            MEV,
            "COINCIDENCE-not-identity",
            f"N_med/(1/c_s)={N_med_mev/(1.0/C_S):.3f} at op-point; breaks under c_s/T_reheat scan (M2b)",
        )
    )
    channels.append(
        score_channel(
            "C10 SM two-scale bath (task14)",
            float("nan"),
            float("nan"),
            rm,
            MEV,
            "OPEN-SCHEMA",
            "photons ride contraction; candidate reframing — still arrives cold at door "
            "unless pre-door contraction already funded MeV (genesis cascade / task#11)",
        )
    )
    channels.append(
        score_channel(
            "C11 genesis cascade (task#11)",
            float("nan"),
            float("nan"),
            rm,
            MEV,
            "OPEN-SCHEMA",
            "O6 funding moved here after task5 close; dynamical half open; not Derived",
        )
    )

    print("\n[4] Channel scorecard (stocked / priced / labeled)")
    print(f"  {'name':38s}  {'gap_T':>10s}  {'gap_ρ':>12s}  grade")
    n_lands = 0
    for ch in channels:
        if ch["land"]:
            n_lands += 1
        gt = ch["gap_T_to_MeV"]
        gr = ch["gap_rho_to_MeV"]
        gt_s = f"{gt:.2e}" if gt == gt else "n/a"
        gr_s = f"{gr:.2e}" if gr == gr else "n/a"
        print(f"  {ch['name']:38s}  {gt_s:>10s}  {gr_s:>12s}  {ch['grade']}")
        print(f"      {ch['note']}")

    print("\n[5] Focus / compression geometry (if O6 funded by F alone)")
    print(f"  volume focus need (ρ_MeV/ρ_eff) = {vol_focus_need:.4e}")
    print(f"  linear compression need         = {lin_focus_need:.4e}")
    print(f"  instrument energy-clean ceiling ≈ {FOCUS_INSTRUMENT_CEILING:.0f}×  (drift∝focus^1.28)")
    print(f"  reconstruction O6 focus bar     ≳ {FOCUS_BAR_O6:.1e}")
    print(
        f"  shortfall ceiling→need          ≈ {vol_focus_need/FOCUS_INSTRUMENT_CEILING:.1e}× "
        f"(~{math.log10(vol_focus_need/FOCUS_INSTRUMENT_CEILING):.1f} dex)"
    )
    print("  spherical adaptive grid: energy errors 22–1817%; NOT CONVERGED / unquotable.")

    print("\n[6] Double-kill reminders")
    print("  K1 free N_med/η as Derived land          → HONESTY KILL (M2 labeled fabricated)")
    print("  K2 N_med=1/c_s identity                  → COINCIDENCE KILL (M2b scan)")
    print("  K3 floor ρ_bounce as MeV heat            → WRONG-OBJECT + scale kill")
    print("  K4 P1+P2 alone close O6                  → sign≠temperature kill")
    print("  K5 invent MeV by dialing keV             → FABRICATION fence")
    print("  K6 one N_med for MeV AND late lock       → SIGN CONFLICT (S2)")

    summary = {
        "package": "o6_mev_residual_20260804",
        "T_bounce_eV": T_b,
        "T_eff_door_eV": T_eff,
        "T_rad_door_eV": T_rad,
        "T_MeV_eV": MEV,
        "gap_T_MeV_over_T_eff": gap_T_eff,
        "gap_T_MeV_over_T_bounce": gap_T_b,
        "gap_T_MeV_over_T_rad": gap_T_rad,
        "gap_rho_MeV_over_rho_eff": gap_rho_eff,
        "gap_rho_MeV_over_rho_bounce": gap_rho_b,
        "gap_rho_MeV_over_rho_rad": gap_rho_rad,
        "N_med_fabricated_eta1": N_med_mev,
        "N_med_late_lock_S2": N_med_late,
        "N_med_theta1_lock": N_med_th1,
        "N_med_is_Derived": False,
        "N_med_equals_1_over_cs": False,
        "sign_conflict_MeV_vs_late_lock": True,
        "vol_focus_need": vol_focus_need,
        "lin_focus_need": lin_focus_need,
        "focus_instrument_ceiling": FOCUS_INSTRUMENT_CEILING,
        "n_channels": len(channels),
        "lands": n_lands,
        "grade": "OPEN-BLOCKED",
        "bounce_closed": False,
        "cyclic_booked": False,
        "channels": [
            {"name": c["name"], "grade": c["grade"], "land": c["land"]} for c in channels
        ],
    }

    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(summary, indent=2))
    print("SUMMARY_JSON_END")

    # Cross-validation: stocked anchors only
    assert 1000.0 < T_b < 1100.0, "ρ_bounce^{1/4} must be ~1.06 keV"
    assert 2500.0 < T_eff < 3000.0, "door T_eff must be ~2.8 keV"
    assert gap_rho_eff > 1e9, "MeV density gap over door must be enormous"
    assert gap_rho_b > 1e11, "MeV density gap over floor must be enormous"
    assert N_med_mev > 5.0, "fabricated N_med to MeV must be ≳6 class"
    assert N_med_late < 0.0, "late-lock dial must be negative (S2)"
    assert N_med_mev * N_med_late < 0.0, "sign conflict required"
    assert abs(N_med_mev / (1.0 / C_S) - 1.0) > 0.05, "N_med is not exactly 1/c_s"
    assert n_lands == 0, "no legal MeV land from stocked arithmetic"
    assert summary["bounce_closed"] is False
    assert rho_quench < 1e-80

    print("\nASSERTS OK — 0 lands; O6 OPEN-BLOCKED; sign conflict recorded")
    print("exit 0 = arithmetic finished; grade is OPEN-BLOCKED (not PASS)")


if __name__ == "__main__":
    main()
