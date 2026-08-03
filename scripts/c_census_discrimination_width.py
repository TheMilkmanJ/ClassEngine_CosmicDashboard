"""c_census_discrimination_width — what width actually separates the census candidates (2026-07-28).

WHAT IS RECORDED
  The c-derivation's gravity-routing step is withdrawn (docket #126): no
  single criterion returns 9/10, so c stands as a counting assumption the
  data confirms rather than a count the framework forces.  The recorded
  closing move is therefore measurement, and it is quoted in five places
  in the same words:

      "the pre-registered width that would SEPARATE the candidates is
       sigma_c <= 0.0115, a 3.3x sharpening"

WHY THAT NUMBER IS CHECKED HERE
  0.0115 is, to three digits, the SPACING between the two closest
  candidates (9/10 and 8/9 are 0.01111 apart).  A measurement whose error
  bar equals the spacing between two hypotheses puts them ONE sigma
  apart, and two hypotheses one sigma apart are not separated — that is
  the width at which they are merely no longer coincident.  So the quoted
  target is a NECESSARY condition being carried as a sufficient one.

WHAT THIS COMPUTES
  the candidate spacings, the width required for a genuine call at 2, 3
  and 5 sigma, and — since an ensemble's width falls as 1/sqrt(N) — the
  data multiple each of those demands relative to what is in hand.
"""
from __future__ import annotations

CANDIDATES = {
    "8/9  (charge-weighted, Sum N_c Q^2 = 8)": 8.0 / 9.0,
    "9/10 (the standing census)": 9.0 / 10.0,
    "12/13 (the wider roster)": 12.0 / 13.0,
}
C_MEAS, SIG_MEAS = 0.903, 0.0375      # the epsilon-blind ensemble, as booked
QUOTED_TARGET = 0.0115


def main() -> None:
    print("=" * 78)
    print("What width actually separates the census candidates")
    print("=" * 78)

    print(f"\n   in hand: c = {C_MEAS} +/- {SIG_MEAS}  (the epsilon-blind ensemble)")
    print("\n   candidate            value      distance from 9/10   sigma now")
    nine_ten = 9.0 / 10.0
    for name, v in CANDIDATES.items():
        d = abs(v - nine_ten)
        print(f"   {name:38s} {v:.5f}   {d:.5f}      {d/SIG_MEAS:.2f}")

    gap = nine_ten - 8.0 / 9.0            # the binding pair
    gap_far = 12.0 / 13.0 - nine_ten
    print(f"\n   the BINDING spacing is 9/10 vs 8/9 = {gap:.5f}")
    print(f"   (9/10 vs 12/13 = {gap_far:.5f}, twice as easy)")

    print(f"\n   the quoted target sigma_c <= {QUOTED_TARGET} buys:")
    print(f"     9/10 vs 8/9   : {gap/QUOTED_TARGET:.2f} sigma")
    print(f"     9/10 vs 12/13 : {gap_far/QUOTED_TARGET:.2f} sigma")
    print("   -- i.e. at the quoted width the charge-weighted candidate still")
    print("      sits one sigma away. That is not a separation; it is the")
    print("      width at which the two stop coinciding.")

    print("\n   what a genuine call costs (binding pair, 9/10 vs 8/9):")
    print("     level    sigma_c needed   sharpening vs now   data multiple")
    for lvl in (2.0, 3.0, 5.0):
        need = gap / lvl
        sharp = SIG_MEAS / need
        print(f"     {lvl:.0f} sigma      {need:.5f}          {sharp:5.1f}x"
              f"              {sharp**2:7.0f}x")

    print("\nVERDICT:")
    print("   THE RECORDED CLOSING MOVE DOES NOT CLOSE. sigma_c <= 0.0115 is")
    print("   the candidate SPACING, so it delivers a 1.0-sigma separation")
    print("   from the charge-weighted alternative — the alternative survives")
    print("   comfortably at that width. A 3-sigma call needs sigma_c <=")
    print(f"   {gap/3.0:.5f}, which is a {SIG_MEAS/(gap/3.0):.1f}x sharpening, not 3.3x, and")
    print(f"   because ensemble width falls as 1/sqrt(N) that is ~{(SIG_MEAS/(gap/3.0))**2:.0f}x the data,")
    print("   not ~11x. The 3.3x figure understates the cost of the closing")
    print("   move by an order of magnitude in width and two in sample.")
    print()
    print("   This does not change c's STATUS — it was already a counting")
    print("   assumption the framework does not force, and the ensemble")
    print("   already confirms without adjudicating. What changes is the")
    print("   cost of the adjudication: it is not nearly in reach, and any")
    print("   plan that treats sigma_c = 0.0115 as the finish line is")
    print("   planning to stop one sigma short of a decision.")
    print("=" * 78)


if __name__ == "__main__":
    main()
