# Circulation hold — the Fairbank note

*Internal. Not part of the letter. `PRTOE_fairbank_note_draft.md` is the letter and reads as
finished prose; everything about when to send it lives here.*

## Status: CLEARED to show, in person, as work in progress

Addressee confirmed: **William Fairbank**. The letter is being shown ahead of a durable evidence
verdict by the owner's decision. That is a coherent choice: nothing in it depends on that verdict
except the H₀ figure, which the letter already carries as provisional in its own voice. Showing
unfinished work to a colleague and mailing a finished claim are different acts, and only the second
needed a gate.

**What carries the evidence verdict now.** Nested sampling (PolyChord, `cmp_prtoe_fixed`) was
ended on 2026-07-20 after ~48 h with no log(Z) — not stalled, just unaffordable on this hardware
(~9.8 h per nested iteration; first checkpoint ~163 days). Archived at
`chains/_archive_polychord_ended_20260720_0915/`. The registered thresholds still stand, but they
are graded against the standing Laplace-from-MCMC ΔlnZ until cluster time makes nested sampling
affordable. The MCMC chains that feed that estimate are therefore the critical path, not a side
referee.

**The one thing not to do:** quote H₀ ≈ 69.9 as a final measured number anywhere it will be
recorded or repeated. In conversation, provisional is what the letter says and what it is.

## Why H₀ is provisional, in full

That figure was measured on chains predating the `YHe` correction, where the helium fraction fed to
the recombination code was ΛCDM's rather than the model's own, leaving n_e ∝ (1−Y_p) about 0.27% off
exactly where the H₀ mechanism operates, and the BBN prior blind the same way (undercharging the
model by ~1 χ²).

That defect was closed on 2026-07-17 (`fe8cd8f2`, 13 configs): the measured varying-m_e response is
now wired into both the `YHe` value and the BBN prior, and the live MCMC configurations carry it.
Scored on the model rather than ΛCDM the BBN prior now carries its own weight (χ² 0.31 → 1.31).
What has not happened is the re-measurement — the same wait as the evidence verdict, hence one gate
rather than two.

**Expect the number to move.** How far is unknown until the run reports — the correction acts on the
free-electron fraction in the damping tail, which is where the H₀ mechanism lives, so this is not a
place to assume the shift is negligible.

## Cleared

- **Citations** — checked against `BIBLIOGRAPHY.md` 2026-07-19. Three gaps found and closed:
  PArthENoPE (underwrites the deuterium theory error, and therefore whether the BBN joint reads
  p = 0.02 or p = 0.21), and arXiv 2606.06495 / 2508.09025 for the varying-m_e support.
  **Corrected 2026-07-20 — that second citation did not say what it was cited for.** The letter
  read "varying-m_e preferred at 2–3.6σ by other groups", and neither paper supports it:
  arXiv:2508.09025's own number is m_e/m_e₀ = 1.0081 ± 0.0046, a **1.8σ** preference, and
  arXiv:2606.06495 quotes no significance and concludes the *opposite* — that varying m_e cannot
  fully resolve the tension once DESI DR2 BAO is added. The string "2.5–3.6σ" lives verbatim in a
  third paper (arXiv:2607.13282) as the **residual tension left over** by the best-performing
  models. A leftover was being quoted as a preference. The letter now gives Hart & Chluba's 3.5σ
  and the recent 1.8σ separately, and states that this mechanism class is outscored by early dark
  energy on the field's own common-framework comparison. **Check any remaining citation in the
  letter against its abstract, not against a doc that quotes it.**
- **The m_ββ window** — recomputed independently. The letter's terms (1.52, 2.67, 1.10) reproduce on
  m₁ = ρ_Λ¼ = 2.25 meV, and the window is **[0.04, 5.3] meV**. An earlier revision of this file
  carried it as [0.02, 5.3] on the grounds that the floor nearly halves across a 1.5% spread in the
  dark-energy scale. **That spread is not real.** Its top end, 2.2842 meV, is the value produced by
  the T_c = 179 keV route, and the failures ledger retires that T_c as the observation-inverted
  176.32 keV rounded up — recording in terms that the "+1.5%" is *the rounding*, not a sourced
  spread. The live uncertainty on ρ_Λ¼ is **0.449%**: Planck's 1.80% on ρ_Λ, quartered by the fourth
  root. Across that range the floor runs 0.050 → 0.038 meV and the ceiling moves 0.28%, so the
  window rounds to [0.04, 5.3] and the ceiling — which every conclusion turns on — is stable.
  The derived anchor 2.2599 sits +0.44% from the observed value, i.e. inside 1σ, and 2.78% below the
  2.324 meV threshold where the floor would vanish, which is 6.2σ away. Harness checks all of it.
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

## Found 2026-07-19, after the audit — read before describing the runs
### Operational snapshot (refreshed 2026-07-21)

**Which jobs are live, as of 2026-07-21.** Nested sampling is **not** live — ended and archived
2026-07-20 (see above). The live MCMC work is: `cmp_prtoe_conv_desi` (running; latest R−1 still
tens against a 0.1 stop — not near convergence), `cmp_prtoe_zon_disp` (running after a 07-20
relaunch; still far from convergence), and `dyad_mnu` (the healthy control, R−1 ~0.14).
`cmp_prtoe_routeD` was relaunched 07-20 on the corrected sampler but is currently stopped
(process state T) with no R−1 row yet; do not describe it as converging until it is running again
and R−1 falls. `twist` and `cmp_prtoe_zon` remain stopped.

**What to say if the runs come up.** The nested evidence number is not coming on this hardware.
The standing instrument is Laplace-from-MCMC, and that estimate is only as good as the chains that
feed it. Several of those chains previously collapsed under Cobaya's default
`learn_proposal_Rminus1_max_early = 30`, which let each chain learn a proposal covariance while
R−1 sat at 8–27 — from a chain that had never converged — shrinking the step size until the chain
stopped exploring. The 07-20 relaunches seed the covariance at physical widths and only learn from
a better-converged chain; **the step-size repair is measured, the convergence claim is not yet
proven**. The safe description is that the evidence comparison is carried by Laplace pending
cluster time for nested sampling, and the MCMC referees are being repaired, not that they are
converging.

**The graded configuration is off the model's onset identity.** It freezes z_on = 3.5619×10⁷ where
the identity is 4.03×10⁷ — 0.053 dex, which is a 28% difference in the dark fluid mass, and that
mass is pinned independently by ξ = 402 AU, the Schive core radii, and the superradiance window.
Laplace and any future nested run on this config therefore grade a point near the model, not the
model's stated configuration. The letter now says so; see `ForJustin/07-zon-two-values.md` for the
three options.

## Before it goes out

1. A durable evidence verdict lands (nested on cluster time, or a Laplace estimate fed by
   converged chains) → replace the provisional H₀ with the measured one, and say what the
   comparison found either way.
2. Re-read the m_ββ floor section against whatever the dark-energy scale settles at — the floor
   vanishes above m₁ = 2.324 meV, and the derived anchor sits 2.78% below that, or 6.2σ on the
   observation's own error. The floor thins across the range the scale is known to but does not
   vanish inside it. If the anchor moves materially, this section is the first thing to recompute.
3. If the ¹³⁶Xe matrix element firms up, the 4.7 meV nEXO reach and the ~11% overlap both move with
   it. Ask (c) puts that question to him directly; his answer should be folded back in.
