# Hubble tension — mechanism, residual, calibration

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Amplitude: [PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md). Risk: [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md). Chains: [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).

> ## Residual freeze — 2026-08-10 (old-BAO Stage B + DESI Stage A; nested still open)
>
> **Document job:** COMPLETE-CONDITIONAL — mechanism, owned residual, ladder ceiling, and
> literature scoreboard are written. **Booked H₀ exists on two stacks; decisive nested evidence does not.**
>
> **Old-BAO pair — BOOKED Stage A + Stage B** (authority
> `bbnfix_booking_20260808_005626/REPORT.md` · Grok red `RED_AUDIT.md` · living
> [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md)):
>
> | leg | N | R−1 | t | converged |
> |---|---:|---:|---|---|
> | `dyad_mnu_bbnfix` | 37605 | **0.048118** | 2026-08-07T04:08:52 | **true** |
> | `cmp_lcdm_mnu_bbnfix` | 26294 | **0.049324** | 2026-08-05T11:52:10 | **true** |
>
> Three-rank GetDist (`ignore_rows=0.3`, SH0ES-conditional): dyad **H₀ = 70.052 ± 0.716**,
> `m_ncdm = 0.0671 ± 0.0583`, **S₈ = 0.821 ± 0.0097**; lcdm **H₀ = 68.345 ± 0.343**,
> `m_ncdm = 0.0192 ± 0.0174`, **S₈ = 0.824 ± 0.0081**. Triangles: `docs/plots/*_bbnfix_triangle.png`.
>
> **Evidence honesty (old-BAO):** sample-cov Laplace **ΔlnZ ≈ +0.21** (cond(Σ)~10⁸). Historical
> **ΔlnZ ≈ +2.6** is pre-bbnfix only. Hessian v2 finite but soft-mode diagnostic (not nested).
>
> **DESI-DR2 pair — BOOKED Stage A (separate instrument; do not mix)** — authority
> `desidr2_bbnfix_booking_20260810_053127` · peel `docs/chains/*_desidr2.*` · Grok red for citation:
>
> | leg | N | R−1 | converged | H₀ (GetDist 30% burn) |
> |---|---:|---:|---|---|
> | `dyad_mnu_bbnfix_desidr2` | 53482 | **0.03321** | **true** | **70.30 ± 0.54** |
> | `cmp_lcdm_mnu_bbnfix_desidr2` | 52031 | **0.041377** | **true** | **68.73 ± 0.25** |
>
> DESI sample-cov Laplace **ΔlnZ ≈ +1.31** (still soft modes; not nested). Nested referee: UltraNest + PolyChord live on SH0ES, TRGB, and noH0. LCDM UltraNest one-legs are **finished**; dyad legs are not. **No nested ΔlnZ yet.**
>
> **What remains open:** nested-quality comparison on DESI-DR2; do **not** use intermediate log(Z)
> or MAP peeks as evidence.
>
> **Forbidden claims:** decisive win from Laplace; mixing old-BAO with DESI posteriors; historical +2.6
> as current authority; inventing nested verdict.

**Status.** Core empirical claim of the program — built against data, not extended to it after the
fact. Two SH0ES-conditional dual-gate pairs are **booked** (old-BAO Stage B published; DESI Stage A
with peel). On both stacks the dyad sits ~1.6–1.7 above the matched ΛCDM+m_ν twin in H₀, but
evidence is only soft-mode Laplace (old-BAO **+0.21** / DESI **+1.31**), not nested. Gold
PolyChord is the open referee. **Do not lead with a win.**

---

## 1. The tension

SH0ES (Cepheid-calibrated SNe): H₀ = 73.0 ± 1.0 km/s/Mpc. ΛCDM + CMB: ~67–68.2. Disagreement ≳ 5σ, durable under scrutiny on both ends.

## 2. Mechanism

