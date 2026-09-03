#!/usr/bin/env bash
# GCP bootstrap for the dyad SH0ES UltraNest evidence leg (the outstanding twin).
#
# Companion runbook (READ IT FIRST — budget math, VM creation flags, teardown):
#   docs/working_logs/_runs/gcp_dyad_un_shoes_prep_20260903/RUNBOOK.md
#
# Stages, in order:
#   build   — deps, likelihood data, modified CLASS, host-path yaml   (~30 min)
#   verify  — CLASS reference spectrum must match the local/AWS build (physics gate)
#   driver  — check recovered scripts/ultranest_cobaya.py vs the freeze sha256
#   time    — measure real s/likelihood-call -> exact finish-cost quote
#   launch  — guarded production start (requires CONFIRM=YES, MAX_HOURS, DRIVER_ARGS)
#   resume  — same, but refuses unless a checkpoint (points.hdf5) exists in OUT_DIR
#   status  — health peek (remainder %, rate). NOT quotable. No mid-run logZ bookings.
#   peel    — tar OUT_DIR for download before teardown
#
# Physics fence: the ONLY yaml edit performed here is the host path rewrite
# (/home/themilkmanj -> $HOME), identical to the AWS fleet's .host.yaml pattern.
# Engine settings are pinned by the driver invocation (nlive=400, frac_remain=0.01).
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/prtoe_class}"
PKG_DIR="${PKG_DIR:-$HOME/cobaya_packages_clean}"
CANDL_DIR="${CANDL_DIR:-$HOME/candl_data}"
VENV="${VENV:-$HOME/venv}"
YAML_SRC="dyad_mnu_bbnfix_desidr2_ev.yaml"
YAML_HOST="dyad_mnu_bbnfix_desidr2_ev.host.yaml"
DRIVER="scripts/ultranest_cobaya.py"
# sha256 of the driver at the 2026-08-13 repro freeze (repro_freeze_20260813/MANIFEST.json).
DRIVER_FREEZE_SHA="0f7932dcc0ebc88cdab24052afd94fd0a5ff6481203b51e614cf1ec42e728e8f"
OUT_DIR="${OUT_DIR:-$HOME/docs_runs/ultranest_gcp/un_dyad_ev_prod}"
NRANKS="${NRANKS:-$(nproc)}"
MPIRUN_EXTRA="${MPIRUN_EXTRA:---use-hwthread-cpus}"

case "${1:-}" in

build)
  sudo apt-get update -qq
  sudo apt-get install -y -qq build-essential gfortran python3-dev python3-pip \
       python3-venv libopenmpi-dev openmpi-bin git cmake wget unzip
  python3 -m venv "$VENV"; source "$VENV/bin/activate"
  pip install -q --upgrade pip wheel
  # ultranest pinned to the version the finished LCDM twin booked with (receipts: 4.5.0).
  pip install -q numpy scipy cython mpi4py "cobaya>=3.5" getdist candl-like \
       "ultranest==4.5.0" h5py
  cd "$REPO_DIR"
  # Host yaml: path rewrite ONLY (same pattern as the AWS .host.yaml receipts).
  sed "s|/home/themilkmanj|$HOME|g" "$YAML_SRC" > "$YAML_HOST"
  echo "yaml sha256 (repo -> host):"
  sha256sum "$YAML_SRC" "$YAML_HOST"
  # Likelihood data (~2.5 GB, fetched at GCP bandwidth — do not upload it).
  cobaya-install "$REPO_DIR/$YAML_HOST" --packages-path "$PKG_DIR" --skip-global || true
  # candl data (ACT DR6 + SPT3G) is NOT in cobaya's index.
  [ -d "$CANDL_DIR" ] || git clone --depth 1 \
      https://github.com/Lbalkenhol/candl_data "$CANDL_DIR"
  [ -d "$CANDL_DIR/candl_data/ACT_DR6_CMB_only_v0" ] || \
      echo "WARNING: ACT_DR6_CMB_only_v0 missing under $CANDL_DIR — fix before 'time'"
  # Build the modified CLASS — this repo IS the CLASS tree.
  make clean || true
  make -j"$(nproc)"
  cd python && python setup.py install && cd ..
  python -c "import classy; print('classy OK:', classy.__file__)"
  python -c "import ultranest; print('ultranest OK:', ultranest.__version__)"
  echo "BUILD DONE. Record this commit:"; git -C "$REPO_DIR" rev-parse HEAD
  ;;

