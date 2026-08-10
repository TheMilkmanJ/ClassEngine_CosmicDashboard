# AGENT4 — RED cure verification, check-12

**Role:** adversarial verifier. Every grade below was made by opening the cured file at the cited
line. No grade rests on a receipt. A grep that printed nothing was only trusted after the same
pattern was shown to fire somewhere else in the tree.

**Package:** `docs/working_logs/_runs/docs_full_check12_20260805/`
**Ground truth used for chain claims** (`chains/*.progress`, last rows, read directly):

| chain | N | R−1 | t |
|---|---:|---:|---|
| `cmp_lcdm_mnu_bbnfix` | 24858 | 0.047912 | 2026-08-05T04:55:58 |
| `dyad_mnu_bbnfix` | 24677 | 0.056889 | 2026-08-05T07:54:30 |
| `cmp_prtoe_routeD` | 6517 | 0.705291 | 2026-08-05T04:07:15 |

---

## 1. Grep-adequacy audit

| staged log | class | pattern actually used (inferred from header + hits) | adequate? | what it MISSES | hits my broader sweep found that it did not |
|---|---|---|---|---|---|
| `grep_repair_log.txt` | repair-log document history | header declares scope **`docs/working_logs/` excl `_runs/`**; hit set keys on `corrected` / `was wrong` / `previously` | **NO — scope** | The **entire forward-facing corpus**: `docs/*.md`, `docs/exploratory/`, `docs/laws_and_rules/`, `docs/Dataset_Comparisons/`, `docs/arXivReady/`. Also misses the phrasings that carry edit history without the word "corrected": *has now actually been removed*, *never applied to*, *stood for a day*, *retraction stands*, *Earlier draft*, *previously carried*, *kept for the record* | `PRTOE_MATH_SPINE.md:356–365`, `:762–766`; `BIBLIOGRAPHY.md:77`; `exploratory/PRTOE_forced_combination.md:90` and `:112`; `PRTOE_honest_status.md:265`; `PRTOE_fairbank_note_draft.md:84` *(this last one has since been cured — it was present at first sweep, absent at re-check)* |
| `grep_editor_instr.txt` | embedded editor instructions | header declares scope **working_logs + BIBLIOGRAPHY**; semantic pattern on *"do not freeze …"* | **NO — scope and pattern** | (a) forward-facing files entirely; (b) the whole **marker** class — `WHOSE_TURN`, `@FROM:`, `@TO:`, `>>BLUE`, `>>RED`, `>>REF`, `TODO`, `FIXME`, `XXX`, `note to self`, `insert here`; (c) instructions to a future writer (*"any manuscript must …"*); (d) internal-process leaks. **Also: the log's 8 lines are 4 hits printed twice** — lines 2–5 are byte-identical to 6–9, so the hit count is inflated 2× | Marker class is **genuinely 0** in forward-facing docs — pattern verified live (it fires in `working_logs/_ARXIV_READINESS.md:1388`, `_AUDIT_LEDGER.md:5855`, several `_runs/` reports), so this is a real clean, not a bad-pattern clean. But: `PRTOE_quantum_gravity.md:303` and `:329` ("Any manuscript must give −1/2 as str[k₁]"), `exploratory/PRTOE_hierarchy_problem.md:1231` ("any manuscript must present the anchor as conditional"), and `PRTOE_INDEPENDENCE_AUDIT.md:66` + `:87` (internal **check-12** sweep named as in-progress inside a forward-facing file) |
| `grep_stale_chain.txt` | stale chain adjectives | header `=== stale chain was-trails ===`; **one** hit, `(was 5.77 H⁻¹` — a `(was …` was-trail hunt | **NO — catastrophically** | Every actual chain-currency form: `currently running`, `now running`, `live`, `in burn-in`, `converging`, `R−1 =`, `@N=`, timestamps, `×stop`, `as of <date>`. This is the highest-volume defect class in the corpus and the log surfaced **one** unrelated line | At time of staging, **11 forward-facing files** carried the superseded **2026-08-04** triple (lcdm 0.071122@21886 / dyad 0.072286@21867 / routeD 4.941933@3290) while 5 others carried the current 08-05 triple — the corpus held two mutually contradicting "current" stamps. Blue has since re-stamped most; **3 sites remain stale** (§3, R4). Also missed `PRTOE_MATH_SPINE.md:356–365` ("Current state (2026-08-02) … It is in burn-in"), still uncured |
| `grep_022.txt` | 0.22% framing | header declares scope **BIBLIOGRAPHY + working_logs excl `_runs` + arXivReady**; pattern on `0.22` / `0.0008` is fine | **pattern yes, scope NO** | **Every file Blue actually cured for this class was outside the grep's scope** — PREREGISTERED_PREDICTIONS, DERIVATION_HUNT, MATH_SPINE, THREE_EQUATIONS, DEPENDENCY_TREE, REFEREE_CALENDAR, READERS_RISK, cosmological_constant, koide_relation, lattice_note are all `docs/PRTOE_*.md`. The cures were driven by line-aware reading, not by this log; the log is decorative for this pass | Pre-cure live D1 sites the log could not see: `PRTOE_cosmological_constant.md` lede + body, `PRTOE_koide_relation.md` τ paragraph, `PRTOE_REFEREE_CALENDAR.md:142`, `PRTOE_PREREGISTERED_PREDICTIONS.md:1500/1504`. **Post-cure my forward-facing sweep for live `must reach 0.22` / `takes 0.22` / `needs σ ≲ 0.22` returns 0** — the class is genuinely cured, despite the log |
| `grep_external_win.txt` | EXTERNAL WIN | **BROKEN** — all 3 logged "hits" are the substring `doi` inside the word **doing** | **NO — the log is 100% false positives and 0% coverage** | Verified: `grep -n "doi" docs/PRTOE_coincidence_problem.md` returns exactly line 75 ("a dial **doi**ng the work"); same for `PRTOE_baryogenesis.md:221` ("is **doi**ng real work") and `PRTOE_quantum_gravity.md:470` ("worth **doi**ng"). The log contains **not one** real class-5 line, and it scanned a file (`quantum_gravity`) whose lines 53/83/486/519 carry `shipped` / `Zenodo-shipped` / `SHIPPED` — so those terms were not in the pattern either | Real class-5 surface, none of it logged: `PRTOE_honest_status.md:45`, `PRTOE_INDEX.md:14` and `:37`, `PRTOE_READERS_RISK.md:378`, `PRTOE_READERS_GUIDE.md:13–14`, `PRTOE_induced_gravity.md:28/45/241`, `PRTOE_neutrino_sector.md:7/173/176`, `PRTOE_neutrino_home.md:11/71/73`, `arXivReady/README.md:12/16`. **My own verdict on the class: CLEAN** — every one is `EXTERNAL WIN PENDING (no DOI)` / `READY not posted` / `SHIPPED` backed by a real Zenodo DOI `10.5281/zenodo.21763188` (`arXivReady/README.md:12`). No fabricated win. But that is my reading, not the log's — **the log proved nothing** |
| `grep_page_claim.txt` | false page COMPLETE | substring match on `complet*` | **NO — pattern** | Matches prose ("is completely", "determines it completely") and **forbid-column protective text** ("Treat floor number as completed bounce dynamics"), i.e. 13/13 hits are non-defects. It does not hunt the defect form at all: bare status stamps `**COMPLETE**`, `SOLVED`, `CLOSED`, `DONE`, `PROVEN` | `PRTOE_granule_scoping.md:7` ("Statistical core (S formula) is **DONE**") and `exploratory/PRTOE_UV_completion.md:7` ("target (deriving **c**) is **CLOSED**") — both qualified in context, both absent from the log. And the one site Blue actually cured, `exploratory/PRTOE_v5_five_verdict_derivation.md:8` ("Status: COMPLETE"), **is not in the log** — found by reading, not by the grep |
| `claude_red_check12.log` | — | **0 bytes** | n/a | Empty file; no evidence of any kind | — |

