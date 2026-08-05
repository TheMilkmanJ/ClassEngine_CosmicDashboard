# Major-doc arXiv matrix (top-level shelf only, 2026-08-05)

Purpose: classify the current top-level `docs/PRTOE_*.md` shelf by what should happen next in the
arXiv-prep lane.

Scope:
- top-level `docs/PRTOE_*.md` only
- excludes `docs/exploratory/`, `docs/historical_*`, `docs/arXivReady/`, `papers/`, and `working_logs/`
- current live disk inventory: **61** files

Status rules:
- `ARXIV_READY`: the file already has a clean ship path as a narrow package or source note; only
  external posting / endorsement gates remain
- `BLOCKED`: a public-paper path could exist, but real machine / theory / external blockers still
  prevent honest promotion now
- `EXPLORATORY`: keep on the shelf as corpus / ledger / hub / duplicate / synthesis; do not
  promote this file directly even if parts of it are complete

Non-negotiable interpretations:
- file completion is **not** paper readiness
- extracted paper slices do **not** auto-promote the parent hub
- `CORPUS_ONLY` in the older candidacy audit maps to `EXPLORATORY` here
- `NOT_READY` in the older candidacy audit maps to `BLOCKED` here

## Counts

| status | count | meaning |
|---|---:|---|
| `ARXIV_READY` | 4 | ship path exists already; external gate only |
| `BLOCKED` | 20 | real blocker still stands |
| `EXPLORATORY` | 37 | keep on shelf; not direct paper targets |
| **total** | **61** | current top-level disk inventory |

## Matrix

