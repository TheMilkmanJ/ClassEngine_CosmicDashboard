# RED CHECK-12 — `docs/exploratory/` (45 files)

**Auditor:** RED (Agent 2). **Date:** 2026-08-05. **Posture:** adversarial. No fixes applied. No fabrications.

**Ground truth used for chain grading** (read directly, `chains/*.progress`, 2026-08-05):

| chain | last N | last timestamp | R−1 |
|---|---|---|---|
| `cmp_lcdm_mnu_bbnfix` | 24858 | 2026-08-05T04:55:58 | **0.047912** |
| `dyad_mnu_bbnfix` | 24677 | 2026-08-05T07:54:30 | **0.056889** |
| `cmp_prtoe_routeD` | 6517 | 2026-08-05T04:07:15 | **0.705291** |

`cmp_prtoe_routeD.launchlog` last rows 2026-08-05 11:08 (rank 0/1/2 stepping, ~40–44k steps, ~2.4–2.7k accepted) — chain live.

**Ground truth used for class 4** (`docs/PRTOE_PREREGISTERED_PREDICTIONS.md:1452–1512`, read in full): clauses 2 and 3 (the crown/null fork, including the 0.22% σ threshold) are **"not executable at present cosmological precision, and no lattice campaign can make them so — the limit is the sky's, not the lattice's."** Only **clause 4** (τ̂ outside [0.330, 0.370] at ≥3σ) is "live and fully executable." The registration says explicitly: *"do **not** book a lattice CONFIRM on this clause alone"* and *"no lattice CONFIRM/KILL on the 0.44% gap alone."* It also says the registration *"is therefore a τ prediction … the closeness of the predicted meV to the observed one is **not** what is being registered."*

---

## VERDICT ON THE PRIOR ROUND'S CLASS-1 "CLEAN CORPUS-WIDE" CLAIM

**FALSE.** The cure at `PRTOE_hierarchy_problem.md:636` holds — that line now reads as physics (`k_F` cancellation), not edit history. But **15 CONFIRMED class-1 survivors across 10 files** remain in `docs/exploratory/` alone, including an entire section (`README.md` "## Links: repaired 2026-07-28") and an entire file's spine (`PRTOE_fairbank_note_HOLD.md`, four sections). The class was not clean corpus-wide.

---

## FINDINGS TABLE

### Class 1 — repair-log document history

| file:line | quote | verdict |
|---|---|---|
| `README.md:104–115` | "## Links: repaired 2026-07-28 … The move broke markdown links in both directions. All of them have been rewritten: **62** references … **142** references … **7** references from `working_logs/` were repaired separately" | **CONFIRMED** — a whole section narrating the document tree's own edit operation to the reader |
| `PRTOE_fairbank_note_HOLD.md:47–56` | "## Terminology pass (2026-07-27, owner-authorized) … Letter changes: 1. \"dyad's nucleosynthesis window\" → \"electron-mass window at nucleosynthesis\" 2. \"genesis dilution ζ\" → \"dark-to-photon temperature ratio ζ\" … 5. Hyphen-as-dash fix" | **CONFIRMED** — literal before→after edit list |
| `PRTOE_fairbank_note_HOLD.md:59–61` | "## Line-by-line pass (2026-07-28) — Eleven terminology/units/fluency edits; no numbers moved (details in git history of that date)." | **CONFIRMED** — pure edit history + git pointer |
| `PRTOE_fairbank_note_HOLD.md:57` | "Staleness fixes: neutrino-sector retired scalar–Majoron merge reworded; deuterium §5 pre-correction Majoron clause aligned with corrected content" | **CONFIRMED** — edit history of *other* documents |
| `PRTOE_fairbank_note_HOLD.md:71` | "Edit *weakens* what the letter claims from numbers that currently favour the model" | **CONFIRMED** |
| `PRTOE_INTERACTION_ATLAS.md:662` | "**What the recorded mass did to the two arguments that used to sit here.**" | **CONFIRMED** — "used to sit here" is this document's own prior content |
| `PRTOE_INTERACTION_ATLAS.md:525` | "the torque version was struck mid-paragraph (the reflex is installed)" | **CONFIRMED** — narrates the act of editing |
| `PRTOE_INTERACTION_ATLAS.md:70–71, 73` | "(moved from Identities: translation, not derivation)" … "(moved from Identities, same ruling)" | **CONFIRMED** — this file's own section reorganisation |
| `PRTOE_THE_CHAIN.md:180` | "*(The draw-epoch conflict this item used to name is settled…)*" | **CONFIRMED** — "this item used to name" |
| `PRTOE_v4_dCDF_results.md:89–98` | "CodeRabbit review of the v4 commit (7 findings): fixed the effective_f_sigma8 memory leak … idm_g missing semicolon (cosmetic; compiled correctly). … a guard comment now protects that ordering." | **CONFIRMED** — an automated code-reviewer's findings + their fixes, shipped to readers |
| `PRTOE_quantum_entanglement.md:106` | "**Content boundary (Claude red cure 2026-08-03 + EN-D2/D3):**" | **CONFIRMED** — names an AI agent and a repair action in reader-facing prose (also class 2) |
| `PRTOE_quantum_entanglement.md:107` | "The older one-line claim \"identify \\(r\\) with the medium's pair parameter\" is **aspirational only** until E6–E7 close" | **CONFIRMED** — "the older one-line claim" |
| `PRTOE_kappa_v_derivation.md:116–117` | "Notation clarified: … (the note's shorthand \"w[(∂ξ)²]\" meant \"function of,\" not \"times\")." | **CONFIRMED** — corrects the document's own earlier notation to the reader |
| `PRTOE_math_story.md:73` | "*(the narrative decomposition this story once carried — c·f_amp·Ψ₀/M_red — was the road…" | **CONFIRMED** — "this story once carried" |
| `PRTOE_intellectual_history.md:161–162` | "The m_e coupling (the possible fourth graft) is under profile test as this document is written." | **CONFIRMED** (mild) — document self-narration + stale present tense |
| `PRTOE_PHYSICS_DOMAINS.md:981, 983` | "## The validation record (added 2026-07-13)" / "*(written 2026-07-07; maintained since)*" | SUSPECT |
| `PRTOE_PHYSICS_DOMAINS.md:386–388` | "an earlier segmented bound's death is filed in the failures ledger — the surviving bound is stated by its own stamped caveat **within the hour**" | SUSPECT — workflow timing leaked to reader |
| `PRTOE_laboratory_cousins.md:128` | "## The three rows added 2026-07-20, and what each is worth" | SUSPECT |
| `PRTOE_quantum_entanglement.md:103` | "**What changed vs storygrade:** E1–E2 are code-enforced limits, not prose." | SUSPECT |
| `PRTOE_hierarchy_problem.md:390–391, 417–418, 424` | "the one that *is* supplied was being carried silently, which is its own hazard" / "this had been carried silently" / "Nothing in §6c said so" | SUSPECT — narrates the document's own prior omission |
| `PRTOE_hierarchy_problem.md:1238–1240` | "*Changed:* the double-counting argument is downgraded from independent to conditional, and the fork is **re-labelled**…" | SUSPECT — grade history (legitimate) written as document re-labelling |
| `PRTOE_sqrt3_derivation.md:87` | "**t_turn ≈ 8.16 H⁻¹** (was 5.77 at B = 1)" | SUSPECT — value history |
| `PRTOE_THE_CHAIN.md:82` | "the older 781 was the Planck-anchored count" | SUSPECT |
| `PRTOE_v4_dCDF_derivation.md:28` | "Three real bugs found and fixed during first build (not just typos —" | SUSPECT |

