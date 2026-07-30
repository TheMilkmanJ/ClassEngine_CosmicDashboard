# If the lightest neutrino mass is the dark-energy scale

**Author:** Justin Pulford (unaffiliated)
**arXiv category:** hep-ph
**Status:** submission-ready. Endorsement is the only remaining step.

## Relation to the framework

**Framework-independent as written. The framework is why the value was interesting, not
why the paper is true.**

The paper's single input is m₁ = ρ_Λ^(1/4) ≃ 2.25 meV, and it is introduced as a
hypothesis — the sharpest arithmetic version of a long-noted numerical coincidence — not
as something derived. The paper explicitly declines to propose a mechanism.

Separately, the corpus reaches m₁ = 2.24 meV and Σm_ν = 61.3 meV by its own route
(prediction registry P-2026-012). That agreement is what made the calculation worth doing.
But a reader who has never heard of the framework loses nothing: the hypothesis is stated
in one equation and everything follows from it plus standard oscillation parameters.

## What it claims

Taking m₁ = 2.25 meV with normal ordering and current oscillation parameters, the three
contributions to the effective Majorana mass are (1.52, 2.67, 1.10) meV, giving

- m_ββ ∈ [0.04, 5.30] meV
- Σm_ν = 61.3 meV

The lower edge is not protected by any symmetry. It is nonzero only because the middle
term exceeds the other two combined by 0.045 meV, so the three phasors cannot close. That
same near-cancellation makes m_ββ an unusually steep function of m₁, and the paper says so
rather than quoting the lower edge as though it were robust.

The useful statement is the upper edge. Minimal normal ordering (m₁ = 0) cannot exceed
3.69 meV at any choice of Majorana phases, while this hypothesis reaches 5.30 meV and
occupies the interval between them 32% of the time. One planned experiment's projected
reach falls inside that interval.

- A detection between 3.69 and 5.30 meV would be hard to attribute to minimal ordering.
- A detection above 5.30 meV excludes the hypothesis outright.
- A null result constrains nothing, at any sensitivity. The paper states this plainly.

## Folder contents

- `main.tex`, `refs.bib` — source. 11 bibliography entries.
- `main.pdf` — 3 pp, ~249 KB (after stripping printed BibTeX `note` audit text).
- `submission/` — exactly what arXiv receives: `main.tex` + `main.bbl`, nothing else.
- `neutrino-mbb.tar.gz` — that directory, ~8 KB. Rebuild whenever `refs.bib` changes so the
  shipped `main.bbl` matches the source.

Verified by extracting `neutrino-mbb.tar.gz` into an empty scratch directory and running two
pdflatex passes with nothing else: 0 errors, 0 undefined references, 0 overfull boxes.

Provenance for individual references is kept as `%` comments in `refs.bib`, not in BibTeX
`note` fields — apsrev4-2 typesets `note` fields into the reference list. Comments must not
contain bare `@…` tokens; BibTeX still tokenizes them.

One packaging note worth keeping: `CUPID2019` is `@misc`, not `@article`. A design report
has no journal locator, and as `@article` apsrev4-2 throws 13 errors trying to match a
missing journal against its abbreviation table.
