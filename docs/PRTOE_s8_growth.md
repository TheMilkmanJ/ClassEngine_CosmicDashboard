# The S₈ Tension and Growth — the Conversion Channel (2026-07-11)

> ## OPEN-MACHINE residual freeze — 2026-08-04
>
> **Status:** OPEN-MACHINE / **OPEN-BLOCKED** on posteriors.
>
> **Machine residual waiting:** (1) `cmp_prtoe_conv_desi` **unproduced** (died twice; last chain write 2026-07-22; progress R−1 = 13.25; not live). (2) Matched DES/KiDS lensing likelihood before any tension-easing claim. (3) routeD thaw is **live** but early (progress N=1609, R−1≈102.8, `converged:false`) — not a substitute for conv_desi.
>
> **What unblocks:** owner restart of `conv_desi` (config/seed decision) → cobaya self-stop at yaml R−1 stop → GetDist booking of conv_g; separate lensing-likelihood campaign for published easing claim.
>
> **Forbidden claims:** measured S₈ win; quoting archive GetDist rows as posteriors; treating routeD early samples as the conversion test; interim conv_g as constraint.

**Audience grade.** Mechanism note only — no matched DES/KiDS lensing fit yet; do not quote S₈ as a measured win. Conversion perts now coded when `dcdf_conv_g>0` (routeD); headline chains have conversion off.


> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Thread 4 of the atom-grammar survey; the standalone for the recorded DM→(DE/dark-radiation)
conversion lead — the consolidated production file is
[PRTOE_s8_tension.md](PRTOE_s8_tension.md). The mechanism is built into CLASS; conv_g is a sampled
parameter in the thaw and conv_desi *configurations*, but those posteriors are **unproduced** (the
conv_desi chain died twice — see §4), not live tests: a one-parameter, physically motivated easing of
the growth tension that ΛCDM must treat as systematics.*

## 0. The tension

Weak-lensing surveys measure S₈ ≡ σ₈√(Ω_m/0.3) below the CMB's ΛCDM prediction: 2–3σ in the
KiDS-1000/DES-Y3 era (central values 0.76–0.78); the KiDS-Legacy joint consensus
(0.814 ± 0.012) has since softened that to a ~1.6σ lean under ΛCDM's 0.833. The direction
never flipped — the late universe reads smoother — and ΛCDM has no lever either way: the
growth history is locked once the CMB is fit.

## 1. The model's lever is not a lever — it is the fluid's own thermodynamics

The dCDF is one fluid whose phases exchange: the conversion channel (recorded, coded:
dcdf_conv_g/at/n) lets the DM component shed into the floor/dark-radiation at late times —
**the same physics as the cycle's pdV work** (the fluid does work against gravity through its own
equation of state; graded). Converting a percent-level
fraction of DM after z ~ 1 suppresses late growth (lower S₈) without touching the CMB-era
history — exactly the shape of the observed tension.

## 2. Where it stands empirically (live)

- The mechanism is built and recorded in the CLASS implementation, and it does not disturb the
 damping tail.
- The omk scan's minimum: S₈ = 0.807; the production joint fit: **S₈ = 0.823 — at the
 KiDS-Legacy consensus, vs ΛCDM's 0.833, at zero χ² cost** (the standing claim). Both
 readings sit on the tension's easing side.
- conv_g is a sampled parameter in the thaw and conv_desi *configurations*, pre-registered at
 g ≈ 0.10 ± 0.05. Their converged posteriors *would be* the mechanism's test once produced; none
 exist yet (§4), and no interim value carries weight.
- Meaning-inversion note (kept): a conv_g pulled large would ease S₈ at the price
 of the thaw/w(z) commitments — the model cannot spend this dial freely; DESI polices it.

## 3. The improvement, bounded

ΛCDM: S₈ tension = hope-it's-systematics. This model: a built, recorded, pre-registered,
one-parameter mechanism with its own police (the w = −1 commitment) — falsifiable in both
directions (conv_g posterior consistent with 0 ⇒ no help, the tension is not ours to ease;
conv_g large but DESI kills the implied w(z) ⇒ the mechanism dies honorably). Either outcome
is information; ΛCDM's position provides none.

## 4. Owed

The chains' converged posteriors — **not running, corrected 2026-07-28.** `conv_desi` holds a
single chain file last written **2026-07-22** at R−1 = 13.25. *(That figure is a within-chain
split-R̂ — one chain cut into four segments — so it is a genuine number, but one that cannot detect
confinement to a single basin; flagged 2026-07-29, since elsewhere the corpus wrongly stated a
one-chain run yields no statistic at all.)* Three runs are live on the box as of 2026-08-04 —
the bbnfix pair and route-D — and **none of them is conv_desi**. Live stamp (progress tails):
lcdm R−1=**0.086466**@N=20409 (was 0.059 — **receding** 1.73× stop) / dyad R−1=**0.128943**@N=20302 / routeD R−1≈103 — all `converged:false`; bookable **no**
(see `PRTOE_CHAIN_TABLES.md`). The chain has died twice (at initialisation on 07-16, then again on
07-22), so **this posterior is unproduced rather than pending** and restarting it is an owner
decision. Also owed: a matched-lensing-likelihood fit (DES/KiDS proper,
not just the S₈ point) before any tension-easing claim is recorded; the conversion's
perturbation-sector treatment.

*The universe got smoother than the standard picture allows. This model's dark sector does extra
work that does exactly that — and the chain that would test it has not yet been produced.*

---

## Claims ledger & discipline (2026-08-04 residual freeze) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Conversion channel can ease late growth (mechanism) | **derived-from-recorded** / coded | CLASS dcdf_conv_*; §1 | DESI polices w(z) |
| 2 | Production joint S₈ ≈ 0.823 (point, not matched lensing) | **machine-backed** provisional | §2 | Not a published tension win |
| 3 | conv_desi / thaw posteriors | **OPEN-BLOCKED** | §4; freeze 2026-08-04 | **OPEN-MACHINE:** conv_desi unproduced; routeD live but R−1≈103 |
| 4 | Matched DES/KiDS lensing likelihood | **OPEN-BLOCKED** | §4 owed | Required before tension-easing claim |
| 5 | conv_g pre-registered ~0.10±0.05 | **registered** | configs | No interim value carries weight |

**Non-claims / forbidden:** not a measured S₈ win; conversion off in headline chains; no archive-row posterior quotes.

**Triage:** elevate-in-place. Physics ceiling: mechanism coded; posteriors **OPEN-BLOCKED** (2026-08-04).
