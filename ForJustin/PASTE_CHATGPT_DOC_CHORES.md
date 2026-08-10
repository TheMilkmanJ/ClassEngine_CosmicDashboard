# PASTE TO CHATGPT — DOC CHORES ONLY (Grok handoff)

**Date:** 2026-08-08  
**From:** Grok (conserving usage)  
**To:** ChatGPT  
**Owner intent:** Burn ChatGPT usage on **substantive documentation chores**. **Skip pure hygiene** (typos, style-only, banner wording thrash, “editor instruction” cleanup, cosmetic renames). Grok is paused on AWS quota + PolyChord fleet; do **not** re-do that.

**Your job:** update living docs so they match **machine truth**, without inventing COMPLETE, wins, or nested verdicts.

---

## 0. Hard rules (read first)

1. **NO FABRICATIONS.** Do not invent COMPLETE, bookable H₀, ΔlnZ wins, or PolyChord results.
2. **exit0 ≠ PASS.** Scripts exiting 0 is not a physics claim.
3. **Dual-gate only** for bbnfix booking authority: both legs R−1 < 0.05 **and** `converged: true`, then only  
   `python3 scripts/book_bbnfix_when_ready.py`.
4. **Hygiene is out of scope** for this paste. If you find only style issues, list them under “deferred hygiene” and move on.
5. **Do not kill or relaunch MCMCs / PolyChord** unless owner orders it.
6. Prefer **currency freezes** with N, R−1, timestamp, path to authority receipt — not narrative soft-close.
7. When numbers conflict, **machine files win** over prose.

---

## 1. Authority sources (look here first — cheap)

| Topic | Where to read (do not guess) |
|---|---|
| Old-BAO bbnfix **BOOKED** GetDist | `docs/working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md` (+ `booking.json`) |
| Sample-cov Laplace + soft-mode warning | `docs/working_logs/_runs/laplace_docs_chains_bbnfix_20260808/REPORT.md` · `docs/chains/LAPLACE_bbnfix_full.md` |
| GetDist ESS / GR diagnostics | `docs/working_logs/_runs/credibility_diagnostics_20260808/posterior_diagnostics.json` · `CHECKLIST.md` |
| Nested / gold PolyChord design (4 legs) | `docs/working_logs/_runs/gold_desidr2_polychord_20260808/REPORT.md` |
| DESI-DR2 MCMC **BOOKED Stage A** | `docs/working_logs/_runs/desidr2_bbnfix_booking_20260810_053127/` |
| Quota request | `docs/working_logs/_runs/quota_increase_20260808/REPORT.md` |
| Booking pipeline / Stage A–B | `docs/working_logs/_runs/laplace_prep_harden_20260804/RUNBOOK.md` · `scripts/bbnfix_when_ready_all.sh` |
| Chain files (export bundle) | `docs/chains/` (old-BAO booked pair copies) |
| Live chain roots (repo) | `chains/dyad_mnu_bbnfix.*` · `chains/cmp_lcdm_mnu_bbnfix.*` |

**How to find more chores without a full tree walk:**

```bash
cd /home/themilkmanj/prtoe_class
# Stale “NOT bookable” / old R−1 after booking existed
rg -n "NOT bookable|NOT BOOKABLE|REFUSED|0\.085619|0\.086073|1\.71×|1\.72×|currency residual|OPEN-BLOCKED|OPEN-MACHINE" docs/*.md
# Living files that still say pair closed
rg -n "book_bbnfix_when_ready|bbnfix pair|dyad_mnu_bbnfix" docs/PRTOE_*.md
# Overclaims in export bundle
rg -n "better than|outperform|COMPLETE|win|ΔlnZ|H0" docs/chains/*.md docs/chains/*.txt
# Open machine residuals (non-hygiene)
rg -n "OPEN-BLOCKED|OPEN-MACHINE|Machine residual|Instrument \*\*not running\*\*" docs/*.md docs/exploratory/*.md
```

---

## 2. Priority chore list (do in order)

### P0 — Currency of the **booked old-BAO bbnfix pair** (substantive)

Living docs still freeze the pair as **NOT bookable** / dyad not self-stopped. That is **stale**.

**Authority (BOOKED):**  
`docs/working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md`

| chain | R−1 | N | t | converged |
|---|---:|---:|---|---|
| `dyad_mnu_bbnfix` | **0.048118** | 37605 | 2026-08-07T04:08:52 | **true** |
| `cmp_lcdm_mnu_bbnfix` | **0.049324** | 26294 | 2026-08-05T11:52:10 | **true** |

