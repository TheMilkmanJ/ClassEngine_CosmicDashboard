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
> against 4πm_H = 1574, +0.14%), and §6 seats the interpretation. **Read that 1576 as a convention
> value, not a prediction:** solving the gap equation exactly rather than adopting its form gives
> 3152 GeV — the booked expression is the exact one with a factor two absorbed (§6d) — and
> and §6j's electroweak-precision bound is a roster bound, not a scale bound. Every anchor
> number quoted in §2 below carries that qualification. Other conditionality: the
> no-bare clause and P-2026-042's anchor identification. **The
> exponent's k is determined** — the screened-interaction integral, three concordant readings
> (1.360 / 1.36461 / 1.3602) inside the Eliashberg window. Its **kernel** is the live front: §6
> seats the gap equation in the basement and §6b fixes the channel as particle-hole, so what is
> owed is no longer an object but a computation — showing the bend-over spectrum condenses in
> that channel at λ = 0.03.
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
two-loop piece is unowned: it was routed to the shooter redesign, and that program closed as
mooted, so nothing inherits it.)

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
three things of its host, and the basement supplies all three:

| what the gap equation needs of its host | status in the Fermi-point basement |
|---|---|
| **a fermionic bath at the cutoff** | **met, recorded** — the finiteness roster IS the Planck-floor fermion content; Fermi-point universality (the Volovik frame the quantum-gravity file already rides) is precisely the statement that such a vacuum's low-energy fermions are generic |
| **the coupling kα_c reaching the basement** | **met, recorded** — k is the screened-interaction integral (basement-independent by construction; the corpus's one shared k), and α_c is the medium's coupling, which reaches the Planck floor through the induced loop — the SAME loop that makes gravity itself (no new bridge is invented; the anchor uses the induced-G channel that no-bare-G already requires) |
| **the attractive channel** (what pairs the census states) | **met — §6b.** The channel is particle-hole, not particle-particle: a charged Cooper condensate is excluded by thirty orders on the photon mass, and particle-hole Coulomb at α_c binds by construction. The residual is narrower than the requirement — showing the bend-over spectrum condenses in that channel at λ = 0.03 |

The arithmetic is self-contained — measured m_H, the shared k, the derived 3/2, reproducing
1576 GeV against 4πm_H = 1574 at +0.14%. Putting the gap equation in this vacuum makes the
hierarchy answer and the gravity answer one statement: **the same fermionic floor that induces
G pairs at kα_c, and the electroweak scale is that pairing's gap.** Grade: **structural** — the
three requirements met, two from recorded structure and the third by the channel argument of
§6b, with the residual now a computation inside the basement rather than a missing object.

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
the cutoff but *a fermionic bath with finite density of states in the pairing shell*. What
supplies one is a **finite chemical potential** — a Fermi surface at some k_F inside the linear
cone, where ρ(E_F) = k_F²/2π²v³ is finite and the shell is locally flat. It is not the bend-over:
§6c shows the anchor requires exactly the cone's density of states, and the van Hove enhancement
at a band extremum would push it eight orders. So the node is what survives in the infrared, the
bend-over is only the cutoff, and **the pairing is a Fermi-surface instability at finite μ inside
the cone** — which is also what the third requirement acts on.

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

### 6b. Which channel pairs

The gap equation's coupling is α_c = 3α — electromagnetic, times the spatial dimension. That
fixes the channel, because the two ways to pair at electromagnetic strength do not both survive.

**Particle-particle is excluded, by thirty orders.** A Cooper-style condensate of two charge-e
fermions carries charge 2e, so it breaks U(1)_EM at the anchor scale and the photon takes an
Anderson-Higgs mass m_γ ~ 2e·v ≈ 9.5×10¹¹ eV. The recorded bound is m_γ < 10⁻¹⁸ eV
([PRTOE_light.md](PRTOE_light.md)), a line the model's own Goldstone reading of light already
treats as a kill. For a charged condensate to clear it the pairing scale would have to sit below
1.65×10⁻¹⁸ eV, which nothing in the sector can do. The same-charge Cooper reading is not merely
unsupported; it is dead.

**Particle-hole is what remains, and it pays the attractive channel for free.** The condensate
⟨ψ̄ψ⟩ is electrically neutral, so the photon stays exactly massless, and the interaction between
a particle and a hole at coupling α_c is attractive by construction — opposite-sign sources need
no phonon analog to bind them. **The requirement §6 lists as owed is discharged by the channel
itself**, not by a new object. Three things corroborate the reading independently:

| corroboration | what it says |
|---|---|
| **k's own form** | k = (1/π)∫₀¹dq/(q + 2α_c/π) is a statically-screened Coulomb momentum integral, screening length 2α_c/π = 0.0139 — the excitonic kernel exactly. A phonon kernel does not produce ln(1 + π/2α_c)/π: the integral the corpus already runs on was Coulomb all along |
| **the density of states (§6a)** | a coupling λ = 0.0299 cannot pair at a node and needs finite DOS in the shell — which is the known condition for particle-hole condensation at a Dirac point, where the instability otherwise demands supercritical coupling. The two constraints agree rather than compete |
| **the 4π** | ⟨ψ̄ψ⟩ is a Dirac mass, so the gap is a dynamically generated fermion mass and m_H = M_anchor/4π reads as its one-loop suppression (+0.13%). §1's "the Higgs mass is that gap's one-loop echo" acquires the mechanism it was asserting |

**The quantum numbers check out.** The condensate must break electroweak symmetry while carrying
no electric charge — weak isospin but not charge — and the roster supplies exactly that. Take
ψ_L a doublet and ψ_R a singlet: the bilinear ⟨ψ̄_L ψ_R⟩ is an SU(2)_L doublet, and its neutral
component carries Q = −Q_L + Q_R = 0 identically, because a particle-hole pair of the *same*
field cancels its own charge whatever that charge is (verified across the up-, down- and
charged-lepton lines). So the condensate is electrically neutral, as the channel requires.

**What that does *not* license.** The bilinear having a Higgs-like quantum-number assignment does
not make it the Higgs. This file's §2(c) is explicit that the Higgs is elementary and its *mass
parameter* is induced — "under the no-bare clause m_H² must be induced; one loop of anchor-scale
census states gives m_H ~ M_anchor/4π" — with the vev remaining the Standard Model's own. The
condensate supplies the states whose loop induces m_H², not the electroweak order parameter. §6j
records what follows from that distinction, and what does not. Both are computations inside the basement rather than new assumptions, so the residual
has changed from *find an attractive channel* to *show this one condenses*.

**The selection rule is the corpus's own.** What decides the channel here — *the condensate must
carry no electric charge* — is the rule the neutrino sector already applies from the other side.
There the seat's occupant is the roster's one neutral fermion, and with no charge to dress, "the
only gauge-invariant bilinear the medium can write on the seat it shares is the direct Majorana
term" ν̄₁ᶜν₁ — a **particle-particle** bilinear, admissible exactly because a neutral fermion's
Cooper condensate carries no charge to break U(1)_EM with. So the charged nine take the
particle-hole channel and the neutral seat takes Majorana, and both follow from the one
requirement that electromagnetism survive the vacuum. The tenth-channel operator and the anchor's
pairing are one rule read at two seats, which is why neither needed a phonon.

### 6c. The gap equation, solved

With the channel fixed, the equation can be written down and solved rather than adopted. Take the
linearised particle-hole gap equation with instantaneous screened-Coulomb exchange in the rainbow
approximation. It factorises the usual way — a Fermi-surface average of the interaction, times the
density of states, times the radial log — so λ = N₀·⟨V⟩_FS and the exponential follows.
Heaviside–Lorentz throughout: e² = 4πα_c, V(q) = e²/(q² + m_D²), and N₀ = k_F²/π²v at linear
dispersion for one band, both spins.

**The Fermi-surface average, in its natural variable.** Write the momentum transfer as
u ≡ q²/q_max² = q²/(4k_F²) = sin²(θ/2). Then du = sin θ dθ/2, and the solid-angle average is
exactly ∫dΩ/4π = ∫₀¹du — the full sphere, no restriction anywhere. **The ∫₀¹ the corpus carries
is not a cut**; it is the whole Fermi surface, written in the variable whose range is unity.

**The screening, and where the 2 lives.** Thomas–Fermi gives m_D² = e²·N_screen. A particle-hole
condensate has two bands at the surface and *both* polarise, so N_screen = 2N₀ — while the pair
itself is one electron and one hole, so the gap equation's own density of states is N₀. That
**2-for-screening, 1-for-pairing** asymmetry is the defining structure of the channel §6b selects,
and it is the entire content of the constant:

$$b \;\equiv\; \frac{m_D^2}{4k_F^2} \;=\; \frac{e^2\,(2N_0)}{4k_F^2} \;=\; \frac{2\alpha_c}{\pi}
\;=\; 0.0139369$$

**So k is derived rather than adopted — on a host this corpus does not record, which the three conditions below name:**

$$\lambda \;=\; N_0\,\langle V\rangle_{\rm FS} \;=\; \frac{\alpha_c}{\pi}\ln\!\Big(1+\tfrac{1}{b}\Big)
\;=\; \frac{\alpha_c}{\pi}\ln\!\Big(1+\frac{\pi}{2\alpha_c}\Big)\;\equiv\;k\,\alpha_c,
\qquad k = 1.36461191$$

against the booked 1.36461191 — every digit carried, nothing fitted.

**What that does and does not fix.** λ is now derived; the *anchor* still needs a prefactor, and
the two available conventions differ by exactly two. Fed through the booked form,
M_red·e^(−1/(kα_c) − 3/2) = 1576.1 GeV against 4πm_H = 1573.9. Fed through the gap equation's own
exact solution, Δ = 2Λ_shell·e^(−1/λ) = **3152 GeV**. §6d shows the booked form is the exact one
with the factor two absorbed. §6j's electroweak bound constrains the portal roster, not the scale —
so the numbers quoted as the anchor's landing in §2 and in this file's header are the *convention*
value, not the derivation's output.

The sensitivity is why the factor matters rather than being bookkeeping: ∂lnM/∂lnk = 1/(kα_c) =
**33.47**, so the anchor amplifies any error in k thirty-threefold. One band screening instead of
two gives k = 1.58305 and an anchor at 1.6×10⁵ GeV. The 2 is not a convention that happened to be
lucky — it is the electron-plus-hole polarisation, and mistaking it misses by two orders.

**Three structural conditions, and they are additions to this corpus.** The calculation above is a
condensed-matter one, and it needs a host with properties the basement is not currently stated to
have. Named plainly, because the numerical agreement makes them easy to skip past:

1. **A finite chemical potential.** The whole Fermi-surface treatment — the average, the density of
   states, the shell — presupposes μ ≠ 0. This corpus's basement is a **Fermi point** (the Volovik
   frame; "three Fermi points" in the light file), which is μ = 0. §6a shows a Fermi point cannot
   pair at this coupling, and the finite-μ Fermi surface is what I introduced to resolve that. It is
   not recorded anywhere else. **The corpus's other finite-μ statements do not supply it**, and the
   near-miss is worth naming so it is not mistaken for a match: the identity paragraph and the
   condensed-matter room both describe the medium as "the phase EFT of a complex condensate at finite
   chemical potential", but that μ is the dark condensate's at basin entry — μ = m ≈ 2.24×10⁻²⁰ eV,
   at z_x ~ 10⁵ — some sixty orders below the Planck-floor basement this section needs, and a
   different object in the model's own layering.
