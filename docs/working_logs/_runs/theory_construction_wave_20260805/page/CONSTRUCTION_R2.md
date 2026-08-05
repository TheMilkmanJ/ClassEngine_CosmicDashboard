# CONSTRUCTION_R2 — Entangling operator candidates (parent L2 / residual R2)

**Package:** `docs/working_logs/_runs/theory_construction_wave_20260805/page/`  
**Date:** 2026-08-05  
**Scope:** R2 only — candidate **classes** of licensed entangling operator laws that *could* be admitted for future write-once scoring  
**Priors:** `desk_t6_page_micro_20260804/R1_R2_R5.md` · residual R2 · D4 map · `page_t8/CONSTRUCTION_LEVERS` L2 · DIAGNOSIS TMS driver · F1 S⋆ fence  
**Champion residual (arrays reconfirm this package):** range/\(S_\star\) = **0.113154…** on bin **[0.10, 0.11)** (need ≤ **0.10**)  
**Fences:** NO FABRICATIONS · `page_curve_claimed: false` · no densify thrash · no coevolve production · leave MCMCs · no PolyChord · pure \(S_\star\) inflation **DEAD** (F1)  
**Stocked licensed alternate entangling law text:** **none** → every candidate below remains **MISSING_INPUT** until named generator + theory weights land

---

## 0. Residual target (R2-specific)

R2 is the **entangling** DOF class. Early \(\mathrm{d}S\) is primarily TMS-driven under champion construction. Pure \(G_{\mathrm{TMS}}\) rescale is **ratio-sticky** (scales early \(\Delta S\) and global \(S_\star\) together).

| quantity | v13 value |
|---|---|
| Fail bin | **[0.10, 0.11)** |
| range (numerator) | **0.0018883423986319587** |
| \(S_\star\) (denominator) | **0.016688199517780646** |
| range/\(S_\star\) | **0.11315435176934464** |
| Need | ≤ **0.10** |
| Rough early \(\mathrm{d}S/\mathrm{d}u\) | ≈ 0.215 (arrays diagnostic) |

**What R2 must eventually do (if ever licensed):** **cap early \(\mathrm{d}S/\mathrm{d}u\)** through \(u\sim0.10\)–\(0.11\) while still producing interior Page peak (T1) and credited early rise on \(\mathrm{d}u>0\) (T3) — not pure \(G_{\mathrm{TMS}}\) / shape thrash, not densify, not pure \(S_\star\) inflation (F1).

**Champion instrument TMS pins (stocked schedule; not a new law):**

| pin | v13 value | role |
|---|---|---|
| `G_TMS` | 0.37 | squeeze amplitude scale (**ratio-sticky** under pure rescale) |
| `TMS_START` | 0.0 | entangle window start |
| `TMS_END` | 0.52 | entangle window end |
| `TMS_SHAPE_POWER` | 2.6 | \(\sin^p\) schedule weight |

Coupling structure (instrument grammar, DIAGNOSIS): \(G_{\mathrm{TMS}}\cdot w_{\mathrm{tms}}(f)\cdot\sqrt{\Gamma_j}\) into two-mode squeeze blocks in free \(A\).

---

## 1. Schema statement (unchanged; not derived)

> Early entanglement growth is **not** forced to pure two-mode-squeeze with \(\sin^p\) schedule weight. A **named entangling operator law** (different generator and/or greybody-fixed channel weights with theory license) **caps early \(\mathrm{d}S/\mathrm{d}u\)** through \(u\sim0.10\)–\(0.11\) while still producing interior Page peak (T1) and credited early rise on \(\mathrm{d}u>0\) (T3).

---

## 2. REQUIRED_INPUTS (must fill before implement/score as new dynamics)

| # | Input | Meaning | Stocked? |
|---|---|---|---|
| R2-I1 | **Named entangling generator** | Alternate to pure TMS envelope; Hamiltonian / symplectic structure | **MISSING_INPUT** |
| R2-I2 | **Channel / greybody weights** | Theory-fixed weights (not free `TMS_SHAPE_POWER` / `G_TMS`) | **MISSING_INPUT** |
| R2-I3 | **Unitarity (N4) proof sketch** | Legal channel; not ad-hoc entropy clamp | **MISSING_INPUT** |
| R2-I4 | **Peak / T3 preservation plan** | How T1 interior max and T3 early rise remain honest | **MISSING_INPUT** |
| R2-I5 | **Stickiness break certificate** | Law is **not** global scale of present TMS (ratio sticky under pure scale) | **MISSING_INPUT** |
| R2-I6 | **F1 disclosure plan** | Report early-bin range **and** \(S_\star\) vs v13 on any future T8_pass (class A/B only) | **protocol ON**; no artifact yet |

