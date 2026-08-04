# The S₈ Tension — the Second Fight, Fought With the Right Sign (2026-07-12)

> ## OPEN-MACHINE residual freeze — 2026-08-04
>
> **Status:** OPEN-MACHINE / **OPEN-BLOCKED** on conversion posterior + matched lensing.
>
> **Machine residual waiting:** `cmp_prtoe_conv_desi` unproduced (last write 2026-07-22; R−1=13.25; not live). Live trio (bbnfix pair + routeD) is **not** this instrument — stamp in `PRTOE_CHAIN_TABLES.md` (bookable **no**). Matched DES/KiDS lensing likelihood still owed before any tension-easing upgrade.
>
> **What unblocks:** owner restart of conv_desi → cobaya self-stop → GetDist of conv_g; then matched lensing likelihood campaign.
>
> **Forbidden claims:** published tension-easing win; quoting R−1=13.25 archive as posterior; interim g as constraint.

**Audience grade.** Companion to s8_growth. No published tension-easing claim until a matched lensing likelihood is run. Chains with conversion (routeD/conv_desi) are exploratory.


> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


> The recorded T4 thread, consolidated. **The conv_desi chain is not running and its posterior is
> unproduced** (corrected 2026-07-29; this line previously read "is refining the posterior now").
> The chain died twice, at initialisation on 07-16 and again on 07-22, and nothing of it survives on
> the box but a seed covariance — restarting it is an owner decision. The companion file had carried
> this correction since 2026-07-28; this one had not. Residual freeze reconfirmed **2026-08-04**.
> *Companion: the conversion-channel standalone, [PRTOE_s8_growth.md](PRTOE_s8_growth.md).*

## 0. The tension
The CMB predicts more late-time clustering (ΛCDM: S₈ ≈ 0.833) than weak lensing measures
(KiDS-1000/DES-Y3 centrals 0.76–0.78; the KiDS-Legacy joint consensus 0.814 ± 0.012).
Most H₀ solutions make S₈ worse — the two tensions pull opposite directions, and killing
both is the field's standing filter.

## 1. The model's mechanism (recorded, coded, fit)

*One route is closed: the screening gate's own energy deposition cannot supply this
suppression. In the limit where gas crosses the transition ballistically the implied entropy
floor is an order of magnitude above what groups show; in the limit where the medium re-phases
around the gas — the physical one — the deposition is a few tens of electron-volts per
particle, far too small to move small-scale power. The delivery therefore rests entirely on
the shed below, which is a pre-registered parameter rather than a derivation
([PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md), [PRTOE_entropy.md](exploratory/PRTOE_entropy.md)).*
The rotation-cancellation conversion: as the medium's twist relaxes, part of the dcdf
matter-component sheds into free-streaming dark radiation (dcdf_conv_g — a ramp,
x^n/(1+x^n), coded in background.h). The shed depletes late-time ρ_m → suppresses
late growth → lowers S₈ — while the background expansion barely moves (the w-mirage
checked and cleared at ~1%).

## 2. Where it lands (production numbers)
The minimizer picks g = 0.12 → **S₈ = 0.821**, and the production joint fit records
**0.823 — within 1σ of the KiDS-Legacy consensus (0.814 ± 0.012), holding the H₀ = 69.9
fit** — the rare right-sign pair. ΛCDM sits at S₈ ≈ 0.833 with H₀ = 68.2 — 1.6σ above the
consensus and wrong on H₀ too; the model's value is twice as close to the consensus as
ΛCDM's. (A matched lensing-likelihood fit — DES/KiDS proper, not the S₈ point — stays owed
before any tension-easing claim upgrades.) The conv_desi chain was to deliver the posterior —
**but it is not running, corrected 2026-07-28.** It holds a single chain file last written
**2026-07-22**, at R−1 = 13.25, which is nowhere near converged. *(That R−1 is a within-chain
split-R̂ — a single chain is split into four segments — so it is a real number but blind to
confinement in one basin; noted 2026-07-29 because elsewhere the corpus wrongly said a one-chain run
yields no statistic at all.)* Three runs are live on the box as of 2026-08-04 — the bbnfix pair
and route-D — and **none is conv_desi**. Live progress: lcdm R−1=**0.086466**@N=20409 (was 0.059 — **receding** 1.73× stop) / dyad R−1=**0.128943**@N=20302 /
routeD R−1≈103; all `converged:false` (see `PRTOE_CHAIN_TABLES.md`). This chain has now died twice (it was found dead at initialisation on
2026-07-16, relaunched, and stopped again), so **the S₈ posterior is not pending — it
is unproduced**, and restarting it is an owner decision. The
firewalled derivation candidate g = 10ε = 54α/π (the machines' table,
[PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md)) awaits its mechanism.

