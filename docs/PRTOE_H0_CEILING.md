# THE H₀ CEILING — how high the model can reach, and why the pipeline can't carry it yet (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*The task: compute the maximum ladder-H₀ the model can account for, show the
formula, and explain the pipeline gap honestly. Statuses per the house law.*

## 1. The adopted symbol: ς (final σ) — THE LAST SIGN

The candle channel's direction is the one number in this formula that took longest to
pin down. It gets the Greek alphabet's famously unemployed letter: **ς ∈ {−1, 0, +1}**,
computed by the synthetic-photometry session (the filter integrals of the
ε-compressed SED through m_B and color simultaneously). The sign session (a
162-configuration template scan, lines-only compression) returned **ς = −1, robust —
the candle term pushes the ladder DOWN.** The final σ: the last sign the model owed,
now signed.

## 2. The formula

$$H_0^{\rm ladder} = H_0^{\rm global}\times\Big[1 + \varsigma\,\beta\,\delta c\,\langle g\rangle_{\rm flow}\,\tfrac{\ln 10}{5} + \Lambda_{\rm leak} + \mathcal{T}_\tau\Big]$$

| term | value | status |
|---|---|---|
| H₀^global | **69.9** | the model's CMB prediction (production fit; the zero-parameter run re-derives it) |
| ς | **−1** | signed — the sign session (162-configuration template scan) |
| β·δc | 0.093 mag | the color channel: Rydberg compression ε through SALT standardization |
| ⟨g⟩_flow | 0.3–1.0 | the flow-SNe mean gate value (the host census, unsized; calibrator side ≈ 0 — screened) |
| Λ_leak | +0.1–0.3% | the lookback-varying dipole leakage past SH0ES's constant template; axis-geometry multiplier open (v4.1) |
| 𝒯_τ | 0–0.4% | the τ room — since **reduced** (THE_CHAIN tether 7→8: the clustering half zero by construction, the atomic half gated by the edge closing before the ionizing era); the surviving contribution rides only the edge's low tail |

## 3. The computed bracket, with ς signed

With ς = −1 the candle term subtracts rather than adds, so it drops out of the
model's reach and the account is carried by leakage and τ alone:

| scenario | ladder reading the model accounts for |
|---|---|
| leakage only (Λ_leak min) | **70.9** — the working number, now that the τ room is reduced |
| leakage + the τ room's un-excluded maximum (the edge-tail loophole) | **71.3** |

**Verdict: the model's ladder reach tops out at ~70.9, with 71.3 the un-excluded ceiling.** SH0ES's 73.0 sits outside
the model's account and stands as genuine residual tension** — the room's surviving
claim is the SN host mass step's direction and class as the gate curve's fingerprint
(see [PRTOE_hubble_tension.md](PRTOE_hubble_tension.md) §4). Appeal path, narrow: the
real-SN-template + real-filter synthetic photometry; the module stays armed-off until
then. The model does not currently explain the full SH0ES reading — it predicts
~70–71 and owns the residual as tension.

## 4. Why PolyChord/CLASS cannot carry these parameters today (the honest gap)

- **CLASS is an isotropic, global Boltzmann code**: it evolves one homogeneous
 background and linear perturbations. The candle term is a PER-OBJECT, ENVIRONMENTAL
 correction (each supernova reads the gate curve at its host's clumping) — it lives in
 the SN standardization layer (the likelihood's data side), not in any background
 equation. No Boltzmann code hosts it; this is a category fact, not a missing feature.
- **ς is signed but not wired in**: the candle-corrected SN likelihood is not yet part
 of the joint fit — the sign session establishes the direction only, from a template
 scan, not the real-SN-template synthetic photometry the appeal path needs.
 The module ships ARMED-OFF (scripts/candle_room_correction.py).
- **The leakage and τ terms** are comparison-layer and reionization-history effects
 respectively — the first lives outside the likelihoods entirely; the second reduced by
 the chain's own structure and survives only through the edge's low tail
 ([PRTOE_THE_CHAIN.md](PRTOE_THE_CHAIN.md), tether 7→8).
- **Nothing is lost**: the evidence run's chains can be IMPORTANCE-REWEIGHTED with the
 candle-corrected SN likelihood retroactively — this run collects the data once;
 the ceiling cashes against it whenever the candle correction is wired in.

## 5. The one-sentence version

The model predicts 69.9 globally, and — through one gate curve it already owns, now
signed negative — accounts for a ladder reading up to ~70.9–71.3; the SH0ES 73.0
reading sits outside the model's reach and is owned as genuine residual tension, not
claimed.

## Sources
The derivation log; scripts/candle_room_correction.py, flow_ladder_correction.py;
[Riess2022] (the ladder), [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).
