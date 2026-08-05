# KILL_AND_BANDS — Pre-registered grading for forward ω_J

**Package:** `theory_construction_20260804/omegaJ_forward`  
**Date:** 2026-08-04  
**Registered:** 2026-08-03 (before any forward derivation)  
**Living homes:** `PRTOE_baryogenesis.md` §3a; `scripts/baryogenesis_junction_closure.py`; `debt_omegaJ_forward_formulability_20260803`; `debt_baryo_d3_provenance_20260803`

**Rule:** score any future derivation against this table only — not against whichever target is nearer. Band does **not** create formulability.

---

## 1. Grading center (back-solve only)

| Quantity | Value | Type |
|---|---|---|
| Grading center | **~5.7 keV** (precisely **5.672 keV** from sourced Γ_φ, θ̇, R_need) | BACK-SOLVED |
| Γ_φ/θ̇ used for center | **9.0319×10⁷** (computed), **not** ~10⁷ shorthand | COMPUTED |
| Forbidden alternate center | **1.90 keV** under stale ratio 10⁷ | ARTIFACT — do not grade against |

---

## 2. Pre-registered bands

| Disposition | Derived ω_J | Meaning |
|---|---|---|
| **ACCEPT** | **[3.0, 12.0] keV** | Junction magnitude reading lives (within ~×2 of 5.7 need); transmission class holds at order of the need |
| **ANOMALOUS-REVIEW** | **(0.057, 3.0) ∪ (12, 30] keV** | Neither auto-accept nor auto-kill; retune j/ratio bookkeeping before booking; not a silent redefinition of success |
| **KILL junction route** | **&lt; 0.057 keV** | More than two orders under ~5.7 (×100); pre-committed kill from baryogenesis §3 / §3a |
| **Forbidden target** | 1.90 keV under Γ_φ/θ̇ = 10⁷ | Artifact basin; a land there with *real* Γ_φ is an R shortfall ×~9 |

Notes:

- Accept band is for a **forward-derived** ω_J, not for restating the back-solve.
- 1.9 keV is **not** an accept-band redefinition even though 1.9 ∈ (0.057, 3); if reached via stale ratio it is artifact; if reached via honest micro with real Γ_φ, treat as transmission miss / anomalous-review, not success redefinition.

---

## 3. Kill conditions (class, not only numeric)

Any of the following ends the junction **magnitude** route (or the carrier class, as noted):

| # | Kill condition |
|---|---|
| K1 | **Derived** ω_J **&lt; 0.057 keV** (×100 under ~5.7) |
| K2 | Failure of overdamping premise Γ_φ/θ̇ ≫ 1 at T_sph (currently holds at ~9×10⁷) |
| K3 | Failure of pinning hierarchy m₁ ≪ θ̇ (currently ~3.8×10⁻⁵) |
| K4 | Failure of fast-drive formalization so that R → ω_J²/(2Γ_φθ̇) no longer applies when claimed |
| K5 | Proof that the seat sector **cannot** supply a junction plasma frequency in the keV band without manufacturing IDs (no micro definition reachable) — class fails even if no single number fires K1 |
| K6 | Historical class kills already on books — do not reopen without new inputs: seat-trickle (~26 orders), static φ₀ under uniform winding (≤ H/θ̇) |

**Not a kill by itself:** landing at factor ~3 from 5.7 inside anomalous-review — but must not be used to move the grading center or to adopt the 1.9 artifact.

---

## 4. What counts as **forward land** (promotion criteria)

A result may be booked as **forward ω_J land** (and may then be graded ACCEPT under the band) **only if all** hold:

1. **Expression** from seat microphysics: ω_J or (χ, J_seat) with ω_J² = J_seat/χ (or equivalent micro definition of the seat junction plasma frequency at T_sph).
2. **Independence:** no use of R_need, η, or j-as-back-solved from them in the price (see `REQUIRED_INPUTS.md` I1–I7).
3. **No forbidden IDs:** no silent v_L = decay constant; no silent f→χ without a *named* new axiom graded as axiom (not as derivation from stocked objects).
4. **No wrong objects:** not Jeans √(4πGρ); not U_pin curvature sold as U_J.
5. **Numeric score** against this file’s bands (ACCEPT / ANOMALOUS-REVIEW / KILL).
6. **Perturbative sanity** at the landed value: j/θ̇ ≪ 1 if the overdamped rectifier formula is used (target region ~10⁻⁴ at 5.7 keV).
7. **Provenance labels** preserved: COMPUTED / BACK-SOLVED / SHORTHAND never mixed; forward land is a new type (DERIVED-MICRO or equivalent), not a relabel of C0.

**Explicit non-lands:**

| Claim | Status |
|---|---|
| Quartet closes at 5.672 keV | Consistency only — **not** forward land |
| Rectifier formula verified 0.06% | Formula land — **not** ω_J land |
| √(m₁ Γ_φ) ≈ 3.5 keV | Proximity — **not** land |
| T_on ≈ 9.4 keV | Proximity — **not** land |
| 1.90 keV artifact | **Forbidden** as target |

---

## 5. Relation to document grades

| Item | Grade | Change by this package? |
|---|---|---|
| AD-direct + transmission class document | **COMPLETE-CONDITIONAL** | **No** — do not upgrade falsely |
| Quartet arithmetic | machine-backed back-solve | Recompute only (`logs/`) |
| Forward ω_J (#39) | **OPEN-BLOCKED** / OPEN-THEORY | **Unchanged** until A_ωJ lands or K1/K5 fires |

---

## 6. Script printout (authoritative band text)

From `scripts/baryogenesis_junction_closure.py` (re-run 2026-08-04 → `logs/baryogenesis_junction_closure.log`):

```
ACCEPT junction magnitude:  ω_J ∈ [3.0, 12.0] keV
ANOMALOUS-REVIEW:           ω_J ∈ (0.057, 3.0) ∪ (12, 30] keV
KILL junction route:        ω_J < 0.057 keV  (×100 under ~5.7)
Real debt unchanged:        forward ω_J from seat χ + pinning curvature (#39)
```

---

*End KILL_AND_BANDS.md*
