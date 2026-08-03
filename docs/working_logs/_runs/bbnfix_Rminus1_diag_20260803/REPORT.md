# bbnfix R−1 diagnostic — 2026-08-03 ~10:30 MDT

**Scope:** diagnose why `cmp_lcdm_mnu_bbnfix` sits at R−1 ≈ 0.054 (stop 0.05) and `dyad_mnu_bbnfix` at ≈ 0.16. No GetDist booking. Rank means via weighted numpy only.

**Sources:** `chains/{cmp_lcdm_mnu_bbnfix,dyad_mnu_bbnfix}.{progress,checkpoint,1..3.txt,input.yaml}`; live `mpirun -n 3` both alive.

---

## Snapshot (read time 2026-08-03 10:28 MDT)

| chain | ranks | samples/rank (lines−1) | progress N | R−1 last | stop | checkpoint | state |
|---|---:|---:|---:|---:|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | 3 | 5571 / 5628 / 5498 | **16075** @ 07:49 | **0.05387** | 0.05 | `converged: false` | LIVE, writing |
| `dyad_mnu_bbnfix` | 3 | 5834 / 5805 / 5878 | **17384** @ 09:32 | **0.15989** | 0.05 | `converged: false` | LIVE, writing |

Progress columns: `N, timestamp, acceptance_rate, Rminus1, Rminus1_cl`. Progress `acceptance_rate` ≈ 0.98–0.996 is **oversampled** (not raw MH accept). `Rminus1_cl` still **NaN** on every row for both chains.

Both have `Rminus1_stop: 0.05`, `Rminus1_cl_stop: 0.2`, `max_samples: 40000`, `learn_proposal: true` with open gates (`learn_proposal_Rminus1_max: 100`).

---

## Time to next progress row

Checkpoints land every **~1400–1500** progress-N (cobaya MPI Gelman–Rubin interval).

### LCDM (`cmp_lcdm_mnu_bbnfix`)
- Last row: N=16075 @ **07:49**, R−1=0.05387
- Last 3 intervals: dN = 1494 / 1482 / 1400 (mean **1459**); dt = 16.5 h / 7.8 h / **5.0 h**
- File growth since last progress: sum(rank N) − 16075 ≈ **+620** at ~10:28 (~2.65 h wall)
- Instant rate ≈ 230–240 progress-N/h → **ETA next row ~3–4 h from 10:28 ≈ 13:30–14:30 MDT**
- Conservative (mean last-3 wall ~9.8 h): could land as late as **~17:30 MDT** if CLASS slows

### Dyad (`dyad_mnu_bbnfix`)
- Last row: N=17384 @ **09:32**, R−1=0.15989
- Last 3 intervals: dN = 1472 / 1425 / 1415 (mean **1437**); dt = 18.1 / 10.9 / **7.0 h**
- Growth since last progress: sum − 17384 ≈ **+130** at ~10:28 (~1 h wall)
- Instant rate lower/noisier → **ETA next row ~6–10 h from 10:28 ≈ 16:30–20:30 MDT**
- Mean last-3 wall ~12 h → upper bracket **~21:30 MDT**

---

## LCDM: about to book, not plateau

### R−1 trajectory (progress)
```
N      R−1
 7400  0.136
 8851  0.181   ← bump
10306  0.176
11699  0.287   ← bump
13193  0.141
14675  0.094
16075  0.054   ← current (1.08× stop)
```

Last three contractions: **0.490 → 0.665 → 0.575** (geom mean **×0.57** per ~1.4k samples).

**If that rate holds, next progress R−1 ≈ 0.031 < 0.05** → mean R−1 should clear the stop on the **next** progress row (today afternoon).

### Why it is not a plateau
1. **Still contracting hard** on the last three checkpoints; 0.054 is a fresh print (07:49 today), not a multi-day hang at the gate.
2. **Per-parameter R−1** (burn 30%, equal-weight rank means; approximate, not cobaya’s joint statistic) all **≪ 0.05**:

| param | approx R−1 | rank means |
|---|---:|---|
| H0 | 0.005 | 68.38 / 68.33 / 68.35 |
| m_ncdm | 0.008 | 0.0191 / 0.0167 / 0.0194 |
| omega_b | 0.003 | 0.02249 / 0.02249 / 0.02250 |
| omega_cdm | 0.014 | 0.1186 / 0.1187 / 0.1187 |
| n_s | 0.007 | 0.9714 / 0.9711 / 0.9709 |
| logA | 0.003 | 3.051 / 3.049 / 3.051 |
| S8 | 0.009 | 0.8224 / 0.8240 / 0.8232 |
| A_planck | **0.035** | 1.0017 / 1.0010 / 1.0014 |
| z_reio | 0.001 | 7.97 / 7.97 / 8.01 |

Joint multivariate R−1 (what cobaya reports) can sit slightly above the worst single-param R−1; residual is consistent with **A_planck + small ω_cdm / S8 scatter**, not disjoint basins.

3. **H0 rank spread last-30%:** max−min ≈ 0.12 km/s/Mpc (well inside within-rank σ ≈ 0.37).

### Caveats before declaring “booked”
- Stop is **R−1 < 0.05 and R−1_cl < 0.2**. CL column is still NaN — first time mean R−1 crosses, cobaya may still refuse if interval R−1 is high. One more row after mean-crossing is normal.
- Gelman–Rubin can **bounce** (history has 0.136→0.181 and 0.176→0.287). A single overshoot back above 0.05 is possible; not a reseed signal.
- Do **not** GetDist-book until checkpoint says `converged: true` (or at least R−1 ≤ 0.05 on a fresh progress row with CL checked).

