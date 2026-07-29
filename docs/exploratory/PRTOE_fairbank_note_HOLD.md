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

## Status sync (2026-07-27)

*Dated addendum; the letter's text is untouched — any change to the letter itself
is listed here first for the owner's approval.*

**The H₀ instrument is running.** The "live MCMC work being repaired" note above
is superseded: the production pair was restarted fresh on 2026-07-26 on the
current code with full provenance (the archived prior samples, the code state at
restart, and the launch environment are recorded in the chains directory and the
repository history). Both chains are sampling; convergence is pending, and the
letter's own caveat — do not quote H₀ ≈ 69.9 as final — stands unchanged until
they report. The onset-identity offset flagged above is now tracked as its own
work item (the evidence-configuration rerun), so the eventual comparison grades
the model's stated configuration rather than a nearby point.

**The m_ββ anchor's source strengthened, value unchanged.** The letter's table
already carries the derived m₁ = 2.2599 meV column (floor 0.038 meV, ceiling
5.310 meV), so the quoted window [0.04, 5.3] meV stands. Since the last check,
the ratio sourcing that value (τ = ½ln2) gained a two-part candidate mechanism —
a conservation law fixing one component (computed) and a ground-state occupancy
condition fixing the other (candidate) — with its external referees unchanged
(the SU(2), N_f = 3 lattice campaign, now carrying five verdicts; the registered
deviation lock; the tau-lepton mass at ≲1.4 ppm). No number in the letter moves;
the mechanism's standing is recorded in the mathematical spine (§23.2).

**Unchanged:** the nested-sampling deferral (hardware), the xenon matrix-element
watch, and the pre-send checklist — items 1 and 3 remain open; item 2 is
satisfied by the letter's existing table pending the final dark-energy scale.

## Terminology pass on the letter, owner-authorized (2026-07-27)

*The owner ordered a field-language pass on the letter and its companion files
in chat on 2026-07-27 ("de-jargon the neutrino files and the fairbank files...
they need to be in field-physics language"). That order supersedes the
list-first protocol for terminology only; content and numbers are untouched.
The five changes made to the letter itself:*

1. "the dyad's nucleosynthesis window" → "the electron-mass window at
   nucleosynthesis" (decomposition table row; same physics, house name removed).
2. "the genesis dilution ζ" → "the dark-to-photon temperature ratio ζ".
3. "m₁ = κ_m·ρ_inf¼" → "m₁ = κ_m·ρ_Λ¼" — a notation consistency fix: the
   letter's own earlier section already writes m₁ = ρ_Λ¼; ρ_inf is the
   corpus-internal name for the same constant floor density.
4. The closing framing paragraph: "in this model's notation" and
   "collateralized charge" removed; the enforced-charge/accounting-identity
   framing and the bank line kept in plain English.
5. One ASCII hyphen-as-dash corrected to an em dash ("not exotic — roughly").

*Companion files brought to the same standard in the same pass:
PRTOE_neutrino_home.md, PRTOE_neutrino_sector.md, PRTOE_deuterium_row.md
(the file the letter's trace note points to for the BBN decomposition).
Two staleness fixes made in the companions and reported to the owner in chat:
the neutrino-sector file asserted the retired scalar–Majoron identification
(the coupling argument stands without it and was reworded to its own feet),
and the deuterium row's closing sentence in §5 still carried the pre-correction
"surrendering the Majoron identification" clause, contradicting the corrected
parenthetical directly above it; it now states the corrected content — the
quark door is shut quantitatively, not by symmetry.*

## Full line-by-line pass, owner-ordered (2026-07-28)

*The owner ordered a complete read-through with fixes ("actually go through the
file"). Eleven changes, all terminology, units, or fluency — no numbers moved:*

1. "the registered collision result" → "a registered prediction-collision test"
   (the last house-protocol term in the letter).
2. "lands at 2.2599" → "lands at 2.2599 meV" (unit).
3. "quoted as [0.04, 5.3]" → "[0.04, 5.3] meV" (unit).
4. The cancellation-threshold sentence rebuilt for fluency: "The model's
   derived anchor sits 2.8% below that threshold — six times the precision to
   which the scale is measured — so the floor thins across the allowed range,
   but it does not vanish inside it."
5. "early dark energy scores −ΔAIC 23.40" → "improves the information
   criterion by 23.40 and leaves a residual tension of 2.51σ" (the sign
   convention no longer requires decoding); "analysis chain" → "analysis
   pipeline" (avoids collision with the sampler sense of "chain").
6. "holding with the SH0ES calibration included and pulling the other way" →
   "included even though that calibration pulls the other way."
7. One comma splice fixed (the κ_m qualification).
8–11. Four overlong lines rewrapped to the file's measure.

---

## Update 2026-07-28 — the letter's Status section re-graded against the live chains

**Why this was touched.** The letter is outward-facing and addressed to a named person, so it is the
worst possible place for a stale evidence claim. Today's live read of the running pair changed the
picture the Status section rested on, and the standing rule is to re-run what was graded at a
corrected input rather than only fix the number.

**What changed.** The section said the fits "match or modestly outperform ΛCDM" and that the H₀
figure was not yet final. Both remain true. What was added is the current position, stated so it
cannot be read as stronger than it is:

- best fit **1377.89** (model) against **1379.79** (ΛCDM) on the matched pair — nominally 1.9 log
  units the model's way;
- **not claimed as a result**: our chain has **1.79×** more samples and best-fit is a running
  minimum favouring the longer chain even for identical models; **neither chain has converged**
  (ΛCDM R−1 ≈ 1.0, ours has no R−1 yet), so both are upper bounds still falling; and **best fit is
  not evidence** — no parameter penalty, which is precisely the quantity at issue when the model's
  case rests on having fewer parameters;
- **the honest position is a wash, quotable in neither direction**, with the standing number still
  the marginal SH0ES-conditional Laplace estimate.

**Note the direction of the edit.** The live numbers currently favour the model, and the change made
here *weakens* what the letter claims from them. That is the correct treatment — a lead that cannot
survive its own sampling asymmetry is not a lead, and discovering it in a reply from Fairbank would
cost far more than declining to bank it now.

**Status unchanged: shareable as a draft.** The letter continues to disclose the transition-epoch
caveat (frozen at a profiled value 0.053 dex from the model's own onset identity, ~28% in the fluid
mass) on its own initiative, which is the right instinct and should survive any later edit.
