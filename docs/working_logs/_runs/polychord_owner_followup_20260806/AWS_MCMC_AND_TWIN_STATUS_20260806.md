# AWS / MCMC Status — 2026-08-06

Purpose: record the current local MCMC state plus the live AWS nested-evidence state after the
LCDM twin autolaunch was armed.

## 1. Local MCMC truth

Checked again on **Thursday, August 6, 2026** just after **00:45 MDT**.

### `dyad_mnu_bbnfix`

- process tree is still live (`mpirun -n 3 ... dyad_mnu_bbnfix.input.yaml`)
- chain rank files are still writing:
  - `dyad_mnu_bbnfix.1.txt` mtime `2026-08-06 00:45:07 MDT`
  - `dyad_mnu_bbnfix.2.txt` mtime `2026-08-06 00:45:17 MDT`
  - `dyad_mnu_bbnfix.3.txt` mtime `2026-08-06 00:44:40 MDT`
- latest progress/checkpoint state is still:
  - `R−1 = 0.085619`
  - `N = 27525`
  - `converged: false`

So dyad is alive, but the booked gate is still blocked and the last referee-grade `R−1` is worse
than the stop bar.

### `cmp_prtoe_routeD`

- process tree is still live (`mpirun -n 3 ... cmp_prtoe_routeD.input.yaml`)
- latest stored progress/checkpoint now says:
  - `R−1 = 0.257073`
  - `N = 11422`
  - `t = 2026-08-06T01:51:33.402664`
  - `converged: false`

So routeD is alive, improving, but still not close enough to book.

### `cmp_lcdm_mnu_bbnfix`

- no live process, which is expected
- latest stored state remains:
  - `R−1 = 0.049324`
  - `N = 26294`
  - `converged: true`

## 2. AWS dyad evidence leg

The AWS dyad PolyChord run is live and advancing.

Healthy watcher:

- script: `scripts/watch_aws_dyad_polychord.sh`
- local watcher PID: `2832976`
- watcher state file:
  `docs/working_logs/_runs/polychord_owner_followup_20260806/aws_dyad_watch.state`

Watcher sample at **2026-08-06 00:47:37 MDT**:

- `status=OK`
- `proc=18`
- `launcher=1`
- `phase=generating_live_points`
- `live_size=708963`

This agrees with the direct AWS read at the same pass: the dyad live-point file is still growing.

## 3. LCDM twin autolaunch

The AWS-correct LCDM twin config has now been deployed to the EC2 box:

- remote YAML: `/home/ubuntu/prtoe_class/cmp_lcdm_ev.yaml`

The autolaunch worker is armed and waiting for the dyad leg to exit:

- remote script: `/home/ubuntu/prtoe_class/aws_autolaunch_lcdm_twin.sh`
- remote worker PID file: `/home/ubuntu/prtoe_class/cmp_lcdm_ev.autolaunch.pid`
- remote worker PID: `59984`
- remote worker log: `/home/ubuntu/prtoe_class/cmp_lcdm_ev.autolaunch.log`

Observed remote state:

- `2026-08-06T06:47:54+00:00 armed; waiting for dyad evidence leg to exit`
- `2026-08-06T06:47:54+00:00 dyad still active; sleeping 60s`
- `2026-08-06T06:48:54+00:00 dyad still active; sleeping 60s`

So the former blocker:

- missing AWS-side `cmp_lcdm_ev.yaml`

is now cured.

The remaining gate on the twin launch is only:

- dyad evidence leg still running
- solo-PolyChord rule remains in force

## 4. Standing

- local `bbnfix` gate: still blocked by dyad
- local `routeD`: still running, still unconverged
- AWS dyad evidence leg: live and growing
- AWS LCDM twin: armed to auto-launch on dyad exit

## 5. Update at 01:46 MDT on Thursday, August 6, 2026

The earlier AWS state above is now stale.

Current AWS truth:

- the **32-vCPU dyad evidence run is no longer live**
- the old AWS LCDM autolaunch worker is **no longer live**
- the EC2 instance is still `c7i.8xlarge`
- both `us-east-1` EC2 standard-vCPU quotas still read `32.0`, so the 96-vCPU resize is **not**
  active yet

What happened:

- the 32-vCPU dyad PolyChord leg reached `all live points generated`
- it then died with a Fortran runtime error while writing
  `chains/cmp_prtoe_dyad_ev_polychord_raw/cmp_prtoe_dyad_ev.stats`
- the concrete error in the launch log is:
  - `Fortran runtime error: Missing comma between descriptors`
  - file: `read_write.F90`

Current control action:

- a persistent local cutover service is now armed under user systemd:
  - unit: `aws-96-cutover.service`
- it already performed remote cleanup on the current AWS box
- it is now polling for the quota flip and will only proceed when both quotas reach `96`
- only after that will it:
  - stop the instance
  - modify it to `c7i.24xlarge`
  - restart the dyad evidence leg fresh at `96` MPI ranks
  - re-arm the LCDM twin at `96` MPI ranks

