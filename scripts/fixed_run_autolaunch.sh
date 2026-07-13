#!/bin/bash
# Auto-launch the zero-parameter PolyChord run when the arbiter exits (operator
# order 2026-07-12 night). The launch guard still protects: no sentinel, no launch.
cd /home/themilkmanj/prtoe_class
while kill -0 61302 2>/dev/null; do sleep 120; done
# arbiter gone; wait for the yaml to be sentinel-free (the profile freeze)
until ! grep -q "ZON_FREEZE_PENDING" cmp_prtoe_fixed.yaml; do sleep 60; done
sleep 30  # settle
echo "$(date): arbiter exited; launching the ZERO-PARAMETER run" >> chains/cmp_prtoe_fixed.launchlog
nohup ./run_cobaya.sh cmp_prtoe_fixed.yaml >> chains/cmp_prtoe_fixed.launchlog 2>&1 &
echo "$(date): launched PID $!" >> chains/cmp_prtoe_fixed.launchlog
