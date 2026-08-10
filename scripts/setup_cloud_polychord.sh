#!/bin/bash
# =====================================================================================
# Cloud-VM setup for the UNSEEDED PolyChord evidence run: PRTOE vs LCDM (Delta lnZ)
# Run STAGE BY STAGE. Do NOT launch the multi-day run until STAGE 6 (--test) passes clean.
# Repo is PUBLIC -> https clone needs no auth. Pipeline runs on python3.12 (classy.so is a 312 build).
#
# !! KNOWN GAPS that must be resolved locally BEFORE this runs clean (see TODOs): !!
#    - clipy (Planck likelihood) and candl are NOT pip-tracked in the source env -- their exact
#      install method is undocumented. Nail this down locally first, or the run can't load Planck/ACT/SPT.
#    - data_set_file paths in the configs point at local dirs; repoint them on the VM.
# =====================================================================================
set -e
PY=python3.12

# --- STAGE 1: system deps + python3.12 ---
sudo apt-get update
sudo apt-get install -y build-essential gfortran libopenmpi-dev openmpi-bin \
    python3.12 python3.12-dev python3-pip git wget curl libgsl-dev libfftw3-dev
$PY -m pip install --upgrade pip

# --- STAGE 2: clone repo (PUBLIC, no auth needed) ---
git clone -b coderabbit-review-2 https://github.com/TheMilkmanJ/ClassEngine_CosmicDashboard.git prtoe
cd prtoe

# --- STAGE 3: python packages ---
$PY -m pip install cobaya==3.6.2 numpy scipy pyyaml pypolychord
# TODO(clipy): reproduce clipy install (source env has it in ~/.local/lib/python3.12; method undocumented)
# TODO(candl):  $PY -m pip install candl-like   # VERIFY package name + version against source env

# --- STAGE 4: compile the modified CLASS for python3.12 ---
( cd class && make -j"$(nproc)" )
( cd python && $PY setup.py install )

# --- STAGE 5: data ---
cobaya-install planck_2018_lowl.TT planck_2018_lowl.EE planck_2018_highl_plik.TTTEEE_lite \
  planck_2018_lensing.clik bao.sixdf_2011_bao bao.sdss_dr7_mgs bao.sdss_dr12_consensus_final \
  sn.pantheonplusshoes --packages-path "$HOME/cobaya_packages_clean"
# TODO(candl data): fetch ACT DR6 + SPT3G (~325MB) from https://github.com/Lbalkenhol/candl_data
#   to $HOME/candl_data, then fix the data_set_file paths in pc_prtoe.yaml / pc_lcdm.yaml.

# --- STAGE 6: MANDATORY --test (must pass before the multi-day run) ---
PYTHONPATH="$HOME/prtoe/python" cobaya-run pc_prtoe.yaml --test

# --- STAGE 7: launch UNSEEDED PolyChord with MPI (~2-3 days on 32 cores) ---
NC="$(nproc)"
PYTHONPATH="$HOME/prtoe/python" mpirun -np "$NC" cobaya-run pc_prtoe.yaml
PYTHONPATH="$HOME/prtoe/python" mpirun -np "$NC" cobaya-run pc_lcdm.yaml
# Delta lnZ = log(Z) from chains/pc_prtoe.stats  minus  chains/pc_lcdm.stats
