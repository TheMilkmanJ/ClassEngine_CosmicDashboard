# BBN — the transition recorded in the light elements

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*The only laboratory in nature that watched the electron-coupled scalar's phase transition live:
T_c = 177.10 keV sits inside the temperature range nucleosynthesis covers. The three light-element
abundances are three views of the same condensation.*

## The equations

- the ramp — ε's linear turn-on with temperature: ε(T) = ε·(1 − T/T_c), with
 **T_c = 177.10 keV**, the value the Koide kernel sources through τ = ½ln2 (193 keV is the
 perturbative μ=T fixed-point cross-check). The coded pipeline and the spliced run below ran at
 the earlier 179 keV and ε = 1.24%. Both replacements are quantified by direct computation, each
 from a wide scan through the production nuclear-reaction network rather than a pair of runs: the
 T_c move costs
 **−0.0036σ ± 0.0013** on D/H and the ε move **+0.0035σ ± 0.0004**. They carry opposite signs and
 near-equal magnitude, so applying both together is **−0.00005σ, zero to within ±0.0014σ** — and
 the re-run buys nothing (`scripts/prym_supersession_pricing.py`,
 [PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md)). The temperature the ramp is keyed to is
 itself now enforced by measurement rather than convention: re-keying the ramp onto the scalar's
 own kernel band (307–714 keV) moves helium-4 by +0.50σ to +1.37σ and deuterium by up to +0.79σ
 across that band — outside the bounds everywhere — so the abundances themselves pin the ramp's
 onset to the transition scale near 177 keV (the re-key grid run through the production splice,
 2026-07-27).
- ε at each epoch: n/p freeze-out (~800 keV): ε = 0 (the scalar is off — above T_c); the
 deuterium bottleneck (~70 keV): ε_eff = 0.61ε; lithium (~40 keV): 0.78ε
- the abundances. **Two runs, two baselines — they are not interchangeable, and D/H must never be
 read across them** (D/H ∝ ω_b^−1.66 in the production run — the most ω_b-sensitive abundance in
 the network; measured by a wide ω_b scan in `scripts/prym_omega_b_elasticity.py`, and within 4%
 of the textbook −1.6).

 (i) The effect of the active window — the temperature interval below T_c where ε is nonzero —
 measured on PRyM's default ω_b (`scripts/prym_ramped_splice.py`, the model's own ε(T) at
 T_c = 179 keV, ε = 1.24%). This run is what licenses the *relative* numbers; **its absolute D/H
 is not the model's prediction**, because its baseline is not the model's ω_b:

 | | Y_p (BBN) | D/H ×10⁵ | Li7/H ×10¹⁰ |
 |---|---|---|---|
 | baseline (ε = 0) | 0.246891 | 2.454498 | 5.438668 |
 | the scalar's active window | 0.248995 | 2.470340 | 5.452964 |
 | **the window's effect** | **+0.852%** | **+0.645%** | **+0.263%** |

 (ii) The model's prediction, on the model's own ω_b (production PRyM; the m_e–ω_b CMB
 degeneracy pulls ω_b up +1.1% against the in-house ΛCDM control on identical data). The
 baryon-density shift is propagated *here*, once:

 > in-house ΛCDM control **2.420** → *(ω_b +1.1%)* → pre-window **2.372** → *(the window,
 > +0.645%)* → **D/H = 2.387×10⁻⁵** — the standing prediction.

 against quasar-optical **2.527 ± 0.030** (Cooke) and own-ΛCDM **2.420**. The scalar sits on the
 low side of that split — a self-adverse, owned bet; **P-2026-027's radio measurement decides the
 observational side, and an unmade d(d,n)³He measurement decides the theory side (P-2026-058) —
 the larger of the two.**

 Where the deficit is made. Taking that chain apart: the ω_b step costs −1.01σ and the scalar's
 own window *gains* +0.31σ, so the nuclear physics helps and the baryon density carries the whole
 deficit. Because that same ω_b shift arrives with the H₀ result, deuterium and H₀ trade at
 **0.59σ per km/s/Mpc**. Full decomposition, the inventory of available levers, and the named
 missing state: [PRTOE_deuterium_row.md](PRTOE_deuterium_row.md).

