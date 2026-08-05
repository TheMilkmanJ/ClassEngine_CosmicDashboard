# Wilson MISSING_INPUTS — Branch A holonomy gate (from debt_koide_wilson)

**Stamp:** 2026-08-04 reconfirm  
**Parent:** [`../../debt_koide_wilson_20260803/REPORT.md`](../../debt_koide_wilson_20260803/REPORT.md)  
**Instrument:** `scripts/koide_wilson_holonomy_inventory.py`  
**This package log:** [`logs/koide_wilson_holonomy_inventory.log`](logs/koide_wilson_holonomy_inventory.log)  
**Exit this re-run:** **2** (expected — refuse invent)  

**Fence:** Do **not** invent Wilson A_μ / θ_W. No bin scored without licensed inputs.

---

## 0. What Branch A is testing

Branch A (T6): arg b is a **Wilson-line electric holonomy** of the dark SU(2) gauge field along the family cycle in a recorded winding background — non-center (continuous), so it *can* land at non-quantized 2/9.

\[
\theta_W \;\equiv\; \text{electric holonomy angle of } A \text{ around family cycle } C
\]

**Not tested by inventory:** re-fitting lepton masses; KMS drift with μ chosen to land 2/9; inserting 2/9 into inputs.

A licensed θ_W would score **only** against pre-registered bins (§1). Changing widths after seeing θ_W is forbidden.

---

## 1. Pre-registered bins (binding; unchanged)

| ID | Center | Value (rad) | Meaning |
|---|---|---:|---|
| **θ★₀** | 2/9 | **0.222222222222** | primary Brannen sheet |
| **θ★₊** | 2/9 + 2π/3 | **2.316617324615** | Z₃ sibling (+1 hop) |
| **θ★₋** | 2/9 − 2π/3 | **−1.872172880171** | Z₃ sibling (−1 hop) |

| Symbol | Value | Source |
|---|---:|---|
| σ_θ_mass | 8.348×10⁻⁶ rad | T6 / P-2026-051 pole-mass σ on δθ |
| half-millidegree | 8.726646×10⁻⁶ rad | T6 “2/9 ± 0.0005°” bar |
| **σ★** | 8.726646×10⁻⁶ rad | max of the two |
| **W_hit** | **2.617994×10⁻⁵ rad** | 3·σ★ (pre-registered half-width) |

| Bin | Definition | If scored |
|---|---|---|
| **HIT_PRIMARY** | d(θ_W, θ★₀) ≤ W_hit | Branch A lands Brannen sheet → crowns Branch A for **#102 as phase-source candidate** (does **not** close #101) |
| **HIT_SIBLING** | not PRIMARY; min(d to ± siblings) ≤ W_hit | wrong Z₃ sheet |
| **ELSE** | neither | kills Branch A *for this debt* under zero-knob Wilson reading |

**Non-elastic:** landing within ~10⁻³ of 2/9 but outside W_hit is **ELSE**, not a widened hit.

**This package:** **No θ_W. No bin scored.**

---

## 2. The 5/5 MISSING_INPUTS list

Every requirement is **MISSING** or **PARTIAL**. PARTIAL also blocks a zero-free-knob run.

| # | Requirement | Status | Proof (corpus / inventory) |
|---|---|---|---|
| **1** | `dark_SU2_A_mu` | **MISSING** | No `data/` or `output/` dark-SU(2) gauge archive. Repo `*.npy` under `_runs/t14_*` are condensate ψ fields for H_kin, **not** dark gauge A_μ. `test_gauge_invariance*.py` are CLASS metric gauge tests, not Wilson lines. |
| **2** | `family_cycle_path_C` | **PARTIAL** | Equilateral topology asserted. Bare Y/Steiner geometry gives c₂ = √3 ≈ 1.732; phase-derived c₂ = 4/(3 ln 2) ≈ 1.924 is **circular** if used to test 2/9; modulus band [1.76, 1.97] is not a fixed number. Spacing not independently fixed → zero-knob path metric unavailable. |
| **3** | `winding_background_n` | **MISSING** | Canonical n ≳ 1.65 is a **bound**, not a determination; L_gen never assigned (`_CANONICAL_VALUES.md`). Widnall n ~ 11–25 is genesis vortex azimuthal structure, **not** a dark-gauge background on the family triangle. |
| **4** | `alpha_d_or_electric_projection` | **PARTIAL** | α_d only **bounded** (≲ 2.2 at target spacing). Forced-combination theorem: pure-gauge ring collapses; hybrid connection required and **not constructed** numerically. Adjoint ε^abc algebra is exact but is not a field configuration. |
| **5** | `holonomy_evaluator` | **MISSING** | No prior zero-knob Wilson-line script for the family cycle. Inventory deliberately does **not** invent one over missing A_μ. |

