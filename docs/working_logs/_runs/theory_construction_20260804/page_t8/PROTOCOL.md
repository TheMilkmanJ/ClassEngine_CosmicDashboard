# PROTOCOL — if a new law appears (Page T8 joint path)

**Date:** 2026-08-04  
**Authority:** PAGE_TURN_ACCEPTANCE_PROTOCOL.md §4.3–4.4;  
`docs/working_logs/_runs/quantum_residual_task_20260803/CLAIM_DECOUPLING_CHECKLIST.md`;  
`scripts/page_protocol_scorecard.py`.  
**NO FABRICATIONS.** This is process only — not a CANDIDATE filing.

---

## Binding fence (always)

| pin | value |
|---|---|
| `page_curve_claimed` | **false** until the **separate claim step** after red AGREE |
| Standing CANDIDATE | **none** until full stack below |
| Scorecard tool | **never** sets claim true |
| Resource | OMP=1; **no PolyChord**; **no MCMC** touch for Page instrument |
| Artifacts | write-once versioned `coevolve_v{N}.json` — **never overwrite** scored JSON |

---

## Ordered path (write-once → claim)

```
0. Licensed new microphysics law written (named; not header thrash)
1. Implement law in instrument → run complete (OMP=1)
2. Write-once JSON on disk (history_full + nulls + schedule_pins + provenance)
3. Arrays-only scorecard:
     python3 scripts/page_protocol_scorecard.py <run.json>
4. Gates: T1–T6 + stall/coevo + DC3 + T8_pass (≤0.10 all bins)
5. Claim-decoupling checklist (independent of run write)
6. Red AGREE on packet
7. Claim step only then — still a separate action for page_curve_claimed
```

### Gate numbers that must hold for step 4

| gate | requirement |
|---|---|
| T1 interior max | True |
| T2 reach | \(u_{\mathrm{late}}\ge 0.9\); drop/noise |
| T3 early rise | credited rise on \(\mathrm{d}u>0\) only |
| T4 nulls | N1–N4 |
| T5 continuum | structural / construction class |
| T6 artifacts | True |
| stall_cap | longest stall ≤ 10 frames (binding coevo pin as on champion path) |
| co_frac / swap / peak_in_motion | pass as scorecard defines |
| DC3 | weight-invariant reach PASS when computable |
| **T8** | **all** occupied \(\Delta u=0.01\) bins: range/\(S_\star\) **≤ 0.10** |
| T7 claim flag | remains false in scorecard |

If T8 residual remains **>0.10** (champion today **0.113**): **stop** — no CANDIDATE, no claim-decoupling packet.

---

## Claim-decoupling checklist (restated)

From `CLAIM_DECOUPLING_CHECKLIST.md` — **in order**:

| # | Gate | Notes |
|---|---|---|
| 1 | Run complete | Producing script finished cleanly |
| 2 | JSON on disk | Full histories present |
| 3 | Scorecard from arrays | `page_protocol_scorecard.py` → `*_scorecard_recompute.json` |
| 4 | Script sha256 | Scorecard + producing script content hash recorded |
| 5 | Git commit when owner allows | Prefer committed scripts for T6 |
| 6 | **Only then** file CANDIDATE packet | Packet **references** existing JSON+scorecard; does **not** re-mint the run |
| 7 | T8_pass | Binding single-valued \(S(u)\) |

**Never** co-write CANDIDATE packet with the first production of the run JSON.

---

## Explicit: when **not** to open a packet

| situation | action |
|---|---|
| T8 early residual **0.113** (v13) | **No packet** |
| T1–T6 machine True but T8 fail | Machine True ≠ candidate |
| D1–D3 style thrash “almost green” | **No packet**; restore champion lock |
| Scorecard-only re-run | Hygiene only — not a filing |
| Q2 area-law coefficient paid | **Not** dynamical Page (Q6) |

---

## Champion lock until unstuck

| item | value |
|---|---|
| Champion | `coevolve_v13.json` |
| Scorecard | `coevolve_v13_scorecard_recompute.json` |
| Schedule header | `v23_champion_locked` |
| LATEST pointer | → v13 |
| Freeze stance | **D4** — accept instrument near-miss until licensed new microphysics |

---

## Optional named diagnostics (not production)

Allowed without opening CANDIDATE:

- Re-run scorecard on existing write-once JSON (this package).  
- Frame-level fail-bin dumps from stored arrays.  
- Existing continuum/null scripts **if** short and not densify thrash.

**Forbidden as “protocol shortcuts”:** densify campaigns, PolyChord, MCMC for Page, T8 threshold loosen, bin subsample.

---

*NO FABRICATIONS. Protocol restates binding rules; does not invent new gates.*
