# BBN dense ε_max(T_c) residual — status 2026-08-03

**Task:** Address UNVERIFIED dense ε_max(T_c) residual for `papers/bbn-eps-bound` if cheap  
(<15 min short grid with existing tools).  
**Verdict:** **NOT CHEAP on this host. Grid not run. Residual remains UNVERIFIED.**  
No new ε_max numbers invented or booked.

---

## 1. What the residual is

From `papers/bbn-eps-bound/README.md` and `main.tex` § “Conservative T_c scan (method only; not produced here)”:

| item | status |
|---|---|
| Bound at measured T_c = 179 keV | **Verified** — ε < 3.2% (2σ) vs Aver, from dY_p/dε = 0.00163 / %ε |
| Dense ε_max(T_c) over free window [70, 500] keV | **UNVERIFIED / not produced** |

Paper method (no new physics): re-measure helium elasticity on a T_c grid at fixed N_eff and code ω_b; invert each elasticity against Aver; report upper envelope ε_max(T_c); if a single number is needed, quote only the **most permissive** (largest) ceiling — never a tighter bound at an unmeasured T_c.

Standing numbers (unchanged by this run):

| quantity | value | source |
|---|---:|---|
| Y_p⁰ (ε=0) | 0.246891 | windowed PRyM baseline |
| Y_p (window) | 0.248995 | ramp at T_c=179 keV, ε≃1.2543% |
| dY_p/dε (paper) | 0.00163 / %ε | four-point ε scan at T_c=179 keV |
| Aver Y_p | 0.2453 ± 0.0034 | Aver et al. 2021 |
| 2σ ceiling @ 179 keV | ε < 3.20% | (Aver+2σ−Y_p⁰)/0.00163 |

Arithmetic recompute already logged:  
`docs/working_logs/_runs/hard_win3_bbn_eps_recompute_20260803/`.

---

## 2. Elasticity notes (docs)

`docs/PRTOE_bbn_witness.md`:

- Ramp: ε(T) = ε · (1 − T/T_c); production splice default T_c = **179 keV**, ε ≈ 1.24–1.2543%.
- Kernel re-pin T_c = 177.10 keV priced as ~0 within solver non-smoothness when combined with ε update.
- Window effect only (PRyM default ω_b): Y_p 0.246891 → 0.248995 (+0.852%).
- Scripts named: `prym_ramped_splice.py`, `prym_supersession_pricing.py`, `prym_omega_b_elasticity.py`.

Supersession pricing recorded a **narrow D/H-only** T_c scan (0.150–0.210 MeV) — **no Y_p**, so it cannot invert to ε_max(T_c).

---

## 3. Existing tools

| path | role |
|---|---|
| `scripts/prym_ramped_splice.py <shift> [T_c_MeV] [omega_b_scale]` | **Production ramp** — exact tool for the paper method. Default T_c=0.179 MeV. Prints `RAMPED ... YPCMB YPBBN ...`. |
| `scripts/prym_elasticity_runner.py` / `tools/PRyMordial/run_elasticity.py` | LT/MTLT **step** splices (zone brackets), not continuous ramp in T_c. |
| `tools/PRyMordial/run_windowed.py` | Fixed shift 1.0124 LT/MTLT bracket. |
| `scripts/prym_omega_b_elasticity.py` | ω_b power-law; not T_c grid. |
| `scripts/prym_supersession_pricing.py` | Narrow T_c scan for D/H pricing only. |

PRyM tree present at `tools/PRyMordial/` (vendored, gitignored).

---

## 4. Timing probe (ran; grid did not)

```text
nice -n 19 python3 scripts/prym_ramped_splice.py 1.012543 0.179
→ ELAPSED_SEC 244.84  (~4.1 min)
→ RAMPED ... YPBBN=0.249019  (booked windowed Y_p=0.248995; small path/numba delta — not re-booked)
```

Host snapshot: **nproc=1**, ~23 GiB RAM, numba 0.66.0 + numpy 2.4.6.

Cost estimate for a short grid (serial only; single core):

| N T_c points | ≈ wall time |
|---:|---:|
| 1 (probe) | 4.1 min |
| 5 | ~20 min |
| 8 | ~33 min |
| 10 | ~41 min |

**Threshold was <15 min.** Even a 5-point grid exceeds it. Parallelism does not help on nproc=1.  
**Decision: do not invent ε_max(T_c); leave residual UNVERIFIED; file NEXT ISSUE.**

Artifact: `timing_probe.txt` in this directory.

---

## 5. NEXT ISSUE — command plan only

