# RouteD post-reseed health — 2026-08-03 ~10:23 MDT

**Verdict: ALIVE and sampling (burn-in). Leave alone. Do not reseed.**

---

## 1. Alive?

| Check | Status |
|---|---|
| MPI parent | PID 175453 `mpirun -n 3 … cobaya.run cmp_prtoe_routeD.input.yaml` |
| Workers | PIDs 175457 / 175458 / 175459 — each ~110% CPU, ~2.0% MEM |
| Elapsed | ~1h16 since launch (~09:07 MDT) |
| Lock | `cmp_prtoe_routeD.input.yaml.locked` present (0 B) |
| Launchlog | Growing; last line 10:22:00 MDT |
| Crashes / Tracebacks | None (only benign `candl_data` import warn; candl likelihoods still init OK) |

**Yes — process-alive and CPU-bound on CLASS evaluations.**

---

## 2. Sampling?

Yes. Cobaya MCMC burn-in in progress on all 3 ranks:

```
[0] 10:21:42  756 steps  — still burning in, 342 accepted steps left
[1] 10:22:00  870 steps  — still burning in, 266 accepted steps left
[2] 10:21:29  771 steps  — still burning in, 345 accepted steps left
```

Log also states: *“no accepted step will be saved until 50 burn-in samples have been obtained”* (`burn_in: 50` in yaml; oversample/blocking inflates the “accepted steps left” counter from 800 → ~266–345 now).

Rough burn-in acceptance (Δacc / Δsteps since start):

| Rank | Steps | Acc left | ~acc rate |
|---|---:|---:|---:|
| 0 | 756 | 342 | **0.61** |
| 1 | 870 | 266 | **0.61** |
| 2 | 771 | 345 | **0.59** |

This is healthy Metropolis acceptance. Contrast archived pre-reseed run: acceptance ≈ 1.0 (oversampled / not true MH mixing) and R−1 = 44.8 @ N=3182.

**ETA to end of burn-in (order-of-magnitude):** ~40–60 min wall from check time if rates hold; then `cmp_prtoe_routeD.[1-3].txt` should appear.

---

## 3. Any samples yet?

**No live chain samples.**

| Artifact | State |
|---|---|
| `chains/cmp_prtoe_routeD.[1-3].txt` | **Absent** |
| `cmp_prtoe_routeD.progress` | Header only (no N / R−1 rows) |
| `cmp_prtoe_routeD.checkpoint` | `converged: false`, `Rminus1_last: .inf`, `burn_in: 50`, `mpi_size: 3` |
| `cmp_prtoe_routeD.covmat` | Seed copy from reseed (mtime 09:04; not yet learned) |

Archived pre-reseed samples live under `chains/_archive_routeD_reseed_20260803_0858/` (~1276/1313/1312 rows) — not part of the live run.

---

## 4. Basin coherence / rank H0–mlp spread

### Live samples
**Not assessable** — zero post-burn samples. No rank H0 / minuslogpost (mlp) spread to compute.

### Seed / basin meta (`routeD_basin_meta.json` = reseed stamp `20260803_0858`)

| Field | Value |
|---|---|
| winner_rank | 1 |
| best_mlp | **1375.844** |
| n_basin | 3241 (mlp ≤ best+δ, δ=8) |
| scale | 0.25 (eig-floored cov std scale) |
| covmat | `routeD_basin.covmat` / `routeD_reseed_20260803_0858.covmat` |

Key ref vs basin-mean (pre-reseed basin, not live):

| param | ref (global best) | basin mean | mean−ref |
|---|---:|---:|---:|
| **H0** | 69.540 | 69.188 | **−0.35** |
| z_reio | 7.983 | 7.659 | −0.32 |
| dcdf_conv_g | 0.208 | 0.241 | +0.034 |
| dcdf_floor_thaw | 0.031 | 0.051 | +0.020 |
| m_ncdm | 0.0080 | 0.0115 | +0.0035 |

Live **initial points** (drawn near refs) — coherent, no rank outlier:

| Rank | H0 | z_reio | m_ncdm |
|---|---:|---:|---:|
| 0 | 69.645 | 8.040 | 0.0157 |
| 1 | 69.712 | 8.196 | 0.0109 |
| 2 | 69.720 | 8.238 | 0.0038 |

H0 spread across starts ≈ 0.08 km/s/Mpc — tight vs prior basin issues (archived z_reio last-half split ~7.84 / 7.95 / 7.04).

---

## 5. Risks / next action

### Risks (watch, do not act yet)
1. **Historical failure mode** (archived run): R−1 stayed huge (129 → 44.8) with z_reio rank split and acceptance ≈ 1.0. Reseed was the correct response; that pathology is not yet visible here.
2. **`learn_proposal_Rminus1_max[_early]: 10000`** — proposal will not adapt until R−1 is absurdly large *or* gates are later lowered. Fixed basin covmat must carry the early chain. Intentional per reseed notes.
3. **No samples yet** — health is process-level only; first real coherence check is after burn-in when `.txt` rows and first `progress` R−1 appear.
4. **Slow CLASS + full dataset** (Planck + DESI BAO + Pantheon+SH0ES + ACT DR6 + SPT3G) — wall time is expected; low step rate is not a hang (CPU 110%, log advancing every ~2 min).

### Next action
**Leave alone.** Do **not** reseed again.

Re-check triggers (any one):
- After burn-in: `cmp_prtoe_routeD.[1-3].txt` exist and grow.
- First non-header `progress` row with finite R−1.
- Hang signal: launchlog stall >30–45 min **and** CPU collapse.
- Pathology signal post-samples: acceptance → ~1.0 again, or rank H0 / z_reio means diverge like the archived split.

Suggested next health window: **~1–2 h after this report** (post burn-in), then recompute rank H0/mlp spreads if N ≳ few hundred per rank.

---

## 6. Non-claims

- **Not** a convergence claim. R−1 = ∞; burn-in incomplete.
- **Not** a cosmology / H0 measurement from this run. No saved samples.
- **Not** a proof that the basin reseed fixed the z_reio multi-modal failure — only that start points and early acceptance look healthy.
- **Not** booking-grade chain status for bbnfix or routeD science claims.
- Basin meta `best_mlp=1375.844` is from the **archived** pre-reseed chains, not the live chain.
- Candl import warning is non-fatal here; ACT/SPT likelihoods initialized successfully.

---

## Artifact map

| Path | Role |
|---|---|
| `chains/cmp_prtoe_routeD.input.yaml` | Live config (refs = global best; covmat = basin) |
| `chains/cmp_prtoe_routeD.launchlog` | Live progress log |
| `chains/cmp_prtoe_routeD.progress` | Empty (header only) |
| `chains/cmp_prtoe_routeD.checkpoint` | Unconverged |
| `chains/routeD_basin_meta.json` | Reseed basin meta |
| `chains/routeD_basin.covmat` | Active proposal covmat |
| `chains/_archive_routeD_reseed_20260803_0858/` | Killed run + WHY_ARCHIVED.md |

**Diagnosed:** 2026-08-03 10:23 MDT  
**Live run start:** 2026-08-03 ~09:07 MDT (post reseed 08:58)
