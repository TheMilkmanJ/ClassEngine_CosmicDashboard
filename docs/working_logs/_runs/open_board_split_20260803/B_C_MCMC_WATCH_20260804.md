# B–C MCMC watch stamp — 2026-08-04 — bbnfix + routeD

**Stamp time (local):** 2026-08-04T00:06:26-0600  
**Stamp time (UTC):** 2026-08-04T06:06:26Z  
**Agent:** Grok blue — **watch only** (no kill / reseed / book MCMC; no PolyChord)  
**Source of R−1:** last line of `*.progress` field 4 + `Rminus1_last` / `converged` in `*.checkpoint`  
**Prior stamps:** `B_C_MCMC_WATCH.md` (23:33 local) · `B_C_MCMC_WATCH_REFRESH.md` (23:56 local)  
**Finalize gate:** `python3 scripts/finalize_h0_at_convergence.py` → **NOT YET** (refuse)  
**Booking gate:** `python3 scripts/book_bbnfix_when_ready.py` → **REFUSED** (exit 2)

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

### Delta vs prior refresh (2026-08-03 ~23:56 local)

| field | change |
|-------|--------|
| progress last rows | **unchanged** (no new Cobaya GR row since 21:05 lcdm / 17:57 dyad / 20:53 routeD) |
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

### Checkpoint grep (`Rminus1_last` | `converged`)

```
chains/cmp_lcdm_mnu_bbnfix.checkpoint:    converged: false
chains/cmp_lcdm_mnu_bbnfix.checkpoint:    Rminus1_last: 0.05905511181721022
chains/dyad_mnu_bbnfix.checkpoint:    converged: false
chains/dyad_mnu_bbnfix.checkpoint:    Rminus1_last: 0.18920075919140164
chains/cmp_prtoe_routeD.checkpoint:    converged: false
chains/cmp_prtoe_routeD.checkpoint:    Rminus1_last: 102.79455471855752
```

(All `chains/*.checkpoint` with a `converged:` line currently read **false**.)

### Live processes (watch only — not touched)

| object | MPI / ranks | note |
|--------|-------------|------|
| `dyad_mnu_bbnfix` | mpirun PID ~3768; ranks ~3776–3778 | live ~23 h; writing `*.txt` |
| `cmp_lcdm_mnu_bbnfix` | mpirun PID ~3769; ranks ~3779,3781,3782 | live ~23 h; writing `*.txt` |
| `cmp_prtoe_routeD` | mpirun PID ~175453; ranks ~175457–175459 | live ~13.5 h; writing `*.txt` |
| false-positive watcher | **PID 212363** (bash loop) | still alive ~12 h — single-chain ≤0.05 fire defect |

Approx post-header sample rows at stamp (not GR N):

| chain | rank1 | rank2 | rank3 |
|-------|------:|------:|------:|
| lcdm bbnfix | 6626 | 6638 | 6487 |
| dyad bbnfix | 6683 | 6621 | 6720 |
| routeD | 696 | 778 | 750 |

---

## Finalize + book scripts (this stamp)

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

**Correct refuse.**

```bash
python3 scripts/book_bbnfix_when_ready.py
```

Stdout (key lines):

```
  dyad_mnu_bbnfix: R−1 = 0.189201 >= 0.05 ... — NOT READY
  dyad_mnu_bbnfix: checkpoint converged: false — NOT READY (self-stop required)
  cmp_lcdm_mnu_bbnfix: R−1 = 0.059055 >= 0.05 ... — NOT READY
  cmp_lcdm_mnu_bbnfix: checkpoint converged: false — NOT READY (self-stop required)

  REFUSED — booking blocked.
```

Refuse card: `docs/working_logs/_runs/bbnfix_booking_20260804_060626/REPORT.md`  
**Correct refuse.** No GetDist booking; living docs unchanged. Exit code 2.

---

## Notes (watch only)

1. **lcdm** still above bar after the 14:21 under-bar print (0.048827) then bounce to **0.059**. Transient sub-bar is **not** booking authority.
2. **dyad** remains the lagging pair member (R−1≈0.19).
3. Progress/checkpoint mtimes lag live `*.{1,2,3}.txt` growth; R−1 above is **last Cobaya-reported** GR, not a recompute from current sample count.
4. **RouteD** still burn-in noise (R−1 ~ 10²); leave alone — do not reseed/book.
5. **Verdict: NOT bookable.** Do not GetDist-book, do not extract letter H₀, do not claim hard-win #1 until **both** bbnfix chains have R−1 < 0.05 **and** `converged: true` (self-stop).

*NO FABRICATIONS · no PolyChord · no premature book.*
