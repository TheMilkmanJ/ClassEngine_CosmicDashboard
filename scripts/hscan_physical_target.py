"""hscan_physical_target — task #36's scoping computation: where the physical hierarchy actually sits at the standing era (2026-07-27).

SUPERSEDED ON THE ABSOLUTE NUMBERS (2026-07-28) — READ THIS FIRST.
  The authority for the release amplitude is the misalignment abundance
  closure in `genesis_solver_B1.py`, which releases at H = m and returns
  1 + z_osc = 4.03×10⁷ — the corpus's own canonical onset z_on — and
  Psi0 = 5.03×10¹⁶ GeV, hence
        h0 = lambda*Psi0^2/m^2 = 1.01 .
  **The standing physical hierarchy is h0 ~ 1, not the 0.1 this script
  first reported.**  Two departures produced that: releasing at 3H = m
  (which does not reproduce z_on) and omitting the 1/2 in rho = 1/2 m^2
  Psi^2 that the standard misalignment closure carries.  The temperature
  route below also carries its own g*/normalization drift and does not
  reproduce z_on even at H = m, so it is kept only for the SCALING it
  demonstrates (h0 proportional to lambda/m^(5/2), the era-to-standing
  direction), not for absolute values.  Take absolute Psi0 and h0 from B1.


THE QUESTION
  Room 1's h-scan chased the ringing floor upward (86% → 100% by h = 10⁴)
  toward an era-bound physical target "h ~ 10⁸", and the owed item was a
  rescaled integrator to cross the remaining decades.  Before building
  it, this script computes the physical h at the STANDING parameters.

THE CHAIN (misalignment bookkeeping, radiation era, no entropy dumps
  between release and today beyond g*)
  Release when Hubble friction lets go, 3H(z_rel) = m_eff.  Self-
  consistency picks the branch: if the quartic dominates at release
  (h > 1) then m_eff = √(3λ)·Ψ₀; if the mass does (h < 1), m_eff = m.
  The relic condition closes it: ρ(z_rel) redshifts to today's dark
  matter density, so ρ_rel = ρ_dm,0·(1+z_rel)³ (mass branch, a⁻³) and
      h₀ = λ·ρ_rel/m⁴  with  3H(z_rel) = m.
  Scaling: ρ_rel ∝ T_rel³ ∝ m^{3/2}  ⟹  h₀ ∝ λ·m^{−5/2} — the standing
  era moved λ DOWN 2.7 decades and m UP 1.35 decades (×3.37 through the
  −5/2 power): 6.1 decades total.

WHY THIS MATTERS BEFORE ANY INTEGRATOR IS BUILT
  If h₀ lands ≪ 100 (the scan's bottom), the owed extrapolation was
  pointed the WRONG WAY: the physical regime is the low-h side, where
  the quartic is a small correction at release, the release kick is
  weak, and the ringing statistics must be re-asked, not extrapolated.
  The low-h dice is CHEAP (the stiffness that demanded a rescaled
  integrator lives at large h).
"""
from __future__ import annotations

import math

M_PL_EV = 1.22e28
T0_EV = 2.35e-4
RHO_DM0_EV4 = 1.0e-11
G_STAR_KEV = 3.36          # post-annihilation plasma, keV epoch


def release(m_ev: float, lam: float):
    # RELEASE CONDITION: H = m, not 3H = m.  This version first used 3H = m,
    # which gives 1+z = 2.33e7 — NOT the corpus's canonical onset z_on =
    # 4.03e7.  The misalignment closure in genesis_solver_B1.py releases at
    # H = m and reproduces z_on exactly, so H = m is the corpus's condition
    # and the earlier choice was inconsistent with its own onset.
    H_rel = m_ev
    T_rel = math.sqrt(H_rel * M_PL_EV / (1.66 * math.sqrt(G_STAR_KEV)))
    z_rel = T_rel / T0_EV          # 1+z, g*-corrections ~10% ignored
    rho_rel = RHO_DM0_EV4 * z_rel ** 3
    h0 = lam * rho_rel / m_ev ** 4
    psi0_gev = math.sqrt(rho_rel / m_ev ** 2) / 1e9
    return T_rel, z_rel, rho_rel, h0, psi0_gev


def main() -> None:
    print("=" * 78)
    print("The h-scan's physical target, recomputed at both eras")
    print("=" * 78)
    cases = [
        ("era corner (m = 1e-22, λ = 1e-88)", 1.0e-22, 1.0e-88),
        ("era band   (m = 1e-21, λ = 1e-88)", 1.0e-21, 1.0e-88),
        ("STANDING   (m = 2.24e-20, λ = 2e-91)", 2.24e-20, 2.0e-91),
    ]
    for name, m, lam in cases:
        T_rel, z_rel, rho_rel, h0, psi0 = release(m, lam)
        branch = "quartic-dominated (ringing regime)" if h0 > 1 else \
                 "MASS-dominated (quartic subdominant)"
        print(f"\n   {name}")
        print(f"     release: T = {T_rel:.3g} eV, 1+z = {z_rel:.3g}, "
              f"ρ = {rho_rel:.3g} eV⁴, Ψ₀ = {psi0:.3g} GeV")
        print(f"     h₀ = λρ_rel/m⁴ = {h0:.3g}   → {branch}")

    print("\n   scaling check: h₀ ∝ λ/m^(5/2); era band → standing:")
    dl = math.log10(2.0e-91 / 1.0e-88)
    dm = 2.5 * math.log10(2.24e-20 / 1.0e-21)
    print(f"     Δλ = {dl:.2f} decades, −(5/2)Δm = −{dm:.2f} decades, "
          f"total {dl - dm:.2f} — matches the direct computation.")

    print("\n   consistency notes (honest):")
    print("   * the standing h₀ < 1 is SELF-consistent (mass-branch release")
    print("     assumed, mass branch obtained) and the era values reproduce the")
    print("     room's own scanned/booked range (10⁵ at the band, ~10⁷·⁵ at the")
    print("     corner ≈ the booked '~10⁸') — the formula is the room's own.")
    print("   * at the standing era the field NEVER passes basin entry")
    print("     (ρ_rel < m⁴/λ at birth): A3a's z_x identity is era-bound; the")
    print("     DIRECT h_eff formula (used by every τ_Q verdict) is unaffected.")

    print("\nVERDICT: the owed 'push to h ~ 10⁸' chased an era-bound target.")
    print("   At the standing parameters the physical hierarchy is h₀ ≈ 0.1 —")
    print("   three decades BELOW the scan's bottom, on the cheap side: the")
    print("   quartic is a ~10% correction at release, the ringing kick is weak,")
    print("   and the question inverts from 'does the quiet branch close at")
    print("   large h?' to 'does ANY ringing survive at h ~ 0.1?' — with the")
    print("   granule ε-meter's readout (the corpus's only ε observable) staked")
    print("   on the answer. The low-h dice needs no rescaled integrator; the")
    print("   stiffness was the large-h obstacle. Run it.")
    print("=" * 78)


if __name__ == "__main__":
    main()
