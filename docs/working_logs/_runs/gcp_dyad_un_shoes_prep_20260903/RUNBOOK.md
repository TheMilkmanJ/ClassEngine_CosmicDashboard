# GCP prep — dyad SH0ES UltraNest leg (the outstanding twin) — 2026-09-04

**Purpose:** exact, budget-guarded runbook to run the **dyad SH0ES UltraNest** evidence leg on
Google Compute Engine. **AWS is closed.** Nothing in this package changes physics, priors,
datasets, likelihood composition, or booked engine settings.

**Hard fences (unchanged project rules):**
- No mid-run logZ quotes. ΔlnZ only after BOTH legs of a twin finish with final summaries.
- Within-anchor only (never mix SH0ES / TRGB / no-H0 Z).
- The integrand is frozen. Path rewrites (`/home/themilkmanj` → host `$HOME`) are the ONLY
  permitted edit to the yaml, exactly as done on the previous fleet (see the `.host.yaml` receipts).

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
| engine settings | `nlive=400`, `frac_remain=0.01`, `dlogz=0.5`, `Lepsilon=0.001`, SliceSampler `nsteps=2*ndim` (LCDM logged 24), `generate_region_oriented_direction`, hdf5, `nbootstraps=30`, `ndraw=128..65536` |
| MPI layout on the booked twin | `mpi_size=96`, one rank per hwthread, `OMP_NUM_THREADS=1` |

**Why this is the outstanding leg:** the SH0ES **LCDM** UltraNest twin FINISHED and is receipted
(`un_lcdm_shoes_finished_20260824/`, logZ −1413.4857 ± 0.5842). The SH0ES **dyad** UltraNest run
was last scanned 2026-08-25 at **remainder 15.0%** and stopped without finishing. Live docs say
"close enough to compare, not far enough to book." No nested ΔlnZ exists.

## 2. Driver — Google-only reconstruction (AWS closed)

The 2026-08-13 freeze driver
(sha256 `0f7932dcc0ebc88cdab24052afd94fd0a5ff6481203b51e614cf1ec42e728e8f`, 14912 B)
was **never committed**. Rechecked 2026-09-04: not in any git branch, not in
TheMilkmanJ GitHub, not in the owner's Google Drive. AWS recovery is off the table.

`scripts/ultranest_cobaya.py` is now **receipts-reconstructed** from the finished LCDM
UltraNest twins. It pins the logged engine settings and integrand convention
(Cobaya logposterior; unit-cube transform on prior support). It will **not** match
the freeze sha256. Do not claim it is the freeze byte copy. The yaml is untouched.

Exact launch (settings pinned; do not change them):

```bash
OMP_NUM_THREADS=1 mpirun --use-hwthread-cpus -n 96 \
  python scripts/ultranest_cobaya.py dyad_mnu_bbnfix_desidr2_ev.host.yaml \
  "$HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod" \
  --nlive 400 --frac-remain 0.01
# resume after GCP preemption (same outdir, hdf5 present):
#   ... --nlive 400 --frac-remain 0.01 --resume
```

The old AWS 15%-remainder checkpoint is unavailable. This Google run is a **fresh start**.

## 3. Parallel scaling analysis (from this repo's receipts)

- **Mechanism:** MPI only. The driver runs under `mpirun`; UltraNest gathers region draws
  across ranks; **rank 0 alone** writes the hdf5 checkpoint. No Slurm, no job arrays, no
  shared filesystem required on one node.
- **Measured throughput (finished LCDM twin):** 2,048,560 likelihood calls in 309.93 h wall on
  96 ranks = **29,753 vCPU-h**, ~52 s per call per rank.
- **Useful ceiling:** ~**150–250 ranks**. A single C4 VM reaches 288 vCPU; multi-machine adds
  risk, not speed. Comparability argues for matching the booked twin's **96 ranks**.
- **RAM / disk:** `c4-highcpu` (2 GiB/vCPU) is the right shape; **50 GB** boot disk is ample.

## 4. Budget math — the $10 verdict (be honest)

Prices verified 2026-09-03, us-central1: `c4-highcpu-96` **$4.0825/h on-demand**,
**$2.4495/h spot**. Spot can preempt; hdf5 + `--resume` makes preemption safe.

| scenario | est. vCPU-h | spot $ | on-demand $ |
|---|---:|---:|---:|
| Fresh dyad leg from zero (the Google path) | ~50,000–57,000 | ~$1,280–1,460 | ~$2,130–2,430 |
| **What $10 buys** (96-vCPU spot, minus ~$1 disk/overhead) | ~350 | $10 | — |

**Verdict: $10 cannot finish this leg.** It buys ~0.7% of a fresh start. What $10 CAN buy:

