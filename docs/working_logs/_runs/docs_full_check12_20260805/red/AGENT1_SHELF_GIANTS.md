# RED check-12 — Agent 1: living shelf sample + the four giants

**Auditor:** RED (adversarial). **Date:** 2026-08-05. **Read window:** 11:08–11:20 MDT.
**Mode:** line-by-line read of the assigned slice + full-file targeted sweeps for all nine defect
classes. I do not fix; I report.

> ## ⚠ READ THIS FIRST — the corpus was edited *underneath this audit*
>
> Between 11:09 and 11:14 MDT, while I was mid-read, at least eight files in my slice were
> rewritten by another seat. Verified by `stat` mtimes (`PRTOE_READERS_RISK.md`,
> `PRTOE_REFEREE_CALENDAR.md`, `PRTOE_honest_status.md` → 2026-08-05 11:11:04;
> `PRTOE_cosmological_constant.md` → 11:11:25; `PRTOE_koide_relation.md` → 11:10:38) and by
> re-running the same greps four minutes apart and getting different text at the same line
> numbers.
>
> **Consequence for this report.** Several defects I read verbatim were *cured while I was
> reading them*. I report those separately as **FOUND-THEN-CURED**, with the exact text I read
> and the timestamp, because (a) a red report that silently drops a defect the seat happened to
> fix in the same minute is not an audit, and (b) the cures need independent verification against
> ground truth, which I have done and record below. Line numbers in the findings table are
> **as of 11:20 MDT** and were re-verified by grep after the edits landed.

---

## 0. Ground truth I established myself (machine state)

Read directly from `chains/` — not from any document:

| chain | N (progress) | R−1 last | timestamp | checkpoint | stop |
|---|---:|---:|---|---|---:|
| `cmp_lcdm_mnu_bbnfix` | 24858 | **0.047912** | 2026-08-05T04:55:58 | `converged: false`, `mpi_size: 3` | 0.05 |
| `dyad_mnu_bbnfix` | 24677 | **0.056889** | 2026-08-05T07:54:30 | — | 0.05 |
| `cmp_prtoe_routeD` | 6517 | **0.705291** | 2026-08-05T04:07:15 | — | 0.1 |

Sources: `chains/cmp_lcdm_mnu_bbnfix.progress` (18 rows), `chains/dyad_mnu_bbnfix.progress`
(18 rows), `chains/cmp_prtoe_routeD.progress` (5 rows),
`chains/cmp_lcdm_mnu_bbnfix.checkpoint`. Chain `.txt` mtimes 11:05–11:08 today confirm all three
are actively writing. Dead chains verified too: `cmp_prtoe_conv_desi.progress` last row
13.251101 @ 2026-07-22T11:06; `cmp_prtoe_zon_disp.progress` last 17.81287 @ 2026-07-22T09:37;
`cmp_prtoe_zon.progress` last 40.362246 @ 2026-07-12T01:10. The corpus's 13.25 / 17.81 / 40.36
rows are **accurate**.

Booking-card directory `docs/working_logs/_runs/bbnfix_booking_20260805_170213/` exists, so
`PRTOE_REFEREE_CALENDAR.md`'s currency citation is real.

---

## 1. FINDINGS TABLE (standing as of 11:20 MDT)

