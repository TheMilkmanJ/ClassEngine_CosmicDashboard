# The Hierarchy Problem — the Electroweak Scale as a Pairing Gap (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


> **STATUS: split, because the pieces did not fail together.** A named condition FAILED — the
> paired lepton-sector vacuum was excluded by the basement rebuild — but "every result inherits
> that conditionality" was too broad, and the split matters:
>
> | piece | does it use the excluded vacuum? | grade |
> |---|---|---|
> | **the −3/2 exponent** | **no** — the chain runs on a pairing log's thermal dressing and equipartition, ⟨E_kin⟩/T = 3/2 at *any* nonrelativistic formation temperature. Self-pinned, no vacuum named | **derived** (additivity grade) |
> | the shared k | no — it is the A_s coupling, three-way concordant at 1.360 / 1.36461 / 1.3602 | derived elsewhere |
> | α_c = 3α | no — the same coupling as the amplitude and the vacuum | registered bet (P-040) |
> | **the anchor's identification with 4πm_H** | **yes** — it is where the gap equation needed a vacuum to sit in | **orphaned pending transfer to the Fermi-point basement** |
>
> So the arithmetic below stands and reproduces (residual 1.5015 against 3/2; M_anchor = 1576 GeV
> against 4πm_H = 1574, +0.15%). What is homeless is the *interpretation* — a gap equation without
> a vacuum. Other conditionality: the no-bare clause, P-2026-042's anchor identification, and the
> gap equation's k. Referees: the α_c MCMC, the two-loop redesign, HL-LHC. Also conditional on: the no-bare
> clause, P-2026-042's
> anchor identification, and the gap equation's k (owed, the working docket). Referees: the α_c MCMC (the
> triangle), the two-loop redesign, HL-LHC (the portal search).

## 0. The problem

Why is the electroweak scale (m_H = 125 GeV) sixteen orders of magnitude below the Planck
scale? In the Standard Model the Higgs mass is quadratically sensitive to the cutoff —
keeping it light requires either fine-tuning to one part in 10³², or new physics
(supersymmetry, compositeness) that has not appeared where predicted.

## 1. The model's answer in one sentence

**The electroweak scale is exponentially below the basement for the same reason a
superconductor's gap is exponentially below its phonon scale: it is a pairing gap —
$M_{\rm anchor} = M_{\rm red}\,e^{-1/(k\,\alpha_c)}$ — and the Higgs mass is that gap's
one-loop echo.**

## 2. The math

**(a) The anchor — current truth.** The arrows, graded:
the hierarchy dial $x_0$ is CONSISTENCY-ONLY (a free dial of the GC dictionary that this
closure selects — failures ledger §6); the census closure / duty-family landing is
STRAINED (the two-loop shooter lands the census portal at 13–20 TeV, not the anchor —
the edge-convention audit decides whether that arrow fell or the convention did). THE
ONE GENUINELY INDEPENDENT ARROW ($m_H$ is measured) STANDS:

$$\ln\!\frac{M_{\rm red}}{4\pi\,m_H} = 34.98 \quad\Longrightarrow\quad M_{\rm anchor} \approx 4\pi\,m_H \approx 1.57\ \text{TeV}\ \ (2.5\%)$$

**(b) The pairing form.** Across the entire cloud the exponent reads as one BCS coupling:

$$\frac{1}{g} = 34.85\text{–}35.43 \;\Longrightarrow\; g = (1.29\text{–}1.31)\,\alpha_c$$

— stable to ±1% while the arrows scatter by ±0.3. Hence
$M_{\rm anchor} = M_{\rm red}\,e^{-1/(k\alpha_c)}$ — and the k in the exponent is **the
corpus's one shared k** (the same screened-interaction coupling that sets A_s: gap-equation
1.360, closed form 1.36461, A_s-measured 1.3602 ± 0.0064 — one object, three determinations,
`scripts/concordance.py`). **The exponent's residual:** with the shared k,
1/(kα_c) = 33.474, while the measured anchor needs
ln(M_red/4πm_H) = 34.975 — a residual of **1.5014** at m_H central,
**1.5000 exactly at m_H + 1σ**. Writing the exponent with that constant:

$$M_{\rm anchor} = M_{\rm red}\,e^{-1/(k\alpha_c)\,-\,3/2} = 1576\ \text{GeV}\quad
(\text{measured } 4\pi m_H = 1574;\ +0.14\%)$$

