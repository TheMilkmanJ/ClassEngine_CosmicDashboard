# machine_r1_currency_20260804c — REPORT

> **Currency note (routeD forward):** living forward routeD numbers superseded by
> [`../machine_r1_currency_20260804d/`](../machine_r1_currency_20260804d/) —
> routeD R−1 now **4.941933**@N=3290 (was 102.794555@N=1609 — **improving**, still early ~**49.4×** stop).
> bbnfix pair stamps in this package (lcdm 0.086466 / dyad 0.128943) remain current as of 20260804d.
> This package remains a valid historical stamp of routeD ~102.79 / N=1609 as then-current.

**Worker:** Grok Build (RED EVENT A2-REVERSAL living-doc currency cure)  
**Package:** `docs/working_logs/_runs/machine_r1_currency_20260804c/`  
**Rules:** NO FABRICATIONS · leave live MCMCs alone · no kill · no restart · no PolyChord · no peek-book H₀ · no H₀ book · **Book still REFUSED**  
**Fence:** do **not** rewrite historical `_runs/**` packages that correctly quote past 0.059055 as then-current

---

## 1. Authority re-verify

**Sources (same fields as `scripts/book_bbnfix_when_ready.py`):**

| source | result |
|---|---|
| `chains/cmp_lcdm_mnu_bbnfix.progress` last row | `20409.000000 2026-08-04T05:21:52.542208  0.983805  0.086466 NaN` |
| `chains/dyad_mnu_bbnfix.progress` last row | `20302.000000 2026-08-04T03:25:56.226343  0.996466  0.128943 NaN` |
| `chains/cmp_prtoe_routeD.progress` last row | `1609.000000 2026-08-03T20:53:57.575011  1.0  102.794555 NaN` |
| `chains/cmp_lcdm_mnu_bbnfix.checkpoint` | `converged: false`; `Rminus1_last: 0.08646576…` |
| `chains/dyad_mnu_bbnfix.checkpoint` | `converged: false`; `Rminus1_last: 0.12894296…` |
| Booking gate | **REFUSED** — both legs fail R−1 < 0.05 **and** `converged: true` |

**lcdm progress trajectory (do not invent extra points):**

```
0.053867 → 0.048827 → 0.059055 → 0.086466
```

**Three consecutive moves away from gate after the dip.** Framing: **nearest-and-receding**, **not** “closest approaching / nearly there.”

Prior currency package (superseded as-current):
[`../machine_r1_currency_20260804b/`](../machine_r1_currency_20260804b/) — lcdm 0.059055@N=19013 era; pointer added on that REPORT.

---

## 2. Quote-ready live numbers

| chain | N (progress) | timestamp | R−1 last | stop | `converged` | bookable? | vs stop |
|---|---:|---|---:|---:|---|---|---|
| `cmp_lcdm_mnu_bbnfix` | **20409** | **2026-08-04T05:21:52** | **0.086466** | 0.05 | **false** | **NO** | **1.73×** (receding from 0.059) |
| `dyad_mnu_bbnfix` | **20302** | 2026-08-04T03:25:56 | **0.128943** | 0.05 | **false** | **NO** | **~2.58×** (~2.6×) |
| `cmp_prtoe_routeD` | **1609** | 2026-08-03T20:53:57 | **102.794555** | 0.1 | **false** | **NO** (early) | far |

**Key narrative:**

- **NOT bookable** / **REFUSED** everywhere.
- lcdm **0.059@N=19013 → 0.086466@N=20409** is **receding** (now **1.73×** stop), not “almost there.”
- Kill as-current: “Closest to gate ~1.18×”, “Closest production object (~1.18× stop)”, “nearly there.”
- Historical “was 0.059” is OK when clearly past.
- dyad stamp **unchanged** at 0.128943@N=20302.
- routeD **unchanged** early (~102.79 / N=1609) — left alone.
- **No H₀** invented or quoted as result.
- MCMCs **not** killed/restarted; PolyChord **not** started.

Canonical phrase for living surfaces:

