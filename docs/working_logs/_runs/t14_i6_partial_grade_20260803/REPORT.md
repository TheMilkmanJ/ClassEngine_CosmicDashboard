# R1-t14-i6 A4 production — partial grade (logs as of ~2026-08-03 10:42 MDT)

**Role:** blue team monitor / grade  
**Run path:** `docs/working_logs/_runs/t14_hkin_i6_prod_20260803_090317/`  
**Console:** `docs/working_logs/_runs/t14_i6_production_console.log`  
**Skeleton:** `docs/working_logs/_runs/t14_i6_TC_SKELETON.md`  
**NO FABRICATIONS:** every number below is from console / `summary.json` on disk.  
**Status at grade:** **IN FLIGHT** — step **[3/4] null nojet**, branch `n+1_f+1` started (no t-lines yet on prod console).  
**Do not kill; do not start new 128³ runs.**

---

## Pipeline steps

| Step | Status | Evidence |
|---|---|---|
| [1/4] calibrate | **PASS** | `calibrate.log` |
| [2/4] null nowinding | **COMPLETE** | `null_nowinding/summary.json` elapsed **5684.48 s** |
| [3/4] null nojet | **IN PROGRESS** | process alive; console header + BRANCH n+1_f+1 |
| [4/4] four-branch | **NOT STARTED** | — |

---

## 1. Calibration (complete)

| Target | Result | Tol | Gate |
|---|---:|---:|---|
| planar circle Wr | +0.0000 | ±0.05 | PASS |
| noisy planar Wr | +0.0049 | ±0.05 | PASS |
| helical ring Wr | inst=truth −0.5722, \|Δ\|=0 | 0.15 | PASS |
| helical n=2 Wr | inst=truth −0.1785, \|Δ\|=0 | 0.15 | PASS |

**CALIBRATION OVERALL: PASS**

Grid: **128×128×256**, `T_MAX=1.5`, protocol 2026-08-03, blind selector (Tw/Wr/H not used in key).

---

## 2. nowinding — complete (from `summary.json`)

### 2a. `n+0_f+1`

| field | value |
|---|---|
| selected t | **1.0** |
| H | **1.873e−15** (numerical zero) |
| W / Tw / Wr | ~−1.4e−16 / ~−1.4e−16 / ~2.0e−15 |
| ampA | 3.13e−17 |
| nphase | 16 |
| drift_phys | **0.03983** (3.983%) |
| dial_spread | ~1.01e−15 |
| margin_ok | **false** (expected for null: \|H\|≈0) |

### 2b. `n+0_f-1`

| field | value |
|---|---|
| selected t | **0.25** |
| H | **0.0** |
| W / Tw / Wr | 0 / 0 / 0 |
| ampA | 8.65e−4 |
| nphase | 16 |
| drift_phys | **0.07305** (7.305%) |
| dial_spread | ~5.55e−17 |
| margin_ok | **false** |

### 2c. Intermediate frames on `n+0_f-1` (console — not hidden)

| t | phase | H / W / Tw | note |
|---:|---|---|---|
| 0.25 | 16/16 | finite H=0 | **selected** |
| 0.50–1.00 | **0/16** | **NaN** | phase-blind |
| 1.25 | **8/16** | **NaN** H | below gate (8 < 12) |
| 1.50 | 16/16 | finite H≈0 | second candidate |

Code path (`ring_toroidal_hkin.py:298`): **W/Tw/H go NaN when `nphase < NBINS−4` i.e. fewer than 12/16 phase bins** — not only when nphase=0. The t=1.25 frame (8/16) NaNs through that gate. (Claude red C1a wording cure 2026-08-03.)

### 2d. Booking string written by runner (nowinding only)

> instrument to the bench — true-mirror checks missing/unmeasured (not a measured violation)

True-mirror pairs missing because this null only runs n=0 branches. Four-branch true-mirror is step [4/4].

---

## 3. Gate table (partial — no fabrications)

| Gate | Target | Result |
|---|---|---|
| Calibrate planar+helix | PASS | **PASS** |
| nowinding \|H\| ≪ 0.2 | yes | **PASS** at selected frames (H≈0) |
| nowinding phase coverage all frames | clean | **FAIL mid-branch f−1** (NaN when nphase&lt;12/16; 4/6 frames instrument-blind; 2-candidate pool) — **OPEN** |
| nojet | no false ring | **TBD** |
| True-mirror residual | **&lt;5%** at 128³ | **TBD** (four-branch) |
| Margins \|H\|&gt;3×spread | all four | **TBD** / nulls expect margin_ok=False |
| Blind selector | no Tw/Wr/H | **held** on recorded SELECTED lines |

---

## 4. What is NOT claimed

- Production booking of sign(H_kin vs n)
- True-mirror residual measured
- nojet clean
- “almost bookable” on bbnfix (lcdm R−1≈0.054, dyad≈0.160 — both ≥ stop)
- Cosmological / sky-facing sign

---

## 5. Red / referee ask (pre-TC)

**Claude C1 (partial):** attack (a) phase-blind NaNs on f−1 as instrument defect vs expected null pathology; (b) ampA≈0 on f+1 null interpretation; (c) do not allow blue to claim nowinding “fully clean” without stating mid-frame NaNs.  
**ChatGPT:** process AGREE that partial grade is record-backed; REMAND any full A4 TC filed before [3/4]+[4/4] artifacts exist.

**Next blue:** finish nojet + four-branch → fill `t14_i6_TC_SKELETON.md` only from files.
