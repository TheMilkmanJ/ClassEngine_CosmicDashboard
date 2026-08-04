# GRADE — Koide residual compute (desk_compute_full_20260804)

**Stamp graded:** 2026-08-04  
**Source SUMMARY:** [`koide/SUMMARY.md`](koide/SUMMARY.md) · console [`koide/console.txt`](koide/console.txt)  
**Pack:** `desk_compute_all_safe.py --pack koide --timeout 240`  
**Fences (binding):** NO FABRICATIONS · do **not** restore thermal delivery as candidate · do **not** invent Wilson inputs · mechanism residual stays **OPEN** · packaging **LOCKED** · exit 0 ≠ physics PASS · MCMCs untouched.

---

## 0. Run counts

| metric | count |
|---|---:|
| **Jobs** | **31** |
| exit 0 (instrument completed) | **29** |
| nonzero exit | **1** (`koide_wilson_holonomy_inventory` → **exit 2**) |
| timeout | **1** (`koide_ring_shape_qm` → exit −9 @ 265 s) |
| missing scripts | 0 |
| token `PASS` in log (SUMMARY scan) | **1** (`koide_triple_point_node` structure checks only) |
| token `FAIL` in log | 0 |
| **Physics promotion of mechanism / #101 / #102** | **0** |
| **Thermal/flat delivery restored as candidate** | **0** (forbidden; kill reconfirmed) |
| **Wilson θ_W scored** | **0** (MISSING_INPUTS; expected) |

**Rule restated:** exit 0 means the script finished; it is **not** a residual PASS. Promotion only where residual freeze allows — and the freeze does **not** allow mechanism grade restore.

---

## 1. Grade table (all 31 logs)

Physics column uses honest residual language: **RECONFIRMED**, **KILLED**, **OPEN**, **OPEN-BLOCKED**, **INSTRUMENT-ONLY**, **TIMEOUT**, **STRUCTURE-PAID**, **CANDIDATE-NOT-PROMOTED**.  
Instrument column: exit / SUMMARY status.

