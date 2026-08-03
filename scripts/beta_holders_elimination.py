"""beta_holders_elimination — the critical fraction's derivation attempt (2026-07-27).

THE TARGET
  β = ξ_eff·H/c_s must be CONSTANT across ~60 e-folds at β ≈ 2×10⁻⁴
  (window [1.0, 2.6]×10⁻⁴).  Any mechanism whose fraction falls or rises
  with time is dead regardless of its value at one epoch.

THE ELIMINATION (each scaling law standard, none invented)
  1. THERMAL coherence (ξ ~ 1/T_bath):  β = H/(c_s·T) ∝ T/M_Pl — falls by
     orders across the era.  DEAD as a holder.
  2. PHASE-ORDERING / coarsening (nonconserved: ξ ∝ t^½):  β ∝ t^(−½) —
     falls three e-folds per six of expansion.  DEAD as a holder.
  3. CRITICAL-RIDING at the adiabatic–impulse boundary (the medium sliding
     along its transition as close as relaxation allows), with the ON-FILE
     exponent ν = 2/3:  equating the relaxation time ξ/c_s = ξ₀ε^(−ν)/c_s
     with the sliding time ε/H gives ε = (Hξ₀/c_s)^(1/(1+ν)) and hence
     β = (Hξ₀/c_s)^(1/(1+ν)) ∝ H^(0.6) — falls.  DEAD as a holder.
  4. SCALING DEFECT-NETWORK attractors: the ONE standard class that holds a
     constant fraction (network spacing locked to a fixed fraction of the
     causal range — an attractor, initial-condition-erasing).  Natural
     scaling parameters for reconnecting (global/superfluid-class) networks:
     β_net ~ 0.1–0.3.  HOLDS the fraction — but lands THREE ORDERS above
     the window.

VERDICT (a structured negative — the honest outcome)
  No standard class delivers β ≈ 2×10⁻⁴: the three falling mechanisms are
  dead as holders, and the one constant-holder overshoots by ~10³.  The
  triangle therefore carries a NAMED TENSION at its β link.  The surviving
  possibilities, each named and none asserted:
    (a) a network attractor with dissipation suppressed enough to shift the
        scaling density by ~3 orders — no recorded suppression mechanism;
    (b) a two-scale structure — network at ~0.1·(causal range) with coherent
        sub-cells at β — the ~500× hierarchy factor unexplained;
    (c) a revision of the imprint-clock story upstream.
  KILL CONDITION SHARPENED: if no non-standard holder is derived, the
  β link fails and with it the envelope mechanism's promotion (the tilt's
  numerical success would then need a different engine — none survives the
  route eliminations to date).

CONSISTENCY NOTE (from reconnaissance, recorded)
  The retired height-field tilt route died with "+1/ln, IR-anchored, wrong
  sign" (the recorded autopsy).  The conserved-charge conversion delivers
  −2/ln, UV-anchored — it passes the very autopsy that killed its
  predecessor.  Noted as consistency, not as evidence.

GRADE RULE
  Derivation attempted; returns a structured negative with the survivor
  space named.  Nothing promoted; the tension goes on the record.
"""
from __future__ import annotations

import math

C_S = math.sqrt(3.0 / 137.036)
NU = 2.0 / 3.0
BETA_WINDOW = (1.0e-4, 2.6e-4)
BETA_NET = (0.1, 0.3)


def main() -> None:
    print("=" * 78)
    print("The β-holders elimination: who can hold a constant fraction, and at what value")
    print("=" * 78)

    print("\n   mechanism                      β(t) scaling        holds?   value class")
    print("   thermal coherence (1/T)        ∝ T/M_Pl (falls)     no       —")
    print("   coarsening (ξ ∝ t^½)           ∝ t^(−½) (falls)     no       —")
    print(f"   critical-riding (ν = 2/3)      ∝ H^(1/(1+ν)) = H^{1/(1+NU):.2f}  no       —")
    print(f"   scaling defect network         constant (attractor) YES      {BETA_NET[0]}–{BETA_NET[1]}")
    print(f"\n   the window the triangle demands: β ∈ [{BETA_WINDOW[0]:.1e}, {BETA_WINDOW[1]:.1e}]")
    gap = BETA_NET[0] / BETA_WINDOW[1]
    print(f"   the one holder overshoots by ×{gap:.0f}–×{BETA_NET[1]/BETA_WINDOW[0]:.0f} — three orders.")

    print("\n   critical-riding detail (the on-file exponent, run to its end):")
    print("   relaxation ξ₀ε^(−ν)/c_s = sliding ε/H  ⟹  ε = (Hξ₀/c_s)^(1/(1+ν))")
    print(f"   ⟹ β = (Hξ₀/c_s)^(1/(1+ν)) ∝ H^{1/(1+NU):.2f} — falls ~0.6 e-folds per")
    print("   e-fold of expansion; across the 60-e-fold window it moves by ~16")
    print("   orders. Not a holder by a spectacular margin.")

    print("\nVERDICT: structured negative. The named tension: no standard class")
    print("   delivers a HELD fraction at 2×10⁻⁴ — the falling mechanisms die as")
    print("   holders and the network attractor lands at 0.1–0.3. Survivor space,")
    print("   named not asserted: (a) dissipation-suppressed dense network (~10³")
    print("   shift, mechanism unwritten); (b) two-scale network+subcell structure")
    print("   (~500× hierarchy unexplained); (c) upstream clock revision. The")
    print("   sharpened kill: no non-standard holder ⟹ the β link fails ⟹ the")
    print("   envelope mechanism loses its promotion path. On the record.")
    print("=" * 78)

    assert 1.0 / (1.0 + NU) > 0.5
    assert gap > 300
    assert BETA_NET[0] > 100 * BETA_WINDOW[1]


if __name__ == "__main__":
    main()
