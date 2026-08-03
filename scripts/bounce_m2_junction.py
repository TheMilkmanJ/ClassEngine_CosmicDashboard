"""bounce_m2_junction — Milestone M2 of the Racing Point bounce reconstruction.

WHAT M2 DOES
  1. Correct the M1 shear clock once anisotropy dominates
     (Friedmann: H² = 8πG ρ/3 + σ²/3).
  2. Price the mixmaster / shear window between Σ ~ 1 and local exit R_σ = ξ.
  3. Build a *toy* three-phase junction with every free knob labeled fabricated.
  4. Score energy available at exit against a MeV hot start (O6).

WHAT M2 DOES NOT DO
  - Derive microphysical matching (F-A1–F-A3 remain fabricated).
  - Promote RP-A to derived.
  - Solve BKL chaos inside the mixmaster window.

PHASES (toy)
  I   Contracting FRW + shear, legal GR, until σ = 1/ξ (medium door).
  II  Non-metric medium interval: metric off; only energy bookkeeping.
      Fabricated knobs: extra compression e-folds N_med, heat efficiency η.
  III Expanding radiation FRW re-entry with H > 0 and T_reheat.

LEGAL INPUTS
  ξ = 402 AU, m, λ → ρ_bounce, H0, Ω_r order-of-magnitude, σ ∝ a^{-3}.
"""
from __future__ import annotations

import math
from typing import Dict, Optional

import numpy as np

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
MEV = 1.0e6
GSTAR = 10.75


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_rad_of_T(T_eV: float, g: float = GSTAR) -> float:
    return (math.pi**2 / 30.0) * g * T_eV**4


class Clock:
    def __init__(self, Sigma0: float):
        self.Sigma0 = Sigma0
        self.sig0 = Sigma0 * H0
        self.rho_r0 = OMEGA_R * rho_c()
        self.xi = XI_AU * AU_M / EVINV_TO_M
        self.rho_b = M_EV**4 / LAM

    def state(self, a: float) -> Dict[str, float]:
        sig = self.sig0 / a**3
        rho = self.rho_r0 / a**4
        H2 = (8.0 * math.pi / 3.0) * rho / M_PL**2 + sig**2 / 3.0
        H = math.sqrt(max(H2, 1e-300))
        return {
            "a": a,
            "H": H,
            "sig": sig,
            "rho": rho,
            "Sigma": sig / H,
            "shear_frac": (sig**2 / 3.0) / H2,
            "R_H": 1.0 / H,
            "R_s": 1.0 / sig,
            "rho_eff": 3.0 * H**2 * M_PL**2 / (8.0 * math.pi),
        }

    def a_local_exit(self) -> float:
        return (self.sig0 * self.xi) ** (1.0 / 3.0)

    def find_thresholds(self) -> Dict[str, Optional[float]]:
        a_loc = self.a_local_exit()
        # contraction: a from ~1 down to a_loc
        grid = np.logspace(0.0, math.log10(max(a_loc * 0.5, 1e-30)), 4000)
        a_S1 = a_sd = None
        for a in grid:
            st = self.state(a)
            if a_S1 is None and st["Sigma"] >= 1.0:
                a_S1 = float(a)
            if a_sd is None and st["shear_frac"] >= 0.5:
                a_sd = float(a)
        return {"a_loc": a_loc, "a_S1": a_S1, "a_sd": a_sd}


def mixmaster_report(S0: float) -> Dict[str, float]:
    clk = Clock(S0)
    th = clk.find_thresholds()
    a_loc = th["a_loc"]
    stL = clk.state(a_loc)
    out: Dict[str, float] = {
        "Sigma0": S0,
        "a_loc": a_loc,
        "R_H_over_xi": stL["R_H"] / clk.xi,
        "R_s_over_xi": stL["R_s"] / clk.xi,
        "Sigma_loc": stL["Sigma"],
        "shear_frac": stL["shear_frac"],
        "T_rad": stL["rho"] ** 0.25,
        "T_eff": stL["rho_eff"] ** 0.25,
        "rho_over_bounce": stL["rho"] / clk.rho_b,
        "gap_MeV_rad": (MEV / max(stL["rho"] ** 0.25, 1e-30)) ** 4,
        "gap_MeV_eff": (MEV / max(stL["rho_eff"] ** 0.25, 1e-30)) ** 4,
    }
    if th["a_S1"] is not None:
        st1 = clk.state(th["a_S1"])
        out["a_S1"] = th["a_S1"]
        out["N_mix"] = math.log(th["a_S1"] / a_loc)
        out["curv_decades"] = math.log10(st1["R_s"] / clk.xi)
        out["R_H_S1_over_xi"] = st1["R_H"] / clk.xi
    else:
        out["a_S1"] = float("nan")
        out["N_mix"] = float("nan")
        out["curv_decades"] = float("nan")
        out["R_H_S1_over_xi"] = float("nan")
    # e-folds of medium compression so toy radiation inversion hits 1 MeV at η=1:
    # rho_out = rho_eff * e^{4N} = (π²/30) g T_MeV^4  ⇒  N = (1/4) ln(ρ_MeV / ρ_eff)
    rho_mev = rho_rad_of_T(MEV)
    out["N_med_needed"] = 0.25 * math.log(rho_mev / max(stL["rho_eff"], 1e-300))
    return out


