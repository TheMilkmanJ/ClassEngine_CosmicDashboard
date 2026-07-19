# Circulation hold — the Fairbank note

*Internal. Not part of the letter. `PRTOE_fairbank_note_draft.md` is the letter and reads as
finished prose; everything about when to send it lives here.*

## Status: CLEARED to show, in person, as work in progress

Addressee confirmed: **William Fairbank**. The letter is being shown ahead of the evidence run by
the owner's decision. That is a coherent choice: nothing in it depends on the run except the H₀
figure, which the letter already carries as provisional in its own voice. Showing unfinished work
to a colleague and mailing a finished claim are different acts, and only the second needed a gate.

**What is still running.** PolyChord has been sampling since 2026-07-18, 400 live points, matched
to a ΛCDM twin so the evidence ratio is valid. As of 2026-07-19 it is ~24h in with no log(Z) yet.
The completion horizon is under review (task #99).

**The one thing not to do:** quote H₀ ≈ 69.9 as a final measured number anywhere it will be
recorded or repeated. In conversation, provisional is what the letter says and what it is.

## Why H₀ is provisional, in full

That figure was measured on chains predating the `YHe` correction, where the helium fraction fed to
the recombination code was ΛCDM's rather than the model's own, leaving n_e ∝ (1−Y_p) about 0.27% off
exactly where the H₀ mechanism operates, and the BBN prior blind the same way (undercharging the
model by ~1 χ²).

That defect was closed on 2026-07-17 (`fe8cd8f2`, 13 configs): the measured varying-m_e response is
now wired into both the `YHe` value and the BBN prior, and the running job carries it. Scored on the
model rather than ΛCDM the BBN prior now carries its own weight (χ² 0.31 → 1.31). What has not
happened is the re-measurement — the same wait as the evidence verdict, hence one gate rather than
two.

**Expect the number to move.** How far is unknown until the run reports — the correction acts on the
free-electron fraction in the damping tail, which is where the H₀ mechanism lives, so this is not a
place to assume the shift is negligible.

## Cleared

- **Citations** — checked against `BIBLIOGRAPHY.md` 2026-07-19. Three gaps found and closed:
  PArthENoPE (underwrites the deuterium theory error, and therefore whether the BBN joint reads
  p = 0.02 or p = 0.21), and arXiv 2606.06495 / 2508.09025 (the source for the 2–3.6σ varying-m_e
  preference the letter quotes).
- **The m_ββ window** — recomputed independently. The letter's terms (1.52, 2.67, 1.10) reproduce on
  m₁ = ρ_Λ¼ = 2.25 meV. The window is **[0.02, 5.3] meV**, not [0.04, 5.3]: the floor is
  anchor-dependent and nearly halves across the model's own 1.5% spread in the dark-energy scale.
- **The experiment overlay** — nEXO 4.7–20.3 meV, LEGEND-1000 9–21, CUPID 12–34, against a model
  ceiling of 5.30. Only nEXO overlaps, at 4.7–5.3 meV, ~10.8% of the model's phase space over flat
  Majorana phases.
- **The registry mismatch** — P-2026-012 does not say what the letter used to say it said. Left
  frozen; **ANN-2026-025** files the three drifts (causal arrow, MaVaN conditional, ordering not
  selected by that entry).
- **The distinctiveness question** — the sum is not testable (2.6 meV above the m₁ = 0 floor against
  ~20 meV planned resolution). The m_ββ structure is. The letter now says so itself, and carries the
  post-hoc flag on the branch-selecting mechanism.
- Every closed-form number in the letter is under regression in `scripts/audit_math_pass.py`.

## Before it goes out

1. The evidence verdict lands → replace the provisional H₀ with the measured one, and say what the
   run found either way.
2. Re-read the m_ββ floor section against whatever the dark-energy scale settles at — the floor
   vanishes above m₁ = 2.324 meV, and the highest recorded anchor (2.284) clears that by 1.7%.
3. If the ¹³⁶Xe matrix element firms up, the 4.7 meV nEXO reach and the ~11% overlap both move with
   it. Ask (c) puts that question to him directly; his answer should be folded back in.
