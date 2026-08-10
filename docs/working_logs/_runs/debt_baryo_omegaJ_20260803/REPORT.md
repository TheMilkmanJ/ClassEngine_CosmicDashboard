# Debt D3 — Baryogenesis ω_J residual (first-principles attack)

**Date:** 2026-08-03  
**Status:** OPEN-THEORY (forward ω_J still missing; quartet *arithmetic* closes)  
**Rules held:** no MCMC/PolyChord; no kill processes; no fake close  
**Scripts run:**
- `nice -n 19 python3 scripts/baryogenesis_junction_closure.py`
- `nice -n 19 python3 scripts/junction_quartet_closure.py`
- `nice -n 19 python3 scripts/winding_turn_budget.py` (context only; does not set ω_J)
- desk numerics for candidate expressions (inline below)

**Primary sources:**
- [`docs/PRTOE_baryogenesis.md`](../../../PRTOE_baryogenesis.md) §3–3a
- [`docs/working_logs/the_transfer_integral_spec.md`](../../the_transfer_integral_spec.md) stages 6–8
- [`docs/working_logs/PRTOE_session_2026-07-29b_findings.md`](../../PRTOE_session_2026-07-29b_findings.md) #39
- [`docs/working_logs/_AUDIT_LEDGER.md`](../../_AUDIT_LEDGER.md) 2026-07-28 #39 entry
- [`docs/exploratory/PRTOE_sqrt3_derivation.md`](../../../exploratory/PRTOE_sqrt3_derivation.md) (Jeans naming collision)

---

## 1. Quartet state (reproduced)

### 1a. Shorthand run — `baryogenesis_junction_closure.py`

Uses the *recorded tilde* quartet as written in early summaries:

| member | recorded value |
|---|---|
| ω_J | 5.7 keV |
| j = ω_J²/Γ_φ | 6 meV |
| Γ_φ/θ̇ | ~10⁷ |
| R needed | 5×10⁻⁵ |

Algebra: once j is fixed, R collapses to **j/(2θ̇)** so ω_J cancels from R and the four numbers over-determine three unknowns. Taking any three and predicting the fourth:

| take | predicts | vs recorded | miss |
|---|---|---|---|
| ω_J, j, ratio | R = 5.54×10⁻⁶ | 5×10⁻⁵ | **×9.03 short** |
| j, ratio, R | ω_J = 1.897 keV | 5.7 keV | **×3.004 low** |
| ω_J, j, R | Γ_φ/θ̇ = 9.03×10⁷ | 10⁷ | **×9.03 high** |
| ω_J, ratio, R | j = 18.0 meV | 6 meV | **×3.004 high** |

**One number, four faces:** factor ~9 in R ≡ √9 ≈ 3 in ω_J. This is exactly what the owner-queue and ForGrok&Claude “quartet miss ×9” line refer to.

### 1b. Sourced run — `junction_quartet_closure.py` (canonical)

Compute Γ_φ and the ratio from their own inputs rather than the OOM shorthand:

```
Γ_φ = G_F² T_sph⁵
    = (1.1663787×10⁻⁵)² · (131.7)⁵ GeV
    = 5.3902×10⁹ eV   (matches recorded ~5.4×10⁹)

θ̇  = 59.68 eV         (deep-frozen winding at T_sph)

Γ_φ/θ̇ = 9.0319×10⁷    ← not 10⁷
```

With the **computed** ratio, the quartet closes simultaneously:

| member | value | status |
|---|---|---|
| Γ_φ | 5.3902×10⁹ eV | derived (Fermi + T_sph) |
| θ̇ | 59.68 eV | derived (winding at T_sph) |
| R | 5.0499×10⁻⁵ | matches needed ~5×10⁻⁵ |
| ω_J | **5.672 keV** | back-solved; agrees with stated 5.7 to 0.5% |
| j | 6.028 meV | follows from ω_J |

The “factor 9” is **exactly** the compression of 9.03×10⁷ → ~10⁷. The transfer-integral spec already stated “overdamped by 9e7” (stage 7); the owner-queue OOM dropped the leading 9.

**Artifact check:** imposing ω_J = 1.90 keV with the *real* Γ_φ, θ̇ yields  
R = 5.61×10⁻⁶ → **8.91× short** of the need. So 1.90 keV is not an alternate physical target; it is what you get by forcing the rounded ratio.

