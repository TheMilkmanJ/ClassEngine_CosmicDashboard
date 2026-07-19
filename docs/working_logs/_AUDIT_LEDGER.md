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

## PRTOE_MATH_SPINE.md — deep audit 2026-07-19

Eleven checks. Nine defects, two of them contradictions between sections of the same file.

1. **§0 graded the dyad mass MEASURED on inverted arithmetic** — "the free-z_on optimizer landing
   7.5517 (→ m = 2.29×10⁻²⁰, 2% above the coded pin)". Recomputed, 7.5517 implies 1.75×10⁻²⁰,
   **22% below**. The grade now stands on three independent uses that do confirm it: ξ = 402 AU
   (returns 398), the Schive core radius (7.14 vs 7.0 pc), and the superradiance window (exact).
   The old basis is marked corrected, not dropped.
2. **§9's ledger credited "dyad onset derived (electron-CW)"** while §4 retires the electron-CW
   route as BBN-fatal. Same file, sixty lines apart. Now credits the Koide kernel's T_c.
3. **§7 read as live for eighty lines** before its own addendum reports the internal falsifier fired
   and Route-D dead. The verdict is now hoisted to the head of §7, where a reader meets it first.
4. **§4's T_c = 179 keV** contradicted the file's own banner (177.10 from the kernel). Fixed, as was
   the same stale value in §22 — with the BBN conclusion checked for sensitivity: the 1.06% change
   moves T_c's position in the 800→70 keV window by 0.3%, so the verdict is untouched.
5. **§6 credited P-2026-012 with selecting the ordering**, which that entry says it does not
   (ANN-2026-025); and sold Σm_ν without noting it is not a discriminator.
6. **§6's "dark-energy-value problem (§2)"** pointed at this file's §2 (radiation youth) rather than
   `neutrino_sector` §2 where the problem is actually stated.
7. **The 42-line grade banner** — the same scar THREE_EQUATIONS carried — compressed to 24 and
   re-pointed at the standing +0.44% claim.
8. **Two inline "+1.5% is the τ rounding" asides** retired to the standing claim.
9. **§2 said "coded z_rad_onset = 4×10⁷"** without noting that the running evidence job is frozen
   at 3.5619×10⁷. Both facts now stated with which configs use which.

The z_on question this file surfaced was settled by computation rather than filed: three
independent pins put the mass at 2.24×10⁻²⁰ and the onset at 4.03×10⁷. Five checks added,
including two that assert the run's implied mass misses ξ.

Citations: all present. Audience laws: clean after the banner compression.

## PRTOE_THE_AMPLITUDE.md — deep audit 2026-07-19

