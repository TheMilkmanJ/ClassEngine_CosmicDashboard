# RESIDUAL RESEARCH — freeze-time / null instruments reconfirm

**Stamp:** 2026-08-04  
**Package:** `theory_construction_20260804/koide_residual`  
**Rule:** re-run = instrument health + number stability. **exit 0 ≠ physics PASS.** Residual research **without grade restore** (lane c).

---

## 0. Required re-runs (mission)

| # | Script | Expected | This package exit | Log |
|---|---|---|---:|---|
| 1 | `scripts/koide_delivery_law_discriminator.py` | 0; thermal kill | **0** | [`logs/koide_delivery_law_discriminator.log`](logs/koide_delivery_law_discriminator.log) |
| 2 | `scripts/koide_lock_algebra_verification.py` | 0; algebra PASS | **0** | [`logs/koide_lock_algebra_verification.log`](logs/koide_lock_algebra_verification.log) |
| 3 | `scripts/koide_wilson_holonomy_inventory.py` | **2**; MISSING_INPUTS | **2** | [`logs/koide_wilson_holonomy_inventory.log`](logs/koide_wilson_holonomy_inventory.log) |

**Command pattern:** `nice -n 19 python3 scripts/<name>.py` → stdout teed into `logs/`.

### Bonus residual instrument (same freeze lane)

| Script | Exit | Log |
|---|---:|---|
| `scripts/koide_freeze_time_sensitivity.py` | **0** | [`logs/koide_freeze_time_sensitivity.log`](logs/koide_freeze_time_sensitivity.log) |

---

## 1. Delivery-law discriminator — thermal / flat **KILLED**

**Purpose:** Can thermal equipartition carry the null at the corpus’s own frequency and claimed exactness?

### Reconfirm numbers (this run = prior)

| Quantity | Value |
|---|---:|
| T_c = τ m_e | 177.099 keV |
| w₁ = (2/9) T_c | 39.355 keV |
| x₁ = ħ w₁ / k T_c | **0.222222** |
| x₀ = x₁/√2 | 0.157135 |
| n̄ charged | ≈ 4.02 (not ≫ 1) |
| Q under exact thermal, ε_D = 2 ε_S | **0.667350286** |
| Target 2/3 | 0.666666667 |
| **miss** | **1025.4 ppm** |
| Claimed exactness budget | 6 ppm |
| Over-budget | **~171×** |
| x₁ needed for ≤6 ppm (at ratio 2) | ≤ 0.016971 (~13× smaller) |

**Epilogue (lane c, post-occupancy kill):**  
Occupancy lock is **not** a live escape (integer ω₁/ω₀ ≠ √2, killed 2026-07-29). Residual exactness research = freeze-time stiffness / Wilson bins only — **not** a restored candidate mechanism.

**Physics grade:** thermal/flat delivery **KILLED reconfirmed**.  
**Forbidden:** restore thermal as candidate.

---

## 2. Lock algebra verification — algebra **RECONFIRMED**, residual OPEN

**Purpose:** Closed-form check of a=3b ⇔ ρ²=1/2, occupancy algebra under N₀=1, and ω₁=(2/9)T_c bookkeeping.

### Reconfirm

| Step | Result |
|---|---|
| (1) a = 3b ⇒ ρ² = 1/2 at every scale; τ = ½ln2 = 0.346574 | **✓** |
| converse ρ² = 1/2 ⇒ a = 3b | **✓** |
| (2) N₀=1 and E_c=ħω₁ ⇒ f₀² = \|f₁\|²+\|f₂\|² scale-free | **✓** (algebra under premises) |
| (3) ω₁ = (2/9)·177.10 keV = 39.356 keV | **✓** bookkeeping |

**Script verdict (quoted):**  
> both load-bearing steps verify from their premises in closed form; the physics questions (why thermal equipartition; why one quantum — T6 residual L2 and survival test) unchanged and open.

**Physics grade:** algebra **RECONFIRMED**.  
**Does not pay:** #101/#102 mechanism; residual L2 OPEN.  
**Forbidden:** “algebra PASS ⇒ mechanism close.”

---

## 3. Wilson holonomy inventory — **exit 2**, MISSING_INPUTS 5/5

