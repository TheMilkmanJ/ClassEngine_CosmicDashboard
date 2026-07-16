# THE H₀ CEILING — how high the model can reach, and why the pipeline can't carry it yet (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*The task: compute the maximum ladder-H₀ the model can account for, show the
formula, and explain the pipeline gap honestly. Statuses per the house law.*

## 1. The adopted symbol: ς (final σ) — THE LAST SIGN

The candle channel's direction is the one number in this formula that does not yet
exist. It gets the Greek alphabet's famously unemployed letter: **ς ∈ {−1, 0, +1},
armed at 0**, computed by the synthetic-photometry session (the filter integrals of the
ε-compressed SED through m_B and color simultaneously). The final σ: the last sign
the model owes.

## 2. The formula

$$H_0^{\rm ladder} = H_0^{\rm global}\times\Big[1 + \varsigma\,\beta\,\delta c\,\langle g\rangle_{\rm flow}\,\tfrac{\ln 10}{5} + \Lambda_{\rm leak} + \mathcal{T}_\tau\Big]$$

| term | value | status |
|---|---|---|
| H₀^global | **69.9** | the model's CMB prediction (production fit; the zero-parameter run re-derives it) |
| ς | {−1, 0, +1}, **armed 0** | UNCOMPUTED — the sign session (the room's crux) |
| β·δc | 0.093 mag | the color channel (entry 68): Rydberg compression ε through SALT standardization |
| ⟨g⟩_flow | 0.3–1.0 | the flow-SNe mean gate value (the host census, unsized; calibrator side ≈ 0 — screened) |
| Λ_leak | +0.1–0.3% | the lookback-varying dipole leakage past SH0ES's constant template (entry 64); axis-geometry multiplier open (v4.1) |
| 𝒯_τ | 0–0.4% | the τ room (the unpaid 7→8 tether), either sign |

## 3. The computed bracket

| scenario | ladder reading the model accounts for |
|---|---|
| floor (ς=+1, ⟨g⟩=0.3, min leakage, no τ) | **70.9** |
| central (⟨g⟩=0.5) | **71.7** |
| **CEILING (ς=+1, ⟨g⟩=1, max leakage, +τ)** | **73.4** |

**Verdict: 73.0 is INSIDE the model's reach.** The gap between "can" and "does" is two
named computations: ς (the sign session) and ⟨g⟩ (the host-environment census against
the gate curve). ς = −1 inverts the candle term and the ceiling collapses to ~70.6 —
the formula is falsifiable in one computation.

## 4. Why PolyChord/CLASS cannot carry these parameters today (the honest gap)

- **CLASS is an isotropic, global Boltzmann code**: it evolves one homogeneous
 background and linear perturbations. The candle term is a PER-OBJECT, ENVIRONMENTAL
 correction (each supernova reads the gate curve at its host's clumping) — it lives in
 the SN standardization layer (the likelihood's data side), not in any background
 equation. No Boltzmann code hosts it; this is a category fact, not a missing feature.
- **ς does not exist yet**: injecting a guessed sign is a coin flip wearing an equation.
 The module ships ARMED-OFF (scripts/candle_room_correction.py) and flips the day the
 sign session signs.
- **The leakage and τ terms** are comparison-layer and reionization-history effects
 respectively — the first lives outside the likelihoods entirely, the second is an
 unrun computation (B-queue).
- **Nothing is lost**: the evidence run's chains can be IMPORTANCE-REWEIGHTED with the
 candle-corrected SN likelihood retroactively — tonight's run collects the data once;
 the ceiling cashes against it whenever ς arrives.

## 5. The one-sentence version

The model predicts 69.9 globally, and — through one gate curve it already owns, read by
candles in unscreened rooms — can account for a ladder reading anywhere up to 73.4; the
difference between reach and claim is one sign (ς) and one census (⟨g⟩), both named,
neither invented.

## Sources
Entries 64–68 (the derivation log); scripts/candle_room_correction.py, flow_ladder_correction.py;
[Riess2022] (the ladder), [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).


## UPDATE (2026-07-13, the sign session) — ς = −1 at estimate grade

The sign session ran (162-configuration template scan, lines-only compression):
**ς = −1, robust — the candle term pushes the ladder DOWN.** The ceiling above is
superseded: the reachable bracket collapses to **~70.9–71.3** (leakage + τ only), and
the ladder's 73 stands as genuine residual tension against the model. The room inverts:
its surviving claim is the SN HOST MASS STEP's direction and class as the gate curve's
fingerprint. Appeal path (narrow): the real-SN-template + real-filter synthetic
photometry; the module stays armed-off. Honesty note: the model does NOT currently
explain the full SH0ES reading — it predicts ~70–71 and owns the residual as tension.
