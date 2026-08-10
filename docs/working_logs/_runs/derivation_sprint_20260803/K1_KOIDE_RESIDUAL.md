# K1 — Koide residual derivation sprint (freeze-time stiffness pair + Wilson gate)

**Date:** 2026-08-03  
**Worker:** blue science (Grok Build subagent)  
**Track:** Derivation sprint K1 (`DERIVATION_SPRINT_BOARD.md`)  
**Hard rules:** NO FABRICATIONS · no invent dark SU(2) A_μ · no MCMC · no free knobs to land Q=2/3 · residual research allowed under tribunal R2-koide-exactness **lane (c)** without grade restore until scored.

**Sources of truth (read this sprint):**
- [`../debt_koide_wilson_20260803/REPORT.md`](../debt_koide_wilson_20260803/REPORT.md)
- [`../debt_koide_20260803/REPORT.md`](../debt_koide_20260803/REPORT.md) (delivery-law section)
- [`../../T6_koide_owed.md`](../../T6_koide_owed.md) — freeze-time / stiffness pair / Branch A
- [`../../../../scripts/koide_equal_quanta_from_adiabaticity.py`](../../../../scripts/koide_equal_quanta_from_adiabaticity.py)

**Run dir:** `docs/working_logs/_runs/derivation_sprint_20260803/`

---

## 0. Re-run status (this sprint)

| Script | Command | Exit code | Log |
|---|---|---:|---|
| Wilson holonomy inventory | `nice -n 19 python3 scripts/koide_wilson_holonomy_inventory.py` | **2** | `koide_wilson_holonomy_inventory.log` |
| Delivery-law discriminator | `nice -n 19 python3 scripts/koide_delivery_law_discriminator.py` | **0** | `koide_delivery_law_discriminator.log` |
| Freeze-time sensitivity (new, bounded) | `nice -n 19 python3 scripts/koide_freeze_time_sensitivity.py` | **0** | `koide_freeze_time_sensitivity.log` |

Exit **2** on Wilson is intentional: gate reports `MISSING_INPUTS` and refuses to invent A_μ / score θ_W.  
Exit **0** on delivery and sensitivity = instruments completed; physics dockets remain open.

---

## 1. What is PAID (disk)

Desk arithmetic, classification, and negative results already on disk — **not** mechanism closure.

| Item | Grade | Evidence (disk) |
|---|---|---|
| Protection half (multiplicative portal → Q invariant) | **PAID** | `debt_koide_20260803/REPORT.md` §1 |
| Fence / Q arithmetic | **PAID** | Q = 0.6666605 ± 6.8×10⁻⁶; A ≈ 1.41420 |
| Equal-stiffness rewrite | **PAID** | A = √2 · (R_c/M_c); residual is R_c = M_c as VEVs |
| #101 structure rewrite | **PAID as classification** | Q=2/3 ⇔ graded null f₀² − \|f₁\|² − \|f₂\|² = 0 |
| #79 magnitude | **CLOSED into #101** | \|f₁/f₀\| = 1/√2 bookkeeping |
| #102 arithmetic / m_τ table | **PAID as measurement table** | θ_B ≈ +0.2222296; not a phase *mechanism* |
| Kernel form 3·θ_B = Q | **PAID as structure IF null sourced** | holonomy *form*, not Wilson evaluation |
| Ring-internal phase candidates | **PAID killed** | φ flat at quadratic; cubic extrema miss 3φ=Q |
| C3 triple-point node as *value* source | **PAID killed** | b=0 → Q=1/3; null is off-node |
| Occupancy lock as exact null escape | **PAID killed** | rational ω₁/ω₀ cannot equal √2 (`occupancy_lock_cannot_deliver.py`; T6 2026-07-29) |
| KZ as exactness rescue | **PAID killed for exactness** | at am=−2 still 1025 ppm (`kibble_zurek_delivery_law.py`) |
| Wilson **bin pre-registration** | **PAID as procedure** | bins + W_hit filed *before* any θ_W; no scoring |
| Observation stiffness pairs (named numbers) | **PAID as named** | radial Hessian k_D/k_S = **1/2**; circulant at Koide **≈0.1213** |
| Equal-quanta → adiabaticity reduction | **PAID as reduction of (P4)** | assembly order + adiabaticity; ramp rate still owed |

