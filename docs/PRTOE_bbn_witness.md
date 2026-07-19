# BBN — The Transition's Witness

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*The only laboratory in nature that watched the dyad's phase transition live: T_c ≈ 179 keV
sits INSIDE the BBN window. The three abundances are three frames of the condensation.*

## The equations

- the ramp: ε(T) = ε·(1 − T/T_c), T_c ≈ 179 keV (the confining chiral value; 193 keV is the perturbative μ=T fixed-point cross-check)
- the epoch stamps: n/p freeze-out (~800 keV): ε = 0 (dyad OFF — above T_c); D bottleneck
 (~70 keV): ε_eff = 0.61ε; Li (~40 keV): 0.78ε
- the abundances. **Two runs, two baselines — they are not interchangeable, and D/H must never be
 read across them** (D/H ∝ ω_b^−1.6 is the most ω_b-sensitive abundance in the network).

 **(i) The window's EFFECT, measured on PRyM's default ω_b** (`scripts/prym_ramped_splice.py`, the
 model's own ε(T) at T_c = 179 keV, ε = 1.24%). This run is what licenses the *relative*
 numbers; **its absolute D/H is not the model's prediction**, because its baseline is not the
 model's ω_b:

 | | Y_p (BBN) | D/H ×10⁵ | Li7/H ×10¹⁰ |
 |---|---|---|---|
 | baseline (ε = 0) | 0.246891 | 2.454498 | 5.438668 |
 | the dyad's window | 0.248995 | 2.470340 | 5.452964 |
 | **the window's effect** | **+0.852%** | **+0.645%** | **+0.263%** |

 **(ii) The model's PREDICTION, on the model's own ω_b** (production PRyM; the m_e–ω_b CMB
 degeneracy pulls ω_b up +1.1% against the in-house ΛCDM control on identical data). The η-flow is
 spent *here*, once:

 > in-house ΛCDM control **2.420** → *(ω_b +1.1%)* → pre-window **2.372** → *(the window,
 > +0.645%)* → **D/H = 2.387×10⁻⁵** — the standing prediction.

 against quasar-optical **2.527 ± 0.030** (Cooke) and own-ΛCDM **2.420**. The dyad sits on the LOW
 side of the fork — a self-adverse, owned bet; **P-2026-027's radio referee decides it.**

- **Y_p from the window alone is +1.09σ** vs Aver 0.2453 ± 0.0034 (**+3.5σ** vs EMPRESS
 0.2370 ± 0.0034 — the helium civil war, unresolved), zero fitted parameters. This row **is**
 baseline-robust: Y_p ∝ ω_b^0.04, so the model's own ω_b moves it only to +1.12σ. The genesis
 residual below adds to this.
- **The fork's width, stated.** Cooke's observational error **±0.030** combines with the
post-LUNA **nuclear-theory error ±0.037** (PRIMAT, cite-verified — arXiv:2011.11320) to
**±0.0476**, putting 2.387 at **−2.9σ** from Cooke before the genesis residual is applied.
*(Against the observational error alone it is −4.7σ — an upper bound, not the tension.)* **What is genuinely open is not the budget
but the code systematic:** the same source reports PRIMAT D/H = 2.439 against PArthENoPE 2.51–2.54
— a **3.5% inter-code spread, 2.3× the nuclear error** — which is *not* folded in above. Folding it
gives **−2.2σ** (half) to **−1.4σ** (full), and the model runs **PRyM**, a third code, so which
central value the theory error should be taken around is undecided. ΛCDM itself carries 1.85σ under
PRIMAT. **The row is quotable at −2.5 to −1.4σ — the ±0.0476 budget with the genesis residual
applied and the code systematic named and unfolded.**
- **The genesis residual, applied.** The standing high-f configuration commits to one genesis
 dilution ζ = T_dark/T_γ ∈ [0.25, 0.35], carrying a relativistic residual
 **ΔN_eff = (27/(7/4))·ζ⁴ = 0.06–0.24**. That residual moves both rows, in opposite directions —
 deuterium up toward Cooke (∂ln(D/H)/∂N = 0.135), helium up away from Aver
 (dY_p/dN = 0.011–0.013). Propagated on the model's own prediction above:

 - **D/H = 2.387 → 2.407–2.463×10⁻⁵** across the window. It moves toward Cooke's 2.527 and **does
 not reach it** — the gap closes from 0.140 to 0.064, never to zero, at any point in the window.
 - **Y_p = 0.24900 → 0.24978–0.25201**, i.e. **+1.3 to +2.0σ vs Aver** (**+3.8 to +4.4σ** vs
 EMPRESS). Helium pays for deuterium's relief.

 Grade: estimate (linear responses; a full nuclear-code re-run is owed only if the joint becomes
 load-bearing). The shift is **hostage to its own falsifier** — CMB-S4 (±0.03) must see the same
 ΔN_eff, and a confirmed ΔN_eff < 0.03 or > 0.3 kills the committed window from either side.

- **The joint verdict HINGES on the code systematic — this is the sector's real open question,
 and the genesis residual does not change that.** Combining the two rows (2 dof, quadrature;
 **correlations between Y_p and D/H are ignored**, as in every joint this corpus has quoted):

 | D/H width used | joint p, pre-residual | **joint p across the ζ window** | reading |
 |---|---|---|---|
 | nuclear only (±0.0476) | 0.007 | **0.02–0.08** | **rejected to marginal** |
 | + half the inter-code spread (±0.0643) | 0.051 | **0.07–0.11** | marginal |
 | + the full inter-code spread (±0.0987) | 0.201 | **0.12–0.21** | comfortable |

 **The model's BBN standing is decided by whether the 3.5% PRIMAT–PArthENoPE disagreement is an
 error or a choice — a question about the nuclear codes, not about the dyad.** The model runs a
 third code (PRyM). The residual lifts every column by roughly a factor of two to three in p and
 leaves the ordering — and therefore the decision — untouched: on the quotable budget the sector is
 still adverse-leaning. **This is booked adverse-leaning and unresolved**; it is not a result the
 model can settle by itself, and the honest range is quoted rather than the flattering end.

 *Both columns are computed on run (ii)'s baseline — the only one whose absolute D/H is a
 prediction — and against deuterium's full stated budget.*

- the elasticities: d(Y_p)/dε = 0.00163 per %ε (linear, verified: ×ε reproduces the window to ~3%); **d(D/H×10⁵)/dε — the 0.00782 figure is UNREPRODUCIBLE and does NOT linearize** (a 4-point PRyM scan gives ~0.0119; the ramped window itself implies ~0.0126, +62%). D/H is a bottleneck quantity, so its ε-response is nonlinear and the uniform-ε derivative under-predicts the ramped window; use the measured window (+0.645%), not this derivative ([PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)). N_eff is unmoved
 (3.04439) — ε shifts weak rates, not relativistic dof.

## How PRTOE connects

The sector is RIGID — every number derived or measured (T_c, ε = c·f̄·α_c, ω_b, the stamps):
the model cannot coach its witness. Referees: the radio referee (P-027), the helium
resolution, the T_c re-audit (flagged-not-taken — a rescue-by-retuning is forbidden), the α_c MCMC
posterior. History: wall → pharmacy → artifact → WITNESS — each
re-posing by better physics, booked adverse when adverse.

## Sources

[Cooke2018] (D/H), [Aver2021] + [EMPRESS2022] (the helium war's two poles), [PRIMAT2018] (rates), [PRyMordial2023] (the windowed engine), [DamourDyson1996] (the Oklo fence). Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## The lithium row — CLOSED AS A NULL (2026-07-12)

The windowed run's full output (tools/PRyMordial): Li7/H = 5.439×10⁻¹⁰ (baseline) →
**5.453×10⁻¹⁰ (the dyad's window, +0.26%)**. The dyad's
windowed effect on lithium is at the percent level and slightly UPWARD — **the model
neither causes nor cures the lithium problem** (observed 1.6×10⁻¹⁰; the ×3.4 discrepancy
stands exactly as the field left it, where the modern consensus leans stellar depletion).
Verdict: the row is SAFE (no new damage) and the model claims nothing — an abstention,
filed with the same prominence as the conquests (the strong-CP precedent). M6's lithium
debt: paid.

The abstention is robust from three directions: the lithium epoch's ε stamp follows from the same ε(T) as every other stamp, with nothing chosen for lithium; no earlier condition in the model reaches the lithium epoch; and the ×3.4 discrepancy has a standing conventional explanation in stellar depletion, which the model neither needs nor contradicts.

