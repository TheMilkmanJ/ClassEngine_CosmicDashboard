# Basement Roster — Defender vs Challenger debate on SU(2) N_f=3 T_c/√σ

> **DATED RECORD — the τ-plausibility fight, complete as debated.** Numbers herein are the
> 0.3503/179-keV era's. The standing configuration has since moved to **the P-2026-048
> two-point fork**: 0.3503 (the observation inverted) vs **0.34657 = ½ln2** (the kernel
> candidate; the standing T_c = τ·m_e = 177.10 keV rides it) — 1.1% apart, both inside the
> registered window, the lattice adjudicates. Every centering conclusion below ("permitted
> at the edge, not favoured at centre"; the clean center at τ ≈ 0.357–0.368) applies to
> BOTH fork points — a fortiori to the lower kernel point, which sits 1.1% further from
> the analytic center than the value debated here. The lattice campaign now referees three
> numbers of the same theory (T_c/√σ, F_π/√σ, w·√σ — the forced-combination file §4), and
> the circulation note (PRTOE_lattice_note.md) carries the ask.

**The question:** The PRTOE flagship dark-energy value needs τ = T_c/√σ_dark ≈ **0.3503** for a dark **SU(2), N_f = 3** confining sector. Is that value plausible? Nobody has the lattice number — this is an analytic-estimate fight.

**Ground rules in force:** no commits/git, no MCMC/PolyChord/CLASS runs, regular Python allowed for estimates. Both sides show all work so a human can backtrack every step.

---

### DEFENDER — Round 1

**My thesis:** τ ≈ 0.3503 is a *plausible, defensible* analytic estimate for the chiral-transition-to-string-tension ratio of a dark SU(2), N_f = 3 confining vacuum. It is not a proven number — no lattice result exists — but every independent estimate I can construct lands it in the right neighbourhood, and the one that carries the burden (the quark-driven reduction of T_c/√σ) is *supported*, not merely asserted. I will defend hard and flag the weak joints myself so the Challenger cannot claim I hid them.

#### 0. What the number has to be, and the honest provenance

τ = T_c/√σ_dark with T_c = 179 keV and √σ_dark = m_e = 510.999 keV:

```
τ = 179 / 510.999 = 0.3503   ✓ (verified)
```

**Honest provenance concession up front (I state it before the Challenger does).** The *specific* value 179 keV is not independently sourced in the corpus. The registry number 0.34506 = 2.25 meV / [(9/2)α⁴m_e] is the observed dark-energy density read *backwards* (PRTOE_DERIVATION_HUNT.md §2), and 0.3503 is that rounded-to-0.35 × m_e re-divided. So I am **not** claiming "the corpus derived 179 keV from first principles." I am defending the narrower, honest, and actually-posed claim:

> **Given a dark SU(2), N_f = 3 confining sector at √σ_dark = m_e, is T_c/√σ ≈ 0.35 a value that sector would plausibly produce?**

That is the physics question. Provenance of the target is a separate fight (I concede the target was fitted); *plausibility of the sector delivering it* is mine to win, and I think I do.

Why plausibility is the whole ballgame: τ scales ρ_Λ¼ **linearly** (verified):

```
ρ_Λ¼ = (9/2)·α⁴·τ·m_e ;  prefactor (9/2)α⁴m_e = 6.5207 meV
  τ = 0.3503 → ρ_Λ¼ = 2.284 meV   (obs 2.25, +1.5%)
  τ = 0.345  → ρ_Λ¼ = 2.250 meV   (the observation, 0.0%)
  τ = 0.30   → ρ_Λ¼ = 1.956 meV   (−13%)
  τ = 0.37   → ρ_Λ¼ = 2.413 meV   (+7%)
```

So the flagship rides on τ to first order. A sector estimate good to ±10% in τ predicts ρ_Λ¼ to ±10%. I will argue the estimate is good to roughly that, and that the *central* value sits right on 0.35.

#### 1. The two-anchor bracket: pure glue above, chiral limit below

Every QCD-like T_c/√σ lives inside a bracket set by two computable endpoints:

- **Pure-glue (heavy/quenched) endpoint — upper bound.** Lattice pure-gauge deconfinement:
  - SU(3): T_c/√σ ≈ **0.63**
  - SU(2): T_c/√σ ≈ **0.69–0.71**  (fewer colours → higher ratio; ~11% above SU(3))
- **Chiral (massless-quark) endpoint — lower bound.** Adding light dynamical quarks restores chiral symmetry at a *lower* T_c/√σ. In continuum SU(3), N_f = 2+1 physical QCD sits at **T_c/√σ ≈ 0.34–0.35** (T_c ≈ 155 MeV, √σ ≈ 440 MeV), and the SU(3) N_f=3 chiral-limit value drops to ≈ **0.30**.

**The target 0.3503 sits inside the SU(2) bracket [~0.30, ~0.70].** That alone is necessary-but-weak (the bracket is wide). The real question is *where inside* the bracket the quark content pulls it. That is Section 2.

#### 2. The load-bearing argument: N_f/N_c = 1.5 buys a stronger reduction, and I can size it

The whole defense rests on one physical claim: **light quarks pull T_c/√σ down, and SU(2) N_f=3 pulls harder than SU(3) N_f=3 because each quark is more influential per colour.** Two independent sizings, both supporting ~0.35.

**(a) The influence ratio N_f/N_c.**
```
SU(3), N_f=3:  N_f/N_c = 3/3 = 1.0
SU(2), N_f=3:  N_f/N_c = 3/2 = 1.5
```
Quarks screen the confining glue and drive chiral restoration; their leverage on the transition scales with how many flavours ride on each colour. SU(2) N_f=3 carries 1.5× the per-colour flavour load of SU(3) N_f=3. Direction is unambiguous: **more reduction**.

**(b) Thermodynamic degrees-of-freedom fraction — a *quantitative* sizing.**
The transition is driven by the fermionic pressure fighting the gluonic. Count relativistic dof near T_c (7/8 fermion factor; quark = 7/8·4·N_f·N_c for spin×(particle+antiparticle)×flavour×colour; gluon = 2(N_c²−1)):
```
SU(3) N_f=3:  gluon dof = 16,  quark dof = 31.5,  fermion fraction = 0.663
SU(2) N_f=3:  gluon dof =  6,  quark dof = 21.0,  fermion fraction = 0.778
fermion-fraction ratio SU(2)/SU(3) = 1.173
```
The fermionic sector is a *larger* share of the plasma in SU(2) N_f=3 (78%) than in SU(3) N_f=3 (66%). If the quark-driven fractional reduction of T_c/√σ scales with this fermion fraction, then from the measured SU(3) reduction:

```
SU(3): 0.63 (glue) → 0.345 (N_f=3) = 45.2% reduction   [verified]
scale by 1.173:  45.2% × 1.173 = 53.0% reduction
SU(2): 0.70 (glue) × (1 − 0.530) = 0.329
```

**And the required reduction is:**
```
SU(2) glue 0.69 → 0.3503:  49.2% reduction
SU(2) glue 0.70 → 0.3503:  50.0% reduction
SU(2) glue 0.71 → 0.3503:  50.7% reduction
```

**Verdict on the core argument.** The heuristic degrees-of-freedom scaling *overshoots* the target — it predicts ~53% reduction (τ ≈ 0.329) where only ~50% (τ ≈ 0.3503) is required. In other words, the physical mechanism that has to deliver the number is **not straining to reach it; if anything it has room to spare.** The target sits between the pure-glue baseline and the naive-scaled chiral pull, exactly where a *slightly-non-chiral* (physical-mass) transition should land — see Section 3. This is the strongest single thing I can say: the number the model needs is *bracketed from below by the mechanism's own estimate*, not perched above it.

#### 3. Crossover, not first-order: the transition type is compatible and it hands us m_q for free

A live worry (PRTOE_DERIVATION_HUNT.md §3): N_f = 3 degenerate massless quarks give a **first-order** chiral transition (the Columbia-plot corner) at any N_c — and a first-order jump is incompatible with the model's coded "order-parameter birth ramp." **Resolved, and in the defense's favour:** "light" means light *relative to Λ*, not massless. Placing τ against the SU(3) chiral anchors:
```
chiral limit:  T_c/√σ ≈ 0.300 at m_π/√σ = 0
physical:      T_c/√σ ≈ 0.352 at m_π/√σ ≈ 0.318
```
τ = 0.3503 interpolates to **m_π,dark/√σ ≈ 0.274** (near the physical point, well away from the chiral limit). The Columbia first-order corner ends at m_π/√σ ≈ 0.06–0.16. So the dark sector sits **1.7–4.6× above the corner → the transition is a CROSSOVER**, compatible with a growing (not jumping) order parameter.

This is not just damage control — it *tightens* the picture and yields a number the model never had:
```
m_π,dark ≈ 0.274 × √σ_dark = 0.274 × 511 keV ≈ 140 keV
GMOR (m_π² f_π² = 2 m_q ⟨q̄q⟩) ⟹ m_q,dark ≈ 38 keV
```
A sector that has to sit at m_π/√σ ≈ 0.27 to be a crossover is *exactly* a sector whose T_c/√σ is pulled well below pure glue but not all the way to the chiral 0.30 — i.e. it is *self-consistently* the ~0.35 regime, not an accident. The crossover requirement and the T_c/√σ value point at the **same** small quark mass.

#### 4. SU(2) is a real, computable theory, and its special features cut for us

SU(2) with fundamental fermions is not exotic — it is "two-color QCD," one of the most-studied lattice theories (chosen historically because its fermion determinant is real ⇒ no sign problem at finite density). Two structural facts:

- **Pseudo-real fundamental → bosonic diquark baryons → BEC side of the BCS–BEC crossover.** The two-color baryon is a scalar diquark (a boson). This is the canonical diquark-BEC realization the flagship's superfluid picture needs (PRTOE_cosmological_constant.md §4c: s-wave/scalar channel). The dark-energy condensate wanting an *unsuppressed s-wave* channel and the gauge group *delivering bosonic scalar baryons* is a genuine consilience, independent of the T_c number.
- **Enlarged chiral symmetry SU(2N_f) → Sp(2N_f).** For N_f=3: SU(6) → Sp(6). This is a *computed* group-theory fact of pseudo-real fermions, not a fit. (It does raise the Goldstone count — see my concession list — but it confirms we are talking about a well-defined, studied theory, not a placeholder.)

#### 5. Consilience: SU(2) N_f=3 is not reverse-engineered from τ

The gauge group is fixed by an *independent* condition — Pauli finiteness applied to the dark sector (PRTOE_DERIVATION_HUNT.md §6):
```
str[k₁]_dark = 2·N_f·N_c − 4(N_c²−1) = 0  ⟹  N_f = 2(N_c²−1)/N_c
  N_c=2 → N_f = 3   (integer! quarks +12, gluons −12)
  N_c=3 → N_f = 5.33 (non-integer)
  N_c=4 → N_f = 7.5  (non-integer)
```
N_c = 2 is the **unique** colour group giving an integer flavour count, and it gives N_f = 3 — the same finiteness logic that fixes three SM generations. So SU(2) N_f=3 was *not* chosen to make τ come out; it was selected by a separate integer condition and then *happens* to be the group whose N_f/N_c = 1.5 gives the extra reduction the flagship needs. That is the difference between a fit and a prediction, and it is real here.

#### 6. My honest concession list (stated by the Defender, not extracted by the Challenger)

I will not pretend these away — a defense that hides them is worthless:

1. **No published lattice number.** There is no computed T_c/√σ for SU(2) with N_f=3 light flavours. Everything above is analytic estimate. This is the single biggest weakness and I own it.
2. **The required reduction (~50%) is aggressive.** It is *larger* than the ~45% that SU(3) unquenching delivers. My dof-scaling argument covers it (~53%), but that scaling is a heuristic, not a first-principles calculation, and the pure-glue SU(2) baseline (0.69–0.71) is itself a ~3% band.
3. **The target was fitted, not sourced.** 179 keV / 0.3503 traces to the observation inverted-and-rounded. I am defending plausibility of the sector, not provenance of the target.
4. **Linear leverage.** τ sets ρ_Λ¼ at first order, so the flagship's entire +1.5% "prediction" is really "ρ_Λ¼ predicted to ±(the τ uncertainty)." Honestly that is ±4–7%, not ±1.5%, until the lattice number lands.
5. **The Sp(6) enlargement raises the Goldstone/ΔN_eff count** (14 vs 8), which is a *separate* problem for the sector (P-2026-048's thermalisation kill) — but it does not touch the T_c/√σ value under debate here, so I set it aside as out-of-scope for *this* question while noting it exists.

#### 7. Defender's bottom line for Round 1

τ ≈ 0.3503 is **plausible and defensible, not proven.** The value sits inside the SU(2) bracket [~0.30, ~0.70]; the mechanism that must pull it there (N_f/N_c = 1.5, fermion fraction 0.78) is *quantitatively sufficient* — the naive scaling actually overshoots to ~0.33, leaving the target comfortably reachable; the transition type is a crossover (compatible with the model, and it pins m_π,dark ≈ 140 keV, m_q,dark ≈ 38 keV self-consistently); and the gauge group was fixed by an independent integer condition, not reverse-engineered. The honest grade: **ρ_Λ¼ is predicted to roughly ±5–7% and the observation sits dead centre; the "±1.5%" becomes real only when someone computes the lattice number.** That is a strong claim, and I can defend it. Over to the Challenger.

---

### CHALLENGER — Round 1

**My thesis:** Strip the one unsupported step out of the Defender's case and the honest analytic estimate for SU(2) N_f=3 lands at **τ ≈ 0.38–0.39, not 0.35** — which *breaks* the flagship (ρ_Λ¼ too high by ~+10–15%). The Defender's rescue is a *single* heuristic (fermion-fraction rescaling of the fractional T_c reduction) that has no derivation and that, under equally-"natural" alternative choices, spits out anything from τ = 0.22 to τ = 0.38. The target 0.3503 is not the center of the estimate — it is the value you land on *only if you pick the rescaling exponent that puts you there.* That is fitting a heuristic, not predicting a number.

I concede real ground where the Defender earned it (§4 below), then press the magnitude, which is the whole ballgame.

#### 1. The Defender's own honest transport gives 0.38, and 0.38 kills the flagship

The Defender's Section 2b anchors on a *measured* fact: SU(3) goes from pure-glue 0.63 to physical N_f-content ≈ 0.345–0.352, a **44–45% reduction**. The clean, assumption-free way to carry that to SU(2) is to apply the *same fractional reduction* to the SU(2) pure-glue baseline (0.69–0.71). Both theories have **N_f = 3**; the most defensible null hypothesis is "same flavour count → same fractional pull." Result (verified Python):

```
SU(2) glue 0.69 × (1 − 0.452) = τ 0.378   → ρ_Λ¼ 2.466 meV   (+9.6%)
SU(2) glue 0.70 × (1 − 0.452) = τ 0.384   → ρ_Λ¼ 2.501 meV   (+11.2%)
SU(2) glue 0.71 × (1 − 0.441) = τ 0.397   → ρ_Λ¼ 2.588 meV   (+15.0%)
```

Central value **τ ≈ 0.384**, giving ρ_Λ¼ ≈ 2.50 meV — an **+11% miss**, ~7× worse than the flagship's advertised +1.5%. This is not a strawman: it uses the Defender's *own* anchors (0.63, 0.69–0.71, 44–45% reduction) with the single most conservative assumption about how the reduction transports. **The honest baseline breaks the flagship.** The Defender needs SU(2) to reduce ~5 percentage points *more* than SU(3), and everything hangs on the argument for that extra 5 pp.

#### 2. The extra 5 pp rides on ONE unfalsifiable knob — and the knob can output anything

The Defender's Section 2b gets the extra reduction by asserting the *fractional reduction of T_c/√σ scales linearly with the relativistic-dof fermion fraction* (SU(2): 0.778 vs SU(3): 0.663, ratio 1.173), so 45.2% × 1.173 = 53%. There is **no derivation** that the fractional reduction is linear in the dof fraction — the reduction of a transition temperature by dynamical quarks is a nonlinear screening effect, not a counting of relativistic species. It is a plausible *direction*, dressed as a *magnitude*.

Watch what happens when I substitute other equally-defensible scaling variables into the *same* transport (verified Python, SU(2) glue 0.70, base reduction 45.2%):

```
scaling variable                         reduction   τ       ρ_Λ¼     dev
none (reduction ∝ N_f, equal)              45.2%    0.384   2.501   +11.2%
√(fermion-frac ratio)  ×1.083              49.0%    0.357   2.330    +3.6%
fermion-frac ratio (Defender's pick) ×1.173 53.0%   0.329   2.144    −4.7%
N_f/N_c ratio (Miransky variable) ×1.5     67.8%    0.225   1.470   −34.7%
```

The estimate swings across **τ ∈ [0.22, 0.38]** — a factor that moves ρ_Λ¼ by ~45% — depending purely on which "natural" exponent you assign to the rescaling. N_f/N_c = 1.5 is at least as physically motivated as the dof fraction (it's the standard chiral-restoration / conformal-window control variable, Miransky–Yamawaki), and it gives an *absurd* τ = 0.225. That the heuristic produces absurdities means it has **no predictive resolution** at the ±5 pp level the flagship needs. And note which row lands *exactly* on the flagship: **√(fermion-fraction ratio), an exponent of ½ with no physical rationale at all.** The target is reachable, but only by selecting the fudge.

**The tell:** the Defender's *chosen* rescaling (×1.173) does not even hit the target — it predicts τ = **0.329**, i.e. ρ_Λ¼ = 2.144 meV, a **−4.7% miss on the low side.** So the Defender's own best mechanism does not "sit dead centre" on the observation as §7 claims — it undershoots by ~5%, while the conservative transport overshoots by ~11%. The observation sits in the *gap between two failing estimates*, and 0.3503 is picked from that gap. That is the opposite of a prediction landing on the number.

#### 3. There is no near-conformal physics to justify the extra pull

One could rescue the big reduction if SU(2) N_f=3 were *near-conformal* (walking coupling → strong suppression of the condensate and T_c). It is not. Asymptotic freedom for SU(2) fundamental Dirac fermions is lost at N_f < 11N_c/2 = 11; the lower edge of the conformal window sits at **N_f\* ≈ 6–8** (lattice: SU(2) N_f=6 is the near-conformal / walking candidate; N_f=2 is QCD-like). **N_f=3 is comfortably below the window → a robust, chiral-symmetry-breaking, QCD-like confiner.** A QCD-like theory should transport QCD-like — i.e. behave like the plain-fractional-reduction estimate (τ ≈ 0.38), *not* like an anomalously over-suppressed one. The physics that could push T_c/√σ far below the naive transport simply isn't operating at N_f=3.

#### 4. Where the Defender is genuinely right (conceded)

I will not pretend these away:

1. **The target is inside the bracket [~0.30, ~0.71].** True and I grant it. But the bracket spans a factor of 2.4 in τ and a factor of 2.4 in ρ_Λ¼ — being inside it is necessary and nearly content-free. The fight was always *where inside*, and "where inside" is unresolved to ±15%.
2. **The group was fixed independently (Pauli finiteness, §5).** I grant SU(2)/N_f=3 was *not* reverse-engineered from τ. That's a fair and non-trivial point. But it is **orthogonal to the value**: fixing the gauge group by an integer condition does nothing to fix the *lattice number* the group produces. 0.3503 vs 0.384 is not adjudicated by how the group was chosen.
3. **Direction of the effect is plausible.** SU(2) N_f=3 (N_f/N_c=1.5) probably reduces *at least as much* as SU(3) N_f=3. I concede the sign. I contest only the magnitude — and the magnitude is 100% of the question.
4. **The crossover classification is internally consistent — conditionally.** *If* τ = 0.35, then m_π/√σ ≈ 0.27 and it's a crossover safely above the Columbia corner. Granted. But this is consistency, not evidence: it assumes the answer. Worse, it cuts slightly for me — a *robust* crossover (safely away from the first-order corner) wants quarks not-too-light, i.e. *less* T_c suppression, i.e. τ *higher* toward 0.38. The Defender's own §2b central estimate (τ=0.329) sits closer to the chiral corner than the value §3 wants.

#### 5. Two smaller cracks

- **√σ convention is not fixed across quark content.** Full-QCD string tension (with string-breaking) is defined differently from quenched σ; the physical SU(3) anchor is quoted anywhere from 0.345 (√σ=440) to 0.373 (√σ=420). Using 0.373 makes the SU(3) reduction only ~41%, transporting to SU(2) τ ≈ 0.41 — *worse* for the flagship. The convention slop alone is a ±0.02–0.03 band in τ, i.e. ±5–8% in ρ_Λ¼, swamping the +1.5%.
- **m_q,dark ≈ 38 keV is an output, not a prediction.** §3's GMOR back-out (m_π,dark≈140 keV ⇒ m_q≈38 keV) is *derived from assuming τ=0.35*; it cannot then be cited as independent support for τ=0.35. It's the same number wearing a second hat.

#### 6. Challenger's bottom line for Round 1

The honest, assumption-minimal analytic estimate is **τ ≈ 0.38 (range 0.36–0.41)**, which overshoots ρ_Λ¼ by ~+10% and **breaks the flagship.** To reach 0.3503 the Defender must reduce ~5 pp harder than SU(3), and the only support offered is a rescaling heuristic that (a) has no derivation, (b) under its own author's chosen exponent predicts 0.329 (a −5% *miss*, not the target), and (c) under other equally-natural exponents ranges over τ = 0.22–0.38. There is no near-conformal physics to justify the extra pull at N_f=3. **The flagship's "+1.5%" is unsupported: the true one-sigma analytic band on ρ_Λ¼ is roughly ±10–15%, and its center sits above the observation, not on it.** Over to the Referee / Defender.


---

### DEFENDER — Round 2

Strong round from the Challenger — genuinely the best attack available, and I concede several sub-points below. But the central move rests on a misclassification I can demolish cleanly: **τ ≈ 0.38 is not the "assumption-minimal central estimate." It is the no-leverage ceiling — the value you get by switching off the one effect both of us have already agreed is nonzero.** Once that is seen, the whole "+11% overshoot breaks the flagship" collapses into "the upper bound overshoots," which is trivially true of any upper bound and says nothing about the center.

#### 1. The Challenger's "equal fractional reduction" is not a null hypothesis — it is a *specific, non-neutral* assumption, and it is the least physical one

The Challenger calls "same N_f → same fractional pull" the "most defensible null hypothesis." It is neither null nor defensible. It embeds a hidden physical claim:

> **the fractional reduction of T_c/√σ by dynamical quarks is independent of N_c.**

That is false, and both of us already know it is false — it is the negation of the Challenger's own conceded point #3 ("SU(2) N_f=3 probably reduces *at least as much* as SU(3)"). Concede #3 and the "equal-fractional" transport is *excluded as a central value*, because it is the boundary case where the concession is saturated to equality. Formally:

```
Conceded: reduction_SU(2) ≥ reduction_SU(3)  (strictly ≥, "at least as much")
Equal-fractional (τ=0.384): reduction_SU(2) = reduction_SU(3)  ← the boundary
Therefore: τ ≤ 0.384 is a CEILING, and the interior (τ < 0.384) is where the physics lives.
```

So 0.384 is the Challenger's *own upper bound*, mislabelled as their center. An upper bound overshooting the target by +11% is not an argument against the target — it is the expected geometry when the target sits below the ceiling. The real question is *how far* below, and that is a question about the magnitude of Effect B, not about whether 0.38 "breaks the flagship."

#### 2. Two competing N_c effects, opposite in sign — and the physical expectation is that they roughly cancel near 0.35

Going SU(3) N_f=3 → SU(2) N_f=3 at fixed flavour content turns two knobs in *opposite* directions:

```
Effect A  pure-glue baseline:  0.63 → 0.70   = +11.1%   (pushes τ UP)
Effect B  quark leverage N_f/N_c: 1.0 → 1.5              (pushes τ DOWN, more reduction)
```

The Challenger keeps Effect A and zeroes Effect B → 0.38. But the honest estimate keeps *both*. The natural leading expectation is that they partially cancel, leaving τ_SU(2),N_f=3 close to the *physical-QCD* value τ_SU(3),N_f=2+1 ≈ 0.35 — the very reference-class the Challenger's §3 insists is correct ("N_f=3 is robustly QCD-like → transport QCD-like"). I agree it is QCD-like; the QCD-like anchor is 0.35, and the two N_c corrections push against each other around it. **"Transport QCD-like" is an argument for ~0.35, not for 0.38 — 0.38 is what you get only if you apply Effect A's +11% and refuse Effect B its offset.**

#### 3. The required leverage is modest, and the two physically-correct laws BRACKET the target

Quantify how much Effect B is needed. From baseline 0.70, hitting τ = 0.3503 requires (verified):

```
reduction 50.0%  vs no-leverage 45.2%   →  enhancement over SU(3) = ×1.106  (+10.6%)
```

We need the fermionic pull to be ~11% stronger in SU(2) than SU(3). Now the two *thermodynamically defensible* enhancement laws — both built on the relativistic-dof fraction that actually sets the free-energy balance at T_c — bracket it (verified):

```
√(dof-fraction ratio) ×1.083  →  reduction 49.0%  →  τ = 0.3573   (+2.0% in τ over target; ρ_Λ¼ +3.5%)
required                ×1.106  →  reduction 50.0%  →  τ = 0.3501   (the target)
   full dof-fraction ratio ×1.173  →  reduction 53.0%  →  τ = 0.3288   (−6.1% in τ; ρ_Λ¼ −4.7%)
```

**The target 0.3503 sits *between* the two most-defensible functional forms, each within ~±2–6% of it.** The Challenger's own table already shows this — their "√(fermion-fraction ratio)" row lands at τ = 0.357, +3.5% in ρ_Λ¼. They framed that as "the target is reachable only by selecting the fudge (exponent ½)." I reframe it correctly: **an estimate whose two natural functional forms bracket the answer to ±(2–6)% is a *good* estimate.** That the truth lies between "reduction ∝ dof-fraction" and "reduction ∝ √(dof-fraction)" is not fudge-selection — it is the ordinary situation where a heuristic brackets rather than pinpoints. My Round-1 §7 claim was "±5–7%, dead centre"; the honest correction from this bracket is: **center ≈ 0.343 (mean of 0.329 and 0.357), band roughly [0.33, 0.36], and 0.3503 is inside it, just above center.** I withdraw "dead centre on the observation"; I hold "inside the physically-supported band, near its upper edge."

#### 4. The τ = 0.225 "absurdity" is a strawman functional form — the control variable was misused

The Challenger's most rhetorically effective row — raw N_f/N_c = 1.5 as a multiplier → 67.8% reduction → τ = 0.225 — is a **misuse of the 't Hooft variable**, and its absurdity is manufactured, not physical:

- The relativistic-**dof fraction** is the correct driver because T_c is fixed by *free-energy / pressure balance* between phases, and pressure counts relativistic species with the 7/8 factor — a quantity that **saturates** (a quark contributes at most its dof; it cannot reduce T_c by more than its share of the plasma). Applying it as ×1.173 or ×√1.173 respects that saturation.
- The raw **N_f/N_c** ('t Hooft λ_f/λ_g) is a *per-loop coupling weight* — it tells you quark effects are "1.5× as important relative to glue," a statement about relative importance, **not** a fractional-reduction multiplier. Feeding it in as ×1.5 on an *already-measured* 45% reduction double-counts (the 45% already includes the SU(3) quark loops) and blows past saturation into the unphysical. Of course it returns nonsense — you fed a coupling weight into a slot that wants a bounded thermodynamic fraction.

So the [0.22, 0.38] "swing" the Challenger displays is not the physical uncertainty; it is the artifact of mixing a saturating variable (dof fraction, the right one) with a non-saturating coupling weight (raw N_f/N_c, the wrong one) in the same transport. **Restrict to the thermodynamically correct family and the swing is [0.33, 0.36], not [0.22, 0.38].** The heuristic has *more* resolution than the Challenger credits — once you stop feeding it the wrong observable.

#### 5. Near-conformal (Challenger §3): conceded, and it was never my claim — it *helps* me

I fully concede N_f = 3 SU(2) is far below the conformal window (edge ~6–8; N_f=6 is the walking candidate). I never invoked walking, and I do not need it. My extra pull comes from *elementary* N_f/N_c leverage — **fewer gluons (3 vs 8) for the same 3 flavours to screen**, so each flavour is more influential per colour. That is ordinary QCD-like physics, present at any N_f, not conformal-window physics. The Challenger's §3 therefore rebuts a claim I did not make. And its conclusion — "robustly QCD-like → use the QCD anchor" — points at **0.35** (physical SU(3) N_f=2+1), as §2 above showed. Being safely QCD-like is a point *for* the defense.

#### 6. The smaller cracks — conceded, with their true weight

- **√σ convention slop (§5a):** Conceded as real. But it is a *reference-class width, symmetric about the center, not a bias*. Quote the SU(3) anchor with string-breaking-corrected full-QCD σ consistently on both sides and the convention **cancels in the ratio transport** to leading order. What survives is an absolute ±0.02–0.03 band in τ — which is exactly why my Round-1 honest grade was **±5–7% on ρ_Λ¼, not ±1.5%.** So this crack *widens the error bar I already quoted*; it does not move the center toward 0.38. (Using the Challenger's high-σ 0.373 anchor shifts the SU(3) *reduction* to ~41% — but that same reference change lowers the pure-glue-to-physical gap symmetrically; it does not selectively push SU(2) up unless you also refuse Effect B, i.e. §1 again.)
- **m_q,dark ≈ 38 keV is an output, not independent support (§5b):** Conceded cleanly. The GMOR back-out assumes τ ≈ 0.35, so it is a **self-consistency check, not evidence.** I labelled it "consilience/self-consistent" in Round 1, not "independent"; the Challenger is right to hold the line hard on that distinction. Weight of that point in my case: it shows the crossover picture is *internally consistent* (m_π/√σ ≈ 0.27 is safely above the Columbia corner across my whole band 0.33–0.36), nothing more. I claim only that, not independent confirmation.
- **Crossover cuts for the Challenger (their #4):** Partly. Their claim "a robust crossover wants quarks not-too-light → τ higher toward 0.38" over-reads it. m_π/√σ ≈ 0.27 is *already* not-too-light — it sits 1.7–4.6× above the corner (0.06–0.16). Even my low-band τ = 0.329 stays above the corner. So the crossover is robust across the entire [0.33, 0.36] band; it does not exert an upward pull toward 0.38. Consistency, granted; directional evidence for 0.38, denied.

#### 7. The one place the Challenger is simply right, and where that leaves us

I concede the meta-point without reservation: **the analytic heuristic does not resolve τ to ±1.5%.** Nobody's estimate does; the "+1.5%" in the corpus is the τ-rounding, not a sourced prediction (I said this in Round-1 §0, and PRTOE_DERIVATION_HUNT.md §2 says it too). If the debate motion were "does the estimate *predict* 0.3503 to 1.5%," I would lose it.

But the motion is **"is 0.3503 plausible."** Plausible means: does it land inside the physically-supported band, computed with the correct observables and respecting what both sides concede? And the answer is yes:

```
Physically-supported band (dof-fraction family, Effect A + Effect B both on): τ ≈ [0.33, 0.36]
Challenger's 0.38: the Effect-B-OFF ceiling, excluded as a center by their own conceded direction
Target 0.3503: inside [0.33, 0.36], just above its center (~0.343)
```

#### 8. Defender's bottom line for Round 2

τ = 0.3503 is **plausible and inside the physically-supported band [0.33, 0.36]**, sitting between the two thermodynamically-defensible dof-fraction transport laws (0.329 and 0.357) to within ±(2–6)%. The Challenger's τ ≈ 0.38 is not a competing central estimate — it is the **no-leverage ceiling**, obtained by zeroing the N_f/N_c leverage that their own concession #3 grants is nonzero and reducing; and their τ = 0.225 "absurdity" is manufactured by feeding a non-saturating coupling weight into a slot that demands a bounded thermodynamic fraction. **Honest grade, revised: ρ_Λ¼ is predicted to ≈ ±5–7% with the observation inside the band and near its center; the "+1.5%" is rounding, not prediction; but "0.35 is where a dark SU(2) N_f=3 confiner plausibly lands" survives the attack.** I withdraw "dead centre"; I hold "in-band, defensible, not proven." Over to the Referee.

---

### CHALLENGER — Round 2

The Defender's Round 2 is good, and it moved the number. I will not pretend it didn't. I **concede their strongest point outright**, then show that the concession does *not* buy them 0.35 — it buys them an *interval* whose upper half still breaks the flagship, and whose survival depends on an unproven functional form doing specific work. The debate has genuinely converged; I mark exactly where.

#### 1. Conceded, cleanly: my 0.384 is a ceiling, not a center

The Defender is right. My "equal fractional reduction" transport sets reduction_SU(2) = reduction_SU(3), which is the *boundary* of my own conceded point #3 (reduction_SU(2) ≥ reduction_SU(3), strict). If the inequality is strict — and I granted it is — then **τ_SU(2),N_f=3 < 0.384 strictly.** So 0.384 is my *upper bound*, and I was wrong in Round 1 to present it as "the central value." I withdraw "τ ≈ 0.38 is the honest central estimate." The correct statement is: **0.384 is the Effect-B-off ceiling.** Good catch; it stands.

I also concede §4 in substance: raw N_f/N_c = 1.5 fed as a *multiplier onto an already-measured reduction* double-counts the loops already inside the SU(3) 45%, and the τ = 0.225 row is therefore not a physical estimate. I withdraw it as evidence of a wide swing. The saturating (dof-fraction) family is the right observable class for a fractional T_c reduction. That narrows the honest instrument to the dof-family, as the Defender says.

**So we agree on the instrument. Now watch what the instrument actually says.**

#### 2. The concession delivers an interval, and the flagship lives in its risky upper half

Ceiling 0.384 (Effect-B off) and floor ~0.329 (full dof-ratio) bracket the admissible τ. Parametrise by the Effect-B *enhancement* over SU(3) (how much stronger the SU(2) fractional reduction is). Verified map:

```
enh ×1.000  τ 0.3836  ρ_Λ¼ 2.501  +11.2%   ← ceiling (Effect-B off)
enh ×1.050  τ 0.3678  ρ_Λ¼ 2.398   +6.6%
enh ×1.069  τ 0.3618  ρ_Λ¼ 2.359   +4.8%
enh ×1.083  τ 0.3573  ρ_Λ¼ 2.330   +3.6%   ← √-law
enh ×1.106  τ 0.3501  ρ_Λ¼ 2.283   +1.5%   ← flagship target
enh ×1.128  τ 0.3431  ρ_Λ¼ 2.237   −0.6%   ← dof-family center
enh ×1.173  τ 0.3289  ρ_Λ¼ 2.144   −4.7%   ← full dof-ratio
```

Two things the Defender's framing understates:

**(a) The flagship sits ABOVE the dof-family center, not at it.** The Defender's own band center is τ ≈ 0.343 (enh ×1.128), which gives ρ_Λ¼ = 2.237 meV — i.e. the honest central estimate lands ~−0.6% *below* the observation and ~2% below the flagship's own 0.3503. To *reach* 0.3503 you must sit at enh ×1.106, on the **weaker-reduction (√-law) side** of the dof-family. So the flagship is not "where the mechanism centrally points"; it is where the mechanism points *if Effect B comes in on the mild end.* That's a legitimate part of the band — but it is the model betting on the weaker of its own two laws.

**(b) The error is ASYMMETRIC, and the asymmetry points at the flagship's throat.** Effect A (the +11–13% pure-glue N_c bump, 0.63→0.71) is **lattice-measured and robust**. Effect B (the reduction enhancement) is a **heuristic with an unproven functional form**. When you difference a solid up-push against a guessed down-push, the result inherits the guess's uncertainty — and it inherits it *toward the solid leg*, i.e. toward higher τ. Concretely: ρ_Λ¼ stays within ±5% of observation only if the enhancement is **≥ ×1.067** (verified). The dof-family (×1.083, ×1.173) clears that bar — but only because we *chose* the dof-family. Any milder scaling of the reduction (enhancement ×1.00–1.07, half the a-priori-plausible range) throws ρ_Λ¼ to +5%…+11% and **breaks the flagship.** The flagship's survival is precisely the claim "Effect B delivers at least a ~7–11% enhancement," and nothing computes that it must.

#### 3. The "two N_c effects cancel at 0.35" story is a plausibility, not a result

The Defender's cleanest intuition is that Effect A (+11%, up) and Effect B (down) "roughly cancel," landing at the SU(3) physical anchor 0.35. But the up-push is a *measured, non-vanishing* N_c effect:

```
SU(2)glue / SU(3)glue = 0.71 / 0.63 = 1.13   (a real +13% N_c effect, it does NOT cancel in pure glue)
```

Large-N_c heuristics do *not* rescue "cancellation to 0.35": if T_c/√σ were N_c-independent we would see 0.63 ≈ 0.71 in pure glue, and we do not — there is a hard +13% N_c dependence sitting right there in the measured numbers. So the claim that adding quarks makes the *net* N_c dependence vanish (Effect B exactly eating Effect A down to the SU(3) value) is an assumption about a cancellation between one measured quantity and one guessed one. It might cancel to 0.35; it might under-cancel to 0.36–0.37 (flagship breaks) or over-cancel to 0.33 (ρ_Λ low). Unconstrained, and the Defender agrees no lattice pins it.

#### 4. Where the debate has landed (my honest read)

I am not going to manufacture a disagreement that the numbers no longer support. Converged facts:

- **0.3503 is inside the physically-supported band** [~0.33, ~0.38]. My Round-1 "the honest estimate is 0.38 and it breaks the flagship" is **withdrawn** — 0.38 is the ceiling, and the target is genuinely inside the instrument's range. The Defender won that exchange.
- **But 0.3503 is not privileged.** It sits above the dof-family center (~0.343), on the mild-enhancement edge; neighbouring values 0.355–0.37 are equally defensible and shift ρ_Λ¼ by +2% to +6%.
- **The flagship's "+1.5%" is not a prediction** (Defender concedes: it's τ-rounding). The honest one-sigma on ρ_Λ¼ is ±5–7% *at best*, widened by √σ convention slop, and the central estimate does not privilege the observation over a several-percent-high alternative.
- **The residual risk is one-sided.** Because Effect A is measured and Effect B is guessed, the fat tail runs toward *higher* τ (0.36–0.38), where the flagship breaks. The flagship is a bet that the reduction-enhancement is ≥ ~×1.07; the dof-family makes that bet look reasonable, but the bet is not won until a lattice number lands.

So: **plausible — conceded. Predicted or privileged — denied.** The motion "is 0.3503 plausible" gets a qualified *yes*; the flagship's *precision* gets a firm *no*, and there remains a real (order tens-of-percent) probability mass on τ ≥ 0.36 that would move ρ_Λ¼ by ≥5% and undercut the flagship's headline agreement. Over to the Referee.


---

### DEFENDER — Round 3

The debate has converged, and the Challenger's Round 2 is honest work — it conceded the ceiling and the double-count, then sharpened to three real points that I will not wave away. I concede two of the three outright, contest the third's *weight* (not its structure), and then consolidate.

#### (a) "0.3503 sits above the dof-family center (~0.343), on the mild-enhancement edge" — CONCEDED

True. The target needs enhancement ×1.106, and the arithmetic center of my two dof laws is ×1.128 → τ = 0.343 (verified). So 0.3503 sits **+2.1% above the dof-family center in τ**, on the √-law (weaker-reduction) side. I accept the characterization: the flagship is the model betting on the *milder* end of its own instrument, not the center. I will not claim otherwise. (I note only that "+2.1% above center" is a small offset, and the center itself, ×1.128 → ρ_Λ¼ = 2.237 meV, is −0.6% from the observation — so the *center* is an excellent match and the *target* is a slightly-high point near it. Neither reading rescues "±1.5% prediction," which I already ceded.)

#### (c) "Two N_c effects cancel at 0.35 is plausibility, not result" — CONCEDED

Also true, and the Challenger's diagnostic is exactly right: the pure-glue N_c effect is *measured and non-vanishing* (0.71/0.63 = 1.13, a hard +13% that does **not** cancel in pure glue), so "Effect B eats Effect A back down to the SU(3) value 0.35" is a cancellation between one measured quantity and one guessed one. It *might* cancel to 0.35, under- to 0.36–0.37, or over- to 0.33. My "roughly cancel" in Round 2 was intuition-framing, and I flagged it as "the natural leading expectation," not a derivation. I withdraw any implication that the cancellation is *forced*. It is a plausibility.

#### (b) The asymmetric-error argument — structure CONCEDED, weight CONTESTED

This is the Challenger's best surviving point and it is structurally correct: Effect A (the +11–13% pure-glue N_c bump) is **lattice-measured**; Effect B (the reduction enhancement) is a **heuristic functional form**. Differencing a solid up-push against a guessed down-push, the uncertainty in the difference is inherited almost entirely from Effect B, and because Effect B only pushes *down*, a weaker-than-expected Effect B leaves τ *high* — toward the ceiling where the flagship breaks. The fat tail is one-sided toward higher τ. **I concede all of that structure.**

Where I contest is the *weight* of the tail — how much probability mass actually sits in the flagship-breaking zone. Quantify it (verified):

```
flagship breaks at >+5% in ρ_Λ¼  ⟺  τ > 0.3623  ⟺  enhancement < ×1.067
softest thermodynamic scaling (√-dof law):  enhancement = ×1.083
DANGER ZONE = enhancement ∈ [×1.000, ×1.067]  — lies ENTIRELY BELOW the √-dof floor (×1.083)
margin: ×1.083 − ×1.067 = +0.016
```

So the tail is real but **thin in the right coordinate**: to break the flagship at the ±5% level, the Effect-B enhancement must come in *below even the softest physically-motivated dof scaling* (√ of the fermion-fraction ratio). The dof-fraction family — the instrument we now *agree* is the correct one — places the enhancement at ×1.083–1.173, and the *entire* danger zone lies below its floor. For the flagship to break, the fermionic pull would have to be **sub-dof**: weaker than the plasma's own fermionic share suggests. That is physically disfavoured (the fermion pressure that drives the reduction *is* the dof fraction), though — honestly — not impossible, because nothing proves the reduction cannot scale sub-linearly-sub-√ in the fraction.

So my honest amendment to the Challenger's point (b): **the tail toward higher τ is real and one-sided, but it requires sub-√-dof scaling to reach the flagship-breaking region, so its probability mass is modest, not "order tens of percent."** I would price P(τ ≥ 0.362, flagship breaks at +5%) as *small-but-nonzero* — the sliver below the soft dof floor — rather than the Challenger's implied ~30%. Neither of us can compute it without the lattice number; that is the irreducible residual.

---

### DEFENDER — FINAL POSITION

**The motion — "is τ = 0.3503 plausible for a dark SU(2), N_f = 3 confiner?" — I have defended, and I hold it: YES, plausible and defensible, not proven.** Here is the consolidated honest ledger, conceding everything the debate forced and keeping only what survived.

**What I won (the Challenger conceded these):**
1. **0.3503 is inside the physically-supported band.** The Challenger withdrew "the honest estimate is 0.38 and it breaks the flagship" — 0.38 is the *no-leverage ceiling*, and the target is genuinely inside the instrument's range [~0.33, ~0.38].
2. **The instrument is the saturating dof-fraction family.** The raw-N_f/N_c → 0.225 "absurdity" was conceded as a loop double-count and withdrawn. Restricted to the correct thermodynamic observable, the band is [0.33, 0.36], not [0.22, 0.38].
3. **The gauge group was fixed independently** (Pauli finiteness, unique integer N_f=3 at N_c=2), not reverse-engineered from τ. Conceded by the Challenger as fair and non-trivial.
4. **Direction and transition type:** SU(2) N_f=3 reduces T_c/√σ at least as much as SU(3) (conceded), and the transition is a crossover safely above the Columbia corner (m_π,dark/√σ ≈ 0.27, i.e. 1.7–4.6× above it) across the whole band.

**What I lost / conceded (honestly):**
1. **It is not a ±1.5% prediction.** The "+1.5%" is the τ-rounding of the observation inverted (0.34506 → 0.35 → 179 keV), not a sourced number. I ceded this in Round 1 and hold it ceded.
2. **The honest one-sigma is ρ_Λ¼ ± ≈5–7%**, widened by √σ convention slop — not ±1.5%.
3. **0.3503 is not privileged/central.** It sits ~+2% above the dof-family center (~0.343), on the mild-enhancement √-law edge. The model is betting on the weaker end of its own two laws. Neighbouring τ = 0.355–0.37 are comparably defensible.
4. **The residual error is one-sided toward higher τ** (Effect A measured, Effect B guessed). The flagship's survival is a genuine *bet* that the reduction-enhancement is ≥ ~×1.067.

**The one thing that decides it:** a lattice computation of T_c/√σ for SU(2) with N_f = 3 light flavours (m_π/√σ ≈ 0.27). Nobody has it. My defense is that when it lands, the dof-fraction physics predicts it in [0.33, 0.36] with the flagship-breaking region requiring physically-disfavoured sub-√-dof scaling — so the odds favour the flagship surviving, but the bet is not won until the number exists.

**Final grade:** τ = 0.3503 is **plausible, in-band, and defensible; it is not proven, not privileged, and not a ±1.5% prediction.** "0.35 is where a dark SU(2) N_f=3 confiner plausibly lands" survives the attack intact; "the flagship predicts ρ_Λ to 1.5%" does not, and I never defended it. The honest bottom line is a **qualified yes** on plausibility with a **firm no** on precision — which, for an analytic-estimate fight over an uncomputed lattice number, is exactly as far as the physics honestly reaches.

---

### CHALLENGER — FINAL POSITION

The Defender argued honestly and the debate converged hard. I agree with most of the consolidated ledger and will not re-fight settled ground. There is exactly **one live disagreement left — the weight of the one-sided tail — and I can now resolve it with a calculation, in my favour.** Then I give my bottom-line grade.

#### What I agree with (settled, no dispute)

- **0.3503 is plausible and in-band.** I withdrew "0.38 is the estimate and it breaks the flagship"; 0.38 is the Effect-B-off ceiling. The target is genuinely inside the instrument's range. The Defender won that.
- **The instrument is the saturating dof-fraction family.** My τ=0.225 row was a loop double-count; withdrawn.
- **The group was fixed independently** (Pauli finiteness, unique integer N_f=3 at N_c=2), not reverse-engineered from τ. Fair and non-trivial.
- **Direction and crossover:** SU(2) N_f=3 reduces at least as much as SU(3); the transition is a crossover safely above the Columbia corner. Conceded.
- **Precision:** the "+1.5%" is τ-rounding, not a prediction. The Defender ceded this from Round 1 and I hold him to nothing more.

#### The one live disagreement: the tail is not thin — and the reason is the anchor, not the enhancement

The Defender's final move (Round 3, point b) is that the flagship-breaking zone (enhancement < ×1.067) lies *entirely below* the softest dof scaling (√-dof ×1.083, margin +0.016), so breaking the flagship needs "physically-disfavoured sub-√-dof physics" → thin tail, not tens of percent.

That argument has a hidden load-bearing assumption: **it fixes the SU(3) reduction at 45.2% (anchor τ₃ = 0.345).** But the anchor is not fixed — it is the physical-QCD chiral T_c/√σ, and that number carries its own convention band, which the Defender *himself conceded is real* (§6, "√σ convention slop... ±0.02–0.03 in τ"). He argued it "cancels in the ratio transport." **It does not cancel** — and here is the mechanism, verified:

```
T_c^chiral = 156.5 MeV (solid).   √σ in full QCD is convention-dependent (string breaks):
   √σ = 420 → τ₃ = 0.373 → reduction 40.9%     √σ = 465 → τ₃ = 0.337 → reduction 46.6%
   √σ = 440 (standard) → τ₃ = 0.356 → reduction 43.5%   ← standard central, NOT the Defender's 0.345
```

The reduction = 1 − τ₃/0.63 depends on τ₃, and a *higher* anchor means *less* reduction, which transports to *higher* τ₂ — the same direction as the Effect-B tail. So the anchor band **stacks with** the one-sided tail rather than cancelling it, and it lives *outside* the enhancement coordinate the Defender used to argue "thin." Two consequences:

1. **The standard central anchor is 0.356 (√σ=440), not 0.345.** The Defender's whole "dof-family center ≈ 0.343" rests on τ₃ = 0.345, which is already on the high-reduction side. Recentre on 0.356 and the honest central transport lands at **τ₂ ≈ 0.355**, i.e. ρ_Λ¼ ≈ +3% — *above* the observation, with the flagship's 0.3503 at the lower-inner edge, not the centre.

2. **The breaking probability is ~25–35%, not a sliver.** Honest Monte-Carlo using *only jointly-accepted ranges* — measured SU(2) baseline U(0.69,0.71), the **agreed** dof-family enhancement U(1.083,1.173), and the anchor convention band the Defender conceded — gives (verified, seeds fixed):

```
anchor fixed 0.345 (Defender's implicit assumption):  median τ₂ 0.343   P(flagship breaks >+5%) =  0%
anchor narrow ±2%  [0.348,0.362]:                     median τ₂ 0.355   P(breaks) = 26%
anchor conservative [0.345,0.365]:                    median τ₂ 0.355   P(breaks) = 28%
anchor moderate    [0.340,0.370]:                     median τ₂ 0.356   P(breaks) = 32%
```

The Defender's "thin tail" is an artifact of collapsing the anchor to a point. Restore even a conservative ±2% anchor band — smaller than the √σ slop he already conceded — and **~1-in-4 to 1-in-3 of the honest probability mass breaks the flagship at ≥+5%.** That vindicates my Round-2 "order tens of percent" and refutes "physically-disfavoured sub-√-dof required": you reach the breaking region with *standard* dof scaling and a *standard* anchor of 0.356.

I concede the symmetric part honestly: this same band also puts mass *below* 0.35 (ρ low). The point is not "it breaks for sure" — it is that the honest **centre sits at ~0.355 (ρ +3%), above the flagship**, and the breaking tail is a real ~30%, not a sliver. The Defender's "odds favour survival" becomes, honestly, roughly **2:1 for survival with a genuine ~1/3 breaking risk** — a real bet with real downside, decided only by the missing lattice number.

#### Bottom-line grade

**Is τ = 0.3503 honest and defensible?** Qualified **YES on plausibility, firm NO on precision, and a correction to the Defender's tail-weight.**

1. **Plausible — yes, conceded.** 0.3503 is inside the physically-supported band [~0.33, ~0.37]; it is not the 0.38 ceiling; the sector delivering ~0.35 is a legitimate reading. My Round-1 "it breaks the flagship" overreached and is withdrawn.
2. **Not privileged, not central.** The honest central transport lands at **τ ≈ 0.355** (ρ_Λ¼ ≈ +3%), *above* the observation; 0.3503 sits at the low-inner edge, and neighbouring 0.355–0.37 are equally defensible.
3. **Not a prediction.** The "+1.5%" is rounding; the honest one-sigma on ρ_Λ¼ is ±5–7%, and the *centre of that band is not the observation.*
4. **The flagship is a real bet with a ~30% downside.** Because the measured up-effects (glue baseline, non-cancelling +13% N_c bump) are firm and the down-effects (reduction enhancement, anchor) carry all the slop one-sidedly-plus-symmetrically, roughly a third of the honest posterior breaks the flagship by ≥5% when the lattice number lands.

**Net:** 0.3503 is an *honest, defensible, in-band value* — I concede the strong-form attack ("the estimate is 0.38, the flagship is dead") fails. But it is *not* the central expectation (~0.355 is), it is *not* a prediction, and the flagship carries a genuine ~1-in-3 chance of being broken at ≥5% by the uncomputed SU(2) N_f=3 lattice number. The single fact that decides it is that lattice computation; until it exists, the flagship's headline agreement is a reasonable bet, not a result — and the honest central estimate points slightly against it.

---

### REFEREE — VERDICT

The debate converged cleanly and honestly; both sides moved off their opening positions on evidence, not rhetoric. This is a neutral summary of where it landed — an assessment of the arguments, not a physics ruling on τ.

**What the two sides agreed on (settled):**
1. **0.3503 is plausible and inside the physically-supported band.** The Challenger explicitly withdrew its Round-1 strong-form claim ("the honest estimate is 0.38 and it breaks the flagship"); both now agree 0.384 is the *Effect-B-off ceiling*, not a central estimate, and that the target lies genuinely inside the instrument's range.
2. **The instrument is the saturating dof-fraction family.** The Challenger withdrew its τ = 0.225 row as a loop double-count; both agree raw N_f/N_c is a coupling weight, not a bounded fractional-reduction multiplier.
3. **The gauge group was fixed independently** (Pauli finiteness → unique integer N_f = 3 at N_c = 2), not reverse-engineered from τ.
4. **Direction and transition type:** SU(2) N_f=3 reduces T_c/√σ at least as much as SU(3); the transition is a crossover safely above the Columbia first-order corner across the whole band.
5. **The "+1.5%" is not a prediction** — it is the τ-rounding of the inverted observation. Both agree the honest one-sigma on ρ_Λ¼ is ≈ ±5–7%, and that 0.3503 is not resolved to ±1.5% by any analytic estimate.
6. **Only a lattice computation of SU(2) N_f=3 T_c/√σ decides it.** Both stated this as the single fact that closes the question.

**What stays genuinely unresolved:**
- **Where the honest center sits — and the anchor question underneath it.** The Defender transports from an SU(3) chiral anchor τ₃ = 0.345 (reduction 45.2%) → dof-family center ≈ 0.343. The Challenger's FINAL re-anchors to the standard τ₃ = 156.5/440 = 0.356 (reduction 43.5%) → center ≈ 0.355–0.357. The referee verified both arithmetics: the shift is real and load-bearing (center 0.343 vs 0.357 turns on 0.345 vs 0.356). The physics crux is whether the quenched-vs-full-QCD √σ convention *cancels in the ratio transport* (Defender's claim) or *stacks one-sidedly* because the reduction 1 − τ₃/0.63 depends directly on the full-QCD anchor while the pure-glue baselines use quenched σ (Challenger's claim). This was **not adjudicated** — and it arrived in the Challenger's FINAL POSITION, so the Defender had no turn to respond to the specific re-anchoring. It is the largest open item.
- **The weight of the one-sided tail.** Both agree the residual error is one-sided toward higher τ (Effect A measured, Effect B a guessed functional form). They disagree on its mass: the Defender prices the flagship-breaking region as thin (requires sub-√-dof scaling, below the ×1.083 floor); the Challenger's Monte-Carlo, once a ±2% anchor band is restored, prices it at ~25–35%. The two numbers differ because they differ on the anchor question above, not on the enhancement law — so this reduces to the same unresolved crux.

**Assessment of the estimate-level case for 0.3503:** As a claim of *plausibility* — "0.35 is a value a dark SU(2) N_f=3 confiner could produce" — the case is **honest and defensible**, and the Challenger conceded exactly that. As a claim of *centrality or prediction* — that the mechanism points at 0.3503 specifically — the case is **strained**, and the Defender conceded exactly that (it sits above the dof-family center, on the milder edge of its own instrument, with a real one-sided downside risk). Both columns' final positions are mutually consistent on those two verdicts; the honest residual is a single unadjudicated convention question (which anchor, and whether it cancels) that moves the center by ~+0.012 in τ and the breaking risk from "sliver" to "~1-in-3." Neither side overclaimed at the close, and neither hid its weak joints. The fight was resolved as far as an analytic estimate over an uncomputed lattice number honestly can be: a qualified yes on plausibility, a firm no on precision, decided ultimately by a number nobody has computed.


---

### DEFENDER — Addendum (anchor rebuttal)

The Challenger's FINAL landed a point I had no turn to answer, and the Referee named it the largest open crux: re-anchor the SU(3) transport at the standard τ₃ = 0.356 (T_c = 156.5 MeV, √σ = 440) instead of my 0.345, and (the claim) the honest center moves to ~0.355 with ~25–35% mass in flagship-breaking territory, because the anchor choice **stacks one-sidedly** into the SU(2) estimate. This turns on ONE decidable question: **in the ratio transport, does the √σ convention cancel or stack?** It is algebra, not opinion. Here is the algebra, and here is where honesty forces a split verdict — I win the convention question, and I concede a real centering cost that the clean algebra exposes.

#### 1. The decidable question: √σ divides out of the reduction fraction. CANCELS.

The transport is glue-anchored:
```
τ₂ = τ₂_glue · (1 − enh · r₃),   r₃ = 1 − τ₃_phys / τ₃_glue
```
Write out r₃ with the SU(3) string tension shown explicitly:
```
r₃ = 1 − (T_c^{3,phys}/√σ₃) / (T_c^{3,glue}/√σ₃) = 1 − T_c^{3,phys}/T_c^{3,glue}
```
**√σ₃ appears in the numerator AND denominator of the same ratio and divides out exactly.** The reduction fraction is intrinsically a *temperature ratio*, carrying no string tension at all. And τ₂_glue = T_c^{2,glue}/√σ_dark uses the *dark* SU(2) string tension (√σ_dark = m_e, the fixed portal), which is intrinsic to the dark theory and shares nothing with √σ₃. So the predicted τ₂ carries **no SU(3) √σ convention**. Convention-independent. **QED — it cancels.**

**Why the Challenger's "0.345 vs 0.356 stacks" looked real:** it is an artifact of forming r₃ from two τ-values that secretly carry *different* √σ conventions. Decompose the anchor gap (verified):
```
0.345 = 155.0 / 449   (T_c=155.0, √σ=449)
0.356 = 156.5 / 440   (T_c=156.5, √σ=440)
```
The gap has two parts: a **√σ change** (449→440, pure convention) and a **T_c change** (155→156.5, +1.0%, physical). In the glue-anchored transport the √σ part **cancels** (it divides out of r₃), and only the T_c part — a genuine ~1% physical uncertainty — survives. So the honest anchor uncertainty propagating into τ₂ is **~1% (the T_c ratio), not the ~3% the raw 0.345-vs-0.356 spread suggests.** The Challenger's stacking is one-sided only in the *direct-anchor* form τ₂ = τ₃ × f that omits the glue baseline; restore the baseline (which the physics requires — the same √σ must sit under both τ₃_phys and τ₃_glue) and the one-sidedness disappears. **On the decidable question, the defense holds: √σ cancels.**

#### 2. But the same clean algebra corrects MY number, and it costs me. CONCEDED.

Honesty compels the other half. My Rounds 1–3 used r₃ = 0.452 — and that value was itself the convention artifact: `1 − 0.345/0.63` mixes √σ=449 (inside 0.345) with √σ=428 (inside 0.63). The convention-clean reduction is the T_c ratio (verified):
```
r₃ = 1 − 156.5/270 = 0.420   (T_c^glue ≈ 270 MeV quenched SU(3), T_c^phys ≈ 156.5 MeV)
   surviving uncertainty (T_c^glue 265–290, T_c^phys 155–158): r₃ ∈ [0.40, 0.47], central ~0.42
```
r₃ = 0.42 is **smaller** than the 0.452 I used — i.e. SU(3) unquenching reduces T_c/√σ by ~42%, not ~45%. A smaller reduction pushes τ₂ **up**. Recomputing the band with the clean r₃ = 0.420 (verified):
```
enhancement        τ₂       ρ_Λ¼     dev
√-dof   ×1.083    0.3812   2.486   +10.5%
dof-center ×1.128 0.3680   2.399    +6.6%
full-dof ×1.173   0.3547   2.313    +2.8%
hit target 0.3503 ×1.188   —        +1.5%
```
So convention-cleanly, the honest dof-family band is **[0.355, 0.381]**, its center ≈ 0.368 (ρ_Λ¼ +6.6%, above the observation), and **the target 0.3503 sits at/just below the full-dof (strong-reduction) edge, needing enh ≈ ×1.19.** In Rounds 1–3 (inflated r₃ = 0.452) the target sat at the *mild* √-law; with the clean r₃ it sits at the *strong* full-dof end. **I concede the substance of the Challenger's Q2 concern: the convention-clean center is above the observation (~+6%), and the flagship rides the full/strong dof enhancement, not the mild one.**

#### 3. The precise split verdict

- **Mechanism (the decidable crux): the Challenger is wrong.** √σ does **not** stack one-sidedly; it cancels exactly in the glue-anchored reduction fraction. The surviving anchor uncertainty is the **two-sided** T_c ratio (r₃ = 0.42 ± ~0.03), not a one-sided √σ fat tail. There is no convention-driven asymmetry toward high τ.
- **Conclusion (centering): the Challenger is substantially right, for a different reason.** Doing the algebra cleanly moves the honest center up to ρ_Λ¼ ≈ +6% (not my earlier ~0%), because the correct reduction is 42% not 45%. The flagship needs the full-dof enhancement (×1.17–1.19) — the *stronger* of the two dof laws, and the more thermodynamically principled one (reduction linear in relativistic-dof fraction, i.e. in pressure), but still the edge, not the center, of the band.
- **Net effect on my FINAL POSITION:** unchanged in kind, worse in degree. τ = 0.3503 remains **in-band** — it is exactly the full-dof-law prediction (0.355, +2.8%) to within the T_c-ratio uncertainty — but I withdraw any suggestion it sits near the band *center*. The convention-clean center is ~0.365–0.368 (+6%), so the flagship's headline agreement requires the reduction to come in on the strong side, and a meaningful fraction of the honest r₃ × enh uncertainty does land at ρ_Λ¼ ≥ +5%. The one-sidedness of that tail, however, is **not** a √σ effect (that cancels) — it is the ordinary spread of an uncomputed T_c ratio times an uncomputed enhancement.

**Bottom line of the addendum:** the convention question resolves for the defense (√σ cancels; the anchor "stacking" is an artifact of an incomplete transport), but the honest recomputation it forces moves my own center up ~6% and puts the flagship on the strong-reduction edge of the dof band. τ = 0.3503 is still plausible and in-band — now specifically as the full-dof-law value — but it is *not* central, and the true residual risk toward higher τ is real (just not convention-driven). Truth over side: I hold the algebra I got right and concede the centering the algebra corrects. Over to the Referee for the crux assessment.

---

### REFEREE — note (after Defender Addendum)

Neutral flag before the Challenger's right of reply. I verified every number in the addendum: r₃ = 1 − 156.5/270 = 0.4204; clean band τ₂ ∈ [0.355, 0.381], center ≈ 0.368 (ρ_Λ¼ ≈ +6.7%), target 0.3503 needs enh ≈ ×1.188; and the self-diagnosis checks out — 0.63 carries an implied √σ ≈ 429 MeV while 0.345 carries √σ ≈ 449 MeV, so the old r₃ = 0.452 did mix two conventions. The internal arithmetic is sound.

One thing the two sides should not talk past: the addendum's step from "√σ cancels" to r₃ = 1 − T_c^phys/T_c^glue is exact algebra **only under the condition that the same √σ sits under both τ_phys and τ_glue.** The clean transport achieves that not by asserting the lattice 0.63 and 0.345 share a √σ (they demonstrably do not, per the 429 vs 449 split above) but by *replacing* the mixed ratio with a pure temperature ratio (156.5/270). Whether that pure-T_c ratio is the right thing to transport rests on a **physical** premise, not on algebra: that the dark portal fixes a single √σ_dark = m_e common to both the glue baseline and the full dark theory, so that only T_c moves. That premise is the new load-bearing claim, and the Challenger has not had a turn on it. (A related open sub-point the Challenger may test: T_c^glue = 270 is a quenched *deconfinement* temperature while T_c^phys = 156.5 is a full-QCD *chiral* crossover — whether those two transitions define a clean ratio is a physics question, not settled by the algebra.) Challenger: your reply, then the token back to me.

---

### CHALLENGER — Reply to Addendum (the anchor crux)

The Defender's addendum is the best turn in this debate: it splits a question I had fused. I owe it a split answer. **On the mechanism, I concede — √σ largely cancels and my "one-sided √σ fat tail" was overstated. On the exactness of that cancellation I hold a residual. And on the centering, I accept the Defender's own clean recomputation, which lands my case harder than I had argued.** Truth over side, same as the Defender.

#### 1. Mechanism: conceded. √σ cancels to leading order; "one-sided fat tail" withdrawn

The algebra is right. In the glue-anchored transport the reduction is a *temperature ratio*:
```
r₃ = 1 − (T_c^phys/√σ₃)/(T_c^glue/√σ₃) = 1 − T_c^phys/T_c^glue
```
and a single common √σ₃ divides out. My Round-2/FINAL framing — that choosing anchor 0.356 vs 0.345 "stacks one-sidedly" into a √σ fat tail — was, to the extent quenched and full string tensions coincide, an artifact of forming r₃ from two τ-values carrying *different hidden* √σ (429 vs 449). Decomposed, most of that gap is convention (√σ 449→440) which cancels, leaving only the ~1% T_c change (155→156.5) which is physical and two-sided. **I withdraw "one-sided √σ fat tail."** The residual high-τ risk is a *two-sided* T_c-ratio spread, not a √σ asymmetry. The Defender won the decidable question.

#### 2. Exactness: the cancellation is a physical premise, ~2.6% imperfect, and it re-enters on the SU(2) side

But "√σ cancels" is exact **only if the same √σ sits under both T_c^phys and T_c^glue** — and the lattice says it does *not*, by a real physical margin, not a convention one (verified):
```
0.63 (glue) carries implied √σ ≈ 429 MeV   (270/0.63)
0.356 (phys) carries implied √σ ≈ 440 MeV  (156.5/0.356)
```
The ~2.6% gap between quenched and full-QCD string tension is **sea-quark screening of the confining force** — the string even *breaks* in full QCD — so σ genuinely changes on unquenching. The Defender's "pure T_c ratio" achieves exact cancellation only by *replacing* the mixed lattice ratio with 156.5/270, i.e. by *assuming* √σ_g = √σ_f. That is a physical premise (as the Referee flagged), not algebra.

And the premise re-enters on the SU(2) side, which the addendum did not close: the baseline τ₂_glue = 0.70 is measured with the **quenched SU(2)** string tension, whereas the target τ₂ is defined against **√σ_dark = m_e**, the *full* dark theory's tension. So the transport silently sets √σ_g^{SU2} = √σ_f^{SU2} = m_e. If those differ by the same ~2–3% the SU(3) lattice shows, there is a dropped factor (√σ_g/√σ_f)^{SU2} in the SU(2) transport (verified sensitivity):
```
(√σ_g/√σ_f)^SU2 = 0.97 → center τ 0.357 (+3.6%)
              = 1.00 → center τ 0.368 (+6.8%)
              = 1.03 → center τ 0.379 (+10.0%)
```
This residual is small (~±3%) and **two-sided** — so I am *not* resurrecting the fat tail. I concede its magnitude is modest. I contest only "cancels exactly / pure convention": the fixed-portal premise (√σ common to quenched glue and full dark theory) is the new load-bearing assumption, and it carries a real ~2–3% two-sided uncertainty of its own.

#### 3. Transition-type (Referee's sub-point): a genuine extra crack, neither side's favour

The clean ratio 156.5/270 compares a **full-QCD chiral crossover** (156.5) to a **quenched deconfinement temperature** (270). Pure glue has *no* chiral transition at all — so a *chiral* τ has no well-defined pure-glue baseline; the transport is implicitly gluing a chiral scale onto a deconfinement scale. In QCD the two transitions sit close, but "close" is not "equal," and the identification is an assumption. This widens r₃ beyond the ±0.03 T_c-ratio band the Defender quoted, in both directions. It does not favour me — it favours *nobody*, and it is exactly the kind of ambiguity that only the actual SU(2) N_f=3 lattice number resolves.

#### 4. Centering: I accept the Defender's clean recomputation — and it lands my case harder than I argued

Here is where the addendum's honesty costs the flagship. The convention-clean reduction is r₃ = 1 − 156.5/270 = **0.420**, not 0.452. Smaller reduction → higher τ₂. Under the clean algebra the *entire* dof-family band sits **above** the observation (verified):
```
enh ×1.083 (√-dof)   τ 0.382  ρ +10.6%
enh ×1.128 (center)  τ 0.368  ρ  +6.8%
enh ×1.173 (full-dof)τ 0.355  ρ  +2.9%   ← the LEAST overshoot the instrument allows
hit target 0.3503    needs enh ×1.188    ← BEYOND the full-dof ceiling
```
So under the Defender's *own* corrected numbers, **every point of the agreed dof instrument predicts ρ_Λ¼ between +2.9% and +10.6% — the flagship's +1.5% lies *below the whole band*,** and reaching 0.3503 requires enhancement *stronger* than the most aggressive thermodynamic law (super-full-dof). Across Rounds 1–3 the target migrated from the *mild √-law edge* → to the *strong full-dof edge* → to *just beyond it*, every step in the same direction: the honest estimate wants **more** reduction than the flagship, i.e. the flagship value is on the low-τ (high-ρ-suppression) side of where the mechanism points.

Honest MC under the clean, two-sided algebra (base U(0.69,0.71), r₃ U(0.40,0.47), enh U(1.083,1.173) — all jointly-accepted ranges) (verified):
```
median τ₂ = 0.357  (ρ_Λ¼ +3.4%)   16–84%: 0.337–0.376
P(ρ_Λ¼ > observation)     = 71%
P(flagship breaks, >+5%)  = 40%
P(within ±5%)             = 54%
```
The breaking probability is *higher* than my earlier ~30%, now for the reason the Defender's algebra exposed (r₃ = 0.42 not 0.45), not the reason I originally gave (√σ). The mechanism critique flips to the Defender; the centering verdict flips harder to me.

#### 5. Updated bottom line (this supersedes my FINAL POSITION on the two split points)

- **√σ cancellation: Defender wins.** I withdraw the one-sided √σ fat tail. What survives is a two-sided T_c-ratio spread plus a ~2–3% fixed-portal (quenched-vs-full tension) residual and a transition-type ambiguity — all modest, none one-sided.
- **Centering: strengthened for the challenge, on the Defender's own arithmetic.** The convention-clean honest center is τ ≈ 0.357–0.368 (ρ_Λ¼ **+3.4% to +6.8%**), *above* the observation; P(ρ high) ≈ 71%; the flagship's 0.3503 sits *below the entire dof band* and needs super-full-dof enhancement to be hit.
- **Plausibility: still conceded.** 0.3503 remains inside the *total* band once the two-sided T_c-ratio uncertainty is included (it is reachable at the high-reduction / low-τ corner). It is not excluded. But it is decidedly **not central** — the central estimate now points ~+3–7% high, more firmly than in my FINAL POSITION.

**Net:** the flagship is a bet on the *strong-reduction, low-τ tail* of an honest distribution whose center sits several percent above the observation, with ~40% of the mass breaking it at ≥5% and ~70% of the mass on the high side. Plausible — yes. Central, predicted, or favoured by the mechanism — no; if anything the corrected algebra points modestly against it. The deciding fact is unchanged and unchallenged by either side: nobody has computed SU(2) N_f=3 T_c/√σ. Over to the Referee.

---

### REFEREE — VERDICT (updated after the anchor crux)

This supersedes the split-open item in my first verdict. The one crux I had left unadjudicated — does the SU(3) √σ convention cancel or stack — was resolved cleanly by the addendum exchange, and it split. I verified all of it independently.

**On the mechanism — resolved for the Defender.** In the glue-anchored transport the reduction is a temperature ratio, r₃ = 1 − (T_c^phys/√σ)/(T_c^glue/√σ) = 1 − T_c^phys/T_c^glue, and a common √σ divides out exactly. The Challenger withdrew its "one-sided √σ fat tail"; both now agree the surviving anchor uncertainty is a *two-sided* T_c-ratio spread, not a convention-driven asymmetry. The Defender won the decidable question it posed.

**On the exactness of that cancellation — a small, two-sided residual both sides accept.** The clean cancellation holds only under the physical premise that one √σ sits under both endpoints — false at the ~2.6% level on the lattice (quenched vs full string tension is real sea-quark screening, the string even breaks), and the premise re-enters untested on the SU(2) side (baseline 0.70 uses quenched SU(2) tension while the target is defined against √σ_dark = m_e, the full dark tension). Both agree this is ~±2–3% and two-sided, not a resurrected tail. A related transition-type ambiguity (the clean ratio compares a full-QCD *chiral* crossover at 156.5 to a quenched *deconfinement* temperature at 270; pure glue has no chiral transition) widens r₃ both ways and favours neither side.

**On centering — moved further against the flagship, on the Defender's own corrected arithmetic.** The same clean algebra that won the Defender the mechanism also corrected its own reduction from r₃ = 0.452 (convention-mixed) to r₃ = 0.420 (convention-clean, verified 1 − 156.5/270 = 0.4204). Smaller reduction pushes τ₂ up, and the Defender conceded this in its addendum. The consequence, which the Challenger then verified and I reproduced: under the clean r₃ the *entire* agreed dof-family band maps to τ₂ ∈ [0.355, 0.382] → ρ_Λ¼ ∈ [+2.9%, +10.6%], so the flagship's +1.5% lies **below the whole instrument band**, and hitting τ = 0.3503 requires enhancement ×1.188 — *beyond* even the strongest (full-dof) thermodynamic law. A clean two-sided Monte-Carlo over the jointly-accepted ranges (base U(0.69,0.71), r₃ U(0.40,0.47), enh U(1.083,1.173)) gives, verified independently: median τ₂ = 0.357 (ρ_Λ¼ +3.4%), 16–84% = 0.337–0.376, P(ρ above observation) = 71%, P(flagship breaks at >+5%) = 40%.

**Updated assessment of the estimate-level case for 0.3503:**
- *Plausibility — unchanged, conceded.* 0.3503 stays inside the total band once the two-sided T_c-ratio uncertainty is included; it is reachable at the high-reduction / low-τ corner and is not excluded. The strong-form attack ("the estimate is 0.38, the flagship is dead") failed and was withdrawn.
- *Centering — strengthened against the flagship, and now on the Defender's own numbers, not a contested anchor.* My first verdict priced the honest center at 0.343–0.357 with breaking risk somewhere between "sliver" and "~1-in-3." The clean recomputation resolves that spread toward the unfavourable end: center ≈ 0.357–0.368 (ρ_Λ¼ +3.4% to +6.8%), with ~40% of the honest posterior breaking the flagship at ≥5% and ~70% on the high-ρ side. The flagship value sits *below* where the mechanism centrally points and is a bet on the strong-reduction tail.
- *Notably, this convergence was reached by the two sides trading concessions in the same direction:* the Defender conceded the centering cost that its own cleaner algebra exposed, and the Challenger conceded the mechanism and dropped its original (convention-based) reason for the high-τ tail — arriving at the same place from opposite starts.

**Final:** the honest verdict is a **qualified yes on plausibility, a firm no on precision, and — after the clean algebra — a mild lean against 0.3503 being where the mechanism centrally points** (the central estimate sits ~+3–7% high in ρ_Λ¼). This is a strengthening of the "not privileged" finding, not a reversal of the "plausible" one. Nothing here is a physics ruling on τ; it is an assessment that both columns argued honestly, corrected themselves against their own interest, and converged. The single fact that would settle it is untouched: a lattice computation of SU(2) N_f=3 T_c/√σ that nobody has performed.

---

## ADDENDUM (2026-07-17): the literature hunt — what the lattice actually says

*A dedicated sweep for T_c/√σ in SU(2) with light fundamental fermions (all papers read in full).
This supersedes the debate's dof-family band as the best available anchor.*

**Headline: NO direct lattice determination of T_c/√σ for SU(2), N_f = 3 exists.** The roster's
open number cannot be closed by citation — only bracketed by inference.

**The hard numbers:**
- **SU(2) N_f=2, rooted staggered** (Braguta school, arXiv:1808.06466; review 2511.19789): measured
  √σ₀ = 476(5) MeV on-ensemble, deconfinement crossover T_d(0) = 230(10) MeV ⟹
  **T_d/√σ = 0.483(23)** at m_π = 740 MeV (heavy quarks). The only SU(2)+fermion number with σ in
  the same units.
- **SU(2) N_f=2, Wilson** (Iida–Itou–Lee, arXiv:2008.06322 vs 2405.20566): the chiral crossover is
  pinned only to **T_c/√σ ≈ 0.36–0.48** — their own two determinations disagree ~30% (admitted
  systematic).
- **SU(3) N_f-dependence** (Karsch–Laermann–Peikert, hep-lat/0012023, Table 3): 0.635 (quenched) →
  0.425(15) (N_f=2 chiral) → ~0.41(2) (N_f=3 chiral); quark-mass slope 0.039(4)·(m_PS/√σ). The
  N_f suppression **saturates** (−0.21 for the first two flavours, −0.03 for the third). The famous
  "0.63 → 0.35" QCD drop conflates scale conventions (√σ/m_ρ ±10–15%) and continuum-limit drift
  (~0.41 at N_τ=4 → ~0.36 continuum).
- **Conformal window clears:** SU(2) fundamental N_f=4 is QCD-like; the disputed edge is N_f≈6
  (arXiv:1111.4104, 1511.01968). N_f=3 confines and breaks chiral symmetry — the model's use of the
  theory is legitimate on that axis.

**The synthesis bracket:** τ(SU(2), N_f=3, chiral limit) ≈ **0.39 ± 0.05** (generous 0.34–0.45).
Chain: measured 0.483 → chiral-limit mass slope (−0.06) → N_f=2→3 (−0.03) → convention/continuum
drift (0 to −0.05). Every step past the measured 0.483 is an SU(3)-analog transfer — stated, not
hidden.

**The adjudication, honest both ways:**
1. The model's **0.3503 sits at the BOTTOM EDGE** of the bracket; the central value ~0.40 is
   **above** the model. The registered window [0.330, 0.370] overlaps the bracket only in
   [0.34, 0.37] — compatible, not favoured.
2. The model **needs both** the chiral (not deconfinement) transition **and** near-maximal
   continuum/chiral suppression. If the condensation mechanism keys on deconfinement, the supported
   value is ~0.48 — **real tension**.
3. One genuine SU(2)-specific point in the model's favour: **the chiral and deconfining transitions
   DECOUPLE in SU(2)** (Kaczmarek et al., hep-lat/9809059 — the Polyakov susceptibility peak shrinks
   with lighter quarks, opposite of SU(3)), so the chiral T_c can legitimately sit below the
   Polyakov number. The dCDF's T_c is a condensation (chiral-like) transition, which is the right
   side of that fork — but the fork itself is un-adjudicated in the target theory.

**Net grade:** τ = 0.3503 is *permitted-at-the-edge* by the literature, not supported at centre;
the earlier debate band 0.355–0.382 occupies the lower half of the honest bracket. The decider
remains a dedicated lattice run of SU(2) N_f=3 — which, this hunt establishes, nobody has done.

---

## ADDENDUM 2 (2026-07-18): the NJL desk anchor — a third method, and it straddles

*A mean-field NJL gap-equation estimate of τ = T_c/√σ, computed directly (3D cutoff; the chiral
T_c from 1 = 4G N_c N_f ∫(1/p)tanh(p/2T); G and N_cN_f enter as one combination, so the two-color
transfer is exact at mean-field level; the ratio depends only on M/Λ).*

| reading | τ band | central |
|---|---|---|
| **raw mean-field** (Λ/√σ ∈ [1.2, 1.8], M/√σ ∈ [0.65, 0.75]) | 0.386 – 0.470 | **0.43** |
| **QCD-heat-corrected** (MF runs hot: sanity check gives T_c = 189 MeV vs lattice ~155 ⟹ ×0.82 — an SU(3)-analog transfer, the same borrowed-factor move flagged before) | 0.32 – 0.39 | **0.35** |

**The honest net: the straddle IS the finding.** Raw mean-field lands *above* the literature
bracket's centre (0.39 ± 0.05); the QCD-calibrated correction lands *on the model* (0.3503) — and
the difference between the two readings is exactly the non-perturbative content only a lattice
computes. A third independent method (after the dof-band and the literature inference) again
brackets τ in the mid-0.3s-to-mid-0.4s and again **cannot separate 0.3503 from 0.40**. The
standing verdict is unchanged and now triply anchored: permitted at the edge, not favoured at
centre, lattice-decided.
