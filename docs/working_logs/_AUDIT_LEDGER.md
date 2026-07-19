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
