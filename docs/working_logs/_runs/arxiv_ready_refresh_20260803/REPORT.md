# arXiv ready refresh — 2026-08-03

**Task:** Blue-team package readiness for external wins (ChatGPT 4/10: arXiv is #1 external event).  
**Generated:** 2026-08-03  
**Audit:** `python3 scripts/arxiv_package_audit.py` → rewrote `docs/working_logs/_PACKAGE_AUDIT.md`  
**Living sources:** `papers/<name>/`  
**Staged shelf:** `docs/arXivReady/`  
**Rule:** Do **not** invent TeX. Do **not** invent endorsement.

---

## 1. Audit hygiene (2026-08-03)

| package | pages | tarball | PRTOE in tex | `note=` / `\bibinfo{note}` |
|---|---:|---|---|---|
| `bbn-eps-bound` | 3 | yes (`main.tex`) | none | n/a |
| `kination-tracking-note` | 2 | yes (`main.tex`) | none | n/a |
| `lattice-tc-gap` | 2 | yes (`main.tex`) | none | n/a |
| `neutrino-mbb` | 3 | yes (`main.tex`+`main.bbl`) | none | none |
| `radio-lattice` | 7 | yes (`main.tex`+`main.bbl`) | none | none |
| `supertrace-note` | 3 | yes (`main.tex`) | none | n/a |
| `fairbank-0nubb` | — | **no** | none | n/a |

**Rollup:** 6/6 TeX packages clean for PRTOE / note-field / tarball presence.  
`fairbank-0nubb` is intentionally README-only (NOT_READY).

### Staged shelf vs living (`docs/arXivReady/` ↔ `papers/`)

| package | PDF match | tar match |
|---|---|---|
| supertrace-note | YES | YES |
| radio-lattice | YES | YES |
| lattice-tc-gap | YES | YES |
| bbn-eps-bound | YES | YES |
| kination-tracking-note | YES | YES |
| **neutrino-mbb** | **NO** (shelf 254556 B / living 253095 B) | **NO** |

**Action (owner or desk when packaging resumes):** refresh `docs/arXivReady/neutrino-mbb.{pdf,tar.gz}` from `papers/neutrino-mbb/`. Living tree is authoritative. Not a TeX invent — copy only.

---

## 2. Inventory

### `docs/arXivReady/*`

| file | role |
|---|---|
| `README.md` | shelf index / status |
| `supertrace-note.pdf` + `.tar.gz` | SHIPPED (Zenodo) |
| `neutrino-mbb.pdf` + `.tar.gz` | READY (stale vs living; see above) |
| `radio-lattice.pdf` + `.tar.gz` | READY |
| `lattice-tc-gap.pdf` + `.tar.gz` | READY |
| `bbn-eps-bound.pdf` + `.tar.gz` | READY |
| `kination-tracking-note.pdf` + `.tar.gz` | READY |

### `papers/*/`

| folder | desk status |
|---|---|
| `supertrace-note/` | SHIPPED (Zenodo DOI 10.5281/zenodo.21763188); arXiv optional |
| `neutrino-mbb/` | READY_PACKAGE; owner → Fairbank 2026-08-03; packaging paused |
| `radio-lattice/` | READY_PACKAGE |
| `lattice-tc-gap/` | READY_PACKAGE |
| `bbn-eps-bound/` | READY_PACKAGE |
| `kination-tracking-note/` | READY_PACKAGE |
| `fairbank-0nubb/` | **NOT_READY** — README only; no TeX |

---

## 3. READY / SHIPPED packages — claim · endorsement · blocker

| package | one-line claim | endorsement gate | blocker (what still stops arXiv post) |
|---|---|---|---|
| **supertrace-note** | Two published gravitational counting conditions for three generations are the *same* algebraic condition (Higgs sector separates them). | gr-qc | **Optional only** — already public on Zenodo; arXiv still needs gr-qc endorsement if desired. |
| **neutrino-mbb** | If m₁ = ρ_Λ^{1/4} ≃ 2.25 meV (hypothesis), m_ββ ∈ [0.04, 5.30] meV with NO ceiling 3.69 meV; nulls do not kill. | hep-ph | **hep-ph endorsement** + **owner Fairbank thread** (packaging paused 2026-08-03; do not invent second Fairbank TeX). |
| **radio-lattice** | Universal m_e shift moves radio observables in fixed atomic-physics weights (+2,+1,−1,−1,−2); ratio structure, not amplitude leadership. | astro-ph | **astro-ph endorsement** only (content hold closed; DM demotion written into text). |
| **lattice-tc-gap** | Literature gap: no published T_c/√σ for SU(2) N_f=3 light fundamentals; note claims *gap*, not a lattice result. | hep-lat | **hep-lat endorsement** only. |
| **bbn-eps-bound** | Linear m_e turn-on at measured T_c=179 keV: Aver Y_p ⇒ ε < 3.2% (2σ); EMPRESS unusable; no chain D/H. | astro-ph | **astro-ph endorsement**; optional residual dense ε_max(T_c) curve (not a hold — bound at measured T_c is the claim). |
| **kination-tracking-note** | Rotating condensate tracking V∝rⁿ has exact w=(n−2)/(n+2); cannot reach kination without trans-Planckian amplitude. | gr-qc | **gr-qc endorsement** only. |

**Not READY:** `fairbank-0nubb` — duplicate of neutrino-mbb arithmetic + model-tied / chain-dependent layers. **Do not invent TeX.**

---

## 4. Fairbank / neutrino-mbb status

| item | status |
|---|---|
| `papers/neutrino-mbb/` | TeX package **ready** (main.tex + main.bbl; 3 pp; hygiene clean). |
| Owner action 2026-08-03 | **Submitted neutrino-mbb package to William Fairbank** (per `docs/arXivReady/README.md` and `_ARXIV_CANDIDACY.md`). |
| Packaging work | **Paused** pending Fairbank correspondence thread. |
| `papers/fairbank-0nubb/` | **NOT_READY** — README only. Numbers match neutrino-mbb; second short paper would be a duplicate. |
| `docs/PRTOE_fairbank_note_draft.md` | CORPUS_ONLY experimental letter; superseded for arXiv by neutrino-mbb. |
| arXiv gate if posting | still **hep-ph endorsement** (separate archive; not claimed). |
| Desk rule | **Do not invent a second Fairbank TeX.** Ship the claim only via neutrino-mbb when endorsement exists / Fairbank thread allows. |

---

## 5. Owner action checklist for posting

### A. Endorsement (external; do not invent)

- [ ] **astro-ph** endorsement — unlocks **radio-lattice** and **bbn-eps-bound** (same archive).
- [ ] **hep-lat** endorsement — unlocks **lattice-tc-gap**.
- [ ] **gr-qc** endorsement — unlocks **kination-tracking-note**; optionally **supertrace-note** on arXiv (already on Zenodo).
- [ ] **hep-ph** endorsement — unlocks **neutrino-mbb** (only after Fairbank thread allows resume).
- [ ] Request endorsement from an active endorsed author *per archive*; arXiv does not auto-grant cross-archive rights.

### B. Fairbank / neutrino-mbb thread

- [ ] Track Fairbank reply; **do not** open parallel packaging on `fairbank-0nubb/`.
- [ ] When packaging resumes: refresh `docs/arXivReady/neutrino-mbb.pdf` and `.tar.gz` from living `papers/neutrino-mbb/` (currently **stale**).
- [ ] Post path: arXiv hep-ph **or** Zenodo preprint first (same pattern as supertrace) if endorsement lags.

### C. Per-package post sequence (when endorsement exists)

For each package, living tree first:

1. Re-run `python3 scripts/arxiv_package_audit.py` — confirm PRTOE/note/tarball clean.
2. Optional clean-room: extract `papers/<name>/<name>.tar.gz` into empty dir → two `pdflatex` passes → 0 errors.
3. arXiv: New submission → category above → upload tarball members only (`submission/` contents).
4. Parallel or fallback: Zenodo → PDF + tarball → Publication/Preprint → CC BY 4.0 → **one DOI per paper** (never bundle).
5. After any edit: Zenodo “New version” on same record (supertrace already: 10.5281/zenodo.21763188); refresh `docs/arXivReady/` copies from `papers/`.

### D. Recommended post order (independence / risk)

| priority | package | why |
|---:|---|---|
| 1 | **supertrace-note** | Already SHIPPED; arXiv optional once gr-qc endorsement exists. |
| 2 | **lattice-tc-gap** | Gap note; no computation claimed; short. |
| 3 | **kination-tracking-note** | Pure negative classical result; short. |
| 4 | **bbn-eps-bound** | Chain-free constraint; Aver only. |
| 5 | **radio-lattice** | Longest; honest methanol/DM caveats already in text. |
| 6 | **neutrino-mbb** | After Fairbank thread + hep-ph endorsement. |

### E. Explicit non-actions (desk + owner)

- [ ] **Do not invent TeX** for Fairbank or any new short paper without closed science.
- [ ] **Do not invent endorsement** or claim any archive is open.
- [ ] **Do not** name the framework in any packaged `main.tex` (already clean).
- [ ] **Do not** put working notes in BibTeX `note` fields or leave empty `acknowledgments`.
- [ ] **Do not** paper open debts (Koide, hierarchy, IGMF, S₈ conversion, bounce, etc.) until named closures.

### F. Zenodo-only path (if arXiv endorsement is slow)

- [ ] Each READY package can ship as a Zenodo preprint **without** arXiv (supertrace precedent).
- [ ] Still one record per paper; PDF + source tarball; CC BY 4.0.
- [ ] Communities optional/curator-gated — DOI + Scholar indexing are the value.

---

## 6. Sources consulted

- `scripts/arxiv_package_audit.py` (ran 2026-08-03)
- `docs/working_logs/_PACKAGE_AUDIT.md` (rewritten by audit)
- `docs/arXivReady/README.md`
- `papers/README.md` + per-package `README.md`
- `docs/working_logs/_ARXIV_CANDIDACY.md` (Fairbank / 2026-08-03 owner note)
- `docs/working_logs/_ARXIV_READINESS.md` (desk snapshot; radio 6 pp in older note — **current pdfinfo = 7 pp**)

---

*End of report. No TeX invented. No endorsement claimed.*
