# Owner queue — decisions the desk cannot make for itself

Live list. Each item names what is blocked, what the arithmetic says, and what a ruling would
unblock. Full workings are in `_AUDIT_LEDGER.md` under the dated entry named in each row. Items
are removed when ruled, not when acted on.

---

## 1. The two production chains are serial on a 12-thread box — 4 ranks would quarter the wait

**Raised 2026-07-28; the diagnosis was corrected the same day and this is the corrected version.**

`cmp_lcdm_mnu_bbnfix` sits at R−1 = 3.24 after 2,890 accepted samples and needs **7.5×10⁴ on the
fitted exponent, 9.7×10⁶ on the asymptotic** to reach `Rminus1_stop = 0.05` — against
`max_samples = 40000`, which it reaches in **83 days** at current throughput. The cap binds first
either way. `dyad_mnu_bbnfix` is the marginal case at R−1 = 1.055.

**The earlier reading of *why* was wrong.** I reported "the box has one core" from `nproc` = 1.
`nproc` honours `OMP_NUM_THREADS`, which is 1 here; the machine is an **i7-9850H, 6 cores / 12
threads**, every process has the full `fff` affinity mask, and `top` showed **41.6% idle**. The
chains are slow because each CLASS+likelihood call costs ~10.5 s, not because they are fighting for
a core — there have been ~9 idle threads beside them throughout.

**Both are single-chain** (one `.1.txt` each) despite launching as MPI singletons, so the reported
R−1 is a within-chain split statistic rather than the between-chain Gelman–Rubin the 0.05 target
assumes.

**Running real MPI ranks fixes both problems at once:**

| ranks per chain | cmp_lcdm to cap | dyad to cap | R−1 |
|---|---|---|---|
| 1 (now) | 83 d | 92 d | within-chain split |
| 2 | 42 d | 46 d | **between-chain** |
| 4 | **21 d** | **23 d** | **between-chain** |
| 6 | 14 d | 15 d | between-chain |

Keep ranks × OMP ≲ 12 and leave headroom for the M6 job.

**The ruling:** relaunch under MPI at 4 ranks (recommended — quarters the wall clock and buys a
real convergence statistic), or leave them serial and accept the cap. Relaunching costs the current
samples unless resumed, and the memory's standing hazard applies — check the `classy` .so mtime
against the launch date before any resume. Tool: `scripts/chain_convergence_forecast.py`.

**Related, same host:** `bounce_m6_rebound_dst.py` (another session) had produced no output for
7.4 hours, and the coarse pass it is refining **failed its own energy gate on every row** — 24%,
119%, 217%, 391% against a declared 2% tolerance, all four already marked unquotable. On the
corrected picture it is not starving anything; it is simply producing unusable output.

**STATUS 2026-07-28, 13:35 — the 3-rank relaunch is healthy, and an alarm about it was withdrawn
before it reached this page.** Both chains run 3 MPI ranks at ~101% CPU. Rank 0 on each was still in
burn-in until ~13:30, which is why only `.2.txt`/`.3.txt` existed — cobaya writes a rank's file after
its burn-in completes — and why the `.progress` files carried headers with no rows: no convergence
check runs until every rank is past burn-in. Both are now clearing it.

The cumulative acceptance the logs report reads **0.207% against 5.434% before the relaunch**, a 26×
collapse that would have argued for reverting to serial. **That reading is wrong and the number is
an artifact.** Cobaya's counter is cumulative since launch, so the fresh start's climb to the peak
sits permanently in the denominator. Differencing consecutive rows per rank gives the *current*
rate:

| | current (incremental) | pre-relaunch |
|---|---|---|
| cmp_lcdm, rank 2 | 5.6 / 15.4 / 7.7 / 11.1 % | 5.434% |
| dyad, rank 1 | steady **6–7%** across 18 intervals | 5.606% |

So acceptance is **at or above** what the serial runs had, and the seed covmat is confirmed loaded
(*"All parameters' covariance loaded from given covmat"*). **No action needed; the ranks ruling
stands on its original grounds.** Recorded as audit check 27c — a cumulative average is not the
current rate.

