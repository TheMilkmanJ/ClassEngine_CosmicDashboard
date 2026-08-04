# EDITS — arXiv currency hygiene 2026-08-04

Only packaging / status language. No physics claims invented. No TeX rebuild. No DOI invent.

## Files changed

| path | change |
|---|---|
| `papers/bbn-eps-bound/README.md` | Folder-contents line: tarball was documented as ``main.tex`` only; corrected to ``main.tex`` + ``recompute_eps_bound.py`` (matches audit tar members and the recompute section already in the same README). Dual stamp left as-is (already correct). |
| `docs/arXivReady/README.md` | BBN READY row: added dual stamp language — ε 2σ 3.196%≈3.20% **ARITHMETIC VERIFIED (internal)**; **EXTERNAL WIN PENDING (no DOI)** — for consistency with `papers/bbn-eps-bound/README.md` and owner checklist. |

## Files written (run package only)

| path | change |
|---|---|
| `docs/working_logs/_runs/arxiv_currency_20260804/audit.log` | stdout of `python3 scripts/arxiv_package_audit.py` |
| `docs/working_logs/_runs/arxiv_currency_20260804/md5_check.log` | papers vs arXivReady MD5 for 6 tar + 6 pdf |
| `docs/working_logs/_runs/arxiv_currency_20260804/bbn_recompute.log` | stranger recompute PASS |
| `docs/working_logs/_runs/arxiv_currency_20260804/REPORT.md` | full hygiene report + score |
| `docs/working_logs/_runs/arxiv_currency_20260804/EDITS.md` | this file |

## Files refreshed by audit script (not hand-edited)

| path | change |
|---|---|
| `docs/working_logs/_PACKAGE_AUDIT.md` | rewritten by `scripts/arxiv_package_audit.py` (6/6 clean) |

## Not changed (verified current)

| path | note |
|---|---|
| `ForJustin/ARXIV_OWNER_CHECKLIST.md` | already 2026-08-04 dual stamp + HOLD; no edit |
| `papers/*/main.tex`, tarballs, PDFs | hygiene clean; MD5 MATCH staged copies |
| `docs/arXivReady/*.{pdf,tar.gz}` | MD5 MATCH papers; no refresh needed |
| any other `papers/*/README.md` | no EXTERNAL WIN DELIVERED; no bookable H₀ |

## Audit score after edits

**6/6 PASS** (unchanged — edits were doc consistency only).