def toy_junction(S0: float, N_med: float, eta: float) -> Dict[str, float]:
    """Fabricated Phase II: compress effective density by e^{4 N_med}, heat with η.

    T_reheat from ρ_out = η * ρ_eff_exit * exp(4 N_med), radiation-like.
    H_reheat > 0 by hand on re-entry (expanding branch declaration).
    """
    clk = Clock(S0)
    a_loc = clk.a_local_exit()
    st = clk.state(a_loc)
    rho_in = st["rho_eff"]
    rho_out = eta * rho_in * math.exp(4.0 * N_med)
    # invert radiation formula for T
    # rho = (pi^2/30) g T^4
    T_reh = (rho_out / ((math.pi**2 / 30.0) * GSTAR)) ** 0.25
    H_reh = math.sqrt(8.0 * math.pi / 3.0) * math.sqrt(rho_out) / M_PL
    return {
        "Sigma0": S0,
        "N_med": N_med,
        "eta": eta,
        "rho_in": rho_in,
        "rho_out": rho_out,
        "T_reheat_eV": T_reh,
        "T_reheat_MeV": T_reh / MEV,
        "H_reheat": H_reh,
        "meets_MeV": T_reh >= 0.999 * MEV,  # float edge at exact threshold
        "meets_0p1_MeV": T_reh >= 0.1 * MEV,
    }


def main() -> None:
    print("=" * 78)
    print("M2 — corrected shear clock, mixmaster window, toy junction")
    print("=" * 78)
    print()
    print("A. Corrected exit (H² = 8πGρ/3 + σ²/3), seed scan")
    print(
        f"  {'Σ0':>8} {'N_mix':>8} {'dec':>8} {'R_H/ξ':>8} {'Σ_loc':>8} "
        f"{'T_rad':>10} {'T_eff':>10} {'N_med*':>8}"
    )
    print("  " + "-" * 78)
    # N_med* = e-folds of fabricated medium compression to reach 1 MeV from ρ_eff
    for S0 in [1e-10, 1e-8, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2]:
        r = mixmaster_report(S0)
        print(
            f"  {S0:8.0e} {r['N_mix']:8.2f} {r['curv_decades']:8.2f} "
            f"{r['R_H_over_xi']:8.3f} {r['Sigma_loc']:8.3f} "
            f"{r['T_rad']:10.3e} {r['T_eff']:10.3e} {r['N_med_needed']:8.2f}"
        )

    print()
    print("  M1 correction:")
    print("    Once shear dominates, R_H/ξ → √3 ≈ 1.73 at local exit — NOT hundreds.")
    print("    Local and Hubble cutoffs are nearly simultaneous in the Kasner-like regime.")
    print("    M1's radiation-only R_H/ξ ~ 650 was an inconsistent late-time clock.")
    print()
    print("  Mixmaster window (CMB-class Σ0 = 1e-5):")
    r5 = mixmaster_report(1e-5)
    print(f"    N_mix ≈ {r5['N_mix']:.2f} e-folds of contraction with Σ ≥ 1 before ξ")
    print(f"    curvature dynamic range ≈ {r5['curv_decades']:.1f} decades down to ξ")
    print(f"    R_H/ξ at Σ=1 ≈ {r5['R_H_S1_over_xi']:.3e} (classical chaos room)")
    print()

    print("B. Energy at door vs MeV hot start")
    print(f"  At CMB-class exit: T_rad ≈ {r5['T_rad']:.1f} eV, T_eff(total) ≈ {r5['T_eff']:.1f} eV")
    print(f"  Density gap to 1 MeV thermal: factor {r5['gap_MeV_eff']:.3e} in ρ")
    print(f"  ⇒ fabricated medium compression N_med ≥ {r5['N_med_needed']:.2f}")
    print("    if ρ scales as radiation through Phase II (η=1).")
    print()

    print("C. Toy junction — fabricated (N_med, η) grid for Σ0=1e-5")
    print(f"  {'N_med':>8} {'η':>6} {'T_reh/MeV':>12} {'≥1 MeV?':>10} {'≥0.1 MeV?':>12}")
    print("  " + "-" * 52)
    for N_med in [0.0, 2.0, 4.0, 5.9, 6.0, 8.0]:
        for eta in [0.1, 1.0]:
            t = toy_junction(1e-5, N_med, eta)
            print(
                f"  {N_med:8.2f} {eta:6.2f} {t['T_reheat_MeV']:12.4e} "
                f"{'YES' if t['meets_MeV'] else 'no':>10} "
                f"{'YES' if t['meets_0p1_MeV'] else 'no':>12}"
            )

    print()
    print("=" * 78)
    print("M2 VERDICT (honest)")
    print("=" * 78)
    print("  1. Shear-dom correction: local ξ-exit and Hubble ξ-exit are O(1) apart")
    print("     (R_H/ξ ≈ √3), not hierarchical. 'Local first' is only barely true.")
    print("  2. Mixmaster window is REAL and finite: ~6 e-folds / ~8 curvature decades")
    print("     at CMB-class seed — classical GR can chaos before the medium door.")
    print("  3. Exit energy budget (even converting all shear+rad) is keV-class,")
    print("     not MeV. O6 fails without fabricated Phase-II compression")
    print(f"     N_med ≳ {r5['N_med_needed']:.1f} (or equivalent inhomogeneous concentration).")
    print("  4. Toy junction can *match* outer MeV by dialing (N_med, η) — that is")
    print("     Racing Point aero, not a derivation. Knobs remain fabricated.")
    print("  5. O2 (H→+): re-entry still declared by hand when metric returns;")
    print("     no dynamical Ḣ>0 from legal parts.")
    print("  Grade: M2 computed; RP-A still reconstructed candidate; bounce not derived.")
    print("=" * 78)

    # asserts: shear-dom exit geometry and MeV gap
    assert abs(r5["R_H_over_xi"] - math.sqrt(3.0)) < 0.05
    assert r5["N_mix"] > 3.0
    assert r5["N_med_needed"] > 4.0
    t_ok = toy_junction(1e-5, r5["N_med_needed"], 1.0)
    assert t_ok["meets_MeV"]


if __name__ == "__main__":
    main()
