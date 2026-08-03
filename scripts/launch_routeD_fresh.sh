#!/bin/bash
# launch_routeD_fresh — board #21's chain, relaunched clean (2026-07-27).
#
# WHY FRESH AND NOT RESUME: the stalled run's checkpoint is from 2026-07-20;
# per the chain-ops rule (classy rebuilds change physics under resumes), a
# checkpoint that old is not trusted across environment drift. The existing
# covmat seeds the proposal, so the burn-in cost of a fresh start is small.
#
# GUARDS (all three must pass):
#   1. the bbnfix pair may still be running (the cap is 3 MCMCs) BUT
#   2. the two heavy GPE runs must be FINISHED (the box saturates at load ~8
#      with them alive — a third chain would slow the pair the letter gates on)
#   3. 1-minute load must be under 6.5
set -euo pipefail
cd "$(dirname "$0")/../chains"

if pgrep -f "bounce_m6_rebound_dst|ring_toroidal_3d" >/dev/null; then
    echo "REFUSED: the heavy GPE runs are still alive — the box has no free core."
    echo "         Re-run when they finish (they auto-notify / are bounded)."
    exit 1
fi
LOAD=$(awk '{print $1}' /proc/loadavg)
if awk "BEGIN{exit !($LOAD > 6.5)}"; then
    echo "REFUSED: load $LOAD > 6.5 — wait for capacity."
    exit 1
fi

STAMP=$(date +%Y%m%d_%H%M)
ARCH="_archive_routeD_stalled0720_${STAMP}"
mkdir -p "$ARCH"
for f in cmp_prtoe_routeD.progress cmp_prtoe_routeD.checkpoint \
         cmp_prtoe_routeD.1.txt cmp_prtoe_routeD.updated.yaml \
         cmp_prtoe_routeD.launchlog; do
    [ -f "$f" ] && mv "$f" "$ARCH/" || true
done
echo "stalled products archived to chains/$ARCH (covmat kept in place as seed)"

nohup /usr/bin/python3.12 -m cobaya.run cmp_prtoe_routeD.input.yaml \
    > cmp_prtoe_routeD.launchlog 2>&1 &
echo "cmp_prtoe_routeD launched fresh (PID $!) — the third and last MCMC slot."
echo "Adjudicates P-2026-056 (thaw vs constitution) jointly with DESI DR3."
