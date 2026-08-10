#!/usr/bin/env bash
set -euo pipefail
OMP="${OMP:-5}"
cd /home/ubuntu/prtoe_class/chains
source /home/ubuntu/venv/bin/activate

echo "Stopping MCMCs via pid files /proc scan..."
for f in /home/ubuntu/prtoe_class/dyad_mnu_bbnfix_desidr2.aws.pid /home/ubuntu/prtoe_class/cmp_lcdm_mnu_bbnfix_desidr2.aws.pid; do
  if [ -f "$f" ]; then
    pid=$(cat "$f" || true)
    if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
      echo "killing launcher $pid"
      kill -- -"$pid" 2>/dev/null || kill "$pid" 2>/dev/null || true
    fi
  fi
done
for pid in /proc/[0-9]*; do
  p=${pid#/proc/}
  cmd=$(tr '\0' ' ' < "$pid/cmdline" 2>/dev/null || true)
  case "$cmd" in
    *desidr2*)
      case "$cmd" in
        *python*|*prterun*|*mpirun*)
          echo "kill $p"
          kill "$p" 2>/dev/null || true
          ;;
      esac
      ;;
  esac
done
sleep 12
for pid in /proc/[0-9]*; do
  p=${pid#/proc/}
  cmd=$(tr '\0' ' ' < "$pid/cmdline" 2>/dev/null || true)
  case "$cmd" in
    *desidr2*)
      case "$cmd" in
        *python*|*prterun*|*mpirun*) kill -9 "$p" 2>/dev/null || true ;;
      esac
      ;;
  esac
done
sleep 3
echo stopped

export OMP_NUM_THREADS="$OMP"
for CH in dyad_mnu_bbnfix_desidr2 cmp_lcdm_mnu_bbnfix_desidr2; do
  echo "== OMP boost resume $(date -Is) OMP=$OMP ranks=3 ==" >> "${CH}.launchlog"
  nohup mpirun --use-hwthread-cpus -n 3 --bind-to none \
    python -m cobaya.run -r "${CH}.input.yaml" \
    >> "${CH}.launchlog" 2>&1 &
  echo $! > "/home/ubuntu/prtoe_class/${CH}.aws.pid"
  echo "$CH resumed pid=$(cat /home/ubuntu/prtoe_class/${CH}.aws.pid)"
  sleep 2
done
echo "done OMP=$OMP"