- Y_p from the window alone is +1.09σ vs Aver 0.2453 ± 0.0034 (**+3.5σ** vs EMPRESS
 0.2370 ± 0.0034 — the unresolved helium disagreement), zero fitted parameters. This comparison
 **is** baseline-robust: Y_p ∝ ω_b^0.04, so the model's own ω_b moves it only to +1.12σ. The
 dark-radiation residual below adds to this.
- The width of that split, stated. Cooke's observational error **±0.030** combines with the
 post-LUNA **nuclear-theory error ±0.037** (PRIMAT, cite-verified — arXiv:2011.11320) to
 **±0.0476**, putting 2.387 at **−2.94σ** from Cooke before the dark-radiation residual is
 applied. This is the corpus-wide standing width: a third ±0.0300 for d(p,γ)³He is *not* folded
 in, because PRIMAT's ±0.037 is a post-LUNA Monte-Carlo error that already varies that rate, and
 adding it again double-counts the dominant deuterium-destruction channel
 ([PRTOE_deuterium_row.md](PRTOE_deuterium_row.md) §1). *(Against the observational error alone
 it is −4.7σ — an upper bound, not the tension.)* **What is genuinely open is not the budget but
 the code systematic:** the same source reports PRIMAT D/H = 2.439 against PArthENoPE 2.51–2.54
 — a **3.5% inter-code spread, 2.3× the nuclear error** — which is *not* folded in above. Folding
 it gives **−2.2σ** (half) to **−1.4σ** (full), and the model runs **PRyM**, a third code, so
 which central value the theory error should be taken around is undecided. ΛCDM itself carries
 1.85σ under PRIMAT. **The deuterium comparison is quotable at −2.5 to −1.4σ — the ±0.0476 budget
 with the dark-radiation residual applied and the code systematic named and unfolded.**
- The dark-radiation residual, applied. The standing high-decay-constant configuration commits to
 one dilution at genesis, ζ = T_dark/T_γ ∈ [0.25, 0.35], carrying a relativistic residual
 **ΔN_eff = (27/(7/4))·ζ⁴ = 0.06–0.24**. The residual's structure is derived — the 27→14
 confinement degrees of freedom, the scale T_c, and the reheat factor (27/14)^⅓ — leaving ζ, the
 dark-to-photon temperature ratio at genesis, as the sector's one un-derived input; the reheat
 cannot size it, because ΔN_eff is a ratio in which T_c cancels and only ζ⁴ survives, and a
 Planck-spectrum fit with ΔN_eff free prefers ζ ≈ 0.31, inside this range, so ζ is data-located
 rather than predicted (`scripts/cmb_realign_5d_neff.py`). That residual moves both abundances,
 in opposite directions — deuterium up toward Cooke (∂ln(D/H)/∂N = 0.135), helium up away from
 Aver (dY_p/dN = 0.011–0.013). Propagated on the model's own prediction above:

 - D/H = 2.387 → 2.407–2.463×10⁻⁵ across the ζ range. It moves toward Cooke's 2.527 and **does
 not reach it** — the gap closes from 0.140 to 0.064, never to zero, anywhere in that range.
 - Y_p = 0.24900 → 0.24978–0.25201, i.e. **+1.3 to +2.0σ vs Aver** (**+3.8 to +4.4σ** vs
 EMPRESS). Helium pays for deuterium's relief.

 The residual is larger below T_c than above, and that matters. The dark sector confines *at*
 T_c — that is what T_c is — dropping from 27 relativistic degrees of freedom (6 gluons + 21 from
 three flavours of SU(2) quarks) to 14 Goldstones (2N_f² − N_f − 1 for SU(2N_f) → Sp(2N_f)). At
 conserved dark entropy the bath reheats itself by (27/14)^⅓ = 1.245, so ΔN_eff below T_c is
 1.245× its value above. Since helium is decided at n/p freeze-out (~800 keV, above T_c) and
 deuterium at the bottleneck (~70 keV, below it), the two abundances do not see the same residual.
 Taking that into account: at the top of the ζ range deuterium reads **−0.84σ** rather than
 −1.29σ, and the joint across that range is **p = 0.022–0.079**.

 This is an estimate (linear responses; a full nuclear-code re-run is owed only if the joint
 becomes load-bearing). The shift is **hostage to its own falsifier** — CMB-S4 (±0.03) must see
 the same ΔN_eff, and a confirmed ΔN_eff < 0.03 or > 0.3 kills the committed ζ range from either
 side.

 And the sector cannot have carried more dark radiation than the microwave background will
 show. The obvious escape from an adverse BBN verdict would be for the dark sector to have held
 more relativistic energy while the elements formed and shed it before recombination. It cannot:
 anything converting to matter survives, growing as a⁻³ against the photons, and the observed
 dark-matter density caps the convertible share at **ΔN_eff ≈ 6×10⁻⁴** — a thousandth of the
 committed ζ range. Dumping the energy into photons instead violates the FIRAS spectral limit by
 three orders. So **ΔN_eff(BBN) ≈ ΔN_eff(CMB)**, and a single instrument reads both
 (P-2026-053).

