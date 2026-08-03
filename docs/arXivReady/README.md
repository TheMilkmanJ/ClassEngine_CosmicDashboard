# arXivReady — staged submission packages

One PDF + one source tarball per package. These are copies for easy access; the living
sources are in `papers/<name>/` at the repository root, and if a paper is ever edited
the copies here must be refreshed from there.

**2026-08-03:** shelf expanded beyond the original three to include lattice-tc-gap,
bbn-eps-bound, and kination-tracking-note. Hygiene reconfirmed same day.

| file | what it is | status |
|---|---|---|
| `supertrace-note.pdf` | *Two gravitational counting conditions for three generations are the same condition* — 3 pp, gr-qc | **SHIPPED** — [Zenodo DOI 10.5281/zenodo.21763188](https://zenodo.org/records/21763188); arXiv optional (gr-qc endorsement) |
| `neutrino-mbb.pdf` | *If the lightest neutrino mass is the dark-energy scale: a narrow window for neutrinoless double-beta decay* — 3 pp, hep-ph | **READY**; **owner submitted to William Fairbank (2026-08-03)** — packaging paused; do not invent a second Fairbank TeX. arXiv still needs hep-ph endorsement |
| `radio-lattice.pdf` | *A ratio-locked radio signature of a universal shift in the electron mass* — 7 pp, astro-ph.CO (+ .IM) | **READY** — astro-ph endorsement |
| `lattice-tc-gap.pdf` | *A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f=3 light fundamental flavours* — 2 pp, hep-lat | **READY** — hep-lat endorsement |
| `bbn-eps-bound.pdf` | *Primordial helium bounds on a leptonic electron-mass transition inside the BBN window* — 3 pp, astro-ph.CO | **READY** — astro-ph endorsement; optional dense ε_max(T_c) residual (bound at measured T_c) |
| `kination-tracking-note.pdf` | *A rotating condensate tracking V∝rⁿ cannot reach kination: exact EOS w=(n−2)/(n+2)* — 2 pp, gr-qc | **READY** — gr-qc endorsement |

The `.tar.gz` files are the exact arXiv source packages (`main.tex` + `main.bbl` where
used) — attach them as a second file on each Zenodo record so the source is archived
alongside the PDF.

**Not staged here:** `papers/fairbank-0nubb/` is **NOT_READY** (README only; duplicate of
neutrino-mbb arithmetic). Fairbank correspondence owns the neutrino-mbb package thread.

**Zenodo, short version:** zenodo.org → New upload → drag in the PDF (+ tarball) →
Resource type: Publication → Preprint → title/author/abstract → license CC BY 4.0 →
"Get a DOI now" → Publish. One record per paper, never bundled. Communities are optional
and curator-gated; the DOI and Google Scholar indexing are the real value.

Package verification / readiness records: `docs/working_logs/_ARXIV_READINESS.md`,
candidacy inventory: `docs/working_logs/_ARXIV_CANDIDACY.md`, live hygiene table:
`docs/working_logs/_PACKAGE_AUDIT.md` (`scripts/arxiv_package_audit.py`).
