# GRADE — Page instrument + quantum residual (desk_compute_full_20260804)

**Stamp:** 2026-08-04 (desk packs `page_instrument` + `quantum_residual`)  
**Grader scope:** Page protocol scorecard on champion `coevolve_v13` + residual pack logs + optional continuum re-runs.  
**NO FABRICATIONS.** **exit 0 ≠ PASS.** **Strong CP abstention.** **No CANDIDATE packet.** **No densify thrash / no new coevolve production.** **MCMCs left alone. No PolyChord.**

---

## Headline (return values)

| quantity | value |
|---|---|
| **T8 early worst-bin residual** | **range/S\* = 0.11315435176934464 ≈ 0.113** |
| T8 need | ≤ 0.10 |
| T8 failing bin | **[0.10, 0.11)** · n=12 · S_range=0.001888 · S\*=0.016688 · threshold=0.001669 |
| **T8_pass** | **False** |
| **CANDIDATE_TURN_binding** | **False** |
| **page_curve_claimed** | **false** (tool never sets true) |
| **Q6 / dynamical Page** | **OPEN — NON-PROMOTION** |

**Champion remains `coevolve_v13`.** Joint near-miss: T1–T6 + stall + DC3 + T2 PASS; **only T8 early bin blocks binding**.

---

## 1. Pack availability

| pack | SUMMARY.md | jobs | exit0 | nonzero | timeout |
|---|---|---:|---:|---:|---:|
| `page_instrument` | yes · 2026-08-04T09:43:03Z | 3 | 3 | 0 | 0 |
| `quantum_residual` | yes · 2026-08-04T09:43:17Z | 5 | 5 | 0 | 0 |

Paths:
- `docs/working_logs/_runs/desk_compute_full_20260804/page_instrument/SUMMARY.md`
- `docs/working_logs/_runs/desk_compute_full_20260804/quantum_residual/SUMMARY.md`

---

## 2. v13 page_protocol_scorecard (BINDING)

**Input:**  
`docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json`  
**Recompute log (desk):**  
`page_instrument/logs/page_scorecard_v13.log`  
**Disk scorecard:**  
`…/page_curve/coevolve_v13_scorecard_recompute.json`  
**tool_sha256:** `1d02a1d4bdd11a88612f6db387a3a819425c3be362bc74a57122162cb90a14b7`

### 2.1 Gates

| gate | result | detail |
|---|---|---|
| **T1** interior max | **PASS** | u\* = 0.2670 |
| **T2** reach u≥0.9 | **PASS** | u_late = 0.9021 |
| **T2** frac/noise | **PASS/PASS** | T2_all = True |
| **T3** early rise | **PASS** | du>1e-9 credit; S_rise_credited = 0.0166874 |
| **T4** nulls | **PASS** | N1=N2=N3=N4 True |
| **T5** continuum | **PASS** | structural inherit (arrays-only) |
| **T6** artifacts | **PASS** | |
| **T7** claim flag | **False** | correct non-claim |
| **T1–T6 machine** | **True** | |
| drop / S\* / σ_jit | — | drop=0.010546 · S\*=0.016688 · σ=1e-8 |
| **stall_cap** | **PASS** | longest_stall_frames=10 ≤ cap 10 |
| **co_frac** ≥0.70 | **PASS** | 0.99995 |
| **swap** ≤0.05 | **PASS** | max |u−v|=1.50e-5 |
| **peak_in_motion** | **PASS** | |
| **T8** single-valued S(u) | **FAIL** | worst **[0.1, 0.11)** range/S\* = **0.113** (need ≤0.10); 1 failing bin / 83 occupied |
| **DC3** weight-invariant reach | **PASS** | v_frozen env/raw 0.9021/0.9021; STRUCTURAL_PURE_ENERGY_FRACTION |
| **CANDIDATE_TURN_T1_T6_only** | True | machine only — **not** a standing candidate |
| **CANDIDATE_TURN_binding** | **False** | T8 fails; DC3 gates when computable |
| **page_curve_claimed** | **false** | |

### 2.2 T8 residual (primary return)

```
T8_status:     ACTIVE_BINDING
T8_pass:       False
S_star:        0.016688199517780646
threshold:     0.1 * S* = 0.0016688199517780646
worst_bin:     [0.1, 0.11)
  n_points:    12
  S_min:       0.0011624560444613143
  S_max:       0.003050798443093273
  S_range:     0.0018883423986319587
  range/S*:    0.11315435176934464   ← T8 residual (need ≤ 0.10)
failing_bins:  1
```

**Interpretation:** early-bin multivalued residual only. Not Page closed. Not CANDIDATE. D4 freeze stance holds (no densify thrash).

---

## 3. Page instrument pack grade

