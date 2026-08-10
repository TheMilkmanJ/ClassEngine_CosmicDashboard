# RUNBOOK — bbnfix booking + Step C (when gate opens)

**Do not run multi-hour re-analyses “to check.”** Execute this file only when both
legs grade. Until then, every booking entrypoint refuses (exit 2).

Working directory: **repo root** `/home/themilkmanj/prtoe_class`.

---


---

## Publish split (Claude red 2026-08-04 — booking ≠ publishing)

`bash scripts/bbnfix_when_ready_all.sh` **defaults to NOT writing** `PRTOE_CHAIN_TABLES.md`.

1. **Stage A (default):** book + finalize H₀ letter (stdout) only.  
2. **Claude red:** audit the booking package; write  
   `docs/working_logs/_runs/bbnfix_booking_<id>/RED_AUDIT.md` with a line  
   `red: AGREE` or `red: AGREE-IF`.  
3. **Stage B:** `bash scripts/bbnfix_when_ready_all.sh --write-tables`  
   (refuses without stamp; `--force-tables` is owner emergency only).

Gate still: both R−1 < 0.05 **and** `converged: true`.


## Gate (must be true before any step below books)

| requirement | how to read |
|-------------|-------------|
| Both R−1 **< 0.05** | `tail -1 chains/dyad_mnu_bbnfix.progress` and `cmp_lcdm_mnu_bbnfix.progress` → field **4** (Rminus1) |
| Both self-stop | `grep converged chains/dyad_mnu_bbnfix.checkpoint chains/cmp_lcdm_mnu_bbnfix.checkpoint` → `converged: true` |
| Ranks present | `chains/<root>.{1,2,3}.txt` for both roots |
| Chains idle | do not GetDist while ranks still writing |
| Stack | BBN-fixed pair only (`dyad_mnu_bbnfix` + `cmp_lcdm_mnu_bbnfix`) |

```bash
cd /home/themilkmanj/prtoe_class
tail -1 chains/dyad_mnu_bbnfix.progress chains/cmp_lcdm_mnu_bbnfix.progress
grep -E 'converged|Rminus1_last' \
  chains/dyad_mnu_bbnfix.checkpoint chains/cmp_lcdm_mnu_bbnfix.checkpoint
```

Safe anytime smoke (≪1 min; must refuse while over bar):

```bash
python3 scripts/book_bbnfix_when_ready.py
# → REFUSED exit 2 until gate open
```

---

## Option 1 — one command (preferred)

Runs only if book succeeds; exits **2** if refuse.

### Stage A (default — booking only; tables OFF)

```bash
cd /home/themilkmanj/prtoe_class
bash scripts/bbnfix_when_ready_all.sh
# WRITE_TABLES=0 by default → stops after book + finalize (+ delta); no shelf write
```

### Stage B (publish tables — only after red audit)

```bash
# Claude first writes: docs/working_logs/_runs/bbnfix_booking_<id>/RED_AUDIT.md
# with a line: red: AGREE   (or red: AGREE-IF)
bash scripts/bbnfix_when_ready_all.sh --write-tables
# refuses (exit 1) without RED_AUDIT stamp
```

Optional flags:

```bash
bash scripts/bbnfix_when_ready_all.sh --skip-tables   # explicit no-op; default already skips
bash scripts/bbnfix_when_ready_all.sh --skip-delta    # skip Δχ² proxy
bash scripts/bbnfix_when_ready_all.sh --force-tables  # OWNER emergency only — bypasses red
```

Pipeline order inside the script:

1. Snapshot progress / checkpoint  
2. `python3 scripts/book_bbnfix_when_ready.py`  
3. `python3 scripts/finalize_h0_at_convergence.py`  
4. **Tables only if Stage B:** `make_getdist_tables.py --include-bbnfix`  
   (default **skipped** until `--write-tables` + `RED_AUDIT`)  
5. `python3 scripts/bbnfix_delta_chi2_proxy.py` (proxy only; not Laplace)

Then optional CosmicForge Laplace (manual — see Step C.2 below). **Not** auto-launched.

---

## Option 2 — ordered manual commands

### Step 0 — confirm gate (seconds)

```bash
cd /home/themilkmanj/prtoe_class
python3 scripts/book_bbnfix_when_ready.py
# Must print BOOKED (exit 0). If REFUSED (exit 2): stop. Do not continue.
```

