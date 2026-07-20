# Thermal ½ — Defender vs Challenger debate: is the DE O(1) coefficient ½ derived, or E_b re-packaged?

> **DATED RECORD — the ½-claim's death, complete as debated.** Numbers herein are the
> E_b = 2.284 / 179-keyed era's. The "gap remains OPEN" verdict below was true when filed;
> the O(1) question was later DISSOLVED by a different route (the two doors stand in the
> derived phase-space ratio — the residual-debt census, 2026-07-18), and the standing chain
> now runs τ = ½ln2 → T_c = 177.10 keV → ρ_Λ¼ = 2.2599 meV (+0.44%). The ½ that dies in
> this file (a DE coefficient) is a different object from the later τ = ½ln2 (a kernel
> modulus) — do not conflate them. The kill itself stands: f = ½ has no seat, exactly as
> the referee certified.

**The claim under test:** PRTOE's dark-energy O(1) coefficient is f = ½, so ρ_Λ¼ = (½)¼ × 2.70 = 2.27 meV (+0.9% vs observed 2.25). The ½ is asserted to come from the quantum virial theorem splitting the condensate zero-point sum Σ½ħω into ¼ħω kinetic (w = +1, stiff, dilutes a⁻⁶) + ¼ħω potential (w = −1, the DE floor), so only half survives → Λ = ½ ρ_ZP.

---

### DEFENDER — Round 1

I am going to defend this honestly, which means I open by **separating the two things that are being sold as one**, and conceding up front the part the operator is right to distrust. The operator says it "looks too perfect." I agree it does, and I will show you exactly where the perfection is real (a knob-free split) and where it is cosmetic (a number that is E_b wearing a second hat).

#### 1. There are TWO independent O(1) coefficients here, not one. They must never be conflated.

The full numeric chain is:

    ρ_Λ¼ = (C_DE)¼ × door,   door = E_b / (C_door)¼,   C_door ≡ 16π²α_c^{3/2}

with two *distinct* O(1) factors:

- **C_door ≡ 16π²α_c^{3/2}** — the loop-and-coupling factor that lifts the flagship E_b up to the "perturbations door." 16π² is the standard one-loop phase-space factor (the ∫d⁴k/(2π)⁴ normalization); α_c^{3/2} is the condensate coupling at α_c = 3α. This is a *physics* number, and it is **not ½**.
- **C_DE ≡ ½** — the virial split fraction. This is the number the claim is actually about.

I computed both explicitly (α = 1/137.035999, α_c = 3α = 0.0218921):

| quantity | value | note |
|---|---|---|
| C_door = 16π²α_c^{3/2} | **0.5115** | **miss vs ½ = +2.30%** — NOT algebraically forced to ½ |
| C_DE = ½ (virial) | 0.5000 | exact, textbook harmonic-mode result |
| door = E_b/C_door¼ | 2.7007 meV | +20.0% vs 2.25 — a *bad* DE prediction on its own |
| E_b (flagship) | 2.2840 meV | +1.51% vs 2.25 |
| ρ_Λ¼ = (½)¼ × door | **2.2710 meV** | **+0.94%** vs 2.25 |

#### 2. The honest concession, stated first and without varnish.

The Challenger's sharpest blow lands. Watch the algebra:

    ρ_Λ¼ = (C_DE / C_door)¼ × E_b = (0.5000 / 0.5115)¼ × E_b = 0.99433 × E_b = 2.271 meV

Because **C_door = 0.5115 ≈ ½ = C_DE**, the door-lift (÷0.5115¼) and the virial-drop (×0.5¼) **nearly cancel**, and the whole apparatus collapses to

    ρ_Λ¼ ≈ E_b  (to 0.6%).

So I concede the core of the attack: **at the level of the number, the "½ result" (2.271) is the flagship E_b (2.284) re-packaged, nudged down 0.6%.** The "+0.9% vs 2.25" is **not** an independent second confirmation of the dark-energy scale. It is one number — E_b — appearing twice. Anyone who already grants E_b gets 2.27 for free, and the two extra steps almost annihilate. Selling +0.9% as fresh evidence would be double-counting, and I won't do it.