Twelve checks (check 12, the post-edit re-read, added during this file's pass). Four defects, all
four in the §2 windows table — the file's self-summary, which is where the pattern says to look.

1. **The ε-dipole carried the superseded sizing.** δm_e/m_e ≈ 6×10⁻⁷, where P-2026-024's own
   amendment (2026-07-17) rescaled it to **4×10⁻⁷** — the Jeans growth rate is √(3/2), not √3. The
   registry had been corrected; the audience-facing summary had not.
2. **H₀ = 69.9 unflagged**, same as the two flagships carried before today.
3. **"ε, A_s, n_s, z_on all stated in advance"** — z_on is the one that is not, being frozen
   0.053 dex off the onset identity. Now excepted explicitly.
4. **T_c ≈ 179 keV** in §3, against the standing 177.10.

Verified and correct as written: the ΔΦ composition-cliff fence, which the whole gate argument
rests on — f_lep = m_e/2m_u recomputes to 2.743×10⁻⁴ against the recorded 2.74, and
√(f_lep·ε₀)·c returns **553 km/s exactly**. The pure-hydrogen bound returns 782 against the
recorded 779, inside the constants' rounding. That fence is sound.

Citations present. Audience laws clean. Check 12 found nothing further in this file.

**Check 12's first catch was in THREE_EQUATIONS, not here** — my own status marker still read "z_on
stated in advance" three edits after I had written the opposite into the stack table two rows above.
Both lines mine, same file, contradicting. That is the case for the check existing.

## PRTOE_honest_status.md — deep audit 2026-07-19

Twelve checks. Four defects, and the most consequential one runs in the model's **favour** — which
is its own kind of failure for a board whose job is to be the candid record.

1. **The code-vs-theory audit was stale in the model's disfavour.** Its 2026-07-08 entry called
   m_e/dcdf independence "the BIGGEST gap" and concluded that "part of the competitive-with-ΛCDM
   result comes from the extra freedom of 2 independent knobs." Re-checked: `thermodynamics.c` still
   has zero dcdf references, so the code-level link genuinely is unenforced — but
   `cmp_prtoe_fixed.yaml` now sets `varying_me: 1.012543`, **pinned at the derived stack**. The
   extra-knob criticism is retired, and its companion inverts: the amplitude derivation is not
   untested by the fit, it is the fit's fixed input, which is the harder test. A board that
   under-rates the model is as wrong as one that over-rates it, and stays wrong longer because
   nobody goes looking.
2. **The superradiance band read 2×10⁸–3×10⁹ M☉** against three other files' 6×10⁸–3×10⁹.
   Recomputed from α_g = Mm/M_Pl² over the efficient ℓ = m = 1 range α_g ∈ [0.1, 0.5]: **5.96×10⁸ to
   2.98×10⁹**. This board was the outlier.
3. **"PolyChord has not been run"** — it has, since 07-18. Corrected, with the fuller picture the
   board did not have: only the evidence job is live; routeD, conv_desi, zon_disp, zon and twist are
   all stopped.
4. **The dark-energy closed form carried the cruder τ ≈ 1/3 form**, (d/2)α⁴m_e = 2.174 meV at 0.97×.
   Same structure with τ approximated; the kernel supplies τ = ½ln2 exactly and the agreement goes
   from −3% to +0.44%.

Check 12 caught a dangling reference inside my own repair — the rewrite said "consequence (b) as
written above" after I had deleted the text listing (a) and (b). Second time in two files that the
post-edit read caught my own work.

Three checks added (139 total).

## Check 13 — first application, back to THE_AMPLITUDE (2026-07-19)

The protocol gained a thirteenth check: **a file's own owed items are work orders**, and a file is
not closed while it still carries the blanks it started with. Outcomes allowed: closed (computed),
reduced (follows from something already in hand), or gated (named the specific external thing it
waits on). "Owed" alone is none of those.

**First application, and it closed by reduction — the item was misidentified.**

`THE_AMPLITUDE` §5 read: *"The chain now hangs on one underived number — the bounce's
stiffness-ceiling scale (~1.6×10¹⁶ GeV) — queued as a named computation."*

That scale appears **once in the whole corpus**, in that sentence. No script computes it. Neither
does the pour scale (8×10¹⁶ GeV) it was paired with. So I checked the A_s closed form term by term
against `DERIVATION_HUNT`, which is its authoritative source:

- **k = ln(1 + π/2α_c)/π = 1.36461**, and it evaluates *identically* to the screened-interaction
  integral (1/π)∫₀¹dq/(q + 2α_c/π) — verified numerically, difference < 10⁻⁹. Inside the Eliashberg
  window [1.35, 1.37], so it is a derived coupling rather than a landing fit.
- 4π is the standard one-loop factor; the cube is the three spatial dimensions.
- Assembled: **A_s = 2.0807×10⁻⁹ against the frozen 2.088×10⁻⁹ — −0.35%.**

**No pour scale and no stiffness ceiling enter at any step.** The chain does not hang on the number
§5 named. The genuine residual is the one `DERIVATION_HUNT` states: the shot-noise count's exact
O(1) normalisation — whether the assembly is exactly (4πk/α_c)³ — which is precisely what the
−0.35% measures.

So the file was carrying an orphan scale as its single outstanding debt while its real residual sat
one document away, already correctly stated. Four checks added pinning the chain end to end.

## Check 13, second application — MATH_SPINE's owed ledger (2026-07-19)

**Five of its six debts were already paid.** The ledger listed them as outstanding anyway, each
tagged "(docketed)".

**There is no docket document in this corpus.** The word appears ~25 times across 12 files and
points at nothing — the third dead-reference pattern found today, after `def357` / `def-quiet` /
`def-atom-night` and THE_AMPLITUDE's orphan stiffness scale. Its effect here was to make five open
debts look tracked when nothing was tracking them.

Checked one by one:

| debt | actual status |
|---|---|
| KP self-consistency | **resolved in this same file** — §7a reports the attempt fails, the addendum reports the full-cycle solve firing the falsifier. Listed as owed eighty lines below its own answer. |
| spurion identification | done — `neutrino_sector` §2, μ as a dimension-1 L-breaking parameter distinct from ε |
| low-scale seesaw | **adjudicated** by the seesaw duty scan, same file |
| leptophilia portal | established — `dyad_gas` §2, census-forced and leptophilic across sectors |
| the gate-0 confirm | #40 confirms rather than decides (§4) |
| the DE value if Route-D dies | **genuinely open**, falls back to constitution |

Rewritten so each debt names where it closed or what it waits on. Two further genuine debts promoted
out of the prose into the ledger where they belong: the density-dependent screening form (§5) and the
seat constant b.

The pattern worth carrying forward: **"owed" survives long after the work is done**, because closing
a debt happens in the file where the work lands and nobody walks back to the summary that was
tracking it. Every ledger in this corpus should be assumed stale in the direction of *over*-stating
what is outstanding.

## PRTOE_DEPENDENCY_TREE.md — deep audit 2026-07-19

Thirteen checks. Five defects, and every one of them **under-graded** the model. For a file whose
sole job is conditionality mapping, and whose own reading rule is "a claim's effective confidence =
its weakest parent," a stale grade does not sit still — it propagates upward.

1. **f̄ = 2/π graded [C], with "the winding sim" named as a parent.** Both flagships say the
   opposite and say it explicitly: derived from the winding's many-turn equidistribution, and
   *"the sim is the check, not the source"* — THREE_EQUATIONS goes as far as "**not a simulation
   output**". Regraded [D] with the sim moved to where it belongs.
2. **ε therefore carried [D-C-R] instead of [D-D-R].** Two of its three factors are derived; the
   weakest parent is α_c, so the stack's effective grade is [R] and it stands or falls with the α_c
   chain. Stated that way now, which is both more accurate and more falsifiable.
3. **ρ_Λ still read "T_c ≈ 179 keV is the observed ρ_Λ inverted-and-rounded, so the 1.01× is not a
   sourced prediction."** Superseded: the kernel sources τ = ½ln2, giving 177.10 keV and +0.44%,
   with nothing cosmological in the chain. Regraded [D].
4. **The superradiance band read 2×10⁸–3×10⁹ M☉** — the same outlier `honest_status` carried. It is
   6×10⁸–3×10⁹ from α_g = Mm/M_Pl² over α_g ∈ [0.1, 0.5].
5. **The mass's basis understated.** It was credited to the onset clock alone, which invites "one
   fit fixes it". Three independent uses confirm it — ξ = 402 AU, the Schive radii, the superradiance
   window — and that is a much stronger footing to state.

Check 13: the row carrying "ONE number owed (the T_pour ceiling scale)" is the orphan dissolved in
THE_AMPLITUDE's pass. Marked not-a-debt with the reason, so it stops being inherited.

**The session's clearest pattern, now seen four times:** this corpus drifts pessimistic. Ledgers
over-state debts (MATH_SPINE: five of six already paid), status boards under-rate closures
(honest_status: three), and the dependency map under-grades derivations (here: all five). Every
instance reads as caution and none of them gets caught by re-reading, because nobody audits a claim
that errs modestly.

## PRTOE_READERS_GUIDE.md — deep audit 2026-07-19

Thirteen checks. Three defects. The pessimistic drift again, and this time in the file a newcomer
opens first.

1. **The symbol table gave τ = 0.3503.** That table's stated purpose is "one symbol, one meaning",
   which makes a stale value there worse than elsewhere — it is the page a confused reader is sent
   to. τ is ½ln2 = 0.34657, sourced by the Koide kernel; 0.3503 was the observed dark-energy density
   inverted and rounded.
2. **"What remains owed there is the screening computation itself"** — flatly contradicted by
   `honest_status`, which records (2026-07-18) that the screening computation "is delivered on all
   four of its items." The reader-facing guide was telling newcomers a closed item was open.
   Replaced with what actually remains, which is observational: the 21-cm edge shape and the DESI
   forest cross-calibration.
3. **ε appeared as both "≈ 1.24%" and "1.2543%"** in the glossary and the symbol table, with nothing
   saying why. They are the fitted value and the derived stack; the ~1.8% gap between them sits
   inside the posterior width and is the thing the running chains grade. Now said.

Check 13: the two remaining "owed"-class statements are correct and stay — the A_s count's O(1) and
the medium's reality as a named open assumption.

Fifth consecutive file drifting the same way. Worth stating as a rule now rather than a repeated
observation: **in this corpus, a claim's recorded grade is a lower bound on its actual grade.** Any
audit that only checks for over-claiming will pass files that are wrong.

## PRTOE_INDEX.md — deep audit 2026-07-19

Thirteen checks. Three defects, all staleness in the one-line descriptions — and structurally the
cleanest file so far, which is worth recording as a result rather than a non-event.

1. **The quartet clock was advertised as an open question** with its 7.59/7.74/7.89 lineup, when the
   file itself resolves it in §4a: the unit is the **pair**, derived — quartets need attractive
   pair–pair coupling and the recorded real sound speed forces λ > 0, so they cannot bind; the Z4
   term locks phases, not composites. §4b marks the lineup superseded. Retitled and restated.
2. **The cosmological constant carried the retired "+1.5% is the τ rounding" reading.** Now the
   kernel-sourced +0.44%, graded CANDIDATE rather than EXPLORATORY, with its lattice referee named.
3. **The registry range read P-001 → P-2026-052.** It runs to P-2026-055.

**Structurally clean:** zero dead links across every path it lists. Four live documents are not
referenced, and all four are deliberate — `honest_status` ("PRIVATE — unlinked from the
reader-facing shelf on purpose"), `fairbank_note_HOLD` ("Internal. Not part of the letter"), and two
session-findings working logs.

Note for the second pass: this file's defects were **all** in the description strings, none in its
structure. An index rots at the sentence that summarises a file, not at the pointer — which is the
same lesson as the ledgers and status boards, one level up.

## PRTOE_PREREGISTERED_PREDICTIONS.md — deep audit 2026-07-19 (part 1: the lattice bet)

2,711 lines, 51 numbered entries. Probed with the values verified earlier today rather than read
linearly. **The sharpest finding in the corpus so far, and it is in the file whose integrity the
whole falsifiability case rests on.**

**P-2026-048 registers T_c/√σ = 0.3503 ± 0.02 as the model's prediction. The flagship files now say
"0.3503 kills both."** Both statements are current in the repository; they cannot both be right.

Untangled, and it is subtler than a contradiction:

| | τ = T_c/√σ | T_c | what it is |
|---|---|---|---|
| observation-inverted | 0.34506 | 176.33 keV | the observed ρ_Λ read backwards |
| **the Koide kernel** | **0.34657** | **177.10 keV** | **the standing prediction** |
| P-048 as registered | 0.35030 | 179.00 keV | superseded — 179 keV was the rounding |

The kernel's value **is inside** P-048's window [0.330, 0.370], so the entry is not violated. Its
central value is simply the old one.

**But the tolerance cannot resolve the test.** The prediction sits +0.44% above the
observation-inverted value — that gap *is* the dark-energy prediction. P-048's ±0.02 is ±5.7%,
**thirteen times wider**. So a lattice landing anywhere in the window scores as confirmation,
including the value meaning "the model only read the observation back." P-048 saw this coming — its
own text warns "a return at 0.345 does not confirm this entry" — but the registered tolerance does
not enforce its own warning.

**What the test actually needs is 0.44% on T_c/√σ.** Published determinations typically carry 1–3%.
So the honest status is that this test may not be performable at the precision the claim requires,
and recording that beats banking a confirmation the tolerance cannot earn.

Filed as **ANN-2026-026**; P-048 left as registered. The SU(2)/N_f = 3 structural result
(str[k₁]_dark = 0 forcing the only integer solution) is untouched and stands on its own. Four checks
added (147 total).

*This is check #10 — "is the distinctive content actually distinctive" — finding its second victim
today, after Σm_ν. Both times the answer was: the prediction is real, and the instrument named to
test it cannot see the difference that matters.*

## PRTOE_PREREGISTERED_PREDICTIONS.md — deep audit 2026-07-19 (part 2: the sweep)

Swept all 51 entries against the values verified earlier today, and separately against the live data
for every entry that has any.

**Numbers: clean apart from P-048.** Four entries flagged by the probe; three were false positives —
two matches landed inside my own ANN-2026-026 text, and one caught "6×10⁻⁷" inside the comb's
unrelated "4.6×10⁻⁷". P-2026-024 carries its rescaled ε-dipole correctly, with the predecessor
sizing marked as predecessor. Only P-048 needed the annotation.

**That is worth stating rather than passing over: the registry's numeric content held up where every
summary file did not.** Frozen entries do not drift — the rot is in prose that *describes* claims,
not in claims recorded once and left alone. Which is an argument for the registry's design, and an
argument against ledgers and status cards as a form.

**No kill condition has fired, and none is being ignored.** Checked every entry with live data
against its own falsification clause:

| entry | data | kill | fired? |
|---|---|---|---|
| P-2026-003 (w₀/wₐ) | DESI DR2: w₀ = −0.838 ± 0.055, wₐ ~ −0.6 | phantom drift with the growth | **no** — DESI is thaw-side, which is Route-D's direction |
| P-2026-009 (β = 0) | hint at 2.4–3.6σ | a consolidated ≥5σ β | **no** |
| P-2026-012 (Σm_ν) | DESI-era reach ≲72 meV | Σ ≫ 0.10 eV, or m₁ pinned ≠ 2.24 meV | **no** — 61.4 sits inside |
| P-2026-055 (LSS parity) | arXiv 2604.06021 finds nothing in BOSS or DESI | an independent confirmation at claimed amplitude | **no** — and favourable |

A registry quietly carrying a fired kill would be the single most damaging thing findable in this
corpus. It is not carrying one.

## PRTOE_FAILURES_LEDGER.md — deep audit 2026-07-19

Thirteen checks on 1,681 lines. **The healthiest file of the nine, and the finding is why.**

Probed both directions a graveyard can fail:

**Does it bury anything alive?** No. Every hit on today's live results was correct in context — the
w = 1/3 mentions concern a separate Koide category error, c = 9/10 appears as *what killed* a
predecessor, the f̄ mentions are killed rosters. And it already carried **τ = ½ln2, T_c = 177.10 keV,
ρ_Λ¼ = 2.2599 meV** — current, at a moment when THREE_EQUATIONS, MATH_SPINE, DEPENDENCY_TREE,
READERS_GUIDE and INDEX were all still quoting the superseded values.

**Does it keep anything open that is settled?** One real case: process error 26 recorded the
ξ-derivation session as merely scheduled. It has since run, and ξ now carries three independent
confirmations. Updated. The MOND kill is legitimately reopened and correctly marked so.

Three dead "(docketed)" pointers resolved to what they actually are — the ξ session (**run**), and
the two-loop shooter redesign (**still unbuilt**, twice). One z_on conflation fixed: the ledger
called ~3.6×10⁷ "the H = m onset", when that is the profiled freeze and the identity is 4.03×10⁷.

**Why the graveyard beat the forward files.** A kill entry is written once, at the moment of death,
and never needs revising — like a registry entry. The forward files are all *summaries*, and a
summary has to be maintained against a thing that keeps moving. Nine files in, the pattern is
unambiguous: **this corpus's rot is entirely in the maintained-summary form.** Frozen records —
registry entries, kill entries — held up. Ledgers, status boards, dependency grades, index lines
and reading guides did not, every one drifting pessimistic.

## PRTOE_READERS_RISK.md — deep audit 2026-07-19

Thirteen checks. Three stale items and — more seriously for a risk page — **two genuine risks it
did not carry.**

Stale, all three the familiar pessimistic drift:
1. **f̄ graded candidate** with the same error the dependency tree had. It is derived; the simulation
   is the check. Regraded, and the compound now names α_c as the weakest parent, which is where a
   reader should actually aim.
2. **The superradiance band at 2×10⁸** rather than 6×10⁸ — the third file carrying that outlier.
   Added the point that makes the exposure sharper, not softer: the mass is pinned three independent
   ways, so the model cannot relieve either exposure by moving it.
3. **The code-vs-theory gap stated in its retired, harsher form.** The source genuinely does not
   compute m_e from the dark sector; but the running config pins `varying_me` at the derived value,
   so the "extra free knob" version of the criticism is gone.

**Missing risks, now added** — and a risk page that omits real risk fails at its one job:
- **(i) The evidence run is sampling off the model's own onset identity** — 0.053 dex, a 28% mass
  difference, so the live comparison grades a point beside the stated configuration.
- **(j) The lattice test that decides the flagship cannot resolve it** — the +0.44% prediction
  against a ±5.7% registered tolerance, thirteen times too wide.

Both were found today; neither had reached this page. Worth noting that this file's §3(a) was
*already* the most current treatment of the τ question anywhere in the corpus — so the drift here is
not uniform neglect. The page keeps up with what it already tracks and does not notice what it does
not.

**A risk summary is the one document where pessimistic drift is not the safe direction.** Understate
a strength and you lose credit. Omit a risk and an outside reader finds it themselves, which costs
the whole document its standing.

## PRTOE_REFEREE_CALENDAR.md — deep audit 2026-07-19

Thirteen checks. Five defects, and the first one is the calendar breaking its own closing law.

1. **A referee had landed and its row was not stamped.** The file's own rule reads: *"when a referee
   lands, its row gets the verdict stamped SAME-SESSION and the failures ledger or the spine inherits
   accordingly."* The DESI 4PCF parity row sat unstamped while arXiv:2604.06021 (2026-04-07) had
   already reported — no parity violation in BOSS or DESI, scatter ~4× tighter than BOSS DR12.
   Stamped, favourable, with the honest limit that it uses composite-field spectra rather than the
   4PCF and so denies confirmation rather than refuting.
2. **The evidence run's ETA read "days".** It is ~24h in with no log(Z), no dead-point file, no
   `.stats`, and the honest horizon is weeks to months with the ΛCDM twin doubling it.
3. **Its launch date read 2026-07-13.** It launched 07-18.
4. **"ε+A_s+n_s+z_on all stated"** — z_on is the exception, frozen 0.053 dex off the identity. Both
   the referee row and the run row now carry that caveat, because a calendar whose job is
   pre-written decision rules must say what the run is actually grading.
5. **The 0νββ row carried [0.04, 5.3] meV** and no discrimination structure. Now the corrected
   window plus the finding that only nEXO can reach the model at all, that barium tagging lifts
   detection to ~69% while *removing* discrimination, and that the discriminating band is
   3.69–5.30 meV.
6. **The lattice row's decision rule cannot be executed** — ±5.7% registered against a +0.44%
   prediction. Recorded in place, because a rule that cannot be run is worse than no rule: it looks
   like a test.

**The pattern here is new and worth naming.** The other summary files drifted by *not being
updated*. This one drifted by **not being fed** — verdicts landed elsewhere and nothing routed them
back. A calendar is only as good as its intake, and this corpus has no intake step. Same failure
shape as READERS_RISK missing two risks discovered the same day.

## The status-tag collision — corpus-wide finding, 2026-07-19

JP: *"think about [Amended] how this [CONFIRMED] reads to a [Pending] person. It looks ugly."*

It is ugly, and chasing why turned up something worse. **Seven independent legend systems, and the
letters collide across files a reader moves between:**

| tag | means here | and here |
|---|---|---|
| **[R]** | a registered bet (DEPENDENCY_TREE) | **ridden physics** — standard physics the model reproduces and does not claim (INDEX, subdomain tree, laser_physics) |
| **[P]** | production, the strongest grade | **parked**, the weakest |
| **[C]** | candidate | CLASS source · content |
| **[S]** | screened | screened-constant |

[R] is the dangerous one: a reader who learns the dependency tree's legend and opens the index sees
the model **claiming credit for standard physics**, or disowning its own bets. That is not a
typographic problem.

92 tags sat in running prose against 40 in tables. Fixed in the entry points — INDEX's relation
classes and DEPENDENCY_TREE's six grades are now written as words, and laser_physics no longer
says "graded [R]".

**The rule going forward: grades are words.** A single letter saves four characters and costs the
reader a lookup, and when two files disagree about the letter it costs them the meaning.

*Check 12 caught two defects inside this very repair — a "derived — derived" stutter from the
substitution, and a leftover "[R]" in a sentence I had just written explaining why letters are bad.*

## PRTOE_CODE_MANIFEST.md — deep audit 2026-07-19

Thirteen checks. Three defects, and the first is the file being wrong about the thing it exists to
be right about.

1. **It said the sampled-ε PolyChord run is LIVE. It is not — and the same table says so two rows
   below.** Row 5: "pc_prtoe.yaml (PolyChord) | **LIVE**". Row 7: "the sampled referee KILLED
   mid-prior by decision". Checked: only `cmp_prtoe_fixed.yaml` appears in `ps`, and every
   `pc_prtoe` file is stamped 2026-07-17. The file calls itself "the single source of truth for
   implementation status" in its own header. Corrected, and the header now says status is checked
   against `ps` and file timestamps rather than against intent.
2. **The home tags carried the [C] collision** — [C] here means CLASS source, while
   DEPENDENCY_TREE's [C] means candidate. Written out: CLASS source, yaml, comparison layer,
   doc-only.
3. **A dead "(docketed)" pointer** on the m_ncdm row, and an "amended conditions" fix-tag in a
   section header. Both resolved.

**Verified correct, which is the other half of the job:** `background.c:915` implements
`f_high = 1 − (1+z)/(1+z_high)` exactly as the file claims, and `thermodynamics.c` contains zero
dark-sector references, so "vanilla CLASS" is accurate. This file's *code* claims hold; what failed
was its claim about what was running.

**The distinction is worth carrying:** a manifest can be right about the source and wrong about the
process table, and only one of those is checkable by reading. Run-state claims need `ps`, not
recollection.

## PRTOE_DERIVATION_HUNT.md — deep audit 2026-07-19

Thirteen checks on 586 lines. Three defects, all in §2 — the dark-energy chain, which is the file's
most-cited section.

1. **A correction jammed mid-sentence.** The chain bullet read "...not independently *(τ is now
   sourced independently by the Koide kernel at ½ln2, giving +0.44%)* derived" — a parenthetical
   inserted between "independently" and "derived", so the sentence contradicted itself around its own
   repair. Rewritten to state the sourced chain plainly.
2. **The τ bullet argued against a position the model no longer holds**, spending a paragraph on why
   0.345 must not be quoted as derived. That warning is now moot: τ is 0.34657 from the kernel. What
   survives, and is what the section should have led with, is *what the prediction must be
   distinguished from* — 0.34506, the observation read backwards, sitting 0.44% below.
   **And the point that was missing entirely: the published 0.34–0.37 band is 8.5% wide against a
   0.44% separation, so it could not adjudicate even if it applied to SU(2).**
3. **z_on listed as "≈3.56×10⁷, fast-profiled estimate".** It is a derived identity at 4.03×10⁷,
   with the mass behind it confirmed three ways. The profiled value is what the evidence run is
   frozen at, which is a fact about the run rather than about the model.

**Check 13 on a file that exists to track owed items:** its list is accurate. A_s's residual is
correctly the shot-noise count's O(1) — this file is where I sourced the correction to
THE_AMPLITUDE's orphan. The G-value bullet correctly states the framework does not compute Newton's
constant. η, n and λ_phys carry honest grades.

**The pattern this file inverts:** it was the *source* of truth for two corrections made elsewhere
today, and simultaneously carried three stale statements of its own. Being right about other files'
debts is no protection against being wrong about your own.

**Correction to this entry, same session:** I recorded the file closed after fixing §2's first two
bullets. Check 12 then found **thirteen more stale instances** through the rest of the 586 lines —
the T_c-not-sourced bullet, the BBN pincer rows, the squeeze table, §4c, the lattice section, the
scale ladder. All cleared; one deliberate "177–179 keV" survives where the BBN books are genuinely
insensitive to the difference (verified: the 1.06% change moves T_c's position in the 800→70 keV
window by 0.3%).

**The lesson is about me, not the file.** I ran check 12 on the *sections I had edited* rather than
on the file, which is the same partial-verification habit the check was added to stop. Check 12 means
the whole file. A grep after editing tests the edit; it does not test the document.

## The superradiance band — a near-miss worth recording (2026-07-19)

While auditing DOMAIN_COVERAGE I found the fourth file carrying "2×10⁸–3×10⁹ M☉" against the
6×10⁸ I had propagated. I opened `smbh_atoms`, found an explicit table whose α_g values all
recompute exactly, saw its criterion (spin-down time versus cosmic age) reach down to 2×10⁸, and
**concluded I had been wrong and was about to revert four files.**

Then I checked the registry. **P-2026-034 registers the band as 6×10⁸–3×10⁹ M☉, cut at
α_g ∈ [0.1, 0.5]** — exactly the criterion I had used. The edits were correct and matched the
frozen prediction.

**Both numbers are right, for different questions.** The registered bet cuts at efficient
superradiance; the domain table asks only whether spin-down beats the age of the universe, and that
reaches wider and weaker. Neither file said the other existed, which is the actual defect and is now
fixed in `smbh_atoms`: quote 6×10⁸–3×10⁹ for the prediction, treat 2×10⁸–6×10⁸ as physics rather
than the bet.

**The process lesson, which is the reason this is recorded at all:** when a value disagrees across
files, check the **registered** version before the domain file. The registry is frozen and
load-bearing; a domain file's number can be a different cut of the same physics. I checked the
domain file first, found a well-computed table, and nearly reverted six correct edits on the
strength of it.

Twice today the right move was to look at one more source before acting — once catching an error
(the m_ββ anchors), once catching a *false* error (here). Both times the tell was the same: a number
that disagreed with something I had just written.

## PRTOE_science_subdomain_tree.md — deep audit 2026-07-19

Thirteen checks. Three defects, and one methodological note about my own probing.

1. **The file states two different values for the same count.** Top: "[C] 14". Bottom: "THE COUNT
   UPDATES: [C] 12 → **13**". Flat contradiction, independent of what the true number is.
   Hand-counted and **enumerated instead of totalled** — the thirteen content leaves are now listed
   by name plus critical phenomena from the audit section, giving 14, with the two "tag shaved"
   borderlines (biochemistry, materials science) and the already-counted metrology stated as
   exclusions. A list can be checked; a total cannot.
2. **The legend collides with the dependency tree's** and this file could not warn about it, since
   the collision lives between files. Here [R] is *ridden physics the model does not claim*; there
   it is a *registered bet the model is exposed on*. [C] is content here, candidate there. A callout
   now says so, because a ninety-node tree earns compact markers **only if** the reader is told not
   to import the other legend. This is the one place today where the tags were kept rather than
   written out, and the reason is that the tree structure is doing real work.
3. **A malformed tag**, `particle [C/[P]]`, with nested brackets. Now "[C, with a parked branch]".

**On my own method:** I tried three times to count the tags by regex and got three different
answers, because the formats vary — `[C:]`, `[C-conditional:]`, `[C — ours]`, `[I→C-borderline]`,
`[C/[P]]`. The counts I printed mid-audit were wrong and I nearly recorded one. The fix was to stop
automating and read the thirty lines. **Where a file's own formats are irregular, a regex count is
a guess wearing a number's clothes.**

## PRTOE_INTERACTION_ATLAS.md — deep audit 2026-07-19, and the propagation it opened

Sixteenth file, and the largest yield so far. Fifteen defects in the atlas itself; then one of them
turned out to be corpus-wide and took the flagship with it.

**In the file.** A broken table cell ("structuralts"); a heading split across two lines with an
orphan bracket; three duplicated-word garbles; "as a interaction"; the third law stated one way at
the top and a different, non-grammatical way at the bottom; a Hulse–Taylor ratio (0.997 ± 0.002)
paired with the 2016 citation that reports 0.9983 ± 0.0016 — number and source belonged to
different papers, now both 2016; "thirty-one decades" for a thirty-decade gap; 10¹⁴ GeV called
"GUT-scale" when it is two decades below it; an orphan section reference `(2.2 Step 1)` pointing
nowhere, replaced with the argument it named.

**The graveyard census was wrong and failed the file's own tripwire.** It read "7 cold / 6 warm /
3 risen" — sixteen — against fourteen entries. Rule 2 says the graveyard has become
finality-avoidance if warm ever exceeds cold, so an inflated warm count makes the file look more
evasive than it is. Hand-classified: **7 cold, 4 warm, 3 risen**, and now enumerated by name so the
tripwire has something countable behind it.

**The superradiance entry was sitting under "Nulls checked" while the recorded mass makes it a live
exposure.** It claimed the axis "misses us TWICE." Both shields were priced at a mass the model no
longer carries. The kinematic one — α_g ≤ 0.075 even for the heaviest holes — reproduces exactly at
m ~ 10⁻²² eV and does not survive the move: at the recorded 2.24×10⁻²⁰ eV the same holes give
α_g ~ 1–17, M87* alone at 1.09, and the superradiant window lands on 6×10⁸–3×10⁹ M☉, which is
populated and carries high measured spins. The λ-quench shield was swept at λ ~ 10⁻⁸⁸; at the
recorded λ ≈ 2×10⁻⁹¹ the self-coupling is 500× weaker, **2.7 decades straight off a margin whose
swept low end was +2.5** — so the low end no longer clears zero, and the α_g shift cannot be folded
in by scaling because its exponent (9−p)/2 flips sign at p = 9. Rewritten as a live exposure with
the re-pricing named as owed, and the discriminator marked un-priced by the same amount, since it
rests entirely on the quench.

**Magnetogenesis was recorded as a silence the model does not claim** — but it is registered as
P-2026-028 with a number (B ≈ 5×10⁻¹⁸ G from Harrison seeding on the model's own vorticity, a bill
ΛCDM cannot pay). The understatement pattern again.

## The M₂ / E_b supersession — corpus-wide, and the harness was certifying it

Chasing M₂ = 9.53 eV in the atlas found it in four more files, and then the reason: **9.53 eV is
α²×179 keV, and 179 keV is the retired T_c.** At the kernel-sourced T_c = 177.10 keV the chain
gives M₂ = 9.43 eV and ρ_Λ¼ = 2.2599 meV, +0.44% — which is what the dependency tree has recorded
as derived all along. Ten forward-facing files were still carrying 9.53 / 2.284 / "+1.5%".

**The harness was passing 151/151 while encoding the retired chain.** It set `Tc = 179e3` as an
input and then checked that M₂ and ρ_Λ¼ came out at 9.53 and 2.2842 — recomputing a claim from its
own stale inputs, which can only ever pass. The chain now runs forward from τ = ½ln2, so T_c is an
*output*, and the retired reading is kept as one explicitly-labelled check so a stale number is
recognisable on sight. **A regression harness that starts from the value under test is not testing
it.**

**The flagship contradicted itself across forty lines.** Its banner said the headline "is not a
+1.5% prediction" because "T_c has no independent source"; its body forty lines down said "the one
order-one number left is τ, and it is sourced," and derived it. The banner was right when written
and was never updated when the kernel supplied τ — the same rot, on the model's most-read page.
Rewritten to lead with the standing grade and the distinction that carries it (0.34657 against the
observation-inverted 0.34506; the gap *is* the claim).

**And a circularity, caught while re-pricing.** The flagship claimed its two doors "stand in the
exact ratio the phase-space factor gives — agreement to 0.04%." Door B is *defined* as E_b/Φ¼ by
the perturbations door's own formula, so (A/B)⁴ = Φ identically, for any E_b whatever. The 0.04%
was rounding in an intermediate value, quoted as a convergence between independent computations.
The content survives — there is no free coefficient to build — but it is an algebraic identity, and
it now says so.

**P-2026-048's own body still said 0.3503** while the title I gave it this session said 0.34657. I
had grepped my way through that entry instead of reading it. The addendum was worse: it posed the
lattice fork as 0.34657 vs 0.3503, making a *rounding artifact* a hypothesis about nature. The fork
is 0.34657 (kernel) against 0.34506 (observation-inverted); nothing sits at 0.3503 except the
consequence of rounding 0.345 to two decimals.

**The one place the retired value stays.** T_c = 179 keV is compiled into the pipeline and the
offline BBN splice. It is one temperature, not two, so the coded value is an approximation of the
standing one — priced rather than assumed: at 177.10 keV the ramp stamps read 0.6047 and 0.7741
against the coded 0.6089 and 0.7765, moving the D/H window from +0.645% to +0.641% and the
prediction by **0.002σ** against a ±0.047×10⁻⁵ budget. Four hundred times smaller than the
measurement it feeds. Stated in the code manifest and left alone.

**The Fairbank letter moved by one number and it is not the one that matters.** The narrowed anchor
range (2.25–2.2599 rather than 2.25–2.284) lifts the m_ββ floor from 0.02 to 0.04 meV. The ceiling
holds at 5.30 either way, and the ceiling is what every conclusion in the letter turns on — the
floor sits two orders below any experiment's reach. Updated, with that insensitivity said out loud
so a reader does not have to wonder.

**Species note.** Today's yield splits the same way the session has all along: frozen records held
(the failures ledger's autopsy was accurate and complete); maintained summaries rotted (the census,
the harness, the flagship banner, my own P-048 entry). The new one is the harness — an *instrument*
that rotted, which is worse than a document rotting, because it was the thing certifying the rest.

## The hadronic-channel review — 2026-07-19, the PBH route opened and closed in one night

JP's route, and the census's strangest entry. The full account is §5b of the scar file; what
belongs in this ledger is what the episode said about the corpus.

1. **The regime blind spot was total.** Zero hits for `hadrodissoc|spallation` anywhere in docs/ or
   scripts/ before tonight; no Carr/Kohri/Kawasaki/Jedamzik in any bibliography. The three-number
   spec was photon-derived in all three legs and stated channel-free in seven places, one of them
   the Fairbank letter, one a live referee's scoping. One sentence was flatly wrong ("an injection
   before ~6 weeks destroys deuterium" — hadronic injection in that interval *produces* D).
2. **The re-audit of every prior kill against the new regime reopened nothing** — and collapsed two
   obstructions into one: the photon channel's "no source" and the quark route's
   "symmetry-forbidden" both reduce to the census's kill on strong-sector couplings.
3. **The one candidate that cleared the roster was killed by a receipt.** The PBH route survived
   Pauli finiteness (a black hole is not a field), landed in the window without tuning, had the
   right shape on both rows — and died on the ⁶Li co-signature at 39–156×, efficiency-free, read
   off the constraint figure's own vector paths. First census entry killed by a co-signature.
4. **The commit gate refused its first commit tonight** — a unit error in a new check's prefactor.
   Two silent red-harness merges happened earlier today under "remember to read the output."
   The mechanism works where the resolution did not.

## PRTOE_PHYSICS_DOMAINS.md — deep audit 2026-07-19

Eighteenth file; 987 lines, the largest summary-shaped target. Twenty-two defects. The finds that
matter beyond their lines:

1. **My own morning drive-by left a three-way contradiction.** I rewrote §12's superradiance body
   (live exposure) and left its verdict ("shielded twice"), the at-a-glance row ("Shielded, twice"),
   and Part II §52 (the old margin, quoted as quotable) all contradicting it — in one file. Check 12
   applies to my edits with exactly the force it applies to anyone's. All four voices now say one
   thing.
2. **The Part II tally was wrong in four of eight classes, always understating.** Claimed
   9 PREDICTS; enumeration gives 12. Both tallies (type and status) are now enumerated by section
   number so they can be checked rather than trusted.
3. **A 74-domain census had no 0νββ entry.** The model's most experimentally-scheduled block —
   m_ββ window, the nEXO overlap, the tagged discriminating band, the Majoron mode — absent from a
   census that includes medical physics. Added as §75, with CMB-S4 (the registered corner-selector,
   ΔN_eff 0.06–0.24 + g₃₃ in-band) as §76. The census now stands at 76.
4. **The deuterium ladder mixed two widths mid-sentence** — the "−2.5 to −1.4σ" window (2-term
   budget) beside numbers on the scar file's 3-term width. Restated on one width; the corpus-wide
   width decision is ForJustin/10.
5. **Cross-file arithmetic caught a garble in the scar file itself**, which survived its own deep
   audit: "(ΔN_eff ≈ 0.26–0.29)" for a window that is exactly 0.06–0.24. The committed window's
   edges now harness-lock to the ΔN_eff band that generates them.
6. **h = λΨ₀²/m² ~ 10⁸ was seven orders stale** — at the recorded λ ≈ 2×10⁻⁹¹ and m = 2.24×10⁻²⁰
   the quartic era at release is h ≈ 2–9. The qualitative claim (not negligible) survives; the
   magnitude collapses.
7. The rest: the graveyard census aligned to the atlas's enumerated 7/4/3 (was 7/5/3, twice); the
   mass-band rows (§§13, 46, 49, 52 + validation) moved off the retired [1,3]×10⁻²¹ band to the
   recorded mass; §21's "new half confessed" updated to the kernel-sourced +0.44% with the whisper
   trial marked resolved (it contradicted §8 in the same file); B−L "GUT-scale" phrasing corrected
   twice; ΛCDM's control aligned to −1.90σ; ε 1.24% → 1.2543% in §74 (shift +2.51%); thirty-one →
   thirty decades; two garbled sentences; one AI-tell ("Crucially") removed on JP's jargon request —
   the sweep found house metaphors ("leverage" as the lever's own leverage) and technical terms
   ("seamless" vs the dead segmented bound) otherwise clean.

**Species note.** Defects 1–3 are all the same species: the maintained summary understating the
model — my own edit included. The census tally understated PREDICTS, the census omitted the
sharpest experimental domain, and the at-a-glance table advertised a shield the body had already
withdrawn.

## PRTOE_the_great_chain.md — deep audit 2026-07-19

Nineteenth file. Nine defects. T_c = 179 keV survived in GEN 2's prose while the appendix row
below it carried the standing 177.10 — one file, both values. The rent was 1.24% twice against
the standing 1.2543%, and appendix row 6 quoted the coded amplitude as 1.0124 against the
pipeline's actual 1.012543; the same row claimed "fits not yet re-run" when the corrected
zero-parameter run is executing now. Row 7 carried the Gaussian gate — **and ForJustin/09
claimed I had already fixed this file's gate form; the claim preceded the fix by half a day.
Recorded against me: a ForJustin note asserted work that had not been done.** Now true. Row 12's
Meissner cap aligned to P-028's registered range; two process scars on the Oklo fence ("now
cited", "new fence added this pass") read fluent; one piece of jargon ("the inheritance DAG")
now plain.

## PRTOE_THE_CHAIN.md — deep audit 2026-07-19

Twentieth file. Six defects and one check-13 closure.

Link 3 carried the retired T_c with its redshift (179 keV / 7.6×10⁸ → 177.10 / 7.5×10⁸) and a
dangling parenthetical. Link 4's z_on moved from "the fit's ~3×10⁷" to the identity 4.03×10⁷
(log 7.605) with the frozen profile stated beside it. Link 5's "781 cells" traced to Planck's
A_s = 2.100×10⁻⁹ — the pipeline freezes 2.088058×10⁻⁹, which gives **782**; both counts are now
harness-locked so the provenance is arithmetic rather than lore. Debt (i) claimed the turn as
owed when tether 10→11 computes its expanding branch two paragraphs above — the debt now names
only the bounce and the contracting branch, and the spine claims the computed tether.

**The check-13 closure: the τ link was a named debt ("a bounded computation, never run") and it
reduces by the file's own structure.** The clustering half is zero by construction — the linear
sector is ΛCDM-identical and the fluid's distinctive scales are sub-parsec. The atomic half is
gated by the edge the chain already carries: ε is OFF by z ~ 30, τ's weight lives at z ≲ 10,
and the overlap tail is orders below Planck's ±0.007. What survives is the edge's shape — the
same discriminator link 7 already measures in 21cm. Four named debts are now three, not by
deciding the question but by noticing the file had already answered it in two other places.

## PRTOE_math_story.md — deep audit 2026-07-19

Twenty-first file, and the most rotted narrative in the corpus: the story of the model as of
July 8, still telling the **dead deuterium heal as its arc**. Act 3 read "D healed (−1.2σ→0)"
and the one-breath arc said "heals deuterium at BBN" — the flat vev died at +7.7σ, κ_v by eight
orders, and the standing row is −2.49σ with the lever census closed. Act 3 is now the witness
era: the dyad condensing mid-window at 177.10 keV, the ramp stamps, the window's real help
(+0.27σ), and the scar carried openly with its dedicated file linked.

The rest of the sweep: "c ≈ 0.93 ± 0.38 measured" → c = 9/10 DERIVED (with f̄ = 2/π beside it
and α_c = 3α as the one registered input — the old c·f_amp·Ψ₀/M_red decomposition demoted to
one clause as the road that found the number); H₀ 70.1 ± 0.7 → 69.9 provisional; ε 1.24% →
1.2543%; the THREATS row replaced wholesale — it still carried "birefringence consolidating
(2.9σ)" against a null since **proven** (P-2026-009), and now names the real exposures: DESI
DR2 at 3.1σ, the superradiance band, the scar's budget, and the priced dark-photon surrender.
The gate got its near-step form; the archived amplitude-derivation pointer moved to
THE_AMPLITUDE.

Check 12 caught two residues of my own rewrite: Act 4 still leaned on "the Act-3 heal" one act
after the heal was removed, and the status key listed tags ([FIT], [TRACED]) the body no longer
uses. Both fixed before commit — the same lesson as every other time, one act downstream of the
edit.

## PRTOE_me_mechanism_math.md — deep audit 2026-07-19

Twenty-second file. Eight defects, one real find.

The ε sweep: the file mixed both values — §0, §4, §8's locked-correlation table and §9's fit
value all carried 1.24%/1.0124 while §8's own forecast block below them used 1.2543%/2.509%.
One document, both epochs. All standing now, and the locked prediction dm_ν = 2·dm_e re-priced
2.48% → 2.51% (1.54 meV on the sum — the harness carries it).

**The find: the BBN-stability fence's lower edge is the retired operating point.** The high-f
table quoted "BBN-stability fence [179, 369]" — and the kernel re-pin puts T_c = 177.10, which
sits 1.1% *below* that fence. The tell is that the lower edge equals the old T_c exactly:
stability was recorded from the then-operating point upward, not probed beneath it. Priced
rather than asserted: the re-pin costs 0.002σ on D/H (four hundred times inside the budget),
and the fence's re-statement is assigned to the same RG-resummation docket that owns the
re-pin. Same note added at the fence's other appearance (DERIVATION_HUNT).

The ramp's absolute stamps rescaled to the standing T_c (154 → 152 keV at half, 114 → 113 at
90% — the ratios are the kernel's and survive). The retired electron-CW section is properly
fenced with its must-not-cite banner and was left as the record it claims to be; its one
current number (κv² delivering the full 1.2543%) was already right.

## PRTOE_me_trigger.md — deep audit 2026-07-19

Twenty-third file. This is the document that *sourced* the n > 2.43 pillar — its §7 is the
derivation the gate-form fix leaned on all day, and that section needed nothing. What rotted
was everything downstream of July 10.

**§8 still called the amplitude "exact value open"** and watched 2α and 3α/2 as coincidences —
against a standing stack that derives it (c = 9/10, f̄ = 2/π, α_c registered). The watched
coincidences are retired; the section now says what is paid and what one input remains.

**§11 carried the dead vev heal as a ran co-signature** ("δv/v ≈ 0.091% heals D/H exactly,
−1.2σ → 0.0σ") — and worse, a universality claim that *contradicts standing leptophilia*: "the
model predicts UNIVERSAL varying-constants," with the leptons-only reading marked retracted.
The standing identification runs the other way: the dyad is the Majoron, quarks carry L = 0,
and a flavor-blind shift would be +12–18σ dead through deuterium's binding. The two-phase
window structure survives as the recorded skeleton; both dead riders are named as dead.

**The same contradiction was still standing in math_story's Act 5** — "shifting ALL masses
UNIVERSALLY (flavor-blind)" — which I audited and missed hours ago. Backfixed to the
leptophilic statement. Cross-file contradictions do not respect the one-file-at-a-time
boundary; when a fix names a principle, the principle's other homes need the same sweep.

**§12's owed list was three-quarters paid**: the amplitude (paid — the stack), the EP-safety
proof (paid — Vainshtein-screened Δa/a three to five orders under MICROSCOPE), the census
adjudication (paid — the consolidated clause). Rewritten as a ledger with the honest remainder:
the condensate-growth profile and R1's #11 sims gate. Also: the bare value at recombination
corrected to 1.012543 (§1 had ≈1.010, conflating R1's variant with the dyad's amendment); the
first-collapse mass note brought to the recorded 2.24×10⁻²⁰; a dangling "§62/§74" booking
pointer resolved to the census's §74.

## PRTOE_wormholes.md — deep audit 2026-07-19

Twenty-fourth file, and the audit's first **clean pass**: no edits. Numbers check (c_s = √α_c;
the 17-order branch-DOS pricing cites its source), the bans match the atlas's wormhole verdict,
the named killer is falsifiable, the legend is defined in place, and the prose is fluent. A
clean file is a result, recorded as one.

## PRTOE_white_holes.md — deep audit 2026-07-19

Twenty-fifth file. Two defects in 397 lines — the best-kept large file so far, and notably it is
a *frozen-record-style* shelf rather than a maintained summary, which is the session's pattern
holding to the end.

Both defects were historical, not physical. The "historical precision" parenthetical dated the
maximal extension "five years after his death" for both Synge [1950] and Kruskal–Szekeres
[1960] — Synge's construction predates Einstein's death by five years, not the reverse. Now
stated correctly, with the honest note that Synge's paper drew little notice in Einstein's
lifetime. And the Haggard–Rovelli work was cited under two different year-tags in one file
(2014 tag, 2015 prose); unified to the bibliography's tag.

Everything with a number checked: the Faraday pricing (4.5×10⁻¹⁰° vs 0.34° is nine orders),
the dimmer's geometric center (√(32×4) ≈ 11.3 against "centered at z ≈ 12"), the z ≲ 0.7
re-domination against THE_CHAIN, the P-028 field value against the registry. Owed items are
all honestly gated (bounce dynamics EXPLORATORY; T10's spectral shapes de-urgented by computed
ceilings; flatness owed to the cycle map).

## PRTOE_weakest_joints_and_cprep_2026-07-10.md — deep audit 2026-07-19

Twenty-sixth file. A dated ledger whose era entries are properly fenced — the right repair was
its own format: **JOINTS UPDATE 3**, bringing all seven joints and the ε joint to standing.
J1's arc alone spans the whole session's physics: RED/UN-DERIVED → the retired 20% reading →
the kernel-sourced +0.44% with one registered input. UPDATE 2's two pending values (c implied
at 0.90 ± 0.04, f̄ pending at 0.644 ± 0.03) both landed at exact derived forms — recorded as
the ledger's own vindication. One in-place fix (B2's ε). The two-widths collision surfaces
here too; stated, and routed to ForJustin/10.

