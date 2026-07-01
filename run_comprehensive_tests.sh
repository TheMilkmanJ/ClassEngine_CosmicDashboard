#!/bin/bash

echo "════════════════════════════════════════════════════════════════════"
echo "   PRTOE COMPREHENSIVE TEST SUITE"
echo "════════════════════════════════════════════════════════════════════"
echo ""

cd /home/themilkmanj/prtoe_class

# Create results file
RESULTS="/tmp/prtoe_test_results.txt"
> $RESULTS

run_test() {
    local test_name=$1
    local ini_file=$2
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Test: $test_name"
    echo "File: $ini_file"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    if [ ! -f "$ini_file" ]; then
        echo "❌ SKIP: $ini_file not found"
        echo "$test_name: SKIP (file not found)" >> $RESULTS
        return 1
    fi
    
    local start_time=$(date +%s)
    local output=$(/tmp/test_output_$$.txt)
    
    if timeout 180 ./class "$ini_file" > $output 2>&1; then
        local end_time=$(date +%s)
        local duration=$((end_time - start_time))
        
        if grep -q "error\|Error\|ERROR" $output 2>/dev/null; then
            echo "❌ FAIL: Runtime errors detected"
            tail -20 $output
            echo "$test_name: FAIL (runtime errors)" >> $RESULTS
        else
            echo "✅ PASS ($duration sec)"
            echo "$test_name: PASS ($duration sec)" >> $RESULTS
        fi
    else
        echo "❌ FAIL: Timeout or crash"
        tail -20 $output
        echo "$test_name: FAIL (timeout/crash)" >> $RESULTS
    fi
    
    rm -f $output
    echo ""
}

# TEST SUITE
echo "SCENARIO 1: LCDM Baseline (verify we didn't break existing code)"
run_test "LCDM Baseline" "test_lambda_cdm.ini"

echo "SCENARIO 2: PRTOE Null Limit (ξ → 0)"
run_test "PRTOE Null Limit" "test_minimal_prtoe_null.ini"

echo "SCENARIO 3: PRTOE Active (full field evolution)"
run_test "PRTOE Active Simple" "test_prtoe_active_simple.ini"

echo "SCENARIO 4: PRTOE Active with Full Perturbations"
run_test "PRTOE Perturbations" "test_prtoe_perturbations.ini"

echo "SCENARIO 5: PRTOE Active Full Cosmology"
run_test "PRTOE Active Full" "test_prtoe_active_full.ini"

echo "════════════════════════════════════════════════════════════════════"
echo "TEST RESULTS SUMMARY"
echo "════════════════════════════════════════════════════════════════════"
cat $RESULTS

# Count results
PASS=$(grep "PASS" $RESULTS | wc -l)
FAIL=$(grep "FAIL" $RESULTS | wc -l)
SKIP=$(grep "SKIP" $RESULTS | wc -l)

echo ""
echo "Summary: $PASS PASS, $FAIL FAIL, $SKIP SKIP"

if [ $FAIL -eq 0 ]; then
    echo "✅ ALL TESTS PASSED"
    exit 0
else
    echo "❌ SOME TESTS FAILED - See results above"
    exit 1
fi