### 1c. Related quick script — `winding_turn_budget.py`

Confirms the winding bookkeeping the θ̇ input rides on (at T_sph: θ̇/H ~ 2.4×10⁶ → ~3.8×10⁵ turns per Hubble; freezes below ~1.7 MeV). Does **not** price ω_J; kept as integrity check that the drive side of the rectifier is not the open residual.

---

## 2. Candidate first-principles expressions for ω_J (corpus-cited)

The rectifier formula (stage 8 / baryogenesis §3) is:

> R = ω_J² / (2 Γ_φ θ̇)  (fast-drive limit p ≪ θ̇)

with the overdamped formalization

> U_J = −χ ω_J² cos(φ − θ̇ t),  j ≡ ω_J²/Γ_φ,  p ≡ m₁²/Γ_φ

What is **derived**: given a sinusoidal seat junction + ν-sector overdamping, the rectified transfer is that formula, verified to 0.06% against direct integration (`scripts/kapitza_junction_response.py`). What is **not derived**: a forward price of ω_J from seat microphysics.

### Candidate roster

| ID | Expression / object | Corpus home | First-principles? | Role for #39 |
|---|---|---|---|---|
| **C0** | ω_J = √(2 R_need Γ_φ θ̇) ≈ 5.672 keV | `PRTOE_baryogenesis.md` §3a; `junction_quartet_closure.py` | **No** — back-target from η/n | grading target, not a land |
| **C1** | Micro definition: ω_J from seat **decay constant + pinning curvature** (or equivalent J, χ with U_J = −χ ω_J² cos …) | `PRTOE_baryogenesis.md` §3a; session #39 | **Yes, in principle** — but **both inputs unstated** in corpus | THE open derivation |
| **C2** | Jeans ω_J = √(4πG ρ) = √(3/2) H | `PRTOE_sqrt3_derivation.md`; coincidence / prereg docs | Yes for **Jeans** growth | **Naming collision only** — different object, ~8 orders under target at T_sph (and ~36 orders vs DE-era Jeans scale elsewhere) |
| **C3** | Leading factor m₁/θ̇ with O(1) F (stage-7 Kapitza watch) | `the_transfer_integral_spec.md` stage 7; `diode_mechanism_pricing.py` | Was candidate | **Killed by stage 8**: overdamped pinning enters as m₁²/Γ_φ, not m₁; R carries no m₁ |
| **C4** | ω_J ~ m₁ = 2.25 meV | neutrino / seat m₁ books | No | 2.5×10⁶ under target; fails kill |
| **C5** | Identify decay constant with v_L (MeV / GeV / 2.4 TeV corners) then invent χ | neutrino-sector v_L corners | Explicitly **declined** as manufactured | session #39: “declined to assume v_L is the decay constant” |
| **C6** | Dimensional guess √(m₁ Γ_φ) ≈ 3.5 keV | nowhere as a derivation | Speculative only | within ×2 of target by chance; no mechanism chain |
| **C7** | Scale proximity to T_on ≈ 9.4 keV (amplitude freeze) | transfer-integral timing wall | No identity claimed | within ×1.7; not identified as ω_J |
| **C8** | Geometric mean √(θ̇ Γ_φ) = 567 keV; then ω_J = √(2R)·that | pure algebra of C0 | Tautology of back-solve | not independent |

**Honest boundary (stage 8, transfer integral spec):** the mapping into the overdamped equation is the standard formalization of the named class, but it is a formalization. The sector must still supply the seat junction’s plasma frequency from microscopic content.

---

## 3. Numerical evaluation of candidates (desk, &lt;10 min)

Inputs fixed to sourced values:  
Γ_φ = 5.3902×10⁹ eV, θ̇ = 59.68 eV, R_need = 5×10⁻⁵, m₁ = 2.25 meV, H(T_sph) ≈ 2.44×10⁻⁵ eV, T_on ≈ 9.4 keV.

