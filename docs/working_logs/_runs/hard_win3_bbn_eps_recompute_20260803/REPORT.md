# Hard Win 3 — BBN ε bound external recompute (2026-08-03)

**Claim (outsider-recomputable):** At T_c = 179 keV, a linear helium response
dY_p/dε = 0.00163 per %ε and Aver et al. Y_p = 0.2453±0.0034 imply
**ε < 3.2% (2σ)** with zero free parameters. Framework not required.

## Arithmetic

| quantity | value |
|---|---:|
| Y_p⁰ (ε=0) | 0.246891 |
| Y_p (ε=1.2543%) | 0.248995 |
| dY_p/dε audit | 0.001677 / %ε |
| dY_p/dε paper | 0.00163 |
| Aver Y_p | 0.2453 ± 0.0034 |
| ε 1σ ceiling | 1.110% |
| ε 2σ ceiling | 3.196% |
| paper claim 2σ | 3.20% |
| match | **PASS** |
| EMPRESS pull at ε=0 | +2.91σ (cannot bound ε) |

## Kill criteria

- If Aver central/error updates such that 2σ ceiling moves >50% relative, re-book.
- If network elasticity re-run changes dY_p/dε by >20%, re-book.
- EMPRESS never used as upper limit (ε=0 already discrepant).

## External recompute recipe

```bash
python3 - <<'PY'
Yp0, dY, Aver, sig = 0.246891, 0.00163, 0.2453, 0.0034
print((Aver + 2*sig - Yp0)/dY)
PY
```

Expected ≈ **3.20%**.

## Status vs ChatGPT 4/10

This is a **thin constraint win** (claim credibility path), not a TOE claim.
Package: `papers/bbn-eps-bound/` / `docs/arXivReady/bbn-eps-bound.tar.gz`.