verify)
  # Physics gate: identical to scripts/aws_polychord_bootstrap.sh 'verify' so the
  # printed values are directly comparable with the box that ran the booked twins.
  source "$VENV/bin/activate"
  python3 - <<'PY'
import classy, numpy as np, hashlib
c = classy.Class()
c.set({'output':'tCl,pCl,lCl','lensing':'yes','l_max_scalars':2500,
       'omega_b':0.02237,'omega_cdm':0.1200,'h':0.6736,
       'ln10^{10}A_s':3.044,'n_s':0.9649,'tau_reio':0.0544,
       'N_ur':2.0328,'N_ncdm':1,'m_ncdm':0.06,'T_ncdm':0.71611})
c.compute()
cl = c.lensed_cl(2500)['tt'][2:2501]
h = hashlib.sha256(np.round(cl,14).tobytes()).hexdigest()[:16]
print("REFERENCE_TT_HASH", h)
print("cl[100],cl[220],cl[1000] =", cl[98], cl[218], cl[998])
c.struct_cleanup()
PY
  echo "Compare against the same snippet on the box that ran the booked twins."
  echo "If values differ beyond ~1e-10 relative, the builds differ -- STOP."
  ;;

driver)
  cd "$REPO_DIR"
  if [ ! -f "$DRIVER" ]; then
    echo "BLOCKER: $DRIVER is missing. It was never committed to git; recover it from"
    echo "  i-04ead482af737e7bf:/home/ubuntu/prtoe_class/scripts/ultranest_cobaya.py"
    echo "  or /home/themilkmanj/prtoe_class/scripts/ultranest_cobaya.py (see RUNBOOK §2)."
    exit 2
  fi
  got="$(sha256sum "$DRIVER" | awk '{print $1}')"
  if [ "$got" = "$DRIVER_FREEZE_SHA" ]; then
    echo "DRIVER OK: sha256 matches the 2026-08-13 repro freeze."
  else
    echo "DRIVER MISMATCH vs freeze sha256:"
    echo "  freeze: $DRIVER_FREEZE_SHA"
    echo "  got:    $got"
    echo "Only proceed if this exact file is verified to be what the finished LCDM twin ran"
    echo "(compare against the copy on the AWS boxes), else the twins are not comparable."
  fi
  source "$VENV/bin/activate"
  python "$DRIVER" --help || true
  ;;

time)
  # The decisive number: real s/call for the DYAD likelihood on THIS machine.
  source "$VENV/bin/activate"
  cd "$REPO_DIR"
  python3 - <<PY
import time, yaml
from cobaya.model import get_model
info = yaml.safe_load(open("$YAML_HOST"))
info.pop('sampler', None); info.pop('output', None)
model = get_model(info)
pt = model.prior.sample(ignore_external=True)[0]
names = list(model.parameterization.sampled_params())
model.loglike(dict(zip(names, pt)))          # warm-up / caches
ts = []
for i in range(5):
    p = model.prior.sample(ignore_external=True)[0]
    t0 = time.time(); model.loglike(dict(zip(names, p))); ts.append(time.time()-t0)
    print(f"  call {i+1}: {ts[-1]:.2f} s")
avg = sum(ts)/len(ts)
print(f"\nMEAN {avg:.2f} s/call, {len(names)} sampled params")
# Receipts: LCDM twin finished at 2,048,560 calls / 96 ranks. Dyad reached rem 15%
# after ~32k vCPU-h; remaining-from-checkpoint ~18-25k vCPU-h at AWS pace.
for calls, label in ((2.6e6, 'fresh dyad leg (est.)'), (0.9e6, 'resume from rem 15% (est.)')):
    vcpu_h = calls*avg/3600
    print(f"  {label}: ~{calls/1e6:.1f}e6 calls -> {vcpu_h:,.0f} vCPU-h"
          f" | spot c4 @\$0.0255/vCPU-h: \${vcpu_h*0.0255:,.0f}"
          f" | 96 ranks: {vcpu_h/96:,.0f} wall-h")