- The joint verdict hinges on the code systematic — this is the sector's real open question, and
 the dark-radiation residual does not change that. Combining the two abundances (2 dof, in
 quadrature; **correlations between Y_p and D/H are ignored**, as in every joint quoted here):

 | D/H width used | joint p, pre-residual | **joint p across the ζ range** | reading |
 |---|---|---|---|
 | nuclear only (±0.0476) | 0.007 | **0.02–0.08** | **rejected to marginal** |
 | + half the inter-code spread (±0.0643) | 0.051 | **0.07–0.11** | marginal |
 | + the full inter-code spread (±0.0987) | 0.201 | **0.12–0.21** | comfortable |

 The model's BBN standing is decided by whether the 3.5% PRIMAT–PArthENoPE disagreement is an
 error or a choice — a question about the nuclear codes, not about the electron-coupled scalar.
 The model runs a third code (PRyM). The residual lifts every column by roughly a factor of two
 to three in p and leaves the ordering — and therefore the decision — untouched: on the quotable
 budget the sector is still adverse-leaning. **This stands on the record as adverse-leaning and
 unresolved**; it is not a result the model can settle by itself, and the honest range is quoted
 rather than the flattering end.

 *Both columns are computed on run (ii)'s baseline — the only one whose absolute D/H is a
 prediction — and against deuterium's full stated budget.*

- Why no amount of dark radiation fixes this. The two abundances respond to extra relativistic
 species with the *same* sign — both rise — but they need opposite moves: deuterium is low and
 helium is high. Scanning ΔN_eff past the committed ζ range, the joint likelihood peaks at
 ΔN_eff ≈ 0.26–0.29 (p = 0.06–0.08 on the quotable budget), so **the committed range tops out
 just under this lever's optimum** — 0.24 against 0.26. Pushing on: zeroing the deuterium tension
 takes ΔN_eff = 0.42, which lands helium at +2.5 to +2.7σ against Aver and **+4.9 to +5.1σ
 against EMPRESS** — trading a 2.5σ deficit for a 2.5σ excess and losing the EMPRESS side of the
 helium disagreement outright — and 0.42 is past where CMB-S4 kills the committed range anyway.
 **The sector cannot be healed by a one-parameter expansion-rate lever, whatever sources it.**
 This is the same anti-correlation the amplitude itself carries (helium wants ε lower, deuterium
 wants it higher, 2.2σ apart): it is the signature of what the light elements themselves record,
 and it is why the model cannot tune it.

 A lever confined below T_c escapes the anti-correlation — measured, not argued. Running PRyM
 with an extra density in the Friedmann equation only, switched on at T_c
 (`scripts/prym_below_Tc_boost.py`; the full-epoch control reproduces the standing coefficients,
 dY_p/dN = 0.0131 and ∂ln(D/H)/∂N = 0.1350):

 | lever | ∂ln(D/H)/∂N_eff | dY_p/dN_eff | deuterium gained per unit helium paid |
 |---|---|---|---|
 | present at both epochs | 0.135 | 0.0131 | 10.3 |
 | **confined below T_c** | **0.116** | **0.0041** | **28.2** |

 Deuterium keeps essentially all its leverage; helium pays a third as much. The reason is that n/p
 freeze-out is nearly the whole helium response but only part of the deuterium one — deuterium is
 set by burning time at the bottleneck, which lies below T_c. **So the sector's problem is not that
 no lever can heal it; it is that the model's own supply of this lever is small.** The confinement
 reheat above delivers a below-T_c excess of only 0.015–0.059, where healing deuterium outright
 would take ≈ 0.49 — a factor of eight to thirty-three, and the count that sets the supply is
 group-theoretically forced, so the shortfall cannot narrow. And an injection that large is
 **itself excluded**: it stands 1.6× over the CMB-S4 ΔN_eff bound, converting it to matter at the
 dCDF's radiation-to-dust onset overproduces dark matter by ~700×, and dumping it into photons
 violates the FIRAS spectral limit by three orders. **What blocks this route is data, not
 symmetry.**

 The lever that would work by a different road is one the model's field content cannot supply. A
 quark-mass shift moves deuterium through the binding energy B_D rather than through the
 expansion rate, so it does *not* drag helium the same way — it heals both abundances. The size
 needed is small: full ε on the quarks would move D/H by +12 to +18σ, so closing −2.5σ takes ~17%
 of ε, a shift of **δm̂/m̂ ≈ 0.2%** — which lands inside P-2026-006's registered healing band of
 0.14–0.21%, with its mandatory Y_p −0.5% co-signature pulling helium favourable too. But the
 electron-coupled scalar has no channel to the quarks at the size required. Its operator is the
 dark-neutral bilinear |Ψ|², a total singlet, which reaches the quark bilinear only at **two
 EW/EM loops — order (α/4π)²** — so the quark shift is many orders under the lepton one. The loop
 path (scalar → lepton loop → two photons → quark) delivers ~7×10⁻⁸, short of the ~2×10⁻³
 required by a factor of ~30,000, and a quark coupling anywhere near ε is independently excluded
 by deuterium itself at 12–18σ. *(Lepton number does not tighten this: |Ψ|² is phase-blind and
 L-neutral, so it screens the quark bilinear no more than the lepton one. The suppression is
 loop-order and the bound is data; a withdrawn symmetry argument for the same conclusion is
 recorded in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md). The margin is four orders
 wider than it needs to be.)* The model knows exactly what would repair its weakest sector and
 has no field that can supply it — which is why P-2026-006 is retained as a statement about a
 lever this model does not have.

