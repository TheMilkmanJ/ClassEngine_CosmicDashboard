#!/bin/bash
# Fairbank chain watchdog: logs stalls/death; never auto-restarts (diagnose first).
PID=2827749
LOG=/home/themilkmanj/prtoe_class/chains/dyad_mnu_watchdog.log
LL=/home/themilkmanj/prtoe_class/chains/dyad_mnu_mcmc.launchlog
while true; do
  TS=$(date '+%F %T')
  if ! ps -p $PID > /dev/null 2>&1; then
    echo "$TS ALERT: chain PID $PID is DEAD. Last log line: $(tail -1 $LL)" >> $LOG
    break
  fi
  AGE=$(( $(date +%s) - $(stat -c %Y $LL) ))
  if [ $AGE -gt 1800 ]; then
    echo "$TS ALERT: launchlog stale ${AGE}s (>30min) — possible stall. $(tail -1 $LL)" >> $LOG
  else
    echo "$TS ok (log age ${AGE}s): $(tail -1 $LL | cut -c1-90)" >> $LOG
  fi
  sleep 900
done
