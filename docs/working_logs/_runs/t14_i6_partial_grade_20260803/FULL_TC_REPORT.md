# R1-t14-i6 FULL TC REPORT — from disk (2026-08-03 14:43)

**NO FABRICATIONS.** Sources: `four_branch/summary.json` + console + auto gates.

## Pipeline
| Step | Result |
|---|---|
| [1/4] cal | PASS |
| [2/4] nowinding | PASS (f−1 2-cand disclosed) |
| [3/4] nojet | PASS no false ring · Claude AGREE |
| [4/4] four-branch | **DONE** elapsed **9009 s** |

## Four-branch selected
| branch | t | H | ampA | n_cand | margin_ok |
|---|---:|---:|---:|---:|---|
| n+1_f+1 | 1.00 | +1.9331 | 1.696 | **5** | True |
| n+1_f-1 | 0.25 | +2.0000 | 0.00122 | **2 censored** | True |
| n-1_f+1 | 1.00 | −1.9929 | 1.418 | **5** | True |
| n-1_f-1 | 0.25 | −2.0000 | 0.000865 | **2 censored** | True |

## Mirrors
| pair | residual | t match |
|---|---:|---|
| (1,1)↔(−1,−1) | **3.40%** PASS (&lt;5%) | **mismatched-t** 1.00 vs 0.25 |
| (1,−1)↔(−1,1) | **0.36%** PASS (&lt;5%) | **mismatched-t** 0.25 vs 1.00 |

## Sign pattern (all four)
sign(H)/sign(n) = **+1** every branch at selected frame.

## Instrument booking string
`overall sign BOOKABLE at candidate grade (configuration-local only)`

## Blue booking stance (conditions 1–6)
| Cond | Result |
|---|---|
| 1 NaN gate nphase&lt;12/16 | held (mid-frame NaNs on f−1 arms) |
| 2 ≤2 cand → censored | **TRIGGERED** on **both** f−1 arms |
| 3 member t / mismatched-t | **both mirror pairs mismatched-t** |
| 4 ampA not helA | ampA quoted (f−1 ampA≪1) |
| 5 nowinding disclosure | paid earlier |
| 6 no production sign unless gates | **Production sign NOT BOOKED by blue** |

**production_auto_eligible = False** (mirror_ok AND margins BUT censored rows).

### What blue will claim
- Instrument fidelity TC: four verdicts + mirrors &lt;5% + margins + nulls — **on disk**.
- Sign pattern observed at selected frames: H≈sign(n)·2 class — **candidate-grade only**, as instrument string says.
- **Not** an unconditional production upgrade of smoke-grade sign booking without red disposition of censored f−1 arms and mismatched-t.

### Non-claims
Not sky IGMF · not top external win · config-local · 4/10 stands · Page OPEN

Artifacts:
- `t14_i6_TC_FROM_DISK.md`
- `t14_i6_TC_GATES.md`
- `t14_i6_TC_SKELETON.md`
- `four_branch/summary.json`

## RED VERDICT disposition (14:46)

**Ruling:** AGREE-IF — production sign **KILLED**; candidate booking only on RESTATED text.

See `CANDIDATE_BOOKING_RESTATED.md`.

Key red findings adopted:
1. f−1 selected rows = input restatement (ampA~1e−3, H=±2 pure mutual) — not ring measurements
2. Fountain-down mirror half **UNMEASURED** (real rings at late t have NaN H)
3. Prior 3.40%/0.36% mismatched-t mirrors **VOID** as ring-physics; replace with matched-t winding mirror **3.04%**
4. |H|≈2 time-windowed t≤1.25
5. sign(H)=sign(n) **14/14** quotable frames survives

Production booking: **not granted**.
