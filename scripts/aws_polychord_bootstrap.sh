#!/usr/bin/env bash
# AWS bootstrap for the dyad PolyChord evidence run.
#
# Stage 1 (cheap instance): build, verify the build matches local physics,
#                           and MEASURE the per-likelihood-call time.
# Stage 2 (big instance):   only after stage 1 gives a number you can afford.
#
# Usage on a fresh Ubuntu 24.04 instance:
#   bash aws_polychord_bootstrap.sh build     # ~20 min
#   bash aws_polychord_bootstrap.sh verify    # must match the local reference
#   bash aws_polychord_bootstrap.sh time      # prints seconds per likelihood call
#
set -euo pipefail
REPO_DIR="${REPO_DIR:-$HOME/prtoe_class}"
PKG_DIR="${PKG_DIR:-$HOME/cobaya_packages_clean}"
CANDL_DIR="${CANDL_DIR:-$HOME/candl_data}"

case "${1:-}" in

build)
  sudo apt-get update -qq
  sudo apt-get install -y -qq build-essential gfortran python3-dev python3-pip \
       python3-venv libopenmpi-dev openmpi-bin git cmake wget unzip
  python3 -m venv "$HOME/venv" && source "$HOME/venv/bin/activate"
  pip install -q --upgrade pip wheel
  pip install -q numpy scipy cython mpi4py "cobaya>=3.5" getdist candl-like
  # PolyChord (Lite) AND the full likelihood stack (Planck clik, Pantheon+, DESI).
  # ~2.5 GB, downloaded on the AWS side at AWS bandwidth -- do not upload it.
  cobaya-install polychord --packages-path "$PKG_DIR"
  cobaya-install "$REPO_DIR/cmp_prtoe_dyad_ev.yaml" --packages-path "$PKG_DIR" --skip-global
  # candl data (ACT DR6 + SPT3G) is NOT in cobaya's index -- it must already be
  # at $CANDL_DIR. If absent, the two candl likelihoods will fail to load.
  [ -d "$CANDL_DIR" ] || echo "WARNING: $CANDL_DIR missing -- upload it (325 MB) before 'time'"
  # Build the modified CLASS -- this repo IS the CLASS tree
  cd "$REPO_DIR" && make clean || true
  make -j"$(nproc)"
  cd python && python setup.py install && cd ..
  python -c "import classy; print('classy OK:', classy.__file__)"
  echo "BUILD DONE. Record this commit:"; git -C "$REPO_DIR" rev-parse HEAD
  ;;

verify)
  # The physics must match the local Jul-23 build, or the evidence is not
  # comparable to anything already computed. Compare one reference spectrum.
  source "$HOME/venv/bin/activate"
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
  echo "Compare the three cl values against the same script run on the local box."
  echo "If they differ beyond ~1e-10 relative, the builds differ -- STOP."
  ;;

time)
  # The decisive number. Times full likelihood calls at the run's real settings.
  source "$HOME/venv/bin/activate"
  cd "$REPO_DIR"
  python3 - <<'PY'
import time, yaml
from cobaya.model import get_model
info = yaml.safe_load(open('cmp_prtoe_dyad_ev.yaml'))
info.pop('sampler', None); info.pop('output', None)
model = get_model(info)
pt = model.prior.sample(ignore_external=True)[0]
names = list(model.parameterization.sampled_params())
model.loglike(dict(zip(names, pt)))          # warm-up / JIT / caches
ts = []
for i in range(5):
    p = model.prior.sample(ignore_external=True)[0]
    t0 = time.time(); model.loglike(dict(zip(names, p))); ts.append(time.time()-t0)
    print(f"  call {i+1}: {ts[-1]:.2f} s")
avg = sum(ts)/len(ts)
print(f"\nMEAN {avg:.2f} s/call over {len(names)} sampled params")
# PolyChord cost model: nlive * num_repeats * D_KL * ~3.5 slice calls
for dkl in (25, 35, 50):
    n = 250*28*dkl*3.5
    ch = n*avg/3600
    print(f"  D_KL={dkl}: ~{n/1e6:.1f}e6 calls -> {ch:,.0f} core-hr"
          f" | 96 vCPU: {ch/96:,.0f} wall-hr"
          f" | spot@$1.40: ${ch/96*1.40:,.0f} | on-demand@$4.28: ${ch/96*4.28:,.0f}")
PY
  ;;

*) echo "usage: $0 {build|verify|time}"; exit 1 ;;
esac
