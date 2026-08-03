# PRTOE — Session Findings 2026-07-29b (the docket sweep)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](../PRTOE_READERS_GUIDE.md); claim
> conditionality maps in [PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md).*

Second session of the day. The first ([2026-07-29](PRTOE_session_2026-07-29_findings.md)) was
corrections; this one was a **sweep of every pending model-building docket**, including the nine that
had never been opened, then a second pass over six more (§8). Audit **1,255 → 1,374** closed-form
checks, all passing. Each docket below names
the instrument built for it; every one carries pre-stated controls and at least one anti-control, and
all pass — including the one whose *result* had to be withdrawn anyway (§3, and §7 on why no control
could have caught it). *(No instrument count is quoted here on purpose: see §7 and protocol 49 — six
such counts in this corpus were wrong when checked today, and an uncheckable tally is worth less than
the per-docket references below.)*

**The single most useful discovery is methodological and it recurred:** *"not desk" labels are
hypotheses, not statuses.* Two were simply wrong (#1, #13), one understated what already existed
(#69), and three more had verifiable arithmetic sitting inside a genuinely blocked physics question
(#39, #62, #75).

**One finding in this record was withdrawn hours after it was written** — #85's, in §3, on re-reading
the script that defines the symbol it fitted. The replacement is stronger than what it replaces, and
the failure mode it exposes is one no anti-control catches.

---

## 1. Dockets closed

**#1 — the family degeneracy.** Answered and closed. Its residual was handed to #2.

**#51 — μ₅ and the third horn.** Both legs verified in exact rationals. **ΣY² = 10** over the
three-generation roster — and *independently validated*, since feeding it through the Standard
Model's own one-loop hypercharge coefficient (⅔ΣY²_f + ⅓ΣY²_s, Higgs contributing ½) returns
**41/6 exactly**, a number the SM fixes without reference to this model. The broken-phase ΣQ² = 16 is
genuinely different, so the phase matters. And **no left-handed field shares a gauge representation
with any right-handed one** — exhaustive over all 2×3 pairings; the weak rep alone forbids it. That is
an *obstruction*, not a shortage of candidates, so "undetermined by construction" is the right grade.
Anti-control: one hypothetical vector-like partner for e_R is detected immediately.

**#64 — the dCDF residual.** Label verified correct. The SOC escape hatch is closed **structurally**
(sub-ohmic self-tuning belongs to the dark-*matter* channel), not conditionally — so it cannot be
discharged by establishing a premise. No desk residue: the corpus records the three s values and the
21-dex miss but not the function connecting them, and reconstructing it would mean inventing the
object under audit.

---

## 2. #2 — the seed route closed, and a Y-junction claim that I later withdrew

> ### ⚠ THE SECOND HALF OF THIS SECTION IS WITHDRAWN — read this first (later the same day)
>
> Everything below about the **seed route** stands. Everything below about the **Y-junction** does not.
> `scripts/y_junction_corrected_functional.py` (17 controls) found two errors:
>
> 1. **α_dark ≈ 3.2 was retracted on 2026-07-18**, eleven days before I graded against it — *"the
>    repulsive-balance α_dark ≈ 3.2 consistency line is RETRACTED — wrong sign in the gauge channel."*
>    I checked the number and not its status.
> 2. **The two-term functional below is the retracted one.** Three SU(2) adjoints in the ε^abc singlet
>    satisfy Σᵢ Tᵢ = 0, so Tᵢ·Tⱼ = **−1, attractive** — a repulsive gauge Coulomb term cannot appear.
>    The live functional is the three-term hybrid **E(d) = √3σd − 3q̃²ln d − 3α_d/d**, with the
>    repulsion supplied by the *medium* as a vortex log.
>
> Not a reparametrisation: the two demand q̃²/√σ = 1.110587 against 2.136318, a factor of exactly c_K.
> The live chain reproduces end to end — q̃²/√σ = 1.1106, stability ceiling c_K²/√3 = 2.1363,
> **F_dark/√σ = 0.420423**, band [0.4009, 0.4700]. **So #2 was never blocked on a convention.** It is
> external compute — one SU(2) N_f = 3 lattice campaign refereeing T_c/√σ, F_π/√σ and w√σ together —
> and has been since 2026-07-18. *(Also: the q² = 2.136318 below is algebraically the same expression
> as that stability ceiling, c_K²/√3. Recorded so it is not chased as a coincidence.)*

**The seed route is closed for supplying the value.** The map from three real seed couplings to
(G₀, b) is an **exact bijection** (round-trip 10⁻¹⁵), and its inverse gⱼ = ⅓[G₀ + 2|b|cos(arg b +
2πj/3)] has *the same functional form as the mass formula*. So **gⱼ ∝ √mⱼ** — fed the measured
leptons, the seeds couple as **1 : 14.379 : 58.969**. Specifying the couplings *is* specifying the
masses; the picture reduces the unknown count by **zero**. C14's "g₁/g₀ = −0.3001 is a constraint on
the seeds" was too generous and is corrected — it is Koide in another basis. *Not vacuous:* four seeds
on three sites **would** reduce (kernel dimension 1).

**So c_K is the only remaining route, and its last step is the Y-junction.** Built explicitly:
minimising E(d) = √3σd + 3q²/d gives **c_K = 3^(1/4)·q**, the Steiner factor being the entire
geometric content, so the target converts directly into **q² = 2.136318**.

> **And it breaks there.** The recorded α_dark ≈ 3.2 does **not** reproduce in any standard
> convention — q²/(4π) = 0.170 (19× low), q²/2 = 1.068 (3× low), q² = 2.136 (1.5× low) — and the
> corpus never says which convention it meant. "Strong-natural, consistency-grade only" was an
> unfalsifiable gesture: a coupling quoted without its convention cannot be confronted with a lattice
> number, which is exactly what the route needs next.

**A self-correction inside the same hour.** I first wrote that the Δ topology "gives 2.067, outside
the correlator locus", treating the locus as selecting Y. That compared at *fixed q*, and q is fixed
by nothing. Each topology reaches the same c_K with its own charge — Y needs q² = 2.136318, Δ needs
1.850106, ratio exactly 2/√3 — so **the locus cannot discriminate**. The ambiguity shifts the coupling
to be justified by 15.5%; it does not threaten the c_K agreement.

---

## 3. #85 — a wrong answer caught and replaced by a stronger one, inside the same session

**First I got it wrong, and the error is the more instructive half.** I read the recorded
ε_D/ε_S ∈ {2, √2, 1, ½} as an *energy* ratio and reproduced all four as 2·(k_D/k_S)^p at p ∈ {0, ½, 1}
on the ring's normal modes — concluding "three laws, not four", "the live fork is p = ½ vs p = 1",
and "the delivery law is a radial-sector statement". **Every clause of that is withdrawn.** The
corpus's ε is a **stiffness**, fixed independently in two scripts by ⟨f²⟩ ∝ 1/ε and ω ∝ √ε. Fitting
four numbers with a quantity that is not the one they denote is **protocol 42** — and I committed it
in the session that wrote protocol 42 up. The two constructions agree at p = 0 **and nowhere else**,
so the matches at √2 and 1 were a coincidence of small powers of 2.

**The corpus's real algebra**, from `scripts/delivery_law_two_parameters.py` (20 controls, two of them
anti-control blocks). With energy per degree of freedom e ∝ ε^p and s recording how a sector's total is
counted, the sector amplitude is X² ∝ g^s·ε^(p−1), and the null R_c = M_c solves to

> **ε₁/ε₀ = 2^( s / (1 − p) )**

| delivery law | energy | s | p | ε₁/ε₀ |
|---|---|---|---|---|
| thermal equipartition | ½T per dof | 1 | 0 | **2** |
| sudden quench, 1/ω² | ∝ 1/ε per dof | 1 | −1 | **√2** |
| equal sector delivery | E per sector | 0 | — | **1** |
| doublet gets half | E, E/2 per sector | −1 | 0 | **½** |
| *zero-point, ½ħω* | ∝ √ε per dof | 1 | ½ | **4** |

**Two parameters, not one** — √2 needs p ≠ 0 and 2 needs s ≠ 0. Three labels were also wrong: √2 is
the **sudden quench**, not the zero-point law; the zero-point law gives **4**, absent from the
recorded four; and **"equal amplitude" is not a delivery law at all** — at p = 1 the amplitude goes
ε-independent, the null degenerates to 2 = 1, and it constrains nothing.

> **And the docket is answered rather than narrowed.** Q = ⅔ needs ρ² = ½, hence ε₁/ε₀ = **2 exactly**,
> hence s = 1 − p. Only thermal equipartition lies on that line — the next-nearest, √2, misses ⅔ by
> **207,107 ppm** against a 6 ppm budget. With s restricted to the two ways a sector total can be
> counted, s = 0 fails at every p and **s = 1 forces p = 0 uniquely**.

**So the fork was never four-way, and what it hid is a tension.** The null selects thermal
equipartition *uniquely*, and the existing discriminator has already shown thermal equipartition
overruns the 6 ppm budget by **171×** at the corpus's own x₁ = 2/9. Those two results conflict, and
the conflict is **inside** the Koide derivation, not upstream of it. The occupancy lock is not one
option among four — it is the only named escape from a contradiction.

**C3's warning is extended, not resolved.** The required ε₁/ε₀ = 2 is **neither** existing pair: the
radial Hessian gives k_D/k_S = ½ (that is law 3, which yields Q = 5/3), and the circulant amplitude
stiffnesses at the Koide point give 0.1213. The delivery law's ε is a **third** stiffness pair, and
which one it is remains open.

---

## 3b. The escape from that contradiction is closed too — by impossibility

`scripts/occupancy_lock_cannot_deliver.py`, 17 controls, three of them anti-control blocks. T6 named the
occupancy lock as the way out, because *"an integer occupancy cannot drift, which is the one exactness
class a 6×10⁻⁶ claim admits."* **It cannot deliver the null at any occupancy.** Two lines: with
⟨x²⟩ = (2n+1)ħ/(2Mω) and w = 2n+1, the null gives ω₁/ω₀ = 2w_D/w_S — **always rational** — while
ε ∝ ω² and ε₁/ε₀ = 2 needs **ω₁/ω₀ = √2**. A ratio of integers is never √2.

> **The property that kills it is the property it was praised for.** Integers that cannot drift also
> cannot drift onto √2.

Checked two ways: an exhaustive scan (90,601 pairs, best miss 8.75 ppm) and exact rational arithmetic
over 4×10⁶ pairs. **And the earlier diagnosis was too kind** — the recorded (n_S, n_D) = (1, 0) forces
ω₁/ω₀ = 1 exactly, so degeneracy isn't a rescue condition, it is what the lock already asserts, giving
**Q = 1**. Both freeze branches fail differently: adiabatic can't reach √2; diabatic freezes the
amplitudes so R_c/M_c = 1 at *every* ratio and the null goes vacuous. The approximate escape needs
**696 and 492 quanta** — a fit, not a lock.

**What survives is a clean division with nothing in both classes:**

| class | reaches ε₁/ε₀ = 2? | can be exact? |
|---|---|---|
| occupancy laws (counts) | **no** — only rational ω₁/ω₀ | yes |
| equipartition (T per dof) | **yes** — null reads 2/ε₁ = 1/ε₀ | **no** — 171× over budget |

Equipartition reaches the target because **ε ∝ ω² absorbs the irrationality** and √2 never has to be
produced by a count. So the debt is re-pointed rather than erased — find a law with that same
frequency dependence *and* exactness, or establish no third class exists.

---

## 3c. And that question has an answer: the whole arc reduces to one condition

`scripts/delivery_law_third_class.py`, 21 controls, three anti-control blocks. For a harmonic mode
⟨x²⟩ = e/ε, so the null 2·e(ε₁)/ε₁ = e(ε₀)/ε₀ together with Q = ⅔'s ε₁/ε₀ = 2 makes **the 2s cancel**:

> ### e(2ε₀) = e(ε₀)

**That is the entire requirement** — the law must be *flat across a factor √2 in frequency*. Every
earlier result is downstream: among power laws only p = 0 is flat (re-deriving §3's uniqueness verdict
from something simpler), and integer occupancies cannot be flattened at all (§3b).

**Thermal equilibrium turns out not to be an arbitrary choice — it is the best flat law there is.**
e = kT + (ħω)²/(12kT): the **linear term in ω is absent**, equilibrium cancels it. A driven law
depositing E₀ per mode is equally flat *in its deposit* but still carries the mode's own zero point,
erring at **first** order — 34,517 quanta needed against thermal's 58, a factor **591**. That reframes
the contradiction rather than softening it: equilibrium was already the best available answer, which is
exactly why its being 171× over budget hurts.

**But an exact law must be non-monotonic**, since g(x) rises strictly and g(√2·x) = g(x) has no
finite-x solution. Two exact routes exist, each costing one number:

1. **A deposition spectrum symmetric in log ω, centred on the geometric mean** ω_p = √(ω₀ω₁) = 2^(¼)ω₀.
   Exact **at any width** — the condition fixes *where* the spectrum sits, not how broad — so it is a
   symmetry statement, not a fine-tuning. Anti-controls confirm no other peak location works and that
   the peak moves with ω₀ at fixed ratio, genuinely tying the spectrum to the ring.
2. **A two-temperature freeze**, exact at T_D/T_S = 0.997936 — a 0.206% split.

**The number, and the search.** Route 1 needs a peak at **33.094 keV**. Nothing in the corpus sits
there, and more decisively **the corpus records no deposition spectrum of any kind** — so route 1 is a
*construction*, not a lookup. Route 2 is a free parameter wearing a mechanism's clothes; nothing else
in the corpus would feel it.

### 3d. And the corpus's own named route fails on sign

T6 had recorded Kibble–Zurek as the way out — *"a textbook mechanism the model already claims"* — and
left the prescription unapplied. `scripts/kibble_zurek_delivery_law.py` (15 controls) applies it.
With ε_i = c_i·λ(t), λ ∝ t^m and τ ∝ ε^(−a), freezing at τ_i(t) = t gives ε_i(t_i) ∝ c_i^(1/(1+am)),
so the null reads **(c_D/c_S)^(1/(1+am)) = 2**.

> **The sign is wrong for every ordering transition.** c_D/c_S = ½ is *below* 1 and the target is
> *above* it, so the exponent must be negative — m < 0 at any damping. Scanned over a ∈ [0.1, 10] and
> m ∈ [0.1, 100], every stiffening quench lands below 1 and puts Q above 1. Reaching the null needs a
> **softening** ramp at a tuned exponent (am = −2).

Two more things fall out. The no-ramp limit am = 0 returns exactly ½ — the recorded "doublet gets
half" law, Q = 5/3 — so KZ *parametrises the existing rows by a quench exponent* rather than adding a
mechanism. And at am = −2 the sectors still freeze at frequencies differing by √2, so the quantum
correction still fails to cancel: **1025.4 ppm**, the identical number the thermal reading gives. KZ
does not touch the thing the arc is blocked on.

**One real gain survives.** Under KZ a mode's stiffness *at freeze* (setting the frozen amplitude)
differs from its stiffness *at observation* (which the mass formula reads) — the (s, p) family assumed
one ε, KZ supplies two. That is a candidate identity for §3's unexplained **third stiffness pair**.

> **Where the arc ends.** The delivery-law question is now completely characterised, its residue is
> **one unsupplied number**, and three named routes are closed — the occupancy lock by impossibility,
> the deposition peak by absence, Kibble–Zurek by sign (docket #88). One lead stays live: the
> freeze-time stiffness pair. **Q = ⅔ itself is untouched — it is measured.** What is now precisely
> known to be missing is its *derivation* from a ring condensate, and "precisely" is the gain: this
> began the day as "four laws and nothing selects among them."

---

## 4. #55 — C8 turned from a hope into a bracket

Since u = |x| and u² = x², **c_w is just the second Taylor coefficient of the response at zero** —
making this a classification rather than a search:

| response | c_w | ensemble [−1.36, −0.32] |
|---|---|---|
| `tanh u`, `u/√(1+u²)` — **odd** | 0 | outside |
| `ln(1+u)`, `1 − e^(−u)` | −½ | inside |
| `u·e^(−u)`, `u/(1+u)` | −1 | inside |
| `u/(1+2u)` | −2 | outside |

**The odd family's failure is structural.** An odd function has no even Taylor terms at *any* order,
so the two forms tried could never have produced a c_w — **and no other odd form can either. That
class is closed permanently.** For F(u) = u/(1+au), c_w = −a exactly, so the ensemble maps onto a
**saturation scale a ∈ [0.32, 1.36]**, with a = ½ and a = 1 both inside. The anti-control earns its
keep: the band rejects **both endpoints of C8's own [−2,0] bracket**, so the wider bracket was the
weaker statement.

---

## 5. #81 — a debt dissolved, and a fork found against a pre-registered prediction

**π/12 is not an independent angle.** With √m_k = a[1 + A cos(φ + 2πk/3)], the middle root vanishes
at cos(φ + 2π/3) = −1/A; at A = √2 that gives **φ_cross = 3π/4 − 2π/3 = π/12 exactly** (1.7×10⁻¹⁶).
So π/12 is fixed by A alone, and A is fixed by Koide via A² = 6(Q − ⅓) — *the same invariant* that
fixes 2/9. My earlier "a pure geometric angle carrying no Q, so a different **kind** of object supplies
it" is withdrawn. A = √2 is the **unique** amplitude producing π/12.

**It also explains the sign branch instead of assuming it:** below the crossing all roots are positive
(charged sector at 2/9, middle root only +0.040); above it the middle root is negative (neutral at
2/9 + π/12, −0.196). The (−,+,+) branch is where one *lands*.

> **⚠ AND THE FORK.** The Σm_ν = 58.5 meV recorded in the earlier session **contradicts P-2026-012**,
> which pre-registers m₁ = 2.3 meV. Solving for both splittings *and* a target m₁: the Koide branch
> gives m₁ = 0.374 meV, Σ = 58.5 meV, Q_ν = ⅔; forcing m₁ = 2.25 meV requires **A = 1.735 (+22.7%)**
> and Q_ν = 0.835 — off the cone. **Alternative hypotheses, not complements.** The Σm_ν figure is
> conditional on the Koide branch and must not be quoted as *the* model's prediction while
> P-2026-012 stands. Owner call; the branches differ 3.8% in Σm_ν, within near-term reach.

---

## 6. Debts isolated rather than paid — and why that is the honest outcome

**#13 — tasks 4 and 5 answered, and they were desk-doable.** A w = −1 component contributes
**exactly zero** to ρ + p, so the vacuum's *sign is irrelevant*: ρ + p = (4/3)ρ_r > 0 always, Ḣ < 0
always, **no bounce** from negative vacuum + radiation at any epoch or ratio. Not a near-miss — the
term is identically absent. H = 0 *is* reachable, but crossing it with Ḣ < 0 is a **turnaround**. The
missing object is a **negative-energy stiff component** (w = +1, ρ < 0): (1+w)ρ = 2ρ < 0, and a⁻⁶
scaling makes it dominant exactly at maximum compression. Both qualifiers load-bearing —
*positive* stiff doesn't flip the sign, negative **matter** does but never dominates.

**#39 — ω_J isolated.** The quartet closes (j = 6.03 meV, Γ_φ/θ̇ = 9.03×10⁷, R = 5.05×10⁻⁵), but
**three of four members are independently derived and ω_J is not** — it is back-derived from the
measured η. A forward route needs the junction phase's decay constant *and* pinning curvature; the
corpus states neither. I declined to assume v_L is the decay constant and solve for the rest, because
that manufactures a derivation from an unstated identification.

**#62 — narrowed to one question.** The averaging is *forced*: pointwise Θ (sd = 0.25 in 3D) would
scatter m_e by ~~**25% within a single absorber**~~ — **see the correction below** — and 10⁹ cells
gives 7.9×10⁻⁶. And **the scale is the model's own** — the condensate's de Broglie length from the
recorded m = 2.24×10⁻²⁰ eV is 0.86/0.43/0.29 pc at 100/200/300 km/s. So the debt is *not* "average
over what scale". What remains is only **why** the coupling averages. The obvious route — a mediator
setting the smoothing — needs ~6×10⁻²⁴ eV, four orders below the condensate mass, so it does not fit.

> **⚠ CORRECTED LATER THE SAME DAY** (`scripts/theta_averaging_forced.py`, 10 controls). The **25% is
> Θ's scatter quoted as m_e's** — off by a factor 80. Θ is a 0-to-1 indicator and the shift it drives
> is ε·Θ, so sd(Θ) = 0.25 induces sd(δm_e/m_e) = ε × 0.25 = **3.14×10⁻³**, i.e. 0.31% of m_e. (It is
> 50% of the *mean shift*, which is the nearest true statement.) Two further corrections to the
> framing: **⟨Θ⟩ = ½ and sd = 0.25 are not new** — they are the Beta(d/2, d/2) law the corpus already
> records, re-derived here as mean ½ and sd = 1/(2√(d+1)). And *"why the coupling averages"* is not an
> open mechanism question: the observable **is** an average, since an absorption line forms across the
> whole column. **The real residual is a check, not a mechanism** — the scatter that averages away in
> the line *centroid* must appear as excess line *width*, and that is externally falsifiable.
> Quantitatively the averaging is forced by 4–5 orders, and the recorded 10⁹ cells is within **2%** of
> exactly what a 10⁻⁷ μ-bound requires.

**#75 — debt 2's arithmetic verified, on the same b_Y = 41/6 as #51.** The whole chain reproduces
(42.888 → 42.9; 55.512 → 55.5; 104.91 → 104.9; 23.44%, 76.56%, 56.4%), and it **pins a convention the
docket never stated**: the *full* Planck mass, since the reduced one gives 57.3. Verifying that 55.5
is correctly computed says nothing about why hypercharge should close to zero — that remains
preon-class, so this label is correct.

**#69 — sharpened, one candidate excluded.** The class *is* named (Affleck–Dine, graded "door") and
supplies all three Sakharov conditions by construction. The missing object is **one thing**: a second
un-rotatable phase from a roll-up-era term — with one tilt and a uniform prior the coin is *exactly*
fair. And the family sector's arg b is **excluded** as its source: the reflection there acts on family
labels, not spacetime CP, and decisively **the spectrum is real for every arg b**, so arg b is a shape
parameter, not a phase surviving into observables.

**#59 — three objects mapped.** Object 3 is #39's ω_J; object 1 is #69's territory and gated *upstream*
of it; **object 2 (amplitude-follows-current) is the only one with no other home.**

---

## 7. What the controls caught, in my own new work

Four specifications failed their own controls today and were fixed before anything relied on them: a
bisection with the monotonic direction inverted (**twice** — φ_cross and the Y-junction charge, both
caught by the same class of anti-control), a c_w label asserting the recorded 3.2 fitted q²/2 when it
does not, and **four audit checks I added to #39 that turned out to be three duplicates plus a
tautology** — protocol 46's own T1 pattern, committed by the person who wrote protocol 46 that
morning. Removing them took the count 1311 → **1307**, and the lower number is the honest one.

**And one result got past its controls and had to be withdrawn afterwards** (§3). The #85 script's
controls were all *internal* — they checked that the family reproduced the four numbers, that the
exponents were distinct, that it could not fit arbitrary targets. Every one passed. None of them
asked **whether ε meant what I was computing**, and no internal control can: the definition lives in
a different script. It surfaced only on going back to `koide_frame_bridge.py` to read the four laws
at their source.

> **The lesson, and it is not the same as the others.** Anti-controls test whether a *check* could
> fail. They cannot test whether the *quantity* is the right one — that needs reading the symbol's
> definition where it is set, not where it is used. Protocol 42 exists precisely for this, and I
> committed the error in the session that wrote it up. The one habit that would have caught it:
> **before fitting a recorded set of numbers, open the script that produced them.**

**And a third failure mode surfaced on the way out, which neither of the above catches.** Correcting
§3 meant restating two control counts, and both were wrong in my own prose — 17 written for 20, 15 for
17. Checking a third found 15 written for 27. Three in one day is a pattern, so it got an instrument:
`scripts/control_count_sweep.py` extracts every "N controls" claim in `docs/`, runs the script it
names, and compares. **First run: 18 claims, 6 wrong**, spanning the docs, the working logs and the
ledger — all six written the same day as the script they described.

> The cause is always the same motion: controls get **added** to a script after the prose describing
> it was written, and nobody re-counts. Only the over-stated ones are misleading — an under-stated
> count is merely stale — but a count is a claim about how hard a result was tested, and it is quoted
> to referees. Protocol **49**; all 18 now match.

**And a fourth failure mode, which is about the ledger rather than the physics.** Twice today I
recorded something as found when the corpus already held it. On **#2** I graded a live docket against
α_dark ≈ 3.2 and reported it "does not reproduce in any convention" — the value had been **retracted
eleven days earlier**, in the same file I was writing into. On **#13** I recorded the bounded-density
bounce lane as the route my earlier answer missed; the corpus names it in **three** places and had
already graded it *un-derived, named in the reconstruction, not stocked* — one of those three even
says *"searching the corpus does not turn up a completed derivation."* The search had been done, and
recorded, and I did not read it.

> **Protocol 50.** Deriving something correctly is not the same as finding it. A result reached by
> thinking is new *to you*; whether it is new *to the corpus* is a separate question with a one-grep
> answer. The two variants are distinct: a stale **input** (a number whose status changed) and a stale
> **priority claim** (a result the shelf already holds). Neither breaks the physics — in both cases
> the algebra was right. What breaks is the ledger, and a session reporting two discoveries when it
> made one correction and one re-derivation leaves the next reader with a wrong picture.

**Applied retroactively to the rest of the day, and it mostly holds.** Grepping each of the session's
other findings for prior art in the corpus: the delivery-law family, the √2-irrationality closure, the
flatness reduction e(2ε₀) = e(ε₀), the intensive/extensive reading of g = 10ε, and the DM/ε timing
degeneracy all come back clean — no prior statement. **Five of six survive; one did not, and it is
recorded as such** rather than quietly downgraded.

**Otherwise the pattern worth keeping:** every other error was caught by an anti-control asking
*could this check fail?* — not by re-reading the result.

---

## 8. After the sweep: six more dockets, and three of my own findings withdrawn

This section covers work done *after* §1–7 were written. The pattern that dominates it is not
discovery — it is **self-correction**, and the corrections are recorded as prominently as the results.

### 8a. Answered

**#82 — total vs average is intensive vs extensive** (`s8_total_vs_average.py`, 14 controls). With the
per-species contribution X = f̄·α_c = 6α/π, the two numbers are the same ten seats read two ways:
ε = (N−1)X/N is a **mean** over seats, g = (N−1)X is the **sum** — verified as an explicit sum of nine
seats carrying X plus one empty vacuum seat. ε is δm_e/m_e for *one* seat; g is a fluid conversion
rate over *all* of them; the ratio of an extensive quantity to its intensive partner is the system
size. **It predicts**: dg/dN = X against dε/dN = X/N², a factor **100**. Anti-controls kill
both-extensive (ratio 1), both-intensive (1) and swapped (1/10), and only N = 10 works over 2–40.

**#55 — C8's even part is a resummation, not an operator** (`cw_response_from_backreaction.py`,
15 controls; now spec **C16**). Take the bare response linear, F₀ = u, and let the medium back-react
in proportion to what it already carries: **F = F₀/(1+aF₀) = u/(1+au), c_w = −a exactly** — solved by
bisection, not quoted. So the even part is *generated by resumming the linear coupling*, and the band
becomes a band on back-reaction strength, a ∈ [0.32, 1.36]. It explains the odd-response failure
structurally (`tanh u` and `u/√(1+u²)` are not of resummed type — 33% error by u = 1.5) and predicts
**c₃ = c_w², c₄ = −|c_w|³** against a corpus that currently *assumes* a unit cubic. Still owed: the
**value** of a.

**#69 — "a second un-rotatable phase" is the wrong name for it** (`second_phase_counting.py`,
13 controls). A single term carries **zero** physical phases; same-power terms merge exactly into one
cosine. What is needed is a second term at a **different winding power**, and the invariant is
**I = n₂φ₁ − n₁φ₂**. The coin flip is a *reflection symmetry* θ → c − θ at c = −2φ/n (exact to
5×10⁻¹⁵, mean torque 3.5×10⁻¹⁷), and it survives two terms **iff I is a multiple of π** — tested both
ways. So the ask is now one testable quantity, gradeable against any candidate potential.

**#59 object 2 — obstructed, not pending** (`amplitude_follows_current_charges.py`, 10 controls, exact
rational charges). "Amplitude-follows-current" asks one field to carry lepton number (for the current
coupling) *and* couple linearly to the charged-lepton mass. **Every SM Yukawa conserves lepton
number** — L̄He_R, Q̄Hd_R, Q̄H̃u_R, L̄H̃ν_R all L = 0, each verified a hypercharge- and colour-singlet —
so an L-charged medium reaches only (LH)(LH) and ν_Rν_R, **both neutrino Majorana masses**. It can
make neutrino mass and cannot shift m_e. Escapes: quadratic (loses leptophilia, already known), two
fields (falsifies the claim), loop-level (the only live one). **Leptogenesis is untouched.**

