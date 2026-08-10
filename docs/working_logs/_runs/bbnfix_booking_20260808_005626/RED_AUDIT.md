# RED_AUDIT — old-BAO bbnfix booking `20260808_005626`

**Auditor:** Grok 4.5 (xAI)  
**Date (UTC):** 2026-08-10  
**Claude status:** unavailable this session — Grok carries red load  
**Package:** Stage A booking receipt (BOOKED)  
**Scope:** license Stage B forward table write for the **old-BAO** production pair only  

```
red: AGREE
```

## What was audited

| check | result | evidence |
|---|---|---|
| Dual gate: both R−1 < 0.05 | **PASS** | dyad **0.048118** @ N=37605; lcdm **0.049324** @ N=26294 (`chains/*.progress`) |
| Dual gate: both `converged: true` | **PASS** | `chains/*.checkpoint` |
| Stage A book script exit | **PASS** | REPORT **Result: BOOKED**, exit 0 |
| Three-rank GetDist present | **PASS** | `booking.json` ranks 1–3; H₀ dyad **70.052±0.716**, lcdm **68.345±0.343** |
| Live chain re-check (this audit) | **PASS** | same R−1 / converged as receipt |
| Peek-book / force path | **N/A** | this is dual-gate BOOKED, not force peek |
| Nested evidence claimed? | **PASS (absent)** | package does not invent PolyChord ΔlnZ |
| Evidence honesty labels | **PASS** | sample-cov Laplace ΔlnZ≈+0.21 soft modes; Hessian v2 diagnostic only |

## Fences that remain (not lifted by this red)

1. **SH0ES-conditional** stack — not a calibration-free H₀.  
2. **Not nested** — Stage B tables are posterior summaries, not gold Bayes factors.  
3. **Do not mix** with DESI-DR2 Stage A booking (`desidr2_bbnfix_booking_20260810_053127`).  
4. **Do not** quote pre-bbnfix historical ΔlnZ ≈ +2.635 as current authority.  
5. `make_getdist_tables.py` loads rank-1 samples for full parameter tables; **banner authority H₀/m_ncdm/S₈ remains three-rank booking REPORT**.

## Stage B license

**Granted:** run  
`bash scripts/bbnfix_when_ready_all.sh --write-tables`  
or  
`python3 scripts/make_getdist_tables.py --include-bbnfix`  

Forward `docs/PRTOE_CHAIN_TABLES.md` may include the booked old-BAO pair under the dual-gate banner. Currency banner + claims ledger must retain honesty fences above.

## Explicit non-claims

- No COMPLETE physics promotion  
- No nested ΔlnZ  
- No DESI-DR2 table merge into old-BAO rows  
- No EXTERNAL WIN for BBN ε (DOI still owner)

*NO FABRICATIONS. delivered ≠ graded beyond this package. Grok red stands in for Claude while Claude is offline.*