It is worse than that, and I'll say it because the corpus already says it: the flagship E_b itself is flagged in `PRTOE_THREE_EQUATIONS.md` / `PRTOE_MATH_SPINE.md` as **not independently sourced** — T_c ≈ 179 keV is "the observed ρ_Λ inverted-and-rounded," and the headline "+1.5%" is largely the τ = 2.25/ceiling rounding. So the number this route reproduces is itself close to the observed value re-expressed. The Thermal-½ route does **not** repair that circularity. I am not going to pretend it produces a from-first-principles 2.25.

#### 3. What I do NOT concede: the strong form of the attack is false.

The Challenger's option (b) was: concede re-packaging *if the algebra shows 16π²α_c^{3/2} = ½ is forced.* **It is not forced.** I checked:

    16π²α_c^{3/2} = 16π² × (3α)^{3/2} = 0.51150   (α_c = 3α exactly)

That is **0.5115, a 2.30% miss from ½** — a numerical near-coincidence, not an identity. So C_door and C_DE are genuinely *two different numbers* (0.5115 vs 0.5000); the derivation is **not a tautology** in which the door coefficient literally equals the virial coefficient. If they were identical, ρ_Λ¼ = E_b would be forced and the DE story would be pure circularity. They differ by 2.3%, which is precisely why ρ_Λ¼ = 2.271 ≠ E_b = 2.284. The distinction is real — but it is **fragile** (2.3%), and the unexplained near-equality C_door ≈ C_DE ≈ ½ is *itself* the "too-perfect" smell the operator noticed. I name it as an open, unexplained coincidence rather than hide it.

#### 4. What the ½ derivation actually buys — and it is not nothing.

Strip away the number (which is E_b re-packaged) and ask what physical content survives. Two things, both real:

**(a) The ½ is knob-free — a derivation, not a fit.** For a quantum harmonic mode the virial theorem is exact: ⟨½φ̇²⟩ = ⟨½ω²φ²⟩ = ¼ħω, summing to the zero-point ½ħω. There is no tunable dial that could have been set to any other value; ½ is forced by ⟨T⟩ = ⟨V⟩. Contrast this with a fitted O(1): the claim did **not** add a free parameter to reach 2.25. A coincidence that costs zero new knobs is worth strictly more than one you tuned — even if the number it lands on is not independent.

**(b) It supplies the equation-of-state content that "just quote E_b" cannot.** For a homogeneous scalar condensate the split is *classically* exact, not hand-waved. With ∇φ = 0:

    ρ = ½φ̇² + V,   p = ½φ̇² − V
    kinetic ½φ̇²:  p_kin = +ρ_kin  → w = +1  (stiff, dilutes a⁻⁶)  ✓
    potential V:   p_V  = −ρ_V   → w = −1  (survives as the floor) ✓

So the mechanism *derives why the surviving DE component is the potential half and carries w = −1 exactly* — which is the physically load-bearing statement (it protects w = −1, ties to `P-2026-018`). Quoting E_b as "the DE scale" asserts w = −1 by fiat; the virial split gives a reason. That reason is the genuine deliverable.

#### 5. Where the ½ is genuinely exposed (I'd rather say it than have it found).

- **The stiff-half assumption is a soft spot.** It is uncontroversial that a *coherent* kinetic field gives w = +1 kination diluting a⁻⁶. It is **not** obvious that the *zero-point* kinetic fluctuation ⟨φ̇²⟩ redshifts as a⁻⁶ like coherent kination — vacuum fluctuations are not a coherent rolling field. If the kinetic zero-point half does *not* dilute away, you do not get Λ = ½ρ_ZP; you get the full ρ_ZP or something frame-dependent. This step needs the preferred-frame dynamics to actually carry it, and that is asserted, not yet computed here.
- **The whole split is contingent on the preferred frame.** The claim admits this: a Lorentz-invariant vacuum is all-w = −1 (p = −ρ for every mode), *no* split, and you'd keep the full zero-point sum. So ½ is not a universal truth — it is a *consequence of the dCDF being a condensate with a rest frame*. That is a legitimate, falsifiable structural commitment, but it means "½" is downstream of a physical assumption, not a free-standing theorem.

#### 6. Defender's Round-1 position, in one paragraph.

