#!/usr/bin/env bash
# Run PRTOE validation tests 1-9; skip test 10 (full publication / PolyChord).
#
# LANE: mostly LEGACY_ST (use_prtoe / historical inis). Passes here are comparison
# regression, not CURRENT_CORE public-core claims.
# CURRENT_CORE null/identity: python3 validate_dcdf.py (use_dcdf + varying_me path).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# classy wheel targets the active `python` (conda 3.13 here), not system python3.
PY="${PYTHON:-python}"
LOG="${ROOT}/Test-Results/validation_suite_$(date +%Y%m%d_%H%M%S).log"
mkdir -p Test-Results

run_step() {
  local n="$1" name="$2"
  shift 2
  echo "" | tee -a "$LOG"
  echo "========== TEST $n: $name ==========" | tee -a "$LOG"
  echo "Command: $*" | tee -a "$LOG"
  local t0=$SECONDS
  if "$@" >>"$LOG" 2>&1; then
    echo "RESULT: PASS ($((SECONDS - t0))s)" | tee -a "$LOG"
    return 0
  else
    local rc=$?
    echo "RESULT: FAIL exit=$rc ($((SECONDS - t0))s)" | tee -a "$LOG"
    return $rc
  fi
}

echo "Validation suite log: $LOG"
echo "Lane: LEGACY_ST comparison suite (use_prtoe / historical). CURRENT_CORE → validate_dcdf.py"
: >"$LOG"
{
  echo "Lane: LEGACY_ST comparison suite (use_prtoe / historical)."
  echo "CURRENT_CORE null/identity is validate_dcdf.py (use_dcdf), not test_prtoe_null_limit.py."
} >>"$LOG"

FAIL=0
run_step 1 "env check" "$PY" scripts/check_prtoe_env.py || FAIL=1
run_step 2 "LEGACY_ST local gravity" "$PY" scripts/test_local_gravity.py --classy || FAIL=1
run_step 3 "LEGACY_ST background only" ./class test_prtoe_bg_only.ini || FAIL=1
run_step 4 "LEGACY_ST null simple mPk" ./class test_prtoe_null_simple.ini || FAIL=1
run_step 5 "LEGACY_ST active mPk fast" ./class test_prtoe_mpk_fast.ini || FAIL=1
run_step 6 "LEGACY_ST BBN activation" "$PY" scripts/test_bbn_activation.py --classy || FAIL=1
run_step 7 "LEGACY_ST null publication fast" ./class test_prtoe_null_publication_fast.ini || FAIL=1
run_step 8 "LambdaCDM baseline" ./class test_lambda_cdm.ini || FAIL=1
run_step 9 "LEGACY_ST null limit Python (use_prtoe)" "$PY" scripts/test_prtoe_null_limit.py --fast --null-only || FAIL=1

echo "" | tee -a "$LOG"
echo "========== SUITE SUMMARY (LEGACY_ST comparison) ==========" | tee -a "$LOG"
if [[ $FAIL -eq 0 ]]; then
  echo "ALL TESTS 1-9 PASSED (LEGACY_ST lane; not CURRENT_CORE claims)" | tee -a "$LOG"
else
  echo "ONE OR MORE TESTS FAILED (see $LOG)" | tee -a "$LOG"
fi
echo "Skipped test 10 (full publication / PolyChord)" | tee -a "$LOG"
echo "CURRENT_CORE: python3 validate_dcdf.py" | tee -a "$LOG"
exit $FAIL