2. **Thomas–Fermi screening.** A Debye/Thomas–Fermi mass requires real carriers at finite density or
   temperature. At a Fermi point with μ = 0 there are none, and the atlas separately scores the
   medium's pre-basin phase as "a gapless acoustic gas, not a plasma (no Debye, no gap)".
3. **Two compensated bands.** The factor 2 in the screening needs an electron pocket and a hole
   pocket at the same Fermi level — a compensated semimetal. The corpus describes no such band
   structure.

**So §6c is a conditional derivation, and its conditions are load-bearing.** *If* the basement has a
compensated two-band Fermi surface at finite chemical potential with Thomas–Fermi screening, *then*
k = 1.36461191 follows exactly, with nothing fitted. That the reconstruction lands on the corpus's
booked value to every digit is either a strong hint about the basement's structure or a coincidence,
and it is worth weighing as evidence — but it is evidence for the conditions, not a derivation from
recorded structure. Supplying or refuting those three is now the basement build's sharpest task.

**What the derivation rests on beyond that.** N₀ = k_F²/π²v assumes linear dispersion at the pairing shell,
and §6a puts that shell at a finite-μ Fermi surface *inside* the cone, not at the bend-over — so the
density of states is owed, as is whatever fixes k_F. The rainbow truncation and the equal-density
assumption for the two bands are the other two. Each is a computation inside the basement rather
than a missing object, and each is on the board.