| file:line | class | verbatim quote | verdict |
|---|---|---|---|
| `docs/PRTOE_MATH_SPINE.md:762-766` | **1** repair-log doc history | *"(This sentence read "is the single decider" until 2026-07-29. The §7 header has carried a correction saying it "previously named it 'the single decider'" since 2026-07-28 — but the correction was written at the head of §7 and never applied to this line down in the addendum, so the retracted phrase stood for a day beneath its own retraction.)"* | **CONFIRMED** — pure edit history of the document narrated to the reader; no physics-claim grade is being reported. The single worst survivor of this class. |
| `docs/PRTOE_MATH_SPINE.md:364-365` | **1** | *"so no chain was ever the single decider — see the addendum, where that phrase has now actually been removed from the sentence carrying it."* | **CONFIRMED** — tells the reader what was deleted from another paragraph of the same file. (Also self-contradictory with :762, which says the phrase stood until 07-29.) Survived the prior grep sweeps because the phrase wraps across two lines. |
| `docs/PRTOE_MATH_SPINE.md:736-739` | **1** | *"Note the earlier gloss here — that a one-chain run "cannot yield a convergence statistic at all" — was **wrong and is corrected in §7**"* | **CONFIRMED** — "the earlier gloss *here*" is this document's own prior text. |
| `docs/PRTOE_PREREGISTERED_PREDICTIONS.md:410` | **1** | *"(This entry formerly demoted "c~1 derived" to "c~1 NATURAL" and booked the exact value as owed via UV threshold matching. That debt does not exist…)"* | **CONFIRMED** — and it violates the file's **own header policy** at :7-9: *"Repair narrative, amendments, and failed/withdrawn predictions are **rehomed** to PRTOE_FAILURES_LEDGER.md … so this file does not read as a fit-forcing repair log."* |
| `docs/PRTOE_PREREGISTERED_PREDICTIONS.md:1677-1692` | **1** + **2** | *"LABEL CORRECTION ONLY — the numbers stand, 2026-07-29 … **Withdrawn the same day it was raised:** an annotation here claimed a factor-2 fork … **That was my error** — it assumed the shift is ε·Θ…"* | **CONFIRMED** — repair narrative *and* first-person seat voice in the audience-facing registry. The identical text is **already** rehomed to `PRTOE_FAILURES_LEDGER.md:5698-5711` under "Rehomed in-entry strips", so this is a duplicate that the rehome pass failed to strip. |
| `docs/PRTOE_PREREGISTERED_PREDICTIONS.md:688-689` | **2** editor instruction | *"**Whether the tag itself should read OBJECT-OBSTRUCTED is an owner call** — I have not rewritten a pre-registration."* | **CONFIRMED** — a workflow question addressed to the owner/next seat, in the reader-facing registry. |
| `docs/PRTOE_cosmological_constant.md:557` | **1** | *"#### Correction to the line above, same day: the 1.33% was an underestimate"* | **CONFIRMED** — a section heading whose subject is this document's own earlier line, not a physics claim's grade. §§474-716 are a chronological edit diary ("as written in §4b" / "what was quoted" / "the note above concluded"). |
| `docs/PRTOE_FAILURES_LEDGER.md:141` | **8** overclaim, false-as-current | *"**The session has since run** — ξ is derived from the medium's own sector and now carries **three independent confirmations** (ξ = 402 AU returning 398 from m = 2.24×10⁻²⁰ eV, the Schive core radii, the superradiance band)"* | **CONFIRMED — flaggable under the ledger's special rule (outright false-as-current).** The same file retracts it at :5860 (*"the claim that … m … is 'confirmed three independent ways'"* — retired), `PRTOE_INDEPENDENCE_AUDIT.md:35` grades it *"Zero confirmations today — three commitments"*, and `PRTOE_MATH_SPINE.md:1014` lists it as a **Non-claim**. Two of the three named legs are the ones the corpus killed: ξ is definitionally circular and superradiance is an *exposure*. |
| `docs/PRTOE_FAILURES_LEDGER.md:159` | **8** overclaim, false-as-current | *"The dyad mass has since been **pinned three independent ways** at **2.24×10⁻²⁰ eV**"* | **CONFIRMED** — same withdrawn claim, second site, same file. |
| `docs/PRTOE_MATH_SPINE.md:158` | **8** overclaim / load-bearing numeric contradiction | *"a +0.44% OFFSET, i.e. **~1.8σ on the observational error** … ρ_Λ¼ **inherits ~0.25% from Ω_Λ's ~1%**"* | **CONFIRMED contradiction.** Every other surface uses **±0.449%** on ρ_Λ¼ (`lattice_note:12`, `READERS_RISK` (j), `REFEREE_CALENDAR:134` *"Planck's 1.80% on ρ_Λ quartered"*, `PREREGISTERED:1477`, `PREREGISTERED:443` ±0.48%) giving **~0.98σ**. This is not cosmetic: the **entire P-2026-048 "crown/null is sky-limited, clauses 2/3 not executable" ruling rests on 0.98σ.** At MATH_SPINE's 0.25% the separation is 1.8σ and the withdrawal's premise weakens. One of the two numbers is wrong and the corpus does not say which. |
| `docs/PRTOE_DERIVATION_HUNT.md:1287-1288` | **8** overclaim / **6**-adjacent | *"**Everything else in the corpus is derived, quantified, or dead with a documented autopsy.**"* | **CONFIRMED** — flatly contradicted by the corpus's own live board: Page Q6 **OPEN** (T8 = 0.113), bounce **OPEN-BLOCKED**, Koide Wilson-holonomy inputs **5/5 MISSING**, unitarized σσ **MISSING_INPUT**, void IGMF ×20 **OPEN**, absolute SI G **OPEN** (`PRTOE_honest_status.md:68-80`). Mitigation: the section is stamped 2026-07-18 and the file's freeze header says *"quote status from living topic files, not from dated rows here"* — but the sentence is unqualified. |
| `docs/PRTOE_PREREGISTERED_PREDICTIONS.md:1888-1896` | **3** stale chain | *"**Chain status (2026-07-28).** It still has not. The run stopped on 2026-07-20 at 21:39 with 363 accepted samples from 11,508 steps … its progress file carries only a header, so no convergence statistic was ever computed … **the adjudication is waiting on a chain that has failed three times**, and on the **single-core host** it runs at roughly thirty accepted samples an hour, so a converged posterior is not weeks away but months."* | **CONFIRMED false-as-current.** `cmp_prtoe_routeD` is live **right now** on **3 MPI ranks** with **5 progress rows** and R−1 descending 102.79 → 4.94 → 1.08 → **0.705291**. Every clause of that paragraph — stopped, no convergence statistic, header-only progress file, single-core — is false today. Partly self-cured 90 lines later at :1975-1977, but a reader hits the false paragraph first. |
| `docs/PRTOE_DERIVATION_HUNT.md:1279` | **4** 0.22%/fork as executable | *"\| T_c/√σ for SU(2), N_f = 3 \| the headline result's ±4.2% → a **0.44%-class prediction (the P-048 fork decided)** \| the lattice (external…)"* | **CONFIRMED (residual).** The open-surface table still sells the lattice as *deciding the fork*. The same file carries the withdrawal correctly at :305 and :327; this row was not swept. |
| `docs/PRTOE_INDEX.md:9` | **9** house jargon | *"Re-running exhausted stocked hunts (amplitude maps, suppression maps, **Θ densify**, **match-book under stocked forms**, **N6-from-absence**, **Wilson invent**, **page densify**, **supertrace-as-G**) is **closed as work**."* | **CONFIRMED.** Eight in-house coinages, none defined anywhere in `PRTOE_READERS_GUIDE.md`'s glossary or symbol table, on the **first shelf file an outside reader opens**. "stocked", "desk residual", "docket #182" join them. |
| `docs/PRTOE_FAILURES_LEDGER.md:5826` | **2** editor instruction (ledger — flaggable) | *"Rehomed for categorize-never-delete compliance after **Claude AUDIT AGREE-IF**."* | **CONFIRMED** — names an agent and an internal verdict class. Companion at :5841 *"**In-entry strip named:** In-entry strip (pass 1): P-2026-007 blockquote…"* is raw pass-bookkeeping. Reader-facing files must not name the seats. |
| `docs/PRTOE_MATH_SPINE.md:282-283` | **1** | *"(The 250–530 keV figure **this replaces** does not follow from the exact kernel over the stated range…)"* | **SUSPECT** — reads as edit history of this file rather than a claim-grade move; owner call. |
| `docs/PRTOE_honest_status.md:147-148` | **1** | *"(**This board's earlier** (d/2)α⁴m_e ≈ 2.17 meV, 0.97×, is the same structure with τ approximated as 1/3…)"* | **SUSPECT** — mitigated: the file is marked *"Private — internal candid self-assessment"* (:6) and self-grades LEDGER/HISTORY (:411). But it lives in `docs/PRTOE_*.md`. |
| `docs/PRTOE_honest_status.md:186-187` | **1** | *"the **2×10⁸ this board carried** was low"* | **SUSPECT** — same mitigation, same exposure. |
| `docs/PRTOE_MATH_SPINE.md:356-362` and `:733-735` | **3** stale chain adjective | *"Route-D runs on its fifth launch … **It is in burn-in**"* / *"(2026-08-01: three MPI ranks … **in burn-in**…)"* | **SUSPECT** — date-stamped 2026-08-02 / 08-01, but routeD has written four convergence statistics since and sits at 7× stop, not burn-in. Both point the reader at `PRTOE_CHAIN_TABLES.md` for the live number, which mitigates. |
| `docs/PRTOE_lattice_note.md:12` | **8** overclaim | *"The program's T_c = 177.10 keV (τ = ½ln2) is the **derived** lepton-side anchor behind 0.34657"* | **SUSPECT** — the same object is **candidate-grade** in `READERS_RISK` §3(a) (*"rests on one hypothesis … and is candidate-grade"*) and **derived-conditional** in `cosmological_constant`'s ledger row 2. The note's own claims ledger row 2 grades it *"registered null / bet"*. "Derived" unqualified is the strongest word used anywhere for it, in the one file **approved for outside circulation**. |
| `docs/PRTOE_FAILURES_LEDGER.md:5522-5535` | **4** | *"confirming or killing requires σ ≤ 0.0008, which is 0.22% … **What the test actually requires:** a lattice determination … to better than **0.44%**."* | **SUSPECT** — prescriptive-voice statement of the withdrawn decision rule. Mitigated: it is a **Rehomed** dated block (ANN-2026-026, 2026-07-19) with a "Rehome reason" header, i.e. history, which the ledger is entitled to keep. Flagged only because it is the last prescriptive "0.22%" in the corpus. |
| `docs/PRTOE_FAILURES_LEDGER.md:5790-5802` | **4** | *"**Adjudication rule, sealed now:** a determination consistent with 0.34657 while excluding 0.34506 at ≥2σ selects the kernel…"* | **SUSPECT** — same shape (P-048 addendum, rehomed, 2026-07-18), same mitigation. |
| `docs/PRTOE_INDEPENDENCE_AUDIT.md:62, 66, 87` | **9** | *"**R4-additivity-neck** (2026-08-03): confirmed underived axiom"* · *"which is the standing **check-12 sweep**, still in progress"* · *"Silent shared premises possible; **check-12** ongoing"* | **SUSPECT** — "check-12" and "R4-…-neck" are process names, undefined for a reader. |
| `docs/PRTOE_CHAIN_TABLES.md:3` and `docs/PRTOE_honest_status.md:248` | **9** / **2** | *"**ForJustin/12 item 5(b)'s instrument** (`scripts/make_getdist_tables.py`)"* · *"Two days of error-counting are filed at `ForJustin/13`"* | **SUSPECT** — internal correspondence-folder references as provenance in shelf files. |
| `docs/PRTOE_honest_status.md:63, 75` | **9** | *"Stocked-desk **thrash** exhausted"* · *"Forward A_ωJ / seat \| **EMPTY_CORPUS_SEAT · Charge A holds**"* | **SUSPECT** — undefined coinages. |
| `docs/PRTOE_INDEX.md:15` | **9** | *"`page_curve_claimed: false`; no CANDIDATE; **F1 ON**."* | **SUSPECT** — "F1" is an undefined internal gate label. |
| `docs/PRTOE_DERIVATION_HUNT.md:208` | **2** | *"…noting that the finite-μ Fermi surface *"is what **I** introduced… It is not recorded anywhere else,"*"* | **SUSPECT** — an attributed quotation, so defensible, but it puts a first-person editor voice into a forward-facing file. |
| `docs/PRTOE_READERS_RISK.md` §3 list labels | *(structural, outside the 9 classes)* | items run **(a) (b) (c) (d) (e) (g) (h) (f) (i) (j) (k)** — `(g)` at §3 precedes `(f)`, which appears two items later | **CONFIRMED (cosmetic)** — the list is mis-lettered; a referee citing "§3(f)" will land in the wrong place. |

