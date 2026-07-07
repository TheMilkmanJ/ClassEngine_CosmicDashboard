#!/bin/bash
# PolyChord stall watchdog: if a run's dead-points file stops growing for
# 20 min while that run is alive, capture py-spy stacks of every rank so we
# see exactly where it hangs (CLASS module, MPI collective, likelihood, ...).
# Tracks dcdf_pc_v1 and lcdm_pc_v1 independently (they can be concurrent).
LOG=/home/themilkmanj/prtoe_class/chains/pc_watchdog.log
declare -A last_size stall
for r in dcdf_pc_v1 lcdm_pc_v1; do last_size[$r]=0; stall[$r]=0; done
while true; do
  sleep 300
  for run in dcdf_pc_v1 lcdm_pc_v1; do
    pids=$(pgrep -f "cobaya run.*${run}.yaml" | head -8)
    [ -z "$pids" ] && continue
    dead=$(find /home/themilkmanj/prtoe_class/chains -name "*${run}*dead*.txt" \
           -newer "/home/themilkmanj/prtoe_class/${run}.yaml" 2>/dev/null | head -1)
    size=$(wc -c < "$dead" 2>/dev/null || echo 0)
    if [ "$size" -gt "${last_size[$run]}" ]; then
      last_size[$run]=$size; stall[$run]=0
    else
      stall[$run]=$((stall[$run]+300))
      if [ "${stall[$run]}" -ge 1200 ]; then
        echo "$(date) STALL DETECTED [$run] (no dead-point growth ${stall[$run]}s). Capturing stacks:" >> $LOG
        for p in $pids; do
          echo "--- [$run] rank pid $p ---" >> $LOG
          /home/themilkmanj/miniconda3/envs/prtoe_gold/bin/py-spy dump --pid "$p" >> $LOG 2>&1
        done
        echo "STALL $run" # event line for the monitor
        stall[$run]=0
      fi
    fi
  done
done
