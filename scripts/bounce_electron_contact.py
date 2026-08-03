"""bounce_electron_contact — the electron-as-bridge proposal, priced (owner, 2026-07-26).

PROPOSAL (owner): the bounce bridge has something to do with electrons — the
carrier that "lets a current flow" so the dCDF can heat at the crunch.

QUESTIONS
  1. Contact: does the electron bath actually reach the dark sector at the melt?
  2. Presence: are electrons even in the bath at T_c on the contracting branch?
  3. Turn: can any electron / current / counterflow channel supply the
     crunch-sector X with rho_X + p_X negative at the handover?
  4. Clock: does the electron gate legalize the fabricated re-entry knob N_med?

GRADE RULE
  Recorded rates are quoted, new numbers are computed, nothing is promoted to
  derived. NEC signs are class statements, not fits.
"""
from __future__ import annotations

import math

M_PL_GEV = 1.22089e19
M_E_KEV = 510.99895
T_C_KEV = 177.10
GSTAR = 10.75
ALPHA = 1.0 / 137.036
G_EE = 0.064            # tribunal linear-fork vertex g_ee = eps*m_e/v
T_EXIT_KEV = 2.8        # M2 door budget T_eff (CMB-class seed, shear included)
N_MED_MEV = 6.184       # M2: knob value needed for T_reheat >= 1 MeV


def gh_linear(T_kev: float) -> float:
    """Tribunal closed form Gamma/H = alpha g^2 M_Pl / (1.66 sqrt(g*) T)."""
    T_gev = T_kev * 1e-6
    return ALPHA * G_EE**2 * M_PL_GEV / (1.66 * math.sqrt(GSTAR) * T_gev)


def rho_rad_kev4(T_kev: float) -> float:
    return (math.pi**2 / 30.0) * GSTAR * T_kev**4


def n_med_for_gate(T_gate_kev: float) -> float:
    """M2 convention: N_med = (1/4) ln(rho_rad(T_gate)/rho_eff), rho_eff = T_exit^4."""
    return 0.25 * math.log(rho_rad_kev4(T_gate_kev) / T_EXIT_KEV**4)


def main() -> None:
    tau = T_C_KEV / M_E_KEV
    supp = math.exp(-M_E_KEV / T_C_KEV)
    gh_me = gh_linear(M_E_KEV)
    gh_tc = gh_linear(T_C_KEV) * supp

    print("=" * 78)
    print("Electron-as-bridge proposal — priced against the recorded corpus")
    print("=" * 78)
    print()
    print("A. Contact (the 'current' side of the proposal)")
    print(f"  electron-coupled scalar vertex (leptophilic), linear fork g_ee = {G_EE}")
    print(f"  Gamma/H at T = m_e            = {gh_me:.2e}   (tribunal: 1.3e17)")
    print(f"  Gamma/H at T = T_c (thinned)  = {gh_tc:.2e}")
    print("  READ: thermal contact between the electron bath and the dark sector")
    print("  through the dyad is already computed and OVERWHELMING — 15+ orders of")
    print("  margin. The 'wire' the proposal asks for exists and is priced.")
    print()
    print("B. Presence at the melt on the contracting branch")
    print(f"  tau = T_c/m_e                 = {tau:.5f}  (kernel: 1/2 ln2 = 0.34657)")
    print(f"  e+- Boltzmann thinning e^(-m_e/T_c) = {supp:.4f}")
    print("  READ: the melt fires exactly as the e+- bath re-ignites (T_c and m_e")
    print("  are one scale family BY CONSTRUCTION, T_c = tau*m_e). Electrons are")
    print("  ~6% of relativistic abundance at T_c and fully back by T ~ m_e.")
    print()
    print("C. Turn (the bridge itself) — NEC class of every electron channel")
    channels = [
        ("relativistic e+- bath (w=1/3)", "rho + p = (4/3) rho  > 0"),
        ("semi-relativistic e gas", "rho + p = rho + nT   > 0"),
        ("Maxwell stress (pure B, best case)", "rho + p_par = 0 (saturates); rho + p_perp = 2 rho"),
        ("drift current (charge flow)", "adds carrier kinetic energy  > 0"),
        ("two-fluid counterflow (heat current)", "adds rho_n w^2  >= 0"),
    ]
    for name, sign in channels:
        print(f"  {name:38s}: {sign}")
    need = -(4.0 / 3.0) * rho_rad_kev4(T_C_KEV)
    print(f"  flat-FRW bounce requirement         : rho_X + p_X <= {need:.2e} keV^4  (NEGATIVE)")
    print("  READ: every channel in the electron/EM/current lane sits on the")
    print("  NEC-nonnegative side — best case saturation (pure field direction),")
    print("  never negative. The lane misses the turn BY CLASS, not by margin.")
    print()
    print("D. Clock (can the electron gate legalize N_med?)")
    for label, tg in [("T_c gate (condensate melt)", T_C_KEV),
                      ("m_e gate (pair threshold)", M_E_KEV),
                      ("1 MeV (BBN weak-equilibrium bar)", 1000.0)]:
        n = n_med_for_gate(tg)
        print(f"  N_med to reach {label:34s} = {n:.2f}")
    print(f"  needed for >= 1 MeV (M2)                            = {N_MED_MEV:.2f}")
    print("  READ: re-entry pegged to the electron-family gates gives T_reheat of")
    print("  177-511 keV — a factor 2-6 UNDER the MeV bar in temperature. And no")
    print("  corpus mechanism selects the gate: the metric cannot ride the")
    print("  condensate order parameter (the model's own hot history runs a metric")
    print("  at T >> T_c), so the gate is a candidate clock, not a legalized knob.")
    print()
    print("VERDICT")
    print("  contact  : PASS (recorded; Gamma/H ~ 1e16-1e17 through the melt scale)")
    print("  presence : PASS (thinned to ~6% at T_c; contact survives easily)")
    print("  turn     : FAIL by class (NEC-nonnegative lane; needs rho_X + p_X < 0)")
    print("  clock    : candidate only (under the MeV bar x2-6; gate unselected)")
    print("  ROLE: the electron sector is the computed thermal-contact channel and")
    print("  a candidate timing threshold for the transition. It is not, and cannot")
    print("  be, the NEC-violating component a bounce requires. Still open.")
    print("=" * 78)

    assert abs(tau - 0.5 * math.log(2.0)) < 2e-5
    assert 0.05 < supp < 0.06
    assert gh_tc > 1e15
    assert need < 0.0
    assert n_med_for_gate(M_E_KEV) < N_MED_MEV


if __name__ == "__main__":
    main()
