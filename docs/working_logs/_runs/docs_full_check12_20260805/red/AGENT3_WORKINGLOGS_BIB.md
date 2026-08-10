# AGENT 3 — RED check-12: `docs/working_logs/*.md` (top level) + `docs/BIBLIOGRAPHY.md`

**Auditor:** red team, adversarial. **Filed:** 2026-08-05.
**Slice:** all 95 top-level `docs/working_logs/*.md` (the `_runs/` subtree is EXCLUDED — another agent owns it) plus `docs/BIBLIOGRAPHY.md` in full.
**Bar:** working_logs = workshop — house shorthand, seat addressing and edit history are ALLOWED. Flagged only what is factually false as of now, contradicts a forward-facing doc, or would be wrong if a reader followed it. `docs/BIBLIOGRAPHY.md` is forward-facing and held to the full bar.
**Rule:** NO FABRICATIONS. Every finding carries `file:line`, a verbatim quote, and a verdict. Where I could not verify, I say so.

---

## 1. FINDINGS TABLE

### Class 3 — stale chain adjectives / stale R−1 (a defect everywhere, because it is factually false)

Ground truth for every row below is §4.

| file:line | quote | why it is a defect | verdict |
|---|---|---|---|
| `_master_computes.md:15` | "The dispersion chain has since been relaunched (**zon_disp live**, R−1 ≈ 23 as of 2026-07-19, drifting through the pair zone unconverged) — the posterior referees 3α when it converges" | `cmp_prtoe_zon_disp` last wrote 2026-07-22T09:37 (R−1 = 17.81287 @ N=3456), has no live process, and `_GATED_SHELF.md:31` records it "Dead at R−1 = 23.3. **Not relaunched deliberately**". "live" + "when it converges" is false and contradicts the shelf. | **CONFIRMED** |
| `_master_computes.md:19` | "**LIVE 2026-07-17: three chains running ~35 h** (`zon_disp`, `routeD`, `fixed_trgb`) — not paused." | Of those three only `cmp_prtoe_routeD` is alive. `zon_disp` dead since 07-22; `cmp_prtoe_fixed_trgb` has **no `.progress` file at all** and no process. | **CONFIRMED** |
| `_master_computes.md:51` | "Test = the thaw posterior (routeD/conv_desi, symmetric-BBN, gated behind the **live pc_prtoe run** for cores)." | PolyChord was ended 2026-07-20 and archived (`chains/_archive_polychord_ended_20260720_0915/`); `PRTOE_honest_status.md:57–60` stamps "**PolyChord off.** Nested sampling not running and not scheduled". | **CONFIRMED** |
| `_FILE_COMPLETION_STATUS.md:67` | "Freeze 2026-08-04: conv_desi unproduced (R−1=13.25, dead); **routeD live but R−1≈103**" | routeD IS live but its R−1 is **0.705291** @ N=6517, t=2026-08-05T04:07:15 (3 ranks, stop 0.1). "≈103" is 146× wrong, and it is verbatim the framing `FINAL_PRODUCT_STYLE_GUIDE.md:23` bans ("routeD stuck at 103"). | **CONFIRMED** |
| `_FILE_COMPLETION_STATUS.md:47` | "Residual freeze 2026-08-04: dyad R−1~0.189 / lcdm~0.059 / **routeD~103**; not self-stopped" | Same frozen plateau, on the `PRTOE_CHAIN_TABLES.md` inventory row. | **CONFIRMED** |
| `_PROJECT_FINISH_ROADMAP.md:27` | "\| `cmp_prtoe_routeD` \| **129.1** \| 0.1 \| **~5.15%** \| N=1593 (first progress only); ranks partially disjoint — see surgery below. **Do not kill.** \|" | routeD now has four progress rows and R−1 = 0.705291. The row is the input to an archive-and-reseed surgery plan. | **CONFIRMED** |
| `_PROJECT_FINISH_ROADMAP.md:163–165` | "2. RouteD: leave alone (**R−1 ~129, one progress row**; mpirun alive) — **surgery plan above** if second progress still has R−1 ≫ 10 and ranks disjoint / raw accept still ~5%" | **Highest operational risk in my slice.** The file's own skip-criterion (`:55–56`, "If a later row shows R−1 falling toward O(10) with rank means overlapping, skip surgery") is now *met* — the trajectory is 102.79 → 4.94 → 1.08 → 0.705 — but the headline still reads 129, so a reader following this file could fire an archive-and-reseed on a converging chain. Violates the standing "let chains finish" rule. | **CONFIRMED** |
| `T3_neutrino_home_owed.md:16–17` | "In flight: item 1 (dyad_mnu chain **running**, R−1 ≈ 0.18 marginal today) and item 2 (**conv_desi running**)." | `cmp_prtoe_conv_desi` last wrote 2026-07-22T11:06 and is stamped "**not running**" on the shelf (`PRTOE_honest_status.md:168`) and "unproduced (R−1=13.25, dead)" (`_FILE_COMPLETION_STATUS.md:67`). `dyad_mnu_mcmc` is archive-only (`_chain_snapshot.md:150`). Also class 9. | **CONFIRMED** |
| `T4_s8_growth_owed.md:3–4` | "> **SUPERSEDED 2026-07-18: the chain is running again** (relaunched, past the initialisation point that killed it, burn-in in progress)." | Presented as the *superseding current status* of item 1's referee. conv_desi is not running. `_AUDIT_PROTOCOL.md:1051` already logs this exact string as a past defect ("`T4_s8_growth_owed.md` (earlier find) — 'the chain is running again' — died a second time") and it has re-staled. Also class 9. | **CONFIRMED** |
| `_GATED_SHELF.md:30` | "**#3 / #54 — routeD + conv_desi** \| the chains converging \| Both relaunched 2026-07-20 on a corrected sampler … **First R−1 rows are the test**" | Sits under "## 2. Gated on in-house runs", i.e. asserts conv_desi is an in-flight run awaiting its first R−1 rows. conv_desi produced nine rows and died; it is not running. | **CONFIRMED** |
| `_RESIDUAL_DEBT_CENSUS.md:79` | "the Σm_ν joint fit (dyad_mnu, R−1 = 0.176 — closest to converging); the double-duty check (**conv_desi, burning in**)" | conv_desi is not burning in; the header claims "2026-08-02 table hygiene — Cells below are brought into line", so this cell was declared cured and was not. | **CONFIRMED** |
| `_RESIDUAL_DEBT_CENSUS.md:80` | "conv_g posterior — **the chain is alive again since 2026-07-18**, superseding this file's dead-chain flag" | Same chain, same falsehood, in the MACHINE column of the T4 row. | **CONFIRMED** |
| `census_democracy_note.md:22` | "The **running** α_c/ε chains are the instrument." | The α_c instrument is `cmp_prtoe_zon_disp` (parked/dead) — see `_GATED_SHELF.md:31`, `_FILE_COMPLETION_STATUS.md:75`. No α_c chain is running. | **CONFIRMED** |
| `T13_fingerprint_owed.md:3` | "2. The masters' calendar: the α_c MCMC (**running**), DESI DR3, PolyChord, the radio referee, BipoSH" | Neither the α_c MCMC nor PolyChord is running. Item is marked PAID at `:30`, so it is legacy list text — low blast radius but still false. | **CONFIRMED (low)** |
| `T2_smbh_atoms_owed.md:48` | "**The referee: NewAthena's projected homogeneous catalog** (~50 nearby AGN at ≤10% spin precision) — **the α_c chain sharpens the band meanwhile.**" | "meanwhile" asserts an α_c chain is currently sharpening the band. None is running. | **CONFIRMED (low)** |
| `SCIENCE_DEBTS_2026-08-03.md:8,13` | "## Machine (**live 2026-08-04 ~02:36 local**) … \| **bbnfix pair** \| **NOT bookable** — progress R−1 lcdm **0.059** / dyad **0.189**" | Quoted with **no N and no timestamp**, contrary to `FINAL_PRODUCT_STYLE_GUIDE.md:8`. Current: lcdm 0.047912@N=24858, dyad 0.056889@N=24677 — dyad is 3.3× off. The verdict ("NOT bookable") remains true; the numbers do not. | **CONFIRMED** |
| `SCIENCE_DEBTS_2026-08-03.md:86` | "**NOT YET** (lcdm 0.059 bounce; dyad 0.189; need R−1&lt;0.05 **and** self-stop)" | Same, no N. | **CONFIRMED** |
| `SCIENCE_DEBTS_2026-08-03.md:129` | "dyad still ~**0.16**" | No N; dyad is 0.056889. Also inconsistent with `:13`'s 0.189 in the same file. | **CONFIRMED** |
| `SCIENCE_DEBTS_2026-08-03.md:15` | "GetDist diag (UNBOOKABLE) \| max GR ~**0.071** (lcdm) / ~**0.086** (dyad) — both >0.05" | Diagnostic snapshot with no N/date on the row; superseded by `PRTOE_honest_status.md:39` (~0.07 / ~0.086 as of 2026-08-05). Marked as diagnostic-only, so low. | **SUSPECT (low)** |
| `_FILE_COMPLETION_STATUS.md:136, 254–255` | "live bbnfix **not bookable** (lcdm~0.059 / dyad~0.189; residual freeze 2026-08-04)" · "**Authority quote (bbnfix, not bookable):** lcdm R−1 **~0.059** (0.059055) / dyad **~0.189** (0.189201)" | Declares itself the *authority quote*. `PRTOE_honest_status.md:83–87` explicitly supersedes: "Any surface still carrying **2026-08-04** live R−1 numbers as if current … is **stale**". | **CONFIRMED** |
| `_POSTERIOR_BOOKING_CHECKLIST.md:11–12` | "Last gate smoke (2026-08-04): dyad R−1 = **0.189**, lcdm R−1 = **0.059**, both `converged: false` → `book_bbnfix_when_ready.py` **REFUSED** (exit 2)." | Dated, and the REFUSED verdict still holds; the numbers are two days stale. | **CONFIRMED (low)** |
| `CHATGPT_REFEREE_4_10_RESPONSE.md:36` | "\| **MCMCs (lcdm near stop)** \| Standard posterior product when R−1 hits \|" | A frozen direction adjective on a noisy R−1 trajectory — exactly what `FINAL_PRODUCT_STYLE_GUIDE.md:9` forbids. No N, no timestamp. | **CONFIRMED (low)** |
| `_OWNER_QUEUE.md:239` | "`scripts/ring_toroidal_3d.py` **is running** (task #42, ~15.4 h, one core at nice 19, first execution that has survived past its opening frames). **It is producing readings**" | Dated 2026-07-28 section; no evidence the sim is running now, and the only live processes are the three MPI chains. A sim, not a chain, so lower weight. | **SUSPECT** |
| `_DOCKET_INDEX.md:53, 102` | "\| 3 \| routeD + conv_desi chains … \| **running** \|" · "\| 54 \| f̄ and α_c — **the two running MCMC referees** \| running \|" | The file defines `running` at `:11` as "waiting on a chain, a sampler or an external referee", which partly excuses row 3; but row 54's prose "the two running MCMC referees" is a direct claim and the α_c referee is dead. | **SUSPECT** |
| `_DOCKET_INDEX.md:63` | "\| 13 \| The DISPERSION zon chain … \| open — **dead, not relaunched** (**R−1 = 23.3**…) \|" | The chain's own last progress row is **17.81287** (2026-07-22T09:37, N=3456); `_FILE_COMPLETION_STATUS.md:75,76,85` quote 17.81. Two working-logs surfaces disagree on the same chain's terminal R−1. | **SUSPECT** |

