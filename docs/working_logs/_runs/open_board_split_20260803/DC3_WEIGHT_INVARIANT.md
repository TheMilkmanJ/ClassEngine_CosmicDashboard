# DC3 — Weight-invariant reach diagnostic

**Date:** 2026-08-03  
**Source:** Claude open-board-split red (R-C DC3 / reconcile union)  
**Owner path:** Grok blue — scorecard + coevolve audit fields only  
**Claim fence:** `page_curve_claimed` stays **false**. No Page turn claimed. No CANDIDATE filing.

---

## Why this exists

Red found that late dynamical reach \(v \ge 0.9\) on coevolve-class instruments can be
**weight-borne, not quanta-borne**:

- `energy_cov` multiplies core covariance diagonals by a scheduled free frequency
  \(w_c(f)\) that decays after `W_C_HOLD`.
- Shrinking \(w_c\) shrinks \(E_\mathrm{core}\) even when occupation excess is fixed,
  which inflates
  \[
  v = \frac{E_\mathrm{rad}}{E_\mathrm{rad}+E_\mathrm{core}}.
  \]
- Recomputing \(v\) with frequency weights **frozen at initial values** collapsed an
  example late reach \(0.9 \to 0.12\) — “v-blend one level down” (deny-on-sight).

**DC3 (binding design condition):** reach must survive frozen-weight recompute
(\(v \ge 0.9\) dynamically **and** weight-invariantly). Artifact should store enough
per-frame data that red can recompute from arrays alone.

This is **not** the same as DC2 (`no_v_blend`: no schedule variable in the *v line*).
A pure energy fraction can still be weight-borne via \(w_c(f)\) inside absolute energy.

---

## Implementation choice

### Scorecard (`scripts/page_protocol_scorecard.py`)

New diagnostic: `eval_weight_invariant_reach` → top-level key **`weight_invariant_reach`**.

| Status | Meaning |
|---|---|
| `PASS` | Frozen-weight envelope late \(u_\mathrm{frozen} \ge 0.9\) |
| `FAIL` | Computable and \(u_\mathrm{frozen} < 0.9\) (weight-borne / short reach) |
| `NOT_COMPUTABLE` | Insufficient stored fields — **no invented numbers** |

**Computable methods (first match):**

1. **`e_c_raw_stored`** — per-frame `e_c_raw` or `E_core_raw` + `E_rad`  
   (preferred; unit-weight core excess).
2. **`w_c_stored_invert`** — per-frame `w_c` + `E_core`/`E_rad`; invert
   \(e_{c,\mathrm{raw}} = E_\mathrm{core}/w_c\), then freeze at \(w_{c0}=1\).
3. **`schedule_pins_reconstruct`** — `E_core`/`E_rad`/`f` on every frame **and**
   top-level `schedule_pins.W_C_HOLD` + `W_C_DECAY` (floor `0.005`, matching
   coevolve / candidate_rebuild). Reconstruct \(w_c(f)\) and invert.

Otherwise → `NOT_COMPUTABLE` with a `missing` list. Gamma diagonals are **not**
required when invert assumptions hold, and are **not invented** when they do not.

**Binding gate (when available):**

- If computable and `weight_invariant_ok is False` → **`CANDIDATE_TURN_binding = False`**
  even if T1–T6 and T8 pass.
- If `NOT_COMPUTABLE` → does **not** invent a pass and does **not** auto-fail older
  artifacts that lack audit fields (`DC3_weight_invariant_gated_binding: false`).
- Flag: `DC3_weight_invariant_gated_binding` = whether DC3 entered the binding AND.

**Structural tag (not a DC3 pass):**

- If `design.no_v_blend` or pure `E_rad/(E_rad+E_core)` v_definition →
  `structural_tag: STRUCTURAL_PURE_ENERGY_FRACTION` with explicit caveat that
  absolute energy may still use time-dependent free frequencies.
- This certifies **DC2 hygiene only**.

Reported numbers when computable (no fabrication beyond invert from stored arrays):

- `v_frozen_raw_late`, `v_frozen_envelope_late`
- `v_dynamic_raw_late`, `v_dynamic_envelope_late`
- `reach_collapse_dyn_env_minus_frozen_env`
- `w_c_late`, `w_c_min`, `method`, `honesty_limits`

Threshold: frozen **envelope** \(\ge 0.9\) (apples-to-apples with T2 reach on \(u=\max_{s\le t} v\)).

### Coevolve (`scripts/quantum_page_coevolve.py`) — option (a) audit store

Future write-once artifacts store per frame:

| key | content |
|---|---|
| `w_c` | core free frequency at that \(f\) |
| `e_c_raw` | occupation excess before \(w_c\) (unit weight) |

`energy_cov` now returns `(E_core, E_rad, w_c, e_c_raw)` with
\(E_\mathrm{core} = w_c \cdot e_{c,\mathrm{raw}}\) (then non-negative clamp).

`design.weight_invariant_audit` documents the store. **Existing** scored artifacts
(`coevolve_v1.json`, etc.) are not rewritten (immutability); scorecard still
computes via `schedule_pins_reconstruct` when pins are present.

---

## Honesty limits (do not over-claim)

1. **No Page turn / no claim.** Diagnostic only. `page_curve_claimed` forced false.
2. **Invert assumption.** Reconstruct/invert paths assume
   \(E_\mathrm{core} = w_c \cdot e_{c,\mathrm{raw}}\) as in coevolve `energy_cov`.
   If a producer used a different energy formula, `schedule_pins_reconstruct` is wrong;
   prefer stored `e_c_raw`.
3. **Clamp.** Stored `E_core = max(w_c * e_c_raw, 0)`. If raw excess was negative and
   clamped, invert under-reports excess as 0.
4. **Radiation weights.** `E_rad` is used as stored (coevolve `omega_r` is fixed from
   week2 modes; no f-dependent rad free frequency in that instrument).
5. **`NOT_COMPUTABLE` is not a pass.** Artifacts without pins / raw series cannot be
   green-lit on DC3 by silence.
6. **`STRUCTURAL_PURE_ENERGY_FRACTION` is not quanta-borne reach.** DC2 ≠ DC3.
7. **Existing coevolve_v1 (example):** scorecard reports
   `weight_invariant_reach: FAIL` via `schedule_pins_reconstruct` —
   frozen envelope \(\approx 0.877 < 0.9\) while dynamic envelope \(\approx 0.998\).
   Binding remains false (also from coevolution_gates / claim-decoupling).

---

## Files touched

| path | change |
|---|---|
| `scripts/page_protocol_scorecard.py` | `eval_weight_invariant_reach`; gate binding when FAIL computable; print block |
| `scripts/quantum_page_coevolve.py` | store `w_c`, `e_c_raw`; design audit note |
| this doc | explanation + honesty limits |

---

## What was *not* done

- No `page_curve_claimed: true`
- No CANDIDATE packet
- No overwrite of scored `coevolve_v*.json`
- No PolyChord / MCMC
- No invented frozen-\(v\) numbers when fields missing

*NO FABRICATIONS.*
