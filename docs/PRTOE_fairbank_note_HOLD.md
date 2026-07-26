# Fairbank note status

*Internal status note. `PRTOE_fairbank_note_draft.md` is the letter itself.*

## Status: shareable as a draft

Addressee confirmed: **William Fairbank**. The letter can be shown now as draft text. The only
number that remains not yet final is the H₀ fit, and the letter already says so.

**What the current evidence comes from.** Nested sampling (`PolyChord`, `cmp_prtoe_fixed`) ended on
2026-07-20 after about 48 hours without a log(Z) value. On this hardware that run is too expensive
to continue, so the standing comparison is a Laplace-from-MCMC estimate. The MCMC chains that feed
that estimate are the main calculation now.

**One thing not to do:** quote H₀ ≈ 69.9 as a final measured value. In conversation, it is still
not yet final.

## Why H₀ is not yet final

The original chains used the ΛCDM helium fraction in the recombination code instead of the model's
own value, which left the free-electron fraction slightly off exactly where the H₀ effect is
generated. That issue was corrected on 2026-07-17, but the model has not yet been rerun to a final
result.

The correction matters because it changes the free-electron fraction in the damping tail, which is
where the H₀ shift comes from. So the number may still move.

## What has been checked

- The citations were checked against `BIBLIOGRAPHY.md` on 2026-07-19.
- The `m_ββ` window was recomputed independently and is `[0.04, 5.3]` meV.
- The comparison with nEXO, LEGEND-1000, and CUPID is unchanged in the draft.
- The registry note `P-2026-012` does not select the ordering by itself.
- Every closed-form number in the letter is under regression in `scripts/audit_math_pass.py`.

## Current operational note

The live MCMC work is still being repaired for convergence. Some chains previously collapsed when
the proposal covariance was learned from a chain that had not converged. The relaunches seed the
proposal widths from a better chain, but the convergence claim itself is not finished.

The graded configuration also still sits slightly away from the model's onset identity. That means
the current comparison grades a point near the model, not the exact stated configuration.

## Before it goes out

1. Re-run the H₀ comparison on the corrected chains and replace the not-yet-final number if it moves.
2. Recheck the `m_ββ` floor against the final dark-energy scale.
3. If the xenon matrix element firm ups, update the nEXO overlap accordingly.
