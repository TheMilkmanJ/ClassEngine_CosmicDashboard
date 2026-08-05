# DE OCCUPANCY — construction package (coincidence / self-tune)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/void_de_seating/`  
**Date:** 2026-08-04  
**Rule:** NO FABRICATIONS. **Do not claim solves coincidence.** Width ≠ occupancy. No MCMC. No PolyChord.  
**Wall ID:** W2 (DE self-tuning / coincidence occupancy).

---

## Residual one-liner

**DE:** era **width** t_turn ≈ 8.16 H⁻¹ **derived** (√3, B=1/√2, A_s); **occupancy** (“why now” / ~1 in 37) **OPEN**; chain “why this cycle?” **OPEN-BLOCKED**; self-tune / ohmic DE channel **OPEN** (least-trusted joint) — permanent demote of “why now” is allowed.

---

## 0. Paid vs OPEN (status freeze)

| item | grade | evidence |
|---|---|---|
| Γ_par/H_Λ = √3 (IR / critical-k scale) | **derived** | `docs/exploratory/PRTOE_sqrt3_derivation.md`; T8 item 1 |
| B = 1/√2 (Jeans thaw rate ω_J = Γ_par/√2) | **derived** | T8 item 2; coincidence file §1 |
| t_turn = ln(1/√A_s)/(√(3/2)·H) ≈ **8.16 H⁻¹** | **derived** (era width) | A_s = 2.088×10⁻⁹ → 8.1597; closed form −0.35% → 8.1611 (0.02% bracket) |
| Width floor-independent in H⁻¹ units | **derived** | δt/t = δ(ln A_s)/19.99 |
| Occupancy fraction ~2.7% of era elapsed (~1 in 37) | **number only, not selection law** | z≈0.33 crossing = 0.219 H_Λ⁻¹; band ±~2% class on odds |
| Occupancy / “why now” | **OPEN** | residual freeze row 2 |
| Chain-level “why this cycle?” | **OPEN-BLOCKED** | T8 item 4; Tolman + arrow reject anthropic repair |
| DE-floor **stability** (w=−1 attractor + k⁴) | **paid mechanism for floor hold** | `scripts/floor_ghost_condensate.py`; honest_status #22 |
| DE-floor **self-tuning of Λ value** | **fail / OPEN** | ohmic DE channel; Weinberg no-go unaddressed; toy ran away |
| Soft-claim demote (width sold as why-now) | **done 2026-08-03** | title + residual notes; `open_board_split_20260803/SOFT_CLAIM_DEMOTE.md` |

**Stamp (living):** `docs/PRTOE_coincidence_problem.md` — *Width Derived; Occupancy OPEN*.

---

## 1. What width buys (and does not)

**Buys:**

- A dial-free **duration** of the dark-energy era from √3, B=1/√2, and measured A_s.  
- Sharper residual than ΛCDM’s free Λ: “why is Λ this size” → “why are we early in a derived era.”  
- Kill couple: evolving-DE detection (DESI) kills self-timed floor and reopens **era-width** package; **occupancy stays OPEN either way**.

**Does not buy:**

- Observer **placement** inside the era (occupancy).  
- Chain-level cycle selection.  
- A solution of the cosmological-constant / coincidence problem in the ordinary sense.  
- Self-tuning of the floor **value** (settling is ohmic in the DE channel — floor value not fixed by settling).

Direction note (ledger / failures): a *longer* derived era makes early placement **slightly harder**, not easier.

---

## 2. Mechanism requirements list (construction — what would unstick occupancy)

Any future mechanism that claims to answer “why now” must satisfy **all** of the following **before** booking COMPLETE. This is a **requirements list**, not a derivation.

| # | requirement | why | status |
|---|---|---|---|
| R1 | **Separate width from placement** | Width is already paid; mechanism must target *selection of observer-time*, not re-derive t_turn | required |
| R2 | **No anthropic free lunch the model rejects** | Arrow-of-time seating rejects standard anthropic repair (`PRTOE_arrow_of_time.md` §3) | constraint |
| R3 | **Compatible with Tolman chain bookkeeping** | Cycles lengthen; elapsed-time weight prefers *late* cycles — early occupancy is **disfavoured** by own bookkeeping (T8 item 4) | constraint |
| R4 | **Kill band pre-registered** | e.g. if mechanism predicts occupancy odds outside [band] under recorded Ω_Λ/Ω_m → kill | process |
| R5 | **No dial whose job is the coincidence** | √3 chain already forbids a coincidence dial; new mechanism must not reintroduce one | constraint |
| R6 | **Does not sell self-tuning of Λ as occupancy** | Self-tune of floor value is a **different** OPEN (ohmic DE); conflating is soft-claim class | fence |
| R7 | **DESI / w=−1 consistency stated** | Era-width package couples to w=−1 now; occupancy mechanism must declare independence or co-kill | kill couple |
| R8 | **Chain vs era level named** | Era-level occupancy ≠ chain-level “why this cycle?”; closing one does not close the other | scope |

