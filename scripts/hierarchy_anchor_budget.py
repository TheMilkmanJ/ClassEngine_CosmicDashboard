"""hierarchy_anchor_budget — the anchor band's explicit error budget (2026-07-27).

STATE COMING IN (the file is ahead of the task list)
  PRTOE_hierarchy_problem.md already carries: the −3/2 derived (equipartition,
  additivity grade); the shared k triple-determined (gap equation 1.360, closed
  form 1.36461, A_s-measured 1.3602 ± 0.0064); the complete O(λ) correction
  evaluated (crossed box c = 0.789, Fock a = 0.281, factor e^{−(c+a)} = 0.343);
  the band 0.55–1.78 TeV; the strain vs the 13–20 TeV shooter sized (7.3–24×).

WHAT THIS ADDS
  The one missing piece: the budget DECOMPOSITION — which input drives the
  band.  Sensitivities are exact from lnM = lnM_red − 1/(kα_c) − 3/2 + lnC:
  ∂lnM/∂lnk = ∂lnM/∂lnα_c = 1/(kα_c) = 33.5.

GRADE RULE
  Propagation arithmetic on recorded numbers.  The verdict names what would
  actually tighten the band.  Nothing promoted.
"""
from __future__ import annotations

import math

M_RED = 2.435e18            # GeV
ALPHA_C = 3.0 / 137.036
K_CLOSED = 1.36461            # the closed form — the file's central convention
K_MEAS, K_SIGMA = 1.3602, 0.0064  # the A_s determination — supplies the spread
C_BOX, A_FOCK = 0.789, 0.281
BAND_LO, BAND_HI = 0.55, 1.78     # TeV, recorded


def anchor(k: float, corr: float = 0.0) -> float:
    """TeV; corr = summed O(λ) exponent actually applied."""
    return M_RED * math.exp(-1.0 / (k * ALPHA_C) - 1.5 - corr) / 1e3


def main() -> None:
    amp = 1.0 / (K_CLOSED * ALPHA_C)
    print("=" * 78)
    print("The anchor band's error budget — who actually drives it")
    print("=" * 78)
    print(f"\n   amplification: ∂lnM/∂lnk = ∂lnM/∂lnα_c = 1/(kα_c) = {amp:.2f}")
    print(f"   bare anchor (no O(λ)): {anchor(K_CLOSED):.3f} TeV;  "
          f"fully corrected: {anchor(K_CLOSED, C_BOX + A_FOCK):.3f} TeV")
    print("\n   input                    spread in          effect on M        share")
    dk = amp * (K_SIGMA / K_MEAS)
    print(f"   shared k (measured)      ±{100*K_SIGMA/K_MEAS:.2f}%             "
          f"±{100*dk:.0f}%              minor")
    print(f"   α_c = 3α (under test)    exact if identity   ±{amp:.0f}·δlnα_c        "
          f"zero if exact")
    print(f"   the −3/2 (derived)       exact               none               zero")
    print(f"   m_H (measured, via 4π)   ±0.1%              ±0.1%              negligible")
    ratio = BAND_HI / BAND_LO
    print(f"   O(λ) correction scheme   e^0 … e^−(c+a)      ×{ratio:.1f} full band     DOMINANT")
    print("\nREAD")
    print(f"  1. The band (0.55–1.78 TeV, ×{ratio:.1f}) is NOT an unpinned-O(1) vibe —")
    print("     the O(1)s are evaluated. The band is the honest spread between the")
    print("     uncorrected and fully-corrected first-order treatments: a")
    print("     perturbative-control statement, the same class as the dark-energy")
    print("     quartic's control edge.")
    print(f"  2. The measured k contributes only ±{100*dk:.0f}% — the triple determination")
    print("     already did its job. Nothing on the desk tightens the band further:")
    print("     what would is the next perturbative order or a nonperturbative")
    print("     treatment of the pairing (named, not owed to any current thread).")
    print("  3. α_c = 3α is the live-bet input: the running chains test it, and a")
    print(f"     confirmed shift δ would move the anchor by {amp:.0f}·δ — the anchor is")
    print("     downstream of the chains, another reason they matter.")
    print("=" * 78)

    assert 33.0 < amp < 34.0
    assert abs(anchor(K_CLOSED) - 1.57) < 0.05
    assert dk < 0.20
    assert ratio > 3.0


if __name__ == "__main__":
    main()