**Legitimately cleared (grade history of a CLAIM, not edit history of the document):** `PRTOE_quantum_gravity.md:8` ("This path is no longer the home of the full QG hub" — the file *is* a MOVED stub; navigational, correct); `PRTOE_hierarchy_problem.md:726, 830, 483`; `PRTOE_PHYSICS_DOMAINS.md:168–171, 301, 318`; `PRTOE_INTERACTION_ATLAS.md:63–64, 194, 319, 413, 526`; `PRTOE_v4_dCDF_derivation.md:449` and the other eight "Grade: superseded lineage" footers.

### Class 2 — embedded editor instructions

| file:line | quote | verdict |
|---|---|---|
| `PRTOE_fairbank_note_HOLD.md:31–35` | "## Before send — 1. Re-run H₀ comparison on corrected chains; replace the provisional number if it moves. 2. Recheck m_ββ floor against final dark-energy scale. 3. If the xenon matrix element firms up, update nEXO overlap." | **CONFIRMED** — a to-do list for the author |
| `PRTOE_fairbank_note_HOLD.md:39` | "content edits to the letter are listed for **owner approval** first" | **CONFIRMED** |
| `PRTOE_v4_dCDF_results.md:132–135` | "**Traps**: OMP_NUM_THREADS=1 in ~/.bashrc throttles CLASS 12× (set per-command); clik imports only under system python3.12; after any rebuild verify BOTH classy .so files … are newer than every source .c file." | **CONFIRMED** — operator runbook in a docs file |
| `PRTOE_v4_dCDF_results.md:77` | "**Fix candidate**: (1+w) factors in the dcdf gauge-transform / metric_euler terms in perturbations.c." | **CONFIRMED** — a coding TODO |
| `PRTOE_kappa_v_derivation.md:20–21` | "\"Derived\" may not re-inflate; **this header governs every summary of this document.**" | **CONFIRMED** — instruction to whoever writes summaries |
| `PRTOE_quantum_superposition.md:14–15` (also `:108`) | "Claim S4 (Born *value*) is **OPEN-BLOCKED** — **do not book as derived; do not soft-close via addenda.**" | **CONFIRMED** |
| `PRTOE_quantum_superposition.md:145`, `PRTOE_quantum_entanglement.md:129` | "*Seating language allowed. \"Transactions proved\" / derived atomic QM **forbidden**.*" | **CONFIRMED** — a writing rule for the next seat |
| `PRTOE_sqrt3_derivation.md:90–91` | "**Do not identify** `dcdf_floor_thaw` with B·√3 — the code parameter is 1+w today" | **CONFIRMED** — aimed at a code operator |
| `PRTOE_intellectual_history.md:173–177` | "*Primary sources: git history of this repository …, archive/root_cleanup_20260705/**HANDOFF_FOR_GEMINI**.md (the v3 closure), and the session memory files.*" | **CONFIRMED** — cites git history, an AI handoff file, and session memory as reader-reachable sources |
| `PRTOE_forced_combination.md:118, 120, 122, 127, 129` | "the coded expression (`:113`)" · "`scripts/de_value_derive_Lambda_g.py:9-11`" · "`de_value_g_to_lambda.py:51`" · "**Λ = 631 MeV** (`:97`)" · "`:123-124` prints 0.1244" | **CONFIRMED** — bare source-line numbers meaningless to a reader |
| `PRTOE_forced_combination.md:159` | "Docket #134 closes." | SUSPECT |
| `PRTOE_quantum_trio.md:42` | "**arXiv / paper stance (worklist red 2026-08-03, three-seat closed).**" | SUSPECT — seat/turn bookkeeping |
| four quantum files (banners) | "Banner (EN-D1 + EN-D2/D3…)", "(TU-D1…)", "(SP-D1 + SP-D4…)", "(trio TR-D1)", "worklist red", "Claude red cure" | SUSPECT — systemic docket/seat codes in reader-facing banners |
| `PRTOE_the_great_chain.md:103, 106, 164, 166, 168` | "(living section; appended as results land)" · "Updated continuously." · "(living; …)" · "*The directive: thread the sciences until…*" · "No equation, no row." | SUSPECT — maintenance directives |
| `PRTOE_PHYSICS_DOMAINS.md:95, 143–145, 1007` | "(commit 7f0dc275)" · "(pre-registered, commit 8a5840a5)" ×2 | SUSPECT — git hashes offered as reader-facing receipts |
| `PRTOE_sqrt3_derivation.md:38` | "*walk 2026-07-17 — real signs, B picked.*" | SUSPECT |

