# `arxiv/` — submission-ready material only

**Nothing enters this folder until it is finished.** This is not a drafting area. A paper lives in
`docs/` while it is being written and is *copied* here only when its row in
`docs/working_logs/_ARXIV_READINESS.md` reads **READY**.

That rule exists so this folder answers one question at a glance: *what could be uploaded right
now?* If half-finished work accumulates here, it stops answering it.

## Current contents

**None.** No document is READY. See `docs/working_logs/_ARXIV_READINESS.md` for what each candidate
still needs — the short version is that no file yet has an abstract, a LaTeX source, or an external
bibliography, and all of them carry internal cross-references.

## Layout

```
arxiv/
  README.md          this file
  _template/         LaTeX skeleton to start each paper from
    main.tex
    refs.bib
  <paper-slug>/      one directory per submission, created when work starts
    main.tex
    refs.bib
    figs/
    NOTES.md         what this paper claims, what it deliberately leaves out
```

One directory per **submission**, not per source document. A paper may draw on several `docs/`
files; the point of the boundary is that each submission carries exactly one falsifiable claim.

## The rule that shapes everything here

**One narrow claim per paper.** A manuscript spanning the Hubble tension, the cosmological constant,
the hierarchy problem and the lepton mass relation will be reclassified to `physics.gen-ph` by
moderation, which is unappealable and effectively unreadable. The corpus's breadth is a strength
everywhere except at the submission boundary, where it is the single largest risk. Each paper here
states its one claim, cites the rest as context in a sentence, and stands alone.

## Build

```
cd arxiv/<paper-slug>
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

Before upload, check: the PDF builds from a clean checkout of *this directory only*; no `\input`
reaches outside it; every citation resolves; no internal identifiers survive anywhere in the text.
