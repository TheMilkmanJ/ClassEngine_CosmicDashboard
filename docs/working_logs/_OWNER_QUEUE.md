# Owner queue — decisions the desk cannot make for itself

Live list. Each item names what is blocked, what the arithmetic says, and what a ruling would
unblock. Full workings are in `_AUDIT_LEDGER.md` under the dated entry named in each row. Items
are removed when ruled, not when acted on.

---

## 1. The two production chains cannot reach their own stopping rule

**Raised 2026-07-28.** `cmp_lcdm_mnu_bbnfix` sits at R−1 = 3.24 after 2,890 accepted samples. To
reach its own `Rminus1_stop = 0.05` it needs **7.5×10⁴ samples on the fitted exponent and 9.7×10⁶
on the asymptotic** — against `max_samples = 40000`, which it will not reach for **83 days**. The
cap binds first on either projection, so the run stops unconverged. `dyad_mnu_bbnfix` is the
marginal case at R−1 = 1.055.

Both are single-chain despite launching as MPI singletons, so the reported R−1 is a within-chain
split statistic rather than the between-chain Gelman–Rubin the 0.05 target assumes — which makes
the forecast optimistic. And `nproc` = 1: MPI buys nothing, and three CPU-bound jobs are dividing
one core at load 9.3.

**The ruling:** let them run to the cap and accept an unconverged posterior; re-tune the proposal
and restart; or move them to hardware with cores. Tool: `scripts/chain_convergence_forecast.py`.

**Related, same host:** `bounce_m6_rebound_dst.py` (another session) had produced no output for
7.4 hours while holding a full core, and the coarse pass it is refining **failed its own energy
gate on every row** — 24%, 119%, 217%, 391% against a declared 2% tolerance, all four already
marked unquotable.

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

## 4. The junction quartet misses closure by nine, and #39's target may be the wrong number

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

---

## Not a decision, but the owner should see it

**The d conflict (2026-07-28).** d is defined once as the spatial dimension and used twice —
α_c = d·α and ρ_Λ¼ = (d²/2)α⁴T_c — and the spine ties them explicitly. Three constraints bear on
that single quantity and do not meet: the indirect band gives d ∈ [2.809, 2.933], the hierarchy
anchor 2.921, the observed dark-energy density 2.993, and the geometry 3. The escape of separating
the two d's is **closed algebraically** — the floor's d² is α_c²/α², so the two forms are one form.
Two branches survive, both empirical, and item 3 above is the tractable one.

---

## Standing re-check list — the four absences

Owner instruction 2026-07-28: these may become derivable once other things are derived, so each
new result gets tested against them. What each is waiting on:

| absence | what would unlock it |
|---|---|
| the α_c band's provenance | any α_c reading that skips the ε-assembly — the dispersion chain, the isocurvature phase speed, or a converged α_c chain |
| the portal roster's doublet count | the census's portal species given electroweak representations; adjacent to #6 and #41 |
| f̄'s averaging window | the epoch at which ε acts — adjacent to #11, the genesis cascade |
| why Q = 2/3 | a mechanism making the Z₃-graded norm vanish; **fired 2026-07-28, see below** |

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

**The return is elsewhere.** The same neutrino failure confirms the selector from a second
direction: T6 concludes from it that the cone acts in the charged sector specifically, and the
basement reaches the same place because screening weights by charge² so a neutrino cone is worth
zero. Two sectors, two arguments, neither using the other — **electric charge is the selector on
both**.
