# machine_r1_currency_20260804b — REPORT

> **Currency note (A2-REVERSAL):** living forward numbers superseded by
> [`../machine_r1_currency_20260804c/`](../machine_r1_currency_20260804c/) —
> lcdm R−1 now **0.086466**@N=20409 (was 0.059055@N=19013 — **receding**).
> This package remains a valid historical stamp of the 0.059 / 0.129 era.

**Worker:** Grok Build (machine-number currency refresh)  
**Package:** `docs/working_logs/_runs/machine_r1_currency_20260804b/`  
**Rules:** NO FABRICATIONS · leave live MCMCs alone · no kill · no restart · no PolyChord · no peek-book H₀ · Book still REFUSED  

---

## 1. Authority re-verify

**Sources (same as `scripts/book_bbnfix_when_ready.py`):**

| source | result |
|---|---|
| `chains/dyad_mnu_bbnfix.progress` last row | `20302.000000 2026-08-04T03:25:56.226343  0.996466  0.128943 NaN` |
| `chains/cmp_lcdm_mnu_bbnfix.progress` last row | `19013.000000 2026-08-03T21:05:36.968557  0.983857  0.059055 NaN` |
| `chains/cmp_prtoe_routeD.progress` last row | `1609.000000 2026-08-03T20:53:57.575011  1.0  102.794555 NaN` |
| `chains/dyad_mnu_bbnfix.checkpoint` | `converged: false`; `Rminus1_last: 0.12894296…` |
| `chains/cmp_lcdm_mnu_bbnfix.checkpoint` | `converged: false`; `Rminus1_last: 0.05905511…` |
| Book script refuse card | [`../bbnfix_booking_20260804_092907/`](../bbnfix_booking_20260804_092907/) — **REFUSED** (exit 2); dyad **0.128943** N=20302 |

Prior mid-day stamp (superseded as-current): dyad R−1 **0.189201** @ N=**18837** (t=2026-08-03T17:57).  
Hygiene package snapshot: [`../machine_watch_hygiene_20260804/REPORT.md`](../machine_watch_hygiene_20260804/REPORT.md) — now carries a currency pointer to this package.

---

## 2. Quote-ready live numbers

| chain | N (progress) | timestamp | R−1 last | stop | `converged` | bookable? | vs stop |
|---|---:|---|---:|---:|---|---|---|
| `dyad_mnu_bbnfix` | **20302** | 2026-08-04T03:25:56 | **0.128943** | 0.05 | **false** | **NO** | ~**2.58×** (~2.6×) |
| `cmp_lcdm_mnu_bbnfix` | **19013** | 2026-08-03T21:05:36 | **0.059055** | 0.05 | **false** | **NO** | ~**1.18×** |
| `cmp_prtoe_routeD` | **1609** | 2026-08-03T20:53:57 | **102.794555** | 0.1 | **false** | **NO** (early) | far |

**Key narrative:**

- **NOT bookable** everywhere. Gate still closed (both R−1 < 0.05 **and** both `converged: true` required).
- Dyad **0.189 → 0.129** is **progress**, still ~**2.6×** the stop bar (0.05).
- lcdm stamp **unchanged** (0.059055 / N=19013).
- routeD **unchanged** early (~102.79 / N=1609) — left alone.
- **No H₀** invented or quoted as result.
- MCMCs **not** killed/restarted; PolyChord **not** started.

Rounded display used on some surfaces: dyad **0.129**, lcdm **0.059**, routeD **~102.79** / **~103**.

---

## 3. What this pass did

1. Re-verified progress + checkpoint + refuse card `bbnfix_booking_20260804_092907` (matches book script authority).  
2. Updated **all** listed high-traffic living surfaces that still quoted dyad **0.189 / 0.189201** as current.  
3. Kept historical “was 0.189” language where useful.  
4. Added currency note on `machine_watch_hygiene_20260804/REPORT.md`.  
5. Package files: this REPORT + [`EDITS.md`](EDITS.md).

### What this pass did **not** do

- Did not kill, pause, restart, or edit live MCMC chain files.  
- Did not start PolyChord.  
- Did not quote H₀ / Σm_ν / S₈ as results.  
- Did not rewrite historical refuse cards / ForGrok event log past numbers as if wrong.  
- Did not invent progress R−1.

---

## 4. Files changed

See [`EDITS.md`](EDITS.md) for path-by-path exact numbers written.

**High-traffic living (primary):**

- `docs/PRTOE_honest_status.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_CHAIN_TABLES.md`
- `docs/PRTOE_hubble_tension.md`
- `docs/PRTOE_neutrino_home.md`
- `docs/PRTOE_CODE_MANIFEST.md`
- `docs/PRTOE_DOMAIN_COVERAGE.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`
- `docs/PRTOE_INDEX.md`
- `docs/PRTOE_fairbank_note_draft.md`
- `docs/PRTOE_s8_tension.md`
- `docs/PRTOE_s8_growth.md`
- `ForJustin/STATUS_CONTINUE.md`
- `ForJustin/PASTE_CHATGPT_REF.md`
- `ForJustin/PASTE_CLAUDE_RED.md`

**Board / residual / hygiene (hardcoded current):**

- `docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md`
- `docs/working_logs/_runs/master_integrate_20260804/RESIDUAL_OPEN.md`
- `docs/working_logs/_runs/master_integrate_20260804/BOARD_DASHBOARD.md`
- `docs/working_logs/_runs/master_integrate_20260804/MASTER_REPORT.md` (authority table)
- `docs/working_logs/_runs/next_queue_20260804/NEXT_QUEUE.md`
- `docs/working_logs/_runs/next_queue_20260804/RESIDUAL_REFRESH.md`
- `docs/working_logs/_runs/next_queue_20260804/REPORT.md`
- `docs/working_logs/_runs/machine_watch_hygiene_20260804/REPORT.md` (currency note)

**Left alone (no live R−1 quote as current, or historical only):**

- `docs/PRTOE_neutrino_sector.md` — no live R−1 numbers  
- `ForGrok&Claude.md` — event log; historical 0.189 mentions stay as past record  
- Prior working-log packages that document a mid-day freeze (e.g. `living_docs_currency_20260804`, `live_surfaces_full_20260804`) — historical stamps; not rewritten

---

## 5. Next machine action (not executed)

1. Leave cobaya alone until **both** bbnfix legs self-stop (`converged: true`) with progress R−1 < 0.05.  
2. Then: `python3 scripts/book_bbnfix_when_ready.py` (or `bash scripts/bbnfix_when_ready_all.sh` Stage A).  
3. Tables only after red: `--write-tables` with `RED_AUDIT.md`.

---

## Key numbers (summary strip)

| quantity | value |
|---|---|
| dyad R−1 / N / t | **0.128943** / **20302** / 2026-08-04T03:25:56 |
| dyad prior (same day, superseded as-current) | 0.189201 / 18837 / 2026-08-03T17:57 |
| lcdm R−1 / N / t | **0.059055** / **19013** / 2026-08-03T21:05:36 |
| routeD R−1 / N / t | **102.794555** / **1609** / 2026-08-03T20:53:57 |
| dyad vs stop | ~**2.6×** (0.128943 / 0.05) |
| book_bbnfix | **REFUSED** — card `bbnfix_booking_20260804_092907` |
| bookable | **NO** |
| H₀ as result | **none** |

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀.*