| file | status | why it sits there now | next action / narrowing rule |
|---|---|---|---|
| `PRTOE_CHAIN_TABLES.md` | `BLOCKED` | live chain honesty board; bbnfix pair still refused | wait for both legs to book; see `blocked_lane_bbnfix_20260805/REPORT.md`; do not paper live diagnostics |
| `PRTOE_CMB_map.md` | `EXPLORATORY` | six-spectra scorecard, not a single claim | keep as map only |
| `PRTOE_CODE_MANIFEST.md` | `EXPLORATORY` | pipeline inventory / honesty surface | keep as ledger |
| `PRTOE_DEPENDENCY_TREE.md` | `EXPLORATORY` | living claim-conditionality map | keep as ledger |
| `PRTOE_DERIVATION_HUNT.md` | `EXPLORATORY` | registry of underived numbers | keep as hunt ledger, not a paper |
| `PRTOE_DOMAIN_COVERAGE.md` | `EXPLORATORY` | domain census / jurisdiction map | keep as shelf map |
| `PRTOE_FAILURES_LEDGER.md` | `EXPLORATORY` | graveyard / discipline object | keep as ledger |
| `PRTOE_H0_CEILING.md` | `EXPLORATORY` | companion formula; rejected as standalone paper | keep only as support note |
| `PRTOE_INDEPENDENCE_AUDIT.md` | `EXPLORATORY` | meta-audit of claim dependence | keep as process discipline |
| `PRTOE_INDEX.md` | `EXPLORATORY` | shelf map | keep as index |
| `PRTOE_LV_pricing.md` | `EXPLORATORY` | corpus-only model certificate; framework-independent extract fails | do not invent an LV note |
| `PRTOE_MATH_SPINE.md` | `EXPLORATORY` | derivation hub; only the kination slice ships separately | keep hub; ship only extracted narrow notes |
| `PRTOE_PREREGISTERED_PREDICTIONS.md` | `EXPLORATORY` | registry, not a derivation paper | keep as registry |
| `PRTOE_READERS_GUIDE.md` | `EXPLORATORY` | orientation object | keep as guide |
| `PRTOE_READERS_RISK.md` | `EXPLORATORY` | risk / honesty decoder, not a paper | keep as guide |
| `PRTOE_REFEREE_CALENDAR.md` | `EXPLORATORY` | process calendar | keep as ledger |
| `PRTOE_THE_AMPLITUDE.md` | `EXPLORATORY` | broad conditional stack with provisional production fit | only extract if a narrow independent slice closes later |
| `PRTOE_THREE_EQUATIONS.md` | `EXPLORATORY` | front-door multi-claim hub | keep as elevator / overview only |
| `PRTOE_TRIALS_FACTOR.md` | `EXPLORATORY` | meta-discipline file | keep as audit |
| `PRTOE_baryogenesis.md` | `EXPLORATORY` | fuller sector note; forward `omega_J` micro input still open | keep on shelf unless a narrow closed subclaim emerges |
| `PRTOE_bbn_witness.md` | `ARXIV_READY` | source note for `papers/bbn-eps-bound/`; package is clean and narrow | external gate only; optional dense full-window scan remains non-blocking; full D/H fork stays on shelf in `../blocked_lane_deuterium_fork_20260805/REPORT.md` |
| `PRTOE_bigbang_no_singularity.md` | `BLOCKED` | bounce dynamics still open theory | close bounce dynamics first or keep blocked |
| `PRTOE_blackholes_no_singularity.md` | `EXPLORATORY` | structural synthesis / conditional hub | keep as shelf synthesis |
| `PRTOE_build_2loop_Veff_spec.md` | `EXPLORATORY` | negative build record tied to framework `T_c` story | keep as corpus record |
| `PRTOE_cmb_anomalies.md` | `BLOCKED` | BipoSH data application still owed | wait for the shared BipoSH referee; see `../blocked_lane_biposh_axis_20260805/REPORT.md`; do not promote now |
| `PRTOE_coincidence_problem.md` | `EXPLORATORY` | width result paid, occupancy not | keep as honesty split, not a paper |
| `PRTOE_cosmic_magnetism.md` | `BLOCKED` | real open theory debt remains in RM / amplitude lane | close the missing formula layer first |
| `PRTOE_cosmological_constant.md` | `BLOCKED` | full stack still depends on lattice `tau` referee and wider chain | keep blocked until the stack closes honestly |
| `PRTOE_cyclic_torus_genesis.md` | `BLOCKED` | open theory / story-grade sector, not closed science | keep blocked until mechanism debts close |
| `PRTOE_dcdf_superfluid.md` | `EXPLORATORY` | identity file with residuals named open | keep as identity note |
| `PRTOE_deuterium_row.md` | `BLOCKED` | D/H fork still open externally | wait on `../blocked_lane_deuterium_fork_20260805/REPORT.md` |
| `PRTOE_direct_detection.md` | `EXPLORATORY` | forced-null certificate given the constitution | keep as corpus certificate |
| `PRTOE_dyad_gas.md` | `EXPLORATORY` | identity file; UV / `T_c` path still open | keep as identity note |
| `PRTOE_fairbank_note_draft.md` | `EXPLORATORY` | duplicate ship path; `neutrino-mbb` already owns the public claim | do not invent second TeX / second posting path |
| `PRTOE_fingerprint_lattice.md` | `EXPLORATORY` | capstone multi-messenger correlation file; too wide for one paper | keep as capstone shelf note; axis-family blocker lives in `../blocked_lane_biposh_axis_20260805/REPORT.md` |
| `PRTOE_galactic_atoms.md` | `BLOCKED` | machine-gated by `alpha_c` / GC budget | wait for the machine closure; see `blocked_lane_zondisp_20260805/REPORT.md` |
| `PRTOE_granule_scoping.md` | `BLOCKED` | sims not started / machine debt real | keep blocked until sim outputs exist |
| `PRTOE_gravitational_waves.md` | `EXPLORATORY` | structural-null certificate with open helicity link | keep as corpus certificate |
| `PRTOE_honest_status.md` | `EXPLORATORY` | internal board / private honesty surface | keep internal |
| `PRTOE_hubble_tension.md` | `BLOCKED` | evidence / booking still chained to live bbnfix gate | wait for booked pair; see `blocked_lane_bbnfix_20260805/REPORT.md`; no paper from provisional chain state |
| `PRTOE_igmf_helicity.md` | `BLOCKED` | production four-branch sign NOT BOOKABLE; `f = −1` branches NOT_MEASURED below the instrument's 0.15 floor, so only two-branch `f = +1` evidence exists | make the `f = −1` branches form a ring and re-run at matched `t`; see `../blocked_lane_t14_igmf_sign_20260805/REPORT.md`. Restating the two-branch result does not produce a four-branch sign |
| `PRTOE_indirect_detection.md` | `EXPLORATORY` | forced-null certificate given the constitution | keep as corpus certificate |
| `PRTOE_induced_gravity.md` | `EXPLORATORY` | broad attach file; only the supertrace algebra slice ships separately | keep as attach hub, not a standalone paper |
| `PRTOE_inflation_replacement.md` | `BLOCKED` | bounce / tilt residuals still open | close theory debts first |
| `PRTOE_koide_relation.md` | `BLOCKED` | open theory in pacing / sign-chain / #101/#102 lane | close the derivation debt first |
| `PRTOE_lattice_note.md` | `ARXIV_READY` | source note for `papers/lattice-tc-gap/`; package is already narrow and clean | external gate only |
| `PRTOE_lowell_anomalies.md` | `BLOCKED` | BipoSH data application is still external | wait for the shared BipoSH referee; see `../blocked_lane_biposh_axis_20260805/REPORT.md` |
| `PRTOE_lss_parity.md` | `BLOCKED` | external state is favorable but not fully closed | wait for `../blocked_lane_lss_parity_20260805/REPORT.md` |
| `PRTOE_me_mechanism_math.md` | `EXPLORATORY` | mechanism companion; public radio / BBN slices already extracted elsewhere | keep as support math note |
| `PRTOE_neutrino_home.md` | `BLOCKED` | joint `Sigma m_nu` story still machine-gated; Fairbank path on hold | wait for booked joint fit; see `blocked_lane_bbnfix_20260805/REPORT.md`; do not promote the home file |
| `PRTOE_neutrino_sector.md` | `ARXIV_READY` | source note for `papers/neutrino-mbb/`; package exists already | external gate / owner Fairbank hold only |
| `PRTOE_quantum_gravity.md` | `EXPLORATORY` | full QG hub is corpus-only; only supertrace algebra is shipped | keep as hub; do not paper the whole file |
| `PRTOE_quartet_clock.md` | `BLOCKED` | machine debt remains with `zon_disp` parked | wait for machine closure; see `blocked_lane_zondisp_20260805/REPORT.md` |
| `PRTOE_radio_lattice.md` | `ARXIV_READY` | source note for `papers/radio-lattice/`; package is already clean | external gate only |
| `PRTOE_s8_growth.md` | `BLOCKED` | `conv_desi` / routeD / matched-lensing debt still open | wait for machine output; see `blocked_lane_s8_conversion_20260805/REPORT.md` |
| `PRTOE_s8_tension.md` | `BLOCKED` | same machine debt as growth companion | wait for machine output; see `blocked_lane_s8_conversion_20260805/REPORT.md` |
| `PRTOE_small_scale_structure.md` | `EXPLORATORY` | consolidation of recorded results, not a new claim paper | keep as assembly note |
| `PRTOE_smbh_atoms.md` | `BLOCKED` | machine-gated by `alpha_g` chain | wait for the machine closure; see `blocked_lane_zondisp_20260805/REPORT.md` |
| `PRTOE_stability.md` | `EXPLORATORY` | model certificate, not standalone public claim | keep as corpus certificate |
| `PRTOE_strong_cp.md` | `EXPLORATORY` | complete abstention; not a paper | keep as jurisdiction note |
| `PRTOE_v4_dCDF_derivation.md` | `EXPLORATORY` | pointer / lineage object, not a standalone note | keep as breadcrumb only |