**Summary of the audit:** three of six staged greps (`stale_chain`, `external_win`, `page_claim`)
are inadequate by *pattern* and produce false cleans; two more (`repair_log`, `022`) are adequate by
pattern but scoped to exclude the forward-facing corpus, which is where the product lives; one
(`editor_instr`) is scoped out *and* prints its hits twice. The cures that landed this pass landed
because Blue read files line-aware, **not** because the staging found the defects.

---

## 2. Independent sweep — classes with no staged log

### 2a. Orphan tables

Scanned all 114 forward-facing `.md` files (`docs/*.md`, `exploratory/`, `laws_and_rules/`,
`Dataset_Comparisons/`, `arXivReady/`, ledger excluded) for pipe-rows with no header separator,
header-only tables, separator-not-second, and column-count drift. Discounting false positives from
escaped `\|` in math cells (`|Q−p| = |p−Q|`, `|Ψ|²H†H`) and from valid single-dash separators
(`|-|-|-|-|` at `PRTOE_MATH_SPINE.md:680` is legal GFM):

**One genuine orphan, and it is load-bearing —**
**`docs/PRTOE_DERIVATION_HUNT.md:159`.**
The ε = c·f̄·α_c factor table has its header at `:28`, separator at `:29`, and rows **c** (`:30`) and
**f̄** (`:31`). The third factor's row —

