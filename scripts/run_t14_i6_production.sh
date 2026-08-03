#!/usr/bin/env bash
# R1-t14-i6 — 128³ production (OWNER-GATED A4)
#
# Will NOT run unless you pass:  --i-approve-a4
# Spec: ForJustin/OVERNIGHT.md A4 + ForGrok&Claude.md NEXT ISSUE R1-t14-i6
#
# Steps:
#   1) calibrate (planar must be ~0)
#   2) nulls at production grid (nowinding, nojet)
#   3) four-branch production
#   4) print decomposition + mirror residual
#
set -euo pipefail
cd "$(dirname "$0")/.."

APPROVED=0
OUT="docs/working_logs/_runs/t14_hkin_i6_prod_$(date +%Y%m%d_%H%M%S)"
for arg in "$@"; do
  case "$arg" in
    --i-approve-a4) APPROVED=1 ;;
    --out=*) OUT="${arg#--out=}" ;;
  esac
done

if [[ "$APPROVED" -ne 1 ]]; then
  cat <<EOF
REFUSED: R1-t14-i6 production is owner-gated (A4 in ForJustin/OVERNIGHT.md).

To run after Justin approves:
  bash scripts/run_t14_i6_production.sh --i-approve-a4

Optional:
  bash scripts/run_t14_i6_production.sh --i-approve-a4 --out=docs/working_logs/_runs/t14_hkin_i6_prod
EOF
  exit 2
fi

echo "============================================================"
echo "  R1-t14-i6 PRODUCTION 128x128x256  out=$OUT"
echo "  OWNER APPROVED via --i-approve-a4"
echo "============================================================"

mkdir -p "$OUT"

echo "[1/4] calibrate..."
python3 scripts/ring_toroidal_hkin.py --calibrate 2>&1 | tee "$OUT/calibrate.log"
grep -q "CALIBRATION OVERALL: PASS" "$OUT/calibrate.log"

echo "[2/4] null nowinding (prod grid)..."
python3 scripts/ring_toroidal_hkin.py --null nowinding --out "$OUT/null_nowinding" \
  2>&1 | tee "$OUT/null_nowinding_console.log"

echo "[3/4] null nojet (prod grid)..."
python3 scripts/ring_toroidal_hkin.py --null nojet --out "$OUT/null_nojet" \
  2>&1 | tee "$OUT/null_nojet_console.log"

echo "[4/4] four-branch production..."
python3 scripts/ring_toroidal_hkin.py --out "$OUT/four_branch" \
  2>&1 | tee "$OUT/four_branch_console.log"

echo "DONE. Review $OUT/four_branch/summary.json for mirror residual (target <5%)."
echo "Decomposition: 2n / Tw / Wr per branch in series + summary."