**Relation Q=2/3 itself:** measured / arithmetic-paid. Stands as **unexplained regularity** under lane (c).

---

## 2. What is CONTRADICTED (thermal/flat)

Re-run of `koide_delivery_law_discriminator.py` (exit 0) reproduces the exclusion:

| Quantity | Value |
|---|---:|
| T_c = τ m_e | 177.099 keV |
| w₁ = (2/9) T_c | 39.355 keV |
| x₁ = ħ w₁ / k T_c | **0.222222** |
| Q under exact thermal law with ε_D = 2 ε_S | **0.667350286** |
| Target 2/3 | 0.666666667 |
| **miss** | **1025.4 ppm** |
| Claimed exactness budget | 6 ppm |
| Over-budget factor | **~171×** |

**Verdict (unchanged):** thermal/flat equipartition **cannot** carry the null at the claimed exactness at the corpus’s own frequency. Classical equipartition reading under pressure; `a = 3b` is the classical limit, not an exact structural relation.

Sensitivity re-confirm (`koide_freeze_time_sensitivity.py`): same 1025.4 ppm / 171× at fixed x₁. To force thermal Q into 6 ppm at fixed x₁ would require dialing ε_D/ε_S ≈ **2.00411** (not 2) — reported as **dial, not derivation**.

Tribunal stance (T6 header + debt_koide REPORT):  
> Mechanism grade is **not** “candidate” for the thermal/flat path.

---

## 3. Wilson: MISSING_INPUTS list (no θ_W score)

Re-run inventory exit **2**. Pre-registered bins stand; **no holonomy produced**.

### Pre-registered bins (binding; not reopened)

| Bin | Center (rad) | Hit half-width W_hit |
|---|---:|---:|
| HIT_PRIMARY | 2/9 = 0.222222222222 | 2.617994×10⁻⁵ |
| HIT_SIBLING | 2/9 ± 2π/3 | same W_hit |
| ELSE | neither | — |

W_hit = 3 · max(σ_θ_mass, half-millidegree) from corpus-stated uncertainties only.

### MISSING_INPUTS (5/5 block zero-knob score)

| Requirement | Status | Note |
|---|---|---|
| `dark_SU2_A_mu` | **MISSING** | No dark-SU(2) gauge-field archive; T14 `psi_n*.npy` are condensate ψ for H_kin, **not** A_μ |
| `family_cycle_path_C` | **PARTIAL** | Equilateral topology asserted; bare Y c₂≈1.732 ≠ phase-derived c₂≈1.924; using phase-derived c₂ to test 2/9 is circular; spacing not independently fixed |
| `winding_background_n` | **MISSING** | n ≳ 1.65 is a **bound**, not a determination; L_gen unassigned; Widnall n~11–25 is a different object |
| `alpha_d_or_electric_projection` | **PARTIAL** | α_d only bounded (≲2.2); pure-gauge ring collapses (forced combination); hybrid connection not constructed |
| `holonomy_evaluator` | **MISSING** | No zero-knob Wilson-line evaluator; inventory deliberately does not invent one |

**Forbidden circular inputs (refused):** μ_face = (2/9)T_c; θ_hop with μ chosen to land 2/9; c₂ = 4/(3 ln 2) as geometry for a 2/9 test; fit of A_μ/path to lepton masses / arg b.

> **No θ_W. No bin scored. Branch A neither crowned nor killed. #102 phase source UNCHANGED.**

---

## 4. Freeze-time stiffness pair: what the corpus *names* vs what is still unbuilt

