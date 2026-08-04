# Leftover formulable-script sweep

**Stamp:** 2026-08-04  
**Outdir:** `docs/working_logs/_runs/desk_compute_full_20260804/leftover/`  
**Runner:** `desk_compute_all_safe.run_one` pattern (OMP=1, timeout 120s default)  
**Fences held:** NO FABRICATIONS · No PolyChord · No cobaya.run · No book_bbnfix · No make_getdist force · Live MCMCs left alone  

**Rule:** exit 0 ≠ physics PASS. Token `PASS`/`FAIL` in logs is not a shelf COMPLETE. No living-shelf edits in this wave.

---

## 1. Inventory vs `desk_compute_all_safe --list`

| bucket | n |
|---|---:|
| `scripts/*.py` total | **385** |
| Covered by desk packs (unique scripts) | **98** |
| Fence / deny excluded from leftover pool | **10** |
| Leftover pool (not pack-covered, not fence) | **277** |
| **Ran this sweep (cap 40)** | **40** |
| **Skipped this sweep** (leftover pool − ran) | **237** |

Packs covered (for diff): `arithmetic`, `bounce`, `koide`, `baryo_rm`, `hierarchy`, `page_instrument`, `quantum_residual`, `alpha_amp`, `tests_analytic`, `current_core` (see parent `orchestrator.log` / pack SUMMARYs).

### Fence exclusions (n=10)

| script | why |
|---|---|
| `book_bbnfix_when_ready.py` | book* / DENY_SUBSTR |
| `finalize_h0_at_convergence.py` | finalize_h0* fence |
| `make_getdist_tables.py` | make_getdist* fence |
| `arxiv_package_audit.py` | arxiv_* / DENY |
| `bbnfix_mcmc_watch_diag.py` | *mcmc* wrapper |
| `build_chain_seed.py` | chain surgery DENY |
| `build_reseed_covmat.py` | chain surgery DENY |
| `standardize_cobaya_yaml.py` | cobaya wrapper DENY |
| `quantum_page_coevolve.py` | production thrash (explicit) |
| `desk_compute_all_safe.py` | orchestrator self |

`hybrid/*` is outside `scripts/` and was not in scope. PolyChord / setup_cloud / watch_* hits were empty under this `scripts/` glob after DENY (or already named above).

### Skip taxonomy for the 237 not run

| reason class | approx | notes |
|---|---:|---|
| Infra / non-physics | 18 | `__init__`, dashboards, plot_*, check_env, trim_icon, print_phi*, data_loader, … |
| CLASS / CMB / likelihood / chain-adjacent | large | `cmb_*`, `bbn_abundances`, `bbn_at_cmb*`, `chain_*`, `prtoe_*_run`, `verify_full_*`, `zon_*`, `crossval*`, … |
| Heavy sims / thrash risk | large | `quantum_page_*` (except already fenced coevolve), `genesis_solver*`, `granule_*`, `r1_caustic*`, continuum page MVPs |
| Formulable but **beyond 40-cap** | residual | further `de_value_*`, `cw_response_*`, `ring_*`, `zeta_*`, `z3_*`, `neutrino_*`, `ns_*`, `prym_*`, `winding_fbar_*`, … — honest backlog, not graded this wave |
| Explicit slow / heavy (peek) | few | `flat_direction_convergence_test.py`, `trace_heal_test.py`, `w_a_onset_truth.py` (classy/cobaya imports) |

Full remainder list is reproducible by: pack `--list` covered set − fence patterns − the 40 ran names below.

---

## 2. Ran (n=40) — SUMMARY

Source: `leftover/SUMMARY.json` / `SUMMARY.md`.

| metric | n |
|---|---:|
| Jobs | **40** |
| exit 0 | **38** |
| timeout (120s) | **2** (`biposh_estimator_pass`, `kapitza_junction_response`) |
| nonzero (non-timeout) | **0** |
| crude token_PASS | **3** |
| crude token_FAIL | **1** |

### True grade (honest; not token)

| true grade | n | labels |
|---|---:|---|
| **PASS verdict / COMPLETE promotion** | **0** | — |
| desk audit / card-only arithmetic (see PROMOTE_CANDIDATES) | few | `g_over_eps_is_the_roster`, `dark_colour_uniqueness_proof`, `pi_over_12_is_the_zero_crossing`, `census_scaling_network` (self-check only) |
| desk audit / priced residual / structured negative | majority | most exit0 jobs |
| FAIL physics (token + narrative) | 1 | `occupancy_lock_cannot_deliver` — hardens #86 contradiction; not a shelf kill of Q |
| timeout / no grade | 2 | biposh, kapitza_junction |

