# 90-day hard external wins — claim-credibility plan

**Date:** 2026-08-03  
**Claude H-PACK correction (same day):** ranking revised. **arXiv postings** are owner-action #1 external event; **T14 i6 reclassified as thread-closure**, not top-3 external win. BBN ε recompute is the cleanest blue external win.

**Context:** ChatGPT referee **4/10** (discipline 6/10, claim credibility 3/10).

---

## Corrected ranking (Claude H1)

| Rank | Win | Who | External? |
|---:|---|---|---|
| **1** | **arXiv postings** (neutrino-mbb + READY packages via Fairbank endorsement) | **Owner** | Yes — public literature |
| **2** | **BBN ε public recompute** ε&lt;3.2% (2σ) at T_c=179 keV | Blue | Yes — pure arithmetic + PRyM provenance |
| **3** | **bbnfix posterior booking** when both R−1&lt;0.05 | Blue | Yes — standard GetDist product |
| (thread) | T14 i6 production TC | Blue | **Thread-closure** (GP numerics; not a cosmology external win) |

**Delivered this session:** Win 2 arithmetic **PASS** at `hard_win3_bbn_eps_recompute_20260803/` (ε 2σ = 3.196% ≈ 3.20%).

**Promotion stamp (2026-08-03 night — improve path):**  
- **Win 2 BBN ε** → **ARITHMETIC VERIFIED (internal)** (package READY + reverify PASS); **EXTERNAL WIN PENDING (no DOI / public record)**.  
- **T14 / A4** → **CANDIDATE CLOSED (config-local)** three-seat; production KILLED (thread-closure, not top sky win).  
- **Win 3 bbnfix booking** → infrastructure READY; **machine gate open** (do not book).  
- **Win 1 arXiv** → owner HOLD (Fairbank).

**Owner HOLD (2026-08-03):** Rank 1 arXiv/Fairbank **not chased** — Fairbank at CSU already contacted; wait further response before any further arXiv push. Blue executes ranks 2–3 readiness + promotions of locked grades (`../PROMOTION_BOARD_20260803_IMPROVE.md`).

---

## Referee bar this plan optimizes for

Each win must give an outsider **one recomputable number or table** with:

1. A thin, killable claim (no medium=gravity identity required for the *number*)  
2. A concrete artifact path (code + inputs + protocol)  
3. A pre-registered kill if the number fails  

Three independent landings of that shape is the minimal path from **claim-credibility 3/10 → ~5/10**. Discipline (6/10) is preserved by Failures Ledger + zero false closures.

---

## Win ranking (highest leverage first) — **SUPERSEDED by Claude H1 table above**

Legacy section numbering below keeps Win 1 = bbnfix booking and Win 3 = BBN ε for artifact paths; **priority order for external claim-credibility is arXiv (owner) → BBN ε → bbnfix → (thread) T14**.


## Win 1 — Book the live BBN-fixed posterior pair (highest leverage)

### 1. One-sentence claim outsiders can recompute

**Under the frozen BBN-fixed production yamls, when both chains have R−1 < 0.05, three-rank GetDist marginals give H₀ = X ± σ_X (ΛCDM+mν twin) and H₀ = Y ± σ_Y (dyad twin), with the same Σm_ν setup, from the released chain files alone.**

### 2. What artifact already exists

| Piece | Path / status (2026-08-03) |
|---|---|
| Live chains | `chains/dyad_mnu_bbnfix.{1,2,3}.txt` + progress/checkpoint/yaml; `chains/cmp_lcdm_mnu_bbnfix.{1,2,3}.txt` + same |
| Last R−1 snapshot | dyad **~0.191** (N≈15969); lcdm **~0.054** (N≈16075) — lcdm at the bar, dyad still ~4× stop |
| Gate / letter script | `scripts/finalize_h0_at_convergence.py` (hard refuse if either R−1 ≥ 0.05) |
| Booking runbook | `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` |
| GetDist instrument | `scripts/make_getdist_tables.py` (needs `ROOTS` extended to the bbnfix pair) |
| Inputs outsiders need | `*.input.yaml` / `*.updated.yaml`, covmats, CLASS/cobaya stack already used for the runs |