### Named on disk (cite)

| Object | What corpus says | Path / lines |
|---|---|---|
| **Third pair problem** | Required ε ratio 2 is **neither** radial Hessian **½** nor circulant Koide **0.1213** — it is a *third* pair | `T6_koide_owed.md` ~L3306–3310 |
| **KZ structural gain** | Under KZ, stiffness **at freeze** (sets amplitude) ≠ stiffness **at observation** (mass formula). KZ *supplies two pairs*; freeze-time pair is the kind of object the third pair would have to be | `T6_koide_owed.md` ~L3498–3502; `scripts/kibble_zurek_delivery_law.py` header L47–52, control K-H |
| **Geometric observation coeffs** | c_S = 6, c_D = 3 → c_D/c_S = ½ | `kibble_zurek_delivery_law.py` L12–14, L76 |
| **KZ closed form** | ε_i(t_i) ∝ c_i^{1/(1+am)}; null needs (c_D/c_S)^{1/(1+am)} = 2 ⇒ **am = −2** (softening) | T6 ~L3466–3481; same script K-C |
| **KZ does not buy exactness** | At am=−2, sectors freeze with ω ratio √2 → **same 1025.4 ppm** | T6 ~L3487–3490 |
| **Shared ramp caveat** | Independent ramps span ratios freely (e.g. 0.224→2.236 class); only shared λ(t) is predictive | T6 ~L3504–3507 |
| **(P4) → adiabaticity** | Equal quanta reduced to assembly order + adiabatic ramp; still needs ramp slow vs ω ≈ 39 keV | `koide_equal_quanta_from_adiabaticity.py` header + §5; T6 ~L2333–2344 |
| **Occupancy lock freeze condition** | Originally: lock needs degeneracy when quanta counted — then **killed**: lock cannot hit √2 at any integer occupancy | T6 ~L3299–3352 |

### Unbuilt (no number without inventing inputs)

| Claimed object | Status |
|---|---|
| Numerical freeze-time stiffness pair (ε_D/ε_S)\|_freeze as a *derived* corpus number | **UNBUILT** |
| Physical quench exponent m (or am) fixed by model dynamics | **MISSING** |
| Independent freeze times t_S, t_D without free ramps | **MISSING** |
| Deposition spectrum at ω_p = 2^{1/4} ω_0 ≈ 33.1 keV | **ABSENT object** (T6: first search finds nothing) |
| Two-temperature freeze T_D/T_S ≈ 0.997936 | **MISSING** (one free number) |
| Ramp duration at freeze in charged-mode periods | **MISSING** (one number would close (P4b) + timescale fork) |

Sensitivity map (`scripts/koide_freeze_time_sensitivity.py`, exit 0) **names** the pairs, re-confirms thermal exclusion, maps am→ratio under fixed c_D/c_S, and **stops** with MISSING_INPUTS rather than inventing a freeze pair.

### Sensitivity snapshot (corpus-fixed; not a mechanism)

| am | freeze ε_D/ε_S (KZ shared ramp) | Q_classical |
|---:|---:|---:|
| −2 | **2.000** | **2/3** (softening, **tuned**, not derived) |
| 0 | 0.500 | 5/3 (law 3 / no-ramp) |
| >0 (stiffening) | <1 | >1 (sign wrong for null) |

At am=−2 + thermal law at x₁=2/9: still **1025.4 ppm**.

---

## 5. Pre-registered next compute that does NOT invent A_μ

