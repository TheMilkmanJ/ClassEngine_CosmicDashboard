#!/usr/bin/env bash
# bbnfix_gate_fire_watch.sh — Stage A book when dual gate opens.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
LOGDIR="${1:-docs/working_logs/_runs/gate_fire_watch_20260804}"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/watch.log"
INTERVAL="${INTERVAL:-300}"
PIDFILE="$LOGDIR/watch.pid"
echo $$ > "$PIDFILE"
echo "$(date -Iseconds) START gate-fire watch interval=${INTERVAL}s pid=$$" | tee -a "$LOG"
while true; do
  OUT="$LOGDIR/poll_$(date -u +%Y%m%dT%H%M%SZ).txt"
  set +e
  python3 scripts/book_bbnfix_when_ready.py >"$OUT" 2>&1
  EC=$?
  set -e
  grep -E 'R−1|R-1|REFUSED|booked|converged' "$OUT" | tail -15 >>"$LOG" || true
  echo "$(date -Iseconds) poll exit=$EC" >>"$LOG"
  if [ "$EC" -eq 0 ]; then
    echo "$(date -Iseconds) GATE OPEN — Stage A" | tee -a "$LOG"
    # Capture booking card path from the successful book poll (Claude nit: claim ships with artifact)
    BOOK_CARD=$(grep -E 'wrote refuse card:|wrote:|bbnfix_booking_' "$OUT" | tail -5 | tr '\n' ' ' || true)
    LATEST_BOOK=$(ls -dt docs/working_logs/_runs/bbnfix_booking_* 2>/dev/null | head -1 || true)
    set +e
    bash scripts/bbnfix_when_ready_all.sh >>"$LOG" 2>&1
    ALL_EC=$?
    echo "$(date -Iseconds) all.sh exit=$ALL_EC" | tee -a "$LOG"
    set -e
    LATEST_BOOK=$(ls -dt docs/working_logs/_runs/bbnfix_booking_* 2>/dev/null | head -1 || true)
    REPORT_PATH="${LATEST_BOOK}/REPORT.md"
    {
      echo ""
      echo "### EVENT gate-fire Stage A @FROM:GROK @TO:ALL >>BLUE >>RED >>REF — bbnfix dual gate OPEN; Stage A book (tables OFF)"
      echo ""
      echo "**Artifact (evidence):** \`${REPORT_PATH}\`"
      echo "**Poll capture:** ${BOOK_CARD}"
      echo "**all.sh exit:** ${ALL_EC}"
      echo ""
      echo "**WHOSE_TURN → Claude** (red audit before tables — open artifact first) **∥ Owner** **∥ Grok** Stage B after red."
      echo ""
      echo "---"
    } >> "ForGrok&Claude.md"
    rm -f "$PIDFILE"
    exit 0
  fi
  sleep "$INTERVAL"
done
