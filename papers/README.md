# Papers

One folder per paper. Each folder is self-contained: source, built PDF, a `submission/`
directory holding exactly the files arXiv receives, a tarball of that directory, and a
`README.md` saying what the paper claims and how it relates to the framework.

## Index

| folder | arXiv | pp | depends on the framework? | desk status (2026-08-02) |
|---|---|---|---|---|
| [`supertrace-note/`](supertrace-note/) | gr-qc | 3 | **No.** Entirely about published literature. | **Published** on Zenodo ([DOI 10.5281/zenodo.21763188](https://zenodo.org/records/21763188)). arXiv still open if endorsement materialises. |
| [`neutrino-mbb/`](neutrino-mbb/) | hep-ph | 3 | **No.** Its input is stated as a hypothesis. | TeX package ready. External gate: hep-ph endorsement. |
| [`radio-lattice/`](radio-lattice/) | astro-ph.CO, astro-ph.IM | 6 | **Motivated by it, does not rest on it.** | TeX package ready. External gate: astro-ph endorsement. |
| [`lattice-tc-gap/`](lattice-tc-gap/) | hep-lat | 2 | **No** as a gap note. Optional transparency stake is one paragraph. | TeX package ready. External gate: hep-lat endorsement. |

All are written so a reader who has never seen this corpus loses nothing. None of them names
the framework in its TeX — which is correct for arXiv. Full candidacy inventory:
`docs/working_logs/_ARXIV_CANDIDACY.md`.

Read in order of independence:

- **`supertrace-note/`** is the cleanest. Two published conditions, one page of algebra
  showing they are the same condition. Public on Zenodo.
- **`lattice-tc-gap/`** is a literature-gap note: no published T_c/√σ for SU(2) N_f=3 light
  fundamentals; the computation is conventional and missing.
- **`neutrino-mbb/`** takes one number as a hypothesis and works out its consequence for
  neutrinoless double-beta decay. The paper never appeals to the framework.
- **`radio-lattice/`** is the one closest to the framework's own machinery. Even so, it
  treats the shift amplitude as a free parameter to be fitted rather than predicted, and
  it states that molecular lines already bound that amplitude ~35× more tightly than its rows do.

## Status (desk readiness, 2026-08-02)

All **TeX packages** below build clean and are packaged. Each `submission/` was tested by
copying it into an empty scratch directory and running pdflatex twice with nothing else
present — which is what arXiv does — giving 0 errors in every case.

| paper | TeX package ready? | Content holds remaining? | External gate |
|---|---|---|---|
| supertrace-note | **Yes** — `main.tex` only; 3 pp | None. Public on Zenodo 2026-08-02. | arXiv: gr-qc endorsement (optional) |
| neutrino-mbb | **Yes** — `main.tex` + `main.bbl`; 3 pp | None blocking. | hep-ph endorsement |
| radio-lattice | **Yes** — `main.tex` + `main.bbl`; 6 pp | None. DM demotion is in the text. | astro-ph endorsement |
| lattice-tc-gap | **Yes** — `main.tex` only; 2 pp | None as a gap note (no lattice result claimed). | hep-lat endorsement |

**Do not invent endorsement.** No arXiv endorsement is claimed here. The remaining step for
arXiv for the two unpublished papers is the same and is not a technical one: arXiv requires
an endorsement for a first submission from an unaffiliated author, **per archive**.

### radio-lattice: DM demotion reconciled

An earlier owner ruling marked radio-lattice **NOT arXiv-ready** after the dispersion-measure
row was demoted (a constant ε is exactly degenerate with the fitted DM). That content hold
was closed by **rewriting the claim**, not by promoting the row:

- the paper states the degeneracy and treats only 21 cm + Faraday as presently measurable
  (σ_ε = σ/√8); σ/√11 is an upper bound, not a forecast
- the five-weight *pattern* is untouched; what dropped is how many rows can be turned into
  a measurement today
- methanol's tighter amplitude bound is stated outright; the paper claims the ratio structure,
  not an improved |ε|

So: **technical package ready; no remaining content hold; external gate is endorsement only.**
Full drafting record: `docs/working_logs/_ARXIV_READINESS.md`. Current snapshot at the top of
that file.

## Two conventions worth keeping

**Do not put working notes in BibTeX `note` fields.** apsrev4-2 typesets them into the
reference list. Reference provenance belongs in `%` comments.

**Do not leave an empty `acknowledgments` environment.** revtex4-2 renders a bare
"ACKNOWLEDGMENTS" heading above the bibliography with nothing under it.

Both of these had reached the packaged tarballs before being caught on 2026-07-29.
Verified 2026-08-02: no live `note =` fields in `refs.bib`; no `\bibinfo{note}` in shipped
`.bbl` files; no empty acknowledgments; no "PRTOE" string in any `main.tex`.
