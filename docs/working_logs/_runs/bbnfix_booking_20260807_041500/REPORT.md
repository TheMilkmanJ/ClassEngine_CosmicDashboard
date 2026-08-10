# bbnfix GetDist booking — 20260807_041500

**Generated (UTC):** 2026-08-07T04:15:12.953733+00:00
**Script:** `scripts/book_bbnfix_when_ready.py`
**Gate:** both of {dyad_mnu_bbnfix, cmp_lcdm_mnu_bbnfix} with R−1 **< 0.05** **AND** `converged: true` (self-stop) — both legs required
**Result:** BOOKED
**Exit code:** 0

## Progress + self-stop gate

| chain | present | N | timestamp | R−1 | converged | ready |
|---|---|---:|---|---:|---|---|
| `dyad_mnu_bbnfix` | YES | 37605.0 | 2026-08-07T04:08:52.190063 | 0.048118 | true | YES |
| `cmp_lcdm_mnu_bbnfix` | YES | 26294.0 | 2026-08-05T11:52:10.194879 | 0.049324 | true | YES |

### Gate messages

- dyad_mnu_bbnfix: R−1 = 0.048118 < 0.05 (N=37605.0) — R−1 GRADED
- dyad_mnu_bbnfix: checkpoint converged: true — self-stop OK
- dyad_mnu_bbnfix: checkpoint Rminus1_last=0.048118 (informational; gate uses progress R−1)
- cmp_lcdm_mnu_bbnfix: R−1 = 0.049324 < 0.05 (N=26294.0) — R−1 GRADED
- cmp_lcdm_mnu_bbnfix: checkpoint converged: true — self-stop OK
- cmp_lcdm_mnu_bbnfix: checkpoint Rminus1_last=0.049324 (informational; gate uses progress R−1)

## Rank files

- `dyad_mnu_bbnfix`: 3 files
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.1.txt`
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.2.txt`
  - `/home/themilkmanj/prtoe_class/chains/dyad_mnu_bbnfix.3.txt`
- `cmp_lcdm_mnu_bbnfix`: 3 files
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.1.txt`
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.2.txt`
  - `/home/themilkmanj/prtoe_class/chains/cmp_lcdm_mnu_bbnfix.3.txt`

## GetDist marginals (`ignore_rows=0.3`)

Three-rank load via `getdist.loadMCSamples`. Means ± std; 68% limits when GetDist MargeStats available.

### `dyad_mnu_bbnfix`

Post-burn samples: 26324

| parameter | present | mean ± std | 68% limits |
|---|---|---|---|
| H0 | YES | 70.052 ± 0.716053 | [69.3523, 70.7673] |
| m_ncdm | YES | 0.0671427 ± 0.0582684 | [0, 0.0820361] |
| omega_b | YES | 0.0227637 ± 0.000125527 | [0.0226353, 0.0228848] |
| S8 | YES | 0.821363 ± 0.00965247 | [0.812563, 0.831771] |

### `cmp_lcdm_mnu_bbnfix`

Post-burn samples: 18406

| parameter | present | mean ± std | 68% limits |
|---|---|---|---|
| H0 | YES | 68.3453 ± 0.343404 | [67.9915, 68.6836] |
| m_ncdm | YES | 0.0192058 ± 0.0173502 | [0, 0.0231012] |
| omega_b | YES | 0.0224995 ± 8.64196e-05 | [0.0224172, 0.0225856] |
| S8 | YES | 0.823628 ± 0.0081253 | [0.815678, 0.83139] |

## External claim (booked numbers only)

Matched-likelihood dyad vs ΛCDM+m_ν posteriors under the BBN-fixed production stack (DESI+Planck+ACT+SPT+SN+BBN prior as in the yamls).

**Kill:** quote while R−1 ≥ 0.05; omit burn-in statement; rank-1-only half-chain σ instead of three-rank GetDist.

## Manual follow-up (not done by this script)

- Paste H₀ letter sentence from `finalize_h0_at_convergence.py` if desired
- Update `docs/PRTOE_CHAIN_TABLES.md`, `_chain_snapshot.md`, referee calendar
- Optional Laplace ΔlnZ per checklist Step C — separate, not this entrypoint