**Verdict LCDM: ABOUT TO BOOK** (next 1 progress row under optimistic contraction; 1–3 rows if a bounce). **Leave alone. No reseed.**

---

## Dyad trajectory: slow mix in a 0.16–0.32 band, not collapsed

### R−1 trajectory (progress)
```
N      R−1
 7211  0.185
 8662  0.175
10107  0.198
11617  0.321   ← peak of late band
13072  0.259
14544  0.192
15969  0.191   ← flat step
17384  0.160   ← current (~3.2× stop)
```

Since N≈7200 (~4 calendar days) the chain has **oscillated in ~0.16–0.32**, with a slow downward envelope. Last step 0.191→0.160 (×0.84) is improvement, not freeze.

### Rank means (last 30% weighted)
| param | r1 / r2 / r3 | max−min | notes |
|---|---|---:|---|
| H0 | 69.98 / 70.00 / 70.22 | 0.24 | mild rank3 high |
| m_ncdm | 0.077 / 0.056 / 0.092 | 0.036 | heavy-tailed; last-20% spread larger |
| omega_b | 0.02277 / 0.02275 / 0.02281 | 6e-5 | small absolute, still a joint driver |
| varying_me | 1.0130 / 1.0127 / 1.0147 | 0.0020 | mild |
| dcdf_rho_inf | 0.7029 / 0.7033 / 0.7041 | 0.0012 | OK |
| Omega0_dcdf | 0.9535 / 0.9536 / 0.9537 | 2e-4 | OK |
| S8 | 0.822 / 0.826 / 0.818 | 0.008 | moderate |

Approx per-param R−1 (burn 30%): **omega_b 0.044, H0 0.034, n_s 0.031, varying_me 0.026, Omega0_dcdf 0.024** — joint 0.16 is the multivariate stack of several O(0.03) disagreements, **not** a single stuck rank / disjoint H0 basin (contrast early routeD-style failure).

### Extrapolation to stop 0.05
| model | estimate |
|---|---|
| geom ×0.84 / row (last 4) | **~7 progress rows** (~2–4 days at 7–12 h/row) |
| conservative ×0.90 / row | ~12 rows (~4–7 days) |
| ×0.95 / row (near-plateau) | ~23 rows (long) |
| linear `R ≈ a/N + b` on N≳5800 | floor **b ≈ 0.09** → **would never hit 0.05** if floor is real |

Honest bracket: **days, not hours**. The 1/N+floor fit is a warning that pure waiting *might* asymptote above 0.05 if between-rank structure freezes — but the last row still moved (0.191→0.160) and ranks overlap on primary physics params, so the floor is **not confirmed**.

**Verdict dyad: SLOW TRAJECTORY / soft quasi-plateau risk, still improving. Leave alone / extend. No reseed now.**

---

## Recommendation

| chain | action | why |
|---|---|---|
| **LCDM** | **LEAVE ALONE** | Contracting into the gate; next progress row likely R−1 ≲ 0.05. Reseed would throw away a near-converged 16k-sample twin. |
| **Dyad** | **LEAVE ALONE / EXTEND** | Alive, mixing, R−1 down-trending inside a 0.16–0.32 band; rank means overlapped. Reseed not justified while still moving. Revisit only if **≥3 consecutive** progress rows stay ≥0.15 with **rising** rank-mean spread on H0 / m_ncdm / varying_me. |
| **Reseed either?** | **NO** | Both live (3+3 ranks, CPU ~109% each worker). LCDM is hours from the bar; dyad is days. |

### Watch list (no action required tonight)
1. LCDM next progress (~13:30–17:30 MDT): expect R−1 print; check `Rminus1_cl` becomes numeric and `< 0.2`; check `checkpoint.converged`.
2. When LCDM converges, do **not** kill dyad for cores — dyad is the model leg of the matched pair.
3. Booking only after both under bar: follow `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` / hard_win1 prep script. Do not book LCDM alone as the dyad–ΛCDM comparison.

### Not done (by design)
- No GetDist load / no posterior means booked
- No process kill / no covmat reseed / no yaml edit

---

## 12-line summary

1. LCDM R−1 = **0.0539** @ N=16075 (07:49); dyad R−1 = **0.160** @ N=17384 (09:32); both **live**, stop 0.05.
2. Next LCDM progress ETA **~3–6 h** (≈13:30–17:00 MDT); dyad **~6–12 h** (evening).
3. LCDM last 3 steps contracted ×0.49/0.67/0.58 → **about to book**, not plateau.
4. Projected next LCDM R−1 ≈ **0.03** if contraction holds; possible one Gelman–Rubin bounce.
5. LCDM rank means overlap tightly (H0 Δ≈0.12); worst single-param R−1 ≈ A_planck **0.035**.
6. Dyad has sat in a **0.16–0.32** band since N≈7k but last step improved 0.191→0.160.
7. Dyad ranks not disjoint; joint R−1 driven by stack of mild H0 / ω_b / n_s / me offsets.
8. Dyad to 0.05: **~7–12 progress rows (days)** under recent ratios; 1/N fit warns of possible ~0.09 floor (unconfirmed).
9. `Rminus1_cl` still NaN both chains — mean R−1 alone may not flip `converged: true`.
10. **Recommendation: leave both alone; no reseed.**
11. Do not GetDist-book until checkpoint `converged: true` (and prefer both legs under bar for the matched claim).
12. Revisit dyad surgery only if R−1 stalls ≥0.15 for ≥3 rows **and** rank-mean spreads grow.
