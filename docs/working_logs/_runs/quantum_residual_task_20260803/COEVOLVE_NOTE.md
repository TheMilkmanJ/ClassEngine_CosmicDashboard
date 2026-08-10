# Co-evolve note (disk-backed; T8 ACTIVE) — champion freeze 2026-08-04

**Champion artifact:** `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json`  
**Scorecard:** `.../page_curve/coevolve_v13_scorecard_recompute.json` (arrays-only; claim-decoupling)  
**LATEST pointer:** `.../page_curve/coevolve_LATEST.txt` → v13 (champion, not last write-once)  
**Schedule version:** `v23_champion_locked`  
**page_curve_claimed:** **false** · **CANDIDATE filed:** **false**

Freeze package: `docs/working_logs/_runs/page_full_freeze_20260804/`

---

## Protocol

| Item | State |
|---|---|
| T8 | **ACTIVE / BINDING** |
| claim-decoupling | **ACTIVE / BINDING** |
| T1–T6 machine (scorecard) | **True** |
| T8_pass (scorecard) | **False** — early bin [0.10, 0.11) range/S* = **0.113** (need ≤0.10) |
| DC3 weight-invariant | **PASS** |
| stall_cap ≤10 | **True** (longest = 10) |
| `CANDIDATE_TURN_binding` | **False** (needs T8_pass) |
| Standing CANDIDATE packet | **none** |
| `page_curve_claimed` | **false** |

---

## Champion curve numbers (v13)

| diagnostic | value |
|---|---:|
| u_at_S_peak | 0.266967 |
| u_late | 0.902078 |
| S_peak | 0.016688 |
| S_late | 0.006142 |
| drop | 0.010546 |
| longest stall frames | 10 |
| T8 worst range/S* | 0.113154 |

---

## Ladder / thrash stop

- Best joint near-miss: **v13** (stall+DC3+T2+T1–T6 pass; T8 only fail).  
- Post-v13 header thrash and D1–D3 deeper construction: **exhausted without joint clear**.  
- **D4 active:** accept instrument near-miss until licensed new microphysics.  
- Do **not** thrash coevolve knobs / densify modes / retune G_BS.  

Historical intermediate notes (older T8_pass on pre-stall-cap runs, densify v38, etc.) are **superseded** by this freeze for champion status.

## Bottom line

- Instrument advanced to joint near-miss; **T8 still fails** → binding false.  
- **Still not a Page claim.** Q6 **OPEN**.  
- Red AGREE + claim-decoupling still required even if T8 later passes.

*NO FABRICATIONS.*
