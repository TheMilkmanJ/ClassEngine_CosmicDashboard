# REPORT — Page T8 residual-demand theory chase

**Package:** `docs/working_logs/_runs/theory_construction_20260804/page_t8_residual_demand/`  
**Date:** 2026-08-04  
**Mode:** Exploratory “laws as suggestions” + Rule 1 (CANDIDATE levers only; can-exist + kill-seeking; band fixed before land)  
**Prior:** `page_t8/` (T8=0.113 fail; D1–D3 exhausted; pure \(G_{\mathrm{TMS}}\) sticky) · champion `coevolve_v13` · `input_sha256 048de43e…`  
**Fences held:** NO FABRICATIONS · `page_curve_claimed: false` · no densify thrash · no coevolve production campaign · no CANDIDATE packet without T8≤0.10+red · MCMCs untouched · no PolyChord · Strong CP abstention · no ownership tasks

---

## 0. Residual one-liner (return stamp)

**T8 keeps forcing lower early dS/du through [0.10,0.11) jointly with T2+stall+DC3; pure G_TMS sticky; D1–D3 dead as program; schemas R1–R3+R5 survive only as licensed-micro CANDIDATEs; champion v13 T8=0.113154… still fail; no packet.**

---

## 1. Mission and prior

| Prior surface | Result used |
|---|---|
| `page_t8/DIAGNOSIS.md` | Early monotone fail bin; TMS–BS overlap; DOFs |
| `page_t8/CONSTRUCTION_LEVERS.md` | L1–L4 CANDIDATE ideas; D1–D3 EXHAUSTED; thrash FORBIDDEN |
| `page_t8/PROTOCOL.md` | Write-once → scorecard → T8≤0.10 → claim-decoupling → red |
| `page_full_freeze_20260804/` | Outsider freeze; D4 active |
| `PAGE_DEEPER_CONSTRUCTION_NOTE.md` + D1–D3 notes | Exhausted constructions |
| Champion JSON | `.../page_curve/coevolve_v13.json` |

**This package does not invent a Page law or land a joint clear.** It names residual demand, proposes kill-seeking CANDIDATE levers, and freezes dead thrash lanes.

**Extension rule:** extends `CONSTRUCTION_LEVERS` L1–L4 into residual levers R1–R8; **does not** reopen EXHAUSTED/FORBIDDEN grades.

---

## 2. T8 reconfirm (arrays-only; no coevolve)

**Hygiene note:** `scripts/page_protocol_scorecard.py` had a one-line print syntax break (`print(...); print()` glued); repaired so re-run could execute. Logic of T8 pins unchanged.

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

**Log:** [`scorecard_v13_rerun_20260804_residual.log`](scorecard_v13_rerun_20260804_residual.log)

| quantity | value |
|---|---|
| Artifact | `coevolve_v13.json` |
| **input_sha256** | **`048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8`** (matches disk) |
| **T8_pass** | **False** |
| Worst / sole fail bin | **[0.10, 0.11)** |
| **range / \(S_\star\)** | **0.11315435176934464** |
| Need | ≤ **0.10** |
| Residual (ratio − 0.10) | **≈ 0.01315** |
| \(S_\star\) | 0.016688199517780646 |
| Threshold \(0.1\cdot S_\star\) | 0.0016688199517780646 |
| S range in fail bin | 0.0018883423986319587 |
| n_points | 12 (frames 43–54) |
| Occupied bins | 83; failing bins = **1** |
| T1–T6 machine | **PASS** |
| T2 u_late | **0.9021 PASS** |
| DC3 | **PASS** |
| `CANDIDATE_TURN_binding` | **False** |
| `page_curve_claimed` | **false** |

Independent arrays recompute of the fail bin reproduced the same range/\(S_\star\). Rough path slope: \(\mathrm{d}S/\mathrm{d}u\sim0.215\) over \(\Delta u\sim0.0088\) in-bin.

**No coevolve production. No densify. No MCMC. No PolyChord.**

---

## 3. Package contents

| file | role |
|---|---|
| [`WHAT_RESIDUAL_DEMANDS.md`](./WHAT_RESIDUAL_DEMANDS.md) | What T8 keeps forcing (early dS/du; joint T2+stall+DC3) |
| [`CANDIDATE_LEVERS.md`](./CANDIDATE_LEVERS.md) | Eight CANDIDATE dynamical/micro levers R1–R8; double scrutiny each |
| [`DEAD_LANES.md`](./DEAD_LANES.md) | Densify thrash, G_TMS-only, threshold loosen, invent island formula, D1–D3, etc. |
| [`SURVIVORS.md`](./SURVIVORS.md) | What survives for deeper work (schemas + D4) |
| [`REPORT.md`](./REPORT.md) | This executive |
| [`scorecard_v13_rerun_20260804_residual.log`](./scorecard_v13_rerun_20260804_residual.log) | Re-score console log |

