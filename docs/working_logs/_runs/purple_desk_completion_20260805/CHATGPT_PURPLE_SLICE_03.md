# ChatGPT purple slice 03 (2026-08-05)

## Scope

- files examined:
  - `docs/PRTOE_INDEX.md`
  - `docs/PRTOE_CHAIN_TABLES.md`
  - `docs/PRTOE_CODE_MANIFEST.md`
  - `docs/PRTOE_REFEREE_CALENDAR.md`
  - `docs/PRTOE_DEPENDENCY_TREE.md`
  - `docs/PRTOE_READERS_GUIDE.md`
  - `docs/PRTOE_hubble_tension.md`
  - `docs/PRTOE_neutrino_home.md`
  - `docs/PRTOE_fairbank_note_draft.md`
  - `docs/PRTOE_DOMAIN_COVERAGE.md`
  - `docs/PRTOE_MATH_SPINE.md`
  - `docs/PRTOE_PREREGISTERED_PREDICTIONS.md`
  - `docs/PRTOE_s8_growth.md`
  - `docs/working_logs/_PROJECT_FINISH_ROADMAP.md`
- scope type: current-state shelf sweep for machine-currency consistency
- targeted patterns:
  - stale lcdm control-leg state
  - stale routeD live stamp
  - stale refuse-card pointers
  - intra-shelf timestamp drift on the live lcdm row

## Findings

### Finding 1 — stale self-stop transition was replicated across shelf surfaces

After lcdm self-stopped, multiple live docs still described the control leg as:

- `R−1 = 0.047912`
- `N = 24858`
- `converged: false`
- "below stop without self-stop"

That state was no longer current. The live progress row at review time was:

- lcdm `0.049324 @ N=26294`
- timestamp `2026-08-05T11:52:10`
- checkpoint `converged: true`

The pair remained **REFUSED**, but for a different reason: dyad had not cleared its own gate.

### Finding 2 — stale routeD stamp was still echoed in live docs

Several shelf surfaces still carried routeD as:

- `R−1 = 0.705291`
- `N = 6517`
- `~7.05×` stop

That was stale. The live routeD progress row at review time was:

- `0.728432 @ N=8120`
- timestamp `2026-08-05T12:54:11`
- `~7.28×` stop

### Finding 3 — current-state docs had timestamp/card drift

Even after the first cure wave, some docs were split between:

- lcdm timestamp `2026-08-05T08:22:10`
- lcdm timestamp `2026-08-05T11:52:10`

and some still pointed at earlier refuse-card paths. For live currency surfaces, that kind of
drift is a real documentation defect because it makes "current state" ambiguous without opening raw
chain files.

## Cures applied

### Cure set 1 — live shelf state normalized

Updated current-state references so the affected live docs now agree on:

- lcdm `0.049324 @ N=26294 @ 2026-08-05T11:52:10`, `converged: true`
- dyad `0.056889 @ N=24677 @ 2026-08-05T07:54:30`, `converged: false`
- pair still **REFUSED**
- one ready leg does **not** open the pair

### Cure set 2 — routeD live references normalized

Updated routeD references so the affected docs now agree on:

- routeD `0.728432 @ N=8120 @ 2026-08-05T12:54:11`
- `~7.28×` the `0.1` stop
- still **not** dual-gate / not bookable

### Cure set 3 — refuse-card / timestamp drift removed

Repointed the touched live docs to the checked refuse card:

- `docs/working_logs/_runs/bbnfix_booking_20260805_190348/REPORT.md`

and normalized the lcdm live timestamp to the raw latest progress row:

- `2026-08-05T11:52:10`

### Cure set 4 — post-patch grep check

Ran a stale-pattern sweep over the touched live docs for:

- `0.047912`
- `24858`
- `0.705291`
- `6517`
- `08:22:10`
- old refuse-card ids

Result: **no matches** on the targeted shelf surfaces.

## Counts

- files updated in this slice: **14**
- defect classes found: **3**
- defect classes cured: **3**

## Not claimed

- no claim that the entire docs tree is globally complete
- no claim that machine / owner / external blockers are resolved
- no physics promotion
- no booking / `H0` / `Σmν` / `S8` promotion
- no claim that exploratory or historical run artifacts were rewritten

## Residuals still honestly open after this slice

- machine:
  - `dyad_mnu_bbnfix` still not self-stopped
  - `cmp_prtoe_routeD` still far above stop
  - `conv_desi` still unproduced
- owner / external:
  - Fairbank path remains HOLD
  - merge / accept-revert decisions remain owner acts
- theory / derivation:
  - open claims remain open for derivation reasons, not stale-current-state reasons, on the files
    touched in this sweep