No hits anywhere in the tree for: `WHOSE_TURN`, `@FROM:`, `>>BLUE`, `>>RED`, `>>REF`, `TODO`, `note to self`, `insert here`, `red should`, `blue should`, `next seat`, `FIXME`, `XXX`. (grep, all 45 files.)

### Class 3 — stale chain adjectives

| file:line | quote | verdict |
|---|---|---|
| `PRTOE_INTERACTION_ATLAS.md:397–398` | "**THE WHISPER'S TRIAL, PRE-REGISTERED (2026-07-07, R−1 = 5.6 and falling — registered BEFORE the judge convicts):**" | **CONFIRMED** — no live chain sits at 5.6; the three active chains are at 0.048 / 0.057 / 0.705. "and falling" is present-progressive on a chain that no longer runs |
| `PRTOE_INTERACTION_ATLAS.md:408` | "The **converging** Fairbank posterior judges both at once" | **CONFIRMED** — no chain by that name; the pair it denotes was archived (`_archive_dyad_prefix_20260728_2140`, `_archive_routeD_20260728_2250`) |
| `PRTOE_fairbank_note_HOLD.md:63–68` | "## Status section re-grade vs **live chains** (2026-07-28) … Live read of the running pair: … neither converged (ΛCDM R−1 ≈ 1.0; ours no R−1)" | **CONFIRMED** — 8 days stale and 1.3 orders wrong: the ΛCDM twin is at 0.0479, ours at 0.0569 |
| `PRTOE_fairbank_note_HOLD.md:41` | "**H₀ instrument running.** Production pair restarted 2026-07-26 … Both sampling; convergence pending." | **CONFIRMED** — that pair was archived/reseeded; the live pair is `cmp_lcdm_mnu_bbnfix` + `dyad_mnu_bbnfix` (started 07-30 / 07-29) |
| `PRTOE_PHYSICS_DOMAINS.md:210` | "The Σm_ν posterior (`chains/dyad_mnu_mcmc`) is still one of the two things that can move the evidence class off zero" | **CONFIRMED** — `chains/dyad_mnu_mcmc.*` exists but is superseded; the live Σm_ν chain is `dyad_mnu_bbnfix` |
| `PRTOE_PHYSICS_DOMAINS.md:25–26` | "provisional — the **running evidence test** re-measures it" | SUSPECT — `PRTOE_fairbank_note_HOLD.md:9` records the nested-sampling evidence run as **ended 2026-07-20 without log(Z)** and deferred |
| `PRTOE_intellectual_history.md:154` | "the refit ΛCDM twin **is converging** to a statistical tie" | SUSPECT — a 2026-07-06 snapshot in present tense on a since-superseded chain |
| `PRTOE_the_great_chain.md:116` | "its chains **have yet to converge**" | SUSPECT — the bbnfix pair now sits at/below the 0.05 stopping target |
| `PRTOE_INTERACTION_ATLAS.md:842, 877` | "a standing bet that is being tested **RIGHT NOW**" · "data arriving **NOW**" | SUSPECT — undated urgency in a static file |

**Clean, and why:** `PRTOE_hierarchy_problem.md:912–922` and `PRTOE_quantum_trio.md:127` both quote **R−1 = 93.1**, but both explicitly frame it as the *historical* last statistic of the archived `cmp_prtoe_zon` and both rule the interval it produced "**worthless** as a constraint." That is correct handling, not a defect. `PRTOE_PHYSICS_DOMAINS.md:1005` ("the chain running right now tests it") is **true** — `dyad_mnu_bbnfix` is live.

### Class 4 — 0.22% / crown-null presented as executable