| label | exit | desk PASS token | physics grade |
|---|---:|---|---|
| `page_scorecard_v13` | 0 | True (tool ran + printed) | **T8 FAIL** — binding candidate **False**; exit0 ≠ joint PASS |
| `area_law_quarter` | 0 | True | **Coefficient 1/4 paid** (algebra + numeric). Dynamical curve **OPEN** (not this script) |
| `page_scaffold` | 0 | False | Toy Page shape **illustration only**. Condensate Page curve **OPEN — not run** |

### 3.1 Optional continuum re-runs (this grade session)

Both scripts finished under 90s; re-ran successfully. **Neither is Q6 close.**

| script | t-class | result | claimed |
|---|---|---|---|
| `scripts/quantum_page_purestate_continuum.py` | <90s | T1–T6 machine True; CANDIDATE_TURN True; **claimed=false** | false |
| `scripts/quantum_page_continuum_coupled_mvp.py` | <90s | unitarity=True; null_g0 ok; page_like curiosity only | false |

Outputs:
- `…/page_curve/purestate_continuum.json`
- `…/page_curve/continuum_coupled_mvp.json`

**Not in desk pack as jobs** — optional adjunct only. No promotion path from continuum MVP / purestate toy to Q6.

---

## 4. Quantum residual pack grade

Source: `quantum_residual/SUMMARY.md` + logs.

| label | exit | PASS token | grade |
|---|---:|---|---|
| `medium_decoherence` | 0 | False | **Null-hardened (10/10 checks).** Ultralight medium induces no lab decoherence (Landau + rigidity). Not a QM-foundation derivation. Cherenkov channel for relativistic matter remains open corner. |
| `chsh_tsirelson` | 0 | True | **Null-hardened PASS.** B(r) saturates Tsirelson from below; never exceeds 2√2. Not a Born/Hilbert derivation. |
| `medium_r_inventory` | 0 | False | **MEDR/PAIRH: EN-D2/D3 → MISSING_INPUT** (scanned=490, medium_pin_found=False). Residual OPEN, not closed. |
| `wkb_medium` | 0 | True | **Shared-math PASS.** WKB thick-barrier ≡ 2× medium decay over same interval. Not a derivation of ℏ. |
| `pair_hamiltonian` | 0 | False | TMSV harness: rows=20, **all_below_tsirelson=True**; **medium_r_derived=False** — EN-D2/D3 still MISSING_INPUT. |

**Rule applied:** exit 0 ≠ automatic physics PASS. MEDR / pair-H medium-r remain **MISSING_INPUT**, not paid.

---

## 5. Hygiene: `page_curve_claimed true` assignments

Repo-wide strict search for **assignments**:

| pattern | count |
|---|---:|
| `"page_curve_claimed": true` in `*.json` | **0** |
| `page_curve_claimed = True` in `*.py` | **0** |
| Strict assignment hits (code/data, prose-forbidden filtered) | **0** |

Prose mentions of the forbidden string (checklists / freezes / “do not set true”) exist and are **not** assignments.  
**Hygiene: PASS — zero true assignments.**

---

## 6. NON-PROMOTION (binding verdict)

1. **No Page claim.** `page_curve_claimed` remains **false**.  
2. **Q6 OPEN.** Dynamical Page curve not closed; instrument joint clear blocked by **T8 early bin 0.113**.  
3. **No CANDIDATE packet.** `CANDIDATE_TURN_binding = False`. Machine T1–T6 True is **not** a standing candidate.  
4. **No densify thrash / no new coevolve production** this grade. Champion stays v13 / `v23_champion_locked`.  
5. **Coefficient ≠ curve.** Area-law quarter paid does **not** close Q6.  
6. **exit 0 ≠ PASS** on residual and scorecard packaging.

### Forbidden (reaffirmed)

- Set `page_curve_claimed: true`  
- File CANDIDATE without T1–T8 + DC3 + claim-decoupling + red AGREE  
- Subsample T8 bins or loosen threshold  
- Equate Q2 / area-law coefficient with dynamical Page  

---

## 7. Source table

| artifact | path |
|---|---|
| Desk page SUMMARY | `docs/working_logs/_runs/desk_compute_full_20260804/page_instrument/SUMMARY.md` |
| Desk residual SUMMARY | `docs/working_logs/_runs/desk_compute_full_20260804/quantum_residual/SUMMARY.md` |
| Scorecard log | `…/page_instrument/logs/page_scorecard_v13.log` |
| Scorecard JSON | `…/quantum_null_hardening_20260803/page_curve/coevolve_v13_scorecard_recompute.json` |
| Champion run | `…/page_curve/coevolve_v13.json` |
| Prior freeze | `docs/working_logs/_runs/page_full_freeze_20260804/REPORT.md` |

---

## 8. One-line return

**T8 = 0.113** (early bin residual; need ≤0.10) · **binding candidate False** · **page_curve_claimed false** · **Q6 OPEN / NON-PROMOTION**.

*NO FABRICATIONS. No CANDIDATE. No thrash. Grade complete.*
