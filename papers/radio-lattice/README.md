# A ratio-locked radio signature of a universal shift in the electron mass

**Author:** Justin Pulford (unaffiliated)
**arXiv category:** astro-ph.CO primary, astro-ph.IM cross-list
**Status:** submission-ready. Endorsement is the only remaining step.

## Relation to the framework

**Motivated by the framework, but written so it does not depend on it.**

The quantity ε is the fractional shift in the electron mass. In the corpus that shift is
the imprint of the electron-coupled scalar, and that is where the interest in it comes
from. The paper does not use any of that. It treats ε as a free amplitude to be fitted to
data rather than predicted, and says so in the abstract. Every weight in the pattern comes
from atomic physics alone.

So the claim stands or falls on its own. If the framework turns out to be wrong, this
paper is unaffected; if the pattern is falsified, the framework loses a channel but the
paper was never resting on it.

Corpus home for the underlying mechanism: `docs/PRTOE_me_mechanism_math.md` and
`docs/PRTOE_lattice_note.md`.

## What it claims

Each radio observable depends on the electron mass through a different power, so a single
universal shift moves them in fixed ratios that are independent of the shift's size:

| observable | weight in ε |
|---|---|
| hydrogen 21 cm hyperfine frequency | +2 |
| radio recombination lines | +1 |
| electron column from a dispersion measure | −1 |
| synchrotron characteristic frequency, fixed Lorentz factor | −1 |
| Faraday rotation | −2 |

One entry is convention-dependent and the paper says so outright: the synchrotron row
reads −3 if the emitting particle's energy is held fixed instead of its Lorentz factor,
and the choice has to be declared before the row is read.

The pattern separates a varying electron mass from a varying fine-structure constant
arithmetically, since α enters the 21 cm frequency at fourth order but does not enter the
dispersion delay at all. The hydrogen-to-deuterium hyperfine ratio is an internal control:
α and the electron mass cancel from it identically.

Read through the pattern, the tightest existing 21 cm comparison gives
|ε| < 1.4 × 10⁻⁵ at 2σ over 1.17 < z < 1.56, limited by systematics rather than precision.

## The honest caveat, which is in the text

Molecular methanol lines already bound ε roughly 35× more tightly. The rows in this paper
therefore do **not** improve the amplitude, and the paper states this rather than burying
it. What the pattern buys is the ratio structure and the degree-of-freedom count: one row
leaves 1 − 1 = 0 degrees of freedom after fitting ε, two rows leave 2 − 1 = 1. That count
carries no σ. A single band deviating from its assigned weight falsifies the pattern.

## Folder contents

- `main.tex`, `refs.bib` — source. 31 bibliography entries, all cited, no orphans.
- `main.pdf` — 7 pp, 312 KB.
- `submission/` — exactly what arXiv receives: `main.tex` + `main.bbl`, nothing else.
- `radio-lattice.tar.gz` — that directory, 20 KB.
- `NOTES.md` — working notes.

Verified by building `submission/` in an empty scratch directory with two pdflatex passes
and nothing else, which is what arXiv does: 0 errors, 0 undefined references, 0 overfull
boxes.

Provenance for individual references is kept as `%` comments in `refs.bib`, not in BibTeX
`note` fields — apsrev4-2 typesets `note` fields into the reference list.
