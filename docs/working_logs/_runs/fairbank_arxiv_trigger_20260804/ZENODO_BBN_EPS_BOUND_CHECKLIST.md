# Zenodo optional path — `bbn-eps-bound` (checklist only · no upload)

**Stamp:** 2026-08-04T18:14Z · trigger package `fairbank_arxiv_trigger_20260804`  
**Purpose:** owner can mint a public DOI **without** arXiv endorsement.  
**Desk does not upload.** This file is a checklist only.

**Dual stamp (do not collapse):**  
- **ARITHMETIC VERIFIED (internal)** — recompute ε 2σ = **3.196%** ≈ paper **3.20%** PASS  
  (`python3 papers/bbn-eps-bound/recompute_eps_bound.py` and staged copy).  
- **EXTERNAL WIN PENDING (no DOI)** — Zenodo publish is what would flip this to external win.  
  Package READY on disk ≠ public external win.

---

## Pre-flight (already true on 2026-08-04 re-audit)

| check | result |
|---|---|
| TeX package audit clean | **yes** (6/6; no PRTOE in tex) |
| Tarball members | `main.tex` + `recompute_eps_bound.py` |
| papers ↔ staged MD5 | **MATCH** (`bbn-eps-bound.tar.gz` / `.pdf`) |
| PDF pages | **3** |
| Claim fence | Aver Y_p only; EMPRESS non-result; no chain D/H; dense T_c curve not claimed |
| Dense ε_max(T_c) | optional residual — **not** a Zenodo hold |

---

## Files to upload (one record · never bundle)

| role | path |
|---|---|
| PDF | `docs/arXivReady/bbn-eps-bound.pdf`  
  *(or rebuild `papers/bbn-eps-bound/main.pdf`)* |
| Source archive | `docs/arXivReady/bbn-eps-bound.tar.gz`  
  *(or `papers/bbn-eps-bound/bbn-eps-bound.tar.gz`)* |

Optional third file: standalone `docs/arXivReady/recompute_eps_bound.py`  
(already inside the tarball; not required separately).

---

## Zenodo click-path (owner)

1. Sign in at [https://zenodo.org](https://zenodo.org) → **New upload**.  
2. Drag **PDF** + **matching `.tar.gz`** (two files for this paper only).  
3. **Resource type:** Publication → **Preprint**.  
4. **Title** (match paper):  
   *Primordial helium bounds on a leptonic electron-mass transition inside the BBN window*  
   (or exact title string on PDF front matter).  
5. **Creators:** Justin Pulford · unaffiliated.  
6. **Description / abstract:** paste from paper abstract (no framework name; no chain posteriors).  
7. **License:** **CC BY 4.0**.  
8. **Keywords (suggested):** Big Bang nucleosynthesis · helium · electron mass · varying constants · Aver  
9. **Related identifiers (optional):** Aver et al. arXiv:2010.04180 as “references”.  
10. Click **Get a DOI now** → review → **Publish**.  
11. Record DOI in owner status / `ForJustin/ARXIV_OWNER_CHECKLIST.md` / dual stamp surfaces:  
    change **EXTERNAL WIN PENDING (no DOI)** → **EXTERNAL WIN** with DOI string.  
12. **Do not** invent a DOI before Publish succeeds.

---

## What Zenodo is / is not

| is | is not |
|---|---|
| Public DOI + Google Scholar indexing | An arXiv listing |
| Enough for “external win” board grade on this arithmetic note | Endorsement for arXiv |
| Same pattern as supertrace (10.5281/zenodo.21763188) | A bundle of multiple papers |

arXiv still needs **astro-ph** endorsement separately if you want an arXiv ID later.  
Zenodo first does **not** block later arXiv; cite the DOI in the arXiv comments if useful.

---

## After publish (owner only)

1. Paste DOI into living dual-stamp lines (`docs/arXivReady/README.md`, `papers/bbn-eps-bound/README.md`, candidacy if you edit).  
2. Corrections = Zenodo **New version** on the **same** record (do not open a second record).  
3. Optional next: same checklist for **radio-lattice** (higher-leverage phenomenology twin).

---

## Explicit non-actions for desk

- No Zenodo upload from this package  
- No arXiv post  
- No Fairbank contact  
- No invent DOI / invent endorsement  

---

*Checklist only. EXTERNAL WIN still PENDING until owner Publish returns a real DOI.*
