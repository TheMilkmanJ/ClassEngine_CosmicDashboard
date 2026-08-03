# T14 H_kin external recompute — smoke grade (2026-08-03)

**Path:** outsider / hard-win thread-closure support (not production 128³).  
**Script:** `scripts/ring_toroidal_hkin.py`  
**Grid:** SMOKE 64×64×128 only (`nice -n 19`).  
**Did not run / did not touch:** A4 production (`t14_hkin_i6_prod_20260803_090317`, 128³).

Recipe: `docs/working_logs/_runs/hard_win_t14_recompute_card/RECIPE.md`.

---

## Commands run

```bash
nice -n 19 python3 scripts/ring_toroidal_hkin.py --calibrate
nice -n 19 python3 scripts/ring_toroidal_hkin.py --smoke --null nowinding \
  --out docs/working_logs/_runs/t14_smoke_revalidate_nw
nice -n 19 python3 scripts/ring_toroidal_hkin.py --smoke --null nojet \
  --out docs/working_logs/_runs/t14_smoke_revalidate_nj
```

Artifacts:

| Step | Console / out |
|------|----------------|
| calibrate | `calibrate.log` (this dir) |
| nowinding | `nowinding_console.log` → `../t14_smoke_revalidate_nw/summary.json` |
| nojet | `nojet_console.log` → `../t14_smoke_revalidate_nj/summary.json` |

Elapsed wall (shared host with A4): nowinding ~753 s; nojet ~683 s.

---

## 1. Calibration (geometry Wr only)

| Target | Measured | Fence | Result |
|--------|----------|-------|--------|
| planar circle Wr | +0.0000 | \|Wr\| < 0.05 | **PASS** |
| noisy planar Wr | +0.0049 | \|Wr\| < 0.05 | **PASS** |
| helical n=3 \|Δ\| vs dense truth | 0.0000 | < 0.15 | **PASS** |
| helical n=2 \|Δ\| vs dense truth | 0.0000 | < 0.15 | **PASS** |

**CALIBRATION OVERALL: PASS**

---

## 2. Null `nowinding` (n=0, jet ±z) — H values & flip residual

Verdict frame selected blind at **t = 1.00** both branches (protocol: prefer t=1.00 when qualified).

| Branch | H | Tw | Wr | ampA | margin_ok |
|--------|---|----|----|------|-----------|
| n+0_f+1 | **−2.050×10⁻¹⁵** | −7.07×10⁻¹⁷ | −1.98×10⁻¹⁵ | ~0 | False* |
| n+0_f-1 | **−2.562×10⁻¹⁶** | 0 | −2.56×10⁻¹⁶ | ~0 | False* |

\* `margin_ok` requires \|H\| > 3× dial_spread; with \|H\|~0 this row is expected **not** to pass the *signal* margin — the null fence is smallness of H, not margin bookability.

### Fence table (RECIPE: nowinding \|H\| and flip residual < 0.2)

| Check | Value | Fence | Result |
|-------|-------|-------|--------|
| \|H\| (f=+1) | 2.050×10⁻¹⁵ | < 0.2 | **PASS** |
| \|H\| (f=−1) | 2.562×10⁻¹⁶ | < 0.2 | **PASS** |
| flip residual H(+)+H(−) | **−2.306×10⁻¹⁵** | \|res\| < 0.2 | **PASS** |
| max\|H\| over jet signs | 2.050×10⁻¹⁵ | < 0.2 | **PASS** |

Instrument booking string (four-branch true-mirror N/A for n=0 null):  
`instrument to the bench — true-mirror checks missing/unmeasured` — expected for null mode; **does not fail the nowinding fence**.

### C8 disclosure (Claude red 2026-08-03) — PASS is **selected-frame only**

Unselected candidate frames (full phase 16/16; genuine pool members) from
`nowinding_console.log`:

| Branch | t | H | note |
|---|---:|---:|---|
| n+0_f+1 | 0.50 | **−1.312** | would fail &lt;0.2 fence by ~6.6× if selected |
| n+0_f+1 | 1.50 | **−0.295** | also outside fence |
| n+0_f−1 | 0.50 | **+1.163** | would fail fence if selected |

Blind selector chose t=1.00 both branches (6 candidates each). The fence table
above applies to **selected verdicts only**. Transient ring helicity and large
|H| at other t are real instrument-readable frames, not buried.

### Anti-generalization to A4 (Claude G1/G2)

- **Smoke** nowinding: both branches selected t=1.00 from 6-cand pools, 16/16 phase everywhere.
- **Production 128³** nowinding: f−1 selected t=0.25 from **2** candidates with mid-frames NaN (nphase&lt;12/16). Smoke never entered that censored regime and **cannot cure** the production OPEN phase-coverage defect.
- Production [3/4] nojet early lines already differ: t=0.50 drift_phys **29.24%** vs smoke ~0.64%. Smoke "no false ring" has **zero predictive weight** for unfinished 128³ nojet frames.

---

## 3. Null `nojet` (winding only, n=±1)

| Branch | Verdict frame | Result vs fence |
|--------|---------------|-----------------|
| n+1_f+1 | **null** (no ring all t∈[0.25,1.50]) | no false ring |
| n−1_f+1 | **null** (no ring all t∈[0.25,1.50]) | no false ring |

Booking: `nothing graded (no ring / no verdict frame)`.

| Check | Fence | Result |
|-------|-------|--------|
| nojet | no false ring | **PASS** |

---

## 4. Acceptance summary vs RECIPE fences (smoke revalidate scope)

| Check | Fence | This run | Status |
|-------|-------|----------|--------|
| Cal planar + helix | PASS | all four geometry targets | **PASS** |
| nowinding \|H\| and flip residual | < 0.2 | max\|H\|=2.05e-15; flip res=−2.31e-15 | **PASS** |
| nojet | no false ring | both branches no verdict | **PASS** |
| True-mirror residual | smoke <10% | **not run** (four-branch full smoke out of this task; A4 owns prod) | N/A here |
| Margins \|H\| > 3× dial | signal branches only | nulls correctly non-bookable on margin | N/A (nulls) |
| Selector outcome-blind | no Tw/Wr/H in key | console: “blind key; Tw/Wr/H not used” | **PASS** (observed) |
| Pattern H ≈ sign(n)·2 | smoke four-branch | **not run** this path | N/A here |

### Overall smoke null / calibrate revalidate: **PASS**

Config-local instrument hygiene only. Not a sky-facing IGMF magnitude claim. Not production 128³ thread-closure (A4). Supports hard-win external recompute path at smoke grade.

---

## 5. Non-interference note

- A4 `run_t14_i6_production.sh --i-approve-a4` left running; out dir  
  `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/` untouched by this agent except read-only process checks.  
- All revalidate work used **`--smoke`** (64³) and **`nice -n 19`**.
