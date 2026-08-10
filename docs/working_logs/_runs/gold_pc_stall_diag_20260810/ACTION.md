# Gold PC re-resume action log — 2026-08-10

## Decision
STALL CONFIRMED → kill stalled trees → clean re-resume both legs from existing `.resume`.  
Watch: dead line count must increase within **90–120 min**. If still 4595 after 2 h, stop both instances.

## SSM / action sequence

1. **Stall confirmed** while both prterun trees were CPU-hot (dead=4595 frozen ~11h).
2. **Kill succeeded** (both trees CLEAN) — command `5cebb827…` / `d5598f0c…`.
3. **Root relaunch FAILED** — OpenMPI `Unable to get the user home directory` / prterun segfault when SSM runs as root.
4. **Ubuntu relaunch without `-r` FAILED** — cobaya: *Delete previous output… or request resuming (`-r`)*.  
   Commands: dyad `3180125c…` / lcdm `a0f6c825…`.  
5. **Explicit `-r` as ubuntu+venv FAILED** — `ImportError: libchord.so: cannot enable executable stack as shared object requires: Invalid argument`  
   (processes that were already loaded kept running after morning resume; kill → cannot reload libchord without execstack allowance)  
   Commands: `21a81327…` / `8a206d55…`
6. **Execstack-tunable relaunch SUCCESS** (`GLIBC_TUNABLES=glibc.rtld.execstack=2` + `-r` + ubuntu + venv):  
   - dyad `32740f90-be56-4b5a-969b-7d236e501b50` — `pypolychord_OK`; prterun 96 live @ ~98%  
   - lcdm `d45359bf-0f5c-42bf-9374-724060f5d201` — same  
   Log: `chains/*reresume_20260810e.log`  
   Started ~19:04Z. Dead still 4595 at launch — **watch for advance**.

### Root causes (stacked)
| Fail | Cause |
|---|---|
| Root prterun | OpenMPI needs user `HOME` (`ubuntu`) |
| Launch script | Did not pass cobaya `-r` |
| `-r` import | `libchord.so` requires executable stack (kernel/glibc reject) |

### Watch
If 10e still fails: stop both instances (save $); rebuild PolyChord without execstack or set system-wide execstack clear; do not invent nested ΔlnZ from frozen dead=4595.

Logs on host:
- `chains/*reresume_20260810e.log` (current attempt)
- prior: `*d.log` (libchord), `*c` path (no -r), root segfault logs

## Watch command (owner or agent)

```bash
aws ssm send-command --instance-ids i-04ead482af737e7bf i-0e353f38544397a6d \
  --document-name AWS-RunShellScript \
  --parameters 'commands=["date -u; wc -l /home/ubuntu/prtoe_class/chains/*_polychord_raw/*dead.txt; ls -la --time-style=full-iso /home/ubuntu/prtoe_class/chains/*_polychord_raw/*dead.txt; uptime"]'
```

Success criterion: **dead lines > 4595** and mtime advancing.

*NO FABRICATIONS. Mid-run log(Z) still not bookable.*
