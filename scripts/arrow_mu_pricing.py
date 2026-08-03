"""arrow_mu_pricing — task #16: the μ-source priced; the condition lands on the standard host (2026-07-28).

WHAT §6n LEFT OPEN
  The screening constant selects a μ-dominated basement (μ/T ≳ 18); the
  candidate source was the arrow sector's ⟨θ̇⟩ (the bibliography's own
  "θ-dot background = the permanent μ").  This script prices that candidate
  against the corpus's recorded structure and reports what survives.

(A) THE SCALING LAW (exact, from the spine's validated tracking result)
  With Q = a³r²θ̇ conserved and the amplitude tracking V ∝ rⁿ
  (r ∝ a^{−6/(n+2)}, the five-decimal-validated relation):
      μ = θ̇ ∝ a^{−3(n−2)/(n+2)},  T ∝ a⁻¹  ⟹  μ/T ∝ a^{(n+2−3(n−2))/(n+2)}...
  computed per regime below.  Harmonic tracking kills the ratio toward the
  floor; quartic tracking freezes it; only n → ∞ grows it as a⁻².

(B) THE CEILING IDENTITY AND THE PRICE (exact algebra, recorded numbers)
  At the ceiling ρ = m⁴/λ with amplitude Ψ₀ = m/√λ, rotation-dominated
  energy θ̇²Ψ₀² = ρ forces θ̇ = m exactly.  So the arrow-sourced chemical
  potential at the floor is μ = m = 2.24×10⁻²⁰ eV — against the door's keV
  bath it misses μ-domination by ~23 orders, against a Planck bath by ~48.
  THE ARROW CANDIDATE IS PRICED OUT at recorded parameters (ledger row).

(C) WHAT SURVIVES — THE DOPING-INDEPENDENCE READING
  b = m_D²/4k_F² = e²/2π² is INDEPENDENT of k_F: the booked constant holds
  at ANY nonzero doping, however small, provided T ≪ μ at the kernel's
  evaluation.  And a T → 0 kernel at the ground state is the STANDARD host
  of every gap equation (BCS/Eliashberg compute the T = 0 kernel; the bath
  only decides when condensation happens).  The mismatch therefore lands:
  the cold Fermi-surface host is not a foreign assumption but the gap
  equation's own standard construction, valid at any doping; the residual
  condition narrows to T ≪ μ AT GAP FORMATION (formation-epoch bath vs the
  band's doping), which is a quantitative question about the formation
  epoch, not a contradiction with the recorded basement.

GRADE RULE
  (A) and (B) exact on recorded structure; the candidate kill goes to the
  ledger.  (C) is the standard-host identification — candidate grade, with
  the formation-epoch condition named.  Nothing promoted.
"""
from __future__ import annotations

import math

M_EV = 2.24e-20
LAMBDA = 2.0e-91
ALPHA_C = 3.0 / 137.036
E2 = 4.0 * math.pi * ALPHA_C
T_DOOR_EV = 1.0e3
T_PLANCK_EV = 1.2209e28


def main() -> None:
    print("=" * 78)
    print("The μ source priced; the host condition lands on standard ground")
    print("=" * 78)

    print("\nA. μ/T scaling under the validated tracking law (exponents of a):")
    print("   n    r-exponent   μ-exponent   (μ/T)-exponent   toward the floor")
    for n in (2, 4, 6, 1000):
        rexp = -6.0 / (n + 2)
        muexp = -3.0 * (n - 2) / (n + 2)
        ratio = muexp + 1.0          # T ∝ a⁻¹ ⟹ μ/T exponent = μexp − (−1)
        tag = ("ratio dies" if ratio > 0 else
               "ratio frozen" if abs(ratio) < 1e-9 else "ratio grows")
        label = "∞" if n == 1000 else str(n)
        print(f"   {label:>4}   {rexp:+8.3f}    {muexp:+8.3f}      {ratio:+8.3f}"
              f"       {tag}")
    print("   the quartic youth (n = 4) FREEZES μ/T on approach; harmonic kills")
    print("   it. No polynomial regime grows it faster than a⁻².")

    psi0 = M_EV / math.sqrt(LAMBDA)
    rho_ceiling = M_EV ** 4 / LAMBDA
    theta_dot = math.sqrt(rho_ceiling) / psi0
    print(f"\nB. the ceiling identity: θ̇ = √(ρ_ceiling)/Ψ₀ = {theta_dot:.3e} eV")
    print(f"   vs m = {M_EV:.3e} eV — identical: the arrow rotates at the mass")
    print(f"   frequency at the floor. Pricing μ = m against the floor baths:")
    print(f"     door bath (keV):    μ/T = {theta_dot/T_DOOR_EV:.1e}  "
          f"(needs ≥ 18: short by {18*T_DOOR_EV/theta_dot:.0e})")
    print(f"     Planck bath:        μ/T = {theta_dot/T_PLANCK_EV:.1e}  "
          f"(short by {18*T_PLANCK_EV/theta_dot:.0e})")
    print("   THE ARROW CANDIDATE IS PRICED OUT at recorded parameters — no")
    print("   charge assignment rescues 23–48 orders. Ledger row filed.")

    b1 = 2.0 * E2 * 1.0 ** 2 / math.pi ** 2 / (4.0 * 1.0 ** 2)
    b2 = 2.0 * E2 * 1.0e-30 ** 2 / math.pi ** 2 / (4.0 * 1.0e-30 ** 2)
    print(f"\nC. doping independence: b at k_F = 1: {b1:.6f}; at k_F = 10⁻³⁰:"
          f" {b2:.6f}")
    print("   — identical: the booked constant holds at ANY nonzero doping with")
    print("   T ≪ μ. A T → 0 kernel at the ground state is the standard host of")
    print("   every gap equation; the bath decides WHEN condensation happens,")
    print("   not the kernel's screening constant. The mismatch lands: the cold")
    print("   host is the gap equation's own construction. RESIDUAL, named: at")
    print("   gap formation the bath must satisfy T ≪ μ for the frozen kernel to")
    print("   apply — a formation-epoch number, owed, not a contradiction.")

    print("\nVERDICT: the dichotomy stays dissolved (§6n's algebra stands); the")
    print("   arrow μ-source dies at recorded parameters (ledger); the surviving")
    print("   reading is standard-host doping-independence with one owed number")
    print("   (T/μ at gap formation). Task #16's gate narrows accordingly.")
    print("=" * 78)

    assert abs(theta_dot - M_EV) / M_EV < 1e-12
    assert abs(b1 - b2) < 1e-15
    assert abs(b1 - 2 * ALPHA_C / math.pi) < 1e-15


if __name__ == "__main__":
    main()
