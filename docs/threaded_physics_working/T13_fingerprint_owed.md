# T13 fingerprint lattice — OWED
1. THE ε(EPOCH) BOOKKEEPING (internal review% residual): recompute every lattice row with the ramp-corrected, epoch-appropriate ε (BBN-era vs recombination-era vs today) — the lattice's weights are epoch-stamped, not one number.
2. The masters' calendar: the α_c MCMC (running), DESI DR3, PolyChord, the radio referee, BipoSH — dates and decision rules in one place.
3. The row-correlation formalization: the joint likelihood of the lattice (a single χ² across rows) as the model's headline statistic.

## PAID item 1 (2026-07-12): THE ε(EPOCH) TABLE — every lattice row now wears its WHEN
(the audit's law: no number without its epoch):
| epoch | ε | provenance |
|---|---|---|
| today (z < 50) | 0 exactly | the window's low edge (Oklo/clock fence) |
| recombination (z ~ 1100) | 1.232% (fit) / 1.254% (derived stack) | the production chain |
| BBN window (LT era, inside) | ε_rec × [0.8–1.0] (mean-field ramp factor, internal review debt) | the windowed splice |
| above z_high (~T_c epoch) | 0 (disordered) | the dyad window's high edge |
Rows must cite THIS table, not "the" ε. Item 2 (the masters' calendar) still open.

## PAID item 2 (2026-07-12): the masters' calendar — docs/PRTOE_REFEREE_CALENDAR.md.
~~T13 is COMPLETE (both items paid: the ε-epoch table + the calendar).~~

> **⚠ THAT CLOSURE WAS FALSE — CORRECTED 2026-07-16.** This file lists **three** items; the
> "COMPLETE" line accounts for **two**. **Item 3 — the row-correlation formalization — is unpaid,
> unbuilt, and was omitted from the closing count.** A corpus-wide search finds **no joint-likelihood
> / single-χ²-across-rows construction anywhere**. **T13 is NOT complete**, and what is missing is
> not a detail: item 3 is *"the model's headline statistic"* by this file's own words.
>
> **Why it matters more than its position in the list suggests.** The lattice's whole claim is that
> one parameter ε must serve every row *at its assigned weight* — H₀, the radio chords, the neutrino
> de-biasing, BBN. That claim is only testable as a **joint** statistic: row-by-row agreement is
> compatible with the lattice being wrong in a way no single row detects, and a single row's failure
> means something different depending on the correlations with the others. Until the joint likelihood
> exists, the lattice is a *set of separate agreements presented as one object*. **Item 3 is the item
> that would make the fingerprint lattice a test rather than a display.**

Coupling-geometry status: the registered-referee set IS the unscreened class (a consistency finding).


## Item 3 BUILT to specification (2026-07-16) — `scripts/lattice_joint_likelihood.py`

**The object is specified and the rows are inventoried; the headline χ² is deliberately NOT
quoted, because it cannot yet be quoted honestly.** Quoting one anyway would be the exact
"display, not a test" failure this item exists to fix.

**What makes the lattice testable at all: the weights are FIXED, not fitted.** The BBN ramp
ε(T) = ε·(1 − T/T_c), T_c ≈ 179 keV, stamps every row — n/p freeze-out (~800 keV) w = 0 (dyad OFF,
above T_c); D bottleneck (~70 keV) w = 0.64; Li (~40 keV) w = 0.79; recombination w = 1.00; today
w = 0. Each row predicts w_i·ε with w_i **known**. The lattice cannot re-weight to escape.

**Two modes, and the second is the headline:**
- **ε free** → dof = N − 1. Tests *"can one ε serve all rows?"*
- **ε derived** (= c·f̄·α_c = 27α/5π) → **dof = N, zero fitted parameters.** Tests the derivation
  itself, with nowhere to hide. **This is the statistic the model should lead with.**

**THREE OBSTRUCTIONS FOUND — all in the inputs, none cosmetic:**

1. **The helium civil war makes a single joint χ² ill-posed.** Aver (0.2453 ± 0.0034) and EMPRESS
   (0.2370 ± 0.0034) are *the same observable* and disagree with each other at **1.7σ**. Summing
   both into one χ² double-counts Y_p *and* imports an unresolved systematic as signal. The joint
   statistic must be reported in **two branches** (model sits +1.2–1.5σ from Aver, **+3.7–4.0σ from
   EMPRESS**) until the helium resolution lands. A property of the data, not of the model — but the
   branch spread is large enough that a single quoted number would be meaningless.
2. **The D/H row's stated significance does not follow from its own quoted numbers.** Model
   2.40–2.42 against *"Cooke 2.527 ± 0.030"* is **−3.6 to −4.2σ**, not the recorded "~1.6–1.9σ."
   That figure requires **σ ≈ 0.067** — i.e. observational error **plus the BBN theory error** (the
   d(p,γ)³He rate), which is real and standard but **is not named in the line that quotes ±0.030
   and concludes 1.6–1.9σ**. Not a physics error; a presentation error that makes the row
   irreproducible as written. **The theory error must be stated for the row to be auditable.**
3. **The elasticities are missing — and they are what turn this into a likelihood.** The corpus
   publishes model values *at* the standing ε (Y_p → 0.2495–0.2505, D/H → 2.40–2.42) but not
   **d(Y_p)/dε** or **d(D/H)/dε**. Without them χ² is computable at a *point* but is not a
   *function* of ε: it cannot be minimised, cannot yield a best-fit ε, and cannot support the dof
   accounting that gives the derived-ε test its force. **These are one PRyM run away** (vary ε,
   re-run, finite-difference) — a measurement, not a derivation. **This is the single blocking
   item.**

**Also fixed in passing:** an earlier framing of this pass compared the derived stack to the
*concordance joint* (+1.77σ) and read it against the corpus's *fit-versus-stack* "1.4σ" as if they
disagreed. They are different comparisons and do not contradict. Recorded so the joint statistic is
not built on the wrong pair.

**Status: item 3 SPECIFIED, not closed.** The object exists, its modes and dof are defined, its rows
carry provenance. It becomes the model's headline statistic the moment (3) lands and (1)–(2) are
stated. T13 is **not** complete.