| file:line | quote | verdict |
|---|---|---|
| `PRTOE_PHYSICS_DOMAINS.md:488–489` | "conditional on α_c = 3α (under MCMC test) and on the one irreducible input, the portal √σ_dark = m_e; **a lattice T_c/√σ for SU(2), N_f = 3 confirms or kills it** (P-2026-048)" | **CONFIRMED** — a live CONFIRM/KILL decision rule on the 0.44% gap, which the registration forbids in exactly those words |
| `PRTOE_PHYSICS_DOMAINS.md:56` | "\| 21 \| The cosmological constant \| … new half kernel-sourced at +0.44% \| **lattice-refereed (P-2026-048)**; standing bet #3 vs DESI DR2 \|" | **CONFIRMED** — no sky-limited caveat anywhere in the row or the at-a-glance table |
| `PRTOE_forced_combination.md:96–97` | "T_c/√σ (the P-048 fork: ½ln2 = 0.34657 vs the observation-inverted 0.34506) is **one independent referee**." | **CONFIRMED** — this *is* clauses 2/3 verbatim, declared not executable |
| `PRTOE_forced_combination.md:185` | "One lattice campaign, three referees: T_c/√σ (the P-2026-048 fork), F_π/√σ (0.40–0.47), and w·√σ (the sheet)" | **CONFIRMED** |
| `PRTOE_forced_combination.md:217` (ledger row 6) | "P-048 T_c/√σ + (F,w) lattice campaign referees \| **OPEN-BLOCKED** \| … **WATCH-EXTERNAL / OPEN-MACHINE: lattice not computed**" | **CONFIRMED** — correct grade, wrong blocker: the registration says "the limit is the sky's, not the lattice's" |
| `PRTOE_INTERACTION_ATLAS.md:875` | "The **meV/m_ν relation** is a neck-out **registered prediction** (P-2026-048)." | **CONFIRMED** — P-048 registers **τ**; its own text: "the closeness of the predicted meV to the observed one is **not** what is being registered" |
| `PRTOE_hierarchy_problem.md:967` | "Theory and observation agree to **0.22%** — which is precisely the floor's recorded +0.44%, since ρ goes as d²" | **NOT the withdrawn framing.** Read in full context (§6g, lines 956–970): the table is *d* = 3 (spatial dimension) vs *d* = 2.993 inverted from the observed ρ_Λ¼ vs *d* = 2.921 from the anchor. The 0.22% is the +0.44% floor offset halved because ρ ∝ d². Coincidental collision with P-048's 0.22% σ threshold; **unrelated**. It is, however, a class-8 defect on its own terms — see below |

### Class 5 — external win without DOI

| file:line | quote | verdict |
|---|---|---|
| `PRTOE_references.md:43–45` | "[V] **Zurek** … **Lab confirmation of Darwinism: Science Advances superconducting-circuit observation.**" | **CONFIRMED** — no authors, year, volume, or DOI, carrying a [V] stamp under a rule (`:12–15`) requiring verification against source before external presentation |
| `PRTOE_INTERACTION_ATLAS.md:514` | "(Sekino–Susskind fast-scrambler conjecture, **cite-verified**)" | **CONFIRMED** — a "cite-verified" stamp with no citation attached at all |
| `PRTOE_intellectual_history.md:179–194` and `PRTOE_PHYSICS_DOMAINS.md:545–546` | "an **independent second review** … The reviewer's closing verdict: \"a smaller, harder, more honest object than the one I opened fire on.\"" | **CONFIRMED** — an endorsement quote with no reviewer identity, venue, date, or record, presented in two shipped files in language a first-time reader will take as external peer review |
| `PRTOE_references.md:60–62` | "a published critique exists (\"Questioning the Recent Observation of Quantum Hawking Radiation\"); follow-up (Nat. Phys. 2021, stationarity)" | SUSPECT — no identifiers for either |
| `PRTOE_references.md:66–68` | "stochastic-fuzziness limit also published in Nat. Phys. 2015" | SUSPECT |
| `PRTOE_INTERACTION_ATLAS.md:160–162`, `PRTOE_PHYSICS_DOMAINS.md:456–457` | "Google Willow (Nature, Dec 2024, cite-verified) — logical errors suppressed 2.14±0.02× per code-distance step" | SUSPECT — no volume/page/DOI |
| `PRTOE_PHYSICS_DOMAINS.md:28` | "the record of dead approaches **is public**" | SUSPECT — no URL or venue |

### Class 6 — false page COMPLETE / SOLVED / CLOSED

