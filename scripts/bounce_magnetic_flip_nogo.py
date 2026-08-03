"""bounce_magnetic_flip_nogo — the polarity-reversal proposal, priced (2026-07-27).

PROPOSAL (owner): cosmic polarity reversal as the turn mechanism — the universe
flips its magnetic polarity the way Earth and the Sun do, and the flip switches
the "expansion levers" into contraction. Companion question: does the dark
sector have diamagnetism, and could that matter?

QUESTIONS
  1. Does a polarity flip couple to expansion at all?
  2. Can magnetic (or magnetization/diamagnetic) energy supply the turn?
  3. What budget does cosmic magnetism actually command?
  4. What parts of the instinct survive, and where do they live in the corpus?

GRADE RULE
  Exact class statements and recorded numbers only. Nothing promoted.
"""
from __future__ import annotations

import numpy as np

GAUSS_EV2 = 1.95e-2          # 1 gauss in eV² (natural units)
RHO_RAD0 = 3.3e-15           # today's radiation energy density, eV⁴
B_CAP_COMOVING = 1e-9        # CMB cap on primordial comoving field, gauss
B_VOID_FLOOR = 1e-16         # blazar-halo void floor, gauss


def maxwell_stress(B: np.ndarray) -> np.ndarray:
    """T_ij for a pure magnetic field (natural units): quadratic in B."""
    rho = 0.5 * (B @ B)
    return rho * np.eye(3) - np.outer(B, B)


def main() -> None:
    print("=" * 78)
    print("Polarity reversal / dark diamagnetism as the turn — priced")
    print("=" * 78)

    print("\n1. Does a polarity flip couple to expansion?")
    rng = np.random.default_rng(3)
    worst = 0.0
    for _ in range(50):
        B = rng.standard_normal(3)
        worst = max(worst, float(np.abs(maxwell_stress(B) - maxwell_stress(-B)).max()))
    print(f"   max |T(B) − T(−B)| over random fields = {worst:.1e}   (identically zero)")
    print("   Gravity couples to the field's stress-energy, which is QUADRATIC in")
    print("   B — a universal polarity reversal is gravitationally invisible, term")
    print("   by term. Earth's and the Sun's reversals redistribute field energy;")
    print("   they do not change it, and expansion sees only the energy.")

    print("\n2. Can magnetic / diamagnetic energy supply the turn?")
    B = rng.standard_normal(3)
    T = maxwell_stress(B)
    rho = 0.5 * (B @ B)
    p_eigs = np.linalg.eigvalsh(T)
    print(f"   NEC along principal axes: ρ+p = "
          f"{', '.join(f'{rho + p:.3f}' for p in p_eigs)}  (≥ 0 always; the")
    print("   parallel direction saturates, nothing goes negative). A diamagnetic")
    print("   response (χ < 0) stores POSITIVE energy in expelling the field —")
    print("   superconductors pay energy for the Meissner state; they do not mint")
    print("   negative energy. The turn needs ρ_X + p_X < 0. Wrong side, by class.")

    print("\n3. The budget, with the frozen-ratio anchor")
    for name, Bg in (("CMB comoving cap (1 nG)", B_CAP_COMOVING),
                     ("void floor (10⁻¹⁶ G)", B_VOID_FLOOR)):
        rho_B = 0.5 * (Bg * GAUSS_EV2) ** 2
        print(f"   {name:26s}: ρ_B = {rho_B:.1e} eV⁴ = "
              f"{rho_B / RHO_RAD0:.1e} of today's radiation")
    print("   Flux freezing gives B ∝ a⁻² ⟹ ρ_B ∝ a⁻⁴ — the SAME scaling as")
    print("   radiation, so these ratios are FROZEN for all time (M5's anchor):")
    print("   cosmic magnetism sits ≥7 orders under the radiation bath at every")
    print("   epoch, positive, forever. It can never even dominate, let alone flip.")

    print("\n4. What survives (and it is real)")
    print("   * The polarity-reversal instinct is the corpus's recorded CYCLIC")
    print("     grammar seen from outside: rotation is dynamical and may reset")
    print("     across cycles (outer working O10), and the helicity sign is set")
    print("     per cycle at genesis (the sign(μ·n) product, P-2026-028's rotation")
    print("     machine). The flip is something the bounce WRITES, not what")
    print("     CAUSES it — effect mistaken for cause.")
    print("   * The dark-diamagnetism instinct has a genuine in-model cousin: a")
    print("     superfluid medium responds to ROTATION the way superconductors")
    print("     respond to magnetic fields (rotation expulsion / London-class")
    print("     physics — the corpus's Fairbank thread). Real bookkeeping for how")
    print("     rotation carries or resets across the interval; NEC-nonnegative,")
    print("     so not a turn term.")

    print("\nVERDICT")
    print("   turn mechanism : FAIL by class, twice — polarity is gravitationally")
    print("                    invisible (quadratic coupling), and field energy is")
    print("                    positive radiation-class (frozen ratio, NEC ≥ 0).")
    print("   surviving role : the reversal as cyclic OUTCOME (O10 grammar); the")
    print("                    medium's rotation-expulsion as interval bookkeeping.")
    print("=" * 78)

    assert worst == 0.0
    assert all(rho + p >= -1e-12 for p in p_eigs)
    assert 0.5 * (B_CAP_COMOVING * GAUSS_EV2) ** 2 / RHO_RAD0 < 1e-6


if __name__ == "__main__":
    main()