### 6d. What the gap equation pins, and what it does not

§6c's λ is solid: it is scale-free, verified in two independent variables, and depends on no
convention. The **anchor** is a different matter, because it needs a prefactor as well as an
exponent, and ∂lnM/∂lnk = 33.47 amplifies every O(1) in sight.

**What the exponent fixes.** Writing the model's form against a gap equation's,
M = M_red·e^(−1/λ−3/2) versus M = Λ_shell·e^(−1/λ), identifies

$$\Lambda_{\rm shell} \;=\; M_{\rm red}\,e^{-3/2} \;=\; 0.223\,M_{\rm red}$$

so **the −3/2 is not a correction to the exponent — it is the statement that the pairing shell's
cutoff is the Planck floor dressed down by the equipartition boost**, which is exactly what route
6 derives from ⟨E_kin⟩/T = 3/2. The two readings are one statement, and that is a real
consistency: the constant the exponent needs and the constant equipartition supplies coincide.

**What is not fixed — three O(1)s, each worth a factor.**

| piece | size | why it is open |
|---|---|---|
| the exact-solution factor | ×2 | the gap equation gives Δ = 2Λ·e^(−1/λ) (asinh, not a bare log); the booked form has no 2, so the convention absorbs it into the −3/2 |
| the shell's density-of-states correction | +0.07% to +1.4% in λ | a pairing shell is *symmetric* about E_F, so the cone's linear variation cancels between the particle and hole sides and only ξ²/E_F² survives; its size depends on E_F |
| where the Fermi surface sits | E_F/M_red ∈ [0.223, 1] | k cancels k_F entirely, so k_F enters only through the correction above, bounded below by Λ_shell and above by the cutoff |

