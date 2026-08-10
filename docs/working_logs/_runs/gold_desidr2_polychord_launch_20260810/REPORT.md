# Gold DESI-DR2 SH0ES PolyChord launch — 2026-08-10

**Status:** **LAUNCHED (process)** — no nested ΔlnZ yet.

| leg | instance | type | yaml |
|---|---|---|---|
| SH0ES dyad | `i-04ead482af737e7bf` | c6i.24xlarge (96) | `dyad_mnu_bbnfix_desidr2_ev.yaml` |
| SH0ES lcdm | `i-0e353f38544397a6d` | c6i.24xlarge (96) | `cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml` |

- AMI: `ami-0162f91b5bf4fbea6` (stack)
- Ranks: 96 per host; OMP_NUM_THREADS=1
- DESI BAO likelihood initialized on dyad host ranks (live)
- TRGB pair: **not launched**
- Quota: on-demand **300** vCPU (approved)

**Forbidden:** invent nested ΔlnZ; mix with old-BAO booked GetDist; claim win from MCMC alone.

