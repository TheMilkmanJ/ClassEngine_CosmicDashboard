# R1-t14-i6 A4 production — grade update (2026-08-03 ~12:15 MDT)

**NO FABRICATIONS.** Numbers from console / `summary.json` only.  
**Run:** `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/`

## Pipeline

| Step | Status | Evidence |
|---|---|---|
| [1/4] calibrate | **PASS** | `calibrate.log` |
| [2/4] null nowinding | **DONE** | `null_nowinding/summary.json` elapsed **5684 s** |
| [3/4] null nojet | **DONE** | `null_nojet/summary.json` elapsed **5622 s** |
| [4/4] four-branch | **IN FLIGHT** | n+1_f+1 + n+1_f-1 VERDICT; n-1_f+1 running; no summary.json |

## Null nojet (production 128³) — COMPLETE

| Branch | Verdict | Result |
|---|---|---|
| n+1_f+1 | **null** all t∈[0.25,1.50] `----` | no false ring |
| n−1_f+1 | **null** all t∈[0.25,1.50] `----` | no false ring |

Booking string: **`nothing graded (no ring / no verdict frame)`**  
Drift at late times large (t=1.50 ~387%) but **no ring** → null fence **PASS** at production grid.

True-mirror N/A on nojet (no verdicts). Same as smoke nojet grade; **does not pre-credit four-branch**.

## Null nowinding — COMPLETE (unchanged)

| Branch | t | H | drift | notes |
|---|---:|---:|---:|---|
| n+0_f+1 | 1.0 | ~1.87e−15 | 3.98% | 5 candidates; margin_ok=false expected |
| n+0_f−1 | 0.25 | 0.0 | 7.31% | **2 candidates**; mid-frames nphase&lt;12/16 NaN; instrument-censored |

Gate: NaN when `nphase < 12/16` (`ring_toroidal_hkin.py:298`).

## Gates vs i6 / Claude conditions 1–6

| Gate / condition | Status |
|---|---|
| Calibrate | **PASS** |
| nowinding H~0 selected | **PASS** (with f−1 instrument-censored disclosure) |
| nojet no false ring | **PASS** |
| True-mirror &lt;5% | **TBD** four-branch |
| Margins four-branch | **TBD** |
| Blind selector | held on recorded SELECTED lines |
| Cond 1 NaN wording | cured in docs |
| Cond 2 candidate-pool + instrument-censored | armed for full TC |
| Cond 3–6 | armed for full TC |

## Non-claims

- **No production sign(H vs n) booking** until four-branch summary + gates.
- Smoke revalidate does not substitute for this production four-branch.
- **4/10 stands**; story-grade corpus lock is separate discipline work.

## Next

Fill `t14_i6_TC_SKELETON.md` + TASK COMPLETE R1-t14-i6 **only** from `four_branch/summary.json` when written. Claude C1 armed; ChatGPT REMAND production booking until then.

## Continuous update (14:06)

- n-1_f+1 advanced through t=1.25 (cand H≈−2.204); t=1.50 computing
- n+1_f-1 remains **2-cand instrument-censored**
- Booking stance prewrite: `../t14_i6_BOOKING_STANCE_PREWRITE.md`
- No production booking

## FULL TC COMPLETE (14:45)

See `FULL_TC_REPORT.md` + `../t14_i6_TC_GATES.md`.

- four_branch/summary.json elapsed 9009s
- Mirrors 3.40% / 0.36% PASS
- Both f−1 **2-cand censored**
- Production sign **NOT booked**
- Red C1 owed
