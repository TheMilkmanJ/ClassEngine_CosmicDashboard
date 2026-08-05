# DEAD_LANES — Immediate deaths on Page T8 residual chase

**Package:** `page_t8_residual_demand`  
**Date:** 2026-08-04  
**Role:** which thrash / fake-pass / exhausted forms die **immediately** — before deeper licensed-micro work  
**Parents:** `page_t8/CONSTRUCTION_LEVERS.md` · D1–D3 attempt notes · PAGE_TURN §4.3  
**Band (not faked here):** all bins range/\(S_\star\) ≤ 0.10 joint with T2+stall+DC3

---

## 0. Death classes (quick reference)

| Class | Meaning |
|---|---|
| **FORBIDDEN thrash** | Explicitly stopped; do not reopen as Q6 program |
| **EXHAUSTED** | Attempted on this instrument family; not joint |
| **PROTOCOL-BREAK** | Changes binding pins or claim hygiene |
| **WRONG_OBJECT** | Solves a different residual (late stall, Q2, etc.) |
| **HONESTY fence** | Fake green / soft pass / invent closed form |

---

## 1. Lanes that die immediately

### 1.1 Header thrash family (FORBIDDEN thrash)

| Dead lane | Typical move | Why dead | Record |
|---|---|---|---|
| **\(G_{\mathrm{TMS}}\) scale scan** | Raise/lower TMS until early range looks better | Ratio sticky ~0.11 under pure scale; or regress T2 | v13 follow-ups; PAGE_DEEPER |
| **`TMS_SHAPE_POWER` / TMS delay grid** | Soften early sin^p / delay start | Often loses T2 or stalls; not a new law | v24–v37 class notes |
| **`BS_MILD` / `G_BS` fine grid** | Dump edge-tune for early du | Joint regression or sticky early bin | freeze surfaces |
| **Late EXTRA_BS boost after soft TMS** | Recover T2 by late dump | Late multivalued \(S\) / no freeze | V13_BEST follow-up table |
| **Coarser sampling to hide range** | Fewer frames in bin | Honesty / protocol theater | FORBIDDEN |

**Disposition:** **DEAD as program.** Do not resume as residual chase.

### 1.2 Exhausted deeper-construction family (D1–D3)

| Dead lane | What was tried | Why dead | Record |
|---|---|---|---|
| **D1 two-phase pure BS→TMS** | `PHASE_BS_ONLY_UNTIL_U`, soft `PHASE1_TMS_FRAC` | Early T8 can pass; **T2 not joint** (u_late 0.86–0.89 class) | `B_A_D1_ATTEMPT.md` |
| **D1 pure-zero TMS until u≥0.12** | vacuum dump | Vacuum dump dead (u_late~0.29) | D1 v40 |
| **D2 free \(w_c\equiv1\) only** | `FREE_W_C_FIXED=True` | **No-op** on champion trajectory (freeze before decay) | `B_A_D2_ATTEMPT.md` |
| **D3 full-20 densify** | midband_omegas 20 | u_late~0.899; stall~554; **DC3 FAIL** | `B_A_D3_ATTEMPT.md` v35–v36 |
| **D3 densify + dump notch** | v37 T2 notch | Still u_late~0.899; late T8 fail | D3 v37 |
| **D3 midband-12** | v38 + champion pins | Worse reach (u_late~0.869) | D3 v38 |

**Disposition:** **EXHAUSTED.** Reopening requires **new non-header inputs** (licensed micro), not another v-number of the same idea.

### 1.3 Protocol-break family

| Dead lane | Move | Why dead |
|---|---|---|
| **Loosen T8 to 0.12 or “≈0.11”** | Soft pass 0.113 | Threshold is binding 0.10; 0.113 is **FAIL** |
| **Widen \(\Delta u\)** | 0.02 bins hide steep rise | Changes T8 definition |
| **Subsample / drop frames in [0.10,0.11)** | Thin the bin | Fake single-valuedness |
| **Machine T1–T6 True ⇒ CANDIDATE** | Skip T8 | Binding requires T8_pass |
| **Co-write CANDIDATE with first JSON** | Same-step filing | Claim-decoupling §4.4 |
| **Scorecard sets `page_curve_claimed`** | Tool claim flip | Tool **never** does; must stay false |
| **“Almost candidate” grade** | Soft social pass | Not a protocol grade |