### Class 7 — orphan / malformed tables

| file:line | quote (head) | defect | verdict |
|---|---|---|---|
| `STORY_GRADE_ELEVATION_RULE.md:55–66` | "\| **registered** \| Umbrella for registered null / bet / kill / candidate on predictions surface …" | Twelve grade rows detached from the grade table (which ends at `:53`) by the blank line at `:54`. **No header row, no `\|---\|` separator** — they render as a headerless table or as raw text. Half the closed grade set lives in this block, and `:68` calls the table "**Closed grade set:** only the labels in this table". | **CONFIRMED** |
| `_FILE_COMPLETION_STATUS.md:105–106` | "\| [`PRTOE_induced_gravity.md`](../PRTOE_induced_gravity.md) \| COMPLETE-CONDITIONAL \| Goal A′ thin shelf …" | Two inventory rows sitting *below* the `---` rule at `:103`, with no header and no separator. Both are counted in the "Total 69" at `:120` and in the Gap-fill note at `:244–245`, so the count depends on rows that are outside the table. | **CONFIRMED** |
| `_ARXIV_READINESS.md:241–243` | "…σ_ε = σ/√11 all-bands, σ/√8 best pair) — *superseded 2026-07-29: the\ndispersion row was demoted…*" | The radio-lattice Tier-A row carries **raw newlines mid-cell** at `:242–243`, terminating the table. Everything from `:244` renders detached. | **CONFIRMED** |
| `_ARXIV_READINESS.md:276–277` | "\| † `PRTOE_neutrino_sector.md` **§3 only** \| with m₁ = ρ_Λ¼ = 2.25 meV …" | Two Tier-A rows separated from their header (`:259–260`) by thirteen lines of prose (`:263–275`). No header, no separator. | **CONFIRMED** |
| `_AUDIT_LEDGER.md:75–77` | "\| **README** \| **3** \| **ODDS (\"~16%\") on the repo's front door** …" | Three defect rows following a bullet list (`:67–74`), with no header and no separator; they belong to the table that ended at `:65`. | **CONFIRMED** |
| `the_transfer_integral_spec.md:79–88` | "\| **fork #1: which portal is the junction** \| **DECIDED (stage 2)** — the **tenth-channel seat\n  term**…" | Three rows with mid-cell newlines (`:80–81`, `:83–86`, `:88`), breaking the fork/status table. The rows that carry "DECIDED (stage 2)" and "COMPUTED (stage 5)" are the ones that break. | **CONFIRMED** |
| `_DOCKET_INDEX.md:163` | "… f₀² = \|f₁\|²+\|f₂\|² at N = 3, uniquely, via (N−1)² = N+1 …" (row #115) | Unescaped `\|` characters inside a table cell split the row into extra columns under a strict renderer. Elsewhere in the corpus (`_REDTEAM_BRIEF.md:13`, `T6_koide_desk_status.md:12`) the same notation *is* escaped, so this is an inconsistency, not a convention. | **SUSPECT (renderer-dependent)** |

### Class 8 — factually wrong against the artifact / self-contradiction

| file:line | quote | verdict |
|---|---|---|
| `_ARXIV_READINESS.md:21` | "\| PDF pages (from build log) \| **6** (309217 bytes ≈ 302 KB) \| **3** (254556 bytes ≈ 249 KB) \| **3** (229842 bytes ≈ 225 KB) \|" | **CONFIRMED FALSE.** Verified against the artifact: `papers/radio-lattice/main.log` reads "Output written on main.pdf (**7 pages, 303368 bytes**)", and `papers/radio-lattice/main.pdf` is **303368 bytes** on disk, mtime 2026-08-02 23:10 (unchanged since). The neutrino byte count (254556 claimed vs 253095 actual) is also wrong. |
| `_ARXIV_READINESS.md:28–29` | "Page counts in the historical log that say **7 pp (radio)** or 4 pp (neutrino) are **pre-note-strip** states; current PDFs are **6** and 3 after provenance was moved out of typeset `note` fields." | **CONFIRMED FALSE — worst of the three.** This sentence actively instructs the reader to disbelieve the correct number. It sits inside the section headed "**Authoritative snapshot** … when history and this section disagree, **this section wins**" (`:10–11`), so the wrong figure has declared priority. Contradicted by the machine-generated `_PACKAGE_AUDIT.md:22` (2026-08-04, `pdfinfo` → **7**), `_ARXIV_CANDIDACY.md:62` and `:121` (**7 pp**), and `_PROJECT_FINISH_ROADMAP.md:120` ("**READY** 7 pp"). |
| `_ARXIV_READINESS.md:53` | "**Yes.** `submission/main.tex` + `main.bbl`. **6 pp**. Notes stripped. Clean-room 0/0/0. 31/31 cites." | **CONFIRMED FALSE** — same object, 7 pp. |
| `T8_coincidence_owed.md:68–69` | "**The answer to \"how sharp is why-now quantitatively\": the width is sharp to 0.07%** and the occupancy odds to under one unit in thirty" | **CONFIRMED — arithmetic does not close.** The same file at `:46` gives "**t_turn: 8.1597–8.1611 H⁻¹, a 0.02% bracket**". (8.1611 − 8.1597)/8.16 = 1.7×10⁻⁴ = **0.017% ≈ 0.02%**. Nothing in the section yields 0.07%; the headline overstates the bracket by 3.5×. |
| `_ARXIV_CANDIDACY.md:150–154` | "### B2. PAPER_CANDIDATE — new short papers still worth drafting … Only **one** corpus object still clears the bar for a *new* paper" | **SUSPECT (internal inconsistency).** The section's only entry (`:156`, kination) is itself marked "**READY_PACKAGE** *(promoted from PAPER_CANDIDATE)*", and the file's header (`:18`), `:330` and `:360` all state PAPER_CANDIDATE = **0**. The section heading and "only one" sentence were not restated after the promotion. |

### Class 9 — contradiction with the current forward-facing shelf

| file:line | quote | what the shelf says | verdict |
|---|---|---|---|
| `census_democracy_note.md:30–31` | "**Grade:** the count moves from \"assumption the data confirms\" to \"**licensed by the blindness principle** with a named sector condition.\" Not derived; the license inherits the principle's own argument grade." | This is precisely the step the corpus **withdrew**. `PRTOE_honest_status.md:132–145`: "the step that would have derived it is **withdrawn** … What was meant to *license* a democratic count was routing the budget split through gravity's blindness, and **that step does not exist** … **No single criterion returns 9/10.**" `_DOCKET_INDEX.md:174` (#126): "closed — **the step is withdrawn, not supplied**." `_REDTEAM_BRIEF.md:12`: "**do not defend it as *derived***." The note (2026-08-... dated 2026-07-27) carries **no withdrawal banner** and its whole body is the withdrawn licensing argument. | **CONFIRMED — highest-value class-9 finding in my slice** |
| `census_democracy_note.md:5–18` | "The licensing argument, at argument grade with its condition named: … a share taken in the MEDIUM sector is identity-blind and **forces the democratic count (9/10)**" | "forces" is the exact overclaim the withdrawal denies. Also class 8. | **CONFIRMED** |
| `_GATED_SHELF.md:19` | "Note the decision rule **cannot currently be executed**: the prediction sits +0.44% from the observation-inverted value against a registered tolerance of ±5.7%, thirteen times wider" | `PRTOE_PREREGISTERED_PREDICTIONS.md:1486–1489`: "**What remains fully executable is clause 4** … the falsification clause is **live** and the claim is genuinely at risk"; `:1509–1511` gives clause 4 as τ̂ outside **[0.330, 0.370]** at ≥3σ. A blanket "the decision rule cannot currently be executed" contradicts the live clause. (Direction is *under*-claim, not over-claim, so it is not a class-4 defect — but it is a shelf contradiction and would mislead a reader into thinking P-2026-048 is entirely un-runnable.) | **CONFIRMED** |
| `_master_computes.md:15,19,51` · `T3:16` · `T4:3` · `_GATED_SHELF:30` · `_RESIDUAL_DEBT_CENSUS:79,80` | (chain-state quotes above) | All contradict `PRTOE_honest_status.md:168` ("conv_desi and zon_disp are **not running**") and `:57–60` ("PolyChord off"). | **CONFIRMED** (already counted under class 3) |

### Class 4 — the withdrawn 0.22% crown/null framing

| file:line | quote | verdict |
|---|---|---|
| `docs/BIBLIOGRAPHY.md:257` | "**P-2026-048:** crown/null discrimination is **sky-limited** at present ρ_Λ precision (**0.22% lattice framing withdrawn**); the live falsifier is **clause 4** (window kill / neighbour inference)." | **CLEAN — not a defect.** Read in full context: the entry states the withdrawal explicitly, names clause 4 as the live falsifier, and carries the SU(3)-vs-SU(2) standing caveat. This is the correct presentation. |
| `_AUDIT_LEDGER.md:6678–6681` | "**The lattice-precision convention aligned to the registered rule.** The registered decision rule (σ ≤ 0.0008, i.e. **0.22% on T_c/√σ**, with the rival excluded at ≥2σ) was quoted as \"0.44% precision\" in READERS_RISK item (j) and the referee calendar's lattice row … **Both aligned to 0.22% with the rule stated.**" | **CONFIRMED (mitigated).** A dated 2026-08-02 ledger entry, so history is allowed — but it is the *propagation instruction* that put 0.22% onto two forward-facing surfaces, and it carries no withdrawal note. Clauses 2/3 are now stamped "**Historical (sky-limited; not currently executable)**" (`PRTOE_PREREGISTERED_PREDICTIONS.md:1500–1508`). A future currency sweep re-syncing from this entry would restore the withdrawn framing. |
| `_AUDIT_LEDGER.md:1527–1528`, `:6300` | "the \"σ ≲ 0.22% to discriminate / > 0.44% scores neither\" thresholds are exactly the registry's own decision rule (σ ≤ 0.0008 / > 0.0015) restated in percent" · "½ln2 = 0.34657; 0.44% above 0.34506; **discrimination needs σ ≲ 0.22%** \| **arithmetic confirmed**" | **SUSPECT (history).** Both are dated audit entries verifying arithmetic; neither claims executability. Flagged only so the withdrawal sweep sees them. |
| `T6_koide_owed.md:1174` | "P-2026-048's registered window **[0.330, 0.370]**, 1.1% below the registered 0.3503." | **CLEAN** — quotes clause 4's window, which is the surviving executable clause. |

### Class 5 — EXTERNAL WIN without DOI

| item | finding | verdict |
|---|---|---|
| Corpus-wide sweep for outright external-win assertions | Grepped all 95 top-level working_logs for `EXTERNAL WIN\|public win\|externally validated\|peer-review\|published (in\|by)\|accepted (by\|at)`. **No unhedged external-win assertion found.** `SCIENCE_DEBTS_2026-08-03.md:37, 88, 279` all carry the correct "**ARITHMETIC VERIFIED (internal)** … **EXTERNAL WIN PENDING (no DOI)**". `_PROJECT_FINISH_ROADMAP.md:118–124` and `_ARXIV_CANDIDACY.md:59` mark the five unposted packages READY, never public. `_ARXIV_READINESS.md:13–14` states "**Do not invent endorsement.**" | **CLEAN** |
| Supertrace-note Zenodo DOI — does it exist in the corpus? | **YES.** `10.5281/zenodo.21763188` is recorded at ≥15 distinct sites, including `papers/supertrace-note/README.md:5`, `papers/README.md:11`, `docs/arXivReady/README.md:12`, `_ARXIV_READINESS.md:39` and `:1493`, `_ARXIV_CANDIDACY.md:69, 344`, `_PROJECT_FINISH_ROADMAP.md:118`, `ForJustin/ARXIV_OWNER_CHECKLIST.md:53, 99`. `_ARXIV_READINESS.md:1494–1495` adds "Record **verified by fetching it back**: title, author, date, license and both files all correct." | **NOT A FINDING** — the DOI is recorded. **I did not verify externally that the DOI resolves** (no network used in this audit); that remains unverified by me. |

### Class 6 — false page COMPLETE

Swept all 95 files for `(is\|are\|now) (COMPLETE\|SOLVED\|CLOSED)` and `SOLVED`, then read the hits in context. **No false COMPLETE / SOLVED / CLOSED found.** Every closure I checked carries a qualifier the body supports:

- `_FILE_COMPLETION_STATUS.md:22, 70, 183–185` keeps the smuggle ban ("No OPEN-THEORY items were marked COMPLETE").
- `T6_koide_desk_status.md:3, 41` — "**Do not mark OPEN-THEORY complete.**" / "**OPEN-THEORY stands.**"
- `_DOCKET_INDEX.md:140` (#92) — the title "(closes the Page curve)" is explicitly annotated "**ON THE COEFFICIENT ONLY** … the dynamical **Page curve remains D9 OPEN** … historical mis-grade language, not a curve booking."
- `_DOCKET_INDEX.md:144` (#96), `:141` (#93), `:143` (#95), `:74` (#24), `:82` (#33), `:116` (#68) all carry "mis-graded" / "unverified" annotations rather than clean closures.
- `bounce_e2e_verdict_2026-07-31.md:3, 19` and `bounce_promotion_2026-07-31.md:7, 11` grade the turn **RECONSTRUCTED CANDIDATE**, "Derived? **no**", matching `PRTOE_honest_status.md:108`.
- `T13_fingerprint_owed.md:34, 219–223` — "**T13 is NOT complete**" / "T13 is **not** complete — but it is no longer blocked."

**Verdict: CLEAN on class 6.**

### Class 1 / 2 in working_logs

Not flagged — allowed by the scope rule. Recorded for completeness: `TRIBUNAL.md:44–49` is the seat-addressing protocol itself (`@TO:GROK`, `>>BLUE`, `>>RED`, `@FROM:`), which is that file's job. `_AUDIT_LEDGER.md:5855` and `_ARXIV_READINESS.md:1388, 1417` mention TODO markers only as things being audited *for*.

---

## 2. `docs/BIBLIOGRAPHY.md` — FULL-BAR AUDIT

Read in full: 270 lines, all 11 numbered sections plus §6b, §8b, §8c and the trailing block.

### 2.1 Class 4 — the withdrawn 0.22% framing: **CLEAN**

`:257` is the only 0.22% site in the file and it presents the withdrawal correctly (quoted in §1 above). It also correctly carries the standing caveat that the τ ≈ 0.34–0.37 band is an **SU(3)** value while the sector is **SU(2) with N_f = 3**, "no determination exists in the right theory".

### 2.2 Class 1 — repair-log document history in a forward-facing file: **9 CONFIRMED sites**

`FINAL_PRODUCT_STYLE_GUIDE.md:17` routes exactly this material to the failures ledger or a working_logs package note, "**not the living paragraph**"; `:11` bans "was X@…; earlier Y@…" chains as "pure repair log".

| line | verbatim |
|---|---|
| `:13–16` | "*Merge note (2026-07-28): the sources held only in [PRTOE_references.md] **are now booked here**. They carry that file's data **verbatim** and keep its **[V]** verification stamp…*" |
| `:250–253` | "*Coverage note: keys appear in the docs as [AuthorYear]. The five internal-provenance **stragglers found by the audit** (SKELETON, the legacy action spec, intellectual_history, lss_parity, v4_dCDF_results) are **stamped in this pass**.*" |
| `:77` | "**Verified against the arXiv abstract page 2026-07-28**; **previously carried here as a bare identifier** with no author, title or year recorded anywhere in the corpus." |
| `:128` | "**Verified against the arXiv abstract and full text 2026-07-28; added because it is PRIOR ART** for the corpus's generation-count conclusion" |
| `:47` | "…so the **SN-stress verdict on the MeV corner was withdrawn** and corner selection **reverted** to CMB-S4 alone … The band's *lower* edge **had been misquoted by three orders in the estimate-grade first pass** — the correction is booked in the failures ledger (2026-07-18)." |
| `:63` | "The friendlier three-term ±0.0563 (−2.49σ) **is retired as failure #157**" |
| `:72` | "It quotes NO significance and concludes varying m_e cannot fully resolve the Hubble tension … i.e. **it runs against the claim it was formerly cited to support.**" |
| `:127` | "…and its Table 1 settled the fermion sign convention (net weight in str[k₁] POSITIVE), **retiring process error 21 in the failures ledger**." |
| `:74` | "**Standing correction on the record:** the \"2.5–3.6σ\" is the *residual tension left over*, **not** a preference for varying m_e (`docs/working_logs/_CANONICAL_VALUES.md`)." |

Note the asymmetry: `:11` of the style guide permits a **retirement notice to name the value it buries** (`_REDTEAM_BRIEF.md:52` restates this), so `:47`'s and `:63`'s *content* is defensible — what is not is the narration of *when the corpus got it wrong* ("first pass", "formerly cited", "process error 21", "in this pass").

### 2.3 Class 2 — embedded editor instructions in a forward-facing file: **5 CONFIRMED sites**

| line | verbatim |
|---|---|
| `:9–10` | "If a claim in any doc leans on a result not listed here, **that is a bug — file it**." |
| `:253` | "Anything cited in a doc but missing here is a **filed bug — the rule: no borrowed result without a line in this file**." |
| `:128` | "**The two are therefore NOT independent confirmations and must never be quoted as such.**" |
| `:195` | "…the journal, volume, article number and year above are the entire receipt, and **it needs an external check before any external presentation**." |
| `:16` | "…the field is left blank here rather than filled in from memory — **an incomplete citation is a smaller defect than a plausible wrong one**." |

The ~14 "**Locator unrecorded — needs external verification**" stamps are **NOT** flagged: they are honest status disclosures about the sources, not instructions to an editor, and they are the file's best feature.

### 2.4 Coverage bugs — sources the corpus leans on that BIBLIOGRAPHY.md does not carry

By the file's own rule (`:9–10`, `:253`) each of these is a filed bug. All verified absent by full read plus grep.

| missing source | where the corpus leans on it | why it matters |
|---|---|---|
| **Kabat (1995)** — the gauge contact term | `PRTOE_quantum_gravity.md:234` ("Gauge fields break the ratio through **Kabat's** contact term"); `exploratory/PRTOE_entropy.md:73` ("**Kabat 1995**") | Load-bearing for the area-law roster extension |
| **Donnelly & Wall** — edge modes | `PRTOE_quantum_gravity.md:234` ("which **Donnelly and Wall**…") ; named in `_RESIDUAL_DEBT_CENSUS.md:41` as "the **Donnelly–Wall edge-mode identification** of Kabat's term" | **37% of roster units** ride this one commitment (`_RESIDUAL_DEBT_CENSUS.md:42–43`); its rejection is the kill |
| **Hou–Slepian–Cahn; Philcox** — the BOSS 4PCF parity claim | `PRTOE_lss_parity.md:23` ("claimed significance (**Hou–Slepian–Cahn; Philcox** — ~5–7σ class)"); `T16_lss_parity_owed.md:3` | This is the **measurement P-2026-055 bets against**. The bibliography carries the two *referee* papers ([BOSSDESIparity2026] `:194`, [PhilTransA2025] `:195`) but not the claim itself — the registered bet has no source line |
| **MICROSCOPE** — the EP test | `PRTOE_stability.md:42` ("**MICROSCOPE** η cleared; measured EP violation kills the census"); `:69` ledger row 6 | §7 carries [Will2014], [HNS2009], [Vainshtein1972] but not the experiment actually named as cleared |
| **Brannen (2006)** — the published neutrino extension | `PRTOE_koide_relation.md:311` ("**Brannen's published neutrino extension (2006)** — which this corpus did not carry"); Brannen's φ = 2/9 + π/12 fit is load-bearing at `_OWNER_QUEUE.md:355–357` | The corpus explicitly notes it did not carry it — and still does not |
| **Martins–Shellard (1996, 2002)**; **Vinen (1957)** | `working_logs/census_scaling_mechanism.md:110–112` "Sources:" block | The VOS model is the entire mechanism that file exhibits (#168) |
| **Milne–McCrea** | `working_logs/expansion_energy_ledger.md:77` "Standard: the Newtonian energy-balance derivation of Friedmann (**Milne–McCrea**)" | Textbook, low weight |
| unattributed Nambu–Goto VOS calibration | `working_logs/census_c_chop_derivation.md:110–113` "Relativistic Nambu–Goto VOS calibrations give **c̃ ≈ 0.23** with characteristic loop-size parameter **α_NG ~ 0.1**" | A borrowed external number with **no source at all**, used as the external cross-check for c_chop = 2 |

**Verdict: CONFIRMED** (Kabat, Donnelly–Wall, Hou–Slepian–Cahn/Philcox, MICROSCOPE, Brannen, Martins–Shellard, Vinen, Milne–McCrea, NG-VOS).

### 2.5 Citation-data defects

| line | verbatim | verdict |
|---|---|---|
| `:264` | "**[TashiroVachaspati2013]** H. Tashiro, T. Vachaspati, \"Parity-odd correlators of diffuse gamma-rays and intergalactic magnetic fields,\" MNRAS 448, 299 (**2015**), arXiv:**1409**.3627." | **CONFIRMED** — the key's year (2013) matches neither the journal year (2015) nor the arXiv posting (1409 = Sept 2014). The file's header (`:3`) declares keys are "[AuthorYear]", so the key is a locator and it is wrong. |
| `:266` | "**[ColpiShapiroWasserman1986]** **S. Colpi**, S. L. Shapiro, I. Wasserman, \"Boson stars: gravitational equilibria of self-interacting scalar fields,\" Phys. Rev. Lett. 57, 2485 (1986)." | **SUSPECT** — the initial appears wrong (the standard PRL 57, 2485 (1986) reference is **M.** Colpi); the other two authors' initials are given correctly. Needs an external check. This is precisely the failure mode `:16` warns against ("a plausible wrong one"). |
| `:31` vs `:63` | `:31` "the model predicts **2.407–2.463**×10⁻⁵ across its committed genesis window, **−2.5 to −1.4σ**" · `:63` "the **standing row is −2.94σ**, the committed window −2.5 to −1.4σ" | **NOT A DEFECT** — cross-checked against `PRTOE_bbn_witness.md:74` (`\| D/H \| 2.387×10⁻⁵ (−2.94σ) \| 2.407–2.463 (−2.5…−1.4σ class) \|`), these are two columns of one table: the model's central value vs the class window. Both arithmetics reproduce on the ±0.0476 width. Flagged only as **presentational**: a reader of BIBLIOGRAPHY alone cannot tell which number is "the model's D/H prediction". |

### 2.6 Workshop leakage (observation, not a listed class)

BIBLIOGRAPHY.md sends a referee into the workshop at eight sites: `:74` (`_CANONICAL_VALUES.md`), `:97` (`PRTOE_room1_complex_completion.md`), `:102`, `:103` (`T7_lab_cousins_owed.md` lines 24, 51), `:259`, `:260`, `:261`, `:262` (`Basement_Roster_Discussions.md` lines 626, 630, 639). Recorded because a forward-facing source list that makes `working_logs/` load-bearing inherits the workshop's grade.

### 2.7 What is strong in BIBLIOGRAPHY.md

Stated so this is a graded audit and not a hit list. The file's discipline on incomplete receipts is the best in the corpus: `:24, 26, 40, 46, 47, 48, 62, 63, 85, 86, 97, 102, 103, 120, 134, 144, 145, 146, 147, 174, 180, 194, 195, 214, 224, 257, 258, 259, 260, 261, 262` each name exactly what is unrecorded rather than filling it from memory, and eleven carry an explicit "**Locator unrecorded — needs external verification**". `:128` [NavarroSalas2024] volunteers prior art *against* the corpus's own novelty and states "**The two are therefore NOT independent confirmations**". `:74` and `:76` book the competitor (EDE) as beating this model's mechanism "on every column". `:72` records that a source "runs against the claim it was formerly cited to support". `:194` records that the parity referee "reported favourably" for the null. That is adversarial self-citation, and it is rare.

---

## 3. PER-FILE COVERAGE LEDGER

**Total top-level files: 95.** `_runs/` excluded per scope. `_dead_runs` is a directory, not counted.

### Read in full with the Read tool — 66 files

`FINAL_PRODUCT_STYLE_GUIDE.md` · `SCIENCE_DEBTS_2026-08-03.md` · `STORY_GRADE_ELEVATION_RULE.md` · `QG_PROMOTION_CHECKLIST_20260803.md` · `CHATGPT_REFEREE_4_10_RESPONSE.md` · `README.md` · `README_LOGS.md` · `T1_galactic_atoms_owed.md` · `T2_smbh_atoms_owed.md` · `T3_neutrino_home_owed.md` · `T4_s8_growth_owed.md` · `T5_lowell_owed.md` · `T6_koide_desk_status.md` · `T7_lab_cousins_owed.md` · `T8_coincidence_owed.md` · `T9_direct_detection_owed.md` · `T10_gw_owed.md` · `T11_hubble_owed.md` · `T12_radio_lattice_owed.md` · `T13_fingerprint_owed.md` · `T15_indirect_detection_owed.md` · `T16_lss_parity_owed.md` · `T14_blue_team_2026-08-03.md` · `T14_i6_mirror_residual_smoke.md` · `T14_link5_joint_draw.md` · `_CANONICAL_VALUES.md` · `_CHAIN_STATUS_2026-07-30.md` · `_CONSISTENCY_AUDIT_2026-07-30.md` · `_SCRIPT_REGRESSION_2026-08-02.md` · `_cross_cutting.md` · `_parked_register.md` · `_RESIDUAL_DEBT_CENSUS.md` · `_MORNING_REPORT.md` · `_E2E_DERIVATION_BOARD.md` · `TOE_EXPANSION_SHELF_FENCE_20260803.md` · `_GATED_SHELF.md` · `_POSTERIOR_BOOKING_CHECKLIST.md` · `_FILE_COMPLETION_STATUS.md` · `_master_computes.md` · `_OWNER_QUEUE.md` · `_AUDIENCE_PREP.md` · `_PACKAGE_AUDIT.md` · `_PAPER_REDTEAM_FIXES.md` · `_SUBSTITUTIONS.md` · `_REDTEAM_BRIEF.md` · `_ARXIV_CANDIDACY.md` · `_PROJECT_FINISH_ROADMAP.md` · `_DOCKET_INDEX.md` · `_CANDIDACY_detection_nulls.md` · `_candidate_late_thaw.md` · `_chain_snapshot.md` · `alpha_c_same_response.md` · `TRIBUNAL.md` · `B1_crown_status_2026-07-31.md` · `B2_winding_gas_cv_findings.md` · `B5_mu_injection_findings.md` · `census_democracy_note.md` · `census_alpha_B_first_principles.md` · `census_c_chop_derivation.md` · `census_gamma_star_derivation.md` · `census_scaling_mechanism.md` · `fairbank_endorsement_packet_2026-08-02.md` · `bounce_e2e_verdict_2026-07-31.md` · `bounce_promotion_2026-07-31.md` · `expansion_energy_ledger.md` · `bounce_photon_medium_mass_note.md`

Plus **`docs/BIBLIOGRAPHY.md` — read in full (270 lines).**

### Partially read (targeted excerpts + full structural/grep sweeps) — 12 files

| file | lines | what I actually read |
|---|---:|---|
| `_ARXIV_READINESS.md` | 1497 | lines 1–70, 232–286, 1470–1497 read; whole file swept by grep for chain adjectives, external-win language, COMPLETE claims, and table structure |
| `_AUDIT_LEDGER.md` | 7176 | lines 62–86, 6290–6310, 6670–6690 read; whole file swept as above |
| `_AUDIT_PROTOCOL.md` | 1396 | grep sweep only (chain adjectives, COMPLETE, tables); hits at 509, 857, 915, 922, 1038, 1046–1051, 1194 inspected in the grep output |
| `T6_koide_owed.md` | 3559 | grep sweep only; hits at 348, 369, 1174, 1187, 1198, 1345, 1585, 2268, 2320, 2589, 2601, 3191, 3422, 3538 inspected in grep output |
| `T14_igmf_helicity_owed.md` | 685 | grep sweep only; all 17 `link 5` hits inspected — link-5 status is correctly synced to CLOSED NEGATIVE |
| `the_transfer_integral_spec.md` | 369 | lines 72–93 read; grep swept |
| `tilt_envelope_derivation.md` | 300 | grep sweep only |
| `ns_routeT_closure.md` | 125 | lines 70–89 read; grep swept |
| `fbar_cw_lo_closure.md` | 99 | grep sweep only |
| `family_coupling_lagrangian_spec.md` | 472 | grep sweep only |
| `basement_build_program.md` | 206 | grep sweep only |
| `first_roll_sign_scope.md` | 65 | grep sweep only |

### NOT OPENED — 17 files

Swept only by the corpus-wide greps (chain adjectives, COMPLETE/SOLVED, external-win, 0.22%/P-048, editor markers, table structure). **I did not read these; any defect not caught by those greps is unaudited.**

`Basement_Roster_Discussions.md` (683) · `Nontherm_Kill_Discussions.md` (888) · `Thermal_Half_Discussions.md` (255) · `Thermal_O1_Discussions.md` (768) · `PRTOE_R1_caustic_precision.md` (165) · `PRTOE_gate0_qft_derivation.md` (354) · `PRTOE_kill_and_patch_2026-07-07.md` (153) · `PRTOE_room1_complex_completion.md` (1208) · `PRTOE_session_2026-07-10_findings.md` (180) · `PRTOE_session_2026-07-11_findings.md` (65) · `PRTOE_session_2026-07-29_findings.md` (209) · `PRTOE_session_2026-07-29b_findings.md` (468) · `PRTOE_weakest_joints_and_cprep_2026-07-10.md` (179) · `bounce_derivation_workplan.md` (1683) · `bounce_reconstruction_rp.md` (1153) · `genesis_solver_B1_findings.md` (123) · `granule_sim_2field_findings.md` (165)

**66 read in full · 12 partial · 17 not opened = 95.** ✓

---

## 4. CHAIN-STATUS GROUND TRUTH — what `chains/` shows right now (2026-08-05)

Sources: `ps aux` (live processes), `chains/*.progress` (Read tool, last row), `chains/*.checkpoint` (`converged` + `Rminus1_last`), `chains/*.input.yaml` (`Rminus1_stop`), `chains/*.launchlog` (acceptance).

### Currently active — 3 chains, 3 MPI ranks each

| chain | process | ranks | last progress N | timestamp | R−1 (progress) | checkpoint `Rminus1_last` | stop | ×stop | `converged` | bookable |
|---|---|---:|---:|---|---:|---:|---:|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | RUNNING, pid **3769** (`mpirun -n 3`, since Aug 03) | 3 | **24858** | 2026-08-05T04:55:58 | **0.047912** | 0.047912299946403544 | 0.05 | **0.96×** (below stop) | **false** | **NO** — below stop but **no sampler self-stop** |
| `dyad_mnu_bbnfix` | RUNNING, pid **3768** (`mpirun -n 3`, since Aug 03) | 3 | **24677** | 2026-08-05T07:54:30 | **0.056889** | 0.0568891446726349 | 0.05 | **1.14×** | **false** | **NO** |
| `cmp_prtoe_routeD` | RUNNING, pid **175453** (`mpirun -n 3`, since Aug 03) | 3 | **6517** | 2026-08-05T04:07:15 | **0.705291** | 0.705290889925035 | 0.1 | **7.05×** | **false** | **NO** |

**Route-D trajectory (four progress rows, all of it):** 102.794555 @ N=1609 (08-03T20:53) → 4.941933 @ N=3290 (08-04T09:00) → 1.078971 @ N=5009 (08-04T19:23) → **0.705291 @ N=6517 (08-05T04:07)**. Monotone since row 2. Its launchlog is live to **2026-08-05 11:09**; raw per-rank accept from the last `Progress @` lines is ≈ **6.0%** (2473/41073, 2685/44347, 2604/43139).

**Acceptance caveat (booking authority):** the two bbnfix `.launchlog` files stopped growing at **2026-08-02 23:10** while their `.progress` files continued to 2026-08-05 — their stdout is no longer landing in `chains/*.launchlog`, so **raw Metropolis acceptance for the bbnfix pair is not readable from the launchlogs right now**. Any file quoting a current bbnfix acceptance from `chains/*.launchlog` is quoting a three-day-old figure. I did not chase where that stdout was re-routed.

### NOT running

| chain | last progress row | R−1 | status on the shelf |
|---|---|---:|---|
| `cmp_prtoe_conv_desi` | N=3744, 2026-07-22T11:06:00 | **13.251101** | "not running … owner restart" (`PRTOE_honest_status.md:168`); "unproduced (R−1=13.25, dead)" (`_FILE_COMPLETION_STATUS.md:67`) |
| `cmp_prtoe_zon_disp` | N=3456, 2026-07-22T09:37:45 | **17.81287** | "parked by decision" (`_PROJECT_FINISH_ROADMAP.md:93`); "Dead … Not relaunched deliberately" (`_GATED_SHELF.md:31`) |
| `cmp_prtoe_zon` | N=832, 2026-07-12T01:10:29 | **40.362246** | superseded by zon_disp |
| `cmp_prtoe_twist` | header only (85 bytes) | — | unstarted |
| `dyad_mnu_omk` | header only (85 bytes) | — | never produced accepted samples |
| `dyad_mnu_mcmc` | **no `.progress` file** | — | archive only (`_chain_snapshot.md:150`) |
| `cmp_prtoe_fixed_trgb` | **no `.progress` file** | — | launchlog only |
| PolyChord pair (`pc_prtoe` / `pc_lcdm`) | — | — | ended 2026-07-20, archived `chains/_archive_polychord_ended_20260720_0915/` |

### Forward-facing cross-check

`PRTOE_honest_status.md:27–37` (2026-08-05 stamp) reproduces all three live rows **exactly** — 0.047912@24858, 0.056889@24677, 0.705291@6517, all `converged: false`, all NOT bookable. That page is correct and is the currency authority.

`PRTOE_INDEX.md:13` still carries the **2026-08-04** numbers (lcdm 0.071122@21886, dyad 0.072286@21867, routeD 4.941933@3290) — labelled "Status 2026-08-04" and quoted with N and t, so it is a properly-stamped snapshot rather than a false present-tense claim; but it is exactly the surface `PRTOE_honest_status.md:83–87` names as superseded. **Out of my slice** (forward-facing, another agent) — recorded so it is not missed.

---

## 5. WHAT I ASSERT CLEAN, AND ON WHAT BASIS

- **Class 6 (false page COMPLETE): clean across all 95 files.** Grep sweep for `(is|are|now) (COMPLETE|SOLVED|CLOSED)` + `SOLVED`, every hit read in context. The corpus's grade discipline holds; `_DOCKET_INDEX.md` annotates its own mis-grades rather than hiding them.
- **Class 5 (external win without DOI): clean across all 95 files.** Grep sweep for external-win language; the only public claim is the supertrace Zenodo DOI, which is recorded at ≥15 sites. Not externally verified by me.
- **Class 4 in `BIBLIOGRAPHY.md:257`: clean** — read in full context; the withdrawal is stated and clause 4 is correctly named as the live falsifier.
- **T14 link-5 sync: clean.** `T14_link5_joint_draw.md:109–111` instructed `T14_igmf_helicity_owed.md` to move link 5 from SPLIT/owed to CLOSED NEGATIVE; `T14_igmf_helicity_owed.md:3, 226, 300` carry it, and `_FILE_COMPLETION_STATUS.md:81` and `_RESIDUAL_DEBT_CENSUS.md:89` agree.
- **`_CANONICAL_VALUES.md`: clean.** Read in full; every row carries home + proof + grade, τ is graded "candidate, referee pending", ρ_Λ¼ carries "**existence yes, precision NO**", c carries "**counting assumption, data-confirmed** — not framework-forced (#126)".
- **`_SUBSTITUTIONS.md`, `_PACKAGE_AUDIT.md`, `_CANDIDACY_detection_nulls.md`, `_PAPER_REDTEAM_FIXES.md`, `B2`, `B5`, `bounce_photon_medium_mass_note.md`, `alpha_c_same_response.md`: clean.** Read in full; all carry explicit do-not-claim fences and none overstates.

---

*Filed by RED AGENT 3. Report only — no file in the audited slice was edited.*
