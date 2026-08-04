# PAGE D4 STATUS — formalize near-miss (document only) — 2026-08-04

**Package:** `docs/working_logs/_runs/next_queue_20260804/`  
**Authority freeze:** [`../page_full_freeze_20260804/`](../page_full_freeze_20260804/)  
**Rule:** **document only.** No densify thrash. No coevolve production campaign.  
**`page_curve_claimed`:** **false** (must stay false).  
**Standing CANDIDATE:** **none.**

---

## 1. Champion instrument

| item | value |
|---|---|
| Artifact | `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| Artifact sha256 | `048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8` |
| Schedule | `v23_champion_locked` |
| Scorecard recompute | `.../page_curve/coevolve_v13_scorecard_recompute.json` |
| Tool | `scripts/page_protocol_scorecard.py` |
| LATEST pointer | `coevolve_LATEST.txt` → v13 (champion, not last densify write) |

Re-score command (arrays-only; already run in freeze):

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

---

## 2. Joint gates on v13 — pass / fail

Numbers from freeze [`SCORECARD_SNAPSHOT.md`](../page_full_freeze_20260804/SCORECARD_SNAPSHOT.md). **Not invented.**

| gate | result | detail |
|---|---|---|
| T1 interior max | **PASS** | u* = 0.266967 |
| T2 reach u≥0.9 | **PASS** | u_late = 0.902078 |
| T2 frac/noise | **PASS** | T2_all True |
| T3 early rise | **PASS** | S_rise_credited = 0.0166874 |
| T4 nulls N1–N4 | **PASS** | True |
| T5 continuum | **PASS** | structural inherit |
| T6 artifacts | **PASS** | True |
| T1–T6 machine (`CANDIDATE_TURN_T1_T6_only`) | **PASS** | True |
| stall_cap ≤10 | **PASS** | longest_stall_frames = **10** |
| co_frac ≥0.70 | **PASS** | ≈ 0.99995 |
| swap_back ≤0.05 | **PASS** | max u−v ≈ 1.50e-5 |
| peak_in_motion | **PASS** | True |
| **DC3** weight-invariant reach | **PASS** | v_frozen env late = 0.902078; method `e_c_raw_stored` |
| **T8** single-valued S(u) | **FAIL** | sole fail |
| T8 worst bin | **[0.10, 0.11)** | n=12; S_range/S* = **0.113154** (need ≤0.10) |
| T8 threshold | 0.1 × S* | S* = 0.0166882; threshold = 0.00166882 |
| T8 occupied bins | 83 | failing bins = **1** |
| T7 claim flag | **False** | correct — scorecard never claim-flips |
| **`CANDIDATE_TURN_binding`** | **False** | requires T8_pass (+ DC3 when computable) |
| **`page_curve_claimed`** | **false** | tool never sets true |

**Interpretation:** best joint instrument near-miss to date. Only early-bin T8 multivalued residual blocks binding. **Not Page closed. Not CANDIDATE.**

### Curve numbers (reference only)

| quantity | value |
|---:|
| S_peak (S*) | 0.016688199517780646 |
| S_late | 0.00614180917446334 |
| drop | 0.010546390343317304 |
| i_peak | 104 |
| n_frames | 188 |

---

## 3. D1–D3 exhausted → D4 active

Source: [`../open_board_split_20260803/PAGE_DEEPER_CONSTRUCTION_NOTE.md`](../open_board_split_20260803/PAGE_DEEPER_CONSTRUCTION_NOTE.md)  
+ attempt notes `B_A_D1_ATTEMPT.md` / `B_A_D2_ATTEMPT.md` / `B_A_D3_ATTEMPT.md`.

| ID | Idea | Outcome |
|---|---|---|
| **D1** | Two-phase Hamiltonian (BS then TMS) | **Exhausted** — early T8 can improve; T2 not jointly recovered |
| **D2** | Free frequencies fixed \(w_c\equiv 1\) | **Exhausted / no-op** on champion trajectory |
| **D3** | Mode densify / continuum band (v35–v38) | **Exhausted** — not joint (reach / stall / DC3 regressions) |
| **D4** | Accept instrument near-miss until new microphysics | **Active freeze stance** |

**Why thrash stops:** early bin [0.10, 0.11) is **monotone** \(S(u)\) while TMS builds. Pure \(G_{\mathrm{TMS}}\) rescales numerator and \(S_\star\) together → **ratio sticky ~0.11**. Soften-early-TMS trades lose T2 or reintroduce late multivalued \(S(u)\).

**Forbidden residual actions:**

- Resume BS_MILD / G_TMS / densify header thrash as the Q6 program  
- Subsample T8 bins or loosen T8 threshold to “pass”  
- File CANDIDATE on v13 (or any coevolve_v*) without full gate stack  

---

## 4. Why CANDIDATE is **not** opened

| reason | detail |
|---|---|
| **T8 fails** | early residual **0.113** &gt; 0.10 → `CANDIDATE_TURN_binding` = **False** |
| **Binding definition** | scorecard: binding requires T1–T6 machine **and** T8_pass (DC3 when computable) |
| **Claim-decoupling** | ACTIVE — packet may not be co-written with first run JSON; checklist not started as a filing |
| **Red AGREE on claim** | no claim packet exists to red-grade |
| **Machine True ≠ candidate** | T1–T6 True is **not** a standing CANDIDATE |
| **Q2 ≠ Q6** | area-law / coefficient payment is **not** dynamical Page curve |

Checklist authority:  
`docs/working_logs/_runs/quantum_residual_task_20260803/CLAIM_DECOUPLING_CHECKLIST.md`  
Protocol: `PAGE_TURN_ACCEPTANCE_PROTOCOL.md` §4.3–4.4.

---

## 5. Explicit: no claim-decoupling packet without T8 ≤ 0.10 and red

**Binding rule (this package restates — does not invent):**

1. **Do not** open a claim-decoupling / CANDIDATE packet while T8 fails (early residual **0.113** today).  
2. **Even if** a future instrument achieves T8 ≤ 0.10 **and** T1–T6 + DC3 + stall + coevo gates still PASS:  
   - run JSON must already exist independently  
   - arrays-only scorecard must show `T8_pass` and `CANDIDATE_TURN_binding` True  
   - **then** claim-decoupling checklist  
   - **then** red AGREE  
   - **only then** any claim path; `page_curve_claimed` stays false until that separate claim step  
3. **Never** set `page_curve_claimed: true` from scorecard tooling or residual thrash.

---

## 6. What would unstick (microphysics only — without inventing it)

D4 is an **honesty freeze**, not a physics close. The only legitimate next Page work is a **licensed new coupling / dump / free-Hamiltonian law** — not edge-tuning the frozen v23 header.

| class | what it would need to do | what this desk will **not** do |
|---|---|---|
| New free-Hamiltonian / coupling law | flatten early \(dS/du\) over Δu=0.01 **without** killing T2 reach or stall_cap | invent an unnamed law |
| Licensed dump / occupation channel | change early transfer shape so early range/S* ≤ 0.10 jointly with DC3 | densify thrash “until green” |
| Deeper continuum construction with new physics justification | not pure mode-count retune of exhausted D3 | resume v35–v38-style densify |

Until that appears:

- Champion remains **v13**  
- schedule_version stays **`v23_champion_locked`**  
- Q6 stays **OPEN**  
- Machine-wait other programs (bbnfix) is fine  
- **Do not thrash Page CPU**

---

## 7. Forbidden claims (outsiders / future agents)

Do **not** claim or write:

1. Page curve closed / Q6 paid  
2. `page_curve_claimed: true`  
3. CANDIDATE packet on v13 without T1–T8 + DC3 + claim-decoupling + red AGREE  
4. Machine `CANDIDATE_TURN` / T1–T6 True as a standing candidate  
5. Q2 area-law coefficient payment = dynamical Page curve  
6. D4 as a physics close  
7. “Almost candidate” as a claim grade  

---

## 8. Cross-links (freeze-consistent surfaces)

| surface | role |
|---|---|
| `page_full_freeze_20260804/REPORT.md` | outsider freeze |
| `page_full_freeze_20260804/SCORECARD_SNAPSHOT.md` | gate numbers |
| `page_full_freeze_20260804/HYGIENE.md` | path checklist |
| `open_board_split_20260803/B_A_COEVOLVE_V13_BEST.md` | champion report |
| `open_board_split_20260803/PAGE_DEEPER_CONSTRUCTION_NOTE.md` | D1–D4 lock |
| `quantum_residual_task_20260803/STATUS.md` | R-PAGE OPEN |
| `docs/PRTOE_quantum_gravity.md` Q6 | OPEN; claimed false |

*NO FABRICATIONS. Zero thrash. Zero premature CANDIDATE. D4 formalized.*
