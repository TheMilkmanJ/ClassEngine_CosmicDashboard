# Candidate rebuild batch9 (hygiene + §4.2 monotone v)

**Script:** `scripts/quantum_page_candidate_rebuild.py`  
**SHA256:** `e7ef3815915a10311b6472c8219fc530ae061674438eff3a1fc5f1449237dd9d`  
**page_curve_claimed:** **false**  
**Machine CANDIDATE_TURN (pre-T8 self-score from full history arrays):** **True**  
**Standing / red:** **DENIED** (batch9 / third denial — multivalued \(S(u)\), §4.2 not pre-ratified, T6 git; see `STATUS.md`)

## Scorecard (recomputed from history_full in JSON)

| test | result |
|---|---|
| T1 | **True** (u*=0.0951) |
| T2 | **True** (u_late=0.9830, drop=2.0363) |
| T3 | **True** |
| T4 | **True** N1=True N2=True N4=True |
| T5 | **True** — Same-run continuum field φ(x,t) + pure Gaussian modes with week2 ω/Γ; not full QFT on curved acoustic spacetime |
| T6 | **True** (full histories + sha256) |
| T7 claim | **false** |
| **Machine CANDIDATE TURN** | **True** (self-score only; full arrays) |
| **Standing CANDIDATE** | **DENIED** (red ×3; not booked) |

## Protocol patches applied this batch
- §4.2 monotone envelope u=max v — later **RATIFIED as scoring aid** (ChatGPT batch9-T8)
- Scorecard only from full arrays
- Script content hash for T6 if untracked
- T8 single-valued \(S(u)\) — **SUPERSEDED:** now **ACTIVE / BINDING** (ChatGPT REFEREE batch9-T8-claim-decoupling). This rebuild’s machine True is **pre-T8** and remains **red DENIED**. See `PAGE_TURN_ACCEPTANCE_PROTOCOL.md` §4.3–4.4.

## Recompute
```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_candidate_rebuild.py
# then recompute scorecard only from JSON history_full
```
