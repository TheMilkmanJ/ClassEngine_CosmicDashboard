# Papers

One folder per paper. Each folder is self-contained: source, built PDF, a `submission/`
directory holding exactly the files arXiv receives, a tarball of that directory, and a
`README.md` saying what the paper claims and how it relates to the framework.

## Index

| folder | arXiv | pp | depends on the framework? |
|---|---|---|---|
| [`supertrace-note/`](supertrace-note/) | gr-qc | 3 | **No.** Entirely about published literature. |
| [`neutrino-mbb/`](neutrino-mbb/) | hep-ph | 3 | **No.** Its input is stated as a hypothesis. |
| [`radio-lattice/`](radio-lattice/) | astro-ph.CO, astro-ph.IM | 6 | **Motivated by it, does not rest on it.** |

All three are written so a reader who has never seen this corpus loses nothing. None of
them names the framework anywhere in its text — which is correct for arXiv, and is exactly
why this index exists.

Read in order of independence:

- **`supertrace-note/`** is the cleanest. Two published conditions, one page of algebra
  showing they are the same condition, no connection to anything else here. Easiest for a
  referee to check, and the natural one to send out first.
- **`neutrino-mbb/`** takes one number as a hypothesis and works out its consequence for
  neutrinoless double-beta decay. The framework independently reaches the same number,
  which is why the calculation was worth doing, but the paper never appeals to it.
- **`radio-lattice/`** is the one closest to the framework's own machinery. Even so, it
  treats the shift amplitude as a free parameter to be fitted rather than predicted, and
  it states in its own abstract that molecular lines already bound that amplitude ~35×
  more tightly than its rows do.

## Status

All three build clean and are packaged. Each `submission/` was tested by copying it into
an empty scratch directory and running pdflatex twice with nothing else present — which is
what arXiv does — giving 0 errors, 0 undefined references and 0 overfull boxes in every
case.

The remaining step for all three is the same and is not a technical one: arXiv requires an
endorsement for a first submission from an unaffiliated author.

## Two conventions worth keeping

**Do not put working notes in BibTeX `note` fields.** apsrev4-2 typesets them into the
reference list. Reference provenance belongs in `%` comments.

**Do not leave an empty `acknowledgments` environment.** revtex4-2 renders a bare
"ACKNOWLEDGMENTS" heading above the bibliography with nothing under it.

Both of these had reached the packaged tarballs before being caught on 2026-07-29.
