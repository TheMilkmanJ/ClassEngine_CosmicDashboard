"""Read-only: show what a reader actually sees for a table row whose cell count
disagrees with its header. GFM splits on every unescaped '|' and then truncates
the row to the header's width, so surplus cells are silently dropped.

Usage: python3 show_split.py <file> <1-indexed row line> <header width>
"""
import re
import sys

path, lineno, width = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
line = open(path, encoding='utf-8').read().split('\n')[lineno - 1]
cells = re.split(r'(?<!\\)\|', line.strip().strip('|'))
print('%s:%d  header=%d  row splits into %d' % (path, lineno, width, len(cells)))
for i, c in enumerate(cells):
    tag = 'RENDERED     ' if i < width else '*** DROPPED **'
    print('  cell %2d %s: %s' % (i + 1, tag, c.strip()[:160]))