**So the anchor is a factor-of-a-few prediction.** Across the allowed range these compound to
roughly **1.6 to 5.2 TeV** from these two terms alone — §6e widens it to 1–8 TeV once the vertex
correction and the band-matching requirement are carried — with the booked 1576 GeV at the bottom
edge, the value
obtained when the exact-solution factor is absorbed and the density of states is treated as flat.
The +0.14% agreement with 4πm_H is therefore **a coincidence of one convention within that band**,
not a measurement of it.

What survives, and it is the part that matters: the *mechanism* is derived end to end — the
channel (§6b), the screening constant and measure (§6c), the shell cutoff as the equipartition-
dressed floor (above) — and it puts the electroweak scale at a few TeV from the Planck floor and
α alone. A few TeV is what HL-LHC tests. Four significant figures was never what the calculation
could support.


### 6e. What equal screening requires, and what nothing yet supplies

§6c's screening constant carries a factor 2 — both bands polarise — and that factor is the most
load-bearing number in the chain: ∂lnM/∂r ≈ 11.6 for N_screen = (1 + r)N₀, so a 25% asymmetry
between the bands moves the anchor by a factor 18. It is not an assumption.

**Neutrality gets most of the way, and not all of it.** The basement vacuum carries no net electric
charge, so a neutral semimetal is *compensated*: n_electron = n_hole exactly. With n ∝ k_F³ that
fixes k_F(e) = k_F(h) whatever the velocities. But the density of states is k_F²/v, so what survives
is **r = v_e/v_h** — compensation equalises the *densities*, not the *densities of states*, and the
remaining factor is a velocity ratio neutrality says nothing about.

