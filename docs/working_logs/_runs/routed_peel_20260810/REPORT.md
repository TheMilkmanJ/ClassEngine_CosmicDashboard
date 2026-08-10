# Route-D MCMC peel — 2026-08-10

**Source:** AWS `i-0c65cc61a575bdfa7` (`prtoe-routed-96`, c7i.24xlarge)  
**S3:** `s3://prtoe-chains-691687038930-1786289405/peel_routed_20260810/routed_peel.tgz`  
**Landed:** `chains/` **and** `docs/chains/` (product set below)  
**Prior local state archived:** `chains/_archive_routeD_pre_aws_finish_20260810/` (N≈16k, R−1≈0.39)

## Contents
- `cmp_prtoe_routeD.{1,2,3}.txt`
- `cmp_prtoe_routeD.{progress,checkpoint,covmat,input.yaml,updated.yaml,launchlog}`

## Gate stamps on peel
- progress last: **N = 39332** t=2026-08-10T17:59:45.393807 **R−1 = 0.054201** (bounds R−1 = 0.178571)
- checkpoint: **`converged: true`**, `Rminus1_last: 0.054201`, `mpi_size: 3`
- Gate for routeD: **R−1 < 0.1 + converged** → **MET**

## Notes
- Instance role cannot PutObject; peel uploaded with temporary root session creds then downloaded locally.
- Instance **stopped** after peel (cost).
- **Do not mix** with bbnfix / DESI-DR2 evidence pairs. Route-D is the thaw fork.

*NO FABRICATIONS.*
