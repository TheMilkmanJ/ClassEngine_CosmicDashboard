# Hubble tension — mechanism, residual, calibration

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Amplitude: [PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md). Risk: [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md).

**Status.** Core empirical claim of the program — built against data, not extended to it after the fact. Evidence number is **Laplace-from-MCMC** (ΔlnZ ≈ +2.6); nested sampling waits on cluster time. Chains must converge before the number is quotable as final. Live matched pairs have been a **wash** when multi-basin (see Risk §3c). **Do not lead with a win.**

---

## 1. The tension

SH0ES (Cepheid-calibrated SNe): H₀ = 73.0 ± 1.0 km/s/Mpc. ΛCDM + CMB: ~67–68.2. Disagreement ≳ 5σ, durable under scrutiny on both ends.

## 2. Mechanism

One addition to known physics: early-universe electron-mass shift ε = 1.2543% (= 27α/5π when the stack holds), screened off late. Heavier early m_e → earlier recombination → smaller sound horizon → CMB fit prefers higher H₀ (varying-m_e degeneracy: Hart–Chluba 2020; Sekiguchi–Takahashi 2021). Origin here: condensate order parameter at T_c = 177.10 keV; inactive for early BBN stages at production grade.

**Stack grade:** conditional (c counting assumption, f̄ derived, α_c = 3α bet). Fixed-ε configs test the hard case (no free m_e knob).

## 3. Where it lands

| | value | note |
|---|---|---|
| ΛCDM (same pipeline) | H₀ ≈ 68.2 | baseline |
| Model (fixed ε) | H₀ ≈ **69.9** | ~half the SH0ES gap |
| Ladder reach ceiling (audit) | **~70.9–71.3** | cannot reach 73 |
| Evidence | ΔlnZ ≈ **+2.6** (Laplace) | marginal; SH0ES-conditional; no nested confirmer |

- Residual **owned**: model refuses the rest of the gap (curvature escape declined by fit).
- Exhaustive lever audit (SN standardization 162 templates — sign **opposite** to tension; geometry leakage; reionization) → ladder account capped ~70.9–71.3.

## 4. Calibration question

If the model is right, Cepheid-calibrated 73 carries ~2–3 km/s/Mpc of systematics. Pre-registered band H₀ ∈ [69, 71] for TRGB; TRGB programs read ~69.8–70.4 [Freedman 2021] and later JWST mixes.

**Crowding referee (JWST):** Riess et al. 2024 — HST–JWST Cepheid distance difference −0.01 ± 0.03 mag; rejects unrecognised distance-dependent crowding at 8.2σ. Photometry is not the 73. Ladders still disagree: CCHP JWST-only TRGB/JAGB near ΛCDM; SH0ES near 73. Model sits on the TRGB side of an open ladder dispute.

**Model’s own SN candidate:** environmental screening → host-density standardization offset (~0.02 mag of observed 0.05–0.08 host-mass step at central values). Full-step corner fixes Lyman-α forest offset → DESI forest decides. No dataset dropped for disagreement; three evidence tiers (Cepheid / anchor-free / TRGB) declared before results.

## 5. Field scoreboard (not flattering)

Common-framework comparison [Schöneberg et al. 2026]: residual tension after early physics —

| model | −ΔAIC | residual Δ_DMAP | note |
|---|---|---|---|
| early dark energy | 23.40 | **~2.5σ** (newer stacks ~2σ) | best residual relief |
| **varying m_e** | 12.58 | **~4.25σ** | this mechanism class |
| ΔN_eff | 3.18 | ~5σ | eliminated |

**On residual tension, EDE is ahead.** A derived amplitude buys economy and falsifiability, not extra H₀ reach.

| | lands | cost | beats this model how |
|---|---|---|---|
| EDE | H₀ toward 70–73 with freedom | +3 params | higher ceiling |
| Free m_e literature | up to ~71+ with SNe / curvature | +1–2 | can re-fit amplitude |
| Ladder systematics | H₀ ~68–70 if 73 wrong | 0 new physics | cheapest |
| **This model** | 69.9 fixed ε; ceiling ~71 | **0** extra vs ΛCDM | — |

**Where this model is stronger:** zero extra parameters (if stack holds), one ε on all messengers, pre-registered kills. **Cheaper and more falsifiable — not better-fitting.**

**S₈:** EDE costs power spectrum; recombination-side m_e(z) also faces structural issues once DESI BAO is in (Lee–Zhou 2026). Neither side is clean.

**Independent m_e support:** Hart–Chluba ~3.5σ; ACT+DESI ~1.8σ. Model’s 1.012543 sits inside those posteriors; preference has shrunk as data improved.

## 6. Kill list (exposure, not fit quality)

1. Same 1.2543% must work on BBN, CMB, 21 cm, neutrinos.  
2. DESI w = −1 (or Route-D thaw) test.  
3. Atomic-ratio locks in radio.  
4. BBN helium remains **adverse** (+1.3 to +2.0σ vs Aver).  

## References

[Riess 2022]; [Freedman 2021, 2025]; [Planck 2018]; [Hart–Chluba 2020]; [Sekiguchi–Takahashi 2021]; [Schöneberg et al. 2026]; [Poulin et al. 2019, 2025]; [Hill et al. 2020]; [Toda–Seto]; [Lee–Zhou 2026]; [Riess et al. 2024]. Full: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md). Dead H₀ routes: [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md).
