"""koide_null_occupancy_lock — the charged-power lock as occupancy-one (2026-07-27).

STATE OF THE NULL COMING IN
  * Neutral half: f₀ is a conserved quantity (computed — m₁(0) = 0 identically);
    set at the cycle start and conserved — it does not fluctuate.
  * Charged half: needs a lock pinning |f₁|² + |f₂|² to f₀² exactly, in a class
    that cannot scatter (index / quantization / conservation — #101's aisle).

THE CANDIDATE LOCK (the invented step, flagged)
  The corpus's occupancy principle (argument-grade, the vacuum-energy source):
  the ground state holds exactly ONE binding quantum per coherence cell.
  Application here — NEW, and the flagged step: the family ring is one coherence
  cell of the confining sector, and its binding quantum is the charged (family)
  mode.  Statement:
      the conserved zero-momentum amplitude (set at the cycle start) carries EXACTLY ONE charged-mode
      quantum of action:   N₀ ≡ M·ω₁·f₀² / ħ = 1,
  with the charged pair in its ground state (zero-point only).

WHAT THE BOOKKEEPING THEN GIVES (verified below, exact)
  charged pair zero-point:  |f₁|² + |f₂|² = 2·(ħ/2Mω₁) = ħ/(Mω₁)
  occupancy-one:            f₀² = ħ/(Mω₁)
  ⟹  f₀² = |f₁|² + |f₂|²   — THE NULL, exactly.
  ⟹  ρ² = 1/2, Q = 2/3, τ = ½ln2, T_c = 177.10 keV, ρ_Λ¼ = 2.2599 meV.
  The a = 3b stiffness relation is recovered as the classical SHADOW: writing
  the same two powers in equipartition language implies ε₁/ε₀ = 2.

WHY THIS IS THE RIGHT EXACTNESS CLASS
  N₀ is an integer.  Integer occupancy does not scatter — the observed
  |Q − 2/3| ~ 6×10⁻⁶ is compatible with a quantized lock in a way no ensemble
  ratio can be.  The full null then reads: CONSERVATION (neutral half, computed)
  + QUANTIZATION (charged half, this candidate).

WHAT IT MUST SURVIVE (named, unpaid)
  1. Why the charged mode's quantum is the unit — candidate answer: the charged
     modes ARE the ring's binding excitations, the same "binding quantum"
     grammar the vacuum argument uses; but this is the invented identification.
  2. The neutrino non-null: the neutrino tower is not a string-bound coherence
     cell of the confining sector ⟹ no occupancy statement applies ⟹ Q_ν ≠ 2/3
     — consistent with the recorded Q_ν = 0.458, and required.
  3. The standing external judges, unchanged: the SU(2) N_f = 3 lattice fork
     (P-2026-048), the deviation lock (P-2026-051), m_τ at ≲1.4 ppm.

GRADE RULE
  Candidate closure — the FIRST exactness-compatible one the null has had.
  The occupancy application is the flagged invented step.  Nothing promoted.
"""
from __future__ import annotations

import numpy as np

HBAR = 1.0


def bookkeeping(M: float, w1: float):
    """Exact mode bookkeeping for the ring cell."""
    zp_pair = 2.0 * (HBAR / (2.0 * M * w1))     # |f1|^2 + |f2|^2, ground state
    f0_sq = HBAR / (M * w1)                     # occupancy-one: N0 = 1
    rho_sq = (zp_pair / 2.0) / f0_sq            # |f1/f0|^2
    Q = 1.0 / 3.0 + (2.0 / 3.0) * rho_sq
    tau = -0.5 * np.log(rho_sq)
    shadow_ratio = f0_sq / (zp_pair / 2.0)      # implied eps1/eps0 in thermal language
    return zp_pair, f0_sq, rho_sq, Q, tau, shadow_ratio


def main() -> None:
    print("=" * 78)
    print("The occupancy lock: N₀ = 1 in the charged unit ⟹ the null, exactly")
    print("=" * 78)
    print("\n   M·ω₁ scan (the lock is scale-free — the point of a quantization law):")
    print("   M·ω₁      |f₁|²+|f₂|²    f₀² (N₀=1)     Q          τ")
    for mw in (0.5, 1.0, 3.7, 120.0):
        zp, f0, r2, Q, tau, _ = bookkeeping(1.0, mw)
        print(f"   {mw:6.1f}    {zp:10.5f}    {f0:10.5f}   {Q:.8f}  {tau:.8f}")
    _, _, r2, Q, tau, shadow = bookkeeping(1.0, 1.0)
    print(f"\n   null: f₀² = |f₁|²+|f₂|² at EVERY scale;  Q = {Q:.10f} = 2/3 exact")
    print(f"   τ = −ln ρ = {tau:.8f} = ½ln2 = {0.5*np.log(2):.8f}")
    print(f"   classical shadow: implied ε₁/ε₀ = {shadow:.1f}  (the a = 3b relation)")
    print("\n   Exactness class: N₀ is an INTEGER — a quantized lock cannot scatter.")
    print("   The full null = conservation (neutral half, computed) + quantization")
    print("   (charged half, this candidate).")
    print("\nVERDICT: candidate closure — the first exactness-compatible source the")
    print("   null has had. The occupancy application to the ring cell is the ONE")
    print("   flagged invented step; its named survival tests and the standing")
    print("   external judges (lattice fork, deviation lock, m_τ) are in the")
    print("   docstring. Registered, not promoted.")
    print("=" * 78)

    for mw in (0.5, 1.0, 3.7, 120.0):
        zp, f0, r2, Q, tau, shadow = bookkeeping(1.0, mw)
        assert abs(f0 - zp) < 1e-15                      # the null, exactly
        assert abs(Q - 2.0 / 3.0) < 1e-15
        assert abs(tau - 0.5 * np.log(2.0)) < 1e-15
        assert abs(shadow - 2.0) < 1e-15                 # the a = 3b shadow


if __name__ == "__main__":
    main()
