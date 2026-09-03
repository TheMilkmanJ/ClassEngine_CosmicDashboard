# GCP prep — dyad SH0ES UltraNest leg (the outstanding twin) — 2026-09-03

**Purpose:** exact, budget-guarded runbook to run the **dyad SH0ES UltraNest** evidence leg on
Google Compute Engine. This is prep + honesty math only. **Nothing in this package changes
physics, priors, datasets, likelihood composition, or engine settings.**

**Hard fences (unchanged project rules):**
- No mid-run logZ quotes. ΔlnZ only after BOTH legs of a twin finish with final summaries.
- Within-anchor only (never mix SH0ES / TRGB / no-H0 Z).
- The integrand is frozen. Path rewrites (`/home/themilkmanj` → host `$HOME`) are the ONLY
  permitted edit to the yaml, exactly as done on the AWS fleet (see the `.host.yaml` receipts).

---

## 1. Exact target (verified)

| item | value |
|---|---|
| repo / branch | `TheMilkmanJ/ClassEngine_CosmicDashboard`, default branch **`master`** |
| commit verified | `3a002d20c8f8c69aeb56473271f08460956bb481` ("Nested status: SH0ES compare, not a booked sampler") |
| canonical yaml | **`dyad_mnu_bbnfix_desidr2_ev.yaml`** (repo root) |
| repo yaml sha256 | `c0be593cae81219c6a69996d046cc6a6eb2c093c7aed5e3609381ebb140b4fae` (6115 B) |
| 2026-08-13 freeze sha256 | `323241c997cbb78ee9b3b74ca6b38672b39a4f2cedd939e0385ada706749de5a` (6114 B) — **identical content; delta is one trailing newline** |
| sampled params (13) | omega_b, H0, logA, n_s, z_reio, dcdf_rho_inf, varying_me, A_planck, A_act, P_act, Tcal, Ecal, m_ncdm |
| likelihood stack | Planck lowl TT+EE, plik-lite TTTEEE, Planck lensing (clik), DESI DR2 BAO ALL, **sn.pantheonplusshoes**, ACT DR6 (candl), SPT-3G lite (candl), production-faithful BBN prior |
| engine | UltraNest **4.5.0** `ReactiveNestedSampler` (driver `scripts/ultranest_cobaya.py`; the yaml `sampler: polychord` block is **unused** by the UN driver) |
| engine settings | `nlive=400`, `frac_remain=0.01`, `dlogz=0.5`, `dKL=0.5`, `Lepsilon=0.001`, `min_ess=400`, `nbootstraps=30`, hdf5 backend, MLFriends region sampling (per lcdm debug.log; the freeze README "step sampler" line does not match the logs) |
| MPI layout on the booked twin | `mpi_size=96`, one rank per hwthread, `OMP_NUM_THREADS=1` |

**Why this is the outstanding leg:** the SH0ES **LCDM** UltraNest twin FINISHED and is receipted
(`un_lcdm_shoes_finished_20260824/`, logZ −1413.4857 ± 0.5842). The SH0ES **dyad** UltraNest run
on `i-04ead482af737e7bf` was last scanned 2026-08-25 at **remainder 15.0%** (partial logZ
−1411.24, health only) and the fleet was stopped without finishing — live docs now say
"close enough to compare, not far enough to book." No nested ΔlnZ exists. Finishing THIS leg
(same engine, same settings) is what unlocks the SH0ES UltraNest ΔlnZ booking.

## 2. BLOCKER — the UN driver is not in git

`scripts/ultranest_cobaya.py` is recorded in `repro_freeze_20260813/MANIFEST.json`
(sha256 `0f7932dcc0ebc88cdab24052afd94fd0a5ff6481203b51e614cf1ec42e728e8f`, 14912 B at freeze)
but was **never committed**. It exists only on:

- the AWS box `i-04ead482af737e7bf` at `/home/ubuntu/prtoe_class/scripts/ultranest_cobaya.py`, and/or
- the local box at `/home/themilkmanj/prtoe_class/scripts/ultranest_cobaya.py`.

**Owner action (AWS console/SSM or local box — outside this repo prep):** recover the file,
verify `sha256sum` against the freeze value, and commit it (or place it on the GCP VM).
The dyad leg MUST run the byte-identical driver the finished LCDM twin used, or the twins
are not comparable. Example peel (owner, only if the box still exists):

```bash
# owner machine — do not run from automation
aws ssm send-command --instance-ids i-04ead482af737e7bf --document-name AWS-RunShellScript \
  --parameters 'commands=["sha256sum /home/ubuntu/prtoe_class/scripts/ultranest_cobaya.py","base64 /home/ubuntu/prtoe_class/scripts/ultranest_cobaya.py"]'
```

