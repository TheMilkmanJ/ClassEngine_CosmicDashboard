# DIAGNOSIS — Page T8 early-bin residual on champion `coevolve_v13`

**Date:** 2026-08-04  
**NO FABRICATIONS.** Arrays-only recompute. **`page_curve_claimed: false`.**  
**No CANDIDATE.** Strong CP abstention (out of scope here).

---

## 1. What T8 measures (binding)

From `scripts/page_protocol_scorecard.py` and PAGE_TURN_ACCEPTANCE_PROTOCOL.md §4.3:

| pin | value |
|---|---|
| Coordinate | \(u(t)=\max_{s\le t} v(s)\) (monotone envelope of pure energy fraction \(v=E_{\mathrm{rad}}/(E_{\mathrm{rad}}+E_{\mathrm{core}})\)) |
| Bin width \(\Delta u\) | **0.01** |
| Pass condition | In each occupied bin: \(\max S_{\mathrm{rad}}-\min S_{\mathrm{rad}} \le 0.1\cdot S_\star\) |
| \(S_\star\) | global peak of \(S_{\mathrm{rad}}\) on the history |
| Binding role | `CANDIDATE_TURN_binding` requires T1–T6 **and** `T8_pass` (and DC3 when computable) |
| Claim | Scorecard **never** sets `page_curve_claimed` true |

**Physical intent of T8:** single-valued \(S(u)\) — entropy is not multivalued over a fixed evaporation-coordinate window. Early-bin fail is a **steep monotone rise** over \(\Delta u=0.01\), not a late envelope-masked stall (that was a different denial class on older artifacts).

---

## 2. Which bin fails (reconfirm 2026-08-04)

**Command** (log: `scorecard_v13_rerun_20260804.log`):

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

| quantity | value |
|---|---|
| Artifact | `.../page_curve/coevolve_v13.json` |
| Schedule (artifact pins) | near-joint polish family; script header now `v23_champion_locked` |
| **T8_pass** | **False** |
| Failing bins | **1** (only) |
| Worst / sole fail | **\([0.10, 0.11)\)** |
| n_points in fail bin | **12** (history frames 43–54) |
| \(S_{\min}\) | 0.0011624560444613143 |
| \(S_{\max}\) | 0.003050798443093273 |
| \(S\) range | 0.0018883423986319587 |
| **range / \(S_\star\)** | **0.11315435176934464** |
| Need | \(\le 0.10\) |
| Excess over threshold | \(\approx 0.01315\) absolute in ratio units (~13% over the 0.10 bar) |
| \(S_\star\) | 0.016688199517780646 |
| Threshold \(0.1\cdot S_\star\) | 0.0016688199517780646 |
| Occupied bins | 83 |

**Neighbor bins (arrays diagnostic, not scorecard change):**

| bin | n | range/\(S_\star\) | pass? |
|---|---:|---:|---|
| [0.09, 0.10) | 40 | 0.0625 | yes |
| **[0.10, 0.11)** | **12** | **0.1132** | **no** |
| [0.11, 0.12) | 7 | 0.0929 | yes |
| [0.12, 0.13) | 6 | 0.0962 | yes |

So the joint block is **one early window**, not a broad multivalued tail.

---

## 3. Dynamics inside the failing bin

All 12 frames show **monotone** \(u\uparrow\) and \(S_{\mathrm{rad}}\uparrow\) (true co-evolution; not frozen-\(u\) purification vertical):

| frame | \(f\) | \(u\) | \(S_{\mathrm{rad}}\) | \(\mathrm{d}u\) | \(\mathrm{d}S\) |
|---:|---:|---:|---:|---:|---:|
| 43 | 0.0573 | 0.1004 | 1.16e-3 | ~5.2e-4 | ~1.2e-4 |
| … | … | … | … | rising | rising |
| 54 | 0.0720 | 0.1092 | 3.05e-3 | ~1.1e-3 | ~2.2e-4 |

- **Schedule fraction** \(f\in[0.057,0.072]\) — early TMS build window (`TMS_START=0`, `TMS_END=0.52`, shape \(\sin^p\) with \(p=\)`TMS_SHAPE_POWER`).
- **Evaporation coordinate** still low (\(u\sim0.10\)–\(0.11\)); peak \(S\) later at \(i=104\), \(u^*\approx0.267\).
- Fail mode class: **steep \(\mathrm{d}S/\mathrm{d}u\) while crossing one \(\Delta u=0.01\) bin** during overlapped TMS+BS, so

