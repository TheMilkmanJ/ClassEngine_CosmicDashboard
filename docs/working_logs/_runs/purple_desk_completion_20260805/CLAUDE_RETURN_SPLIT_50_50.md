# Claude return split — 50/50 draft (2026-08-05)

Purpose: pre-split the remaining docs-hardening / blocked-lane queue so Claude can resume on a
finite half instead of reopening routing drift.

## Ground rules

- no fabrication
- exact authority cards first, then dependent docs
- no grade promotion without the real blocker closing
- tribunal file and working-log artifacts stay authoritative over memory

## ChatGPT half

Retained by ChatGPT while Claude was asleep:

1. `BipoSH / axis-family` blocker centralization
   - status: **DONE** in `blocked_lane_biposh_axis_20260805/REPORT.md`
   - dependent docs already rewired
2. Next retained blocker family after BipoSH:
   - `deuterium / radio referee` lane — **DONE** in `blocked_lane_deuterium_fork_20260805/REPORT.md`
   - `lss_parity / DESI 4PCF` lane
3. Matrix / cures / tribunal synchronization for the retained half

## Claude half

Start here on return:

1. `T14 / IGMF sign` blocker family
   - build one exact authority card for current production-sign status
   - dependent docs:
     - `docs/PRTOE_igmf_helicity.md`
     - `docs/PRTOE_cosmic_magnetism.md`
     - `docs/working_logs/_runs/purple_desk_completion_20260805/MAJOR_DOC_ARXIV_MATRIX.md`
   - binding facts to preserve:
     - overall four-branch production sign is **NOT BOOKABLE**
     - `f = +1` gives two-branch candidate evidence only
     - `f = -1` branches are **NOT_MEASURED**, not passes
     - matter-helicity lock is **void**
2. Purple-package review
   - review `CHATGPT_PURPLE_SLICE_01.md` through `CHATGPT_PURPLE_SLICE_09.md`
   - review `CURES.md`
   - review `MAJOR_DOC_ARXIV_MATRIX.md`
   - either `AGREE` or flag exact defects in the tribunal file

## Why this is 50/50 enough

The split is by blocker families, not by raw file count:

- ChatGPT keeps the analysis/external-referee half
- Claude gets the production-sign / chirality-family half plus audit review

That avoids both seats editing the same blocker family at once.

## Wake instructions for Claude

On return, Claude should:

1. read this split file
2. read `blocked_lane_biposh_axis_20260805/REPORT.md` and
   `blocked_lane_deuterium_fork_20260805/REPORT.md` for the half already retained by ChatGPT
3. take the `T14 / IGMF sign` family as the first owned lane
4. report review verdicts on the purple slices and matrix in `ForGrok&Claude.md`
