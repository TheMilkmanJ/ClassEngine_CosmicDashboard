# Note for Prof. W. Fairbank — 0νββ in a unified dark-fluid cosmology

*2026-07-19. Self-contained; plain physics.*

*Status: **experimental letter** · **CORPUS_ONLY** (not an arXiv package; ship path = `neutrino-mbb` only). The bridge to the neutrino sector is a registered model relation, not a first-principles derivation. **HOLD** — desk does not email Fairbank, invent endorsement, or invent a second Fairbank TeX.*

**Authority cards (2026-08-05).**
- Fairbank hold / posting path: `working_logs/_runs/blocked_lane_fairbank_hold_20260805/REPORT.md`
- live helium benchmark state: `working_logs/_runs/blocked_lane_helium_fork_20260805/REPORT.md`

> **Currency residual freeze — 2026-08-05.** Live bbnfix progress (quote R−1 **with N and timestamp**): model `dyad_mnu_bbnfix` R−1 = **0.060201** (N=26135, t=2026-08-05T15:50:02 — **1.20×** stop; `converged: false`), twin `cmp_lcdm_mnu_bbnfix` R−1 = **0.049324** (N=26294, t=2026-08-05T11:52:10 — control leg ready; `converged: true`). **NOT bookable.** Do **not** quote H₀ / joint posteriors as results until `scripts/book_bbnfix_when_ready.py` passes (requires both R−1 < 0.05 **and** self-stop). Cross-links: [neutrino_full_honesty](working_logs/_runs/neutrino_full_honesty_20260804/REPORT.md) · [arxiv_owner_prep](working_logs/_runs/arxiv_owner_prep_20260804/REPORT.md) · [neutrino_home](PRTOE_neutrino_home.md) · [HOLD companion](exploratory/PRTOE_fairbank_note_HOLD.md) · blocker card [blocked_lane_bbnfix_20260805/REPORT.md](working_logs/_runs/blocked_lane_bbnfix_20260805/REPORT.md).

## Result in three sentences

In a unified dark-sector cosmology — one superfluid scalar for dark matter and dark energy, plus a single early-universe electron-mass shift ε = 1.2543% (= 27α/5π, from one derived factor, one counting assumption, and one registered coupling) — the neutrino sector is an output: the dark-energy scale ties to the lightest neutrino mass, giving **Σm_ν = 61.4 meV with normal ordering**. The mass mechanism violates lepton number, so **neutrinos are Majorana and 0νββ is required**. With measured splittings and free Majorana phases,

**m_ββ ∈ [0.04, 5.3] meV**, phase-averaged rms **3.3 meV** (rate ∝ m_ββ²; median over phases 3.05 meV).

## Experimental reach

**Of the planned experiments below, only nEXO reaches this band, and only at the favourable matrix-element end.** Model ceiling m_ββ = 5.30 meV; nEXO projected reach at the favourable end is 4.7 meV — common band roughly **4.7–5.3 meV**. LEGEND-1000 (9–21 meV) and CUPID (12–34 meV) sit entirely above the ceiling. A confirmed detection outside the thin band falsifies the model.

**A null does not.** Phases can cancel. Dirac nature would kill the model (Majorana is required), but there is no practical way to prove Dirac: you cannot prove a process is absent. Experimentally: **this setup can refute the model; it cannot confirm it.**

**Near-term pressure is cosmological, from below.** DESI-era CMB+BAO limits reach Σm_ν ≲ 72 meV, some combinations lower. The model sits at 61.4 meV, just inside. The live risk is an upper limit descending through that value. The model’s reply is that those limits are ΛCDM-conditional and the squeeze relaxes under its recombination physics (section below) — a testable claim, not an escape.

**Σm_ν itself is not distinctive.** 61.4 meV is only **2.6 meV** above the normal-ordering floor (58.8 meV at m₁ = 0); planned cosmological resolution is ~20 meV. Nothing planned can separate this sum from the minimal-ordering case every squeezed model lands on.

**m_ββ is distinctive** because it depends on m₁ itself. At m₁ = 0 the window is [1.48, 3.69] meV; at the model’s m₁ = 2.25 meV it is [0.04, 5.30] meV. Ceiling up 44%, floor nearly collapses. Minimal ordering puts the whole window below nEXO’s best reach; this model puts about **11%** of phase space above it. That is the difference an experiment can see.

