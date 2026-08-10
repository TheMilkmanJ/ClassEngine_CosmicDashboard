# T7 — Wilson inputs corpus hunt (file:line)

**Date:** 2026-08-04  
**Package:** `desk_t7_koide_wilson_20260804/`  
**Instrument:** `scripts/koide_wilson_holonomy_inventory.py`  
**This re-run exit:** **2** (expected) — log: [`logs/koide_wilson_holonomy_inventory.log`](logs/koide_wilson_holonomy_inventory.log)  
**Fence:** NO FABRICATIONS · do not invent A_μ / n / α_d / θ_W · exit2 ≠ failure of honesty  

**Prior (parent stamps):**

| Source | Verdict |
|---|---|
| [`../../debt_koide_wilson_20260803/REPORT.md`](../../debt_koide_wilson_20260803/REPORT.md) | 5/5 MISSING_INPUTS |
| [`../koide_residual/WILSON_MISSING_INPUTS.md`](../koide_residual/WILSON_MISSING_INPUTS.md) | reconfirm 5/5 |
| [`../../desk_compute_full_20260804/GRADE_koide.md`](../../desk_compute_full_20260804/GRADE_koide.md) §3.3 | 5/5 |
| [`../../derivation_sprint_20260803/K1_KOIDE_RESIDUAL.md`](../../derivation_sprint_20260803/K1_KOIDE_RESIDUAL.md) | 5/5 |

---

## Scoring convention (this hunt)

| Label | Meaning for zero-knob Wilson |
|---|---|
| **PRESENT** | Corpus-fixed input usable without free dial → **fills** that requirement |
| **PARTIAL** | Something related exists (topology, bound, algebra) but **not** a fixed zero-knob number / field → **still blocks** |
| **MISSING** | No licensed object on disk → **blocks** |

**Count rule for T7 return values:**

- `n_filled` = count of **PRESENT** only  
- `n_still_missing` = count of **PARTIAL + MISSING** (both block zero-knob score)

---

## Hunt table (5 requirements)

### 1. `dark_SU2_A_mu` — **MISSING**

| Probe | Result | file:line / path |
|---|---|---|
| Candidate archives named by inventory | **all ABSENT** | `data/dark_su2_gauge_config.npy`, `data/wilson_Amu.npy`, `data/family_triangle_connection.json`, `output/dark_su2_gauge.dat` |
| `data/` directory | empty of gauge configs | `data/` (dir exists; no SU(2) A archive) |
| T14 `psi_n*.npy` | **exist but are condensate ψ for H_kin, not A_μ** | e.g. `docs/working_logs/_runs/t14_hkin_*/psi_n*.npy` (many); inventory refuse at `scripts/koide_wilson_holonomy_inventory.py:80-94` |
| CLASS “gauge” tests | metric synchronous/Newtonian, **not** Wilson line | `test_gauge_invariance.py:1-12` |
| Inventory status | **MISSING** | `scripts/koide_wilson_holonomy_inventory.py:86-94`; log `logs/koide_wilson_holonomy_inventory.log` |
| Prior debt stamp | **MISSING** | `debt_koide_wilson_20260803/REPORT.md:129` |

**No PRESENT field configuration.** Algebra of adjoints / ε^abc is **not** a gauge-field archive.

---

### 2. `family_cycle_path_C` — **PARTIAL**

| Probe | Result | file:line |
|---|---|---|
| Topology equilateral asserted | present as geometry claim | `docs/working_logs/T6_koide_owed.md:301-306` (Lagrange equilateral) |
| Bare Y/Steiner geometry | √3 ≈ 1.73205 (outside modulus band) | `T6_koide_owed.md:1397-1400` |
| Phase-derived spacing c_K = 4/(3 ln 2) ≈ 1.92359 | **circular if used to test 2/9** | `docs/PRTOE_READERS_GUIDE.md:72`; inventory `scripts/koide_wilson_holonomy_inventory.py:96-106` |
| Modulus band [1.76, 1.97] | locus, **not** a fixed path metric | `T6_koide_owed.md:1204-1206`, `:1265` |
| Inventory status | **PARTIAL** | inventory.py:100-106 |

**Not PRESENT:** no independently fixed face-spacing / path metric that can host a zero-knob line integral without importing the phase target.

---

### 3. `winding_background_n` — **MISSING**

| Probe | Result | file:line |
|---|---|---|
| Canonical n | **bound** n ≳ 1.65, not determination | `docs/working_logs/_CANONICAL_VALUES.md:49` |
| L_gen | **never assigned** | `_CANONICAL_VALUES.md:49`; `docs/PRTOE_baryogenesis.md:59-63` |
| Floor evaluation | n ≳ 1.65 at L ≥ 27.6 Gpc, ξ_K = 256 Mpc | `PRTOE_baryogenesis.md:61-63` |
| Preferred band n ~ 10–30 | unpinned bookkeeping, not fixed n | `PRTOE_baryogenesis.md:239` |
| Widnall n ~ 11–25 | **different object** (genesis vortex azimuthal / CMB comb), not dark-gauge A on family triangle | `docs/PRTOE_DEPENDENCY_TREE.md:74`; inventory note inventory.py:114-117 |
| Inventory status | **MISSING** | inventory.py:110-118 |

**No PRESENT fixed (n, orientation) for family-cycle holonomy.**

---

### 4. `alpha_d_or_electric_projection` — **PARTIAL**

