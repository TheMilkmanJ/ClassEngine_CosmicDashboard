# machine_watch_hygiene_20260804 — REPORT

**Worker:** Grok Build (machine-facing hygiene)  
**Package:** `docs/working_logs/_runs/machine_watch_hygiene_20260804/`  
**Rules:** NO FABRICATIONS · leave live MCMCs alone · no kill · no restart · no chain-file edits · no PolyChord · no peek-book H₀  

---

## 1. Progress snapshot (live re-read of `chains/*.progress`)

Authority = last row of each progress file (cobaya columns: N, timestamp, acceptance_rate, Rminus1, Rminus1_cl).  
Checkpoint `converged` re-read from `chains/*.checkpoint`. **No R−1 invented.**

| chain | N (progress) | timestamp (progress) | R−1 last | stop | `converged` | bookable? |
|---|---:|---|---:|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | **19013** | 2026-08-03T21:05:36.968557 | **0.059055** | 0.05 | **false** | **NO** |
| `dyad_mnu_bbnfix` | **18837** | 2026-08-03T17:57:59.890097 | **0.189201** | 0.05 | **false** | **NO** |
| `cmp_prtoe_routeD` | **1609** | 2026-08-03T20:53:57.575011 | **102.794555** | 0.1 | **false** | **NO** (early; separate instrument) |

**Last progress rows (verbatim):**

```
# cmp_lcdm_mnu_bbnfix
19013.000000 2026-08-03T21:05:36.968557  0.983857  0.059055 NaN

# dyad_mnu_bbnfix
18837.000000 2026-08-03T17:57:59.890097  0.99672  0.189201 NaN

# cmp_prtoe_routeD
1609.000000 2026-08-03T20:53:57.575011  1.0  102.794555 NaN
```

**Checkpoint Rminus1_last (informational only; gate uses progress R−1):**

| chain | Rminus1_last | converged |
|---|---:|---|
| `cmp_lcdm_mnu_bbnfix` | 0.05905511181721022 | false |
| `dyad_mnu_bbnfix` | 0.18920075919140164 | false |
| `cmp_prtoe_routeD` | 102.79455471855752 | false |

**lcdm history (not authority):** progress once showed R−1 = **0.048827** at N=17458 (2026-08-03T14:21:54) then rose to **0.059055**. Temporary R−1 < 0.05 without self-stop is **not** bookable.

**Currency vs prior open_machine_full stamp (2026-08-04T02:40):** progress tails **unchanged** (same N / R−1 / timestamps). Progress files still lag chain `.txt` growth until cobaya’s next R−1 write — expected; **not** a license to book.

**Key numbers (quote-ready):**

- lcdm R−1 **0.059055** (N=19013) · dyad R−1 **0.189201** (N=18837) · routeD R−1 **102.794555** (N=1609)
- both bbnfix legs `converged: false` · **NOT bookable**
- Do **not** quote H₀ from these chains as results

---

## 2. Booking gate: still REFUSES

**Script:** `scripts/book_bbnfix_when_ready.py`  
**Rule:** both of `{dyad_mnu_bbnfix, cmp_lcdm_mnu_bbnfix}` with progress R−1 **< 0.05** **AND** checkpoint **`converged: true`** (both legs required). Exit 2 on refuse.

### Live refuse card (script-generated; progress identical to §1)

| field | value |
|---|---|
| package | [`docs/working_logs/_runs/bbnfix_booking_20260804_091234/`](../bbnfix_booking_20260804_091234/) |
| generated UTC | 2026-08-04T09:12:34.463753+00:00 |
| Result | **REFUSED** |
| Exit code | **2** |
| booking | `null` (no GetDist marginals) |

Gate messages from that card (match live progress/checkpoint re-read):

- dyad: R−1 = 0.189201 >= 0.05 — NOT READY; `converged: false` — NOT READY  
- lcdm: R−1 = 0.059055 >= 0.05 — NOT READY; `converged: false` — NOT READY  

**Hygiene reconfirm:** gate inputs re-read from disk at this pass; **no progress-file change** since `091234`. Refuse is still mandatory. Earlier same-day refuse: `bbnfix_booking_20260804_084008/` (also REFUSED; same numbers). Living docs unchanged by refuse path.

