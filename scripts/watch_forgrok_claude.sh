#!/bin/bash
set -euo pipefail

repo_root="/home/themilkmanj/prtoe_class"
target="$repo_root/ForGrok&Claude.md"
log_dir="$repo_root/docs/working_logs/_runs"
log_file="$log_dir/forgrok_claude_monitor.log"
interval="${1:-10}"
heartbeat_every="${2:-6}"

mkdir -p "$log_dir"

if [ ! -f "$target" ]; then
  echo "target missing: $target" >&2
  exit 1
fi

last_mtime="$(stat -c %Y "$target")"
printf '%s\n' "$$" > "$log_dir/forgrok_claude_monitor.pid"
echo "$(date -Iseconds) monitor armed for $target interval=${interval}s pid=$$" >> "$log_file"

tick=0
while true; do
  sleep "$interval"
  tick=$((tick + 1))

  if [ ! -f "$target" ]; then
    echo "$(date -Iseconds) target missing: $target" >> "$log_file"
    exit 1
  fi

  current_mtime="$(stat -c %Y "$target")"
  if [ "$current_mtime" != "$last_mtime" ]; then
    last_mtime="$current_mtime"
    echo "$(date -Iseconds) change detected in $target" >> "$log_file"
    tail -n 12 "$target" >> "$log_file"
    echo "---" >> "$log_file"
  elif [ $((tick % heartbeat_every)) -eq 0 ]; then
    echo "$(date -Iseconds) heartbeat: monitoring $target (pid=$$, mtime=$last_mtime)" >> "$log_file"
  fi
done
