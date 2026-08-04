# Model improvement board — every step except PolyChord

**Date:** 2026-08-03 night  
**Owner order:** improve the model; **do every required step except PolyChord**.  
**Fairbank/arXiv:** still owner HOLD (packages ready; no chase).  
**Full no-PolyChord matrix:** `MODEL_IMPROVE_NO_POLYCHORD_20260803.md`

**Hard rules:** NO FABRICATIONS · **no PolyChord** · leave cobaya MCMCs alone · OMP=1/nice · no premature CANDIDATE · booking only after **R−1 &lt; 0.05 AND self-stop** (both).

---

## Ranking (active)

| Pri | Win / lever | Owner | Status |
|---:|---|---|---|
| — | **arXiv / Fairbank packages** | Owner | **HOLD** — wait Fairbank response (not chased here) |
| **1** | **bbnfix posterior booking readiness** | Blue | Preflight + finalize hardened (R−1 **and** self-stop); gate not met |
| **2** | **BBN ε recompute card** | Blue | **PASS** kept (3.196%≈3.20%) |
| **3** | **Page co-evolution under T8** | Blue | **coevolve_v1** write-once; **T8_pass True**; stall_cap still fails → no CANDIDATE; claimed false |
| **4** | **Fence clarity** (dark-sector / seating) | Blue | Stamp + Claude R-E CONFORMS |
| **5** | **Theory walls honest queue** | Blue | Status-only; no invented closes |
| **6** | **C-code LEGACY_ST vs CURRENT_CORE** | Blue | **DONE** labels + rename |
| **7** | **Claude red cures** | Blue | **APPLIED** (T3 du-gate, immutability, booking, rename) |
| **8** | **Promote what can** | Blue | **DONE** — see `PROMOTION_BOARD_20260803_IMPROVE.md` (A4 candidate, BBN ε win, Koide (c), Page T8 instrument, …) |
| — | **PolyChord** | — | **SKIP** (this box) |

---

## 1. bbnfix booking (do not book yet)

| Item | Value (2026-08-03 ~23:05 local progress) |
|---|---|
| `cmp_lcdm_mnu_bbnfix` R−1 | **0.059** (bounced above 0.05; `converged: false`) |
| `dyad_mnu_bbnfix` R−1 | **0.189** (`converged: false`) |
| Rank files | both have `{1,2,3}.txt` |
| `finalize_h0_at_convergence.py` | **NOT YET** (refuses correctly) |
| GetDist | `make_getdist_tables.py --include-bbnfix` only after both R−1 &lt; 0.05 |

**When both R−1 &lt; 0.05 and preferably self-stop:** run `_POSTERIOR_BOOKING_CHECKLIST.md` → GetDist three-rank → one-page recompute card → then tables. **No peek H₀.**

Detail: `hard_wins_90day_20260803/BBNFIX_BOOKING_PREFLIGHT.md`

---

## 2. BBN ε (ARITHMETIC VERIFIED internal; EXTERNAL WIN PENDING no DOI)

- Card: `hard_win3_bbn_eps_recompute_20260803/`  
- ε 2σ ≈ **3.196%** ≈ paper 3.20% — **PASS** (internal arithmetic)  
- Kill criteria not tripped; keep card; do not re-litigate without new data.  
- **EXTERNAL WIN PENDING (no DOI)** — Zenodo one-record public ship still owed.

---

## 3. Page / R-PAGE

| Item | State |
|---|---|
| T8 + claim-decoupling | **ACTIVE / BINDING** |
| Co-evolution script | `scripts/quantum_page_coevolve.py` |
| Scorecard | `scripts/page_protocol_scorecard.py` (T8 gates binding CANDIDATE score) |
| `page_curve_claimed` | **false** |
| Standing CANDIDATE | **none** (denied ×3; coevolve does not auto-file) |

---

## 4. Fence clarity

PRTOE = dark-sector cosmology of expansion; local bound matter / atomic QM **seated** on SM unless a foundations program pays. See `FENCE_CLARITY_STAMP_20260803.md`.

---

## 5. Theory walls (honest; no invent)

| Wall | Action allowed now |
|---|---|
| DE self-tune | Status only — still open joint |
| Bounce turn H&gt;0 | Floor derived; turn not derived |
| MEDR / pair H | MISSING_INPUT — no formula invent |
| Born / atom | Desk done; derivation blocked |

Detail: `THEORY_WALLS_QUEUE_20260803.md`

---

## Explicit non-goals under this board

- arXiv chase / Fairbank follow-up emails  
- Peek-booking H₀ or bbnfix tables  
- Page CANDIDATE filing without T1–T8 + claim-decoupling + red  
- Inventing medium \(r\), Born, or atomic QM  

*NO FABRICATIONS.*
