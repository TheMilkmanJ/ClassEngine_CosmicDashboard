"""census_democratic_license — task #6: the equal-share step, licensed and refereed (2026-07-27).

THE OPEN STEP (recorded)
  c = 9/10 counts the universal charged-fermion roster over ten channels with
  EQUAL SHARE per channel — "which the framework does not force."  The
  ensemble confirms 9/10 at −0.08σ but excludes neither 12/13 nor the
  charge²-weighted 8/9 (0.30σ).

THE LICENSING ARGUMENT (new; argument grade, with its condition named)
  The corpus's recorded census principle is blindness: the medium couples to
  energy content, not particle identity.  Weightings diagnose sectors:
    * if the shared object is the MEDIUM's binding budget, blindness forces
      equal share — the democratic count, c = 9/10;
    * if the shared object were an ELECTROMAGNETIC response, weights would be
      charge² — c = 8/9;
    * per-generation sharing or roster changes give 12/13-class counts.
  So "equal share" is not a free assumption: it is the direct consequence of
  the recorded blindness principle, CONDITIONAL on the sharing happening in
  the medium sector — which is where the amplitude's chain lives (ε = c·f̄·α_c
  is built from the medium's coupling and the winding average, not from an EM
  response).  The condition is named, not hidden: a future demonstration that
  the share is taken in the EM sector would flip the count to 8/9 and the
  measurement would show it.

  Observation, weight zero: this is the third appearance of one counting law —
  equal integer occupancy per cell gives the vacuum energy (recorded), the
  lepton-ring balance (the occupancy lock, candidate), and here the equal
  channel share.  One principle, three uses; noted, not stacked.

THE REFEREE (computed below)
  The three candidates differ by 1.2–2.6% in c, hence in ε linearly.  From the
  recorded anchors (9/10 at −0.08σ, 8/9 at 0.30σ) the current ensemble width
  on c is ~4%.  The table gives the ε-precision needed to separate the
  candidates at 3σ — and the instrument is the running α_c/ε chain.

GRADE RULE
  Licensing at argument grade with a named condition; referee arithmetic
  exact.  The count does not become "derived."  Nothing promoted.
"""
from __future__ import annotations

C_DEM = 9.0 / 10.0
C_Q2 = 8.0 / 9.0
C_1213 = 12.0 / 13.0
SIGMA_NOW = (C_DEM - C_Q2) / C_Q2 / 0.30    # fractional width implied by 0.30σ


def main() -> None:
    print("=" * 78)
    print("The democratic count: licensed by blindness, refereed by precision")
    print("=" * 78)
    print("\n   candidate counts and separations:")
    print(f"   democratic (medium-sector share)  c = 9/10  = {C_DEM:.4f}")
    print(f"   charge²-weighted (EM-sector)      c = 8/9   = {C_Q2:.4f}"
          f"   ({100*(C_DEM-C_Q2)/C_Q2:+.2f}%)")
    print(f"   roster-variant                    c = 12/13 = {C_1213:.4f}"
          f"   ({100*(C_1213-C_DEM)/C_DEM:+.2f}%)")
    print(f"\n   implied current ensemble width on c: ~{100*SIGMA_NOW:.1f}%")
    print("\n   separation requirements (3σ), as precision on ε = c·f̄·α_c:")
    for name, other in (("9/10 vs 8/9", C_Q2), ("9/10 vs 12/13", C_1213)):
        sep = abs(C_DEM - other) / C_DEM
        need = 100 * sep / 3.0
        print(f"   {name:15s}: Δc/c = {100*sep:.2f}%  ⟹  σ_ε ≲ {need:.2f}%")
    print("\nREAD")
    print("  1. The equal-share step is now LICENSED, not bare: the recorded")
    print("     blindness principle (the medium couples to energy content, not")
    print("     identity) forces the democratic count, conditional on the share")
    print("     being taken in the medium sector — where the amplitude chain")
    print("     lives. The weighting is a SECTOR DIAGNOSTIC: 9/10 medium,")
    print("     8/9 electromagnetic. The condition is named and falsifiable.")
    print("  2. The referee is quantitative: separating 9/10 from 8/9 at 3σ")
    print("     needs σ_ε ≈ 0.4% — the running α_c/ε chains are the instrument,")
    print("     and their posterior width decides when the count stops being")
    print("     conditional. 12/13 needs only ~0.9% and falls first.")
    print("  3. Grade: assumption → licensed-with-named-condition. Not derived;")
    print("     the license inherits the blindness principle's own grade.")
    print("=" * 78)

    assert abs(SIGMA_NOW - 0.041) < 0.01
    assert abs(100 * (C_DEM - C_Q2) / C_DEM / 3.0 - 0.41) < 0.05
    assert C_Q2 < C_DEM < C_1213


if __name__ == "__main__":
    main()
