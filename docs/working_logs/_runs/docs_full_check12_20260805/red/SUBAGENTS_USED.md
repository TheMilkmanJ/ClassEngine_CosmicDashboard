# SUBAGENTS_USED — RED, docs full check-12 (2026-08-05)

**Seat:** Claude RED (CLI). Four subagents dispatched **in parallel, in a single message**, per the
owner's instruction ("at least 4 parallel"). All read-only with respect to `chains/`; none was
permitted to fix anything — red's seat reports, blue cures.

---

## Roster

| # | agent | slice | status | report |
|---|---|---|---|---|
| 1 | shelf sample + giants | 10 living `docs/PRTOE_*.md` read in full + the 4 giants (PREREGISTERED 2229 ln, DERIVATION_HUNT 1299, MATH_SPINE 1017, FAILURES_LEDGER 5869) | **complete** — 716 s, 58 tool calls | `AGENT1_SHELF_GIANTS.md` |
| 2 | `docs/exploratory/` | all 45 files | **complete** — 859 s, 60 tool calls | `AGENT2_EXPLORATORY.md` |
| 3 | `docs/working_logs/` (excl `_runs/`) + `BIBLIOGRAPHY.md` | 95 files + bibliography at full forward-facing bar | **complete** — 1026 s, 124 tool calls | `AGENT3_WORKINGLOGS_BIB.md` |
| 4 | verify blue's cures + audit the grep staging | `batches/`, `cures/`, `logs/*.txt`, working tree | **complete** — 700 s, 75 tool calls | `AGENT4_CURE_VERIFY.md` |

Each was given the nine defect classes, the standing facts (P-2026-048 withdrawal, the BBN-ε
"PENDING (no DOI)" correct phrasing, the ledger's history charter, the conjunctive booking gate), and
one standing instruction: **a grep that prints nothing proves nothing — read the file.**

---

## What each contributed that red did not have

| agent | unique contribution |
|---|---|
| **1** | The `MATH_SPINE:158` **±0.25% vs ±0.449%** contradiction — the only finding capable of moving a physics verdict, since P-048's sky-limited ruling rests on 0.98σ. Also the 6 repair-log survivors that **falsify red's own prior "clean corpus-wide" commit**, the `FAILURES_LEDGER:141/159` "three independent confirmations" false-as-current, and `DERIVATION_HUNT:1287`. |
| **2** | The `exploratory/README.md` **broken acceptance-test claim** ("883 links … Zero unresolved" — false, 13 sites), `fairbank_note_HOLD`'s shareable-vs-superseded contradiction plus its "## Before send" list, **five more** fork-as-executable sites, and the unflagged **65×** `df_amp/dθ₀` discrepancy. |
| **3** | The **operational risk** — `_PROJECT_FINISH_ROADMAP.md:161-165`'s **183×-stale** routeD surgery trigger, which a skimming reader could act on against a converging chain. Also `_ARXIV_READINESS.md`'s page count **falsified at the artifact** (PDF is 7 pp, not 6), `census_democracy_note.md` being wholly a **withdrawn** argument with no banner, `_master_computes.md`'s dead-chain and **PolyChord** claims, BIBLIOGRAPHY's **9** coverage gaps, and the observation that **both bbnfix launchlogs stalled 08-02** so acceptance is unreadable. |
| **4** | The **grep-staging adequacy audit** — three of six staged greps produce false cleans; `grep_external_win` matched the substring `doi` inside the word *doing* and found nothing real. Also the **cure-induced dangling reference** at `MATH_SPINE:762`, the sharper diagnosis of the `DERIVATION_HUNT:159` orphan (it is the ε-table's stranded third factor), and the three stale-stamp sites blue missed. |

## What red did itself, not delegated

Chain ground truth from `chains/` + `ps` + `book_bbnfix_when_ready.py`; the two read-only detectors in
this package (`orphan_tables.py`, `show_split.py`, `empty_residual.py`) and all 8 broken-table
findings proven **at render**; the f̄ cross-file overclaim; the **resolution** of agent 1's
0.25%/0.449% finding (ρ_Λ ∝ h²Ω_Λ; the ~1% reading drops h²; 1.80% reproduces to 0.01%); adjudication
of the three 0.22% non-instances; and diff-level verification of every blue cure.

---

## Red did not take any agent at face value

Every finding adopted into `MASTER_RED.md` was re-opened at the file by red before adoption. Two
corrections resulted:

1. **Agent 4 was wrong** to discount the `|Ψ|²` table breaks as escaped-pipe false positives.
   `grep -c '\|Ψ'` on `fingerprint_lattice.md:32` returns **0** escaped matches and the render proof
   splits the row into 7 cells against a 3-column header. Sites stand.
2. **Agent 1 filed `MATH_SPINE:158` as an owner call.** Red resolved it instead — the arithmetic
   decides it, and no physics verdict moves.

Agent 2's `hierarchy_problem:967` reading **corrected red's own** in the useful direction: red had
cleared it as a non-instance of the 0.22% class (correct), agent 2 added that it remains a class-8
overclaim because the agreement sits inside its own ±0.449% error bar. Adopted.

---

## Cost and honesty

~1.27M subagent tokens across four agents (317 tool calls, ~48 min wall-clock in parallel).
**Coverage is not complete and is not claimed to be:** `FAILURES_LEDGER.md` lines 381–2699 and
3040–5499 are unaudited by line-read; **25 of 45** exploratory files were covered by structural sweep
only (agent 2 explicitly declines to certify those clean); **17 of 95** working-log files were
grep-swept only. **#94 / docket #149 stays OPEN.**

*NO FABRICATIONS.*