## PRTOE_UV_completion.md — deep audit 2026-07-19

Twenty-seventh file, and the audit's second **clean pass** — zero edits, for the opposite reason
wormholes earned it. This is a *superseded docket that was fenced correctly at supersession*: the
reading-rule banner declares everything below it an era record ("nothing below is current unless
MATH_SPINE also says it"), the head states the standing result and names the docket's own dead
premise, the killed #17 candidate carries "Do not cite," and the speculative sections are fenced
as assumptions with their unprovability stated. The head's live target (ξ_H = 1/6 as input;
P-2026-045's conditionality) is current. **This file is the template for how a docket should be
retired** — every defect the audit has spent the day fixing elsewhere is the absence of exactly
this pattern.

## QUEUE STATE (2026-07-19, end of the summary-shaped tier) — where each audited file's record lives

The scan rule: a file is deep-audited when its whole contents passed the 13 checks, wherever the
record sits. Files whose audits live under thematic headers rather than name-headers:

- **PRTOE_interaction_map.md** — audited 2026-07-19 (the gate-form commit): the Gaussian → near-step
  correction, the signature law rewritten to survive both gate readings, P-007 un-understated,
  ε to 1.2543%. Record: the commit of that title plus ForJustin/09.
- **PRTOE_cosmological_constant.md** — audited 2026-07-19 under "The M₂/E_b supersession": banner
  rewritten to the standing grade, the door-B identity caught, all retired values purged, whole-file
  re-read. Harnessed end to end.
- **PRTOE_deuterium_scar.md** — created and completed 2026-07-19: §§2, 5, 5b, 6, 6b, 7 all worked,
  the hadronic channel and PBH route added and closed, every number harnessed.
- **PRTOE_fairbank_note_draft.md / _HOLD.md** — the priority set, audited line-by-line 2026-07-19
  (pre-compaction record) plus today's channel-qualifier and window fixes.
- **PRTOE_neutrino_sector.md** — §3 reworked to the standing anchors, §3b (the Majoron mode) added,
  claim-1 floor made consistent; harnessed.
- **PRTOE_bbn_witness.md** — partial: today's channel-qualifier and co-signature fixes only. **Still
  owes its full pass** (queued next, highest citation of the remainder).
- The flagship trio, entry points, registry, ledgers, calendars, atlas, tree, chains, PHYSICS_DOMAINS,
  math_story, me_* pair, UV_completion, weakest_joints, white_holes, wormholes, subdomain_tree,
  smbh_atoms (superradiance rewrite), CODE_MANIFEST, DERIVATION_HUNT — name-headed entries above.

**The remaining tier** (domain files by citation depth, then working logs): bbn_witness (full pass),
family_tree, fingerprint_lattice, dcdf_superfluid, dyad_gas, hubble_tension, DOMAIN_COVERAGE,
koide_relation, MATH_SPINE-cited leaves, then the long tail of single-domain files, then
working_logs/. Pass 2 (varied attack) follows the tail.

## PRTOE_bbn_witness.md — deep audit 2026-07-19 (the full pass)

Twenty-eighth file. Six fixes, one number saved from a wrong fix, and the day's tidiest
provenance result: **the scar's ΔN_eff garble traced to its source.** This file's "joint
likelihood peaks at ΔN_eff ≈ 0.26–0.29" is the constant lever's *optimum*; that number was
transcribed into the scar as the *committed window*. Both files now state the true relation —
the window (0.06–0.24) tops out just under the optimum (0.26).

The zero point was wrong (0.44 leaves D/H at 2.512; the true value is 0.49 = ln(2.527/2.387)/0.116,
harnessed), restoring exact agreement with the scar's 8–33× shortfall. The MeV corner
contradicted today's roster result ("remains open" as the source vs the scar's 4.7–4.9×-short
seats) — aligned. The T_c and ε supersessions priced at the header (0.002σ and 0.004σ). The
two-widths cross-pointer added.

