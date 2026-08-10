# GATED_WAITING — stamps only (no invent closes)

**Package path:** `docs/working_logs/_runs/theory_exhaust_20260805/gated/GATED_WAITING.md`  
**Date:** 2026-08-05  
**Sibling exhaust:** `../mb/foundations_addendum_exhaust/`  
**Inventory parent:** `../theory_task_inventory_20260804/`  
**Rules:** NO FABRICATIONS · leave MCMCs · no PolyChord · no invent red lists without board

---

## Grade stamps used here

| stamp | meaning |
|---|---|
| **OPEN-MACHINE** | Waiting on production / instrument run |
| **OPEN-BLOCKED** | Waiting on named fix; desk note only where stated |
| **EXTERNAL PENDING** | Owner / DOI / external delivery |
| **RUN-GATED** | Production chain / likelihood stack |
| **FENCED** | Permanent do-not-reopen / abstention / null stands |
| **HOLD** | Owner external (Fairbank / arXiv) |
| **SKIP** | Offline / fenced skip this box |
| **RED_OWED** | Red audit owed when package becomes booking/paper-grade-changing — **list not invented here** |
| **NOT_BOOKABLE** | Dual-gate not met |

---

## Waiting table

| ID | object (short) | stamp | owner / gate | corpus cite | note |
|---|---|---|---|---|---|
| **T-W7** | T14 production sign(\(H_\mathrm{kin}\)) | **OPEN-MACHINE** | machine / pre-reg four-branch production + red | inventory T-W7; `PRTOE_igmf_helicity.md`; T14 production dirs | **Kill:** book from smoke/partial; invent sign |
| **T-X1** | Onset MCMC bias (science debt D2) | **OPEN-BLOCKED** | desk **note only** | inventory T-X1; `SCIENCE_DEBTS` / debt_p042 | **Leave chains.** No chain edit / rebook from this exhaust. Named instrument fix when desk owns one. |
| **T-X2** | BBN ε external win | **EXTERNAL PENDING** | **owner** DOI + recompute card | inventory T-X2; hard_wins · arXivReady bbn-eps | Internal arithmetic may be verified; **not** EXTERNAL WIN without DOI |
| **T-D1** | P-2026-048 lattice \(T_c/\sqrt{\sigma}\) | **EXTERNAL** (clause 4 live) | external lattice + owner | inventory T-D1 (IF-C restatement); prereg P-2026-048 | Clauses 2/3 **sky-limited** on \(\rho_\Lambda\); 0.22% framing **withdrawn**; live risk = clause-4 \(\hat{\tau}\) window |
| **T-D2** | Matched lensing DES/KiDS | **RUN-GATED** | production likelihood | inventory T-D2; docket #161 / #32 | Do not peek partials as final |
| **T-D3** | Modern joint stack (PR4 · DESI-full · Pantheon+) | **RUN-GATED** | production after instruments | inventory T-D3; docket #40 | Do not peek partials as final |
| **T-D4** | conv_desi full restart | **RUN-GATED** | clean relaunch post-classy | inventory T-D4; docket #89 · chains | **Kill:** resume dead state |
| **T-M1** | bbnfix dual-gate book | **BOOKED** | machine dual gate met | inventory T-M1; old-BAO Stage B + DESI Stage A | Old-BAO Stage B published (Grok red); DESI Stage A + peel; **do not mix**; not nested |
| **T-M2** | routeD leave | **RUN-GATED** (leave alone) | machine optional leave | inventory T-M2 | Early / improving; **not** dual-gate book target |
| **T-M3** | PolyChord nested ln Z | **SKIP** | offline / fenced skip this box | inventory T-M3 | **No PolyChord work** from this exhaust |
| **T-O1** | Fairbank / arXiv | **HOLD** | **owner** | inventory T-O1; fairbank packet | Endorsement / posts external-gated |
| **T-W3** | \(c=9/10\) counting | **FENCED** permanent | do-not-reopen | inventory T-W3 (IF-A) | Close **N/A**; democratic derivation not live desk target |
| **T-W4** | α base (P-2026-040) | **FENCED** permanent bet | external / instrument optional only | inventory T-W4 (IF-A) | Close **N/A**; **T-S5 rides this fence** |
| **T-X4** | Strong CP | **FENCED** COMPLETE-ABSTENTION | constitution silence | inventory T-X4; `PRTOE_strong_cp.md` | **Kill:** any \(\bar\theta\) mechanism |
| **T-X5** | Cosmic birefringence null | **FENCED** null stands | prediction fence | inventory T-X5 | **Kill:** invent β source (IM-B etc. already KILL) |
| **T-X6** | Load-bearing red audits | **RED_OWED** | **red** when booking/paper/grade-changing | inventory T-X6; board audit column | Default honest `red: none`. **Do not invent audit list without board.** Stamp only. |

---

## Explicit non-actions (this file)

| forbidden | why |
|---|---|
| Launch / edit MCMC chains for T-X1 “fix” | desk note only; leave chains |
| PolyChord runs | T-M3 SKIP |
| Peek-book bbnfix H₀ / Σm_ν / S₈ | T-M1 NOT_BOOKABLE |
| Invent T-X6 red checklist | RED_OWED until board enumerates |
| Reopen T-W3 democratic derivation | FENCED permanent |
| Claim base α derived (T-W4) | FENCED permanent bet |
| θ̄ / birefringence source invent | T-X4 / T-X5 FENCED |
| Soften T-D1 after lattice answer | kill on card |
| Book T14 from smoke | T-W7 kill |

---

## Cross-link to foundations/addendum exhaust

Cards **not** waiting on machine/owner in the same sense — disposed in  
`../mb/foundations_addendum_exhaust/MASTER.md`:

T-W11, T-W12, T-W13, T-W14, T-D5, T-D6, T-D7, T-D8, T-S5…T-S11.

Note: T-D5/D8/S11 **sim halves** are sim-staged OPEN there; they are not re-listed as dual-gate book targets here.

---

## Counts

| bucket | n |
|---|---:|
| OPEN-MACHINE | 1 (W7) |
| OPEN-BLOCKED desk-note | 1 (X1) |
| EXTERNAL / HOLD | 3 (X2, D1, O1) |
| RUN-GATED | 4 (D2, D3, D4, M2) |
| NOT_BOOKABLE | 1 (M1) |
| SKIP | 1 (M3) |
| FENCED permanent | 4 (W3, W4, X4, X5) |
| RED_OWED | 1 (X6) |
| invent COMPLETE | **0** |
| MCMC/PolyChord edits | **0** |

*NO FABRICATIONS. Leave MCMCs. No PolyChord. RED_OWED ≠ invent list.*
