# Reproducibility freeze — Stage A + nested yamls — 2026-08-13

**Purpose:** Immutable snapshot of the production likelihood yamls, nested EV yamls, and driver scripts used for the challenge paper and nested campaign.  
**Not:** chain binaries (too large; live on EC2 / S3).  
**Not:** nested ΔlnZ (still OPEN-MACHINE).

## Contents

| Path | Role |
|------|------|
| `yamls/*.yaml` | Frozen copies of Stage A + EV + zon_disp yamls |
| `pypolychord_cobaya.py` / `ultranest_cobaya.py` | Nested drivers at freeze |
| `MANIFEST.json` | SHA-256 of every frozen file + authority booking JSONs |

## Reproduce Stage A posteriors (local or EC2)

```bash
# after packages_path rewrite to host home
python -m cobaya.run dyad_mnu_bbnfix_desidr2.yaml
python -m cobaya.run cmp_lcdm_mnu_bbnfix_desidr2.yaml
# TRGB twins:
python -m cobaya.run dyad_mnu_bbnfix_desidr2_trgb.yaml
python -m cobaya.run cmp_lcdm_mnu_bbnfix_desidr2_trgb.yaml
# GetDist ignore_rows=0.3 on ≥3 ranks — see docs/PRTOE_CHAIN_TABLES.md
```

## Reproduce nested (engine settings)

**UltraNest:** `nlive=400`, `frac_remain=0.01`, step sampler, 96 ranks, `scripts/ultranest_cobaya.py`  
**PolyChord GIL:** `nlive=500`, `nprior=500`, `num_repeats=5*ndim` (65 dyad / 60 lcdm), `precision=0.001`, `synchronous`, `scripts/pypolychord_cobaya.py` under `prterun -n 96`

PolyChord production tree must include the **Still Active** format-comma patch in `read_write.F90` (see rescue 2026-08-13 on `i-0941e936fd100c309`).

## Authority numbers

| Stack | Authority |
|-------|-----------|
| SH0ES H0 / S8 | `docs/working_logs/_runs/bbnfix_booking_desidr2_sh0es_20260811_094254/` |
| TRGB H0 / S8 / ⟨χ²⟩ | `docs/working_logs/_runs/trgb_results_20260812/` |
| Chain tables | `docs/PRTOE_CHAIN_TABLES.md` |

## Verify freeze integrity

```bash
python3 - <<'PY'
import json, hashlib
from pathlib import Path
m = json.loads(Path('docs/working_logs/_runs/repro_freeze_20260813/MANIFEST.json').read_text())
for rel, meta in m['files'].items():
    if meta.get('missing') or 'sha256' not in meta: continue
    p = Path('docs/working_logs/_runs/repro_freeze_20260813/yamls') / Path(rel).name
    if not p.exists():
        p = Path('docs/working_logs/_runs/repro_freeze_20260813') / Path(rel).name
    if not p.exists():
        p = Path(rel)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    ok = h == meta['sha256']
    print(('OK' if ok else 'MISMATCH'), rel)
PY
```
