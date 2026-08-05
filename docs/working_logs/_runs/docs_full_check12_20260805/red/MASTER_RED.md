# MASTER_RED — docs full check-12 (2026-08-05)

**Seat:** Claude RED (CLI) · **Package:** `docs/working_logs/_runs/docs_full_check12_20260805/`
**Charge:** full line-by-line / check-12 of the whole docs tree; verify blue's cures.
**Rules honoured:** NO FABRICATIONS · MCMCs left running (read-only throughout) · no PolyChord ·
failures ledger may keep history · grade-history of a *claim* is legitimate, edit-history of a
*document* is not.

---

## 0. CORRECTION RED OWES FIRST

**Commit `d6b6e664`'s claim — "RED AGREE tenth site: repair-log class now clean corpus-wide" — is
false, and it was red's own claim.** Three independent seats this round found survivors in
`PRTOE_MATH_SPINE.md`, `PRTOE_PREREGISTERED_PREDICTIONS.md` and `PRTOE_cosmological_constant.md`
(§2a). Red's earlier sweep missed them because the phrases **wrap across lines** and the patterns
were single-line. Red also re-ran a "clean" verdict on this same class earlier **today** (§5) and was
wrong again for the same reason.

The standing lesson, now demonstrated three times: **a grep that prints nothing proves nothing.**
Red states it plainly rather than filing it quietly.

---

## 1. Chain ground truth — derived independently, before reading any blue or agent file

Read from `chains/` and `ps`, not from any document.

| chain | ranks | R−1 | N | timestamp | vs stop | checkpoint |
|---|---:|---:|---:|---|---|---|
| `cmp_lcdm_mnu_bbnfix` | 3 | **0.047912** | 24858 | 2026-08-05T04:55:58 | **below** 0.05, no self-stop | `converged: false` |
| `dyad_mnu_bbnfix` | 3 | **0.056889** | 24677 | 2026-08-05T07:54:30 | 1.14× stop 0.05 | `converged: false` |
| `cmp_prtoe_routeD` | 3 | **0.705291** | 6517 | 2026-08-05T04:07:15 | 7.05× stop 0.1 | `converged: false` |

Three `mpirun -n 3` trees alive in `ps`. Agents 1 and 4 reproduced this table independently and
digit-for-digit. Dead instruments confirmed dead: `conv_desi` last 13.251101 @ 2026-07-22,
`zon_disp` last 17.81287 @ 2026-07-22 — the corpus's quoted 13.25 / 17.81 are **accurate**.

**Booking gate read at `scripts/book_bbnfix_when_ready.py`:** requires **(1)** progress R−1 < 0.05
**and (2)** `converged: true`. All three checkpoints read `false`.

> **Conclusion re-graded, not just the numbers.** The ΛCDM twin has crossed **below** 0.05. This does
> **not** move booking — the gate is conjunctive and nothing has self-stopped. **NOT bookable remains
> correct.** Blue's chosen phrasing ("below stop 0.05 **without** self-stop, still **NOT bookable**")
> is exactly right and red endorses it.

---

## 2. Findings

### 2a. Repair-log document history — CLASS NOT CLEAN (6 CONFIRMED)

