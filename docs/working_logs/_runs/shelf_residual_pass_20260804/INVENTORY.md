# Shelf residual pass — OPEN inventory (2026-08-04)

**Source of truth:** `docs/working_logs/_FILE_COMPLETION_STATUS.md` (stamped 2026-08-03 C3)  
**Banner refresh:** file heads re-read 2026-08-04; status tags below unless noted  
**Rule:** NO FABRICATIONS. Prefer OPEN-BLOCKED / machine-wait over fake COMPLETE.

**Action classes**

| code | meaning |
|---|---|
| **(a)** | Formulable recompute card/script exists (desk recompute, no new physics) |
| **(b)** | Discipline-only fix (fence, ledger, soft-claim demote) |
| **(c)** | Permanent / long OPEN-BLOCKED (named missing axiom / theory wall) |
| **(d)** | Machine wait (chain, sim, sampler — leave alone this pass) |
| **(e)** | External wait (data, lattice campaign, facility) |

**OPEN-DESK count in completion status:** **0** (tag defined; no file currently primary-tagged OPEN-DESK).

---

## OPEN-MACHINE (8)

| file | status (banner) | residual | next action | notes |
|---|---|---|---|---|
| `docs/PRTOE_CHAIN_TABLES.md` | OPEN-MACHINE | Live bbnfix + routeD; GetDist archive unconverged | **(d)** | Banner stale (2026-08-02 R−1 ~0.19/0.14/129). Night watch 2026-08-04: lcdm R−1≈0.059, dyad≈0.189, still not bookable. **Do not touch chains.** |
| `docs/PRTOE_s8_growth.md` | OPEN-MACHINE | conv_desi unproduced; matched lensing OPEN (#161) | **(d)** / **(b)** if soft | Conversion channel stated; posterior unproduced |
| `docs/PRTOE_s8_tension.md` | OPEN-MACHINE | same as growth | **(d)** | Companion; conv_desi dead twice |
| `docs/PRTOE_neutrino_home.md` | OPEN-MACHINE | Σm_ν joint (dyad_mnu) + double-duty | **(d)** | Relation established; joint fit machine (T3) |
| `docs/PRTOE_galactic_atoms.md` | OPEN-MACHINE | α_c → r_1s; GC budget live tests (T1) | **(d)** + **(b)** done | Soft “resolves GC” fenced this pass |
| `docs/PRTOE_smbh_atoms.md` | OPEN-MACHINE | α_g chain-gated; NewAthena WATCH (T2) | **(d)** / **(e)** | Desk half paid |
| `docs/PRTOE_quartet_clock.md` | OPEN-MACHINE | live readout vs zon_disp | **(d)** | Unit=pair resolved; zon_disp parked/unconverged |
| `docs/PRTOE_granule_scoping.md` | OPEN-MACHINE | SP dynamics + χ-lag sim + data | **(d)** | Statistical core DONE; sims not started |

---

## OPEN-THEORY (8 inventory rows; 6 live shelf + 2 exploratory)

| file | status (banner) | residual | next action | notes |
|---|---|---|---|---|
| `docs/PRTOE_igmf_helicity.md` | OPEN-THEORY | sign(H_kin) production; sampling defect; 3D re-run | **(d)** / **(c)** | T14 i6 **candidate-closed config-local**; production sign **KILLED** (SCIENCE_DEBTS D1). Do not invent production sign. |
| `docs/PRTOE_cosmic_magnetism.md` | OPEN-THEORY | void floor OPEN; RM n_e amplitude open | **(a)** paid + **(c)** void | RM geometric **paid** (`rm_coherence_kibble.py`); void = WATCH/new seed |
| `docs/PRTOE_koide_relation.md` | OPEN-THEORY | #101/#102 residual; Wilson missing inputs | **(a)** recompute + **(c)** | Protection derived; thermal path contradicted; relation unexplained regularity. Lock algebra / τ Parseval re-PASS this pass |
| `docs/exploratory/PRTOE_hierarchy_problem.md` | OPEN-THEORY | §6f / basement μ5 (gated #146) | **(a)** scripts exist; **(c)** residual | Exponent derived; anchor band honest — not shelf-primary close |
| `docs/PRTOE_bigbang_no_singularity.md` | OPEN-THEORY | classical turn OPEN | **(c)** | Floor ρ_bounce paid; F-A3 H_re **OPEN-BLOCKED** (debt_bounce) |
| `docs/exploratory/PRTOE_white_holes.md` | OPEN-THEORY | global ID provisional; bounce turn shared | **(c)** | Local WH forbidden derived |
| `docs/PRTOE_inflation_replacement.md` | OPEN-THEORY | bounce + tilt residual | **(c)** + **(b)** done | Soft “answers each problem / jewel” fenced |
| `docs/PRTOE_cyclic_torus_genesis.md` | OPEN-THEORY | bounce/cyclic rungs vs theorems | **(c)** | Self-banner story/physics-mixed; ledger present; no invent |

---

## WATCH-EXTERNAL (5)

| file | status (banner) | residual | next action | notes |
|---|---|---|---|---|
| `docs/PRTOE_lattice_note.md` | WATCH-EXTERNAL | SU(2) N_f=3 T_c/√σ (#67) | **(e)** | Circulation-approved bet P-048 |
| `docs/PRTOE_deuterium_row.md` | WATCH-EXTERNAL | LUNA d(d,n)³He (P-058) | **(e)** | Model−ΛCDM gap not waiting |
| `docs/PRTOE_lowell_anomalies.md` | WATCH-EXTERNAL | BipoSH data application (T5) | **(e)** + **(b)** done | Soft “improvement” fenced |
| `docs/PRTOE_cmb_anomalies.md` | WATCH-EXTERNAL | joint BipoSH referee | **(e)** | Axis-family candidate; cold spot not member |
| `docs/PRTOE_lss_parity.md` | WATCH-EXTERNAL | DESI 4PCF (T16) | **(e)** + **(b)** done | Amp ~7 orders short; soft DESI validation fenced |

---

## Related COMPLETE-CONDITIONAL with formulable (a) residual (not OPEN-primary)

These are **not** in the OPEN counts but host preferred recompute cards:

| file | relevant residual | recompute |
|---|---|---|
| `PRTOE_bbn_witness.md` / BBN ε package | ε &lt; 3.2% (2σ) outsider card | **(a)** BBN eps arithmetic — PASS this pass |
| `PRTOE_quantum_gravity.md` / `induced_gravity.md` | area-law ratio; supertrace | **(a)** PASS |
| `PRTOE_baryogenesis.md` | junction quartet back-solve | **(a)** PASS; forward **(c)** |
| `PRTOE_koide_relation.md` | lock algebra / τ Parseval | **(a)** PASS; mechanism **(c)** |

---

## Theory walls crosswalk (`THEORY_WALLS_QUEUE_20260803.md`)

| wall | shelf files | class |
|---|---|---|
| Bounce turn H&gt;0 | bigbang, inflation_replacement, cyclic_torus, white_holes, stability | **(c)** |
| Koide residual | koide_relation | **(c)** + residual research **(a)** |
| DE self-tuning / coincidence | coincidence_problem (COMPLETE-CONDITIONAL occupancy OPEN) | **(c)** — do not claim solves |
| Page / Q6 | quantum_gravity, induced_gravity, information_paradox | **(c)** OPEN-BLOCKED |
| MEDR / Born / atomic QM | exploratory quantum wing | **(c)** seating fence |

---

## Counts

| bucket | n |
|---|---:|
| OPEN-MACHINE | 8 |
| OPEN-THEORY (shelf + exploratory listed) | 8 |
| WATCH-EXTERNAL | 5 |
| OPEN-DESK | 0 |
| **Total inventoried OPEN residual docs** | **21** |

Banner vs inventory: **no status-tag promotions**. CHAIN_TABLES banner numbers lag night-watch R−1 (lcdm improved toward gate but still unbookable) — leave tag OPEN-MACHINE.
