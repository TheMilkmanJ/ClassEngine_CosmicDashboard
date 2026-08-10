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
STATE="${LOG%.log}.state"
REMINDER_EVERY=5

mkdir -p "$(dirname "$LOG")"
echo "$$" > "${LOG%.log}.pid"
echo "$(date -Iseconds) START tribunal monitor interval=${INTERVAL}s filter=${FILTER} file=$FILE" >>"$LOG"
# one DONE so the tool knows the watcher is alive (not a tribunal mail)
echo "DONE monitor_started filter=${FILTER}"

heading_stream() {
  local file="$1"
  grep -E '^### ' "$file" 2>/dev/null | grep -E '@FROM:|@TO:|>>'
}

last_activity_line() {
  heading_stream "$1" | tail -1 | cut -c1-160
}

last_relevant_line() {
  local file="$1"
  local wanted="$2"
  local line to
  while IFS= read -r line; do
    case "$line" in
      '### '*)
        to=$(parse_to "$line")
        if matches_filter_target "$wanted" "$to"; then
          printf '%s' "${line:0:160}"
          return
        fi
        ;;
    esac
  done < <(tac "$file" 2>/dev/null | grep -E '^### ' | grep -E '@FROM:|@TO:|>>')
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
  heading_stream "$file" | grep -E "$pattern" | tail -1 | cut -c1-160
}

count_markers() {
  local file="$1"
  local count
  [ -f "$file" ] || { echo 0; return; }
  count=$(heading_stream "$file" | wc -l | tr -d ' ')
  printf '%s\n' "${count:-0}"
}

whose_turn() {
  local line tail seat
  while IFS= read -r line; do
    tail="$line"
    if [[ "$tail" == *"WHOSE_TURN"* ]]; then
      tail="${tail#*WHOSE_TURN}"
    fi
    if [[ "$tail" == *"→"* ]]; then
      tail="${tail#*→}"
    elif [[ "$tail" == *":"* ]]; then
      tail="${tail#*:}"
    fi
    seat=$(printf '%s\n' "$tail" | grep -oE 'ChatGPT|Claude|Grok' | head -1)
    case "$seat" in
      ChatGPT) echo CHATGPT; return ;;
      Claude) echo CLAUDE; return ;;
      Grok) echo GROK; return ;;
    esac
  done < <(grep -E '\*\*WHOSE_TURN' "$1" 2>/dev/null | tac)
  echo ""
}

# Parse TO address(es) from a heading line.
# Returns a comma-separated list like GROK,CHATGPT or ALL.
parse_to() {
  local line="$1"
  local targets=()
  if echo "$line" | grep -qE '@TO:ALL|>>ALL'; then echo ALL; return; fi
  if echo "$line" | grep -qE '@TO:GROK|>>BLUE'; then targets+=("GROK"); fi
  if echo "$line" | grep -qE '@TO:CLAUDE|>>RED'; then targets+=("CLAUDE"); fi
  if echo "$line" | grep -qE '@TO:CHATGPT|>>REF'; then targets+=("CHATGPT"); fi
  if echo "$line" | grep -qE '@TO:OWNER'; then targets+=("OWNER"); fi
  if [ "${#targets[@]}" -gt 0 ]; then
    local joined=""
    local item
    for item in "${targets[@]}"; do
      if [ -n "$joined" ]; then
        joined="${joined},${item}"
      else
        joined="$item"
      fi
    done
    echo "$joined"
    return
  fi
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

target_list_has() {
  local list="$1"
  local target="$2"
  case ",$list," in
    *,"$target",*) return 0 ;;
    *) return 1 ;;
  esac
}