| file:line | quote | verdict |
|---|---|---|
| `PRTOE_INTERACTION_ATLAS.md:1018–1042` | "**THE EQUATION OF NOTHING — \"nothing happens until contact is made,\" tested against total, gutted vacuum, and CONFIRMED.** … VERDICT: … **confirmed as the correct description of how curvature comes to exist at all** … **Adopted as a standing law of this framework**" | **CONFIRMED** — an inspection argument promoted to CONFIRMED and to standing law, inside a file whose own binding headline (`:9–13`) records "**ZERO confirmed entries to date**" |
| `PRTOE_INTERACTION_ATLAS.md:553–558` | "**THE CENSUS IS COMPLETE**: gravity is the medium's only coupling … after exhaustive checking of every legal alternative … The identity's isolation is now a **theorem-grade** census result." | **CONFIRMED** — COMPLETE + theorem-grade for an enumeration; the file's own ledger (`:1140`) grades this family "mixed (parent-graded)" and `PRTOE_PHYSICS_DOMAINS.md:1066` grades it "**interpretation**" |
| `PRTOE_INTERACTION_ATLAS.md:777` (heading) vs `:794–805` | "## **Killed candidates** (set 3)" containing "**THE INDIRECT-DETECTION STANDING BET (kill-only, permanent …)**" and "THE DARK-ANTIMATTER REFRAME" | **CONFIRMED** — two live standing bets filed under a "Killed candidates" heading; the section grade contradicts its contents |
| `PRTOE_fairbank_note_HOLD.md:5, 73` vs `:78–80` | "## **Status: shareable as a draft**" / "**Status unchanged: shareable as a draft.**" — against the footer "**Grade:** superseded lineage / **Non-claims:** do not use as live derivation" | **CONFIRMED** — the top of the page authorises an outreach action the bottom of the page archives. A reader who stops at line 7 acts on it |
| `PRTOE_sqrt3_derivation.md:113` vs `:118–121` | "**B = 1/√2 is derived.**" against "**Grade:** superseded lineage … do not use as live derivation" | SUSPECT |
| `PRTOE_kappa_v_derivation.md:78` vs `:140–142` | "## 3a. THE THREE SEAMS — **closed**" against "the w-portal's radiative bill is … payable **if and only if** the completion delivers the form factor" | SUSPECT |

### Class 7 — orphan / broken tables

Script-checked column counts on every markdown table in all 45 files (fenced code excluded).

| file:line | quote | verdict |
|---|---|---|
| `PRTOE_the_great_chain.md:120` | `\| 10 \| \|Δμ/μ\|(z≤4) < 10⁻⁶ (quasar fence); today: gate-zeroed \| chemistry uniform to ppm since z=4 \| quasar μ-fence \|` | **CONFIRMED** — 6 cells against a 4-column header; the unescaped pipes in `\|Δμ/μ\|` split the row and it renders broken |
| `PRTOE_the_great_chain.md:172` | `\| chemistry \| Ĥ = … \| QM (reproduced exactly) \| m_e, α held constant BY THE GATE … the Oklo natural reactor: \|Δα/α\| < 10⁻⁸ over 2 Gyr …\|` | **CONFIRMED** — 6 cells against 4 |
| `PRTOE_hierarchy_problem.md:1094` | `\| Higgs-coupled, to induce m_H² under the no-bare clause \| λ\|S\|²\|H\|² for a gauge-singlet scalar S \|` | **CONFIRMED** — 6 cells against a 2-column header |

**Cleared as false positives (escaped pipes render correctly):** `PRTOE_laboratory_cousins.md:94` (`⟨\|cos\|⟩`), `PRTOE_quantum_tunneling.md:94` (`$\ln\|\psi\|$`). No header-without-separator and no headerless table found anywhere in the tree.

### Class 8 — overclaims

