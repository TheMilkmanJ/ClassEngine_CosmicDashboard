# Targeted docs queue — blocked lanes, hidden theory work, exploratory fronts (2026-08-06)

Purpose: consolidate the remaining real work inside the named docs, after the prose-sweep phase
stopped being the bottleneck.

## 1. Machine currency at queue time

Local machine:

- `dyad_mnu_bbnfix` — **running**; latest progress stamp `R−1 = 0.085619`, `N = 27525`,
  `t = 2026-08-05T22:03:22.458467`; checkpoint `converged: false`
- `cmp_lcdm_mnu_bbnfix` — **finished**; latest progress stamp `R−1 = 0.049324`, `N = 26294`,
  `t = 2026-08-05T11:52:10.194879`; checkpoint `converged: true`
- `cmp_prtoe_routeD` — **running**; latest progress stamp `R−1 = 0.257073`, `N = 11422`,
  `t = 2026-08-06T01:51:33.402664`; checkpoint `converged: false`

The shared `bbnfix` gate remains **REFUSED**. Authority:

- `working_logs/_runs/blocked_lane_bbnfix_20260805/REPORT.md`
- `working_logs/_runs/bbnfix_booking_20260806_053434/REPORT.md`

AWS nested sampling:

- `cmp_prtoe_dyad_ev.yaml` sampled-ε PolyChord leg is **live**
- no nested verdict is bookable yet
- repaired `cmp_lcdm_ev` twin worker is armed and waiting behind dyad

Authority:

- `working_logs/_runs/polychord_owner_followup_20260806/REPORT.md`

## 1a. Code-vs-theory audit — 2026-08-06

Authority note:

- `working_logs/_runs/docs_queue_20260806/C_CODE_THEORY_AUDIT.md`

Desk verdict:

- the C code matches the two theory/config lanes that are currently on disk
- the **public hard lane** is `use_dcdf + dcdf_dyad_link + screened/derived varying_me`
- the **current live AWS evidence lane** is the softer **sampled-ε** path:
  `use_dcdf + varconst_density_gate=yes + sampled varying_me`
- `use_prtoe` remains legacy scalar-tensor baggage only; it is not the public core

Consequence:

- **no restart is required** for the live AWS dyad PolyChord leg on code-vs-theory grounds
- the correct desk action is to keep sampled-ε and fixed/derived-ε lanes separated explicitly

## 2. Blocked top-level docs — real closure still owed

### `PRTOE_hubble_tension.md`

Still blocked on the live `bbnfix` pair. Safe desk work is only:

- keep the pair gate exact
- keep pre-bbnfix Laplace clearly labeled as pre-bbnfix
- keep nested status exact

Real closure path:

- dyad self-stop under `R−1 < 0.05`
- rerun booking script
- finish the AWS nested pair

### `PRTOE_neutrino_home.md`

Still blocked on the same `bbnfix` gate for joint `Sigma m_nu`, plus owner/external Fairbank hold.

Real closure path:

- same dyad book as above
- Fairbank / posting decision from owner

### `PRTOE_bigbang_no_singularity.md`

Still blocked on the bounce-turn construction:

- exterior `H_re`
- handover stress / junction law
- no desk-only bounce close

### `PRTOE_cosmic_magnetism.md`
### `PRTOE_igmf_helicity.md`

Still blocked on the T14 / IGMF sign lane:

- no production-grade sign close
- no external-grade verdict yet
- keep the lane frozen to the shared blocker card, not to narrative language

### `PRTOE_s8_growth.md`
### `PRTOE_s8_tension.md`

Still blocked on the S8 conversion lane:

- `conv_desi` posterior unproduced
- `routeD` live but not converged and not a substitute

### `PRTOE_galactic_atoms.md`
### `PRTOE_smbh_atoms.md`

Still blocked on the zon/onset mass lane:

