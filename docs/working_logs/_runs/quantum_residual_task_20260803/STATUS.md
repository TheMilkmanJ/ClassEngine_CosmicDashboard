# STATUS — quantum residual task (currency sync 2026-08-04)

**Hard rules:** NO FABRICATIONS · no PolyChord on this box · leave cobaya MCMCs alone · OMP=1 / nice when load high  
**page_curve_claimed:** **false** everywhere · **Q6 OPEN** · **Standing CANDIDATE:** **none**  
**Authority freeze:** `docs/working_logs/_runs/page_full_freeze_20260804/`  
**Status sync package:** `docs/working_logs/_runs/quantum_status_sync_20260804/`

---

## Residual rollup

| ID | Status | Notes |
|---|---|---|
| **R-PAGE** | **OPEN** (claim false) | **Champion = `coevolve_v13`** (schedule `v23_champion_locked`). Joint near-miss: T1–T6 + stall_cap + DC3 + T2 **PASS**; **T8 sole fail** early bin ratio **0.113** (need ≤0.10). `CANDIDATE_TURN_binding` **False**. `page_curve_claimed` **false**. **No CANDIDATE.** D1/D2/D3 exhausted; **D4 active** (accept instrument near-miss until new microphysics). **No thrash coevolve.** |
| **R-MEDR** | **MISSING_INPUT** | Deep hunt empty; no corpus-licensed \(r=r(\mathrm{medium})\) |
| **R-PAIRH** | **MISSING_INPUT** | Textbook harness only; no medium-licensed pair \(H\) |
| **R-BORN** | Desk process **DONE**; derivation **OPEN-BLOCKED** | Kill-band + empty survey locked; no derivation |
| **R-ATOM** | Desk process **DONE**; derivation **BLOCKED** | Seating fence + owner one-pager; no atomic QM from medium |

---

## R-PAGE (detail) — freeze currency

### Champion (binding instrument)

| item | value |
|---|---|
| Artifact | `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| Pointer | `page_curve/coevolve_LATEST.txt` → **v13** |
| Schedule | `v23_champion_locked` |
| T8 (single-valued S(u)) | **FAIL** — [0.10, 0.11) range/S* = **0.113** |
| Binding | `CANDIDATE_TURN_binding` = **False** |
| Claimed | `page_curve_claimed` = **false** |
| Standing CANDIDATE | **none** (no packet; no thrash) |
| Deeper construction | D1–D3 **exhausted**; **D4 active** |
| Next unblock | **microphysics only** — not knob thrash |

Re-score command (freeze):

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

### CANDIDATE TURN: **DENIED (×3)** — standing claim **none**

Last grounds (batch9 / third denial):
- \(S(u)\) multivalued at stalled \(u\) — sequencing, not co-evolution
- §4.2 monotone envelope **not** pre-ratified for claiming runs alone
- T6 git / claim-decoupling hygiene

Machine scorecards that printed `CANDIDATE_TURN: True` (purestate, candidate_rebuild) are **self-scores under pre-T8 criteria**. They are **not** standing candidates. Red: **DENIED**.

**v13 is not a CANDIDATE.** Machine T1–T6 True + T8 fail = joint near-miss only.

### Affirmed
- Unitarity on pure-state / hybrid instruments where scored
- **Purification can occur** in the pure-state instrument class
- Protocol catches claim-hygiene failures (denials are working as designed)
- **T8 + claim-decoupling ratified ACTIVE/BINDING**
- Freeze 2026-08-04: champion locked; D4 freeze stance; zero thrash

### Binding gates (do not treat machine True as filing)
- **T8** single-valued \(S(u)\) — ACTIVE (`PAGE_TURN_ACCEPTANCE_PROTOCOL.md` §4.3)
- **Claim-decoupling** — ACTIVE (§4.4 + `CLAIM_DECOUPLING_CHECKLIST.md`)
- Scorecard: `scripts/page_protocol_scorecard.py` → `CANDIDATE_TURN_binding` = T1–T6 ∧ T8_pass; never sets `page_curve_claimed`

### Blue stance
- No CANDIDATE filing until checklist complete + red AGREE  
- Physics build: **co-evolve \(S\) with advancing \(u\)** (`scripts/quantum_page_coevolve.py`) — header frozen `v23_champion_locked`  
- All instruments: `page_curve_claimed: false`  
- **Do not thrash** BS_MILD / G_TMS / densify / coevolve knobs for T8 ratio

Instrument index: `INSTRUMENT_INDEX.md`  
Co-evolve result: `PAGE_COEVOLVE_RESULT.md`  
Full freeze: `../page_full_freeze_20260804/REPORT.md`

---

## R-MEDR / R-PAIRH

| residual | status |
|---|---|
| R-MEDR | **MISSING_INPUT** |
| R-PAIRH | **MISSING_INPUT** (harness only) |

See `MEDR_PAIRH_DEEP_HUNT.md`, `MEDR_PAIRH_INVENTORY.md`.  
Do **not** write `quantum_medium_r_from_corpus.py` until a licensed closed formula + file:line exists.

---

## R-BORN / R-ATOM (desk complete)

| residual | desk | residual science |
|---|---|---|
| R-BORN | process lock **DONE** (`BORN_PROCESS_LOCK.md`) | derivation OPEN-BLOCKED / MISSING_AXIOM |
| R-ATOM | one-pager **DONE** (`ATOM_OWNER_ONEPAGER.md`) | derivation BLOCKED; default permanent seating |

No further desk work without a new foundations / microphysics program.

---

## MCMC fence (side note — not a residual close)

| item | status |
|---|---|
| lcdm R−1 | **0.059** (bounced above gate) |
| dyad R−1 | **0.189** |
| Book as result? | **Do not book** — gate not met |

Leave cobaya MCMCs alone on this box. Preflight: `../hard_wins_90day_20260803/BBNFIX_BOOKING_PREFLIGHT.md`

---

## Explicit non-closes

- Born rule **not** derived  
- Page curve **not** closed; Q6 **OPEN**  
- Medium \(r\) / pair \(H\) **not** found  
- Atomic QM from medium **not** derived  
- No `page_curve_claimed: true` on disk  
- **No standing CANDIDATE** (v13 near-miss only; T8 0.113 blocks)  
- **No thrash coevolve** under D4  
- arXiv / Fairbank **owner HOLD** (wait response)  

*NO FABRICATIONS.*

---

## Currency stamp (quantum_status_sync_20260804)

Synced from `page_full_freeze_20260804`:  
**Champion v13 · T8 0.113 · D4 active · claimed false · no CANDIDATE · no thrash.**
