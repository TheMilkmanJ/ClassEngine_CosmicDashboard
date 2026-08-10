"""Read-only: claims-ledger rows that assert a closed grade but print no residual.

The corpus convention is that every claims-ledger row carries a
'Residual / blocker' cell. A row graded derived / complete / verified whose
residual cell is empty or an em-dash asserts closure with nothing owed --
the shape THE_AMPLITUDE row 2 has for f-bar, which DERIVATION_HUNT grades
'not an absolute closure'.

Usage: python3 empty_residual.py
Makes no edits.
"""
import glob
import re

CLOSED = re.compile(r'derived|complete|verified|proven|closed', re.I)
CONDITIONAL = re.compile(r'conditional|candidate|open|assumption|bet|provisional', re.I)
EMPTY = {'', '-', '--', '\u2014', '\u2013', 'n/a', 'none', '\u2014 ', 'tbd'}


def strip_escaped(x):
    return x.replace('\\|', '\x00')


def cells(line):
    return [c.strip() for c in strip_escaped(line.strip()).strip('|').split('|')]


for f in sorted(glob.glob('docs/*.md')) + sorted(glob.glob('docs/exploratory/*.md')):
    lines = open(f, encoding='utf-8').read().split('\n')
    header = None
    ridx = None
    for i, line in enumerate(lines):
        s = line.strip()
        if not (s.startswith('|') and s.endswith('|')):
            header = None
            continue
        c = cells(line)
        if any(re.search(r'residual|blocker', x, re.I) for x in c):
            header = c
            ridx = next(k for k, x in enumerate(c) if re.search(r'residual|blocker', x, re.I))
            continue
        if header is None or ridx is None or ridx >= len(c):
            continue
        if re.fullmatch(r'[\s:\-|]+', s):
            continue
        grade = ' '.join(c[1:ridx])
        resid = c[ridx].strip().strip('*').strip()
        if CLOSED.search(grade) and not CONDITIONAL.search(grade) and resid.lower() in EMPTY:
            print('%s:%d: CLOSED_GRADE_NO_RESIDUAL :: %s' % (f, i + 1, s[:130]))
