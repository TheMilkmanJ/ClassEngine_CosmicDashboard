#!/usr/bin/env python3
"""bounce_s2_rho_suppression_hunt — S2 ρ_re/ρ_eff suppression law without dial (2026-08-04).

QUESTION
  N1 showed late lock needs ρ_need/ρ_eff ~ 2.8e-5 (or Θ_lock ~ 12).
  Does any *legal* junction/medium expression from *stocked* parts produce
  such suppression without fabricated M2 knobs (N_med, η)?

TARGET SUPPRESSION
  S ≡ ρ_re / ρ_eff
  late  : S_need = (H_kin(Θ_late)/H_door)² ~ 2.8e-5
  Θ=1   : S_need = (H_kin(1)/H_door)² = (c_s/√3)² ~ 7.3e-3

CANDIDATES SCORED (can-exist + should-not-exist in package docs)
  A1  acoustic dilution over healing lengths (stocked c_s, ξ, H·t_heal)
  A2  shear dilution / shear energy split
  A3  radiation vs medium (door ρ_rad/ρ_eff)
  A4  mixmaster window e-folds N_mix *if used as derived* (legal N_mix; illegal arrow)
  A5  free N_med dial to target ratio — EXPLICIT KILL (fabricated)
  A6  0D overshoot / n_late O(1) dilution
  A7  quench channel (door budget) — wrong scale
  A8  inverse (H_kin/H_door)² tautology — not a medium law

HARD RULES
  - No invent H_re · no free N_med/η as Derived land · no bounce closed
  - N_mix from shear clock is stocked; using it as Phase-II compression/expansion
    dial is still fabrication when aimed at a target ratio
  - exit 0 = compute finished; PASS/FAIL is physics grade in SUMMARY
  - Prefer kill / exact obstruction over fake land

Output: required S, stocked-derived factors, shortfall vs need, land count.
"""
from __future__ import annotations

import json
import math
from typing import Any, Dict, List, Optional

import numpy as np

# --- same anchors as bounce_n1_fa2_amplitude_hunt / M2 ---
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
SIGMA0_DOOR = 1e-5  # CMB-class seed (M2 default)


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


def rho_from_H(H: float) -> float:
    return 3.0 * H**2 * M_PL**2 / (8.0 * math.pi)


def door_state(Sigma0: float = SIGMA0_DOOR) -> Dict[str, float]:
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
        "sig0": sig0,
        "rho_rad": rho,
        "rho_eff": rho_eff,
        "xi": xi,
        "T_eff": rho_eff**0.25,
        "T_rad": rho**0.25,
        "shear_frac": (sig**2 / 3.0) / H2,
        "Sigma_loc": sig / H,
        "rho_r0": rho_r0,
    }


