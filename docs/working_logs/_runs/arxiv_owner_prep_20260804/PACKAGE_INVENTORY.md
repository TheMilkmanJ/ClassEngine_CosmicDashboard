# Package inventory — arXiv / Fairbank owner prep (2026-08-04)

**Lane:** Owner Fairbank / arXiv prep.  
**Hard rule:** packages are **READY on disk**; **owner HOLD** until Fairbank replies.  
**Desk does not:** post to arXiv · email Fairbank · invent endorsement · invent second Fairbank TeX · touch MCMCs / PolyChord.

Living sources: `papers/<name>/`. Staged PDF + tarball: `docs/arXivReady/`.  
Hygiene: `scripts/arxiv_package_audit.py` → `docs/working_logs/_PACKAGE_AUDIT.md`.  
Candidacy: `docs/working_logs/_ARXIV_CANDIDACY.md`.  
**Trigger refresh:** `docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/` (OWNER_SHIP_NOW · REPORT · Zenodo checklist).

---

## Verification stamp (this run)

| check | result |
|---|---|
| `python3 scripts/arxiv_package_audit.py` | **6/6** TeX packages clean (PRTOE / note-field / tarball) — re-run 2026-08-04T18:14Z → `fairbank_arxiv_trigger_20260804/arxiv_package_audit.log` |
| papers ↔ `docs/arXivReady/` tarball **and** PDF MD5 | **MATCH** all six |
| `pdfinfo` pages (papers + staged) | supertrace 3 · neutrino-mbb 3 · radio-lattice **7** · lattice-tc-gap 2 · bbn-eps-bound 3 · kination 2 |
| `python3 papers/bbn-eps-bound/recompute_eps_bound.py` | **PASS** ε 2σ = 3.196% ≈ paper 3.20% — dual stamp: **ARITHMETIC VERIFIED (internal)** / **EXTERNAL WIN PENDING (no DOI)** |
| bbnfix booking gate | **REFUSED** — lcdm R−1 0.086466 N=20409 · dyad R−1 0.128943 N=20302 · not a READY-package hold |
| `scripts/prepare_publication_validation.sh` | print-only checklist; **not executed** as a full CLASS/Cobaya/PolyChord run (would touch heavy lanes) |
| Stray file | `docs/arXivReady/main.pdf` = **duplicate of** `bbn-eps-bound.pdf` (same MD5); ignore for upload |

---

## Inventory table (every shippable / non-shippable object)

