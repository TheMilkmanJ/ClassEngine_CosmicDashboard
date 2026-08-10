# Gold PolyChord stall diagnosis — 2026-08-10 ~18:50Z

## Verdict

**STALL CONFIRMED on both SH0ES gold legs.**  
Processes are **CPU-hot** but **dead-point files have not advanced for ~11 hours**.  
Mid-run `log(Z)` is **not bookable**.  

## Instances

| leg | instance | type | yaml |
|---|---|---|---|
| SH0ES dyad | `i-04ead482af737e7bf` | c6i.24xlarge (96) | `dyad_mnu_bbnfix_desidr2_ev` |
| SH0ES lcdm | `i-0e353f38544397a6d` | c6i.24xlarge (96) | `cmp_lcdm_mnu_bbnfix_desidr2_ev` |

Both: `prterun -n 96` + `cobaya.run -r …` live; host load ≈ 96–98.

## Dead-file freeze

| leg | dead lines | last mtime (UTC) | mid-run log(Z) in `.stats` |
|---|---:|---|---|
| dyad | **4595** | **2026-08-10 07:34:40** | −6605.59 ± 0.83 |
| lcdm | **4595** | **2026-08-10 07:15:46** | −3798.69 ± 0.81 |

Resume launched ~**15:08Z** (launchlog + dir mtime). By **18:50Z** (~3.7 h of this resume) **zero new dead points**.  
Phys_live / resume / stats share the same frozen timestamps.

## Launchlog (both)

PolyChord 1.20.1, nlive=500, clustering on, synchronous parallelisation:

```
Resuming from previous run
number of repeats: …
started sampling
```

No further progress lines after “started sampling”.

## Process state sample (dyad)

| pid class | wchan | note |
|---|---|---|
| prterun | `ep_poll` | sleeping |
| many python ranks | `futex_do_wait` | blocked |
| some python ranks | `R` (running) | high nonvoluntary ctxt switches |

Consistent with **MPI ranks waiting on a barrier / load imbalance**, not clean I/O-bound nested progress.  
`strace` attach from SSM worker failed (pid churn / no ptrace) — non-blocking for verdict.

## What this is **not**

- Not a finished nested pair  
- Not a bookable ΔlnZ (and dyad vs lcdm mid-run Z are not comparable)  
- Not “just slow” after 11 h with dead frozen through a multi-hour resume

## Decision (2026-08-10)

1. **Do not** quote mid-run log(Z) or invent ΔlnZ.  
2. **Clean re-resume** both legs from existing `.resume` (kill prterun/cobaya, restart same `-r` yaml, same 96 ranks).  
3. **Watch 90–120 min:** dead line count **must** increase.  
4. If still frozen after re-resume + 2 h → **stop both instances** (save cost) and open a root-cause ticket (path/write, PolyChord MPI hang, single-rank smoke).  
5. TRGB legs remain **not launched** until SH0ES pair is healthy or deliberately abandoned.

## Action taken this package

1. Confirmed stall (dead frozen 11h; futex/R mix).  
2. Killed stalled trees.  
3. Re-resume required **three** fixes stacked: run as `ubuntu` (HOME), cobaya **`-r`**, and `GLIBC_TUNABLES=glibc.rtld.execstack=2` for `libchord.so`.  
4. Both legs **live again** ~19:04Z (96 ranks, high CPU). Dead still 4595 at start of re-resume — progress watch required.  
5. Full command log: `ACTION.md`.

*NO FABRICATIONS. Mid-run log(Z) still not bookable until clean finish.*