**And the save:** "ΛCDM itself carries 1.85σ under PRIMAT" looked like the stale in-house control
— it is PRIMAT's own ΛCDM (2.439) at the 2-term width, exactly 1.85σ, correct as written. Now
harnessed so nobody "fixes" it later. The audit's job is as much protecting right numbers as
correcting wrong ones.

## PRTOE_family_tree.md — deep audit 2026-07-19

Twenty-ninth file. Four defects: three empty "()" husks from the reference purge (the
ForJustin/08 species — the l_Pl cell split as "(forced,/)", two branch cells bare), one
editorial trim. Every number in the tree checked against standing and held: the floor 2.26 meV,
λ ≤ 2×10⁻⁹¹, α_g = 1 at 6×10⁹ M☉, H₀ 69.9, the comb's 3.1n, the four ladder scales. The
purchased-null perimeter reads as the standing kill set. A sed mis-hit during repair (took the
wrong paren) was caught by re-reading the line before commit — the small version of check 12.

## PRTOE_fingerprint_lattice.md — deep audit 2026-07-19

Thirtieth file. Three defects, and one is the audit's first **overclaim** — the drift's rare
direction. "All three factors DERIVED" graded α_c = 3α above its registered-bet standing; the
file's own next sentence (the chain *referees* the value) already knew better. Now "two derived,
one registered." The conditional footnote named the wrong run (pc_prtoe — the killed sampled-ε
config — where the executing run is cmp_prtoe_fixed). And the ε(epoch) table called the coded
T_c = 179 "derived"; it is coded, with the kernel value and its 0.002σ price now stated beside
it. The quark-bleed row and the de-biased Σm_ν band both checked against their sources and held.

