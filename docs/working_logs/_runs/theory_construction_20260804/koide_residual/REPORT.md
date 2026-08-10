# Theory construction map — Koide residual #101 / #102

**Date:** 2026-08-04  
**Package:** `docs/working_logs/_runs/theory_construction_20260804/koide_residual/`  
**Worker:** Grok Build subagent (theory construction)  
**Docket:** D5 / T6 — graded null (#101) + Brannen phase (#102) as one node residual  

## Fences (binding)

| Fence | Status |
|---|---|
| NO FABRICATIONS | enforced |
| Do **not** restore thermal delivery as candidate | **LOCKED** — contradicted ~171× |
| Do **not** invent Wilson A_μ / θ_W | enforced; inventory exit 2 |
| Mechanism residual stays **OPEN** | no close this package |
| Packaging lane **(c)** | **LOCKED** (three-seat R2-koide 2026-08-03) |
| Leave MCMCs alone / no PolyChord | observed |

## One-liner residual status

**#101/#102 OPEN-BLOCKED (OPEN-THEORY): protection + arithmetic paid; thermal/flat KILLED; Wilson 5/5 MISSING_INPUTS; packaging lane (c) LOCKED; no mechanism close.**

---

## 0. What this package is

A **construction map**, not a closure. It freezes:

1. what is **derived / paid** on disk  
2. what is **OPEN** (mechanism residual)  
3. what **MISSING_INPUTS** block the Wilson path (from `debt_koide_wilson`)  
4. what residual research scripts **reconfirm** (re-run 2026-08-04 into `logs/`)  
5. honest **construction options** with **no fake close**  
6. explicit **non-claims**

**Sources of truth (read, not rewritten):**

- [`../../debt_koide_20260803/REPORT.md`](../../debt_koide_20260803/REPORT.md)  
- [`../../debt_koide_wilson_20260803/REPORT.md`](../../debt_koide_wilson_20260803/REPORT.md)  
- [`../../../T6_koide_desk_status.md`](../../../T6_koide_desk_status.md)  
- [`../../../T6_koide_owed.md`](../../../T6_koide_owed.md) (header: lane (c))  
- [`../../../../PRTOE_koide_relation.md`](../../../../PRTOE_koide_relation.md) residual freeze 2026-08-04  
- [`../../desk_compute_full_20260804/GRADE_koide.md`](../../desk_compute_full_20260804/GRADE_koide.md)  
- [`../../derivation_sprint_20260803/K1_KOIDE_RESIDUAL.md`](../../derivation_sprint_20260803/K1_KOIDE_RESIDUAL.md)

**Sibling package files:**

| File | Role |
|---|---|
| [`PAID_VS_OPEN.md`](PAID_VS_OPEN.md) | derived vs open ledger |
| [`WILSON_MISSING_INPUTS.md`](WILSON_MISSING_INPUTS.md) | 5/5 gate + unstick without inventing fields |
| [`RESIDUAL_RESEARCH.md`](RESIDUAL_RESEARCH.md) | re-run instruments + logs |
| [`CONSTRUCTION_OPTIONS.md`](CONSTRUCTION_OPTIONS.md) | honest options A/B/C |
| [`NON_CLAIMS.md`](NON_CLAIMS.md) | forbidden closes |
| `logs/*.log` | 2026-08-04 reconfirm stdout |

---

## 1. Residual definition (one node)

| ID | Name | Content | Grade |
|---|---|---|---|
| **#101** | Graded null exactness | What enforces \(f_0^2 - \|f_1\|^2 - \|f_2\|^2 = 0\) (⇔ Q=2/3 ⇔ A=√2) to ~10⁻⁵ **without** equilibrium scatter | **OPEN-BLOCKED** |
| **#102** | Brannen phase source | What sources θ_B = 2/9 as holonomy Q/3 around the cone — **not** independently of #101 | **OPEN-BLOCKED** (same residual) |

**Packaging (lane c):** Q=2/3 stands as **measured / unexplained regularity**; protection derived; thermal/flat **not** a candidate mechanism. Residual research (freeze-time / Wilson inventory) allowed **without grade restore**.

---

## 2. Construction map (summary)

```
PAID ─────────────────────────────────────────────────────────────
  protection (multiplicative portal → Q invariant)
  fence arithmetic (Q, A, m_τ table)
  #101 structure rewrite (null ⇔ Q=2/3) — classification only
  #79 magnitude closed into #101 (τ = ½ln2 bookkeeping IF null)
  #102 measurement table (θ_B, δθ) — not phase mechanism
  holonomy form 3·θ_B = Q — structure IF null sourced
  ring-internal phase / node-as-value / thermal delivery — KILLED
  Wilson bin pre-registration (procedure) — no score
  lock algebra (a=3b ⇔ ρ²=1/2) — algebra only
KILLED ───────────────────────────────────────────────────────────
  thermal/flat delivery @ corpus x₁=2/9: 1025.4 ppm vs 6 ppm (~171×)
  three-draw / SOC / medium-w / virial ring / ring-internal phase
  occupancy lock as live exactness escape (integer ω ≠ √2)
OPEN ─────────────────────────────────────────────────────────────
  #101 mechanism (node / constraint / index / conservation)
  #102 phase source (closes with #101 or not at all)
  freeze-time third stiffness pair (named, unbuilt)
  Wilson Branch A (MISSING_INPUTS 5/5; bins unscored)
  R_c = M_c VEVs; equal-coeff K∼R²,V∼M²; democratic (P1)/(P4)
  locking τ without input Q
BLOCKED (external / non-desk) ────────────────────────────────────
  lattice T_c/√σ (P-048); Belle-II-class m_τ ≲1.4 ppm
```

---

## 3. Reconfirm stamp (this package)

| Script | Exit | Physics |
|---|---:|---|
| `koide_delivery_law_discriminator.py` | 0 | thermal **KILLED** 1025.4 ppm / ~171× |
| `koide_lock_algebra_verification.py` | 0 | algebra **RECONFIRMED**; residual L2 OPEN |
| `koide_wilson_holonomy_inventory.py` | **2** | **MISSING_INPUTS 5/5**; no θ_W |
| `koide_freeze_time_sensitivity.py` (bonus) | 0 | thermal kill + freeze pair **UNBUILT** |

Logs: [`logs/`](logs/).

---

## 4. What would move the residual (no invention)

| Path | License condition | Does **not** alone close |
|---|---|---|
| New scored **#101** mechanism (constraint / index / conservation) forcing null to ~10⁻⁵ without scatter | independent of free dials; survives exactness budget | — (this *is* the close for #101) |
| Wilson Branch A θ_W after **all** corpus-fixed inputs present | score only pre-registered bins; no A_μ invent | #101 still needs exactness source |
| External lattice T_c/√σ (P-048) | crowns/kills τ composite | not #101 mechanism |
| External m_τ refine ≲1.4 ppm | separates Q vs θ_B vs closure watches | not mechanism |

**There is no currently runnable zero-knob compute that closes #101/#102 without inventing A_μ, freeze m, a deposition spectrum, or a T_D/T_S split.**

---

## 5. Executive stamp

| Outcome | Grade |
|---|---|
| Packaging lane (c) | **LOCKED** |
| Thermal/flat | **KILLED** reconfirmed |
| Lock algebra | **RECONFIRMED** (desk only) |
| Wilson | **OPEN-BLOCKED** (5/5 MISSING_INPUTS) |
| #101 / #102 | **OPEN** |
| Mechanism candidate | **not restored** |
| MCMC / PolyChord | **untouched** |

**Do not present Koide as solved.**