**And one cone cannot supply both pockets.** At finite chemical potential a single Dirac cone has a
Fermi surface in one branch only; the other branch is entirely below or above μ. So the two pockets
the screening needs must come from **two distinct bands**, whose velocities are independent
parameters. r = 1 is therefore a genuine structural requirement on the basement's band structure —
two velocity-matched bands — and not something the vacuum's neutrality delivers for free.

**The residual, priced.** The anchor's response to the velocity ratio is steep: a **1% asymmetry
shifts it 13%, 5% shifts it by roughly a factor two, and 10% by a factor four.** So the two bands
must be velocity-matched at the percent level for the anchor to hold at all, and nothing yet
supplies that match. It is not the node's particle-hole symmetry — that concerns one cone's two
branches and does not reach two separate bands. **This is the sharpest constraint the basement build
must meet**, and it is a constraint on band structure rather than on a symmetry the vacuum already
has.

**The band, assembled.** Three independent O(1)s survive: the vertex correction to the rainbow
truncation, which enters at relative order λ = 3% and so is a factor ≈ 2.7 either way; the Fermi
surface's position within Λ_shell ≤ E_F ≤ M_red, worth ≈ 1.6; and percent-level particle-hole
asymmetry, worth ≈ 1.1 per percent. Compounded, **the anchor is a few TeV to within a factor of a
few** — call it 1 to 8 TeV — with the vertex correction dominating. Every piece of the mechanism is
derived; the precision is what the truncation costs.


### 6f. At what scale is α evaluated?

Sizing the vertex correction turned up a larger question the chain has never asked. §6c's
derivation treats α_c as an electromagnetic coupling — Coulomb exchange, Thomas–Fermi screening,
e² = 4πα_c — and the pairing sits at a Fermi surface near M_red. **An electromagnetic coupling
runs.** The corpus evaluates it at zero momentum.

The leverage is the same 33× compounded with k's own response: ∂lnM/∂lnα_c = **25.8**.

| α used | 1/α | k | M_anchor |
|---|---|---|---|
| **α(0) — as booked** | 137.036 | 1.3646 | **3152 GeV** |
| α(M_Z) | 127.951 | 1.3431 | 1.76×10⁴ GeV |
| naive extrapolation toward 10¹⁸ GeV | ~106 | 1.2841 | 1.22×10⁶ GeV |

The 7.1% between α(0) and α(M_Z) is already a factor 5.6 on the anchor; running to the pairing
scale is a factor of hundreds. **So the anchor's landing requires the zero-momentum value
specifically, at a process eighteen orders above the scale that defines it.**

The tension is sharp and it cuts both ways. If α_c is genuinely electromagnetic — which is what
§6c's Coulomb kernel and Thomas–Fermi screening assume — then it must be evaluated at the pairing
scale, and the anchor moves by orders. If instead α_c is a *medium* constant that happens to equal
3α(0) numerically — which is how P-2026-040 registers it, as a value bet rather than an
identification with running QED — then it need not run, but the Coulomb form and the screening
that §6c derives its factor 2α_c/π from both need a separate justification, because they were
imported from electromagnetism.

Both readings cannot be held at once, and the chain currently holds both: the *kernel* is
electromagnetic, the *coupling* is not allowed to run. Resolving that is now the single largest
exposure in the hierarchy chain — larger than the vertex correction it was found while sizing, and
larger than every O(1) in §6e.


### 6g. Which α, sharpened

Three things narrow §6f's fork without closing it.

**The corpus's own stance is principled, and it is horn (b).** MATH_SPINE records
"α_c = 3α = d·α — *the dCDF's* condensate coupling (α is its Goldstone's — light **is** that
Goldstone)", and the superfluid file carries the same identification. So α is not an external gauge
coupling imported into the medium: it is the medium's coupling to its own massless Goldstone, which
is also why the exchange has a 1/q² form. On that reading the kernel is not borrowed from
electromagnetism — it *is* electromagnetism, because electromagnetism is the medium.

