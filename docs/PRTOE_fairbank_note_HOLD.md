# Circulation hold — the Fairbank note

*Internal. Not part of the letter. `PRTOE_fairbank_note_draft.md` is the letter and reads as
finished prose; everything about when to send it lives here.*

## Status: HELD on one item

**The zero-parameter evidence verdict.** PolyChord has been sampling since 2026-07-18, 400 live
points, matched to a ΛCDM twin so the evidence ratio is valid. The completion horizon is itself
under review (task #99), so this may hold the letter for a long time. That is the honest
expectation rather than a delay.

## What the hold actually covers

**The H₀ number.** The letter quotes H₀ ≈ 69.9 as provisional. The reason it is provisional, in
full: that figure was measured on chains predating the `YHe` correction, where the helium fraction
fed to the recombination code was ΛCDM's rather than the model's own, leaving n_e ∝ (1−Y_p) about
0.27% off exactly where the H₀ mechanism operates, and the BBN prior blind the same way
(undercharging the model by ~1 χ²).

That defect was closed on 2026-07-17 (`fe8cd8f2`, 13 configs): the measured varying-m_e response is
now wired into both the `YHe` value and the BBN prior, and the running job carries it. Scored on
the model rather than ΛCDM the BBN prior now carries its own weight (χ² 0.31 → 1.31). What has not
happened is the re-measurement — which is the same wait as the evidence verdict, hence one gate
rather than two.

**Expect the number to move.** Nobody should quote 69.9 externally as final until the run reports.

## Cleared

- **Citations** — checked against `BIBLIOGRAPHY.md` on 2026-07-19. One gap: PArthENoPE, which
  underwrites the deuterium theory error and therefore the difference between the BBN joint reading
  p = 0.02 and p = 0.21. Added.
- **The m_ββ window** — recomputed independently; the letter's [0.04, 5.3] meV and
  (1.52, 2.67, 1.10) reproduce on m₁ = ρ_Λ¼ = 2.25 meV. Under regression in
  `scripts/audit_math_pass.py`.

## Before it goes out

1. The evidence verdict lands → replace the provisional H₀ with the measured one, and say what the
   run found either way.
2. Re-read the m_ββ floor section against whatever the dark-energy scale settles at — the floor
   vanishes above m₁ = 2.324 meV, and the highest recorded anchor (2.284) clears that by 1.7%.
3. Confirm the addressee's current institution and the nEXO barium-tagging context before sending.
