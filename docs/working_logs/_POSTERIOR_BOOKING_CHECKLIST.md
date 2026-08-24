# Posterior booking checklist — Stage A done; nested gold in flight

> ## Currency — 2026-08-15
>
> **Stage A MCMC is BOOKED** for old-BAO SH0ES `bbnfix`, DESI-DR2 SH0ES, and DESI-DR2 TRGB
> (see [`../PRTOE_CHAIN_TABLES.md`](../PRTOE_CHAIN_TABLES.md)). This file is no longer “wait for
> first R−1 gate” for those twins — it is the **publish / nested / Laplace honesty** runbook.
>
> **Nested evidence (gold logZ):** Nested UN+PC **all anchors RUNNING** (SH0ES, TRGB, no-H0).
> **Mid-run nested logZ is FORBIDDEN** until final `ultranest_summary.json` / PC `.stats`.
> zon retune **STOPPED** GetDist **INCONCLUSIVE**. conv_desi retune **STOPPED** GetDist **INCONCLUSIVE** (`g`).
> Runbook: [`_runs/dual_nested_runbook_20260812/RUNBOOK.md`](_runs/dual_nested_runbook_20260812/RUNBOOK.md).
>
> **Hard fences:** NO FABRICATIONS · do not book unconverged posteriors · leave **live nested**
> alone · booking ≠ publishing (tables need `RED_AUDIT`) · never quote pre-bbnfix ΔlnZ ≈ +2.6
> as final bbnfix evidence · **do not** treat Laplace interim as nested gold · within-anchor ΔlnZ
> only (never mix SH0ES vs TRGB vs no-H0 Z).
>
> Historical 2026-08-04 gate-smoke numbers below are **receipts**, not live R−1.

**Do not run multi-hour re-analyses “to check” live nested.** For Stage A re-book only if a new
chain supersedes a booked twin.

Packages (ops):
- [`_runs/dual_nested_runbook_20260812/`](_runs/dual_nested_runbook_20260812/) — dual UN+PC  
- [`_runs/noh0_nested_un_20260813/`](_runs/noh0_nested_un_20260813/) — no-local-H0 UN  
- [`_runs/trgb_pc_1.22.2_ready_20260810/`](_runs/trgb_pc_1.22.2_ready_20260810/) — TRGB nested prep (now **RUNNING** with all anchors; receipt)  

- `docs/working_logs/_runs/laplace_booking_full_20260804/` — Laplace RUNBOOK (interim only)  
- `docs/working_logs/_runs/laplace_prep_harden_20260804/` — Stage A/B harden  

---

## Publish split — Stage A vs Stage B

| stage | meaning | command | forward shelf? |
|-------|---------|---------|:--------------:|
| **Stage A** (default) | book + finalize H₀ (stdout) + optional Δχ² proxy | `bash scripts/bbnfix_when_ready_all.sh` | **NO** |
| **Red** | audit booking package | `bbnfix_booking_<id>/RED_AUDIT.md` with `red: AGREE` or `red: AGREE-IF` | no |
| **Stage B** | write GetDist tables to living docs | `bash scripts/bbnfix_when_ready_all.sh --write-tables` | **YES** (needs red stamp) |

`WRITE_TABLES` defaults to **0**. Without red stamp, `--write-tables` refuses.
Owner emergency only: `--force-tables`. Force GetDist (`--force-bbnfix`) is
**UNBOOKABLE-only** → `getdist_force_UNBOOKABLE_*`, never `PRTOE_CHAIN_TABLES.md`.

---

## Gate definition

| object | chain roots | stop | both required? |
|---|---|---:|---|
| letter H₀ + pair tables | `dyad_mnu_bbnfix`, `cmp_lcdm_mnu_bbnfix` | **R−1 < 0.05** each | **yes** — letter / Δχ² / Laplace pair |
| RouteD thaw | `cmp_prtoe_routeD` | **R−1 < 0.1** | separate; optional CL gate `Rminus1_cl_stop = 0.2` |

Authoritative R−1 source (not launchlog, not oversampled progress accept):