---

## 2. FOUND-THEN-CURED during this audit (verbatim, with timestamps)

These were **real defects when I read them**. Another seat fixed them between 11:09 and 11:14.
I record them because the cures are 3 minutes old and unverified by anyone but me — and because
the class-3 failure was **corpus-wide**, which is a process signal, not a typo.

### 2a. Class 3 — stale R−1 as current, on six shelf surfaces simultaneously

At **11:09–11:11 MDT** every one of these carried the **2026-08-04** numbers as the live gate:

- `PRTOE_INDEX.md:13` — *"lcdm R−1 **0.071122** (N=21886, t=2026-08-04T13:01:13; **1.42×** stop), dyad R−1 **0.072286** (N=21867…) … Route-D live R−1 **4.941933**@N=3290 (~**49.4×** stop 0.1)"*
- `PRTOE_honest_status.md:28-36` — same three, in prose and in a table
- `PRTOE_READERS_RISK.md:4-6, 166-169, 328-337, 356, 388` — same three, in five places
- `PRTOE_READERS_GUIDE.md:10-12` — same, labelled **"(CURRENT: …)"**
- `PRTOE_CHAIN_TABLES.md:27-37, 52-54, 162-163` — same, in the file the other five name as **authority**
- `PRTOE_DOMAIN_COVERAGE.md:21` — same

