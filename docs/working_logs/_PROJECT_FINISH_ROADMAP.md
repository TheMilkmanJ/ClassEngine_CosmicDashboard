# Project finish roadmap (2026-08-02; packaging refresh 2026-08-03)

Honest path from “desk clean” to “science closed.” Desk OPEN is at zero; the rest is
machine, theory, external, or packaging.

## Already done (recent)

- Six arXiv TeX packages on desk (supertrace, neutrino-mbb, radio-lattice, lattice-tc-gap, bbn-eps-bound, kination-tracking-note); readiness + candidacy notes current; package audit script
- **2026-08-03 re-audit:** PAPER_CANDIDATE from docs still 0; neutrino-mbb submitted to Fairbank (packaging paused); arXivReady expanded toward all six packages
- Tracker hygiene + file completion inventory (64 PRTOE files classified)
- Strong CP complete as abstention
- Check 12 batches 1–3 (stale “owed” / “running chain” residues)
- Check 12 residual pass (2026-08-02): dead-premise greps clean except one calendar
  historical present-tense block; S₈ live-trio date stamps refreshed
- Live chain status tables refreshed (bbnfix pair + routeD)
- Baryogenesis ω_J quartet-closure re-landed as back-target; Page-curve status lock;
  magnetism void shortfall priced

## LIVE machines (do not kill casually)

Re-read 2026-08-02 ~22:20 — R−1 **unchanged** at last progress rows; launchlogs still advancing.

| chain | R−1 (last) | stop | raw accept | note |
|---|---:|---:|---:|---|
| dyad_mnu_bbnfix | **0.192** | 0.05 | ~6.4% | N=14544; ~3.8× stop; leave alone |
| cmp_lcdm_mnu_bbnfix | **0.141** | 0.05 | ~8.6% | N=13193; closest (~2.8× stop) |
| cmp_prtoe_routeD | **129.1** | 0.1 | **~5.15%** | N=1593 (first progress only); ranks partially disjoint — see surgery below. **Do not kill.** |

When dyad + lcdm both hit R−1 ≤ 0.05 (+ CL test): run Laplace / finalize scripts; update
CHAIN_TABLES with bookable GetDist; close T3 / T11 machine halves. Exact commands:
`docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`.

## RouteD — recommended next surgery (document only; **do not kill** until owner fires it)

**Trigger met in spirit, early in wall-clock:** raw accept still **~5%** and R−1 **high (129)**
on the first progress row; three ranks are **not yet in one basin**.

| diagnostic (2026-08-02 ~22:20) | value |
|---|---|
| raw accept Σ | 5.15% (1828/35479) |
| R−1 / stop | 129.1 / 0.1 (~1290×) |
| H₀ post-50% means by rank | ≈ **68.55 / 68.66 / 69.83** (spread ~1.28) |
| thaw (`dcdf_floor_thaw`) rank means | ≈ 0.076 / 0.063 / 0.045 (rank3 lower) |
| live proposal seed | `chains/routeD_basin.covmat` (meta scale **0.25**; basin from winner rank-1, n_basin=139) |
| learn_proposal gates (live input) | `learn_proposal_Rminus1_max[_early] = 10000` (open) |

**Interpretation:** accept ~5% is low-but-alive Metropolis, not the old ~99% crawl; the
remaining defect is **between-rank basin offset** (especially rank 3 on H₀), which inflates
Gelman–Rubin regardless of within-rank step size. Waiting alone does not merge disjoint ranks
if the seed basin was cut from one rank’s samples at scale 0.25.

### Recommended surgery (owner-gated; archive-then-reseed pattern — same family as prior routeD repairs)

1. **Do not kill yet** until at least a **second progress row** lands *or* owner decides the
   first-row R−1 is enough evidence that patience is wasted. If a later row shows R−1
   falling toward O(10) with rank means overlapping, skip surgery.
2. When firing surgery (owner decision):
   - Archive live products to `chains/_archive_routeD_<stamp>/` (progress, checkpoint,
     `.{1,2,3}.txt`, launchlog, covmat copy). Keep yaml.
   - Rebuild proposal from **overlapping best samples across all three ranks**, not a single
     winner basin at scale 0.25:
     - Prefer samples within ~few units of the global best −logpost on **each** rank that
       reached that neighbourhood; if rank 3 never entered the low-H₀ pocket, **re-init
       rank starts** (ref) near the winner mean from `routeD_basin_meta.json` /
       best-of-rank-1 rather than only shrinking covmat.
     - Covmat recipe: empirical covariance of pooled near-best samples, then optional
       **widen** diagonals toward config proposal widths if raw accept stays ≲5% after
       restart (scale **up**, not another 0.25 shrink — the basin matrix is already tight:
       H₀ sd ~0.13 vs config proposal 0.5).
     - Tooling in tree: `scripts/build_reseed_covmat.py` (model-chain pattern),
       `scripts/build_chain_seed.py` (correlation-preserving physical-width seed),
       `scripts/rank_basin_diagnostic.py` (extend `BASES` to include `cmp_prtoe_routeD`
       before/after).
   - Point `covmat:` at the new seed; keep `learn_proposal_Rminus1_max` gated so the
     sampler cannot re-collapse from an unconverged cloud (historical failure mode when
     early max was 30). Live input currently uses 10000 — after reseed, consider
     restoring a moderate gate (e.g. 2–30) once ranks share a basin, or leave open only
     if ranks already overlap.
   - Relaunch fresh (not resume) per classy-rebuild / checkpoint trust rules; pattern
     reference: `scripts/launch_routeD_fresh.sh` (update guards/paths to current seed).
3. **Success criteria after reseed:** raw accept in a healthy band (~10–30% with blocking),
   rank H₀ means within ~1 within-rank σ of each other, R−1 falling over successive
   progress rows toward 0.1. Only then is `dcdf_floor_thaw` bookable.

