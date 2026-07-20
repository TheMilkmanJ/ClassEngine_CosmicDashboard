# One observable, two "full budgets" — a width decision only you can make

**The finding.** The corpus quotes the deuterium tension against two different error budgets, both
called "the full budget":

| width | what it includes | who uses it | the standing 2.387 reads | the window 2.407–2.463 reads |
|---|---|---|---|---|
| 0.0476 | obs ±0.030 ⊕ theory ±0.037 | the coverage map's row 2, and the corpus's famous "−2.5 to −1.4σ" | −2.94σ | −2.5 to −1.3σ |
| 0.0563 | the above ⊕ the d(p,γ)³He rate term | the scar file's headline "−2.49σ" | −2.49σ | −2.1 to −1.1σ |

So "−2.49σ" and "−2.5 to −1.4σ" — which the corpus quotes side by side — are not the same statement
at two precisions. They are different objects at different widths that happen to collide numerically:
the first is the standing value on the 3-term width, the second is the committed window on the 2-term
width.

**What I did.** PHYSICS_DOMAINS now states the whole ladder on ONE width (the scar file's 0.0563,
since that file is the dedicated, deep-audited authority and its budget is the fuller one):
standing −2.49σ · window −2.1 to −1.1σ · spread-unfolded ≈−1.4σ · ΛCDM control −1.90σ. The harness
carries all four.

**What I did not do.** Touch the coverage map's row 2 or the other files that quote "−2.5 to −1.4σ".
Standardizing on 0.0563 corpus-wide would re-quote the advertised window as **−2.1 to −1.1σ** —
a friendlier number arrived at by a width choice, which is exactly the kind of move that must be
yours, not mine. The alternative — standardizing on 0.0476 — makes the standing row read −2.94σ,
harsher, and drops a real error term.

**My recommendation:** adopt 0.0563 everywhere, because the d(p,γ)³He term is a real uncertainty and
the fuller budget is the honest one — accepting that a referee may ask why the window softened, to
which the answer is "we stopped quoting two different widths in one sentence."

---

## ADDENDUM (2026-07-20): the desk work is done, and it points the other way

**Your decision is still yours — but the question changed.** Three findings, in order of weight.

**1. The recommendation above rests on a premise the citation does not support.** It reads "adopt
0.0563, because the d(p,γ)³He term is a real uncertainty and the fuller budget is the honest one."
The term is real. What is not established is that it is *additional*. PRIMAT's ±0.037 is quoted
**post-LUNA** (`docs/PRTOE_references.md:96–97`: arXiv:2011.11320, D/H = 2.439 ± 0.037), and
LUNA's result **is** the d(p,γ)³He cross-section measurement. If that rate's uncertainty is
already inside the ±0.037 — which is what "post-LUNA" ordinarily means — then the three-term
0.0563 folds the dominant deuterium rate in **twice**, and the two-term **±0.0476 is the correct
width**, not merely the harsher one.

**What settles it:** read arXiv:2011.11320's error decomposition and check whether d(p,γ)³He is
itemised inside the ±0.037. That is a fifteen-minute literature check, and it decides the width
without anyone having to make a taste call.

**2. Why this was invisible: ±0.0476 names two different objects.** The third term is numerically
equal to the observational error (±0.0300, recovered by inverting 0.0563), which makes the
⊕-folding degenerate:

> observational ⊕ nuclear = **0.047634**  ·  nuclear ⊕ rate = **0.047634** — identical to five figures.

Both routes to the combined width then land on **0.0563** (0.0562939 vs 0.0562939). So the corpus
uses "±0.0476" for the two-term *combined* width in six files and for the *theory-only* budget in
the scar file, and **no arithmetic check can separate them** — which is exactly why the harness has
never caught it and why the budget kept reading as "unstated". Only the wording of a citation
distinguishes the two, and the wording is inconsistent.

**3. The direction of the correction, stated so you can weigh it.** Your original framing was that
adopting 0.0563 makes the advertised window friendlier and therefore must be your call. That logic
now runs the other way: the finding above pushes toward **0.0476**, which makes the standing row
**−2.94σ instead of −2.49σ** — worse for the model. A correction that costs the model does not need
your protection from self-interest. **But it re-quotes the headline number of the file the corpus
designates as this row's authority, so the booking is still yours.**

**Revised recommendation:** run the fifteen-minute check on 2011.11320. If d(p,γ)³He is inside the
±0.037, standardize on **±0.0476** corpus-wide and re-quote the standing row at **−2.94σ**; the
advertised window **−2.5 to −1.4σ** then needs no change at all, since it was always the two-term
number. If it is genuinely additional, your original recommendation stands and 0.0563 is right.

**What was done at the desk, needing nothing from you:** the split is now stated explicitly with
every term valued in `docs/PRTOE_deuterium_scar.md` §1, the fork is quoted there rather than one
side, the ±0.0476 degeneracy is flagged in place, and the harness pins both decompositions so
neither can drift. No σ was re-booked. *(One more for the same source check: the scar file
attributed the theory budget to "the ⁴He(d,γ)⁶Li and d(p,γ)³He rate uncertainties" — ⁴He(d,γ)⁶Li
is a ⁶Li production channel and is not a D/H driver, so that attribution wants verifying too.)*

---

**Found en route, already fixed:** the scar file's §5 said the committed ζ window is
"(ΔN_eff ≈ 0.26–0.29)". The window 2.407–2.463 that the whole corpus quotes corresponds exactly to
**ΔN_eff 0.06–0.24** (the ζ ∈ [0.25, 0.35] band, the same one bet at CMB-S4); 0.26–0.29 would give
2.471–2.480, which nothing quotes. Corrected, and the correspondence is now harness-locked.