One coupling serves both floors (A_s to −0.35%, the anchor to +0.14%). The data selects the
log normalization: a single-log gap condition [ln(M_red/M) − 3/2] = 1/(kα_c) matches; a
squared-mass-log form gives 3/4 (excluded). **Grade: sharp underived residual — the
derivation of the 3/2 is DEAD.** All four natural attachment routes were computed and fail:
the CW minimum gives 1/2, the tachyonic onset 3/4, the sharp-cutoff BCS gap equation ln 2,
and scheme/threshold matching gives {0 (gauge decoupling), 5/6 (momentum-scheme), 1 (the
pairing-susceptibility scheme — the honest reading of "gap-scheme coupling")}. The
obstruction is structural: every one-loop dimensional-regularization constant enters against
ln μ² (squared-log), so it halves at this single-log normalization — landing 3/2 requires a
squared-log constant of 3, absent from the one-loop fermionic menu. The earlier
identification with the T_c derivation's own bracket constant (L − 1 = ln(m_e0²/μ²) − 3/2)
is **retracted** on the same ground: that bracket is squared-log, and at this normalization
it predicts the excluded 3/4 (autopsy:
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md)). Any future exhibition must produce 3
at squared-log or a natively single-log mechanism — and the one arithmetic door in the menu
(½ + 1 = 3/2 as a forced sum) is closed by the RG dichotomy: conditions that combine objects
cancel their μ-logs (they fix ratios, not scales), and conditions that keep the log are
single-object. No route is named at one loop — but the failure is now classified: the
constant is **seam-class** (neither ratio nor scale; the number that converts a scheme
condition into a physical scale), which no single-sector menu contains. The seam census
(ledger) finds exactly one structure carrying 3/2 natively at single-log: the d = 3
phase-space power d/2 — **route 6**, sharpened to the equipartition reading: the constant as
the mean kinetic cost ⟨E_kin⟩/T = d/2 of nonrelativistic census states at pairing.
Self-pinning is automatic (the cost (3/2)T rides the same T — no scale chosen) and the sign
is right (suppression: the anchor sits e^(−1.5) below naive transmutation). **The 3/2 is
now DERIVED at additivity grade.** The chain: a pairing log's infrared end is the gap
dressed by the constituents' thermal boost (pairs must out-bind moving partners; per state,
e^(E_kin/T)); the frozen cutoff composes multiplicatively over the population's events —
logs add, one contribution per constituent, **the corpus's one shared additivity** (the same
assumption A_s, n_s, and the Koide power reading already ride — one neck, not four); the
geometric mean is then forced, M_eff = M·e^(⟨E_kin⟩/T), and equipartition gives
⟨E_kin⟩/T = **3/2 exactly at any nonrelativistic formation temperature** — self-pinned. The
gap condition ln(M_red/M_eff) = 1/(kα_c) delivers the recorded formula. Sign automatic
(boost raises the cutoff, suppresses the gap); the factor-of-2 wall evaded legitimately
(E_kin/T dresses the LINEAR scale — natively single-log, which is why the five in-sector
routes could never find it); the Saha log-power hazard evaded explicitly (the dressed object
is a dimensionless boost ratio — no density, no (mT)^(3/2); this is also why the mean-field
venue, which weights by density, saw nothing). **Conditions: the shared additivity (one
corpus-wide neck) and the nonrelativistic formation window.** The constant joins the moment
family: linear channel → ⟨|cos|⟩ = 2/π; quadratic channel → √⟨cos²⟩ = 1/√2; exponential
channel → e^(−⟨E_kin⟩/T) = e^(−3/2) — the portfolio's three floors each carrying the average
their coupling order forces. Guards that stand: the sharp precision
rides the closed-form k (the A_s-measured k gives 1.39 ± 0.16, consistent not sharp), and
the result is conditional on the recorded 4πm_H anchor definition. The coupling in the
exponent is not new — it is the SAME α_c = 3α
that runs the dyad and prices the vacuum (the one-coupling portfolio).

**(c) The Higgs mass with no bare term.** Under the no-bare clause $m_H^2$ must be
induced; one loop of anchor-scale census states (the portal species — Higgs-coupled,
leptophilic, exactly what the corrected census demanded) gives:

$$m_H \sim \frac{M_{\rm anchor}}{4\pi} \approx 125\ \text{GeV}$$

The plain-language form, registered with P-2026-042: *the anchor is where the
zero-point becomes non-zero* — the birth scale of mass; $m_H \to v \to$ every fermion
mass cascades from it.

## 3. The one-coupling portfolio (this file's family)

| floor | expression | the famous problem it answers |
|---|---|---|
| linear | $\varepsilon = c\,\bar f\,\alpha_c$ | the Hubble tension |
| squared | $\rho_\Lambda^{1/4} = \tfrac12\alpha_c^2 M_2$ | the cosmological constant |
| exponential | $M_{\rm anchor} = M_{\rm red}e^{-1/k\alpha_c}$ | the hierarchy problem |

One lepton coupling, three functional floors, all measured.

## 4. Kills

(i) the gap equation failing to produce k ≈ 1.3; (ii) the α_c MCMC killing 3α (the exponent's
coupling); (iii) the redesigned two-loop run landing the portal far from ~1.5 TeV;
(iv) HL-LHC exhausting 1–2 TeV without the portal states (the visible branch dies);
(v) any demonstrated bare-m_H² contribution (kills the no-bare reading outright).

## Sources
[BCS1957] (the gap form), [MachacekVaughn1983] (the loop structure), [Volovik2003],
the internal chain (PRTOE_DERIVATION_HUNT.md), P-2026-042. Full list:
[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## 5. Addendum (the stability audit)

The reading's owed consistency check — do the portal's Yukawas destabilize the Higgs
vacuum? — computed at one loop: the dip is SHALLOWER than the SM's own (−0.017 vs −0.022),
and the census's rising gauge couplings then return λ to **+0.146 at 10¹⁶ GeV**: the
endpoint is stable, unlike the SM's. The anchor does not merely coexist with the vacuum's
health; the census structure CURES the Standard Model's metastability. (One-loop;
two-loop inherited by the shooter redesign.)

## Where the dead ends live

The collider knife-edge P-2026-039 — once read as a sharp [1.00–1.19] TeV prediction — is
SUSPENDED: the two-loop term is a shift, not a smear, and the masses open to a "1–100 TeV
decade" pending the full two-loop run. That suspension, and the rigid-13 census count it rode
with, live in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) under **"The census &
roster count."**
