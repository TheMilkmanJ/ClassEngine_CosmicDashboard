# T13 fingerprint lattice — OWED
1. THE ε(EPOCH) BOOKKEEPING (internal review% residual): recompute every lattice row with the ramp-corrected, epoch-appropriate ε (BBN-era vs recombination-era vs today) — the lattice's weights are epoch-stamped, not one number.
2. The masters' calendar: the α_c MCMC (running), DESI DR3, PolyChord, the radio referee, BipoSH — dates and decision rules in one place.
3. The row-correlation formalization: the joint likelihood of the lattice (a single χ² across rows) as the model's headline statistic.

> **⚠ THREE VALUES IN THIS WORKING LOG WERE SUPERSEDED BY THE 2026-07-17 AUDIT — corrections live
> in the reader-facing files; this log is kept as the dated record of how they were found.**
> 1. **The BBN-window ramp factor `[0.8–1.0]`** (the ε(EPOCH) table below, and line ~12): **wrong
>    band.** The model's own ramped stamps are **0 / 0.61 / 0.78** (1 − T/T_c at the derived
>    T_c = 179 keV) — the band contains neither. Fixed in `PRTOE_fingerprint_lattice.md`.
> 2. **`d(D/H)/dε = 0.00782`** (item 3, below): **UNREPRODUCIBLE from the engine** — a fresh 4-point
>    PRyM scan gives a linear 0.0119 and the row 2.470340 does not reproduce. Filed
>    `PRTOE_FAILURES_LEDGER.md`; the splice has no B_D channel (D/H is a bottleneck quantity).
>    Y_p's 0.00163 *is* correct (measured 0.001628).
> 3. **`+3.7σ vs EMPRESS` / D/H `~1.6–1.9σ`** (below): the +3.7σ is the **step-era** pull (ramped
>    gives **+3.53σ**); the ~1.6–1.9σ D/H is the **withdrawn PRyM-default-ω_b** baseline (process
>    error 38). Standing D/H is **−2.9σ** on the full budget.

