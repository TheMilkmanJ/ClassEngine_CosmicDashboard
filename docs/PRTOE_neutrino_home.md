# Neutrino home — the lightest-mass relation (2026-07-11)

> ## Residual freeze — FULL honesty (neutrino home + Fairbank path) — 2026-08-05
>
> **Status:** OPEN-MACHINE / **OPEN-BLOCKED** on joint Σm_ν posterior · Fairbank path **HOLD** · m_ββ package **READY not posted**.
>
> **1. Σm_ν joint waits on `dyad_mnu_bbnfix` book.** Live pair: model `dyad_mnu_bbnfix` (Σm_ν free) vs twin `cmp_lcdm_mnu_bbnfix`. Progress: dyad N=27525 **R−1=0.085619** (t=2026-08-05T22:03:22; **1.71×** stop; `converged: false`), lcdm N=26294 **R−1=0.049324** (t=2026-08-05T11:52:10; control leg ready; `converged: true`). Bookable **NO** — requires both progress R−1 < 0.05 **and** `converged: true`, then `scripts/book_bbnfix_when_ready.py`. Offline GetDist GR (~0.086 / ~0.07) is **diagnostic only**, never the gate. Double-duty conv_g (T3 item 2) rides unproduced `conv_desi` / early routeD, not desk. §2 minima table is **not** the joint posterior — **no invented posteriors**. Live authority: [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).
>
> **2. Fairbank HOLD.** Experimental letter + hep-ph endorsement path paused at owner. This is an owner-controlled correspondence / endorsement path only; no second Fairbank TeX belongs to the ship path. Companion: [exploratory/PRTOE_fairbank_note_HOLD.md](exploratory/PRTOE_fairbank_note_HOLD.md). Draft letter: [PRTOE_fairbank_note_draft.md](PRTOE_fairbank_note_draft.md). Owner branch table: [arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md](working_logs/_runs/arxiv_owner_prep_20260804/OWNER_ACTION_WHEN_FAIRBANK_REPLIES.md).
>
> **3. m_ββ package READY not posted.** `papers/neutrino-mbb/` + staged [arXivReady/neutrino-mbb](arXivReady/README.md) PDF+tarball are **READY_PACKAGE** (audit-clean). Owner submitted to William Fairbank 2026-08-03; packaging **paused**. **No arXiv post** until Fairbank reply / hep-ph endorsement (or owner-chosen parallel archive path). Inventory: [arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md](working_logs/_runs/arxiv_owner_prep_20260804/PACKAGE_INVENTORY.md). Full honesty package: [neutrino_full_honesty_20260804/REPORT.md](working_logs/_runs/neutrino_full_honesty_20260804/REPORT.md).
>
> **What unblocks:** (machine) both bbnfix legs self-stop → `python3 scripts/book_bbnfix_when_ready.py` → bookable Σm_ν joint; conv_desi owner restart for double-duty. (owner) Fairbank reply → owner branch table → possible hep-ph post of **neutrino-mbb only**.
>
> **Forbidden claims:** booked Σm_ν / H₀ from live chains; GetDist GR or crude param R−1 as gate; §2 minima as joint posterior; “posted to arXiv” without ID; second Fairbank TeX; H₀ ≈ 69.9 / “outperform” as result.
>
> **Blocked-lane audit:** shared `bbnfix` booking gate is frozen in
> [blocked_lane_bbnfix_20260805/REPORT.md](working_logs/_runs/blocked_lane_bbnfix_20260805/REPORT.md).
>
> **Fairbank hold card:** shared owner-hold posting state is frozen in
> [blocked_lane_fairbank_hold_20260805/REPORT.md](working_logs/_runs/blocked_lane_fairbank_hold_20260805/REPORT.md).

Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Full sector: [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md). Letter to experiment: [PRTOE_fairbank_note_draft.md](PRTOE_fairbank_note_draft.md). Package path: [arXivReady README](arXivReady/README.md) · [arxiv owner prep](working_logs/_runs/arxiv_owner_prep_20260804/REPORT.md).

Third thread of the atomic-constant survey; collects the neutrino-sector relation. One registered prediction rides it (P-2026-023). Relative to standard cosmology, the model shifts the *inferred* neutrino mass upward, not down.

**Status.** Lightest-mass relation and upward shift established in the model. Open: joint-fit consistency (**OPEN-MACHINE**, `dyad_mnu_bbnfix` book not ready 2026-08-06 — lcdm R−1 0.049324 with `converged:true`, dyad 0.085619 with `converged:false`, pair still refused), Fairbank HOLD + m_ββ READY not posted (owner/external), exact v_L branch selection, comparison with direct and oscillation bounds.

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
| 2 | Model fit prefers m_ncdm ~0.07–0.09 eV (upward vs ΛCDM 0) | **machine-backed** provisional | §2 table; P-2026-023 | **OPEN-MACHINE:** joint `dyad_mnu_bbnfix` book **NO** (lcdm R−1=**0.049324**@N=26294 t=2026-08-05T11:52:10 with `converged:true`; dyad **0.085619**@N=27525 t=2026-08-05T22:03:22 with `converged:false`) |
| 3 | Upward shift direction generic to varying-m_e | **interpretation** | §4 | Specific numbers are model’s |
| 4 | Exact v_L derivation / branch selection | **OPEN** | status; T3 | Benchmark A: 5 MeV candidate; MeV vs high-v_L is CMB-S4 / leptogenesis, not desk |
| 5 | CMB-S4 tests MeV-scale v_L corner (P-2026-025) | **registered** | §3 | High-v_L corner not accessible |
| 6 | conv_g double-duty (Σm_ν + S₈ in one fit) | **OPEN-BLOCKED** | T3/T4 | **OPEN-MACHINE:** conv_desi unproduced |
| 7 | Fairbank experimental path | **WATCH-EXTERNAL** / **HOLD** | letter draft; arxiv_owner_prep | Owner-controlled correspondence / endorsement / posting path only; see `working_logs/_runs/blocked_lane_fairbank_hold_20260805/REPORT.md` |
| 8 | m_ββ window package (`neutrino-mbb`) | **READY_PACKAGE** not posted | arXivReady; PACKAGE_INVENTORY | hep-ph endorsement; Fairbank thread live; **no invent arXiv ID**; see `working_logs/_runs/blocked_lane_fairbank_hold_20260805/REPORT.md` |

**Non-claims / forbidden:** not a precision Σm_ν discriminator; full sector lives in [PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md); no booked joint posterior until gate; no “posted” without arXiv ID; no second Fairbank TeX.

**Triage:** elevate-in-place. Physics ceiling: structural + provisional fit numbers; joint chain **OPEN-BLOCKED**; package **READY not posted** (2026-08-05).