---

# THE DECISION NOTE (#157) — the D/H width, on one page

*The addendum above is a record of how the question was found. This is the decision instrument:
the two candidate widths side by side, what each one assumes, and the single piece of evidence
that retires one of them. **Nothing here is decided. The booking is yours.***

## The one observable

The model predicts **D/H = 2.387×10⁻⁵**; the quasar-optical measurement is **2.527 ± 0.030**
(Cooke) — `docs/PRTOE_deuterium_scar.md:12-13`. The gap is **−0.140** and is not in dispute. The
only question is what to divide it by.

## The two decompositions

Three components are on the table, all three real, all three cite-verified
(`docs/PRTOE_deuterium_scar.md:18-22`):

| component | value | source |
|---|---|---|
| observational | ±0.030 | Cooke's quasar-optical measurement error |
| BBN nuclear theory | ±0.037 | PRIMAT **post-LUNA** (arXiv:2011.11320, D/H = 2.439 ± 0.037) |
| the d(p,γ)³He rate | ±0.0300 | carried separately **only** by the three-term folding |

| | folding | width | **what it assumes** | standing row | advertised window |
|---|---|---|---|---|---|
| **A** | obs ⊕ nuclear | **±0.0476** | the ±0.037 **already contains** the d(p,γ)³He rate error | **−2.94σ** | −2.5 to −1.3σ |
| **B** | obs ⊕ nuclear ⊕ rate | **±0.0563** | the ±0.037 **excludes** it, so it must be added | **−2.49σ** | −2.1 to −1.1σ |

A and B are not one statement at two precisions. They are **the same three numbers folded under
two incompatible readings of one citation**, and exactly one reading is correct.

## What the post-LUNA quote does and does not settle

**What it establishes.** The anchor is Pitrou, Coc, Uzan & Vangioni, MNRAS 502, 2474 (2021)
(`docs/PRTOE_references.md:96-100`), whose ±0.037 is a **propagated nuclear-rate uncertainty** on a
network run **after** LUNA — and LUNA's measurement *is* the d(p,γ)³He cross section. On the
ordinary meaning of "post-LUNA", the rate is inside the ±0.037, which selects **A**.

**What it does not establish.** "Post-LUNA" states which *central rate* the network used. It does
not, by itself, state that the rate's *uncertainty* was propagated into the quoted ±0.037 rather
than held aside. That is the entire remaining ambiguity, and no amount of internal arithmetic
reaches it — see below.

**The prior, stated so it is not mistaken for the finding:** in every published BBN code d(p,γ)³He
is the dominant single contributor to the D/H theory error, so a quoted nuclear-theory budget that
omitted it would be unusual. That is a reason to expect **A**, not evidence for it.

## Why no internal check can decide it

The third term (±0.0300) is numerically equal to the observational error (±0.030), which makes
the ⊕-folding **degenerate**:

> obs ⊕ nuclear = **0.047634**  ·  nuclear ⊕ rate = **0.047634** — identical to six figures,
> and both routes to the combined width land on **0.0563** (0.0562939 either way).

So "±0.0476" names the two-term *combined* width in six files and the *theory-only* budget in the
scar file, and **the two are arithmetically indistinguishable**. Only the wording of a citation
separates them. Pinned so neither can drift: `scripts/audit_math_pass.py:1070-1083`.

## What would settle it

**One literature check, fifteen minutes.** Read the error decomposition in arXiv:2011.11320 and
determine whether d(p,γ)³He is itemised **inside** the ±0.037.

- **Itemised inside** ⟹ folding **B** double-counts the dominant deuterium reaction. Adopt
  **±0.0476**, re-quote the standing row at **−2.94σ**; the advertised window **−2.5 to −1.4σ**
  needs no change, having always been the two-term number.
- **Held outside** ⟹ folding **B** is correct as recorded, ±0.0563 stands, and the original
  recommendation in this file is right.

**A second source worth the same glance:** Pisanti et al., JCAP 04 (2021) 020, arXiv:2011.11537,
"Primordial Deuterium after LUNA" (`docs/PRTOE_references.md:101-104`) — an independent post-LUNA
code whose error decomposition would corroborate either reading.

**A third item, same check, already flagged:** the scar file attributed the theory budget to "the
⁴He(d,γ)⁶Li and d(p,γ)³He rate uncertainties". ⁴He(d,γ)⁶Li is a ⁶Li production channel and is not a
D/H driver, so that attribution wants verifying at the same source.

## The direction, stated plainly

**The honest reading now runs against the model.** This file's original framing was that
standardising on 0.0563 buys a friendlier advertised window and therefore "must be yours, not
mine". That logic has inverted: the evidence assembled since points to **A**, and A moves the
standing row from **−2.49σ to −2.94σ** — a **half-sigma against the model** on its own weakest
measured row, with the advertised window unchanged.

The original reason for handing the decision over was protection against self-interest, and that
reason has lapsed — a correction that costs the model needs no such protection. **One reason to
hand it over survives, and it is sufficient:** the change re-quotes the headline number of the
file the corpus designates as this row's authority. That is a booking, not a desk computation.

**Recommended disposition:** run the check on 2011.11320; if d(p,γ)³He is inside the ±0.037,
standardise on **±0.0476** corpus-wide and take the **−2.94σ**. Until the check is run, the scar
file's standing instruction holds — **quote the fork, not one side**
(`docs/PRTOE_deuterium_scar.md:31`).
