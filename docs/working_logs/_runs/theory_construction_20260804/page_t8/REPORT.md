# REPORT — Page T8 theory/instrument construction package (“what would unstick”)

**Date:** 2026-08-04  
**Path:** `docs/working_logs/_runs/theory_construction_20260804/page_t8/`  
**NO FABRICATIONS.**  
**`page_curve_claimed`:** **false**  
**Standing CANDIDATE:** **none**  
**PolyChord / MCMC:** **not touched**  
**coevolve production / densify thrash:** **not launched**  
**Strong CP:** **abstention**

---

## 1. Mission and fences

Honest construction package for champion instrument **`coevolve_v13`**: diagnose the T8 early-bin residual, list **licensed** levers (not invent), re-score only. No premature CANDIDATE; no claim.

| fence | held? |
|---|---|
| `page_curve_claimed` false | **yes** |
| No CANDIDATE without T8≤0.10 **and** red | **yes** (no packet) |
| No densify thrash / no coevolve_v39 production | **yes** |
| Leave MCMCs alone; no PolyChord | **yes** |
| Strong CP abstention | **yes** |

---

## 2. T8 reconfirm (arrays-only)

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

**Log:** [`scorecard_v13_rerun_20260804.log`](scorecard_v13_rerun_20260804.log)  
**Tool also rewrote:** `.../page_curve/coevolve_v13_scorecard_recompute.json`

| quantity | value |
|---|---|
| **T8_pass** | **False** |
| Worst / sole fail bin | **[0.10, 0.11)** |
| **range / \(S_\star\)** | **0.11315435176934464** |
| Need | ≤ **0.10** |
| Residual (ratio − 0.10) | **≈ 0.01315** |
| \(S_\star\) | 0.016688199517780646 |
| Threshold \(0.1\cdot S_\star\) | 0.0016688199517780646 |
| S range in fail bin | 0.0018883423986319587 |
| n_points in fail bin | 12 |
| Occupied bins | 83; failing bins = **1** |
| T1–T6 + stall + DC3 + T2 | **PASS** |
| `CANDIDATE_TURN_binding` | **False** |
| `page_curve_claimed` | **false** |

**Headline residual:** early multivalued (steep monotone) \(S(u)\) in \(\Delta u=0.01\) bin at low evaporation coordinate — **0.113** vs **0.10**.

---

## 3. Package contents

| file | role |
|---|---|
| [`REPORT.md`](REPORT.md) | this summary |
| [`DIAGNOSIS.md`](DIAGNOSIS.md) | fail bin, T8 definition, dynamical DOFs |
| [`CONSTRUCTION_LEVERS.md`](CONSTRUCTION_LEVERS.md) | levers graded CANDIDATE idea / EXHAUSTED / FORBIDDEN thrash |
| [`PROTOCOL.md`](PROTOCOL.md) | write-once → scorecard → T8≤0.10 → claim-decoupling → red; claim flag false until claim step |
| [`NON_CLAIMS.md`](NON_CLAIMS.md) | explicit non-claims |
| [`scorecard_v13_rerun_20260804.log`](scorecard_v13_rerun_20260804.log) | re-score console log |

Optional continuum diagnostic scripts: **not run** (scorecard + fail-bin dump sufficient; avoid thrash risk / time).

---

## 4. Diagnosis (one paragraph)

T8 is binding single-valued \(S(u)\) in \(\Delta u=0.01\) bins with range ≤ \(0.1\cdot S_\star\). On `coevolve_v13`, only bin **[0.10, 0.11)** fails at **range/\(S_\star\)=0.113**. Frames 43–54 (\(f\sim0.057\)–\(0.072\)) show **monotone** rise of both \(u\) and \(S_{\mathrm{rad}}\) during early **TMS+BS overlap**. Primary drivers: TMS entangling slope vs BS dump advance. Pure \(G_{\mathrm{TMS}}\) rescaling is **ratio-sticky**; D1 (two-phase) improves early T8 but loses T2; D2 (\(w_c\equiv1\)) is a no-op on this trajectory; D3 densify breaks reach/stall/DC3. Joint clear needs a **licensed new coupling/dump/free-Hamiltonian law**, not header thrash.

---

## 5. What would unstick (honest)

| path | status |
|---|---|
| Header G_TMS / BS_MILD / densify | **FORBIDDEN thrash** (exhausted) |
| D1–D3 deeper construction as already tried | **EXHAUSTED** without joint clear |
| **D4** accept near-miss | **Active** |
| New licensed microphysics (L1–L4 in CONSTRUCTION_LEVERS) | **Only legitimate next Page work** — not derived here |
| Protocol after any future joint clear | JSON write-once → scorecard → T8≤0.10 → claim-decoupling → red → claim step; `page_curve_claimed` false until claim |

---

## 6. Cross-links

| surface | role |
|---|---|
| `page_full_freeze_20260804/` | outsider freeze |
| `open_board_split_20260803/B_A_COEVOLVE_V13_BEST.md` | champion report |
| `open_board_split_20260803/PAGE_DEEPER_CONSTRUCTION_NOTE.md` | D1–D4 |
| `next_queue_20260804/PAGE_D4_STATUS.md` | D4 formalization |
| `quantum_residual_task_20260803/CLAIM_DECOUPLING_CHECKLIST.md` | claim-decoupling |
| `docs/PRTOE_quantum_gravity.md` Q6 | OPEN; claimed false |

---

## 7. Bottom line

| item | value |
|---|---|
| Champion | `coevolve_v13` |
| T8 | **FAIL 0.113154** (need ≤0.10) |
| Residual | **~0.013** in ratio units over bar |
| Binding candidate | **False** |
| Page claimed | **false** |
| Next | microphysics only; zero thrash |

*NO FABRICATIONS. Zero densify. Zero premature CANDIDATE. Package complete.*

## Claude red AGREE cure — input artifact hash (2026-08-04)

Write-once evidence for champion `coevolve_v13.json`:

```
input_sha256 = 048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8
```

Recorded by `scripts/page_protocol_scorecard.py` as `input_sha256` on every scorecard write (tool + input hash). Silent rewrite of the JSON is now greppable against this stamp.
