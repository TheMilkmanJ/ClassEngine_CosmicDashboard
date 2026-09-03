# Neutrino home — the lightest-mass relation (2026-07-11)

> ## Residual freeze — FULL honesty (neutrino home + Fairbank path) — 2026-08-10
>
> **Status:** old-BAO joint Σm_ν **BOOKED Stage B** · DESI-DR2 joint Σm_ν **BOOKED Stage A** (separate; SH0ES + TRGB Stage A also booked) · Fairbank **HOLD** · m_ββ **READY not posted** · On SH0ES, nested sampling got close enough to compare the twins, not far enough to book a full sampler. No nested ΔlnZ.
>
> **1. Old-BAO joint Σm_ν is booked (Stage B published).** Authority:
> [`bbnfix_booking_20260808_005626`](working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md)
> · [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md). Three-rank GetDist (`ignore_rows=0.3`, SH0ES-conditional):
> dyad **H₀ = 70.052 ± 0.716**, `m_ncdm = 0.0671 ± 0.0583`, **S₈ = 0.821 ± 0.0097**; lcdm
> **H₀ = 68.345 ± 0.343**, `m_ncdm = 0.0192 ± 0.0174`, **S₈ = 0.824 ± 0.0081**. Evidence honesty:
> sample-cov Laplace only **ΔlnZ ≈ +0.21** (cond(Σ)~10⁸).
>
> **2. DESI-DR2 joint Σm_ν is BOOKED Stage A (separate instrument — do not mix).** Authority:
> [`desidr2_bbnfix_booking_20260810_053127`](working_logs/_runs/desidr2_bbnfix_booking_20260810_053127/REPORT.md);
> peel `docs/chains/*_desidr2.*`. dyad R−1 **0.03321** / lcdm **0.041377**, both `converged:true`;
> GetDist `m_ncdm` means **0.0508 ± 0.0473** (dyad) / **0.0138 ± 0.0128** (lcdm); H₀
> **70.30±0.54** / **68.73±0.25**. Sample-cov Laplace **ΔlnZ ≈ +1.31** (CHAIN_TABLES 1.305; soft modes; **not nested**). FD Hessian
> finished finite but ΔlnZ_H ≈ **−25** vs samplecov **+1.5** — **diagnostic fail, not bookable**.
> On SH0ES, nested sampling got close enough to compare the twins, not far enough to book a full sampler. No nested ΔlnZ.
>
> **3. Fairbank HOLD.** Experimental letter + hep-ph endorsement path paused at owner. Companion:
> [exploratory/PRTOE_fairbank_note_HOLD.md](exploratory/PRTOE_fairbank_note_HOLD.md). Draft:
> [PRTOE_fairbank_note_draft.md](PRTOE_fairbank_note_draft.md) (letter H₀ sentence ready from booking).
>
> **3b. Fairbank desk workload COMPLETE (2026-08-10).** Full re-derivation of the lab window:
> [fairbank_desk_workload_20260810/REPORT.md](working_logs/_runs/fairbank_desk_workload_20260810/REPORT.md)
> · `TODO.md` all desk items **DONE**. **LAB WINDOW GREEN:** \(m_{\beta\beta}\in[0.04,5.3]\,\mathrm{meV}\)
> reproduces; ceiling stable under ±1σ NuFIT shifts (5.22–5.38 meV); discriminating band
> 3.69–5.30 meV intact; baseline nEXO ~10.8% flat-phase; nulls do not confirm. Owner path still HOLD.
>
> **4. m_ββ package READY not posted.** `papers/neutrino-mbb/` + arXivReady — **READY_PACKAGE**.
> **No arXiv post** until Fairbank reply / endorsement. Inventory:
> [arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md](working_logs/_runs/arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md).
>
> **What unblocks next:** (machine) nested gold finish; (owner) Fairbank → hep-ph post of **neutrino-mbb only**.
>
> **Forbidden claims:** mixing old-BAO with DESI posteriors; Hessian ΔlnZ_H as evidence; “posted to arXiv”
> without ID; H₀ ≈ 69.9 / “outperform” as result; nested invent.

Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Full sector: [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md). Letter to experiment: [PRTOE_fairbank_note_draft.md](PRTOE_fairbank_note_draft.md). Package path: [arXivReady README](arXivReady/README.md) · [arxiv owner prep](working_logs/_runs/arxiv_owner_prep_20260804/REPORT.md).

Third thread of the atomic-constant survey; collects the neutrino-sector relation. One registered prediction rides it (P-2026-023). Relative to standard cosmology, the model shifts the *inferred* neutrino mass upward, not down.