---

## 2. Task #21's deciding chain has been dead eight days, on its third failure

**Raised 2026-07-28.** `cmp_prtoe_routeD` stopped 2026-07-20 21:39 with **363 accepted samples
from 11,508 steps** and a progress file containing only its header — **no convergence statistic
has ever been computed** for it. Two earlier attempts are archived beside it, one collapsed at
6,937 rows and one a diagonal-seed retry; all three stalled inside a single day.

P-2026-056's pre-hoc standing is untouched. Its timetable is not: on current hardware a converged
Route-D posterior is months away, not weeks.

**The ruling:** relaunch as-is, re-tune the proposal, move it to other hardware, or accept that
#21 stays open indefinitely and say so in the registry.

---

## 3. RESOLVED 2026-07-28 — the band's provenance is found, and it cannot grade anything

**Raised and closed the same day, on the owner's instruction to find the derivation or toss the
prediction.** The earlier sweep searched the working tree and not the history. It is in the
history: commit **a48b2a1e, 2026-07-11 20:25**, registering P-2026-040 — *"registered while the
zon chain's center is still watch-only and the indirect band [0.0205, 0.0214] sits 2.3% BELOW the
claim"*.

So the band is a posterior interval from `cmp_prtoe_zon`. Its last convergence row before the
reading, at 20:03 that evening, was **R−1 = 93.1** against the chain's own `Rminus1_stop = 0.05` —
a factor **1,862**. It wrote one further row at R−1 = 40.4 and stopped. Its successor
`cmp_prtoe_zon_disp` reached 11.9 and was archived as collapsed. Neither is running.

**The prediction is not tossed, because the entry never claimed more than it had.** Betting a value
against an instrument that has not reported is pre-registration in its strongest form, and
P-2026-040 says so in those words. **What is tossed is the band's standing as a constraint** — an
interval read at R−1 = 93 is the spread of a chain that has not found the distribution, and is
typically far too narrow rather than too wide.

**This corrects three of my own results.** "d = 3 is excluded at every scale", the three-way
conflict on d, and the reading that the α_c convergence pointed at §6f horn (b) all counted the
band as a constraint and none survives. With it withdrawn the picture is *simpler and better*:
theory (d = 3) and the observed floor (d = 2.993) agree to 0.22%, and the lone outlier is the
hierarchy anchor at 2.921, which is §6f's already-named exposure rather than a new one.

Corrected in `PRTOE_hierarchy_problem.md` §6g, `PRTOE_quantum_trio.md`, the registry's instrument
note, and the harness (checks relabelled from constraints to positions).

**Remaining owner call:** whether P-2026-040 should stay registered while its only instrument is a
chain that has never converged and is not running — i.e. whether an un-gradeable pre-registration
keeps its place in the registry or moves to a parked register until an instrument exists.

---

## 3b. z_on (task #23) is queued correctly, but the queue does not clear for three months

**Raised 2026-07-28, on the owner's question.** The queueing discipline is already built and
already right: `scripts/launch_zon_identity_rerun.sh` **refuses to start while either bbnfix chain
is alive**, and it records the `classy` .so mtime and git HEAD into the launchlog so the physics
provenance is unambiguous. Nothing needs adding to make it queue properly.

**The problem is when the queue clears.** At measured throughput the pair reaches its own
`max_samples = 40000` cap in **83 and 92 days**, so the launcher unblocks in about **three
months** — and then the z_on chain starts from zero on the same one-core box. Adding it *now*
instead pushes the pair to 111 and 123 days, buying nothing: three unconverged chains instead of
two.

**And the instrument may be wrong for the job.** What #23 feeds is the zero-parameter evidence
exposure, carried as **Laplace-from-MCMC** — which needs a well-located mode and a local curvature,
not a converged posterior. Per check 24 that is a *point plus a Hessian*, and no chain in this tree
has ever produced a defensible width anyway. `scripts/zon_bobyqa_frozen.py` already finds that mode
by BOBYQA over the six compensating dimensions, and at ~66 s per likelihood it costs **6–30 hours**
on the contended core depending on the eval budget — against three months of waiting followed by
months of sampling.