**No new PolyChord. No new campaign.** Leave both mpiruns alone until gates; then book.

### 3. Concrete work steps (≤2 weeks once both R−1 < 0.05)

1. **Watch only:** `tail -1 chains/dyad_mnu_bbnfix.progress` and `cmp_lcdm_mnu_bbnfix.progress` (field 4 = R−1). Do not peek-quote H₀ while over bar.  
2. When **both** R−1 < 0.05 (prefer `converged: true` in checkpoints): freeze or wait for idle ranks; run `python3 scripts/finalize_h0_at_convergence.py`.  
3. Extend `make_getdist_tables.py` `ROOTS` to `dyad_mnu_bbnfix` + `cmp_lcdm_mnu_bbnfix`; produce three-rank marginals (H₀, Σm_ν, Ω_b h², …) + triangles.  
4. Write a **one-page recompute card** under `docs/working_logs/_runs/bbnfix_booking_<stamp>/REPORT.md`: exact R−1 values, git commit or chain file hashes, GetDist commands, table of means ±68%.  
5. Update living tables only after booking (`PRTOE_CHAIN_TABLES.md`, referee calendar Sitting NOW) — no “almost bookable” language.  
6. Optional same window: Laplace / Δχ² pair per checklist **only** if CLASS rebuild not required between last sample and re-eval.

**Wall-clock to gate:** not under desk control; 90-day budget assumes dyad continues to fall (historical trend 0.32 → 0.19). If dyad stalls above 0.05 for the full quarter, this win **misses** — do not substitute RouteD.

### 4. Kill criterion

- Either chain fails to reach R−1 < 0.05 within 90 days → **win not earned** (record as open machine, not partial book).  
- Booked H₀ quoted from rank-1 half-chain only, or while R−1 ≥ stop → **process kill** (Failures Ledger if any public claim leaked).  
- Rank means disagree beyond within-rank σ after “convergence” → **do not book**; reseed/diagnose first.  
- Outsider with the same yaml + CLASS cannot reproduce the GetDist table from released samples → **artifact incomplete**.

### 5. How it raises the 3/10 claim score

This is the first **standard cosmology product** (posterior tables outsiders already know how to audit) that does not require accepting the medium=gravity story. It converts “ambitious corpus + live chains” into **one external-grade numerical package**. One hard cosmology win alone can move claim credibility ~3 → ~4; paired with Wins 2–3, the referee’s “three independent external results → ~5/10” bar becomes reachable.

---

## Win 2 — T14 H_kin production TC with external recompute path

### 1. One-sentence claim outsiders can recompute

**On the production grid 128×128×256 with the 2026-08-03 single-instrument protocol, the signed kinetic helicity diagnostic satisfies H ≈ sign(n)·2 within the pre-registered band, with null branches (n=0 nowinding / no-jet) below threshold and mirror residual across opposite-n branches < 5%.**

### 2. What artifact already exists

| Piece | Path / status |
|---|---|
| Production run | `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/` (**RUNNING**; cal PASS; nulls in flight) |
| Launcher | `scripts/run_t14_i6_production.sh` (owner-approved A4) |
| Instrument | `scripts/ring_toroidal_hkin.py` (+ protocol printed in consoles) |
| Prior smokes / nulls | `_runs/t14_hkin_resmoke_*`, `t14_hkin_null_*` (smoke only — **not bookable**) |
| Debt seat | SCIENCE_DEBTS **D1** — TC when done; mirror <5% |

Config-local GP numerics: **no cosmology ontology**, no CLASS, no MCMC.

### 3. Concrete work steps (≤2 weeks after production finishes)