**Status.** Lightest-mass relation and upward shift established in the model. Joint-fit Σm_ν is
**BOOKED** on old-BAO (Stage B) and **BOOKED Stage A** on DESI-DR2 as a separate instrument (both
show dyad `m_ncdm` mean above the lcdm twin, with large soft-mode errors). On SH0ES, nested sampling got close enough to compare the twins, not far enough to book a full sampler. No nested ΔlnZ. Fairbank HOLD + m_ββ READY not posted
remain owner/external.

## 0. Standard-cosmology tension

ΛCDM-conditional fits push Σm_ν down. Tightest combinations sit at or below the oscillation floor — tension between cosmology and the lab neutrino sector.

## 1. Model structure

Neutrino mass is not an ordinary Higgs Yukawa. It is medium-sourced (inverse-seesaw / Majoron), with the lepton-number-breaking scale tied to the condensate and the recorded DE–lightest-mass relation. Structural claim: neutrino mass lives in the medium sector, not the electroweak Higgs sector.

## 2. Fit numbers (P-2026-023)

Same data; `m_ncdm` is the sampler’s neutrino-mass parameter (sampled Σm_ν):

| setup | m_ncdm |
|---|---|
| ΛCDM fit | 0.000 eV |
| model preference | 0.0875 eV |
| model + free curvature | 0.071 eV |

Electron-mass shift reallocates part of the CMB constraint budget.

**Test.** As data sharpen: ΛCDM-conditional bound below 59 meV conflicts with the cosmological fit while the model posterior stays above the floor. Failure mode: model posterior collapses.

## 3. Forward structure (benchmark)

Benchmark A: v_L = 5 MeV, heavy-state mass M = 10 TeV — near-resonant; inverse-seesaw parameter μ/Γ = 0.46; Majoron coupling g = m₃/v_L = 1.0×10⁻⁸ inside CMB-S4 band (P-2026-025). CMB-S4 tests v_L < 20 MeV (~1/3 of natural parameter space). Same sector appears in baryogenesis (equilibrium ratio K = Γ_N/H = 9×10⁷ computed).

## 4. Scope

- Upward-shift direction is generic to varying-m_e cosmologies; specific numbers are this model’s.
- Two viable v_L points: MeV-scale (CMB-S4 accessible) and high-v_L (not).
- CMB-S4 is the cleanest discriminator between points.
- KATRIN-class direct limits and the oscillation floor bracket the remaining window.

Standard cosmology pushes neutrino mass down. This model keeps it heavy enough to stay visible because the medium that replaces DM+DE pays that mass from its own sector. Cosmological and laboratory posteriors should diverge if the model is right.

---

## Claims ledger & discipline (2026-08-04 residual freeze — FULL honesty) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Neutrino mass medium-sourced (not ordinary Higgs Yukawa) | **interpretation** / structural | §1 | Inverse-seesaw / Majoron seating |
| 2 | Old-BAO joint posterior books an upward-shifted `m_ncdm` relative to ΛCDM | **machine-backed** | booking receipt; §2 table; P-2026-023 | DESI Stage A also books higher dyad `m_ncdm` mean (separate; soft errors); SH0ES nested: close enough to compare, not booked |
| 3 | Upward shift direction generic to varying-m_e | **interpretation** | §4 | Specific numbers are model’s |
| 4 | Exact v_L derivation / branch selection | **OPEN** | status; T3 | Benchmark A: 5 MeV candidate; MeV vs high-v_L is CMB-S4 / leptogenesis, not desk |
| 5 | CMB-S4 tests MeV-scale v_L corner (P-2026-025) | **registered** | §3 | High-v_L corner not accessible |
| 6 | conv_g double-duty (Σm_ν + S₈ in one fit) | **OPEN** / `g` **INCONCLUSIVE** | T3/T4; `conv_desi_retune_grade_20260824` | Retune stopped; lever not demanded; lensing still owed |
| 7 | Fairbank experimental path | **WATCH-EXTERNAL** / **HOLD** | letter draft; arxiv_owner_prep | Owner-controlled correspondence / endorsement / posting path only; see `working_logs/_runs/blocked_lane_fairbank_hold_20260805/REPORT.md` |
| 8 | m_ββ window package (`neutrino-mbb`) | **READY_PACKAGE** not posted | arXivReady; PACKAGE_INVENTORY | hep-ph endorsement; Fairbank thread live; **no invent arXiv ID**; see `working_logs/_runs/blocked_lane_fairbank_hold_20260805/REPORT.md` |

**Non-claims / forbidden:** not a precision Σm_ν discriminator; full sector lives in [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md); not nested ΔlnZ (Stage A booked; nested mid-run forbidden); no “posted” without arXiv ID; no second Fairbank TeX.

**Triage:** elevate-in-place. Physics ceiling: structural + booked joint Stage A; SH0ES nested: close enough to compare, not booked; package **READY not posted** (2026-08-15).
