"""bounce_m1_shear_xi — Milestone M1 of the Racing Point bounce reconstruction.

QUESTION (F-A4)
    On a contracting approach, can the *local* shear curvature radius
        R_σ ≡ 1/σ
    fall to the healing length ξ *before*
        (i)  the Hubble radius R_H ≡ 1/|H| falls to ξ, and
        (ii) the condensate floor density ρ_bounce is exceeded,
    for seeds allowed by late-time isotropy / structure?

WHAT THIS IS
    A scale-clock calculation with recorded numbers. It does **not** derive the
    bounce, write metric matching, or promote RP-A to derived.

LEGAL PARTS USED
    ξ      = 402 AU          (corpus coherence / healing length)
    m, λ   → ρ_bounce        (scripts/rho_bounce.py)
    H0, Ω_r order-of-magnitude cosmology for the radiation clock
    shear free-propagation: σ ∝ a^{-3}  (Bianchi / GR textbook)

DEFINITIONS
    Σ ≡ σ / |H|              anisotropy parameter
    Local exit candidate:    R_σ = ξ  ⇔  σ = 1/ξ
    Hubble exit candidate:   R_H = ξ  ⇔  |H| = 1/ξ
    Local-before-Hubble:     at local exit, R_H / ξ = Σ > 1

    During radiation domination on contraction:
        H(a) = H0 √Ω_r / a^2
        σ(a) = σ0 / a^3      with σ0 = Σ0 H0  (a0 = 1 today)
        path through turnaround cancels for σ∝a^{-3}

MILESTONE GRADE OPTIONS
    PASS-shaped:     open window of Σ0 where local exit precedes Hubble exit
                     and occurs at ρ ≤ ρ_bounce (sub-floor)
    FAIL-shaped:     no such window for any plausible seed
    MIXED:           window exists, but a classical mixmaster interval
                     (Σ ≳ 1 with R_σ ≫ ξ) sits in front of the exit

Nothing here is stamped derived.
"""
from __future__ import annotations

import math

# ---- recorded / standard inputs ---------------------------------------------
M_PL_EV = 1.22089e19 * 1e9
AU_M = 1.496e11
EVINV_TO_M = 1.973269804e-7
XI_AU = 402.0
M_EV = 2.24e-20
LAM = 2e-91

# H0 = 67 km/s/Mpc → eV
H0_SI = 67e3 / 3.085677581e22  # 1/s
HBAR_EV_S = 6.582119569e-16
H0 = H0_SI * HBAR_EV_S  # eV
OMEGA_R = 9.0e-5  # rough, sufficient for scale clock
A_TURN = 2.5  # registered turnaround ballpark; only for commentary


def rho_c_from_H0() -> float:
    """Critical density from H^2 = (8π/3) ρ / M_Pl^2 (full Planck mass)."""
    return 3.0 * H0**2 * M_PL_EV**2 / (8.0 * math.pi)


