# A4 production booking stance (pre-write — apply after summary)

**NO FABRICATIONS.** Use only after `four_branch/summary.json` + auto gates.

## Known hard residual (console, pre-summary)

| Row | Issue | Condition |
|---|---|---|
| n+1_f-1 | SELECTED from **2 candidates** only | **Cond. 2 → instrument-censored** |
| n+1_f-1 | mid-frames nphase &lt; 12/16 → NaN H | Cond. 1 gate held |
| n+1_f-1 vs n+1_f+1 | different selected t (0.25 vs 1.00) | Cond. 3 mismatched-t if used in mirror |

## Default honest booking ladder

1. **If mirror &lt;5% both pairs AND all margins AND no censored rows:**  
   Eligible for production sign(H vs n) **only after** red/ref AGREE.

2. **If any censored row (expected: n+1_f-1):**  
   - **Do not** book unconditional production sign pattern.  
   - Book: *instrument produced verdicts; at least one arm instrument-censored; production sign OPEN/partial.*  
   - May quote smoke-grade H≈sign(n)·2 as **prior smoke**, not upgraded.

3. **If mirror ≥5%:**  
   Mirror residual FAIL at 128³ — OPEN residual; no production sign.

4. **Never:**  
   Hide 2-cand selection · call “null clean” without disclosure · upgrade smoke to production without gates.

## Suggested TC non-claim block (copy when applicable)

```
Production sign(H vs n): NOT BOOKED.
Reason: [mirror_ok / censored / margin] from t14_i6_TC_GATES.md.
Smoke-grade H≈sign(n)·2 remains the last clean sign booking (i5).
Thread-closure TC is instrument fidelity, not sky IGMF.
```
