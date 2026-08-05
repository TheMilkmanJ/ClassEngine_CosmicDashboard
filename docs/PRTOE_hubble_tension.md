# Hubble tension — mechanism, residual, calibration

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Amplitude: [PRTOE_THE_AMPLITUDE.md](PRTOE_THE_AMPLITUDE.md). Risk: [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md). Chains: [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).

> ## Residual freeze — 2026-08-05 (H₀ letter **NOT bookable** until bbnfix gate)
>
> **Document job:** COMPLETE-CONDITIONAL — mechanism, owned residual, ladder ceiling, and
> literature scoreboard are written. **Bookable H₀ / model−ΛCDM ΔlnZ from the live BBN-fixed
> pair: NO.**
>
> **Live pair (progress authority; booking refuse card `bbnfix_booking_20260805_170213`):**
>
> | leg | N | R−1 | t | converged |
> |---|---:|---:|---|---|
> | `dyad_mnu_bbnfix` | 24677 | **0.056889** (**1.14×** stop) | 2026-08-05T07:54:30 | **false** |
> | `cmp_lcdm_mnu_bbnfix` | 24858 | **0.047912** (below stop, no self-stop) | 2026-08-05T04:55:58 | **false** |
>
> Quote R−1 with N and timestamp. **NOT bookable**.
>
> **Gate:** both legs with progress R−1 **< 0.05** *and* checkpoint **`converged: true`**
> (self-stop). Booking entrypoint only:
> [`scripts/book_bbnfix_when_ready.py`](../scripts/book_bbnfix_when_ready.py)
> (`python3 scripts/book_bbnfix_when_ready.py`). Gate reconfirm → **REFUSED**. Offline GetDist
> GR / crude param R−1 peeks (`bbnfix_mcmc_watch_diag.py`) are **UNBOOKABLE** — never the
> authority.
>
> **Standing numbers in this letter** (H₀ ≈ 69.9 fixed-ε; Laplace ΔlnZ ≈ +2.6,
> SH0ES-conditional) are **pre-bbnfix** production claims. They are **not** results from the
> live pair and must not be silently replaced by unconverged peeks. Nested sampling remains
> offline (PolyChord not running; not started by residual freezes).
>
> **What unblocks a bookable H₀ sentence:** both bbnfix legs self-stop under the bar → run
> `book_bbnfix_when_ready.py` only → then (manual) refresh this letter from the booking card.
> Do **not** use `bbnfix_delta_chi2_proxy.py` peeks as Laplace ΔlnZ.
>
> **Forbidden claims (until gate):** booked live-pair H₀ / Σm_ν / Δχ² / ΔlnZ; interim GetDist
> tables as letter results; treating GR≈0.07/0.086 as the gate; leading with a win from peeks.

**Status.** Core empirical claim of the program — built against data, not extended to it after the fact. Standing evidence number is **pre-bbnfix Laplace-from-MCMC** (ΔlnZ ≈ +2.6; SH0ES-conditional; **not** a live-pair result). Nested sampling waits on cluster time and is **not** running. Live bbnfix pair is **not bookable** (lcdm R−1 **0.047912**@N=24858 t=2026-08-05T04:55:58 — below stop without self-stop; dyad **0.056889**@N=24677 t=2026-08-05T07:54:30 — **1.14×** stop; both not self-stopped — residual freeze above). Live matched pairs have been a **wash** when multi-basin (see Risk §3c). **Do not lead with a win.**

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
- **Live BBN-fixed pair:** do not quote H₀ / ΔlnZ from `dyad_mnu_bbnfix` / `cmp_lcdm_mnu_bbnfix` until both self-stop and [`book_bbnfix_when_ready.py`](../scripts/book_bbnfix_when_ready.py) books them.

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
| 1 | ε at recombination → H₀ ≈ 69.9 (fixed-ε; ~half SH0ES gap) | **machine-backed** provisional **pre-bbnfix** | production fit; CLASS | Stack conditional; YHe re-measure pending; **live bbnfix H₀ NOT bookable** (lcdm R−1=**0.047912**@N=24858 — below stop, no self-stop; dyad **0.056889**@N=24677 — **1.14×**; both not self-stopped) |
| 2 | Ladder ceiling ~70.9–71.3; cannot reach 73 | **machine-backed** | H0_CEILING; ς = −1 | Residual tension owned |
| 3 | ΔlnZ ≈ +2.6 Laplace evidence | **machine-backed** provisional **pre-bbnfix** | earlier MCMC Laplace | **OPEN-MACHINE:** **not** the live-pair result; nested offline; gate = both bbnfix R−1<0.05 **and** `converged:true` → `book_bbnfix_when_ready.py` only; peeks UNBOOKABLE |
| 4 | ε stack c·f̄·α_c conditional | **complete-conditional** | THE_AMPLITUDE | α_c instrument not running |
| 5 | EDE better residual tension (~2.5σ vs ~4.25σ class) | **interpretation** (literature scoreboard) | Schöneberg 2026 table | Model cheaper/falsifiable, not better-fitting; desk fairness paid (T11) |
| 6 | SN candle term pushes ladder *down* (ς = −1) | **machine-backed** | 162-template scan | Real-SN synthetic photometry appeal open |
| 7 | Kill: same ε on all messengers; DESI w; radio locks; He adverse | **registered** | §6 kill list | — |
| 8 | Bookable BBN-fixed H₀ / model−ΛCDM ΔlnZ letter sentence | **OPEN-BLOCKED** | residual freeze 2026-08-05 | **OPEN-MACHINE:** wait self-stop; then `scripts/book_bbnfix_when_ready.py` |

**Non-claims / forbidden:** not a closed H₀ win; not full SH0ES account; not nested-confirmed evidence; **no peek numbers as letter results**; pre-bbnfix ΔlnZ ≈ +2.6 is standing, not a live-pair booking.

**Triage:** elevate-in-place. Physics ceiling: mechanism production-grade; live-pair evidence **OPEN-BLOCKED** (bbnfix gate: lcdm **0.047912**@N=24858 / dyad **0.056889**@N=24677 t=2026-08-05T07:54:30 / **NOT bookable**).
