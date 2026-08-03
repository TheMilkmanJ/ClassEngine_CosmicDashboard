"""Which of the math audit's checks would notice if a booked input were corrected?

This measures the PROPAGATION axis of protocol check 21, not the closure axis of check 23 --
the two are easy to conflate and this script only sees the first. Entries divide as:

  SELF-CONTAINED  chk("...", "...", 0.7071, math.sqrt(1.5)/math.sqrt(3), 1e-4)
                  the computed side is closed in literals. This one is a genuine closure
                  check -- it derives B from two other booked ratios -- but it retypes their
                  values rather than referencing them, so if either upstream number were
                  corrected this line would keep the old one and still pass.

  COUPLED         chk("...", "...", 1.36461, _kNv(2, 1), 1e-6)
                  the computed side reaches named quantities, so a correction upstream
                  propagates into it automatically.

Self-contained is not the same as weak: many are exact-surd checks that catch mistyped
decimals, and some, like the example above, are real closure tests. What they share is that
they cannot inherit a fix. The ratio is worth knowing because it bounds how much of the
harness would notice if a load-bearing input moved.

Run: python3 scripts/harness_strength_census.py
"""
import os
import re
from collections import Counter

HARNESS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audit_math_pass.py")
SAFE = {"math", "cmath", "pi", "e", "sqrt", "log", "exp", "sin", "cos", "tan", "atan",
        "atan2", "asin", "acos", "log10", "log2", "sinh", "cosh", "tanh", "asinh",
        "acosh", "atanh", "hypot", "fabs", "abs", "min", "max", "sum", "float", "int",
        "round", "pow", "inf", "nan", "tau", "degrees", "radians", "gamma", "lgamma",
        "erf", "erfc", "factorial", "comb", "prod", "isclose", "phase", "polar", "rect"}
IDENT = re.compile(r"[A-Za-z_][A-Za-z_0-9]*")


def split_args(s):
    """Split a call's argument text on top-level commas."""
    out, depth, cur, instr = [], 0, "", None
    for ch in s:
        if instr:
            cur += ch
            if ch == instr:
                instr = None
            continue
        if ch in "\"'":
            instr, cur = ch, cur + ch
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


src = open(HARNESS).read()
# Pull each chk( ... ) call, balancing parentheses.
calls = []
for m in re.finditer(r"\bchk\(", src):
    i, depth = m.end(), 1
    while i < len(src) and depth:
        if src[i] == "(":
            depth += 1
        elif src[i] == ")":
            depth -= 1
        i += 1
    calls.append(src[m.end():i - 1])

selfc, coupled, unparsed = [], [], 0
for c in calls:
    args = split_args(c)
    if len(args) < 4:
        unparsed += 1
        continue
    got = args[3]
    # strip string literals before looking for identifiers
    bare = re.sub(r"\"[^\"]*\"|'[^']*'", "", got)
    names = {n for n in IDENT.findall(bare) if n not in SAFE}
    tag = args[0].strip().strip("\"'")
    (coupled if names else selfc).append(tag)

total = len(selfc) + len(coupled)
print("=" * 74)
print("MATH AUDIT — WHICH CHECKS INHERIT AN UPSTREAM CORRECTION")
print("=" * 74)
print(f"  chk() call sites parsed   {total}   (unparsed: {unparsed})")
print("  the harness reports more checks than this because some call sites sit in loops")
print(f"  COUPLED        (references named quantities) {len(coupled):5}   {len(coupled)/total*100:5.1f}%")
print(f"  SELF-CONTAINED (literals only)              {len(selfc):5}   {len(selfc)/total*100:5.1f}%")
print()
print("  Self-contained checks are not padding — they catch mistyped digits and some are")
print("  genuine closure tests. What they cannot do is inherit a correction: if a booked")
print("  input moves, only the coupled fraction follows it automatically.")

print()
print("=" * 74)
print("WHERE THE SELF-CONTAINED CHECKS CLUSTER")
print("=" * 74)
print("  Sections with the most literal-only entries — where a corrected input would be")
print("  least likely to propagate, and where check 23 therefore looks first.")
print()
for tag, n in Counter(selfc).most_common(12):
    d = sum(1 for t in coupled if t == tag)
    print(f"    {tag:<34} self {n:4}   coupled {d:4}   ({n/(n+d)*100:4.0f}% self-contained)")

print()
print("=" * 74)
print("SECTIONS WITH NO COUPLED CHECK AT ALL")
print("=" * 74)
only = sorted({t for t in selfc} - {t for t in coupled})
print(f"  {len(only)} of {len(set(selfc) | set(coupled))} tagged sections are entirely self-contained:")
for t in only:
    print(f"    {t}  ({Counter(selfc)[t]} checks)")
print()
print("  In these sections nothing the harness computes depends on anything else it holds,")
print("  so no correction can propagate and no set can be seen to fail closure. That is the")
print("  configuration the junction quartet was in when its four numbers passed separately.")
