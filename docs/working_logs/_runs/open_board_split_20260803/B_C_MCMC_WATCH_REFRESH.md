# B–C MCMC watch refresh — bbnfix + routeD

**Stamp time (local):** 2026-08-03T23:56:41-0600  
**Stamp time (UTC):** 2026-08-04T05:56:41Z  
**Agent:** Grok blue — **watch only** (no kill / reseed / book MCMC; no PolyChord)  
**Source of R−1:** last line of `*.progress` field 4 + `Rminus1_last` / `converged` in `*.checkpoint`  
**Prior stamp:** `B_C_MCMC_WATCH.md` @ 2026-08-03T23:33 local (same progress tails; no new Cobaya GR row since)  
**Finalize gate:** `python3 scripts/finalize_h0_at_convergence.py` → **NOT YET**

---

## Explicit non-action

| Action | Status |
|--------|--------|
| Book H₀ / Σm_ν / Ω_b h² / S8 posteriors | **DO NOT BOOK** |
| Kill / reseed / restart any chain | **DO NOT** |
| PolyChord / nested sampling | **DO NOT** (this box) |
| Treat lcdm under-bar dip as pair-ready | **NO** — both R−1 **and** self-stop |
| Treat routeD as bookable thaw | **NO** |

**Booking bar (hard-win #1):** R−1 **< 0.05** on **both** `cmp_lcdm_mnu_bbnfix` and `dyad_mnu_bbnfix`, **and** Cobaya self-stop (`converged: true`) on both, chains idle.  
Until **BOTH** legs clear on **BOTH** chains → **NOT bookable**.

---

## R−1 table (this stamp)

| chain | N (progress) | progress timestamp | acceptance (oversampled) | **R−1** | checkpoint `Rminus1_last` | `converged` | vs bar |
|-------|-------------:|--------------------|-------------------------:|--------:|--------------------------:|:-----------:|:-------|
| `cmp_lcdm_mnu_bbnfix` | 19013 | 2026-08-03T21:05:36.968557 | 0.983857 | **0.059055** | 0.05905511181721022 | **false** | **above** 0.05 (was 0.048827 @ N=17458, bounced) |
| `dyad_mnu_bbnfix` | 18837 | 2026-08-03T17:57:59.890097 | 0.99672 | **0.189201** | 0.18920075919140164 | **false** | **above** (far; ~3.8× stop) |
| `cmp_prtoe_routeD` | 1609 | 2026-08-03T20:53:57.575011 | 1.0 | **102.794555** | 102.79455471855752 | **false** | N/A (stop 0.1; early burn-in) |

### Delta vs prior `B_C_MCMC_WATCH.md` (23:33 local)

| field | change |
|-------|--------|
| progress last rows | **unchanged** (no new R−1 print since 21:05 lcdm / 17:57 dyad / 20:53 routeD) |
| checkpoints | **unchanged** (`converged: false` all three) |
| chain `*.{1,2,3}.txt` | **still growing** (live MPI as of stamp) |

### Raw last progress lines

```
# cmp_lcdm_mnu_bbnfix.progress
19013.000000 2026-08-03T21:05:36.968557  0.983857  0.059055 NaN

# dyad_mnu_bbnfix.progress
18837.000000 2026-08-03T17:57:59.890097  0.99672  0.189201 NaN

# cmp_prtoe_routeD.progress
1609.000000 2026-08-03T20:53:57.575011  1.0  102.794555 NaN
```

### Checkpoint (`Rminus1_last` | `converged` | `mpi_size`)

```
chains/cmp_lcdm_mnu_bbnfix.checkpoint: converged: false; Rminus1_last: 0.05905511181721022; mpi_size: 3
chains/dyad_mnu_bbnfix.checkpoint:     converged: false; Rminus1_last: 0.18920075919140164; mpi_size: 3
chains/cmp_prtoe_routeD.checkpoint:    converged: false; Rminus1_last: 102.79455471855752; mpi_size: 3
```

### Live processes (watch only — not touched)

| object | MPI / ranks | note |
|--------|-------------|------|
| `dyad_mnu_bbnfix` | mpirun PID ~3768; ranks ~3776–3778 | live ~23 h; writing `*.txt` |
| `cmp_lcdm_mnu_bbnfix` | mpirun PID ~3769; ranks ~3779,3781,3782 | live ~23 h; writing `*.txt` |
| `cmp_prtoe_routeD` | mpirun PID ~175453; ranks ~175457–175459 | live ~13.5 h; writing `*.txt` |
| false-positive watcher | **PID 212363** (bash loop) | still alive ~12 h — see defects |

Approx post-header sample rows at stamp (not GR N):

| chain | rank1 | rank2 | rank3 |
|-------|------:|------:|------:|
| lcdm bbnfix | 6615 | 6622 | 6471 |
| dyad bbnfix | 6670 | 6614 | 6710 |
| routeD | 689 | 772 | 738 |

RouteD launchlog raw accept ~5–6% (e.g. ~689/12397, ~772/13658) — healthy high-d Metropolis; progress accept 1.0 is oversampled.

---

## Finalize script (this stamp)

```bash
python3 scripts/finalize_h0_at_convergence.py
```

Stdout (verbatim shape):

```
==========================================================================
H₀ finalization gate (letter item 1)
==========================================================================
   cmp_lcdm_mnu_bbnfix: R−1 = 0.059  (converging)  [not-stopped]
   dyad_mnu_bbnfix: R−1 = 0.189  (converging)  [not-stopped]

   NOT YET — need R−1 < 0.05 on both chains AND sampler self-stop
   (converged: true). Both required (Claude R-D cure).
   Nothing extracted; the letter's provisional caveat stands.
==========================================================================
```

**Correct refuse.** Gate encodes both legs.

---

## Notes (watch only)

1. **lcdm** still above bar after the 14:21 under-bar print (0.048827) then bounce to **0.059**. Transient sub-bar is **not** booking authority.
2. **dyad** remains the lagging pair member (R−1≈0.19).
3. Progress/checkpoint mtimes lag live `*.{1,2,3}.txt` growth; R−1 above is **last Cobaya-reported** GR, not a recompute from current sample count.
4. **RouteD** still burn-in noise (R−1 ~ 10²); leave alone — do not reseed/book.
5. **Verdict:** **NOT bookable.**

---

## Watcher / gate defects (this pass)

See also `LAPLACE_PREP.md` and section below. Summary:

| defect | path / PID | status |
|--------|------------|--------|
| Live bash watcher fires `GATE CROSSED - A2 FIRES` on **single-chain** `r <= 0.05` (≤ not <; no pair; no self-stop) | **PID 212363** (inline Claude shell; no repo script file) | **OPEN — not killed** (watch-only; owner may retire) |
| `book_bbnfix_when_ready.py` gated R−1 only | `scripts/book_bbnfix_when_ready.py` | **FIXED** this pass — now requires `converged: true` both |
| `make_getdist_tables.py --include-bbnfix` gated R−1 only | `scripts/make_getdist_tables.py` | **FIXED** this pass — self-stop required unless `--force-bbnfix` |
| Checklist title used ≤ vs body < | `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` | **FIXED** title → strict `<` + self-stop |
| Preflight kill list lacked self-stop | `.../BBNFIX_BOOKING_PREFLIGHT.md` | **FIXED** kill row added |

`finalize_h0_at_convergence.py` already required both legs (post R-D cure) — no change needed this pass.
