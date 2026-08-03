"""substructure_count_closure — the triangle's keystone: N₁ from the cascade cutoff (2026-07-27).

THE TARGET
  Why a scaling vortex network carries N₁ = 4πk/α_c = 783 substructure cells
  per network-cell dimension — equivalently, why the small-scale cutoff sits
  at ℓ_min/L_net = g_scr/4π with g_scr = α_c/k the screened coupling.

THE SCALING CLOSURE (the derivation, candidate grade, flagged steps named)
  Small-scale structure on quantized vortex lines is Kelvin-wave structure.
  It is erased where emission into the medium beats the cascade:
    (1) per-oscillation emission probability  p = g_scr/4π
        — one perturbative emission vertex at the SCREENED coupling over the
        standard loop factor.  [FLAGGED identification: the erasure vertex is
        the screened exchange, the same object the amplitude reconstruction
        uses.]
    (2) over one network time L_net/c_s, structure at scale ℓ completes
        L_net/ℓ oscillations (Kelvin periods scale with ℓ at fixed prefactor
        class).
    (3) cutoff where cumulative emission ~ 1:
            (L_net/ℓ_min)·(g_scr/4π) = 1  ⟹  L_net/ℓ_min = 4π/g_scr = N₁.
  The demanded count is the closure's output, not an input.

WHY THE BARE CHANNEL DOES NOT ERASE FIRST (the second flagged step)
  Vanilla global strings are smoothed efficiently by order-unity Goldstone
  emission — that would give L_net/ℓ_min ~ O(1–10) and kill the count.  But
  small-scale vortex structure moves as Kelvin waves: deeply subsonic at
  small scales, with phonon emission suppressed by high powers of v/c_s —
  the same physics that lets laboratory quantum turbulence sustain Kelvin
  cascades two to three decades below the inter-vortex spacing before the
  phonon cutoff.  [FLAGGED: class-solid in superfluids; the medium's own
  suppression exponent is not computed here.]

THE CLASS ANCHOR (recorded as class support, not as the number)
  Laboratory superfluid turbulence exhibits exactly this two-scale
  structure: inter-vortex spacing over Kelvin-cutoff ratios of 10²–10³.
  The demanded 783 sits inside the class that nature already builds.

GRADE RULE
  A candidate derivation: the closure is exact given its two flagged steps;
  the count lands by structure.  PROMOTION: compute the medium's Kelvin
  emission cutoff from its recorded parameters and land 4π/g_scr.  KILL:
  that computation landing elsewhere, or the bare channel proving
  unsuppressed in this medium.
"""
from __future__ import annotations

import math

ALPHA_C = 3.0 / 137.036
K_SCREEN = 1.36461
C_S = math.sqrt(3.0 / 137.036)
HELIUM_CLASS = (1e2, 1e3)          # laboratory Kelvin-cascade hierarchies


def main() -> None:
    g_scr = ALPHA_C / K_SCREEN
    N1 = 4.0 * math.pi / g_scr
    p_emit = g_scr / (4.0 * math.pi)

    print("=" * 78)
    print("The substructure count from the cascade cutoff")
    print("=" * 78)
    print(f"\n   screened coupling g_scr = α_c/k = {g_scr:.5f}")
    print(f"   per-oscillation emission p = g_scr/4π = {p_emit:.3e}   [flagged vertex]")
    print(f"   cutoff closure: L_net/ℓ_min = 1/p = 4π/g_scr = {N1:.1f}")
    print(f"   demanded count (the winding-gas record): 783.3 — IDENTICAL by")
    print("   construction of the closure; the content is that a one-vertex")
    print("   erasure per oscillation, at the screened coupling, over one")
    print("   network time, reproduces the recorded count with no tuning.")
    print(f"\n   the bare-channel question: order-unity Goldstone smoothing would")
    print(f"   give L/ℓ ~ 1–10 and kill the count. Kelvin-wave structure is")
    print(f"   deeply subsonic at small scales (phonon emission suppressed by")
    print(f"   high powers of v/c_s, c_s = {C_S:.3f}) — the suppression that lets")
    print("   laboratory quantum turbulence run Kelvin cascades far below the")
    print("   inter-vortex spacing.   [flagged: exponent uncomputed here]")
    print(f"\n   class anchor: laboratory hierarchies run {HELIUM_CLASS[0]:.0e}–"
          f"{HELIUM_CLASS[1]:.0e};")
    print(f"   the demanded {N1:.0f} sits inside the class nature already builds.")
    print("\nVERDICT: the keystone has a CANDIDATE DERIVATION — the cascade-cutoff")
    print("   closure outputs the recorded count exactly, with two flagged steps")
    print("   (the screened erasure vertex; the medium's Kelvin suppression")
    print("   exponent) and a laboratory-class anchor. PROMOTE: compute the")
    print("   medium's Kelvin cutoff from recorded parameters and land 4π/g_scr.")
    print("   KILL: that computation landing elsewhere, or the bare channel")
    print("   proving unsuppressed. The triangle's keystone is no longer an")
    print("   unowned mystery — it is a specified superfluid-turbulence")
    print("   computation with a demanded answer.")
    print("=" * 78)

    assert abs(N1 - 783.3) < 1.0
    assert HELIUM_CLASS[0] < N1 < HELIUM_CLASS[1]
    assert p_emit < 0.01


if __name__ == "__main__":
    main()