| # | label | exit | instrument | physics grade (this recompute) | load-bearing note |
|---:|---|---:|---|---|---|
| 1 | `koide_3body_test` | 0 | ok | INSTRUMENT-ONLY / structure | A=√2 as CV≈1 reframed; not derived; electron 2.27° off massless wall |
| 2 | `koide_KV_identification` | 0 | ok | OPEN (debt sharpened) | Graph supplies bond types; equal-coeff K∼R², V∼M² **not** paid |
| 3 | `koide_delivery_law_discriminator` | 0 | ok | **KILLED reconfirmed — thermal/flat** | **1025.4 ppm** miss vs **6 ppm** budget (~**171×**); Q_therm=0.667350286 @ x₁=2/9 |
| 4 | `koide_democratic_graph_null` | 0 | ok | CANDIDATE-NOT-PROMOTED | (P1)–(P4) ⇒ Q=2/3 if paid; (P4) equal quanta still open |
| 5 | `koide_equal_quanta_from_adiabaticity` | 0 | ok | OPEN (reduction only) | Adiabatic ramp can land null numerically; corpus ramp rate vs ω₁ still MISSING |
| 6 | `koide_frame_bridge` | 0 | ok | RECONFIRMED (fork named) | Geometry ceiling ε_D/ε_S < 3/4 vs thermal-null need 2; law at freeze still open |
| 7 | `koide_freeze_time_sensitivity` | 0 | ok | **KILLED reconfirmed + MISSING** | Same 1025.4 ppm; freeze pair / am / spectrum **unbuilt**; 6/6 MISSING_INPUTS |
| 8 | `koide_lock_algebra_verification` | 0 | ok | **RECONFIRMED — algebra** | a=3b ⇔ ρ²=1/2; τ=½ln2; ω₁=(2/9)T_c=39.356 keV; **physics residual open** |
| 9 | `koide_lock_pressure_test` | 0 | ok | STRUCTURE-PAID / residual L2 OPEN | Integer N=1 only matches Q=2/3 table; residual = value of conserved amplitude |
| 10 | `koide_node_vs_backdrop` | 0 | ok | OPEN | 18/18 checks; #1 model-building (threefold stiffness before pin) |
| 11 | `koide_null_occupancy_lock` | 0 | ok | ALGEBRA exact · **NOT live escape** | N₀=1 ⇒ null exact *if* applied; occupancy **killed 2026-07-29** as ω₁/ω₀=√2 source (integer) |
| 12 | `koide_null_stiffness_reduction` | 0 | ok | RENAME only | Q=2/3 ⇔ a=3b on ring; does not close exactness |
| 13 | `koide_null_sum_rule_check` | 0 | ok | SPLIT | Neutral seat conservation paid; ratio a=3b **not** a sum rule |
| 14 | `koide_phase_is_a_flat_direction` | 0 | ok | **KILLED — ring-internal phase** | φ flat at quadratic; cubic extrema miss 3φ=Q; #102 needs external reference |
| 15 | `koide_pour_before_split` | 0 | ok | INSTRUMENT-ONLY | Degenerate-pour path lands 0 ppm under stated assembly; not a free mechanism |
| 16 | `koide_quantum_law_null` | 0 | ok | FORK reconfirmed | Same delivery-law tension as discriminator (classical vs quanta) |
| 17 | `koide_ring_ab_from_binding` | 0 | ok | NEGATIVE (proxy) | On-site/bond from geometric binding **fails** a=3b |
| 18 | `koide_ring_color_rigidity` | 0 | ok | FAIL candidate (c) | Collinear color chain fails as ring stabilizer |
| 19 | `koide_ring_face_mass` | 0 | ok | OPEN / external referee | Lattice three-source geometry still arbiter |
| 20 | `koide_ring_junction_core` | 0 | ok | FAIL candidate (a) | Junction-core energetics fail thin-string |
| 21 | `koide_ring_quartic` | 0 | ok | Virial route stays dead | Shape-direction structure; no null from virial |
| 22 | `koide_ring_shape_modes` | 0 | ok | FAIL stiffness/virial → null | Shape sector soft route reconfirmed dead |
| 23 | `koide_ring_shape_qm` | −9 | **timeout** | **TIMEOUT — incomplete** | Partial landscape only (V origin/valley, k_b); **no full verdict**; not scored as kill/pass |
| 24 | `koide_ring_zero_point` | 0 | ok | CANDIDATE-NOT-PROMOTED (b) | Stabilizer (b) survives estimate grade; fences on η / m_face; not promoted |
| 25 | `koide_scheme_dependence` | 0 | ok | INSTRUMENT-ONLY | Pole vs other mass vars ≫ watch gap; scheme is load-bearing, not a close |
| 26 | `koide_triple_point_node` | 0 | ok | STRUCTURE-PAID | Node = structure + 2 knobs; **not** values; token PASS = checks only |
| 27 | `koide_watch_triangle` | 0 | ok | MEASUREMENT table | Light-mass A/φ conjunction sub-ppm tension; τ hides; external m_τ refine still required |
| 28 | `koide_wilson_holonomy_inventory` | **2** | **nonzero (expected)** | **OPEN-BLOCKED · MISSING_INPUTS 5/5** | No θ_W; no bin scored; refuse invent A_μ / n / α_d |
| 29 | `delivery_law_is_one_exponent` | 0 | ok | CLASSIFICATION | Four laws → one exponent family; p=0 (thermal) already under pressure |
| 30 | `delivery_law_third_class` | 0 | ok | CLASSIFICATION · not mechanism | Flatness e(2ε₀)=e(ε₀); deposition peak / T_D/T_S **not derived** |
| 31 | `delivery_law_two_parameters` | 0 | ok | TENSION named | Null selects thermal uniquely *inside* (s,p) **and** thermal overruns 6 ppm — **direct tension** |

---

## 2. What is RECONFIRMED

### 2.1 Thermal / flat delivery-law kill (special attention)

| quantity | this recompute | prior (debt_koide / K1) |
|---|---:|---:|
| x₁ = ħ w₁ / k T_c | 0.222222 | same |
| Q under exact thermal, ε_D = 2 ε_S | **0.667350286** | same |
| miss from 2/3 | **1025.4 ppm** | same |
| claimed exactness budget | 6 ppm | same |
| over-budget | **~171×** | same |
| x₁ needed for ≤6 ppm | ≤ 0.016971 | same |

**Verdict:** thermal/flat equipartition **cannot** carry the null at claimed exactness at the corpus frequency.  
**Fence:** mechanism grade is **not** “candidate” for this path (tribunal R2-koide lane **(c)**).  
**Also reconfirmed in:** `koide_freeze_time_sensitivity`, `delivery_law_two_parameters`, `delivery_law_third_class`, `delivery_law_is_one_exponent`.