```bash
# from repo root
tail -1 chains/dyad_mnu_bbnfix.progress
# columns: N  timestamp  acceptance_rate  Rminus1  Rminus1_cl
# use field 4 (Rminus1). Field 3 is oversampled accept — ignore for the gate.

tail -1 chains/cmp_lcdm_mnu_bbnfix.progress
grep -E 'Rminus1_last|converged' chains/dyad_mnu_bbnfix.checkpoint \
  chains/cmp_lcdm_mnu_bbnfix.checkpoint
```

Optional one-shot refuse/grade:

```bash
python3 scripts/book_bbnfix_when_ready.py   # preferred gate authority; exit 2 if refuse
python3 scripts/finalize_h0_at_convergence.py
# Unconverged: prints both R−1 and "NOT YET", exits 2.
# Graded: prints model/control H₀ ± σ and the letter replacement sentence (stdout only).
```

**Raw accept (diagnostic only, not the gate):** sum `accepted/steps` from the last
`[rank : mcmc] Progress @ …` lines in each `chains/<root>.launchlog`. Progress
`acceptance_rate` near 0.99 is oversampled (`oversample_power = 0.4`).

---

## Prerequisites (all must be true before booking)

**Claude open-board-split R-D cure (2026-08-03): both required — no soft language.**

1. **Both** `dyad_mnu_bbnfix` and `cmp_lcdm_mnu_bbnfix` have last-row R−1 **< 0.05**
   (strict `<`, not `≤`).
2. **Sampler self-terminated** on **both** chains: `converged: true` in `.checkpoint`
   (or cobaya idle after writing a final progress row under the bar).  
   **Both R−1 < 0.05 AND self-stop — both required.** No “prefer” / “preferably.”
3. All three rank files exist per root: `chains/<root>.{1,2,3}.txt` (MPI size 3).
4. Chains are **idle or finished** for the write pass. **Do not** run GetDist on a
   still-writing chain (moving-file escape hatch **killed** by red).
5. Working directory = repo root (`/home/themilkmanj/prtoe_class`).
6. Env has `getdist`, `numpy`, and the same classy/cobaya stack used for the runs
   (no classy rebuild between last samples and booking if you plan a Laplace
   re-eval that re-calls CLASS).
7. **Do not** promote any number that was peeks while R−1 ≥ stop.

---

## Stage A — book + H₀ letter (seconds–minutes; no forward shelf)

Preferred one-shot (tables **OFF** by default):

```bash
cd /home/themilkmanj/prtoe_class
bash scripts/bbnfix_when_ready_all.sh
```

### A.1 — GetDist booking entrypoint (production authority)

```bash
python3 scripts/book_bbnfix_when_ready.py
```

| | |
|---|---|
| **Hard gate** | both R−1 < 0.05 **and** both `converged: true` |
| **Reads** | three ranks via GetDist `loadMCSamples`, ignore_rows=0.3 |
| **Writes** | private `_runs/bbnfix_booking_<stamp>/REPORT.md` + `booking.json` only |
| **Refuse** | exit **2**; refuse card always written |

### A.2 — H₀ letter gate (stdout only)

```bash
python3 scripts/finalize_h0_at_convergence.py
```

| | |
|---|---|
| **Script** | `scripts/finalize_h0_at_convergence.py` |
| **Hard gate** | both of `PAIR = ("cmp_lcdm_mnu_bbnfix", "dyad_mnu_bbnfix")` with R−1 < `RBAR = 0.05` **and** self-stop |
| **Reads** | progress R−1; rank-1 H₀ (**50% burn**) when graded |
| **Writes** | **nothing** — stdout only (manual-edits rule) |
| **Manual follow-up** | paste printed H₀ sentence into Fairbank letter Status **after** red if publishing; close HOLD item 1 with date + both R−1 |

**Limitation:** rank `.1.txt` only. Prefer three-rank book card for public σ.

---

## Stage B — GetDist tables + triangles (publish; needs RED_AUDIT)

Instrument: `scripts/make_getdist_tables.py` (ForJustin/12 item 5(b)).