Ground truth at that moment: lcdm **0.047912** (below stop), dyad **0.056889**, routeD
**0.705291**. The routeD error was the largest: **4.941933 quoted against 0.705291 actual — a
factor of 7**, and the doc's "~49.4× stop" was actually ~7.05×. The lcdm leg had crossed *below*
its 0.05 stop and every surface still said "1.42× stop".

**The corpus contained its own indictment at the time.** `PRTOE_REFEREE_CALENDAR.md:11-30`
already carried a **"Live read 2026-08-05"** block with the exact correct numbers — so one shelf
file was current and six were a day stale, including the designated authority.
`PRTOE_honest_status.md:82-84` states the governing rule: *"Any surface still carrying **2026-08-02**
live R−1 numbers as if current … is stale."* The same rule fired one date later and nobody ran it.

**Verified cured at 11:14 MDT.** All six now carry 0.047912 / 0.056889 / 0.705291 with the
correct timestamps, matching my ground truth exactly.

### 2b. Class 7 — orphan/misaligned table row (`PRTOE_READERS_RISK.md`, the §4 chain table)

Read verbatim at 11:09:

```
| chain | last recorded R−1 | N (progress) | `converged` | live? | note |
|---|---|---:|---|---|---|
| `dyad_mnu_bbnfix` | 21867 | **0.072286** | 0.05 | **false** | **NO** |
```