**The running direction is adverse, which is a real constraint.** Solving for the coupling that
would land the anchor exactly on 4πm_H gives α_c = 0.021316, i.e. **1/α = 140.7 at the pairing
scale — weaker than the infrared 137.04.** Running takes α the other way: stronger in the
ultraviolet. So running cannot rescue the anchor's value under any amount; it can only move it
further. Horn (a) is disfavoured by sign, not merely by magnitude.

**But horn (b) carries a double-counting hazard.** α(0) is the *fully infrared-screened* coupling —
the value after all vacuum polarisation has been summed. §6c then adds Thomas–Fermi screening from
the basement's own fermions on top of it. Either α(0) is the bare coupling at the basement's cutoff
and the two screenings are distinct, or it already contains the basement's polarisation and §6c
counts it twice. Nothing yet decides which, and the answer is worth a factor of a few.

**One further consequence, recorded because it touches the exponent.** Solving exactly gives
Δ = 2Λ·e^(−1/λ), so matching the booked form requires Λ_shell = M_red·e^(−3/2−ln2) = 0.1116 M_red
rather than 0.2231. The shell cutoff wanted by the exact solution therefore differs from the
equipartition constant route 6 derives by exactly **ln 2** — which is not a free number in this
corpus, since τ = ½ln2 already sits at the Koide kernel. Whether that is a coincidence or a seam is
not decided here.


### 6h. The residual, named exactly

The double-counting worry of §6g resolves, and what is left is sharper than it was.

**It is not double-counting.** Vacuum polarisation and Thomas–Fermi screening are physically
distinct — the first is virtual pairs and exists at zero density, the second needs real carriers
and scales as e²N₀ — and they add in the polarisation, Π = Π_vac + Π_matter. The correct
prescription is therefore α evaluated *at the momentum scale*, with Thomas–Fermi on top of it. No
term is counted twice. What is wrong is the scale.

**Where α_c's value is actually fixed.** α_c enters ε = c·f̄·α_c = 1.2543%, the electron-mass shift
at recombination — an atomic-scale observable — and P-2026-040's referee is a cosmological chain.
Both are infrared. **The amplitude pins α_c in the infrared; the anchor spends it at the Planck
floor.** One number, two regimes eighteen orders apart, with no statement connecting them.

**And the Goldstone defence has a matching problem.** If light *is* the medium's massless Goldstone,
then α *is* the electromagnetic coupling — and that coupling demonstrably runs. A medium coupling
which is electromagnetic cannot also be scale-independent. The only escape is that α_c (the
condensate's coupling) and α (its Goldstone's) are genuinely different objects, tied by d = 3 — but
a relation between two couplings holds *at a scale*, and which scale is exactly what is unstated.

**So the residual is one missing sentence, and it is nameable:** *at what scale does α_c = 3α hold?*
The amplitude answers "the infrared" by construction. If that is the right answer, the anchor needs
α_c run up to the pairing shell and lands orders higher. If instead the relation is meant at the
basement, then the amplitude's use of it in the infrared is the loose end and ε inherits the same
question. The corpus currently uses the infrared value in both places, which cannot be right in both.


### 6i. The scale, data-selected — and two claims that now stand or fall together

§6h reduced the residual to one question: at what scale does α_c = 3α hold? The corpus already
contains the discriminator, and it is **A_s**.

α_c enters at four points spanning cosmic history — ε at recombination and ρ_Λ at the eV scale,
both infrared; A_s at genesis and the hierarchy anchor at the Planck floor, both ultraviolet. The
anchor cannot test the scale, because ∂lnM/∂lnα_c = 25.8 swamps it. **A_s can**: its sensitivity is
∂lnA_s/∂lnα_c = 3.69, and it is measured to ~1.4%.

| α_c | A_s | vs measured 2.088×10⁻⁹ |
|---|---|---|
| **3α(0)** | 2.0807×10⁻⁹ | **−0.4%** |
| 3α(M_Z) | 2.681×10⁻⁹ | +28.4% |
| 3α extrapolated toward 10¹⁷ GeV | 5.395×10⁻⁹ | +158% |

