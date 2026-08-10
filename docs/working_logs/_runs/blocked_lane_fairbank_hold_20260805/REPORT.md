# Blocked lane audit — Fairbank hold / neutrino-mbb posting path (2026-08-05)

Purpose: freeze the owner-hold state on the neutrino package path exactly, so the neutrino shelf
stops restating the same posting restrictions in slightly different ways.

## Lane

Primary blocked lane for:

- `docs/PRTOE_neutrino_home.md`
- `docs/PRTOE_neutrino_sector.md`

Secondary spillover:

- `docs/PRTOE_fairbank_note_draft.md`

This lane controls whether the desk may quote:

- the `neutrino-mbb` package as posted
- any Fairbank correspondence as sent by the desk
- any second Fairbank-specific TeX package

## Authority sources

Exact authority used for this freeze:

- `docs/PRTOE_neutrino_home.md`
- `docs/PRTOE_neutrino_sector.md`
- `docs/PRTOE_fairbank_note_draft.md`
- `docs/working_logs/_runs/arxiv_owner_prep_20260804/REPORT.md`
- `docs/working_logs/_runs/neutrino_full_honesty_20260804/REPORT.md`

## Exact state

### 1. The ship artifact is ready, but not posted

Current shelf state:

- `papers/neutrino-mbb/` is the only ship artifact
- it is `READY_PACKAGE`
- owner submitted that package to William Fairbank on `2026-08-03`
- no arXiv post is claimed

Referee read:

- package readiness is real
- posting is paused

### 2. The Fairbank path is owner-only

Current hold rules on shelf:

- desk does not email Fairbank
- desk does not invent endorsement
- desk does not invent an arXiv ID
- desk does not invent a second Fairbank TeX

Referee read:

- this is an owner gate, not a desk-closure lane

### 3. The draft letter is corpus-only

Current shelf state:

- `PRTOE_fairbank_note_draft.md` is an experimental letter draft
- it is explicitly `CORPUS_ONLY`
- it is not a second ship artifact

Referee read:

- the draft note stays as support material only

## What is blocked exactly

| object | current state | why blocked |
|---|---|---|
| `neutrino-mbb` public posting | not posted | Fairbank hold / endorsement gate still live |
| Fairbank letter as a desk action | forbidden | owner-only lane |
| second Fairbank TeX path | forbidden | only `neutrino-mbb` is the ship artifact |

## Allowed

- quote `neutrino-mbb` as `READY_PACKAGE not posted`
- quote Fairbank hold as live owner state
- quote the draft letter as `CORPUS_ONLY`

## Forbidden

- claim the package is posted
- claim the desk emailed Fairbank
- invent endorsement
- invent a second Fairbank TeX or second ship path

## Honest unblock path

There is only one honest closure path:

1. owner receives or decides on the Fairbank branch outcome
2. owner follows the branch table already on disk
3. only then may the posting state change

No docs-only cleanup cures this lane.