> lcdm R−1 **0.086466** (N=20409, t=2026-08-04T05:21:52; was 0.059@N=19013 — **receding**, now **1.73×** stop)

---

## 3. What this pass did

1. Re-verified progress + checkpoint authority (matches LIVE AUTHORITY table in task).  
2. Updated **Claude list of 14** living PRTOE surfaces.  
3. Updated ForJustin STATUS + PASTE_* and forward-facing board/queue files that hardcode current R−1.  
4. Added currency pointer on `machine_r1_currency_20260804b/REPORT.md`.  
5. Package files: this REPORT + [`EDITS.md`](EDITS.md).

### What this pass did **not** do

- Did not kill, pause, restart, or edit live MCMC chain files.  
- Did not start PolyChord.  
- Did not quote H₀ / Σm_ν / S₈ as results.  
- Did **not** rewrite historical `_runs/**` dated packages that correctly quoted 0.059055 as then-current (e.g. prior refuse cards, `living_docs_currency_*`, `live_surfaces_full_*` body stamps).  
- Did not invent progress R−1 or trajectory points beyond the four progress-file stamps above.

---

## 4. Files changed

See [`EDITS.md`](EDITS.md) for path-by-path exact numbers written.

**Claude list of 14 (primary):**

1. `docs/PRTOE_CHAIN_TABLES.md`  
2. `docs/PRTOE_CODE_MANIFEST.md`  
3. `docs/PRTOE_REFEREE_CALENDAR.md`  
4. `docs/PRTOE_DEPENDENCY_TREE.md`  
5. `docs/PRTOE_DOMAIN_COVERAGE.md`  
6. `docs/PRTOE_INDEX.md`  
7. `docs/PRTOE_READERS_GUIDE.md`  
8. `docs/PRTOE_READERS_RISK.md`  
9. `docs/PRTOE_fairbank_note_draft.md`  
10. `docs/PRTOE_honest_status.md`  
11. `docs/PRTOE_hubble_tension.md`  
12. `docs/PRTOE_neutrino_home.md`  
13. `docs/PRTOE_s8_growth.md`  
14. `docs/PRTOE_s8_tension.md`

**Also (quoted 0.059 as current):**

- `ForJustin/STATUS_CONTINUE.md`  
- `ForJustin/PASTE_CHATGPT_REF.md`  
- `ForJustin/PASTE_CLAUDE_RED.md`  
- `docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md`  
- `docs/working_logs/_runs/next_queue_20260804/NEXT_QUEUE.md`  
- `docs/working_logs/_runs/next_queue_20260804/RESIDUAL_REFRESH.md`  
- `docs/working_logs/_runs/next_queue_20260804/REPORT.md`  
- `docs/working_logs/_runs/machine_r1_currency_20260804b/REPORT.md` (currency note only)

---

## 5. Next machine action (not executed)

1. Leave cobaya alone until **both** bbnfix legs self-stop (`converged: true`) with progress R−1 < 0.05.  
2. Then: `python3 scripts/book_bbnfix_when_ready.py` (or `bash scripts/bbnfix_when_ready_all.sh` Stage A).  
3. Tables only after red: `--write-tables` with `RED_AUDIT.md`.

---

## Key numbers (summary strip)

| quantity | value |
|---|---|
| lcdm R−1 / N / t | **0.086466** / **20409** / **2026-08-04T05:21:52** |
| lcdm prior (superseded as-current) | 0.059055 / 19013 / 2026-08-03T21:05:36 |
| lcdm trajectory | 0.053867 → 0.048827 → 0.059055 → 0.086466 |
| lcdm vs stop | **1.73×** (**receding**) |
| dyad R−1 / N / t | **0.128943** / **20302** / 2026-08-04T03:25:56 |
| dyad vs stop | ~**2.58×** |
| routeD R−1 / N / t | **102.794555** / **1609** / 2026-08-03T20:53:57 |
| book_bbnfix | **REFUSED** |
| bookable | **NO** |
| H₀ as result | **none** |
| framing | **nearest-and-receding** (not closest-approaching) |

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀. No historical _runs rewrites of old 0.059 packages.*
