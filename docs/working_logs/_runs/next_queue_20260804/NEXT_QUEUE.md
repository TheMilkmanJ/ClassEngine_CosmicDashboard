# NEXT_QUEUE — ordered improve loop (2026-08-04 post full-sweep)

**Package:** `docs/working_logs/_runs/next_queue_20260804/`  
**Board authority:** [`../improve_loop_20260804/BOARD_STATUS.md`](../improve_loop_20260804/BOARD_STATUS.md)  
**Rule:** concrete file/script targets. **NO FABRICATIONS · no PolyChord · leave MCMCs · no invent · Strong CP abstention · BBN dual stamp.**

---

## Priority order (who can move it)

| pri | residual | who | action (concrete) | when |
|---:|---|---|---|---|
| **1** | bbnfix dual self-stop + book | **Machine** | leave cobaya; when both legs clear → book scripts | continuous wait |
| **2** | Fairbank / arXiv / BBN ε DOI | **Owner** | reply branch + endorsement + optional DOI ship | external |
| **3** | Laplace / tables after book | **Desk→Red** | runbook Stage A → RED_AUDIT → `--write-tables` | after #1 |
| **4** | Page T8 joint | **Theory** | licensed new microphysics only (D4); no thrash | unknown / construction |
| **5** | Named theory walls | **Theory** | bounce H_re, void, Koide, ω_J, DE occupancy, Born/atom | construction only |
| **6** | PolyChord nested | **Skip** | cluster later | not this box |

---

## 1. Machine — bbnfix (highest leverage)

**Do not kill. Do not peek-book H₀.**

| check | path / command |
|---|---|
| progress | `tail -1 chains/dyad_mnu_bbnfix.progress chains/cmp_lcdm_mnu_bbnfix.progress` |
| checkpoint | `grep -E 'converged\|Rminus1_last' chains/dyad_mnu_bbnfix.checkpoint chains/cmp_lcdm_mnu_bbnfix.checkpoint` |
| refuse smoke (safe anytime) | `python3 scripts/book_bbnfix_when_ready.py` → expect **REFUSED** until gate |
| diagnostic only (UNBOOKABLE) | `python3 scripts/bbnfix_mcmc_watch_diag.py` |
| living freeze | `docs/PRTOE_CHAIN_TABLES.md` |
| refuse cards | `docs/working_logs/_runs/bbnfix_booking_*/` |

**Gate:** both R−1 **&lt; 0.05** **and** both `converged: true`.

**When gate opens (Stage A — tables OFF by default):**

```bash
cd /home/themilkmanj/prtoe_class
bash scripts/bbnfix_when_ready_all.sh
# or: python3 scripts/book_bbnfix_when_ready.py
# then finalize path as in laplace_booking_full RUNBOOK
```

**Stage B tables (only with red stamp):**

```bash
# require docs/working_logs/_runs/bbnfix_booking_<id>/RED_AUDIT.md
# with line: red: AGREE   or   red: AGREE-IF
bash scripts/bbnfix_when_ready_all.sh --write-tables
```

| artifact | role |
|---|---|
| `scripts/book_bbnfix_when_ready.py` | dual-leg gate authority |
| `scripts/bbnfix_when_ready_all.sh` | Stage A/B wrapper |
| `scripts/bbnfix_mcmc_watch_diag.py` | UNBOOKABLE diag |
| `docs/working_logs/_runs/laplace_booking_full_20260804/RUNBOOK.md` | post-gate Laplace + publish split |
| `docs/working_logs/_runs/booking_pipeline_red_gate_20260804/REPORT.md` | red table gate |
| `docs/working_logs/_runs/machine_watch_hygiene_20260804/REPORT.md` | watch hygiene lock |

**Current disk (do not invent change):** lcdm R−1 **0.071122** (N=21886, t=2026-08-04T13:01:13; was 0.086466@N=20409; earlier 0.059@N=19013 — **1.42×** stop) / dyad **0.128943** (N=20302); both `converged: false`. Currency: `machine_r1_currency_20260804e`.

---

## 2. Owner — Fairbank / arXiv / DOI

**Desk does not post, email, or invent endorsement.**

