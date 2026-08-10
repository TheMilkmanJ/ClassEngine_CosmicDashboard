# REPORT — Forward ω_J theory construction map

**Package:** `docs/working_logs/_runs/theory_construction_20260804/omegaJ_forward/`  
**Date:** 2026-08-04  
**Mission:** Construction map for **new microphysics** required to un-block forward junction ω_J; candidate roster with honest grades; formulable *structure* only — **no invented χ / pinning-curvature numbers**; **do not** close as Derived.  
**Fences held:** no fabrications; MCMCs untouched; no PolyChord; junction COMPLETE-CONDITIONAL grade not falsely upgraded.

---

## 0. Executive residual (one-liner)

**Forward ω_J remains OPEN-BLOCKED on missing axiom A_ωJ (χ + pinning curvature / J_seat); quartet back-solves at 5.672 keV; accept [3,12] keV, kill &lt;0.057 keV — construction map only, zero non-circular lands.**

---

## 1. Starting point (corpus conclusion, not overturned)

| Prior artifact | Conclusion used here |
|---|---|
| [`../debt_omegaJ_forward_formulability_20260803/REPORT.md`](../debt_omegaJ_forward_formulability_20260803/REPORT.md) | **Zero** non-circular formulable expressions for junction ω_J from stocked objects; names **A_ωJ** |
| [`../debt_baryo_omegaJ_20260803/REPORT.md`](../debt_baryo_omegaJ_20260803/REPORT.md) | Quartet closes with sourced Γ_φ/θ̇; candidate desk roster C0–C8; NI-D3-1 open |
| [`../debt_baryo_d3_provenance_20260803/REPORT.md`](../debt_baryo_d3_provenance_20260803/REPORT.md) | 5.672 keV is back-solve; bands pre-registered |
| `PRTOE_baryogenesis.md` §3a + claims row 6 | Forward micro **OPEN-BLOCKED** #39 |

This package is **construction after formulability failure**, not a second attempt to invent a land from empty shelves.

---

## 2. Package contents

| File | Role |
|---|---|
| [`FORMULABILITY.md`](./FORMULABILITY.md) | Restatement of the block; cites debt_omegaJ_forward |
| [`REQUIRED_INPUTS.md`](./REQUIRED_INPUTS.md) | Exact missing objects; independence; circularity traps |
| [`CANDIDATE_ROSTER.md`](./CANDIDATE_ROSTER.md) | Named seats/expressions graded CANDIDATE / DEAD / MISSING_INPUT |
| [`KILL_AND_BANDS.md`](./KILL_AND_BANDS.md) | Pre-registered [3,12] keV; kill &lt;0.057 keV; forward-land criteria |
| [`logs/baryogenesis_junction_closure.log`](./logs/baryogenesis_junction_closure.log) | Recompute 2026-08-04 |
| [`logs/junction_quartet_closure.log`](./logs/junction_quartet_closure.log) | Recompute 2026-08-04 |

---

## 3. Construction map — what new microphysics must supply

```
                    stocked & closed                    blocked
         ┌─────────────────────────────┐    ┌──────────────────────────┐
         │ Γ_φ = G_F² T_sph⁵           │    │ χ  (junction stiffness)  │
         │ θ̇  (winding @ T_sph)        │    │ J_seat / U_J curvature   │
         │ R_need from η·n (grading)   │    │   OR direct micro ω_J    │
         │ Rectifier R=ω_J²/(2Γ_φθ̇)    │    │         = A_ωJ           │
         │ Overdamped class premises   │    └────────────┬─────────────┘
         └──────────────┬──────────────┘                 │
                        │                                │
                        ▼                                ▼
              R known once ω_J known          ω_J unknown without A_ωJ
                        │                                │
                        └────────────┬───────────────────┘
                                     ▼
                    forward land only if A_ωJ is real micro
                    and ω_J scores under pre-registered band
```

### Layer A — already formulable structure (no new numbers)

1. Overdamped EOM with χ-cancel: φ̇ = −p sin φ − j sin(φ − θ̇t).  
2. Fast-drive R = ω_J²/(2Γ_φθ̇) (0.06% vs integration; m₁ drops out).  
3. Quartet consistency at computed ratio 9.03×10⁷ → back-solve **5.672 keV**.  
4. Definitional identity ω_J² ≡ J_seat/χ **if** both legs exist.