Occupancy / cold-law was historically named as alternative class; **occupancy lock is not a live exactness escape** (integer ω ratio cannot be √2 — killed 2026-07-29; discriminator epilogue matches). Residual research stays **freeze-time stiffness / Wilson bins only** — **without** grade restore.

### 2.2 Lock algebra (special attention)

`koide_lock_algebra_verification` re-derives closed form:

1. **a = 3b ⇔ ρ² = 1/2** at every scale; **τ = −ln ρ = ½ ln 2 = 0.346574** ✓  
2. **N₀ = 1** and **E_c = ħω₁** ⇒ **f₀² = |f₁|²+|f₂|²** scale-free (algebra under premises) ✓  
3. **ω₁ = (2/9)·T_c = 39.356 keV** (bookkeeping with phase chain) ✓  

**Grade:** algebra **RECONFIRMED** (desk).  
**Not claimed:** why thermal equipartition, why one quantum — residual L2 / survival tests **OPEN** (same as shelf recompute 2026-08-04 and T6).

`koide_lock_pressure_test`: integer scan only N=1 lands Q=2/3 table; residual L2 = value of conserved amplitude — **OPEN**, not promoted.

### 2.3 Packaging / lane lock

| item | status |
|---|---|
| Packaging lane **(c)** | **LOCKED** (unchanged) |
| Q=2/3 as measured regularity | stands (fence 6.8×10⁻⁶) |
| Mechanism candidate grade | **not restored** |
| OPEN-THEORY | **stands** |

---

## 3. What remains OPEN

### 3.1 #101 — what enforces the null exactly

- Graded null **classified** (f₀² − |f₁|² − |f₂|² = 0 ⇔ Q=2/3) — structure paid.  
- **Not sourced.** No conservation/index/delivery law closes exactness to ~10⁻⁵ without dial.  
- Delivery-law fork: thermal uniquely selected *inside* some families **and** thermal fails exactness → **direct tension** (two-parameters log).  
- Freeze-time third stiffness pair: **named, unbuilt** (`koide_freeze_time_sensitivity` MISSING_INPUTS).  
- Democratic (P1)–(P4): conditional candidate; **(P4)** equal quanta unpaid.

### 3.2 #102 — phase source (Brannen 2/9)

- Measurement table paid (θ_B ≈ 0.2222296; δθ ≈ +7.409×10⁻⁶).  
- Ring-internal phase **retired** (`koide_phase_is_a_flat_direction`).  
- Holonomy **form** 3·θ_B = Q paid as structure **if** null sourced — **not** a Wilson evaluation.  
- **#102 OPEN** with #101 as one node residual.

### 3.3 Wilson holonomy inventory (special attention — expected exit 2)

`koide_wilson_holonomy_inventory` **exit 2**:

| requirement | status |
|---|---|
| `dark_SU2_A_mu` | **MISSING** |
| `family_cycle_path_C` | **PARTIAL** (phase-derived c₂ circular for 2/9 test) |
| `winding_background_n` | **MISSING** |
| `alpha_d_or_electric_projection` | **PARTIAL** |
| `holonomy_evaluator` | **MISSING** |

**MISSING_INPUTS: 5/5.** No θ_W. No bin scored. Pre-registered bins (HIT_PRIMARY / HIT_SIBLING / ELSE, W_hit = 2.617994×10⁻⁵ rad) **stand**.  
**Do not invent A_μ.** Branch A neither crowned nor killed.

### 3.4 Other open / incomplete this pack

| item | status |
|---|---|
| `koide_ring_shape_qm` | **TIMEOUT** — incomplete instrument; do not treat partial landscape as verdict |
| Equal quanta / adiabatic ramp rate | OPEN (need corpus freeze ramp vs ω₁) |
| R_c = M_c as classical VEVs | OPEN |
| K∼R², V∼M² equal coefficient | OPEN (`koide_KV_identification`) |
| Stabilizer (b) zero-point | estimate candidate only — not promoted |
| Light-mass watch triangle | measurement tension; needs external m_τ ≲1.4 ppm |

---

## 4. NON-PROMOTION list

Do **not** promote or forward-file any of the following from this recompute:

1. **Thermal / flat delivery** as a candidate mechanism for exact null (KILLED @ 1025 ppm / ~171×).  
2. **#101 closed** — null classified, not sourced.  
3. **#102 closed** — Brannen is table + form; phase mechanism open.  
4. **Wilson Branch A crowned/killed** — no θ_W; bins unscored.  
5. **Occupancy lock as live exactness escape** — algebra under N₀=1 is not a free promotion; integer ω₁/ω₀ ≠ √2 kill stands.  
6. **Democratic graph proven** — conditional on unpaid (P1)/(P4).  
7. **C3 triple-point node derives √2 or 2/9** — structure + knobs only (token PASS ≠ residual PASS).  
8. **am = −2 as model freeze law** — KZ needs it for classical ratio 2; not derived; thermal still fails.  
9. **Freeze-time stiffness pair as a number** — unbuilt; no invent.  
10. **Ring shape QM full verdict** — **timeout**, incomplete.  
11. **Stabilizer (b) / zero-point** as derivation — estimate viability only.  
12. **Any mechanism grade restore** under residual research.  
13. **Any MCMC / PolyChord / chain result** — none run; leave alone.  
14. **exit 0 ⇒ PASS** — forbidden reading of SUMMARY.

---

## 5. Cross-check: `T6_koide_owed.md` consistency

| T6 claim | This pack | consistent? |
|---|---|---|
| Header: thermal/flat **contradicted** 1025 ppm ≈ 171×; lane **(c)**; mechanism **not** candidate | Discriminator + freeze-time + delivery_law cousins reconfirm | **YES** |
| Residual research allowed (freeze-time / Wilson) **without grade restore** | Instruments re-ran; no promotion | **YES** |
| Item 1 / #101 mechanism OPEN | No close | **YES** |
| #102 phase OPEN; ring-internal phase retired | `phase_is_a_flat_direction` reconfirms | **YES** |
| Lock algebra holds; physics residual open | `lock_algebra_verification` ✓ | **YES** |
| Wilson needs A_μ etc.; do not invent | exit 2 MISSING_INPUTS 5/5 | **YES** |
| Occupancy not live escape for exactness | Discriminator epilogue + prior kill | **YES** |
| Packaging / OPEN-THEORY stand | No packaging unlock; OPEN-THEORY unchanged | **YES** |
| Desk status: protection + arithmetic paid; #101/#102 one node | Unchanged by recompute | **YES** |

**No T6 edit required** from this grade: owed file header and residual framing already match the recompute.  
(Optional hygiene only, not performed here: long body still contains historical “candidate” language for occupancy/thermal in older sections — **header + 2026-08-03 supersede rule** control; do not re-litigate thermal.)

Related board stamps still consistent:  
- [`T6_koide_desk_status.md`](../../T6_koide_desk_status.md) — OPEN-THEORY  
- [`RESIDUAL_IMPROVE_INVENTORY_20260803.md`](../RESIDUAL_IMPROVE_INVENTORY_20260803.md) — packaging **LOCKED**, residual **OPEN**  
- [`debt_koide_20260803/REPORT.md`](../debt_koide_20260803/REPORT.md) / [`K1_KOIDE_RESIDUAL.md`](../derivation_sprint_20260803/K1_KOIDE_RESIDUAL.md) / Wilson REPORT — numbers reproduced  

---

## 6. Executive stamp

| outcome | grade |
|---|---|
| Thermal/flat delivery | **KILLED** reconfirmed (1025.4 ppm / ~171×) |
| Lock algebra | **RECONFIRMED** (desk); residual L2 OPEN |
| Wilson inventory | **OPEN-BLOCKED** exit **2** · MISSING_INPUTS **5/5** |
| #101 / #102 | **OPEN** (OPEN-THEORY) |
| Packaging lane (c) | **LOCKED** |
| Mechanism candidate | **not restored** |
| Pack health | 29/31 exit0 · 1 timeout · 1 expected nonzero |

**One-liner:** Full koide pack reconfirms the thermal kill and lock algebra, blocks Wilson on missing inputs (exit 2 as designed), times out only `ring_shape_qm`, and **promotes nothing** — mechanism residual and #101/#102 stay OPEN; packaging stays LOCKED.

---

## Appendix — paths

```
docs/working_logs/_runs/desk_compute_full_20260804/
  GRADE_koide.md                 # this file
  koide/SUMMARY.md
  koide/SUMMARY.json
  koide/console.txt
  koide/logs/*.log               # 31 logs

docs/working_logs/T6_koide_owed.md
docs/working_logs/T6_koide_desk_status.md
```