If you only want the letter path first:

```bash
python3 scripts/finalize_h0_at_convergence.py
# NOT YET (exit 2) until both R−1 + self-stop; graded → letter sentence on stdout
```

### Step A — H₀ letter gate (seconds; edits nothing)

```bash
python3 scripts/finalize_h0_at_convergence.py
```

| | |
|---|---|
| **Reads** | progress R−1; rank-1 H₀ (50% burn) when graded |
| **Writes** | nothing (stdout only) |
| **Manual** | paste printed sentence into Fairbank letter Status; close HOLD #1 with date + both R−1 |

Prefer three-rank GetDist H₀ from Step B for public quote.

### Step B — production GetDist booking (minutes)

```bash
python3 scripts/book_bbnfix_when_ready.py
```

| | |
|---|---|
| **Hard gate** | both R−1 < 0.05 **and** `converged: true` |
| **Reads** | three ranks via GetDist `loadMCSamples`, ignore_rows=0.3 |
| **Writes** | `docs/working_logs/_runs/bbnfix_booking_<stamp>/REPORT.md` + `booking.json` |
| **Params** | H0, m_ncdm, omega_b, S8 (if present) |

Optional tables + triangles (rank-1 only; **overwrites** `docs/PRTOE_CHAIN_TABLES.md`):

```bash
python3 scripts/make_getdist_tables.py --include-bbnfix
# If gate NOT satisfied (book refuses: R−1≥0.05 and/or not self-stopped): exit 2, does NOT write tables
# If dual gate open (both R−1 < 0.05 AND converged:true): exit 0, may write tables
#   — production publish prefers bash scripts/bbnfix_when_ready_all.sh --write-tables
#     only with RED_AUDIT path (Stage B after red: AGREE / AGREE-IF)
# After success: restore live-status banner on PRTOE_CHAIN_TABLES.md if clobbered
# Do NOT use --force-bbnfix for booking (writes UNBOOKABLE working_logs only; never living shelf)
```

Sync living docs only after book card lands (manual):

- `docs/working_logs/_chain_snapshot.md` — pair **booked**, final R−1 / N  
- `docs/PRTOE_CHAIN_TABLES.md` — bookable rows; restore banner  
- `docs/PRTOE_REFEREE_CALENDAR.md` Sitting NOW  
- `docs/PRTOE_CODE_MANIFEST.md` §1 live rows  
- `docs/working_logs/T11_hubble_owed.md` machine half  

### Step C — Laplace / evidence under BBN-fixed stack

