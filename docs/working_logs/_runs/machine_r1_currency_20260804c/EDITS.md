# machine_r1_currency_20260804c — EDITS

**Authority numbers written (as current):**

| field | value |
|---|---|
| lcdm R−1 | **0.086466** |
| lcdm N | **20409** |
| lcdm t | **2026-08-04T05:21:52** |
| lcdm vs stop | **1.73×** (**receding** from 0.059@N=19013) |
| lcdm trajectory | `0.053867 → 0.048827 → 0.059055 → 0.086466` |
| dyad R−1 | **0.128943** (rounded **0.129** only where already rounded) |
| dyad N | **20302** |
| dyad t | 2026-08-04T03:25:56 |
| dyad vs stop | ~**2.58×** (~2.6×) |
| routeD R−1 | **102.79** / **~103** |
| routeD N | **1609** |
| both bbnfix `converged` | **false** |
| book | **REFUSED** / **NOT bookable** |
| framing kill | “Closest to gate ~1.18×”, “Closest production object (~1.18×)”, “nearly there / closest approaching” |
| framing keep | **nearest-and-receding**; historical “was 0.059” OK |

**Historical retained where useful:** “was 0.059055@N=19013” / “was 0.059”; temporary dip 0.048827@N=17458.

---

## Path-by-path

### Living PRTOE surfaces (Claude 14)

| file | change |
|---|---|
| `docs/PRTOE_CHAIN_TABLES.md` | freeze table lcdm **0.086466**/N=**20409**/t=05:21:52; kill “Closest to gate ~1.18×”; trajectory + nearest-and-receding; residual row 2; currency `20260804c` |
| `docs/PRTOE_CODE_MANIFEST.md` | live stamp table + twin row → 0.086466/N=20409; kill “Closest production object (~1.18× stop)”; trajectory framing |
| `docs/PRTOE_REFEREE_CALENDAR.md` | Sitting NOW table + twin ETA row → 0.086466/N=20409; kill ~1.18× closest language |
| `docs/PRTOE_DEPENDENCY_TREE.md` | banner residual → lcdm 0.086466@N=20409 receding 1.73× |
| `docs/PRTOE_DOMAIN_COVERAGE.md` | row 1 cosmology → 0.086466 / 0.128943 with receding note |
| `docs/PRTOE_INDEX.md` | production chains stamp → 0.086466@N=20409; must-not “nearly there / ~1.18×” |
| `docs/PRTOE_READERS_GUIDE.md` | currency board CURRENT → 0.086466 / 0.128943 |
| `docs/PRTOE_READERS_RISK.md` | banner, §3c, §4 table, basin prose, ledger row 5 → 0.086466 receding; currency package → `20260804c` |
| `docs/PRTOE_fairbank_note_draft.md` | currency freeze quotes R−1 **with N and timestamp**; body + ledger → 0.086466; supersedes 0.059 / 1.18× as-current |
| `docs/PRTOE_honest_status.md` | CURRENT table lcdm 0.086466/N=20409; trajectory note; body residual strip |
| `docs/PRTOE_hubble_tension.md` | freeze table + status + ledger + triage → 0.086466@N=20409 receding; currency `20260804c` |
| `docs/PRTOE_neutrino_home.md` | freeze + ledger → 0.086466@N=20409; currency link `20260804c` |
| `docs/PRTOE_s8_growth.md` | live stamp → 0.086466@N=20409 (receding) / 0.128943 |
| `docs/PRTOE_s8_tension.md` | live progress → 0.086466@N=20409 (receding) / 0.128943 |

### ForJustin

| file | change |
|---|---|
| `ForJustin/STATUS_CONTINUE.md` | Machine: lcdm **0.086466** N=**20409** t=05:21:52 receding; currency `20260804c` |
| `ForJustin/PASTE_CHATGPT_REF.md` | gate / E2 / one-liner / reply shape → 0.086466 |
| `ForJustin/PASTE_CLAUDE_RED.md` | gate / fences / R-gate → 0.086466 receding |

### Board / residual / currency pointer

| file | change |
|---|---|
| `docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md` | not-desk-forceable bbnfix row → 0.086466@N=20409 receding |
| `docs/working_logs/_runs/next_queue_20260804/NEXT_QUEUE.md` | current disk → 0.086466; currency `20260804c` |
| `docs/working_logs/_runs/next_queue_20260804/RESIDUAL_REFRESH.md` | M1 → 0.086466@N=20409 |
| `docs/working_logs/_runs/next_queue_20260804/REPORT.md` | residual #1 → 0.086466@N=20409 |
| `docs/working_logs/_runs/machine_r1_currency_20260804b/REPORT.md` | **currency note only** (prior body left as historical 0.059 stamp) |

### This package

| file | role |
|---|---|
| `docs/working_logs/_runs/machine_r1_currency_20260804c/REPORT.md` | authority + summary |
| `docs/working_logs/_runs/machine_r1_currency_20260804c/EDITS.md` | this file |

---

## Explicitly **not** rewritten (historical correctness)

- `docs/working_logs/_runs/bbnfix_booking_*/` refuse cards that recorded 0.059055  
- `docs/working_logs/_runs/living_docs_currency_20260804/` and other dated freeze packages  
- `docs/working_logs/_runs/live_surfaces_full_20260804/` historical stamps  
- `docs/working_logs/_runs/machine_r1_currency_20260804b/` body numbers (pointer only)  
- `docs/working_logs/_runs/improve_loop_20260804/REPORT.md` historical booking recheck line  
- Chain `.progress` / `.checkpoint` / `.txt` files (read-only)  
- MCMCs left running  

---

## Exact numbers written (canonical)

```
cmp_lcdm_mnu_bbnfix: R−1 = 0.086466  N = 20409  converged:false  t=2026-08-04T05:21:52
                      was 0.059055@N=19013 — receding — now 1.73× stop (0.05)
                      trajectory: 0.053867 → 0.048827 → 0.059055 → 0.086466
dyad_mnu_bbnfix:     R−1 = 0.128943  N = 20302  converged:false  t=2026-08-04T03:25:56
                      ~2.58× stop (unchanged stamp)
cmp_prtoe_routeD:     R−1 ≈ 102.79    N = 1609   converged:false  (early; leave)
book: REFUSED (NOT bookable)
framing: nearest-and-receding; NOT "closest approaching / ~1.18×"
H0: not quoted as result
```