## Immediate action queue

### `ARXIV_READY`

- `PRTOE_bbn_witness.md` -> `papers/bbn-eps-bound/`
- `PRTOE_lattice_note.md` -> `papers/lattice-tc-gap/`
- `PRTOE_neutrino_sector.md` -> `papers/neutrino-mbb/`
- `PRTOE_radio_lattice.md` -> `papers/radio-lattice/`

These are not desk-clean because of external gates, but they are the only current top-level docs
that already map to clean ship artifacts.

### `BLOCKED`

Work here is real science / machine / external closure, not shelf polishing. Do not pretend a docs
pass cures these.

### `EXPLORATORY`

Keep these as shelf surfaces, ledgers, or broader hubs. If a narrow exportable claim emerges, cut a
new package from it rather than promoting the whole hub.

## Important omissions from the top-level-doc view

- `papers/supertrace-note/` is already **SHIPPED**, but its public artifact lives under `papers/`,
  not as a top-level `docs/PRTOE_*.md`.
- `papers/kination-tracking-note/` is **READY_PACKAGE**, but it is an extracted slice from
  `PRTOE_MATH_SPINE.md`, not the full spine file.
- Everything under `docs/exploratory/` remains outside this matrix and should be treated as
  exploratory unless promoted by a separate narrowing pass.
