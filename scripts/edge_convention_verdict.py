"""edge_convention_verdict — docket #124's deciding arithmetic, absent from the corpus until now (2026-07-27).

THE QUESTION
  Is the gap between the anchor band and the shooter's 13–20 TeV census
  landing an artifact of how the anchor's edges are defined?  The corpus
  recorded the CONCLUSION ("the arrow fell, not the convention",
  2026-07-20) but never the computation: every recorded ratio uses the
  booked convention only.  This script prices EVERY admissible pairing.

THE CONVENTIONS (from the hierarchy file's own budget table)
  booked:          the −3/2 form, no exact-solution factor — base band
                   1.6–5.2 TeV × e^(−(c+a)) = 0.343029 → 0.549–1.784 TeV
  exact-solution:  the asinh form's ×2 absorbed — doubles the band:
                   1.098–3.568 TeV
  (c = 0.789262 the crossed box, a = 0.280677 the Fock companion)

THE BAND-DEFINITION ADJUDICATION (the audit's check F)
  Two recorded readings of what the corrected band IS:
    A. the two-term range compounded with the full O(λ) factor:
       [1.6, 5.2] × 0.343 = [0.549, 1.784]  (the booked numbers);
    B. the perturbative-control spread around the bottom-edge point:
       [1.576 × 0.343, 1.576] = [0.541, 1.576].
  They differ by 11% at the top edge.  BOTH are priced below — the
  verdict must be (and is) convention-robust across A, B, and the ×2.

THE SHOOTER-SIDE CAVEAT (check H, recorded not resolved)
  13–20 TeV appears in three files with NO computation in the
  repository behind it (the shooter program is recorded as mooted; no
  script produces the number).  The verdict below is therefore a
  statement about the ANCHOR side: no anchor-edge convention closes the
  gap TO the quoted shooter numbers.  Whether those numbers are
  reproducible is a separate, open provenance question.
"""
from __future__ import annotations

C_BOX = 0.789262
A_FOCK = 0.280677
import math

F = math.exp(-(C_BOX + A_FOCK))
SHOOTER = (13.0, 20.0)


def main() -> None:
    print("=" * 78)
    print("Every admissible edge pairing, priced — docket #124's verdict arithmetic")
    print("=" * 78)
    print(f"\n   O(λ) factor e^(−(c+a)) = {F:.6f}")
    bands = {
        "A booked (two-term × full O(λ))": (1.6 * F, 5.2 * F),
        "B control-spread (bottom-point)": (1.576 * F, 1.576),
        "A × exact-solution (×2)": (2 * 1.6 * F, 2 * 5.2 * F),
        "B × exact-solution (×2)": (2 * 1.576 * F, 2 * 1.576),
    }
    print(f"   shooter (as quoted, provenance NOT in repo): {SHOOTER[0]}–{SHOOTER[1]} TeV\n")
    print("   convention                          band [TeV]     min gap   max gap")
    best = 1e9
    for name, (lo, hi) in bands.items():
        gmin = SHOOTER[0] / hi
        gmax = SHOOTER[1] / lo
        best = min(best, gmin)
        print(f"   {name:<34} {lo:.3f}–{hi:.3f}   {gmin:6.2f}×  {gmax:6.2f}×")
    print(f"\n   the most anchor-favorable pairing in the table: {best:.2f}× — NO OVERLAP.")
    print("\n   ratio-convention fix (the files' inconsistency): the honest range is")
    print(f"   nearest-edges to farthest-edges: {SHOOTER[0]/bands['A booked (two-term × full O(λ))'][1]:.1f}× to "
          f"{SHOOTER[1]/bands['A booked (two-term × full O(λ))'][0]:.1f}× under the booked convention")
    print("   (the recorded '24×' was 13/bottom — a mixed pairing; the recorded")
    print("   '5.4×' was display-propagated where the source gives 5.50).")

    print("\nVERDICT: the 2026-07-20 conclusion is CONFIRMED BY COMPUTATION —")
    print("   no anchor-edge convention closes the gap (minimum 3.6× under the")
    print("   most favorable admissible pairing; the two band definitions agree")
    print("   on the verdict within their 11%). The arrow fell, not the")
    print("   convention. The one open item is the SHOOTER side: 13–20 TeV has")
    print("   no recorded computation in this repository — the verdict's other")
    print("   leg rests on an unreproduced number, recorded as the closure's")
    print("   standing caveat.")
    print("=" * 78)


if __name__ == "__main__":
    main()
