#!/usr/bin/env bash
# bbnfix_when_ready_all.sh — gated booking pipeline when the gate opens.
#
# Ordered (Claude red 2026-08-04: booking ≠ publishing):
#   0) progress + checkpoint snapshot
#   1) book_bbnfix_when_ready.py     → private booking card under _runs/bbnfix_booking_*
#   2) finalize_h0_at_convergence.py → letter sentence on stdout (not auto-pasted to shelf)
#   3) make_getdist_tables --include-bbnfix → FORWARD-FACING write to PRTOE_CHAIN_TABLES.md
#        **BLOCKED by default** until red audit stamp OR --write-tables after audit
#   4) bbnfix_delta_chi2_proxy.py      → proxy only (not Laplace)
#
# Claude A2 protocol: blue books; **red audits tables BEFORE forward-file entry**.
# Default: stop after book+finalize and print "tables blocked pending red audit".
#
# Exit codes:
#   0  book (+ finalize) succeeded; tables either skipped (default) or written after stamp
#   2  gate refused
#   1  book ok but later step failed
#
# Hard rules: NO PolyChord. NO kill chains. NO book while R−1 high.
#
# Usage (repo root):
#   bash scripts/bbnfix_when_ready_all.sh
#   bash scripts/bbnfix_when_ready_all.sh --write-tables   # only after red stamp present
#   bash scripts/bbnfix_when_ready_all.sh --force-tables   # OWNER override (logged); not default
#   bash scripts/bbnfix_when_ready_all.sh --skip-delta
#
# Red audit stamp (required for --write-tables):
#   docs/working_logs/_runs/bbnfix_booking_<id>/RED_AUDIT.md
#   must contain a line matching: red:\s*(AGREE|AGREE-IF)
#   (created by red auditor after auditing that booking package —
#    Claude when available; Grok may stamp when Claude is offline)

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

# Claude cure: tables OFF by default (booking ≠ publishing)
WRITE_TABLES=0
FORCE_TABLES=0
SKIP_DELTA=0
for arg in "$@"; do
  case "$arg" in
    --write-tables) WRITE_TABLES=1 ;;
    --force-tables) FORCE_TABLES=1; WRITE_TABLES=1 ;;
    --skip-tables)  WRITE_TABLES=0 ;;  # explicit no-op; default already skip
    --skip-delta)   SKIP_DELTA=1 ;;
    -h|--help)
      sed -n '2,40p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg" >&2
      exit 1
      ;;
  esac
done

echo "========================================================================"
echo "bbnfix_when_ready_all — gated booking pipeline"
echo "  repo: $REPO"
echo "  rule: both R−1 < 0.05 AND converged:true; no PolyChord; no kills"
echo "  publish rule: tables DEFAULT OFF until red audit stamp (Claude 2026-08-04)"
echo "========================================================================"

# --- 0. Read-only progress precheck ---
echo ""
echo "[0] progress / checkpoint snapshot"
for root in dyad_mnu_bbnfix cmp_lcdm_mnu_bbnfix; do
  prog="chains/${root}.progress"
  ckpt="chains/${root}.checkpoint"
  if [[ -f "$prog" ]]; then
    echo "  $root progress last: $(tail -1 "$prog")"
  else
    echo "  $root progress: MISSING"
  fi
  if [[ -f "$ckpt" ]]; then
    grep -E 'converged:' "$ckpt" | head -1 | sed "s/^/  $root /"
  else
    echo "  $root checkpoint: MISSING"
  fi
done

# --- 1. Book (hard gate; exit 2 if refuse) ---
echo ""
echo "[1] book_bbnfix_when_ready.py"
set +e
python3 scripts/book_bbnfix_when_ready.py
BOOK_RC=$?
set -e
if [[ "$BOOK_RC" -eq 2 ]]; then
  echo ""
  echo "REFUSED — gate not open. No finalize / tables / delta."
  echo "Re-run when both legs R−1 < 0.05 AND converged: true:"
  echo "  bash scripts/bbnfix_when_ready_all.sh"
  exit 2
fi
if [[ "$BOOK_RC" -ne 0 ]]; then
  echo "BOOK FAILED (exit $BOOK_RC) — aborting pipeline." >&2
  exit 1
fi
echo "  book: OK"

# Locate latest booking package (for red stamp path)
BOOK_DIR="$(ls -1dt docs/working_logs/_runs/bbnfix_booking_2* 2>/dev/null | head -1 || true)"
if [[ -n "$BOOK_DIR" ]]; then
  echo "  booking package: $BOOK_DIR"
  echo "  red stamp expected at: $BOOK_DIR/RED_AUDIT.md"