print("  \$10 credit at 96-vCPU spot (\$2.45/h): ~4.0 wall-h ~= 390 vCPU-h. Do the math above.")
PY
  ;;

launch|resume)
  # Guarded production start. Deliberately refuses to guess the driver CLI:
  # confirm flags via 'driver' stage first, then pass DRIVER_ARGS verbatim.
  : "${CONFIRM:?refusing: set CONFIRM=YES after reading the RUNBOOK budget section}"
  [ "$CONFIRM" = "YES" ] || { echo "refusing: CONFIRM must be YES"; exit 2; }
  : "${MAX_HOURS:?refusing: set MAX_HOURS (in-VM shutdown backstop; size it to the credit)}"
  : "${DRIVER_ARGS:?refusing: set DRIVER_ARGS (exact driver flags; see 'driver' stage --help)}"
  cd "$REPO_DIR"
  [ -f "$DRIVER" ] || { echo "BLOCKER: $DRIVER missing (see 'driver' stage)"; exit 2; }
  if [ "$1" = "resume" ]; then
    [ -f "$OUT_DIR/results/points.hdf5" ] || {
      echo "refusing resume: no checkpoint at $OUT_DIR/results/points.hdf5"; exit 2; }
    case "$DRIVER_ARGS" in *resume*) ;; *)
      echo "refusing resume: DRIVER_ARGS carries no resume flag"; exit 2 ;; esac
  fi
  mkdir -p "$OUT_DIR"
  # Budget backstop: hard power-off even if SSH and mpirun are lost. The primary
  # guard is the VM-level --max-run-duration set at instance creation (RUNBOOK §5.0).
  mins="$(python3 -c "print(max(1, int(float('$MAX_HOURS')*60)))")"
  sudo shutdown -h "+$mins"
  echo "shutdown scheduled in $mins minutes (cancel: sudo shutdown -c)"
  source "$VENV/bin/activate"
  stamp="$(date -u +%Y%m%dT%H%M%SZ)"
  echo "[$stamp] $1 MPI x $NRANKS -> $OUT_DIR" | tee -a "$OUT_DIR/launch.log"
  # shellcheck disable=SC2086
  OMP_NUM_THREADS=1 nohup mpirun $MPIRUN_EXTRA -n "$NRANKS" \
      python "$DRIVER" $DRIVER_ARGS \
      > "$OUT_DIR.run.log" 2>&1 &
  echo "PID $! ; log: $OUT_DIR.run.log"
  ;;

status)
  echo "=== run log tail (health only — NOT quotable, no mid-run logZ bookings) ==="
  tail -5 "$OUT_DIR.run.log" 2>/dev/null || echo "(no run log)"
  echo "=== debug log remainder ==="
  grep -o 'remainder_fraction=[0-9.]*%' "$OUT_DIR/debug.log" 2>/dev/null | tail -3 || echo "(no debug log)"
  echo "=== checkpoint ==="
  ls -la --time-style=full-iso "$OUT_DIR/results/points.hdf5" 2>/dev/null || echo "(no checkpoint yet)"
  uptime; df -h "$HOME" | tail -1
  ;;

peel)
  tar -C "$(dirname "$OUT_DIR")" -czf "$HOME/un_dyad_ev_prod_$(date -u +%Y%m%d).tar.gz" \
      "$(basename "$OUT_DIR")"
  ls -la "$HOME"/un_dyad_ev_prod_*.tar.gz
  echo "Download this, THEN tear down (RUNBOOK §5.3). A stopped VM still bills its disk."
  ;;

*) echo "usage: $0 {build|verify|driver|time|launch|resume|status|peel}"; exit 1 ;;
esac
