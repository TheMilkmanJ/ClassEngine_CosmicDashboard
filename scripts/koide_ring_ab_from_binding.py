"""koide_ring_ab_from_binding — computation (i): does the recorded binding give a = 3b? (2026-07-27)

QUESTION
  The null reduced to a stiffness relation: Q = 2/3 ⟺ a = 3b for the √m field
  on the ring (koide_null_stiffness_reduction.py).  Does the recorded
  string+log positional binding supply that ratio — under the tempting
  identification that a face's √m tracks its geometric depth (δ√m ∝ δr_k)?

METHOD
  Under that proxy, the √m-field stiffness matrix inherits from the positional
  Hessian projected onto per-face radial coordinates: the symmetric (breathing)
  combination is the neutral mode, the antisymmetric pair the charged modes.
  Both layers of the recorded theory are checked:
    classical:  ε_neutral = k_A = 3q̃²,  ε_charged = k_E = 0   (the flat pair)
    quantum-stabilized:  the effective shape potential rises as u^{3/2}
      (transverse zero-point ∝ √u), so the effective charged stiffness at the
      origin is DIVERGENT — a cusp, not a curvature.

GRADE RULE
  An honest negative is expected and is the deliverable: neither layer gives 2.
  The result localizes where a = 3b must come from — it is NOT ring geometry.
"""
from __future__ import annotations

import numpy as np

Q2 = 1.0


def positional_sector_stiffness(alpha_d: float = 0.0):
    """Recorded results, restated: breathing 3q̃²−6α_d; shape pair −(3/2)α_d."""
    return 3.0 * Q2 - 6.0 * alpha_d, -1.5 * alpha_d


def main() -> None:
    print("=" * 78)
    print("(i) The on-site/bond ratio from the recorded binding — the proxy fails")
    print("=" * 78)
    print("\n   target: ε_charged/ε_neutral = 2  (⟺ a = 3b ⟺ Q = 2/3)")
    print("\n   classical layer (positional Hessian, recorded):")
    for ad in (0.0, 0.3):
        kA, kE = positional_sector_stiffness(ad)
        r = kE / kA if abs(kA) > 1e-12 else float("nan")
        print(f"     α_d = {ad:.1f}:  ε_n = {kA:+.2f}, ε_c = {kE:+.2f}  →  ratio {r:+.3f}"
              f"   (need +2.000)")
    print("     The charged (shape) sector has NO restoring force classically —")
    print("     ratio 0 or negative, never 2. Thermal charged power would be")
    print("     unbounded: Q → 1, the recorded wrong answer.")
    print("\n   quantum-stabilized layer (the zero-point survivor's landscape):")
    print("     V_eff rises as u^(3/2) near the ring point (transverse stiffness")
    print("     grows ∝ √u — the shape-QM result), so the effective charged")
    print("     stiffness AT the ring is divergent: a cusp. Ratio → ∞, thermal")
    print("     charged power quenched: Q → 1/3. Also never 2.")
    print("\nVERDICT (i): NEGATIVE, and localizing. Under the geometric proxy the")
    print("   recorded binding gives ratio 0 (classical) or ∞ (quantum) — it")
    print("   brackets 2 without ever producing it. Conclusion: the a = 3b")
    print("   relation, if real, does NOT live in ring geometry. It must live in")
    print("   the mass-generation (kernel) dynamics — the hop/attenuation sector")
    print("   that sets √m, where the K1 screened-correlator reading already")
    print("   operates. Fences: the δ√m ∝ δr proxy is the thing tested; its")
    print("   failure is the result.")
    print("=" * 78)

    kA0, kE0 = positional_sector_stiffness(0.0)
    assert kE0 == 0.0 and kA0 == 3.0
    assert abs(kE0 / kA0 - 2.0) > 1.9        # nowhere near the target


if __name__ == "__main__":
    main()