- the elasticities: **d(Y_p)/dε = 0.00163 per %ε**, linear — multiplying by ε reproduces the
 window to ~3%. **Deuterium has no usable elasticity:** it is a bottleneck quantity, so its
 ε-response is nonlinear and a uniform-ε derivative under-predicts the window by a large margin
 (a 4-point PRyM scan gives ~0.0119 per %ε where the window itself implies ~0.0126). Use the
 measured window effect, +0.645%, not a derivative. N_eff is unmoved (3.04439) — ε shifts weak
 rates, not relativistic degrees of freedom.

## The deuterium repair route — a mechanism without a source

Deuterium is the most fragile nucleus nucleosynthesis makes: 2.22 MeV of binding against a bath
carrying 1.6 billion photons per baryon, whose high-energy tail keeps breaking it long after the
temperature falls below that. It cannot accumulate until T < B_D/ln(1/η) ≈ 105 keV — the deuterium
bottleneck — and the moment it does, it burns through to helium-4. **What survives is a residue,
not an equilibrium abundance**, which is why deuterium responds so sharply to everything.

That fragility cuts both ways, and it opens the one repair route that clears every constraint the
sector carries. An electromagnetic injection late enough to photodissociate **helium-4** produces
deuterium among the fragments. Helium sits at 8.3% of hydrogen by number against a deuterium
abundance near 10⁻⁵, so breaking a very small fraction of it is a large relative change in
deuterium.

The injection window is fixed by the photon bath, not chosen. Energetic photons pair-produce on
the CMB, capping the spectrum near m_e²/22T. That gates the two thresholds at different times:

| target | threshold | reachable below | time |
|---|---|---|---|
| deuterium | 2.22 MeV | T = 5.35 keV | t > 4.6×10⁴ s (1 day) |
| **helium-4** | 19.8 MeV | T = 0.60 keV | **t > 3.6×10⁶ s (42 days)** |

Between one day and six weeks an injection **destroys** deuterium — the wrong direction. Only after
~42 days can photons reach helium and start making it. The window opens at z ≈ 2.6×10⁶, which is
also where the universe loses its ability to thermalize injected energy back into a perfect
blackbody: earlier injections leave no trace whatever, later ones leave a spectral fingerprint.

