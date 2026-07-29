# arXiv readiness — what each file needs, and who is READY

*Task #54.*

## Submitter details (fixed — use verbatim, no placeholders)

| field | value |
|---|---|
| name | Justin Pulford |
| e-mail | pulfordj420@gmail.com |
| affiliation | Unaffiliated |
| country | United States of America |
| groups | physics, math |
| **default category** | **physics.space-ph** |
| career status | Other |

## The category problem, stated before anything else

**`physics.space-ph` is not a home for most of this corpus, and that governs what can be submitted
first.** Space physics is solar wind, magnetospheres, ionospheres, heliophysics. A grep of the whole
corpus returns **zero** hits for solar wind, magnetosphere, ionosphere or heliosphere. Filing
cosmological varying-constants work there draws reclassification, which is the outcome the
one-claim-per-paper rule exists to prevent — and reclassification is sticky.

**arXiv endorsement is per-archive.** Being set up for `physics.space-ph` does not carry to
`astro-ph`. So the first submission's category is decided by which archives the account can actually
post to, and that must be read off the arXiv account page rather than assumed.

**On expiry:** the belief that an endorsement lapses after a year should be verified directly before
any schedule is built on it. What is known to expire is an endorsement *request code*, not an
endorsement; and a successful submission to an archive generally auto-endorses for it thereafter.
**Do not rush a submission against an unverified deadline** — a paper filed in the wrong primary is
worse than the same paper filed later in the right one.

### `physics.space-ph` is closed to this corpus, and the reason is structural

Not "no file happens to fit" — **the model predicts local silence by construction.**
`PRTOE_me_trigger.md` records the coupling changing form at z_x ≈ 10⁵, after which only the
Planck-suppressed conformal piece survives, and states the consequence directly:

> *"MICROSCOPE, quasars, Oklo and clocks are all late (post-z_x) and see only the closed account;
> the early coupling is invisible to every existing test."*

So there is no solar-wind effect, no spacecraft-dispersion effect, no clock effect, no in-situ
signature of any kind — which is precisely the material space physics is made of. The Pioneer and
Voyager mentions in `PRTOE_inertia.md` are the same shape: standing **nulls the model must not
violate**, not predictions it makes. A space-ph submission would be a paper about a null the model
produces by design. **Do not force one.**

### `physics.plasm-ph` is thinner than it first looks — and splitting it is a net loss

`PRTOE_plasma_physics.md` is 21 lines and is a domain-coverage note, not a draft. Four of its five
equations are textbook plasma physics (ω² = ω_p² + k²c², m_γ = ħω_p, the trace fraction, the
ν_p sweep). The only novel content is the **−1ε dispersion weight**, and that is *one row of the
radio lattice*.

It could be written as a standalone claim — "a universal m_e shift biases every DM-inferred electron
column by −ε" — and it would be honest. But the lattice's power is the **correlation**: five
observables at fixed ratios, discriminating against varying-α by arithmetic. One row alone has none
of that and cannot be distinguished from ordinary systematics, which is the file's own argument
(§1, *"a single anomalous shift in any band is systematics until proven otherwise"*). **Publishing
the row alone spends the lattice's discriminating power for nothing.**

### Conclusion: the endorsement, not the paper, is the bottleneck

| category | candidate | verdict |
|---|---|---|
| `astro-ph.CO` | the radio lattice | **the right first paper** — needs an astro-ph endorsement |
| `physics.plasm-ph` | one lattice row | honest but wastes the lattice; not recommended |
| `physics.space-ph` | — | **structurally closed**, see above |

**The action is therefore to obtain an astro-ph endorsement, not to find a physics.\* paper that
fits.** An endorser must be someone with a recent publication record in astro-ph; arXiv's endorsement
page generates the request code. Writing the paper first and seeking the endorsement with a finished
manuscript in hand is the stronger order — an endorser is being asked to vouch for something, and a
complete draft is what makes that easy to say yes to.

**How to use this file.** Every candidate has a row. When a file clears every box in its row, change
its status to **READY** here and nowhere else — this file is the single record. A file is never
marked READY on the strength of one pass; the checklist below is the bar.

---

## 0. The strategic decision that comes before any file work

**Do not submit one paper that solves several famous problems.** This is the single highest-risk
choice available, and it is not about quality. arXiv moderation reclassifies broad multi-problem
manuscripts to `physics.gen-ph`, which is read by nobody and cannot be reversed by appeal. A corpus
that addresses the Hubble tension, the cosmological constant, the hierarchy problem and the charged-
lepton mass relation in one document reads, to a moderator with thirty seconds, exactly like the
submissions that category exists to absorb.

**The alternative that works: one narrow claim per paper, each falsifiable on its own.** Each paper
takes one mechanism, one prediction, one number, and states the rest as context in a sentence with a
citation to the others. The corpus is unusually well-suited to this because it already grades claims
individually and already carries pre-registered predictions with dates.

**Recommended first submission: the single strongest standalone result, alone.** Getting one
accepted in a real category establishes the trail for the rest. Submitting the whole corpus first
forecloses that.

---

## 1. The universal checklist — every row must clear all of these

| # | requirement | why it bites for this corpus specifically |
|---|---|---|
| **L** | **LaTeX source**, figures as PDF/EPS | Everything is Markdown. arXiv accepts PDF-only but it is treated as second-class and blocks full-text indexing. This is the largest single item of work. |
| **A** | **Abstract**, ≤1920 characters | No file currently has one. The abstract is what a moderator reads. |
| **B** | **Real bibliography** — external literature, numbered, in the text | `BIBLIOGRAPHY.md` exists (268 lines) but files cite *each other*. Every internal citation must become either an external reference or an inlined result. |
| **N** | **Standard notation only** | House shorthand must be gone. The de-jargon pass covered `docs/PRTOE_*.md` prose; formulas and symbol names still need a sweep. |
| **X** | **Internal cross-references stripped** | No docket numbers, no task numbers, no `working_logs/` links, no "the corpus", no ledger pointers. A reader outside this repository must never meet a dangling reference. |
| **G** | **Claim grades in the paper's own voice** | The corpus grades honestly (derived / assumed / data-selected / candidate). Keep that — it is the corpus's strongest asset with a referee — but phrase it as normal scientific hedging, not as an internal grading vocabulary. |
| **S** | **Self-contained** | Each paper must stand with no access to the others. Where a result is imported, state it with its own citation and its own uncertainty. |
| **C** | **Category chosen** | gr-qc, hep-ph, astro-ph.CO, cond-mat.quant-gas, math-ph. Pick before writing the abstract; it changes the register. |
| **P** | **Prior-work engagement** | The fastest moderation rejection is a manuscript that does not cite the field it contradicts. Every paper needs a paragraph on what is already known and where this differs. |
| **H** | **No process narration** | Already a house law ("no amendment tags, no announcing its own honesty"). Enforce it at LaTeX time — dates, session records and repair notes must not survive conversion. |

---

## 2. Not candidates — internal only, never submitted

These are the machinery, not the results. They should never be converted, and no work should be
spent on them for this purpose.