Provenance: registered before deciding data (2026-07-07, git-timestamped). Bridge is the same lightest-mass relation as in the neutrino sector. Ordering from a registered prediction-collision test (P-2026-004); P-2026-012 records the relation but does not select the branch (ANN-2026-025). See those entries for the full record.

## Cancellation floor

Lightest mass m₁ = ρ_Λ¼. Observed 2.25 meV (0.45% — Planck 1.8% on ρ_Λ, quartered). Model chain: 2.2599 meV (+0.44%), inside 1σ of observation. Sum barely moves: Σm_ν = 61.34–61.37 meV → quoted 61.4. Effective mass is more sensitive at the floor.

NuFIT-class mixings across the observation’s range:

| term | m₁ = 2.2399 meV (−1σ) | m₁ = 2.25 meV (obs.) | m₁ = 2.2599 meV (derived) |
|---|---|---|---|
| \|U_e1\|² m₁ | 1.52 meV | 1.52 meV | 1.53 meV |
| \|U_e2\|² m₂ | 2.67 meV | 2.67 meV | 2.67 meV |
| \|U_e3\|² m₃ | 1.10 meV | 1.10 meV | 1.10 meV |
| **floor** | **0.050 meV** | **0.044 meV** | **0.038 meV** |
| ceiling | 5.295 meV | 5.302 meV | 5.310 meV |

Floor moves ~25% across the range; ceiling moves 0.3%. Window quoted **[0.04, 5.3] meV**; conclusions below depend on the ceiling.

A floor exists because the middle term exceeds the other two (2.67 vs 2.62). Margin 0.05 meV on O(2) terms — three phasors barely fail to close a triangle. Above m₁ = **2.324 meV** the floor is zero. Derived anchor is 2.8% below that (six times the measurement precision on the scale): floor thins but does not vanish inside the allowed range.

Floor ~0.04 meV is a scale coincidence, not a protected feature; two orders below any planned reach. The useful consequence: near-cancellation makes **m_ββ a sharp probe of the dark-energy scale**.

## Overlay on experiments

Projected 10-year reaches (spans = nuclear matrix-element range), model window [0.04, 5.30] meV:

| experiment | isotope | projected m_ββ reach | vs 5.30 meV ceiling |
|---|---|---|---|
| **nEXO** | ¹³⁶Xe | **4.7 – 20.3 meV** | **overlaps 4.7–5.3 meV** |
| LEGEND-1000 | ⁷⁶Ge | 9 – 21 meV | entirely above |
| CUPID | ¹⁰⁰Mo | 12 – 34 meV | entirely above |

Only nEXO can touch the model, and only if the ¹³⁶Xe matrix element is favourable. Flat Majorana phases (convention, not a result): model exceeds 4.7 meV about **10.8%** of the time.

If barium tagging delivers the projected factor-of-four half-life gain, reach improves by √4 = 2 in m_ββ → ~**2.35 meV**. Detection probability on this model: 10.8% → **69%**. Discrimination is weaker: minimal normal ordering [1.48, 3.69] meV exceeds 2.35 meV **63.7%** of the time.

| reach | this model | minimal ordering | separates? |
|---|---|---|---|
| 4.7 meV (baseline nEXO) | 10.8% | **0%** | **yes** |
| 2.35 meV (Ba tagging) | 69.1% | 63.7% | no |

**Discriminating band: 3.69–5.30 meV** — above minimal ordering’s hard ceiling, below this model’s. Minimal ordering cannot produce a signal there; this model lands there **31.7%** of the time. All of baseline nEXO’s 10.8% falls in that band.

**Barium tagging makes the test likely; baseline nEXO makes it decisive.** A tagged detection near 2 meV barely moves this model’s posterior. A baseline detection near 4.5 meV cannot be minimal ordering.

## Why the cosmological squeeze relaxes

ΛCDM-conditional analyses squeeze Σm_ν toward (and below) the ~59 meV oscillation floor. This model replaces CDM+Λ with one fluid (ΛCDM-degenerate at background and linear level, checked to five decimals) plus an electron-mass shift at recombination (Hart–Chluba). Varying-m_e support is real but not flattering: Hart & Chluba 2020 at **3.5σ**; recent ACT DR6 + DESI DR2 fit m_e/m_e₀ = 1.0081 ± 0.0046 (**1.8σ**); other work finds varying m_e does not fully resolve H₀ once DESI DR2 BAO is in. Common-framework scoreboard (Schöneberg et al. 2026, 14 models): early dark energy ΔIC 23.40, residual tension 2.51σ; varying m_e 12.58 and 4.25σ. This letter does not rest on being the best H₀ route.

