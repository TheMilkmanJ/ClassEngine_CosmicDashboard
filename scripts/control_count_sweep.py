#!/usr/bin/env python3
"""
An integrity sweep, not a physics result: does every "N controls" claim in docs/ match
the number the named script actually runs?

WHY. Three such claims were found wrong on 2026-07-29 -- two written the same hour
(17 vs 20, 15 vs 17) and one from earlier that day (15 vs 27). A control count is a
claim about how hard a result was tested, and it is quoted to referees. Getting it
wrong is not cosmetic: it is the same class as an inflated audit count, which
protocol 46 already treats as a defect.

The three found by hand share a cause -- controls were ADDED to a script after the
prose was written, and nobody re-counted. That is a drift failure, so it will recur,
so it wants an instrument rather than another careful read.

WHAT IT DOES. Scans docs/ for claims of the form "<script>.py ... (N controls" or
"<script>.py, N controls", runs each named script, counts its passing controls, and
reports mismatches. A script is counted by its "  ok  " / "  FAIL" harness lines,
which is the house convention across scripts/.

WHAT IT DELIBERATELY DOES NOT DO. It does not rewrite anything. Control counts sit in
prose that also states what the controls FOUND, and a scripted substitution cannot
tell an outdated count from a deliberate count of a subset. Every hit is reported for
a manual decision -- consistent with the standing manual-edits rule.

Run: python3 scripts/control_count_sweep.py
"""

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"

# "foo.py` (12 controls" | "foo.py`, 12 controls" | "foo.py (12 controls"
CLAIM = re.compile(
    r"(?:scripts/)?([a-z0-9_]+\.py)`?\s*(?:\(|,\s*)\s*(\d+)\s+controls",
    re.IGNORECASE,
)

# the house harness lines
OK = re.compile(r"^\s{2,}(ok|FAIL)\s", re.MULTILINE)


def count_controls(script):
    """run a script and count its harness lines; None if it will not run."""
    try:
        r = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, timeout=900,
        )
    except subprocess.TimeoutExpired:
        return None, "timed out"
    if r.returncode != 0:
        return None, f"exit {r.returncode}"
    n = len(OK.findall(r.stdout))
    return (n, "") if n else (None, "no harness lines found")


def main():
    claims = []
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        for m in CLAIM.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            claims.append((md.relative_to(ROOT), line, m.group(1), int(m.group(2))))

    print("=" * 78)
    print("  CONTROL-COUNT SWEEP — do the docs' claims match the scripts?")
    print("=" * 78)
    print(f"\n  {len(claims)} claim(s) found across docs/")

    if not claims:
        print("\n  nothing to check.")
        return

    # run each distinct script once
    wanted = sorted({c[2] for c in claims})
    print(f"  {len(wanted)} distinct script(s) to run\n")
    actual = {}
    for name in wanted:
        path = SCRIPTS / name
        if not path.exists():
            actual[name] = (None, "script not found")
            print(f"    {name:<44} MISSING")
            continue
        n, why = count_controls(path)
        actual[name] = (n, why)
        print(f"    {name:<44} {n if n is not None else 'unrunnable (' + why + ')'}")

    print("\n" + "-" * 78)
    mismatches, unverifiable = [], []
    for doc, line, name, claimed in claims:
        n, why = actual[name]
        if n is None:
            unverifiable.append((doc, line, name, claimed, why))
        elif n != claimed:
            mismatches.append((doc, line, name, claimed, n))

    if mismatches:
        print(f"\n  {len(mismatches)} MISMATCH(ES) — each needs a manual decision:\n")
        for doc, line, name, claimed, n in mismatches:
            print(f"    {doc}:{line}")
            print(f"      {name}: doc says {claimed}, script runs {n}"
                  f"   ({'under' if claimed < n else 'OVER'}-stated by {abs(n-claimed)})")
    else:
        print("\n  no mismatches — every claim matches its script.")

    if unverifiable:
        print(f"\n  {len(unverifiable)} claim(s) could not be checked:\n")
        for doc, line, name, claimed, why in unverifiable:
            print(f"    {doc}:{line}  {name} ({why}) — claim of {claimed} not verified")

    print("\n" + "=" * 78)
    over = [m for m in mismatches if m[3] > m[4]]
    print(f"  {len(claims)} claims, {len(mismatches)} wrong, {len(over)} OVER-stated")
    if over:
        print("  Over-stated counts are the ones that matter: they claim more testing")
        print("  than was done. Under-stated ones are stale, not misleading.")
    print("=" * 78)
    print("\n  Nothing was rewritten. Control counts sit in prose that also says what the")
    print("  controls FOUND, and a substitution cannot distinguish a stale count from a")
    print("  deliberate count of a subset. Fix each by hand.")


if __name__ == "__main__":
    main()
