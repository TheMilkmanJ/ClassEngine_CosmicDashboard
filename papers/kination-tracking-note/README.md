# A rotating condensate tracking $V \propto r^n$ cannot reach kination

**Status:** draft package (extracted 2026-08-02 from `docs/PRTOE_MATH_SPINE.md` §7 BKL block + `scripts/bounce_bkl_stiff_check.py`).

**Category:** gr-qc (optional hep-th)

**Claim:** For a rotating complex scalar with conserved charge tracking $V_{\mathrm{eff}}$ on $V\propto r^n$,
$w=(n-2)/(n+2)$ exactly; no finite polynomial reaches kination; freeze-out needs trans-Planckian amplitude.

**Framework independence:** High. Classical field equation + conserved $Q$. No PRTOE name, no bounce construction, no dark-energy story. Negative sector result only.

**Source corpus:**
- `docs/PRTOE_MATH_SPINE.md` §7 (BKL / tracking paragraphs)
- `scripts/bounce_bkl_stiff_check.py` (analytic + integration)

## Build

```bash
cd papers/kination-tracking-note
pdflatex main.tex
pdflatex main.tex
```

## Submission tarball

Clean room (tex only; no bbl needed with inline `thebibliography`):

```bash
mkdir -p submission
cp main.tex submission/
tar czf kination-tracking-note.tar.gz -C submission main.tex
```

## Endorsement

arXiv gr-qc endorsement required for first-time submitters (owner external task).