---

## 4. What residual demands (headline)

T8 keeps forcing **one dynamical object**:

> A **licensed microphysical law** that lowers **early \(\mathrm{d}S/\mathrm{d}u\)** through \(\Delta u=0.01\) at \(u\sim0.10\)–\(0.11\) so range/\(S_\star\le0.10\), **jointly** with T2 reach, stall_cap, DC3, and T1–T6 — without pure \(G_{\mathrm{TMS}}\) rescaling, densify thrash, threshold games, or invented island formulas.

Negative demands: header thrash, D1–D3 reheat, soft pass 0.113, premature packet, Q2-as-Q6.

Full list: [`WHAT_RESIDUAL_DEMANDS.md`](./WHAT_RESIDUAL_DEMANDS.md).

---

## 5. CANDIDATE levers (headline)

| ID | Name | Outcome |
|---|---|---|
| **R1** | Licensed dump / occupation-transfer law (L1) | **SURVIVOR-SCHEMA** · MISSING law |
| **R2** | Licensed entangling operator law (L2) | **SURVIVOR-SCHEMA** · MISSING law |
| **R3** | Free-Hamiltonian redesign beyond D2 (L3) | **SURVIVOR-SCHEMA** · DC3-hard |
| **R4** | Continuum back-reaction law (L4; not densify) | **FRAGILE-SCHEMA** |
| **R5** | Single-micro TMS×BS co-modulation | **SURVIVOR-SCHEMA** |
| **R6** | Theory-fixed greybody/spectrum law | **FRAGILE-SCHEMA** |
| **R7** | Licensed early seed occupation | **FRAGILE-SCHEMA** |
| **R8** | D4 honesty near-miss disposition | **ACTIVE-DISPOSITION** |

**Joint lands: 0.** **Packets: 0.** Each lever carries can-exist / should-not-exist / joint-gate risk / kill in [`CANDIDATE_LEVERS.md`](./CANDIDATE_LEVERS.md).

---

## 6. Dead lanes (headline)

- **Header thrash:** \(G_{\mathrm{TMS}}\), `BS_MILD`, TMS shape/delay, EXTRA_BS boost grids  
- **D1–D3:** two-phase / free-\(w_c\) flip / densify — EXHAUSTED without joint clear  
- **Protocol-break:** loosen 0.10 bar, widen \(\Delta u\), subsample bins, machine-True⇒candidate  
- **Wrong object:** late-stall thrash on v13, Q2-as-Page, PolyChord/MCMC Page, invent island \(S(u)\)  
- **Launders:** densify as “R4 continuum,” manual nbar as “R7 seed,” D1 flags as “new law”

Full table: [`DEAD_LANES.md`](./DEAD_LANES.md).

---

## 7. Survivors / next (headline)

| Item | Status |
|---|---|
| Deeper work if content appears | Primary: **R1 / R2 / R5** licensed micro → write-once → full scorecard stack |
| Stretch | R3 (DC3-hard), R4/R6 (non-densify only), R7 (null-safe seed only) |
| Default now | **R8 / D4** — accept near-miss; zero thrash |
| Champion | **v13** locked; schedule `v23_champion_locked` |
| Q6 | **OPEN**; claimed **false** |

Details: [`SURVIVORS.md`](./SURVIVORS.md).

---

## 8. Non-claims (hard)

1. Page curve **not** closed; Q6 **not** paid.  
2. **`page_curve_claimed`** remains **false**.  
3. **No** standing CANDIDATE packet.  
4. **0.113 is FAIL**, not soft pass.  
5. Levers are **not** predictions of joint clear.  
6. No invented microphysics derived here.  
7. Scorecard hygiene fix ≠ physics progress.  
8. Strong CP / MCMC / PolyChord / ownership: untouched / abstained.

---

## 9. Bottom line

| item | value |
|---|---|
| Champion | `coevolve_v13` · sha256 `048de43e…` |
| T8 | **FAIL 0.113154…** (need ≤0.10) on **[0.10,0.11)** only |
| Joint other gates | **PASS** |
| Binding candidate | **False** |
| Page claimed | **false** |
| Residual program | licensed micro only; thrash dead; D4 active |

*NO FABRICATIONS. Zero densify. Zero coevolve production. Zero premature CANDIDATE. Package complete.*
