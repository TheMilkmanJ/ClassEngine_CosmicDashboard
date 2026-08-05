"""Read-only detector: orphaned / malformed markdown tables in the forward-facing docs tree.

Flags three failure modes that render broken or read as a table with no head:
  NO_SEPARATOR      - a run of table rows with no |---| separator anywhere
  SEP_NOT_SECOND    - separator is not the second line, so the header is not a header
  COLCOUNT_MISMATCH - rows in one block disagree on column count

Usage: python3 docs/working_logs/_runs/docs_full_check12_20260805/red/orphan_tables.py
Makes no edits.
"""
import glob
import re

files = sorted(glob.glob('docs/*.md')) + sorted(glob.glob('docs/exploratory/*.md'))


def strip_escaped(x):
    """Escaped \\| is a literal pipe inside a cell, not a delimiter."""
    return x.replace('\\|', '\x00')


def is_row(x):
    x = strip_escaped(x.strip())
    return x.startswith('|') and x.endswith('|') and x.count('|') >= 3


def is_sep(x):
    x = strip_escaped(x.strip())
    return bool(re.fullmatch(r'\|[\s:\-\|]+\|', x)) and '-' in x


def ncells(x):
    """Delimiter count for a row, ignoring escaped pipes."""
    return strip_escaped(x.strip()).strip('|').count('|') + 1


for f in files:
    lines = open(f, encoding='utf-8').read().split('\n')
    i = 0
    n = len(lines)
    while i < n:
        if is_row(lines[i]) and not is_sep(lines[i]):
            start = i
            block = []
            while i < n and (is_row(lines[i]) or is_sep(lines[i])):
                block.append(lines[i])
                i += 1
            seps = [k for k, b in enumerate(block) if is_sep(b)]
            ncols = [ncells(b) for b in block if not is_sep(b)]
            head = block[0].strip()[:100]
            if not seps:
                print('%s:%d: NO_SEPARATOR (%d lines) :: %s' % (f, start + 1, len(block), head))
            elif seps[0] != 1:
                print('%s:%d: SEP_NOT_SECOND (sep at index %d) :: %s' % (f, start + 1, seps[0], head))
            elif len(set(ncols)) > 1:
                # header width is authoritative; report each row that disagrees with it
                width = ncells(block[0])
                for k, b in enumerate(block):
                    if is_sep(b) or ncells(b) == width:
                        continue
                    why = 'UNESCAPED_PIPE_IN_MATH' if re.search(r'[^\s\\|]\|[^\s|]', b) else 'CELL_COUNT'
                    print('%s:%d: %s header=%d row=%d :: %s' % (
                        f, start + 1 + k, why, width, ncells(b), b.strip()[:90]))
        else:
            i += 1
