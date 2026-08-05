# Primordial helium bounds on a leptonic electron-mass transition inside the nucleosynthesis window

**Author:** Justin Pulford (unaffiliated)
**arXiv category:** astro-ph.CO (optional hep-ph)
**Status (2026-08-02):** TeX package ready. **Red-team pass 2026-08-02.** Constraint half only. Endorsement is the external gate — not claimed here.

**Arithmetic reverify (2026-08-03; status cured 2026-08-04; reconfirm 2026-08-04T18:14Z):**
hard-win card `docs/working_logs/_runs/hard_win3_bbn_eps_recompute_20260803/` +
trigger re-run `docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/` —
ε 2σ = **3.196% ≈ paper 3.20%** — **PASS** (disk-backed; MCMC untouched). Board grade:
**ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** — public record
(Zenodo one record) still required for external-win done. Zenodo click-path checklist
(no desk upload):
`docs/working_logs/_runs/fairbank_arxiv_trigger_20260804/ZENODO_BBN_EPS_BOUND_CHECKLIST.md`.
Not an arXiv post; Fairbank/endorsement still owner gate.

## Relation to the framework

**Framework-independent as a constraint paper.** The amplitude ε and the critical temperature
T_c are free parameters of a temperature-dependent electron-mass shift that turns on inside the
BBN window. No model value of either is used as an input to the bound. The framework is why the
ramp topology was interesting to compute; it is not why the Aver limit is true. Positioned against
existing constant/power-law varying-constant BBN literature (Dent–Stern–Wetterich and CMB
citations already in the TeX); novelty underclaimed to the turn-on topology at one measured T_c.

Corpus home: `docs/PRTOE_bbn_witness.md` (constraint half only; prediction half with chain-dependent
D/H is excluded).

**The framework is not named in the TeX.**

## What it claims

- With ε free, a linear turn-on below T_c deforms the weak rates in a production BBN network
  (PRyMordial). At the measured point T_c = 179 keV the helium response is linear:
  dY_p/dε = 0.00163 per %ε.
- Against Aver et al. (Y_p = 0.2453 ± 0.0034) that elasticity implies

  **ε < 3.2% (2σ)**

  at that measured T_c only, with zero fitted parameters. (Verified arithmetic: baseline
  Y_p⁰ = 0.246891, windowed Y_p = 0.248995 at ε = 1.2543%; 1σ ceiling ε < 1.11%, 2σ ceiling
  ε < 3.20%.) Not a first bound on varying m_e.
- EMPRESS (Y_p = 0.2370 ± 0.0034) **cannot** be used for this bound: standard BBN at ε = 0 is
  already +2.91σ high, so the discrepancy is not attributable to the transition — a non-result,
  not an unquoted EMPRESS limit. Aver is used because the ε=0 null is consistent with it
  (≲0.5σ), not because it is kinder to the ramp.
- Deuterium is **not** used for a derivative bound (nonlinear bottleneck response). Absolute
  model−ΛCDM D/H from cosmological chains is **not** quoted (chain-dependent ban).
- Conservative T_c scan method stated (grid of elasticities; upper envelope; most-permissive
  single number if needed); dense ε_max(T_c) curve still **not produced**.
- ΔN_eff is not floated; lithium is recorded as percent-level and unused.

## UNVERIFIED / incomplete

| item | status |
|---|---|
| Dense ε_max(T_c) curve over the full [70, 500] keV interval | **UNVERIFIED / not produced.** The paper quotes the verified bound at the measured T_c (179 keV) and states explicitly that a grid map of the upper edge over the free-T_c window is future network work, not a result of this note. |
| Chain-dependent central D/H as a model prediction | **Excluded by design** (not a gap — a ban). |
| EMPRESS-based upper limit on ε | **None exists** (explained in the paper; not a missing number). |

## Folder contents

- `main.tex` / `submission/main.tex` — source (inline bibliography; no BibTeX).
- `main.pdf` — clean-room build.
- `bbn-eps-bound.tar.gz` — arXiv payload (`main.tex` + `recompute_eps_bound.py`).

Verified by extracting the tarball into an empty directory and running two pdflatex passes.

## Number provenance (spot-check)

| quantity | value | source |
|---|---|---|
| Y_p⁰ (ε=0) | 0.246891 | windowed PRyM baseline (`docs/PRTOE_bbn_witness.md`; LT scan row) |
| Y_p (window) | 0.248995 | ramped splice at T_c = 179 keV, ε ≃ 1.25% |
| dY_p/dε | 0.00163 / %ε | measured linear elasticity (audit: 0.001628) |
| Aver Y_p | 0.2453 ± 0.0034 | Aver et al., JCAP 03 (2021) 027, arXiv:2010.04180 |
| EMPRESS Y_p | 0.2370 ± 0.0034 | Matsumoto et al., ApJ 941, 167 (2022), arXiv:2203.09617 |
| 2σ Aver bound | ε < 3.20% | (Y_p^Aver + 2σ − Y_p⁰) / 0.00163 |
| EMPRESS at ε=0 | +2.91σ | (0.246891 − 0.2370) / 0.0034 |

## External recompute (Claude C3 / hard-win path)

Stranger-runnable arithmetic (no PRyM install required for the Aver ceiling):

```bash
python3 recompute_eps_bound.py
```

Expected: `ε 2σ ceiling = 3.196%` ≈ paper claim **3.20%** (PASS).
Included in `bbn-eps-bound.tar.gz` alongside `main.tex`.
