#!/bin/bash
# Robust tribunal file watcher — fires on ANY seat activity, not just ### Handoff
FILE="${1:-/home/themilkmanj/prtoe_class/ForGrok&Claude.md}"
LOG="${2:-/home/themilkmanj/prtoe_class/docs/working_logs/_runs/tribunal_monitor.log}"
INTERVAL="${3:-15}"

mkdir -p "$(dirname "$LOG")"
echo "$$" > "${LOG%.log}.pid"
echo "$(date -Iseconds) START tribunal monitor interval=${INTERVAL}s file=$FILE" | tee -a "$LOG"

fingerprint() {
  # mtime + size + count of activity markers + last marker line + WHOSE_TURN
  local f="$1"
  local mt sz
  mt=$(stat -c %Y "$f" 2>/dev/null || echo 0)
  sz=$(stat -c %s "$f" 2>/dev/null || echo 0)
  local n
  n=$(grep -cE '^### (Handoff|TASK COMPLETE|NEXT ISSUE|REFEREE|PROCESS|AUDIT|CHALLENGE|RED |OWNER NOTICE)' "$f" 2>/dev/null || echo 0)
  local last turn
  last=$(grep -E '^### (Handoff|TASK COMPLETE|NEXT ISSUE|REFEREE|PROCESS|AUDIT|CHALLENGE|RED )' "$f" 2>/dev/null | tail -1 | cut -c1-120)
  turn=$(grep -m1 '^\*\*WHOSE_TURN\*\*' "$f" 2>/dev/null | sed 's/.*`\([^`]*\)`.*/\1/' || true)
  # also table form
  if [ -z "$turn" ] || [ "$turn" = "**WHOSE_TURN**" ]; then
    turn=$(grep -m1 '| \*\*WHOSE_TURN\*\*' "$f" 2>/dev/null | sed 's/.*`\([^`]*\)`.*/\1/' || echo "?")
  fi
  printf '%s|%s|%s|%s|%s' "$mt" "$sz" "$n" "$turn" "$last"
}

prev=$(fingerprint "$FILE")
while true; do
  sleep "$INTERVAL"
  [ -f "$FILE" ] || continue
  cur=$(fingerprint "$FILE")
  if [ "$cur" != "$prev" ]; then
    prev=$cur
    mt=${cur%%|*}; rest=${cur#*|}
    sz=${rest%%|*}; rest=${rest#*|}
    n=${rest%%|*}; rest=${rest#*|}
    turn=${rest%%|*}; last=${rest#*|}
    # Classify seat from last marker
    seat="UNKNOWN"
    echo "$last" | grep -qiE 'Claude|Attacker|RED' && seat="Claude"
    echo "$last" | grep -qiE 'ChatGPT|REFEREE' && seat="ChatGPT"
    echo "$last" | grep -qiE 'Grok|Defender' && seat="Grok"
    msg="EVENT seat=$seat turn=$turn markers=$n last=${last:0:100}"
    echo "$(date -Iseconds) $msg" | tee -a "$LOG"
    # stdout lines for Grok monitor tool (must be one of DONE/FAILED/CANCELLED for wake)
    case "$seat" in
      Claude)  echo "DONE Claude activity: $last" ;;
      ChatGPT) echo "DONE ChatGPT activity: $last" ;;
      Grok)    echo "DONE Grok activity: $last" ;;
      *)       echo "DONE tribunal file changed: $last" ;;
    esac
  fi
done
