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
