# Two gravitational counting conditions for three generations are the same condition

**Author:** Justin Pulford (unaffiliated)
**arXiv category:** gr-qc
**Status:** submission-ready. Endorsement is the only remaining step.

## Relation to the framework

**None. This one is fully independent.**

Of the three papers this is the only one with no connection to the framework at all. It is
entirely about two conditions already in the published literature — Navarro-Salas (CQG
2024) on conformal anomaly cancellation, and Pauli's finiteness requirement in the form
Visser (2002) records it. The argument is a page of algebra over their equations.

Nothing in it depends on the framework being right, and nothing in the framework depends
on it. It could have been written by someone who had never seen the rest of this corpus.
If any paper here should go out first, it is this one, because it is the least entangled
and the easiest for a referee to check.

The corpus does use the same supertrace identity — see `docs/PRTOE_quantum_gravity.md`,
verified by `scripts/supertrace_k1_verify.py` (16 controls, all passing) — but the paper
neither cites nor needs that.

## What it claims

Two conditions of gravitational origin have both been used to argue for three generations,
and they are often quoted together as independent corroboration. They are not independent.

Eliminating the auxiliary scalar count N_ξ from the two anomaly conditions leaves

    N_½ = 4N₁ − N₀/2

and the finiteness condition str[k₁] = 0 evaluates to

    N_½ = 4N₁

These coincide whenever conventional scalars drop out of the count — either at N₀ = 0, or
at the conformal coupling ξ = 1/6. Both are then solved by N_½ = 48 at N₁ = 12: sixteen
Weyl fields per generation, three times over. So the agreement is arithmetic, not
evidential, and should not be read as two independent gravitational arguments for the
observed generation number.

The conditions *are* distinguishable, and the Higgs is what distinguishes them. Anomaly
cancellation forbids a fundamental Higgs doublet and requires thirty-six additional
fields; the finiteness condition admits the doublet as a conformally coupled field and
requires nothing new. That row of the comparison table is the content of the note — not
the row where the two agree.

## What is explicitly not claimed

The generation-counting result is Navarro-Salas's; the finiteness condition is Pauli's.
Neither is presented as new. What is new is the observation that they are one constraint,
and the identification of the scalar sector as what separates them.

## Folder contents

- `main.tex` — source. Uses an inline `thebibliography` with 5 references, so there is no
  `.bib` file and the paper never calls `\bibliography`. A `main.bbl` may still appear here
  as a leftover from the build harness running BibTeX unconditionally; it is unused, and it
  is deliberately **not** in `submission/`.
- `main.pdf` — 3 pp, 228 KB.
- `submission/` — exactly what arXiv receives: `main.tex` alone.
- `supertrace-note.tar.gz` — that directory, 8 KB.

Verified by building `submission/` in an empty scratch directory with two pdflatex passes
and nothing else: 0 errors, 0 undefined references, 0 overfull boxes.