**No peek-book.** No H₀ quoted.

---

## 3. `make_getdist_tables.py --force-bbnfix` path — code review (safe)

**File:** `scripts/make_getdist_tables.py`  
**Long getdist:** **not re-run** this pass (code review only).

### Gate incomplete + force → living path not written

Source logic (lines 106–160, 206–228):

1. `unbookable_force` set when `--force-bbnfix` and gate incomplete (`both_ok` false).  
2. Explicit print: **will NOT write `docs/PRTOE_CHAIN_TABLES.md`**.  
3. On `unbookable_force`: writes only  
   `docs/working_logs/_runs/getdist_force_UNBOOKABLE_<stamp>/CHAIN_TABLES_UNCONVERGED.md`  
   with banner **UNBOOKABLE / Do not quote as results**, and bbnfix parameter rows tagged `**UNBOOKABLE**` / `**UNCONVERGED**`.  
4. Living shelf write (`open("docs/PRTOE_CHAIN_TABLES.md", "w")`) is on the **non-force / gate-open** branch only (after the `if unbookable_force:` early return path that returns 0 without touching the living file).  
5. Default / `--include-bbnfix` with gate closed: **exit 2**, no living write, no bbnfix triangles.

### Force UNBOOKABLE smoke (cited, not re-run)

**Path:** [`docs/working_logs/_runs/getdist_force_UNBOOKABLE_20260804_030942/`](../getdist_force_UNBOOKABLE_20260804_030942/)  
**Artifact:** `CHAIN_TABLES_UNCONVERGED.md`

Banner excerpt (file authority):

> **UNBOOKABLE GetDist force peek — NOT a living chain table**  
> rmap={'cmp_lcdm_mnu_bbnfix': 0.059055, 'dyad_mnu_bbnfix': 0.189201}  
> cmap={'cmp_lcdm_mnu_bbnfix': False, 'dyad_mnu_bbnfix': False}

bbnfix sections tagged **UNCONVERGED / UNBOOKABLE (force peek)**. Living `PRTOE_CHAIN_TABLES.md` still carries residual-freeze banner (bookable **NO**) — consistent with force path not clobbering shelf.

**Verdict:** `--force-bbnfix` with incomplete gate is **safe for living shelf** (routes to working_logs UNBOOKABLE artifact only).

---

## 4. `scripts/bbnfix_when_ready_all.sh` — tables OFF by default

**File:** `scripts/bbnfix_when_ready_all.sh`

| check | evidence | status |
|---|---|---|
| Tables default OFF | `WRITE_TABLES=0` (line 39); comment “Claude cure: tables OFF by default” | **OK** |
| Default path blocks stage 3 | when `WRITE_TABLES=0`: prints “make_getdist_tables BLOCKED (default) — booking ≠ publishing”; no `make_getdist_tables` call | **OK** |
| `--write-tables` needs RED_AUDIT | requires `$BOOK_DIR/RED_AUDIT.md` with line matching `red:\s*(AGREE\|AGREE-IF)`; else “REFUSED write-tables” exit 1; living `PRTOE_CHAIN_TABLES.md` not modified | **OK** |
| Owner override | `--force-tables` sets FORCE+WRITE; logged as non-default; not the standard path | noted |
| Gate refuse short-circuit | book exit 2 → “No finalize / tables / delta” exit 2 | **OK** |

**Usage on refuse (current state):**  
`bash scripts/bbnfix_when_ready_all.sh` → book REFUSED → exit 2 → no tables.

---

## 5. `open_machine_full` package currency

**Exists:** `docs/working_logs/_runs/open_machine_full_20260804/`  
**Updated:** `WATCH_SNAPSHOT.md` — **currency note only**; **no new R−1 invented**.

Progress tails in that snapshot (lcdm 0.059055 / dyad 0.189201 / routeD 102.79) remain **byte-identical** to live progress re-read this pass. Currency stamp added pointing at this hygiene package + refuse card `091234`. Offline GetDist GR numbers left as historical diag from 02:40 (not re-run).