The cell count matched the header but the **semantics did not**: the row had been pasted from
`PRTOE_honest_status.md`'s table (`chain | N | R−1 | stop | converged | bookable`), so it rendered
as *"last recorded R−1 = 21867, N = 0.072286, converged = 0.05, live? = false"*. The very next row
(`cmp_lcdm_mnu_bbnfix`) used the correct column order, so the two rows disagreed with each other
inside one table. **Verified cured at 11:20** (now `READERS_RISK.md:316`, correctly ordered).

### 2c. Class 4 — 0.22% presented as a live decision rule

At **11:09** these carried the withdrawn framing with no caveat:

- `PRTOE_cosmological_constant.md:21` — *"for SU(2) with N_f = 3 **decides it** (P-2026-048), and **it must reach 0.22% precision to tell the** …"*
- `PRTOE_cosmological_constant.md:124` — *"lattice T_c/√σ for SU(2), N_f = 3 **decides it** (P-2026-048), and **must reach 0.22% precision to tell** …"*
- `PRTOE_koide_relation.md:242` — *"advance — separating the two takes **0.22% precision**). The same number then **decides** whether the …"*
- `PRTOE_REFEREE_CALENDAR.md:141` — *"**Discriminating needs 0.22% on T_c/√σ** (the registered rule: σ ≤ 0.0008 with the rival excluded at ≥2σ)"* — this one *did* carry "the decision rule cannot currently be executed", but justified it by the ±5.7% registered tolerance rather than by the sky limit, and never named the withdrawal.

**Verified cured at 11:11–11:12.** `0.22%` is now entirely absent from `cosmological_constant.md`;
`koide_relation.md:242` reads *"**0.22% framing withdrawn**); **clause 4** is the live…"*;
`REFEREE_CALENDAR.md:142` reads *"**0.22% lattice-discrimination framing withdrawn** (P-048 living currency…)"*.

### 2d. Class 3 — GetDist GR values quoted in reversed order

