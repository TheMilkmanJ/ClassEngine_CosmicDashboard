# Red audit — TRGB DESI-DR2 dual-gate Stage A

**Date (UTC):** 2026-08-12  
**Package:** `trgb_booking_desidr2_20260812`  
**Auditor:** Grok (acting red stamp; Claude offline)

## Verdict

**red: AGREE** — Stage A posteriors bookable under stated fences.

## Checks

| check | result |
|---|---|
| Both legs R−1 < 0.05 on last progress | **PASS** (dyad 0.045, lcdm 0.040) |
| MCMC processes stopped (not mid-run quote) | **PASS** |
| GetDist `ignore_rows=0.3` documented | **PASS** |
| SH0ES pair not mixed into TRGB numbers | **PASS** |
| Nested ΔlnZ claimed | **FAIL avoided** — not claimed |
| R−1_cl honesty | **PASS** — noted ~0.18–0.19, not ultra-tight |
| Living tables updated | **PASS** (`PRTOE_CHAIN_TABLES.md`) |
| Plots present | **PASS** (`docs/plots/*trgb*`) |

## Kill lines (must not appear as Stage A products)

- Mid-run nested logZ as evidence  
- “Converged on all derived parameters” without R−1_cl caveat  
- Single H0 for “the model” without ladder (SH0ES vs TRGB)

## Grade

`red: AGREE` for **Stage A parameter posteriors and ladder comparison**.  
Stage B paper-facing prose still owner/tribunal optional.
