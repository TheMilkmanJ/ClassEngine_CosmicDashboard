# ChatGPT purple slice 04 — source-note boundary + major-doc matrix

Date: 2026-08-05

## Purpose

Finish both remaining purple-lane tasks that were still desk-closeable without inventing science:

1. harden the source-note / ship-artifact boundary on the strongest near-paper hubs
2. build a strict top-level-doc matrix that says which files are actually promotion targets,
   which are blocked, and which should stay on the shelf

## What changed

### 1. Hub boundary hardening

Updated:

- `docs/PRTOE_MATH_SPINE.md`
- `docs/PRTOE_induced_gravity.md`

Changes:

- `PRTOE_MATH_SPINE.md` now says explicitly near the top that the spine is a **corpus hub**, not a
  submission artifact, and that the only live paper extraction from it is
  `papers/kination-tracking-note/`.
- `PRTOE_induced_gravity.md` now says explicitly that no standalone paper should be cut from the
  full attach file and that the public algebra slice is `supertrace-note`, not this wider hub.

Why:

- the old state still required the candidacy audit to carry too much of the “ship the slice, not
  the hub” interpretation
- making the boundary explicit in the source files reduces future relapse into fake promotion

### 2. Major-doc matrix

Created:

- `docs/working_logs/_runs/purple_desk_completion_20260805/MAJOR_DOC_ARXIV_MATRIX.md`

Scope:

- current top-level `docs/PRTOE_*.md` only
- **61** live disk files
- excluded exploratory tree / history / `papers/` / `arXivReady/`

Matrix statuses:

- `ARXIV_READY`
- `BLOCKED`
- `EXPLORATORY`

Counts:

- `ARXIV_READY = 4`
- `BLOCKED = 20`
- `EXPLORATORY = 37`

`ARXIV_READY` top-level source notes:

- `PRTOE_bbn_witness.md`
- `PRTOE_lattice_note.md`
- `PRTOE_neutrino_sector.md`
- `PRTOE_radio_lattice.md`

Important explicit rule recorded there:

- extracted packages do **not** auto-promote the parent hub

That is why:

- `PRTOE_MATH_SPINE.md` stays `EXPLORATORY` even though `kination-tracking-note` is ready
- `PRTOE_quantum_gravity.md` stays `EXPLORATORY` even though `supertrace-note` is already shipped

## What this did not do

- no grade promotions
- no chain booking
- no claim that blocked theory / machine files became arXiv-ready
- no rewriting of exploratory hubs into fake papers

## Desk judgment

This materially improves the docs shelf because the promotion queue is now finite and explicit.
Further progress on the `BLOCKED` set is mostly not a docs-cleanup problem anymore.
