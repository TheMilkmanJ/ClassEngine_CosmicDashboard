# T14 H_kin recompute recipe (thread-closure; not top external win)

**Outsider path:** no PRTOE cosmology ontology required — pure GP + geometry.

## Recompute

```bash
# from repo root; ~minutes at 64³ smoke, hours at 128³
python3 scripts/ring_toroidal_hkin.py --calibrate
python3 scripts/ring_toroidal_hkin.py --smoke --null nowinding --out /tmp/t14_null_nw
python3 scripts/ring_toroidal_hkin.py --smoke --null nojet --out /tmp/t14_null_nj
python3 scripts/ring_toroidal_hkin.py --smoke --out /tmp/t14_four
# production (owner A4):
# bash scripts/run_t14_i6_production.sh --i-approve-a4
```

## Acceptance (Claude i5/i6)

| Check | Fence |
|---|---|
| Cal planar + helix | PASS |
| nowinding \|H\| and flip residual | < 0.2 |
| nojet | no false ring |
| True-mirror residual | smoke <10%; **prod target <5%** |
| Margins | \|H\| > 3× dial_spread |
| Selector | outcome-blind (no Tw/Wr/H in key) |
| Pattern | H ≈ sign(n)·2 (smoke-grade booked) |

## Artifacts when A4 finishes

`docs/working_logs/_runs/t14_hkin_i6_prod_*/` — summary.json, series, psi_*.npy

## Non-claim

Config-local instrument result. Not a sky-facing IGMF magnitude claim. Not ChatGPT-ranked top external win (thread-closure).

## Production A4 result (2026-08-03 14:44)

**Run:** `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/four_branch/`  
**elapsed_s:** 9009  

| branch | t | H | n_cand |
|---|---:|---:|---:|
| n+1_f+1 | 1.00 | +1.9331 | 5 |
| n+1_f-1 | 0.25 | +2.0000 | 2 censored |
| n-1_f+1 | 1.00 | −1.9929 | 5 |
| n-1_f-1 | 0.25 | −2.0000 | 2 censored |

Mirrors: **3.40%** / **0.36%** (target &lt;5% PASS).  
sign(H)/sign(n)=+1 all four.  

**Booking:** instrument says candidate-grade config-local; **blue production sign NOT booked** (cond.2 both f−1). Red C1 owed.  
**Non-claim:** not sky IGMF; not ChatGPT top external win (thread-closure).

## RED fullTC disposition (2026-08-03 14:46)

Production sign **KILLED**. Quote only restated candidate text in `CANDIDATE_BOOKING_RESTATED.md`.  
Matched-t winding mirror 3.04% only. f−1 arms disclosure-only. Smoke i5 stands.
