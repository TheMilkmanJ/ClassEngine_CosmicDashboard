# arXiv / Fairbank — owner checklist (external win #1)

**Date:** 2026-08-03 (living) · **prep re-stamp: 2026-08-04** · **trigger re-stamp: 2026-08-04T18:14Z**  
**Role:** Owner-only actions. Blue cannot invent endorsement or post for you.  
**Claude H1 rank #1:** public arXiv postings (neutrino-mbb + READY packages). Not a blue desk win.

Living sources: `papers/<name>/`. Staged PDF+tarball: `docs/arXivReady/`. Hygiene: `scripts/arxiv_package_audit.py`.  
**Do not invent endorsement.** Per-archive. Account default `physics.space-ph` is **not** a home for any of these.

### Owner HOLD (2026-08-04)

- Packages are **READY on disk** (6 TeX packages audit-clean; staged MD5 MATCH papers — re-verified 2026-08-04T18:14Z).  
- **HOLD arXiv posts** until Fairbank replies on neutrino-mbb **or** you deliberately take a parallel archive path (astro-ph / Zenodo).  
- Desk will **not** post, email Fairbank, invent endorsement, or invent a second Fairbank TeX.  
- **Do this next (one page):**  
  [`docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/OWNER_SHIP_NOW.md`](../docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/OWNER_SHIP_NOW.md).  
- When he replies (branch detail):  
  [`docs/working_logs/_runs/arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md`](../docs/working_logs/_runs/arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md).  
- Full inventory:  
  [`docs/working_logs/_runs/arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md`](../docs/working_logs/_runs/arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md).  
- Trigger REPORT:  
  [`docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/REPORT.md`](../docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/REPORT.md).

---

## 1. neutrino-mbb ↔ Fairbank (status)

| item | fact |
|---|---|
| Package | `papers/neutrino-mbb/` — **READY_PACKAGE** (3 pp, hep-ph) |
| Payload | `submission/main.tex` + `main.bbl`; tarball `neutrino-mbb.tar.gz`; staged in `docs/arXivReady/` |
| Fairbank letter draft | `docs/PRTOE_fairbank_note_draft.md` — **CORPUS_ONLY** personal letter |
| `papers/fairbank-0nubb/` | **NOT_READY** — README only; **no TeX**; numbers already match neutrino-mbb |
| Owner action taken | **Submitted neutrino-mbb package to William Fairbank (2026-08-03)** |
| Desk consequence | Further packaging on this thread **paused**. Do **not** invent a second Fairbank TeX. |
| arXiv still needs | **hep-ph endorsement** (separate archive from astro-ph) |
| Claim (one line) | Hypothesis m₁ = ρ_Λ¼ ≃ 2.25 meV + NO ⇒ m_ββ ∈ [0.04, 5.30] meV; useful edge vs min-NO ceiling 3.69 meV |

**Owner next buttons (Fairbank / hep-ph thread only):**

1. Track Fairbank reply / feedback; do not rewrite package unless he requests a concrete change. **HOLD post until reply (or explicit parallel path).**
2. If he (or another hep-ph author with recent posts) can endorse: generate arXiv endorsement request code for **hep-ph**, send finished PDF + tarball.
3. After endorse → submit **primary hep-ph** from `docs/arXivReady/neutrino-mbb.{pdf,tar.gz}` (or rebuild from `papers/neutrino-mbb/`).
4. Until then: optional public path without arXiv = Zenodo one record (PDF + tar.gz, CC BY 4.0) — same pattern as supertrace.
5. Branch table (positive / content edit / decline / silence): `docs/working_logs/_runs/arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md`.

---

## 2. Each package — next button (owner)

