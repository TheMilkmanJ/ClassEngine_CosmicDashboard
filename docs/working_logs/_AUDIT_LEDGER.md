# THE FULL AUDIT — every file, every number (opened 2026-07-17)

*Operator's order: "continue auditing every single file again, regardless of how big of a task it
is. **Accuracy is more important than usage.**"*

## Why the previous audits passed and missed everything

Three prior passes ran to completion and found none of 2026-07-17's defects: **#51** (audience-law
scrub, every doc), **#30** (full docs hygiene), **#24** (re-audit every domain verdict). They failed
for one structural reason: **they checked WORDS.** A stale number looks exactly like a fresh one.
`+3.7σ` does not announce that it came from the step splice; `2.470340` does not announce that its
baseline was withdrawn. **Reading 130 files by eye repeats that failure with more effort.**

## The six species (every 2026-07-17 defect was one of these)

| # | species | example found | how to hunt it |
|---|---|---|---|
| **1** | **stale value** — a retired number quoted as current | `+3.7σ` vs EMPRESS (step-era); the v5 scar −1.2σ in 4 docs | `scripts/value_audit.py` — recompute from standing inputs |
| **2** | **withdrawn baseline** — a number whose *provenance* was retired | D/H 2.470340 (PRyM-default ω_b, process error 38) | trace each number to the run that made it |
| **3** | **retired object cited live** | `f_amp` as a check; `c = 1` as owed | name-grep (the ONE species greps catch) |
| **4** | **self-contradictory row** — two halves disagree by orders of magnitude | "δm_q = ε full → ~1σ nudge" (really +12…+18σ) | evaluate BOTH halves, compare |
| **5** | **arithmetic that does not close** | "2.470340 −(η-flow)→ 2.387" (really 2.4275) | recompute every stated chain end-to-end |
| **6** | **unreachable answer / unsearched debt** — booked "owed" while the answer exists elsewhere | the D/H error budget (cite-verified all along, process error 40); α_c's owner (in a build spec) | before booking an "owed", SEARCH FOR THE NUMBER |

**Species 6 is the one that costs most and is hardest to see:** it is not a wrong statement, it is a
right statement filed where no reader reaches. Two of today's biggest finds were species 6.

## The rule this audit runs under

> **An "owed" is a CLAIM.** It needs a search before it is booked, exactly like a result does. A debt
> asserted in two places is not evidence of absence anywhere else.

## Tiers — ordered by what an error COSTS, not by size

