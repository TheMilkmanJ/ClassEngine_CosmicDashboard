#!/bin/bash
# Launch the onset-identity evidence rerun (task #23) — QUEUED behind the
# bbnfix production pair; this script REFUSES to start while either is alive.
#
# Environment facts (same stack as resume_bbnfix_chains.sh — the hard-won ones):
#   * system /usr/bin/python3.12 with ~/.local (cobaya 3.6.2, clipy, candl);
#     NOT the conda env.
#   * classy is an egg-link into this repo. If the .so was rebuilt after the
#     bbnfix pair launched, the physics changed — record the mtime in the
#     launchlog (done below) so the provenance is unambiguous.
#   * Run from the repo root; the config's output prefix is repo-relative.
set -e
cd "$(dirname "$0")/.."

for CH in cmp_lcdm_mnu_bbnfix dyad_mnu_bbnfix; do
  if pgrep -f "cobaya.run.*$CH" > /dev/null; then
    echo "REFUSING: $CH is still running — the identity rerun queues behind the pair."
    exit 1
  fi
done
if pgrep -f "cobaya.run.*cmp_prtoe_fixed_zon_identity" > /dev/null; then
  echo "already running"
  exit 0
fi

SO=python/classy.cpython-312-x86_64-linux-gnu.so
{
  echo "== launch $(date -Is) =="
  echo "classy binary mtime: $(stat -c '%y' $SO | cut -c1-19)"
  echo "git HEAD: $(git rev-parse HEAD)"
} >> chains/cmp_prtoe_fixed_zon_identity.launchlog

nohup setsid /usr/bin/python3.12 -m cobaya.run cmp_prtoe_fixed_zon_identity.yaml \
  >> chains/cmp_prtoe_fixed_zon_identity.launchlog 2>&1 &
echo "launched, pid $!"
