# The Independence Audit — Which Multi-Way Agreements Are Real, Pair by Pair

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim
> conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> Written 2026-08-02, at the corpus's own red-team review. The motivating precedent is
> recorded in the bibliography: the corpus's finiteness count (str[k₁] = 0 over the Standard
> Model's 48 Weyl fermions) and Navarro-Salas 2024's exact-conformal-symmetry condition were
> briefly held as independent confirmations of the generation count — until the algebra showed
> both collapse to N_½ = 4·N₁ at N₀ = 0. **One equation, two costumes.** That collapse was
> found by accident. This document runs the same check deliberately, on every multi-way
> agreement the corpus quotes, so no "N independent confirmations" claim outlives its
> derivation.

## 0. Two kinds of independence, and both are required

- **Data-side independence:** the targets are separate measurements with unrelated error
  budgets (A_s and n_s are different Planck observables; a lattice T_c and a CMB amplitude
  share nothing).
- **Assumption-side independence:** the derivations reaching those targets do not share a
  load-bearing premise. Two results that ride the same assumption are **one bet counted
  twice at the assumption level**, however independent their data.

A pair earns the word "independent" only when both columns hold. Most of the corpus's
multi-way agreements pass one column and fail the other, and the honest label is stated per
row below.

## 1. The audit table

| # | claimed agreement | data-side | assumption-side | verdict |
|---|---|---|---|---|
| 1 | Finiteness count ↔ Navarro-Salas 2024 conformal condition | — | **collapses**: both are N_½ = 4·N₁ (at N₀ = 0) | **NOT independent. Never quote as two.** The template case ([BIBLIOGRAPHY.md](BIBLIOGRAPHY.md), NavarroSalas2024) |
| 2 | k three ways: gap-equation 1.360 / closed form 1.36461 / A_s-measured 1.3602 ± 0.0064 | measured value is independent data | the gap-equation determination and the closed form are **the same integral** — hierarchy §6c derives the closed form *from* the screened kernel | **Really two-way**: one derivation ↔ one measurement. The hierarchy file already says "one object, three determinations"; the honest count of independent confirmations is **one** (the measurement) |
| 3 | d = 3 three ways: spatial dimension / ρ_Λ-implied 2.993 / anchor-implied 2.921 | ρ_Λ and the anchor are different observables | the floor's d² **is** α_c²/α² by algebra (hierarchy §6g: "not a naming coincidence"); the anchor reading rides the §6f ontology fork | **One definition + one measurement consistency (0.22%) + one conditional outlier (−2.6%).** Not three confirmations |
| 4 | m = 2.24×10⁻²⁰ eV "three uses": onset clock, galactic cores, superradiance band | three genuinely different observables | one committed value, none of the three yet measured; ξ ≡ ħ/(m·c_s) is *defined* from m (circularity found at check 34; "pinned three ways" withdrawn) | **Zero confirmations today — three commitments.** Becomes one confirmation the day any one use is measured; becomes three only if all are, jointly |
| 5 | Σm_ν twice: P-2026-012 (relation) and P-2026-004 (ordering collision) | same eventual referee data | separated by ANN-2026-025: the ordering comes from P-2026-004 only; P-2026-012 does not fix it | **Genuinely two distinct bets** — but on the *same* future measurement, so they can pay at most once each, not corroborate each other now |
| 6 | T_d/√σ two routes: 0.483 read directly / 0.487 through r₀ | **fails**: both numbers descend from the same improved-staggered lattice lineage; same-ensemble identity not established (docket note, 2026-07-29) | different arithmetic paths only | **One source, two arithmetic paths. Count as one.** |
| 7 | τ = ½ln2 twice: the Koide kernel and the ρ_Λ quartic | ρ_Λ is measured; the Koide relation is measured | one number doing two jobs by construction — a **commitment**, exactly like row 4; and the pairing shell's ln 2 brush was inspected and recorded closed (match is to 2τ; convention artifact) | **A joint constraint, not two confirmations.** Its strength is prospective: a τ-lock derivation would have to satisfy both at once |
| 8 | A_s, n_s, the Koide power reading, the hierarchy 3/2 | four separate measured targets | **all four ride the corpus's one shared additivity** (hierarchy §2: "one bottleneck, not four") | **Data-independent, assumption-correlated.** As evidence *for the additivity*: four joint hits, genuinely strong. As four independent successes of the model: no — one assumption failing anywhere takes all four |
| 9 | α_c = 3α four places: ε, the ρ_Λ floor, A_s, the anchor exponent | four separate observables | one committed coupling; the anchor's use additionally rides the §6f ontology horn; the ρ_Λ use rides τ (row 7) | **The corpus's strongest joint object, quoted with its riders.** The clean joint is ε–A_s (different epochs, different physics, same value). The other two uses carry named conditions and must be quoted with them |
| 10 | ΣY² = 10 validated by the hypercharge beta coefficient b_Y = 41/6 | the Standard Model's own structure — external to this corpus | the validation uses no corpus assumption | **Genuinely independent, and small.** A real external check of one counting step, not of the model |

## 2. What the table changes about quotation practice

1. **The corpus currently has exactly one fully independent external validation** (row 10),
   and it is minor. Every other multi-way agreement is either a joint constraint on a shared
   object (rows 7–9), a commitment awaiting measurement (rows 4, 5), or an overcount (rows
   1–3, 6).
2. Joint constraints are not weaker than independent confirmations — they are *different*:
   they concentrate risk. The correct forward-facing sentence for rows 8–9 is "N observables
   jointly constrain one object," never "N successes." The trials-factor document
   ([PRTOE_TRIALS_FACTOR.md](PRTOE_TRIALS_FACTOR.md) §4b) prices why joint fits carry weight;
   this table is the register of which joints are real.
3. Any future claim of the form "X and Y independently give Z" must add a row here, with
   both columns filled, before it appears in a forward file. The Navarro-Salas collapse was
   found by accident; the next one should be found by this table.

## 3. Standing exposure this audit does not discharge

The audit checks pairwise collapse among *recorded* agreements. It cannot rule out an
unrecorded shared premise — an assumption two derivations both use without either naming it.
The shared additivity (row 8) was itself carried silently for weeks before being named as one
bottleneck; the velocity condition v = 1 in the hierarchy kernel was likewise carried
silently until 2026-07-28. The honest statement is that this table is complete over *named*
premises as of its date, and that both prior discoveries of silent sharing were made by
whole-file re-reads — which is the standing check-12 sweep, still in progress.

## Sources

Internal: [PRTOE_hierarchy_problem.md](PRTOE_hierarchy_problem.md) (§2, §6c, §6g),
[PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md), [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md),
[PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md) (standing; P-004 and other rehomed IDs also in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md); P-012,
ANN-2026-025), [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md),
[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) (NavarroSalas2024). External: Navarro-Salas, *Class.
Quantum Grav.* (2024), arXiv:2403.13201.
