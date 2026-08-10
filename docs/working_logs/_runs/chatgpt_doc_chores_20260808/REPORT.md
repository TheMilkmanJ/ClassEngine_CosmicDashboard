# ChatGPT doc chores — 2026-08-08

## Scope

Substantive doc-currency pass only. No new MCMCs or PolyChord launches. No archive-log rewrites.
Goal: bring living docs into line with current machine truth:

- old-BAO production `bbnfix` pair is **BOOKED**
- booked old-BAO evidence class is **sample-covariance Laplace only**, not a nested-quality win
- DESI-DR2 bbnfix twins are **live and not bookable**
- gold DESI-DR2 PolyChord is a **four-leg design**, **not launched**

## Authority used

- old-BAO booking receipt:
  `docs/working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md`
- sample-cov Laplace:
  `docs/working_logs/_runs/laplace_docs_chains_bbnfix_20260808/REPORT.md`
- DESI-DR2 live state:
  `docs/working_logs/_runs/desidr2_ondemand_launch_20260808/STATUS_20260808T1856Z.md`
- gold DESI-DR2 nested design:
  `docs/working_logs/_runs/gold_desidr2_polychord_20260808/REPORT.md`
- quota state:
  `docs/working_logs/_runs/quota_increase_20260808/REPORT.md`

## Numbers stamped

### Booked old-BAO pair

- `dyad_mnu_bbnfix`: `R−1 = 0.048118`, `N = 37605`, `converged: true`
- `cmp_lcdm_mnu_bbnfix`: `R−1 = 0.049324`, `N = 26294`, `converged: true`
- dyad GetDist: `H0 = 70.052 ± 0.716053`, `m_ncdm = 0.0671427 ± 0.0582684`, `S8 = 0.821363 ± 0.00965247`
- lcdm GetDist: `H0 = 68.3453 ± 0.343404`, `m_ncdm = 0.0192058 ± 0.0173502`, `S8 = 0.823628 ± 0.0081253`

### Evidence honesty on booked old-BAO pair

- `ΔlnZ_Laplace = +0.211493`
- `Δ(min −logpost) = -2.962700`
- `cond(Σ) ~ 10^8` on both legs

### Current live DESI-DR2 MCMC state

- dyad: `R−1 = 0.108745`, `N = 21827`, `converged: false`
- lcdm: `R−1 = 0.140148`, `N = 22848`, `converged: false`

### Current nested-design state

- four configs on disk:
  - `dyad_mnu_bbnfix_desidr2_ev.yaml`
  - `cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml`
  - `dyad_mnu_bbnfix_desidr2_trgb_ev.yaml`
  - `cmp_lcdm_mnu_bbnfix_desidr2_trgb_ev.yaml`
- launch state: **designed, not launched**
- quota request to `512` vCPU: **CASE_OPENED**

## Files touched

### Core current-state docs

- `docs/PRTOE_CHAIN_TABLES.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_honest_status.md`
- `docs/PRTOE_hubble_tension.md`
- `docs/PRTOE_DOMAIN_COVERAGE.md`
- `docs/PRTOE_INDEX.md`
- `docs/PRTOE_DEPENDENCY_TREE.md`
- `docs/PRTOE_READERS_GUIDE.md`
- `docs/PRTOE_CODE_MANIFEST.md`
- `docs/PRTOE_THREE_EQUATIONS.md`
- `docs/PRTOE_THE_AMPLITUDE.md`
- `docs/PRTOE_CMB_map.md`
- `docs/PRTOE_MATH_SPINE.md`

### Neutrino / Fairbank surfaces

- `docs/PRTOE_neutrino_home.md`
- `docs/PRTOE_neutrino_sector.md`
- `docs/PRTOE_fairbank_note_draft.md`

### Exploratory / map surfaces with current-facing machine language

- `docs/PRTOE_fingerprint_lattice.md`
- `docs/exploratory/PRTOE_INTERACTION_ATLAS.md`
- `docs/exploratory/PRTOE_math_story.md`
- `docs/exploratory/PRTOE_the_great_chain.md`
- `docs/PRTOE_DERIVATION_HUNT.md`

### Owner-facing docs

- `ForJustin/STATUS_CONTINUE.md`
- `ForJustin/ARXIV_OWNER_CHECKLIST.md`
- `ForJustin/14_where_the_model_stands.md`

## What remains open

- booked old-BAO pair is real, but evidence remains **Laplace-marginal**
- DESI-DR2 MCMC twins are still **not bookable**
- gold DESI-DR2 nested evidence remains **not launched**
- Route-D remains **OPEN-MACHINE**
- Stage B forward-table publication remains separate from Stage A booking and still needs the owner/red path

## Historical text intentionally left in place

These were not scrubbed out if they were explicitly historical and already fenced:

- historical pre-bbnfix `+2.635` sections
- dated trigger stamps in owner notes
- dated exploratory / working-log narrative blocks

The criterion for leaving them was: historical section, explicit date/context, and no present-tense
claim that contradicts current machine truth.

## Deferred on purpose

- archive `working_logs/` refuse cards and historical run receipts
- paste files / handoff files that are explicitly instructions or historical snapshots
- style-only cleanup

## Sidecar compute status

The full finite-difference Hessian-Laplace run requested on `docs/chains` is still running:

- command:
  `python3 scripts/bbnfix_hessian_laplace.py --chain-dir docs/chains --which both --out docs/working_logs/_runs/credibility_diagnostics_20260808/hessian_laplace.json`
- PID at last check: `518375`
- status: alive, CPU-bound
- output JSON: not written yet at the time of this receipt

This sidecar compute did **not** change any booked physics claim during this docs pass.
