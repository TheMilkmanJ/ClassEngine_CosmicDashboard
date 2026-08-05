# machine_r1_currency_20260804e — EDITS

**Authority numbers written (as current):**

| field | value |
|---|---|
| lcdm R−1 | **0.071122** |
| lcdm N | **21886** |
| lcdm t | **2026-08-04T13:01:13** |
| lcdm vs stop | **1.42×** |
| lcdm trajectory | `0.093682 → 0.053867 → 0.048827 → 0.059055 → 0.086466 → 0.071122` |
| dyad R−1 | **0.128943** (**UNCHANGED**) |
| dyad N | **20302** |
| dyad t | 2026-08-04T03:25:56 |
| dyad vs stop | ~**2.58×** |
| routeD R−1 | **4.941933** (**UNCHANGED** from 20260804d) |
| routeD N | **3290** |
| both bbnfix `converged` | **false** |
| book | **REFUSED** / **NOT bookable** |
| framing kill | “0.086466 as current”; permanent “nearest-and-receding forever”; “nearly there / ~1.18×” |
| framing keep | R−1 **with N + timestamp**; historical “was 0.086” / “was 0.059” OK; temporary R−1 < 0.05 without self-stop is **not** bookable |

**Historical retained where useful:** “was 0.086466@N=20409”; “was 0.059055@N=19013”; temporary dip 0.048827@N=17458.

---

## Path-by-path

### Living PRTOE surfaces

| file | change |
|---|---|
| `docs/PRTOE_CHAIN_TABLES.md` | freeze table lcdm **0.071122**/N=**21886**/t=13:01:13; trajectory +6 points; kill permanent “nearest-and-receding”; residual row 2; currency `20260804e` |
| `docs/PRTOE_CODE_MANIFEST.md` | live stamp table + twin row → 0.071122/N=21886; trajectory framing; currency `20260804e` |
| `docs/PRTOE_INDEX.md` | production chains stamp → 0.071122@N=21886; must-not “nearest-and-receding forever”; currency `20260804e` |
| `docs/PRTOE_READERS_GUIDE.md` | currency board CURRENT → 0.071122 / 0.128943 |
| `docs/PRTOE_READERS_RISK.md` | banner, §3c, §4 table, basin prose, ledger row 5 → 0.071122; currency package → `20260804e` |
| `docs/PRTOE_REFEREE_CALENDAR.md` | Sitting NOW table + twin ETA row → 0.071122/N=21886; trajectory; no permanent receding |
| `docs/PRTOE_DEPENDENCY_TREE.md` | banner residual → lcdm 0.071122@N=21886 |
| `docs/PRTOE_DOMAIN_COVERAGE.md` | row 1 cosmology → 0.071122 / 0.128943 |
| `docs/PRTOE_honest_status.md` | CURRENT table lcdm 0.071122/N=21886; trajectory note; body residual strip |
| `docs/PRTOE_hubble_tension.md` | freeze table + status + ledger + triage → 0.071122@N=21886; currency `20260804e` |
| `docs/PRTOE_neutrino_home.md` | freeze + ledger → 0.071122@N=21886; currency link `20260804e` |
| `docs/PRTOE_s8_growth.md` | live stamp → 0.071122@N=21886 / 0.128943 |
| `docs/PRTOE_s8_tension.md` | live progress → 0.071122@N=21886 / 0.128943 |
| `docs/PRTOE_fairbank_note_draft.md` | currency freeze + body + ledger → 0.071122; supersedes 0.086 as-current; currency `20260804e` |

### ForJustin

| file | change |
|---|---|
| `ForJustin/STATUS_CONTINUE.md` | Machine: lcdm **0.071122** N=**21886** t=13:01:13; currency `20260804e` |
| `ForJustin/PASTE_CHATGPT_REF.md` | gate / E2 / one-liner / reply shape → 0.071122 |
| `ForJustin/PASTE_CLAUDE_RED.md` | gate / fences / R-gate → 0.071122 |
| `ForJustin/ARXIV_OWNER_CHECKLIST.md` | bbnfix stamp → 0.071122 N=21886 |

### Board / residual / watch / currency pointer

| file | change |
|---|---|
| `docs/working_logs/_runs/gate_fire_watch_20260804/REPORT.md` | live currency table lcdm 0.071122@N=21886 (arm-time 0.086 kept as historical) |
| `docs/working_logs/_runs/next_triggers_20260804/MASTER_REPORT.md` | lcdm row → 0.071122 N=21886 |
| `docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md` | not-desk-forceable bbnfix row → 0.071122@N=21886 |
| `docs/working_logs/_runs/next_queue_20260804/NEXT_QUEUE.md` | current disk → 0.071122; currency `20260804e` |
| `docs/working_logs/_runs/next_queue_20260804/RESIDUAL_REFRESH.md` | M1 → 0.071122@N=21886 |
| `docs/working_logs/_runs/next_queue_20260804/REPORT.md` | residual #1 → 0.071122@N=21886 |
| `docs/working_logs/_runs/machine_r1_currency_20260804d/REPORT.md` | **currency note only** (prior body left as historical 0.086 stamp) |

### This package

| file | role |
|---|---|
| `docs/working_logs/_runs/machine_r1_currency_20260804e/REPORT.md` | authority + summary |
| `docs/working_logs/_runs/machine_r1_currency_20260804e/EDITS.md` | this file |

---

## Explicitly **not** rewritten (historical correctness)

- `docs/working_logs/_runs/bbnfix_booking_*/` refuse cards that recorded 0.086466 (or earlier 0.059) as then-current  
- `docs/working_logs/_runs/gate_fire_watch_20260804/poll_*.txt` and `watch.log` historical poll lines  
- `docs/working_logs/_runs/machine_r1_currency_20260804{b,c,d}/` body numbers (pointer only on d)  
- `docs/working_logs/_runs/arxiv_owner_prep_20260804/` historical package stamps  
- Chain `.progress` / `.checkpoint` / `.txt` files (read-only)  
- MCMCs left running  

---

## Exact numbers written (canonical)

```
cmp_lcdm_mnu_bbnfix: R−1 = 0.071122  N = 21886  converged:false  t=2026-08-04T13:01:13
                      was 0.086466@N=20409; earlier 0.059055@N=19013 — 1.42× stop (0.05)
                      trajectory: 0.093682 → 0.053867 → 0.048827 → 0.059055 → 0.086466 → 0.071122
dyad_mnu_bbnfix:     R−1 = 0.128943  N = 20302  converged:false  t=2026-08-04T03:25:56
                      ~2.58× stop (unchanged stamp)
cmp_prtoe_routeD:     R−1 = 4.941933  N = 3290   converged:false  t=2026-08-04T09:00:36
                      ~49.4× stop 0.1 (unchanged from 20260804d)
book: REFUSED (NOT bookable)
framing: facts + N+t; NOT permanent "nearest-and-receding forever"; NOT "0.086 as current"
H0: not quoted as result
```