1. Let production complete four-branch + nulls; do **not** quote sign from incomplete rows.  
2. Grade against TC: |H − sign(n)·2| band, null floors, mirror residual <5% (as in production script target).  
3. Freeze a **reproduce bundle**: command lines, grid params, RNG/seeds if any, `summary.json` for all branches, nulls, calibration log.  
4. Write `docs/working_logs/_runs/t14_hkin_i6_prod_*/EXTERNAL_RECOMPUTE.md` with a single shell recipe an outsider can run on one GPU/CPU box.  
5. If TC passes: book the **config-local** claim only (not “universe is GP,” not cosmology H).  
6. If TC fails: Failures Ledger row + instrument fix path; **do not** retarget H to match data.

Effort after wall-clock: documentation + grading ~few days; full outsider dry-run of a reduced grid smoke ≤1 week.

### 4. Kill criterion

- Mirror residual ≥5% or nulls fire at signal level → **sign claim dead** for this instrument generation.  
- Production incomplete / outcome row mislabeled as “violated” vs “unmeasured” → process defect (already referee-flagged pattern).  
- Claim expanded to cosmology, bounce, or medium=gravity without new evidence → **overclaim kill**.  
- Outsider cannot reproduce calibration PASS + one production branch from the recipe → artifact not external.

### 5. How it raises the 3/10 claim score

Gives a **second independent external surface**: pure numerics with a preregistered falsifier, independent of the BBN/H₀ product. Survives even if the unified ontology is wrong. Addresses referee “load-bearing claims blocked by conceptual gaps” by putting one load-bearing **numerical** link (T14 sign) on an external recompute path rather than corpus narrative.

---

## Win 3 — Public BBN ε bound with one-command recompute (no MCMC)

### 1. One-sentence claim outsiders can recompute

**For a linear leptonic m_e turn-on at the measured T_c = 179 keV, PRyMordial elasticity dY_p/dε = 0.00163 per %ε plus Aver et al. Y_p = 0.2453 ± 0.0034 implies ε < 3.2% (2σ), with EMPRESS unusable because the ε=0 null is already +2.9σ high.**

### 2. What artifact already exists

| Piece | Path / status |
|---|---|
| TeX package | `papers/bbn-eps-bound/` — **READY**, red-team pass 2026-08-02; staged `docs/arXivReady/bbn-eps-bound.{pdf,tar.gz}` |
| Number provenance | Paper README: Y_p⁰=0.246891, windowed Y_p at ε≃1.25%, dY_p/dε=0.00163/%ε, 2σ ceiling 3.20% |
| Network scripts | `scripts/prym_ramped_splice.py`, `scripts/prym_elasticity_runner.py`, `scripts/prym_supersession_pricing.py` |
| Framework independence | ε and T_c free; Aver only; **no PRTOE name in TeX**; no chain-dependent D/H |

Sister READY thin notes (same 90-day public surface, lower individual leverage): `radio-lattice`, `kination-tracking-note`, `lattice-tc-gap`; supertrace already **SHIPPED** Zenodo DOI 10.5281/zenodo.21763188; neutrino-mbb paused on Fairbank thread.

### 3. Concrete work steps (days–≤2 weeks; no endorsement required for the win)

1. Add a **single recompute entrypoint** (thin wrapper or README block) that prints: baseline Y_p, elasticity, Aver 2σ ceiling, EMPRESS null test — calling existing PRyM scripts or frozen scan tables with hash.  
2. Zenodo **one record** for bbn-eps-bound: PDF + arXiv tarball + recompute script/output log (CC BY 4.0). Do not bundle unrelated papers.  
3. Optional same week: Zenodo for `kination-tracking-note` (exact w=(n−2)/(n+2); script `scripts/bounce_bkl_stiff_check.py`) and/or `radio-lattice` (weight table only — not amplitude novelty).  
4. Do **not** invent dense ε_max(T_c) as a shipped result unless the grid is actually run and audited (still UNVERIFIED residual).  
5. Endorsement chase for arXiv remains **owner-external** and is **not** counted as this win’s kill/pass.

### 4. Kill criterion

