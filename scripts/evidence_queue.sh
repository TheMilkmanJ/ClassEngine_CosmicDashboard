#!/bin/bash
# The evidence-trio queue (task #25, 2026-07-13). Watches the live PRTOE-TRGB
# PolyChord run (PIDs recorded below at creation time) and, when it exits,
# runs the declared follow-ups SEQUENTIALLY — the box stays one-PolyChord-solo:
#   1. cmp_lcdm_trgb.yaml          (the ΛCDM-TRGB twin — the tier-3 pair completes)
#   2. cmp_prtoe_fixed_noshoes.yaml (the anchor-free headline, PRTOE side)
#   3. cmp_lcdm_noshoes.yaml       (the anchor-free headline, ΛCDM side)
# The SH0ES companion pair (cmp_prtoe_dyad_ev / cmp_lcdm_ev) is NOT auto-queued:
# author's launch call, per the standing order that paused it.
cd /home/themilkmanj/prtoe_class
LOG=chains/evidence_queue.launchlog
echo "$(date): queue watcher started, PID $$; watching 464355/464357" >> "$LOG"
echo $$ > chains/evidence_queue.pid

while kill -0 464355 2>/dev/null || kill -0 464357 2>/dev/null; do sleep 180; done
echo "$(date): PRTOE-TRGB run exited; queue begins after settle" >> "$LOG"
sleep 60

for Y in cmp_lcdm_trgb.yaml cmp_prtoe_fixed_noshoes.yaml cmp_lcdm_noshoes.yaml; do
  if pgrep -f cobaya.run > /dev/null; then
    echo "$(date): SKIP $Y — another cobaya is alive (manual run?); queue aborts to stay solo" >> "$LOG"
    exit 1
  fi
  echo "$(date): launching $Y" >> "$LOG"
  ./run_cobaya.sh "$Y" >> "$LOG" 2>&1
  echo "$(date): $Y exited with code $?" >> "$LOG"
  sleep 60
done
echo "$(date): queue complete — trio tiers done; SH0ES companion awaits the author's order" >> "$LOG"