**Instrument already stocked (not substitutes):** TMS envelope + sin^p schedule; `G_TMS` pin; pure-scale stickiness already documented.

---

## 3. Candidate entangling operator law classes (construction dump)

These are **CANDIDATE classes** for kill-seeking scrutiny. **Not** Derived, **not** implemented, **not** claimed to clear T8.

### R2-C1 — Alternate symplectic generator (not pure two-mode squeeze envelope)

| field | content |
|---|---|
| **Idea** | Named generator \(K_{\mathrm{ent}}\) with symplectic structure different from pure TMS envelope blocks; early \(\mathrm{d}S\) growth rate not proportional to present \(G_{\mathrm{TMS}} w_{\mathrm{tms}}(f)\). |
| **Why it might act** | Residual is steep early \(\mathrm{d}S\); different generator can break **ratio stickiness** that pure scale cannot. |
| **can-exist** | Instrument already uses free \(A\) + TMS blocks; alternate symplectic maps are a legal class if N4 holds. |
| **should-not-exist** | Non-symplectic ad-hoc \(S\) clamp; free generator matrix fitted entrywise to [0.10,0.11). |
| **stickiness kill** | If law is still global scale of present TMS → ratio unchanged → DEAD as residual fix. |
| **S⋆-only kill (F1)** | Late entangling boost that inflates \(S_\star\) while early absolute range fixed → **DEAD**. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** |

### R2-C2 — Greybody-fixed multi-channel entangling weights (theory-locked \(\Gamma_j\))

| field | content |
|---|---|
| **Idea** | Channel weights for entangling fixed by derived greybodies / barrier law (not free `TMS_SHAPE_POWER` or hand midband densify). |
| **Why it might act** | Early modes dominate fail window; theory-fixed soft early weights can cap early \(\mathrm{d}S\) while midband peak survives. |
| **can-exist** | \(\sqrt{\Gamma_j}\) already multiplies TMS; spectrum DOF is real (honest form of D3 intent = R6). |
| **should-not-exist** | Hand densify midband fracs as “weights”; barrier params fitted to T8; silent week2 densify. |
| **densify kill** | **ON** — count change without spectrum derivation is D3 thrash **DEAD**. |
| **S⋆-only kill (F1)** | Weighting that only raises peak without cutting early range → DEAD. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** (derivation-first; densify form dead) |

### R2-C3 — Soft early entangling with dump-compensated midband (joint-licensed pair — prefer R5 if non-factorized)

| field | content |
|---|---|
| **Idea** | Soft early \(K_{\mathrm{ent}}\) **plus** independently licensed dump compensation so T2 is recovered — only if both pieces are micro-justified (else becomes D1 thrash). |
| **Why it might act** | Shape/delay thrash showed *direction* (soften early) but not joint optimum under fixed operator class; licensed soft early is the honest form. |
| **can-exist** | D1 family proved early T8 *can* improve; residual forbids only the **header** two-phase thrash, not all soft-early physics. |
| **should-not-exist** | Soft `PHASE1_TMS_FRAC` / TMS delay grid alone (FORBIDDEN thrash); dump compensation as EXTRA_BS thrash. If pair is factorized free knobs, **redirect to R5 honesty**. |
| **joint risk** | Primary — T2/stall historically kill soft-early alone. |
| **S⋆-only kill (F1)** | Soft early that only relocates entropy to peak without early-range cut → DEAD. |
| **Grade** | **FRAGILE-SCHEMA · MISSING_INPUT** (thin ice next to D1; prefer R5 if single-H) |

### R2-C4 — Unitarity-preserving delayed-entangle with interior peak lock