**Strongly recommended second recovery — the checkpoint.** The dyad run's UltraNest outdir
`/home/ubuntu/docs_runs/ultranest_20260811/un_dyad_ev_prod/` (notably `results/points.hdf5`)
holds ~85% of the leg's completed work. UltraNest resumes from the hdf5 store
(`ReactiveNestedSampler(..., resume=True)` semantics — confirm the driver's resume flag via
`--help` after recovery). Resuming instead of restarting cuts the remaining cost by roughly
**60%** (Section 4). If the instance or its EBS volume still exists, tar and download that
directory before any GCP spend.

## 3. Parallel scaling analysis (from this repo's receipts)

- **Mechanism:** MPI only. The driver runs under `mpirun` (OpenMPI/prterun); UltraNest gathers
  region draws across ranks each iteration; **rank 0 alone** writes the hdf5 checkpoint and
  chains. No Slurm, no job arrays, no Python multiprocessing, no shared filesystem required
  for multi-node (data must simply exist at identical paths on every node).
- **Measured throughput (finished LCDM twin):** 2,048,560 likelihood calls in 309.93 h wall on
  96 ranks = **29,753 vCPU-h**, i.e. ~52 s per call per rank. Endgame acceptance efficiency
  0.73% (~137 draws per accepted point) — near-linear scaling at 96 ranks.
- **Dyad pace (from the 24/25 Aug scans):** remainder 21.1% → 15.0% in ~24 h at 96 ranks
  (0.34 remainder e-folds/day). The dyad likelihood is slower than LCDM (13 dims,
  varying-constants CLASS; desk-recorded 66 s/call class).
- **Useful ceiling:** parallelism is bounded by draws-per-iteration (~1/efficiency ≈ 140–900
  during the run), so ~**150–250 ranks** is the practical ceiling; beyond that, gather rounds
  idle. A single C4 VM reaches 288 vCPU, so **multi-machine adds risk, not speed**, for this
  workload. Comparability argues for matching the booked twin's **96 ranks**.
- **RAM:** 2 GiB/rank held on AWS (c6i.24xlarge, 192 GiB / 96 ranks) → `c4-highcpu` (2 GiB/vCPU) is the right shape.
- **Disk:** repo ~0.2 GB + cobaya packages ~2.5 GB + candl_data ~0.4 GB + venv/CLASS build ~2 GB + outputs <1 GB → **50 GB** boot disk is ample.

## 4. Budget math — the $10 verdict (be honest)

Prices verified 2026-09-03, us-central1: `c4-highcpu-96` **$4.0825/h on-demand**,
**$2.4495/h spot** ($0.0255/vCPU-h); `c4-highcpu-8` spot $0.204/h. Spot can preempt;
the hdf5 checkpoint + resume makes preemption safe (lose at most the in-flight iteration).

| scenario | est. vCPU-h | spot $ | on-demand $ |
|---|---:|---:|---:|
| Fresh dyad leg from zero | ~50,000–57,000 | ~$1,280–1,460 | ~$2,130–2,430 |
| Resume from AWS checkpoint (rem 15% → 1% + strategy tail) | ~18,000–25,000 | ~$470–640 | ~$780–1,060 |
| **What $10 buys** (96-vCPU spot, minus ~$1 disk/overhead) | ~350 | $10 | — |

**Verdict: $10 cannot finish this leg.** It buys ~2% of the remaining work even with the AWS
checkpoint, ~0.7% from scratch. What $10 CAN buy safely:

1. **Stage 1 — full validation on GCP (~$1–2):** build the exact stack on a `c4-highcpu-8`
   spot VM, verify the CLASS reference spectrum matches, measure real s/call, and produce an
   exact finish-cost quote from measured numbers.
2. **One checkpointed production burst (~$6):** ~2.4 h on `c4-highcpu-96` spot (or ~7 h on
   32 vCPU if quota-bound), resumable later. Meaningful only as a pipeline proof, not progress.

**Core-count report (as requested):**
- *Theoretical maximum:* 288 vCPU on one C4 VM; multi-node MPI beyond that is technically
  possible but wasted (ceiling ~150–250 useful ranks) and violates nothing but the wallet.
- *Likely new-account quota:* free-trial billing = hard **8 vCPU** global cap (no increase
  possible on trial). New paid accounts: `CPUS_ALL_REGIONS` typically 12–32 plus a separate
  C4-family per-region quota; 96 usually requires a quota request with billing history.
- *Recommended initial:* **8 vCPU** (validation), then **32–96 vCPU spot, single node,
  96 ranks max**, in checkpointed bursts sized to the credit.

## 5. Exact commands

### 5.0 Workstation: create the VM (budget guard at the VM level)

