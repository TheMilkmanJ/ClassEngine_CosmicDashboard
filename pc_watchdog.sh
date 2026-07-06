#!/bin/bash
# PolyChord stall watchdog: if the dead-points file stops growing for 20 min
# while a polychord run is alive, capture py-spy stacks of every rank so we
# see exactly where it hangs (CLASS module, MPI collective, likelihood, ...).
LOG=/home/themilkmanj/prtoe_class/chains/pc_watchdog.log
last_size=0; stall=0
while true; do
  sleep 300
  pids=$(pgrep -f "cobaya run.*_pc_v1.yaml" | head -8)
  [ -z "$pids" ] && continue
  dead=$(find /home/themilkmanj/prtoe_class/chains -name "*_pc_v1*dead*.txt" -newer /home/themilkmanj/prtoe_class/dcdf_pc_v1.yaml 2>/dev/null | head -1)
  size=$(wc -c < "$dead" 2>/dev/null || echo 0)
  if [ "$size" -gt "$last_size" ]; then
    last_size=$size; stall=0
  else
    stall=$((stall+300))
    if [ "$stall" -ge 1200 ]; then
      echo "$(date) STALL DETECTED (no dead-point growth ${stall}s). Capturing stacks:" >> $LOG
      for p in $pids; do
        echo "--- rank pid $p ---" >> $LOG
        /home/themilkmanj/miniconda3/envs/prtoe_gold/bin/py-spy dump --pid "$p" >> $LOG 2>&1
      done
      echo "STALL" # event line for the monitor
      stall=0
    fi
  fi
done