**The ruling, three options:**

1. **Leave it queued as built.** Correct, self-enforcing, and nothing happens for three months.
2. **Run the optimizer instead, now.** Gets the identity-configuration mode and χ² floor in under a
   day, which is what the Laplace ΔlnZ actually consumes. Costs the production pair ~25% throughput
   while it runs. This is the recommendation.
3. **Both** — optimizer now for the point, MCMC still queued for a width nobody can currently
   defend.

Nothing has been launched: adding a CPU-bound job to a saturated core is the owner's call, and the
standing instruction is that the current pair finishes because it rides the latest C build.

---

## 4. ~~The junction quartet misses closure by nine~~ — **DISSOLVED 2026-07-28, no ruling needed**

> **RESOLVED before it reached the owner. The quartet closes; there is no factor-9 discrepancy and
> #39's 5.7 keV target is correct.** The item below is kept as raised, then answered.
>
> **The overdamping ratio is 9.03×10⁷, not 10⁷.** Computed from its own sourced inputs:
> Γ_φ = G_F²T⁵ = 5.3902×10⁹ eV at T_sph = 131.7 GeV (control: reproduces the recorded 5.4×10⁹), and
> θ̇ = 59.68 eV, giving **Γ_φ/θ̇ = 9.0319×10⁷**. The transfer-integral spec records this correctly —
> *"overdamped by 9×10⁷"* — and the summary below compressed it to an order of magnitude. **The
> missing 9.03 is exactly that compression**, which is why the shortfall came out at 9.03 rather
> than some incommensurate number.
>
> With the computed ratio all four numbers agree simultaneously:
> **ω_J = 5.7 keV → j = 6.03 meV** (recorded ~6) **→ R = 5.05×10⁻⁵** (needed ~5×10⁻⁵). Inverting,
> the need requires ω_J = **5.672 keV**, which is **0.5%** from the stated target.
>
> **The 1.90 keV alternative must NOT be adopted** — it is what you get by imposing the *rounded*
> ratio, and a derivation landing there would be **8.9× short** of the transmission the reservoir
> needs. #39 should be graded against 5.7 keV after all.
>
> Verified: `scripts/junction_quartet_closure.py`. This is protocol entry **40**'s failure mode for
> the second time in one day — a factor inferred from a quantity quoted to one figure, then
> attributed to physics. The entry below even names the mechanism ("all three inputs are quoted to
> one significant figure") and still filed it as an open ruling instead of computing the ratio.

**Raised 2026-07-28.** Baryogenesis records ω_J ≈ 5.7 keV, j = ω_J²/Γ_φ ≈ 6 meV, Γ_φ/θ̇ ≈ 10⁷ and
a needed R ≈ 5×10⁻⁵. Substituting Γ_φ collapses R to j/(2θ̇), so ω_J cancels out of R and the four
numbers constrain three unknowns. Any three predict the fourth wrong — R short by 9.03, or ω_J low
by 3.004, or the ratio high by 9.03, or j high by 3.004. All three inputs are quoted to one
significant figure with a tilde, and moving any one closes the system.

**#39's target is stated as "derive ω_J, needs ≈5.7 keV".** On the recorded j and ratio the
internally consistent value is **1.90 keV**, so a derivation landing there would read as a 3× miss
while actually closing the transmission. The pre-committed kill at two orders is untouched either
way.

**The ruling:** which of ω_J, j or Γ_φ/θ̇ moves. Until then #39 should not be graded against
5.7 keV.

---

## 5. ω_J denotes two unrelated quantities in five live files

**Raised 2026-07-28.** The **Jeans** frequency √(4πGρ) = √(3/2)·H_Λ in `PRTOE_sqrt3_derivation.md`,
`PRTOE_coincidence_problem.md` and `PRTOE_PREREGISTERED_PREDICTIONS.md`; the **junction** plasma
frequency in `PRTOE_baryogenesis.md` and the failures ledger. Both own the subscript honestly, the
values sit ~36 orders apart, and nothing is numerically at risk — a reader meeting both is.

**The ruling:** which sense keeps ω_J. Same category as the de-jargon pass's naming collisions.

**A second collision, and this one has already cost real work (added 2026-07-28).** The pair
(a, b) denotes two different decompositions of the *same* family-ring operator:

| convention | form | the graph's values |
|---|---|---|
| T6's stiffness pair | H = ½Σ[**a**·f_k² + **b**·(f_k − f_{k+1})²] — on-site, bond | **a = b** = g |
| the circulant pair | H = **a**·I + **b**·P + **b**\*·P² — diagonal, hopping | a = 3g, **b = −g** |

Both are live, both are standard, and they disagree on the value of "a/b" for one matrix — 1 versus
−3. This is not hypothetical: the null was carried for a day as "a = 3b", a statement true only in
the first convention and only under the thermal delivery law. **The ruling:** either rename one pair
(the circulant hopping to t, say, which is the usual letter for it), or require every quotation of
a and b to name its convention inline. The second is cheaper and weaker; the first is what audit
check 29 would recommend.

---

## 6. The toroidal fork's energy gate looks unsatisfiable by construction (2026-07-28)

`scripts/ring_toroidal_3d.py` is running (task #42, ~15.4 h, one core at nice 19, first execution
that has survived past its opening frames). It is producing readings: a ring is detected from
t = 1.00 with shape helicity **helA = −1** and core-circuit winding **W = −1.19**.

**The problem is its third gate.** The header's quotability gates are (i) a ring detected in ≥14 of
16 azimuthal bins, (ii) the n = ±1 pair behaving as a parity pair, and (iii) **energy drift ≤ 2% per
run**. Observed drift is 16.1% at t = 1.00 and 19.2% at t = 1.25, climbing steadily, against a run
that goes to t = 8.

That is not a numerical failure — it is the sponge doing its job. The integrator carries an explicit
dissipative term, `psi -= 0.4·dt·SPONGE·(n−1)·psi`, whose purpose is to absorb the directed
fountain's radiation at the box edge, and the energy functional integrates the whole box. **An
absorbing boundary and an energy-conservation gate cannot both be satisfied**; the 2% figure appears
to have been written for a closed system.

**The decision.** Gate (iii) as written will fail, and under "quotable only if all pass" that would
bury a result whose actual content — the parity behaviour of helA across n = ±1 — is a *relative*
comparison that a common dissipation does not corrupt. Three options:

- **(a)** re-scope gate (iii) to the physical region inside the sponge, which is what it was meant to
  measure, and grade the run on that;
- **(b)** keep gate (iii) literal, bury the run, and re-register the experiment with a conserving
  boundary — expensive, and the sponge exists because a periodic box without it is worse;
- **(c)** grade the parity test on its own and record the drift beside it, unquoted.

**Recommendation: (a).** It is the only one that keeps the pre-registration honest without
discarding a result for failing a condition its own instrument design forbids. This should be ruled
**before** the n = −1 half completes, so the ruling cannot be accused of following the answer.

**MEASURED, not argued (`scripts/toroidal_energy_gate_diagnostic.py`).** The recommendation above
was an argument, and the corpus has buried a run on this exact bar before — the adaptive spherical
rebound (bounce_reconstruction_rp §23) failed it at 22–1817% and was correctly recorded as
"numerically unresolved by this method at this resolution." So re-scoping needs evidence that this
case differs in *cause*, not merely in sympathy. The two candidate causes are separable by one
experiment: same initial condition, sponge on versus sponge off.

| configuration | drift over 200 steps | per step |
|---|---|---|
| sponge **ON** (as run) | **3.8341%** | 0.019170% |
| sponge **OFF** | **0.0003%** | 0.000002% |

A ratio of **12,705×**. With the absorbing term removed the integrator conserves energy to four
significant figures; switching it on reproduces the drift. **The 2% bar is measuring the sponge, not
the numerics.** It cannot be met by any run using an absorbing boundary, and this instrument uses one
by design — a periodic box without it reflects the fountain's radiation back onto the ring being
measured.

That is a different situation from the spherical run, where the energy error was the integrator
failing with no dissipative term to blame. Same symptom, different cause, and the distinguishing
measurement is above. **Recommendation (a) stands and is now evidenced.** Note also that the fork's
actual content — the parity of helA across n = ±1 — is a *relative* comparison from which a common
dissipation cancels, so it survives either ruling.

## Not a decision, but the owner should see it

**The d conflict (2026-07-28).** d is defined once as the spatial dimension and used twice —
α_c = d·α and ρ_Λ¼ = (d²/2)α⁴T_c — and the spine ties them explicitly. Three constraints bear on
that single quantity and do not meet: the indirect band gives d ∈ [2.809, 2.933], the hierarchy
anchor 2.921, the observed dark-energy density 2.993, and the geometry 3. The escape of separating
the two d's is **closed algebraically** — the floor's d² is α_c²/α², so the two forms are one form.
Two branches survive, both empirical, and item 3 above is the tractable one.

**A registrable prediction, offered rather than filed (2026-07-28).** The democratic construction for
the null fixes the family ring's *neutral* mode frequency, not only Q: the spectrum ε₀ = a,
ε_charged = 4a gives ω₀ = ω₁/2, so with the recorded ω₁ = (2/9)T_c = 39.355 keV,

> **ω₀ = (1/9)·T_c = 19.677 keV.**

The corpus carries no independent ω₀ — every occurrence traces to this session — so nothing tests it
today, and it is the cheapest single number that could kill the mechanism. **Whether this earns a
P-number is the owner's call, not mine**; registering a prediction is a commitment, and this one
descends from a candidate resting on one structural and one dynamical claim rather than from a
banked result. Recorded here so
the option is visible and the number is not quietly lost. It sits in T6's log with the mechanism's
three other consequences (the uniform mode is bound rather than flat; no null for any neutral
triple, ever; and N = 3 uniquely, so a fourth generation breaks the null rather than merely
extending it).

---

## Standing re-check list — the four absences

Owner instruction 2026-07-28: these may become derivable once other things are derived, so each
new result gets tested against them. What each is waiting on:

| absence | what would unlock it |
|---|---|
| the α_c band's provenance | any α_c reading that skips the ε-assembly — the dispersion chain, the isocurvature phase speed, or a converged α_c chain |
| ~~the portal roster's doublet count~~ | **RESOLVED 2026-07-28** — the count is zero; `scripts/portal_roster_doublet_count.py`. S counts electroweak-*charged* states, and each property the portal species are asked for (Higgs-coupled, leptophilic, m_H at one loop) is met by a gauge singlet at the right size — n_S·λ = 1 returns 125.25 GeV from the 4π anchor. The census counts SM charged fermions and never ranged over these states. Carried forward as a design rule: the portal may not acquire more than two electroweak doublets. |
| f̄'s averaging window | **NARROWED 2026-07-28 to evidence grade** — `scripts/fbar_window_discriminator.py`. The accumulated reading (N = 3.82×10⁵ turns ⇒ f̄ = 2/π to 8×10⁻⁵%) predicts 2/π; the instantaneous reading makes f̄ a frozen \|cos θ\| with a 48% spread. The fit-implied f̄ = 0.6253 sits 1.78% from 2/π, which a frozen phase reaches with probability 1.87% — **54 : 1 for the accumulated reading**, read as modest given look-elsewhere. *The winding-sim's 0.25% is NOT usable — it simulates the premise under test.* Consequence: the α_c conflict stands at its full 2.08% and nothing about f̄ is available to relieve it. Still owed: the operator form (integral over the winding epoch vs value at recombination) |
| ~~why Q = 2/3~~ | **CANDIDATE MECHANISM 2026-07-28** — the medium as a fourth node: `koide_democratic_graph_null.py`, `koide_equal_quanta_from_adiabaticity.py`, `koide_pour_before_split.py`. Democratic K₄ + equal quanta gives a = b, ε ratio 4, Q = 2/3 exactly, and selects N = 3 uniquely via (N−1)² = N+1; passes the charge filter unprompted. Reduced to one structural question — the assembly order (task #1). |

**First hit.** The charge-weighted selection (§6c) supplies the selector the μ₅ residue needed,
and it is electric charge rather than the Z₃ — which means it breaks the family symmetry, exactly
as DERIVATION_HUNT's obstruction says any selector must. The new step is that the obstruction is
**scale-conditional**: 3q = 0 needs the seats to be one orbit *at the shell*, 17.5 orders above
where the Koide node lives. An **emergent** Z₃ — exact in the infrared, broken in the ultraviolet —
is the only realisation letting both hold, and it commits to the Koide relation being approximate.
It is, at 0.17 ppm in Q. Candidate, not an account: no spurion is exhibited and the obvious scales
miss the residual by 32× and 10¹⁴×.

**And it is untestable inside the sector.** Its one further prediction — an electron-localised
breaking — does not bite: the two natural spurion forms rank the seats oppositely (additively the
τ carries most, relatively the electron does at +28.8 ppm), which is arithmetic rather than
evidence, since the electron's seat ratio is 0.0403 against the τ's 2.379. Three masses with one
fitted scale leave two residuals, exactly the freedom A and φ already use. **A fourth mass
governed by the same node is what would give it a handle**, and there is none: the neutrino triple
cannot be on the node for *any* lightest mass, Q_ν topping out at 0.585 against 2/3 — short by
12.2%. The reading is untestable inside the corpus's structure, which is its status rather than a
step toward one.

> **⚠ QUALIFIED 2026-07-29, and this one may reopen rather than close.** The 0.585 ceiling assumes
> all three square roots POSITIVE — Q = Σm ⁄ (Σ√m)² depends on those signs, and the ring form
> generates a negative root whenever 2|b| > a, with only m = (√m)² observable. On the **(−,+,+)
> branch Q_ν crosses 2/3 at m₁ ≈ 0.00040 eV** (`scripts/neutrino_Q_sign_branch.py`, which reproduces
> the 0.585 ceiling exactly as a control). **So the "there is none" may be wrong**: Brannen's
> φ = 2/9 + π/12 fit reproduces the measured Δm²₃₁/Δm²₂₁ to 0.5% on precisely that branch, predicts
> m₁ = 0.000374 eV — agreeing with the branch's own crossing — and pins **Σm_ν = 0.0585 eV**. If the
> negative branch is admissible, the fourth handle this passage says does not exist would exist, and
> it would be a testable number rather than an untestable reading. **Whether that branch is
> physically admissible is the open question, and it is now the one worth owner attention.** Note the
> *second* leg below (charge² weighting makes a neutral cone worth zero) is untouched by any of this
> — as this passage already says, the two arguments do not use each other.

**The return is elsewhere.** The same neutrino failure confirms the selector from a second
direction: T6 concludes from it that the cone acts in the charged sector specifically, and the
basement reaches the same place because screening weights by charge² so a neutrino cone is worth
zero. Two sectors, two arguments, neither using the other — **electric charge is the selector on
both**.

## The radio-lattice paper: one sentence, and one item that closed itself (2026-07-29)

`scripts/dm_row_sigma_eps.py`, 9 controls. Two things for the owner, one of which needs no decision.

**No decision needed — item 1 of "what is still genuinely owed" is closed.** The readiness note read
*"σ_ε in physical units … needs the DM timing-model conversion. This is the one piece of physics still
missing."* It is not missing. **A universal constant ε is exactly degenerate with the fitted dispersion
measure**: it rescales the delay's coefficient and leaves its 1/ν² shape untouched, so a timing model
absorbs it completely — DM_fit = (∫n_e dl)/(1+ε), t_∞ unchanged, residuals at machine precision, at
every frequency coverage tested. So there is nothing to convert, and the 20 μs figure bounds ε
*variation* (1.7×10⁻⁶ to 3.1×10⁻⁴ depending on band and column, a span of 183×), not ε. Full working
in `_ARXIV_READINESS.md`.

> ### ✅ RULED 2026-07-29 — demote the row, and hold the paper back
>
> **Owner ruling: demote.** Applied — the ranking sentence is replaced by the degeneracy statement,
> the dispersion row joins the two already set aside as failing Eq. (ML)'s presumption "not as a
> matter of precision but of kind", and the measurable set drops from three rows to two
> (**σ_ε = σ/√8 ≈ 0.35σ**; σ/√11 retained as an upper bound, not a forecast). Rebuilt clean: 0 errors,
> 0 undefined, 6 pp. **And the paper is now marked NOT arXiv-ready** until an independent
> electron-column determination promotes the row back. Full record in `_ARXIV_READINESS.md`.
>
> *Original decision text retained below for provenance.*
>
> ### ⚠ DECISION NEEDED — one sentence in `papers/radio-lattice/main.tex`
>
> *"The dispersion-measure row is statistically the strongest."*
>
> Both numbers in that paragraph are correct and reproduce exactly. But they are the precision of the
> **DM measurement**, and by the degeneracy above that precision **does not transfer to ε** — a better
> DM measurement gives a better DM_fit and says nothing about the shift. The paper already declines to
> fold the 10⁻⁷ into a forecast, so the caution is there; the ranking claim is what a referee
> following the degeneracy would stop on.
>
> **The minimal repair is one clause** — that the row's strength lies in DM precision, while its
> sensitivity to ε is set by the independent column determination, which is what the paper's own next
> sentence already says. **I have not edited it.** It is an authorship call in your paper, and the
> alternatives (leave it, qualify it, or demote the row's ranking) differ in what they concede.
>
> Note the two **line** rows are unaffected: a shifted rest frequency is an irreducible apparent
> redshift against the fixed laboratory value, at weight +2 for 21 cm and +1 for the RRL (ratio
> exactly 2, checked). The degeneracy is specific to the reconstructed-quantity rows.

## A pre-registered prediction's tag may need changing (2026-07-29)

**P-020 carries `[OBJECT-PENDING on: … amplitude-follows-current …]`, and that object is now
obstructed rather than pending.** `scripts/amplitude_follows_current_charges.py`, 10 controls, exact
rational charge arithmetic; full working in the failures ledger and annotated at the prediction.

The claim asks one field to carry lepton number (so its phase couples to the lepton current, which is
what drives the asymmetry) *and* to couple linearly to an operator containing the charged-lepton mass.
Those are incompatible: **every Standard Model Yukawa conserves lepton number**, so an L-charged field
can only reach (LH)(LH) and ν_Rν_R — both ΔL = 2, both neutrino Majorana masses. It can make neutrino
mass; it cannot shift m_e.

> **I have annotated the prediction but not rewritten it.** Changing a pre-registration's status tag
> is your call, not mine. The three options differ in what they concede:
>
> 1. **Leave `OBJECT-PENDING`** and rely on the annotation. Cheapest; but the tag then overstates how
>   open the object is, and a referee who does the charge arithmetic will notice.
> 2. **Change to `OBJECT-OBSTRUCTED`** for that one item, keeping the other two pending. Most accurate
>   to what is now known.
> 3. **Change to `OBJECT-PENDING (loop route only)`** — escape (c) survives, so this is defensible and
>   is the narrowest honest statement, but it commits to a mechanism nobody has estimated.
>
> **Nothing about the leptogenesis side changes** under any of the three, and leptophilia is still
> carried by data exactly as P-020 already says. What changes is only how open the *drag* to δm_e is
> allowed to look.

## Both dead chains are UNRESUMABLE — classy was rebuilt after they last wrote (2026-07-29)

Found while checking whether conv_desi could be restarted into a freed core. It cannot be *resumed*,
and neither can the other dead chain. The timeline is unambiguous:

| | |
|---|---|
| `cmp_prtoe_conv_desi` last write | **2026-07-22 14:25** |
| `cmp_prtoe_zon` last write | **2026-07-22 14:27** |
| `libclass.a` rebuilt | **2026-07-23 18:48** |
| `classy` py3.12 module rebuilt | **2026-07-23 20:00** |

The standing chain-ops rule is that a classy rebuild changes physics under a resume. Both dead chains
predate the rebuild, so resuming either would splice samples from two different physics builds into
one posterior. **They must be restarted from scratch, losing their burn-in and their learned
covariances.** The 3.2 MB conv_desi chain and its R−1 = 13.25 are not a head start; they are a
different theory's samples.

> **The three live runs are unaffected and self-consistent** — all three started 2026-07-28, after the
> rebuild. Nothing running needs to be touched.

### Consequence for the "one more core" offer

Measured per-core load, 6 s sample: cores 1–8 are at **91–100%**; core 0 is at **41.9%**; cores 9, 10
and 11 are at **18.1%, 31.9%, 18.1%** — which is the TV and desktop, not idle capacity. So the picture
is not "9 busy cores and 3 spare"; it is **~0.6 cores of genuine slack on core 0, inside the range
already permitted**, plus whatever can be taken from the owner's own cores.

**But cores are not the binding constraint.** conv_desi needs a *fresh* multi-day run through burn-in,
not a resume. Starting one on ~1.4 cores of leftovers — while contending with the TV on core 9 —
would take weeks and invites a fourth death on a chain that has already died three times.

> **Recommendation: do not launch on the extra core.** The honest move is to wait for one of the three
> live runs to finish and give conv_desi real cores. The extra core does not change the answer,
> because the cost was never one core — it was a full restart. **The TV reservation stays intact.**

## DECISION: which Θ regime does unvirialized gas occupy? (raised 2026-07-29)

**Why it is yours and not mine.** It is a model question about the coupling's own state, and both
answers are internally consistent — they just are not the same prediction.

**The collision.** P-2026-050 takes **Θ = 1** in unvirialized gas. The coupling's framework in
`PRTOE_me_mechanism_math.md` names **two** states — laminar Θ = 1.9×10⁻⁶ and developed speckle at
**⟨Θ⟩ = ½**, described there as *"a distributional fact, not something the model arranges"* — and
**contains no Θ = 1 state at all.** Θ = 1 is the upper endpoint of the Beta(d/2,d/2) support, not its
mean, and a dark-ages or cosmic-dawn signal is a volume average.

| | Θ = 1 (as registered) | ⟨Θ⟩ = ½ (the Beta law) |
|---|---|---|
| rest-frequency offset | +2.509% | **+1.254%** |
| dark-ages trough offset | **+0.40 MHz** | **+0.20 MHz** |
| cosmic-dawn trough offset | +1.96 MHz | +0.98 MHz |
| discriminant at ±0.1 MHz | **4.1σ** | **2.0σ** |

Exactly a factor of 2, no residual. **The entry's arithmetic is correct at Θ = 1** — every registered
figure reproduces to three decimals — so this is not an algebra error, it is an unstated choice of
regime, and the kill threshold inherits it.

**Already done without waiting for you:** the false uniqueness claim in kill (ii) is withdrawn, since
it read *"the mechanism's own arithmetic allows no other number"* and the mechanism's own arithmetic
allows exactly one other. The entry now presents the fork.

**The two ways out.**
1. **Unvirialized gas is a third, fully coherent regime (Θ = 1).** Then the framework must add that
   state and say *why voids are coherent where the same field is speckled elsewhere.* The registered
   numbers stand as they are.
2. **Unvirialized gas is developed speckle (⟨Θ⟩ = ½).** Then the registered offsets and the kill
   threshold both halve, and the entry's advertised 4σ discriminant is really 2σ at the same
   instrument. Note this branch also carries docket #62's 0.101 MHz broadening.

Instrument: `scripts/theta_regime_fork_21cm.py`, 15 controls including three anti-controls, all pass.