matches_filter_target() {
  local filter="$1"
  local to="$2"
  case "$filter" in
    ALL) return 0 ;;
    GROK)
      target_list_has "$to" "ALL" || target_list_has "$to" "GROK"
      return
      ;;
    CLAUDE)
      target_list_has "$to" "ALL" || target_list_has "$to" "CLAUDE"
      return
      ;;
    CHATGPT)
      target_list_has "$to" "ALL" || target_list_has "$to" "CHATGPT" || target_list_has "$to" "REF_UNADDRESSED"
      return
      ;;
    *)
      return 0
      ;;
  esac
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

extract_packet() {
  local line="$1"
  local left right packet
  left="$line"
  left="${left#\#\#\# }"
  left="${left%% @FROM:*}"
  left=$(printf '%s\n' "$left" | sed -E 's/^(TASK OPEN|TASK COMPLETE|RED VERDICT|RED VERIFY \+ CLOSE|RED VERIFY|RED BATCH VERDICT|REFEREE PROCESS DIRECTIVE|REFEREE PROCESS|REFEREE|THREE-SEAT \/ WORKLIST CLOSE|THREE-SEAT \/ PROCESS LOCK|THREE-SEAT LOCK|RECEIPT \+ DRAFT|RECEIPT|PROCESS|Note|RED CONCUR)[[:space:]]*//')
  left=$(printf '%s\n' "$left" | sed -E 's/[[:space:]]+$//')
  if [ -n "$left" ] && [ "$left" != "$line" ]; then
    printf '%s\n' "$left" | cut -c1-120
    return
  fi
  if [[ "$line" == *"—"* ]]; then
    right="${line#*— }"
    packet=$(printf '%s\n' "$right" | sed -E 's/[[:space:]]*\([0-9:]+\)$//')
    printf '%s\n' "$packet" | cut -c1-120
    return
  fi
  printf '%s\n' "$line" | cut -c1-120
}

write_state() {
  local turn="$1"
  local markers="$2"
  local owed="$3"
  local last="$4"
  local packet="$5"
  local from="$6"
  local to="$7"
  {
    printf 'timestamp=%s\n' "$(date -Iseconds)"
    printf 'pid=%s\n' "$$"
    printf 'filter=%s\n' "$FILTER"
    printf 'turn=%s\n' "$turn"
    printf 'markers=%s\n' "$markers"
    printf 'owed=%s\n' "$owed"
    printf 'from=%s\n' "$from"
    printf 'to=%s\n' "$to"
    printf 'packet=%s\n' "$packet"
    printf 'last=%s\n' "$last"
  } >"$STATE"
}

is_owed_turn() {
  local filter="$1"
  local turn="$2"
  local last="$3"
  local from
  [ "$filter" = "ALL" ] && return 1
  [ "$turn" = "$filter" ] || return 1
  from=$(parse_from "$last")
  [ "$from" = "$filter" ] && return 1
  return 0
}

emit_filtered_line() {
  local filter="$1"
  local from="$2"
  local to="$3"
  local line="$4"
  case "$filter" in
    GROK)
      emit_stdout "DONE TO_GROK from=$from: $line"
      ;;
    CLAUDE)
      emit_stdout "DONE TO_CLAUDE from=$from: $line"
      ;;
    CHATGPT)
      emit_stdout "DONE TO_REF from=$from: $line"
      ;;
    *)
      case "$to" in
        ALL)
          emit_stdout "DONE TO_ALL from=$from: $line"
          ;;
        REF_UNADDRESSED)
          emit_stdout "DONE REF_NEEDS_TO_TAG from=$from: $line"
          ;;
        *)
          emit_stdout "DONE tribunal change from=$from to=$to: $line"
          ;;
      esac
      ;;
  esac
}

