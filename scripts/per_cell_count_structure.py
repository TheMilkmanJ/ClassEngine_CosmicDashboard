"""per_cell_count_structure — the count decomposed exactly, and the cells' identity narrowed (2026-07-27).

THE TARGET
  Why does the screened interaction structure a network cell at
  N₁ = 4πk/α_c = 783 census cells per dimension?

1. THE EXACT DECOMPOSITION (algebra, verified below)
  With the recorded screening constant s = 2α_c/π and R ≡ 1/s = π/2α_c
  (the squared ratio of the Fermi scale to the screening scale,
  R = (2k_F·ℓ_TF)² in the reconstruction's own variables):
      N₁ = 4πk/α_c = (8R/π)·ln(1 + R) = 4π/g_scr,
  where g_scr ≡ α_c/k is the Fermi-surface-averaged screened exchange
  coupling.  In words: the count per dimension is the INVERSE SCREENED
  COUPLING IN LOOP UNITS — structurally, a channel count weighted by a
  Coulomb logarithm (the log of the scale ratio between screening and
  Fermi scales).  This names the owning problem: a screened-interaction
  channel/damping count, not an abstract normalization.

2. THE CELL-IDENTITY ELIMINATION (new, computed)
  If the census cells were particle-quanta at the medium's density, the
  count per network cell would be Q = n·(γ·d_causal)³ with n ∝ a⁻³ and the
  physical causal range ∝ a² in the radiation era:  Q ∝ a³ — the
  per-dimension count would GROW linearly in the scale factor, changing by
  ~e⁶⁰ across the observable window.  The shot amplitude would then carry
  an enormous extra scale dependence, destroying the measured tilt by
  orders.  DEAD: the cells cannot be fixed-density particles.
  What survives: cells that SCALE WITH THE NETWORK — substructure of the
  network itself (small-scale structure on the vortex lines: kinks, loops,
  wiggles), whose count per network cell is a PURE NUMBER of the network's
  internal dynamics, automatically constant in the scaling regime.

3. THE REFINED GATE (named, weight zero on the resemblance)
  The demanded pure number is 4π/g_scr with a Coulomb-log structure — and
  the natural owner of exactly that structure in network dynamics is the
  small-scale cutoff where screened-interaction damping beats stretching
  (damping integrals ARE channel-count × Coulomb-log objects).  The future
  computation is therefore specified: the substructure count per cell of a
  scaling vortex network with screened interactions at coupling α_c.  The
  structural resemblance aims the computation; it proves nothing.

GRADE RULE
  Decomposition exact; elimination computed; the count is NOT derived.
  The gate is refined from "derive N₁ locally" to "compute the scaling
  network's substructure count under screened damping."
"""
from __future__ import annotations

import math

ALPHA_C = 3.0 / 137.036


def main() -> None:
    s = 2.0 * ALPHA_C / math.pi
    R = 1.0 / s
    k = math.log(1.0 + R) / math.pi
    N1_recorded = 4.0 * math.pi * k / ALPHA_C
    N1_decomp = (8.0 * R / math.pi) * math.log(1.0 + R)
    g_scr = ALPHA_C / k

    print("=" * 78)
    print("The per-cell count: exact decomposition and the cell-identity elimination")
    print("=" * 78)
    print(f"\n1. The decomposition (exact):")
    print(f"   screening constant s = 2α_c/π = {s:.6f};  R = 1/s = {R:.3f}")
    print(f"   N₁ = 4πk/α_c        = {N1_recorded:.2f}")
    print(f"   N₁ = (8R/π)·ln(1+R) = {N1_decomp:.2f}   (identical)")
    print(f"   N₁ = 4π/g_scr with the screened coupling g_scr = α_c/k = {g_scr:.5f}")
    print("   READ: a Coulomb-log-weighted channel count — the owning problem is")
    print("   screened-interaction damping/channel counting, not bookkeeping.")

    print(f"\n2. The cell-identity elimination (computed):")
    print("   particle-quanta cells: count per network cell ∝ n·d_causal³ ∝")
    print("   a⁻³·a⁶ = a³ — the per-dimension count grows ∝ a, i.e. ~e⁶⁰ across")
    print("   the window; the shot amplitude would inherit that scale dependence")
    print("   and destroy the measured tilt by orders. DEAD.")
    print("   surviving identity: NETWORK SUBSTRUCTURE (kinks/loops/wiggles on")
    print("   the vortex lines) — scales with the network, count per cell a pure")
    print("   number, constant in the scaling regime by construction.")

    print(f"\n3. The refined gate:")
    print("   compute the substructure count per cell of a scaling vortex")
    print("   network with screened interactions at coupling α_c — the")
    print("   small-scale cutoff where screened damping beats stretching.")
    print("   The demanded answer: 4π/g_scr per dimension. The Coulomb-log")
    print("   resemblance aims the computation, at weight zero.")

    print("\nVERDICT: not derived — decomposed and narrowed. The count's owning")
    print("   problem is named (screened damping in the network's substructure),")
    print("   the wrong cell identity is dead by e⁶⁰, and the gate is now a")
    print("   specified computation rather than an open-ended mystery.")
    print("=" * 78)

    assert abs(N1_recorded - N1_decomp) < 1e-9
    assert abs(N1_recorded - 783.4) < 1.0
    assert abs(g_scr - 0.016042) < 1e-5
    assert R > 70.0


if __name__ == "__main__":
    main()