| file:line | quote | verdict |
|---|---|---|
| `README.md:113–115` | "Acceptance test: all **883** local markdown links under `docs/` were resolved against the filesystem relative to their containing file. **Zero unresolved.**" | **CONFIRMED FALSE** — 13 broken links survive in this directory alone, enumerated in the bonus section below. The verification claim is the strongest statement in the README and it does not hold |
| `PRTOE_kappa_v_derivation.md:69–72` | "κ_v = (k·w/2)/(ρ_d/ρ_r) = **0.06 at the ΔN_eff bound — inside ANN-2026-005's [0.06, 0.41] window**, **derived, not fitted to it**." | **CONFIRMED** — the file's own binding header (`:17–24`) reads "AMPLITUDE-INPUT (k_eff is chosen, **not derived**)" and "0.06 lands inside … **as a consistency, not a prediction**" and "\"Derived\" **may not re-inflate**". §3 does precisely what §0 forbids |
| `PRTOE_kappa_v_derivation.md:167–168` | "*Chain of custody: … **Scripts were job-scratch, not retained.**" — under the title "# The κ_v **Derivation**" | **CONFIRMED** — a titled derivation whose computation is unreproducible by its own admission |
| `PRTOE_the_great_chain.md:189–191` | "the medium's contribution is the **PROOF OF CONSTANCY** the sciences borrowed unexamined — now a registered, falsifiable, court-dated prediction. **Oklo … is a passed fence, and every radiometric date in every geology paper inherits it.**" | **CONFIRMED** — "PROOF" plus a sweeping external-reach claim, in a file graded "story/map — exploratory-ok" |
| `PRTOE_the_great_chain.md:77, 96, 122` | "the birefringence zero, **proven**" · "(L1a, **proven**)" · "birefringence ≡ 0, **proven**" | **CONFIRMED** — "proven" three times in a story/map file whose non-claims line says "not a derivation" |
| `PRTOE_the_great_chain.md:93` | "**Every arrow above is a citation, not a metaphor**" | **CONFIRMED** — contradicted by its own table: row 0 cites "model construction", row 3 "model derivation", row 9's number cell is "—" |
| `PRTOE_INTERACTION_ATLAS.md:927–928` | "*Method note: **entries are added only when a relation is DERIVED**. The atlas is falsified entry-by-entry…*" | **CONFIRMED** — contradicted by the file's own coherence-, correspondence-, interpretation-, analogy- and whisper-graded entries throughout |
| `PRTOE_INTERACTION_ATLAS.md:1056` vs `:1069–1073` | "THE PAYOFF — this **DERIVES** the coupling channel structure from one rule instead of asserting it" against "GRADE: architectural/foundational principle … does **NOT** produce a new number" | **CONFIRMED** — internal contradiction inside one entry |
| `PRTOE_PHYSICS_DOMAINS.md:367` vs `:875` | "At the standing hierarchy it is **5.4/rad** at r_t = 0.9" against "this program's own θ-channel veto (**~350/rad** at r_t = 0.9, step-converged in the h-scan)" | **CONFIRMED** — the same quantity (df_amp/dθ₀) at the same tilt, quoted **65× apart** in one file. One of them is wrong and neither is flagged |
| `PRTOE_hierarchy_problem.md:967` | "Theory and observation agree to **0.22%**" | **CONFIRMED** (class 8, not class 4) — the observational side carries **±0.449%** on ρ_Λ by P-2026-048's own accounting, so the quoted "agreement" sits inside its own measurement error and cannot be claimed at that precision. Stated bare and bolded |
| `PRTOE_hierarchy_problem.md:102–105` | "the corpus's **one shared k** … gap-equation 1.360, closed form 1.36461, A_s-measured 1.3602 … **one object, three determinations**" | **CONFIRMED** — the file's own ledger residual (`:1253`) says "Gap eq + closed form = **one integral**", and 1.3602 is read *back* from measured A_s. §2 sells three independent determinations; the ledger discloses at most one calculation and one data inversion |
| `PRTOE_references.md:4–5, 12–15` | "**THIS file is the verification record — which receipts were checked against their sources**" / "every load-bearing receipt is **verified against its source**" — but the method is "(identifiers **checked via search**)" | SUSPECT — the [V] stamp claims more than the stated method delivers |
| `PRTOE_PHYSICS_DOMAINS.md:22–24, 283`; `PRTOE_INTERACTION_ATLAS.md:558` | "a **theorem-grade** counting argument, not an assumption" · "Gravity-only is now a **theorem-grade** census result" | SUSPECT — the file's own ledger PD3 (`:1066`) grades it "**interpretation** (cross-link)" |
| `PRTOE_PHYSICS_DOMAINS.md:189` | "a falsified-then-confirmed midpoint prediction: 2812.1 predicted, **2812.15 measured**" | SUSPECT — "measured" for a CLASS χ² evaluation |
| `PRTOE_forced_combination.md:168` | "**c_K = Q/τ = 1.924 becomes a prediction** the correlator locus must independently accommodate — **it does** (the band [1.76, 1.97] contains it…)" | SUSPECT — a band containing a value is consistency, quoted as a satisfied prediction |
| `PRTOE_INTERACTION_ATLAS.md:227–228` vs `:232–233` | headline "**MATH DERIVED AND VERIFIED**" against body "quantization of the substrate's phase sector is **asserted, not derived**" | SUSPECT |
| `PRTOE_PHYSICS_DOMAINS.md:402` | "P(f_amp>0.2) rose with h — 84 → 82 → 84 → 94 → **100%**" | SUSPECT — a 100% probability from a 50-angle scan |

### Class 9 — missing exploratory framing

Checked all 45 files programmatically for top-of-file framing and for a "Discipline triage" footer, then read the borderline cases.

| file | quote / structure | verdict |
|---|---|---|
| `PRTOE_fairbank_note_HOLD.md` | Opens "# Fairbank note — internal status / ## **Status: shareable as a draft** / Addressee: **William Fairbank**. Letter may be shown as draft." Only framing is the footer at `:77–80` ("superseded lineage / do not use as live derivation") | **CONFIRMED — worst case in the tree.** A first-time reader is told at line 5 that a named-addressee outreach letter is shareable, 72 lines before being told the file is archived. Also flagged for owner call: this file ships a real person's name and an outreach plan under `docs/` |
| `PRTOE_the_great_chain.md` | Opens "*The great chain is this model's **end-to-end derivation sequence**…*" (`:6`) with no top fence; triage at `:195–199` | **CONFIRMED** — headline reads as a settled derivation chain |
| `PRTOE_PHYSICS_DOMAINS.md` | Opens "PRTOE's mature form is a two-part claim … buys **H₀ = 69.9** … at zero χ² cost" (`:17–27`) with no exploratory banner; triage at `:1060`, 1043 lines below | **CONFIRMED** |
| `PRTOE_THE_CHAIN.md` | Opens "# THE CHAIN — the Linear Unification" + "*The law:*" with no top fence; triage at `:227–233` | **CONFIRMED** |
| `PRTOE_family_tree.md` | "# The PRTOE Family Tree — **Everything That Spawns From the Model**"; triage at `:82` | SUSPECT |
| `PRTOE_references.md` | "# PRTOE **Verified** References"; triage at `:145` | SUSPECT |

