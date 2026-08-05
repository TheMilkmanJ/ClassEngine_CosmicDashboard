# machine_r1_currency_20260804d — REPORT

**Worker:** Grok Build (routeD living-doc currency update)  
**Package:** `docs/working_logs/_runs/machine_r1_currency_20260804d/`  
**Rules:** NO FABRICATIONS · leave live MCMCs alone · no kill · no restart · no PolyChord · no peek-book H₀ · **Book still REFUSED** for bbnfix · routeD **not** dual-gate  
**Fence:** do **not** rewrite historical `_runs/**` packages that correctly quote past 102.79 as then-current

> **Currency note (20260804e):** lcdm R−1 moved to **0.071122**@N=21886 (this package’s lcdm
> **0.086466**@N=20409 is historical as-current for that stamp). See
> [`../machine_r1_currency_20260804e/`](../machine_r1_currency_20260804e/). routeD **4.941933**@N=3290
> and dyad **0.128943**@N=20302 stamps here remain unchanged through 20260804e.

---

## 1. Authority re-verify

**Sources (progress / checkpoint; bbnfix gate fields same as `scripts/book_bbnfix_when_ready.py`):**

| source | result |
|---|---|
| `chains/cmp_prtoe_routeD.progress` last row | `3290.000000 2026-08-04T09:00:36.864132  0.995763  4.941933 NaN` |
| `chains/cmp_prtoe_routeD.progress` prior row | `1609.000000 2026-08-03T20:53:57.575011  1.0  102.794555 NaN` |
| `chains/cmp_prtoe_routeD.checkpoint` | `converged: false`; `Rminus1_last: 4.94193275…` |
| `chains/cmp_lcdm_mnu_bbnfix.progress` last row | `20409.000000 2026-08-04T05:21:52.542208  0.983805  0.086466 NaN` (**UNCHANGED**) |
| `chains/dyad_mnu_bbnfix.progress` last row | `20302.000000 2026-08-04T03:25:56.226343  0.996466  0.128943 NaN` (**UNCHANGED**) |
| Booking gate (bbnfix) | **REFUSED** — both legs fail R−1 < 0.05 **and** `converged: true` |
| routeD dual gate? | **no** — separate instrument; stop 0.1 only |

**routeD trajectory (do not invent extra points):**

```
102.794555@N=1609 (2026-08-03T20:53) → 4.941933@N=3290 (2026-08-04T09:00)
```

**Ratio to stop:** 4.941933 / 0.1 = **~49.42×** (display **~49.4×**). Was ~1028× at 102.79.

Prior currency package (superseded as-current for routeD):
[`../machine_r1_currency_20260804c/`](../machine_r1_currency_20260804c/) — routeD 102.79@N=1609 era; pointer added on that REPORT. bbnfix pair numbers there remain current.

---

## 2. Quote-ready live numbers

| chain | N (progress) | timestamp | R−1 last | stop | `converged` | bookable? | vs stop |
|---|---:|---|---:|---:|---|---|---|
| `cmp_lcdm_mnu_bbnfix` | **20409** | 2026-08-04T05:21:52 | **0.086466** | 0.05 | **false** | **NO** | **1.73×** (receding; **UNCHANGED**) |
| `dyad_mnu_bbnfix` | **20302** | 2026-08-04T03:25:56 | **0.128943** | 0.05 | **false** | **NO** | **~2.58×** (**UNCHANGED**) |
| `cmp_prtoe_routeD` | **3290** | **2026-08-04T09:00:36** | **4.941933** | 0.1 | **false** | **NO** (early) | **~49.4×** (**improving**) |

**Key narrative:**

- routeD **improving** (102.79→4.94), still **early / not bookable** (~**49.4×** stop 0.1).
- Kill as-current: “stuck at 103”, “R−1 ~103”, “~102.79 at N=1609” as **present** truth.
- Historical “was 102.79@N=1609” is OK when clearly past.
- bbnfix pair **UNCHANGED** (lcdm 0.086466@N=20409, dyad 0.128943@N=20302).
- **Book still REFUSED** for bbnfix. routeD **not** part of dual gate.
- **No H₀** invented or quoted as result.
- MCMCs **not** killed/restarted; PolyChord **not** started.

Canonical phrase for living surfaces:

> routeD R−1 **4.941933** (N=3290, t=2026-08-04T09:00:36; was 102.79@N=1609 — **improving**, still early ~**49.4×** stop 0.1)

---

## 3. What this pass did

1. Re-verified routeD progress + checkpoint authority (matches LIVE AUTHORITY in task).  
2. Confirmed bbnfix pair progress stamps **unchanged**.  
3. Updated living PRTOE surfaces that quoted routeD ~102/103 as current.  
4. Added currency pointer on `machine_r1_currency_20260804c/REPORT.md`.  
5. Package files: this REPORT + [`EDITS.md`](EDITS.md).

### What this pass did **not** do

- Did not kill, pause, restart, or edit live MCMC chain files.  
- Did not start PolyChord.  
- Did not quote H₀ / Σm_ν / S₈ as results.  
- Did **not** rewrite historical `_runs/**` dated packages that correctly quoted 102.79 as then-current (e.g. `live_surfaces_full_*`, `machine_r1_currency_20260804b`, refuse cards, hygiene packages).  
- Did not invent progress R−1 beyond the two routeD progress-file stamps above.  
- Did not touch dual-gate / book logic (routeD remains separate).  
- `next_triggers_20260804/MASTER_REPORT.md` — no routeD ~102 claim; left alone.

---

## 4. Files changed

See [`EDITS.md`](EDITS.md) for path-by-path exact numbers written.

**Must-update living surfaces:**

1. `docs/PRTOE_CHAIN_TABLES.md`  
2. `docs/PRTOE_CODE_MANIFEST.md`  
3. `docs/PRTOE_INDEX.md`  
4. `docs/PRTOE_READERS_RISK.md`  
5. `docs/PRTOE_REFEREE_CALENDAR.md`  
6. `docs/PRTOE_honest_status.md`  
7. `docs/PRTOE_s8_growth.md`  
8. `docs/PRTOE_s8_tension.md`  

**Currency pointer only:**

- `docs/working_logs/_runs/machine_r1_currency_20260804c/REPORT.md`

---

## 5. Next machine action (not executed)

1. Leave cobaya alone (bbnfix + routeD).  
2. bbnfix book only when **both** legs self-stop with progress R−1 < 0.05.  
3. routeD thaw posterior only after R−1 < 0.1 **and** `converged: true` — still ~49× away; not dual-gate.

---

## Key numbers (summary strip)

| quantity | value |
|---|---|
| routeD R−1 / N / t | **4.941933** / **3290** / **2026-08-04T09:00:36** |
| routeD prior (superseded as-current) | 102.794555 / 1609 / 2026-08-03T20:53:57 |
| routeD vs stop | **~49.4×** (**improving** from ~1028×) |
| routeD `converged` | **false** |
| lcdm R−1 / N / t | **0.086466** / **20409** / 2026-08-04T05:21:52 (**UNCHANGED**) |
| dyad R−1 / N / t | **0.128943** / **20302** / 2026-08-04T03:25:56 (**UNCHANGED**) |
| book_bbnfix | **REFUSED** |
| routeD dual gate? | **no** |
| framing | **improving** (102.79→4.94); still early / not bookable; **not** “stuck at 103” |
| H₀ as result | **none** |

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀. No historical _runs rewrites of old 102.79 packages.*
