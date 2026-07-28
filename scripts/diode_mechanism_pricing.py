"""diode_mechanism_pricing — #39/#104 stage 7: the rectifier's mechanism classes, each priced from recorded inputs (2026-07-27).

SUPERSEDED ON CLASS B'S PARAMETERISATION (stage 8, 2026-07-28) — READ FIRST.
  The ELIMINATION below stands: classes A and C are dead by 26 and 2.1
  orders, and class B is the survivor.  What does NOT stand is class B's
  efficiency as written here, R_B ~ (m1/thetadot)*F.
  `scripts/kapitza_junction_response.py` performs the owed averaging and
  returns  R_B = omega_J^2 / (2*Gamma_phi*thetadot), with no m1 in it.
  The reason: for an OVERDAMPED coordinate — and class B's own premise is
  that the bath overdamps by ~1e7 — a pinning term enters as the
  relaxation rate m1^2/Gamma_phi = 9.4e-16 eV, not as the frequency m1.
  Comparing m1 to thetadot is what an undamped phase would do.
  Consequence: the m1/thetadot = 3.8e-5 watch is NOT earned, the F
  needed below is not a meaningful O(1) target, and the number the sector
  actually owes is the seat coupling's junction plasma frequency
  omega_J ~ 5.7 keV at T_sph.  Take class B's efficiency from stage 8.

WHAT STAGE 6 LEFT
  The symmetric junction is adiabatically null; the whole transmission
  rides the junction's θ → −θ symmetry breaking.  The needed efficiency:
  ~5×10⁻⁵.  The watch: m₁/θ̇(T_sph) = 3.8×10⁻⁵ (ratio 0.75 of need).

THE HONEST METHOD (no winner declared by hope)
  Three known mechanism classes can make a wound junction transfer net
  charge.  Each has a DERIVABLE efficiency scaling from recorded inputs.
  Price all three; report which (if any) lands; state the kill honestly
  if none does.  The classes:

  A. SPONTANEOUS-LEPTOGENESIS (dissipative bias): the rotating phase acts
     as chemical potential μ = θ̇ for the current it couples to; net
     asymmetry needs a ΔL-VIOLATING RATE Γ_ΔL in the bath:
         η_A ~ (Γ_ΔL/H)·(θ̇/T)   at T_sph.
     Recorded (stage 4): Γ_ΔL/H = 1.6×10⁻¹², θ̇/T = 1.9×10⁻²⁴ →
     η_A ~ 3×10⁻³⁶ — computed dead (26 orders), kept for the roster.

  B. KAPITZA-RECTIFIED PINNED PHASE (the driven overdamped junction):
     the visible-side phase φ is overdamped by the thermal bath
     (Γ_φ ≫ θ̇), pinned by the Majorana term (strength ∝ m₁), and shaken
     by the fast seat-coupling drive J·sin(φ − θ(t)).  Second-order
     averaging (Kapitza) gives a rectified slip current; the efficiency
     relative to the coherent transfer scale carries the pinning-to-drive
     ratio:  R_B ~ (m₁/θ̇)·F(J/Γ_φθ̇)  with F ≤ O(1).
     The LEADING factor is the watch's own ratio — this is the class the
     coincidence points at.  What is NOT derived here: F's value (needs
     the ν-sector damping Γ_φ and the seat J at T_sph — both recorded
     objects, but their junction combination is the careful derivation).

  C. STATIC φ₀-DIODE (harmonic asymmetry): a static current-phase
     relation with harmonics.  Under UNIFORM winding every zero-mean
     periodic I(θ) time-averages to zero — this class is DEAD by the
     same adiabatic theorem as stage 6 unless the winding is modulated;
     the winding's only recorded modulation is Hubble (θ̇ ∝ a⁻³), giving
     back the H/θ̇ suppression stage 6 already priced: R_C ~ (H/θ̇)·h₂
     with h₂ ≤ 1 the harmonic asymmetry → ≤ 4×10⁻⁷.  Dead by ≥ 10².

THE VERDICT STRUCTURE (pre-committed)
  * If only class B lands in the decade of the need, the rectifier is
    the Kapitza-pinned junction at candidate-mechanism grade, with the
    one owed factor F named (the careful derivation's object) and the
    kill condition: F < 10⁻² kills it (then nothing recorded transfers).
  * The watch m₁/θ̇ is EARNED as class B's leading factor or not at all.
"""
from __future__ import annotations