## 3. Kills
(i) conv_desi's posterior excluding the S₈-fixing g region while lensing holds low;
(ii) the shed violating N_eff bounds at CMB epochs (the ramp's timing is the protection —
auditable); (iii) future lensing converging up to the ΛCDM value (dissolves the tension and the
mechanism's purpose — a null, not a kill; KiDS-Legacy's 0.814 is a half-step in that
direction, and the model's 0.823 sits between the consensus and ΛCDM).

## Sources
KiDS/DES (via [Planck2018]-era compilations), internal: thread 4 (T4), the mirage
check, the conv machinery in background.h, the machines' table. Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## Why the shed coupling sees the total and the amplitude sees the average (2026-07-29)

`scripts/s8_total_vs_average.py`, 14 controls including three anti-controls. The closed form
g = 10ε = 54α/π was known to have the 10 equal to N, the roster size — nine charged species plus the
vacuum's own seat. What was open is why one quantity takes the sum and the other the average. **The
answer is dimensional.**

Writing the per-species contribution as X = f̄·α_c = 6α/π, the two numbers are the same ten seats read
two ways:

| | | |
|---|---|---|
| ε = (N−1)/N · X | the **mean** over seats | **intensive** |
| g = (N−1) · X | the same total, undivided | **extensive** |

Verified as an explicit sum rather than a formula: nine seats carrying X and one vacuum seat carrying
zero sum to g and average to ε. The census fraction 9/10 is a **probability** — the chance a seat
carries a charged species rather than the vacuum — so ε is an expectation value and g the ensemble
total. The ratio between an extensive quantity and its intensive partner is the **system size**, which
is why it is N.

**Why each is what it is.** ε is δm_e/m_e — a property of *one* electron, hence of one seat, which
cannot count seats it does not occupy. g is a conversion **rate** for the fluid (`dcdf_conv_g`, the DM
component shedding into the floor), an aggregate property of the whole ensemble that counts every
contributor.

> **And the reading predicts rather than relabels.** The two respond to a roster change by
> dg/dN = X against dε/dN = X/N², a factor **N² = 100**: adding a species adds its full contribution
> to g, but adds only a share to ε *while diluting the average*.

**The anti-controls do real work.** Both-extensive or both-intensive would give ratio 1; the roles
swapped give 1/10. The observed factor 10 excludes all three outright. And the split is not a free
fit — scanned over roster sizes 2 to 40, **only N = 10** reproduces it, and 10 is the recorded census.

**What remains owed is smaller than what was owed.** Not the total-versus-average question, which is
settled. The unclosed item is the one the docket carried from the start: g = 54α/π is a derivation
*candidate*, firewalled from the fit and agreeing with the minimiser's g ≈ 0.12 at 4.53%. This
explains the **factor** relating it to ε; it does not promote the closed form, which still awaits its
mechanism through ε.

---

## Claims ledger & discipline (2026-08-04 residual freeze) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Right-sign S₈+H₀ pair: S₈≈0.823 with H₀=69.9 (point) | **machine-backed** provisional | §2 production numbers | Matched lensing owed |
| 2 | Screening-gate energy deposition cannot supply S₈ suppression | **failed** (route closed) | §1; Failures; entropy | Delivery rests on shed |
| 3 | g = 10ε = 54α/π is firewalled derivation *candidate* | **OPEN** / candidate | §2; s8_total_vs_average | Factor settled; mechanism through ε open |
| 4 | Total-vs-average (g extensive, ε intensive) at N=10 | **machine-backed** | `s8_total_vs_average.py` | Does not promote closed form |
| 5 | conv_desi posterior unproduced | **OPEN-BLOCKED** | freeze 2026-08-04; R−1=13.25 | **OPEN-MACHINE:** owner restart; not live |
| 6 | Kills: conv excludes easing g; N_eff violation; lensing rises to ΛCDM | **registered** | §3 | Null if tension dissolves |

**Non-claims / forbidden:** not published tension-easing; routeD/conv_desi exploratory; no archive posterior quotes.

**Triage:** elevate-in-place. Physics ceiling: right-sign point + factor math; posterior **OPEN-BLOCKED** (2026-08-04).
