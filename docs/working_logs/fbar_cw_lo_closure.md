# Track A3 — f̄ LO / c_w residual / leading-order dominance (2026-07-31)

Code: `scripts/fbar_cw_lo_closure.py` (self-checking controls A–J).  
Depends on: C8–C9 / C16 in `family_coupling_lagrangian_spec.md`,  
`cw_response_from_backreaction.py`, `cw_response_bracket.py`,  
`fbar_leading_order_price.py`, ε stack (c·f̄·α_c).

## Result (headline)

| piece | status | content |
|---|---|---|
| f̄ form = ⟨\|cos\|⟩ = 2/π | already settled | mass-positivity + equidistribution; data rejects RMS |
| **LO dominance of \|x\| over c_w x²** | **proved as bound** | expansion param = ε; worst quad/lead ≤ 2.0% on data band |
| **form of c_w** | **mechanism exhibited** | medium back-reaction: c_w = −a exactly |
| **value of a (= −c_w)** | **named residual** | ensemble a ∈ [0.32, 1.36]; fit a ≈ 1.80 (1.9σ tension) |

**Grade: CANDIDATE CLOSED** — mechanism exhibited; one named residual (value of a), data-refereed.  
Not Derived: a is not fixed by recorded couplings. Not inflated: residual is stated, not averaged away.

## 1. Leading-order dominance (proved, not assumed)

Write the fractional mass shift against the winding projection x = ε·cos θ:

> δm/m = \|x\| + c_w·x² + O(x³)

After equidistributed θ-average (⟨\|cos\|⟩ = 2/π, ⟨cos²⟩ = ½):

> f̄_eff = 2/π + c_w · ε / 2  
> quadratic / leading = \|c_w\| · ε · (π/4)

| input | value |
|---|---|
| ε = 27α/(5π) | 1.2543% |
| unit-\|c_w\| quad/lead | **0.985%** (C9 corrected; old 0.83% was 2/3·ε booking slip) |
| ensemble \|c_w\| band | 0.32 – 1.36 → quad/lead **0.32 – 1.34%** |
| fit-implied \|c_w\| = 1.80 | quad/lead **1.77%** |
| C8 wide floor \|c_w\| = 2 | quad/lead **1.97%** |
| cubic/lead at \|c_w\|=1.80 (c₃=a²) | **0.034%** |

**Conclusion:** LO dominance is a *bound* forced by ε ≈ 1.25% and the O(1) character of the data on c_w. It does not need the un-built family-coupling Lagrangian. The residual deficit of measured f̄ against 2/π (−1.8% fit, −0.8% ensemble) is the expansion's own next term at the predicted size — evidence *for* the leading-order reading, not against it.

## 2. Form of c_w — medium back-reaction (C16)

Bare response linear in the rectified amplitude, F₀(u) = u = \|x\|. Medium back-reacts in proportion to the response it already carries, strength a:

> F = F₀ − a·F₀·F  ⇒  F = u/(1 + a u)  ⇒  **c_w = −a exactly**

Solved by bisection in the harness (not quoted). Consequences:

- The even part C8 demanded is a *resummation*, not a new operator.
- Sign of c_w is predicted **negative**; data agrees.
- Whole series fixed from one number: c₃ = c_w², c₄ = −\|c_w\|³.
- Odd responses (tanh u, u/√(1+u²)) are structurally c_w = 0 and are excluded by the ensemble band — and are not of resummed type.

## 3. Value of a — named residual (not forced by recorded couplings)

Candidates built from the ε-stack and natural O(1)s:

| candidate | value | in ensemble a ∈ [0.32, 1.36]? |
|---|---|---|
| α_c = 3α | 0.0219 | no (far too small) |
| ε | 0.0125 | no (far too small) |
| a = 1 (unit back-reaction) | 1.00 | **yes** |
| a = 1/2 (ln / 1−e⁻ᵘ family) | 0.50 | **yes** |
| π/4, 2/π, √2−1 | 0.41–0.79 | yes (numerology, not forced) |

**No unique a is forced.** α_c and ε are not the back-reaction scale. Multiple natural O(1)s sit inside the ensemble band; that is a residual, not a derivation.

Data-refereed (do **not** average the two readings — they disagree):

| determination | c_w | a = −c_w |
|---|---|---|
| winding ensemble (n≥4) | −0.84 ± 0.52 | **[0.32, 1.36]** |
| fit-implied | −1.80 | **≈ 1.80** |
| separation | | **1.9σ** of ensemble error |

This residual does **not** threaten f̄ = 2/π: any O(1) a leaves the identification standing to ~1%. Only \|c_w\| ~ 100 would break the expansion (anti-control in the script).

## What this does *not* claim

- **a is derived** — it is not; deriving the medium's back-reaction strength remains the single open number inside a named mechanism (docket #55's remaining object).
- **Zero free parameters for the ε-stack** — c = 9/10 is still a counting assumption (Track B); α_c's same-response identity is A4.
- **The two c_w determinations agree** — they do not; the tension is booked, not resolved by averaging.

## Kill conditions

1. A measurement of f̄ at a different ε shows a deficit that does **not** scale as c_w·ε/2 (not a subleading term).
2. Medium calculation returns \|a\| ≫ 10 (expansion broken).
3. Ensemble and fit-implied reconcile only at a \|c_w\| that breaks the LO bound (quad/lead ≳ 5–10%).

## Cross-links

- Spec C8–C9, C16: `family_coupling_lagrangian_spec.md`
- Back-reaction form: `scripts/cw_response_from_backreaction.py`
- Response bracket: `scripts/cw_response_bracket.py`
- LO price: `scripts/fbar_leading_order_price.py`
- f̄ check: `scripts/winding_fbar_spatial.py` (0.63137 ± 0.00328, 1.6σ from 2/π)
- Hunt §1: `PRTOE_DERIVATION_HUNT.md`
- Board: `_E2E_DERIVATION_BOARD.md` A3