Authoritative local cutover files:

- `docs/working_logs/_runs/polychord_owner_followup_20260806/aws_96vcpu_cutover.log`
- `docs/working_logs/_runs/polychord_owner_followup_20260806/aws_96vcpu_cutover.state`
- `docs/working_logs/_runs/polychord_owner_followup_20260806/aws_96vcpu_cutover.stdout`

## 6. Update at 02:08 MDT on Thursday, August 6, 2026

The replacement path is now in force and has superseded the failed in-place cutover.

What happened:

- the stopped `c7i.8xlarge` Spot instance could not be resized in place
- AWS returned:
  - `UnsupportedOperation: Modifying 'instanceType' is not supported for spot instances`
- so the valid recovery path was a new Spot instance from the same AMI

Current AWS truth:

- new instance id: `i-0cb294312a23c4fe6`
- type: `c7i.24xlarge`
- AZ: `us-east-1a`
- lifecycle: `spot`

Current dyad truth:

- `cmp_prtoe_dyad_ev.yaml` is now live on the new box at `96` ranks
- launch uses:
  - `mpirun --use-hwthread-cpus -n 96 --bind-to none`
- live process tree shows the `prterun` launcher plus `96` `python -m cobaya.run` ranks
- dyad log is now past the old allocation failure and has reached:
  - `Writing a resume file ...`
  - `generating live points`

Current twin truth:

- `cmp_lcdm_ev.yaml` had a real config bug on disk:
  - it ended with `sampler: evaluate: null`
  - it was missing the BBN-symmetric `YHe` / `bbn` pieces
- that file is now repaired locally and re-synced to AWS
- the remote autolaunch worker is alive and now correctly waiting behind the live dyad process
- current worker behavior:
  - `dyad still active; sleeping 60s`

Watcher truth:

- local watcher service: `aws-dyad-watch.service`
- current watcher family is pointed at the new instance id and public IP
- early stale `DOWN` was from the failed first 96-rank launch before the `--use-hwthread-cpus`
  fix; that is no longer the authoritative read

## 7. Update at 02:42 MDT on Thursday, August 6, 2026

The replacement-box dyad run is still **up**, but it is no longer actively growing.

Current watcher state:

- `status=STALLED`
- `stalled_intervals=17`
- `proc=97`
- `launcher=1`
- `phase=generating_live_points`
- `resume=yes`
- `live_size=2181554`
- last observed growth / mtime: `2026-08-06 02:21 MDT`

So the accurate read is:

- AWS dyad process is still present
- it is **not** dead
- it is also **not** currently advancing
- the LCDM twin worker is still queued behind the dyad process

## 8. Update at 11:10 MDT on Thursday, August 6, 2026

The stalled Spot-box state above is now superseded by a clone-and-resume recovery.

What happened:

- all previously used AWS evidence instances were confirmed **stopped**
- the stopped `96`-vCPU Spot box `i-0cb294312a23c4fe6` was cloned to a new AMI
- a new **on-demand** `c7i.24xlarge` replacement was launched from that clone:
  - instance id: `i-0fca634f317aaf4bc`
  - AZ: `us-east-1d`
  - public IP: `34.207.247.94`

Exact failure diagnosed on the clone:

- the prior dyad run had reached `all live points generated`
- it then died while writing the `.stats` file
- root cause was a real PolyChord Fortran format bug in:
  - `cobaya_packages_clean/code/PolyChordLite/src/polychord/read_write.F90`
- bug shape:
  - missing comma before `" (Still Active)"`

Repairs applied:

1. patched `read_write.F90` locally and on the cloned AWS host
2. rebuilt PolyChord on the cloned AWS host
3. repaired the local LCDM twin YAML:
   - `num_repeats: 2d` -> `num_repeats: 24`
4. patched the LCDM autolaunch matcher so it recognizes resumed dyad commands
5. patched the local watcher so stopped instances are not misreported as `EIC_KEY_FAIL`

Current dyad truth:

- resumed on the new on-demand box with:
  - `mpirun --use-hwthread-cpus -n 96 --bind-to none python -m cobaya.run -r cmp_prtoe_dyad_ev.yaml`
- direct remote reads show the full `96`-rank process tree is **alive**
- log state is now:
  - `Resuming from previous run`
  - `started sampling`
- however, the live-point file has **not yet shown fresh growth** after the repaired resume

Current twin truth:

- the LCDM twin worker is re-armed on the new host
- it is correctly waiting behind the active dyad process under the solo-PolyChord rule

Current honest phrase:

- **dyad is alive, resumed, and sampling on the new on-demand 96-vCPU host, but it is not yet
  revalidated as actively re-growing on disk**
- **LCDM twin is armed and waiting**