fi

# --- 2. Finalize H₀ letter (stdout only — not a shelf write) ---
echo ""
echo "[2] finalize_h0_at_convergence.py"
set +e
python3 scripts/finalize_h0_at_convergence.py
FIN_RC=$?
set -e
if [[ "$FIN_RC" -ne 0 ]]; then
  echo "finalize_h0 failed (exit $FIN_RC) after successful book — unexpected." >&2
  exit 1
fi
echo "  finalize_h0: OK (stdout letter only — paste only after red if publishing)"

# --- 3. GetDist tables → PRTOE_CHAIN_TABLES.md (forward-facing; red-gated) ---
echo ""
if [[ "$WRITE_TABLES" -eq 0 ]]; then
  echo "[3] make_getdist_tables BLOCKED (default) — booking ≠ publishing"
  echo "  Red: tables must not enter forward-facing docs until red audit stamp."
  echo "  After red writes $BOOK_DIR/RED_AUDIT.md with 'red: AGREE' or 'red: AGREE-IF':"
  echo "    bash scripts/bbnfix_when_ready_all.sh --write-tables"
  echo "  (Owner emergency only: --force-tables — logged; not default.)"
else
  STAMP=""
  if [[ -n "$BOOK_DIR" && -f "$BOOK_DIR/RED_AUDIT.md" ]]; then
    STAMP="$BOOK_DIR/RED_AUDIT.md"
  fi
  if [[ "$FORCE_TABLES" -eq 1 ]]; then
    echo "[3] make_getdist_tables --include-bbnfix  **FORCE** (owner override; no red stamp)"
    echo "  WARNING: bypasses red audit — not the standard path."
  elif [[ -n "$STAMP" ]] && grep -qiE 'red:[[:space:]]*(AGREE|AGREE-IF)' "$STAMP"; then
    echo "[3] make_getdist_tables --include-bbnfix  (red stamp OK: $STAMP)"
  else
    echo "[3] REFUSED write-tables — missing red audit stamp (Stage B blocked)"
    if [[ -z "${BOOK_DIR:-}" ]]; then
      echo "  No bbnfix_booking_* package found under docs/working_logs/_runs/."
      echo "  Run Stage A first (default, no flags) so a booking card exists, then red-audit it."
    else
      echo "  Need: $BOOK_DIR/RED_AUDIT.md containing a line: red: AGREE   (or AGREE-IF)"
      echo "  Claude red: audit that booking package before Stage B publish."
    fi
    echo "  Forward-facing PRTOE_CHAIN_TABLES.md was NOT modified."
    echo "  booking ≠ publishing: Stage A book+finalize is separate from table shelf write."
    exit 1
  fi
  set +e
  python3 scripts/make_getdist_tables.py --include-bbnfix
  TAB_RC=$?
  set -e
  if [[ "$TAB_RC" -ne 0 ]]; then
    echo "make_getdist_tables failed (exit $TAB_RC)." >&2
    exit 1
  fi
  echo "  tables: OK (forward file written — restore live banner if needed)"
fi

# --- 4. Δχ² proxy (not full Laplace; not forward shelf by itself) ---
if [[ "$SKIP_DELTA" -eq 0 ]]; then
  echo ""
  echo "[4] bbnfix_delta_chi2_proxy.py  (proxy only — not bookable Laplace ΔlnZ)"
  set +e
  python3 scripts/bbnfix_delta_chi2_proxy.py
  DEL_RC=$?
  set -e
  if [[ "$DEL_RC" -ne 0 ]]; then
    echo "delta_chi2_proxy failed (exit $DEL_RC)." >&2
    exit 1
  fi
  echo "  delta_chi2_proxy: OK (label as proxy, not Laplace)"
else
  echo ""
  echo "[4] bbnfix_delta_chi2_proxy SKIPPED (--skip-delta)"
fi

echo ""
echo "========================================================================"
if [[ "$WRITE_TABLES" -eq 0 ]]; then
  echo "PIPELINE STAGE A COMPLETE (book + finalize). Tables NOT written."
  echo "  → Claude: audit booking package, write RED_AUDIT.md"
  echo "  → then: bash scripts/bbnfix_when_ready_all.sh --write-tables"
else
  echo "PIPELINE STAGE B COMPLETE (tables written after red stamp / force)."
fi
echo "  CosmicForge Laplace optional — see RUNBOOK.md Step C (no PolyChord)."
echo "  Do NOT substitute pre-bbnfix ΔlnZ ≈ +2.6."
echo "Package: docs/working_logs/_runs/laplace_booking_full_20260804/"
echo "========================================================================"
exit 0
