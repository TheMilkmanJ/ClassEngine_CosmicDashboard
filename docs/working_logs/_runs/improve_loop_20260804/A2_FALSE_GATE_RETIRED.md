# A2 false gate watcher — retired 2026-08-04

**Process:** PID 212363 (bash loop on progress files since Aug03)  
**Bug:** Fired language "GATE CROSSED - A2 FIRES" on **single-chain** R−1 ≤ 0.05 without requiring **both** legs + self-stop.  
**Conflict:** corpus booking requires both bbnfix legs R−1 < 0.05 **and** `converged: true`.  
**Action:** process terminated. Use only `scripts/book_bbnfix_when_ready.py` and `bbnfix_mcmc_watch_diag.py`.  
**NO FABRICATIONS.**