**Title:** Produce short ε_max(T_c) grid for bbn-eps-bound ([70, 500] keV)  
**Goal:** Close UNVERIFIED dense ε_max(T_c) residual with production PRyM ramp elasticities.  
**Do not:** invent ceilings; quote tighter bounds at unmeasured T_c without the envelope rule; use EMPRESS as an upper limit; float ΔN_eff; use D/H for the derivative bound.

### Method (matches paper)

1. Fix ε_ref = 1.2543% → `shift = 1.012543`, ω_b scale = 1.0, standard N_eff.  
2. Baseline once: `shift = 1.0` → Y_p⁰ (or use booked 0.246891 if bit-identical).  
3. For each T_c on the grid: run ramped splice → Y_p(T_c, ε_ref).  
4. Elasticity: `dY_p/dε = (Y_p − Y_p⁰) / 1.2543` per %ε.  
5. Invert Aver (0.2453 ± 0.0034):
   - `ε_max_nσ(T_c) = (0.2453 + n·0.0034 − Y_p⁰) / (dY_p/dε)` for n=1,2  
   - Only valid where dY_p/dε > 0 and linear response holds.  
6. Report table ε_max(T_c); if one number required, **max_T ε_max_2σ** only.

### Suggested short grid (8 T_c, MeV)

`0.070  0.100  0.150  0.179  0.250  0.300  0.400  0.500`  
(includes paper anchor 179 keV + edges of free window)

Optional denser later: log-spaced 15–20 points once short grid validates.

### Commands (repo root)

```bash
OUT=docs/working_logs/_runs/bbn_eps_max_grid_YYYYMMDD
mkdir -p "$OUT"

# (A) baseline ε=0 once  [~4 min]
nice -n 19 python3 scripts/prym_ramped_splice.py 1.0 0.179 \
  | tee "$OUT/baseline.txt"

# (B) short T_c grid at paper ε_ref  [~33 min serial @ ~4.1 min/pt]
for Tc in 0.070 0.100 0.150 0.179 0.250 0.300 0.400 0.500; do
  echo "=== Tc=$Tc $(date -Is) ===" | tee -a "$OUT/grid_raw.txt"
  nice -n 19 python3 scripts/prym_ramped_splice.py 1.012543 "$Tc" \
    | tee -a "$OUT/grid_raw.txt"
done

# (C) post-process (parse RAMPED lines; field YPBBN = column 8 after split)
python3 - <<'PY'
# RAMPED shift eps% Tc wb Neff YPCMB YPBBN DoH He3 Li7
from pathlib import Path
import re
out = Path("docs/working_logs/_runs/bbn_eps_max_grid_YYYYMMDD")
# set Yp0 from baseline RAMPED or booked 0.246891
Aver, sig = 0.2453, 0.0034
eps_ref = 1.2543
# ... parse grid_raw.txt, compute dYp_deps, eps_1sig, eps_2sig per Tc ...
# write table.csv + REPORT.md; no hand-typed ceilings
PY
```

### Runtime / env notes

- Expect **~4 min per splice** on this single-core host (probe: 244.84 s).  
- Budget **~35–45 min** for 8 points + baseline, or run overnight.  
- Prefer production path with numba ON if numpy/numba compatible (comments in `prym_omega_b_elasticity.py`); otherwise pure-numpy is slower but usable — **do not mix** numba-ON and numba-OFF elasticities in one table without a re-anchor.  
- Cross-check: T_c=0.179 must recover paper window Y_p ≈ 0.248995 and dY_p/dε ≈ 0.00163 (or audit 0.001677) before trusting other T_c.  
- Linearity: if any T_c shows |ΔY_p| ≪ solver noise, do not invert; mark point non-constraining.

### Acceptance

- [ ] Table of (T_c, Y_p, dY_p/dε, ε_max_1σ, ε_max_2σ) for ≥5 points spanning [70,500] keV  
- [ ] Anchor T_c=179 keV matches paper arithmetic to ~few percent  
- [ ] Most-permissive 2σ ceiling stated separately from measured-T_c bound  
- [ ] `papers/bbn-eps-bound/README.md` UNVERIFIED row updated only after numbers exist  
- [ ] No EMPRESS-based ε ceiling; no chain-dependent D/H prediction

### Out of scope for this issue

- Full dense curve for paper figure (can follow short grid).  
- Re-deriving Y_p⁰ from nuclear-rate compilations.  
- MCMC or joint CMB–BBN.

---

## 6. Bottom line

| question | answer |
|---|---|
| Residual closed? | **No** — still UNVERIFIED |
| Grid executed? | **No** (would exceed 15 min) |
| Timing known? | **Yes** — ~245 s / ramped splice |
| Tool ready? | **Yes** — `scripts/prym_ramped_splice.py` |
| Numbers invented? | **None** |
| Next action | Execute §5 command plan when ≥35 min budget available |
}