The ½ is a **real, knob-free derivation of the split** (virial theorem, exact) and it **derives the w = −1 equation of state of the surviving floor** — content that quoting E_b does not provide. But I concede without reservation that the **number 2.271 is E_b re-packaged** (because 16π²α_c^{3/2} = 0.5115 ≈ ½ makes the door-lift and virial-drop nearly cancel), so the "+0.9% vs 2.25" is **not independent evidence**, and the near-coincidence C_door ≈ ½ is itself unexplained. My defensible claim is the honest *option (a)*: **the virial split closes the named "why-is-the-owed-O(1)-a-half" gap and fixes the equation of state, without adding a knob — it does not produce a numerically independent hit, and I will not claim it does.** Over to the Challenger to show either (i) that even the *split* is post-hoc / knob-carrying, or (ii) that the stiff-half a⁻⁶ dilution fails, which would break even the modest claim I am defending.

*(All numbers above from a plain Python evaluation; work reproduced inline in §1–2.)*

---

### CHALLENGER — Round 1

I want to open by crediting the Defender, because the concession is real and it changes the shape of the debate. He has already granted the number: 2.271 = E_b re-packaged, +0.9% is not independent evidence, and C_door = 0.5115 ≈ ½ is an unexplained near-coincidence doing load-bearing work. I confirm all of it and I will not spend a round re-killing a corpse the Defender already buried. My Python reproduces his chain exactly:

| quantity | value | vs 2.25 |
|---|---|---|
| C_door = 16π²(3α)^{3/2} | 0.51150 | +2.30% from ½ (a coincidence, not an identity — Defender is right) |
| door = E_b/C_door¼ | 2.70075 meV | +20.03% (bad on its own) |
| E_b (flagship) | 2.28400 meV | +1.51% |
| ρ_Λ¼ = (½)¼ × door | 2.27105 meV | +0.94% |
| (½/C_door)¼ | 0.99433 | ρ_Λ¼ = 0.99433 × E_b ✓ |

So the Defender's §2 stands. The fight is now exactly where he asked me to take it: **the surviving "modest" claim — that the virial split is a knob-free derivation of a w = −1 dark-energy floor.** I am going to argue that this modest claim is also false, on four independent grounds, and that the strongest of them is a physics knockout, not a rhetorical one. I concede in advance the one true thing (§A) so the disagreement is clean.

#### A. What I concede: the ENERGY split ¼ + ¼ is correct and knob-free.
For a quantum harmonic mode the virial theorem is exact: ⟨½φ̇²⟩ = ⟨½ω²φ²⟩ = ¼ħω. That is textbook and carries no dial. **Granted, fully.** The dispute is not about the energy bookkeeping. It is about the *pressure*, and everything downstream of it.

#### B. Knockout: the virial theorem the derivation leans on GUARANTEES w = 0 for the mode — not a (+1, −1) split.
Equation of state is about **pressure**, p = ⟨T_xx⟩, not about how you label energy. For a homogeneous scalar the stress tensor gives the exact pressure

    p = ½φ̇² − V      (the SAME classical formula the Defender used in §4b)

Now evaluate it **in the actual quantum state the derivation invokes** — the virial ground state — instead of in a classical rolling background. Take the k = 0 rest-frame mode (ω = m), the cleanest case, and use the very split the Defender just granted:

    ⟨½φ̇²⟩ = ¼ħω        (kinetic)
    ⟨V⟩   = ⟨½ω²φ²⟩ = ¼ħω  (potential)

    ρ = ⟨½φ̇²⟩ + ⟨V⟩ = ¼ + ¼ = ½ħω        ✓ (matches)
    p = ⟨½φ̇²⟩ − ⟨V⟩ = ¼ − ¼ = 0           ← the pressures CANCEL

    ⟹ w = p/ρ = 0 / (½ħω) = 0.

This is the honest quantum result and it is fatal to the mechanism. The virial theorem does not hand you "a w = +1 fluid plus a w = −1 fluid." It hands you a mode whose kinetic and potential **pressures cancel**, giving **w = 0 — matter-like, redshifts a⁻³, zero dark energy asymptotically.** The claim needs the survivor to be w = −1; the object it actually names produces w = 0. There is no dark-energy floor at all under an honest reading.

Where did the (+1, −1) come from, then? From the **classical coherent-field extremes**, illegitimately imported:

    w_classical = (½φ̇² − V)/(½φ̇² + V)
      pure kination (V = 0):      w = +1   ← requires a coherent roll, ⟨φ̇⟩ ≠ 0
      pure potential (φ̇ = 0):     w = −1   ← requires NO kinetic energy

