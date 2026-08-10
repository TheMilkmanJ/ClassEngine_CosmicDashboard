# Tribunal process rules — permanent single source (ChatGPT REF)

**Stamp:** 2026-08-04  
**Audience:** ChatGPT (neutral referee memory) · Grok (blue) · Claude (red) · Owner  
**Scope:** process / grading / booking / Page / Strong CP / PolyChord — **NO physics invent**  
**Authority roots:** `ForGrok&Claude.md` REFEREE RECORD board-clear-rules · Claude R5 · board-clear receipt · open-board process police  

This file is the **permanent process rule sheet**. Prefer it over scattered receipts when REF needs a single list. Living board index is separate (delivery vs grade); this sheet is the law.

---

## Rule list (locked)

### 1. exit 0 ≠ PASS

| Term | Means | Does **not** mean |
|---|---|---|
| **exit 0** / ran clean | Script finished without crash | Arithmetic or physics **PASS** |
| **desk audit** | Honest recompute / restate of open debt | Debt closed |
| **PASS** | Explicit verdict (e.g. BBN ε ceiling, area-law quarter, τ Parseval) | Implied by green CLI |

**Implications:**

- Recompute tables may say **N/N ran clean** while only a subset carries explicit **PASS**.
- Labelling desk audits as PASS is the same conflation class as artifact-mismatch overclaims.
- Load-bearing bookings, papers, and grade changes **must not** inherit a fake PASS from a delivery/exit-0 table.

**Origin:** Claude red all-four-lanes AGREE-IF (Lane 2 strike) · ChatGPT REFEREE RECORD board-clear-rules §1 · cures on disk in `shelf_residual_pass_20260804/`, `all4lanes_20260804/`, `open_theory_full_20260804/RECOMPUTES.md`.

Also locked as dual phrasing:

- **DONE on disk ≠ Claude AGREE**
- **delivery ≠ grade** (see Rule 2)

---

### 2. delivered ≠ red-graded

| Board column | Values | Meaning |
|---|---|---|
| **delivery** | DONE / partial / … | Package landed on disk |
| **red** | **none** (default) · AGREE · AGREE-IF · DENIED | Claude verdict only |

**Law:**

- Board `red` column **defaults to `none`** unless Claude filed a verdict.
- Only actual Claude verdicts may elevate `none` → AGREE / AGREE-IF / DENIED.
- Grok/blue delivery does **not** auto-grade packages.
- Load-bearing packages (booking, paper, grade change) get red audit **before** they land forward, not after.

**Locus (living index):**  
[`docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md`](../improve_loop_20260804/BOARD_STATUS.md)

**Origin:** Claude FLAG on board-clear · Grok RECEIPT RED CLOSE three-cures + audit-column · ChatGPT REFEREE RECORD board-clear-rules §2.

---

### 3. Booking gate (bbnfix H₀ / pair tables)

**Both legs required — no soft language:**

1. **Both** chains last-row **R−1 < 0.05** (strict `<`, not `≤`):
   - `dyad_mnu_bbnfix`
   - `cmp_lcdm_mnu_bbnfix`
2. **Both** samplers self-stopped: **`converged: true`** in `.checkpoint` (or cobaya idle after final progress under the bar).

| Forbidden | Why |
|---|---|
| **Peek-book** H₀ / tables while either leg over bar or not self-stopped | Premature posterior is not a booked posterior |
| **Almost bookable** language at R−1 just above/below a bounce | Bounce history (lcdm 0.0488 → 0.059) proved gate discipline |
| **Single-chain watcher** “GATE CROSSED” on one root R−1 | Retired; R−1 is a multi-chain statistic; dual + self-stop both required |

**Authoritative instruments only:**

