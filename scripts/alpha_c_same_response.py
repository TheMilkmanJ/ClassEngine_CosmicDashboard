#!/usr/bin/env python3
"""
A4 — α_c same-response identity: permanent-bet grade (not a derivation).

Corpus anchors:
  - PRTOE_DERIVATION_HUNT.md §1 (piece 1 + doped-pair table)
  - scripts/two_channel_polarization_obstruction.py (symmetry obstruction)
  - P-2026-040 (PRTOE_PREREGISTERED_PREDICTIONS.md)
  - A_s closed form as IR scale referee (hierarchy / amplitude stack)

What is FORCED
  α_c = d · α_base with d = 3 the spatial dimension
  (Landau second sound c₂ = c₁/√d; transverse loop trace).

What is NOT derived
  The same-response identification: that α_base is α_EM because one medium
  response sets both the photon's coupling and the condensate compressibility
  with unit coefficient.  DERIVATION_HUNT §1 grades this as empty (μ=0 IR /
  single form factor) or a doped-pair O(1–12.5%) correction, not a free O(1)
  to compute from unbuilt constituents.  Either way there is no two-channel
  identity left to "close" as a derivation of α_c = 3α.

Permanent grade
  PERMANENT BET P-2026-040.  Primary referee: A_s (and any future converged
  α_c chain).  Do not reopen as "open derivation debt" — reopen only if a
  new microphysical polarization computation appears that is *not* already
  covered by the symmetry table below.
"""
from __future__ import annotations

import math
import sys

ALPHA = 1.0 / 137.036
D = 3
ALPHA_C = D * ALPHA

# A_s closed form used as IR scale referee (same stack as hierarchy notes)
K = math.log(1.0 + math.pi / (2.0 * ALPHA_C)) / math.pi
AS_CLOSED = (ALPHA_C / (4.0 * math.pi * K)) ** 3
AS_MEAS = 2.100e-9

# SM-like roster charge² weights (DERIVATION_HUNT §1 doped-pair table)
# Σ Q² over 48 Weyl ≈ 16 (3 gen × 16/3); pair fractions of total Π weight
DOPED_PAIRS = [
    ("ν_L or ν_R", 0.0, 0.0),
    ("d_L or d_R", 2.0 / 9.0, (2.0 / 9.0) / 16.0),
    ("u_L or u_R", 8.0 / 9.0, (8.0 / 9.0) / 16.0),
    ("e_L or e_R", 2.0, 2.0 / 16.0),
]


def main() -> int:
    print("=" * 72)
    print("A4 — α_c same-response identity")
    print("=" * 72)

    print("\n(1) GEOMETRIC FACTOR — DERIVED")
    print(f"  d = {D} (spatial dimension)")
    print(f"  α_c = d · α = {ALPHA_C:.6e}  (= 3α)")
    print("  Sources: Landau c₂ = c₁/√d with c₁ = √α_c · c ⇒ α_c = d·α")
    print("           when the middle rung is identified with √α·c.")
    print("  The 3 is geometry.  It is not a free integer or flavour count.")

    print("\n(2) TWO-CHANNEL POLARIZATION — SYMMETRY TABLE (no constituents needed)")
    print("  Gauge invariance + Lorentz vacuum  →  one form factor: Π_T ≡ Π_L")
    print("    ⇒ unit-coefficient identity is AUTOMATIC and EMPTY (tautology).")
    print("  Medium rest frame u^μ              →  two form factors Π_T, Π_L")
    print("    Normal Fermi surface: Π_L finite (Debye), Π_T(0)→0 — not related by O(1).")
    print("    Condensate: both finite; unit coeff ⇔ n_s/m = ∂n/∂μ (Galilean/rel. tie).")
    print("  Standing basement (Volovik μ=0 at IR where α_EM is read): single form")
    print("    factor → identity empty.  Doped-pair configuration (hierarchy §6c):")
    print("    Π_T − Π_L sourced by ONE pair's share of ΣQ² over the roster.")
    print()
    print(f"  {'doped pair':<14}  {'Q²(pair)':>8}  {'|ΔΠ|/Π (share)':>16}")
    for name, q2, frac in DOPED_PAIRS:
        print(f"  {name:<14}  {q2:8.4f}  {100*frac:15.2f}%")
    print("  Bound: unit-coefficient identification holds up to [0, 12.5%], exact")
    print("  if the doped pair is electromagnetically neutral.  Owed object is")
    print("  *which* pair is doped — a constituent choice, not a free O(1) fit.")

    print("\n(3) A_s REFEREE (consistency on the IR value, not a derivation)")
    print(f"  A_s closed (α_c / 4πK)³ = {AS_CLOSED:.6e}")
    print(f"  A_s measured            = {AS_MEAS:.6e}")
    print(f"  fractional offset       = {(AS_CLOSED/AS_MEAS - 1)*100:+.2f}%")
    print("  A_s selects the IR reading of α_c = 3α(0) over UV/running alternatives;")
    print("  it does not prove same-response.  Posterior scalar ≠ identity of two Π's.")

    print("\n(4) ROSTER / BASE-α CONDITION (piece 2 — still open, not this identity)")
    print("  'Base = α_EM' was conditioned on a ~44% induced fraction that belongs to")
    print("  hypercharge@M_Z.  Electromagnetic q→0 induced share is ~23.5%.  That is")
    print("  a separate debt from piece 1; it does not reopen the geometric 3.")

    print("\n" + "=" * 72)
    print("VERDICT — PERMANENT BET P-2026-040 (A_s referee only for the value)")
    print("=" * 72)
    print("""
  Factor 3 = d:          DERIVED (geometry / second sound).
  Same-response base α:  NOT DERIVED.  Either tautology (μ=0 IR) or doped-pair
                         O(≤12.5%) correction — not a missing polarization calc
                         that upgrades α_c = 3α to a theorem.
  Standing grade:        PERMANENT BET  P-2026-040
  Primary referee:       A_s (IR); secondary: any future *converged* α_c chain
  Do not:                claim 'same-response derived' in audience text
  Do not:                reopen as open derivation without new microphysics
                         outside the symmetry table above
""")
    print("SUMMARY")
    print("  grade=PERMANENT_BET_P-2026-040")
    print("  d_factor=DERIVED")
    print("  same_response_identity=NOT_DERIVED")
    print("  base_alpha=BET")
    print(f"  As_frac_err={(AS_CLOSED/AS_MEAS - 1):+.6f}")
    print("  doped_pair_bound_pct=[0, 12.5]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
