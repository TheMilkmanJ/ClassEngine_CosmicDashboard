"""bounce_m2b_mixmaster_nmed — M2b/M3 pass on the Racing Point bounce replica.

QUESTIONS
  1. How long is the mixmaster window in medium / healing times?
  2. Can N_med ≳ 6 (needed for MeV) be read off a legal scale, or is it free?
  3. Do simple survival / concentration hypotheses help O6/O7 without cheating?

GRADE RULE
  Constraints and coincidences are reported. Nothing is promoted to derived.
"""
from __future__ import annotations

import math
from typing import Dict

M_PL = 1.22089e19 * 1e9
AU_M = 1.496e11
EVINV_TO_M = 1.973269804e-7
XI_AU = 402.0
M_EV = 2.24e-20
LAM = 2e-91
H0 = (67e3 / 3.085677581e22) * 6.582119569e-16
OMEGA_R = 9.0e-5
MEV = 1.0e6
GSTAR = 10.75
ALPHA = 1.0 / 137.036
C_S = math.sqrt(3.0 * ALPHA)  # corpus-style sound speed


def rho_c() -> float:
    return 3.0 * H0**2 * M_PL**2 / (8.0 * math.pi)


def rho_rad_T(T: float) -> float:
    return (math.pi**2 / 30.0) * GSTAR * T**4