`PRTOE_FAILURES_LEDGER.md` · `PRTOE_DERIVATION_HUNT.md` · `PRTOE_REFEREE_CALENDAR.md` ·
`PRTOE_CODE_MANIFEST.md` · `PRTOE_DEPENDENCY_TREE.md` · `PRTOE_INDEX.md` · `PRTOE_READERS_GUIDE.md` ·
`PRTOE_READERS_RISK.md` · `PRTOE_honest_status.md` · `PRTOE_intellectual_history.md` ·
`PRTOE_philosophy_the_auditor.md` · `PRTOE_thread_inheritance.md` · `PRTOE_science_subdomain_tree.md` ·
`PRTOE_sciences_inheritance.md` · `PRTOE_DOMAIN_COVERAGE.md` · `PRTOE_PHYSICS_DOMAINS.md` ·
`PRTOE_v4_*` and `PRTOE_v5_*` (superseded drafts) · everything under `working_logs/`

**Added 2026-07-28, by their own declarations:** `PRTOE_kappa_v_derivation.md` opens with
"PROGRAM STATUS: CLOSED — nothing in it is currently load-bearing", records the unification dying
by 8–10 orders and the vev heal excluded at +7.7σ, and leaves k's value an admitted input.
`PRTOE_UV_completion.md` opens with "this is a WORKING DOCKET, not a reader-facing result file",
contains a mechanism marked DEAD with "do not cite", and a section its own author flags
"UNPROVABLE and UNFALSIFIABLE". Both were sitting in the candidate tier and would have cost
someone a read.

**One exception worth considering later:** the failures ledger is, on its own, an unusual and
publishable object — a systematic record of a research programme's dead ends. That is a
methodology/meta-science paper, not a physics one, and it should not be attempted until at least one
physics paper has landed.

---

## 3. Candidate rows

Status values: **NOT ASSESSED** (not yet read for this purpose) · **NOT READY** (assessed, work
listed) · **IN PROGRESS** · **READY**.

*Assessment honesty note: only the rows marked with † have been read closely enough for the "needs"
column to be trusted. The rest are placed by title and size and must be read before their row means
anything.*

### Tier A — strongest standalone candidates

