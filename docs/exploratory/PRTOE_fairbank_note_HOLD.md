# Fairbank note — internal status

*Companion to the letter itself: [`PRTOE_fairbank_note_draft.md`](../PRTOE_fairbank_note_draft.md).*

## Status: shareable as a draft

Addressee: **William Fairbank**. Letter may be shown as draft. H₀ fit is still not final; the letter says so.

**Evidence source.** Nested sampling (`PolyChord`, `cmp_prtoe_fixed`) ended 2026-07-20 after ~48 h without log(Z). Too expensive on current hardware. Standing comparison: Laplace-from-MCMC. MCMC chains that feed that estimate are the main calculation.

**Do not quote H₀ ≈ 69.9 as final.**

## Why H₀ is not final

Original chains used the ΛCDM helium fraction in recombination instead of the model’s YHe, leaving n_e slightly off where the H₀ effect is generated. Fixed 2026-07-17; model not yet rerun to a final result. Correction moves free-electron fraction in the damping tail — number may still move.

## Checks done

- Citations vs `BIBLIOGRAPHY.md` (2026-07-19)
- m_ββ window recomputed independently: **[0.04, 5.3] meV**
- nEXO / LEGEND-1000 / CUPID overlay unchanged
- P-2026-012 does not select ordering by itself
- Closed-form numbers under regression in `scripts/audit_math_pass.py`

## Operations

Live MCMC still being brought to convergence. Prior collapses from learning proposal covariance on an unconverged chain; relaunches seed widths from a better chain. Convergence claim not finished.

Graded configuration still slightly off the model’s onset identity (profiled freeze). That comparison grades a nearby point until the evidence-config rerun lands on the stated setup.

## Before send

1. Re-run H₀ comparison on corrected chains; replace the provisional number if it moves.
2. Recheck m_ββ floor against final dark-energy scale.
3. If the xenon matrix element firms up, update nEXO overlap.

## Sync 2026-07-27

*Letter text not changed by this note; content edits to the letter are listed for owner approval first.*

**H₀ instrument running.** Production pair restarted 2026-07-26 with provenance (archived prior samples, code state, launch environment). Both sampling; convergence pending. Letter caveat on H₀ ≈ 69.9 stands.

**m_ββ anchor source strengthened; value unchanged.** Letter table already has derived m₁ = 2.2599 meV (floor 0.038, ceiling 5.310 meV) → window [0.04, 5.3] meV. τ = ½ln2 gained a two-part candidate mechanism (conservation law + ground-state occupancy; lattice/external referees unchanged). No letter numbers move; mechanism in mathematical spine §23.2.

**Unchanged:** nested-sampling deferral, xenon ME watch, pre-send items 1 and 3. Item 2 satisfied by the letter’s table pending final DE scale.

## Terminology pass (2026-07-27, owner-authorized)

Field-language pass on letter and companions; content/numbers untouched. Letter changes:

1. “dyad’s nucleosynthesis window” → “electron-mass window at nucleosynthesis”
2. “genesis dilution ζ” → “dark-to-photon temperature ratio ζ”
3. m₁ = κ_m·ρ_inf¼ → m₁ = κ_m·ρ_Λ¼ (notation consistency)
4. Closing framing: house jargon stripped; enforced-charge / accounting-identity kept in plain English
5. Hyphen-as-dash fix

Companions: `PRTOE_neutrino_home.md`, `PRTOE_neutrino_sector.md`, `PRTOE_deuterium_row.md`. Staleness fixes: neutrino-sector retired scalar–Majoron merge reworded; deuterium §5 pre-correction Majoron clause aligned with corrected content (quark door shut quantitatively).

## Line-by-line pass (2026-07-28)

Eleven terminology/units/fluency edits; no numbers moved (details in git history of that date).

## Status section re-grade vs live chains (2026-07-28)

Letter is outward-facing; stale evidence claims are expensive. Live read of the running pair:

- Best fit 1377.89 (model) vs 1379.79 (ΛCDM) — nominally 1.9 log units the model’s way
- **Not claimed as a result:** 1.79× more samples on our chain; neither converged (ΛCDM R−1 ≈ 1.0; ours no R−1); best fit ≠ evidence
- **Honest position: wash, quotable neither way.** Standing number remains marginal SH0ES-conditional Laplace estimate

Edit *weakens* what the letter claims from numbers that currently favour the model — correct treatment if a lead cannot survive sampling asymmetry.

**Status unchanged: shareable as a draft.** Letter still discloses the transition-epoch offset (0.053 dex / ~28% in fluid mass) on its own.

---

## Discipline triage (2026-08-03)
**Grade:** superseded lineage
**Triage:** archive-ok / exploratory historical; not Failures unless a specific false claim needs ledgering
**Non-claims:** do not use as live derivation