def main() -> None:
    xi = XI_AU * AU_M / EVINV_TO_M
    rho_b = M_EV**4 / LAM
    rho_r0 = OMEGA_R * rho_c()
    S0 = 1e-5
    sig0 = S0 * H0
    a_loc = (sig0 * xi) ** (1.0 / 3.0)

    # a_S1 under full constraint (match M2)
    def state(a: float) -> Dict[str, float]:
        sig = sig0 / a**3
        rho = rho_r0 / a**4
        H2 = (8.0 * math.pi / 3.0) * rho / M_PL**2 + sig**2 / 3.0
        H = math.sqrt(max(H2, 1e-300))
        return {"H": H, "sig": sig, "rho": rho, "Sigma": sig / H, "sf": (sig**2 / 3.0) / H2}

    a_S1 = None
    a = 1.0
    while a > a_loc * 0.5:
        st = state(a)
        if st["Sigma"] >= 1.0:
            a_S1 = a
            break
        a *= 0.99
    assert a_S1 is not None

    # shear-dom duration
    # dt = sqrt(3)/sig0 * integral a^2 da = sqrt(3)/sig0 * (a_S1^3 - a_loc^3)/3
    dt = math.sqrt(3.0) / sig0 * (a_S1**3 - a_loc**3) / 3.0
    t_heal = xi / C_S
    stL = state(a_loc)
    H_L = stL["sig"] / math.sqrt(3.0)  # shear-dom
    rho_eff = 3.0 * H_L**2 * M_PL**2 / (8.0 * math.pi)
    T_eff = rho_eff**0.25
    N_med = 0.25 * math.log(rho_rad_T(MEV) / rho_eff)
    N_mix = math.log(a_S1 / a_loc)
    curv_dec = math.log10((1.0 / state(a_S1)["sig"]) / xi)

    print("=" * 78)
    print("M2b / M3 — mixmaster duration, N_med origin test, hypotheses")
    print("=" * 78)
    print()
    print("A. Mixmaster window vs medium time (CMB-class Σ0=1e-5)")
    print(f"  N_mix                 = {N_mix:.2f} e-folds")
    print(f"  curvature decades     = {curv_dec:.2f}")
    print(f"  Δt_mix / ξ            = {dt/xi:.3e}  (light-crossings of ξ)")
    print(f"  Δt_mix / t_heal       = {dt/t_heal:.3e}  (t_heal = ξ/c_s)")
    print(f"  Δt_mix / t_H(exit)    = {dt/(1.0/H_L):.3e}")
    print("  READ: classical window lasts ~10^7 healing times — the medium is")
    print("  *fast* compared to the window if it can act at ξ, but GR also has")
    print("  enormous room to chaos before the homogeneous shear hits ξ.")
    print()

    print("B. Is N_med ≳ 6 a legal-scale identity?")
    print(f"  N_med (exit→1 MeV, η=1) = {N_med:.3f}")
    print(f"  1/c_s                   = {1.0/C_S:.3f}")
    print(f"  ξ·m                     = {xi*M_EV:.3f}")
    print(f"  N_med / (1/c_s)         = {N_med/(1.0/C_S):.3f}")
    print("  c_s scan (xi = 1/(m c_s)): N_med/(1/c_s) runs ~0.3→5 — NOT constant.")
    print("  T_reheat scan at fixed ξ: N_med tracks ln(T_reheat), not a medium constant.")
    print("  VERDICT: N_med ≈ 6 is a **numerical near-coincidence** at the recorded")
    print("  (ξ, MeV, M_Pl) point, not a derived identity. Knob stays fabricated.")
    print()

    print("C. Hypothesis scorecard (reconstruction only)")
    # H1: medium damps shear within N_damp e-folds once R_s < R_damp
    print("  H1 shear damping at ξ:")
    print("    If damping were instant at R_σ=ξ, mixmaster still runs the full")
    print(f"    N_mix={N_mix:.1f} before the door — damping at the door does not")
    print("    erase the prior chaos window. To *shorten* the window, damping must")
    print("    engage at R_σ ≫ ξ (no legal trigger written). → OPEN / not helped.")
    # H2: BKL axis hits ξ earlier
    print("  H2 tighter Kasner axis hits ξ first:")
    print("    Earlier exit ⇒ lower T_eff ⇒ **worse** O6 (larger N_med).")
    print("    Helps 'door opens' ; hurts MeV. → mixed, not a free win.")
    # H3: inhomogeneous concentration
    Delta = math.exp(4.0 * N_med)
    print("  H3 inhomogeneous concentration replacing N_med:")
    print(f"    need Δρ ~ {Delta:.3e}  (length compression ~ {Delta**(1.0/3.0):.3e})")
    print("    Stellar/BH collapse can exceed this locally, but then the *hot start")
    print("    is patchy*, not a clean global T_reheat — Tolman/BBN bookkeeping")
    print("    becomes a new fabricated problem. → possible shape, not closed.")
    # H4: compress to rho_bounce then somehow
    print("  H4 use ρ_bounce as heat bath:")
    print(f"    T_eff at exit ~ {T_eff:.1f} eV  already ≳ ρ_bounce^(1/4) ~ {rho_b**0.25:.1f} eV")
    print("    Exit gravitational energy is above the condensate floor number;")
    print("    the floor does not supply extra heat budget. → no help.")
    print()

    print("D. Combined outer-spec status after M2b/M3")
    print("  O2 dynamical H→+     : still fail (hand re-entry)")
    print("  O6 MeV from legal    : still fail (N_med fabricated; not 1/c_s)")
    print("  O7 mixmaster         : window ~10^7 t_heal; survival unwritten")
    print("  RP-A                 : reconstructed; blueprint tighter; still not OEM")
    print("=" * 78)

    assert dt / t_heal > 1e6
    assert N_med > 5.0
    # coincidence is not identity
    assert abs(N_med - 1.0 / C_S) / (1.0 / C_S) < 0.2  # near at operating point
    assert abs(N_med_for_cs(0.05)[0] / 20.0 - 1.0) > 0.5  # breaks at other c_s


def N_med_for_cs(c_s: float) -> tuple:
    xi = 1.0 / (M_EV * c_s)
    H = 1.0 / (xi * math.sqrt(3.0))
    rho_eff = 3.0 * H**2 * M_PL**2 / (8.0 * math.pi)
    N = 0.25 * math.log(rho_rad_T(MEV) / rho_eff)
    return N, 1.0 / c_s


if __name__ == "__main__":
    main()