| tier | what it is | files | status |
|---|---|---|---|
| **0** | **leaves the repo; a person reads it and acts** | fairbank_note_draft ✔, README ✔ (first 70 lines; 329 remain), PREREGISTERED_PREDICTIONS, REFEREE_CALENDAR | **IN PROGRESS** |
| **1** | **the spine — everything inherits** | MATH_SPINE, THREE_EQUATIONS, DEPENDENCY_TREE, READERS_GUIDE, INDEX | **IN PROGRESS** — THREE_EQUATIONS + MATH_SPINE audited (all arithmetic recomputed clean; 2 species-4 grade contradictions fixed 2026-07-17); DEPENDENCY_TREE, READERS_GUIDE, INDEX pending |
| **2** | **computational — numbers that get consumed** | bbn_witness, cosmological_constant, neutrino_sector, fingerprint_lattice, CODE_MANIFEST, THE_AMPLITUDE, THE_CHAIN | **IN PROGRESS** — bbn_witness ✔, cosmological_constant ✔ (all arithmetic reverified clean; repair-history scars stripped, grades kept), neutrino_sector ✔ (Σm_ν/m_ββ reverified); CODE_MANIFEST, THE_AMPLITUDE, THE_CHAIN, fingerprint_lattice pending |
| **3** | **domain files** (~40) | hubble_tension, s8_tension, light, quantum_gravity, … | **DONE** — 75 files, 5 parallel agents; all numbers recomputed (numbers flagged not changed), repair-history scars stripped, honest grades kept |
| **4** | **working files** (21) | T1–T16, _master_computes, _cross_cutting | **DONE** — 19 files + REFEREE_CALENDAR; conservative scar pass (debt language kept) |
| **5** | **code + configs** | 55 yaml, 98 py, source/*.c | partial (varconst path done 2026-07-17) |
| **6** | **archive** | provenance only — audit ONLY for "cited as live from a live file" | pending |

## Findings ledger

*(one row per defect; species-tagged; the fix commit)*

| file | species | defect | status |
|---|---|---|---|
| bbn_witness | 2,5 | η-flow spent twice; withdrawn-baseline σ | FIXED (2026-07-17) |
| MATH_SPINE | 1 | `+3.7σ` EMPRESS = step-era value | FIXED |
| PHYSICS_DOMAINS ×3, DOMAIN_COVERAGE | 1 | v5-era scar carried as current | FIXED |
| PREREGISTERED_PREDICTIONS | 3,6 | "exact c owed via threshold matching" — c = 9/10 is derived | FIXED |
| fingerprint_lattice | 4 | quark-bleed row: "ε full" vs "~1σ" | FIXED (symmetry-forbidden) |
| UV_completion | 3,6 | docket premise dead; c = 1 candidate live | FIXED |
| koide_relation | — | 4 stacked dated passes; f_amp cited live | FIXED |
| fairbank_note_draft | 4 | BBN claimed in a favourable fit record | FIXED + gated |
| 13 configs | 2 | YHe/bbn blind to varying_me | FIXED (measured curve) |
| MATH_SPINE, cosmological_constant | 6 | α_c's owner stated only in a build spec | FIXED |
| THREE_EQUATIONS | 4 | stated-stack T_c row: grade cell "derived" vs value cell "not independently sourced" — reader-facing contradiction | FIXED (2026-07-17) |
| MATH_SPINE | 4 | §7d narrative "the SAME **derived** T_c of §4" — "derived" contradicts the file's own flagship-grade block | FIXED (2026-07-17) |
| PHYSICS_DOMAINS | 3 | D/H "healer" (P-006) soft-sold as a live dyad bet — the Majoron forbids the quark coupling; retired to "no healer available to the dyad" (2 spots) | FIXED |
| the_great_chain | 1 | Appendix A stated the DE floor as the **observed** 2.25 meV (model derives 2.284; +1.5% = rounding) | FIXED |
| IMPLEMENTATION_SUMMARY, VALIDATION_RESULTS, derivation, safe_region | 3 | whole files present the **pre-dyad scalar-tensor F(φ)R** model as current ("Complete/Publication-Grade") | FIXED — superseded banners added, files kept as record |

### Flagged for model-judgment (surfaced by the audit; NOT scars/arithmetic — need the operator's call)
- **S₈ three-way**: s8_tension 0.821, s8_growth 0.807, PHYSICS_DOMAINS §3 0.823 — none cross-references the others (may be distinct chains/mechanisms).
- **Σm_ν "pending" framing**: PHYSICS_DOMAINS §8 + DOMAIN_COVERAGE present the ordering race as open, but P-004 (inverted) is falsified and 61.4 meV NO stands — likely stale.
- **honest_status.md** uses a different DE closed form (ρ_Λ¼ = (d/2)α⁴m_e ≈ 2.17 meV, τ-free) than the flagship (9/2)α⁴τ·m_e = 2.284; unreconciled (private ledger, left).
- **scale_ladder** α_c inconsistency (½α_c² printed 2.29×10⁻⁴ from old α_eff=0.0214 vs standing 2.396×10⁻⁴; "3α (0.0073)" mislabel — 0.0073 is α).
- **ς config count**: hubble_tension "180" vs H0_CEILING "162" template-scan.
- **T13 elasticity**: d(D/H)/dε = 0.00782 called "unreproducible" in the top banner yet re-derived correctly ~140 lines later — internal contradiction, needs a script re-run.
- **c_s = √α_c label** 0.146 (should be 0.148); Kaup mass 4 vs 6×10⁹ M☉ (reduced-vs-non-reduced Planck convention).
| **README** | **3** | **ODDS ("~16%") on the repo's front door** — the standing law is that odds are never audience-facing | FIXED |
| **README** | **1** | **sold "a varying-mₑ STEP in cosmic voids" as one of 4 headline bets** — P-022 retired that reading 2026-07-16; the registry now says a sharp global step **counts against** the model | FIXED |
| **README** | **2** | ΔlnZ ≈ +2.6 quoted bare — it came from chains scored with a ΛCDM helium fraction | FIXED (asterisked pending re-run) |

## PRTOE_THREE_EQUATIONS.md — deep audit 2026-07-19

Eleven checks run. Six defects, one of them a flat self-contradiction.

1. **The file contradicted itself on its own headline number.** The banner stated τ sourced by the
   Koide kernel at 0.34657 → T_c = 177.10 keV → +0.44%. The stated-stack table, forty lines later,
   still read "T_c ≈ 179 keV, τ = 0.3503, not independently sourced." Table row rewritten to the
   kernel value with its real referee (an SU(2), N_f = 3 lattice T_c/√σ).
2. **H₀ = 69.9 carried grade "production"** with no provisional flag, while the Fairbank letter
   states the same number as pre-correction and being re-measured. Now flagged in place.
3. **The Σm_ν row credited P-2026-012 with selecting the ordering.** That entry says explicitly it
   does not (ANN-2026-025); the ordering is data-selected. The row also sold the sum as a recorded
   prediction without noting it is not a discriminator — 2.6 meV above the m₁ = 0 floor against
   ~20 meV planned resolution.
4. **Equation 1 still led with 2.284 meV and "agreeing to 1.5%"**, correcting itself inline. Now
   leads with the standing claim, +0.44%.
5. **A_s landed −0.35%; it is −0.34%** (2.081/2.088).
6. **Status marker said the evidence run was in progress "as of 2026-07-13"**; it launched 07-18.

Also: the 42-line grade banner was compressed to 24 and re-pointed. It opened with a warning about
the model's own number being an artifact and spent a page on the archaeology of a rounding — which
is scar, and already lives in the failures ledger (7 references). It now states the standing claim
first, the grade, the referee, and one line marking the superseded figure.

Citations: all eleven present in BIBLIOGRAPHY. Audience laws: clean. Three new regression checks.

**Open, not fixed — for the owner.** z_on appears as 3.5619×10⁷ here and 4.0×10⁷ elsewhere in the
corpus. These look like different objects — the profiled value against the coded H = m identity —
and the file labels its own as profiled, so nothing is stated wrongly. But two numbers 12% apart
under one name is a trap for any reader who meets both, and which is canonical is a judgement I
should not make silently. Filed to ForJustin.
