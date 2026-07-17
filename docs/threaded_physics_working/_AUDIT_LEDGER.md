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
| **2** | **computational — numbers that get consumed** | bbn_witness, cosmological_constant, neutrino_sector, fingerprint_lattice, CODE_MANIFEST, THE_AMPLITUDE, THE_CHAIN | pending |
| **3** | **domain files** (~40) | hubble_tension, s8_tension, light, quantum_gravity, … | pending |
| **4** | **working files** (21) | T1–T16, _master_computes, _cross_cutting | pending |
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
| **README** | **3** | **ODDS ("~16%") on the repo's front door** — the standing law is that odds are never audience-facing | FIXED |
| **README** | **1** | **sold "a varying-mₑ STEP in cosmic voids" as one of 4 headline bets** — P-022 retired that reading 2026-07-16; the registry now says a sharp global step **counts against** the model | FIXED |
| **README** | **2** | ΔlnZ ≈ +2.6 quoted bare — it came from chains scored with a ΛCDM helium fraction | FIXED (asterisked pending re-run) |
