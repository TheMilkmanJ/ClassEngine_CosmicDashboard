# Story-grade elevation & triage rule (owner 2026-08-03)

**NO FABRICATIONS.** Elevating a file does **not** mean inventing derivations, fake
closes of OPEN residuals, or packaging inflation. It means making the document’s
*discipline* honest and non-story: every claim graded, evidenced, or explicitly OPEN.

Applies to: all `docs/PRTOE_*.md`, `docs/exploratory/`, and any future audience file.
Does **not** invent new physics to “finish” a story.

---

## 1. What “above story-grade” means

A file is **above story-grade** when **all** of the following hold:

| # | Requirement |
|---|---|
| A | **Claims ledger** (or equivalent table): each load-bearing claim has Grade + Evidence path + Residual |
| B | **No smuggled discovery**: literature/standard formulas cited; content boundary if null-hardened only |
| C | **OPEN locked**: anything not derived stays OPEN with a named kill or blocker — not soft-sold as done |
| D | **No “almost” bookings** while machine/theory gates fail |

**Elevation methods (cheap → hard):**

1. **Discipline elevation** — add claims ledger, non-claims, provenance, fence selected-frame language (desk; no new physics).
2. **Null-hardening** — code that enforces a *registered* formula under stated assumptions (not discovery).
3. **Machine/theory paydown** — real compute or derivation named in blocker; then re-grade.

Discipline elevation alone is enough to leave pure “story voice” if the claims are
honestly graded as **interpretation / story / OPEN**. That is still *above story-grade
discipline* even when the *physics grade* remains story.

---

## 2. Grades inside a claims ledger

| Grade | Meaning |
|---|---|
| **null-hardened** | Code or arithmetic enforces a registered formula; not a derivation of foundations |
| **derived** | Follows from named premises already in the corpus (cite premise paths) |
| **derived-conditional** | Derivation holds only under named conditionals (list them in Residual) |
| **complete-conditional** | Document *job* finished for the claims it owns at the grades in its ledger; every conditional is a Residual cell — **not** a free “COMPLETE” sticker |
| **registered null** | Model is forbidden from claiming credit if X appears |
| **machine-backed** | Number from named chain/script/artifact path on disk |
| **estimate** | Order-of-magnitude or scaling argument; not exact derivation |
| **interpretation** | Ontology / vocabulary seating; no new number |
| **story** | Coherent narrative assembly; not a derivation — **forbidden as final physics grade on shelf** after PASS3; convert to OPEN-BLOCKED or map-assembly |
| **map-assembly** | File is a map/spine assembling graded children; not itself a derivation |
| **candidate** | Motivated identification; not closed |
| **OPEN** | Not closed; residual named |
| **OPEN-BLOCKED** | OPEN *and* the blocker is named (see §3) |
| **failed / retired** | Route or claim **dead**; Residual **must** cite a Failures Ledger row or docket kill |
| **provisional** | Still pending named referees; **not** failed; must not use hybrid `failed/provisional-dead` |

| **registered** | Umbrella for registered null / bet / kill / candidate on predictions surface — prefer specific subtype when known |
| **registered kill** | Named kill condition on a registered object |
| **registered bet** | Timestamped prediction bet (points at predictions register) |
| **honest constraint / fence / scope-limit** | Explicit non-claim or jurisdiction fence (not a physics win) |
| **derived-from-recorded** | Follows from another corpus file already graded derived (cite that file) |
| **meta** | Document-about-documents (pointer, inventory, process) |
| **adopted** | Standard literature / GR fact cited, not re-derived |
| **paid** | Named residual paid by script/report this session (prefer machine-backed when path exists) |
| **framework** | Structural seating of the medium framework (near interpretation) |
| **awaiting** | Explicit wait on external/machine input (prefer OPEN-BLOCKED) |
| **back-solved** | Arithmetic closes given a target; forward derivation still OPEN (cite both) |
| **adverse-leaning candidate** | Candidate with known adverse tension (not a win) |

**Closed grade set:** only the labels in this table (amended 2026-08-03 C2 cure — recurring honest families admitted with one-line defs). Inventing *new* hybrid grades outside this table is a process defect. Prefer the most specific label.

**Smuggle ban:** A file may **never** mark physics-grade **COMPLETE** solely because discipline is above-story. `_FILE_COMPLETION_STATUS.md` updates **must** keep the split: document job status ≠ physics ceiling.

---

## 3. Triage when a file cannot go above story-grade *physics*

Ask in order:

### Step 1 — Can discipline elevation work?

If yes → add claims ledger + non-claims + banner; **keep location**; mark
`discipline: above-story` even if physics rows stay `story` / `OPEN`.

### Step 2 — Is it **BLOCKED**?

There is a **named** missing ingredient such that *if paid*, elevation becomes possible:

