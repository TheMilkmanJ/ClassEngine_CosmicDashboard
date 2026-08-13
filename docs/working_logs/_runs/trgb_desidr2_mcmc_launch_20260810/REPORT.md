# TRGB DESI-DR2 MCMC twins — launch 2026-08-10

**Instance:** `i-0c65cc61a575bdfa7` (`prtoe-routed-96`, c7i.24xlarge)  
**AMI:** stack `ami-0162f91b5bf4fbea6`  
**Launch:** ~19:40Z — both legs got initial points and measured speeds.

## Roots

| leg | yaml | output | ranks × OMP |
|---|---|---|---|
| dyad TRGB | `dyad_mnu_bbnfix_desidr2_trgb.yaml` | `chains/dyad_mnu_bbnfix_desidr2_trgb` | 3 × 16 |
| lcdm TRGB | `cmp_lcdm_mnu_bbnfix_desidr2_trgb.yaml` | `chains/cmp_lcdm_mnu_bbnfix_desidr2_trgb` | 3 × 16 |

## Stack (matched to SH0ES DESI-DR2 bbnfix twins)

- Planck lowℓ TT/EE + plik lite + lensing  
- **DESI DR2 BAO ALL**  
- ACT DR6 + SPT-3G lite (candl)  
- BBN production-faithful prior  
- **SN:** `pantheonplus` + `H0_trgb_cchp` (69.8±1.7) — **not** pantheonplusshoes  

## Gate

R−1 < 0.05 **and** `converged: true` on **both** legs before booking.  
Do **not** mix with SH0ES DESI-DR2 or old-BAO pairs.

## Covmat seed

- dyad: `chains/dyad_mnu_bbnfix_desidr2.covmat`  
- lcdm: `chains/cmp_lcdm_mnu_bbnfix_desidr2.covmat`  

*NO FABRICATIONS. Leave running until dual-gate.*