One addition to known physics: early-universe electron-mass shift ε = 1.2543% (= 27α/5π when the stack holds), screened off late. Heavier early m_e → earlier recombination → smaller sound horizon → CMB fit prefers higher H₀ (varying-m_e degeneracy: Hart–Chluba 2020; Sekiguchi–Takahashi 2021). Origin here: condensate order parameter at T_c = 177.10 keV; inactive for early BBN stages at production grade.

**Stack grade:** conditional (c counting assumption, f̄ derived, α_c = 3α bet). Fixed-ε configs test the hard case (no free m_e knob).

## 3. Where it lands

**Pre-bbnfix standing production claims** (not live-pair posteriors; see residual freeze):

| | value | note |
|---|---|---|
| ΛCDM (same pipeline) | H₀ ≈ 68.2 | baseline |
| Model (fixed ε) | H₀ ≈ **69.9** | ~half the SH0ES gap; **pre-bbnfix** |
| Ladder reach ceiling (audit) | **~70.9–71.3** | cannot reach 73 |
| Evidence | ΔlnZ ≈ **+2.6** (Laplace) | **pre-bbnfix**; marginal; SH0ES-conditional; no nested confirmer; **not bookable** as the BBN-fixed pair result until gate |

- Residual **owned**: model refuses the rest of the gap (curvature escape declined by fit).
- Exhaustive lever audit (SN standardization 162 templates — sign **opposite** to tension; geometry leakage; reionization) → ladder account capped ~70.9–71.3.
- **Live BBN-fixed pairs (booked):** quote H₀ / Σm_ν / S₈ only from booking receipts / Stage B
  [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md). Do **not** mix old-BAO with DESI-DR2. Do **not**
  quote nested ΔlnZ until gold PolyChord finishes.

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
| **This model** | 69.9 fixed ε; ceiling ~71 *(pre-bbnfix CosmicForge; not chain-booked)* | **0** extra vs ΛCDM | — |

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

---

## Claims ledger & discipline (2026-08-05 residual freeze) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | ε at recombination lifts H₀ relative to ΛCDM | **machine-backed** | production fit; old-BAO booking receipt; CLASS | Historical fixed-ε ~69.9 line remains pre-bbnfix; current booked old-BAO dyad is **70.052 ± 0.716**; DESI-DR2 Stage A booked; nested twins still open |
| 2 | Ladder ceiling ~70.9–71.3; cannot reach 73 | **machine-backed** | H0_CEILING; ς = −1 | Residual tension owned |
| 3 | Evidence remains marginal | **machine-backed** current + historical | booked old-BAO sample-cov Laplace; earlier MCMC Laplace | **OPEN-NESTED:** current booked pair is only **ΔlnZ ≈ +0.21**; historical **+2.6** remains pre-bbnfix; nested launched, no twin ΔlnZ |
| 4 | ε stack c·f̄·α_c conditional | **complete-conditional** | THE_AMPLITUDE | α_c instrument STOPPED, INCONCLUSIVE |
| 5 | EDE better residual tension (~2.5σ vs ~4.25σ class) | **interpretation** (literature scoreboard) | Schöneberg 2026 table | Model cheaper/falsifiable, not better-fitting; desk fairness paid (T11) |
| 6 | SN candle term pushes ladder *down* (ς = −1) | **machine-backed** | 162-template scan | Real-SN synthetic photometry appeal open |
| 7 | Kill: same ε on all messengers; DESI w; radio locks; He adverse | **registered** | §6 kill list | — |
| 8 | Current-stack nested-quality H₀ / model−ΛCDM evidence sentence | **OPEN-BLOCKED** | residual freeze 2026-08-08 | **OPEN-NESTED:** DESI-DR2 Stage A booked; nested launched, dyad unfinished, no twin ΔlnZ |

**Non-claims / forbidden:** not a closed H₀ win; not full SH0ES account; not nested-confirmed
evidence; no live DESI-DR2 peek numbers as letter results; historical **+2.6** is not the current
booked verdict.

**Triage:** elevate-in-place. Physics ceiling: mechanism production-grade; booked old-BAO receipt in
hand, but current-stack evidence still **OPEN-NESTED** and DESI-DR2 Stage A booked; **OPEN-NESTED**.