Shifted calibration frees damping-tail budget that ΛCDM spends against neutrino mass, so model-conditional fits leave Σm_ν near its physical value. If the class is right, the meV-scale m_ββ frontier is physically open rather than cosmologically foreclosed.

## Status of the cosmological fits

Provisional fit diagnostics (sound-horizon driven; SH0ES included though that calibration pulls the other way) have sat near H₀ ≈ 69.9 on Planck 2018 + ACT DR6 + SPT-3G + BAO + Pantheon+SH0ES. **Do not quote H₀ ≈ 69.9, any “outperform ΛCDM” claim, or a best-fit comparison as a result.** Chains are still being brought to convergence under a corrected sampler; the value may move.

**A stopped run from late July looked better than it was, and we stopped it rather than quote it.** Best fit 1377.89 (model) vs 1379.79 (ΛCDM) — 1.9 log units our way. **That number was never quotable.** Its three parallel chains sat at best fits **1377.9, 1610.6, 1440.6** with H₀ = 69.5, 64.0, 64.8 — three regions, not one posterior. The 1377.89 was one chain that found a good region. The reference ΛCDM chains were better behaved (spread 0.43) but not converged either. Acceptance was **5.3–6.2%** (model) and 8.5–8.9% (ΛCDM) vs a ~25% target; proposal poorly matched. Re-tuning is a collective checkpoint all ranks must reach; one rank lagged and the other two waited. **No convergence statistic was computed for that run** (empty progress file). Proposal reseeded from the good chain; acceptance moved to **31%**.

**We do not claim the comparison as a result.** The matched relaunch that replaced that run has merged the basins (every sampled parameter agrees across ranks to within ~0.6 within-chain s.d.) and is *converging but not yet quotable*: progress R−1 = **0.060201** (model `dyad_mnu_bbnfix`, N=26135, t=2026-08-05T15:50:02; **1.20×** stop; `converged: false`) and **0.049324** (ΛCDM+m_ν twin, N=26294, t=2026-08-05T11:52:10; control leg ready; `converged: true`) — the pair is still **NOT bookable** because the model leg has not self-stopped; do not quote H0/posteriors as results until `book_bbnfix_when_ready.py` passes.

**Further reasons that stopped run could never have been claimed:** its model chain had 1.79× more samples (best-fit is a running minimum that favours the longer chain); neither side had converged (ΛCDM R−1 ≈ 1.0; the model run never produced an R−1 at all); and best fit is not evidence (no parameter penalty — the whole point when one model has fewer parameters). **The live comparison today is the relaunched pair above, and it is not quotable either way until R−1 reaches its stop.** Standing evidence number remains the marginal, SH0ES-conditional Laplace estimate below.

**Zero-parameter evidence test.** Amplitude, tilt, coupling, and transition epoch frozen in advance vs ΛCDM at full freedom. Nested sampling started then stood down on this hardware (hundreds of days to first checkpoint); waits for cluster time. Until then: Laplace-from-MCMC. Caveat: transition epoch frozen at a **profiled** value 0.053 dex from the model’s onset identity (~28% in dark-fluid mass). **The graded configuration is near the model, not the stated one.**

Validation: exact ΛCDM null to five decimals, gauge invariance, precision-stability battery. Medium’s reality is carried as an open assumption. Entry points: THREE_EQUATIONS, DEPENDENCY_TREE, PREREGISTERED_PREDICTIONS (50+ bets), FAILURES_LEDGER.

Context: ~99% of ordinary mass is QCD-condensate binding. This model adds one more condensate and asks whether it reads into the remaining Yukawa percent at the 10⁻² level for one epoch.

### BBN (worst column)

