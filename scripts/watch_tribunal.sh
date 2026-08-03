#!/bin/bash
# Tribunal address-aware watcher.
# Routes events by @TO: / >> codes so seats only wake for mail addressed to them.
#
# Usage:
#   watch_tribunal.sh [FILE] [LOG] [INTERVAL] [FILTER]
# FILTER (optional): GROK | CLAUDE | CHATGPT | ALL
#   GROK     — only emit DONE for @TO:GROK / >>BLUE / >>ALL / WHOSE_TURN Grok
#   CLAUDE   — only @TO:CLAUDE / >>RED / >>ALL / WHOSE_TURN Claude
#   CHATGPT  — only @TO:CHATGPT / >>REF / >>ALL / WHOSE_TURN ChatGPT
#   ALL      — emit every change (default)
#
# Address codes (must appear on the ### heading line preferred):
#   @FROM:GROK|CLAUDE|CHATGPT|OWNER
#   @TO:GROK|CLAUDE|CHATGPT|ALL|OWNER
#   Short: >>BLUE (to Grok)  >>RED (to Claude)  >>REF (to ChatGPT)  >>ALL
#
# See ForGrok&Claude.md § Address codes.

FILE="${1:-/home/themilkmanj/prtoe_class/ForGrok&Claude.md}"
LOG="${2:-/home/themilkmanj/prtoe_class/docs/working_logs/_runs/tribunal_monitor.log}"
INTERVAL="${3:-12}"
FILTER="${4:-ALL}"

mkdir -p "$(dirname "$LOG")"
echo "$$" > "${LOG%.log}.pid"
echo "$(date -Iseconds) START tribunal monitor interval=${INTERVAL}s filter=${FILTER} file=$FILE" >>"$LOG"
# one DONE so the tool knows the watcher is alive (not a tribunal mail)
echo "DONE monitor_started filter=${FILTER}"

last_activity_line() {
  grep -E '^### ' "$1" 2>/dev/null | tail -1 | cut -c1-160
}

last_relevant_line() {
  local file="$1"
  local wanted="$2"
  local line to last=""
  while IFS= read -r line; do
    to=$(parse_to "$line")
    case "$wanted" in
      ALL)
        last="$line"
        ;;
      GROK)
        if [ "$to" = "GROK" ] || [ "$to" = "ALL" ]; then last="$line"; fi
        ;;
      CLAUDE)
        if [ "$to" = "CLAUDE" ] || [ "$to" = "ALL" ]; then last="$line"; fi
        ;;
      CHATGPT)
        if [ "$to" = "CHATGPT" ] || [ "$to" = "ALL" ] || [ "$to" = "REF_UNADDRESSED" ]; then last="$line"; fi
        ;;
    esac
  done < <(grep -E '^### ' "$file" 2>/dev/null)
  printf '%s' "${last:0:160}"
}

last_exact_line() {
  local file="$1"
  local wanted="$2"
  local pattern=""
  case "$wanted" in
    GROK) pattern='@TO:GROK|>>BLUE' ;;
    CLAUDE) pattern='@TO:CLAUDE|>>RED' ;;
    CHATGPT) pattern='@TO:CHATGPT|>>REF' ;;
    OWNER) pattern='@TO:OWNER' ;;
    *) pattern='' ;;
  esac
  if [ -z "$pattern" ]; then
    return 0
  fi
  grep -E '^### ' "$file" 2>/dev/null | grep -E "$pattern" | tail -1 | cut -c1-160
}

count_markers() {
  grep -cE '^### ' "$1" 2>/dev/null || echo 0
}

whose_turn() {
  local t
  t=$(grep -m1 '| \*\*WHOSE_TURN\*\*' "$1" 2>/dev/null | sed -n 's/.*`\([^`]*\)`.*/\1/p')
  # strip trailing notes after space inside backticks content already captured
  echo "${t%% *}"
}

# Parse TO address from a heading line
parse_to() {
  local line="$1"
  if echo "$line" | grep -qE '@TO:ALL|>>ALL'; then echo ALL; return; fi
  if echo "$line" | grep -qE '@TO:GROK|>>BLUE'; then echo GROK; return; fi
  if echo "$line" | grep -qE '@TO:CLAUDE|>>RED'; then echo CLAUDE; return; fi
  if echo "$line" | grep -qE '@TO:CHATGPT|>>REF'; then echo CHATGPT; return; fi
  if echo "$line" | grep -qE '@TO:OWNER'; then echo OWNER; return; fi
  # Infer from block type if no explicit TO
  if echo "$line" | grep -qiE 'NEXT ISSUE|CHALLENGE|AUDIT|PROCESS FLAG|RED TASK|RED OBJECTION'; then
    # Red posts usually go to Grok (build) or ChatGPT (after next issue)
    if echo "$line" | grep -qiE 'NEXT ISSUE'; then echo CHATGPT; return; fi
    if echo "$line" | grep -qiE 'AUDIT|CHALLENGE'; then echo GROK; return; fi
    echo ALL; return
  fi
  if echo "$line" | grep -qiE 'REFEREE'; then
    # Ambiguous without @TO — flag as REF_UNADDRESSED
    echo REF_UNADDRESSED; return
  fi
  if echo "$line" | grep -qiE 'TASK COMPLETE|Grok/Defender|Agent: Grok'; then
    echo CLAUDE; return  # completer → red by default
  fi
  echo UNKNOWN
}

