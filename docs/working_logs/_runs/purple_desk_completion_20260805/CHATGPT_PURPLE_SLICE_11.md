# ChatGPT purple slice 11 — helium benchmark correction (2026-08-05)

Purpose: correct the live helium benchmark state, which had drifted from the current literature.

## Work completed in this slice

### 1. Centralized the helium benchmark lane

Filed:

- `docs/working_logs/_runs/blocked_lane_helium_fork_20260805/REPORT.md`

What it freezes:

- LBT Y_p Project IV now gives `Y_p = 0.2458 +- 0.0013`
- EMPRESS XV now gives `Y_p = 0.2402 +- 0.0040`
- the old `0.2453 / 0.2370` pair is stale as live benchmark prose

### 2. Rewired the affected shelf surfaces

Updated:

- `docs/PRTOE_bbn_witness.md`
- `docs/PRTOE_READERS_RISK.md`
- `docs/PRTOE_fairbank_note_draft.md`

Net effect:

- the shelf no longer treats the pre-2026 helium pair as the current outside state
- the model's helium direction stays adverse, but old benchmark sigma language is no longer allowed
  to stand as live currency
