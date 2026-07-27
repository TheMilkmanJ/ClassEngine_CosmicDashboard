"""as_normalization_triangle — task #15: the normalization becomes a two-parameter triangle (2026-07-27).

WHAT THE ENVELOPE MECHANISM DID TO THIS TASK
  The old bookkeeping (one-shot transfer) carried C = R²(k_*ℓ_p)³/2π² with a
  factor-250 convention spread — an identification, not a result.  The
  derived mechanism replaces it: ζ_k = r·L·S_k with L = ln(k_UV/k) computed,
  so  A_s = r²·L*²·f³/2π²  with exactly two physical parameters:
    r — the conversion rate per e-fold;
    f — the cell fraction at imprint (k·ξ_imprint).
  The convention ambiguity is GONE: L* is computed, 2π² is standard, and the
  pivot-volume convention was an artifact of the one-shot reading.

THE COMPONENT-IDENTITY RULING (forced, with a four-order kill)
  The rate normalizes as r = c·f_E, with f_E the energy fraction of the
  component carrying the conserved census.  Two readings existed:
    * DARK-SUBCOMPONENT census: the dark fluid's radiation-like fraction
      before its transition is (Ω_dm/Ω_r)/(1+z_on) ≈ 7.2×10⁻⁵ — computed
      below.  Meeting the registered isocurvature band would then need the
      order-one coefficient c ≳ 10⁴.  DEAD by four orders on recorded
      numbers.
    * SUBSTRATE census: the corpus's census is the substrate's own occupancy
      (the same counting that prices the vacuum energy), and the substrate
      underlies the whole bath — its "fraction" is identically 1, at every
      epoch.  The constant-fraction premise of the envelope derivation
      becomes EXACT rather than approximate, and r = c ~ O(1).
  The ruling retroactively strengthens the envelope derivation (its premise
  is now exact) and kills its only soft reading.

THE TRIANGLE (computed below)
  * the registered isocurvature band (sub-% to %) bounds r two-sided;
  * A_s then pins f = (2π²A_s)^{1/3}/(r·L*)^{2/3} — the basement's forward
    target, REVISED from the one-shot 3.45×10⁻³ to ~2×10⁻⁴;
  * the closed form (α_c/4πk)³ becomes a testable point on the (r, f) curve.

GRADE RULE
  C = 1 is not derived tonight; it is TRANSFORMED — from one opaque
  identification into two physical parameters, one bounded two-sided by
  observables and the other pinned given the first.  Task stays open with
  sharper gates.  The sub-kill is real and carries its number.
"""
from __future__ import annotations

import math

AS_MEAS = 2.100e-9
L_STAR = 61.86
OM_DM_H2 = 0.120
OM_R_H2 = 4.15e-5
Z_ON = 4.03e7
ISO_MIN, ISO_MAX = 0.005, 0.02      # registered band class, sub-% to %
ALPHA_C = 3.0 / 137.036
K_SCREEN = 1.36461


def f_of_r(r: float) -> float:
    return (2.0 * math.pi**2 * AS_MEAS) ** (1.0 / 3.0) / (r * L_STAR) ** (2.0 / 3.0)


def main() -> None:
    print("=" * 78)
    print("The normalization triangle: two parameters, three observables")
    print("=" * 78)

    print("\n1. The component-identity ruling (the four-order kill):")
    fE_dark = (OM_DM_H2 / OM_R_H2) / Z_ON
    c_needed = (1.0 / ISO_MAX) / (fE_dark * L_STAR)
    print(f"   dark-subcomponent fraction pre-transition: "
          f"(Ω_dm/Ω_r)/(1+z_on) = {fE_dark:.2e}")
    print(f"   coefficient needed to meet the registered residual band: "
          f"c ≥ {c_needed:.1e}")
    print(f"   DEAD by ~4 orders — the census is the SUBSTRATE's (fraction ≡ 1,")
    print(f"   the same counting that prices the vacuum energy); the envelope")
    print(f"   derivation's constant-fraction premise becomes EXACT.")

    print("\n2. The residual band bounds the rate two-sided:")
    r_lo = 1.0 / (ISO_MAX * L_STAR)
    r_hi = 1.0 / (ISO_MIN * L_STAR)
    print(f"   S/ζ = 1/(r·L*) ∈ [{ISO_MIN}, {ISO_MAX}]  ⟹  r ∈ "
          f"[{r_lo:.2f}, {r_hi:.2f}]  — order one, as a conversion rate should be")

    print("\n3. A_s pins the cell fraction given the rate:")
    print("   r        f = k·ξ_imprint      S/ζ residual")
    for r in (r_lo, 1.0, 2.0, r_hi):
        print(f"   {r:5.2f}    {f_of_r(r):.3e}          {1/(r*L_STAR):.4f}")
    print(f"   the basement's forward target REVISED: f ~ 2×10⁻⁴ "
          f"(was 3.45×10⁻³ in the one-shot bookkeeping — the L*² factor is the")
    print("   difference, and it is computed, not chosen).")

    print("\n4. The closed form as a testable point:")
    lhs_cube = (ALPHA_C / (4.0 * math.pi * K_SCREEN)) ** 3
    print(f"   (α_c/4πk)³ = {lhs_cube:.4e} = r²L*²f³/2π² demands, at r = 1:")
    f_closed = (2.0 * math.pi**2 * lhs_cube) ** (1.0 / 3.0) / (L_STAR) ** (2.0 / 3.0)
    print(f"   f = {f_closed:.3e} — within the triangle's window: the closed")
    print("   form is CONSISTENT with the mechanism at order-one rate, and")
    print("   deriving f from the basement now decides both at once.")

    print("\nVERDICT: C = 1 transformed, not derived. The opaque identification")
    print("   became (r, f): r bounded two-sided by the registered residual band")
    print("   [0.8, 3.2], f pinned to ~2×10⁻⁴ given r, the closed form a")
    print("   consistent point, and the dark-subcomponent reading killed by four")
    print("   orders. FINISH: derive f (the imprint cell fraction) from the")
    print("   medium — one number closes #15, gates #8, and referees #9.")
    print("=" * 78)

    assert fE_dark < 1e-4
    assert c_needed > 5e3
    assert 0.5 < r_lo < 1.0 and 3.0 < r_hi < 3.5
    assert 1.5e-4 < f_of_r(1.0) < 2.5e-4
    assert abs(f_closed / f_of_r(1.0) - 1.0) < 0.05


if __name__ == "__main__":
    main()