| candidate | number | vs 5.672 keV | verdict |
|---|---|---|---|
| C0 back-solve √(2R Γ θ̇) | **5.672 keV** | 1.00 | closes quartet; not forward |
| C0 with rounded ratio → “1.90 keV” | 1.897 keV | 0.33 | artifact; R short ×8.9 on real Γ_φ |
| C2 Jeans √(3/2) H at T_sph | 2.98×10⁻⁵ eV | 5.3×10⁻⁹ | wrong object; fails kill by >> 10² |
| C4 ω_J ~ m₁ | 2.25×10⁻³ eV | 4.0×10⁻⁷ | fails kill |
| C3 stage-7 watch m₁/θ̇ | 3.77×10⁻⁵ (dimensionless R) | n/a | stage 8 killed as mechanism leading factor |
| C6 √(m₁ Γ_φ) | 3.48 keV | 0.61 | no derivation; do not adopt |
| C5 √(m₁ v_L) MeV corner | 0.097 keV | 0.017 | near kill edge; manufactured ID |
| C5 √(m₁ v_L) GeV corner | 1.50 keV | 0.26 | manufactured ID |
| C5 √(m₁ v_L) 2.4 TeV | 73.5 keV | 13 | manufactured ID |
| C7 T_on | 9.4 keV | 1.66 | proximity only |
| C8 √(θ̇ Γ_φ) | 567 keV | 100 | = target / √(2R); tautology |

**None of C2–C8 is a legitimate first-principles land of the junction plasma frequency.** C1 remains the only real route and is blocked by missing micro inputs (decay constant, pinning curvature / seat J and χ).

Perturbative-validity check at the target (stage 8): j/θ̇ ≈ 6 meV / 60 eV ≈ 10⁻⁴ ≪ 1 — OK if ω_J lands near 5.7 keV.

---

## 4. Is restating the target to 1.9 keV legitimate, or fudging?

**Verdict: fudging. Do not restate.**

Reasons, in order:

1. **Sourced ratio dissolves the miss.** Γ_φ/θ̇ is not free to OOM accuracy; it is G_F² T⁵ / θ̇ = **9.03×10⁷**. With that value, ω_J = 5.67 keV, j = 6.03 meV, and R = 5.05×10⁻⁵ close together (`junction_quartet_closure.py`; `PRTOE_baryogenesis.md` §3a).

2. **1.9 keV fails the transmission it pretends to close.** Using real Γ_φ and θ̇, R(1.9 keV) ≈ 5.6×10⁻⁶ — **~9× short** of the η-implied need. The only way 1.9 “closes” is to keep the *wrong* ratio 10⁷ while changing ω_J — i.e. to fix one recording error by introducing another.

3. **Protocol 40 / check-23 class.** This is the documented failure mode: a factor inferred from a quantity quoted to one figure, then attributed to physics (`_AUDIT_LEDGER.md` 2026-07-28; junction_quartet_closure header). Same day the harness already carries the correction under `junction quartet` checks.

4. **What is still open is not which number to move.** Three of four quartet members are independently derived (Γ_φ, θ̇, R_need-from-η·n-band). ω_J is the *one* back-derived member. Moving the target to 1.9 would grade a future derivation against the wrong need and hide a 9× transmission deficit.

5. **Kill threshold is untouched either way** (factor 3 ≪ 10²), so restating is not forced by kill arithmetic — only by the desire to “close” a non-discrepancy.

**Legitimate statement:** target remains **~5.7 keV (precisely 5.672 keV from sourced inputs)**. Status remains **back-target, not a land**. Residual is forward micro derivation (C1), not quartet consistency.

---

## 5. Kill conditions and NEXT ISSUE

### Kill conditions (pre-committed; unchanged)

From `PRTOE_baryogenesis.md` §3 / §3a and transfer-integral stage 7–8:

1. **Derived ω_J more than two orders below ~5.7 keV** (i.e. ≲ 57 eV) ends the junction route.
2. **Failure of the overdamped-junction class premises:**
   - overdamping Γ_φ/θ̇ ≫ 1 at T_sph (holds at 9×10⁷);
   - pinning hierarchy m₁ ≪ θ̇ (holds at 3.8×10⁻⁵);
   - in the overdamped formalization, p/θ̇ ≪ 1 so R → ω_J²/(2Γ_φθ̇) (holds at 1.6×10⁻¹⁷).
3. **If the seat term cannot supply a junction plasma frequency in the keV band at all** (no micro definition reachable without manufacturing IDs), the carrier class fails even if no single number fires (2).
4. Historical class kills already on the books (do not reopen without new inputs): spontaneous-leptogenesis seat trickle (26 orders), static φ₀ under uniform winding (≤ H/θ̇, 2 orders under).