Centring deuterium on the observed value requires destroying **1.7×10⁻⁵ of the helium** — about
30 eV of dissociation energy per hydrogen. What that costs elsewhere:

- helium itself: unmoved (ΔY_p = −4×10⁻⁶, or 0.001σ — the fraction destroyed is far too small
 to matter)
- spectral distortion: μ ≈ 2×10⁻¹¹, against the FIRAS limit of 9×10⁻⁵
- the joint: p = 0.135–0.43, with helium then the only residual

The co-signature is **helium-3**, which rises by roughly 14% — the same dissociation makes ³He and
³H alongside the deuterium. That is the abundance a referee will ask about, and it is weakly
constrained observationally because stellar processing dominates it. **That co-signature belongs
to the electromagnetic channel.** A hadronic injection carries a different one — non-thermal
**⁶Li** from nucleon spallation of ⁴He — which is bound far more sharply, and which this file does
not quantify.

The missing piece is the source, and the specification below is the electromagnetic one. A
candidate must satisfy all three of:

1. mass ≳ 20 MeV, so its decay cascade reaches the helium-4 threshold at all — this is the
 photodissociation threshold, and a hadronic parent must instead clear ~2m_N ≈ 1.9 GeV to put free
 nucleons into the bath;
2. lifetime ~10⁶–10⁸ s, placing the deposit inside the window the *photon* cutoff defines;
3. abundance delivering ~30 eV per hydrogen, and exhausted before recombination — that same
 energy is 2.2× the ionization energy of every hydrogen atom, so a residue surviving to z ≈ 1100
 would prevent recombination outright.

The scalar's own quantum cannot do it: its derived roll time puts that mass near 10⁻⁵ eV, twelve
orders below the threshold. The only states the standing configuration carries anywhere near the
scale are the Majoron's **MeV-range** states — and they sit at ~4.2 MeV, short of the ⁴He
threshold by 4.7–4.9×, and a threshold does not partly fire. The field content itself is provably
complete (P-2026-045), so the specification has **no candidate in the standing field content** —
[PRTOE_deuterium_row.md](PRTOE_deuterium_row.md) §6 carries the full accounting, including the one
source exempt from that count and the observation that excludes it. **This is a mechanism without
a source, and the field content cannot supply one** — any future candidate can be graded against
the three conditions above immediately.

*This route is distinct from P-2026-006's, which heals deuterium through a quark-mass shift and
carries a helium −0.5% and lithium −7…−13% co-signature. That route needs a coupling the model does
not have; this one needs a particle it has not named.*

## How PRTOE connects

The sector is rigid — every number derived or measured (T_c, ε = c·f̄·α_c, ω_b, the ε value at
each epoch): the model cannot tune what the light elements record. Deciding observations: the
radio measurement (P-027), the resolution of the helium disagreement, the T_c re-audit (flagged
and not taken — a rescue by retuning is forbidden), the α_c MCMC posterior. Adverse outcomes
stand on the record as adverse.

## Sources

[Cooke2018] (D/H), [Aver2021] + [EMPRESS2022] (the two poles of the helium disagreement),
[PRIMAT2018] (rates), [PRyMordial2023] (the nucleosynthesis code run with the window),
[DamourDyson1996] (the Oklo bound). Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## Lithium (2026-07-12)

The windowed run's full output (tools/PRyMordial): Li7/H = 5.439×10⁻¹⁰ (baseline) →
**5.453×10⁻¹⁰ (the scalar's active window, +0.26%)**. The scalar's windowed effect on lithium is
at the percent level and slightly upward — **the model neither causes nor cures the lithium
problem** (observed 1.6×10⁻¹⁰; the ×3.4 discrepancy stands exactly as the field left it, where the
modern consensus leans stellar depletion). The lithium abundance is safe — no new damage — and the
model claims nothing: an abstention, filed with the same prominence as the successes (the
strong-CP precedent). The lithium question this sector owed is therefore answered.

The abstention is robust from three directions: the ε value at the lithium epoch follows from the
same ε(T) as every other epoch, with nothing chosen for lithium; no earlier condition in the model
reaches the lithium epoch; and the ×3.4 discrepancy has a standing conventional explanation in
stellar depletion, which the model neither needs nor contradicts.