Standing method: **Laplace-from-MCMC** (docket #155). **No** PolyChord.

#### C.1 — Δχ² proxy (fast; not full evidence)

```bash
python3 scripts/bbnfix_delta_chi2_proxy.py
# Optional peek while over bar (UNBOOKABLE): --force-peek
# Optional JSON: --out docs/working_logs/_runs/bbnfix_delta_<stamp>.json
```

Report **Δ(min −logpost)** = model − control with explicit caveat:

- missing Hessian volume terms and prior measure  
- **not** bookable as Laplace ΔlnZ  
- do **not** substitute pre-bbnfix ΔlnZ ≈ +2.6  

#### C.2 — CosmicForge Laplace (Hessian) — bookable ΔlnZ if configured correctly

There is **no** standalone `scripts/laplace_bbnfix.py`. CosmicForge computes:

```text
log_z_laplace = -0.5 * χ² + 0.5 * n * log(4π) - 0.5 * logdet(Hessian)
```

in `run_cosmicforge.py` (~L2083–2095), method label **Laplace (Hessian)**.

**Only after** the pair has self-stopped (or owner accepts CPU contention risk).  
Confirm CLI before launch:

```bash
python3 run_cosmicforge.py --help | head -40
```

Shape (example — **confirm** production yamls match the BBN-fixed stack used for the chains):

```bash
# Model (dyad BBN-fixed)
python3 run_cosmicforge.py dyad_mnu_bbnfix.yaml --cores <N> --mcmc-steps 0
# Control twin
python3 run_cosmicforge.py cmp_lcdm_mnu_bbnfix.yaml --cores <N> --mcmc-steps 0
```

Notes:

- `--mcmc-steps 0` aims for optimizer/Hessian path without a long MH re-run; still re-calls CLASS at mode fit — can be long.  
- Book printed `log_z_laplace` for model and twin; **ΔlnZ = lnZ_model − lnZ_ΛCDM**.  
- Label method **Laplace (Hessian)** and stack **BBN-fixed** (`dyad_mnu_bbnfix` / `cmp_lcdm_mnu_bbnfix`).  
- Do **not** pass `--polychord` / `--run-polychord` / `--cross-validate` for this booking session.  
- If CosmicForge yaml/mode path is unclear or fails, **stop** — prefer C.1 proxy with caveats rather than inventing a Hessian CLI.

#### C.3 — Bridge sampling (non-default)

`forge/evidence.py` (Meng–Wong) only if Laplace disputed or posterior clearly non-Gaussian.  
Costs many fresh likelihood evals. Not the default booking path.

#### C.4 — Never

```bash
# DO NOT for booking on this box:
# python3 run_cosmicforge.py ... --polychord
# run_polychord_pair.sh / nested sampling reopen
```

---

## What files get updated when the gate opens

| file | update |
|---|---|
| `_runs/bbnfix_booking_<stamp>/REPORT.md` + `booking.json` | bookable GetDist marginals |
| stdout of `finalize_h0_at_convergence.py` | letter H₀ sentence (manual paste) |
| `docs/plots/*bbnfix*_triangle.png` | if tables step run |
| `docs/PRTOE_CHAIN_TABLES.md` | if tables step run — restore banner |
| living docs (manual list above) | after book card |
| optional evidence note | only after C.1/C.2 under **this** stack |

Nothing auto-commits. Nothing kills chains.

---

## RouteD (separate — stop 0.1)

Not part of the letter H₀ pair. When `cmp_prtoe_routeD` R−1 < 0.1 and self-stops,
add to GetDist separately. Do not substitute for bbnfix.

---

## Failures / refuse codes

| exit | meaning |
|-----:|---------|
| 0 | success / booked (Stage A) or tables written (Stage B) |
| 2 | gate refuse (not ready) — expected until pair grades |
| 1 | unexpected error after gate **or** Stage B missing RED_AUDIT |
| 3 | `bbnfix_delta_chi2_proxy.py --force-peek` under open gate (UNBOOKABLE) |

---

## Kill criteria (any = stop; do not claim done)

| # | kill if… |
|---|----------|
| K1 | Book while either R−1 ≥ 0.05 |
| K2 | Book before both `converged: true` |
| K3 | Quote peeks / force GetDist / force Δχ² as bookable results |
| K4 | Living shelf written from `--force-bbnfix` (must stay UNBOOKABLE path) |
| K5 | Stage B tables without `RED_AUDIT` (`red: AGREE` / `AGREE-IF`) except owner `--force-tables` |
| K6 | PolyChord / nested sampling for booking |
| K7 | Kill live MCMCs without owner order |
| K8 | Promote pre-bbnfix ΔlnZ ≈ +2.6 as final bbnfix evidence without fence |
| K9 | RouteD substitute for letter H₀ pair |
| K10 | Invent a Laplace number or invent `scripts/laplace_bbnfix.py` |

---

## Laplace prep vs waits for bbnfix book

| ready now (prep only) | waits for Stage A book |
|-----------------------|------------------------|
| Gate refuse paths on all entrypoints | Bookable three-rank H₀ / Σm_ν / S8 |
| CosmicForge Hessian formula in `run_cosmicforge.py` | Bookable ΔlnZ under **BBN-fixed** stack |
| Δχ² proxy script (gate-hard) | Proxy number itself |
| Historical pre-bbnfix ΔlnZ ≈ +2.6 (fenced) | Replacing standing claim with bbnfix ΔlnZ |
| MISSING honest: no `scripts/laplace_bbnfix.py` | Inventing that CLI |

---

## Quick reference (copy-paste when gate open)

```bash
cd /home/themilkmanj/prtoe_class
# Stage A
bash scripts/bbnfix_when_ready_all.sh
# → red audit RED_AUDIT.md on the booking package
# Stage B
bash scripts/bbnfix_when_ready_all.sh --write-tables
# optional CosmicForge Laplace per Step C.2 if capacity
# then manual living-doc sync + letter paste
```

*NO FABRICATIONS. NO POLYCHORD. NO EARLY BOOK. booking ≠ publishing.*