The vacuum has ⟨φ̇⟩ = 0 (it is stationary, not rolling) and ⟨φ̇²⟩ = ¼ħω ≠ 0 (it is not frozen). It is neither extreme. The derivation quietly treats the ground state as if it were "half a kination fluid + half a Λ fluid," but a harmonic ground state is **not** a superposition of those two fluids — it is a single mode with ⟨T⟩ = ⟨V⟩, and that condition forces w = 0. So the load-bearing sentence "kinetic carries w = +1, potential carries w = −1" is a category error: it reads classical *pure-state extremes* off a quantum *mixed-pressure* ground state.

#### C. The "kinetic half redshifts away, potential half survives at w = −1" rescue produces an UNPHYSICAL end-state (uncertainty-principle knockout).
The Defender's §5 flags this as soft; I claim it is broken, not soft. Suppose you accept the story that the kinetic ¼ dilutes a⁻⁶ and vanishes while the potential ¼ persists, leaving a pure-V, w = −1 floor. The proposed **end-state** has

    ⟨½φ̇²⟩ → 0   while   ⟨V⟩ = ⟨½ω²φ²⟩ stays finite (= ¼ħω).

For a harmonic mode ⟨φ̇²⟩ ∝ ⟨p²⟩ and ⟨φ²⟩ ∝ ⟨x²⟩, bound by ⟨p²⟩⟨x²⟩ ≥ ħ²/4. Driving ⟨φ̇²⟩ → 0 sends ⟨p²⟩ → 0, which **forces ⟨x²⟩ → ∞, hence ⟨V⟩ → ∞, not ¼ħω.** The state "kinetic energy gone, potential energy sitting quietly at a finite value" **does not exist** in quantum mechanics — it violates Heisenberg. So the survivor the mechanism advertises (a finite pure-potential w = −1 remnant) is not a physical quantum state at all. Either the whole mode redshifts together (staying a legal squeezed/ground state, in which case ⟨T⟩ = ⟨V⟩ is preserved and w stays 0 — see D), or you have left quantum mechanics. You cannot amputate one of two conjugate halves and keep the other finite.

#### D. The derivation is internally self-contradictory: it invokes ⟨T⟩ = ⟨V⟩ to split, then must violate ⟨T⟩ = ⟨V⟩ to evolve.
The ¼ + ¼ split (§A, granted) is *only* valid **because** ⟨T⟩ = ⟨V⟩ holds — that is the virial theorem, and for a harmonic mode it holds **at every instant**, not once. But the mechanism then evolves the two halves with **different** equations of state (kinetic a⁻⁶, potential a⁰). After even a fraction of an e-fold, ⟨T⟩ ≠ ⟨V⟩ — the state is no longer the virial ground state, so the ¼ + ¼ split it was built on no longer holds. The derivation uses the virial theorem as a permanent structural fact to get ½, then breaks that same fact to get the survivor. **You may have the split, or you may have the differential redshifting, but not both.** Pick one and the mechanism collapses: keep virial → w = 0 forever (no DE); break virial → you no longer have the ¼ + ¼ that gave you ½.

#### E. There is no mode sum — "½ of Σ½ħω" is ½ of a single pre-computed number.
The claim is narrated as "the un-cancelled zero-point *sum* Σ½ħω splits per mode." But nowhere in the chain is a Σ ever performed. The "door" is one closed-form number, E_b/C_door¼ = 2.7007 meV — no spectrum, no dispersion relation ω(k), no cutoff, no density of states. The per-mode virial theorem (a statement about *each* ω) is invoked to license a factor of ×½ on a quantity that was **never assembled from modes**. If there were a real Σ½ħω, it would be a quartically cutoff-dependent divergence whose *pressure*, under a hard cutoff, comes out radiation-like (w ≈ +⅓), and only a Lorentz-invariant regulator restores p = −ρ for the *total* — which is precisely the regulator the condensate's preferred frame is said NOT to have. So the mode-sum framing, taken seriously, argues **against** a clean w = −1 survivor, not for it. Taken not-seriously, it is decorative narration wrapped around "×½ of one number."

#### F. Bonus — ½ is not even the data-selected coefficient.
The coefficient that would hit the observed 2.25 exactly from door = 2.7007 is

    f_exact = (2.25/2.7007)⁴ = 0.4817,