### Forbidden circular inputs (refused)

- μ_face = (2/9) T_c  
- θ_hop with μ chosen to land 2/9  
- c₂ = 4/(3 ln 2) as geometry for a 2/9 test  
- Fit of A_μ or path to lepton masses / arg b  
- Picking n ∈ [11, 25] as “the” winding  

### Verdict (reconfirmed 2026-08-04)

> **MISSING_INPUTS: 5/5 requirements block a zero-free-knob Wilson holonomy.**  
> No θ_W produced. **No bin scored.** Pre-registration stands.  
> **#102 phase source: still open. OPEN-THEORY unchanged. No false closure.**

---

## 3. What would unstick the Wilson path **without inventing fields**

Honest unstick = supply **corpus-fixed or externally measured** inputs that the inventory already names — **not** toy A_μ, not dialed n, not phase-derived geometry used to test the phase.

| Input | Licensed unstick (examples) | Still forbidden |
|---|---|---|
| **1. A_μ / connection** | External **SU(2) N_f=3 lattice** gauge configurations at family-relevant scale; or a **derived** dual-superconductor / hybrid orientational connection with **fixed** F_dark/√σ, w·√σ (not a band used as dial); archival field from a completed genesis sim **if** it is actually dark-SU(2) A, not ψ | Hand-written A_μ; reuse T14 ψ as A_μ; fit A_μ to θ_B |
| **2. Path C metric** | Independently derived face spacing c₂ from Y-junction screened correlator or lattice geometry — **not** c₂ = Q/τ | Using phase-derived c₂ to score 2/9; free path length |
| **3. Winding n** | Completed genesis determination of L_gen → fixed (n, orientation); **or** a proof that holonomy is n-independent under the forced-combination hybrid | Picking n from Widnall band to hit 2/9; n ≳ 1.65 bound as if fixed |
| **4. α_d / electric projection** | Fixed coupling from lattice / dual-superconductor profile at the **same** scale as A_μ; constructed hybrid connection (pure gauge alone collapses) | Using α_d bound edge as dial; pure-gauge-only Wilson as if licensed |
| **5. Evaluator** | Implement zero-knob line integral / path-ordered exponential **after** 1–4 exist; unit tests on known center elements; continuous non-center angle output | Evaluator that embeds 2/9; scoring before A_μ exists |

### Minimal sequence (licensed)

1. Obtain corpus-fixed **connection** (item 1) and **projection** (item 4) from the same external/derived campaign.  
2. Fix **path geometry** (item 2) independently of the phase target.  
3. Fix **n** or prove n-independence (item 3).  
4. Only then run evaluator (item 5) → θ_W → score §1 bins **once**.  
5. Interpret: HIT_PRIMARY crowns Branch A for **#102 candidate only**; **#101 still open**.

### What does **not** unstick (common false moves)

| False move | Why it fails |
|---|---|
| Invent toy constant A_μ so inventory exits 0 | Fabrication; violates NO FABRICATIONS / no invent A_μ |
| Score θ_B measurement table as Wilson | Already paid as table; not mechanism |
| Use KMS form 3·θ_B = Q as Wilson evaluation | Structural identity / ansatz chain, already desk-paid as form |
| Claim #101 closed by a phase hit | Null exactness is a separate source |
| Dial ε_D/ε_S ≈ 2.004 to “fix” thermal then smuggle Wilson | Thermal path already contradicted; dial ≠ derivation |

---

## 4. Relation to #101 / packaging

| Claim | Status after Wilson gate |
|---|---|
| #102 independent of #101 | **No** — closes with the node or not at all |
| Phase hit alone closes residual | **No** |
| Packaging lane (c) | **Unchanged LOCKED** |
| Thermal delivery restored via holonomy story | **Forbidden** |

---

## 5. Cross-check stamp

| Source | 5/5? | Exit |
|---|---|---|
| debt_koide_wilson REPORT 2026-08-03 | yes | 2 |
| desk_compute GRADE_koide 2026-08-04 | yes | 2 |
| derivation sprint K1 | yes | 2 |
| **this package re-run** | **yes** | **2** |

**Stable result:** Wilson path remains **OPEN-BLOCKED** on named MISSING_INPUTS. Residual research keeps the inventory current; it does not invent fields.
