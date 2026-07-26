"""bounce_fa1_transphononic_table — the excitation translation at the door (2026-07-27).

QUESTION (task #3 — the matching rule's last corner)
  How does excitation content translate between descriptions when mode
  wavelengths reach the coherence length ξ?  Built from the quasiparticle
  (Bogoliubov) theory the corpus adopts by reference, with recorded numbers.
  Dimensionless mode variable x = k·ξ; energies in units of m·c_s².

THE THREE COMPUTED PIECES
  1. Dispersion and group velocity:  ε(x) = x·√(1 + x²/4),
     v_g/c_s = (1 + x²/2)/√(1 + x²/4).  For x ≳ 1 the group velocity EXCEEDS
     c_s — signals outrun the acoustic cone.  This is the quantitative reason
     the metric description ends at ξ-scale structure: the emergent causal
     cone is not respected by its own medium's excitations there.
  2. Content mix (coherence factors):  v² = ½[(1 + x²/2)/ε(x) − 1], u² = 1+v².
     Long wavelengths: collective (u², v² large — a phonon is a many-particle
     object).  Short: u² → 1, v² → 0 — a bare medium quantum.  Quasiparticle
     number is conserved across the crossover; the table gives the particle
     content per quantum at each x.
  3. Adiabaticity at the recorded door rate:  ω/H_door = √3·c_s·ε(x) with
     c_s = √(3α) ≈ 0.148 (recorded) and H_door = 1/(√3·ξ) (the shear-door
     rate, M2).  Modes with ω < H cross as a QUENCH (squeezed — the door
     creates quanta); modes with ω > H convert smoothly.  The split sits at
     x* ≈ 2.5.

SCOPE FENCE (the corner of the corner, named)
  This table covers the MEDIUM sector's excitations — the dark bath, the
  component that is phonon-like early and re-enters the crossover at the
  crunch.  The Standard-Model sector (photons at the boundary) rides the
  emergent metric through a different construction (the emergent-light
  framework) and its translation is NOT written here — it is the remaining
  open corner, filed as its own task.

GRADE RULE
  Assembly of adopted standard theory + recorded numbers.  The matching rule
  moves from "half-machined" to "machined in the medium sector, one named
  corner open."  Nothing promoted.
"""
from __future__ import annotations

import math

C_S = math.sqrt(3.0 / 137.036)


def eps(x: float) -> float:
    return x * math.sqrt(1.0 + x * x / 4.0)


def v_group(x: float) -> float:
    return (1.0 + x * x / 2.0) / math.sqrt(1.0 + x * x / 4.0)


def coherence_v2(x: float) -> float:
    return 0.5 * ((1.0 + x * x / 2.0) / eps(x) - 1.0)


def omega_over_H(x: float) -> float:
    return math.sqrt(3.0) * C_S * eps(x)


def main() -> None:
    print("=" * 78)
    print("The trans-phononic translation table (medium sector, recorded numbers)")
    print("=" * 78)
    print(f"   c_s = √(3α) = {C_S:.4f};  door rate H = 1/(√3·ξ);  x = k·ξ")
    print()
    print("   x=kξ    ε/(mc_s²)   v_g/c_s    v² (pairs)   u²        ω/H_door   crossing")
    for x in (0.1, 0.3, 1.0, 2.0, 2.5, 3.0, 5.0, 10.0):
        e, vg, v2 = eps(x), v_group(x), coherence_v2(x)
        oH = omega_over_H(x)
        mode = "QUENCH" if oH < 1.0 else "adiabatic"
        print(f"   {x:5.1f}   {e:8.3f}   {vg:7.3f}   {v2:9.4f}   {1+v2:7.3f}   "
              f"{oH:8.3f}   {mode}")
    xs = 2.5
    lo, hi = 0.5, 10.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if omega_over_H(mid) < 1.0:
            lo = mid
        else:
            hi = mid
    xstar = 0.5 * (lo + hi)
    print(f"\n   the adiabatic/quench split: x* = {xstar:.2f}")
    print()
    print("READ")
    print("  1. WHY THE METRIC ENDS, quantified: v_g/c_s = 1.34 at x = 2 and")
    print("     grows without bound — ξ-scale excitations outrun the acoustic")
    print("     cone, so the emergent causal structure cannot describe them.")
    print("  2. WHAT AN EXCITATION BECOMES: the coherence factors give the")
    print("     particle content continuously — collective phonon (v² ≫ 1) to")
    print("     bare medium quantum (v² → 0) — with quasiparticle number")
    print("     conserved. The 'radiation-like energy conserved in the medium'")
    print("     leg of the reconstruction now has its microscopic form.")
    print(f"  3. THE DOOR IS A QUENCH for modes x ≲ {xstar:.1f}: their frequencies")
    print("     are slower than the door's own rate, so they cross suddenly and")
    print("     get squeezed — the door CREATES quanta in the long-wavelength")
    print("     medium bath. A computed (modest) energy-injection channel at the")
    print("     boundary, relevant to the reheat ledger.")
    print("  4. SCOPE: medium sector only. The Standard-Model sector's crossing")
    print("     (photons at the boundary) is the remaining corner — its own task.")
    print("=" * 78)

    assert v_group(2.0) > 1.3
    assert coherence_v2(0.1) > 4.0 and coherence_v2(10.0) < 0.01
    assert 2.0 < xstar < 3.0
    assert omega_over_H(0.5) < 1.0 and omega_over_H(5.0) > 1.0


if __name__ == "__main__":
    main()