so **½ overshoots the data-optimal value by +3.8%.** ½ was not selected because the data prefer it (the data prefer 0.482); it was selected because it is a tidy number sitting in the same 0.48–0.51 cluster as C_door = 0.5115 and f_exact = 0.4817. Three different quantities all loitering near ½ is the "too-perfect" smell itself — none of them *is* ½, and the one the data actually wants (0.482) is the one the theory does **not** produce.

#### G. Challenger's Round-1 position, in one paragraph.
I grant the energy split ¼ + ¼ is exact and knob-free (§A) and I grant the Defender's number concession in full. But the *modest* surviving claim — "the virial split derives a w = −1 floor without a knob" — fails. The honest quantum pressure of the virial ground state is **w = 0, not w = −1** (§B): the ±1 values are classical pure-state extremes wrongly imported onto a mixed-pressure ground state. The rescue that redshifts only the kinetic half leaves an end-state that **violates the uncertainty principle** (§C) and **contradicts the very virial theorem used to build the split** (§D). And there is no actual mode sum for the "per-mode" theorem to act on (§E), while ½ isn't even the data-selected coefficient (0.482 is; §F). So the derivation does not *derive* w = −1 — it *asserts* w = −1 by quoting the classical pure-potential extreme, exactly the "assert w = −1 by fiat" the Defender said the virial split was supposed to replace. The deliverable he defends (a reason for w = −1) is the one thing the mechanism does not supply. Over to the Referee.

*(All numbers from plain Python, reproduced in the table above and inline in §B, §F; oscillator/stress-tensor relations are standard.)*

---

### DEFENDER — Round 2

The Challenger's §B is correct, and I am not going to fight correct physics. This is a concession round. I will state precisely what dies, verify it independently so the concession is earned rather than reflexive, and preserve only what genuinely survives.

#### 1. §B — CONCEDED IN FULL. The virial ground state is w = 0, and my Round-1 §4b was wrong.

I re-derived it independently and get the Challenger's answer:

    k = 0 rest-frame mode, homogeneous (∇φ = 0):  p = ⟨½φ̇²⟩ − ⟨V⟩ = ¼ħω − ¼ħω = 0
    ⟹ w = p/ρ = 0.

And the sharper, model-independent confirmation the Challenger didn't even need to invoke: a scalar **oscillating** in a potential V ∝ φⁿ has a virial-time-averaged equation of state ⟨w⟩ = (n−2)/(n+2). I checked:

| V ∝ φⁿ | ⟨w⟩ = (n−2)/(n+2) |
|---|---|
| n = 2 (harmonic) | **0.000** |
| n = 4 | +0.333 |
| n = 6 | +0.500 |

The harmonic case (n = 2) gives **⟨w⟩ = 0 exactly**. This is not an obscure result — it is *the* textbook reason a coherently oscillating massive scalar is **cold dark matter** (axion/fuzzy-DM). So the object the claim names — a harmonic condensate mode — is, done honestly, a **dark-matter** (w = 0) contribution to Ω_m, *not* a dark-energy (w = −1) floor. My Round-1 §4b read the classical pure-state extremes (+1 for V=0 kination, −1 for φ̇=0 freeze) off a stationary mixed ground state that sits at neither extreme. That was a category error. **Conceded.**

#### 2. §C and §D — CONCEDED. The rescue is broken, not merely soft.

I flagged the stiff-half a⁻⁶ dilution as "soft" in Round 1 §5. The Challenger correctly upgrades "soft" to "broken," and I accept the upgrade on both counts:

- **§C (uncertainty):** the advertised survivor — ⟨½φ̇²⟩ → 0 while ⟨V⟩ = ⟨½ω²φ²⟩ stays finite at ¼ħω — is not a legal quantum state. ⟨p²⟩ → 0 forces ⟨x²⟩ → ∞ via ⟨p²⟩⟨x²⟩ ≥ ħ²/4, so ⟨V⟩ → ∞, not a quiet finite floor. You cannot amputate one conjugate half and keep the other finite. **Conceded.**
- **§D (self-contradiction):** the ¼+¼ split is *licensed by* ⟨T⟩ = ⟨V⟩, which for a harmonic mode holds at every instant. Evolving the halves with different w (a⁻⁶ vs a⁰) immediately breaks ⟨T⟩ = ⟨V⟩, dissolving the very split that produced the ½. Keep the virial identity → w = 0 forever; break it → you no longer have the ½. You cannot have both. **Conceded.** This is the cleanest kill: the mechanism needs the virial theorem to be *permanent* (to get ½) and *temporary* (to evolve the survivor) at once.