def medium_rebound_0d(
    n0: float = 6.0, Theta0: float = -2.0, t_max: float = 40.0, dt: float = 5e-4
) -> Dict[str, float]:
    """Same stand-in as N1 / FA3 (κ=1.5, γ=0.15)."""
    kappa, gamma = 1.5, 0.15
    n, Th = float(n0), float(Theta0)
    n_peak, t_turn = n0, 0.0
    turned = False
    t = 0.0
    th_hist: List[float] = []
    n_hist: List[float] = []
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
        if turned and t > t_turn + 8.0:
            break
    late = th_hist[-max(1, len(th_hist) // 10) :]
    late_n = n_hist[-max(1, len(n_hist) // 10) :]
    return {
        "turned": float(turned),
        "late_Theta": float(np.mean(late)),
        "late_n": float(np.mean(late_n)),
        "overshoot": n_peak / max(n0, 1e-12),
        "n_peak": n_peak,
    }


def mixmaster_N_mix(door: Dict[str, float]) -> Dict[str, float]:
    """Derived N_mix from shear clock (Σ≥1 → a_loc); same construction as M2."""
    sig0 = door["sig0"]
    rho_r0 = door["rho_r0"]
    a_loc = door["a_loc"]
    xi = door["xi"]

    def state(a: float) -> Dict[str, float]:
        sig = sig0 / a**3
        rho = rho_r0 / a**4
        H2 = (8.0 * math.pi / 3.0) * rho / M_PL**2 + sig**2 / 3.0
        H = math.sqrt(max(H2, 1e-300))
        return {"H": H, "sig": sig, "Sigma": sig / H}

    a_S1: Optional[float] = None
    a = 1.0
    while a > a_loc * 0.5:
        st = state(a)
        if st["Sigma"] >= 1.0:
            a_S1 = a
            break
        a *= 0.99
    assert a_S1 is not None
    N_mix = math.log(a_S1 / a_loc)
    # duration in healing times (M2b arithmetic)
    dt = math.sqrt(3.0) / sig0 * (a_S1**3 - a_loc**3) / 3.0
    t_heal = xi / C_S
    return {
        "a_S1": a_S1,
        "N_mix": N_mix,
        "dt_mix_over_t_heal": dt / t_heal,
        "H_t_heal": door["H_door"] * t_heal,
    }


def score_S(
    name: str,
    S: float,
    S_need_late: float,
    S_need_th1: float,
    grade: str,
    reason: str,
    fabricated: bool = False,
    legal_stocked_number: bool = True,
) -> Dict[str, Any]:
    """Score a candidate suppression factor S = ρ_re/ρ_eff against needs."""
    # shortfall: how many times too large (S/S_need); >1 means not enough suppression
    short_late = S / S_need_late if S_need_late > 0 else float("inf")
    short_th1 = S / S_need_th1 if S_need_th1 > 0 else float("inf")
    # magnitude proximity: log10 distance to late need (0 = exact)
    if S > 0 and S_need_late > 0:
        log_dist_late = abs(math.log10(S / S_need_late))
    else:
        log_dist_late = float("inf")
    if S > 0 and S_need_th1 > 0:
        log_dist_th1 = abs(math.log10(S / S_need_th1))
    else:
        log_dist_th1 = float("inf")
    # "near" band for diagnostics only: within factor 2 of late need
    near_late = 1.0 if 0.5 <= short_late <= 2.0 else 0.0
    return {
        "name": name,
        "S": S,
        "shortfall_late_S_over_Sneed": short_late,
        "shortfall_th1_S_over_Sneed": short_th1,
        "log10_dist_late": log_dist_late,
        "log10_dist_th1": log_dist_th1,
        "near_late_factor2": near_late,
        "grade": grade,
        "reason": reason,
        "fabricated": fabricated,
        "legal_stocked_number": legal_stocked_number,
        "counts_as_land": False,  # filled by policy below
    }


def main() -> None:
    print("=" * 78)
    print("S2 — ρ_re/ρ_eff suppression law hunt (no free dial)")
    print("=" * 78)

    door = door_state(SIGMA0_DOOR)
    xi = door["xi"]
    H_door = door["H_door"]
    rho_eff = door["rho_eff"]
    rb = rho_bounce()
    r6 = medium_rebound_0d(6.0, -2.0)
    assert r6["turned"] > 0.5
    Th_late = r6["late_Theta"]
    n_late = r6["late_n"]
    overshoot = r6["overshoot"]
    d = 3
    mix = mixmaster_N_mix(door)

    Hk_late = abs(H_kin(Th_late, d, xi))
    Hk_th1 = abs(H_kin(1.0, d, xi))
    S_need_late = (Hk_late / H_door) ** 2
    S_need_th1 = (Hk_th1 / H_door) ** 2
    # cross-check inverse ρ
    rho_need_late = rho_from_H(Hk_late)
    rho_need_th1 = rho_from_H(Hk_th1)
    assert abs(rho_need_late / rho_eff - S_need_late) / S_need_late < 1e-9
    assert abs(rho_need_th1 / rho_eff - S_need_th1) / S_need_th1 < 1e-9

    Theta_lock = d / (C_S * math.sqrt(3.0))
    N_mix = mix["N_mix"]

    print("\n[0] Anchors (stocked; N1-compatible)")
    print(f"  c_s                    = {C_S:.6f}")
    print(f"  ξ                      = {xi:.6e} eV^{{-1}}")
    print(f"  H_door                 = {H_door:.6e} eV")
    print(f"  ρ_eff^{{1/4}} (door)      = {door['T_eff']:.4e} eV")
    print(f"  ρ_rad^{{1/4}} (door)      = {door['T_rad']:.4e} eV")
    print(f"  ρ_bounce^{{1/4}}          = {rb**0.25:.4e} eV")
    print(f"  shear_frac (door)      = {door['shear_frac']:.6f}")
    print(f"  0D late_Θ              = {Th_late:+.4f}")
    print(f"  0D late_n              = {n_late:.4f}")
    print(f"  0D overshoot           = {overshoot:.4f}")
    print(f"  N_mix (Σ≥1→a_loc)      = {N_mix:.4f}  [derived shear clock, not dial]")
    print(f"  Δt_mix / t_heal        = {mix['dt_mix_over_t_heal']:.3e}")
    print(f"  H_door · t_heal        = {mix['H_t_heal']:.4f}")

    print("\n[1] Required suppression S ≡ ρ_re/ρ_eff for H_kin = H_F(ρ_re)")
    print(f"  |H_kin(Θ=1)|/H_door    = {Hk_th1/H_door:.6e}")
    print(f"  |H_kin(late)|/H_door   = {Hk_late/H_door:.6e}")
    print(f"  Θ_lock @ door (d=3)    = {Theta_lock:.4f}")
    print(f"  S_need (Θ=1)           = {S_need_th1:.6e}   (= (c_s/√3)²)")
    print(f"  S_need (late)          = {S_need_late:.6e}   (= (H_kin_late/H_door)²)")
    print(f"  ρ_need^{{1/4}} late       = {rho_need_late**0.25:.4e} eV")
    print(f"  ρ_need^{{1/4}} Θ=1        = {rho_need_th1**0.25:.4e} eV")

    candidates: List[Dict[str, Any]] = []

    # --- A1 acoustic dilution over healing lengths ---
    # Stocked: t_heal = ξ/c_s; H_door t_heal = 1/(√3 c_s)
    # Candidate expressions that *could* be written from stocked lengths — none derived as ρ_re law.
    H_theal = mix["H_t_heal"]
    S_cs2 = C_S**2
    S_cs4 = C_S**4
    S_exp_Htheal = math.exp(-4.0 * H_theal)  # radiation-like dilution over H·t_heal e-folds
    S_exp_theal = math.exp(-H_theal)  # single-power speculative
    candidates.append(
        score_S(
            "A1a acoustic c_s²",
            S_cs2,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "c_s stocked; c_s² is not a derived ρ_re/ρ_eff map; O(10⁻²) only",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A1b acoustic c_s⁴",
            S_cs4,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "c_s⁴ ~ 4.8e-4 still short of late need by ~17×; not a written medium law",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A1c exp(-4 H t_heal)",
            S_exp_Htheal,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "H·t_heal=1/(√3 c_s) stocked; treating it as radiation e-folds is speculative "
            "and oversuppresses late by ~10²",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A1d exp(-H t_heal)",
            S_exp_theal,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "Single-power exp(-H t_heal)~0.02; not a law and wrong scale for late",
            legal_stocked_number=True,
        )
    )

    # --- A2 shear dilution ---
    # shear_frac ≈ 1: almost all door energy is shear. If one *drops* shear and keeps only rad:
    S_shear_drop = 1.0 - door["shear_frac"]  # residual non-shear fraction = ρ_rad/ρ_eff
    # σ²/3 contribution as "dilution of isotropic ρ" is NOT a re-entry law
    candidates.append(
        score_S(
            "A2a residual non-shear frac (1−shear_frac)",
            S_shear_drop,
            S_need_late,
            S_need_th1,
            "WRONG-OBJECT",
            "Equals ρ_rad/ρ_eff at door; shear cannot be deleted by fiat at re-entry — "
            "σ_re bookkeeping missing; not F-A2",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A2b identity keep-all (S=1, shear kept)",
            1.0,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "No suppression; late fails by ~1/S_need",
            legal_stocked_number=True,
        )
    )

    # --- A3 radiation vs medium energy split ---
    S_rad = door["rho_rad"] / rho_eff
    candidates.append(
        score_S(
            "A3 ρ_rad/ρ_eff (door split)",
            S_rad,
            S_need_late,
            S_need_th1,
            "WRONG-OBJECT",
            "Stocked split; magnitude near late need (~few×) but wrong object — "
            "door radiation ≠ re-entry amplitude law; Θ=1 fails by ~10³",
            legal_stocked_number=True,
        )
    )

    # --- A4 mixmaster N_mix derived (legal number; illegal application as suppression) ---
    S_Nmix = math.exp(-4.0 * N_mix)
    # directional door mean e-folds ~1.6–1.9 from O7; mid 1.73 used as *illustrative stocked band*
    N_dir = 1.73  # O7 mean-e-fold band center (recorded, not dialed to S_need)
    S_Ndir = math.exp(-4.0 * N_dir)
    candidates.append(
        score_S(
            "A4a exp(-4 N_mix) [N_mix derived; arrow illegal]",
            S_Nmix,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            f"N_mix={N_mix:.2f} is derived from Σ≥1→ξ clock, BUT mixmaster is *contraction* "
            "(ρ grows, not diluted). Using exp(-4N_mix) as re-entry suppression is wrong-arrow "
            "bookkeeping; also oversuppresses by ~10⁶ vs late",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A4b exp(-4 N_dir~1.73) [O7 directional; still not law]",
            S_Ndir,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "Directional mean e-folds stocked ~1.6–1.9; exp(-4N) not a written ρ_re law; "
            "scale wrong for both targets",
            legal_stocked_number=True,
        )
    )

    # --- A5 free N_med dial — EXPLICIT KILL ---
    N_med_late = 0.25 * math.log(S_need_late)  # negative "compression"
    N_med_th1 = 0.25 * math.log(S_need_th1)
    rho_mev = (math.pi**2 / 30.0) * GSTAR * MEV**4
    N_med_mev = 0.25 * math.log(rho_mev / max(rho_eff, 1e-300))
    S_Nmed_late = math.exp(4.0 * N_med_late)  # = S_need_late by construction
    candidates.append(
        score_S(
            f"A5a free N_med={N_med_late:.3f} → late lock (KILL)",
            S_Nmed_late,
            S_need_late,
            S_need_th1,
            "FABRICATED",
            f"Hits late S by dial. M2 labels N_med fabricated; M2b: N_med≠1/c_s identity. "
            f"N_med(MeV)=+{N_med_mev:.2f} has *opposite sign* to late-lock dial. "
            "EXPLICIT KILL as F-A2 land",
            fabricated=True,
            legal_stocked_number=False,
        )
    )
    candidates.append(
        score_S(
            f"A5b free N_med={N_med_th1:.3f} → Θ=1 lock (KILL)",
            math.exp(4.0 * N_med_th1),
            S_need_late,
            S_need_th1,
            "FABRICATED",
            "Hits Θ=1 S by dial; same honesty kill",
            fabricated=True,
            legal_stocked_number=False,
        )
    )

    # --- A6 overshoot / n_late ---
    candidates.append(
        score_S(
            "A6a 1/overshoot (0D)",
            1.0 / max(overshoot, 1e-12),
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            f"overshoot={overshoot:.2f} only O(1); need 10⁴–10⁵ for late",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A6b n_late",
            max(n_late, 1e-12),
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            f"n_late={n_late:.3f} O(1); not suppression law",
            legal_stocked_number=True,
        )
    )
    candidates.append(
        score_S(
            "A6c ρ_bounce/ρ_eff",
            rb / rho_eff,
            S_need_late,
            S_need_th1,
            "WRONG-OBJECT",
            "Floor/ceiling PAID; not turn amplitude; short of late by ~700×",
            legal_stocked_number=True,
        )
    )

    # --- A7 quench (task5 door budget) ---
    # ρ_quench ≈ 0.5 · m · c_s² / ξ³ with ξ = 1/(m c_s) in eV units → inv_xi = m c_s
    inv_xi = M_EV * C_S
    mc2 = M_EV * C_S**2
    rho_quench = 0.5 * mc2 * inv_xi**3
    candidates.append(
        score_S(
            "A7 quench ρ_quench/ρ_eff",
            rho_quench / rho_eff,
            S_need_late,
            S_need_th1,
            "DEAD-as-law",
            "Task5: quench injects ~10⁻⁹⁷ of door budget — wrong scale; channel closed for MeV, "
            "useless as controlled F-A2 suppression",
            legal_stocked_number=True,
        )
    )

    # --- A8 tautology ---
    candidates.append(
        score_S(
            "A8 inverse S=(H_kin_late/H_door)² [tautology]",
            S_need_late,
            S_need_late,
            S_need_th1,
            "TAUTOLOGY",
            "Always matches late by construction; residual rename, not medium law (N1 C4)",
            legal_stocked_number=False,
        )
    )

    # Land policy: never for fab/tautology/wrong-object/dead; would need derived law + score
    for c in candidates:
        c["counts_as_land"] = False  # S2: no candidate is a closed derived law

    print("\n[2] Candidate suppression factors S = ρ_re/ρ_eff")
    print(
        f"  {'ID/name':48} {'S':>12} {'S/S_late':>10} {'S/S_Θ1':>10} "
        f"{'log|late|':>9}  grade"
    )
    print("  " + "-" * 110)
    for c in candidates:
        print(
            f"  {c['name'][:48]:48} {c['S']:12.4e} "
            f"{c['shortfall_late_S_over_Sneed']:10.3e} "
            f"{c['shortfall_th1_S_over_Sneed']:10.3e} "
            f"{c['log10_dist_late']:9.3f}  {c['grade']}"
        )
        print(f"       → {c['reason']}")

    # Best non-fabricated among legal_stocked_number and not tautology
    nonfab = [
        c
        for c in candidates
        if (not c["fabricated"])
        and c["grade"] not in ("TAUTOLOGY", "FABRICATED")
        and c["S"] > 0
        and c["S"] < 1.0  # actual suppression (S<1)
    ]
    # Prefer those with S ≤ 1; rank by proximity to late need among non-fab
    nonfab_sorted = sorted(nonfab, key=lambda c: c["log10_dist_late"])
    best = nonfab_sorted[0] if nonfab_sorted else None

    # Also report strongest stocked suppression (smallest S) that is stocked
    stocked_supp = [
        c
        for c in candidates
        if c["legal_stocked_number"]
        and (not c["fabricated"])
        and c["grade"] != "TAUTOLOGY"
        and 0 < c["S"] < 1.0
    ]
    strongest = min(stocked_supp, key=lambda c: c["S"]) if stocked_supp else None

    lands = [c for c in candidates if c["counts_as_land"]]
    fab = [c for c in candidates if c["fabricated"] or c["grade"] == "FABRICATED"]
    taut = [c for c in candidates if c["grade"] == "TAUTOLOGY"]
    near_nonfab = [
        c
        for c in nonfab
        if c.get("near_late_factor2", 0) > 0.5 and c["grade"] not in ("WRONG-OBJECT",)
    ]

    print("\n[3] Verdict assembly")
    print(f"  legal LANDs (derived ρ_re law)     = {len(lands)}")
    print(f"  fabricated dials (N_med class)     = {len(fab)}")
    print(f"  tautologies                        = {len(taut)}")
    print(f"  near-late non-fab non-wrong-obj    = {len(near_nonfab)}")
    if best is not None:
        print(f"  best non-fab by |log10 S/S_late|   = {best['name']}")
        print(f"      S_best                         = {best['S']:.6e}")
        print(f"      S_best / S_need_late           = {best['shortfall_late_S_over_Sneed']:.4e}")
        print(f"      log10 |S/S_need_late|          = {best['log10_dist_late']:.4f}")
        print(f"      grade                          = {best['grade']}")
    if strongest is not None:
        print(f"  strongest stocked S(<1)            = {strongest['name']}")
        print(f"      S_strong                       = {strongest['S']:.6e}")

    print("\n[4] Explicit KILL: free N_med to target ratio")
    print(f"  N_med for late lock  = {N_med_late:+.4f}  (negative = fabricated dilution)")
    print(f"  N_med for Θ=1 lock   = {N_med_th1:+.4f}")
    print(f"  N_med for MeV (η=1)  = {N_med_mev:+.4f}  (positive compression; O6 toy)")
    print("  Verdict: dialing N_med to hit either lock or MeV is M2 fabrication.")
    print("  M2b already showed N_med ≉ 1/c_s as identity. NOT a Derived F-A2 land.")

    print("\n[5] What residual still forces (honest)")
    print("  Stocked parts do NOT supply a derived S = ρ_re/ρ_eff ~ 2.8e-5 law.")
    print("  Closest stocked magnitude (ρ_rad/ρ_eff ~ 7e-6) is WRONG-OBJECT and")
    print("  fails Θ=1 by ~10³. Mixmaster N_mix is real but wrong-arrow as dilution.")
    print("  Still force: (i) derive Θ_heal ≳ 12, or (ii) true junction ρ_re law,")
    print("  or (iii) different matching rule (N2 match-book).")

    can_land = False
    best_S = best["S"] if best is not None else float("nan")
    best_name = best["name"] if best is not None else None
    summary = {
        "package": "s2_rho_suppression_20260804",
        "can_land_rho_suppression_from_stocked_parts": can_land,
        "n_candidates": len(candidates),
        "n_lands": len(lands),
        "n_fabricated": len(fab),
        "n_tautology": len(taut),
        "S_need_late": S_need_late,
        "S_need_Theta1": S_need_th1,
        "H_kin_late_over_H_door": Hk_late / H_door,
        "H_kin_Theta1_over_H_door": Hk_th1 / H_door,
        "Theta_lock_door_d3": Theta_lock,
        "late_Theta": Th_late,
        "overshoot_0d": overshoot,
        "N_mix_derived": N_mix,
        "rho_rad_over_rho_eff": S_rad,
        "N_med_late_lock_FABRICATED": N_med_late,
        "N_med_Theta1_lock_FABRICATED": N_med_th1,
        "N_med_MeV_FABRICATED": N_med_mev,
        "best_nonfab_name": best_name,
        "best_nonfab_S": best_S,
        "best_nonfab_grade": best["grade"] if best else None,
        "best_nonfab_log10_dist_late": best["log10_dist_late"] if best else None,
        "strongest_stocked_S_name": strongest["name"] if strongest else None,
        "strongest_stocked_S": strongest["S"] if strongest else None,
        "grade_S2": "OPEN-BLOCKED",
        "obstruction_C": "stands",
        "bounce_closed": False,
        "cyclic_cosmology": False,
        "exit0_is_not_PASS": True,
        "candidates": [
            {
                "name": c["name"],
                "S": c["S"],
                "grade": c["grade"],
                "shortfall_late": c["shortfall_late_S_over_Sneed"],
                "log10_dist_late": c["log10_dist_late"],
                "fabricated": c["fabricated"],
                "counts_as_land": c["counts_as_land"],
                "reason": c["reason"],
            }
            for c in candidates
        ],
    }

    print("\nSUMMARY_JSON_BEGIN")
    print(json.dumps(summary, indent=2))
    print("SUMMARY_JSON_END")

    assert can_land is False
    assert summary["grade_S2"] == "OPEN-BLOCKED"
    assert summary["bounce_closed"] is False
    assert abs(summary["H_kin_Theta1_over_H_door"] - C_S / math.sqrt(3.0)) < 1e-6
    # free N_med late is negative (dilution dial) while MeV is positive
    assert N_med_late < 0.0
    assert N_med_mev > 5.0
    # ρ_rad/ρ_eff stocked and small
    assert 1e-6 < S_rad < 1e-4
    print("\nASSERTS OK — S2 no land; free N_med killed; obstruction C stands.")


if __name__ == "__main__":
    main()
