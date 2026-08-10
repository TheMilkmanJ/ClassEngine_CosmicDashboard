# DESI-DR2 FD Hessian Laplace — launch — 2026-08-10

**Why:** DESI-DR2 bbnfix pair dual-gate met and Stage A booked
(`desidr2_bbnfix_booking_20260810_053127`). Idle 48-vCPU box reused for DESI FD Hessian.

| | |
|---|---|
| Instance | `i-096d08d2dc9d8f42c` (`prtoe-desidr2-hessian-48`) c7i.12xlarge |
| Script | `scripts/bbnfix_hessian_laplace.py --which desi --step-frac 0.05` |
| Chain dir | `/home/ubuntu/prtoe_class/chains` |
| OMP | 46 |
| Log | `.../credibility_diagnostics_20260808/hessian_desi_run.log` |
| Out | `.../credibility_diagnostics_20260808/hessian_laplace_desi.json` |
| Started | ~2026-08-10T15:46Z |
| PID | 2157 (at launch) |

**Process stamp:** likelihoods init OK; dyad MAP `mlp=1375.803`; FD steps applied.

**Not nested. Not bookable until JSON lands and owner/red review.**  
Pull with SSM/S3 when done; stop instance to save cost.

*NO FABRICATIONS.*