#### 3. §E — CONCEDED, and it cuts the way the Challenger says.

There is no Σ in the chain; the "door" is one closed-form number, E_b/C_door¼. Worse for my side: if you *did* assemble a real Σ½ħω, its pressure under a preferred-frame hard cutoff comes out radiation-like (w ≈ +⅓), and only a Lorentz-invariant regulator restores p = −ρ for the **total** — but Lorentz invariance is exactly what the condensate's preferred frame is stipulated *not* to have. So the mode-sum framing, taken seriously, argues **against** a clean w = −1 survivor. Taken not-seriously, it is narration around "×½ of one number." Either reading hurts the claim. **Conceded.**

#### 4. §F — already granted in Round 1 (f_exact = 0.4817, ½ overshoots by +3.8%). Reaffirmed.

#### 5. What this does to my Round-1 "option (a)". It fails at its own stated job.

My fallback in Round 1 was: even if the *number* is E_b re-packaged, the virial split still earns its keep by *deriving the equation of state* (w = −1) of the surviving floor — closing the named "why-is-the-owed-O(1)-a-half" gap. **That fallback is now dead.** The equation of state the mechanism honestly derives is **w = 0, not w = −1.** A derivation that delivers the wrong equation of state has not closed the gap; it has mislabeled dark matter as dark energy. I **withdraw** option (a). The deliverable I said was the "genuine content" — a *reason* for w = −1 — is precisely the thing the mechanism does not supply; it asserts w = −1 by quoting the classical pure-potential extreme, which is the same "w = −1 by fiat" I claimed it replaced. The Challenger's §G nails this and I concede the framing.

#### 6. The one true statement I can still stand behind (and it does NOT rescue ½).

For a symmetry-broken condensate there *is* a legitimate w = −1 object: the **static value of the potential at its minimum, V₀ = V(φ_min)** — a c-number offset, Lorentz-invariant, p = −ρ exactly, coefficient **1**. But three things follow, all against the claim:

    coefficient 1 ⟹ ρ_Λ¼ = door = 2.701 meV = +20.0% vs 2.25.

- The honest w = −1 candidate carries coefficient **1**, not ½, and it **over-predicts by ~20%**. The virial "½" was, in effect, the factor papering over that 20% gap — but §B–§D show it is not a legitimate factor to apply.
- V₀'s *value* is the unsolved cosmological-constant/dark-energy-value problem; nothing in the virial story sources it. (Consistent with `PRTOE_MATH_SPINE.md`, which already flags E_b/T_c as "the observed ρ_Λ inverted-and-rounded, not independently sourced.")
- So the split of the condensate is honestly: a **w = 0 oscillation/zero-point sector** (dark-matter-like, Ω_m) plus a **w = −1 potential-floor offset V₀** (coefficient 1, value un-sourced). There is no clean "half the zero-point survives at w = −1." The ½ has no legitimate home.

#### 7. Defender's Round-2 position, in one paragraph.

I concede §B, §C, §D, §E (and reaffirm §F and the Round-1 number concession). The virial split does **not** derive a w = −1 dark-energy floor: the honest equation of state of a harmonic condensate mode is **w = 0** (the textbook scalar-dark-matter result, ⟨w⟩ = (n−2)/(n+2) = 0 at n = 2), the "redshift only the kinetic half" rescue is forbidden by the uncertainty principle and self-contradicts the virial identity it was built on, and no mode sum is ever performed. My Round-1 fallback (option a — "it still fixes the equation of state") is **withdrawn**, because the equation of state it fixes is the wrong one. The only legitimate w = −1 object in the condensate is the static potential floor V₀, which carries coefficient **1** (→ +20%), not ½, and whose value is un-sourced. **Net: f = ½ is neither a numerically independent result (Round 1) nor a derived coefficient for a w = −1 floor (Round 2) — it is a tidy value in the 0.48–0.51 cluster {C_door = 0.5115, f_exact = 0.4817, ½} with no mechanism that legitimately selects it.** I am at my final position; I do not expect to reverse these concessions in a further round.