- Independent recompute of elasticity at T_c=179 keV disagrees with 0.00163/%ε beyond stated linear window → **bound number dies**; revise or Failures Ledger.  
- Paper ships a chain-dependent D/H prediction or EMPRESS “limit” → **honesty kill**.  
- DOI lands without recompute artifact (PDF only) → **external win incomplete** (publicity ≠ recompute).  
- Claim rewritten as “PRTOE predicts ε = …” inside the public note → independence broken.

### 5. How it raises the 3/10 claim score

Delivers a **third independent external surface** that is already almost finished: a literature-facing constraint with arithmetic an outsider can redo without the corpus. Aligns with referee preference for **thin killable claims** over mega-package ambition. Together with Wins 1–2, satisfies the “three independent external-grade results” minimal path in `CHATGPT_REFEREE_4_10_RESPONSE.md`.

---

## How 3/10 becomes ~5/10 (and what does not)

| Landed | Expected claim-credibility effect |
|---|---|
| None of the three | Stays ~3/10 (discipline can still hold at 6) |
| Any one solid external | ~3.5–4/10 |
| All three, no overclaim | **~5/10** (referee’s stated minimal) |
| Papers + process docs without recomputable numbers | **No** real move (packaging theater) |
| Book RouteD thaw early / quote peek H₀ | **Score drop** (discipline and claim both hurt) |

**Not required for 5/10:** finishing the TOE, Koide, bounce dynamics, magnetism void, Page curve dynamics, new PolyChord, arXiv endorsement on every note.

---

## Three things to STOP doing (internal scaffolding that does not help 4/10)

### STOP 1 — Parallel OPEN-THEORY multi-debt sprints without an external win criterion