`PRTOE_INDEX.md:13` at 11:09: *"GetDist GR **~0.086 / ~0.07** diagnostic only"*, following a
sentence that lists lcdm then dyad — i.e. it read lcdm = 0.086, dyad = 0.07. The authority
(`PRTOE_CHAIN_TABLES.md:43-44` diagnostic table) has **dyad 0.0857, lcdm 0.0721**, and
`honest_status.md:38` + `READERS_RISK.md:340` both state *lcdm ~0.07, dyad ~0.086*. INDEX was
backwards or, at best, unlabelled and ambiguous. **Cured** — INDEX now says only
*"GetDist GR diagnostic only"*.

---

## 3. Coverage ledger — exactly what I read

| file | lines | read | method |
|---|---:|---|---|
| `docs/PRTOE_INDEX.md` | 136 | **1–136 (100%)** | full Read; line 13 re-Read post-cure |
| `docs/PRTOE_honest_status.md` | 415 | **1–415 (100%)** | full Read; 143–150 re-Read post-cure |
| `docs/PRTOE_READERS_RISK.md` | 395→~380 | **1–395 (100%)** of the 11:09 version; **308–325 re-Read** post-cure | full Read + targeted re-verify |
| `docs/PRTOE_READERS_GUIDE.md` | 141 | **1–141 (100%)** | full Read |
| `docs/PRTOE_lattice_note.md` | 142 | **1–142 (100%)** | full Read |
| `docs/PRTOE_cosmological_constant.md` | 806→809 | **1–420 + 420–809 (100%)** | two Reads |
| `docs/PRTOE_DOMAIN_COVERAGE.md` | 105 | **1–105 (100%)** | full Read |
| `docs/PRTOE_CHAIN_TABLES.md` | 170 | **1–170 (100%)** | full Read |
| `docs/PRTOE_REFEREE_CALENDAR.md` | 162→164 | **1–164 (100%)** | full Read; :83 re-verified post-cure |
| `docs/PRTOE_INDEPENDENCE_AUDIT.md` | 92 | **1–92 (100%)** | full Read |
| `docs/PRTOE_PREREGISTERED_PREDICTIONS.md` | 2218→2229 | **1–450, 450–1009, 1010–1569, 1570–2229 (100%, contiguous)** | four Reads |
| `docs/PRTOE_DERIVATION_HUNT.md` | 1295→1299 | **1–450, 450–899, 900–1299 (100%, contiguous)** | three Reads |
| `docs/PRTOE_MATH_SPINE.md` | 1014→1017 | **1–520, 520–1019 (100%, contiguous)** | two Reads; :355–368 re-Read |
| `docs/PRTOE_FAILURES_LEDGER.md` | 5869 | **1–380, 2700–3039, 5500–5869 read = ~1,090 lines ≈ 19%** | three Reads + **100% grep coverage** for all nine classes |
| ground truth | — | `chains/*.progress` ×6, `cmp_lcdm_mnu_bbnfix.checkpoint`, chain `.txt` mtimes, `docs/working_logs/_runs/bbnfix_booking_20260805_*` | Read + ls |
| DOI verification | — | `docs/arXivReady/README.md`, `docs/working_logs/_ARXIV_READINESS.md`, `_ARXIV_CANDIDACY.md` | grep + read |

### What I did NOT cover — stated plainly

1. **`PRTOE_FAILURES_LEDGER.md` lines 381–2699 and 3040–5499 (~4,780 lines, ≈81% of the file) were
   not read line by line.** The file's long lines put a 1,500-line Read at 58k tokens, over the
   tool ceiling. I covered it with full-file `grep` sweeps for every one of the nine defect
   classes (editor-instruction markers, repair-log markers, `0.22%`, `three independent`,
   `pinned three`, chain names, DOI/Zenodo, COMPLETE) and read the head, a 340-line middle sample
   and the whole tail. **A grep miss is not evidence of cleanliness** — my own sweeps proved that
   twice (a case-sensitivity miss hid `MATH_SPINE:762`; a line-wrap miss hid `MATH_SPINE:364`).
   **Treat the ledger's middle as UNAUDITED.**
2. I did not read `PRTOE_koide_relation.md`, `BIBLIOGRAPHY.md`, `PRTOE_THREE_EQUATIONS.md`,
   `PRTOE_DEPENDENCY_TREE.md` or `exploratory/PRTOE_hierarchy_problem.md` in full — only the
   specific lines named in my brief as class-4 suspects, which I read in context.