| file:line | verbatim | note |
|---|---|---|
| `MATH_SPINE.md:762-766` | *"This sentence read 'is the single decider' until 2026-07-29. The §7 header has carried a correction saying it 'previously named it "the single decider"' since 2026-07-28 — but the correction … never applied to this line … so the retracted phrase stood for a day beneath its own retraction."* | Worst survivor. Pure document edit-history. **Also now a dangling reference — see §3.** |
| `MATH_SPINE.md:364-365` | *"see the addendum, where that phrase has now actually been removed from the sentence carrying it"* | Tells the reader what was deleted elsewhere in the same file |
| `MATH_SPINE.md:736-739` | *"the earlier gloss here … was **wrong and is corrected in §7**"* | "the earlier gloss *here*" = this document's own prior text |
| `PREREGISTERED_PREDICTIONS.md:410` | *"(This entry formerly demoted 'c~1 derived' to 'c~1 NATURAL' …)"* | **Violates the file's own header policy** at `:7-9`: repair narrative is to be *rehomed to the ledger* "so this file does not read as a fit-forcing repair log" |
| `PREREGISTERED_PREDICTIONS.md:1677-1692` | *"LABEL CORRECTION ONLY … **That was my error** — it assumed the shift is ε·Θ…"* | Repair narrative **+ first-person seat voice**; the identical text is *already* rehomed to `FAILURES_LEDGER.md:5698-5711`, so this is an un-stripped duplicate |
| `cosmological_constant.md:557` | *"#### Correction to the line above, same day: the 1.33% was an underestimate"* | A section **heading** whose subject is the document's own earlier line; §§474-716 read as a chronological edit diary |

### 2b. Broken / orphaned tables — 8 sites, CONFIRMED at render

Detector `red/orphan_tables.py`; render proof `red/show_split.py` (both read-only, in this package).
First pass returned 22; **15 were escaped-`\|` false positives** which the refined pass excludes.
GFM splits on every unescaped `|` and **silently drops** cells past the header width.