def main() -> None:
    xi = XI_AU * AU_M / EVINV_TO_M
    rho_b = M_EV**4 / LAM
    rho_b_q = rho_b**0.25
    H_b = math.sqrt(8.0 * math.pi / 3.0) * math.sqrt(rho_b) / M_PL_EV
    rH_b_over_xi = (1.0 / H_b) / xi

    rho_c = rho_c_from_H0()
    rho_r0 = OMEGA_R * rho_c
    H_r0 = H0 * math.sqrt(OMEGA_R)  # |H| = H_r0/a^2 in pure radiation

    sig_exit = 1.0 / xi  # local exit
    H_hub_exit = 1.0 / xi

    # a at Hubble exit under pure radiation: H_r0/a^2 = 1/xi
    a_hub = math.sqrt(H_r0 * xi)
    rho_hub = rho_r0 / a_hub**4

    print("=" * 78)
    print("M1 — shear / local curvature vs ξ vs Hubble (RP-A F-A4 clock)")
    print("=" * 78)
    print(f"  ξ                = {XI_AU:.0f} AU")
    print(f"  ρ_bounce^(1/4)   = {rho_b_q:.3e} eV")
    print(f"  at floor: R_H/ξ  = {rH_b_over_xi:.3f}  (Hubble exit NOT automatic at floor)")
    print(f"  σ_local-exit     = 1/ξ = {sig_exit:.4e} eV")
    print(f"  pure-rad Hubble exit: a={a_hub:.4e}, ρ^(1/4)={rho_hub**0.25:.3e} eV, "
          f"ρ/ρ_b={rho_hub/rho_b:.3e}")
    print()
    print("  Seed scan (Σ0 = σ0/H0 today; σ∝a^{-3} through turnaround):")
    print(f"  {'Σ0':>10} {'a_loc':>12} {'ρ_loc^(1/4)':>12} {'ρ/ρ_b':>10} "
          f"{'R_H/ξ':>10} {'Σ_at_loc':>10} {'a_Σ1':>10} {'R_H(Σ1)/ξ':>12}  flags")
    print("  " + "-" * 110)

    # plausible band: CMB-isotropy class to nonlinear structure
    seeds = [1e-12, 1e-10, 1e-8, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0]

    n_local_first = 0
    n_sub_floor = 0
    n_mixmaster_window = 0
    windows = []

    for S0 in seeds:
        sig0 = S0 * H0
        # local exit: sig0/a^3 = 1/xi
        a_loc = (sig0 * xi) ** (1.0 / 3.0)
        rho_loc = rho_r0 / a_loc**4
        H_loc = H_r0 / a_loc**2
        rH_over_xi = (1.0 / H_loc) / xi
        Sigma_loc = sig_exit / H_loc  # = rH_over_xi

        # when Σ first hits 1 under radiation: σ/H =1
        # (sig0/a^3) / (H_r0/a^2) =1 => sig0/(H_r0 a) =1 => a = sig0/H_r0 = S0 H0/H_r0 = S0/sqrt(Ω_r)
        a_S1 = S0 / math.sqrt(OMEGA_R)
        if a_S1 > 0:
            H_S1 = H_r0 / a_S1**2
            rH_S1_over_xi = (1.0 / H_S1) / xi if H_S1 > 0 else float("inf")
        else:
            rH_S1_over_xi = float("inf")

        local_first = rH_over_xi > 1.0  # Σ_loc > 1
        sub_floor = rho_loc <= rho_b
        # mixmaster window: Σ reaches O(1) while R_σ = R_H still ≫ ξ
        mix = (a_S1 > a_loc) and (rH_S1_over_xi > 10.0) and local_first
        # a_S1 > a_loc means Σ=1 happens at larger a (earlier in contraction) than local exit

        flags = []
        if local_first:
            flags.append("LOC>HUB")
            n_local_first += 1
        else:
            flags.append("HUB>=LOC")
        if sub_floor:
            flags.append("SUB-FLOOR")
            n_sub_floor += 1
        else:
            flags.append("OVER-FLOOR")
        if mix:
            flags.append("MIXMASTER-WINDOW")
            n_mixmaster_window += 1
        if local_first and sub_floor:
            windows.append(S0)

        print(
            f"  {S0:10.0e} {a_loc:12.4e} {rho_loc**0.25:12.4e} {rho_loc/rho_b:10.3e} "
            f"{rH_over_xi:10.3e} {Sigma_loc:10.3e} {a_S1:10.4e} {rH_S1_over_xi:12.3e}  "
            f"{','.join(flags)}"
        )

    # critical seed: local exit exactly at ρ_bounce under pure radiation
    # rho_r0/a^4 = rho_b => a_b = (rho_r0/rho_b)^{1/4}
    a_at_floor = (rho_r0 / rho_b) ** 0.25
    # σ(a_b) = sig0/a_b^3 = 1/ξ => sig0 = a_b^3/ξ => Σ0 = sig0/H0
    S0_crit = (a_at_floor**3 / xi) / H0
    # at floor, R_H/ξ fixed ~12; local-first at floor needs Σ>= R_H/ξ ~12
    # Σ_floor = σ/(H_b) = (1/ξ)/H_b = R_H_b/ξ if σ=1/ξ
    print()
    print("  Critical seed for local exit *exactly* at ρ_bounce (pure-rad clock):")
    print(f"    a(ρ_bounce)     = {a_at_floor:.4e}")
    print(f"    Σ0_crit         = {S0_crit:.4e}")
    print(f"    at floor if σ=1/ξ: Σ = R_H/ξ = {rH_b_over_xi:.3f} > 1 ⇒ local-first at floor")
    print()
    print("  Interpretation:")
    print("    • Larger Σ0 → earlier local exit (lower density), more local-before-Hubble.")
    print("    • CMB-class Σ0 ~ 10^{-5} sits in LOC>HUB + SUB-FLOOR if the rad clock holds.")
    print("    • Tiny Σ0 ≲ few×10^{-10} pushes exit over-floor or hub-first.")
    print("    • Whenever LOC>HUB with room, Σ hits O(1) earlier with R_H/ξ ≫ 1:")
    print("      a classical mixmaster / BKL *window* opens before the medium cutoff ξ.")
    print()

    # --- verdict ---
    print("=" * 78)
    print("M1 VERDICT (honest)")
    print("=" * 78)
    if windows:
        print(f"  Local-before-Hubble AND sub-floor window in Σ0: "
              f"{min(windows):.0e} … {max(windows):.0e}")
        print("  ⇒ F-A4 is PASS-SHAPED on the scale clock: exit *can* precede Hubble exit")
        print("    and can occur before the CSW floor for isotropy-to-structure seeds.")
    else:
        print("  No seed in the scan gives local-first + sub-floor.")
        print("  ⇒ F-A4 is FAIL-SHAPED on this clock.")

    print()
    print("  Caveats (load-bearing, not fine print):")
    print("  1. Pure-radiation H(a) near exit is an approximation; full multi-fluid")
    print("     contraction shifts a_loc by O(1) factors, not 30 orders.")
    print("  2. Σ0 is a homogeneous Bianchi seed. Real collapse is inhomogeneous;")
    print("     overdense patches can reach large local σ earlier (helps RP-A locally).")
    print("  3. MIXMASTER-WINDOW: classical GR can go chaotic (Σ≳1, R_σ≫ξ) *before*")
    print("     the medium cutoff. RP-A needs either to survive that window or to")
    print("     redefine exit by a different curvature invariant. NOT computed here.")
    print("  4. This does NOT write F-A1–F-A3 matching. M1 only prices the shear clock.")
    print("  5. Grade: reconstructed milestone, not a derived bounce.")
    print("=" * 78)

    # hard asserts: floor Hubble factor and that CMB-class seed is local-first sub-floor
    assert rH_b_over_xi > 5.0
    # CMB-class
    S_cmb = 1e-5
    a_cmb = (S_cmb * H0 * xi) ** (1.0 / 3.0)
    rho_cmb = rho_r0 / a_cmb**4
    H_cmb = H_r0 / a_cmb**2
    assert (1.0 / H_cmb) / xi > 1.0, "CMB-class seed should be local-before-Hubble"
    assert rho_cmb < rho_b, "CMB-class seed should exit sub-floor on rad clock"


if __name__ == "__main__":
    main()
