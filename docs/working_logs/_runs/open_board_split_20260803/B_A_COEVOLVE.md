# B-A REPORT — Page co-evolution instrument → T8

**Task:** Improve Page co-evolution instrument toward T8_pass (single-valued \(S(u)\)).  
**Date:** 2026-08-03  
**Resource:** OMP_NUM_THREADS=1, nice -n 10. No PolyChord. MCMCs left alone.

---

## T8_pass

| item | value |
|---|---|
| **T8_pass** | **True** |
| T1–T6 machine | True |
| CANDIDATE_TURN_binding (scorecard machine flag) | True |
| **page_curve_claimed** | **false** |
| **CANDIDATE packet filed** | **no** |

---

## Key numbers (from disk only)

### Run artifact
`docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve.json`  
Schedule: `v12_T8_coevolve` · script sha256 prefix `d789fb0c03a41416`

| quantity | value |
|---|---:|
| u* (S peak) | 0.3363344401575123 |
| u_late | 0.9979399799431029 |
| S_peak / S* | 0.01387766233170623 |
| S_late | 0.00348582470494281 |
| drop | 0.01039183762676342 |
| frac S-rise while u advances | 0.9957423828167425 |
| co_frac steps to peak | 0.7327586206896551 |
| freeze-rise steps (dS>0.005 @ du=0) | 0 |
| midband S rises while u advances | True |
| N1 / N2 / N3 / N4 | True / True / True / True |

### Scorecard artifact
`docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_scorecard_recompute.json`  
tool sha256 prefix `175bcdd50086d3c2`

| T8 quantity | value |
|---|---:|
| T8_pass | True |
| threshold 0.1·S* | 0.001387766233170623 |
| occupied bins | 91 |
| failing bins | 0 |
| worst bin | [0.12, 0.13) |
| worst range/S* | 0.08786278941135602 (pass) |

---

## What changed

**Problem (prior v3 coevolve):** T1–T6 True, T8 False — multivalued \(S(u)\) in late freeze bin often [0.95,0.96) with long stall (~400 steps, range/S*~0.32) plus early thin-bin multivalued rise (~0.13–0.15 S*).

**Frozen-header schedule v12** in `scripts/quantum_page_coevolve.py`:

1. **`IDLE_AFTER_F=0.32`** — after first high-\(u\) contact, set \(g_{\mathrm{TMS}}=g_{\mathrm{BS}}=0\) and hold state. Cuts post-freeze purification tail that made late \(S(u)\) multivalued (v3 denial mode). Does **not** blend schedule into \(v\); \(v\) remains pure \(E_{\mathrm{rad}}/(E_{\mathrm{rad}}+E_{\mathrm{core}})\).
2. **`TMS_SHAPE_POWER=4`** — \(\sin^p\) envelope softens early TMS onset so early \(dS/du\) does not pile entropy into thin low-\(u\) bins.
3. **Near-v3 energy lock** — `G_BS=3.8`, `W_C_DECAY=6.5`, modest `G_TMS=0.37`, `BS_MILD=0.23`. Soft-BS trials (v4–v6) caused Rabi reverse / freeze-rise / T1 fail; early EXTRA_BS (v5–v6) moved S peak onto frozen high \(u\).
4. **Claim-decoupling preserved** — run JSON written first; scorecard is a separate CLI step; run script never sets `page_curve_claimed` or self-files CANDIDATE.

**Docs updated from disk numbers:**  
- `docs/working_logs/_runs/quantum_null_hardening_20260803/PAGE_CURVE_COEVOLVE.md`  
- `docs/working_logs/_runs/quantum_residual_task_20260803/PAGE_COEVOLVE_RESULT.md`  
- `docs/working_logs/_runs/quantum_residual_task_20260803/COEVOLVE_NOTE.md`

---

## Explicit non-claim

- **Not a Page curve claim.** Q6 remains OPEN.  
- Machine `CANDIDATE_TURN_binding=True` is a scorecard flag only — **no CANDIDATE packet was filed**.  
- `page_curve_claimed` remains **false** everywhere.  
- Protocol still requires claim-decoupling checklist + red AGREE before any claim path.  
- Continuum ingredient is week2 ω/Γ + same-run field evidence class — not full QFT on curved acoustic spacetime.  
- No coefficient \(A/4G\) payment; no \(4v(1-v)\) ansatz as physics; no thermal-only \(dE/T\) as Page.

---

## Paths

| role | path |
|---|---|
| Script | `/home/themilkmanj/prtoe_class/scripts/quantum_page_coevolve.py` |
| Scorecard tool | `/home/themilkmanj/prtoe_class/scripts/page_protocol_scorecard.py` |
| Run JSON | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve.json` |
| Scorecard JSON | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_scorecard_recompute.json` |
| This report | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/open_board_split_20260803/B_A_COEVOLVE.md` |

*NO FABRICATIONS.*