BBN-fixed roots are already in `BBNFIX_ROOTS` and gated behind `--include-bbnfix`
(both R−1 < 0.05 **and** self-stop). Do **not** hand-edit `ROOTS` for a peek.

Preferred publish path (Stage B after red):

```bash
# After Claude writes bbnfix_booking_<id>/RED_AUDIT.md with: red: AGREE
bash scripts/bbnfix_when_ready_all.sh --write-tables
```

Direct instrument (still gate-hard; prefer shell Stage B for red stamp):

```bash
python3 scripts/make_getdist_tables.py --include-bbnfix
# gate closed → exit 2, no write
# --force-bbnfix → UNBOOKABLE working_logs only; living shelf untouched
```

| | |
|---|---|
| **Reads** | `chains/<root>.1.txt` (30% burn); first ≤8 non-nuisance params |
| **Writes (gate open)** | triangles + **overwrites** `docs/PRTOE_CHAIN_TABLES.md` body |
| **Writes (force, gate incomplete)** | `docs/working_logs/_runs/getdist_force_UNBOOKABLE_<stamp>/` only |
| **Preserve** | restore live-status banner on `PRTOE_CHAIN_TABLES.md` if clobbered |
| **Publish rule** | means / 68% enter forward docs only after Stage B + red |

Sync living docs only after Stage B + intentional publish:

- `docs/working_logs/_chain_snapshot.md` — mark pair **booked**, record final R−1 / N
- `docs/PRTOE_REFEREE_CALENDAR.md` Sitting NOW
- `docs/PRTOE_CODE_MANIFEST.md` §1 live rows
- `docs/working_logs/T11_hubble_owed.md` machine half
- `docs/working_logs/T3_*` if Σm_ν row is released from the same chain

---

## Step C — Laplace ΔlnZ (model − ΛCDM) under the BBN-fixed stack

