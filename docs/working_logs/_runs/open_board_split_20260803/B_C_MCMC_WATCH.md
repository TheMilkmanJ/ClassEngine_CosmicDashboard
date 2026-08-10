# B–C MCMC watch stamp — bbnfix + routeD

**Stamp time (local):** 2026-08-03T23:33:22-0600  
**Stamp time (UTC):** 2026-08-04T05:33:22Z  
**Agent:** Grok blue — **watch only** (no kill / reseed / book)  
**Source of R−1:** last line of `*.progress` + `Rminus1_last` / `converged` in `*.checkpoint`  
**Finalize gate:** `python3 scripts/finalize_h0_at_convergence.py` → **NOT YET**

---

## Explicit non-action

| Action | Status |
|--------|--------|
| Book H₀ / Σm_ν / Ω_b h² / S8 posteriors | **DO NOT BOOK** |
| Kill / reseed / restart any chain | **DO NOT** |
| Treat lcdm dip under bar as pair-ready | **NO** — both must clear **and** self-stop |
| Treat routeD as bookable thaw | **NO** |

**Booking bar (hard-win #1):** R−1 **< 0.05** on **both** `cmp_lcdm_mnu_bbnfix` and `dyad_mnu_bbnfix`, with Cobaya self-stop (`converged: true`).  
Until **BOTH** are under the bar **and** self-stopped → **NOT bookable**, even if one chain briefly or currently sits under 0.05.

---

## Table (progress tails + checkpoints)

| chain | N (progress) | progress timestamp | acceptance | **R−1** | checkpoint `Rminus1_last` | `converged` | vs bar 0.05 |
|-------|-------------:|--------------------|-----------:|--------:|--------------------------:|:-----------:|:-----------:|
| `cmp_lcdm_mnu_bbnfix` | 19013 | 2026-08-03T21:05:36.968557 | 0.983857 | **0.059055** | 0.05905511181721022 | **false** | **above** (was 0.048827 @ N=17458, then bounced) |
| `dyad_mnu_bbnfix` | 18837 | 2026-08-03T17:57:59.890097 | 0.99672 | **0.189201** | 0.18920075919140164 | **false** | **above** (far) |
| `cmp_prtoe_routeD` | 1609 | 2026-08-03T20:53:57.575011 | 1.0 | **102.794555** | 102.79455471855752 | **false** | N/A (early burn-in; not bbnfix pair) |

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

---

## Finalize script

```
python3 scripts/finalize_h0_at_convergence.py
```

Output (expected):

```
cmp_lcdm_mnu_bbnfix: R−1 = 0.059  (converging)
dyad_mnu_bbnfix: R−1 = 0.189  (converging)

NOT YET — the grading bar is R−1 < 0.05 on both chains.
Nothing extracted; the letter's provisional caveat stands.
```

---

## Notes (watch only)

1. **lcdm** crossed under 0.05 once (N=17458, R−1=0.048827) then returned to **0.059** at N=19013. That transient is **not** booking authority.
2. **dyad** still the lagging gate member (R−1≈0.19).
3. Progress/checkpoint mtimes lag live `*.[123].txt` growth (chains still writing as of stamp); R−1 numbers above are **last Cobaya-reported** Gelman–Rubin, not a recompute from full current sample count.
4. **RouteD** first GR row post-reseed (2026-08-03 ~08:58) is still burn-in noise (R−1 ~ 10²); leave alone — do not reseed/book.
5. **Verdict:** **NOT bookable.** Do not GetDist-book, do not extract letter H₀, do not claim hard-win #1 until **both** bbnfix chains have R−1 < 0.05 **and** `converged: true` (self-stop).