```
| **α_c** | 3α | **candidate (under test)** — a pre-registered value. …
```

— sits **alone at line 159**, after ~127 lines of intervening prose (`:33`–`:158`). It renders as
literal pipe-delimited text, not as a table row, and the rendered ε-decomposition table is missing
its third and most-contested factor. No staged log covers this class; Blue's `BATCH_GIANTS` row 4
marks `DERIVATION_HUNT` **CURE** for the 0.22% sites and reports nothing here.

The prior round's orphaned-table cure at `docs/PRTOE_quantum_gravity.md:243–245` was checked at the
file: a clean one-row table with a proper `| objection | status | note |` header and separator, not
nested inside or duplicating another table. **Correct.**

### 2b. Overclaims

Swept for `solves the` / `proves` / `first-principles derivation` / `zero free parameters` /
`theory of everything` / `outperform` / `beats ΛCDM` / `vindicat` / `breakthrough` / `definitive` /
`settles the` across the forward-facing corpus. **The corpus is disciplined on this class.** Nearly
every hit is a *fence against* the overclaim, not the overclaim:
`PRTOE_THE_AMPLITUDE.md:28`/`:141`, `PRTOE_DOMAIN_COVERAGE.md:21`, `exploratory/PRTOE_hierarchy_problem.md:1254`/`:1271`
("Do not say 'zero free parameters' unless c, f̄, α_c all hold"; "not 'zero free parameters'");
`PRTOE_deuterium_row.md:82` ("'the new physics beats ΛCDM on deuterium' is not a claim available to
it"); `PRTOE_fairbank_note_draft.md:80` ("Do not quote H₀ ≈ 69.9, any 'outperform ΛCDM' claim");
`PRTOE_honest_status.md:19`/`:94`, `PRTOE_READERS_RISK.md:22`, `PRTOE_induced_gravity.md:6`,
`exploratory/README.md:3`, `laws_and_rules/README.md:351` (all "**not** a Theory of Everything").

Two rhetorical flags, neither a false claim:

- `docs/laws_and_rules/README.md:237` — "**it VINDICATES the model**" (caps in original). Read in
  context it is defensible (if the observed β is instrumental systematics, P-2026-009's null is
  confirmed), but the register is promotional for a rules file.
- `docs/PRTOE_honest_status.md:225` — "this is now **proven**" on the genesis-draw handedness. Used
  of an adverse result, so it is a self-adverse "proven", not a win claim.

**No fabricated or unfenced overclaim found in the forward-facing corpus.**

---

## 3. Residuals — what is still wrong, verified at the file

| # | site | class | why it is a defect |
|---|---|---|---|
| **R1** | `docs/PRTOE_MATH_SPINE.md:356–365` | **stale chain + repair-log**, uncured | Reads *"**Current state (2026-08-02):** Route-D runs on its fifth launch…"*, narrates the 07-29 deadlock and the 08-01 relaunch, then *"**It is in burn-in**"* — and closes with pure edit history: *"see the addendum, where that phrase has now actually been removed from the sentence carrying it."* Ground truth: routeD is at N=6517, R−1=0.705291, t=2026-08-05T04:07:15 — three days past the stamp and out of burn-in. Blue's cure edited the paragraph **directly beneath this block** (`:367–374`) and left this one untouched |
| **R2** | `docs/PRTOE_MATH_SPINE.md:762–766` | **repair-log, now ORPHANED by a cure** | *"(This sentence read 'is the single decider' until 2026-07-29. **The §7 header has carried a correction saying it 'previously named it "the single decider"' since 2026-07-28** — but the correction was written at the head of §7 and never applied to this line…)"*. The §7 correction block it points at **was deleted** by the prior round's cure (visible in `git diff` on this file). The addendum now cites text that no longer exists — a cure-induced dangling reference, exactly the failure mode this verification is for |
| **R3** | `docs/PRTOE_DERIVATION_HUNT.md:159` | **orphan table row** | See §2a. Third factor of the ε decomposition detached from its table at `:28–31` |
| **R4** | `docs/PRTOE_DEPENDENCY_TREE.md:10`, `docs/PRTOE_neutrino_home.md:7`, `docs/PRTOE_neutrino_home.md:65` | **stale chain currency** | Still on the superseded 2026-08-04 triple. `DEPENDENCY_TREE:10` labels it *"**CURRENT** gate"*. `neutrino_home:7` is a residual-freeze banner. **The corpus self-identifies this:** `PRTOE_honest_status.md:83–87` says *"Any surface still carrying **2026-08-04** live R−1 numbers as if current (lcdm 0.071122 / dyad 0.072286 / routeD 4.941933) is stale."* Three surfaces still do. Blue marked `neutrino_home` **LEAVE** with the note "R−1 quoted present-only" (`BATCH_GIANTS:66`) |
| **R5** | `docs/PRTOE_INDEPENDENCE_AUDIT.md:66`, `:87` | **internal-process leak** | *"…which is the standing **check-12 sweep, still in progress**"* and *"check-12 ongoing"* in a forward-facing audit file. Goes stale the moment the sweep ends, and "check-12" is a house code no outside reader can resolve. Blue explicitly LEAVEs it (`BATCH_GIANTS:24`) |
| **R6** | `docs/PRTOE_quantum_gravity.md:303`, `:329`; `docs/exploratory/PRTOE_hierarchy_problem.md:1231` | **embedded editor instruction** | *"Any manuscript **must** give −1/2 as str[k₁]…"* etc. Instructions to a future writer, in living files. `:329` sits **inside a block the prior round cured** — the repair-log wrapper was removed and the instruction left behind. Never swept: `grep_editor_instr` was scoped to working_logs |
| **R7** | `docs/PRTOE_honest_status.md:91` | date drift | `## CURRENT (2026-07-31)` coexists with the 2026-08-05 CURRENT block above it — two "CURRENT" headers, four days apart |
| **R8** | `docs/PRTOE_REFEREE_CALENDAR.md` PolyChord row | date drift | Reads *"Not running — PolyChord off (**2026-08-04 stamp**)"* inside a header block Blue re-stamped to 2026-08-05 in this same pass |
| **R9** | `docs/BIBLIOGRAPHY.md:257` | internal rule inconsistency | Retains *"**0.22% lattice framing withdrawn**"* — the exact "D2 repair voice" Blue's own `BATCH_B:32` rule defines as a defect and which Blue **removed** from `lattice_note.md` and `cosmological_constant.md` in this same pass. `CURE_BIBLIOGRAPHY_P048_022.md:16` defends keeping it. Not a physics error (the framing *is* withdrawn per P-2026-048) — a consistency error: keep it everywhere or nowhere |
| **R10** | `exploratory/PRTOE_forced_combination.md:90`, `:112` | mild repair-log | *"The **earlier reading** that put the two 0.3% apart divided the model's number by √2…"* and *"…it is not a normalization spread, **which the paragraph above has now removed**."* `BATCH_EXPLORATORY:14` reports "Document repair-log / edit diary sections: **0**" across 44 exploratory files |

**Errors inside Blue's own package** (not forward-facing, but they misreport the tree):

- `BATCH_GIANTS.md:49` grades `grep_stale_chain.txt` **LEAVE** on the claim *"honest_status names
  stale ~0.14/0.19 as stale (correct)"*. Neither number appears in that log (which has one hit,
  `was 5.77 H⁻¹`) nor in `honest_status.md`, which names **0.071122 / 0.072286 / 4.941933** at
  `:84`. The disposition is supported by nothing.
