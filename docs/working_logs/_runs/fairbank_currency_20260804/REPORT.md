# Fairbank note draft — currency full freeze (2026-08-04)

**Worker:** Grok Build subagent  
**Package:** `docs/working_logs/_runs/fairbank_currency_20260804/`  
**Target:** `docs/PRTOE_fairbank_note_draft.md`  
**Rules:** NO FABRICATIONS · **no invented posteriors** · **no arXiv post** · no Fairbank email · no MCMC kill · no PolyChord · no peek H₀ as result

Artifacts:

- [`REPORT.md`](REPORT.md) — this file  
- [`EDITS.md`](EDITS.md) — file-level edit list  

---

## Mission checklist

| # | task | status |
|---|---|---|
| 1 | Find any “as of 2 August R−1 = 0.19 / 0.14” language | **DONE** — not present as live text (git history only, Aug 2 re-tense); superseded language named in freeze banner |
| 2 | Replace with 2026-08-04 truth: dyad **0.189** / lcdm **0.059**, **NOT bookable**, no peek H₀ as result | **DONE** — banner + status § + ledger row 4 |
| 3 | Keep **CORPUS_ONLY** / experimental letter fences | **DONE** — status line + ledger rows 5–6 + HOLD |
| 4 | Cross-link `neutrino_full_honesty` and `arxiv_owner_prep` | **DONE** — freeze banner + triage line |
| 5 | Package this dir REPORT.md + EDITS.md | **DONE** |

---

## Authority quote (bbnfix — **NOT bookable**)

Read-only from progress + checkpoint (same stamp as open_machine / neutrino_full_honesty):

| leg | N | R−1 | converged | bookable |
|---|---:|---:|---|---|
| `dyad_mnu_bbnfix` | 18837 | **0.189201** (~0.189) | **false** | **NO** |
| `cmp_lcdm_mnu_bbnfix` | 19013 | **0.059055** (~0.059) | **false** | **NO** |

**Quote for letter currency:** dyad R−1 **0.189**, lcdm **0.059**, both not self-stopped, **NOT bookable**. Do not quote H₀ / joint posteriors as results until `scripts/book_bbnfix_when_ready.py` passes (both R−1 < 0.05 **and** `converged: true`).

Stale “as of 2 August R−1 = 0.19 / 0.14” (Aug 2 re-tense in git) is **superseded**. Offline GetDist GR peeks are **diagnostic only**, never the gate.

---

## What was frozen on the letter

| locus | before / risk | after (this freeze) |
|---|---|---|
| Status line | “experimental note” only | **experimental letter** · **CORPUS_ONLY** · ship = neutrino-mbb only · **HOLD** (no email / no second TeX / no invent endorsement) |
| Top residual freeze | absent as dedicated currency banner | **Currency residual freeze — 2026-08-04**: 0.189 / 0.059; NOT bookable; no peek H₀; supersedes 0.19/0.14; links honesty + owner prep + home + HOLD |
| Status of the cosmological fits (§) | already carried 2026-08-04 0.189/0.059 (prior honesty pass) | **confirmed** as live currency (no invent) |
| Claims ledger row 4 | demote H₀/outperform; joint waits book | adds explicit live R−1 **0.189 / 0.059**; **NOT bookable**; no peek H₀; `book_bbnfix_when_ready.py` |
| Claims ledger row 5 | experimental note draft · HOLD | + **CORPUS_ONLY** fence |
| Non-claims / triage | honesty cross-links | + no invent posteriors / no peek H₀; + this currency package path |

Physics arithmetic (m_ββ window, nEXO overlay, BBN columns, Σm_ν relation 61.4 meV) **unchanged** — relation packaging only; **≠** booked joint posterior.

---

## Fences kept

| fence | where |
|---|---|
| **CORPUS_ONLY** | status line; ledger row 5; triage |
| **experimental letter** | status line; ledger row 5 |
| **HOLD** | status; ledger row 5; no desk email |
| Ship vehicle = `neutrino-mbb` only | status; ledger row 6 |
| **READY not posted** | ledger row 6 (arxiv_owner_prep) |
| No second Fairbank TeX | status; ledger row 6 |
| No arXiv post without endorsement/ID | ledger row 6 |
| No peek H₀ / invented posteriors as results | freeze banner; status §; ledger row 4; non-claims |

---

## Cross-links

| path | role |
|---|---|
| [`../neutrino_full_honesty_20260804/REPORT.md`](../neutrino_full_honesty_20260804/REPORT.md) | Σm_ν joint · Fairbank HOLD · m_ββ READY not posted |
| [`../arxiv_owner_prep_20260804/REPORT.md`](../arxiv_owner_prep_20260804/REPORT.md) | Owner Fairbank / arXiv prep; no post |
| [`../arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md`](../arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md) | Branch table on reply |
| [`../../../PRTOE_neutrino_home.md`](../../../PRTOE_neutrino_home.md) | Home residual freeze |
| [`../../../PRTOE_neutrino_sector.md`](../../../PRTOE_neutrino_sector.md) | Relation shelf |
| [`../../../exploratory/PRTOE_fairbank_note_HOLD.md`](../../../exploratory/PRTOE_fairbank_note_HOLD.md) | HOLD companion |
| `papers/neutrino-mbb/` + `docs/arXivReady/` | Ship vehicle READY not posted |
| `papers/fairbank-0nubb/` | stays README-only **NOT_READY** |

---

## What this package did **not** do

- Invent or quote joint Σm_ν / H₀ posteriors  
- Post to arXiv  
- Email or contact Fairbank  
- Invent endorsement or arXiv ID  
- Create second Fairbank TeX  
- Kill/pause live cobaya  
- Start PolyChord  
- Change m_ββ / nEXO / BBN arithmetic  

---

## Next actions (not executed)

1. **Machine:** leave bbnfix pair running until both legs self-stop with R−1 < 0.05 → only then `python3 scripts/book_bbnfix_when_ready.py`.  
2. **Owner:** wait Fairbank reply → owner branch table.  
3. **Desk:** no arXiv post; no second Fairbank package.

---

## Files edited / written (absolute paths)

1. `/home/themilkmanj/prtoe_class/docs/PRTOE_fairbank_note_draft.md`  
2. `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/fairbank_currency_20260804/REPORT.md`  
3. `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/fairbank_currency_20260804/EDITS.md`  

*NO FABRICATIONS. NO invented posteriors. NO arXiv post.*
