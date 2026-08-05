# Dense ε_max(T_c) grid — SKIP (cores not free)

**Date:** 2026-08-05  
**Plan:** `docs/working_logs/_runs/bbn_eps_max_grid_20260803/REPORT.md` (~35–45 min serial)  
**Decision:** **not run**

## Why

| check | value |
|---|---|
| load average | ~12 |
| live heavy python ranks | multiple ~108% classy/MCMC workers |
| user rule | run grid **only if cores free** |

**Stamp:** residual remains **UNVERIFIED** for dense ε_max(T_c) curve. Paper bound at measured T_c stands. Not a Zenodo hold.

When free:
```bash
# see bbn_eps_max_grid_20260803/REPORT.md acceptance criteria
```

*NO FABRICATIONS. No invented ε_max table.*
