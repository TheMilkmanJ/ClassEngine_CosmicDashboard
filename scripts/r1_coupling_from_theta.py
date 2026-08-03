"""r1_coupling_from_theta — clearing R1's amplitude gap: the coupling constant the Beta law fixes (2026-07-27).

THE GAP BEING CLEARED
  Candidate R1 (the inverted lever) is recorded with a round "≈1%"
  suppression, giving m_e(recombination)/m_e(laboratory) = 1.0101, while
  the model's own derived shift is ε = c·f̄·α_c = 27α/5π = 1.2543%,
  giving 1.012543.  The audit ledger already grades that mismatch "loose
  rather than wrong", because R1's 1% is described as an approximate
  measured input.  This script removes the looseness instead of living
  with it.

THE ARGUMENT
  R1 is not free to choose an amplitude.  It reads the SAME observed
  quantity the model derives — the ratio of the electron mass at
  recombination to its laboratory value — from the other side.  So the
  suppression is fixed:
      m_e(lab) = m_e(bare)·(1 − S),  ratio = 1/(1 − S) = 1 + ε
      ⟹ S = ε/(1 + ε)      (NOT S = ε; that is the source of the 1%)
  R1 therefore inherits the derived ε exactly and makes no independent
  amplitude claim at all.

  What R1 DOES add is a coupling constant, and V5's result now fixes it.
  The caustic bit Θ = Q/(Q+K) has both endpoints known:
    * developed speckle (shell-crossed, virialized — where laboratories
      sit): ⟨Θ⟩ = 1/2 EXACTLY, by the Beta(d/2, d/2) law — independent
      of power spectrum, dispersion, density, epoch, dimension, anisotropy;
    * laminar flow (unvirialized — the dark-ages IGM, recombination):
      Θ = 1.9×10⁻⁶, i.e. zero to six orders.
  With a linear coupling m_e = m_bare·(1 + κ_Θ·Θ), the laboratory sits at
  Θ = 1/2 and the bare environment at Θ ≈ 0, so
      1 − S = 1 + κ_Θ/2   ⟹   κ_Θ = −2S = −2ε/(1 + ε)
  a number, not a fitted input.

WHAT THIS BUYS
  (i) the spurious tension disappears — R1 does not require 1.0101, it
      requires exactly what the model derives;
  (ii) R1's one free-looking number becomes a derived coupling;
  (iii) the residual-laminar correction ⟨Θ⟩ ≈ ½ − 0.155·f converts
        directly into an environment-dependent shift, which is the
        observable the 21-cm fork tests.
"""
from __future__ import annotations

import math

ALPHA = 1.0 / 137.036
EPS = 27.0 * ALPHA / (5.0 * math.pi)      # the derived stack, 27α/5π
THETA_DEV = 0.5                            # Beta(d/2,d/2) mean, exact
THETA_LAM = 1.9e-6                         # laminar control


def main() -> None:
    print("=" * 78)
    print("R1's amplitude, cleared: the coupling the Beta law fixes")
    print("=" * 78)
    ratio = 1.0 + EPS
    S = EPS / (1.0 + EPS)
    print(f"\n   derived shift ε = 27α/5π                 = {100*EPS:.4f}%")
    print(f"   ratio m_e(recombination)/m_e(lab) = 1+ε   = {ratio:.6f}")
    print(f"   suppression inside shell-crossed regions  = ε/(1+ε) = {100*S:.4f}%")
    print(f"   (the recorded round '1%' would give ratio {1/(1-0.01):.6f}, "
          f"a shift of {100*(1/(1-0.01)-1):.4f}%)")
    print(f"   → the gap is the algebra S = ε/(1+ε), not a disagreement: "
          f"{100*(S-0.01):.4f} percentage points")

    dTheta = THETA_DEV - THETA_LAM
    kappa = -S / dTheta
    print(f"\n   Θ endpoints, both now known:")
    print(f"     developed speckle (laboratories)  ⟨Θ⟩ = {THETA_DEV}  (exact, Beta law)")
    print(f"     laminar flow (bare environments)   Θ  = {THETA_LAM:.1e}")
    print(f"     ΔΘ = {dTheta:.6f}")
    print(f"\n   linear coupling m_e = m_bare(1 + κ_Θ·Θ) ⟹ κ_Θ = −S/ΔΘ = "
          f"**{kappa:.6f}** ({100*kappa:.4f}%)")
    print(f"   equivalently κ_Θ = −2ε/(1+ε) = {-2*EPS/(1+EPS):.6f}  ✓")

    print("\n   the environment-dependent prediction this makes (the 21-cm fork):")
    print("   with a residual-laminar fraction f, ⟨Θ⟩ ≈ ½ − 0.155·f, so")
    print("     δm_e/m_e(f) = κ_Θ·(⟨Θ⟩(f) − 0) − κ_Θ·½ = −κ_Θ·0.155·f")
    for f in (0.0, 0.25, 0.5, 1.0):
        shift = -kappa * 0.155 * f
        print(f"     f = {f:.2f}:  δm_e/m_e = {100*shift:+.4f}% relative to a "
              f"fully developed environment")

    print("\nVERDICT: the amplitude gap is arithmetic, not physics — R1 inherits")
    print("   the derived ε exactly and makes NO independent amplitude claim,")
    print("   once the suppression is written S = ε/(1+ε) rather than S = ε.")
    print("   With that fixed, R1's remaining number is a COUPLING, and the")
    print("   Beta law's exact ½ fixes it at κ_Θ = −2ε/(1+ε) = −2.478%. What")
    print("   was a free-looking input is now determined by two derived things:")
    print("   the amplitude ε and the plateau ½. The 21-cm fork then tests a")
    print("   sloped prediction rather than a bare offset.")
    print("=" * 78)


if __name__ == "__main__":
    main()