| # | file:line | mode | what the reader loses |
|---|---|---|---|
| 1 | `PRTOE_fingerprint_lattice.md:32` | unescaped `\|Ψ\|²` ×2 → **7** cells vs header 3 | **Severest.** The *current standing* column renders as the single character **"Ψ"**. Dropped: the two-loop argument, the `~20,000× short` figure, and the row's whole verdict — **"no bleed, no blowout, and no healer: D/H carries −2.5 to −1.4σ"** |
| 2 | `PRTOE_DERIVATION_HUNT.md:159` | **orphan row** | The **α_c** row of the ε = c·f̄·α_c factor table, stranded **127 lines** from its header/separator at `:28-29` (rows c and f̄ sit at `:30-31`). The rendered ε-decomposition is **missing its third and most-contested factor**. *(Diagnosis credit: agent 4 — sharper than red's own.)* |
| 3 | `PRTOE_DEPENDENCY_TREE.md:47` | 4 cells vs header 3 | The ultralight-mass row's **falsifier** dropped: "either exposure closing the gap kills the mass…" — a Tier-2 "dies if" cell written into a Tier-1 3-column table |
| 4 | `exploratory/PRTOE_hierarchy_problem.md:1094` | `λ\|S\|²\|H\|²` → 6 vs 2 | Cell renders as bare **"λ"**; "for a gauge-singlet scalar S" dropped |
| 5 | `exploratory/PRTOE_the_great_chain.md:172` | `\|Δα/α\|` → 6 vs 4 | The **Oklo bound `< 10⁻⁸ over 2 Gyr`** — the passed fence itself — dropped |
| 6 | `exploratory/PRTOE_the_great_chain.md:120` | `\|Δμ/μ\|` → 6 vs 4 | GEN-10 row mangled; "chemistry uniform to ppm since z=4" + citation dropped |
| 7-8 | `PRTOE_FAILURES_LEDGER.md:684`, `:685` | 3 vs 2 | Third cell dropped ("the pair stands by derivation"). Ledger's charter protects *content*, not a broken render — reported, ranked lowest |

> **Red corrects agent 4 here.** Agent 4 dismissed the `|Ψ|²` sites as escaped-pipe false positives.
> They are **not escaped** — `grep -c '\\|Ψ'` on `fingerprint_lattice.md:32` returns **0**, and the
> render proof splits the row into 7 cells. Sites 1, 4, 5, 6 stand.

### 2c. Overclaims — 4 CONFIRMED

| file:line | claim | why it is an overclaim |
|---|---|---|
| `FAILURES_LEDGER.md:141` | *"ξ … now carries **three independent confirmations**"* | **False as current** — flaggable under the ledger's special rule. The same file retracts it at `:5860`; `INDEPENDENCE_AUDIT.md:35` grades it *"Zero confirmations today — three commitments"*; `MATH_SPINE.md:1014` lists it as a **non-claim**. Two of the three legs are ones the corpus itself killed (ξ is definitionally circular; superradiance is an *exposure*) |
| `FAILURES_LEDGER.md:159` | *"pinned **three independent ways**"* | Same withdrawn claim, second site |
| `DERIVATION_HUNT.md:1287` | *"**Everything else in the corpus is derived, quantified, or dead with a documented autopsy.**"* | Contradicted by the corpus's own board: Page Q6 **OPEN**, bounce **OPEN-BLOCKED**, Koide Wilson inputs **5/5 MISSING**, σσ **MISSING_INPUT**, absolute SI G **OPEN** |
| `THE_AMPLITUDE.md:133` (+`:34`) | f̄ = 2/π graded **derived**, residual column **"—"** | `DERIVATION_HUNT.md:156-158` states the residual explicitly — *"strengthened candidate, coupling form data-selected, **not an absolute closure**"*; `FAILURES_LEDGER.md:4926` agrees. The page also contradicts **itself**: `:26` calls f̄ "**a live triple**". **Blue graded this file LEAVE; red disagrees on this row.** |

> **f̄ conclusion re-graded:** the overclaim is **local and does not propagate.** The page's own rule
> is "Effective grade = weakest parent", and c = 9/10 is *OPEN/assumption* while α_c is
> *OPEN-BLOCKED* — both weaker than f̄ either way. **The ε stack grade is unchanged.**

Screen `red/empty_residual.py` surfaced 16 closed-grade/empty-residual rows. Red adjudicated only
those it could cross-check and confirms **exactly one** (f̄). Others cleared on inspection —
`entropy.md:189` area-law 1/4 "complete (paid)" is a machine-checked ratio (12π/48π), consistent with
`induced_gravity.md:28`; `quantum_tunneling.md:93` is textbook WKB. **13 remain unadjudicated and are
listed as residual, not as findings.**

### 2d. The one finding that can move a physics verdict — and red resolves it

`PRTOE_MATH_SPINE.md:158`:

> *"a +0.44% OFFSET, i.e. **~1.8σ** on the observational error … ρ_Λ¼ inherits **~0.25% from Ω_Λ's
> ~1%**"*

Every other surface uses **±0.449% → ~0.98σ** (`lattice_note:12`, `READERS_RISK:234`,
`REFEREE_CALENDAR:134` and `:142`, `PREREGISTERED:1477`). This is load-bearing: **the entire
P-2026-048 "crown/null is sky-limited, clauses 2/3 not executable" ruling rests on that 0.98σ** — the
ruling four files spent this morning propagating. Agent 1 flagged it as an owner call.

**Red resolves it instead.** `ρ_Λ = 3H₀²Ω_Λc²/8πG ∝ h²Ω_Λ`, so the error must carry **h² as well as
Ω_Λ**. `REFEREE_CALENDAR:134` gives the provenance in words — *"Planck's **1.80% on ρ_Λ** quartered"*
→ 0.449%. Check against Planck 2018: Ω_Λ = 0.6889 ± 0.0056 → 0.81%; H₀ = 67.36 ± 0.54 → 0.80%,
doubled for h² → 1.60%; quadrature **√(0.81² + 1.60²) = 1.80%**, reproducing the corpus figure
exactly.

> **MATH_SPINE:158 is the wrong number** — it quarters Ω_Λ's ~1% alone and **drops the h²
> contribution**. Therefore **±0.449%, 0.98σ, and the sky-limited withdrawal all STAND.** The fix is
> local to `MATH_SPINE:158`; no other surface moves, and **no physics verdict changes.**
> *(Caveat stated, not hidden: Ω_Λ and h are correlated in Planck, so strict quadrature is an
> approximation — but it lands on 1.80% and the ~1% reading cannot, because it omits h² entirely.)*

### 2e. Stale chain currency — 4 sites uncured after blue's sweep

| file:line | text | ground truth |
|---|---|---|
| `PRTOE_DEPENDENCY_TREE.md:10` | *"**CURRENT gate** REFUSED (lcdm R−1 **0.071122** N=21886 … dyad **0.072286**)"* | Superseded 08-04 triple, **explicitly labelled CURRENT** — worse than an undated quote |
| `PRTOE_neutrino_home.md:7` (and `:65`) | same 08-04 triple | Superseded |
| `MATH_SPINE.md:356-365` | *"**Current state (2026-08-02):** Route-D runs on its fifth launch … **It is in burn-in**"* | routeD has written 4 convergence statistics since and sits at 7.05× stop — not burn-in. Blue cured the paragraph **immediately beneath** this one |
| `PREREGISTERED_PREDICTIONS.md:1888-1896` | *"The run stopped … **no convergence statistic was ever computed** … failed three times … **single-core host** … months"* | **Every clause false today**: routeD is live on **3 MPI ranks**, 5 progress rows, R−1 102.79 → **0.705291**. Partly self-cured 90 lines later, but the reader hits the false paragraph first |

### 2f. Editor instructions in forward-facing files — 5 sites

Red does **not** flag the corpus-wide **"Forbidden claims"** blocks or `Forbidden` ledger columns:
those are a deliberate reader-facing honesty convention. These are different — imperative voice aimed
at a writer or a seat:

- `PRTOE_quantum_gravity.md:329` *"**Any manuscript must** give −1/2 as str[k₁] with the Weyl deficit alongside it"* — left behind *inside* a block cured this round; `:303` same shape
- `exploratory/PRTOE_hierarchy_problem.md:1231` *"any manuscript must present the anchor as conditional"*
- `PRTOE_THE_AMPLITUDE.md:28` *"**Do not say** 'zero free parameters' unless c, f̄, and α_c all hold"* — mid-prose; `:141` already carries the reader-facing form ("**Non-claims:** …")
- `PRTOE_INDEPENDENCE_AUDIT.md:66`, `:87` *"the standing **check-12 sweep**, still in progress"* — an internal process, named as live, inside a forward-facing file
- `PRTOE_PREREGISTERED_PREDICTIONS.md:688-689` *"**Whether the tag itself should read OBJECT-OBSTRUCTED is an owner call** — I have not rewritten a pre-registration"*
- `FAILURES_LEDGER.md:5826` *"Rehomed … after **Claude AUDIT AGREE-IF**"* — names a seat and an internal verdict class

Consistency point: blue cured "Do not kill" as instruction voice in `CODE_MANIFEST` / `CHAIN_TABLES`
this round but left these.

### 2g. 0.22% — one residual survives

`PRTOE_DERIVATION_HUNT.md:1279`: *"a 0.44%-class prediction (**the P-048 fork decided**)"* — the open
-surface table still sells the lattice as *deciding the fork*. The same file carries the withdrawal
correctly at `:305`/`:327`; this row was not swept.

### 2h. Lower-severity / advisory

- `PRTOE_lattice_note.md:12` — T_c = 177.10 keV called **derived** unqualified, in the one file **approved for outside circulation**; `READERS_RISK` §3(a) calls the same object *candidate-grade*. **SUSPECT**, owner's call.
- `PRTOE_INDEX.md:9` — eight undefined in-house coinages ("Θ densify", "match-book under stocked forms", "N6-from-absence", "Wilson invent", "page densify", "supertrace-as-G") on **the first shelf file an outside reader opens**; none in the READERS_GUIDE glossary.
- `PRTOE_READERS_RISK.md` §3 — list mis-lettered **(a)(b)(c)(d)(e)(g)(h)(f)(i)(j)(k)**; a referee citing "§3(f)" lands in the wrong place.
- `exploratory/PRTOE_INTERACTION_ATLAS.md:553` — "theorem-grade census result" over a four-portal enumeration. Mitigated by an unusually honest header ("the bet itself is **UNSETTLED** … **ZERO** confirmed entries"). Wording, owner's call.

### 2i. `docs/exploratory/` — the tree is materially dirtier than the shelf

Agent 2 read 16 of 45 files line-by-line (~5,200 lines) and swept all 45 structurally. Tally:
**15 repair-log CONFIRMED · 11 editor instructions · 6 fork-as-executable · 11 overclaims · 4 false
COMPLETE · 3 broken tables · 13 broken links.** The five red verified at the file:

| file:line | class | finding |
|---|---|---|
| `exploratory/README.md:114-115` | **false COMPLETE / overclaim** | *"all **883** local markdown links under `docs/` were resolved against the filesystem … **Zero unresolved.**"* — **the acceptance test's own claim is false.** Red verified three failure modes by `ls`: `](exploratory/PRTOE_light.md)` from *inside* `exploratory/` resolves to the nonexistent `docs/exploratory/exploratory/…`; `](BIBLIOGRAPHY.md)` → nonexistent `docs/exploratory/BIBLIOGRAPHY.md`; `](../scripts/…)` → nonexistent `docs/scripts/`. All three correct targets **do** exist, so these are depth errors, not missing files. **13 sites** |
| `exploratory/PRTOE_fairbank_note_HOLD.md` | **overclaim + editor instr + stale chain** | Header says *"shareable as a draft"* for a **named-addressee outreach letter**; footer 72 lines later says *"superseded lineage / do not use as live derivation"*. Carries a literal **"## Before send"** to-do list, an owner-approval instruction, four sections of before→after edit history, and a chain read **8 days and 1.3 orders stale** (quotes ΛCDM R−1 ≈ 1.0; ground truth **0.047912**) |
| `exploratory/PRTOE_PHYSICS_DOMAINS.md:56, 488-489`; `PRTOE_forced_combination.md:96-97, 185, 217` | **4** fork-as-executable | Five further sites sell the P-2026-048 lattice as a live CONFIRM/KILL referee (*"a lattice T_c/√σ … confirms or kills it"*), against the registration's own *"not executable at present cosmological precision — the limit is the sky's, not the lattice's"*. **This more than triples the class-4 residual** beyond §2g |
| `exploratory/PRTOE_PHYSICS_DOMAINS.md:367` vs `:875` | **8** unflagged numeric contradiction | Same file, same quantity (θ-channel `df_amp/dθ₀`), same `r_t = 0.9`: **"5.4/rad"** at `:367` vs **"~350/rad"** at `:875`. **65× apart, unflagged.** Red confirms both refer to the θ-channel gradient at the same r_t; red does **not** claim to know which is right — owner call |
| `exploratory/PRTOE_kappa_v_derivation.md:69-72` | **8** overclaim | Body says the window landing is *"derived, not fitted to it"* while the file's own binding header says *"AMPLITUDE-INPUT (k_eff is **chosen, not derived**)"* and *"'Derived' may not re-inflate"*. File also admits *"Scripts were job-scratch, not retained"* |

Agent 2 independently reached red's §5 adjudication on `hierarchy_problem:967` (**not** the withdrawn
framing — it is d = 3 vs 2.993) and **sharpened it**: on its own terms it is still a class-8
overclaim, because the observational side carries ±0.449%, so the quoted agreement **sits inside its
own error bar**. Red adopts that sharpening.

