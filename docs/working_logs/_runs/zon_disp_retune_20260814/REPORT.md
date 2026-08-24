# zon_disp MCMC — stop + retune (2026-08-14)

**Class:** ops rescue (optional research lane)  
**Not:** nested ΔlnZ booking · gold Stage A

## Action taken

| Step | Status |
|------|--------|
| Stop `cobaya.run cmp_prtoe_zon_disp` on `i-090c0275d8198ae14` | **done** (N_COB=0) |
| Harvest 48 chain files + progress + covmat on box | **done** → `docs_runs/zon_disp_20260813/harvest_20260814T200340Z` |
| Pull progress/covmat/yaml smalls locally | **done** (this package) |
| S3 backup (smalls) | **ok** — `s3://prtoe-chains-…/zon_disp_retune_20260814/zon_disp_harvest_small.tgz` |
| S3 full chains from instance role | **denied** (SSM role no `s3:PutObject`); full 48× chains remain on **stopped instance EBS** under harvest dir |
| Install covmat for relaunch | `chains/zon_disp_from_run_20260814.covmat` |
| Draft retune YAML | `cmp_prtoe_zon_disp_retune.yaml` (+ copy in this package) |
| Stop EC2 instance (cost) | **requested** (stop, not terminate) |

## Final mid-run state (stopped)

| Metric | Value |
|--------|------:|
| Last N | 318437 |
| Last R−1 | **187.79** |
| Acceptance | ~0.971 |
| Stop target was | R−1 ≤ 0.05 |
| Trajectory | 3234 → 188 (improving, flattening) |

## Why stop

- Unlikely to hit 0.05 before sample budget at observed slope.
- `learn_proposal_Rminus1_max: 2.0` blocked proposal learning for entire run.
- Acc ~0.97 + high R−1 ⇒ under-mixing, not “almost done.”
- Free ×48 c7i.12xlarge while nested twins remain the priority.

## Retune deltas (next launch)

| Knob | Old | New |
|------|-----|-----|
| `learn_proposal_Rminus1_max` | 2.0 | **50** |
| `learn_proposal_Rminus1_max_early` | 2.0 | **100** |
| `covmat` | `zon_disp_seed.covmat` | **`zon_disp_from_run_20260814.covmat`** |
| `max_samples` | 40000 | **80000** |
| `burn_in` | 40 | **100** |
| `log10_zon` proposal | 0.08 | **0.12** |
| `dcdf_rho_inf` proposal | 0.02 | **0.03** |
| `output` | `chains/cmp_prtoe_zon_disp` | **`chains/cmp_prtoe_zon_disp_retune`** |

Original `cmp_prtoe_zon_disp.yaml` **unchanged** (audit trail).

## Relaunch (when ready)

Do **not** auto-relaunch unless asked. Suggested:

```bash
# on a fresh/stopped-started zon box, after syncing repo + covmat
prterun -n 48 python -m cobaya.run cmp_prtoe_zon_disp_retune.yaml
```

Watch R−1: expect faster drop once proposal learning engages below 50.

## Stamp

| Field | Value |
|-------|--------|
| package | `zon_disp_retune_20260814` |
| host | `i-090c0275d8198ae14` `prtoe-zon-disp-ac-48` |
| bookable_posterior | **false** |
| next | optional relaunch with retune YAML |

## Relaunch executed (2026-08-14 ~20:28 UTC)

| Field | Value |
|-------|--------|
| Host | `i-090c0275d8198ae14` `prtoe-zon-disp-ac-48` **started** |
| Ranks | **48** (remaining free after nested: 64 vCPU; used 48, ~16 spare) |
| Command | `prterun -n 48 python -m cobaya.run cmp_prtoe_zon_disp_retune.yaml` |
| Workers at peel | **49** (prterun + 48 cobaya) |
| Log | `/home/ubuntu/docs_runs/zon_disp_retune_20260814/zon_disp_retune.run.log` |
| Output | `chains/cmp_prtoe_zon_disp_retune.*` |
| Status | **LIVE** — initial points accepted; measuring speeds |

Notes: first attempts failed (root HOME / candl path / resume lock); fixed by ubuntu+venv, path rewrite, archive of failed retune outputs.
