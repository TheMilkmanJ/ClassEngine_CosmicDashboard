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

# THE NAMING LAW (owner ruling 2026-07-19): PRTOE expands ONLY to
# "Pulford-Romsa Theory of Expansion". Any other expansion in live files is a defect.
# History homes (archive/, the failures ledger, the audit ledger, git logs) are exempt.
bad=$(grep -rln "Pulford-Romsa Theory of Everything\|Phantom Rip Theory"       --include="*.md" --include="*.py" --include="*.js" --include="*.html" --include="*.c" --include="*.yaml"       README.md docs/ scripts/ cosmic_dashboard/ cosmic_explorer.py 2>/dev/null       | grep -v "docs/archive/\|FAILURES_LEDGER\|_AUDIT_LEDGER" || true)
if [ -n "$bad" ]; then
  echo
  echo "NAMING LAW VIOLATION — a wrong PRTOE expansion is live in:"
  echo "$bad"
  echo "REFUSING TO COMMIT — the name is: Pulford-Romsa Theory of Expansion."
  exit 1
fi