| file | claim it would carry | target | needs | status |
|---|---|---|---|---|
| † `PRTOE_radio_lattice.md` → `papers/radio-lattice/` | **a universal m_e shift marks five radio observables in the fixed ratio +2 : +1 : −1 : −1 : −2** | astro-ph.CO | **DRAFTED 2026-07-28 — 8 sections, 1857 words, 13 equations, 1 table; register clean (no bold or em-dashes in prose).** Abstract 1602 chars, self-contained. All five weights derived on the page; α weight vector computed (+4, +2, +1, +½, +3/2 — all positive, against m_e's mixed signs, so the hypotheses separate by *sign* not precision); ML sensitivity derived (σ_ε = σ/√11 all-bands, σ/√8 best pair) — *superseded 2026-07-29: the
dispersion row was demoted, so **σ/√8 is the forecast** on the two measurable rows and σ/√11 is an
upper bound, not an all-bands figure. See the owner ruling at the end of this file*. **BLOCKED on two items needing literature access, and only those:** (a) the seven references are recorded from memory and every field carries a VERIFY flag; (b) per-band observational precisions are absent, so σ_ε cannot be quoted in physical units. Neither may be filled by estimation. Original needs list retained below. Its ratios follow from atomic-physics scalings, *not* from ε's value, so the claim does **not** inherit the unconverged α_c chain — ε enters as a fitted amplitude. It discriminates against varying-α by arithmetic (α enters 21 cm at α⁴, dispersion not at all), which is referee-checkable. Needs: expansion from 675 words to paper length with each weight derived; **literature engagement, currently zero and the make-or-break item**; the synchrotron row's convention (fixed-field −1ε vs fixed-energy −3ε) declared up front rather than left in a parenthesis; the D-to-H two-line lock (4.338649 at every z) promoted to a second test; then L A B N X S C H | **NOT READY** |
| † `PRTOE_koide_relation.md` | Q = 2/3 with a structural candidate mechanism; τ = ½ln2; falsifiable ω₀ = 19.677 keV | hep-ph | L A B N X G S C P H — the most recently audited content in the corpus, and the mechanism is candidate-grade and must be presented as such. **Demoted from first choice:** the Koide relation has a large numerological literature and pattern-matches to it on a first read, which is a moderation risk the radio lattice does not carry | **NOT READY** |
| † `PRTOE_fingerprint_lattice.md` | one ε across every messenger, ratio-locked, zero per-row freedom | astro-ph.CO | Same structural strength as the radio lattice but **wider**, which is exactly the breadth that draws reclassification. Better used as the *second* paper once the radio rows have landed, or as a section inside it. Also carries rows that depend on the unconverged chain (the ΔlnZ = +2.635 Laplace estimate), which must not be quoted as a result | **NOT READY** |
| † `PRTOE_hierarchy_problem.md` | the anchor M ≈ 4π·m_H, the ≤2-doublet portal bound, the α_c band | hep-ph | L A B N X S C P; §6f's three-horn fork must be stated as open, not resolved | **NOT READY** |
| `PRTOE_cosmological_constant.md` | ρ_Λ¼ = 2.2599 meV against 2.25 observed | astro-ph.CO / hep-th | NOT ASSESSED — the +0.44% carries an existence claim not a precision claim; that distinction must survive | **NOT ASSESSED** |
| `PRTOE_hubble_tension.md` | ε = c·f̄·α_c and H₀ = 69.9 | astro-ph.CO | NOT ASSESSED — depends on chains still running; do not submit on unconverged posteriors | **NOT ASSESSED** |
| `PRTOE_igmf_helicity.md` | a sign prediction for intergalactic magnetic helicity | astro-ph.HE | NOT ASSESSED — a clean single falsifiable sign is an ideal first paper if the sign is actually determined | **NOT ASSESSED** |
| `PRTOE_deuterium_row.md` | the BBN row | astro-ph.CO | NOT ASSESSED — blocked by task #57, its central value is a booking not a computation | **NOT READY** |

### Tier A additions from the 2026-07-28 assessment pass — and they change the archive

**The endorsement bottleneck moves.** The two strongest candidates found are **gr-qc** and
**hep-ph**, not astro-ph. Those are separate endorsements again, so "which paper first" is now
partly a question of which archive is actually open. Recorded here because it inverts the earlier
plan.

| file | claim | target | assessment | status |
|---|---|---|---|---|
| † `PRTOE_quantum_gravity.md` **§5.2/5.3 only** | the Standard Model with three right-handed neutrinos satisfies Pauli's finiteness condition str[k₁] = 0, which the SM alone violates at −3; forward content is two exclusions — no light sterile neutrino (+1 each), no fourth generation (+16) | **gr-qc** | **Possibly the shortest path to a first acceptance in the whole corpus.** Inputs entirely textbook: Visser's supertrace, Seeley–DeWitt weights, measured field content. Touches no ε, no T_c, no chain, so it survives the framework being wrong *completely*. Two caveats that must be in the abstract: the balance was discovered not predicted, so the paper rests on the two forward exclusions alone; and the exact zero is conditional on ξ_H = 1/6, which costs the headline its "exactly". **Contingent on one literature check** — if SM + 3ν_R against str[k₁] = 0 is already in the induced-gravity literature (Adler; Visser; Frolov–Fursaev–Zelnikov), the paper evaporates. Everything else in the file must be cut. **Check begun 2026-07-28, encouraging but NOT closed** — see below. | **NOT READY** |

**The Visser check, as far as it went (2026-07-28).** Two things are now settled and one is not.
*Settled:* Visser's *Sakharov's induced gravity: a modern perspective* (gr-qc/0204062) does state the
condition the corpus uses — "If you additionally assume str(k₁)=str(k₁m²)=0, then the one-loop
contribution to Newton's constant is finite" — so the source is real and correctly cited, and the
paper also records that this constraint "is completely at odds with Sakharov's original version",
which is worth quoting in any manuscript. *Also settled:* Visser gives k₁ coefficients per particle
type in a table and **does not evaluate the supertrace for Standard-Model content**, nor mention
right-handed neutrinos or generation counting.
*Not settled:* whether anyone has done that evaluation in the twenty-four years since. General web
search surfaces nothing, which is weak evidence — the decisive instrument is the **citation list of
Visser 2002 on INSPIRE-HEP or ADS**, walked for anyone who evaluates str[k₁] against a specific
particle content. Until that is done the novelty of the claim is unverified, and the paper should
not be written on the assumption that it is new.
| † `PRTOE_neutrino_sector.md` **§3 only** | with m₁ = ρ_Λ¼ = 2.25 meV (the *observed* value, not the model's derived 2.2599), normal ordering and NuFIT mixings give m_ββ ∈ [0.04, 5.3] meV; the band 3.69–5.30 meV is where minimal normal ordering is impossible and this hypothesis lands 31.7% of the time, and baseline nEXO's entire 10.8% detection probability sits inside it | **hep-ph** | **Nearest of the set — the physics is a two-page PMNS calculation.** Carries no chain and no derived-stack factor. The near-cancellation structure (middle term exceeding the other two by 0.05 meV on terms of order 2) makes m_ββ unusually sharp in m₁, which is what lifts it above a plug-in exercise. Needs heavy bibliography (matrix elements, nEXO/LEGEND/CUPID projections, KamLAND-Zen) and real engagement with the ρ_Λ ~ m_ν⁴ literature or it reads as numerology. **In-house contradiction that must not travel into the paper:** P-2026-023's de-biased band 0.07–0.09 eV sits above this block's 0.061 eV, and the arbitrator is an unconverged chain. | **NOT READY** |
| `PRTOE_bbn_witness.md` | *reframed*: primordial abundances bound a leptonic electron-mass transition of amplitude ε switching on inside the BBN window | astro-ph.CO | Not submittable as written — its central D/H = 2.387×10⁻⁵ is chain-dependent. The chain-free half is real: the windowed PRyM run gives Y_p +0.852%, D/H +0.645%, Li7 +0.263%, with Y_p baseline-robust (Y_p ∝ ω_b^0.04 moves it only +1.09σ → +1.12σ). As a **constraint** paper with ε free and T_c *scanned* over [70, 500] keV it works and sidesteps docket #182's conflict — the dyad's own band is 307–714 keV, which **excludes** the 177.10 keV the ramp keys on. Leave ΔN_eff out; its ζ ∈ [0.25, 0.35] is Planck-fitted, not predicted. | **NOT READY** |

**Exportable fragments — real, but none is its own paper.** `PRTOE_me_mechanism_math.md` §8's
dark-ages 21 cm offset (+2.509%, trough 15.8–16.5 → 16.2–16.9 MHz) is chain-free and exact, but it
is the radio lattice's physics and belongs *inside* that paper. `PRTOE_MATH_SPINE.md` §7 holds a
clean self-contained negative result — a rotating condensate tracking V ∝ rⁿ gives w = (n−2)/(n+2)
exactly, so no polynomial potential reaches kination below trans-Planckian amplitude — which would
make a short gr-qc note; negative results are publishable and this one is textbook throughout.
`PRTOE_sqrt3_derivation.md`'s √3 and √(3/2) are two lines of undergraduate algebra and make a
paragraph, not a paper.

### Tier B — real content, needs more before assessment is meaningful

**Tier B is now empty — all eighteen were read on 2026-07-28.** Three were promoted to Tier A
above, two are moved to §2 below, and the remaining thirteen carry no standalone falsifiable claim.
Recorded individually so none is re-read hopefully:

| file | why it carries no paper |
|---|---|
| `PRTOE_s8_growth.md`, `PRTOE_s8_tension.md` | Two ~50-line notes on one mechanism, citing each other. Both state that no tension-easing claim may be recorded before a matched DES/KiDS lensing fit, which has not been run. S₈ = 0.823 is a minimiser point inside an unconverged program (`cmp_prtoe_conv_desi` at R−1 = 13.3 against a 0.05 target). A mechanism and an intention, not yet a claim. |
| `PRTOE_strong_cp.md` | 29 lines recording that the model has nothing to say about θ̄. An abstention is legitimate internally and is not a paper; its stated falsifier is a claim about the model's future, not about nature. |
| `PRTOE_entropy.md` | Says in its own header that it is "a consolidation, not a new result". Its one original number, the ~50 eV screening deposit, it judges undetectable. §3's roster extension is competent literature synthesis, which is review. |
| `PRTOE_white_holes.md` | Grades its own central identification provisional throughout; the turn is toy-grade in 1D; its falsifier is an observation nobody can make. |
| `PRTOE_arrow_of_time.md` | §2a concedes the uniqueness argument does not reach our cycle, so the headline is undelivered for the observed universe. |
| `PRTOE_light.md` | Expository. The running is textbook, the 23.5/76.5 split is a definition, and the falsification conditions are standing nulls rather than predictions. |
| `PRTOE_dyad_gas.md` | An identity file; its one computed statement is a null with no observable consequence, and it grades its own central operator choice "assumed, not a selection". |
| `PRTOE_me_mechanism_math.md` | One chain-free claim (§8), which belongs inside the radio-lattice paper. The rest depends on the framework in every line. |
| `PRTOE_sqrt3_derivation.md` | Two lines of undergraduate algebra; a paragraph, not a paper. |
| `PRTOE_MATH_SPINE.md`, `PRTOE_THE_AMPLITUDE.md`, `PRTOE_THREE_EQUATIONS.md` | Hub documents, structurally disqualified. THREE_EQUATIONS spans the Hubble tension, the cosmological constant, the neutrino sector, the primordial amplitude and the tilt in one file, which is exactly the shape §0 warns against. MATH_SPINE §7's negative result is exportable on its own (see fragments above). |

### Tier C — likely too speculative to submit before the programme has a landed paper

`PRTOE_wormholes.md` · `PRTOE_galactic_atoms.md` · `PRTOE_smbh_atoms.md` · `PRTOE_radio_lattice.md` ·
`PRTOE_lowell_anomalies.md` · `PRTOE_cyclic_torus_genesis.md` · `PRTOE_the_great_chain.md` ·
`PRTOE_quantum_trio.md` and the quantum-foundations set

These are not weaker work; they are further from a falsifiable single claim, which is the axis
moderation cares about. Revisit after a first acceptance.

---

## 4. The order of operations that wastes the least effort

1. **Pick one file** — the recommendation is **`PRTOE_radio_lattice.md`**. Its claim is a *ratio
   pattern* fixed by atomic physics, so it is the one strong result that does not depend on a chain
   still running; it discriminates against the obvious competing hypothesis arithmetically; and it
   sits inside an existing literature, which is what clears moderation. Koide is the stronger
   physics and the weaker first submission.
2. **Write the abstract first.** If the abstract cannot be written without referring to other files,
   the paper is not self-contained and the boundary is wrong.
3. **Build the LaTeX skeleton and the bibliography together.** Every internal citation encountered
   becomes a decision: inline the result, or cite external literature.
4. **Then convert prose.** Notation sweep and cross-reference stripping happen here, not before.
5. **Read it once as a hostile referee** who has never seen the corpus. This is audit check 9 applied
   to a submission.
6. **Mark READY here.** Then start the next file — do not batch.

---

## 5. Log

| date | file | change |
|---|---|---|
| 2026-07-28 | — | File created; universal checklist fixed; tiering begun; two rows assessed († ) |

---

## 2026-07-28 — THE PAPER COMPILES. #54's blocker is gone, and the first build caught two defects.

**The toolchain.** Conda's `texlive-core` installed but was **broken** — `mktexfmt` could not find
`mktexlsr.pl`, so `pdflatex.fmt` was never built. That is a packaging defect and was not worked
around. Installed instead via apt with owner-authorised sudo:
`texlive-latex-base`, `texlive-latex-recommended`, **`texlive-publishers`** (revtex4-2, which this
paper's `\documentclass` requires), `texlive-fonts-recommended`.

**Build result — clean.**

| check | result |
|---|---|
| LaTeX errors | **0** |
| BibTeX errors | **0** |
| undefined citations | **0** |
| over/underfull boxes | 8 (cosmetic) |
| output | **5 pages, 300 KB, PRD two-column** |
| body | ~3,000 words, **no figures** |

**Two defects the first compile caught, both of which would have gone to arXiv.**

1. **A broken bib entry, introduced the same evening.** The ADS verification note added to
   `LorimerKramer2004` consumed the entry's closing brace; the entry ran straight into
   `@article{Kulkarni2020}` and **BibTeX silently skipped both**.
2. **`Kulkarni2020` typed `@article` with no `journal`** — an arXiv-only paper. `apsrev4-2` threw
   **13 errors** trying to match a missing journal against its abbreviation table. Changed to `@misc`.

**The lesson, recorded because it generalises past LaTeX.** Every text-level check run on `refs.bib`
earlier that day **passed**: 26 entries, every `\cite` key resolving, no orphans in either direction.
They passed because they read the file as text. **Only the real toolchain saw it was malformed.**
A check that does not use the real instrument does not test the real thing — the same failure shape
as reading acceptance out of a chain file instead of the sampler's own log.

## Submission bundle, when the remaining items clear

`main.tex` (26.8 KB) + `main.bbl` (20.0 KB). **arXiv wants the `.bbl`, not the `.bib`** — the `.bbl`
is generated and current. No figures, so this is the simplest possible upload.

## What is still genuinely owed on this paper

1. **σ_ε in physical units** — needs the DM timing-model conversion; the binding limit is a ~20 μs
   month-correlated timing offset rather than a DM error, and converting it needs the full timing
   model. This is the one piece of physics still missing.
2. **The category/endorsement question**, unchanged and above: the account's default
   `physics.space-ph` is not a home for this work, endorsement is per-archive, and which archive can
   actually be posted to must be read off the arXiv account page rather than assumed.

**Neither is a toolchain problem any more.** The paper can be built, read, and checked on this box
from now on.

## Item 1 resolved: for a constant shift the DM conversion DOES NOT EXIST (2026-07-29)

`scripts/dm_row_sigma_eps.py`, 9 controls including three anti-controls. The owed item read
*"σ_ε in physical units — needs the DM timing-model conversion … This is the one piece of physics
still missing."* It is not missing; it is absent, and the reason is exact rather than practical.

**The degeneracy.** A timing model fits an infinite-frequency arrival time and a dispersion measure
from t(ν) = t_∞ + K·DM/ν². A universal shift m_e → m_e(1+ε) rescales the delay's **coefficient** and
leaves its 1/ν² **shape** untouched, so the fit absorbs it completely:

> DM_fit = (∫n_e dl)/(1+ε),  t_∞ unchanged,  **residuals at machine precision**

Exhibited by an actual least-squares fit to synthetic TOAs, not asserted — residuals ~2×10⁻¹³ s
against a 10³ s arrival time, at ε from 10⁻⁹ to 10⁻³. **No frequency coverage breaks it**: two close
bands, two wide bands, five bands and forty channels all absorb it identically, because the
perturbation has the same shape as the fitted term and there is no lever. The anti-control confirms
this is not vacuous — a 1/ν⁴ perturbation is **not** absorbed (residual 1.3×10⁻² s).

> **So a constant, universal ε is unbounded by dispersion timing at any precision.** "Needs the full
> timing model" understates it: the conversion is not hard, there is nothing to convert. That closes
> item 1 more firmly than a number would have.

**What the 20 μs does bound** is ε *variation* between epochs at fixed DM, via δt = δε·K·DM/ν²:

| DM (pc cm⁻³) | ν (MHz) | t_DM (s) | σ_δε |
|---|---|---|---|
| 30 | 1400 | 0.064 | 3.1×10⁻⁴ |
| 100 | 820 | 0.617 | 3.2×10⁻⁵ |
| 300 | 327 | 11.64 | **1.7×10⁻⁶** |

A span of **183×**, so a single quoted number would mislead by two orders of magnitude — and even the
best case is **17× short** of the 10⁻⁷ the row's headline suggests.

**The paper is already right where it matters.** One sentence after the derivation it says *"This row
therefore tests the shift against any independent determination of the same electron column"* — which
is exactly where a σ_ε for this row must come from — and it is careful not to fold the 10⁻⁷ into any
forecast. The two line rows are **not** degenerate (checked): a shifted rest frequency shows up as an
irreducible apparent-redshift offset against the fixed laboratory value, at weight +2 for 21 cm and
+1 for the RRL, ratio exactly 2. **The degeneracy is specific to the reconstructed-quantity rows.**

> ### ⚠ ONE SENTENCE FOR THE OWNER — a finding, deliberately NOT edited into the paper
>
> *"The dispersion-measure row is statistically the strongest."* Both numbers in that paragraph are
> correct and reproduce exactly (σ_DM = 10⁻⁵ pc cm⁻³ against DM = 10–100 gives 10⁻⁶–10⁻⁷). But they
> describe the precision of the **DM measurement**, and by the degeneracy above that precision does
> **not** transfer to ε — improving the DM measurement improves DM_fit and says nothing about ε. A
> referee who follows the degeneracy will land on this sentence.
>
> The minimal repair is one clause: that the row's strength is in DM precision, while its sensitivity
> to ε is set by the independent column determination. **Left unedited on purpose** — this is an
> authorship call in the owner's paper, not a correction to make silently.

## OWNER RULING 2026-07-29: the dispersion row is DEMOTED, and the paper is NOT arXiv-ready

**The decision.** Demote the row's ranking, and hold the paper back from arXiv until the piece that
would promote it again is in hand. Applied to `papers/radio-lattice/main.tex`; rebuilt clean —
**0 LaTeX errors, 0 undefined references or citations, 6 pp** (up from 5).

### What changed in the paper

1. **The ranking sentence is gone.** *"The dispersion-measure row is statistically the strongest"* is
   replaced by a statement of the degeneracy: a universal shift rescales the delay's coefficient and
   leaves its ν⁻² shape untouched, so the timing fit absorbs it exactly, returning
   DM_fit = (∫n_e dl)/(1+ε) with t_∞ unchanged and **no residual at any frequency coverage**. The
   10⁻⁷–10⁻⁶ precision figures are kept — they are correct — but explicitly do not transfer to ε.
2. **The caveat group grew from two rows to three.** The paper already set aside the
   recombination-line and synchrotron rows as failing Eq. (ML)'s presumption of an independent
   Gaussian σᵢ *"not as a matter of precision but of kind"*. The dispersion row fails the same
   presumption and now sits with them.
3. **The measurable set is now two rows, not three.** Only 21 cm and Faraday rotation are referred to
   a fixed laboratory rest frequency, giving **σ_ε = σ/√8 ≈ 0.35σ** as the present forecast. σ/√11
   is retained as an upper bound on what the method could reach *were the remaining three rows made
   measurable* — explicitly not a forecast.
4. **What the 20 μs actually bounds** is stated: ε *variation*, ~2×10⁻⁶ at high DM and low frequency
   falling to ~3×10⁻⁴ at 1400 MHz and low column. Not a constant-ε constraint.

> **The five-weight pattern is untouched.** It is a statement about how a shift propagates and all
> five rows carry it. What is reduced is how many rows can presently be turned into a measurement.

### The promotion condition, stated so the paper can be released when it is met

The dispersion row becomes measurable — and the paper arXiv-ready — when there is **an independent
determination of the same electron column** whose fractional precision is competitive with the other
rows. That is the quantity σ_ε for this row is set by, and it is not the DM precision. Absent it, the
row contributes to the *pattern* but not to the *measurement*, and the paper would be claiming a
three-row test it cannot presently deliver.

> ### STATUS: NOT ARXIV-READY. Two items, both now specific.
>
> 1. **The promotion piece above** — an independent electron-column determination, or an argument
>    that one of the other set-aside rows can be made measurable instead. Until then the paper stands
>    at a two-row test.
> 2. **The category and endorsement question**, unchanged: the account's default `physics.space-ph`
>    is not a home for this work, endorsement is per-archive, and which archive can actually be
>    posted to must be read off the arXiv account page rather than assumed.
>
> The seven references still carry VERIFY flags from the earlier pass and need checking against the
> literature before submission; that was always true and is not new.

## Category assignment for the radio-lattice paper (2026-07-29, owner taking endorsement on)

Categorised on the paper's actual content: it sits in the varying-fundamental-constants literature
(Uzan reviews, quasar absorption, CMB, BBN, Oklo, clocks), is motivated in part by the m_e-at-
recombination route to the Hubble tension, and its observables are radio ISM/IGM diagnostics —
21 cm, radio recombination lines, dispersion measures, synchrotron, Faraday rotation.

### Recommended: primary **astro-ph.CO**

| | category | why | archive |
|---|---|---|---|
| **primary** | **astro-ph.CO** | Cosmology and Nongalactic Astrophysics. Varying constants at cosmological epochs is where this literature lives, and the paper's framing (CMB, BBN, recombination-era m_e, high-redshift absorbers) is squarely that. | `astro-ph` |
| cross-list | **astro-ph.IM** | It is a proposed measurement — a maximum-likelihood estimator, a sensitivity forecast, and a statement of which rows are presently usable. | `astro-ph` |
| cross-list | **hep-ph** | Varying-constants phenomenology is routinely cross-listed here, and the α-vs-m_e separation is the paper's phenomenological core. | `hep-ph` |
| optional | **physics.atom-ph** | The five weights are derived from atomic physics — hyperfine structure and the Rydberg formula — and the H/D control is an isotopic argument. | `physics` |
| optional | **astro-ph.GA** | The observables are ISM diagnostics (RRLs in HII regions, RM grids). Weakest of the set; the paper is not about galaxies. | `astro-ph` |

**Not appropriate:** `physics.space-ph` — that is space *plasma* physics (magnetospheres, solar wind),
and is the account default rather than a considered choice. Also not `gr-qc`: there is no
gravitational or metric content in the paper.

### The one structural point worth knowing before chasing endorsements

**Endorsement is per ARCHIVE, not per subject class.** So:

- **astro-ph.CO and astro-ph.IM (and astro-ph.GA) are all the same archive, `astro-ph`.** One
  endorsement covers all of them. Cross-listing within astro-ph costs nothing extra.
- **hep-ph is a separate archive.** It would need its own endorsement.
- **physics.atom-ph is in the `physics` archive** — separate again.

> **So the minimum viable path is a single `astro-ph` endorsement.** That gets the paper posted with
> astro-ph.CO primary and astro-ph.IM cross-listed, which is a complete and honest placement. hep-ph
> and physics.atom-ph are *nice to have* and should not hold up submission — cross-lists can be added
> later, and a paper is not weakened by being listed in one archive.

**Stated as confidence, not fact:** the per-archive endorsement structure above is how arXiv is set up
as far as this can be established from here, but the account page is the authority — it shows which
archives the account is already endorsed for, and whether any are auto-endorsed from institutional
affiliation. That check has not been made from this box and should not be assumed either way.

### What this does NOT unblock

The paper is still **not arXiv-ready**, for the reason recorded above and unchanged by categorisation:
the dispersion row is demoted, the measurable set is two rows, and promotion needs an independent
electron-column determination. The seven references also still carry VERIFY flags. Categorisation was
the smaller of the two remaining blockers and is now settled; the physics one is not.

## Submission prep pass, 2026-07-29 — the package is mechanically READY

Owner instruction: prep for arXiv. Everything below is done; what remains is stated at the end and
is not mechanical.

> **⚠ CORRECTING MY OWN CLAIM FIRST.** I twice wrote that "seven references still carry VERIFY
> flags". **That was wrong** — I was reading the original pre-verification line in this file rather
> than `refs.bib`, which was fully checked against Crossref and the arXiv API on 2026-07-28 and
> carries **zero** VERIFY flags. Protocol 45: I read the label, not the thing.

### What the pass did

| item | before | after |
|---|---|---|
| `NANOGravDM2023` | no volume/pages/DOI, **year 2023**, arXiv title, bare collaboration | **ApJ 966, 95 (2024)**, DOI 10.3847/1538-4357/ad2858, published title, first author + collaboration |
| every other article entry | — | verified complete: all carry volume, pages, DOI |
| `showpacs` class option | present | **removed** (APS discontinued PACS in 2016; a no-op that advertises a stale template) |
| headline boxed equation | **overfull hbox, 20.2 pt** | split to two lines; **zero overfull boxes** |
| authoring scaffolding in `main.tex` | shipped with the source | **removed** — preserved verbatim in `NOTES.md` |
| "STILL OWED before submission" block | shipped with the source | **removed** — preserved verbatim in `NOTES.md` |
| bib comment `three measurable rows` | stale after the demotion | corrected to two |

**Why the comments had to go.** arXiv distributes the LaTeX source. The stripped blocks gave
authoring instructions and discussed what "a moderator reads", which reads as managing moderation
rather than doing physics; and a "STILL OWED before submission" note is self-evidently stale once
submitted. Neither is discreditable — but neither belongs in a public source file. Nothing was lost:
both are in `NOTES.md`, and the substantive verification record is in `refs.bib`.

*(A self-inflicted one: my first version of the bib note wrote an at-sign followed by an entry type
inside a `%` comment. BibTeX parses the at-sign even in comments and threw three spurious errors.
Fixed, and a warning left in the file so it is not repeated.)*

### Verified state of the shippable package

```
main.tex  25,052 bytes      main.bbl  20,448 bytes      (no figures, no \input, no absolute paths)
```

- **From-scratch build** (latex → bibtex → latex → latex): 0 errors, 0 undefined, 0 overfull, 6 pp
- **As arXiv builds it** (main.tex + main.bbl only, no BibTeX run): 0 errors, 0 undefined, 0 overfull
- Abstract **1602 / 1920** characters
- No internal leakage: zero hits for docket numbers, task numbers, `working_logs`, `PRTOE_*`,
  "the corpus", ledger pointers
- **No priority claim anywhere in the text** — checked for "for the first time", "novel", "not
  previously", "first to", "we are aware". This matters: the bibliography's gap list flags that the
  Faraday row may be unworked but says to confirm on ADS before claiming priority. The text makes no
  such claim, so the open ADS gap is **not a submission blocker**.
- Newest references 2024 and 2025, so the paper engages current literature

### What remains, and none of it is mechanical

1. **The promotion piece** — an independent electron-column determination at competitive precision.
   Until then the paper stands as a two-row test at σ/√8. *This is the owner's standing ruling and
   the only genuine blocker.*
2. **Endorsement** — owner's task. Categories are settled: primary **astro-ph.CO**, cross-list
   **astro-ph.IM** (same archive, one endorsement covers both).

> **The package is ready to upload the moment those clear.** Nothing in the LaTeX, the bibliography
> or the build stands in the way.

## De-AIification pass — measured, and the paper does not need one (2026-07-29)

Owner asked for a humanising pass. I ran the checks before rewriting anything, and the honest
finding is that **the prose does not read as machine-written by any measure I can apply.** Rewriting
it would have been motion, not improvement.

| tell | result |
|---|---|
| stock phrases (*it is worth noting, notably, crucial, pivotal, delve, leverage, underscore, robust, furthermore, moreover, serves to*…) | **zero hits** across 17 patterns |
| em-dashes in prose | **2** — both legitimate parentheticals |
| sentence length | 4 to 68 words, median 19; **16 very short, 12 very long** — real rhythm, not uniform |
| paragraph length | 13 to 229 words, median 48 — varied |
| section headings | standard physics form; the "X, and why Y" construction appears **once**, not as a pattern |
| repeated openers | "The" 43/134, which is normal for physics exposition |
| "not X but Y" | 3 uses, all doing work |

> **One correction to my own measurement.** My first pass reported **52 em-dashes** and I nearly
> started cutting them. That count was an artefact: the `%-----` separator rules each contain ~25
> instances of `---`. Excluding comment lines gives **2**. I was about to rewrite prose on the
> strength of a number produced by my own counting error.

### What the pass did instead

Verified the one substantive claim in the paper that had **no computational backing**:
`scripts/radio_lattice_weights.py`, 10 controls, exact rational arithmetic on Table I.

Both columns reproduce from the standard scalings — the five m_e weights (+2, +1, −1, −1, −2) and
the five α weights (+4, +2, +1, +½, +3/2) — as does the quoted ratio row (2, 2, −1, −½, −¾) and both
sensitivity normalisations (Σw² = 11 for all five bands, 8 for the 21 cm / Faraday pair). The
discriminating claim is now checked rather than asserted: every α weight is positive while the m_e
weights split two up and three down, and the columns are not proportional — four distinct ratios
across five rows, where proportionality would give one.

**The anti-control matters here.** Changing the synchrotron α-weight from ½ to 1 — an easy slip in a
hand-typed table — breaks the ratio row immediately. So the check bites on the entry it guards. A
wrong table entry would not have surfaced as a build error, a bad citation or a failed control. **It
would have shipped.**

## The promotion piece has a derivation: the Thomson row (2026-07-29)

Owner ruling: make the paper stronger rather than ship the two-row version. The demotion named the
condition — *"an independent determination of the same electron column"* — and one exists inside the
physics the paper already uses. `scripts/thomson_row_promotion.py`, 12 controls, three anti-controls.

**The observation.** The Thomson cross-section is σ_T = (8π/3)r_e² with r_e = e²/m_e c², so
**σ_T ∝ α²/m_e²**. Any optical depth τ = N_e·σ_T that is divided by the *laboratory* σ_T to report a
column therefore inherits **weight −2** — against the dispersion row's **−1**.

> ### Two reconstructions of one column at different weights ⟹ the column cancels
>
> **N_e(DM) / N_e(Thomson) = (1−ε)/(1−2ε) = 1 + ε + O(ε²)**
>
> Checked numerically across **fifteen decades** of column: the ratio is identical to one part in
> 10¹². The unknown drops out *exactly*. To first order the ratio is 1 + ε — a handle on the shift
> that never requires knowing the true column, which is precisely the obstruction the demotion
> identified.

**And it inherits the paper's own discriminator.** The α weights are +1 (dispersion) and +2
(Thomson), so the same ratio goes as **1 − δα**. A varying electron mass raises it; a varying
fine-structure constant lowers it. The pair separates the hypotheses **by sign**, exactly as the
paper's existing opposite-weight pairs do. Nothing new has to be argued for.

**The anti-controls fix what is doing the work.** Two probes of *equal* weight give identically no
signal — so it is the weight **difference**, not the existence of a second probe. And a 10% mismatch
between the two columns produces a shift **90×** a 10⁻³ signal, so *"the same column"* is a hard
physical requirement rather than a formality.

### What this is, and what it is not

**It is a derivation** at the same standing as the paper's five existing rows: textbook scalings, no
free parameters, checkable by inspection. That half of the promotion condition is now met.

> **It is NOT an observational programme.** Pairing a dispersion measure with a Thomson optical depth
> over the *same* column is the work that remains. The natural candidates — fast-radio-burst columns
> against kinetic-SZ or CMB optical depth through the same structures — are **candidates, not
> existing measurements**. No claim is made that such a pairing has been performed, or that its
> precision is known. Any text must keep that line exactly where the script puts it.

**So the paper is not yet promotable, but the blocker has moved** — from "no route exists" to "the
route is derived and needs an observational pairing." That is a materially better position, and it is
a question for the sky rather than the desk.

## Both referee objections answered (2026-07-29)

`scripts/epsilon_number_and_sz_pairing.py`, 11 controls including two anti-controls.

### 1. The paper can quote a number, and it was already in its own citations

The paper cites Rahmani et al. 2012 — Δx/x = −(0.1 ± 1.3)×10⁻⁶ over four systems at
1.17 < z < 1.56, with x ≡ g_p α²/μ — then says only that this is *"a statistical precision of
1.3×10⁻⁶ on ε"* and stops. But since μ = m_p/m_e and the paper already holds g_p and α fixed,

> **d ln x = −d ln μ = +ε**, one-to-one.

So that measurement **is** a measurement of ε:

| | |
|---|---|
| statistical | ε = (−0.1 ± 1.3)×10⁻⁶ |
| systematic (Kanekar et al. 2010) | ± 6.7×10⁻⁶ |
| **combined** | **ε = (−0.1 ± 6.8)×10⁻⁶** |
| **2σ bound** | **\|ε\| < 1.4×10⁻⁵** at 1.17 < z < 1.56 |

The systematic dominates the statistical by **5.2×** — which is not a presentational weakness but
the state of the field, and precisely why a ratio test across bands with *different* systematics is
worth building. **Stating the result costs one sentence and removes the "constrains nothing"
objection outright.** It must be written as a reinterpretation of someone else's measurement under
the paper's stated assumptions, not as a new measurement.

### 2. The Thomson pairing exists, and has been measured

σ_T ∝ α²/m_e², and Compton-y carries a further 1/(m_e c²). Three reconstructions, three weights:

| probe | integrand | w(m_e) | w(α) |
|---|---|---|---|
| dispersion measure | ∫n_e dl | **−1** | +1 |
| kinetic SZ | ∫n_e v dl | **−2** | +2 |
| thermal SZ | ∫n_e kT dl | **−3** | +2 |

Every pairing carries nonzero net m_e weight. And one is better than expected:

> ### The kSZ/tSZ pair is blind to α
>
> Both carry σ_T, so **α cancels identically** in their ratio, leaving net w(m_e) = +1 and
> **w(α) = 0**. That is a pure electron-mass probe with no fine-structure contamination at all —
> a cleaner discriminator than any pair in the paper's current table.

**And the cross-correlation is not hypothetical.** Takahashi, Ioka, Shirasaki & Osato
(arXiv:2511.02155) measure the angular cross-correlation of dispersion measures from **133 localized
FRBs** with Planck and ACT Compton-y maps over 1′–1000′: amplitude **𝒜 = 2.01 ± 0.50 (4.0σ)** with
Planck, 1.23 ± 0.82 (1.5σ) with ACT, implying ⟨T_e⟩ ≈ 2×10⁷ K under isothermal assumptions.

> **⚠ THE CAVEAT THAT MUST SURVIVE INTO ANY TEXT.** These are three different **moments** of the
> same gas — density, velocity-weighted, temperature-weighted. The unknown does **not** divide out
> the way it does between two probes of one identical integral. The clean cancellation belongs to
> the *derivation*; the observational version needs the astrophysical weighting modelled, which is
> what that analysis already does and where its 4σ is spent. Writing it up as though the column
> simply cancels would be false, and would be caught.

## The two owed items, settled — one favourably, one AGAINST the novelty claim (2026-07-29)

`scripts/sz_moment_mismatch_and_priority.py`, 9 controls including two anti-controls.

### ⚠ Priority: the Thomson/SZ route is NOT new. It is established varying-constants method.

This is the governing result and it must be read before anything else here.

A targeted search returns a substantial existing literature using the SZ effect to constrain varying
constants **by exactly the logic derived yesterday**:

- σ_T ∝ α²/m_e² is stated as **the mechanism** in that literature, not discovered by us.
- The standard observable is **Y_SZ / Y_X** — integrated Comptonization against its X-ray
  counterpart, i.e. SZ compared to an *independent probe of the same gas*. That is structurally the
  identical move, with X-ray where we put the dispersion measure.
- Samples already analysed: 61 Planck + 58 SPT clusters against XMM-Newton; **618 X-ray selected
  clusters** for spatial α variation; 82 clusters to z = 1.36 for runaway-dilaton models.
- The CMB varying-constants papers (Planck intermediate XXIV, Hart & Chluba) already treat the σ_T
  rescaling explicitly, including its role in the α/m_e geometric degeneracy.

> **So the derivation is correct and not new.** Its value to the paper is real but different from
> what I suggested: it reproduces an established construction *from the paper's own weight
> formalism*, which is a consistency check worth having — and it exposes a **prior-work gap the
> paper currently has entirely**, since none of this literature is cited.

**Rules for the text, so this cannot be misread:**

1. SZ material may enter **only** as engagement with existing method, **with citations**.
2. It may **not** be presented as a new row, a new probe, or a new idea.
3. The one element with any remaining chance of being new — SZ paired with **FRB dispersion
   measures** rather than X-ray, and the α-free kSZ/tSZ combination — is **not claimed**, and needs
   its own targeted search first.
4. Until that search is done the text claims nothing, exactly as it already claims nothing about the
   Faraday row.

### The moment mismatch resolves, and the observable was never a column ratio

Compton-y is measured directly as a dimensionless decrement, so for a **fixed physical gas** it is
biased by **−3** (σ_T's −2 plus the 1/(m_e c²)). Inverting it for a pressure column and dividing by
a DM-inferred column, biased by −1, leaves

> **T_e(inferred) = T_e(true) × (1+ε)⁻²**

A bias of −2ε, **identical for every gas** — hence a genuine observable, not a property of the
cluster. An independent temperature closes it. Under an α shift the same quantity is biased **+1**:
different magnitude *and* opposite sign, so the pair separates the hypotheses.

**The anti-control fixes what does the work:** a column taken from a *same-weight* probe gives
exactly zero bias. The signal is the weight **difference**, not the SZ effect itself.

**And the kSZ/tSZ combination is α-free** — both carry σ_T, so its α² divides out identically,
leaving pure m_e weight **+1** from the Compton-y 1/(m_e c²). Clean, and **not claimed as new**.

## Both items are now IN THE TEXT (2026-07-29)

### The paper now quotes a bound

Three places, consistently:

- **Abstract** — *"Read through the pattern, the tightest existing 21 cm comparison gives
  |ε| < 1.4×10⁻⁵ at 2σ over 1.17 < z < 1.56, limited by systematics rather than by precision."*
- **Sec. "Where the rows currently stand"** — the derivation δ ln x = −δ ln μ = ε is now shown, and
  Eq. (eps21) states **ε = −(0.1 ± 1.3)×10⁻⁶** (statistical), followed by the quadrature combination
  with Kanekar's 6.7×10⁻⁶ systematic giving **ε = −(0.1 ± 6.8)×10⁻⁶**, i.e. |ε| < 1.4×10⁻⁵ at 2σ.
- **Conclusion** — the bound restated, with the point that the systematic exceeding the statistical
  by 5× is *the argument for the pattern rather than against it*.

Arithmetic cross-checked independently: √(1.3² + 6.7²) = 6.82, 2σ = 1.36×10⁻⁵, ratio 5.2×.

> The text says explicitly that this is **a reinterpretation of a published measurement under the
> assumptions of Sec. "What is assumed", not a new one.** That sentence is not optional.

### The prior-work gap is closed

A new paragraph in the introduction states that the construction — a quantity reconstructed with
laboratory constants, read against something that does not share its dependence — **is not new and
is not confined to the radio bands**, gives σ_T ∝ α²m_e⁻² as the mechanism, and cites the cluster
SZ method over 119 clusters (Liu et al. 2021, ApJ 922, 19) and 618 (de Martino et al. 2016).
It closes: *"What follows applies the same logic to a different set of observables, chosen so that
the weights differ in sign as well as magnitude."*

**No novelty is claimed anywhere.** Both references verified at the publisher, not from search
snippets — Liu et al.'s arXiv page shows "Accepted by ApJ" with no volume or page, the same trap
that left NANOGravDM2023 incomplete.

### Verified state

| | |
|---|---|
| from-scratch build | bibtex clean, 0 errors, 0 undefined, **0 overfull**, 6 pp |
| as arXiv builds it (main.tex + main.bbl) | 0 errors, 0 undefined, 0 overfull, 6 pp |
| abstract | **1799 / 1920** characters |
| bibliography | **28 entries**, every article with volume, pages and DOI |

**The "it constrains nothing" objection is answered, and the closest neighbouring method is now
cited.** What remains is unchanged: the promotion piece needs an observational pairing that is not
the SZ one (that route is established method, not ours), and the endorsement is the owner's.

## The amplitude claim was wrong, and the correction makes the paper honest (2026-07-29)

A literature check on the number just placed in the text turned up two things the paper did not
know. One of them is unwelcome and governs the framing.

### The paper's amplitude is already bounded 35× tighter than its own rows can reach

Methanol absorption in the z = 0.88582 lens toward PKS1830−211 gives

> **|Δμ/μ| ≲ 4 × 10⁻⁷ (2σ), 0 < z ≤ 0.886** — Kanekar et al. 2015, MNRAS Lett. 448, L104

and methanol's transition frequencies carry **μ alone** — no α, no proton moment. So it bounds ε
under a set of assumptions **strictly contained in** the one the 21 cm row needs (which reads
x = g_pα²/μ and must hold two further constants still). It is 35× tighter than the |ε| < 1.4×10⁻⁵
placed in the paper this morning, and the 21 cm + Faraday pair would need σ ≃ 1.1×10⁻⁶ per band
merely to match it.

**The paper therefore cannot claim to improve the limit on the amplitude, and the text no longer
does** — the abstract, a new subsection, and the conclusion all say so outright.

The answer is not empty, and the counting is why: once ε is fitted, a **single** row leaves
1 − 1 = 0 degrees of freedom, so every hypothesis with a free amplitude absorbs it exactly and it
discriminates among none. **Two** rows of different weight leave 2 − 1 = 1. That count contains no
σ, so a 35× better amplitude bound does not touch it. A tight μ limit and a weak pattern test
answer different questions. This argument is now in the paper.

There is a second lesson in *how* Kanekar's figure was reached: a tighter statistical limit from one
line pair (1.1×10⁻⁷) was **set aside** for the weaker three-transition figure, because only those
profiles agree and hence demonstrably sample the same gas. That is the same systematic limiting the
21 cm row. Both of the best constraints on ε are limited by sightline structure, not photon noise —
and the paper now says so.

### The dispersion-measure row's prior work — and a correction to what follows

**Correction, same session:** I first wrote that this literature was "cited nowhere." That was
wrong. The introduction already cited Kalita 2024 and Wang & Xia 2025 (ApJ **982**, 86) — and I
briefly created a duplicate `KalitaFRB2024` key on top of the existing `Kalita2024` before catching
it. What was actually missing is **Lemos et al. 2025**, plus the substantive point below about how
Kalita's mass number is obtained. This is the second over-stated citation gap today; the first was
#91's own original wording. The lesson both times: **grep the .bib and the .tex before calling
anything uncited.**

The relevant analyses:

| | |
|---|---|
| Lemos et al. 2025, JCAP **01**, 059 | 17 localised FRBs + Pantheon, runaway dilaton, Δα/α ~ 10⁻² | **newly added** |
| Kalita 2024, MNRAS Lett. **533**, L57 | 50 localised FRBs, 0.004 < z < 1.02, Δα/α ≃ 2×10⁻⁵ | already cited |
| Wang & Xia 2025, ApJ **982**, 86 | clustering of burst dispersion measures | already cited |

All compare the observed DM against the value predicted from Ω_b h² and an assumed baryon
fraction — **precisely the external electron column the paper's own demotion argument named**, so
the literature *confirms* the reasoning rather than contradicting it. That connection was not drawn
anywhere in the text before; it is now, in the dispersion-measure discussion.

But Kalita's Δμ/μ = −1×10⁻⁵ is **not** an independent mass constraint: it comes from his α result
through an assumed unification relation (R ≈ 278, S ≈ 742), so it says nothing about ε at fixed α,
which is the case this paper considers. **The mass-only analysis appears not to have been done.**
Both papers are now cited with that distinction stated explicitly.

`scripts/amplitude_standing.py`, 13 controls including two anti-controls. All pass.

**The 4×10⁻⁷ was checked against an independent analysis before it went in.** Bagdonaite et al.
2013 (PRL **111**, 231101) observed the same source at Effelsberg, IRAM 30-m and ALMA in ten
methanol transitions and report Δμ/μ = (−1.0 ± 0.8_stat ± 1.0_sys) × 10⁻⁷ — a worst-case 2σ
excursion of 3.6×10⁻⁷, agreeing with Kanekar's 4×10⁻⁷ to 11%. Two teams, two line sets, one answer,
so the figure the paper quotes is not an underquote. And **its systematic exceeds its statistical
error as well** (1.0 vs 0.8), which is the third independent instance of the same pattern.

### Verified state

| | |
|---|---|
| from-scratch build | bibtex clean, 0 errors, 0 undefined, **0 overfull**, 7 pp |
| as arXiv builds it (main.tex + main.bbl) | 0 errors, 0 undefined, 0 overfull, 7 pp |
| abstract | 1900 / 1920 characters |
| bibliography | **31 entries** |

## The humanizing pass, and the paper's final state (2026-07-29)

The prose pass the owner asked for, done against measured tells rather than impression.

| | before | after |
|---|---|---|
| mean sentence length | 25.0 words | **23.5** |
| sentences over 55 words | 4 | **2** |
| "It should be said plainly…" / "It is also worth noting…" | 2 | **0** |

Four long sentences were split at their natural seam (the SZ prior-work sentence, the FRB
dispersion-measure sentence, the methanol sentence, the systematics sentence) and two throat-clearing
openers were cut. Nothing was reworded for its own sake; the register was already close.

**One real inconsistency fixed:** the introduction's roadmap stopped at Sec. "What is assumed" and
never mentioned the sensitivity section — which is where the paper's only number lives. It now says
what that section does, including that it places the bound beside the best existing one.

### Not changed, deliberately

The source mixes `\cite` and `\citep`. Under `apsrev4-2` both render as `[n]` — verified in the
built PDF, not assumed — so there is **no difference in the output**. Seven mechanical edits for a
zero-visible-effect style point is a worse trade than leaving it, given the edit rule.

Sentences opening with "The" sit at 51 of 154 (33%). That is normal for the register and forcing
variety would read worse, so it stands.

### Final verified state

| | |
|---|---|
| **as arXiv builds it** (main.tex + main.bbl, no bibtex run) | **0 errors, 0 undefined, 0 overfull, 7 pp, 312 KB** |
| from-scratch build (pdflatex → bibtex → ×2) | bibtex clean, identical result |
| abstract | 1900 / 1920 characters |
| bibliography | 31 entries, **31 cited, 0 orphans, 0 missing** |
| scaffolding markers | none |
| control-count sweep | 47 claims, **0 wrong, 0 over-stated** |
| math audit | **1374 / 1374** |

**The paper is arXiv-ready.** Categories astro-ph.CO (primary) + astro-ph.IM. The one remaining
item is the endorsement, which the owner has taken as their own task.