**Booked GetDist (ignore_rows=0.3) — quote only from booking REPORT:**

| | H₀ | Σm_ν (m_ncdm) | S₈ |
|---|---|---|---|
| dyad | 70.052 ± 0.716 | 0.0671 ± 0.0583 | 0.821 ± 0.0097 |
| lcdm twin | 68.345 ± 0.343 | 0.0192 ± 0.0174 | 0.824 ± 0.0081 |

**Files that almost certainly need currency updates (non-hygiene):**

1. `docs/PRTOE_CHAIN_TABLES.md` — freeze banner + bookable row  
2. `docs/PRTOE_REFEREE_CALENDAR.md` — bbnfix machine table  
3. `docs/PRTOE_READERS_RISK.md` — top banner + § tables still REFUSED/0.085619  
4. `docs/PRTOE_honest_status.md`  
5. `docs/PRTOE_fairbank_note_draft.md` — currency residual freeze  
6. `docs/PRTOE_DOMAIN_COVERAGE.md` / `docs/PRTOE_neutrino_home.md` / `docs/PRTOE_neutrino_sector.md` if they still say joint Σm_ν waits on unbooked bbnfix  
7. Any exploratory that freezes “pair closed”

**Rules when updating:**

- Say **BOOKED** under dual-gate + path to `bbnfix_booking_20260808_005626`.  
- H₀ is **SH0ES-conditional** (pantheonplusshoes stack).  
- **Stage B tables:** living `PRTOE_CHAIN_TABLES` publish path still wants red audit per runbook — if you write tables, follow  
  `bash scripts/bbnfix_when_ready_all.sh --write-tables` only with `RED_AUDIT.md` (`red: AGREE` / `AGREE-IF`), or document that Stage A book exists and Stage B is still owner/red.  
  Do **not** invent red agreement.  
- Do **not** claim nested evidence from this booking.

### P0b — Evidence honesty (Laplace soft, not a win)

**Authority:** `docs/working_logs/_runs/laplace_docs_chains_bbnfix_20260808/REPORT.md`

| quantity | value | meaning |
|---|---:|---|
| Δ(min −logpost) proxy | **−2.96** | MAP fit favors dyad; **not** full Laplace |
| ΔlnZ sample-cov Laplace | **+0.21** | essentially **inconclusive** |
| cond(Σ) | ~10⁸ both legs | soft modes → **do not headline** ΔlnZ |

**Chore:** Wherever docs still promote pre-bbnfix ΔlnZ ≈ +2.6, or claim a statistical win from bbnfix, **fence or replace** with the above labels. Prefer “MAP better by ~3 in −logpost; volume-aware Laplace inconclusive.”

Also audit `docs/chains/PRTOE_dyad_completed_chains.md` and `docs/chains/best_fit_comparison.txt` for **overclaim** language (Gemini-era “show the world” tone). Keep numbers; kill sales copy.

### P1 — DESI-DR2 program (docs awareness, not launch)

**Separate instrument** from old-BAO booked pair.

| Item | Truth |
|---|---|
| MCMC configs | `dyad_mnu_bbnfix_desidr2.yaml`, `cmp_lcdm_mnu_bbnfix_desidr2.yaml` |
| BAO | `bao.desi_dr2.desi_bao_all` only (Y3/DR2) |
| Live box | on-demand `i-096d08d2dc9d8f42c`, OMP-boosted, **not bookable** last stamps ~R−1 0.11 / 0.13 |
| PolyChord gold (4 legs) | SH0ES pair + TRGB pair — see gold REPORT |

**Chore:** Add a short **currency residual** or machine table section (CHAIN_TABLES / REFEREE_CALENDAR / honest_status) that:

- Names DESI-DR2 MCMC twins as **live, not bookable**  
- Names **four** gold PolyChord configs (do not invent results)  
- States nested **not launched** pending EC2 quota (512 request CASE_OPENED)  
- Forbids mixing DESI-DR2 ΔlnZ with old-BAO booked posteriors

Config inventory (for your table, not to invent stats):

1. `dyad_mnu_bbnfix_desidr2_ev.yaml` — dyad, SH0ES  
2. `cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml` — lcdm, SH0ES  
3. `dyad_mnu_bbnfix_desidr2_trgb_ev.yaml` — dyad, TRGB CCHP  
4. `cmp_lcdm_mnu_bbnfix_desidr2_trgb_ev.yaml` — lcdm, TRGB CCHP  

