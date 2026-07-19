# Overnight summary — the audit passes

## What ran

Three passes, on the 3-minute cadence you set.

**Pass 1** finished the file-by-file audit (batches 20–26).
**Pass 2** swept all 91 live forward docs by *defect class* rather than file by file — which
catches things a serial re-read cannot, because a class of error shows up as a pattern.
**Pass 3** is the math audit you asked for: every closed-form claim recomputed from its own inputs.

## The two things that need you

- **`01-orphan-portal-scale.md`** — the 3.5×10¹⁷ GeV "portal" in the two detection files appears
  nowhere else in the corpus and is twelve orders above every other portal number. I moved the
  reasoning onto sourced scales so nothing audience-facing depends on it, but the number itself
  needs your ruling: dead relic, mislabelled object, or something real and underived.
- **`02-P051-lock-slope-corrected.md`** — a registered prediction's slope was 2× its own
  derivative. Corrected; you should know it moved.

## What the math audit found

**56 checks, 56 pass** after the one correction. The harness is `scripts/audit_math_pass.py` —
run it any time; it fails loudly if a booked number drifts.

The corrected one: **P-2026-051's lock slope was exactly twice its own closure's derivative.**
The closure θ = (1 + A²/2)/9 differentiates to A/9 = √2/9 = 0.1571; the entry registered 2√2/9 =
0.3143 and called it "the closure's exact differential." Data moves from −0.31σ to −0.54σ off the
line — still consistent, so nothing structural falls, but the registered kill was pointing Belle II
at the wrong locus.

Three checks worth seeing because they came out better than they had to:

- **θ = 2/9 reproduces the real lepton mass ratios** — m_τ/m_e to 0.7 parts in 10⁴, m_μ/m_e to
  11 ppm. That is not a fit; it falls out of the parametrisation.
- **Σm_ν = 61.35 meV** recomputed from m₁ = 2.25 meV plus the NuFIT splittings, against the
  booked 61.4.
- **The Pauli finiteness condition is one statement, not two.** The corpus separately records
  "str[k₁] = 16·N_gen − 48 = 0 at N_gen = 3" and "the Standard Model alone gives −3". Sixteen is
  the Weyl-fermion count per generation *including* the right-handed neutrino; fifteen without.
  15×3 − 48 = −3. The Standard Model's deficit **is** the three missing ν_R, exactly.
- The soliton core radii now verify against Schive's published relation (7.14 and 0.71 pc against
  the booked 7 and 0.7). Those are the numbers corrected by 1000× earlier in the session, so the
  fix confirms itself independently.

## Coverage

`_audit_coverage.md` has the full ledger: 143 files, split into 91 live forward docs (full content
audit), 21 bannered archives (banner check only — their numbers are supposed to be old, and editing
them destroys the record), and 31 working logs (leak check — a log may hold a relative result but
must not export it as an absolute one, which is precisely how the BBN mis-price happened).

Other pass-2 results: **zero broken internal links**, **zero unresolved citation keys** (five were
missing, all in files I wrote earlier that evening — added), and the standing values are consistent
corpus-wide, with every divergence a documented one.
