# ForJustin owner paste pack — full update

**Stamp:** 2026-08-04  
**Mission:** refresh owner paste surfaces so ChatGPT/Claude get current state, not stale open-board thrash.  
**Authority:** `docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md` · book gate **0.059 / 0.189** · page freeze **v13**.  
**Hard rules:** NO invent · NO arXiv post · NO peek-book H₀ · NO PolyChord · NO θ̄ mechanism.

---

## Deliverables written

| path | role |
|---|---|
| [`ForJustin/STATUS_CONTINUE.md`](../../../../ForJustin/STATUS_CONTINUE.md) | Full current: machine R−1, packages + red column, waiting on, board clear, when-ready command |
| [`ForJustin/PASTE_CHATGPT_REF.md`](../../../../ForJustin/PASTE_CHATGPT_REF.md) | REF process rules + open board short + WHOSE_TURN + reply shape |
| [`ForJustin/PASTE_CLAUDE_RED.md`](../../../../ForJustin/PASTE_CLAUDE_RED.md) | What red closed; optional re-verify only; no θ̄; load-bearing audit policy |
| this `REPORT.md` | Package receipt |

---

## Facts frozen into paste (no invention)

### Machine

| fact | value |
|---|---|
| lcdm progress R−1 | **0.059055** (~**0.059**), N=19013, `converged: false` |
| dyad progress R−1 | **0.189201** (~**0.189**), N=18837, `converged: false` |
| bookable | **NO** |
| when-ready | `bash scripts/bbnfix_when_ready_all.sh` (prefer `--skip-tables` until red between book and tables) |

Sources: live progress tails; latest refuse cards under `bbnfix_booking_20260804_*`; `GATE_SNAPSHOT.md` / `BOARD_STATUS.md`.

### Page

| fact | value |
|---|---|
| champion | `coevolve_v13` |
| T1–T6 | PASS |
| T8 | FAIL **0.113** |
| CANDIDATE / claimed | none / false |
| stance | D4 freeze (microphysics only) |

Source: `page_full_freeze_20260804/REPORT.md`.

### Board / red

| fact | value |
|---|---|
| three cures | **CLOSED** (red verified) |
| θ̄ | **DENY standing** |
| audit column | default **none**; delivered ≠ graded |
| process rules (REF) | exit0≠PASS · delivered≠graded · DONE≠AGREE |
| open residual mail | booking-pipeline (book ≠ publish tables) — process, not physics |

Sources: `BOARD_STATUS.md`; tribunal blocks `RED CLOSE three-cures`, `REFEREE RECORD board-clear-rules`, `RED FINDING booking-pipeline`.

### Owner

| fact | value |
|---|---|
| Fairbank / arXiv | **HOLD** — no desk post |
| checklist | `ForJustin/ARXIV_OWNER_CHECKLIST.md` |

---

## What changed vs prior paste packs

| prior paste | now |
|---|---|
| Open-board-split lanes R-A…R-F as primary work | **Stale** as standing work; board cure queue empty |
| Claude “help Grok with open list via full subagent red” | **Optional re-verify** + event-driven load-bearing only |
| ChatGPT “record open board + process police” generic | Explicit **locked** process rules from board-clear REF |
| Machine “0.059/0.189 NOT YET” | Same numbers kept; exact 0.059055 / 0.189201; when-ready command named |
| Packages | Full delivery table + **red** column from `BOARD_STATUS.md` |

---

## Explicit non-actions (this package)

- Did **not** run booking, GetDist, or PolyChord  
- Did **not** post or prepare a new arXiv upload  
- Did **not** invent θ̄ / Page close / CANDIDATE  
- Did **not** kill or reseed MCMCs  
- Did **not** implement the booking-pipeline code cure (documented only for seats)

---

## Owner how-to

1. Paste `ForJustin/PASTE_CHATGPT_REF.md` into ChatGPT when REF memory needs refresh.  
2. Paste `ForJustin/PASTE_CLAUDE_RED.md` into Claude when red needs current closed/open fences.  
3. Read `ForJustin/STATUS_CONTINUE.md` for one-page desk truth.  
4. When bbnfix self-stops both legs with R−1 < 0.05:  
   `bash scripts/bbnfix_when_ready_all.sh --skip-tables` then red-audit before forward tables.

*NO FABRICATIONS.*
