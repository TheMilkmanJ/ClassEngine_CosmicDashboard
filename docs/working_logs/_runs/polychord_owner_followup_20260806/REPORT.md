# PolyChord owner follow-up — live AWS dyad evidence leg (2026-08-06)

Purpose: record the owner-run follow-up after the cloud build note, so forward-facing docs can
quote the live nested-sampling state without pretending a verdict already exists.

## 1. What is live

Owner-launched on AWS:

- config: `cmp_prtoe_dyad_ev.yaml`
- sampler: PolyChord
- output path: `chains/cmp_prtoe_dyad_ev_polychord_raw/`

Observed owner-console state:

- `pypolychord` loaded successfully
- raw output directory created
- resume file written
- live-point file created
- run entered `Calling PolyChord...`
- run advanced to `generating live points`

This is a **real live nested run**, not a dry bootstrap.

## 2. What is not yet true

- no nested evidence number is bookable yet
- no `Delta ln Z` verdict exists yet
- Laplace-from-MCMC remains the only graded evidence number until the nested pair is complete

So the correct shelf sentence is:

> AWS PolyChord **sampled-ε dyad** evidence leg is live, but no nested verdict is bookable yet and
> the repaired ΛCDM twin is still only a waiting remote worker, not a finished denominator.

## 3. Timing follow-up

Owner `time` run on the AWS box reported:

- mean `3.68 s/call`
- `14` sampled parameters

This supersedes the older slower cloud bootstrap timing for forward-facing affordability language.
It does **not** itself decide `P-2026-044`; it only changes the cost reality.

The safe current affordability statement is:

> nested sampling is no longer blocked by laptop economics alone; the live blocker is completion of
> the AWS dyad leg and then letting the repaired ΛCDM twin run on the same build.

## 4. Shelf implications

Use this note to update forward-facing docs that still say:

- PolyChord is offline
- nested sampling waits on cluster time
- the lane is unaffordable

Do **not** use this note to:

- promote a nested evidence result
- quote a `Delta ln Z`
- claim the dyad leg alone decides anything

## 5. Update at 2026-08-06 02:08 MDT

The original owner-follow-up state above is superseded by the 96-vCPU replacement-box state.

Current truth:

- the old `c7i.8xlarge` Spot box was not resized in place; AWS does not support Spot instance-type
  modification
- the active evidence box is a fresh `c7i.24xlarge` Spot instance
- `cmp_prtoe_dyad_ev.yaml` is live there at `96` ranks using
  `mpirun --use-hwthread-cpus -n 96 --bind-to none`
- the live dyad log has reached `generating live points`
- `cmp_lcdm_ev.yaml` was found to have a real config drift (`sampler: evaluate: null`) and was
  repaired from the repo's own LCDM PolyChord authority before being resynced to AWS
- the remote autolaunch worker is alive and waiting behind the live dyad process

## 6. Update at 2026-08-06 02:42 MDT

The 96-rank replacement-box run is still **up**, but it is no longer actively advancing.

Current watcher truth:

- process tree still present (`proc=97`, `launcher=1`)
- phase still reads `generating_live_points`
- last live-point growth was at **2026-08-06 02:21 MDT**
- watcher state at **2026-08-06 02:41 MDT** is:
  - `status=STALLED`
  - `stalled_intervals=17`
  - `live_size=2181554`
  - `resume=yes`

So the correct shelf sentence is now:

> AWS PolyChord **sampled-ε dyad** evidence process is still up on the 96-vCPU replacement box,
> but the watcher currently marks it **STALLED** rather than actively growing. The repaired ΛCDM
> twin worker remains queued behind it, and there is still no nested verdict.
