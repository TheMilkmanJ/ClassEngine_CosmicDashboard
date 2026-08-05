# Blocked lane — T14 production sign / IGMF helicity family

**Run id:** `blocked_lane_t14_igmf_sign_20260805`
**Date:** 2026-08-05
**Seat:** Claude (purple)
**Owner half:** Claude, per `purple_desk_completion_20260805/CLAUDE_RETURN_SPLIT_50_50.md`
**Status:** **OPEN-MACHINE / NOT BOOKABLE** — production sign is not available, and this card says why in one place.

**Every number below was read from the artifact or the source by this seat.** Nothing is carried from a log, a receipt, or another seat's summary.

---

## 1. The one-line status

> **The overall four-branch production sign is NOT BOOKABLE.** The run produced a real two-branch antisymmetry result at `f = +1`; the `f = −1` branches did not form a ring and are **NOT_MEASURED**, not passes. **The matter–helicity lock is void** and nothing here revives it.

Any shelf file needing T14 sign status cites **this card** and stops.

---

## 2. The deciding run

| field | value |
|---|---|
| run | `t14_i6_prod_20260804_230225` |
| stages | calibrate → `null_nowinding` → `null_nojet` → `four_branch` (all four ran) |
| four_branch elapsed | 15,266 s ≈ **4.24 h** |
| artifact | `four_branch/summary.json` (4,793 B, 2026-08-05 07:50:31) |

**Do not read the `four_branch/summary.json` under `t14_hkin_i6_prod_20260803_090317` as this run.** That is an older production and is a different object.

---

## 3. The four branches, as the artifact reports them

| branch | n | f | t | helA | ampA | H | dial_spread | margin_ok |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `n+1_f+1` | +1 | +1 | **1.00** | −1 | **1.69632** | +1.9331 | 5.38e−02 | **True** |
| `n−1_f+1` | −1 | +1 | **1.00** | +1 | **1.41759** | −1.9929 | 5.92e−02 | **True** |
| `n+1_f−1` | +1 | −1 | **0.25** | 0 | **0.00122** | +2.0000 | **1.48e−16** | **False** |
| `n−1_f−1` | −1 | −1 | **0.25** | 0 | **0.00087** | −2.0000 | **3.31e−16** | **False** |

---

## 4. Why two branches are NOT_MEASURED, not failures and not zeros

`scripts/ring_toroidal_hkin.py:292-293`, verbatim:

```
# i4: noise floor from n=0 null (spurious helA at amp~0.05)
helA = float(np.sign(np.imag(z1 * np.conj(r1)))) if amp > 0.15 else 0.0
```

The `f = −1` branches carry `ampA` of **0.00122** and **0.00087** — roughly **140× and 170× below** the instrument's own 0.15 floor. **`helA = 0` there is the instrument declining to report, not a helicity of zero.** Three corroborating tells, all in the artifact:

1. **`dial_spread ≈ 1e−16`** — machine epsilon. `H = ±2.0000` across all 18 dials is a constant, not a scan that held.
2. **`t = 0.25` against the live pair's `t = 1.00`.** The frame rule (`ring_toroidal_hkin.py:11-13`) takes the first qualifying frame and *prefers* `t = 1.00` when it also qualifies — so for these branches `t = 1.00` **never qualified**.
3. Both are now flagged `verdict_null` / `not_measured` at `fill_t14_i6_tc_when_ready.py:107-121` (`below_floor = amp <= 0.15`).

**Correct language:** *not measured*. **Forbidden:** "failed", "gave zero helicity", "the negative-fountain branches disagree".

---

## 5. What the run *did* establish, and it is real

Flip `n` at fixed `f = +1` and the instrument flips sign cleanly:

| | `n+1_f+1` | `n−1_f+1` |
|---|---:|---:|
| helA | **−1** | **+1** |
| H | **+1.9331** | **−1.9929** |
| ampA | 1.69632 | 1.41759 |

Real amplitude, real dial spread (~0.054–0.059), matched `t = 1.00`. **This is antisymmetry in `n` at fixed `f = +1` — a two-branch candidate result, and it is worth having.**

It is **not** the test the run was built for. The header's parity requirement is `(n, +z) ↔ (−n, −z) ⟹ H → −H`, and that diagonal is exactly what the two unmeasured branches were to supply.

---

## 6. Gate state — both instrument gates now refuse correctly

**Booking string, verbatim from the artifact:**

> *"antisymmetry in n CONFIRMED at f=+1 only (two branches, t=1.00); f=−1 branches NOT_MEASURED (ampA below instrument 0.15 helA floor); overall four-branch sign NOT BOOKABLE"*

**Emitted gate card** (`TC_GATES_R3b.md`):

| gate | result |
|---|---|
| Mirror `(n+1_f+1) ↔ (n−1_f−1)` | **N/A — unmeasured branch in pair** |
| Mirror `(n+1_f−1) ↔ (n−1_f+1)` | **N/A — unmeasured branch in pair** |
| `mirror_ok` | **False** (unmeasured branch in pair — red R3-b) |
| True-mirror residual <5% | **FAIL/TBD** |
| Margins all four | **False** |

`eligible` is blocked **twice over and independently** — `all_have_verdict` (2 measured ≠ 4 rows) and `len(not_measured) == 0`.

**Two red findings, both cured and verified in the artifact:**

- **R3** — per-branch `margin_ok: True` on sub-floor branches was a pass earned by absence. Now `False`.
- **R3-b** — every mirror pair crosses one measured against one unmeasured branch, so `mirror_ok` was scoring half on the noise-floor constant ±2.0000. Now refuses.

**No false book was ever produced.** `eligible` was False throughout. Both were defects in what the scorecard *reported*.

---

## 7. Downstream — what this lane does and does not license

| statement | status |
|---|---|
| Four-branch production sign | **NOT BOOKABLE** |
| `f = +1` antisymmetry in `n` | **two-branch candidate evidence only** |
| `f = −1` branches | **NOT_MEASURED** |
| **Matter–helicity lock** | **VOID** — established corpus position (`PRTOE_igmf_helicity.md:10`, `PRTOE_baryogenesis.md:77`, non-claim at `PRTOE_cosmic_magnetism.md:239`). This run does **not** revive it. |
| Void IGMF ×20 shortfall | **untouched** — separate lane (`void_door_A_lit_20260805`), still OPEN-BLOCKED |
| COMPLETE physics | **0** |

---

## 8. What would unblock the sign

1. **Make the `f = −1` branches form a ring** — initial condition or `T_MAX` — then re-run and compare all four **at matched `t`**. This is the only route that produces a four-branch sign.
2. Anything short of that leaves a two-branch candidate. **A two-branch result cannot be promoted to a four-branch sign by restating it.**

Not unblocking: re-aggregating, re-wording the booking string, or lowering the 0.15 floor. The floor is the instrument's own guard against spurious helicity at `amp ~ 0.05`; moving it to admit `amp ~ 0.001` would manufacture the measurement it is there to prevent.

---

## 9. Dependent docs

| file | what it takes from here |
|---|---|
| `docs/PRTOE_igmf_helicity.md` | production-sign status; NOT_MEASURED language; lock void |
| `docs/PRTOE_cosmic_magnetism.md` | non-claim list; sign not available |
| `purple_desk_completion_20260805/MAJOR_DOC_ARXIV_MATRIX.md` | T14 row |

---

*NO FABRICATIONS. exit 0 ≠ PASS. A noise-floor zero is not a measurement, and a constant from an empty field is the easiest thing to mirror.*