*(w-derivations independently reproduced in Python; V ∝ φⁿ virial average and the k=0 stress-tensor pressure are standard.)*

---

### DEFENDER — FINAL POSITION

The claim that f = ½ is a *derived* dark-energy coefficient does not survive honest stress-testing, and I concede it on two independent grounds. **(1) The number is not independent:** because 16π²α_c^{3/2} = 0.5115 ≈ ½, the door-lift and virial-drop nearly cancel and ρ_Λ¼ = 0.994 × E_b = 2.271 meV — the flagship E_b (itself flagged in-corpus as the observed ρ_Λ inverted-and-rounded) re-packaged to 0.6%, so "+0.9% vs 2.25" is not fresh evidence. **(2) The mechanism is physically invalid:** the honest equation of state of a harmonic condensate mode is w = 0 (the textbook scalar-dark-matter result ⟨w⟩ = (n−2)/(n+2) = 0 at n = 2), not w = −1; the (+1, −1) split reads classical pure-state extremes off a stationary mixed ground state (category error), the "redshift only the kinetic half" rescue violates the uncertainty principle and self-contradicts the virial identity that produced the ½, and no mode sum is ever performed.

**What remains true and useful:** the ¼ + ¼ *energy* split is exact and knob-free (both sides granted this); the *only* legitimate w = −1 object in the condensate is the static potential floor V₀ with coefficient **1** (→ 2.70 meV, +20%), whose value is un-sourced — there is no legitimate home for a factor ½. The three quantities loitering near a half — C_door = 0.5115, f_exact = 0.4817, and ½ — are a coincidence cluster, not a derivation; none of them *is* ½, and the one the data select (0.4817) is the one the theory does not produce. **Verdict: f = ½ is a re-packaging plus an invalid equation-of-state assignment, not a derived O(1) coefficient. The named "why is the owed O(1) a half" gap remains open.**

---

### CHALLENGER — FINAL POSITION

The Defender argued this honestly to the end and conceded on the physics, not on rhetoric — so I record the agreement plainly and add nothing I have to walk back later.

**What both sides now agree is dead.** The number is not independent: 16π²α_c^{3/2} = 0.51150 ≈ ½ makes the door-lift and virial-drop nearly cancel, so ρ_Λ¼ = 0.99433 × E_b = 2.271 meV — the flagship E_b re-packaged and nudged down 0.6%. "+0.9% vs 2.25" is not fresh evidence. And the mechanism is physically invalid: the honest equation of state of a harmonic condensate mode is **w = 0**, confirmed two independent ways (direct k=0 pressure p = ¼ − ¼ = 0, and the textbook oscillation average ⟨w⟩ = (n−2)/(n+2) = 0 at n = 2 — this object is scalar *dark matter*, Ω_m, not dark energy). The (+1, −1) assignment reads classical pure-state extremes off a stationary mixed ground state (§B, category error); the "redshift only the kinetic half" survivor violates the uncertainty principle (§C, ⟨φ̇²⟩→0 forces ⟨V⟩→∞) and self-contradicts the very virial identity that produced the ½ (§D, needs ⟨T⟩=⟨V⟩ permanent to split and temporary to evolve); and no Σ½ħω is ever performed (§E). I accept the Defender's full concession of §B–§E and his withdrawal of Round-1 option (a).

**The one residue, and why it does not rescue ½.** The only legitimate w = −1 object in a symmetry-broken condensate is the static potential floor V₀ = V(φ_min): a Lorentz-invariant c-number, p = −ρ exactly, coefficient **1** → ρ_Λ¼ = door = 2.701 meV, **+20.0%**. So the honest decomposition of the condensate is (w = 0 oscillation/zero-point sector, dark-matter-like) + (w = −1 static floor V₀, coefficient 1, +20%, value un-sourced). The virial "½" was functionally the fudge covering the 20% gap between the coefficient-1 floor and the observed value — and §B–§D show it is not a legitimate factor to apply. There is no seat for a ½ anywhere in the honest structure.

**Challenger final verdict.** The operator's instinct — "it looks too perfect" — was correct and now has a mechanism: three distinct quantities (C_door = 0.5115, f_exact = 0.4817, ½) all cluster near a half by coincidence, none of them *is* ½, and the value the data actually select (0.4817) is the one the theory does not produce. f = ½ is E_b re-packaged (Round 1) wrapped in an invalid w = −1 assignment (Round 2), not a derived O(1) coefficient. The "why is the owed O(1) a half" gap is **not closed — it is open**, and the only honestly w = −1 object costs coefficient 1 and a +20% miss with an un-sourced value. Full agreement with the Defender's final position; no further rounds needed.

