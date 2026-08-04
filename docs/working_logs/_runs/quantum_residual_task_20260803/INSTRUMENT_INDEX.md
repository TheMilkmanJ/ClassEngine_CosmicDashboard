# R-PAGE instrument index (currency sync 2026-08-04)

**Date currency:** 2026-08-04 (full freeze + status sync)  
**Rule:** every instrument row has `page_curve_claimed: false`. No Q6 close.  
**Standing CANDIDATE:** **none**  
**Champion:** **`coevolve_v13`** — T8 fail **0.113**; binding false; **D4 active**  
**Authority freeze:** `docs/working_logs/_runs/page_full_freeze_20260804/`  
**Status sync:** `docs/working_logs/_runs/quantum_status_sync_20260804/`

Scripts live under `scripts/`. JSON artifacts under  
`docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/` unless noted.  
Task reports under this directory.

---

## Scripts

| Script | Purpose (one line) | page_curve_claimed |
|---|---|---|
| `scripts/quantum_page_curve_scaffold.py` | Early scaffold / placeholder for Page program layout | **false** |
| `scripts/quantum_page_sonic_horizon_week1.py` | Week1 sonic / acoustic horizon \(\kappa\), \(T_H\) instrument | **false** |
| `scripts/quantum_page_bogoliubov_week2.py` | Week2 stationary Bogoliubov + greybody continuum modes | **false** |
| `scripts/quantum_page_core_skeleton_week3.py` | Week3 finite-core skeleton (toy Gaussian core bookkeeping) | **false** |
| `scripts/quantum_page_week3_nulls.py` | Week3 null suite (g=0 / vacuum / unitarity class checks) | **false** |
| `scripts/quantum_page_week3_Nc_scan.py` | Week3 \(N_c\) scan of hybrid \(S_\mathrm{rad}\) curiosity curves | **false** |
| `scripts/quantum_page_week3_week2_coupled.py` | Couple week2 greybodies into week3 core skeleton | **false** |
| `scripts/quantum_page_srad_unitary_mvp.py` | Unitary pure-state \(S_\mathrm{rad}(v)\) MVP (toy modes; free squeeze dial) | **false** |
| `scripts/quantum_page_continuum_coupled_mvp.py` | C1–C2 continuum-informed hybrid: week2 Γ weights + evaporating unitary core | **false** |
| `scripts/quantum_page_continuum_evaporating.py` | Thermal-only cumulative \(dE/T\) vs unitary hybrid on evaporating schedule | **false** |
| `scripts/quantum_page_continuum_dynamical_p2.py` | Adiabatic P2 snapshots: re-solve week2 modes along ell↑ / κ↓ family | **false** |
| `scripts/quantum_page_continuum_field_td.py` | Time-dependent 1D continuum field \(\phi(x,t)\) + cumulative \(S_\mathrm{rad}\) scorecard | **false** |
| `scripts/quantum_page_purestate_continuum.py` | Pure-state continuum-weighted Gaussian modes; protocol scorecard | **false** |
| `scripts/quantum_page_candidate_rebuild.py` | Batch8/9 hygiene rebuild: full histories + §4.2 monotone \(u\); scorecard from arrays | **false** |
| `scripts/quantum_page_coevolve.py` | T8-era co-evolution: write-once `coevolve_v{N}.json`; header **`v23_champion_locked`**; no self-claim | **false** |
| `scripts/page_protocol_scorecard.py` | Arrays-only T1–T8 + coevolution gates (binding); never sets claimed true | **false** |

---

## Reports (this run dir)

| Report | Purpose (one line) | page_curve_claimed | Standing CANDIDATE? |
|---|---|---|---|
| `PAGE_TURN_ACCEPTANCE_PROTOCOL.md` | Binding pre-reg fence (T1–T8 + claim-decoupling ACTIVE) | n/a (fence) | **no** |
| `CLAIM_DECOUPLING_CHECKLIST.md` | Filing order after JSON + scorecard | n/a | **no** |
| `PAGE_COEVOLVE_RESULT.md` | **Champion freeze result** — v13 joint near-miss | **false** | **no** |
| `page_curve/coevolve_v1.json` + `*_scorecard_recompute.json` | Historical write-once; stall_cap fails → no CANDIDATE | **false** | **no** |
| `page_curve/coevolve_v13.json` + scorecard + `coevolve_LATEST.txt` | **CHAMPION:** T1–T6+stall+DC3+T2 PASS; **T8 fail 0.113**; binding **false**; schedule `v23_champion_locked`; **D4 active** | **false** | **no** |
| `../page_full_freeze_20260804/` | Full residual freeze + hygiene package (authority) | **false** | **no** |
| `../quantum_status_sync_20260804/` | Currency rewrite of residual-task surfaces to match freeze | **false** | **no** |
| `PAGE_C1C2_RESULT.md` | Result of continuum-coupled MVP | **false** | **no** |
| `PAGE_EVAPORATING_RESULT.md` | Thermal vs unitary hybrid evaporating instrument | **false** | **no** |
| `PAGE_P2_DYNAMICAL_RESULT.md` | Adiabatic P2 dynamical continuum scorecard | **false** | **no** (machine False) |
| `PAGE_FIELD_TD_RESULT.md` | TD field instrument scorecard | **false** | **no** (machine False) |
| `PAGE_PURESTATE_RESULT.md` | Pure-state continuum scorecard | **false** | **no** — machine True, **red DENIED** |
| `PAGE_CANDIDATE_REBUILD.md` | Candidate rebuild batch9 scorecard | **false** | **no** — machine True, **red DENIED** |
| `STATUS.md` | Honest residual rollup (currency 2026-08-04) | **false** / Q6 OPEN | **no CANDIDATE** |
| `INSTRUMENT_INDEX.md` | This index | — | — |

---

## Champion lock (do not thrash)

| item | value |
|---|---|
| Champion artifact | `coevolve_v13.json` |
| LATEST pointer | → v13 (not later densify attempts) |
| T8 residual | **0.113** (sole binding fail) |
| D1–D3 | exhausted (no joint clear) |
| **D4** | **active** — accept near-miss until licensed new microphysics |
| Thrash | **forbidden** (no coevolve knob thrash, no densify mode thrash, no G_BS retune for T8) |
| CANDIDATE | **none** |

---

## Related null-hardening mirrors (not re-claimed here)

Parallel prose under `docs/working_logs/_runs/quantum_null_hardening_20260803/`  
(`PAGE_CURVE_*.md`, `page_curve/*.json`) mirrors the same instruments.  
Same rule: **`page_curve_claimed: false`**; no Q6 close; bare machine CANDIDATE scores are not standing after red denial.

---

## Explicit non-claims

- No instrument books a Page turn as physics.  
- No script may flip `page_curve_claimed` without T1–T8 + claim-decoupling + red AGREE under the binding protocol.  
- Curiosity / page-like shape ≠ CANDIDATE TURN ≠ PAGE CLAIM.  
- Machine T1–T6 True on v13 ≠ standing CANDIDATE (T8 0.113 blocks).  
- D4 is a freeze stance, not a physics close.

*NO FABRICATIONS.*