| Candidate | Status this sprint |
|---|---|
| Branch A Wilson holonomy, zero free knobs, score HIT_PRIMARY / HIT_SIBLING / ELSE | **BLOCKED** — MISSING_INPUTS (especially A_μ). Pre-registered bins stand; no score until corpus-fixed A_μ + path + n without dials |
| Freeze-time *physical* pair from derived m | **BLOCKED** — m unsupplied; inventing m to hit 2 is a dial |
| Third-class deposition spectrum peak at ω_p | **BLOCKED** — object absent; constructing a spectrum is invention, not lookup |
| Two-temperature freeze | **BLOCKED** as mechanism — T_D/T_S is one free number |
| Adiabaticity check once corpus supplies freeze ramp rate vs ω₁ | **FORMULABLE later** if/when ramp rate is independently fixed; not runnable now without inventing the rate |
| Re-run thermal discriminator / KZ map / sensitivity | **DONE** (instruments only; no new physics claim) |

> **If none exists that is both licensed and unblocked: state it.**  
> **There is no currently runnable zero-knob compute that closes #101/#102 or restores a candidate mechanism without inventing A_μ, m, a deposition spectrum, or a freeze temperature split.**  
> Residual work that remains honest: keep inventories current; do not re-litigate thermal exclusion; do not score Wilson bins.

---

## 6. Explicit non-claims

This sprint does **not** claim:

1. That **#101 is closed.** Graded null is classified, not sourced.  
2. That **#102 is closed.** Brannen 2/9 is measurement-table paid; phase mechanism open.  
3. That any **candidate mechanism is restored.** Lane (c): thermal/flat path **contradicted**; residual research ≠ grade restore.  
4. That **θ_W** was computed or scored.  
5. That a **freeze-time stiffness pair** has a derived numerical value.  
6. That **am = −2** is the model’s freeze law (it is the value KZ *needs* for classical ratio 2 under shared ramp — softening, tuned).  
7. That **occupancy lock** remains a live escape (killed: integers cannot produce √2).  
8. That **adiabatic equal-quanta** is paid without a corpus ramp rate.  
9. That **democratic-graph (P1)–(P4)** is proven.  
10. That inventing A_μ, n ∈ [11,25], or dialing ε_ratio ≈ 2.00411 would be a licensed closure.  
11. Any MCMC / PolyChord / chain result.  
12. That Q=2/3 itself is false — it remains a measured regularity under fence 6.8×10⁻⁶.

---

## 7. Board stamp (K1)

| Outcome | Grade |
|---|---|
| Thermal/flat delivery | **KILLED** (1025 ppm / ~171×) — re-confirmed |
| Wilson gate | **OPEN-BLOCKED** (MISSING_INPUTS; bins pre-registered) |
| Freeze-time third stiffness pair | **OPEN-BLOCKED** (named, unbuilt; sensitivity instrument only) |
| #101 / #102 | **OPEN** (OPEN-THEORY) |
| Mechanism candidate grade | **not restored** |

**Executive one-liner for tribunal:**  
K1 re-confirms thermal exclusion and Wilson block; freeze-time pair remains a named but unbuilt third object; no licensed next compute closes residual without inventing A_μ or freeze dials; #101/#102 still open; no candidate mechanism restored.

---

## Appendix — file inventory this sprint

```
docs/working_logs/_runs/derivation_sprint_20260803/
  K1_KOIDE_RESIDUAL.md          # this report
  DERIVATION_SPRINT_BOARD.md    # board (pre-existing)
  koide_wilson_holonomy_inventory.log
  koide_delivery_law_discriminator.log
  koide_freeze_time_sensitivity.log

scripts/koide_freeze_time_sensitivity.py   # new bounded sensitivity; exit 0
scripts/koide_wilson_holonomy_inventory.py # gate; exit 2 on MISSING_INPUTS
scripts/koide_delivery_law_discriminator.py
```

### Stale-log cure (2026-08-03 16:30) — Claude R2-deriv-K1 AGREE-IF

Older runs of `koide_delivery_law_discriminator.py` printed an epilogue calling the
**occupancy lock the live alternative**. That is **superseded**: occupancy lock was
**KILLED** 2026-07-29 (rational ω₁/ω₀ cannot equal √2). Script epilogue updated this stamp.
Thermal exclusion numbers (1025 ppm / ~171×) are unchanged and still load-bearing.