**Disposition:** **PROTOCOL-BREAK / DEAD.**

### 1.4 Wrong-object / wrong-tool family

| Dead lane | Move | Why dead |
|---|---|---|
| **Late envelope-stall thrash on v13** | Fix frozen-u purification vertical | v13 late gates already PASS; residual is **early** |
| **Q2 area-law payment as Page** | Cite coefficient work | Distinct ledger (Q2 ≠ Q6) |
| **PolyChord evidence for Page instrument** | Nested sampling | Wrong tool; fenced |
| **MCMC chain retune for T8** | Cosmology chains | Leave MCMCs alone; T8 is arrays-on-coevolve |
| **Strong CP seating for Page** | Seat residual swap | Abstention / out of scope |
| **Invent closed-form island \(S(u)\)** | Analytic curve without dynamics | NO FABRICATIONS; scorecard scores histories |

**Disposition:** **WRONG_OBJECT / FORBIDDEN.**

### 1.5 Lever-collapse temptations (look like R1–R7 but die on arrival)

| Temptation | Maps to | Kill |
|---|---|---|
| “Just lower G_TMS 10%” | Header thrash | Sticky / T2 |
| “PHASE until 0.12 again” | D1 | EXHAUSTED joint fail |
| “20 modes fixed it in self-score once” | D3 | EXHAUSTED joint fail |
| “FREE_W_C again” | D2 | no-op |
| “T8 bar was meant to be ~0.12” | threshold | PROTOCOL-BREAK |
| “S(u)=… island formula green” | invent formula | HONESTY / WRONG_OBJECT |
| “File packet; red will sort T8” | premature CANDIDATE | PROTOCOL-BREAK |
| “Densify is continuum (R4)” without law text | D3 launder | Densify kill |
| “nbar seed = 0.01 by hand” | R7 collapse | Honesty / null risk |

---

## 2. Candidate levers — immediate death vs delayed

| Lever | Immediate death? | On what? | Note |
|---|---|---|---|
| **R1** dump law | **No** (not yet) | — | Dies if implemented as BS header grid |
| **R2** entangling law | **No** (not yet) | — | Dies if only TMS shape/G_TMS thrash |
| **R3** free-H redesign | **No** (not yet) | — | D2 form dead; beyond-D2 still open as schema |
| **R4** continuum law | **Partial** | densify form **DEAD** | Lives only with non-count continuum license |
| **R5** co-modulation | **No** (not yet) | — | Dies if still factorized free knobs |
| **R6** spectrum law | **Partial** | densify form **DEAD** | Lives only derivation-first |
| **R7** seed law | **Borderline** | D1-adjacent | Pure vacuum / manual nbar dead |
| **R8** D4 disposition | **N/A** | — | Active honesty; dies only as false physics close |

---

## 3. What does *not* die immediately (but is not a land)

See [`SURVIVORS.md`](./SURVIVORS.md):

- R1–R3, R5 as **schemas** pending licensed micro text.  
- R4/R6 only in **non-densify** form.  
- R7 only with independent seed micro (not D1 reheat).  
- R8 as **standing disposition**.  
- Failures-style residual OPEN until joint clear or formal instrument retirement (not claimed here).

---

## 4. Failures-ledger posture

This package is the **exploratory** death table for T8 thrash / fake-pass lanes.  
It does **not** auto-write living `PRTOE_FAILURES_LEDGER.md` (no ownership tasks).  
Instrument near-miss remains on freeze surfaces; Q6 stays OPEN.

---

## 5. Explicit non-claims

- Killing thrash is not a T8 pass.  
- Exhausted ≠ “physics impossible forever.”  
- No joint land is claimed.

---

*End DEAD_LANES.md*
