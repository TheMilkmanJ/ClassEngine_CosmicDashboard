# LCDM TRGB DESI-DR2 — Stage A peel into `docs/chains` — 2026-08-10

**Result:** LOGGED (LCDM leg only)  
**Root:** `cmp_lcdm_mnu_bbnfix_desidr2_trgb`  
**Host:** `i-0c65cc61a575bdfa7` (`prtoe-routed-96`)  
**Landed:** `docs/chains/` **and** `chains/` (identical product set)

## Gate (this leg)

| field | value |
|---|---|
| `converged` | **true** |
| R−1 last | **0.04015** |
| R−1_cl last | 0.184 |
| N (progress) | **39046** |
| progress time | 2026-08-10T23:15:46Z |
| GetDist Gelman-Rubin (post 30% burn) | 0.0459 |

**Note:** Dyad TRGB twin (`dyad_mnu_bbnfix_desidr2_trgb`) was **not** converged at peel time — **not** dual-gate BOOKED as a pair. This is a single-leg log of the LCDM TRGB chain.

## Stack

- Planck lowℓ TT/EE + plik lite + lensing  
- **DESI DR2 BAO ALL**  
- ACT DR6 + SPT-3G lite (candl)  
- BBN production-faithful prior  
- **SN:** `pantheonplus` + `H0_trgb_cchp` (69.8±1.7) — **not** pantheonplusshoes  

**Do not mix** with SH0ES DESI-DR2 or old-BAO booked pairs.

## Products in `docs/chains/`

```
cmp_lcdm_mnu_bbnfix_desidr2_trgb.1.txt
cmp_lcdm_mnu_bbnfix_desidr2_trgb.2.txt
cmp_lcdm_mnu_bbnfix_desidr2_trgb.3.txt
cmp_lcdm_mnu_bbnfix_desidr2_trgb.checkpoint
cmp_lcdm_mnu_bbnfix_desidr2_trgb.covmat
cmp_lcdm_mnu_bbnfix_desidr2_trgb.input.yaml
cmp_lcdm_mnu_bbnfix_desidr2_trgb.launchlog
cmp_lcdm_mnu_bbnfix_desidr2_trgb.progress
cmp_lcdm_mnu_bbnfix_desidr2_trgb.updated.yaml
```

Tar SHA256: `521c72db97f76281bd4cb57dd44e61fb4c63953d23201b340500775fb42afbad`  
S3: `s3://prtoe-class-upload-1f41456b/trgb_lcdm_desidr2_booking_20260810/cmp_lcdm_mnu_bbnfix_desidr2_trgb.tar.gz`

## GetDist marginals (`ignore_rows=0.3`)

Post-burn samples: **27332**

| parameter | mean ± std | 68% |
|---|---|---|
| H0 | **68.387 ± 0.262** | [68.122, 68.647] |
| m_ncdm | 0.0201 ± 0.0170 | [0, 0.0243] |
| omega_b | 0.022480 ± 8.5e-5 | [0.022394, 0.022566] |
| omega_cdm | 0.11845 ± 0.00061 | [0.11785, 0.11909] |
| Omega_m | **0.3018 ± 0.0034** | [0.2983, 0.3052] |
| S8 | **0.8224 ± 0.0075** | [0.8147, 0.8299] |
| sigma8 | 0.8199 ± 0.0060 | [0.8143, 0.8259] |
| n_s | 0.9715 ± 0.0030 | [0.9686, 0.9745] |
| logA | 3.0529 ± 0.0130 | [3.0401, 3.0660] |

Compare (same GetDist settings, SH0ES DESI-DR2 LCDM booked earlier): H0 **68.729 ± 0.250**, S8 **0.817 ± 0.007** — TRGB anchor pulls H0 slightly lower (as expected vs SH0ES).

## Fences

- TRGB-conditional DESI-DR2 instrument — **separate** from SH0ES DESI-DR2 BOOKED pair.  
- Not nested PolyChord evidence.  
- Pair Stage A only when dyad TRGB also dual-gates.  
- Hessian/Laplace optional later; not done here.

## Sidecars

- `getdist_stats.json`  
- `booking.json`  
- `cmp_lcdm_mnu_bbnfix_desidr2_trgb.tar.gz`

*NO FABRICATIONS. Live peel from AWS after converged:true.*