- `scripts/book_bbnfix_when_ready.py` / `scripts/finalize_h0_at_convergence.py`
- `scripts/bbnfix_mcmc_watch_diag.py` (diag)
- Runbook: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`
- When gate opens (pipeline): `bash scripts/bbnfix_when_ready_all.sh` — post-gate tables still need red path per protocol (no unaudited overwrite of forward-facing chain tables without red seat).

**Retired hazard:** A2 false gate watcher PID 212363 — single-chain R−1 fire without both legs + self-stop.  
Receipt: [`improve_loop_20260804/A2_FALSE_GATE_RETIRED.md`](../improve_loop_20260804/A2_FALSE_GATE_RETIRED.md)

---

### 4. Strong CP — pre-emptive DENY on θ̄ bridges; seat-hunt itch-only OK

| Action | Status |
|---|---|
| **θ̄ / white-hole / reverse / “medium explains Strong CP” bridge** | **PRE-EMPTIVE DENY on sight** (Claude **R5**) |
| Compute lane for θ̄ mechanism | **Forbidden** under current constitution |
| Wording drift “shared itch” → “PRTOE explains θ̄” | **Forbidden** |
| **Seat-hunt itch-only** (parity / missing EM-anomalous angular mode cousin; no mechanism) | **OK** |

**Why DENY (corpus law, not taste):**

- Birefringence is **propagation**, not a white-hole epoch.
- Corpus birefringence = electron/photon anomaly channel (θ·F·F̃); Strong CP = gluon θ̄·G·G̃ — wrong gauge field for a free bridge.
- `PRTOE_strong_cp.md`: needing θ̄ / quark flavour to fit data **kills the constitution**. Silence is load-bearing.

**Itch file (no solution invent):**  
[`physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md`](../physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md)

**Origin:** `RED NOTE R5-strongcp-whitehole` · blue AGREE · ChatGPT REFEREE RECORD board-clear-rules §3.

---

### 5. Page — no CANDIDATE without full gate set; champion v13 near-miss

**No standing CANDIDATE** without **all** of:

- **T1–T8** machine gates  
- **DC3** weight-invariant / quanta-borne reach  
- **claim-decoupling** checklist  
- **red AGREE**

Also required in practice (open-board merge): stall_cap validity, write-once versioned artifacts, no silent overwrite of scorecards.

| Standing | Value |
|---|---|
| Champion | **`coevolve_v13`** (schedule `v23_champion_locked`) |
| Near-miss shape | T1–T6 + T2 + stall_cap + DC3 **PASS**; **T8** early bin **FAIL** (range/S\* ≈ **0.113**, need ≤ 0.10) |
| `CANDIDATE_TURN_binding` | **False** |
| `page_curve_claimed` | **false** |
| Q6 | **OPEN** |
| Thrash | **Stop** pure header / densify / G_TMS retune for T8 — next unblock = licensed **new microphysics** (D4 freeze) |

**Package:** [`page_full_freeze_20260804/`](../page_full_freeze_20260804/)

---

### 6. PolyChord — skip this box

| Rule | Detail |
|---|---|
| **No PolyChord** on this machine / this improve path | Nested evidence deferred (cluster later) |
| Leave production MCMCs alone | No kill / no reseed / no peek-book |
| Standing evidence method until cluster | Laplace-from-MCMC (when booking gate opens) — not invented ΔlnZ |

Owner may reverse PolyChord only as a **deliberate future act**, not casual resumption of mid-prior killed runs.

---

### 7. Pointers (living artifacts)

| What | Path |
|---|---|
| **Board status** (delivery + `red` column) | [`docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md`](../improve_loop_20260804/BOARD_STATUS.md) |
| **Board-clear receipt** (desk queue empty; packages listed) | `ForGrok&Claude.md` → `### RECEIPT board-clear @FROM:GROK` |
| **Claude R5** (Strong CP / white-hole pre-emptive DENY) | `ForGrok&Claude.md` → `### RED NOTE R5-strongcp-whitehole` |
| **ChatGPT REF board-clear-rules** (this sheet’s parent record) | `ForGrok&Claude.md` → `### REFEREE RECORD board-clear-rules` |
| A2 watcher retired | [`improve_loop_20260804/A2_FALSE_GATE_RETIRED.md`](../improve_loop_20260804/A2_FALSE_GATE_RETIRED.md) |
| Booking checklist | [`docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`](../../_POSTERIOR_BOOKING_CHECKLIST.md) |
| Strong CP seat-hunt (itch-only) | [`physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md`](../physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md) |
| Page freeze / champion v13 | [`page_full_freeze_20260804/REPORT.md`](../page_full_freeze_20260804/REPORT.md) |
| Open-board paste pack (REF process police) | [`ForJustin/PASTE_CHATGPT_REF.md`](../../../../ForJustin/PASTE_CHATGPT_REF.md) |
| Tribunal quick card | [`docs/working_logs/TRIBUNAL.md`](../../TRIBUNAL.md) |
| Full seats / TURN BOARD | repo root `ForGrok&Claude.md` |

---

## Standing locks (unchanged by this sheet)

- bbnfix **NOT bookable** until Rule 3  
- **no** Page CANDIDATE · Q6 OPEN · champion v13 near-miss only  
- **θ̄ DENY** standing · seat-hunt itch-only  
- **no** PolyChord this box  
- **no** fabrications / no invent r, H, Born, atom, θ̄ mechanism  
- overall claim-credibility stance **4/10** (open-board record) unless Owner moves it  

---

## RECEIPT block — paste to `ForGrok&Claude.md` if needed

```markdown
### RECEIPT tribunal-process-rules SoT @FROM:GROK @TO:ALL >>BLUE >>REF >>RED

**Permanent single source for ChatGPT REF process memory:**
`docs/working_logs/_runs/tribunal_process_rules_20260804/REPORT.md`

**Rule list locked (no physics invent):**
1. **exit 0 ≠ PASS** (desk audits vs arithmetic PASS; DONE ≠ Claude AGREE)
2. **delivered ≠ red-graded** — board `red` column default **none** (`improve_loop_20260804/BOARD_STATUS.md`)
3. **Booking gate:** both R−1 < 0.05 **AND** `converged: true`; no peek-book; single-chain A2 watcher **retired**
4. **Strong CP:** pre-emptive **DENY** on θ̄ bridges (Claude R5); seat-hunt **itch-only** OK
5. **Page:** no CANDIDATE without T1–T8 + DC3 + claim-decoupling + red; champion **v13** near-miss (T8≈0.113)
6. **PolyChord:** skip this box
7. Pointers: BOARD_STATUS.md · board-clear receipt · Claude R5 · REFEREE RECORD board-clear-rules

**AGREE with** ChatGPT REFEREE RECORD board-clear-rules + Claude R5 DENY + board-clear FLAG.

**WHOSE_TURN →** unchanged (Grok free hygiene / Owner Fairbank / Machine bbnfix / Claude event-driven load-bearing only)
```

---

*NO FABRICATIONS. Process only. This sheet does not book posteriors, close Page, or invent Strong CP.*

## 8. Booking ≠ publishing (Claude RED FINDING 2026-08-04)

- Gate (dual R−1 + self-stop) protects against **early** book.
- Forward-facing `PRTOE_CHAIN_TABLES.md` write is a **separate stage**.
- `bbnfix_when_ready_all.sh` defaults to Stage A only (book + finalize).
- Stage B `--write-tables` requires `bbnfix_booking_*/RED_AUDIT.md` with `red: AGREE` or `AGREE-IF`.
- Package: `booking_pipeline_red_gate_20260804/REPORT.md`

