#!/bin/bash
# SH0ES-companion evidence pair auto-launcher (armed 2026-07-16, by user order:
# "wait for those MCMCs to finish and then launch polychord").
#
# Waits for the three live MCMC referees (PIDs below, captured at arm time) to ALL exit,
# then runs the evidence pair SEQUENTIALLY — the box is 1 core, so strictly one solo
# PolyChord at a time:
#   1. cmp_prtoe_dyad_ev.yaml   (the sampled-e dyad, the ΔlnZ numerator)
#   2. cmp_lcdm_ev.yaml         (the matched ΛCDM twin, the ΔlnZ denominator)
# The killed run's stale raw dir is moved aside so each starts FRESH (prior phase was
# declared non-resumable). Guards solo: aborts a launch if any other cobaya is alive.
cd /home/themilkmanj/prtoe_class
LOG=chains/evidence_companion.launchlog
PIDS="3305 3306 3307"          # fixed_trgb, routeD, zon_disp (the MCMC referees)
echo "$(date): companion watcher armed, PID $$; waiting on MCMC PIDs [$PIDS]" >> "$LOG"
echo $$ > chains/evidence_companion.pid

# wait until ALL three MCMC referees have exited
while true; do
  alive=0
  for p in $PIDS; do kill -0 "$p" 2>/dev/null && alive=1; done
  [ "$alive" -eq 0 ] && break
  sleep 300
done
echo "$(date): all MCMC referees exited; settling 120s before evidence pair" >> "$LOG"
sleep 120

for Y in cmp_prtoe_dyad_ev.yaml cmp_lcdm_ev.yaml; do
  if pgrep -f cobaya.run > /dev/null; then
    echo "$(date): SKIP $Y — another cobaya is alive; aborting to stay one-PolyChord-solo" >> "$LOG"
    exit 1
  fi
  base="${Y%.yaml}"
  raw="chains/${base}_polychord_raw"
  if [ -d "$raw" ]; then
    mv "$raw" "${raw}.stale.$(date +%s)" 2>/dev/null
    echo "$(date): moved stale raw dir aside for a fresh $base" >> "$LOG"
  fi
  echo "$(date): launching $Y (fresh, forced)" >> "$LOG"
  ./run_cobaya.sh "$Y" -f >> "$LOG" 2>&1
  echo "$(date): $Y exited code $?" >> "$LOG"
  sleep 60
done
echo "$(date): evidence pair complete — ΔlnZ = logZ(dyad_ev) - logZ(lcdm_ev) ready in the .stats files" >> "$LOG"