1. **Stage 1 — validation on GCP (~$1–2):** `c4-highcpu-8` spot, build + CLASS verify + measured s/call.
2. **One checkpointed production burst (~$6):** ~2.4 h on `c4-highcpu-96` spot. Pipeline proof only.

**Core-count report:**
- *Theoretical maximum:* 288 vCPU on one C4 VM.
- *Likely new-account quota:* free-trial = hard **8 vCPU**. Paid: often 12–32 until a C4 quota request.
- *Recommended initial:* **8 vCPU** (validation), then **32–96 vCPU spot, single node**, bursts sized to the credit.

## 5. Exact commands

### 5.0 Owner workstation: GCP login + create the VM

This cloud agent has **no gcloud and no Google Cloud credentials**. The owner must log in
on a machine that can reach the Google Cloud console (or `gcloud auth login`).

```bash
# Preflight — verify credit/billing and quota BEFORE creating anything
gcloud auth login
gcloud config set project PROJECT_ID
gcloud billing accounts list
gcloud compute regions describe us-central1 --format='value(quotas)' | tr ';' '\n' | grep -i -E 'CPUS|C4'

# Stage 1 VM (validation, ~$0.20/h spot; hard 6h self-destruct)
gcloud compute instances create prtoe-un-dyad-stage1 \
  --zone=us-central1-a --machine-type=c4-highcpu-8 \
  --provisioning-model=SPOT --instance-termination-action=STOP \
  --max-run-duration=6h \
  --create-disk=boot=yes,image-family=ubuntu-2404-lts-amd64,image-project=ubuntu-os-cloud,size=50,type=hyperdisk-balanced

# Production burst (only after stage 1; 96-vCPU spot ~$2.45/h -> 2h20m ~= $5.7)
gcloud compute instances create prtoe-un-dyad-burst \
  --zone=us-central1-a --machine-type=c4-highcpu-96 \
  --provisioning-model=SPOT --instance-termination-action=STOP \
  --max-run-duration=2h20m \
  --create-disk=boot=yes,image-family=ubuntu-2404-lts-amd64,image-project=ubuntu-os-cloud,size=50,type=hyperdisk-balanced
```

`--max-run-duration` + `--instance-termination-action=STOP` is the primary budget guard.

### 5.1 On the VM: bootstrap, verify, time (Stage 1)

```bash
git clone https://github.com/TheMilkmanJ/ClassEngine_CosmicDashboard.git "$HOME/prtoe_class"
cd "$HOME/prtoe_class" && git checkout cursor/gcp-dyad-shoes-ultranest-prep-4b50
bash scripts/gcp_ultranest_dyad_bootstrap.sh build
bash scripts/gcp_ultranest_dyad_bootstrap.sh verify
bash scripts/gcp_ultranest_dyad_bootstrap.sh driver    # reconstructed-driver self-test + --help
bash scripts/gcp_ultranest_dyad_bootstrap.sh time
```

`verify` prints `REFERENCE_TT_HASH` and three C_l values. If they differ from the booked
twin box beyond ~1e-10 relative, STOP.

### 5.2 Launch / resume (production burst)

```bash
CONFIRM=YES MAX_HOURS=2.3 NRANKS=96 \
  DRIVER_ARGS="dyad_mnu_bbnfix_desidr2_ev.host.yaml $HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod --nlive 400 --frac-remain 0.01" \
  bash scripts/gcp_ultranest_dyad_bootstrap.sh launch

CONFIRM=YES MAX_HOURS=2.3 NRANKS=96 \
  DRIVER_ARGS="dyad_mnu_bbnfix_desidr2_ev.host.yaml $HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod --nlive 400 --frac-remain 0.01 --resume" \
  bash scripts/gcp_ultranest_dyad_bootstrap.sh resume

bash scripts/gcp_ultranest_dyad_bootstrap.sh status    # health only — NOT quotable
bash scripts/gcp_ultranest_dyad_bootstrap.sh peel
```

Checkpoint path: `$HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod/`
(`results/points.hdf5` = resume; `ultranest_summary.json` is the only quotable logZ).

### 5.3 Teardown verification (leave NOTHING running)

```bash
gcloud compute instances list
gcloud compute disks list
gcloud compute snapshots list
```

## 6. Blockers requiring the Google console or the owner

1. **Google Cloud login + project + billing.** This agent has no `gcloud` and no GCP credentials.
   Confirm the $10 Google AI Pro credit applies to Compute Engine. Treat $10 as a hard cap.
2. **Quota.** Free-trial billing caps at 8 vCPU. A 96-vCPU burst needs a paid account + C4 quota.
3. **Decision.** Spend the credit on Stage 1 validation (recommended) or one ~2 h burst.
   Finishing the leg needs ~$1.3–1.5k spot from scratch — out of scope for this credit.
