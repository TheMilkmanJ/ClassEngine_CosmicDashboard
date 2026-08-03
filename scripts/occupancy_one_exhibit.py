"""occupancy_one_exhibit — task #15's last gate: the identification argued and data-locked (2026-07-28).

THE IDENTIFICATION DEMANDED (Addendum 11)
  The erasure channel that lands p = g_scr/4π needs exactly ONE partner
  quantum per substructure cell.  The corpus's occupancy-one principle
  states this for the vacuum's coherence cells (one binding quantum per
  cell — the ρ_Λ counting, argument-grade in its own file, §4).  The gate:
  does the same count govern the network's substructure cells?

(A) THE ARGUMENT TRANSFERS — same two pinches, marginal scale for binding scale
  The vacuum argument pinches occupancy from both sides: ≥ 1 by stability
  (every binding mode holds its quantum or there is no condensate) and
  ≤ 1 by coherence (the cell IS the mode's own wavelength; a second
  quantum is an excitation, not the state).  At the cascade's cutoff the
  same two pinches close: the cutoff scale is the MARGINAL-SURVIVAL scale
  (cascading-in balances erasure-out), so the mode holds its quantum or
  the structure is not there (≥ 1), and the cell is again the mode's own
  wavelength, so a second quantum is an excitation the cascade immediately
  passes down (≤ 1).  Stated difference, named: the vacuum argument runs
  in the ground state; the cutoff is a driven steady state at
  marginality — the transfer inherits the original's own grade
  (argument-grade), no more.

(B) THE COUNT IS ALREADY MEASURED — the data lock
  If the partner count were N ≠ 1, the per-vertex factor would be
  N·g_scr/4π and the amplitude's closed form would read
  A_s = (N·α_c/4πk)³.  The recorded concordance between the closed form
  and the measured amplitude therefore PINS N:
      N = (A_s,measured / A_s,closed)^{1/3}
  computed below from the recorded numbers — landing at 1 to the
  half-percent level.  The identification is not only argued; the sky has
  already weighed the count.

GRADE RULE
  (A) inherits argument-grade from the occupancy file's own §4, with its
  owned BEC-side assumption and its named referee (P-2026-048).  (B) is
  arithmetic on recorded numbers.  Together with Addendum 11's channel,
  the keystone's normalization is DERIVED AT CANDIDATE GRADE with three
  live referees: P-2026-048 (the crossover number), #16's T/μ at gap
  formation, and the concordance k at chain convergence.
"""
from __future__ import annotations

import math

ALPHA_C = 3.0 / 137.036
K_CLOSED = math.log(1.0 + math.pi / (2 * ALPHA_C)) / math.pi
AS_CLOSED = (ALPHA_C / (4 * math.pi * K_CLOSED)) ** 3
AS_MEASURED = 2.100e-9          # Planck 2018: ln(10^10 As) = 3.044 ± 0.014
AS_MEAS_SIG = 0.014             # fractional (σ of ln As)


def main() -> None:
    print("=" * 78)
    print("Occupancy-one on the substructure: argued, and already measured")
    print("=" * 78)

    print("\nA. the argument transfers (grade inherited, difference named):")
    print("   ≥ 1: the cutoff is the marginal-survival scale — the mode holds")
    print("        its quantum or the structure is not there;")
    print("   ≤ 1: the cell is the mode's own wavelength — a second quantum is")
    print("        an excitation the cascade immediately passes down;")
    print("   difference: ground state (vacuum) vs driven marginal steady state")
    print("   (cutoff) — argument-grade, exactly as the source file grades itself.")

    n_hat = (AS_MEASURED / AS_CLOSED) ** (1.0 / 3.0)
    n_sig = AS_MEAS_SIG / 3.0
    print(f"\nB. the data lock:")
    print(f"   A_s closed form (k = {K_CLOSED:.5f}):  {AS_CLOSED:.4e}")
    print(f"   A_s measured (Planck 2018):          {AS_MEASURED:.4e} ± {100*AS_MEAS_SIG:.1f}%")
    print(f"   N = (measured/closed)^(1/3) = {n_hat:.4f} ± {n_sig:.4f}")
    print(f"   ⟹ the partner count is 1 within {abs(n_hat-1)/n_sig:.1f}σ, pinned")
    print(f"   at the half-percent level. A count of 2 is excluded at "
          f"{(2**(1)-1)/ (3*n_sig):.0f}σ-class")
    print("   (N enters cubed; even N = 1.05 would sit ~10σ out).")

    print("\nVERDICT: the keystone's normalization is DERIVED AT CANDIDATE GRADE —")
    print("   channel (pairwise screened de-excitation, Addendum 11) + count")
    print("   (occupancy-one: argued by the same two pinches at the marginal")
    print("   scale, and measured at N = 1 to half a percent by the amplitude")
    print("   concordance) + measure (unit s-wave, contact-class exchange).")
    print("   Live referees, named: P-2026-048 (the BEC-side crossover number),")
    print("   #16's T/μ at gap formation, and the concordance k at chain")
    print("   convergence. The keystone promotes; its kills stay armed.")
    print("=" * 78)

    assert abs(AS_CLOSED - 2.0807e-9) / 2.0807e-9 < 0.001
    assert abs(n_hat - 1.0) < 2 * n_sig
    assert n_sig < 0.006


if __name__ == "__main__":
    main()