Deliberately absent from the fit list above. Electron-mass shift is on during nucleosynthesis; sector is rigid (inputs derived or measured) — model cannot coach its witness. Net adverse. The live helium benchmark state moved in 2025-2026 and is now centralized in `working_logs/_runs/blocked_lane_helium_fork_20260805/REPORT.md`; do not headline the older Aver/EMPRESS sigma pair as current literature currency. D/H predicted 2.407–2.463×10⁻⁵ vs Cooke 2.527 ± 0.030 → −2.5 to −1.4σ on the full budget (obs. ±0.030 ⊕ PRIMAT post-LUNA ±0.037). Ranges span ζ = T_dark/T_γ ∈ [0.25, 0.35], used everywhere it appears; CMB-S4 measures it via ΔN_eff = 0.06–0.24.

*(Next section uses ζ baseline before dark-radiation dilution; same calculation, earlier stage: 2.387×10⁻⁵.)*

Joint decided by a nuclear-code systematic outside our control: PRIMAT D/H = 2.439 vs PArthENoPE 2.51–2.54 (3.5% = 2.3× quoted nuclear error). Carrying none of it: joint p = 0.02–0.08; half: 0.07–0.11; all: 0.12–0.21. Model on the low side of the deuterium fork — self-adverse, registered before referee (P-2026-027: dark-ages radio primordial D/H at 327 MHz).

**Inside our pipeline the systematic is one reaction.** Switching PRIMAT ↔ NACRE II at fixed everything else: D/H +2.33%, row −2.94σ → −1.77σ; helium 0.02σ. **d(d,n)³He carries 94%.** Not a LUNA effect: compilations agree on d(p,γ)³He to 0.12%. They disagree on how well d(d,n)³He is known: PRIMAT 1.10% vs NACRE II 5.86% (factor 5.2); central values differ 4.31%.

Pisanti et al. (JCAP 04 (2021) 020): D/H = (2.51 ± 0.06 ± 0.03)×10⁻⁵ — rate error **±0.06**, 2.5× the ±0.037 we use; 3% spread in d(d,n)³He from analysis choice alone. LUNA collaboration (EPJ Web Conf. 279, 01002 (2023)): D(d,n)³He and D(d,p)³H are the top remaining priority for primordial deuterium. Not done as of now.

**Column magnitude is set by unsettled nuclear data.** Rate error carried at four values in the literature; baseline row (2.387 before dilution) reads **−3.6σ to −1.6σ** depending on error bar. (−2.5 to −1.4σ earlier is the ζ window at fixed error bar — a different object.) Our −2.94σ uses the tightest assessment (conservative). Registered as two-sided bet **P-2026-058**: closing onto Cooke needs true d(d,n)³He 5.0–9.6% below PRIMAT. If LUNA-precision confirms PRIMAT to ~1%, deuterium is wrong at −3.6σ with no model lever. Bet largely shared with ΛCDM (needs −8.9% on the same rate); discriminates only in a narrow band.

## Where the deuterium deficit comes from

At ζ baseline (before dark-radiation dilution that lifts 2.387 into 2.407–2.463), from an in-house ΛCDM control, same code and data:

| step | D/H ×10⁻⁵ | vs Cooke (±0.0476) |
|---|---|---|
| ΛCDM control | 2.420 | −2.25σ |
| model baryon density, +1.1% | 2.372 | −3.25σ |
| electron-mass window at nucleosynthesis, +0.645% | 2.387 | −2.94σ |

**Nucleosynthesis new physics helps.** ε ramp on at T_c = 177.10 keV raises D/H +0.645% (+0.31σ). On ΛCDM control alone that would be −1.93σ vs control’s −2.25σ — a decomposition only: window and baryon shift are the same ε at two epochs; the model cannot have one without the other. Conclusion: **deficit is not made in the nuclear sector.**

**Deficit is imported from the CMB fit.** Varying m_e returns ω_b 1.1% above control; d ln(D/H)/d ln ω_b = −1.66 → 1.8% deuterium loss — three times the window’s help, opposite sign.

**Same baryon shift buys the Hubble result.** Exchange rate **0.59σ deuterium per km/s/Mpc of H₀** (secant between model fit and control, 1.7 km/s/Mpc apart — trustworthy inside the interval, extrapolation outside). Parity with ΛCDM control costs 1.17 of 1.7 km/s/Mpc (**69% of H₀ relief**). Centring D/H on Cooke would take ~3× the measured interval (direction/scale only).

Deuterium tension and Hubble result are one trade. A real cure must raise D/H at fixed ω_b and fixed m_e. Expansion-rate levers fail (wrong shape). Two survivors: boost confined below T_c (right shape, 8–33× too weak on dof counting); late ⁴He photodissociation (cheap on paper; needs ≳20 MeV state, lifetime 10⁶–10⁸ s, ~30 eV per H — not in the model’s field content).

