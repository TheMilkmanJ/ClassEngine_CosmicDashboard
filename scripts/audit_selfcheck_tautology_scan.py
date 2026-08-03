#!/usr/bin/env python3
"""
META-AUDIT: which of audit_math_pass.py's checks CANNOT FAIL?

WHY. The corpus leans hard on "1282 closed-form checks, all pass". That number is
only worth what the checks are worth, and a check whose booked value is recomputed
from the same expression it is compared against is not verification -- it is a
tautology that reports success unconditionally. A few of those inflate the count
and, worse, create false confidence exactly where confidence is being claimed.

Noticed while reading an unrelated line:

    chk("S8 pair", "g candidate identity 10*eps == 54a/pi", 1.0,
        (10*27/(5*math.pi)*(1/137.035999)) / (54/(math.pi*137.035999)), 1e-12)

The computed side is a ratio that reduces to 10*27/5 / 54 = 1 identically. It
verifies the arithmetic 10 * 27/5 = 54 -- a real transcription check, but NOT the
physical claim its label suggests ("g candidate identity"), because the identity
holds for ANY alpha and any value of eps's definition. A reader scanning the pass
list would credit it as physics.

WHAT THIS SCRIPT DOES. Parses the chk(...) call sites and flags three patterns:

  T1  RATIO-TO-ONE: booked is 1.0 (or 0.0) and the computed side is a ratio
      (or difference) of two expressions built from the same literals -- passes
      by construction whenever the algebra is right, independent of any input.
  T2  LITERAL ECHO: the booked value appears verbatim as a literal inside the
      computed expression, so the check compares a number to itself.
  T3  CONSTANT-FREE: the computed side contains no name and no call -- it is a
      pure arithmetic literal expression, so it can only test transcription.

None of these are necessarily WRONG. T3 in particular is legitimate for pinning a
definition. The point is that they are a different KIND of check from one that
recomputes a physical quantity by an independent route, and the headline count
should not blur the two.

This script does NOT edit the audit. It reports, so the split can be stated
honestly.
"""

import ast
import os
import re

AUDIT = "/home/themilkmanj/prtoe_class/scripts/audit_math_pass.py"


def literals_in(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            out.append(n.value)
    return out


def names_in(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            out.append(n.id)
        elif isinstance(n, ast.Attribute):
            out.append(n.attr)
    return out


def calls_in(node):
    return [n for n in ast.walk(node) if isinstance(n, ast.Call)]


def main():
    src = open(AUDIT).read()
    tree = ast.parse(src)
    lines = src.splitlines()

    total = 0
    t1, t2, t3 = [], [], []

    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "chk"):
            continue
        if len(node.args) < 4:
            continue
        total += 1
        doc = node.args[0]
        claim = node.args[1]
        booked = node.args[2]
        got = node.args[3]
        label = ""
        if isinstance(claim, ast.Constant):
            label = str(claim.value)
        docs = str(doc.value) if isinstance(doc, ast.Constant) else "?"
        ln = node.lineno

        booked_val = booked.value if isinstance(booked, ast.Constant) else None

        # T1: booked is 1.0 or 0.0 and got is a ratio/difference
        if booked_val in (1.0, 1, 0.0, 0) and isinstance(got, ast.BinOp) \
                and isinstance(got.op, (ast.Div, ast.Sub)):
            gl = literals_in(got)
            # same literals on both sides of the operator -> reduces identically
            left = set(literals_in(got.left))
            right = set(literals_in(got.right))
            if left & right and not calls_in(got):
                t1.append((ln, docs, label))

        # T2: booked literal appears verbatim inside got
        if booked_val is not None and booked_val not in (0, 0.0, 1, 1.0):
            if booked_val in literals_in(got):
                t2.append((ln, docs, label))

        # T3: got is pure literal arithmetic (no names, no calls)
        if not names_in(got) and not calls_in(got) and literals_in(got):
            t3.append((ln, docs, label))

    print("=" * 78)
    print("  META-AUDIT — which checks cannot fail?")
    print("=" * 78)
    print(f"\n  chk() call sites parsed: {total}")

    def show(tag, desc, rows):
        print(f"\n  {tag}  {desc}")
        print(f"      count: {len(rows)}")
        for ln, docs, label in rows[:14]:
            print(f"      line {ln:<6} [{docs}] {label[:58]}")
        if len(rows) > 14:
            print(f"      ... and {len(rows)-14} more")

    show("T1", "RATIO-TO-ONE — reduces to an identity regardless of inputs", t1)
    show("T2", "LITERAL ECHO — booked value appears verbatim in the computed side", t2)
    show("T3", "CONSTANT-FREE — pure literal arithmetic (transcription check only)", t3)

    flagged = {r[0] for r in t1} | {r[0] for r in t2} | {r[0] for r in t3}
    print("\n" + "=" * 78)
    print(f"  {len(flagged)} of {total} call sites flagged "
          f"({100*len(flagged)/max(total,1):.1f}%)")
    print("=" * 78)
    print("""
  HOW TO READ THIS -- AND THE ONE WAY TO MISREAD IT BADLY.

  Flagged does NOT mean wrong, and the flagged fraction is an UPPER BOUND on the
  soft checks, not an estimate of them. T3 conflates two different things:

    (a) PINNING AN EXTERNAL INPUT -- a measured rate, a published uncertainty, a
        literature band. You CANNOT recompute a measurement. Pinning is the
        correct and necessary check here, and counting these as weak is simply
        wrong. Spot-checking the deuterium_row block shows many of its 12
        pure-literal checks are exactly this: "d ln(D/H)/d ln omega_b (production,
        MEASURED)", "Pisanti's rate error", "tau_n bottle->beam".

    (b) PINNING SOMETHING DERIVABLE -- where an independent route existed and was
        not taken. This is the only case that is a missed opportunity.

  This scanner CANNOT separate (a) from (b), because the distinction is about
  PROVENANCE, not syntax: it lives in whether the number came from a measurement or
  from the theory, which no amount of AST inspection can see. So do not quote the
  flagged percentage as a defect rate. The honest phrasing is:

      "N% are definition- or input-pins rather than independent recomputations,
       most of them legitimately so."

  WHAT IS ACTUALLY WORTH FIXING: anything in T1 or T2 whose LABEL implies a
  physical identity. The fix is the label, not the check -- a reader scanning a
  pass list credits what the label says, and a check that cannot fail should not
  be wearing the name of a claim that is still owed.
""")


if __name__ == "__main__":
    main()