## PRTOE_dcdf_superfluid.md — deep audit 2026-07-19

Thirty-first file. Two purge husks (dangling space-periods where references were stripped) — and
otherwise clean, with one verification worth its line: the identity file's "H = m onset at
z ≈ 4×10⁷" checks arithmetically against the recorded mass (ħH at that redshift is 2.2×10⁻²⁰ eV),
so the file's onset statement and the z_on identity are one fact stated two ways. Sections 2–5
all consistent with today's standing (2.2599, the SU(2) diquark story, the winding-signed
chirality, the Pauli count, the honest 21-dex non-closure).

## PRTOE_dyad_gas.md — deep audit 2026-07-19

Thirty-second file. Four defects: T_c still "≈ 179, observation-inverted rather than
independently sourced" against a kernel that now sources 177.10 (fixed, with the coded-pipeline
price stated); a self-inconsistent amplitude line ("ε ≈ 1.24% (= 27α/5π)" — the formula
evaluates to 1.2543); Σm_ν rounded below its booked value; and one purge husk mid-sentence
("the sub-ohmic/smooth region of hunt the derivation log"). The dead-ends block — the P-011
retraction's precise scope, leptophilia forced twice over, the counting-measure distinction —
is exactly right and needed nothing. The neutrino_home link verified as live.

