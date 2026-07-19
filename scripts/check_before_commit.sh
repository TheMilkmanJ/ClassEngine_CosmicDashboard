#!/usr/bin/env bash
# Run the math harness and REFUSE to proceed on any failure.
# Use as:  bash scripts/check_before_commit.sh && git commit ...
set -euo pipefail
out=$(python3 "$(dirname "$0")/audit_math_pass.py" 2>&1)
printf "%s\n" "${out%%$'\n'*}"
if echo "$out" | grep -q "^FAILURES:"; then
  echo
  echo "$out" | sed -n '/^FAILURES:/,$p'
  echo
  echo "REFUSING TO COMMIT — fix the failing check(s) first."
  exit 1
fi