3. I did not verify any physics arithmetic beyond the σ-ratio contradiction reported above.
4. **Everything in this report is a snapshot of a moving file set.** Files in the slice were being
   rewritten during the audit; anything I mark CONFIRMED could be cured minutes after this is
   written, and anything I mark clean could regress.

---

## 4. CLEAN CLAIMS — with exactly what I read to establish each

**Class 5 (EXTERNAL WIN without DOI) — CLEAN across the slice.**
- The supertrace-note DOI **does** exist and **is** recorded: `docs/arXivReady/README.md:12`
  (*"SHIPPED — Zenodo DOI 10.5281/zenodo.21763188"*), `docs/working_logs/_ARXIV_READINESS.md:39`
  (*"Published 2026-08-02: Zenodo DOI 10.5281/zenodo.21763188 (PDF + source tarball, CC BY 4.0)"*),
  `_ARXIV_CANDIDACY.md:69,344`. So `PRTOE_INDEX.md:37`'s *"supertrace-note **SHIPPED** Zenodo"* is
  **earned**.
- Every BBN-ε site I read carries the correct fence: `PRTOE_INDEX.md:14,37`, `honest_status.md:44`,
  `READERS_GUIDE.md:13-14`, `READERS_RISK.md` claims-ledger row 8 — all read
  *"ARITHMETIC VERIFIED (internal)"* + *"EXTERNAL WIN PENDING (no DOI)"*. `docs/arXivReady/README.md:16`
  matches. **No site claims it as a public win.** I found no paper called shipped/posted without a DOI.

