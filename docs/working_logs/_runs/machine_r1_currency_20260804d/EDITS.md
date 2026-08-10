# machine_r1_currency_20260804d — EDITS

**Authority numbers written (as current):**

| field | value |
|---|---|
| routeD R−1 | **4.941933** (rounded **4.94** only in narrative “102.79→4.94”) |
| routeD N | **3290** |
| routeD t | **2026-08-04T09:00:36** |
| routeD vs stop | **~49.4×** (stop 0.1) |
| routeD prior (historical) | was **102.794555**@N=**1609** (2026-08-03T20:53) |
| routeD framing | **improving** (102.79→4.94); still **early / not bookable**; **not** “stuck at 103” |
| routeD dual gate? | **no** |
| lcdm R−1 / N | **0.086466** / **20409** (**UNCHANGED**) |
| dyad R−1 / N | **0.128943** / **20302** (**UNCHANGED**) |
| both bbnfix `converged` | **false** |
| book | **REFUSED** / **NOT bookable** (bbnfix) |

**Historical retained where useful:** “was 102.79@N=1609” / “was ~103”; prior ratio ~1028× at old stamp.

---

## Path-by-path

### Living PRTOE surfaces (must-update)

| file | change |
|---|---|
| `docs/PRTOE_CHAIN_TABLES.md` | routeD row N=**3290** R−1=**4.941933** t=09:00:36; was 102.79@N=1609 improving; distance ~**49.4×** (was ~1028×); residual row 3; currency `20260804d` |
| `docs/PRTOE_CODE_MANIFEST.md` | live stamp table + Route-D item row → 4.941933/N=3290 improving; currency `20260804d` |
| `docs/PRTOE_INDEX.md` | production chains stamp → routeD improving 4.941933@N=3290; must-not “stuck at 103”; currency `20260804d` |
| `docs/PRTOE_READERS_RISK.md` | §4 table routeD **4.941933**/N=3290; currency package → `20260804d` |
| `docs/PRTOE_REFEREE_CALENDAR.md` | Sitting NOW table + thaw ETA row + present-tense diagnostic line → 4.941933/N=3290 improving |
| `docs/PRTOE_honest_status.md` | CURRENT table + body residual strip → 4.941933/N=3290; currency `20260804d` |
| `docs/PRTOE_s8_growth.md` | freeze banner + §4 live stamp + ledger row 3 → 4.941933 improving (was ~103) |
| `docs/PRTOE_s8_tension.md` | §2 live progress routeD → 4.941933@N=3290 improving |

### Currency pointer only

| file | change |
|---|---|
| `docs/working_logs/_runs/machine_r1_currency_20260804c/REPORT.md` | **currency note only** (prior body left as historical 102.79 stamp; bbnfix pair still current) |

### This package

| file | role |
|---|---|
| `docs/working_logs/_runs/machine_r1_currency_20260804d/REPORT.md` | authority + summary |
| `docs/working_logs/_runs/machine_r1_currency_20260804d/EDITS.md` | this file |

---

## Explicitly **not** rewritten (historical correctness)

- `docs/working_logs/_runs/live_surfaces_full_20260804/` (102.79 then-current stamps)  
- `docs/working_logs/_runs/machine_r1_currency_20260804b/` body numbers  
- `docs/working_logs/_runs/machine_r1_currency_20260804c/` body numbers (pointer only)  
- `docs/working_logs/_runs/machine_watch_hygiene_20260804/`  
- `docs/working_logs/_runs/gate_fire_watch_20260804/` (no routeD 102 claim)  
- `docs/working_logs/_runs/next_triggers_20260804/MASTER_REPORT.md` (no routeD 102 claim)  
- Chain `.progress` / `.checkpoint` / `.txt` files (read-only)  
- MCMCs left running  

---

## Exact numbers written (canonical)

```
cmp_lcdm_mnu_bbnfix: R−1 = 0.086466  N = 20409  converged:false  t=2026-08-04T05:21:52  (UNCHANGED)
dyad_mnu_bbnfix:     R−1 = 0.128943  N = 20302  converged:false  t=2026-08-04T03:25:56  (UNCHANGED)
cmp_prtoe_routeD:     R−1 = 4.941933  N = 3290   converged:false  t=2026-08-04T09:00:36
                      was 102.794555@N=1609 (2026-08-03T20:53) — improving — now ~49.4× stop (0.1)
book: REFUSED (bbnfix NOT bookable)
routeD dual gate: no
framing: improving (102.79→4.94); still early / not bookable; NOT "stuck at 103"
H0: not quoted as result
```