### Layer B — required new microphysics (not stocked)

| Need | Description | Status |
|---|---|---|
| **Seat model completion** | UV/IR content of tenth-channel seat term that generates the cos(φ − θ̇t) junction at T_sph | Portal class selected; **price missing** |
| **χ** | Phase stiffness / decay constant of the *junction formalization’s* visible phase | **Unstated** |
| **Pinning curvature of U_J / J_seat** | Independent cos-term curvature | **Unstated** (stage 7 name only) |
| **Or:** direct micro ω_J | Single number from seat content | **Unstated** |

### Layer C — must not be used as substitutes

Forbidden or dead substitutes catalogued in `CANDIDATE_ROSTER.md` and `REQUIRED_INPUTS.md` (v_L, f→χ, Jeans, m₁, U_pin, η-bootstrap, 1.9 keV artifact, proximity scales).

---

## 4. Candidate roster (headline)

| Grade | Headline |
|---|---|
| **CANDIDATE** | **C1 only:** ω_J² = (seat pinning curvature)/χ — real form, both inputs missing |
| **MISSING_INPUT** | χ, J_seat, C6/C7 proximity forms without chain |
| **DEAD** | C2 Jeans, C3 m₁/θ̇ watch, C4 m₁, C5 v_L ID, C9 f→χ, C10 U_pin, C11 1.9 artifact; seat-trickle; static φ₀ |
| **CIRCULAR** | C0 / C0b / C8 back-solve family |
| **Numeric non-circular lands** | **0** |

Full table: [`CANDIDATE_ROSTER.md`](./CANDIDATE_ROSTER.md).

---

## 5. Kill & bands (headline)

| Disposition | ω_J |
|---|---|
| ACCEPT | **[3, 12] keV** |
| ANOMALOUS-REVIEW | (0.057, 3) ∪ (12, 30] keV |
| KILL | **&lt; 0.057 keV** |
| Forbidden center | 1.90 keV under stale 10⁷ ratio |

Full criteria for “forward land”: [`KILL_AND_BANDS.md`](./KILL_AND_BANDS.md).

---

## 6. Recompute (desk only — not a land)

Commands (2026-08-04):

```bash
nice -n 19 python3 scripts/baryogenesis_junction_closure.py
nice -n 19 python3 scripts/junction_quartet_closure.py
```

| Check | Result |
|---|---|
| Exit codes | **0** / **0** |
| Quartet | **CLOSES** — Γ_φ/θ̇ = 9.03×10⁷; R ≈ 5.05×10⁻⁵ at ω_J = 5.7 keV path |
| Back-solve center | **5.672 keV** |
| Artifact path | ~1.89 keV under shorthand 10⁷ — **not a target** |
| Forward debt printout | “Real debt unchanged: forward ω_J from seat χ + pinning curvature (#39)” |

Logs: [`logs/`](./logs/).

---

## 7. Living-doc pointer

Surgical pointer added on `docs/PRTOE_baryogenesis.md` residual freeze / claims residual for row 6 → this package.  
**Document grade COMPLETE-CONDITIONAL for AD-direct + transmission class is unchanged.**  
Forward row remains **OPEN-BLOCKED**.

---

## 8. Explicit non-claims

- No derivation of ω_J.  
- No invented χ, J_seat, or pinning-curvature values.  
- No adoption of 1.9 keV, √(m₁ Γ_φ), T_on, Jeans, or v_L.  
- No MCMC / PolyChord work.  
- No false promotion of forward ω_J to Derived.  
- Quartet recompute ≠ forward land.

---

## 9. Legal next steps (no invention)

1. Owner / seat-sector write **explicit A_ωJ** from model operators already intended as the seat junction, **or** prove the sector cannot and fire K5.  
2. External micro/lattice only if inputs are already named in corpus.  
3. Keep recomputing quartet as hygiene only.  
4. Pin L_gen / n (#180) for 𝒯 band — does not create ω_J.  
5. Optional hygiene: rename Jeans ω_J → ω_Jeans (non-blocking naming collision).

---

*End REPORT — theory_construction_20260804/omegaJ_forward*