- `BATCH_GIANTS.md:91` — the "Authority held (no invent)" block quotes the **stale 08-04** pair
  (`0.071122@21886` / `0.072286@21867`) while the same pass was re-stamping `REFEREE_CALENDAR` to
  the 08-05 numbers.
- `CURES.md:35–36` lists `PRTOE_lattice_note.md` and `PRTOE_koide_relation.md` under **"Explicit
  leave (not cured)"**, while the working tree carries real uncommitted edits to both (and
  `BATCH_B:43,45` records both as **CURE**). The cure ledger contradicts the tree and the batch.

---

## 4. Blue batch / cure verification — per cure

Every row below was verified by `git diff` on the touched file **and** by reading the cured lines in
place.

| # | file / site | Blue's claim | RED grade | basis |
|---|---|---|---|---|
| 1 | `PRTOE_PREREGISTERED_PREDICTIONS.md:1486–1516` | P-048 clauses 2/3 → Historical/sky-limited; clause 4 Live | **AGREE** | Read at file. Clause 4 window **[0.330, 0.370]** intact, neighbour inference **0.39 ± 0.05** intact, σ ≤ 0.0008 retained under an explicit "Historical (sky-limited; not currently executable)" label. Matches the standing facts exactly. No new repair-log |
| 2 | same file, `:1638`, `:1641`, `:1643` | m_π/√σ row repair-log removed | **AGREE** | *"(recomputed 2026-07-17 … the row previously read 0.274, computed at the retired τ = 0.345)"* → *"(anchors: chiral 0.300 at m_π/√σ = 0, physical 0.352 at 0.318)"*. Anchors, 0.308, the 1.9–5.1× margin and the Columbia corner 0.06–0.16 all survive |
| 3 | same file, `:1974–1978` | P-018 adjudicator repair-log removed | **AGREE** | Nine lines of edit diary replaced by present-tense *"a one-chain split-R̂ cannot detect confinement to a single basin (see math spine §7); multi-chain Route-D production is the standing instrument"*. The physics point (split-R̂ blind to single-basin confinement) survives; DESI DR3 as external adjudicator survives |
| 4 | `PRTOE_DERIVATION_HUNT.md:300–306`, `:325–327` | 0.22% decision rule → sky-limited + clause 4 | **AGREE** at the two cited sites; **DISAGREE on the file** | Both sites correct at the file. But the orphan α_c row at `:159` (R3) is untouched and unreported |
| 5 | `PRTOE_MATH_SPINE.md:33–36` | banner restated | **AGREE** at the banner; **DISAGREE on the file** | Banner verified: ideal point-values named, crown/null sky-limited (~0.98σ at σ=0), clause 4 live. But R1 (`:356–365`) and R2 (`:762–766`) remain, and R2 was **orphaned by the earlier cure to this same file** |
| 6 | `PRTOE_THREE_EQUATIONS.md:17` | referee sentence | **AGREE** | *"0.34657 crowns both; 0.34506 kills both"* → ideal point-values + sky-limited + clause 4 |
| 7 | `PRTOE_DEPENDENCY_TREE.md:68`, `:94` | ρ_Λ dies-if + Koide triple | **AGREE** at both cells; **DISAGREE on the file** | Cells verified. Line `:10` still carries the superseded 08-04 stamp labelled "CURRENT gate" (R4) |
| 8 | `PRTOE_REFEREE_CALENDAR.md` header block + `:142` | live read 08-05; lattice row clause-4 | **AGREE** | **Numbers checked against `chains/*.progress` digit for digit** — 0.047912@24858@04:55:58, 0.056889@24677@07:54:30, 0.705291@6517@04:07:15 all exact; ratios correct (0.705291/0.1 = 7.05×, 0.056889/0.05 = 1.14×). Lattice row `:142` correctly restated. Nit: PolyChord row still "(2026-08-04 stamp)" (R8) |
| 9 | `PRTOE_READERS_RISK.md:98–99`, `:235–240` | risk (a) + (j) | **AGREE** | Both read at file. (j) now: clauses 2/3 sky-limited, clause 4 executable, ordinary 1–3% scores neither way. Correct per standing facts |
| 10 | `PRTOE_cosmological_constant.md:3`, `:18–24`, `:123–127` | audience grade + 2 body sites | **AGREE** | *"must reach 0.22% precision to tell the two apart"* removed from both lede and body; replaced with sky-limited + clause 4. The +0.44% / 2.2599 meV / 0.34506 arithmetic and the existence-not-precision framing all survive |
| 11 | `PRTOE_koide_relation.md:237–244` | τ lattice paragraph | **AGREE** at the file | 0.44% gap, both candidate values and the one-temperature-or-two question all survive; the "separating the two takes 0.22% precision" clause is gone. *(Receipt mismatch: `CURES.md:36` files this under "not cured")* |
| 12 | `PRTOE_lattice_note.md:8`, `:94–96`, `:134` | D2 voice restated | **AGREE** at the file | Banner, precision § and ledger row 2 all now state the sky limit positively; the ~0.98σ number and the clause-4 window survive. *(Receipt mismatch: `CURES.md:35` files this under "not cured")* |
| 13 | `PRTOE_bigbang_no_singularity.md:14` | "AGREE-IF cure" process label removed | **AGREE** | *"§0/§1 prose fence (2026-08-04 AGREE-IF cure)"* → *"§0/§1 fence."*. Every substantive fence (floor paid, H_re OPEN-BLOCKED, F-A3, cyclic not booked, freeze link) survives verbatim |
| 14 | `PRTOE_coincidence_problem.md:30–31` | was-trail removed | **AGREE** | *"(was 5.77 H⁻¹ at the par-normalized B = 1…)"* → *"(B = 1/√2 from the dispersion, not a menu; par-normalized B = 1 would give 5.77 H⁻¹)"*. The counterfactual number is **kept** as a present-tense conditional rather than deleted — the right cure |
| 15 | `PRTOE_inflation_replacement.md:19–31` | horizon + seeds fenced | **AGREE** | Both bullets now conditional and marked **OPEN-BLOCKED**, consistent with `bigbang_no_singularity` ledger row 3. No claim strengthened |
| 16 | `exploratory/PRTOE_v5_five_verdict_derivation.md:8`, `:14–18` | COMPLETE → document-job COMPLETE + fence | **AGREE** | Header restated and a fence blockquote added directing readers to shelf/INDEX/honest_status for living grades. Correct class-6 cure |
| 17 | `BIBLIOGRAPHY.md:257` | 0.22% decision rule removed | **AGREE-IF** | **Condition:** the retained phrase *"0.22% lattice framing withdrawn"* is the same D2 voice Blue's own rule removed from `lattice_note` and `cosmological_constant` in this pass. Physics is right; the pass is internally inconsistent. Resolve one way or the other (R9) |
| 18 | `working_logs/_CANONICAL_VALUES.md:62` | ε-blind row repair voice removed | **AGREE** | *"corrected 2026-07-28: that figure is the candidate SPACING"* → present-tense restatement. σ_c ≤ 0.0115 as spacing, 0.97σ from 8/9, σ_c ≤ 0.0037 for 3σ, the 10×/~100× costs, the script pointer and #126 all survive |
| 19 | `DISPOSITION_STYLE_GUIDE_AND_FAMILY.md` | no edit; style guide is instruction home | **AGREE** | Verified `FINAL_PRODUCT_STYLE_GUIDE.md` is the declared home and the "do not freeze" language does not appear in forward-facing refuse columns |

