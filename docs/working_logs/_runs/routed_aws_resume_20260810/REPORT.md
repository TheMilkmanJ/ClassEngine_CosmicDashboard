# Route-D AWS resume — 2026-08-10

**Instance:** `i-0c65cc61a575bdfa7` (`prtoe-routed-96`) **c7i.24xlarge** (96 vCPU)  
**AMI:** `ami-0162f91b5bf4fbea6` (stack)  
**Resume:** `cobaya.run -r cmp_prtoe_routeD.input.yaml`  
**MPI ranks:** **3** (checkpoint `mpi_size: 3` — cannot change on resume without restart)  
**OMP_NUM_THREADS:** **32** (3×32 = 96 vCPU full blast for CLASS)  
**Started:** ~2026-08-10T16:20:47Z  

## Prior state (resume from)
- N = 16085, R−1 = **0.3898**, stop = **0.1** (~3.9×)
- Best earlier: R−1 = 0.257 @ N=11422 then bounced up
- Local laptop was 3 ranks × low OMP; this is same ranks, **much higher OMP**

## Ops notes
- DESI Hessian box `i-096d08d2dc9d8f42c` **stopped** to free quota
- Gold PolyChord 2×96 **left alone**
- Quota use: 96+96+96 = **288 / 300**
- Gate: R−1 < 0.1 + converged — **not bookable until then**
- Do not mix with bbnfix evidence

## S3
- Chains: `s3://…/routed_resume/routed_resume.tgz`
- Bootstrap: `scripts/start_routed_resume.sh`

*NO FABRICATIONS. ETA unknown; faster CLASS ≠ guaranteed overnight dual-gate.*