Standing **interim** evidence method while nested runs: **Laplace-from-MCMC** (docket #155).
**Gold nested** is dual UltraNest + PolyChord GIL on AWS (see dual nested runbook) — **not**
“deferred forever.” Laplace remains interim until nested finishes. Paths in this repo:

| path | role |
|---|---|
| `run_cosmicforge.py` (~L2083–2095) | CosmicForge mode fit: Hessian → `log_z_laplace = -0.5 χ² + 0.5 n log(4π) - 0.5 logdet` |
| `forge/evidence.py` | bridge sampling (Meng–Wong) from posterior samples + fresh `log_post_fn` evals — heavier; only if Laplace is not enough |
| pre-bbnfix standing claim | ΔlnZ ≈ **+2.6** (SH0ES-conditional, **not** the BBN-fixed stack) — do not silently replace |

### Practical booking procedure for the bbnfix pair

When both chains are under the bar:

1. **Best-fit χ² proxy from MCMC** (fast, no re-CLASS if you only need Δχ² at
   sampled best points):

   ```bash
   # Gate-hard wrapper (refuses unless both R−1 < 0.05 AND self-stop):
   python3 scripts/bbnfix_delta_chi2_proxy.py
   # Optional peek while over bar (marks UNBOOKABLE): --force-peek
   ```

   Report **Δ(min −logpost)** only with the caveat that this is not a full
   Laplace evidence (missing Hessian volume terms and prior measure). Prefer
   CosmicForge / explicit Hessian for a bookable ΔlnZ.

2. **CosmicForge Laplace** (uses Hessian at a mode; can re-call CLASS — can be
   long if misconfigured). Only launch if you have capacity **after** the pair
   has stopped or you are sure you will not starve live ranks:

   ```bash
   # Example shape only — use the production yaml pair as the mode definitions
   # the project actually used for CosmicForge comparisons. Confirm flags in
   # run_cosmicforge.py --help / README before a real booking run.
   python3 run_cosmicforge.py --help | head
   ```

   Book the printed `log_z_laplace` for model and twin; ΔlnZ = lnZ_model − lnZ_ΛCDM.
   Label method **Laplace (Hessian)** and the exact data stack (BBN-fixed pair).

3. **Bridge sampling** (`forge/evidence.py`) only if Laplace is disputed or the
   posterior is clearly non-Gaussian — costs N2 fresh likelihoods; not the
   default booking path.

**Do not** re-open PolyChord on this hardware for the booking session.

---

## What files get updated when the gate opens

| file | update |
|---|---|
| stdout of `finalize_h0_at_convergence.py` | H₀ sentence (manual paste into letter) |
| Fairbank letter / Status (manual) | replace provisional H₀; close HOLD #1 |
| `docs/PRTOE_CHAIN_TABLES.md` | bookable GetDist means + 68% for dyad + lcdm; demote archive-only disclaimer for those rows |
| `docs/plots/dyad_mnu_bbnfix_triangle.png` | new |
| `docs/plots/cmp_lcdm_mnu_bbnfix_triangle.png` | new |
| `docs/working_logs/_chain_snapshot.md` | R−1 final, **booked** flag |
| `docs/working_logs/T11_hubble_owed.md` | machine half: H₀ + ΔlnZ status |
| `docs/PRTOE_REFEREE_CALENDAR.md` / `PRTOE_CODE_MANIFEST.md` | live → graded |
| optional evidence note / hubble_tension fairness table | only after Laplace/Δχ² exists under **this** stack |

Nothing auto-commits. Nothing kills chains.

---

## RouteD (separate, stop 0.1) — when **its** R−1 grades

Same GetDist path after adding `cmp_prtoe_routeD` to `ROOTS`. Key parameter:
`dcdf_floor_thaw` (≡ 1+w_fl,0). **Do not** treat a non-zero mean as evidence
against w = −1 until R−1 < 0.1 and ranks share a basin (see
`scripts/rank_basin_diagnostic.py` pattern; extend `BASES` or run an equivalent
three-rank mean check).

---

## Explicit kill criteria

| # | kill if… |
|---|----------|
| K1 | Book while either R−1 ≥ 0.05 |
| K2 | Book before both `converged: true` (self-stop) |
| K3 | Quote peeks / `--force-bbnfix` / `--force-peek` as bookable results |
| K4 | Living `PRTOE_CHAIN_TABLES.md` written from force path (must be UNBOOKABLE only) |
| K5 | Stage B tables without `RED_AUDIT` (`red: AGREE` / `AGREE-IF`) except owner `--force-tables` |
| K6 | PolyChord / nested sampling for this booking session |
| K7 | Kill live MCMCs without owner order |
| K8 | Promote pre-bbnfix ΔlnZ ≈ +2.6 as final bbnfix evidence without fence |
| K9 | RouteD substitute for the letter H₀ pair |
| K10 | Invent a Laplace number or invent `scripts/laplace_bbnfix.py` |

## Explicit non-actions

- Do **not** kill `dyad_mnu_bbnfix`, `cmp_lcdm_mnu_bbnfix`, or `cmp_prtoe_routeD` for booking prep.
- Do **not** quote 68% limits while R−1 > stop (they understate width).
- Do **not** use progress `acceptance_rate` as R−1 or as raw Metropolis accept.
- Do **not** overwrite `PRTOE_CHAIN_TABLES.md` live-status banner without restoring it.
- Do **not** replace the standing pre-bbnfix ΔlnZ ≈ +2.6 with an unconverged peek **or** treat it as the BBN-fixed-pair result.
- Do **not** run long GetDist force “for results.”
- Do **not** treat Stage A book as authorization to publish tables (needs Stage B + red).

---

## Quick pre-flight (safe anytime, ≪2 min)

```bash
cd /home/themilkmanj/prtoe_class
python3 scripts/book_bbnfix_when_ready.py          # expect REFUSED / exit 2 until gate
python3 scripts/finalize_h0_at_convergence.py       # expect NOT YET / exit 2 until gate
tail -1 chains/dyad_mnu_bbnfix.progress chains/cmp_lcdm_mnu_bbnfix.progress \
  chains/cmp_prtoe_routeD.progress
```
