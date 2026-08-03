#!/bin/bash
# Resume the two BBN-prior production chains after a stop/reboot (2026-07-26).
#
# CRITICAL environment facts (learned the hard way — see the launchlogs):
#   * These chains run on the SYSTEM python 3.12 stack (~/.local site-packages:
#     cobaya 3.6.2, clipy 0.15, candl 2.2.0) — NOT the prtoe_gold conda env.
#     The conda env carries different cobaya/python versions and cannot resume
#     these checkpoints.
#   * classy is an egg-link into this repo (python/classy.cpython-312-*.so).
#     REBUILDING CLASS MID-RUN CHANGES THE PHYSICS UNDER A FUTURE RESUME.
#     Before resuming, compare the .so mtime against the chain's launch date;
#     if the binary changed since launch, STOP and decide (restart vs accept),
#     do not resume silently.
#   * Launch from chains/ — the output prefix in the recorded inputs is
#     relative to it.
set -e
cd "$(dirname "$0")/../chains"
SO=../python/classy.cpython-312-x86_64-linux-gnu.so
echo "classy binary: $(stat -c '%y' $SO | cut -c1-19)"
for CH in cmp_lcdm_mnu_bbnfix dyad_mnu_bbnfix; do
  if pgrep -f "cobaya.run.*$CH" > /dev/null; then
    echo "$CH: already running"
    continue
  fi
  START=$(head -1 $CH.1.txt 2>/dev/null && stat -c '%y' $CH.1.txt | cut -c1-19 || echo none)
  echo "$CH: resuming (chain file dated: $(stat -c '%y' $CH.1.txt 2>/dev/null | cut -c1-19))"
  nohup setsid /usr/bin/python3.12 -m cobaya.run -r $CH.input.yaml >> $CH.launchlog 2>&1 &
  echo "$CH: pid $!"
done
