# arXivReady — the three submission-ready papers

One PDF + one source tarball per paper. These are copies for easy access; the living
sources are in `papers/<name>/` at the repository root, and if a paper is ever edited
the copies here must be refreshed from there.

| file | what it is | post where |
|---|---|---|
| `supertrace-note.pdf` | *Two gravitational counting conditions for three generations are the same condition* — 3 pp, gr-qc | **Post first** (cleanest, fully standalone) |
| `neutrino-mbb.pdf` | *If the lightest neutrino mass is the dark-energy scale* — 3 pp, hep-ph | Second |
| `radio-lattice.pdf` | *A ratio-locked radio signature of a universal shift in the electron mass* — 6 pp, astro-ph.CO | Third |

The `.tar.gz` files are the exact arXiv source packages (`main.tex` + `main.bbl` where
used) — attach them as a second file on each Zenodo record so the source is archived
alongside the PDF.

**Zenodo, short version:** zenodo.org → New upload → drag in the PDF (+ tarball) →
Resource type: Publication → Preprint → title/author/abstract → license CC BY 4.0 →
"Get a DOI now" → Publish. One record per paper, never bundled. Communities are optional
and curator-gated; the DOI and Google Scholar indexing are the real value.

All three were verified before packaging: clean-room builds (0 errors / 0 undefined /
0 overfull, built exactly the way arXiv builds them), every numerical claim re-derived
independently (15/15, 8/8, and full symbolic verification respectively), and the
rendered PDFs read end-to-end. Verification records: `docs/working_logs/_ARXIV_READINESS.md`.