- `zon_disp` not running
- no quotable `alpha_c` / `log10_zon` center
- no propagated measured mass posterior for the galactic / SMBH claims

## 3. Hidden theory work still sitting inside top-level docs

### `PRTOE_cosmological_constant.md`

Load-bearing owed object still present:

- unitarized `sigma sigma` amplitude at `lambda ~ 45.7` is **MISSING_INPUT**

This file is honest already; the remaining work is not prose.

### `PRTOE_me_mechanism_math.md`

Single named owed object still present:

- `ell_seed` — the seed correlation length inside the portal coherence volume

This is the one residual the file itself names.

### `PRTOE_coincidence_problem.md`

Still split correctly into:

- width derived
- occupancy open
- chain-level cycle selection open-blocked

No desk rewrite turns width into occupancy.

### `PRTOE_quantum_gravity.md`

Still carries real Goal-B residuals:

- Page dynamics open
- absolute SI `G` open
- nonlinear continuum Einstein / continuum limit open-theory

## 4. Exploratory — active fronts, not shelf clutter

### Highest-value active fronts

- `exploratory/PRTOE_hierarchy_problem.md`
  - host ontology / `alpha_c = 3 alpha` scale residual still open
- `exploratory/PRTOE_information_paradox.md`
  - Page-curve dynamics still open-blocked
- `exploratory/PRTOE_quantum_entanglement.md`
- `exploratory/PRTOE_quantum_superposition.md`
- `exploratory/PRTOE_quantum_tunneling.md`
  - Born value open-blocked; medium pair `r` and pair Hamiltonian are still missing inputs
- `exploratory/PRTOE_arrow_of_time.md`
- `exploratory/PRTOE_white_holes.md`
  - bounce turn / `H_re` family still open-blocked
- `exploratory/PRTOE_forced_combination.md`
  - Koide / family-ring closing chain still open-blocked
- `exploratory/PRTOE_light.md`
  - constituent-side EM / unification residuals still open-blocked

### Lower-priority exploratory maps / stubs

- `exploratory/PRTOE_astrochemistry.md`
- `exploratory/PRTOE_chaos_dynamics.md`
- `exploratory/PRTOE_laser_physics.md`

These are already honest: no registered prediction or script path yet.

## 5. What `#94` is

`#94` is the unfinished deep-audit queue, not a single physics claim.

Practical content:

- whole-file reads of remaining unread giant docs
- open-class audit for stale numbers / dead premises / claims outrunning evidence
- registry / failures-ledger burden not fully discharged

Current docket references:

- `ForGrok&Claude.md`
- `working_logs/_DOCKET_INDEX.md`

## 6. Safe next actions

Docs-side safe work:

1. keep machine currency exact
2. keep shared blocker cards exact
3. finish `#94` whole-file reads

Real closure work that docs cannot fake:

1. `dyad_mnu_bbnfix` book
2. `cmp_prtoe_dyad_ev` + `cmp_lcdm_ev` nested pair completion
3. bounce / `H_re`
4. T14 / IGMF sign
5. `conv_desi`
6. `zon_disp`

No prose-only pass closes any of those.

## 7. Desk stop update — 2026-08-06 02:42 MDT

Desk status at stop:

- current-surface routeD / bbnfix currency has been synced across the main shelf files
- sampled-ε AWS evidence wording has been separated from the fixed/derived-ε hard lane
- exploratory map/stub files that needed top-fences now carry them
- stale “cluster time only” language has been converted where it was still presenting as current

Current AWS wrinkle:

- the replacement-box dyad PolyChord process is still **up**
- watcher state is now **STALLED** rather than actively growing
- the repaired LCDM twin worker remains queued behind dyad
- this changes current-status wording, but it does **not** create a code-vs-theory restart obligation

Practical conclusion:

- the docs desk is at a safe stop for the **currency / wording / shelf-honesty** class
- remaining work is either:
  - real machine progress
  - real theory closure
  - or `#94` deep-audit reading
