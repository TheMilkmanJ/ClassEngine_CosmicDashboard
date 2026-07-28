#!/bin/bash
# Relaunch the bbnfix pair under real MPI, pinned so the desktop stays responsive.
#
# WHY (2026-07-28): the pair was running as two SERIAL processes. `nproc` reported 1,
# which was read as a one-core box; it is not — `nproc` honours OMP_NUM_THREADS, set to
# 1 here. The machine is an i7-9850H, 6 cores / 12 threads, and ~9 threads were idle
# beside the chains. Single-chain also meant R−1 was a within-chain split statistic
# rather than the between-chain Gelman–Rubin the 0.05 target assumes.
#
# WHAT THIS CHANGES: 3 MPI ranks per chain. Samples accumulate 3x faster AND R−1 becomes
# a genuine between-chain statistic.
#
# DESKTOP HEADROOM (the operator's constraint — "leave enough to watch TV"):
#   * all six ranks are pinned to CPUs 0-7, so CPUs 8-11 (two physical cores) are never
#     touched by this work;
#   * every rank runs at nice +10, so anything interactive preempts it;
#   * OMP_NUM_THREADS stays 1 — ranks x OMP must not exceed the pinned set.
#
# SAFETY (the standing chain-ops hazards):
#   * system /usr/bin/python3.12, NOT conda — cobaya 3.6.2, clipy, candl, mpi4py 4.1.2;
#   * /usr/bin/mpirun (Open MPI 4.1.6), NOT the conda one on PATH;
#   * classy .so mtime is recorded below. It was 2026-07-23 20:00, older than the
#     2026-07-26 restart, so resuming does not splice physics. VERIFY THIS AGAIN before
#     any future resume.
set -e
cd "$(dirname "$0")/../chains"

PIN="0-7"
RANKS=3
SO=../python/classy.cpython-312-x86_64-linux-gnu.so

for CH in cmp_lcdm_mnu_bbnfix dyad_mnu_bbnfix; do
  if pgrep -f "cobaya.run.*$CH" > /dev/null; then
    echo "stopping serial $CH ..."
    pkill -f "cobaya.run.*$CH" || true
  fi
done
sleep 5

for CH in cmp_lcdm_mnu_bbnfix dyad_mnu_bbnfix; do
  {
    echo "== MPI relaunch $(date -Is) =="
    echo "ranks: $RANKS   pinned to CPUs: $PIN   nice: +10   OMP_NUM_THREADS=1"
    echo "classy .so mtime: $(stat -c '%y' $SO | cut -c1-19)"
    echo "git HEAD: $(git rev-parse HEAD)"
    echo "pre-MPI samples preserved in the _snapshot_pre_mpi_* directory beside this file"
  } >> $CH.launchlog

  OMP_NUM_THREADS=1 nohup setsid taskset -c $PIN nice -n 10 \
    /usr/bin/mpirun -n $RANKS --oversubscribe --bind-to none \
    /usr/bin/python3.12 -m cobaya.run $CH.input.yaml -r \
    >> $CH.launchlog 2>&1 &
  echo "$CH launched under $RANKS ranks, pid $!"
  sleep 3
done

echo
echo "CPUs 8-11 left free. Verify with:  ps -eo pid,psr,comm | grep python"