**Purpose:** Prove whether corpus-fixed inputs exist for zero-free-knob Branch A; refuse to invent A_μ or score θ_W.

### Pre-registered (documentation only; no scoring)

| Item | Value |
|---|---|
| θ★_primary | 2/9 = 0.222222222222 rad |
| θ★_sibling± | 2/9 ± 2π/3 |
| W_hit | 2.617994×10⁻⁵ rad |
| Bins | HIT_PRIMARY \| HIT_SIBLING \| ELSE |

### Requirements this run

| Requirement | Status |
|---|---|
| dark_SU2_A_mu | **MISSING** |
| family_cycle_path_C | **PARTIAL** |
| winding_background_n | **MISSING** |
| alpha_d_or_electric_projection | **PARTIAL** |
| holonomy_evaluator | **MISSING** |

**MISSING_INPUTS: 5 of 5.** No θ_W. No bin scored.  
Full table + unstick without inventing: [`WILSON_MISSING_INPUTS.md`](WILSON_MISSING_INPUTS.md).

**Physics grade:** **OPEN-BLOCKED** (expected instrument nonzero).  
**Forbidden:** invent A_μ; treat exit 2 as failure to fix rather than successful gate.

---

## 4. Freeze-time sensitivity (bonus) — named, unbuilt

**Purpose:** Map classical/thermal Q vs freeze stiffness ratio and KZ am→ratio using **only** corpus-fixed numbers; stop on MISSING_INPUTS rather than invent a freeze pair.

### Paid / reconfirmed by instrument

- Observation pairs named: radial Hessian **1/2**; circulant Koide **≈0.1213**  
- Thermal exclusion at x₁: same **1025.4 ppm / ~171×**  
- KZ shared-ramp map: am=−2 → freeze ratio 2 (softening **tuned**, not derived); at am=−2 + thermal still 1025.4 ppm  
- Dial report: ε_D/ε_S ≈ 2.00411 would force thermal into 6 ppm at fixed x₁ — **dial, not derivation**

### MISSING for a *physical* freeze pair (instrument list)

| Object | Status |
|---|---|
| physical quench exponent m / am from dynamics | MISSING |
| independent freeze times t_S, t_D | MISSING |
| deposition spectrum at ω_p = 2^{1/4} ω₀ | ABSENT |
| two-temperature split T_D/T_S | MISSING |
| ramp rate at freeze vs ω₁ | MISSING |
| dark SU(2) A_μ (Wilson, out of scope here) | MISSING |

**Physics grade:** freeze-time third pair **OPEN-BLOCKED** (named, unbuilt). No freeze-pair number invented.

---

## 5. What residual research **may** do vs **must not** do

| May | Must not |
|---|---|
| Re-run inventory / discriminator / freeze sensitivity | Restore thermal grade |
| Keep pre-registered Wilson bins current | Score θ_W without licensed inputs |
| Name freeze-time pair as research object | Invent am, A_μ, spectrum, T_D/T_S to “close” |
| Document new scored mechanisms if they appear | Fake close of #101/#102 |
| External lattice / m_τ watches | Touch MCMC / PolyChord / chains |

---

## 6. Aggregate reconfirm

| Outcome | Grade |
|---|---|
| Thermal/flat | **KILLED** reconfirmed (1025.4 ppm / ~171×) |
| Lock algebra | **RECONFIRMED** (desk); L2 OPEN |
| Wilson gate | **exit 2** · MISSING_INPUTS **5/5** |
| Freeze-time pair | **UNBUILT** |
| #101 / #102 | **OPEN** |
| Mechanism candidate | **not restored** |
| Packaging lane (c) | **LOCKED** |

**There is no currently runnable zero-knob residual script that closes the residual.** Instruments only reconfirm the freeze.

---

## Appendix — log inventory

```
docs/working_logs/_runs/theory_construction_20260804/koide_residual/
  RESIDUAL_RESEARCH.md
  logs/
    koide_delivery_law_discriminator.log   # exit 0
    koide_lock_algebra_verification.log    # exit 0
    koide_wilson_holonomy_inventory.log    # exit 2
    koide_freeze_time_sensitivity.log      # exit 0 (bonus)
```