## PRTOE_hubble_tension.md — deep audit 2026-07-19

Thirty-third file, the core empirical claim. Four value supersessions and nothing structural:
both ε statements to 1.2543%, T_c to the kernel's 177.10, z_on to the identity's ≈4×10⁷ in the
dead-ends note. Everything that carries weight held on inspection — the reach cap (70.9–71.3,
"the model cannot reach 73, and says so"), the three-tier data-ethics declaration, the TRGB band
against Freedman, the honest half-the-gap framing, and the dead-ends note that explains *why*
the honest H₀ is 69.9. The SN mass-step corner references the gate window without hard-coding
C_ref, so it survives whichever way ForJustin/09 resolves.

## PRTOE_DOMAIN_COVERAGE.md — deep audit 2026-07-19

Thirty-fourth file. Three fixes: the cc-problem row's "new half: confessed" brought to the
kernel-sourced +0.44% (the same supersession PHYSICS_DOMAINS §21 carried); the superradiance
verdict label "live-if-heavy" to "live now" (the mass moved into the live regime — the row's own
text already said so, the label lagged its own sentence); and the BBN row's booking pointer now
names the dedicated scar file. The superradiance and neutrino rows were already current — this
map was maintained better than most of its class. The advertised −2.5 to −1.4σ range left as is
per ForJustin/10.