---

## 6. Stale “almost bookable” / false-gate language (0.048827)

### Living docs (`docs/PRTOE_*.md`) — fence status

| file | 0.048827 / almost-bookable language | status |
|---|---|---|
| `PRTOE_CHAIN_TABLES.md` | historical dip then rose; “**not** bookable” | **already fenced** |
| `PRTOE_honest_status.md` | “without self-stop; that is **not** bookable” | **already fenced** |
| `PRTOE_REFEREE_CALENDAR.md` | temporary <0.05 without self-stop **not** bookable | **already fenced** |
| `PRTOE_CODE_MANIFEST.md` | same fence | **already fenced** |
| `PRTOE_READERS_RISK.md` | “once briefly dipped … **not** bookable” | **already fenced** |

**No “almost bookable” string** found in living `docs/PRTOE_*.md` or `ForJustin/*.md`.  
**No fence edits required** this pass.

### Working-log historical only (not living shelf; list only)

| location | note |
|---|---|
| `docs/working_logs/_runs/SESSION_CONTINUE_SUMMARY_20260803.md` | table row “0.048827 · gate crossed · **no book until self-stop**” — historical event log; correctly says no book; not a living PRTOE surface |
| `ForGrok&Claude.md` EVENT A2 / C2 threads | log of “GATE CROSSED” language with booking HOLDS; C2 sweep says no overclaim |
| `open_board_split_20260803/*` | documents false single-chain watcher risk (PID 212363); retired narrative in `improve_loop_20260804/A2_FALSE_GATE_RETIRED.md` |

No living-doc rewrite performed (nothing unfenced found).

---

## What this pass did **not** do

- Did not kill, pause, restart, or edit live MCMC chain files.  
- Did not start PolyChord.  
- Did not re-run long GetDist / force peek.  
- Did not quote H₀ / Σm_ν / S₈ as results.  
- Did not write `docs/PRTOE_CHAIN_TABLES.md` body.  
- Did not invent progress R−1.

---

## Next machine action (not executed)

1. Leave cobaya alone until **both** bbnfix legs self-stop (`converged: true`) with progress R−1 < 0.05.  
2. Then: `python3 scripts/book_bbnfix_when_ready.py` (or `bash scripts/bbnfix_when_ready_all.sh` stage A).  
3. Tables only after red: `bash scripts/bbnfix_when_ready_all.sh --write-tables` with `RED_AUDIT.md` present.

---

## Key numbers (summary strip)

| quantity | value |
|---|---|
| lcdm R−1 / N / t | **0.059055** / 19013 / 2026-08-03T21:05:36 |
| dyad R−1 / N / t | **0.189201** / 18837 / 2026-08-03T17:57:59 |
| routeD R−1 / N / t | **102.794555** / 1609 / 2026-08-03T20:53:57 |
| book_bbnfix | **REFUSED** (exit 2) — card `bbnfix_booking_20260804_091234` |
| force-bbnfix living write | **blocked** (code + smoke `getdist_force_UNBOOKABLE_20260804_030942`) |
| when_ready_all tables default | **OFF**; `--write-tables` needs **RED_AUDIT** |
| bookable | **NO** |

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀.*

---

## Currency note (post-hygiene; 2026-08-04 later)

**Superseded as-current numbers in this report:** dyad R−1 **0.189201** / N=18837 is **historical** for this hygiene package only.

**Live authority now:** see [`../machine_r1_currency_20260804b/REPORT.md`](../machine_r1_currency_20260804b/REPORT.md) and refuse card [`../bbnfix_booking_20260804_092907/`](../bbnfix_booking_20260804_092907/).

| chain | N | R−1 | converged | bookable |
|---|---:|---:|---|---|
| `dyad_mnu_bbnfix` | **20302** | **0.128943** | false | **NO** |
| `cmp_lcdm_mnu_bbnfix` | **19013** | **0.059055** | false | **NO** |
| `cmp_prtoe_routeD` | **1609** | **~102.79** | false | **NO** (early) |

Dyad improved **0.189 → 0.129** (still ~2.6× stop bar). Gate still **REFUSED**. No H₀.
