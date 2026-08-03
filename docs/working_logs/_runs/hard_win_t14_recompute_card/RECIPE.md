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