| package | status | archive | next button for owner |
|---|---|---|---|
| **supertrace-note** | **SHIPPED** Zenodo [10.5281/zenodo.21763188](https://zenodo.org/records/21763188) | gr-qc (optional) | Optional only: gr-qc endorsement → arXiv mirror of existing Zenodo record. Corrections = Zenodo “New version.” |
| **neutrino-mbb** | READY; **with Fairbank** | hep-ph | Fairbank thread + **hep-ph endorsement** → upload. Packaging paused on desk. |
| **radio-lattice** | READY (7 pp; DM demotion in text) | astro-ph.CO (+ .IM) | Get **astro-ph endorsement** → upload. One endorsement covers .CO + .IM. Strong first *astro* post if Fairbank/hep-ph stalls. |
| **bbn-eps-bound** | READY (3 pp; Aver only) · **ARITHMETIC VERIFIED (internal)** 3.196%≈3.20% · **EXTERNAL WIN PENDING (no DOI)** | astro-ph.CO | Same **astro-ph endorsement** as radio-lattice → upload. Optional residual dense ε_max(T_c) is **not** a hold. Optional DOI without arXiv: [`ZENODO_BBN_EPS_BOUND_CHECKLIST.md`](../docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/ZENODO_BBN_EPS_BOUND_CHECKLIST.md) (checklist only; desk did not upload). |
| **lattice-tc-gap** | READY (2 pp; gap note only) | hep-lat | Get **hep-lat endorsement** → upload. No lattice result claimed. |
| **kination-tracking-note** | READY (2 pp) | gr-qc | Get **gr-qc endorsement** → upload (or after supertrace arXiv if same archive opens). |
| **fairbank-0nubb** | NOT_READY | — | **Do nothing technical.** Keep README-only. Ship via neutrino-mbb. |

**Upload materials (already built):** for each READY/SHIPPED name, use  
`docs/arXivReady/<name>.pdf` + `docs/arXivReady/<name>.tar.gz`  
(or rebuild from `papers/<name>/submission/`).

**Submitter fields (fixed):** Justin Pulford · pulfordj420@gmail.com · Unaffiliated · USA · career Other.  
Do **not** file under default `physics.space-ph`.

---

## 3. Endorsement needs (minimum set)

Endorsement is **per archive**. Success on one does **not** open another. First successful post on an archive usually auto-endorses you for further posts there.

| archive | packages unlocked | endorser profile |
|---|---|---|
| **hep-ph** | neutrino-mbb | Recent hep-ph author (Fairbank thread is the live path) |
| **astro-ph** | radio-lattice, bbn-eps-bound | Recent astro-ph author; one endorse covers both notes |
| **hep-lat** | lattice-tc-gap | Recent hep-lat author |
| **gr-qc** | supertrace (optional), kination-tracking-note | Recent gr-qc author |

**Practical order (owner):**

1. **hep-ph** via Fairbank / neutrino-mbb (already in flight).  
2. **astro-ph** for radio-lattice + bbn-eps-bound (highest non-Fairbank public surface; recommended first *if* hep-ph blocks).  
3. **hep-lat** / **gr-qc** when convenient (thin notes; lower priority).  
4. Do **not** rush a wrong primary to beat an unverified “endorsement expires” story — request *codes* expire; posts do not.

**Zenodo without arXiv** (no endorsement): already done for supertrace; available any day for the other five (one record per paper, never bundled). That is public DOI / Scholar indexing, **not** an arXiv listing.

---

## 4. What blue already did (do not redo)

- Six TeX packages clean: no “PRTOE” in `main.tex`, no live BibTeX `note=` leakage, no empty acknowledgments, clean-room pdflatex 0/0/0 where claimed.
- Full `submission/` + tarballs + staged `docs/arXivReady/` (all six PDF+tar.gz present 2026-08-03; neutrino-mbb stage refreshed MATCH papers evening).
- Red-team pass on paper-facing claims (2026-08-02/03); content holds closed on READY set (bbn dense T_c curve optional residual only).
- `fairbank-0nubb` deliberately **not** TeX’d; cross-check table vs neutrino-mbb filed.
- neutrino-mbb: 8/8 numbers re-derived; packaging **paused** after owner Fairbank submit.
- supertrace **published** Zenodo DOI 10.5281/zenodo.21763188.
- Candidacy / readiness / package-audit living logs: `_ARXIV_CANDIDACY.md`, `_ARXIV_READINESS.md`, `_PACKAGE_AUDIT.md`.
- Claude H1 ranking filed: arXiv postings = external win #1 (owner); T14 reclassified thread-closure.
- **2026-08-03 evening process lock:** derivation exit gate **CLOSED** (Claude + Grok + ChatGPT); arXiv-ready P1–P2 **BOOKED** (69 rows; 0 new PAPER_CANDIDATE; exploratory 44/44 CORPUS_ONLY). Detail: `docs/working_logs/_runs/arxiv_ready_pass_20260803/`. **No further derivation hunting** unless a paper claim finds a *new* missing derivation.

---

## 5. What NOT to wait on blue for

| do not wait for | why |
|---|---|
| More TeX packaging on neutrino-mbb / Fairbank | Owner already submitted; desk paused; second TeX is duplicate |
| New short papers from COMPLETE docs | 2026-08-03 re-audit: **0** new PAPER_CANDIDATEs |
| Dense ε_max(T_c) curve | Optional residual; Aver bound at measured T_c already in READY package |
| Deeper kination Q-ball lit review | Optional; claim stands |
| bbnfix posterior booking / R−1 < 0.05 | Separate external win (blue machine); **not** needed for any READY note |
| T14 / IGMF / H₀ / multi-claim overview | Thread-closure or NOT_READY; wrong shape for first posts |
| Blue to “get endorsement” | Impossible from desk — human with recent archive posts + arXiv request code |
| More derivation sprints | Exit gate closed; blocked register is finite and named; inventing is forbidden |
| New short papers from docs shelf | arXiv pass: **0** PAPER_CANDIDATE after full grade + exploratory sweep |
| Blue to choose primary category | Owner account + endorser; never force `physics.space-ph` |

**Owner-only loop this week:** Fairbank follow-up **or** find one astro-ph endorser for radio-lattice (PDF in hand) **or** Zenodo the two highest-leverage READY notes (radio-lattice, bbn-eps-bound) while endorsements pend. **Do not treat desk prep as a post.**

### Prep verification (desk, 2026-08-04) — do not redo

- Re-ran `scripts/arxiv_package_audit.py` → 6/6 clean; `_PACKAGE_AUDIT.md` refreshed.  
- papers ↔ `docs/arXivReady/` tarball MD5 **MATCH** all six.  
- BBN ε stranger recompute **ARITHMETIC VERIFIED (internal)** (ε 2σ 3.196% ≈ 3.20%); **EXTERNAL WIN PENDING (no DOI)** — package READY ≠ public external win.  
- Fairbank letter: H₀ / “outperform” opener **surgically demoted** (still CORPUS_ONLY letter; not a package).  
- No CLASS/MCMC/PolyChord in this lane.  
- Artifacts: `_runs/arxiv_owner_prep_20260804/{PACKAGE_INVENTORY,OWNER_ACTION_WHEN_FAIRBANK_REPLIES,REPORT}.md`.

### Trigger re-stamp (desk, 2026-08-04T18:14Z) — do not redo

- Re-ran `scripts/arxiv_package_audit.py` → **6/6** clean; log at `_runs/fairbank_arxiv_trigger_20260804/arxiv_package_audit.log`.  
- papers ↔ staged **tar + PDF MD5 MATCH** all six; pages 3/3/7/2/3/2.  
- BBN recompute (papers + staged) **PASS** 3.196% ≈ 3.20% — dual stamp unchanged.  
- bbnfix **still NOT bookable:** lcdm R−1 **0.071122** N=21886 · dyad R−1 **0.072286** N=21867 · gate REFUSED.  
- New owner one-pager: `OWNER_SHIP_NOW.md`; Zenodo bbn checklist only (no upload).  
- **No** Fairbank contact · **no** arXiv post · **no** MCMC/PolyChord/H₀ peek.

---

*Sources: `papers/README.md`, `papers/*/README.md`, `docs/arXivReady/README.md`, `docs/working_logs/_ARXIV_CANDIDACY.md`, `_ARXIV_READINESS.md`, `_PACKAGE_AUDIT.md`, `_runs/hard_wins_90day_20260803/REPORT.md` (Claude H1), `_runs/arxiv_owner_prep_20260804/`, `_runs/fairbank_arxiv_trigger_20260804/`.*
