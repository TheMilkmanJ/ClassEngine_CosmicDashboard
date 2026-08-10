# Gold-standard DESI-DR2 PolyChord program — 4 matched legs

## Direct answer: what is in the SH0ES gold pair?

**Yes.** Both `*_desidr2_ev.yaml` configs include:

| Dataset | Cobaya name | Present? |
|---|---|---|
| Planck CMB low-ℓ TT | `planck_2018_lowl.TT` | **yes** |
| Planck CMB low-ℓ EE | `planck_2018_lowl.EE` | **yes** |
| Planck CMB high-ℓ TTTEEE (plik lite) | `planck_2018_highl_plik.TTTEEE_lite` | **yes** |
| Planck **lensing** | `planck_2018_lensing.clik` | **yes** |
| DESI DR2 / Y3 BAO (ALL) | `bao.desi_dr2.desi_bao_all` | **yes** |
| ACT DR6 | `act_dr6` (candl) | **yes** |
| SPT-3G (lite) | `spt3g_lite` (candl) | **yes** |
| Pantheon+ **SH0ES** | `sn.pantheonplusshoes` | **yes** (SH0ES pair only) |
| Production BBN prior + YHe | `prior.bbn` + `YHe` | **yes** |

(SPT, not “SRT”.)

---

## Four PolyChord legs (2 anchors × 2 models)

| # | Config | Model | Ladder anchor |
|---|---|---|---|
| 1 | `dyad_mnu_bbnfix_desidr2_ev.yaml` | dyad | **SH0ES** (`sn.pantheonplusshoes`) |
| 2 | `cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml` | ΛCDM+m_ν | **SH0ES** |
| 3 | `dyad_mnu_bbnfix_desidr2_trgb_ev.yaml` | dyad | **TRGB CCHP** (`sn.pantheonplus` + `H0_trgb_cchp` 69.8±1.7) |
| 4 | `cmp_lcdm_mnu_bbnfix_desidr2_trgb_ev.yaml` | ΛCDM+m_ν | **TRGB CCHP** |

**Shared on all four:** Planck CMB+lensing, DESI DR2 BAO ALL, ACT DR6, SPT-3G lite, production BBN.

**Only difference between pairs:** SH0ES Cepheid ladder vs TRGB CCHP compressed H0 + plain Pantheon+.

### Why TRGB is set up this way (repo convention)

Plain `sn.pantheonplus` marginalizes absolute magnitude internally; the TRGB calibration enters as the compressed CCHP prior  
`H0_trgb_cchp: λ H0: −½((H0−69.8)/1.7)²` (Freedman 2021), matching `cmp_lcdm_trgb.yaml` / `cmp_prtoe_fixed_trgb.yaml`.

**Honesty flag (carry into papers):** TRGB has its own sub-debate (CCHP vs CATS). This tier tests **CCHP as labeled**, not a blended ladder.

---

## Nested settings (all four)

| | dyad | lcdm |
|---|---:|---:|
| nlive | 500 | 500 |
| num_repeats | 65 (5×13) | 60 (5×12) |
| precision_criterion | 0.001 | 0.001 |
| clustering | on | on |
| OMP | 1 | 1 |

---

## Quote rules

| Comparison | Allowed? |
|---|---|
| ΔlnZ SH0ES: dyad − lcdm | **yes** (legs 1−2) |
| ΔlnZ TRGB: dyad − lcdm | **yes** (legs 3−4) |
| Mix SH0ES model vs TRGB control | **no** |
| Mix DESI-DR2 with old-BAO / sampled-ε evidence | **no** |

---

## Compute (when quota ≥ 32 + 4×96 = 416, or staged)

Ideal: four on-demand `c7i.24xlarge` boxes in parallel after 512 quota.

```bash
bash scripts/launch_gold_desidr2_polychord.sh shoes_dyad
bash scripts/launch_gold_desidr2_polychord.sh shoes_lcdm
bash scripts/launch_gold_desidr2_polychord.sh trgb_dyad
bash scripts/launch_gold_desidr2_polychord.sh trgb_lcdm
```

Staged if quota partial: run SH0ES pair first (2×96), then TRGB pair.

Current on-demand quota still **96** (request **512** CASE_OPENED) → cannot launch PC fleet yet.

---

## MCMC note

DESI-DR2 MCMC twins remain on SH0ES stack (`*_desidr2` with pantheonplusshoes), OMP-boosted.  
Optional later: TRGB MCMC twins for posteriors under TRGB — separate from nested evidence.
