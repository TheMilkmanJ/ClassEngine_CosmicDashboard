# RED_AUDIT — DESI-DR2 bbnfix booking `20260810_053127`

**Auditor:** Grok 4.5 (xAI)  
**Date (UTC):** 2026-08-10  
**Claude status:** unavailable — Grok carries red load  
**Package:** Stage A DESI-DR2 GetDist booking (BOOKED)  
**Scope:** license **citation of DESI Stage A numbers** on living surfaces as a **separate instrument**  

```
red: AGREE
```

## What was audited

| check | result | evidence |
|---|---|---|
| Dual gate both legs | **PASS** | dyad R−1 **0.03321** @ N=53482; lcdm **0.041377** @ N=52031; both `converged:true` |
| Instrument label | **PASS** | DESI-DR2 BAO stack; `not_old_bao: true` in booking.json |
| GetDist H₀ | **PASS** | dyad **70.299±0.541**; lcdm **68.729±0.250** (30% burn) |
| Mix with old-BAO | **PASS (forbidden, documented)** | package fences separate instrument |
| Nested claimed? | **PASS (absent)** | no PolyChord ΔlnZ |
| Sample-cov Laplace | **PASS as diagnostic** | ΔlnZ≈**+1.38**, cond(Σ)~10⁸ — soft modes; not nested |

## Fences

1. **Separate instrument** from old-BAO BOOKED pair — never replace old-BAO rows.  
2. Not nested; gold PolyChord still open.  
3. `make_getdist_tables.py --include-bbnfix` does **not** auto-include DESI roots (old-BAO BBNFIX_ROOTS only). DESI numbers live in currency banner + booking receipt until a dedicated DESI table path exists.

## Stage B for DESI tables

**Granted for shelf citation** of Stage A DESI GetDist from this receipt.  
**Not** a license to merge DESI into old-BAO production table rows as one stack.

*NO FABRICATIONS. Grok red stands in for Claude while Claude is offline.*
