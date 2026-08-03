# fairbank-0nubb — **NOT_READY**

**Source draft:** `docs/PRTOE_fairbank_note_draft.md`  
**Assessed:** 2026-08-02 / 2026-08-03  
**Verdict:** **NOT_READY** as a separate arXiv short paper.  
**No `main.tex`.** Do not invent TeX for a duplicate or chain-dependent claim.

## Why not

The draft is a personal experimental letter (to W. Fairbank) wrapping three layers of material:

1. **Standard m_ββ / ton-scale experimental framing** under a fixed lightest mass  
   (window [0.04, 5.3] meV, minimal-ordering ceiling 3.69 meV, nEXO 4.7–5.3 meV overlap,
   Ba-tagging likelihood vs discrimination, nulls do not kill).  
   This layer is **already the entire content** of the ready package  
   [`papers/neutrino-mbb/`](../neutrino-mbb/) (READY_PACKAGE; hep-ph endorsement only).  
   A second short paper with the same arithmetic would be a duplicate, not a new extract.

2. **Model-tied scaffolding** that cannot ship under the “strip framework name / one
   checkable claim” rule: unified dark fluid, ε = 27α/5π, Majorana as a *structural*
   necessity of a lepton-number-violating mass mechanism, recombination m_e shift as the
   reason cosmological Σm_ν bounds “relax,” BBN/deuterium decomposition, house prediction
   IDs (P-2026-012, ANN-2026-025, …). None of that is standard m_ββ framing; all of it
   needs the framework or is already out of scope for a short hep-ph note.

3. **Unconverged-chain cosmology** that the draft itself forbids quoting: H₀ ≈ 69.9,
   best-fit Δχ² fragments, multi-rank basin disagreement, acceptance rates, Laplace ΔlnZ
   caveats (Status section, “Where those chains stand as of 28 July…”). A short extract
   that keeps those numbers violates the governing rule; one that drops them has nothing
   left beyond layer (1).

## Cross-consistency with `papers/neutrino-mbb`

| quantity | Fairbank draft | neutrino-mbb package |
|---|---|---|
| m₁ input | 2.25 meV (model / ρ_Λ¼) | 2.25 meV as **hypothesis** |
| m_ββ window | [0.04, 5.3] meV | [0.04, 5.30] meV |
| terms (|Uei|² mi) | (1.52, 2.67, 1.10) meV | same |
| Σm_ν | 61.4 meV | 61.3 meV |
| min. NO ceiling | 3.69 meV | 3.69 meV |
| nEXO / LEGEND / CUPID | 4.7–20.3 / 9–21 / 12–34 meV | same |
| phase fractions | 10.8% / 69% / 31.7% | 10.8% / 69.1% / 31.8% |

Numbers match. The published-facing packaging of this physics **is** neutrino-mbb; Fairbank
is the corpus letter that motivated packaging it.

## What would change the verdict

- **Not** “rewrite Fairbank as TeX with PRTOE stripped” — that is neutrino-mbb again.  
- A *new* short paper only if Fairbank gained a **distinct, chain-free claim** that
  neutrino-mbb does not already make (e.g. an endorsed experimental reach revision from
  the nEXO/Ba-tagging side that changes the discrimination table in a way worth a
  separate experimental note). Until then: keep the draft as CORPUS_ONLY; ship via
  `papers/neutrino-mbb/` when hep-ph endorsement exists.

## Folder policy

This directory holds only this README. No `main.tex`, no `submission/`, no tarball.
See `docs/working_logs/_ARXIV_CANDIDACY.md` (2026-08-02/03 Fairbank addendum).