**Honest bottom line:** **no new COMPLETE promotions.** Token PASS ≠ shelf PASS. Several scripts tighten residual language or recompute known arithmetic; none dual-evidence a living-shelf COMPLETE.

### Jobs table (abbrev)

| label | exit | status | token | true note |
|---|---:|---|---|---|
| census_democratic_license | 0 | ok | — | desk |
| census_alpha_B_first_principles | 0 | ok | — | desk / GRADE in log |
| census_vos_microphysics | 0 | ok | — | desk / GRADE in log |
| census_scaling_network | 0 | ok | PASS | self-check ALL CHECKS PASS; mechanism class exhibited; γ\* value still OPEN |
| census_c_chop_transverse | 0 | ok | — | desk |
| as_coincidence_price | 0 | ok | — | PRICED AND HELD; not promoted |
| as_normalization_triangle | 0 | ok | — | C=1 transformed, not derived |
| as_count_normalization | 0 | ok | — | desk |
| beta_holders_elimination | 0 | ok | — | structured negative |
| biposh_estimator_pass | -9 | timeout | — | no grade |
| candle_room_correction | 0 | ok | — | desk numbers |
| candle_fence_check | 0 | ok | — | desk |
| candle_fence_check_v2 | 0 | ok | — | desk |
| cell_fraction_reduction | 0 | ok | — | f REDUCED not derived |
| diode_mechanism_pricing | 0 | ok | — | class selected; ω_J target owed |
| kapitza_drift_direction | 0 | ok | — | desk |
| kapitza_junction_response | -9 | timeout | — | no grade (diode log points here for averaging) |
| winding_comb_cl | 0 | ok | — | OUTSIDE fence (low) |
| winding_quadratic_pricing | 0 | ok | PASS | token from internal "identical: PASS"; #55 derivation NOT AVAILABLE |
| tau_deconfinement | 0 | ok | — | scale table; not COMPLETE |
| de_value_expansion_check | 0 | ok | — | desk |
| de_value_alpha2_handshake | 0 | ok | — | α⁴ power derived *in-script* grade language; still not shelf COMPLETE without dual evidence |
| de_value_Tc_exact_thermal | 0 | ok | — | desk |
| de_value_kp_selfconsistency | 0 | ok | — | desk |
| de_value_thermal_door | 0 | ok | — | re-derives known form |
| de_value_seam_scale | 0 | ok | — | desk |
| de_value_beta_functions_1loop | 0 | ok | — | desk |
| de_value_gap_equation | 0 | ok | — | T_c well-defined; residual named |
| de_value_derive_tau | 0 | ok | — | desk |
| dark_count_uniqueness | 0 | ok | — | licensed candidate w/ conditions; not derived |
| dark_colour_uniqueness_proof | 0 | ok | — | divisibility uniqueness; strengthens claim |
| dark_neff | 0 | ok | — | desk |
| dark_neff_su2 | 0 | ok | — | termination-B bookable failure language |
| cubic_charge_forbidden_test | 0 | ok | — | cubic kill on neutrino side; fence survives |
| coulomb_ring_stiffness_ratio | 0 | ok | — | desk |
| pi_over_12_is_the_zero_crossing | 0 | ok | — | exact identity at A=√2; displacement rule OPEN |
| null_mechanism_class_filter | 0 | ok | — | desk |
| occupancy_lock_cannot_deliver | 0 | ok | FAIL | hardens delivery-law contradiction |
| g_over_eps_is_the_roster | 0 | ok | PASS | g/ε = N=10 controls PASS; +4.5% residual OPEN |
| y_junction_ck_from_alpha | 0 | ok | — | desk |

Logs: `leftover/logs/<label>.log`.

---

## 3. NEW promotable PASS?

| question | answer |
|---|---|
| Any **COMPLETE** shelf promotion? | **No** |
| Any new dual-evidence win? | **No** (single-script desk only) |
| Any new arithmetic **card** worth cite-tracking? | **Card-only candidates** — see `PROMOTE_CANDIDATES.md` (do not edit living shelf without dual evidence) |

---

## 4. Return counts

| key | value |
|---|---:|
| **n_ran** | **40** |
| **n_skip** | **237** (leftover pool not executed this wave) |
| pack-covered (out of leftover scope) | 98 |
| fence-excluded | 10 |
| promote candidates | card-only (see companion); COMPLETE = 0 |

*NO FABRICATIONS. No PolyChord. No live MCMC. No H₀ book. Leftover sweep closed for the 40-cap batch.*