**Dispositions I DISAGREE with:**

| Blue's call | RED |
|---|---|
| `BATCH_GIANTS:24` — `INDEPENDENCE_AUDIT` **LEAVE**, "check-12 mention is process, not a false COMPLETE" | **DISAGREE.** Correct that it is not a false COMPLETE; it is an internal-process leak with a built-in expiry (R5) |
| `BATCH_GIANTS:49` — `grep_stale_chain` **LEAVE** | **DISAGREE.** The supporting claim matches neither the log nor the file, and the class is not clean (R1, R4) |
| `BATCH_GIANTS:66` — `neutrino_home` **LEAVE**, "R−1 quoted present-only" | **DISAGREE.** `:7` and `:65` carry the superseded 08-04 stamp that `honest_status:83–87` declares stale (R4) |
| `BATCH_EXPLORATORY:14` — "Document repair-log / edit diary sections: **0**" over 44 files | **DISAGREE.** `forced_combination.md:90`, `:112` (R10) |
| `BATCH_GIANTS:19` / `CURES.md:18` — `MATH_SPINE` **CURE** (banner only) | **AGREE-IF** the file is finished. As it stands the banner is cured and the two worst sites in the file are not (R1, R2) |

**Not fabricated, checked:** the receipt cited at `PRTOE_honest_status.md:31` and in the
`REFEREE_CALENDAR` header — `bbnfix_booking_20260805_170213` — **exists** on disk.