should_emit() {
  local to="$1"
  matches_filter_target "$FILTER" "$to"
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
prev_markers=$(count_markers "$FILE")
prev_turn=$(whose_turn "$FILE")
prev_last_relevant=$(last_relevant_line "$FILE" "$FILTER")
owed_polls=0
# Startup snapshot so a late-starting watcher still notices existing referee mail / turn state.
startup_turn=$(whose_turn "$FILE")
startup_last=$(last_relevant_line "$FILE" "$FILTER")
startup_exact=$(last_exact_line "$FILE" "$FILTER")
startup_markers=$(count_markers "$FILE")
startup_board_last=$(last_activity_line "$FILE")
startup_state_last="${startup_last:-$startup_board_last}"
startup_owed=0
startup_from=$(parse_from "$startup_board_last")
startup_to=$(parse_to "$startup_board_last")
startup_packet=$(extract_packet "$startup_board_last")
if is_owed_turn "$FILTER" "$startup_turn" "$startup_board_last"; then
  startup_owed=1
fi
write_state "$startup_turn" "$startup_markers" "$startup_owed" "$startup_state_last" "$startup_packet" "$startup_from" "$startup_to"
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
  turn=$(whose_turn "$FILE")
  n=$(count_markers "$FILE")
  last=$(last_activity_line "$FILE")
  current_last_relevant=$(last_relevant_line "$FILE" "$FILTER")
  state_last="${current_last_relevant:-$last}"
  state_from=$(parse_from "$last")
  state_to=$(parse_to "$last")
  state_packet=$(extract_packet "$last")
  owed=0
  if is_owed_turn "$FILTER" "$turn" "$last"; then
    owed=1
  fi
  if [ "$cur" = "$prev" ]; then
    write_state "$turn" "$n" "$owed" "$state_last" "$state_packet" "$state_from" "$state_to"
    if [ "$owed" -eq 1 ]; then
      owed_polls=$((owed_polls + 1))
      if [ $((owed_polls % REMINDER_EVERY)) -eq 0 ]; then
        emit_stdout "DONE REMINDER_${FILTER} still_owed packet=${state_packet}: $state_last"
      fi
    else
      owed_polls=0
    fi
    continue
  fi
  emitted=0
  owed_polls=0

  if [ "$n" -lt "$prev_markers" ]; then
    echo "$(date -Iseconds) RESET markers old=$prev_markers new=$n" >>"$LOG"
    prev_markers=0
  fi

  if [ "$n" -gt "$prev_markers" ]; then
    idx=$prev_markers
    while IFS= read -r line; do
      [ -n "$line" ] || continue
      idx=$((idx + 1))
      to=$(parse_to "$line")
      from=$(parse_from "$line")
      msg="EVENT idx=$idx from=$from to=$to turn=$turn markers=$n last=${line:0:120}"
      echo "$(date -Iseconds) $msg" >>"$LOG"

      if ! should_emit "$to"; then
        echo "$(date -Iseconds) SKIP filter=$FILTER (mail for $to)" >>"$LOG"
        continue
      fi

      emit_filtered_line "$FILTER" "$from" "$to" "$line"
      emitted=1
    done < <(heading_stream "$FILE" | tail -n +"$((prev_markers + 1))")
  else
    msg="EVENT from=$(parse_from "$last") to=$(parse_to "$last") turn=$turn markers=$n last=${last:0:120}"
    echo "$(date -Iseconds) $msg" >>"$LOG"
  fi

  if [ "$FILTER" != "ALL" ] && [ "$turn" = "$FILTER" ] && [ "$prev_turn" != "$turn" ] && [ "$emitted" -eq 0 ]; then
    emit_stdout "DONE TURN_${FILTER} board: ${current_last_relevant:-$last}"
    emitted=1
  fi

  if [ "$FILTER" != "ALL" ] && [ "$emitted" -eq 0 ] && [ "$current_last_relevant" != "$prev_last_relevant" ] && [ -n "$current_last_relevant" ]; then
    emit_stdout "DONE UPDATE_${FILTER} current_mail: $current_last_relevant"
  fi

  write_state "$turn" "$n" "$owed" "$state_last" "$state_packet" "$state_from" "$state_to"
  prev=$cur
  prev_markers=$n
  prev_turn=$turn
  prev_last_relevant=$current_last_relevant
done