**Not a kill:** landing at 1.9 keV (factor ~3) — but that number is the wrong grading target (see §4); a honest derivation at 1.9 with real Γ_φ would be an **R shortfall ×9**, which is still inside the old “factor 100 acceptance” band for the naive gap but **fails** the stage-8 need R ≈ 5×10⁻⁵ at the 10× level. Treat a 1.9 land as a **transmission miss**, not a redefinition of success.

### What is closed vs open

| item | state |
|---|---|
| Quartet arithmetic with sourced Γ_φ/θ̇ | **CLOSED** (no ×9 physics miss) |
| Rectifier formula R = ω_J²/(2Γ_φθ̇), m₁-independence | **CLOSED** (0.06% numerical) |
| Mechanism class (driven overdamped junction) | **SELECTED** by elimination |
| Forward ω_J from seat microphysics | **OPEN-THEORY** |
| n / L_gen pin (affects 𝒯 target band) | **OPEN** (docket #180; prerequisite for final η verdict) |

### NEXT ISSUE (falsifiable, no fake close)

**NI-D3-1 — Seat micro price of ω_J (blocking).**  
Write and compute a *forward* expression

> ω_J² = (pinning curvature of U_seat) / χ  or  ω_J² = J_seat / χ

with **both** of:

- χ (or equivalent phase stiffness / decay constant of the visible-side junction phase), and  
- the seat coupling J (or curvature of the cos(φ − θ̇t) term)

sourced from existing corpus objects **without** new unstated identifications (in particular: no silent “decay constant = v_L”).

**Pass criterion:** derived ω_J within a factor ~ few of 5.67 keV (and thus R within a few of 5×10⁻⁵).  
**Fail / kill criterion:** derived ω_J ≲ 57 eV, or proof that the corpus cannot supply (χ, J) without manufacturing.

**NI-D3-2 — Hygiene (non-blocking, owner decision).**  
Resolve the ω_J naming collision (Jeans √(4πGρ) vs junction plasma frequency) in live docs — same symbol, unrelated objects (`_AUDIT_LEDGER.md` 2026-07-28). Suggest: keep ω_J for junction; rename Jeans to ω_Jeans or Γ_J.

**NI-D3-3 — Upstream band (does not replace NI-1).**  
Pin L_gen / restate n as the bound it is (#180). Moves 𝒯 and therefore the exact keV target, but does not create a first-principles ω_J.

### Explicit non-claims (anti-fake-close)

- This report does **not** derive ω_J.
- This report does **not** adopt 1.9 keV.
- This report does **not** identify v_L, T_on, or √(m₁ Γ_φ) with ω_J.
- The residual remains **OPEN-THEORY** until NI-D3-1 lands or kills.

---

## Appendix A — command log (stdout abbreviated)

```
$ nice -n 19 python3 scripts/baryogenesis_junction_closure.py
  R short by x9.025; omega_J low by x3.004; ratio high by x9.025; j high by x3.004
  internally consistent value under rounded ratio: 1.90 keV

$ nice -n 19 python3 scripts/junction_quartet_closure.py
  Gamma_phi/thetadot = 9.0319e+07
  omega_J required = 5671.8 eV = 5.672 keV
  VERDICT: THE QUARTET CLOSES. There is no factor-9 discrepancy.

$ nice -n 19 python3 scripts/winding_turn_budget.py
  at T_sph: theta_dot/H = 2.4e+06 → 3.820e+05 turns per Hubble
  (drive-side integrity only; does not set omega_J)
```

## Appendix B — file map

| path | role |
|---|---|
| `scripts/baryogenesis_junction_closure.py` | shows ×9 under OOM ratio |
| `scripts/junction_quartet_closure.py` | dissolves ×9 with sourced ratio |
| `scripts/kapitza_junction_response.py` | R formula + 0.06% verification |
| `scripts/diode_mechanism_pricing.py` | class A/B/C elimination (B’s old m₁/θ̇ form superseded) |
| `docs/PRTOE_baryogenesis.md` §3a | canonical “closed vs missing” statement |
| `docs/working_logs/the_transfer_integral_spec.md` | stages 6–8 mechanism record |

---

*End REPORT — debt_baryo_omegaJ_20260803*