## PAID item 1: THE ε(EPOCH) TABLE — every lattice row now wears its WHEN
(the audit's law: no number without its epoch):
| epoch | ε | provenance |
|---|---|---|
| today (z < 50) | 0 exactly | the window's low edge (Oklo/clock fence) |
| recombination (z ~ 1100) | 1.232% (fit) / 1.254% (derived stack) | the production chain |
| BBN window (LT era, inside) | ε_rec × [0.8–1.0] (mean-field ramp factor, internal review debt) | the windowed splice |
| above z_high (~T_c epoch) | 0 (disordered) | the dyad window's high edge |
Rows must cite THIS table, not "the" ε. Item 2 (the masters' calendar) still open.

## PAID item 2: the masters' calendar — docs/PRTOE_REFEREE_CALENDAR.md.

> **Item 3 — the row-correlation formalization — is unpaid, unbuilt.** This file lists **three**
> items; the ε-epoch table and the calendar cover two of them. A corpus-wide search finds **no
> joint-likelihood / single-χ²-across-rows construction anywhere**. **T13 is NOT complete**, and what
> is missing is not a detail: item 3 is *"the model's headline statistic"* by this file's own words.
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

**THREE OBSTRUCTIONS FOUND — all in the inputs, none cosmetic. Their current state is marked;
(3) is closed, (1) and (2) stand:**

1. **The helium civil war makes a single joint χ² ill-posed.** Aver (0.2453 ± 0.0034) and EMPRESS
   (0.2370 ± 0.0034) are *the same observable* and disagree with each other at **1.7σ**. Summing
   both into one χ² double-counts Y_p *and* imports an unresolved systematic as signal. The joint
   statistic must be reported in **two branches** (model sits +1.2–1.5σ from Aver, **+3.7–4.0σ from
   EMPRESS**) until the helium resolution lands. A property of the data, not of the model — but the
   branch spread is large enough that a single quoted number would be meaningless.
2. **The D/H row's significance is irreproducible — the error budget is unstated. REDUCED
   (2026-07-20): the budget is now stated term by term** — observational ±0.030 ⊕ PRIMAT
   post-LUNA nuclear ±0.037 (⊕ the d(p,γ)³He rate ±0.0300 on the three-term folding) — **in
   `PRTOE_deuterium_row.md` §1. CLOSED (2026-07-21, #157): the source check settled it — PRIMAT's
   ±0.037 is a post-LUNA Monte-Carlo error that already varies d(p,γ)³He, so the three-term folding
   counted the dominant rate twice. Standing width **±0.0476**, standing row **−2.94σ**; ±0.0563 is
   retired. The ±0.0476 label is degenerate (observational ⊕ nuclear and nuclear ⊕ rate agree to
   five figures), which is why no arithmetic check separated the two readings. One ruling still
   closes this obstruction, the red-team brief's D/H row, and the joint statistic's quotability at
   once.**
   At least three readings each reproduce a figure quoted somewhere in the corpus: the raw windowed
   2.477 against ±0.030 (−1.67σ); the net 2.41 against σ ≈ 0.067 (−1.75σ); the net 2.41 against
   σ ≈ 0.053 (−2.21σ, which is what P-2026-027 quotes). **Two live documents imply different widths
   from each other.** Which is intended is not determinable from the corpus. **The budget is now
   stated** (observational versus the BBN theory error, chiefly the d(p,γ)³He rate — all three
   terms valued in the deuterium row file). The row is quotable as a fork; a single σ waits on the
   standardization.
3. **The elasticities — RESOLVED (measured 2026-07-16; see below).** They were the single blocking
   item; they are no longer missing.

**Note:** the derived stack compared to the *concordance joint* (+1.77σ) and the corpus's
*fit-versus-stack* "1.4σ" are different comparisons and do not contradict each other.

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

## THE TRUE RAMPED SPLICE — COMPUTED (2026-07-16). `scripts/prym_ramped_splice.py`

The decisive task, run. The ramp ε(T) = ε(1 − T/T_c) is applied **pointwise** to the weak-rate
grids — rate(T) = std(T) + [shf(T) − std(T)]·w(T), w(T) = max(0, 1 − T/T_c) — instead of switching
zones on and off. Exact at w = 0 and w = 1, first-order in between; ε = 1.24% is small enough that
the rates' departure from linearity is negligible (the scan's Y_p increments are linear to < 2%).

**Read the pull, χ², and p columns as splice-comparison only.** Every row is computed on PRyM's
default ω_b — run (i)'s baseline — and its deuterium pull is taken against Cooke's *observational*
error alone. Neither is a legitimate absolute reading: the model's D/H prediction lives on the
model's own ω_b (2.387×10⁻⁵, not 2.470×10⁻⁵), and deuterium's honest width folds the PRIMAT
nuclear-theory error (±0.0476, not ±0.030). The columns rank the splices correctly, which is what
this table was built to do; the sector's absolute books are
[PRTOE_bbn_witness.md](../PRTOE_bbn_witness.md)'s.

| splice | Y_p | pull (Aver) | D/H | pull (Cooke, obs-only) | χ² (2 dof) | p |
|---|---|---|---|---|---|---|
| LT step (claimed "low edge") | 0.249701 | +1.29σ | 2.47734 | −1.66σ | 4.42 | 0.110 |
| MTLT step (claimed "high edge") | 0.258573 | +3.90σ | 2.52747 | +0.02σ | 15.24 | 0.0005 |
| **RAMPED, T_c = 0.179 (DERIVED)** | **0.248995** | **+1.09σ** | **2.47034** | **−1.89σ** | **4.75** | **0.093** |
| RAMPED, T_c = 0.193 (cross-check) | 0.249215 | +1.15σ | 2.47663 | −1.68σ | 4.14 | 0.126 |

**THREE FINDINGS, and the first overturns a recorded claim:**

**1. The bracket does not bracket.** Y_p: ramped 0.248995 **<** LT 0.249701 < MTLT 0.258573. D/H:
ramped 2.47034 **<** LT 2.47734 < MTLT 2.52747. **The truth lies BELOW the LT edge, not between the
two.** `run_windowed.py`'s header calls LT the *"ramp low edge → UNDER-counts"* — it is neither: LT
applies the **full** shift (w = 1) across the whole LT zone where the true w runs 0.44 → 1, so LT
**over**-applies. The bracket's lower edge was never a lower bound, and every conclusion drawn from
"the truth is somewhere in [LT, MTLT]" was drawn from a false enclosure.

**2. The MTLT catastrophe was a step artifact — and the depth law called it.** MTLT applies the full
shift across 0.179–1 MeV **where the true ramp is exactly zero** (the dyad is OFF above T_c). Its
p = 0.0005 "rejection" was an artifact of the approximation, not a statement about the model.
Amendment 5 (steps illegal as computational entries *and methods*) demanded the ramp be computed
rather than bracketed; doing so **removes a 3.5σ rejection that never existed.**

**3. The ramped splice is the best of the three at the derived ε, with ZERO fitted parameters**
(χ² = 4.75 on 2 dof against 15.24 for MTLT; 0.126 vs 0.093 between the two T_c values). That is a
statement about the splices, not about the sector: on the model's own ω_b and deuterium's full
error budget the same abundances give p = 0.02–0.08 with the genesis residual applied
([PRTOE_bbn_witness.md](../PRTOE_bbn_witness.md)) — adverse-leaning, not "surviving". The
p = 0.093 headline was read absolutely off this relative table and propagated; that reading is
withdrawn ([PRTOE_FAILURES_LEDGER.md](../PRTOE_FAILURES_LEDGER.md)).

**The internal strain survives the rescue.** Ramped elasticities (T_c = 0.179):
d(Y_p)/dε = **0.00163**/%, d(D/H)/dε = **0.00782**/% — both *smaller* than the LT step's, as they
must be (the ramp never applies the full shift anywhere except T → 0). Inverting: Y_p (Aver) wants
ε = **−1.02 ± 2.08 %**, D/H (Cooke) wants ε = **+8.49 ± 3.84 %** — **still 2.2σ apart.** The rows
still pull in opposite directions on one parameter. That finding is robust to the splice.

**A T_c inconsistency surfaced in passing.** The corpus's epoch stamps (D bottleneck ε_eff = 0.64ε,
Li = 0.79ε) reproduce 1 − T/**193 keV** (0.637, 0.793), not 1 − T/**179 keV** (0.609, 0.777) — the
BBN engine's ramp is keyed to the **perturbative Coleman–Weinberg cross-check**, while the DE chain
derives T_c = **179 keV** (the confining chiral value, τ·m_e). The consequence is small here
(χ² 4.75 vs 4.14) but the engine should be keyed to the derived value, and the stamps restated.

**Status: item 3's blocking input CLOSED; the statistic is EVALUABLE and has been evaluated. Two
obstructions remain before a single headline number can be quoted:** the helium branch problem
(Aver vs EMPRESS, 1.7σ apart on the same observable — the EMPRESS branch is far worse: it wants
ε = −1.06 ± 0.37 %, putting the derived ε **6.3σ** away) and the D/H presentation gap below. T13 is
**not** complete — but it is no longer blocked.