| action | concrete target |
|---|---|
| On Fairbank reply | `docs/working_logs/_runs/arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md` |
| Package inventory | `.../arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md` |
| Owner checklist | `ForJustin/ARXIV_OWNER_CHECKLIST.md` |
| Ship vehicle (0νββ) | `papers/neutrino-mbb/` + `docs/arXivReady/` |
| HOLD companion | `docs/exploratory/PRTOE_fairbank_note_HOLD.md` |
| Fairbank letter (CORPUS_ONLY) | `docs/PRTOE_fairbank_note_draft.md` |
| Package audit (desk re-run only) | `python3 scripts/arxiv_package_audit.py` |
| BBN ε dual stamp | arithmetic PASS in `papers/bbn-eps-bound/recompute_eps_bound.py`; **DOI still owner** |
| READY set | neutrino-mbb · radio-lattice · lattice-tc-gap · bbn-eps-bound · kination-tracking-note |
| SHIPPED | supertrace-note Zenodo **10.5281/zenodo.21763188** |

**Post order (owner):** neutrino-mbb (hep-ph) first when endorsement lands; parallel astro-ph options for radio/bbn-eps if hep-ph stalls — see owner prep REPORT.

---

## 3. Desk post-gate only (not forceable now)

| step | script / file |
|---|---|
| Book pair | `scripts/book_bbnfix_when_ready.py` / `bbnfix_when_ready_all.sh` |
| Laplace prep | `docs/working_logs/_runs/open_board_split_20260803/LAPLACE_PREP.md` |
| Laplace runbook | `docs/working_logs/_runs/laplace_booking_full_20260804/RUNBOOK.md` |
| Red audit before tables | `bbnfix_booking_<id>/RED_AUDIT.md` |
| Living chain tables write | only `--write-tables` with red, or owner `--force-tables` |
| Neutrino home residual lift | after book — `docs/PRTOE_neutrino_home.md` (do not invent numbers early) |

---

## 4. Page D4 — theory / microphysics only

**Do not thrash.** Formal status: [`PAGE_D4_STATUS.md`](PAGE_D4_STATUS.md).