parse_from() {
  local line="$1"
  if echo "$line" | grep -qE '@FROM:GROK|Agent: Grok|Grok/Defender'; then echo GROK; return; fi
  if echo "$line" | grep -qE '@FROM:CLAUDE|Agent: Claude|Claude/Attacker|RED\)|red only'; then echo CLAUDE; return; fi
  if echo "$line" | grep -qE '@FROM:CHATGPT|Agent: ChatGPT'; then echo CHATGPT; return; fi
  if echo "$line" | grep -qiE 'Claude|Attacker'; then echo CLAUDE; return; fi
  if echo "$line" | grep -qiE 'ChatGPT|REFEREE'; then echo CHATGPT; return; fi
  if echo "$line" | grep -qiE 'Grok|Defender'; then echo GROK; return; fi
  echo UNKNOWN
}

emit_stdout() {
  local text="$1"
  echo "$text"
  echo "$(date -Iseconds) $text" >>"$LOG"
}

should_emit() {
  local to="$1"
  case "$FILTER" in
    ALL) return 0 ;;
    GROK)
      [ "$to" = "GROK" ] || [ "$to" = "ALL" ] && return 0
      return 1
      ;;
    CLAUDE)
      [ "$to" = "CLAUDE" ] || [ "$to" = "ALL" ] && return 0
      return 1
      ;;
    CHATGPT)
      [ "$to" = "CHATGPT" ] || [ "$to" = "ALL" ] || [ "$to" = "REF_UNADDRESSED" ] && return 0
      return 1
      ;;
    *) return 0 ;;
  esac
}

fingerprint() {
  local f="$1"
  local mt sz n last turn
  mt=$(stat -c %Y "$f" 2>/dev/null || echo 0)
  sz=$(stat -c %s "$f" 2>/dev/null || echo 0)
  n=$(count_markers "$f")
  last=$(last_activity_line "$f")
  turn=$(whose_turn "$f")
  printf '%s|%s|%s|%s|%s' "$mt" "$sz" "$n" "$turn" "$last"
}

prev=$(fingerprint "$FILE")
# Startup snapshot so a late-starting watcher still notices existing referee mail / turn state.
startup_turn=$(whose_turn "$FILE")
startup_last=$(last_relevant_line "$FILE" "$FILTER")
startup_exact=$(last_exact_line "$FILE" "$FILTER")
if [ "$FILTER" != "ALL" ] && [ "$startup_turn" = "$FILTER" ]; then
  emit_stdout "DONE TURN_${FILTER} current_board: ${startup_last:-$(last_activity_line "$FILE")}"
elif [ -n "$startup_exact" ]; then
  emit_stdout "DONE EXACT_${FILTER} current_mail: $startup_exact"
elif [ -n "$startup_last" ]; then
  emit_stdout "DONE SNAPSHOT_${FILTER} current_mail: $startup_last"
fi
while true; do
  sleep "$INTERVAL"
  [ -f "$FILE" ] || continue
  cur=$(fingerprint "$FILE")
  if [ "$cur" = "$prev" ]; then
    continue
  fi
  prev=$cur
  turn=$(whose_turn "$FILE")
  last=$(last_activity_line "$FILE")
  to=$(parse_to "$last")
  from=$(parse_from "$last")
  n=$(count_markers "$FILE")

  msg="EVENT from=$from to=$to turn=$turn markers=$n last=${last:0:120}"
  # Log-only (never stdout) — Grok monitor tool wakes on every stdout line
  echo "$(date -Iseconds) $msg" >>"$LOG"

  if [ "$FILTER" != "ALL" ] && [ "$turn" = "$FILTER" ]; then
    emit_stdout "DONE TURN_${FILTER} from=$from: $last"
    continue
  fi

  if ! should_emit "$to"; then
    echo "$(date -Iseconds) SKIP filter=$FILTER (mail for $to)" >>"$LOG"
    continue
  fi

  # ONLY DONE/FAILED/CANCELLED lines go to stdout (wake filter)
  case "$to" in
    GROK)
      emit_stdout "DONE TO_GROK from=$from: $last"
      ;;
    CLAUDE)
      emit_stdout "DONE TO_CLAUDE from=$from: $last"
      ;;
    CHATGPT)
      emit_stdout "DONE TO_REF from=$from: $last"
      ;;
    ALL)
      # Broadcast wakes every filter that includes ALL
      emit_stdout "DONE TO_ALL from=$from: $last"
      ;;
    REF_UNADDRESSED)
      emit_stdout "DONE REF_NEEDS_TO_TAG from=$from: $last"
      ;;
    *)
      emit_stdout "DONE tribunal change from=$from to=$to: $last"
      ;;
  esac
done
