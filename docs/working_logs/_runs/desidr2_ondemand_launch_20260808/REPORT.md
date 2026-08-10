# DESI-DR2 bbnfix twin launch — on-demand (2026-08-08)

## Instance

| field | value |
|---|---|
| InstanceId | `i-096d08d2dc9d8f42c` |
| Name | `prtoe-pc-probe` (reused on-demand) |
| Type | `c7i.8xlarge` (32 vCPU) |
| Lifecycle | **on-demand** (not Spot) |
| Public IP | `100.48.192.31` |
| AZ | us-east-1a (from describe) |

## Configs (local + remote)

- `dyad_mnu_bbnfix_desidr2.yaml` — model leg
- `cmp_lcdm_mnu_bbnfix_desidr2.yaml` — ΛCDM+m_ν twin
- **Only BAO change** vs production bbnfix: `bao.desi_dr2.desi_bao_all` replaces 6dF+MGS+DR12
- Covmat seeds from booked old-BAO pair
- Paths rewritten `/home/themilkmanj` → `/home/ubuntu` on box

## Launch

```text
mpirun --use-hwthread-cpus -n 3 --bind-to none \
  python -m cobaya.run dyad_mnu_bbnfix_desidr2.yaml
# same for cmp_lcdm_mnu_bbnfix_desidr2.yaml
```

- Launched ~2026-08-08T01:10 UTC
- Both legs **Sampling** after burn-in (lcdm already writing rank files by 01:26)
- dyad still finishing burn-in / early samples at last check
- Dual gate for **this** pair is separate from booked old-BAO pair:
  R−1 < 0.05 **and** `converged: true` on **both** desidr2 legs before any booking

## Not claims

- Not bookable yet
- Does not replace the booked old-BAO bbnfix GetDist tables
- No COMPLETE; speed ≠ PASS