## PRTOE_koide_relation.md — deep audit 2026-07-19

Thirty-fifth file. Two defects in 234 lines of the corpus's most carefully-hedged sector file.
The ε in the protection statement (1.24 → 1.2543), and **the 0.3503 fork again** — "0.34657
crowns the kernel, 0.3503 kills it" posed the lattice question against the rounding artifact,
the same error corrected in P-048's addendum this morning. The fork now reads 0.34657 vs
0.34506, 0.44% apart, with the decision rule's inconclusive band named. Everything else held:
the CV = 1 arithmetic (V/μ² = 3Q−1 to 18 ppm), the 0.9σ fence, the honest "landing not derived;
protection still is," the echo-not-witness provenance on 2/9, and the moment-condition chain.

## PRTOE_coincidence_problem.md — deep audit 2026-07-19

Thirty-sixth file. One defect: the residual-honesty clause still rested the floor's value on
"M₂ being selected by the same closure" — the framing the failures ledger retired as circular.
Now rests on what actually carries it: the kernel-sourced τ, the portal, and α_c. The width
arithmetic all verified (8.16 H⁻¹, the 3.5% occupancy, one-in-thirty), and the file's central
honesty — width derived, occupancy not, and a longer era makes placement *harder* — is exactly
the right shape and was left untouched.

## PRTOE_scale_ladder.md — deep audit 2026-07-19

Thirty-seventh file, and the third **clean pass** (its one stale line was corrected in the
morning's supersession sweep). Every rung's α_eff and ½α² verified — cluster through planet
orbit from orbital velocities, the atom from α, the universe rung's identity honestly labeled
as an identity. The hinge fact, the priced prediction zone (10⁻¹⁸, no wide-binary anomaly),
and the couplings-column closing note all current.

## PRTOE_hierarchy_problem.md — deep audit 2026-07-19

Thirty-eighth file. One structural defect and two roundings: the banner carried the same
conditionality-and-referees sentence pair **twice** (a copy-paste doubling, the fuller version
kept), and its 1.5015 / +0.15% disagreed with the file's own §2 and the harness (1.5014 /
+0.14%). The split-grade banner table — the day's most careful piece of supersession bookkeeping
anywhere in the corpus, grading each piece by whether it used the excluded vacuum — needed
nothing. The additivity-grade 3/2 chain, the three-way k concordance, the one-coupling
portfolio, and the stability addendum all verified against the harness.

## PRTOE_galactic_atoms.md — deep audit 2026-07-19

Thirty-ninth file, and the fourth **clean pass**. The Galactic-Centre pricing is complete inside
it — the 2.9× adverse at 1 pc stated as adverse, the sphere-of-influence escape derived rather
than hoped, P-2026-054's two-class boundary registered with its m^(−0.73) scaling, and the
honest relocation of the clean test to the dwarfs. Task #98 closed against it. Every number
verified (the 224× mass ratio, the Schive cores, the soliton masses, the six-per-cent dwarf
share). This is what a priced adverse constraint should look like.

## PRTOE_entropy.md — deep audit 2026-07-19

Fortieth file. One defect, of the self-inconsistency species: §4's formula line said
ΔE = ε·m_e·f, but its own quoted numbers (50 eV at f = 0.023; ~150 at mergers) cohere only on
the ballistic ~2 keV base — the kinetic third of the 6.41 keV step — which is what the harness
has carried since the gate's energy-bookkeeping session. The formula now states the share
explicitly, and all three points of §4's velocity scaling are harnessed. Everything else held:
the rank-condition theorem's framing, the 48π·η debt stated as one number, the ~70-order budget
subordination, and the §5 non-claims list.

## PRTOE_arrow_of_time.md — deep audit 2026-07-19

Forty-first file. One defect: the free-energy gauge still quoted the Gaussian gate — the form
this file's own §2 makes load-bearing, in the last home the gate-form sweep had missed. Now the
near-step, and a corpus-wide grep confirms no Gaussian-as-the-form statement survives anywhere
(the two-recorded-rooms treatment in the mechanism doc is the lone, correct exception). The
file's structure is among the corpus's best: §2a names exactly what the uniqueness argument
does not reach, refuses to let §1 cover for it, and declines the anthropic repair its own §3
rejects — honesty with teeth. The 10³⁶-vs-10¹⁰⁴ budget agrees with the entropy page.

## PRTOE_information_paradox.md — deep audit 2026-07-19

Forty-second file. One defect, in the head-versus-body species: the banner carried the standing
state (the coefficient derived-conditional as the heat-kernel ratio 12π/48π = 1/4, one regulator
check owed) while the §2 table still said **OWED** and §3 still called the functional "the
single debt behind three documents." Both brought to the banner's own state.

**And a correction to my own audit of two files ago:** `entropy` §3 said "coefficient one number
short" while its §5 carried the ratio resolution — a §3-vs-§5 tension I read past and called
consistent. Reconciled now, both directions. A file audited clean is only as clean as the
auditor's attention; the miss is recorded here with the same prominence as anyone else's.

## PRTOE_blackholes_no_singularity.md — deep audit 2026-07-19

Forty-third file. Two finds above the pattern. **The λ-convention split:** §3's CSW threshold
and §8's recomputed one sat 12.8× apart — a factor-4π difference in the quartic's normalization,
unflagged, with the summary row advertising only the friendlier ~250× margin. The conservative
clearance is 20×; both sections now name the convention and lead with it, and all four
thresholds are harnessed. A margin that depends on a convention is not a margin until the
convention is named. **The lean that was a bet:** §7(iv) still called the superradiance band
"a lean, not a bet" on "sparse spin measurements," against a registered P-2026-034 and a
populated band — brought to the live-exposure statement. The Kaup cap verified (3.7×10⁹), the
r_s/ξ table checked, the Penrose discharge and area-law rows already current.

## PRTOE_bigbang_no_singularity.md — deep audit 2026-07-19