import math

M1_EV = 2.25e-3
THETA_DOT_EV = 59.7
H_EV = 2.44e-5
T_SPH_EV = 131.7e9
NEED = 5.0e-5
GAMMA_DL_OVER_H = 1.6e-12


def main() -> None:
    print("=" * 78)
    print("The rectifier's mechanism classes, priced — #104 stage 7 / board #39")
    print("=" * 78)

    eta_A = GAMMA_DL_OVER_H * (THETA_DOT_EV / T_SPH_EV)
    R_B = M1_EV / THETA_DOT_EV
    R_C = H_EV / THETA_DOT_EV

    print(f"\n   need: R ≈ {NEED:.1e}")
    print(f"\n   A. spontaneous-leptogenesis (dissipative): "
          f"η_A ~ {eta_A:.1e} → dead by {math.log10(NEED/eta_A):.0f} orders")
    print(f"   B. Kapitza-pinned junction: R_B ~ (m₁/θ̇)·F = {R_B:.2e}·F"
          f" → F needed: {NEED/R_B:.2f} (an O(1))")
    print(f"   C. static φ₀-diode under uniform winding: R_C ≤ {R_C:.1e}"
          f" → dead by {math.log10(NEED/R_C):.1f} orders (stage 6's theorem)")

    print("\n   the discrimination is clean: classes A and C are computed dead")
    print("   (26 and 2.1 orders); class B is the ONLY survivor, and its")
    print("   leading factor is exactly the recorded watch:")
    print(f"      m₁/θ̇(T_sph) = {M1_EV}/{THETA_DOT_EV} = {R_B:.2e}"
          f"  = {R_B/NEED:.2f} × need")
    print("   with the remaining factor F an O(1) junction response that the")
    print("   careful derivation owes (inputs: the ν-sector damping at T_sph —")
    print("   deep equilibrium, overdamped ✓ — and the seat coupling J; both")
    print("   recorded objects).")

    print("\nVERDICT:")
    print("   THE MECHANISM CLASS IS SELECTED BY ELIMINATION, at candidate-")
    print("   mechanism grade: the rectifier is the driven overdamped")
    print("   junction — the only class of the three that recorded inputs do")
    print("   not kill.")
    print()
    print("   THE m₁/θ̇ LEADING FACTOR SHOWN ABOVE IS SUPERSEDED (stage 8).")
    print("   The owed averaging was performed in")
    print("   scripts/kapitza_junction_response.py and returns")
    print("      R_B = ω_J²/(2Γ_φθ̇)   — no m₁ in it.")
    print("   An overdamped phase feels a pinning term as the rate m₁²/Γ_φ =")
    print("   9.4e-16 eV, seventeen orders under θ̇, so m₁ vs θ̇ was never the")
    print("   right comparison; and where such a term IS strong enough to")
    print("   hold the phase it destroys the accumulated asymmetry instead of")
    print("   supplying it. The m₁/θ̇ = 0.75×-need watch is therefore a")
    print("   coincidence, not a mechanism.")
    print()
    print("   What the sector owes is the seat coupling's junction plasma")
    print("   frequency at T_sph: ω_J ≈ 5.7 keV (equivalently a ~6 meV")
    print("   relaxation rate on the visible phase). Four consumers ride")
    print("   that number; it is the owner-session's sharpest single target.")
    print("=" * 78)


if __name__ == "__main__":
    main()
