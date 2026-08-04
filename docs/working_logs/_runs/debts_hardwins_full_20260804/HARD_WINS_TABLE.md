# Hard wins — single source of truth table

**Stamp:** 2026-08-04T02:36 local  
**Parent:** `REPORT.md` in this directory  
**Plan home:** `docs/working_logs/_runs/hard_wins_90day_20260803/REPORT.md`  
**Rule:** NO FABRICATIONS · leave MCMCs alone · no PolyChord · no peek-book H₀

---

## Ranking (Claude H1 — still binding)

| Rank | Win | Who | External? | Status 2026-08-04 |
|---:|---|---|---|---|
| **1** | arXiv postings (neutrino-mbb + READY packages; Fairbank) | Owner | Yes | **OWNER HOLD** |
| **2** | BBN ε public recompute ε&lt;3.2% (2σ) @ T_c=179 keV | Blue | Yes | **ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** |
| **3** | bbnfix posterior booking (both R−1&lt;0.05 + self-stop) | Blue | Yes | **NOT YET** |
| (thread) | T14 i6 production sign TC | Blue | Thread-closure only | **CANDIDATE CLOSED (config-local)**; production **KILLED** |

---

## Evidence rows

### Rank 2 — BBN ε (**ARITHMETIC VERIFIED (internal)**; external win PENDING)

| Field | Value |
|---|---|
| Claim | Linear m_e turn-on; dY_p/dε=0.00163/%ε; Aver Y_p → ε&lt;3.2% (2σ) |
| 2σ ceiling (live recompute) | **3.196%** |
| Paper claim | **3.20%** |
| Match | **PASS** (`pass_2sig_matches_paper: true`) |
| EMPRESS | +2.91σ at ε=0 — **cannot** bound ε |
| Artifacts | `papers/bbn-eps-bound/recompute_eps_bound.py`; `hard_win3_bbn_eps_recompute_20260803/`; `BBN_EPS_REVERIFY_20260804.md` |
| Language | **ARITHMETIC VERIFIED (internal)** (3.196%≈3.20% PASS). **EXTERNAL WIN PENDING (no DOI)** — public record (Zenodo one record / DOI) still required for done; package READY, endorsement pending. |

### Rank 3 — bbnfix (**NOT YET**)

| Field | Value |
|---|---|
| Gate | BOTH chains R−1 &lt; 0.05 **and** `converged: true` |
| lcdm progress R−1 / N | **0.059055** / 19013 |
| dyad progress R−1 / N | **0.189201** / 18837 |
| Self-stop both | **false** |
| `book_bbnfix_when_ready.py` | **REFUSED** |
| `finalize_h0_at_convergence.py` | **NOT YET** |
| GetDist max GR (diag) | ~0.071 / ~0.086 — **UNBOOKABLE** authority |
| Infrastructure | READY (`book_bbnfix_when_ready.py`, checklist, refuse cards) |
| Language | **NOT YET** — never “delivered” until both gates fire |

### Thread — T14 (**candidate-local closed; production KILLED**)

| Field | Value |
|---|---|
| Production sign | **KILLED** |
| Candidate grade | **CLOSED (config-local)** three-seat |
| Binding text | `t14_i6_partial_grade_20260803/CANDIDATE_BOOKING_RESTATED.md` |
| Allowed | sign(H)=sign(n) 14/14; mirror 3.04%; mutual ≤3.4% self |
| Denied | f−1 as evidence; production booking; double-flip mirror half |
| Language | Thread-closure · **not** top sky external win |

### Rank 1 — arXiv (**HOLD**)

| Field | Value |
|---|---|
| Packages | 6/6 READY/SHIPPED hygiene (supertrace already DOI) |
| Fairbank | Contacted; **wait** further response |
| Posts this stamp | **none** |
| Language | **OWNER HOLD** — not blue chase |

---

## Language lock matrix (anti-contradiction)

| Topic | Must say | Must not say |
|---|---|---|
| BBN ε | **ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** | “EXTERNAL WIN” as delivered (no DOI) / “open arithmetic” / “unverified” |
| bbnfix | **NOT YET** | “delivered” / “booked” / quote H₀ |
| T14 production | **KILLED** | “production closed” / sky win |
| T14 candidate | **config-local closed** | “universe is GP” / cosmology H |
| arXiv | **HOLD** | “posted” without endorsement |

---

## What three wins buy (honesty)

Even if all three external ranks eventually land, **unified** package remains candidate-grade: D2–D9 open arms (except D8 parked) stay open. Hard wins buy **external load-bearing surfaces**, not TOE closure.

*End HARD_WINS_TABLE.*
