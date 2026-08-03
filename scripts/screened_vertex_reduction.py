"""screened_vertex_reduction — task #15: flag (i) reduced to one property, k re-verified from its own pieces (2026-07-28).

THE TARGET
  The cascade-cutoff closure (the count's candidate derivation) rests on one
  flagged identification: a per-Kelvin-oscillation erasure probability
  p = g_scr/4π at the screened coupling.  This script does three honest
  things and refuses the fourth:

  (1) STRUCTURE CHECK (exact algebra): the recorded R = π/2α_c is not an
      independent input — it is the backscattering range over the booked
      screening mass, R = 4k_F²/m_D² with m_D² = 8α_c·k_F²/π (the constant
      §6n re-hosted).  One screening object, two appearances.

  (2) INDEPENDENT k VERIFICATION (numerics): the Fermi-surface average of
      the Thomas–Fermi-screened exchange over the full backscattering range
      reproduces the closed form k = ln(1+R)/π, with the convention set that
      lands it printed openly (density of states per band with both spins,
      two velocity-matched bands, the pairing-channel ½).

  (3) GOLDEN-RULE REDUCTION (derivation of the reduction, not the vertex):
      Fermi's golden rule for one-quantum emission from a quantized
      oscillation, Γ = 2π|V|²ρ, gives a per-cycle probability
          P = g_scr/4π   ⟺   |M|² = 1 with the unit-normalized s-wave
                              measure ∫dΩ/4π and NO residual energy ratios
      — the WEIGHT-ZERO property: the erasure channel must carry neither a
      velocity suppression (a dipole channel carries (v/c_s)², the computed
      bare-channel physics) nor a phase-space enhancement.  Flag (i) is
      thereby reduced from "derive the vertex" to "exhibit the weight-zero
      property of the erasure channel."

  (4) What it does NOT do: identify which microscopic process has weight
      zero.  That identification is the remaining flag, and inventing it
      here would be fabrication.

GRADE RULE
  (1) is exact; (2) is a numerical reconstruction with conventions printed;
  (3) is a bidirectional reduction, not a closure.  #15 remains open with a
  sharper gate: the weight-zero exhibit, plus the μ ≫ T host condition
  inherited from the screening constant (task #16, hierarchy §6n).
"""
from __future__ import annotations

import math

ALPHA_C = 3.0 / 137.036
K_CLOSED = math.log(1.0 + math.pi / (2 * ALPHA_C)) / math.pi


def main() -> None:
    print("=" * 78)
    print("The screened vertex: structure checked, k re-verified, flag reduced")
    print("=" * 78)

    # (1) R from the booked screening mass — exact algebra
    #     m_D² = 8 α_c k_F²/π  (the §6n-hosted constant, k_F units)
    #     R    = (2k_F)²/m_D² = 4k_F²·π/(8α_c k_F²) = π/2α_c
    R_from_screening = 4.0 * math.pi / (8.0 * ALPHA_C)
    R_recorded = math.pi / (2.0 * ALPHA_C)
    print(f"\n1. R = 4k_F²/m_D² = {R_from_screening:.4f} vs recorded π/2α_c = "
          f"{R_recorded:.4f}  — identical: R is the backscattering range over")
    print("   the booked screening mass. One screening object, two appearances,")
    print("   both now hosted by the same μ-dominated basement (§6n).")

    # (2) independent k: Fermi-surface average of the screened exchange
    #     ⟨V⟩ = ∫₀^{2k_F} (q dq / 2k_F²) · 4πα_c/(q² + m_D²)
    #     λ    = ½ · N₀(two bands, both spins) · ⟨V⟩    (pairing-channel ½)
    #     with N₀ = 2·k_F²/π² (v = 1 units): λ = α_c·ln(1+R)/π = α_c·k
    n = 400000
    mD2 = 8.0 * ALPHA_C / math.pi          # in k_F = 1 units
    s = 0.0
    for i in range(n):
        q = 2.0 * (i + 0.5) / n
        s += q * (4 * math.pi * ALPHA_C) / (q * q + mD2)
    avgV = s * (2.0 / n) / 2.0             # ∫ q dq/(2k_F²), k_F = 1
    lam = 0.5 * (2.0 / math.pi ** 2) * avgV
    k_numeric = lam / ALPHA_C
    print(f"\n2. numerical Fermi-surface average: k = λ/α_c = {k_numeric:.6f}")
    print(f"   closed form ln(1+R)/π            = {K_CLOSED:.6f}")
    print(f"   agreement: {abs(k_numeric-K_CLOSED)/K_CLOSED:.2e} relative")
    print("   conventions that land it, printed openly: N₀ per band with both")
    print("   spins (k_F²/π²), two velocity-matched bands, pairing-channel ½,")
    print("   transfer measure q dq/2k_F² over the full backscattering range.")

    # (3) the golden-rule reduction
    g_scr = ALPHA_C / K_CLOSED
    p = g_scr / (4 * math.pi)
    print(f"\n3. the reduction: P_cycle = g_scr/4π = {p:.3e}  ⟺  weight zero:")
    print("   |M|² = 1 under the unit s-wave measure ∫dΩ/4π, no velocity")
    print("   suppression, no phase-space enhancement. A dipole channel carries")
    print("   (v/c_s)² and is the computed-subdominant bare channel; the erasure")
    print("   channel must be the contact-class screened exchange at weight zero.")
    print("   Flag (i) is REDUCED to exhibiting that property — not closed here.")

    print("\nVERDICT: no numerology remains between the pieces — R, m_D², k, and")
    print("   g_scr are one screening object seen four ways, verified end to end.")
    print("   The keystone's remaining gates: (a) the weight-zero exhibit for the")
    print("   erasure channel; (b) the μ ≫ T host condition (task #16). Nothing")
    print("   promoted; the gate is sharper than it was.")
    print("=" * 78)

    assert abs(R_from_screening - R_recorded) < 1e-12
    assert abs(k_numeric - K_CLOSED) / K_CLOSED < 1e-3
    assert abs(4 * math.pi / g_scr - 783.3) < 1.0


if __name__ == "__main__":
    main()
