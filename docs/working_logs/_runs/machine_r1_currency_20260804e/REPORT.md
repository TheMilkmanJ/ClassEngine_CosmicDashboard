# machine_r1_currency_20260804e — REPORT

**Worker:** Grok Build (lcdm R−1 living-doc currency update)  
**Package:** `docs/working_logs/_runs/machine_r1_currency_20260804e/`  
**Rules:** NO FABRICATIONS · leave live MCMCs alone · no kill · no restart · no PolyChord · no peek-book H₀ · **Book still REFUSED** for bbnfix · routeD **not** dual-gate  
**Fence:** do **not** rewrite historical `_runs/**` packages (including refuse cards) that correctly recorded 0.086 as then-current

---

## 1. Authority re-verify

**Sources (progress / checkpoint; bbnfix gate via `scripts/book_bbnfix_when_ready.py`):**

| source | result |
|---|---|
| `python3 scripts/book_bbnfix_when_ready.py` | **REFUSED** — wrote `bbnfix_booking_20260804_190636/` |
| `chains/cmp_lcdm_mnu_bbnfix.progress` last row | `21886.000000 2026-08-04T13:01:13.920757  0.982762  0.071122 NaN` |
| `chains/cmp_lcdm_mnu_bbnfix.checkpoint` | `converged: false`; `Rminus1_last: 0.07112240248461754` |
| `chains/dyad_mnu_bbnfix.progress` last row | `20302.000000 2026-08-04T03:25:56.226343  0.996466  0.128943 NaN` (**UNCHANGED**) |
| `chains/dyad_mnu_bbnfix.checkpoint` | `converged: false`; `Rminus1_last: 0.12894296386177484` |
| `chains/cmp_prtoe_routeD.progress` last row | `3290.000000 2026-08-04T09:00:36.864132  0.995763  4.941933 NaN` (**UNCHANGED** from 20260804d) |
| `chains/cmp_prtoe_routeD.checkpoint` | `converged: false`; `Rminus1_last: 4.9419327502973` |
| Booking gate (bbnfix) | **REFUSED** — both legs fail R−1 < 0.05 **and** `converged: true` |
| routeD dual gate? | **no** — separate instrument; stop 0.1 only |

**lcdm trajectory (progress authority — do not invent extra points):**

```
0.093682 → 0.053867 → 0.048827 → 0.059055 → 0.086466 → 0.071122
```

**Ratio to stop:** 0.071122 / 0.05 = **~1.42×** (display **1.42×**). Was **1.73×** at 0.086466@N=20409.

Prior currency package (superseded as-current for lcdm):
[`../machine_r1_currency_20260804d/`](../machine_r1_currency_20260804d/) — lcdm 0.086466@N=20409 era (routeD update); pointer added on that REPORT. dyad + routeD numbers there remain current.

Claude red (ForGrok&Claude.md, 2026-08-04 ~13:0x) reported the same lcdm stamp and withdrew permanent “nearest-and-receding” as living-doc narrative; this package implements that framing.

---

## 2. Quote-ready live numbers

| chain | N (progress) | timestamp | R−1 last | stop | `converged` | bookable? | vs stop |
|---|---:|---|---:|---:|---|---|---|
| `cmp_lcdm_mnu_bbnfix` | **21886** | **2026-08-04T13:01:13** | **0.071122** | 0.05 | **false** | **NO** | **1.42×** (was 0.086466@N=20409) |
| `dyad_mnu_bbnfix` | **20302** | 2026-08-04T03:25:56 | **0.128943** | 0.05 | **false** | **NO** | **~2.58×** (**UNCHANGED**) |
| `cmp_prtoe_routeD` | **3290** | 2026-08-04T09:00:36 | **4.941933** | 0.1 | **false** | **NO** (early) | **~49.4×** (**UNCHANGED** improving stamp) |

**Key narrative:**

- lcdm **0.086466@N=20409 → 0.071122@N=21886** — new progress stamp; still **above** gate (**1.42×** stop).
- Historical **was 0.059** / **was 0.086** as past stamps are OK.
- Trajectory must include the new point after 0.086466: `… → 0.086466 → 0.071122`.
- **NOT** “nearest-and-receding forever” as permanent living narrative (direction adjectives go stale between checkpoints).
- Still **NOT bookable**; both bbnfix legs `converged: false`.
- dyad **UNCHANGED**. routeD **UNCHANGED** from 20260804d.
- **Book still REFUSED**. **No H₀** as result.
- MCMCs **not** killed/restarted; PolyChord **not** started.

Canonical phrase for living surfaces:

> lcdm R−1 **0.071122** (N=21886, t=2026-08-04T13:01:13; was 0.086466@N=20409; earlier 0.059@N=19013 — **1.42×** stop)

---

## 3. What this pass did

1. Re-ran `book_bbnfix_when_ready.py` (REFUSED; refuse card historical, not rewritten).  
2. Confirmed progress/checkpoint authority for lcdm / dyad / routeD.  
3. Updated living PRTOE surfaces + ForJustin pastes that quoted **0.086466 as current**.  
4. Extended lcdm trajectory through **0.071122**; retired permanent “nearest-and-receding” framing.  
5. Updated gate_fire REPORT live currency + next_triggers MASTER + board/queue stamps.  
6. Currency pointer on `machine_r1_currency_20260804d/REPORT.md`.  
7. Package files: this REPORT + [`EDITS.md`](EDITS.md).

### What this pass did **not** do

- Did not kill, pause, restart, or edit live MCMC chain files.  
- Did not start PolyChord.  
- Did not quote H₀ / Σm_ν / S₈ as results.  
- Did **not** rewrite historical `_runs/**` refuse cards or poll logs that correctly recorded 0.086 as then-current.  
- Did not invent progress R−1 beyond progress-file stamps.  
- Did not touch dual-gate / book logic.

---

## 4. Files changed

See [`EDITS.md`](EDITS.md) for path-by-path exact numbers written.

---

## 5. Next machine action (not executed)

1. Leave cobaya alone (bbnfix + routeD).  
2. bbnfix book only when **both** legs self-stop with progress R−1 < 0.05.  
3. Re-verify with `python3 scripts/book_bbnfix_when_ready.py` before any next currency pass.  
4. Do **not** freeze permanent direction adjectives on noisy R−1.

---

## Key numbers (summary strip)

| quantity | value |
|---|---|
| lcdm R−1 / N / t | **0.071122** / **21886** / **2026-08-04T13:01:13** |
| lcdm prior (superseded as-current) | 0.086466 / 20409 / 2026-08-04T05:21:52 |
| lcdm earlier (historical) | 0.059055 / 19013 |
| lcdm vs stop | **~1.42×** |
| lcdm `converged` | **false** |
| lcdm trajectory | 0.093682 → 0.053867 → 0.048827 → 0.059055 → 0.086466 → 0.071122 |
| dyad R−1 / N / t | **0.128943** / **20302** / 2026-08-04T03:25:56 (**UNCHANGED**) |
| routeD R−1 / N / t | **4.941933** / **3290** / 2026-08-04T09:00:36 (**UNCHANGED**) |
| book_bbnfix | **REFUSED** |
| framing | facts + N+t; **not** permanent “nearest-and-receding forever” |
| H₀ as result | **none** |

*NO FABRICATIONS. No MCMC kill. No PolyChord. No peek-book H₀. No historical _runs rewrites of old 0.086 refuse cards.*
