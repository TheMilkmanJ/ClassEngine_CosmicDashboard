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

## 3. P-2026-040 is graded against a number with no recorded computation

**Raised 2026-07-28.** The indirect band **[0.0205, 0.0214]** on α_c exists nowhere in the
repository except as prose — four forward-facing citations and one ledger entry, all quoting, none
deriving. No chain samples α_c; the archived `alpha_scan` runs vary `varying_alpha`, the
fine-structure multiplier. The 2026-07-19 audit verified the transcription, never the source.

Nor is it the assembly inverted on the posterior: **ε ≈ 1.24% maps to α_c = 0.021642**, above the
band's top, the band corresponding to ε ∈ [1.175%, 1.226%]. The conversion is exact to a part in
ten million, so those two ε-side numbers genuinely differ by **1.13%**.

Which one is the instrument decides the bet's standing against the dark-energy floor: **0.93% on
the posterior, 2.08% on the band.**

**The ruling:** supply the band's provenance, or grade P-2026-040 against the ε posterior instead.

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
