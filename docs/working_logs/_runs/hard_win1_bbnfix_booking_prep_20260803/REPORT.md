# Hard Win 1 — bbnfix pair booking prep

| chain | N | R−1 | stop | ready |
|---|---:|---:|---:|---|
| cmp_lcdm_mnu_bbnfix | 16075 | 0.0539 | 0.05 | NO |
| dyad_mnu_bbnfix | 15969 | 0.1910 | 0.05 | NO |

**Both ready for GetDist booking:** **NO — wait**

## When ready (do not run early)

```bash
# from repo root; requires getdist
python3 - <<'PY'
from getdist import loadMCSamples
import numpy as np
for root in ["chains/dyad_mnu_bbnfix", "chains/cmp_lcdm_mnu_bbnfix"]:
    s = loadMCSamples(root, settings={"ignore_rows": 0.3})
    for p in ["H0", "m_ncdm", "omega_b", "S8"]:
        if p in s.getParamNames().list():
            m = s.mean(p); e = s.std(p)
            print(f"{root} {p}: {m:.4g} ± {e:.4g}")
PY
```

## External claim (when booked)

Matched-likelihood dyad vs ΛCDM+m_ν posteriors under DESI+Planck+ACT+SPT+SN+BBN prior.
Kill: if R−1 quoted while >0.05, or if chains mixed without burn-in statement.

## Non-claim

Do **not** book RouteD thaw until its own R−1 and basin checks pass.
