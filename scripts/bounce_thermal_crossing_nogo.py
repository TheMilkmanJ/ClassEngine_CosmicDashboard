"""bounce_thermal_crossing_nogo — does T = T_c make a cosmological bounce?

WHAT THIS CHECKS
    The bounce workplan asks whether the contracting-branch thermal crossing
        T(a_b) = T_c
    is only a melt threshold, or whether it can also satisfy the bounce
    conditions in flat FRW:
        H  = 0   ⇒  ρ_tot = 0
        Ḣ  > 0   ⇒  ρ_tot + p_tot < 0

INPUTS (recorded; none invented here)
    T_c        = 177.10 keV     lepton-mass relation τ = ½ ln 2
    m          = 2.24e-20 eV    ultralight medium mass
    lambda     = 2e-91          repulsive amplitude quartic
    rho_bounce = m^4 / lambda   CSW ceiling (scripts/rho_bounce.py)
    g_*        = 10.75          standard MeV-class radiation d.o.f.

WHAT IS NOT CLAIMED
    This script does not invent a noncanonical source term X.
    It only prices the thermal crossing against the FRW bounce conditions
    using the recorded numbers.

VERDICT (computed, not argued)
    At T_c, radiation dominates the condensate floor by ~9 orders in density.
    Canonical FRW then has ρ + p ≈ (4/3) ρ_rad > 0, so Ḣ < 0.
    The thermal crossing is therefore a melt threshold only — not a bounce.
    Closing the bounce still requires a crunch-sector X (or a modified
    Friedmann branch that changes the H = 0 bookkeeping), which is not
    written in the corpus.
"""
from __future__ import annotations

import math

# ---- recorded inputs ---------------------------------------------------------
T_c_eV = 177.10e3          # eV
m_eV = 2.24e-20            # eV
lam = 2e-91
gstar = 10.75
rho_Lambda_eV4 = (2.25e-3) ** 4  # eV^4 ; observed DE scale

# ---- derived -----------------------------------------------------------------
rho_bounce = m_eV**4 / lam
rho_bounce_q = rho_bounce**0.25


def rho_rad(T_eV: float, g: float = gstar) -> float:
    return (math.pi**2 / 30.0) * g * T_eV**4


def main() -> None:
    rr = rho_rad(T_c_eV)
    rr_q = rr**0.25
    nec_can = (4.0 / 3.0) * rr  # canonical ρ + p if radiation dominates

    print("=" * 78)
    print("bounce thermal-crossing no-go  (T = T_c vs H=0, Ḣ>0)")
    print("=" * 78)
    print(f"  T_c            = {T_c_eV:.3e} eV = {T_c_eV/1e3:.2f} keV")
    print(f"  rho_bounce     = {rho_bounce:.3e} eV^4   (^(1/4) = {rho_bounce_q:.3e} eV)")
    print(f"  rho_rad(T_c)   = {rr:.3e} eV^4   (^(1/4) = {rr_q:.3e} eV, g*={gstar})")
    print(f"  rho_rad/rho_bounce = {rr/rho_bounce:.3e}   ({math.log10(rr/rho_bounce):.2f} dex)")
    print(f"  rho_rad/rho_Lambda = {rr/rho_Lambda_eV4:.3e}")
    print(f"  |rho_bare|~rho_L / rho_rad(T_c) = {rho_Lambda_eV4/rr:.3e}  (bare is invisible at T_c)")
    print()
    print("  Canonical FRW at radiation-dominated T_c:")
    print(f"    rho + p  ≈ (4/3) rho_rad = {nec_can:.3e} eV^4  > 0")
    print("    => Ḣ = −4πG(ρ+p) < 0")
    print("    => bounce condition Ḣ > 0 FAILS")
    print()
    print("  Required noncanonical budget to flip the sign at T_c:")
    print(f"    need  rho_X + p_X  <  −{nec_can:.3e} eV^4")
    print(f"    i.e. |rho_X + p_X| scale ≳ {nec_can**0.25:.3e} eV")
    print(f"    vs rho_bounce scale          {rho_bounce_q:.3e} eV")
    print(f"    ratio need/rho_bounce      ≈ {nec_can/rho_bounce:.3e}")
    print()
    print("  Flat H = 0 still requires rho_tot = 0 even in the historical")
    print("  F-modified Friedmann form 3 F H² + 3 H Ḟ = ρ_tot (K=0):")
    print("    setting H=0 forces ρ_tot = 0; Ḟ selects the branch, not the zero.")
    print()
    print("  Hot-start gap (already in rho_bounce.py), restated:")
    for T_MeV in (1.0, 2.0, 4.0):
        rh = rho_rad(T_MeV * 1e6)
        print(
            f"    T={T_MeV:.0f} MeV: rho_rad/rho_bounce = {rh/rho_bounce:.3e} "
            f"({math.log10(rh/rho_bounce):.1f} dex)"
        )
    print()
    print("VERDICT:")
    print("  Thermal crossing at T_c is a MELT THRESHOLD only.")
    print("  It does not produce H=0 with Ḣ>0 in canonical FRW.")
    print("  The missing crunch-sector X (or live modified branch) is still open.")
    print("  Do not promote the thermal picture to a derived bounce.")
    print("=" * 78)

    # hard asserts — these are the no-go, not soft commentary
    assert rr > rho_bounce * 1e6, "radiation must dominate the floor at T_c"
    assert nec_can > 0.0, "canonical NEC combination must be positive"
    assert rho_Lambda_eV4 / rr < 1e-20, "bare vacuum must be negligible at T_c"


if __name__ == "__main__":
    main()
