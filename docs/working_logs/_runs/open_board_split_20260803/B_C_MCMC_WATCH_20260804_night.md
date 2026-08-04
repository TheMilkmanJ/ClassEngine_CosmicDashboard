# MCMC watch — 2026-08-04 night

**Stamp:** 2026-08-04T01:52 local  
**Rule:** NO FABRICATIONS · leave chains alone · no peek-book H₀ · no PolyChord

## Cobaya gate (authority for booking)

| chain | progress R−1 | N | progress mtime | checkpoint converged | Rminus1_last |
|---|---:|---:|---|---|---:|
| cmp_lcdm_mnu_bbnfix | **0.059** | 19013 | 2026-08-03T21:05 | **false** | 0.059 |
| dyad_mnu_bbnfix | **0.189** | 18837 | 2026-08-03T17:57 | **false** | 0.189 |

`book_bbnfix_when_ready.py` → **REFUSED**.

## Live growth (chains still writing)

| chain | rows/rank (approx) | latest chain mtime |
|---|---|---|
| lcdm | ~6550–6700 | 2026-08-04 ~01:51 |
| dyad | ~6670–6780 | 2026-08-04 ~01:48 |

Progress/checkpoint **lag** chain files by hours — normal until cobaya’s next R−1 checkpoint write; **not** a license to book.

## Diagnostics (UNBOOKABLE)

| measure | lcdm | dyad |
|---|---:|---:|
| crude max-param R−1 (burn 50%) | ~0.019 | ~0.034 |
| **GetDist** max GR (`ignore_rows=0.3`) | **~0.068** | **~0.086** |

GetDist is the better offline proxy: both still **> 0.05**. Crude param R−1 is optimistically low — do not use it for gates.

Tool: `scripts/bbnfix_mcmc_watch_diag.py`

## Explicit

- **NOT bookable**
- No H₀ quote, no GetDist booking, no living-doc edit for posteriors
- Leave cobaya alone until self-stop

*NO FABRICATIONS.*