## Lightest mass and framing

Oscillations fix two splittings, not the absolute floor. Here the floor is medium-sourced: **m₁ = κ_m · ρ_Λ¼ with κ_m ≈ 1** — the dark-energy scale **sets** the lightest mass; Σm_ν = 61.4 meV follows from measured splittings.

Three qualifications:

1. The model does **not** derive 2.25 meV (dark-energy-value problem). Claim is that one un-derived number does two jobs standard cosmology treats as unrelated. Predictive content is the relation.
2. κ_m ≈ 1 is residual freedom: form from channel counting; O(1) coefficient not independently pinned.
3. Not a MaVaN construction (those hit the Afshordi–Zaldarriaga–Kohri instability). m_ν is set by a frozen lepton-number-breaking VEV, not a rolling DE field.

Framing: 0νββ decides whether lepton number is an enforced charge (field-backed) or an unenforced accounting identity that Majorana neutrinos default. The detector audits whether that debt has a bank.

## The ask

**(a)** Is the meV-window prediction in the form most useful to the 0νββ community — especially the two-sided kill structure, and whether the floor’s thinness should be stated up front?

**(b)** Critical eye on BBN (model’s weakest sector). Three questions: which rate-error assessment a referee expects (PRIMAT vs NACRE; difference is rejection at 5% vs comfort — we took the harshest); whether the deficit should be argued as a BBN problem or as a statement about the m_e–ω_b degeneracy; whether the dark-ages radio referee is a real path.

**(c)** Two numbers you own: is **4.7 meV** the right baseline nEXO reach at favourable ¹³⁶Xe matrix element? Is the barium-tagging factor-of-four correctly read as half-life (→ 2× in m_ββ) or something else? Every probability above moves with those; the discriminating-band argument is only as good as the 3.69 meV minimal-ordering ceiling.

---

*Trace: [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md), [PRTOE_deuterium_row.md](PRTOE_deuterium_row.md), [PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md), [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).*

---

## Claims ledger & discipline (2026-08-04 residual freeze) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Σm_ν = 61.4 meV NO; m_ββ ∈ [0.04, 5.3] meV | **complete-conditional** | neutrino_sector bridge | Relation registered, not first-principles; **≠** booked joint posterior |
| 2 | Only nEXO overlaps; null does not confirm | **machine-backed** / literature | experiment tables | Phases can cancel |
| 3 | Does not derive 2.25 meV | **honest fence** | qualifications | One number, two jobs |
| 4 | Fit status / multi-basin stopped run not quotable; H₀ ≈ 69.9 and “outperform” demoted; live R−1 lcdm **0.049324**@N=26294 t=2026-08-05T11:52:10 (`converged:true`; control leg ready) / dyad **0.060201**@N=26135 t=2026-08-05T15:50:02 (**1.20×**, `converged:false`) | **honest constraint** | status section; progress | **NOT bookable**; no peek H₀ as result; joint waits `dyad_mnu_bbnfix` book via `book_bbnfix_when_ready.py` |
| 5 | Experimental letter draft (Fairbank) · **CORPUS_ONLY** | **meta** / draft · **HOLD** | banner; HOLD companion | **WATCH-EXTERNAL:** correspondence not production booking; desk does not email |
| 6 | Ship vehicle is `neutrino-mbb` only | **READY_PACKAGE** not posted | arXivReady; arxiv_owner_prep | **No** second Fairbank TeX; **no** arXiv post without endorsement/ID |

**Non-claims:** not A4 production; not confirmation path via null; not MaVaN; not arXiv-posted; not invent endorsement; not invent posteriors; not peek H₀ as result.

**Triage:** elevate-in-place (draft note · CORPUS_ONLY). Physics ceiling: registered relation packaging. Cross-links: [neutrino_home residual freeze](PRTOE_neutrino_home.md) · [arxiv_owner_prep](working_logs/_runs/arxiv_owner_prep_20260804/REPORT.md) · [neutrino_full_honesty](working_logs/_runs/neutrino_full_honesty_20260804/REPORT.md) · [fairbank currency package](working_logs/_runs/fairbank_currency_20260804/REPORT.md).