| field | content |
|---|---|
| **Idea** | Theory-fixed delay of entangling onset (not free `TMS_START` thrash) with explicit T1 interior-max lock and T3 credit on \(\mathrm{d}u>0\). |
| **Why it might act** | Fail frames sit at \(f\sim0.057\)–\(0.072\); lawful delay past that window could cap early range if peak still interior. |
| **can-exist** | Window pins are schedule **suggestions** under exploratory protocol if replaced by derived onset. |
| **should-not-exist** | Free `TMS_START` scan; peak moved onto frozen high-\(u\); frozen-\(u\) rise gaming T3. |
| **S⋆-only kill (F1)** | Delay that only reshapes peak height without early-range move → DEAD. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** (onset must be derived, not dialed) |

### Explicitly **not** candidates (killed thrash / densify / fake)

| dead form | why dead |
|---|---|
| Header `G_TMS` pure scale | Ratio sticky ~0.11 |
| `TMS_SHAPE_POWER` / `TMS_START` grid | FORBIDDEN thrash (post-v13) |
| Non-Hamiltonian entropy clamp | Unitarity kill (N4) |
| Mode densify to “soften TMS channels” | D3 densify DEAD |
| Pure \(S_\star\) inflation via late entangle boost | **F1 DEAD** |

---

## 4. can-exist (framework / instrument permission)

- Residual is **steep early \(\mathrm{d}S\)** under present TMS.  
- Pure \(G_{\mathrm{TMS}}\) rescale is **ratio-sticky** (scales \(\Delta S\) and \(S_\star\) together).  
- Different generator / greybody-fixed weights can break stickiness **if** unitarity holds.  
- Shape/delay thrash showed *direction* (soften early) but not joint optimum under fixed operator class.  
- Unitarity N4 constrains legal channels — not unlimited fantasy operators.

---

## 5. should-not-exist (adversarial; includes S⋆-only)

- **Knob laundering:** `TMS_SHAPE_POWER` / `TMS_START` / `G_TMS` retune sold as “new law.”  
- **Peak destruction:** capping early \(S\) kills T1 or moves peak onto frozen high-\(u\).  
- **T3 credit games:** frozen-\(u\) rise that “passes” T8 while gaming T3.  
- **Unitarity smuggle:** non-symplectic ad-hoc maps that lower \(S\) growth without a Hamiltonian.  
- **Densify thrash:** extra modes as fake entangling-channel softener — **DEAD**.  
- **S⋆-only lever (F1):** an “entangling” retune that **inflates late peak \(S_\star\)** without cutting early-bin absolute \(\Delta S\), selling ratio drop as micro win. Under pure TMS scale this is the classic sticky/fake path; under renamed knobs it remains **DEAD** (F1). Must show early-bin **range** moved vs v13.

---

## 6. joint-gate risk

| gate | risk |
|---|---|
| T1 / T3 | Peak / rise credit fail if entangling delayed too hard |
| T2 | Soft early entangle needs dump compensation → stall/T2 stress |
| N4 | Non-unitary “entropy cap” dead on sight |
| T8 mid | Moving peak can open new multivalued windows |
| stickiness | Law remains global TMS scale → residual unchanged |

---

## 7. kill table

| Kill | Trigger |
|---|---|
| Thrash kill | Only header TMS shape/start/G_TMS scan |
| Densify kill | Mode-count densify as entangling “fix” |
| Unitarity kill | Non-Hamiltonian entropy clamp |
| Joint kill | Early T8 pass with T1/T2/stall fail |
| Stickiness kill | Law is still global scale of present TMS |
| **F1 / S⋆ kill** | Only denominator moved; early range flat vs v13 |

---

## 8. Stocked vs MISSING_INPUT (this wave)

| Asset | Status |
|---|---|
| TMS envelope + sin^p schedule | Stocked **instrument** |
| Pure-scale stickiness documentation | Stocked diagnostic |
| Named alternate entangling operator law | **MISSING_INPUT** |
| Unitarity proof sketch for alternate generator | **MISSING_INPUT** |
| Write-once coevolve under new entangle law | **not started** |
| Coevolve production this package | **0** |
| Densify runs this package | **0** |

**Immediate grade:** **SURVIVOR-SCHEMA · MISSING_INPUT · no production**  
**Land this package:** **0**  
**CANDIDATE packet:** **0**

---

## 9. Explicit non-claims

- Candidate classes ≠ Derived entangling law.  
- Soft-early *direction* from thrash history ≠ licensed soft-early law.  
- No invented generator claims T8 pass without instrument.  
- `page_curve_claimed` remains **false**.

---

*End CONSTRUCTION_R2.md. NO FABRICATIONS. Stickiness + densify + F1 fences ON.*
