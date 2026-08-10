# ChatGPT purple slice 14 - bbnfix currency sweep and table-render repair (2026-08-05)

Purpose: finish the docs-side fixes that were still safely editable after Claude's later purple
passes:

1. refresh the shared `bbnfix` blocker card to the current verified dyad state
2. propagate that current state through the forward-facing shelf surfaces that were still carrying
   the superseded `0.056889 / 1.14x` stamp or the old refuse-card pointer
3. repair the five table-render defects Claude isolated in PURPLE CLAUDE 03 without changing any
   claim, grade, number, or verdict beyond the live chain stamp

## Inputs verified before editing

- `chains/dyad_mnu_bbnfix.progress`
- `chains/dyad_mnu_bbnfix.checkpoint`
- `chains/cmp_lcdm_mnu_bbnfix.progress`
- `chains/cmp_lcdm_mnu_bbnfix.checkpoint`
- latest booking artifact on disk:
  `docs/working_logs/_runs/bbnfix_booking_20260805_222942/REPORT.md`

Verified current machine truth used in this slice:

- `cmp_lcdm_mnu_bbnfix`: `R-1 = 0.049324`, `N = 26294`, `converged: true`
- `dyad_mnu_bbnfix`: `R-1 = 0.060201`, `N = 26135`, `converged: false`
- `cmp_prtoe_routeD`: `R-1 = 0.728432`, `N = 8120`, `converged: false`
- pair status: still `REFUSED`; one ready leg does not open the pair

## Docs updated

Shared blocker authority:

- `docs/working_logs/_runs/blocked_lane_bbnfix_20260805/REPORT.md`

Forward-facing shelf surfaces refreshed to current dyad currency and shared blocker-card pointers:

- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_DEPENDENCY_TREE.md`
- `docs/PRTOE_CHAIN_TABLES.md`
- `docs/PRTOE_DOMAIN_COVERAGE.md`
- `docs/PRTOE_READERS_GUIDE.md`
- `docs/PRTOE_hubble_tension.md`
- `docs/PRTOE_INDEX.md`
- `docs/PRTOE_neutrino_home.md`
- `docs/PRTOE_CODE_MANIFEST.md`
- `docs/PRTOE_fairbank_note_draft.md`
- `docs/PRTOE_honest_status.md`
- `docs/PRTOE_REFEREE_CALENDAR.md`

Renderer-safe table repairs from PURPLE CLAUDE 03:

- `docs/exploratory/PRTOE_hierarchy_problem.md`
- `docs/exploratory/PRTOE_the_great_chain.md`
- `docs/PRTOE_FAILURES_LEDGER.md`

## Exact cures

### 1. bbnfix currency

- updated the shared blocker card from dyad `0.056889 @ N=24677` to
  `0.060201 @ N=26135`
- replaced old shelf pointers to `bbnfix_booking_20260805_190348` with the shared blocker card in
  the touched forward-facing files
- refreshed prose/table references that still stated dyad as `1.14x stop` to the current
  `1.20x stop`

### 2. table-render defects

The following were repaired mechanically:

- `PRTOE_hierarchy_problem.md:1093`
  - escaped `lambda|S|^2|H|^2` table-cell pipes
- `PRTOE_the_great_chain.md:120`
  - escaped `|Delta mu / mu|`
- `PRTOE_the_great_chain.md:172`
  - escaped `|Delta alpha / alpha|`
- `PRTOE_FAILURES_LEDGER.md:684`
  - collapsed an unintended third table cell into the second cell
- `PRTOE_FAILURES_LEDGER.md:685`
  - collapsed an unintended third table cell into the second cell

No claim wording, grade, or physics result changed in those table repairs.

## Verification after editing

Top-level shelf sweep:

- `rg -n "0.056889|1.14x|bbnfix_booking_20260805_190348" docs/PRTOE_*.md`
- result: no remaining live top-level shelf hits except the deliberate historical comparison phrase
  in `docs/PRTOE_honest_status.md` ("moved away from the bar from 0.056889")

Bounded table-repair verification:

- the five named rows now contain either escaped literal pipes or a single intended second cell
- no new table rows were introduced

## Deliberately not touched

Owner-only / registry decisions from Claude's later purple passes remain untouched:

- `P-2026-004` registry absence
- the five other dangling prediction IDs
- one ID-format decision for the prediction registry
- `Sigma m_nu` registry commitment choice (`61.3 / 61.4 / range`)

Also untouched:

- machine/external blockers (`bbnfix`, `routeD`, `conv_desi`, Fairbank, lattice, T14)
- Claude's `T14 / IGMF sign` lane
- broad historical run logs that intentionally preserve older machine snapshots as archival record

## Review request for Claude

Please review:

1. this slice
2. `CURES.md`
3. the refreshed shared blocker card
4. the five rendering repairs

Expected review scope:

- verify the live chain stamp is copied correctly
- verify no claim/grade drift was introduced
- verify the five table rows now render with intended cell counts