\[
\frac{\max S-\min S}{S_\star}\approx\frac{1}{S_\star}\int_{u}^{u+\Delta u}\frac{\mathrm{d}S}{\mathrm{d}u}\,\mathrm{d}u
\]

exceeds 0.10. Pure \(G_{\mathrm{TMS}}\) rescaling multiplies numerator and \(S_\star\) together → **ratio sticky ~0.11** (documented on freeze surfaces).

---

## 4. Which dynamical degrees drive early multivalued (steep) \(S(u)\)

Licensed construction of `quantum_page_coevolve.py` (not invented here):

| degree of freedom | role on early \(S(u)\) | evidence class |
|---|---|---|
| **TMS coupling** \(G_{\mathrm{TMS}}\cdot w_{\mathrm{tms}}(f)\cdot\sqrt{\Gamma_j}\) | Builds entanglement / \(S_{\mathrm{rad}}\) rise (two-mode squeeze blocks in free \(A\)) | Primary driver of early \(\mathrm{d}S\) |
| **TMS shape** `TMS_SHAPE_POWER`, window `[TMS_START,TMS_END)` | Sets how fast squeeze ramps at \(f\sim0.06\) | Controls early slope of \(S\) |
| **BS dump** \(G_{\mathrm{BS}}\cdot w_{\mathrm{bs}}(f)\cdot\sqrt{\Gamma_j}\) | Continuous mild energy transfer; advances \(v\) and thus \(u\) while \(S\) builds | Primary driver of early \(\mathrm{d}u\) |
| **BS_MILD + BS_RAMP_POWER** | Early floor + ramp of dump | Couples early reach vs early \(S\) slope |
| **Mode greybodies** \(\omega_j,\Gamma_j\) (week2 9-mode band) | Weights TMS/BS channel strengths | D3 densify exhausted; not free knob |
| **Core free frequency \(w_c(f)\)** | Can weight \(E_{\mathrm{core}}\); DC3 freezes weight | **D2:** \(w_c\equiv1\) **no-op** on champion path (freeze before former decay) |
| **Late EXTRA_BS sweeps** | Completes \(u\ge0.9\) and purification drop | Not in early fail bin; thrash risk for late multivalued if over-boosted |
| **Field continuum \(\phi(x,t)\)** | T5 structural class evidence | Not the T8 residual coordinate |

**Diagnosis in one line:** early fail is driven by the **TMS–BS overlap ratio** at \(f\sim0.06\): squeeze builds \(S\) faster per unit \(u\) than the T8 bin budget allows, while pure rescaling of TMS cannot fix the ratio and softening TMS / retuning BS / densify modes trades off **T2 / stall / DC3** (D1–D3 exhausted).

---

## 5. Joint gate context (what already PASSes)

From the same re-score (not hand numbers):

| gate | result |
|---|---|
| T1–T6 machine | **PASS** |
| T2 \(u_{\mathrm{late}}\ge0.9\) | **PASS** (0.9021) |
| stall_cap ≤10 | **PASS** (longest=10) |
| co_frac / swap / peak_in_motion | **PASS** |
| DC3 weight-invariant reach | **PASS** |
| **T8** | **FAIL 0.113** only |
| `CANDIDATE_TURN_binding` | **False** |
| `page_curve_claimed` | **false** |

Champion remains best joint near-miss. Sole residual for binding is early T8.

---

## 6. What would unstick (honest, not a claim)

Need a construction that **lowers early \(\mathrm{d}S/\mathrm{d}u\) over \(\Delta u=0.01\)** so range/\(S_\star\le0.10\) **without** losing T2 reach, stall_cap, coevo gates, nulls, or DC3. Header fine-tuning of v23 pins is **exhausted / sticky**. Next legitimate path is **licensed new microphysics** (new coupling / dump / free-Hamiltonian law), not densify thrash.

See `CONSTRUCTION_LEVERS.md`.

---

*NO FABRICATIONS. Diagnosis only. Q6 OPEN.*
