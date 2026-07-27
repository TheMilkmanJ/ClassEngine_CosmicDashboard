"""cell_fraction_reduction — task #15's keystone: f reduced to the held fraction β (2026-07-27).

WHAT A DERIVATION OF f MUST SUPPLY
  Two things: the imprint CLOCK (when each mode's census locks) and the
  coherence SCALE at that moment.  Self-similarity — required by the recorded
  scaling ruling and by the data through the tilt — constrains both jointly.

THE CLOCK ELIMINATION (computed)
  * single-epoch census (all modes locked at one time, constant physical ξ):
    f(k) ∝ k ⟹ shot power ∝ k³ ⟹ n_s = 4.  The recorded excluded branch.
  * mode-scaled clock with CONSTANT physical coherence (lock at horizon or
    sound-horizon crossing, ξ = ħ/mc_s): at crossing, f = H·ξ(/c_s), and in
    the radiation era H ∝ k² along the crossing curve ⟹ f ∝ k² ⟹ shot power
    ∝ k⁶ ⟹ n_s ≈ 7.  Killed — by six units of tilt.  (Numerical check below;
    also lands f ~ 10⁻⁶ at the pivot, 150× under the triangle window — wrong
    value AND wrong scaling.)
  * mode-scaled clock with HORIZON-TRACKING coherence (ξ_eff = β·c_s/H, the
    coherence held at a fixed fraction of the causal range): at crossing,
    f = β for every mode — constant, self-similar, scale-invariant shot.
    THE SOLE SURVIVOR, and verbatim the class the hunt's scaling ruling
    already recorded ("a length held at a constant fraction of the horizon
    while both grow").

THE REDUCTION
  f = β — the medium's early-era coherence-to-causal-range fraction — with
  the triangle demanding β ∈ [1.0, 2.6]×10⁻⁴ and the closed form's point at
  β = 2.21×10⁻⁴ (unit conversion rate).

WHAT REMAINS (the basement number, honestly fenced)
  β's dynamical origin.  Standard phase-ordering laws FAIL to hold it:
  nonconserved coarsening gives coherence ∝ t^(1/2) against horizon ∝ t, a
  falling ratio — so the medium's radiation-like era must be scale-free
  (critical) with a fixed small ordering fraction.  Deriving β is deriving
  that critical fraction.  No candidate value is named here; the two
  numerological temptations in range are recorded ONLY as temptations to be
  tested against a derivation, never as answers.

GRADE RULE
  A reduction: clock derived by elimination (two computed kills), scale
  requirement identified with the recorded ruling, target window restated.
  f is NOT derived; β is now the program's single sharpest open number.
"""
from __future__ import annotations

import math

M_EV = 2.24e-20
C_S = math.sqrt(3.0 / 137.036)
H0_EV = 1.44e-33
OM_R, OM_M = 9.0e-5, 0.31
K_EQ = 0.010          # /Mpc
Z_EQ = 3400.0
K_PIVOT = 0.05        # /Mpc
BETA_LO, BETA_HI = 1.0e-4, 2.6e-4
BETA_CLOSED = 2.21e-4


def hubble(z: float) -> float:
    return H0_EV * math.sqrt(OM_R * (1 + z) ** 4 + OM_M * (1 + z) ** 3)


def main() -> None:
    xi = 1.0 / (M_EV * C_S)          # constant physical coherence length, eV^-1
    print("=" * 78)
    print("The cell fraction reduced: the clock elimination and the held fraction")
    print("=" * 78)

    print("\n1. Constant-ξ clocks, killed by scaling (computed):")
    print("   k/k_eq    z_entry (RD)      f = H·ξ         d ln f/d ln k")
    prev = None
    for ratio in (2.0, 5.0, 10.0, 20.0):
        z = Z_EQ * ratio
        f = hubble(z) * xi
        slope = (math.log(f) - math.log(prev)) / math.log(2.0) if prev else float("nan")
        pr = f"{slope:+.2f}" if prev else "  — "
        print(f"   {ratio:5.1f}    {z:9.0f}      {f:.3e}      {pr}")
        prev = f
    f_piv = hubble(Z_EQ * K_PIVOT / K_EQ) * xi
    print(f"   at the pivot: f = {f_piv:.2e} — {BETA_CLOSED/f_piv:.0f}× under the")
    print("   triangle window, AND f ∝ k² ⟹ shot power ∝ k⁶ ⟹ n_s ≈ 7:")
    print("   wrong value and wrong scaling — dead twice over. The single-epoch")
    print("   clock is the recorded n_s = 4 exclusion. Both constant-ξ clocks die.")

    print("\n2. The sole survivor: horizon-tracking coherence")
    print("   ξ_eff = β·(c_s/H) ⟹ at every mode's crossing, f = β — constant,")
    print("   self-similar, scale-invariant: exactly the recorded scaling ruling")
    print("   ('a length held at a constant fraction of the horizon while both")
    print("   grow'). The clock is derived by elimination; the scale requirement")
    print("   is the corpus's own recorded class.")

    print("\n3. The target the basement owes:")
    print(f"   β ∈ [{BETA_LO:.1e}, {BETA_HI:.1e}]  (the triangle's window)")
    print(f"   β = {BETA_CLOSED:.2e}  (the closed form's point at unit rate)")
    print("   In causal language: the medium's early coherence saturates at")
    print("   ~1/5000 of its own causal range — a small, scale-free ordering")
    print("   fraction that standard coarsening laws cannot hold (they give a")
    print("   falling ratio ∝ t^(−1/2)); the radiation-like era must be critical.")

    print("\n4. Temptations recorded as temptations (weight zero, tested later):")
    print(f"   α_c²/2 = {(3/137.036)**2/2:.2e} (8% from the closed point);")
    print(f"   α_c²   = {(3/137.036)**2:.2e} (2.2× off). Neither is an answer;")
    print("   either would need the derivation to produce it, not the reverse.")

    print("\nVERDICT: f is REDUCED, not derived — to one number β with a derived")
    print("   clock, a recorded scale class, a two-sided target window, and the")
    print("   critical-era requirement named. β is now the program's sharpest")
    print("   open number: it closes #15, gates #8, and referees #9 at once.")
    print("=" * 78)

    assert f_piv < 3e-6
    assert BETA_CLOSED / f_piv > 100
    assert BETA_LO < BETA_CLOSED < BETA_HI


if __name__ == "__main__":
    main()