| # | package path | staged (`docs/arXivReady/`) | status | archive | claim fence (one-liner) | kill / non-claim conditions | external gate |
|---:|---|---|---|---|---|---|---|
| 1 | `papers/supertrace-note/` | `supertrace-note.{pdf,tar.gz}` | **SHIPPED** Zenodo [10.5281/zenodo.21763188](https://zenodo.org/records/21763188) | gr-qc (optional) | Navarro-Salas anomaly cancellation and Pauli/Visser finiteness are the **same** constraint when conventional scalars drop out; they **differ** on the Higgs sector | Not a new generation-counting discovery; ξ=1/6 is an extra naturalness input if used; do not present two independent gravitational arguments for three generations | Optional gr-qc endorsement → arXiv mirror; corrections = Zenodo “New version” only |
| 2 | `papers/neutrino-mbb/` | `neutrino-mbb.{pdf,tar.gz}` | **READY_PACKAGE** · **with Fairbank (owner submit 2026-08-03)** · packaging **paused** · **READY not posted** | hep-ph | Hypothesis m₁ = ρ_Λ¼ ≃ 2.25 meV + normal ordering + NuFIT ⇒ m_ββ ∈ [0.04, 5.30] meV; useful edge vs min-NO ceiling **3.69 meV** | Lower edge unprotected (knife-edge); null constrains nothing; detection **>5.30 meV** kills hypothesis; **do not** claim framework derivation of m₁; **do not** invent second Fairbank TeX | **hep-ph endorsement** (Fairbank thread is live path). Full honesty: [`../neutrino_full_honesty_20260804/REPORT.md`](../neutrino_full_honesty_20260804/REPORT.md) |
| 3 | `papers/radio-lattice/` | `radio-lattice.{pdf,tar.gz}` | **READY_PACKAGE** | astro-ph.CO (+ .IM) | Universal m_e shift imprints five radio observables at fixed weights +2:+1:−1:−1:−2; pattern discriminates varying-α; only 21 cm + Faraday presently measurable (σ_ε = σ/√8) | Methanol already ~35× tighter on amplitude (stated); DM row demoted (ε–DM degeneracy); template not survey; ε free / no mechanism; single band off weight falsifies pattern | **astro-ph endorsement** |
| 4 | `papers/lattice-tc-gap/` | `lattice-tc-gap.{pdf,tar.gz}` | **READY_PACKAGE** | hep-lat (opt. hep-ph) | Literature gap: no published T_c/√σ for SU(2), N_f=3 light fundamentals; calculation conventional and scientifically interesting alone | **No lattice result claimed**; stake is transparency only; “to our knowledge / dated sweep” not absolute omniscience | **hep-lat endorsement** |
| 5 | `papers/bbn-eps-bound/` | `bbn-eps-bound.{pdf,tar.gz}` (+ staged `recompute_eps_bound.py`) | **READY_PACKAGE** · dual: **ARITHMETIC VERIFIED (internal)** / **EXTERNAL WIN PENDING (no DOI)** | astro-ph.CO | Free ε, Aver Y_p ⇒ **ε < 3.2% (2σ)** at measured T_c ≈ 179 keV for a leptonic m_e turn-on inside BBN window | EMPRESS cannot bound ε (ε=0 already +2.9σ); no D/H derivative bound; no chain-dependent D/H prediction; dense ε_max(T_c) curve **not produced** (optional residual, not a hold) | **astro-ph endorsement** (same as radio-lattice); optional Zenodo checklist: `../fairbank_arxiv_trigger_20260804/ZENODO_BBN_EPS_BOUND_CHECKLIST.md` |
| 6 | `papers/kination-tracking-note/` | `kination-tracking-note.{pdf,tar.gz}` | **READY_PACKAGE** | gr-qc (opt. hep-th) | Rotating condensate tracking V∝rⁿ has exact w=(n−2)/(n+2); no polynomial n reaches kination; freeze-out needs trans-Planckian amplitude | Negative-sector only; no bounce/genesis narrative; optional deeper Q-ball lit not required for claim | **gr-qc endorsement** |
| 7 | `papers/fairbank-0nubb/` | *(not staged)* | **NOT_READY** | — | README only — duplicate of neutrino-mbb arithmetic + model-tied + chain-dependent layers | **Do not invent TeX**; ship claim via neutrino-mbb only | n/a |

**Source notes (not packages):**  
`docs/PRTOE_fairbank_note_draft.md` — CORPUS_ONLY personal letter (owner ↔ Fairbank).  
`docs/exploratory/PRTOE_fairbank_note_HOLD.md` — exploratory HOLD companion (do not quote H₀ as final).

---

## Artifact contents (verified 2026-08-04)

| package | PDF pages | tarball members | papers MD5 = staged? |
|---|---:|---|---|
| supertrace-note | 3 | `./main.tex` | yes |
| neutrino-mbb | 3 | `./main.tex`, `./main.bbl` | yes |
| radio-lattice | 7 | `./main.tex`, `./main.bbl` | yes |
| lattice-tc-gap | 2 | `./main.tex` | yes |
| bbn-eps-bound | 3 | `main.tex`, `recompute_eps_bound.py` | yes |
| kination-tracking-note | 2 | `main.tex` | yes |
| fairbank-0nubb | — | no tarball | n/a |

Upload materials for owner:  
`docs/arXivReady/<name>.pdf` + `docs/arXivReady/<name>.tar.gz`  
(or rebuild from `papers/<name>/submission/`).

---

## Status rollup

| status | count | names |
|---|---:|---|
| **SHIPPED** | 1 | supertrace-note (Zenodo) |
| **READY_PACKAGE** | 5 | neutrino-mbb, radio-lattice, lattice-tc-gap, bbn-eps-bound, kination-tracking-note |
| **NOT_READY** | 1 | fairbank-0nubb |
| **New PAPER_CANDIDATE** (docs shelf) | **0** | 2026-08-03 arXiv-ready pass |

**Owner HOLD:** no arXiv post until Fairbank replies on the neutrino-mbb thread (or owner explicitly chooses a parallel archive path — see `OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md`).

---

## Kill-switch summary (what would force a package hold)

| package | hard kill on claim | soft residual (not a hold) |
|---|---|---|
| supertrace-note | algebra error in N_½ reduction / scalar-sector distinction | optional arXiv mirror only |
| neutrino-mbb | wrong NuFIT arithmetic; claim m₁ as derived without stating hypothesis | lower-edge fragility (already stated) |
| radio-lattice | claim improved |ε| vs methanol; claim DM row as free measurement | none blocking |
| lattice-tc-gap | publish a central T_c/√σ as *this note’s result* | literature may close gap later |
| bbn-eps-bound | use EMPRESS as ε upper limit; quote chain D/H | dense T_c map optional |
| kination-tracking-note | claim kination reachable for finite polynomial n under tracking | deeper lit optional |
| fairbank-0nubb | inventing TeX | permanently NOT_READY as separate paper |

---

*Inventory filed 2026-08-04 · re-verified 2026-08-04T18:14Z (fairbank_arxiv_trigger). No arXiv post. No Fairbank email. No MCMCs.*