**What:** Simultaneous deep pushes on Koide (#101/#102), bounce turn, hierarchy/μ₅, Page *curve* dynamics, ω_J *forward* (#39), magnetism RM — each generating debt REPORTs and red-pack cycles.

**Why stop:** These are real debts, but they only raise **internal** consistency. Referee: not fixed by more conceptual scaffolding; needs hard external wins. One theory line at a time, and only if it has a recomputable external kill (per roadmap “never all three half-done”).

### STOP 2 — Identity-map / “almost derived” closures that only close inside the corpus

**What:** New bridges that make PRTOE files agree with each other (seat χ pinning language, horn sentences, template centers, dependence maps) without a number an outsider can recompute from public inputs.

**Why stop:** This is exactly “unified-claim packaging” that inflates apparent completeness while claim-credibility stays 3/10. Cures that only change corpus wording are hygiene, not hard wins. Keep honesty edits; stop treating them as science progress against the 3/10 axis.

### STOP 3 — Process / packaging theater mistaken for external load-bearing work

**What:** More tribunal monitors, docket churn, PAPER_CANDIDATE hunts on a shelf already at **0** candidates, arXivReady refreshes without DOI/recompute, red-pack D-cycles that produce only AGREE-IF prose, or language that grades the package as if it were 8/10.

**Why stop:** Discipline is already the strong axis (6/10). More process preserves the notebook; it does **not** create outsider-recomputable wins. Packaging is allowed only when it ships Win 3–style thin claims with kill bands — not when it rearranges COMPLETE ledgers.

---

## 90-day sequence (recommended)

```
NOW ── leave dyad+lcdm+routeD alone; finish T14 i6 production; draft BBN recompute entrypoint
  │
  ├─ Week 1–2:  Win 3 Zenodo (bbn-eps-bound ± kination) + recompute card
  ├─ When T14 ends:  Win 2 grade + EXTERNAL_RECOMPUTE.md (or Failures Ledger)
  └─ When both R−1 < 0.05:  Win 1 GetDist booking + chain tables (checklist only)
```

**Capacity rule:** do not kill bbnfix pair for RouteD surgery or new campaigns. RouteD surgery is owner-gated repair, not a hard win until R−1 → stop.

---

## Honest residual after all three wins

Even at ~5/10 claim credibility the **unified** package remains candidate-grade: Koide, bounce, hierarchy residual, magnetism void shortfall, Page dynamics, and ω_J forward stay open. Wins 1–3 buy **external load-bearing surfaces**, not TOE closure. That is the correct ambition level for the referee grade.

## Continuous stamp 2026-08-03 13:59

- BBN ε recompute still **PASS** (numbers.json pass_2sig_matches_paper=true).
- T14 A4 four-branch still IN FLIGHT (not yet win-eligible TC).
- Owner arXiv checklist: `OWNER_ARXIV_CHECKLIST.md`.
- 4/10 stands.

## A2 gate stamp (2026-08-03 14:24)
lcdm R−1 **0.048827** &lt; 0.05 (progress file). **Do not book** until chain self-stops. dyad still ~0.16 — hard-win #1 still needs both + clean stop.

## T14 i6 A4 complete (2026-08-03 14:43)
Production four-branch on disk (mirrors &lt;5%). **Thread-closure instrument** — not top external win. Production sign **not** booked (cond.2 both f−1 2-cand). Red C1 owed. See `t14_i6_partial_grade_20260803/FULL_TC_REPORT.md`.

## T14 three-seat candidate (2026-08-03 15:32)
Production **KILLED**. Candidate grade **three-seat locked** (text in CANDIDATE_BOOKING_RESTATED.md). Thread-closure not top external win. Smoke i5 stands.

---

## Status table — full refresh 2026-08-04 (~02:36 local)

**Canonical package:** `docs/working_logs/_runs/debts_hardwins_full_20260804/`  
**Gates live-checked:** progress + checkpoint + `book_bbnfix_when_ready.py` + `finalize_h0_at_convergence.py` + BBN ε recompute.

| Rank / ID | Win | Status | Evidence @ 2026-08-04 |
|---:|---|---|---|
| **1** | arXiv / Fairbank public postings | **OWNER HOLD** | Packages READY (6/6 audit clean); no Fairbank reply action; no arXiv post |
| **2** | BBN ε public recompute ε&lt;3.2% (2σ) | **ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** | `recompute_eps_bound.py` → 2σ ceiling **3.196%** ≈ paper **3.20%** **PASS**; EMPRESS +2.91σ at ε=0 (cannot bound); reverify `BBN_EPS_REVERIFY_20260804.md` + shelf recompute PASS; public record (Zenodo DOI) still owed |
| **3** | bbnfix posterior booking | **NOT YET** | lcdm R−1 **0.059** (N=19013); dyad R−1 **0.189** (N=18837); both `converged: false`; book **REFUSED**; finalize **NOT YET**; GetDist GR ~0.071/~0.086 UNBOOKABLE |
| (thread) | T14 i6 H_kin | **CANDIDATE CLOSED (config-local)**; production **KILLED** | Three-seat restated text; 14/14 sign track; mirror 3.04%; f−1 UNMEASURED; **not** top sky win |

### Explicit language locks (no contradiction)

| Phrase allowed | Phrase forbidden |
|---|---|
| BBN ε **ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** | BBN ε EXTERNAL WIN as delivered (no DOI); bbnfix **delivered** / booked / H₀ quoted |
| T14 **candidate-closed config-local** | T14 production sign **delivered** / closed for sky |
| bbnfix **NOT YET** / infrastructure READY | bbnfix **almost booked** as if product landed |
| arXiv **HOLD** (owner) | arXiv **posted** without Fairbank |

### Live machine (read-only; leave MCMCs alone)

| Chain | progress R−1 | self-stop | bookable leg |
|---|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | 0.059055 | false | false |
| `dyad_mnu_bbnfix` | 0.189201 | false | false |

Refuse card stamp example: `bbnfix_booking_20260804_083546/` (both_ready: false).

### Credibility path (unchanged honesty)

- Win 2 arithmetic **landed** → thin external surface exists.  
- Win 3 booking **not landed** → standard cosmology product still machine-gated.  
- Win 1 arXiv **not landed** → owner external.  
- Claim-credibility still **not** at referee ~5/10 bar (needs independent landings beyond one arithmetic card).  
- **Do not** invent theory closes (Koide / bounce / ω_J / void / Page) to fake score.

*NO FABRICATIONS. No PolyChord. No peek-book H₀.*
