"""bounce_floor_frw_nogo — can the CSW / dCDF floor produce a homogeneous FRW bounce?

WHAT THIS CHECKS
    Three related promotions that must not be smuggled past the equations:

    (A) CSW ceiling as cosmological bounce
        rho_bounce = m^4 / lambda  is a real finite density (scripts/rho_bounce.py).
        Does it make H=0 with Ḣ>0 in homogeneous FRW?

    (B) Live barotropic dCDF as bounce engine
        The production fluid has w = -exp(-s) with s = ln(max(rho/rho_inf, 1)),
        i.e. p = -rho_inf exactly (include/background.h). Can rho+p go negative?

    (C) Metric-exit-at-xi vs the recorded floor
        The no-singularity synthesis says the crunch exits the metric at xi.
        At rho_bounce, is the Hubble radius already below xi?

INPUTS (recorded)
    m       = 2.24e-20 eV
    lambda  = 2e-91
    xi      = 402 AU   (coherence / healing length, corpus value)
    M_Pl    = 1.22089e19 GeV

VERDICT (computed)
    (A) NO. CSW polytrope p = K rho^2 has rho+p > 0 for all rho>0.
        Relativistic p~rho ceiling still has rho+p = 2 rho > 0.
        Bare vacuum is ~10^23 too small to cancel rho_bounce.
        Homogeneous quantum pressure vanishes (no spatial gradients).
        The CSW ceiling is a BH/core hydrostatic result, not an FRW bounce.

    (B) NO. Live w in [-1, 0) gives rho+p = rho - rho_inf >= 0 always.
        At the floor, rho+p = 0 => Ḣ = 0 (de Sitter coast), not Ḣ > 0.

    (C) NOT YET. At rho_bounce, H^{-1}/xi ~ 12: the homogeneous metric is
        still classically OK. Metric exit on the Hubble scale needs
        ~150x higher density than the recorded floor allows.

    None of this invents a bounce source. It only blocks three false bridges.
"""
from __future__ import annotations

import math

m_eV = 2.24e-20
lam = 2e-91
M_Pl_eV = 1.22089e19 * 1e9
AU_m = 1.496e11
eVinv_to_m = 1.973269804e-7
xi_AU = 402.0
rho_Lambda = (2.25e-3) ** 4


def main() -> None:
    rho_b = m_eV**4 / lam
    rho_b_q = rho_b**0.25
    K = lam / (8.0 * m_eV**4)
    p_poly = K * rho_b**2

    xi_m = xi_AU * AU_m
    xi_eVinv = xi_m / eVinv_to_m
    H_b = math.sqrt(8.0 * math.pi / 3.0) * math.sqrt(rho_b) / M_Pl_eV
    R_H = 1.0 / H_b
    rho_exit = (M_Pl_eV / xi_eVinv) ** 2 * 3.0 / (8.0 * math.pi)

    print("=" * 78)
    print("bounce floor / live-dCDF / metric-exit  no-go checks")
    print("=" * 78)

    print("\n(A) CSW ceiling in homogeneous FRW")
    print(f"  rho_bounce^(1/4)     = {rho_b_q:.3e} eV")
    print(f"  polytrope p/rho      = {p_poly/rho_b:.3e}  (p=K rho^2)")
    print(f"  rho+p (polytrope)    > 0  for all rho>0")
    print(f"  rho+p (p~rho ceil.)  = 2 rho > 0")
    print(f"  rho_bounce/|rho_L|   = {rho_b/rho_Lambda:.3e}  (bare cannot cancel)")
    print("  homogeneous QP        = 0  (no gradients)")
    print("  VERDICT A: CSW floor ≠ FRW bounce (core/hydrostatic ≠ homogeneous)")

    print("\n(B) Live barotropic dCDF  w = -rho_inf/rho")
    for ratio in (1.0, 1.01, 10.0, 1e6, 1e12):
        w = -1.0 / ratio
        nec = ratio * (1.0 + w)  # in units of rho_inf
        print(f"  rho/rho_inf={ratio:.3e}  w={w:.6f}  (rho+p)/rho_inf={nec:.6e}")
    print("  VERDICT B: NEC combination never negative; floor gives Ḣ=0 not Ḣ>0")

    print("\n(C) Metric exit at xi vs recorded floor")
    print(f"  xi                   = {xi_AU:.0f} AU")
    print(f"  H^{'-1'}/xi at floor  = {R_H/xi_eVinv:.2f}")
    print(f"  rho_exit^(1/4)       = {rho_exit**0.25:.3e} eV  (where H^{'-1'}=xi)")
    print(f"  rho_exit/rho_bounce  = {rho_exit/rho_b:.3e}")
    print("  VERDICT C: homogeneous metric still valid at the recorded floor;")
    print("             Hubble-scale metric exit is above the CSW ceiling.")
    print("             Local BKL curvature >> H is uncomputed, not a free pass.")

    print("\nOVERALL:")
    print("  Finite rho_bounce is real and sub-Planckian (no-singularity number).")
    print("  Homogeneous FRW bounce dynamics are still missing.")
    print("  Do not promote the floor, the live dCDF, or Hubble-scale metric exit")
    print("  to a derived bounce.")
    print("=" * 78)

    assert p_poly / rho_b > 0.0
    assert rho_b / rho_Lambda > 1e20
    assert R_H / xi_eVinv > 1.0
    assert rho_exit / rho_b > 10.0


if __name__ == "__main__":
    main()