**#78 — the paper's one physics item closed** (`dm_row_sigma_eps.py`, 9 controls). A constant ε is
**exactly degenerate** with the fitted dispersion measure: it rescales the delay's coefficient and
leaves its 1/ν² shape alone, so a timing model absorbs it completely — DM_fit = N_e/(1+ε), residuals
at machine precision, at every frequency coverage. So there is nothing to convert. The 20 μs bounds ε
*variation* (1.7×10⁻⁶ to 3.1×10⁻⁴, a span of 183×).

### 8b. Withdrawn or corrected — my own work, same day

| what | the error | status |
|---|---|---|
| **#2** Y-junction | graded against a value **retracted 11 days earlier**, using the superseded functional | §2 banner; docket is run-gated |
| **#13** bounce | presented as "the route I missed" — the corpus names it in **three** places and had already graded it un-derived | net effect on the docket **nil** |
| **#62** Θ scatter | quoted **Θ's** sd as **m_e's** — 25% for 3.14×10⁻³, off by **80×** | corrected; the averaging is still forced |
| C9 quadratic | 0.83% used the *cubic's* moment ratio; correct value **0.985%** | corrected in spec and ledger |

**#13's correction is the one that stings**, because the algebra was right and the *claim of novelty*
was wrong. **#62's** survives better than it reads: the averaging is forced by 4–5 orders, and the
recorded 10⁹ cells is within **2%** of exactly what a 10⁻⁷ μ-bound requires — with the residual now a
**check** (does the scatter show as excess line *width*?) rather than a missing mechanism.

### 8c. Two protocols came out of it

**48 — before fitting a recorded set of numbers, open the script that produced them.** Caught C9's
mis-booked quadratic; would have caught #85's first answer.

**50 — before recording a finding as NEW, search the shelf for it.** Two distinct failure modes: a
stale *input* (#2) and a stale *priority claim* (#13). Neither breaks the physics; both break the
ledger. Applied retroactively to the day's other findings — the delivery-law family, the √2 closure,
the flatness reduction, the intensive/extensive reading and the DM degeneracy all come back clean.
**Five of six survive; one did not.**

> **The honest scoreboard for §8.** Five dockets answered, three of my own findings withdrawn or
> materially corrected, two protocols added, and the audit carried from 1,312 to **1,374** checks with
> the control-count sweep catching me three further times — once **over**-stating. None of the five
> answers changes a physical claim of the model; all five change what is *owed*, and in every case
> the debt got smaller and more specific.