| Blocker class | Examples |
|---|---|
| **OPEN-MACHINE** | MCMC R−1, sim, four-branch production, Page-curve dynamics |
| **OPEN-THEORY** | Bounce H_re, Koide node, ω_J forward micro, RM formula |
| **WATCH-EXTERNAL** | Fairbank, BipoSH data, LUNA, stranger recompute |

**Action:** keep on shelf (or exploratory if not shelf-worthy); ledger row
`OPEN-BLOCKED` with **blocker ID + path**; do **not** rehome to Failures.

### Step 3 — Is it **just a story**?

No named path to a killable claim without inventing physics. Narrative / metaphor /
assembly only.

**Action — choose destination:**

| Destination | When |
|---|---|
| **`docs/exploratory/`** | Still useful as orientation, genealogy, or research brainstorm; **not retracted**; work may continue |
| **`docs/PRTOE_FAILURES_LEDGER.md`** | Claim was tested and **failed**, route **retired**, prediction **lost**, or false statement that must not live as living claim |
| **`docs/archive/`** | Superseded lineage already replaced; historical only |
| **Stay shelf with story banner** | Load-bearing *map* whose only honest grade is story **and** reader banner already forbids derivation reading — then discipline-elevate in place. (Example class: cyclic-genesis *assembly* — triage is decided by evidence, not hardcoded.) |

**Never delete.** Categorize (owner tribunal rule).

### Step 3b — Row-level Failures (Claude red 2026-08-03)

A single **row** can be `failed/retired` while the file stays shelf or exploratory.
That row’s Residual **must** name a Failures Ledger entry (or docket kill ID).
Do **not** invent hybrid grades like `failed/provisional-dead`. Choose one:

| Situation | Grade |
|---|---|
| Dead amplitude / killed route | **failed/retired** + Failures pointer |
| Still pending referees / escape hatch open | **provisional** or **OPEN-BLOCKED** |
| Structure real, amplitude inaccessible | **story** + provisional Residual — not “failed” |

### Step 4 — Mixed files

Split in the ledger: rows that are machine-backed stay; story rows marked `story`;
OPEN-BLOCKED rows name the paydown. Do not move the whole file to Failures because
one paragraph is story.

---

## 4. Failures vs exploratory (sharp edge)

| | **Failures Ledger** | **exploratory/** |
|---|---|---|
| Meaning | Graveyard: lost bets, killed routes, forced-fit losses | Living neighborhood: unlinked from public shelf; not retired |
| Reader | “This died or was wrong” | “This is not the testable core; work may continue” |
| Predictions | Retired rows leave predictions register → Failures | Usually never on predictions surface |
| Example | PolyChord nested run ended without checkpoint; wrong D/H exponent fixed | wormholes framing; math_story map; quantum trio before null-hardening |

**Predictions hygiene (owner):** repair/fail/amend → Failures, not scars on
`PRTOE_PREREGISTERED_PREDICTIONS.md`. Red does not attack that recategorization.

---

## 5. Inventory process (how we grade the corpus)

1. For each `docs/PRTOE_*.md` and each `docs/exploratory/*.md`:
   - assign **discipline grade**: `above-story` | `story-voice` | `ledger/history`
   - assign **physics ceiling**: max grade of load-bearing claims
   - assign **triage**: `elevate-in-place` | `blocked` | `exploratory-ok` | `failures-candidate` | `archive-ok`
2. Record in `docs/working_logs/_runs/story_grade_triage_20260803/INVENTORY.md`
3. Apply elevation or rehome **only with evidence**; tribunal red/ref on moves that touch shelf claims
4. Update `_FILE_COMPLETION_STATUS.md` when status changes

---

## 6. Forbidden (NO FABRICATIONS)

- Inventing numbers or derivations to force “above story”
- Closing Born, Page *curve*, bounce H_re, ω_J forward, Koide node without record
- Moving a living OPEN claim to Failures because it is hard
- Calling discipline elevation a physics win or 4/10 grade bump
- Packaging story arcs as external validation

---

## 7. Template — claims ledger footer

```markdown
## Claims ledger & discipline (YYYY-MM-DD) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | … | derived / null-hardened / story / OPEN-BLOCKED | path or § | … |

**Non-claims:** …
**Triage:** elevate-in-place | blocked (name) | exploratory | failures (row)
```

---

## 8. Owner standing links

- NO FABRICATIONS: `docs/working_logs/_runs/quantum_null_hardening_20260803/NO_FABRICATION.md`
- File completion tags: `docs/working_logs/_FILE_COMPLETION_STATUS.md`
- Failures: `docs/PRTOE_FAILURES_LEDGER.md`
- Exploratory policy: `docs/exploratory/README.md`
- Tribunal: `ForGrok&Claude.md`