**What would unstick (from residual freeze):**

| residual | what unsticks (honest) |
|---|---|
| Occupancy / “why now” | Observer-selection mechanism meeting R1–R8 **without** inventing rejected anthropics — **or** permanent demote of “why now” as unanswerable |
| Chain cycle selection | Licensed cycle accounting / selection law — not invent |
| DE self-tune / ohmic | Mechanism requirements only for value-fixing; no fake solve of Weinberg no-go |

---

## 3. Dead-lanes survey pointer

Do **not** re-open these as construction without new licensed content. Pointers to existing honesty surfaces:

| dead / failed / conceded lane | where recorded | lesson for construction |
|---|---|---|
| DE self-tuning toy **ran away** | `PRTOE_honest_status.md` #22; least-trusted joint #1 | value-fixing not automatic from settling |
| Self-tuning **fail** with stable floor kept | same; `floor_ghost_condensate.py` | keep w=−1 attractor; **concede** “solves CC / coincidence” |
| Ohmic response in **DE** channel | honest_status (sub-ohmic self-tune is DM channel, not DE) | wrong channel for DE value fix |
| Weinberg no-go unaddressed | honest_status #22 | no desk circumvention without named axiom |
| Soft conflation width = why-now | `SOFT_CLAIM_DEMOTE.md`; failures ledger “CLAIM WAS WIDER” | re-grade: width derived, occupancy not |
| Anthropic repair of early placement | coincidence §2; arrow_of_time reject | not available under model seating |
| Homogeneous P(X) thaw as “why now” | T8 — homogeneous gives settling (wrong sign); Jeans branch is width clock only | width mechanism ≠ occupancy |
| Equipartition / coincidence dresses (broader corpus) | failures ledger many rows | adjacency ≠ closure discipline |

**Survey authority files (absolute paths):**

- `/home/themilkmanj/prtoe_class/docs/PRTOE_coincidence_problem.md`  
- `/home/themilkmanj/prtoe_class/docs/working_logs/T8_coincidence_owed.md`  
- `/home/themilkmanj/prtoe_class/docs/PRTOE_honest_status.md` (§ least-trusted joints; #22)  
- `/home/themilkmanj/prtoe_class/docs/PRTOE_FAILURES_LEDGER.md` (coincidence re-grade §)  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/open_board_split_20260803/SOFT_CLAIM_DEMOTE.md`  
- `/home/themilkmanj/prtoe_class/docs/PRTOE_cosmological_constant.md` (floor / radiative band)  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/THEORY_WALLS_QUEUE_20260803.md` W2  

No new dead-lane **physics** is invented here; this is a **pointer map** for construction triage.

---

## 4. Construction options

### Option D1 — Document-only mechanism requirements (default now)

Keep occupancy OPEN; maintain R1–R8 list; refresh residual freeze hygiene. **No invent.**

### Option D2 — Permanent demote of “why now”

Treat ordinary “why now” as **unanswerable under current axioms**:

- Width remains **derived** (do not demote the √3 chain).  
- Occupancy stays **OPEN** or is re-labeled **permanent non-goal**.  
- Public language: “era duration computed; observer placement not claimed.”

**Permanent demote is an allowed improvement** (walls queue: mechanism walls → demote claims if no licensed derivation).

### Option D3 — Licensed selection mechanism (owner only)

Only if a **named** axiom satisfies R1–R8 with kill band first. **Not stocked.** Do not invent.

### Option D4 — Self-tune value channel (orthogonal construction)

Separate program for DE **value** self-tuning (ohmic / Weinberg). Explicitly **not** occupancy close. Requirements: address Weinberg no-go with named loophole **or** concede permanently (already partially conceded).

---

## 5. Forbidden

1. “Solves coincidence.”  
2. Sell width / √3 / t_turn as “why now answered.”  
3. Anthropic free lunch against arrow seating.  
4. Invent chain selection law.  
5. Conflate DE self-tune value-fix with occupancy.  
6. Quote occupancy as exact fixed odds (radiative band ± class).  
7. MCMC / PolyChord as theory close.  
8. Strong CP / θ̄ linkage (abstention — out of this wall).

---

## 6. Residual freeze crosswalk

| residual | grade | blocker |
|---|---|---|
| Occupancy / “why now” | **OPEN** | no selection mechanism meeting R1–R8 |
| Chain “why this cycle?” | **OPEN-BLOCKED** | Tolman + no licensed selection |
| DE self-tune / ohmic | **OPEN** (least-trusted) | Weinberg; ohmic DE; toy fail |

*NO FABRICATIONS. Occupancy remains OPEN. Width remains derived.*
