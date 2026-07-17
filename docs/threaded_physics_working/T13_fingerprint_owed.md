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

## Item 3 — THE BLOCKING INPUT IS MEASURED (2026-07-16). Runner: `scripts/prym_elasticity_runner.py`

*(The vendored PRyMordial tree and `*.dat` are gitignored, so the raw scan is reproduced inline
below rather than committed as a data file. Reproduce with:
`python3 scripts/prym_elasticity_runner.py <LT|MTLT> <shift>`, shift = 1 + ε.)*

**The raw scan** — `ELAST <mode> <shift> <ε%> <N_eff> <YPCMB> <YPBBN> <D/H×10⁵> <He3/H×10⁵> <Li7/H×10¹⁰>`:

```
ELAST LT   1.000000 0.0000 3.044389 0.245565 0.246891 2.454498 1.041187 5.438668
ELAST LT   1.006200 0.6200 3.044389 0.246991 0.248323 2.470454 1.043149 5.439146
ELAST LT   1.012400 1.2400 3.044389 0.248365 0.249701 2.477344 1.044013 5.456383
ELAST LT   1.018600 1.8600 3.044389 0.249691 0.251032 2.488618 1.045361 5.461626
ELAST MTLT 1.000000 0.0000 3.044389 0.245565 0.246891 2.454498 1.041187 5.438668
ELAST MTLT 1.006200 0.6200 3.044389 0.251424 0.252771 2.492799 1.046368 5.508075
ELAST MTLT 1.012400 1.2400 3.044389 0.257206 0.258573 2.527466 1.051316 5.577972
ELAST MTLT 1.018600 1.8600 3.044389 0.262905 0.264292 2.558475 1.055974 5.650593
```

**The elasticities exist now.** Eight production-splice PRyM runs (the `run_windowed.py` machinery,
`shift` promoted from hardcoded 1.0124 to an argument), central-differenced about the standing ε:

| mode | d(Y_p^BBN)/dε | d(D/H×10⁵)/dε |
|---|---|---|
| **LT** (ramp low edge, under-counts) | **0.00218** per %ε | **0.01465** per %ε |
| **MTLT** (ramp high edge, over-counts) | **0.00929** per %ε | **0.05296** per %ε |

**N_eff is identical (3.04439) across all eight runs** — the ε shift moves weak rates, not
relativistic dof. No hidden N_eff leak.

### What the joint statistic says the moment it can be evaluated

**(i) The lattice's two BBN rows pull in OPPOSITE directions on ε.** Inverting the elasticities:

| mode | Y_p (Aver) wants | D/H (Cooke) wants | mutual disagreement |
|---|---|---|---|
| LT | ε = **−0.73 ± 1.56 %** | ε = **+4.95 ± 2.05 %** | **2.2σ** |
| MTLT | ε = **−0.17 ± 0.37 %** | ε = **+1.37 ± 0.57 %** | **2.3σ** |

Read separately these are the recorded mild strains (Y_p "+1.2–1.5σ", D/H "~1.6–1.9σ"). Read
**jointly** they are a contradiction: Y_p sits too **high** (wants ε *lower*), D/H too **low** (wants
ε *higher*) — **same parameter, opposite signs, ~2.3σ apart in both modes.** The corpus's own numbers
implied this and never stated it. **This strain is independent of whether the derived ε is right.**

**(ii) The derived ε at zero fitted parameters — and the bracket is now the whole verdict.**
Evaluating at ε = c·f̄·α_c = 1.2543 % (nothing fitted, dof = 2):

| ramp position | Y_p pull | D/H pull | joint χ² | p |
|---|---|---|---|---|
| **LT** | +1.29σ | −1.66σ | **4.42** | **0.11 — survives** |
| halfway | +2.60σ | −0.82σ | 7.43 | 0.024 |
| **MTLT** | +3.90σ | **+0.02σ** | **15.24** | **0.0005 — rejected** |

**The bracket spans "not rejected" to "rejected at 3.5σ", and the model says the truth is inside
it.** Buying one row costs the other: MTLT lands D/H on Cooke to **0.02σ** — a bullseye — and blows
Y_p out to +3.9σ in the same breath.

### The consequence, and it is a depth-law consequence

**LT and MTLT are STEP-APPROXIMATIONS of the model's own derived ramp** ε(T) = ε(1 − T/T_c) —
"shifted rates in the LT zone only" versus "in MT+LT". The bracket was recorded as a harmless
numerical uncertainty. **It is now the entire BBN verdict.** Amendment 5 (the depth law, TOTAL —
steps illegal as *computational entries and methods*) already required the ramp be computed rather
than bracketed by steps; that was hygiene an hour ago, and it is now **the difference between
p = 0.11 and p = 0.0005**. **Computing the true ramped splice is the decisive open BBN task.**

**Status: item 3's blocking input CLOSED; the statistic is EVALUABLE and has been evaluated. Two
obstructions remain before a single headline number can be quoted:** the helium branch problem
(Aver vs EMPRESS, 1.7σ apart on the same observable — the EMPRESS branch is far worse: it wants
ε = −1.06 ± 0.37 %, putting the derived ε **6.3σ** away) and the D/H presentation gap below. T13 is
**not** complete — but it is no longer blocked.