| item | path |
|---|---|
| Freeze package | `docs/working_logs/_runs/page_full_freeze_20260804/` |
| Champion JSON | `.../quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| Scorecard tool | `scripts/page_protocol_scorecard.py` |
| Producing script (locked) | `scripts/quantum_page_coevolve.py` (`v23_champion_locked`) |
| Claim-decoupling | `.../quantum_residual_task_20260803/CLAIM_DECOUPLING_CHECKLIST.md` |
| Acceptance protocol | `.../PAGE_TURN_ACCEPTANCE_PROTOCOL.md` |
| D1–D4 note | `.../open_board_split_20260803/PAGE_DEEPER_CONSTRUCTION_NOTE.md` |
| Hub Q6 | `docs/PRTOE_quantum_gravity.md` |

**Only if** a licensed new microphysics law appears (not densify):

1. New instrument run (write-once versioned JSON; never overwrite scored artifact).  
2. `python3 scripts/page_protocol_scorecard.py <run.json>`.  
3. Require **T8 ≤ 0.10** (and all prior joint gates still PASS).  
4. Claim-decoupling checklist **then** red AGREE — **no** packet without T8 and red.  
5. Keep `page_curve_claimed: false` until separate claim step.

**Forbidden queue items:** coevolve_v39 densify; G_BS retune campaign; T8 threshold loosen; claim packet on v13.

---

## 5. Theory walls — construction only (no invent closes)

| wall | living freeze | construction target (when formulable) |
|---|---|---|
| Bounce \(H_\mathrm{re}\) | `docs/PRTOE_bigbang_no_singularity.md` · `bounce_full_freeze_20260804/` | exterior re-entry proof path; **not** desk numeric invent |
| Void floor | `docs/PRTOE_cosmic_magnetism.md` · `debt_rm_formula_20260803/` | seed / void amplitude (RM geometry already paid) |
| Koide residual | `docs/PRTOE_koide_relation.md` · `debt_koide_20260803/` | mechanism; Wilson inputs not invented |
| Forward ω_J | `docs/PRTOE_baryogenesis.md` · `debt_baryo_omegaJ_20260803/` | A_ωJ from seat microphysics |
| DE occupancy | `docs/PRTOE_coincidence_problem.md` | occupancy mechanism or permanent demote |
| Born / atom / MEDR / pair H | `quantum_residual_task_20260803/BORN_PROCESS_LOCK.md` · MEDR inventory | MISSING_INPUT — no invent |
| Onset bias D2 | SCIENCE_DEBTS / debt_p042 | instrument / theory — no invent |
| Hierarchy horn-(a) | exploratory hierarchy | residual sized; no precision close |

Honesty audit (0 overclaims): `docs/working_logs/_runs/theory_walls_honesty_20260804/REPORT.md`.

---

## 6. Explicit skip

| item | stance | note |
|---|---|---|
| **PolyChord** | **Skip** | `hybrid/polychord_*`, `run_polychord_pair.sh` — cluster later; not residual thrash |
| Strong CP θ̄ | **DENY standing** | `docs/PRTOE_strong_cp.md` COMPLETE-ABSTENTION; seat-hunt itch only |
| New production MCMC | **Forbidden** this wave | leave dyad / lcdm / routeD alone |
| densify coevolve campaign | **Forbidden** | D3 exhausted |

---

## 7. Desk-forceable now? (honest) — post `desk_compute_full_20260804`

**Compute wave landed:** named packs + leftover-40 + bounce finished and graded; **COMPLETE promotions = 0**.  
**Authority residual audit:** [`../desk_compute_full_20260804/FINAL_RESIDUAL_AUDIT.md`](../desk_compute_full_20260804/FINAL_RESIDUAL_AUDIT.md)  
**Verdict:** *desk formulable compute exhausted under fences: **YES*** (leftover2 SUMMARY incomplete but no high-value dual-evidence backlog identified).

| class | desk-forceable under fences? | post-wave note |
|---|---|---|
| Named formulable recompute packs (arithmetic, bounce, koide, hierarchy, baryo/RM, page, quantum residual, core, alpha/amp, analytic tests) | **exhausted** | all SUMMARY + `GRADE_*.md` written; reconfirms only |
| Leftover high-value cap-40 sweep | **exhausted** | 0 COMPLETE; card-only cites only (`leftover/PROMOTE_CANDIDATES.md`) |
| leftover2 / ~200 unscored scripts | **optional hygiene only** | incomplete async (~31 logs, no SUMMARY); overwhelmingly re-run / CLASS / infra noise — **not** residual-critical |
| Timeout re-runs (bounce m6*, ring_shape_qm, vertex, biposh, kapitza) | **optional instrument only** | does not unlock COMPLETE / H_re / Page T8 |
| Hygiene / dual-stamp language / residual boards | **largely exhausted** | this package + compute wave |
| bbnfix book | **no** — machine | leave cobaya; refuse smoke only |
| arXiv / Fairbank / DOI | **no** — owner | |
| Page T8 joint | **no** — theory / microphysics | T8≈0.113 reconfirmed; no densify |
| Theory wall closes (H_re, void, Koide, ω_J, …) | **no** — invent forbidden | |
| PolyChord | **no** — skip | |

**Remaining optional desk (only if inconsistency found — do not thrash):**

| optional | target |
|---|---|
| re-refuse smoke | `python3 scripts/book_bbnfix_when_ready.py` |
| re-audit packages | `python3 scripts/arxiv_package_audit.py` |
| BBN ε recompute | `python3 papers/bbn-eps-bound/recompute_eps_bound.py` |
| Page re-score champion only | scorecard on **v13** only (no new coevolve) |
| leftover2 SUMMARY close or explicit abandon | inventory hygiene — not a COMPLETE path |
| ForJustin paste currency | `ForJustin/STATUS_CONTINUE.md` if R−1 stamp drifts |

---

## 8. Next 5 concrete desk actions (if any remain)

1. **Watch-only stamp (≤2 min):** re-run `python3 scripts/book_bbnfix_when_ready.py` and confirm **REFUSED**; if ever exit 0, stop and execute §1 Stage A immediately.  
2. **Do not** launch coevolve densify / new Page production — D4 formalized; re-score v13 only if board disputes numbers.  
3. **Owner handoff only:** point owner at `OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md` + READY inventory — no desk email.  
4. **After book (future):** follow `laplace_booking_full_20260804/RUNBOOK.md` Stage A → red → tables.  
5. **Theory:** park construction on named walls only when a licensed derivation path exists; otherwise idle — residual honesty already frozen. **Do not** thrash leftover2 / timeout re-runs as if they were residual-critical.

*NO FABRICATIONS. Desk formulable compute wave landed and is exhausted under fences; improve loop is machine/owner/theory.*
