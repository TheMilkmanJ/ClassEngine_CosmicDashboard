#!/bin/bash
# quick status of the pc_prtoe evidence run
cd /home/themilkmanj/prtoe_class
if pgrep -f "cobaya.run pc_prtoe" >/dev/null 2>&1; then
  echo "RUNNING  (etime $(ps -o etime= -p $(pgrep -f 'cobaya.run pc_prtoe') | tr -d ' '))"
  grep -oE "ncluster:[0-9]+|nlike:[0-9]+|log\(Z\) = [-0-9.]+ \+/- [0-9.]+" chains/pc_prtoe.launchlog 2>/dev/null | tail -3
  ls -t chains/pc_prtoe_polychord_raw/*.stats 2>/dev/null | head -1 | xargs -r grep -iE "log\(Z\)|nlike" 2>/dev/null | head -2
else
  echo "NOT RUNNING — finished or stopped"
  if grep -qiE "traceback|exception|Error:" chains/pc_prtoe.launchlog 2>/dev/null; then echo "  -> CRASHED:"; grep -iE "traceback|exception|Error:" chains/pc_prtoe.launchlog | tail -3
  else echo "  -> completed; evidence:"; grep -iE "log\(Z\)|Bayes" chains/pc_prtoe.launchlog 2>/dev/null | tail -3; ls chains/pc_prtoe_polychord_raw/*.stats 2>/dev/null | head -1 | xargs -r grep -iE "log\(Z\)" 2>/dev/null; fi
fi