**No cure was found to have weakened the physics.** Every edit I opened preserved the substantive
content (numbers, windows, conditionality, fences) and removed only narration. Zero new repair-log
sentences were introduced by this pass; zero new dangling tables. The one dangling artefact (R2) was
created by the **prior** round's cure, not this one.

---

## 5. Working-tree state

**The prior round's cures were left uncommitted and are still uncommitted.** Check-12's cures have
been layered on top of them in the same unstaged diff, so the two rounds are **no longer separable
by `git diff` alone**. Anyone auditing "what did check-12 change" from the tree will also be reading
the previous round's edits.

28 modified `.md` files under `docs/` (excluding `_runs/`), none staged:

```
docs/BIBLIOGRAPHY.md                         docs/PRTOE_cosmological_constant.md
docs/PRTOE_CHAIN_TABLES.md                   docs/PRTOE_fairbank_note_draft.md
docs/PRTOE_CODE_MANIFEST.md                  docs/PRTOE_honest_status.md
docs/PRTOE_DEPENDENCY_TREE.md                docs/PRTOE_hubble_tension.md
docs/PRTOE_DERIVATION_HUNT.md                docs/PRTOE_inflation_replacement.md
docs/PRTOE_DOMAIN_COVERAGE.md                docs/PRTOE_koide_relation.md
docs/PRTOE_INDEX.md                          docs/PRTOE_lattice_note.md
docs/PRTOE_MATH_SPINE.md                     docs/PRTOE_quantum_gravity.md
docs/PRTOE_PREREGISTERED_PREDICTIONS.md      docs/PRTOE_s8_growth.md
docs/PRTOE_READERS_GUIDE.md                  docs/PRTOE_s8_tension.md
docs/PRTOE_READERS_RISK.md                   docs/PRTOE_bigbang_no_singularity.md
docs/PRTOE_REFEREE_CALENDAR.md               docs/PRTOE_coincidence_problem.md
docs/PRTOE_THREE_EQUATIONS.md                docs/exploratory/PRTOE_hierarchy_problem.md
docs/exploratory/PRTOE_v5_five_verdict_derivation.md
docs/working_logs/_CANONICAL_VALUES.md
```

Diffstat: **322 insertions, 343 deletions** — net-negative, consistent with a narration-removal pass
rather than a claim-adding one.

Also untracked and accumulating: ~120 `docs/working_logs/_runs/bbnfix_booking_20260805_*/`
directories (the 5½-minute booking-refuse cards, running through `..._171307`). Not a defect —
noting them because they dominate `git status` and make the docs changes hard to see.

The commit `d6b6e664` message — *"RED AGREE tenth site: repair-log class now clean corpus-wide"* —
**is not accurate.** R1, R2 and R10 are repair-log residue outside the failures ledger, and R2 is
residue the tenth-site cure itself orphaned. The three currently-active chains
(`cmp_lcdm_mnu_bbnfix`, `cmp_prtoe_routeD`, `dyad_mnu_bbnfix`) were read-only throughout; nothing
was stopped, restarted or reconfigured.

*NO FABRICATIONS. Every grade above was made at the file.*
