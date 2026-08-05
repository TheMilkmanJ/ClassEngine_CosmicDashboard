# ChatGPT purple slice 15 - reader-facing wording cleanup and docs-side freeze (2026-08-05)

Purpose: close the last forward-facing wording defects that were still safely editable after the
currency sweeps and blocker-card passes.

This slice does **not** change any grade, claim, number, gate, or route. It only removes
writer/process phrasing from live shelf files so the docs read as reader-facing statements instead
of desk instructions.

## Defects targeted

The remaining fixable class was:

- forward-facing lines that still said things like "any manuscript must ..." or "desk does not ..."
- owner-hold language that was true in substance but phrased as internal operations instead of as
  ship-path constraints

## Files updated

- `docs/PRTOE_quantum_gravity.md`
- `docs/exploratory/PRTOE_hierarchy_problem.md`
- `docs/PRTOE_neutrino_home.md`
- `docs/PRTOE_fairbank_note_draft.md`

## Exact cures

### 1. `PRTOE_quantum_gravity.md`

- rewrote "it is what any manuscript must say" to "it is the correct reader-facing formulation"
- rewrote "Any manuscript must give -1/2 ..." to "The reader-facing form should therefore give
  -1/2 ..."

These are phrasing-only cures. The supertrace content, numbers, and claim scope are unchanged.

### 2. `docs/exploratory/PRTOE_hierarchy_problem.md`

- rewrote "any manuscript must present the anchor ..." to direct shelf language:
  "the anchor has to be presented as conditional on horn (b) ..."

Again, no change to the ontology fork, conditionality, or status.

### 3. `docs/PRTOE_neutrino_home.md`

- rewrote the Fairbank HOLD banner line from "desk does not email / endorse / post" to the
  reader-facing constraint "owner-controlled correspondence / endorsement / posting path only"
- rewrote the companion residual-freeze sentence the same way

No change to the Fairbank hold state, ship path, or posting constraints.

### 4. `docs/PRTOE_fairbank_note_draft.md`

- rewrote the top status banner from desk-instruction phrasing to ship-path phrasing:
  owner-controlled correspondence path only; no endorsement claimed; no second Fairbank TeX in the
  ship path
- rewrote the claims-ledger row to the same reader-facing formulation

No change to the scientific content, claim grades, or the owner-hold state.

## Verification after editing

Forward-facing leak sweep:

- `rg -n "desk does not|any manuscript must|owner-only|owner only" docs --glob '*.md' --glob '!docs/working_logs/**' --glob '!docs/historical_*/**'`
- result: **no remaining matches**

Interpretation:

- the bounded docs-side cleanup is now at a safe stop
- the remaining non-closed items are not wording defects; they are owner decisions, machine gates,
  theory debts, or external referee blockers

## Deliberately not touched

- owner actions / registry decisions
- machine-gated blockers (`bbnfix`, `routeD`, `conv_desi`, `zon_disp`)
- external/posting holds (Fairbank, lattice, T14)
- broad `working_logs/` and `historical_*` records that intentionally preserve process language

## Review request for Claude

Please verify:

1. the four wording patches are purely reader-facing and did not change substance
2. the forward-facing leak sweep is genuinely zero for the targeted phrases
3. this slice is a real docs-side stopping point rather than a hidden content rewrite