```bash
# Preflight — verify credit/billing and quota BEFORE creating anything (console or:)
gcloud billing accounts list
gcloud compute regions describe us-central1 --format='value(quotas)' | tr ';' '\n' | grep -i -E 'CPUS|C4'

# Stage 1 VM (validation, ~$0.20/h spot; hard 6h self-destruct)
gcloud compute instances create prtoe-un-dyad-stage1 \
  --zone=us-central1-a --machine-type=c4-highcpu-8 \
  --provisioning-model=SPOT --instance-termination-action=STOP \
  --max-run-duration=6h \
  --create-disk=boot=yes,image-family=ubuntu-2404-lts-amd64,image-project=ubuntu-os-cloud,size=50,type=hyperdisk-balanced

# Production burst VM (only after stage 1 passes; size MAX_RUN to your remaining credit:
# spot 96 vCPU = $2.45/h -> 2h20m ~= $5.7)
gcloud compute instances create prtoe-un-dyad-burst \
  --zone=us-central1-a --machine-type=c4-highcpu-96 \
  --provisioning-model=SPOT --instance-termination-action=STOP \
  --max-run-duration=2h20m \
  --create-disk=boot=yes,image-family=ubuntu-2404-lts-amd64,image-project=ubuntu-os-cloud,size=50,type=hyperdisk-balanced
```

`--max-run-duration` + `--instance-termination-action=STOP` is the primary budget guard: the
VM stops itself even if SSH is lost; the checkpoint survives on the boot disk (a stopped VM
bills only the disk, cents/day). The bootstrap script adds an in-VM `shutdown` backstop.

### 5.1 On the VM: bootstrap, verify, time (Stage 1)

```bash
git clone https://github.com/TheMilkmanJ/ClassEngine_CosmicDashboard.git "$HOME/prtoe_class"
cd "$HOME/prtoe_class" && git checkout 3a002d20c8f8c69aeb56473271f08460956bb481
# place the recovered scripts/ultranest_cobaya.py here (see Section 2), then:
bash scripts/gcp_ultranest_dyad_bootstrap.sh build     # ~30 min: deps + data + CLASS build + host yaml
bash scripts/gcp_ultranest_dyad_bootstrap.sh verify    # CLASS reference spectrum — must match local
bash scripts/gcp_ultranest_dyad_bootstrap.sh driver    # sha256 check vs freeze + prints driver --help
bash scripts/gcp_ultranest_dyad_bootstrap.sh time      # measured s/call -> exact finish-cost quote
```

`verify` prints `REFERENCE_TT_HASH` and three C_l values; compare against the same snippet on
the box that ran the booked twins (`scripts/aws_polychord_bootstrap.sh verify` format).
**If they differ beyond ~1e-10 relative, STOP — the evidence would not be comparable.**

### 5.2 Launch / resume (production burst)

The exact driver CLI is confirmed from `driver --help` after recovery (receipts pin the
required values: yaml, outdir, `nlive=400`, `frac_remain=0.01`). Shape:

```bash
# fresh start (only if the AWS checkpoint is unrecoverable)
CONFIRM=YES MAX_HOURS=2.3 NRANKS=96 \
  DRIVER_ARGS="dyad_mnu_bbnfix_desidr2_ev.host.yaml $HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod --nlive 400 --frac-remain 0.01" \
  bash scripts/gcp_ultranest_dyad_bootstrap.sh launch

# resume after preemption / stop / new burst: restore un_dyad_ev_prod/ (incl. results/points.hdf5)
# to the SAME outdir path, add the driver's resume flag, then:
CONFIRM=YES MAX_HOURS=2.3 NRANKS=96 \
  DRIVER_ARGS="dyad_mnu_bbnfix_desidr2_ev.host.yaml $HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod --nlive 400 --frac-remain 0.01 --resume" \
  bash scripts/gcp_ultranest_dyad_bootstrap.sh resume

bash scripts/gcp_ultranest_dyad_bootstrap.sh status    # remainder %, rate, disk — health only, NOT quotable
bash scripts/gcp_ultranest_dyad_bootstrap.sh peel      # tar outdir for download before teardown
```

Checkpoint/output path on GCP: `$HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod/`
(`results/points.hdf5` = resume authority; `ultranest_summary.json` appears only at DONE and
is the only quotable logZ artifact, same as the lcdm receipts).

### 5.3 Teardown verification (leave NOTHING running)

```bash
gcloud compute instances list                 # must be empty (or all TERMINATED)
gcloud compute disks list                     # delete leftovers: gcloud compute disks delete <name> --zone=<zone>
gcloud compute snapshots list                 # should be empty
# next day: check billing report shows $0/day burn
```

## 6. Blockers requiring the GCP console or the owner

1. **Driver + checkpoint recovery** from AWS/local (Section 2) — nothing can launch without the driver.
2. **Billing/credit verification:** the $10 Google AI Pro credit is unverified; confirm it applies
   to Compute Engine in this project before creating VMs. Treat $10 as a hard cap.
3. **Quota:** free-trial billing caps at 8 vCPU with no increase path; a 96-vCPU burst needs a
   paid account + C4-family quota in one region.
4. **Decision:** spend the credit on Stage 1 validation + exact quote (recommended), or on a
   ~2 h symbolic burst. Finishing the leg needs either the AWS checkpoint + roughly $500–650
   of spot, or ~$1.3–1.5k spot from scratch — out of scope for this credit.
