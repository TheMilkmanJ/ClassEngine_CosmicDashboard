# Page coevolve best joint near-miss — v13 (2026-08-04)

**NO FABRICATIONS.** Write-once. No CANDIDATE packet. `page_curve_claimed: false`.

---

## Champion artifact: `coevolve_v13.json` (schedule v23)

| gate | result |
|---|---|
| T1–T6 | **True** (`CANDIDATE_TURN` machine True with coevo gates) |
| T2 u≥0.9 + drop | **True** (u_late=0.9021) |
| stall_cap ≤10 | **True** (longest=**10**) |
| co_frac / swap / peak_in_motion | **True** |
| **DC3** weight-invariant | **PASS** |
| **T8** | **False** — sole fail [0.10,0.11) range/S*=**0.113** (need ≤0.10) |
| CANDIDATE_TURN_binding | **False** (needs T8) |
| page_curve_claimed | **false** |

Scorecard: `page_curve/coevolve_v13_scorecard_recompute.json`

---

## Progress ladder

| ver | stall | DC3 | T2 | T8 worst ratio | machine T1–T6+coevo |
|---|---|---|---|---:|---|
| v2 | pass | fail | pass | pass | — |
| v11 | 11 fail | pass | pass | 0.122 | fail |
| **v13** | **10 pass** | **pass** | **pass** | **0.113** | **pass** |
| v14–v16 | regressed | — | — | — | — |

Single-knob attempts after v13 (v24–v26) either regressed T2/stall or did not improve T8 early bin. **Stop thrash; v13 stands as best.**

---

## What remains for joint clear
Only **T8 early bin** (0.113 → ≤0.10). One early multivalued S(u) window at low evaporation coordinate. Not a late-stall class.

## Explicit non-claims
Not Page physics claim. Not CANDIDATE filing. Q6 OPEN. Claim-decoupling still required before any red packet even if T8 later passes.

*NO FABRICATIONS.*


## Follow-up attempts 2026-08-04 (later)

Tried: TMS delay (0.07–0.08), TMS_SHAPE 3.2–3.8, G_TMS cuts, BS_MILD 0.208–0.218, coarser sampling, late-dump boosts.

| Outcome class | Result |
|---|---|
| Soften early TMS enough for T8 early ≤0.10 | Often loses T2 (u_late&lt;0.9) or stall |
| More late dump after soft TMS | Late multivalued / no freeze |
| G_TMS scale alone | Early range and S* scale together — **ratio sticky ~0.11** |

**Conclusion:** early T8 fail is structural for this construction (monotone S(u) over Δu=0.01 while TMS builds); not fixed by small header knobs without regression. **v13 remains champion.** Deeper dynamics (not edge-tune) needed for joint clear.

---

## Deeper construction aftermath (2026-08-04 night)

| ID | Outcome |
|---|---|
| D1 two-phase | early T8 better; T2 not joint — `B_A_D1_ATTEMPT.md` |
| D2 free \(w_c\equiv1\) | no-op on champion path — `B_A_D2_ATTEMPT.md` |
| D3 mode densify | v35–v38 not joint (u_late&lt;0.9, stall/DC3 fail) — `B_A_D3_ATTEMPT.md` |
| **D4** | **active** — accept instrument near-miss until new microphysics |

No CANDIDATE. Q6 OPEN. Script header: `v23_champion_locked`.

---

## Full residual freeze stamp (2026-08-04)

Re-scored this freeze (OMP=1):

```bash
python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

Confirmed: T1–T6+stall+DC3+T2 **PASS**; T8 **0.113** only fail; `CANDIDATE_TURN_binding` **False**; `page_curve_claimed` **false**.  
Package: `docs/working_logs/_runs/page_full_freeze_20260804/` (REPORT + SCORECARD_SNAPSHOT + HYGIENE).  
**Champion locked. Zero thrash. Zero premature CANDIDATE.**
