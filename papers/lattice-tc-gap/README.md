# A well-posed gap in the two-color lattice literature: T_c/√σ for SU(2) with N_f = 3

**Author:** Justin Pulford (unaffiliated)  
**arXiv category:** hep-lat (optional hep-ph)  
**Status (2026-08-02):** TeX package ready for submission. **Red-team pass 2026-08-02.** Endorsement (hep-lat) is the external gate. No computation is claimed — this is a gap/motivation note.

## Relation to the framework

**Independent of the framework as a literature-gap paper.** The note argues that, to our knowledge (literature sweep, 2026-07), no published T_c/√σ is available for SU(2) with N_f=3 light fundamentals, and that the calculation is conventional and scientifically interesting for lattice QCD alone. An optional transparency paragraph (end of conclusion only) records a pre-registered numerical stake from a separate program; the stake is not the paper's result or purpose. **This note reports no lattice result.**

Corpus home: `docs/PRTOE_lattice_note.md`.

## What it claims

- The missing number (to our knowledge / dated literature sweep) and the four requirements for a serious determination.
- Why the gap matters without any dark-sector model (pseudo-real flavour pattern, conformal-window safety, cost).
- That discretization (staggered rooting vs Wilson) is part of the science, not a footnote.
- Explicit: **no lattice measurement, no continuum extrapolation, no claimed central value.**
- Optional transparency only: a demoted pre-registered stake and the sub-percent precision it would need — not the paper's purpose.

## Folder contents

- `main.tex` / `submission/main.tex` — source (inline bibliography).
- `main.pdf` — clean-room build.
- `lattice-tc-gap.tar.gz` — arXiv payload (`main.tex` only).

Verified by extracting the tarball into an empty directory and running two pdflatex passes.
