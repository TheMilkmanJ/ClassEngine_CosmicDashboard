# ChatGPT purple slice 02 (2026-08-05)

## Scope

- file: `docs/PRTOE_READERS_RISK.md`
- scoped sections examined: status banner, H0-evidence warning block, live chain table, basin-status paragraph, summary table
- scoped paragraphs examined: **11**

## Findings

### Finding 1 — stale current-state banner

The top `Status (2026-08-05 currency)` banner still claimed:

- lcdm `R−1 = 0.047912`, `N = 24858`, `converged: false`
- booking card `bbnfix_booking_20260805_170213`
- both bbnfix legs `converged: false`

That banner was stale after lcdm self-stopped.

### Finding 2 — stale mid-file bbnfix callback

Section `§3c` still described the pair as "converging but not bookable" using the old lcdm
sub-stop/no-self-stop state, rather than the current mixed-ready state.

### Finding 3 — stale live chain table

The live chain table still listed lcdm as:

- `R−1 = 0.047912`
- `N = 24858`
- `converged = false`

That table is explicitly presented as live status, so the stale control-leg row was a real defect.

### Finding 4 — stale basin-status prose

The later basin-status paragraph still said neither checkpoint had self-stopped. That was no longer
true once lcdm reached `converged: true`.

### Finding 5 — stale summary-table row

Summary row `#5` still carried the old lcdm status and the false statement that both legs were
`converged:false`.

## Cures applied

### Cure set

Updated all five current-state references so they now agree with live disk state:

- lcdm `0.049324 @ N=26294`, `converged: true`
- dyad `0.056889 @ N=24677`, `converged: false`
- one ready leg does **not** open the pair
- booking still `REFUSED`
- current refuse card now points to `bbnfix_booking_20260805_183401`

## Counts

- defects found: **5**
- defects cured: **5**

## Not claimed

- no change to evidence grade
- no bankable H₀ / Σm_ν / S₈ claim
- no claim that the whole file is "clean"
- no claim that the rest of the purple file list is reviewed

## Next docs still owed after this slice

- `docs/PRTOE_MATH_SPINE.md`
- `docs/PRTOE_PREREGISTERED_PREDICTIONS.md`
- `docs/PRTOE_INDEX.md`
- remaining blue-list docs untouched in this package