**Non-goals:** do not kill the bbnfix pair for RouteD capacity; do not quote thaw ≠ 0
from the current disjoint ranks.

## OPEN-MACHINE (waits on runs)

- Matched DES/KiDS lensing (#161) — after capacity free
- conv_desi — unproduced; owner whether to re-architect seed
- zon_disp — parked by decision
- Granule SP dynamics / χ-lag sims
- α_c / α_g posteriors for galactic / SMBH atoms

## OPEN-THEORY (do not fake-complete)

- Koide #101 / #102 (node + Brannen phase)
- T14 link 4 sign(H_kin) — 3D toroidal product
- Bounce turn dynamics (bigbang / white holes / inflation / cyclic)
- Hierarchy §6f / basement μ5 residual
- Page *curve* dynamics (coefficient paid)
- Baryogenesis ω_J *forward* derivation (back-target only so far)
- Cosmic magnetism void floor + RM coherence formula

## WATCH-EXTERNAL

- Lattice T_c/√σ (#67), DESI 4PCF, NewAthena, BipoSH data application, helium fork, …

## Packaging / public

Hygiene reconfirmed **2026-08-03** (`scripts/arxiv_package_audit.py` → `_PACKAGE_AUDIT.md`).
Staging shelf `docs/arXivReady/` is being refreshed to include lattice-tc-gap, bbn-eps-bound,
and kination-tracking-note in addition to the original three.

| deliverable | status |
|---|---|
| supertrace-note | **SHIPPED** (Zenodo); arXiv optional (gr-qc) |
| neutrino-mbb | TeX ready; **owner submitted to William Fairbank (2026-08-03)** — packaging paused; hep-ph endorsement still the arXiv gate |
| radio-lattice | **READY** 7 pp; **astro-ph endorsement** |
| lattice-tc-gap | **READY** 2 pp; **hep-lat endorsement** |
| fairbank-0nubb | **NOT_READY** — README only; do not invent TeX (duplicate of neutrino-mbb; Fairbank thread owns neutrino-mbb) |
| bbn-eps-bound | **READY** 3 pp; **astro-ph endorsement**; optional dense ε_max(T_c) residual (bound at measured T_c) |
| kination-tracking-note | **READY** 2 pp; **gr-qc endorsement**; extracted from MATH_SPINE §7 2026-08-02 |

Hygiene: `scripts/arxiv_package_audit.py` → `docs/working_logs/_PACKAGE_AUDIT.md`.

### Docs shelf remainder (not package sources)

After kination extraction, **PAPER_CANDIDATE count on top-level `docs/PRTOE_*.md` is zero.**
**2026-08-03 re-audit:** still **0** new candidates — all borderline COMPLETE rechecked and
rejected (see `_ARXIV_CANDIDACY.md` header / §E). Remaining work on the live shelf is not
“make more short papers from COMPLETE files”:

| bucket | n (approx) | what to do |
|---|---:|---|
| COMPLETE / COMPLETE-CONDITIONAL / LEDGER | ~41 | **CORPUS_ONLY** — keep as identity/scorecard/registry; de-AI residual greps clean |
| OPEN-MACHINE | 8 | Wait on chains/sims (bbnfix, routeD, conv_desi, lensing, α_c/α_g, granule) |
| OPEN-THEORY | 10 | Real mechanism debt — do not fake-complete (Koide, bounce, T14 sign, hierarchy, …) |
| WATCH-EXTERNAL | 5 | Lattice, DESI 4PCF, NewAthena, BipoSH data, helium fork |
| exploratory/ | 37 | Unlinked breadth; work continues there, not on the public shelf |

Desk OPEN remains **0**. Residual “owed” language in COMPLETE files is mostly honest open residue, not stale premise (one BipoSH line in `PRTOE_radio_lattice.md` corrected 2026-08-02).

## Tribunal coordination (Grok + Claude + ChatGPT)

Live handoff brief: **[`ForGrok&Claude.md`](../../ForGrok&Claude.md)** (repo root; now a
**three-seat tribunal**). Quick card: [`TRIBUNAL.md`](TRIBUNAL.md).

| Seat | Role |
|---|---|
| Grok | Blue builder |
| Claude | **Red team only** (pure attack; no blue) |
| ChatGPT | **Neutral referee — no side** |

**Law:** unanimous AGREE or the conversation continues (no majority booking). Primary science:
T14; not three deep theory sprints in parallel.

## Next recommended sessions

1. Leave bbnfix pair alone unless dual gate opens (live: lcdm R−1 **0.049324**@N=26294 with
   `converged:true` · dyad **0.056889**@N=24677 with `converged:false` — one ready leg is **NOT**
   bookable);
   book only via `_POSTERIOR_BOOKING_CHECKLIST.md` + dual R−1&lt;0.05 + self-stop
2. RouteD: leave alone (live R−1 **0.728432**@N=8120, three ranks — early ~7.28× stop 0.1; **not**
   the old ~129 one-row state). Do **not** archive-and-reseed a converging multi-rank chain from a
   stale headline; **owner kills only when applying a reseed**
3. Theory sprints one at a time (Koide OR bounce OR T14 3D), never all three half-done —
   see `ForGrok&Claude.md` for dual-agent split
4. Endorsement chase in parallel (radio-lattice, lattice-tc-gap, bbn-eps-bound, kination READY;
   supertrace SHIPPED; **neutrino-mbb with Fairbank** — packaging paused; Fairbank-0nubb NOT_READY)
5. Check 12 on hierarchy / remaining giants only when editing them
6. Residual dead-premise greps are clean as of 2026-08-02 residual pass; re-run only after
   large chain-status edits