**Cleared on class 9 (strong in-body framing that my keyword scan initially missed):** `PRTOE_quantum_entanglement.md`, `PRTOE_quantum_superposition.md`, `PRTOE_quantum_tunneling.md` — all three carry "INTERPRETATION LAYER", a dated Banner block, and a "VERDICT (2026-08-03) — arXiv ready as quantum-mechanics papers: **NO** / Does this model provide quantum mechanics? **NO**" within the first 28 lines. `PRTOE_INTERACTION_ATLAS.md` — no banner keyword, but `:5–23` carry a binding headline-honesty block stating the bet is UNSETTLED with ZERO confirmed entries. `README.md` — an exemplary "Authority fence (read first)". All other 39 files carry either a top banner or a footer triage.

### BONUS — broken reader-reachable links (13, verified against the filesystem)

These directly falsify `README.md:114–115`.

| pattern | resolves to | sites |
|---|---|---|
| `](BIBLIOGRAPHY.md)` | `docs/exploratory/BIBLIOGRAPHY.md` — **does not exist** (canonical is `../BIBLIOGRAPHY.md`, which `PRTOE_THE_CHAIN.md:223` and `PRTOE_sqrt3_derivation.md:107` use correctly) | `PRTOE_hierarchy_problem.md:193`, `PRTOE_white_holes.md:191`, `PRTOE_forced_combination.md:199`, `PRTOE_entropy.md:179`, `PRTOE_no_singularities.md:133` |
| `](exploratory/…)` | `docs/exploratory/exploratory/…` — **does not exist** (the `exploratory/` prefix was applied to files already inside `exploratory/`) | `PRTOE_hierarchy_problem.md:299`, `:866` (→ `PRTOE_light.md`); `PRTOE_white_holes.md:197` (→ `PRTOE_wormholes.md`); `PRTOE_no_singularities.md:13` (→ `PRTOE_quantum_trio.md`), `:19` (→ `PRTOE_wormholes.md`) |
| `](../scripts/…)` | `docs/scripts/` — **does not exist**; correct depth is `../../scripts/`, as `PRTOE_INTERACTION_ATLAS.md:676` uses | `PRTOE_hierarchy_problem.md:729`, `:783`; `PRTOE_white_holes.md:175` |

Note the shape: the `exploratory/` and `../scripts/` breakages are exactly the two rewrite rules `README.md:108–110` describes ("**62** references … now carry an `exploratory/` prefix", "**3** links to `scripts/` needed `../../` rather than `../`") — the repair over-applied the prefix and under-applied the depth fix, and the acceptance test did not catch it.

Minor, same file family: `PRTOE_kappa_v_derivation.md:13–14` reads "see the **deuterium deuterium** row's §7" (duplicated word).

---

## PER-FILE COVERAGE LEDGER

**Read in full, line by line (16 files, ~5,200 lines):**

| file | lines |
|---|---|
| `PRTOE_hierarchy_problem.md` | 1273 |
| `PRTOE_INTERACTION_ATLAS.md` | 1149 |
| `PRTOE_PHYSICS_DOMAINS.md` | 1071 |
| `PRTOE_THE_CHAIN.md` | 233 |
| `PRTOE_forced_combination.md` | 221 |
| `PRTOE_intellectual_history.md` | 202 |
| `PRTOE_the_great_chain.md` | 199 |
| `README.md` | 192 |
| `PRTOE_kappa_v_derivation.md` | 175 |
| `PRTOE_references.md` | 151 |
| `PRTOE_v4_dCDF_results.md` | 143 |
| `PRTOE_quantum_entanglement.md` | 129 |
| `PRTOE_sqrt3_derivation.md` | 121 |
| `PRTOE_family_tree.md` | 86 |
| `PRTOE_fairbank_note_HOLD.md` | 80 |
| `PRTOE_quantum_gravity.md` | 17 |

**Read in substantial part (headers, fences, ledgers, and the sections the sweeps flagged) — NOT line by line (4 files):**
`PRTOE_UV_completion.md` (lines 1–60 read; fence + §-target confirmed), `PRTOE_quantum_superposition.md` (1–40 + ledger rows 106–145 via targeted grep), `PRTOE_quantum_tunneling.md` (1–40 + rows 83–117 via targeted grep), `PRTOE_quantum_trio.md` (banner 13–44 + line 127 via targeted grep).

**Covered by structural sweeps only — NOT read line by line (25 files).** Each of these was run through: (a) a table column-count script over every table, (b) a top-of-file framing + footer-triage script, (c) six full-text greps covering classes 1, 2, 3, 4, 5/6, and link integrity. Findings above from these files come from those sweeps and are quoted verbatim from grep output, but **I did not read their prose end to end and cannot certify them clean**:

`PRTOE_v5_five_verdict_derivation.md` (471) · `PRTOE_v4_dCDF_derivation.md` (451) · `PRTOE_white_holes.md` (319) · `PRTOE_me_trigger.md` (285) · `PRTOE_light.md` (265) · `PRTOE_arrow_of_time.md` (214) · `PRTOE_entropy.md` (197) · `PRTOE_inertia.md` (161) · `PRTOE_no_singularities.md` (155) · `PRTOE_laboratory_cousins.md` (154) · `PRTOE_math_story.md` (132) · `PRTOE_science_subdomain_tree.md` (123) · `PRTOE_scale_ladder.md` (123) · `PRTOE_information_paradox.md` (111) · `PRTOE_laser_physics.md` (109) · `PRTOE_wormholes.md` (88) · `PRTOE_interaction_map.md` (87) · `PRTOE_special_relativity.md` (79) · `PRTOE_philosophy_the_auditor.md` (77) · `PRTOE_classical_gravity.md` (77) · `PRTOE_thread_inheritance.md` (70) · `PRTOE_sciences_inheritance.md` (63) · `PRTOE_plasma_physics.md` (36) · `PRTOE_astrochemistry.md` (36) · `PRTOE_chaos_dynamics.md` (34)

