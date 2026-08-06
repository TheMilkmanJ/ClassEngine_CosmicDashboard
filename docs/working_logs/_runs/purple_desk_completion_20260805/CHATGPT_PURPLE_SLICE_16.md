# ChatGPT purple slice 16 - sigma-mnu surface freeze + bbnfix diag portability (2026-08-06)

Purpose: do one owner/process attack and one machine/tooling attack that were both still safely
actionable without inventing new science.

## Lane A - owner/process inconsistency

Problem:

- forward-facing shelf files were split between bare `61.3 meV` and bare `61.4 meV` for the same
  neutrino-floor relation
- that is a process/surface inconsistency, especially when the number appears in falsifier clauses
  and referee-facing summaries

What was frozen:

- public prose form: `Σm_ν ≈ 61.35 meV, normal ordering`
- exact public band when the number itself matters: `Σm_ν = 61.34–61.37 meV`

Authority report added:

- `docs/working_logs/_runs/sigma_mnu_public_form_20260806/REPORT.md`

Forward-facing files normalized:

- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_CODE_MANIFEST.md`
- `docs/PRTOE_cosmological_constant.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`
- `docs/PRTOE_DEPENDENCY_TREE.md`
- `docs/PRTOE_THE_AMPLITUDE.md`
- `docs/PRTOE_DERIVATION_HUNT.md`
- `docs/PRTOE_DOMAIN_COVERAGE.md`
- `docs/PRTOE_THREE_EQUATIONS.md`
- `docs/PRTOE_dyad_gas.md`
- `docs/PRTOE_koide_relation.md`
- `docs/PRTOE_fairbank_note_draft.md`
- `docs/PRTOE_neutrino_sector.md`
- `docs/PRTOE_MATH_SPINE.md`

Scope rule:

- no booked-posterior promotion
- no registry / ID decisions
- no historical-log rewrite

## Lane B - machine/tooling blocker

Problem:

- `python3 scripts/bbnfix_mcmc_watch_diag.py` hard-failed in the base environment with
  `ModuleNotFoundError: No module named 'numpy'`
- that blocked direct inspection of the live pair unless extra packages were installed

What changed:

- `scripts/bbnfix_mcmc_watch_diag.py` now computes its crude parameter R−1 in pure Python and no
  longer depends on `numpy` just to start

Direct test after patch:

- `python3 scripts/bbnfix_mcmc_watch_diag.py`
- result: script now runs and reports both legs, chain growth, crude parameter R−1, and bookable
  status
- `GetDist` is still absent in this environment, but that failure is now non-fatal and clearly
  labeled as diagnostic-only

Verified machine state from the tested script:

- `dyad_mnu_bbnfix`
  - progress: `R−1 = 0.060201`, `N = 26135`, `converged: false`
  - chain rows are still growing (`[8901, 8841, 8974]` at test time)
  - bookable leg: `False`
- `cmp_lcdm_mnu_bbnfix`
  - progress: `R−1 = 0.049324`, `N = 26294`, `converged: true`
  - bookable leg: `True`

Direct booking gate re-check:

- `python3 scripts/book_bbnfix_when_ready.py`
- latest refuse card on disk:
  `docs/working_logs/_runs/bbnfix_booking_20260806_001856/REPORT.md`
- result unchanged: `REFUSED`

Shared blocker audit refreshed:

- `docs/working_logs/_runs/blocked_lane_bbnfix_20260805/REPORT.md`

## What this slice did not do

- it did not open the bbnfix gate
- it did not convert live chain peeks into bookable H₀ / Σm_ν / S₈
- it did not resolve registry decisions
- it did not touch owner-only posting choices

## Review request for Claude

Please verify:

1. the Σm_ν normalization pass uses one surface form consistently without changing scientific
   content
2. the new authority report is coherent with the already-recorded anchor ranges
3. `scripts/bbnfix_mcmc_watch_diag.py` now runs in the base environment without `numpy`
4. the refreshed bbnfix blocker audit still matches the direct booking script output
