# AWS Spot MCMC resume — 2026-08-07

## Instance

| field | value |
|---|---|
| InstanceId | `i-0b3afa463aded5fb2` |
| Name | `prtoe-dyad-spot-final` |
| Type | `c7i.24xlarge` (96 vCPU) |
| Lifecycle | **spot** |
| AZ | `us-east-1c` |
| Public IP (at launch) | `98.90.196.48` |

## What was wrong

The Spot AMI was PolyChord-oriented: **no** `dyad_mnu_bbnfix` / `cmp_prtoe_routeD` chain files or yamls on disk. Earlier on-demand attempts also died on hardcoded laptop paths (`/home/themilkmanj/cobaya_packages_clean/...`).

## What we did

1. Staged local chain state + input/updated yamls for `dyad_mnu_bbnfix` and `cmp_prtoe_routeD`.
2. Rewrote `/home/themilkmanj/` → `/home/ubuntu/` in those yamls.
3. rsync'd into `/home/ubuntu/prtoe_class/chains/` (and root yamls).
4. Resumed at **3 MPI ranks** each (checkpoint `mpi_size: 3` — rank count must not change):

```bash
cd /home/ubuntu/prtoe_class/chains
source ~/venv/bin/activate
OMP_NUM_THREADS=1 mpirun --use-hwthread-cpus -n 3 --bind-to none \
  python -m cobaya.run -r dyad_mnu_bbnfix.input.yaml
# same for cmp_prtoe_routeD.input.yaml
```

## Live truth at resume (~2026-08-07 00:41 UTC)

- **dyad_mnu_bbnfix**: `Resuming from previous sample!` — loaded 10950 / 10908 / 11034 points; **Sampling!**
- **cmp_prtoe_routeD**: `Resuming from previous sample!` — loaded 5665 / 5852 / 6220 points; **Sampling!**
- 3+3 cobaya ranks alive; not bookable (dual-gate unchanged)

## Booking gate (unchanged)

Still **REFUSED** until both bbnfix legs have R−1 < 0.05 **and** `converged: true`. lcdm twin already self-stopped locally; model leg is the blocker. routeD is a separate instrument (stop 0.1).

**Do not treat Spot speed as PASS. exit0 ≠ PASS. No COMPLETE from this resume.**

## Not started here

- `cmp_lcdm_mnu_bbnfix` (already `converged: true` — control leg ready; pair still closed)
- PolyChord evidence pair (separate; prior Fortran/segfault issues on other boxes)
