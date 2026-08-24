# The S₈ Tension and Growth — the Conversion Channel (2026-07-11)

> **Status.** Conversion MCMC retune **STOPPED** (`cmp_prtoe_conv_desi_retune`, R−1=0.0447, `converged: true`). GetDist: `dcdf_conv_g` **inconclusive** (0.080±0.072). Matched DES/KiDS lensing likelihood still **OPEN-BLOCKED**.
>
> Route-D thaw is **finished** Stage A (separate instrument; not a substitute for conv_desi). Nested / zon instruments do not book this channel.
>
> **Do not claim:** published tension-easing win; archive R−1 as a posterior; interim g as a constraint.


**Audience grade.** Mechanism note only — no matched DES/KiDS lensing fit yet; do not quote S₈ as a measured win. Conversion perts now coded when `dcdf_conv_g>0` (routeD); headline chains have conversion off.


> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Thread 4 of the atom-grammar survey; the standalone for the recorded DM→(DE/dark-radiation)
conversion lead — the consolidated production file is
[PRTOE_s8_tension.md](PRTOE_s8_tension.md). The mechanism is built into CLASS; conv_g is a sampled
parameter in the thaw and conv_desi *configurations*. The conv_desi **retune stopped 2026-08-24**;
`g` is **inconclusive** (not demanded). Jul-22 deaths are historical. Still not a KiDS shear test.*

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
- conv_g on the stopped retune: **0.080 ± 0.072** (68% [0.015, 0.146]); 44% of samples g<0.05.
 Registered 0.10 is inside 68%. **Inconclusive — lever not on.** Authority:
 `working_logs/_runs/conv_desi_retune_grade_20260824/`. Derived S₈ = 0.816 ± 0.009 (KiDS-Legacy
 *number* 0.814±0.012) is not a shear fit.
- Meaning-inversion note (kept): a conv_g pulled large would ease S₈ at the price
 of the thaw/w(z) commitments — the model cannot spend this dial freely; DESI polices it.

## 3. The improvement, bounded

ΛCDM: S₈ tension = hope-it's-systematics. This model: a built, recorded, pre-registered,
one-parameter mechanism with its own police (the w = −1 commitment) — falsifiable in both
directions (conv_g posterior consistent with 0 ⇒ no help, the tension is not ours to ease;
conv_g large but DESI kills the implied w(z) ⇒ the mechanism dies honorably). Either outcome
is information; ΛCDM's position provides none.

## 4. Owed

**`conv_desi` retune STOPPED** (2026-08-24). Dual gate met. `g` inconclusive; derived S₈ ~0.816 is a
point match to KiDS-Legacy, not lensing data. Jul-22 R−1=13.25 archive is **not** this run.
Still owed: a matched-lensing-likelihood fit (DES/KiDS proper, not the S₈ point) before any
tension-easing claim.

*The conversion MCMC exists. It did not turn the lever on. Lensing is still the remaining growth test.*

---

## Claims ledger & discipline (2026-08-04 residual freeze) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Conversion channel can ease late growth (mechanism) | **derived-from-recorded** / coded | CLASS dcdf_conv_*; §1 | DESI polices w(z) |
| 2 | Production joint S₈ ≈ 0.823 (point, not matched lensing) | **machine-backed** provisional | §2 | Not a published tension win |
| 3 | conv_desi retune posterior | **STOPPED** / `g` **INCONCLUSIVE** | `conv_desi_retune_grade_20260824` | Not a tension win; routeD is a separate Stage A thaw |
| 4 | Matched DES/KiDS lensing likelihood | **OPEN-BLOCKED** | §4 owed | Required before tension-easing claim |
| 5 | conv_g pre-registered ~0.10±0.05 | **registered**; posterior **inconclusive** | configs + GetDist | 0.10 inside 68%; lever not demanded |

**Non-claims / forbidden:** not a measured S₈ win; no archive-row posterior quotes; do not treat derived S₈ vs KiDS-Legacy as a shear fit.

**Triage:** elevate-in-place. Physics ceiling: mechanism coded; MCMC **stopped**; `g` inconclusive; lensing still owed.