### 2j. `docs/working_logs/` + `BIBLIOGRAPHY.md` — the operational risk lives here

Agent 3 read **66 of 95** top-level files in full, 12 partial, 17 grep-swept only; `BIBLIOGRAPHY.md`
in full. Working-logs bar is narrower (history and house shorthand are allowed there) — these are
flagged because they are **factually false now** or **contradict the shelf**. Tally: **19 stale-chain
CONFIRMED · 6 malformed tables · 4 wrong-vs-artifact · 3 shelf contradictions · 9 repair-log and 5
editor-instruction sites in BIBLIOGRAPHY (full bar applies there) · 9 bibliography coverage gaps.**

| file:line | class | finding — red-verified |
|---|---|---|
| `_PROJECT_FINISH_ROADMAP.md:161-165` | **3, operational risk** | *"RouteD: leave alone (**R−1 ~129, one progress row**) — **surgery plan above** if second progress still has R−1 ≫ 10 … "*. routeD has **four** progress rows and sits at **0.705291** — the headline figure is **183× stale**. Line 161 likewise quotes dyad ~0.192 / lcdm ~0.141 against 0.056889 / 0.047912. **The doc's own skip-criterion is met, so the correct action is "leave alone" — but a reader skimming the stale headline could fire an archive-and-reseed on a converging chain.** Partially guarded by *"owner kills only when applying the reseed"*. **Highest operational risk red found this pass** |
| `_master_computes.md:19, 51` | **3** | *"**LIVE 2026-07-17: three chains running** (`zon_disp`, `routeD`, `fixed_trgb`)"* — zon_disp died 2026-07-22, `fixed_trgb` has **no progress file**; and *"gated behind the **live pc_prtoe run**"* — PolyChord was **archived 2026-07-20** and is under a standing ban. Date-stamped, which mitigates |
| `_ARXIV_READINESS.md:28-29` | **8, wrong vs artifact** | *"Page counts … that say **7 pp (radio)** … are pre-note-strip; **current PDFs are 6**"*. **Verified at the artifact:** `papers/radio-lattice/main.log` reports *"Output written on main.pdf (**7 pages**, 303368 bytes)"* and the on-disk `main.pdf` is **exactly 303368 bytes**, mtime 2026-08-02 23:10 — so the log describes the current PDF and the current PDF is **7 pages**. The false number sits in the section that declares *"this section wins"* |
| `census_democracy_note.md:30-31` | **9, shelf contradiction** | Grades c = 9/10 as *"licensed by the blindness principle"* — a step the shelf **withdrew**: `honest_status.md:132-145` (*"that step does not exist … **No single criterion returns 9/10**"*), `_DOCKET_INDEX.md:174` (#126 *"withdrawn, not supplied"*). **The whole file is the withdrawn argument, carrying no banner** |
| `docs/BIBLIOGRAPHY.md` | **coverage gaps** | Forward-facing sources absent **by the file's own rule** ("no borrowed result without a line in this file"): **Hou–Slepian–Cahn / Philcox** (the BOSS 4PCF result P-2026-055 bets against), **Kabat 1995** + **Donnelly–Wall** (37% of the area-law roster rides the edge-mode commitment), **MICROSCOPE**, **Brannen 2006**, Martins–Shellard / Vinen / Milne–McCrea, and an unattributed Nambu–Goto c̃ ≈ 0.23 |
| `_FILE_COMPLETION_STATUS.md:47, 67` | **3** | Carries *"routeD~103"* — verbatim the framing `FINAL_PRODUCT_STYLE_GUIDE.md:23` **bans** |

**Machine-state note worth the owner's eye, independent of any document:** both bbnfix **launchlogs
stopped growing 2026-08-02 23:10** while their progress files ran on to 08-05. Since acceptance lives
in the launchlog and never in the chain file, **raw acceptance for the bbnfix pair is not currently
readable**. routeD's launchlog is live (~6.0% raw accept). Red changed nothing — chains untouched.

---

## 3. Cure-induced defect — the check red exists to run

**`MATH_SPINE.md:762-763` is now a dangling reference to text this round deleted.** It states that
"The §7 header **has carried** a correction saying it 'previously named it "the single decider"'".
`git diff` shows that block was **removed** this pass:

> `-> **Correction, 2026-07-28 …: there was …** This passage previously named it "the single decider".`

The cure was correct in itself; it orphaned a citation 400 lines away. Red found no other
cure-induced defect: re-running the repair-log, editor-instruction and orphan-table sweeps *after*
blue's edits landed produced **no new** "this was corrected"-class sentence and **no new** broken
table.

---

## 4. Blue's cures — verified at the file/diff, never at the receipt

| cure | verdict | what red checked |
|---|---|---|
| Chain currency corpus-wide → 08-05 | **AGREE** | Blue's stamps match red's independent ground truth (§1) exactly, ratios included |
| `READERS_RISK` repair-log strip | **AGREE** | "Corrected 2026-07-29 / 23,855 s.e. was overstated" gone; **317 s.e.**, 1.6 s.e. single basin, acceptance 5.3–6.2%, R−1 = 1.011 all survive; re-learn diagnosis intact at `:141`/`:146` |
| `READERS_RISK` broken dyad row | **AGREE** | Detector returns clean on this file |
| "Do not kill" operator voice | **AGREE** | Independent sweep: **0** hits corpus-wide |
| `BIBLIOGRAPHY.md` Karsch P-048 | **AGREE-IF** | Withdrawal correct, arithmetic preserved (2.2599 meV, +0.44%, null 0.34506), clause 4 named — **IF:** it keeps the "0.22% framing withdrawn" D2 voice blue stripped from `lattice_note` and `cosmological_constant` in the same pass. Inconsistent, not wrong |
| `_CANONICAL_VALUES.md` ε-blind row | **AGREE** | "corrected 2026-07-28" gone; σ_c ≤ 0.0115 spacing, 0.97σ, σ_c ≤ 0.0037, #126 preserved |
| `v5_five_verdict` "Status: COMPLETE" | **AGREE** | → "document-job COMPLETE" + exploratory fence; no physics grade invented |
| `MATH_SPINE`, `DERIVATION_HUNT`, `DEPENDENCY_TREE` | **DISAGREE on the file** | Each cure correct **where made**; each file retains a worse defect elsewhere (§2a, §2b, §2e, §2g) |
| `THE_AMPLITUDE` = LEAVE | **DISAGREE** | §2c f̄ row |

**Errors inside blue's own package** (agent 4, red-verified): `BATCH_GIANTS:49` grades the stale-chain
log LEAVE on a claim supported by neither the log nor the file; `BATCH_GIANTS:91` "Authority held"
quotes the **stale** 08-04 numbers; `CURES.md:35-36` files `lattice_note` and `koide_relation` as "not
cured" while the working tree carries real edits to both.

---

## 5. The grep staging is not fit to certify a clean — and red relied on it too

Agent 4 audited `logs/*.txt`. **Three of six staged greps produce false cleans by pattern:**

- `grep_stale_chain.txt` hunts `(was …` was-trails and returned **one** unrelated hit. It never looks for `R−1`, `@N=`, `×stop`, `in burn-in`, `live`. At staging time **11 forward-facing files carried the superseded 08-04 triple while 5 carried the current one** — the corpus held two contradicting "current" stamps and the log saw none of it.
- `grep_external_win.txt` — **100% false positives**: all three "hits" are the substring `doi` inside the word **doing**. Zero real coverage.
- `grep_page_claim.txt` — substring `complet*`; 13/13 hits are prose or protective forbid-column text; misses bare status stamps entirely, including the one site blue cured.

Two more (`grep_repair_log`, `grep_022`) are adequate by pattern but **scoped to exclude the
forward-facing corpus** — every file blue cured for the 0.22% class was outside that grep's scope.
`grep_editor_instr` is scoped out *and* prints its four hits twice. `claude_red_check12.log` is **0
bytes**.

**The cures that landed this pass landed because blue read files line-aware, not because the staging
found anything.** Red records that in blue's favour.

**Red's own §-earlier "clean" verdicts were made the same bad way** and are withdrawn where §2a and
§2g contradict them. What survives independent re-testing:

| class | red's re-tested verdict |
|---|---|
| **EXTERNAL WIN without DOI** | **CLEAN.** All sites read "ARITHMETIC VERIFIED (internal); EXTERNAL WIN PENDING (no DOI)". supertrace **SHIPPED** is backed by a real DOI, **`10.5281/zenodo.21763188`**, verified in `papers/README.md`, `papers/supertrace-note/README.md`, `arXivReady/README.md:12`. Confirmed independently by agents 1 and 4 |
| **false page COMPLETE** | **CLEAN.** No bare COMPLETE; `page_curve_claimed: false` at all 10 sites; files carry "**Non-claims:** no physics COMPLETE from this file alone" |
| **marker-class editor instructions** (`WHOSE_TURN`, `@FROM:`, `>>BLUE`, `TODO`…) | **CLEAN — and this one is a real clean**, not a bad-pattern clean: agent 4 proved the pattern fires elsewhere in the tree (`_ARXIV_READINESS.md:1388`, `_AUDIT_LEDGER.md:5855`) before trusting the zero |
| **repair-log** | **NOT CLEAN** — §2a, verdict withdrawn |
| **0.22% executable** | **NOT CLEAN** — §2g, one residual |

Blue's three 0.22% *exclusions* were re-adjudicated by red and are **correct**:
`INDEPENDENCE_AUDIT:34` and `hierarchy_problem:967` are the **d = 3 vs ρ_Λ-implied 2.993** consistency
(0.23% ≈ 0.22%, and ρ ∝ d² is why it maps to the floor's 0.44%) — unrelated to the lattice rule;
`PREREGISTERED:1480` sits *inside* the not-executable argument.

---

## 6. Process note — the corpus was edited underneath the audit

Between 11:09 and 11:14 MDT at least eight files in agent 1's slice were rewritten mid-read
(mtimes + same-grep-different-text four minutes apart). Agent 1 recorded **12 found-then-cured**
defects verbatim rather than dropping them, which is correct auditor behaviour. Red notes the
consequence plainly: **this pass's cures and the prior round's are now layered into one unstaged
diff and are no longer separable by `git diff`** (28 modified `.md` under `docs/`, 322 insertions /
343 deletions, net-negative — consistent with narration removal). Red has committed nothing.

---

## 7. Coverage honesty

**Red personally verified:** chain ground truth at `chains/` + `ps` + the booking script; all 8 table
defects at render; the f̄ contradiction across four files; the 0.449%/0.25% resolution and its
arithmetic; the `MATH_SPINE:762` dangling reference at the diff; every cure in §4 at the diff; every
re-tested class in §5; and spot-verification of agent 1's and agent 4's top findings at the file
before adopting any of them — including **one correction to agent 4** (§2b).

**Not personally read line-by-line by red:** the full 62 shelf + 45 exploratory + 95 working-log
files. Delegated to four subagents (`SUBAGENTS_USED.md`). Detector classes (tables, empty residuals)
**are** corpus-wide by construction.

**Known coverage hole, stated:** `PRTOE_FAILURES_LEDGER.md` — agent 1 read ~1,090 of 5,869 lines
(~19%). **Lines 381–2699 and 3040–5499 are UNAUDITED** by line-read; grep-only there, and this report
demonstrates three times that grep-only is not cleanliness.

**Second coverage hole, stated:** of the 45 exploratory files, agent 2 read **16 line-by-line** and
covered the other **25 by structural sweep only** — it explicitly declines to certify those clean,
and red does not certify them either.

**Third coverage hole, stated:** of 95 top-level working-log files, agent 3 read **66 in full**, 12
partial, and **17 grep-swept only** (named individually in its report). Those 17 are not certified.

**Not claimed:** that the docs tree is defect-free; that check-12 is COMPLETE; any physics grade.
**`#94` / docket `#149` stays OPEN.** Two things nobody verified: the Zenodo DOI's **external**
resolution (no network was used — it is recorded at ≥15 sites in-corpus, which is why class 5 is not
a finding), and current bbnfix acceptance (launchlogs stalled, §2j).

*NO FABRICATIONS. Verified at the file, at the diff, and at the render. Failures stay in the ledger.*