Forty-fourth file. Two fixes. §1.2's joint constraint quoted the bounce floor off the BH
*threshold* rather than the derived λ (1.1 keV at 2×10⁻⁹¹, harnessed) and inherited the
convention question — now flagged as immaterial to its own 14-order tension, which is the
point of pricing it. And §5's first owed item was a check-13 payment: λ is derived at the CMB
ceiling and clears the BH core's requirement — the bullet now says paid and points the residue
where it actually lives (the un-simulated two-component bounce profile, which still carries the
named MeV-over-keV number it must hit). The zero-energy theorem, the emergent-clock reading
with its kill clause, and the falsifier table all held.

## PRTOE_cyclic_torus_genesis.md — deep audit 2026-07-19

Forty-fifth file. Five fixes, one of them a correction to my own PBH-night reading: the
"only ~10¹⁵ g PBHs radiate appreciably" line is *correct in its context* (the present-day
radiation brake — lighter classes already evaporated) and only misleads when quoted as general
lore, which is how I quoted it. The epoch is now explicit, with the ~10¹¹ g BBN-era class
cross-linked to its ⁶Li kill. Also: the EB hint was called "measured" (now: claimed,
calibration-degenerate, against the model's own zero); the BH entropy budget disagreed with the
corpus's other two files (10¹⁰⁶ → 10¹⁰⁴, 16 orders over CMB); the exploratory turn timings
(+33 to +76 Gyr) now carry the computed tether's supersession (16–26 Gyr, MATH_SPINE §7d); and
the "cycle (Tolman)" verdict gained the finite-chain clarifier so it cannot be read against the
standing frame that *accepts* Tolman. The honest-status block — "a story built from real parts,
NOT a derivation" — is the right grade and was left exactly as written.

## PRTOE_baryogenesis.md / PRTOE_igmf_helicity.md / PRTOE_lss_parity.md — deep audits 2026-07-19

Files forty-six through forty-eight, and all three are **clean passes** (the fifth, sixth, and
seventh). The parity family's records are the corpus's healthiest tissue:

- **baryogenesis** holds the crux-vs-integral distinction exactly right — the frozen-era
  category error resolved (phase conducts while the modulus sits still), the transmission
  integral still owed with its target range stated (𝒯 = 2–6×10⁻¹¹, now harnessed), and the
  un-refereed portions marked as such.
- **igmf_helicity** grades its own hint as "a watch rather than a test" until the sign map runs,
  and the 07-18 addendum sharpens the owed item to one relative sign with the closing object
  named (the roll-up theorem, run for its sign).
- **lss_parity** carries the referee's report with the model's position vindicated-but-not-called
  (DESI's null, the blinded 2.9σ, the honest "not a direct replication" caveat), P-2026-055's
  provenance stated including the after-the-fact mirroring, and a §4 owed list in perfect
  check-13 form.

The pattern is now beyond doubt: files written or reworked on 07-18 are clean; the rot lives in
everything maintained-but-not-rewritten between 07-07 and 07-16.

## PRTOE_cosmic_magnetism.md — deep audit 2026-07-19

Forty-ninth file. One fix: the EM-neutrality clause said "forced to 25–45 orders" against a
registered bound (q_EM < 4.7×10⁻³⁸…10⁻⁴⁷) that is 37–47 orders below unit charge — the clause
now quotes the bound itself. Everything else held: the seed's arithmetic (harnessed since the
first pass), the void gap's honest OPEN status with both rescues closed by flux conservation
and the single external referee named, the precise-boast section that separates the standard
mechanism from the model's three genuine additions, and the signed-helicity falsifier with no
dial. The pathology table for competitors is accurate to the literature.

## PRTOE_gravitational_waves.md — deep audit 2026-07-19

Fiftieth file. Two fixes, both the head-vs-tail species. §2 still flagged the chiral amplitude
"un-computed" while the file's own 07-18 addendum computes it as a structural null — the flag
now points at the computation and relocates the family's falsifiable content to the two
readable members. And the addendum's computed margins (8 orders under PTA, 4 under LISA-class,
1.5 under the B-mode floor — all harnessed) contradicted white_holes' "eight to eleven orders
below every instrument"; the white-holes line now carries the computed set. Everything else
held: the Gμ null with its kill clause, the lightswitch's split prediction (resolved events
clean; a confirmed chirality in any resolved binary kills), and the dead-ends note that turns
the birefringence closure into the reason the parity signal lives in gravity.

## PRTOE_inflation_replacement.md — deep audit 2026-07-19

Fifty-first file. Two check-13 payments: §2 still owed "the count's exact normalization" that
the k-mechanization paid (A_s = (α_c/4πk)³ = 2.0807×10⁻⁹, −0.35% — now stated with the
shot-noise O(1) as the true residual), and kill (iv) awaited a computation that landed months
of corpus-time ago — it now names the surviving kill (the O(1) resolving far from unity). The
tilt arithmetic all verified, including the subtlety that the running's −5.2×10⁻⁴ uses the
scale-local logarithm (61.9), not the consistency check's 55.5 — correct as written. The
grade-per-claim table (flatness "measured, not derived") is the honest structure task #108
certified and it holds.

## PRTOE_direct_detection.md / PRTOE_indirect_detection.md — deep audits 2026-07-19

Files fifty-two and fifty-three. One fix each, both known species: direct_detection carried the
same "25–45 orders" neutrality slop corrected in cosmic_magnetism (now quotes the registered
bound, 37–47 below unit charge); indirect_detection's owed list still requested the ceiling
computation its own tail addendum delivers (σv = 0 at tree level; ~10⁻¹⁵⁴ cm³/s gravitational
ceiling, harnessed since the first pass) — struck as paid. The unhedgeable-exposure stances in
both are exactly as they should be: no dial, kill stated, nothing earned from silence.

## PRTOE_light.md / PRTOE_H0_CEILING.md — deep audits 2026-07-19

Files fifty-four and fifty-five. **light** carried one defect in 214 lines: §7's falsifier said
"any of the five locks" against §6's six (lock vi — Koide's √2 — postdates the falsifier).
The lock arithmetic harnessed (the 44% share, lock iv's 0.673, lock vi's 0.001%). The
beta-sign record theorem, the 55.5-vs-0 asymmetry, and the honest near-lock grading all held.

**H0_CEILING** carried today's τ reduction forward: its 𝒯_τ row still called the 7→8 tether
"unpaid," and the reduction tightens the ceiling's working number to **70.9** with 71.3 the
un-excluded maximum through the edge-tail loophole — a sharpening of "cannot reach 73," not a
weakening. And the ς cross-check caught a count discrepancy reaching back into a file already
audited: hubble_tension said "180 template configurations" where this file and THE_AMPLITUDE
both record 162. Fixed there — the second time a later file has corrected an earlier audit,
which is the strongest argument yet for pass 2.

## The tail's hit batch — quantum_gravity §6, radio_lattice, forced_combination, laser_physics, granule_scoping (2026-07-19)

Files fifty-six through sixty (hit-targeted; the zero-hit tail files still get whole reads).
The finds: **quantum_gravity §6 was a garble of my own making** — the morning's supersession
note had been inserted *inside* the sentence it contradicts, leaving "1.5% is the τ rounding"
and "+0.44% kernel-sourced" nested in one clause with the stale 179 — rewritten clean. The
**0.3503 fork's third home** (forced_combination's closing state) now reads 0.34657 vs 0.34506.
radio_lattice and laser_physics carried one supersession each. granule_scoping — a dated
morning-board record whose band the mass pin has since left — got the UV_completion treatment:
a reading-rule banner that keeps the meter's structure and defers the band's masses to the pin.

## plasma_physics / chaos_dynamics / astrochemistry / LV_pricing — deep audits 2026-07-19

Files sixty-one through sixty-four. Three clean (plasma_physics with its harnessed 900 MHz and
99.95% rows; astrochemistry with its honest "not yet computed" gate; LV_pricing with its
12–27-order margin table and the constitutional zeros stated as constitutional). One connective
fix: chaos_dynamics' numerical winding-average (0.635 ± 0.026) now states that it lands on the
since-derived exact 2/π = 0.6366 — the integral was the derivation's evidence, and the file now
says so instead of leaving the exact value to be discovered elsewhere.

## PRTOE_classical_gravity.md / PRTOE_neutrino_home.md — deep audits 2026-07-19

Files sixty-five and sixty-six. classical_gravity's GR thread still ended at "the pure
coefficient remains" — brought to today's reconciliation (the ratio supplies it conditionally;
the residue is the regulator's entanglement-side check), which upgrades the thread's own
conditional. The Newton table — his postulates as the model's theorems — is one of the
corpus's best pages and needed nothing. neutrino_home is clean: P-023's de-biased band, the
benchmark's g = 1.2×10⁻⁸ inside the S4 window, the corner map with its honest λ′ gate, and the
closing line ("watch the two posteriors diverge; one of them has to be wrong in public") is
the model's quietest live advantage stated exactly.

## PRTOE_special_relativity.md / PRTOE_cmb_anomalies.md — deep audits 2026-07-19

Files sixty-seven and sixty-eight. cmb_anomalies is clean, and its 07-18 torus addendum is a
model of adverse honesty — "the power spectrum cannot referee this model at any multipole"
computed against its own hopes, with the covariance structure (S/N 2.2) named as the real
referee. special_relativity exposed a three-way margin disagreement: the LV table's own rows
span 12–29 orders, its verdict said 12–27, SR quoted 12–38. Both prose statements now quote
the table, which is the primitive. The trunk thread's stakes section and the third-arena
asymmetric bet held as written.