| Probe | Result | file:line |
|---|---|---|
| Stability bound | α_d ≲ 2.2 at working spacing — **window, not fixed coupling** | `docs/exploratory/PRTOE_forced_combination.md:55-56`, table row `:214` |
| Pure-gauge ring | **collapses** (no stationary point) | `PRTOE_forced_combination.md:19-20`, `:50-51` |
| Hybrid required | gauge–superfluid hybrid; **connection not constructed numerically as A** | `PRTOE_forced_combination.md:19-20`, `:54-59` |
| Adjoint ε^abc algebra | exact algebra ≠ field configuration | `PRTOE_forced_combination.md:32-36`, `:40-46` |
| Retracted α_dark ≈ 3.2 | **RETRACTED** (wrong-sign balance) — not a fill | `docs/working_logs/T6_koide_owed.md:1290` (retraction); inventory refuses dial |
| Inventory status | **PARTIAL** | inventory.py:122-129 |

**Not PRESENT:** no fixed α_d and no hybrid connection field on disk.

---

### 5. `holonomy_evaluator` — **MISSING**

| Probe | Result | file:line / path |
|---|---|---|
| Named evaluator candidates | **all ABSENT** | `scripts/koide_wilson_holonomy.py`, `scripts/wilson_family_cycle.py`, `scripts/branch_a_holonomy.py` |
| What exists | inventory **gate only** (never scores θ_W) | `scripts/koide_wilson_holonomy_inventory.py:1-25`, `:132-149` |
| Inventory status | **MISSING** | inventory.py:141-148 |

**No PRESENT zero-knob path-ordered / line-integral evaluator.** Building one *over missing A_μ* would be invention — refused.

---

## Aggregate (this hunt)

| # | Requirement | Status | Fills zero-knob? |
|---|---|---|---|
| 1 | `dark_SU2_A_mu` | **MISSING** | no |
| 2 | `family_cycle_path_C` | **PARTIAL** | no |
| 3 | `winding_background_n` | **MISSING** | no |
| 4 | `alpha_d_or_electric_projection` | **PARTIAL** | no |
| 5 | `holonomy_evaluator` | **MISSING** | no |

| metric | value |
|---|---:|
| **n_filled** (PRESENT) | **0** |
| **n_still_missing** (PARTIAL+MISSING) | **5** |
| Inventory exit | **2** |
| θ_W scored | **0** |
| Bins scored | **none** (HIT_PRIMARY / HIT_SIBLING / ELSE unscored) |

**Change vs debt_koide_wilson_20260803 / koide_residual 2026-08-04:** **none.** Stable 5/5 block.

---

## What would fill each **without free dial**

Licensed fills only. Still forbidden: toy A_μ, dialed n, phase-derived c₂ as geometry for a 2/9 test, α_d bound edge as dial, evaluator that embeds 2/9.

| Input | Licensed fill (examples) | Still forbidden |
|---|---|---|
| **1. A_μ** | External **SU(2) N_f=3 lattice** gauge configs at family-relevant scale; **or** derived dual-superconductor / hybrid orientational connection with **fixed** F_dark/√σ, w·√σ (not a band-as-dial); archival genesis field **if** it is actually dark-SU(2) A, not T14 ψ | Hand-written A_μ; treat ψ as A_μ; fit A_μ to θ_B / lepton masses |
| **2. Path C** | Independently derived face spacing from Y-junction **screened correlator** or lattice geometry — **not** c₂ = Q/τ = 4/(3 ln 2) | Phase-derived c₂ to score 2/9; free path length |
| **3. Winding n** | Completed genesis determination of L_gen → fixed (n, orientation); **or** proof holonomy is n-independent under licensed hybrid | Pick n ∈ Widnall [11,25] to hit 2/9; treat n ≳ 1.65 as fixed |
| **4. α_d / electric projection** | Fixed coupling from lattice / dual-SC profile at **same** scale as A_μ; constructed hybrid connection (pure gauge alone collapses) | α_d bound edge as dial; pure-gauge-only Wilson as if licensed |
| **5. Evaluator** | Zero-knob path-ordered exp / electric line integral **after** 1–4 exist; unit tests on known center elements; continuous non-center angle | Evaluator embedding 2/9; scoring before A_μ exists |

### Minimal licensed sequence

1. Connection (1) + projection (4) from same campaign.  
2. Path geometry (2) independent of phase target.  
3. Fix n or prove n-independence (3).  
4. Run evaluator (5) → θ_W → score pre-registered bins **once**.  
5. HIT_PRIMARY crowns Branch A for **#102 candidate only**; **#101 still open**.

---

## Optional reconfirm: desk audits ≠ mechanism close

| Script | Exit / verdict | What it is | What it is **not** |
|---|---|---|---|
| `scripts/tau_parseval_recompute.py` | PASS exact τ=½ln2 at Q=2/3; `locking_without_Q: OPEN` | Parseval identity **conditional on measured Q**; desk arithmetic | Mechanism for #101/#102; derivation of Q |
| `scripts/koide_lock_algebra_verification.py` | exit 0 algebra (a=3b ⇔ ρ²=1/2; occupancy books) | Desk **algebra audit** under stated premises | Mechanism close; why equipartition / one quantum |

Corpus stamps agreeing: `docs/PRTOE_koide_relation.md:721,735`; `docs/working_logs/_runs/THEORY_WALLS_QUEUE_20260803.md:78-79`; packaging lane (c) **LOCKED**.

---

*End WILSON_HUNT.md*
