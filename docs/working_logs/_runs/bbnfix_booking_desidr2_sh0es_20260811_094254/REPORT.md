# bbnfix GetDist booking — 20260811_094254

**Generated (UTC):** 2026-08-11T09:42:58.263995+00:00
**Script:** `scripts/book_bbnfix_when_ready.py`
**Gate:** both of {dyad_mnu_bbnfix_desidr2, cmp_lcdm_mnu_bbnfix_desidr2} with R−1 **< 0.05** **AND** `converged: true` (self-stop) — both legs required
**Result:** BOOKED
**Exit code:** 0

## Progress + self-stop gate

| chain | present | N | timestamp | R−1 | converged | ready |
|---|---|---:|---|---:|---|---|
| `dyad_mnu_bbnfix_desidr2` | YES | 54964.0 | 2026-08-11T08:45:56.673078 | 0.035149 | true | YES |
| `cmp_lcdm_mnu_bbnfix_desidr2` | YES | 52031.0 | 2026-08-09T01:19:08.800013 | 0.041377 | true | YES |

### Gate messages

- dyad_mnu_bbnfix_desidr2: R−1 = 0.035149 < 0.05 (N=54964.0) — R−1 GRADED
- dyad_mnu_bbnfix_desidr2: checkpoint converged: true — self-stop OK
- dyad_mnu_bbnfix_desidr2: checkpoint Rminus1_last=0.035149 (informational; gate uses progress R−1)
- cmp_lcdm_mnu_bbnfix_desidr2: R−1 = 0.041377 < 0.05 (N=52031.0) — R−1 GRADED
- cmp_lcdm_mnu_bbnfix_desidr2: checkpoint converged: true — self-stop OK
- cmp_lcdm_mnu_bbnfix_desidr2: checkpoint Rminus1_last=0.041377 (informational; gate uses progress R−1)

## Rank files

- `dyad_mnu_bbnfix_desidr2`: 3 files
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix_desidr2.1.txt`
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix_desidr2.2.txt`
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix_desidr2.3.txt`
- `cmp_lcdm_mnu_bbnfix_desidr2`: 3 files
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix_desidr2.1.txt`
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix_desidr2.2.txt`
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix_desidr2.3.txt`

## GetDist marginals (`ignore_rows=0.3`)

Three-rank load via `getdist.loadMCSamples`. Means ± std; 68% limits when GetDist MargeStats available.

### `dyad_mnu_bbnfix_desidr2`

Post-burn samples: 38474

| parameter | present | mean ± std | 68% limits |
|---|---|---|---|
| H0 | YES | 70.302 ± 0.541195 | [69.7354, 70.8098] |
| m_ncdm | YES | 0.0515166 ± 0.0469602 | [0, 0.0615147] |
| omega_b | YES | 0.0227757 ± 0.000114997 | [0.0226527, 0.0228792] |
| S8 | YES | 0.82288 ± 0.00940453 | [0.814793, 0.832765] |

### `cmp_lcdm_mnu_bbnfix_desidr2`

Post-burn samples: 36422

| parameter | present | mean ± std | 68% limits |
|---|---|---|---|
| H0 | YES | 68.729 ± 0.249673 | [68.4798, 68.9778] |
| m_ncdm | YES | 0.0138314 ± 0.01277 | [0, 0.0162727] |
| omega_b | YES | 0.0225215 ± 8.50473e-05 | [0.0224377, 0.0226068] |
| S8 | YES | 0.817197 ± 0.00731161 | [0.810299, 0.82483] |

## External claim (booked numbers only)

Matched-likelihood dyad vs ΛCDM+m_ν posteriors under the BBN-fixed production stack (DESI+Planck+ACT+SPT+SN+BBN prior as in the yamls).

**Kill:** quote while R−1 ≥ 0.05; omit burn-in statement; rank-1-only half-chain σ instead of three-rank GetDist.

## Manual follow-up (not done by this script)

- Paste H₀ letter sentence from `finalize_h0_at_convergence.py` if desired
- Update `docs/PRTOE_CHAIN_TABLES.md`, `_chain_snapshot.md`, referee calendar
- Optional Laplace ΔlnZ per checklist Step C — separate, not this entrypoint

