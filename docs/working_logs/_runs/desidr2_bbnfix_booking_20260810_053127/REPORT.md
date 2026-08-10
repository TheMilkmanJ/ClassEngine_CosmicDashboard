# DESI-DR2 bbnfix GetDist booking — 20260810_053127

**Result:** BOOKED
**Gate:** both legs R−1 < 0.05 AND converged:true
**Instrument:** DESI-DR2 (separate from old-BAO booked pair)

## Gate

- `dyad_mnu_bbnfix_desidr2`: R−1=0.03321 N=53482.0 t=2026-08-10T04:55:47.607730 converged=True ready=True
- `cmp_lcdm_mnu_bbnfix_desidr2`: R−1=0.041377 N=52031.0 t=2026-08-09T01:19:08.800013 converged=True ready=True

### Messages
- dyad_mnu_bbnfix_desidr2: R-1=0.03321 < 0.05
- dyad_mnu_bbnfix_desidr2: converged true
- cmp_lcdm_mnu_bbnfix_desidr2: R-1=0.041377 < 0.05
- cmp_lcdm_mnu_bbnfix_desidr2: converged true

## GetDist marginals (ignore_rows=0.3)

### `dyad_mnu_bbnfix_desidr2`
Post-burn samples: 37438

| parameter | mean ± std | 68% |
|---|---|---|
| H0 | 70.2986 ± 0.54062 | [69.7295, 70.794] |
| m_ncdm | 0.050776 ± 0.0472665 | [0, 0.0598373] |
| omega_b | 0.0227722 ± 0.000116988 | [0.0226481, 0.0228791] |
| S8 | 0.82321 ± 0.00939377 | [0.814077, 0.832482] |

### `cmp_lcdm_mnu_bbnfix_desidr2`
Post-burn samples: 36422

| parameter | mean ± std | 68% |
|---|---|---|
| H0 | 68.729 ± 0.249673 | [68.4798, 68.9778] |
| m_ncdm | 0.0138314 ± 0.01277 | [0, 0.0162727] |
| omega_b | 0.0225215 ± 8.50473e-05 | [0.0224377, 0.0226068] |
| S8 | 0.817197 ± 0.00731161 | [0.810299, 0.82483] |

## Fences

- SH0ES-conditional DESI-DR2 stack; **do not mix** with old-BAO BOOKED pair.
- Not nested PolyChord evidence.
- Stage A process receipt only.