**A_s is a primordial observable, and it selects the infrared value.** So the answer to §6h is
horn (b), and it is *data-selected* rather than assumed, in the same way the corpus already selects
f̄'s coupling form: **α_c is a scale-independent medium constant, numerically 3α(0)**, and using the
same number at recombination, at the eV scale, at genesis and at the Planck floor is consistent.
The "orders higher" worry of §6f is therefore lifted — the anchor's use of 3α(0) is correct, and its
band stays where §6e put it.

**The condition, stated because it binds.** A_s = C·(α_c/4πk)³ with the count C an unmechanized
O(1) that the corpus claims is exactly 1. If C were instead ≈ 0.385, a running α_c would reproduce
A_s and the test evaporates. So this argument rides C = 1 — which means **"the count is exactly
(4πk/α_c)³" and "α_c does not run" now stand or fall together.** They were previously independent
claims; they are one joint now, and either one failing takes the other with it. That is a real
tightening of the corpus's exposure and it is recorded as such rather than as a free win.


### 6j. Electroweak precision — the constraint that actually applies

An earlier pass of this section priced the anchor as a *composite* Higgs and derived a
compositeness bound from the S parameter, plus an extended-technicolor flavour problem. **That was
a misreading of this file's own §2(c)** and both are withdrawn: the Higgs here is elementary, its
mass parameter induced by one loop of anchor-scale states, and its vev the Standard Model's. A
model with an elementary Higgs inherits neither the compositeness bound nor the flavour problem —
the Yukawas are the Standard Model's own, so no extended-technicolor operators exist to hit K⁰
mixing.

**What does apply is a counting bound.** The anchor-scale portal species carry electroweak quantum
numbers, and a degenerate heavy doublet contributes ΔS = 1/6π = 0.053 **without decoupling** — the
contribution is mass-independent. Against |S| ≲ 0.14:

| new electroweak doublets | S | |
|---|---|---|
| 1 | 0.053 | allowed |
| 2 | 0.106 | allowed |
| 3 | 0.159 | excluded |

**So electroweak precision limits the portal roster to at most two new doublets**, and says nothing
about where the anchor sits. That is a real constraint on the census's portal content and a
falsifiable one — but it is a roster bound, not a scale bound, and it leaves §6d's band and the
4πm_H identification untouched.


### 6m. Cold or hot? The screening constant discriminates, and not in §6c's favour

§6c's three conditions (finite chemical potential, Thomas–Fermi screening, two compensated bands)
would all dissolve if the basement were read as **hot** rather than cold: at the Planck floor the
roster sits in a thermal bath, and a relativistic plasma at μ = 0 screens by the **Debye** mass
without needing any chemical potential, while particles and antiparticles are present in exactly
equal numbers by CPT — giving r = 1 with no semimetal band structure required. That reading is also
closer to this corpus's own cosmology, where the Planck era is hot.

**It does not reproduce the constant.** The booked b = 2α_c/π = 0.013937 corresponds to
m_D²/T² = 2e²/π² = e²/4.94. The standard thermal Debye mass is e²T²/3 (or e²T²/6 per Weyl), giving
b = e²/12 = 0.022925 or e²/24 = 0.011463 — **off by 1.64× and 0.82× respectively**, at every
standard normalisation.

The cold degenerate reading, by contrast, reproduces it exactly from standard pieces and no chosen
ones: e² = 4πα_c, N₀ = k_F²/π²v for one band with both spins, the factor 2 for the second band, and
b = m_D²/4k_F² in the natural transfer variable.

**So the screening constant is itself a discriminator, and it points the wrong way.** If k's
screened-exchange reading is physics rather than coincidence, the host is **cold and degenerate** —
which the basement, as a hot Planck-era Fermi-point vacuum, is not. Three readings remain and they
should be held apart:

| reading | status |
|---|---|
| the host is cold and degenerate | reproduces k exactly; contradicts the recorded basement |
| the host is the hot Planck-era bath | matches the recorded basement; misses k by 1.6–2× |
| k's screened-exchange form is a coincidence | leaves k as the recognised closed form it was before today, with §6a's no-pairing-at-a-node result standing against the pairing reading generally |

Nothing here selects among them, and the third is not the least likely. What today's work established
is that the choice is now sharp and numerical rather than interpretive.