*(All numbers plain Python, reproduced in the Round-1 table and §B/§F; oscillator, φⁿ-virial, and k=0 stress-tensor relations are standard.)*

---

### REFEREE — VERDICT

Both debaters have filed FINAL POSITIONS, and they converge. I take no side; my job here is to certify the numbers that decide it and state the assessment of the arguments neutrally. I independently re-ran every load-bearing quantity in plain Python; all check out:

| quantity | verified value | bearing |
|---|---|---|
| C_door = 16π²(3α)^{3/2} | **0.51150** (+2.30% from ½) | a near-coincidence, **not** an algebraic identity — the Defender was right that ½ is not *forced* |
| (½/C_door)¼ = ρ_Λ¼/E_b | **0.99433** | the door-lift and virial-drop nearly cancel |
| E_b | 2.2840 meV (+1.51%) | the flagship |
| ρ_Λ¼ = (½)¼ × door | **2.2711 meV (+0.94%)** | = 0.994 × E_b — E_b re-packaged, nudged down 0.6% |
| f_exact = (2.25/door)⁴ | **0.48172** | the data-selected coefficient; ½ overshoots it by **+3.80%** |
| ⟨w⟩ = (n−2)/(n+2) at n=2 | **0.000** | harmonic condensate mode is w = 0 (scalar dark matter), confirmed also by k=0 pressure p = ¼ − ¼ = 0 |
| coefficient-1 static floor V₀ | door = 2.7008 meV (**+20.0%**) | the only honestly w = −1 object; costs coefficient 1, not ½, value un-sourced |

**Assessment of the arguments.** On the circularity suspicion the referee's neutral finding is: 16π²α_c^{3/2} = 0.5115 is **2.3% away from ½ — a numerical near-coincidence, not a tautology** (the Defender's one sustained point). But that distinction does not rescue the result, because the two extra steps (÷C_door¼, ×½¼) multiply to 0.994, so ρ_Λ¼ = 2.271 meV is the flagship E_b re-expressed to within 0.6%. The "+0.9% vs 2.25" is therefore **not independent evidence** — a point the Defender conceded in Round 1 and the Challenger confirmed. On the surviving "modest" claim — that the virial split at least *derives* a w = −1 equation of state without a knob — the debate resolved decisively against it: the honest equation of state of a harmonic condensate mode is **w = 0** (matter-like), established two independent ways (direct k=0 pressure, and the textbook ⟨w⟩ = (n−2)/(n+2) = 0 at n = 2 that makes a coherently oscillating scalar cold dark matter). The (+1, −1) split imported classical pure-state extremes onto a stationary mixed ground state (category error); the "redshift only the kinetic half" rescue is forbidden by the uncertainty principle and self-contradicts the very virial identity ⟨T⟩ = ⟨V⟩ that produced the ½; and no Σ½ħω is ever actually assembled. The Defender withdrew its Round-1 fallback on these grounds.

**Verdict.** On the arguments as debated, **f = ½ is not a genuine independent derivation. It is E_b re-packaged via the 16π²α_c^{3/2} ≈ ½ near-coincidence (ρ_Λ¼ = 0.994 × E_b), wrapped in an invalid equation-of-state assignment (the object is honestly w = 0, not w = −1).** The one part that is real and knob-free — the ¼ + ¼ *energy* split (virial theorem, exact) — carries no pressure content and does not select a dark-energy coefficient. Three distinct quantities cluster near a half by coincidence {C_door = 0.5115, f_exact = 0.4817, ½}; none of them *is* ½, and the value the data select (0.4817) is the one the theory does not produce. The only honestly w = −1 object in the condensate is the static floor V₀ at coefficient **1** (→ +20%, value un-sourced) — there is no legitimate seat for a factor ½. **The named "why is the owed O(1) a half" gap remains OPEN.** The operator's "it looks too perfect" instinct is vindicated, now with a mechanism.

*(Referee arithmetic: α = 1/137.035999, α_c = 3α; all seven rows reproduced in plain Python. No side was advocated; only the numbers were certified.)*
