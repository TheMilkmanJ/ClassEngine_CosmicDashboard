import re, sys
from collections import Counter

files = [
    "docs/PRTOE_honest_status.md",
    "docs/PRTOE_MATH_SPINE.md",
    "docs/PRTOE_PREREGISTERED_PREDICTIONS.md",
    "docs/PRTOE_READERS_RISK.md",
    "docs/PRTOE_INDEX.md",
]

pats = {
    'revision_verb': r'\b(corrected|correction|fixed|fix|repaired|repair|revised|revision|updated|update|superseded|supersedes|withdrawn|withdraw|retracted|amended|patched|rewrote|rewritten|restored|removed|deleted)\b',
    'self_reference': r'(this (file|document|doc|note|section|table|entry|page)|earlier version|previous version|see above|see below|prior draft|the audit|this audit|this seat|red team|blue team|tribunal)',
    'date_2026': r'2026[-_/ ]?[0-9]{2}',
    'repair_log': r'(repair log|repair-log|repaired on|was wrong|had been wrong|error was|bug was|mistake|typo|erratum|changelog|revision history)',
    'stale_chain': r'(R-1|R−1|chain|MCMC|Gelman|converg|running|in progress|ongoing|pending|preliminary)',
    'soft_complete': r'\b(COMPLETE|complete|done|closed|resolved|settled|final|locked|derived|proven|established)\b',
}

total = 0
for f in files:
    txt = open(f).read()
    paras = re.split(r'\n\s*\n', txt)
    ln = 1
    hits = []
    for p in paras:
        nl = p.count('\n') + 1
        cls = [k for k, v in pats.items() if re.search(v, p, re.I)]
        if cls:
            hits.append((ln, cls))
        ln += nl + 1
    total += len(hits)
    c = Counter(k for _, cl in hits for k in cl)
    print("%s: paras=%d candidates=%d  %s" % (f, len(paras), len(hits), dict(c)))
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        for ln, cls in hits:
            print("   L%-5d %s" % (ln, ','.join(cls)))
print("TOTAL candidate paragraphs: %d" % total)
