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
> | **the anchor's identification with 4πm_H** | **yes** — it is where the gap equation needed a vacuum to sit in | **seated in the Fermi-point basement (§6) — structural, basement-gated** |
>
> So the arithmetic below stands and reproduces (residual 1.5014 against 3/2; M_anchor = 1576 GeV
> against 4πm_H = 1574, +0.14%), and §6 seats the interpretation. Other conditionality: the
> no-bare clause and P-2026-042's anchor identification. **The
> exponent's k is determined** — the screened-interaction integral, three concordant readings
> (1.360 / 1.36461 / 1.3602) inside the Eliashberg window. What the gap equation still owes is not
> its coupling but its **kernel**: no pairing interaction has ever been specified and no gap
> equation solved in the medium — the exponential form is adopted, the coupling computed, the
> constant derived. §6 states what the basement demands of that kernel.
> Referees: the α_c MCMC (the triangle) and HL-LHC (the portal search).

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
coupling); (iii) HL-LHC exhausting 1–2 TeV without the portal states (the visible branch dies);
(iv) any demonstrated bare-m_H² contribution (kills the no-bare reading outright).

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
SUSPENDED: the two-loop term is a shift, not a smear, and the masses open across a "1–100 TeV
decade". The perturbative program that would have narrowed that decade is closed, so the decade
is refereed by the collider search directly, and the census arrow's strain by the edge-convention
audit. That suspension, and the rigid-13 census count it rode with, live in
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) under **"The census & roster count."**

## 6. Where the gap equation sits: the Fermi-point basement

The anchor's identification with 4πm_H belongs to the induced-gravity basement, and **there is
no choice about which vacuum:** the standing corpus has exactly one with a fermionic
bath at the Planck floor (the str[k₁] = 0 roster: the Standard Model's 48
Weyl fermions plus three right-handed neutrinos, the same content P-2026-045 registers and
the same floor the dark SU(2) sector's own balance joins). A BCS-class gap equation needs
three things of its host, and the standing basement supplies two from recorded structure:

| what the gap equation needs of its host | status in the Fermi-point basement |
|---|---|
| **a fermionic bath at the cutoff** | **met, recorded** — the finiteness roster IS the Planck-floor fermion content; Fermi-point universality (the Volovik frame the quantum-gravity file already rides) is precisely the statement that such a vacuum's low-energy fermions are generic |
| **the coupling kα_c reaching the basement** | **met, recorded** — k is the screened-interaction integral (basement-independent by construction; the corpus's one shared k), and α_c is the medium's coupling, which reaches the Planck floor through the induced loop — the SAME loop that makes gravity itself (no new bridge is invented; the anchor uses the induced-G channel that no-bare-G already requires) |
| **the attractive channel** (the phonon's analog: what pairs the census states) | **OWED — the one genuine residual.** The medium's own exchange must be shown attractive in the Fermi-point vacuum. This is basement-build territory, and it is the SAME gate the neutrino sector's seat constant b already waits at — the rehome adds no new gate, it joins a standing one |

The arithmetic is self-contained — measured m_H, the shared k, the derived 3/2, reproducing
1576 GeV against 4πm_H = 1574 at +0.14%. Putting the gap equation in this vacuum makes the
hierarchy answer and the gravity answer one statement: **the same fermionic floor that induces
G pairs at kα_c, and the electroweak scale is that pairing's gap.** Grade: **structural,
basement-gated** — two of the three requirements met by recorded structure, the third sharing
its gate with the seat constant b.

### 6a. What the basement demands of the kernel

The vacuum constrains the pairing sharply. Write the pairing integral in cutoff units, J ≡ ∫₀^Λ [ρ(E)/ρ₀]·dE/√(E² + Δ²), so the gap condition is
λ·J = 1 with λ = kα_c = **0.029874** — i.e. the kernel must deliver **J = 33.47**.

| host spectrum | J as Δ → 0 | verdict |
|---|---|---|
| **finite DOS in the pairing shell** (ρ = ρ₀) | J = asinh(Λ/Δ) → **diverges** | reaches 33.47 at Δ/Λ = 5.8×10⁻¹⁵ — **14.2 orders, against the measured 15.19.** The divergence IS the hierarchy: an exponentially small scale from an O(10⁻²) coupling |
| **a Fermi point** (ρ ∝ E², linear node) | J → **1.50** (equal-states) / **0.50** (cutoff-DOS) — **convergent** | **cannot pair.** No log, no exponential; pairing needs λ ≥ 2/3, and the model has 0.0299 — **subcritical by 22–67×** |

So the node cannot host the pairing. A Fermi-point vacuum's phase space vanishes at the node
exactly where BCS needs it finite, and no amount of weak coupling recovers it. **So the first
requirement is stricter than the table states it:** the host needs not just a fermionic bath at
the cutoff but *a fermionic bath with finite density of states in the pairing shell*. A
Fermi-point vacuum has one, but only at its bend-over, where the linear cone terminates and the
full spectrum resumes. The node is the infrared remnant; the pairing is a cutoff-scale event —
and the third requirement inherits that: the attractive channel must act on the bend-over
states, not the cone's.

**The two 3/2's are different objects.** Under equal-states normalization the node's saturation
is exactly d/2 = **3/2**, numerically the exponent's own constant — but the exponent's −3/2 is
not the node's phase-space deficit. Give the spectrum a crossover
(ρ ∝ E^p below a bend-over E_*, flat above) and the integral is exactly J = 1/p + ln(Λ/E_*)
— verified numerically to four decimals at p = 1, 2, 3 — so the gap condition reads
ln(Λ/E_*) = 1/λ − 1/p. Two failures at once: it fixes the **node-emergence scale** rather than
a gap (Δ drops out — the node, not the gap, regulates the infrared), and it carries the **wrong
sign**, a deficit that *raises* the scale where the anchor needs suppression. At p = 2 it lands
11.65 TeV against the anchor's 1576 GeV — over by e² = 7.4×. **The node-deficit route to the 3/2
does not source the exponent's constant**: route 6's equipartition reading carries it alone,
and of the two it is the one with the sign.