**Class 4 (0.22% as executable) — CLEAN at every site I was asked to adjudicate, as of 11:20.**
Read in context and confirmed carrying the withdrawal: `lattice_note:8, 12, 95, 134` ·
`READERS_RISK:98, 236` · `MATH_SPINE:34-36` · `THREE_EQUATIONS:17` · `DEPENDENCY_TREE:68` ·
`BIBLIOGRAPHY:257` (*"crown/null discrimination is **sky-limited** … **0.22% lattice framing
withdrawn**"* — this suspect was **already clean before the cure wave**) ·
`REFEREE_CALENDAR:142` · `PREREGISTERED:1476-1515` (clauses 2/3 explicitly labelled
*"Historical (sky-limited; not currently executable)"*, clause 4 *"Live and fully executable"*) ·
`cosmological_constant:20-24, 126-127` · `koide_relation:242` · `DERIVATION_HUNT:305, 327`.
`INDEPENDENCE_AUDIT:34` and `hierarchy_problem:967` use "0.22%" for an unrelated quantity
(the d = 3 agreement level) — **not** this class. **Residual: `DERIVATION_HUNT:1279` only** (table above).

**Class 6 (false page COMPLETE) — CLEAN.** I read every claims-ledger and triage block in the
slice. No bare "COMPLETE" appears. Grades used are COMPLETE-CONDITIONAL, COMPLETE-ABSTENTION,
OPEN-MACHINE, OPEN-THEORY, OPEN-BLOCKED, candidate, machine-backed, honest fence, meta —
all legitimate. Strong CP's **COMPLETE-ABSTENTION** is consistently stated with its non-claims at
`INDEX:16,36`, `honest_status:52-54,80`, `DOMAIN_COVERAGE:49,103`. `INDEX:9` states
*"Physics COMPLETE promotions this wave: **0**"* — honest. The only body-contradicts-grade case I
found is `DERIVATION_HUNT:1287` (table above), which is a prose overclaim rather than a grade tag.

**Class 7 (orphan tables) — CLEAN apart from §2b.** I checked header/separator/cell-count on every
table in the slice: `INDEX:11-16` (3 cols ✓), `honest_status:32-36` (6 ✓), `:68-80` (2 ✓),
`:100-107` (3 ✓), `READERS_GUIDE:38-61, 65-81, 131-137` (✓), `lattice_note:87-90, 131-138` (✓),
`DOMAIN_COVERAGE:19-54` (5 cols, 34 rows — row count matches the file's own stated 34 ✓),
`CHAIN_TABLES:33-37` (8 cols, separator 8 ✓), `:41-44, 74-79, 159-164` (✓),
`REFEREE_CALENDAR:32-41, 119-129, 132-145` (✓), `INDEPENDENCE_AUDIT:30-41, 81-88` (✓),
`cosmological_constant` all tables (✓), `MATH_SPINE:104-107, 160-164, 679-685, 1003-1012` (✓),
`PREREGISTERED` all (✓), `DERIVATION_HUNT:70-74, 232-237, 541-543, 672-676, 1103-1107, 1187-1190,
1274-1282` (✓). `DOMAIN_COVERAGE`'s deliberate row-number gaps (27, 28, 31) are **documented at
:66-68** and are not a defect.

**Class 1 (repair-log) — the "clean corpus-wide" claim from the prior round is FALSE.** I read the
nine sites listed in the findings table. Six are CONFIRMED. The prior sweeps missed them for two
mechanical reasons I reproduced: **case sensitivity** (`This sentence` vs `this sentence`) and
**line wrapping** (`has now actually\nbeen removed`). Any future sweep must use `-i` and must
tolerate newlines inside the phrase.

**Class 2 — mostly clean.** A grep for `WHOSE_TURN|@FROM:|>>BLUE|>>RED|TODO|note to self|insert
here|red should|blue should|owner: please|next seat|do not edit this line|FIXME|XXX:|<!--` across
all fourteen files returns **zero hits**. The three sites I did find (`PREREGISTERED:688`,
`PREREGISTERED:1686`, `LEDGER:5826`) were found by reading, not by the pattern list.

**Chain-name accuracy — CLEAN.** Every chain named as running in the slice (`cmp_lcdm_mnu_bbnfix`,
`dyad_mnu_bbnfix`, `cmp_prtoe_routeD`) is in `chains/` with activity today. Every chain named as
not running (`cmp_prtoe_conv_desi`, `cmp_prtoe_zon_disp`, `cmp_prtoe_zon`, `dyad_mnu_mcmc`,
PolyChord) is correctly described, and their quoted R−1 values (13.25 / 17.81 / 40.36 / none) match
the progress files exactly. **No posterior is booked from a chain file anywhere in the slice** —
every surface routes booking through `scripts/book_bbnfix_when_ready.py` and states REFUSED.
`CHAIN_TABLES:19-21` correctly warns that `.progress` `acceptance_rate` is oversampled and that the
real accept rate lives in the launchlog.

---

## 5. Tally

| class | CONFIRMED | SUSPECT | found-then-cured |
|---|---:|---:|---:|
| 1 — repair-log document history | 6 | 3 | 0 |
| 2 — embedded editor instructions | 2 | 3 | 0 |
| 3 — stale chain / stale R−1 | 1 | 2 | **7 surfaces** (6 R−1 + 1 GR-order) |
| 4 — 0.22% as executable | 1 | 2 (both ledger-history) | 4 |
| 5 — EXTERNAL WIN without DOI | 0 | 0 | 0 |
| 6 — false page COMPLETE | 0 | 0 | 0 |
| 7 — orphan tables | 1 (cosmetic: §3 mis-lettering) | 0 | 1 |
| 8 — overclaims | 4 | 1 | 0 |
| 9 — house jargon | 1 | 5 | 0 |
| **total** | **16** | **16** | **12** |

---

## 6. What a reader should take from this

Three things, in order of how much they cost:

1. **The class-3 failure was corpus-wide and the corpus's own rule caught nothing.** Six shelf
   surfaces — including the designated authority `PRTOE_CHAIN_TABLES.md` — carried a one-day-stale
   R−1 as the live gate while `PRTOE_REFEREE_CALENDAR.md` already carried the correct one. The
   worst error was 7× on routeD. This is a *propagation* defect, not an authoring defect: the
   corpus has one file that updates and six that copy.
2. **`PRTOE_MATH_SPINE.md` is the class-1 reservoir**, and the prior "clean corpus-wide" verdict was
   reached with a grep that could not see the text. Three confirmed sites in one file, one of them
   a full paragraph of edit archaeology.
3. **The ±0.25% vs ±0.449% split on ρ_Λ¼ is the only finding here that could move a physics
   verdict.** The entire P-2026-048 withdrawal — the thing four files just spent the morning
   propagating — rests on 0.98σ, and `MATH_SPINE:158` says 1.8σ. Somebody has to rule.