**Not opened at all:** none. All 45 were touched by at least the automated sweeps.

---

## CLEAN CLAIMS (with the basis for each)

1. **No agent/seat markup of the `WHOSE_TURN` / `@FROM:` / `>>BLUE` / `>>RED` / `>>REF` / `TODO` / `FIXME` family exists anywhere in the tree.** Basis: case-insensitive grep for all 14 listed markers plus `note to self`, `insert here`, `red should`, `blue should`, `next seat` across all 45 files — two hits total, both benign (`PRTOE_arrow_of_time.md:17` "not a stale placeholder", `PRTOE_UV_completion.md:212` "not a placeholder"). The class-2 findings above are a *different* shape of defect (runbooks, do-not-book rules, source-line refs), not this markup.

2. **No headerless tables and no header-without-separator anywhere in the tree.** Basis: a script that walked every line of all 45 files, tracked fenced-code state, and compared each table row's cell count to its header's. Only three genuine mismatches, all listed above; the two escaped-pipe rows were checked by eye and render correctly.

3. **The prior round's cure at `PRTOE_hierarchy_problem.md:636` holds.** Basis: read in context (lines 633–648). The line now reads "The density of states is already supplied here, N₀ = k_F²/π²v, and **k_F is not an input the construction contains**" — physics, with no narration of the document's own prior text.

4. **`PRTOE_quantum_gravity.md` (17 lines) is clean on all nine classes.** Basis: read in full. Its "no longer the home of the full QG hub" (`:8`) is the navigational content of a MOVED stub, not repair-log residue, and it carries an explicit exploratory fence, a Page-curve OPEN flag, and two "do not cite / do not claim" lines.

5. **The R−1 = 93.1 quotations in `PRTOE_hierarchy_problem.md:912–922` and `PRTOE_quantum_trio.md:127` are correct handling, not stale-chain defects.** Basis: read in full context. Both explicitly date the statistic to 2026-07-11 on the archived `cmp_prtoe_zon`, both name the 0.05 stopping target it missed, and `hierarchy_problem` goes further — "**As a constraint it is worthless**, and it must not be used as one." That is the model of how a dead chain should be quoted.

6. **`PRTOE_hierarchy_problem.md`'s claims ledger and residual freeze (`:1250–1273`) contain no false COMPLETE.** Basis: read row by row against the body. Grades used are derived-conditional, derived, complete-conditional, OPEN-BLOCKED, registered bet, OPEN — all legitimate, each with a named residual and a "Forbidden" column. Row 3 explicitly forbids "1576≈1574 as discovery."

7. **`PRTOE_INTERACTION_ATLAS.md`'s headline honesty block (`:5–23`) is accurate and binding.** Basis: read in full. "The evidence class … holds **ZERO confirmed entries to date**" and the Pinning Rule ("3 for 3") are stated up front and are consistent with the ledger at `:1137–1148`. The atlas's defects listed above are body entries that violate this header, not a header that oversells.

8. **`PRTOE_PHYSICS_DOMAINS.md`'s Part II census arithmetic checks.** Basis: hand-summed both tallies. Type tally (`:965–972`) = 14+8+4+6+12+2+2+4 = 52, matching "52 domains (25–76)". Standing tally (`:1045–1055`) = 0+1+15+12+12+2+10 = 52. Both self-consistent.

9. **`README.md`'s file count is right.** Basis: `ls` — 45 `.md` files, of which 44 are `PRTOE_*.md`, matching "Forty-four files (after 2026-08-03 fence pass)" at `:119`.

---

## WHAT I WOULD ESCALATE FIRST

1. `README.md:114–115` — "**Zero unresolved**" is false; 13 broken links, and the failure mode is traceable to the very rewrite the same section describes.
2. `PRTOE_fairbank_note_HOLD.md` — a named-person outreach letter whose top line says "shareable as a draft" and whose footer says "superseded lineage / do not use as live derivation", carrying a "## Before send" to-do list, an owner-approval instruction, an 8-day-stale "live chains" read, and four sections of literal edit history. Owner call needed on whether this file should ship under `docs/` at all.
3. `PRTOE_PHYSICS_DOMAINS.md:488–489` + `:56` and `PRTOE_forced_combination.md:96–97, 185, 217` — five sites presenting the P-2026-048 crown/null lattice fork as a live CONFIRM/KILL referee, against the registration's own "not executable … the limit is the sky's, not the lattice's."
4. `PRTOE_PHYSICS_DOMAINS.md:367` vs `:875` — 5.4/rad vs ~350/rad for df_amp/dθ₀ at the same r_t = 0.9, in one file, unflagged.
5. `PRTOE_kappa_v_derivation.md:69–72` — the body re-inflates "derived" in the exact phrase its own binding header forbids, on a derivation whose scripts were not retained.
