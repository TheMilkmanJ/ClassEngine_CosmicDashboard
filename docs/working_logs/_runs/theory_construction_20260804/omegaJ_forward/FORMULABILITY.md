# FORMULABILITY — Forward ω_J is blocked on stocked objects

**Package:** `theory_construction_20260804/omegaJ_forward`  
**Date:** 2026-08-04  
**Debt cited:** [`../debt_omegaJ_forward_formulability_20260803/REPORT.md`](../debt_omegaJ_forward_formulability_20260803/REPORT.md)  
**Supporting debts:** [`../debt_baryo_omegaJ_20260803/REPORT.md`](../debt_baryo_omegaJ_20260803/REPORT.md), [`../debt_baryo_d3_provenance_20260803/REPORT.md`](../debt_baryo_d3_provenance_20260803/REPORT.md)

---

## One-line restatement

**Forward junction ω_J is not formulable from objects already stocked in the corpus.**  
Quartet arithmetic closes as a **back-solve**; the rectifier formula is machine-backed; the micro pair (χ, seat pinning curvature / J_seat) that would *price* ω_J without η is **unstated**. Nothing non-circular remains without a new explicit axiom **A_ωJ**.

This package does **not** overturn that conclusion. It maps construction requirements around it.

---

## What the debt report established (H2 / #39)

From `debt_omegaJ_forward_formulability_20260803/REPORT.md`:

| Question | Answer |
|---|---|
| Non-circular forward expression for ω_J from corpus objects alone? | **No** |
| Non-circular formulable expressions found | **0** |
| Single missing axiom | **A_ωJ**: independent micro price of ω_J **or** pair (χ, J_seat) with ω_J² ≡ J_seat/χ, without η / R_need / v_L |
| χ alone formulable? | **No** — cancels in EOM; never priced as this phase’s stiffness |
| Quartet consistent? | **Yes** at Γ_φ/θ̇ = 9.0319×10⁷; ω_J = **5.672 keV** is BACK-SOLVED |

Candidate class counts from that report (do not re-open as lands):

| Class | Count | IDs |
|---|---|---|
| CIRCULAR (η / R_need / tautology / artifact) | 5 | C0, C0b, C3, C8, C11 |
| MISSING INPUT / MISSING AXIOM | 5 | C1, C1χ, C1J, C6, C7 |
| WRONG OBJECT / WRONG SCALE | 3 | C2, C4, C10 |
| FORBIDDEN ID (v_L or f→χ) | 2 | C5, C9 |
| **FORMULABLE non-circular junction ω_J** | **0** | — |

---

## What *is* formulable (structure only — not a land)

These objects are stocked and recomputable; none of them is a forward ω_J:

| Object | Status | Role |
|---|---|---|
| Γ_φ = G_F² T_sph⁵ | COMPUTED | overdamping rate |
| θ̇ at T_sph | COMPUTED | drive |
| R_need ~ 5×10⁻⁵ | FROM η·n band | grades need; **cannot** enter forward price |
| R = ω_J²/(2 Γ_φ θ̇) (fast-drive) | MACHINE-BACKED formula | response, not price of ω_J |
| ω_J = √(2 R_need Γ_φ θ̇) ≈ 5.672 keV | BACK-SOLVED | grading center only |
| Overdamped EOM with χ-cancel | formalization | structure of C1 route |

**Structure that *would* be formulable if A_ωJ were supplied:**

```
U_J   = −χ ω_J² cos(φ − θ̇ t)
ω_J²  ≡ (pinning curvature of U_J) / χ   ≡   J_seat / χ
R     = ω_J² / (2 Γ_φ θ̇)     (p ≪ θ̇ already holds)
```

The algebra is closed. The **inputs** χ and J_seat (or ω_J direct) are not.

---

## Why each “almost land” fails (short)

| Attempt | Failure mode |
|---|---|
| Back-solve C0 / C0b / C8 | Imports R_need / η — circular by construction |
| 1.90 keV (C11) | Stale Γ_φ/θ̇ ~ 10⁷ artifact; R short ×~9 on real ratio |
| m₁ / θ̇ watch (C3) | Stage 8: R carries no m₁ in fast-drive limit |
| Jeans √(4πGρ) (C2) | Wrong object; ~8 orders under at T_sph |
| ω_J ~ m₁ (C4) | Wrong scale; kills if adopted |
| v_L as decay constant (C5) | **FORBIDDEN ID** — declined in #39 |
| f_e-scalar as χ (C9) | Different sector; no map |
| √(m₁ Γ_φ), T_on (C6, C7) | Proximity / chance; no mechanism chain |

---

## Blocking issue (unchanged)

**NI-D3-1 / A_ωJ:** supply independent (χ, J_seat) or micro ω_J from seat content **without** manufacturing IDs, **or** prove the sector cannot — then kill under pre-registered band.

Until then: grade remains **OPEN-BLOCKED (OPEN-THEORY)**, not Derived.

---

## Explicit non-claims

- This file does **not** invent χ or pinning-curvature numbers.
- This file does **not** close forward ω_J as Derived.
- Quartet recompute in `logs/` restates consistency only.
- Junction document grade COMPLETE-CONDITIONAL is **not** upgraded by this package.

---

*End FORMULABILITY.md*