Stack on all four: Planck CMB+lensing, DESI DR2 BAO, ACT, SPT, production BBN; ladder differs SH0ES vs TRGB.

### P2 — Open machine residuals (substantive, not hygiene)

Use the OPEN-BLOCKED / OPEN-MACHINE freeze banners as a task list. Examples known live:

| Residual | Doc touchpoint | Note |
|---|---|---|
| `cmp_prtoe_conv_desi` not live | `PRTOE_s8_tension.md` | conversion instrument; not replaced by bbnfix |
| Route-D thaw | CHAIN_TABLES / REFEREE_CALENDAR | separate stop 0.1; not dual-gate pair |
| Nested evidence unmatched | READERS_RISK / DOMAIN_COVERAGE | gold DESI-DR2 PolyChord is the intended fix; **not done** |
| Fairbank / DOI / external win | fairbank draft, BBN ε | external win pending DOI — don’t invent |
| zon_disp / α_c | various | instrument status, not bbnfix |

**Chore:** For each, ensure the freeze states **current machine truth** and **does not** get soft-closed by desk hygiene or by the old-BAO booking.

### P3 — Index / dependency map (light)

- `docs/PRTOE_INDEX.md` — point readers to booked bbnfix receipt + DESI-DR2 open lane + gold PolyChord design path.  
- `docs/PRTOE_DEPENDENCY_TREE.md` if it still blocks Σm_ν/H₀ on unbooked bbnfix only.

### P4 — Owner-facing checklist sync

- `ForJustin/ARXIV_OWNER_CHECKLIST.md` / `STATUS_CONTINUE.md` — only if they still say bbnfix unbookable; update to BOOKED old-BAO + open DESI-DR2/nested.  
- Do **not** rewrite the whole ForJustin novel.

---

## 3. Explicitly **out of scope** (hygiene / do not burn usage)

- Style guide thrash, em dash bans, “editor instruction” purge  
- Purple co-build “examined/found/cured” unless a **false physics claim**  
- Renaming files for neatness  
- Full docs tree check-12  
- Tribunal mail format polish  
- Re-running purple subagents  

If you hit pure hygiene, skip.

---

## 4. Deliverables when you finish a batch

For each batch of edits, write a short receipt:

```text
docs/working_logs/_runs/chatgpt_doc_chores_<YYYYMMDD>/REPORT.md
```

Include:

- Files touched  
- Numbers stamped (with authority path)  
- What remains OPEN  
- Any AGREE-IF / owner decisions needed (e.g. Stage B tables without red)  

Do **not** claim the doc tree COMPLETE.

---

## 5. Suggested first 60 minutes

1. Read `bbnfix_booking_20260808_005626/REPORT.md` + Laplace REPORT + gold PolyChord REPORT (15 min).  
2. Fix **P0** freezes on CHAIN_TABLES, REFEREE_CALENDAR, READERS_RISK, honest_status, fairbank (30 min).  
3. Fence Laplace / ΔlnZ language (10 min).  
4. Add DESI-DR2 + 4-leg PolyChord “not launched” machine residual (5 min).  
5. Write receipt.

---

## 6. One-line owner truth (for your banners)

> Old-BAO production bbnfix pair is **BOOKED** (dual-gate, 2026-08-08 receipt). H₀/Σm_ν/S₈ GetDist as in that receipt, SH0ES-conditional. Sample-cov Laplace ΔlnZ ≈ +0.21 (inconclusive; soft modes). DESI-DR2 MCMC twins live, **not bookable**. Gold nested evidence is **four** DESI-DR2 PolyChord legs (SH0ES×2 + TRGB×2), designed not launched (quota). No nested verdict. No COMPLETE.

---

**End of paste.** Grok is not executing these chores. ChatGPT owns the doc burn.


---

## Currency refresh 2026-08-10

- Old-BAO bbnfix **BOOKED** + DESI-DR2 **BOOKED Stage A** (do not mix).
- Gold PolyChord SH0ES **both legs running** (no nested ΔlnZ yet).
- Hessian v2 old-BAO **done**; DESI Hessian **process**.
- Stage B tables still red-gated without `RED_AUDIT.md`.
- Theory: stocked desk exhausted; no invent COMPLETE; Page T8 still fail.

