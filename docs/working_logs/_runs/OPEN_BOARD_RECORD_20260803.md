# OPEN BOARD RECORD — full rewrite 2026-08-04

**File kept:** `docs/working_logs/_runs/OPEN_BOARD_RECORD_20260803.md`  
**Stamp:** **2026-08-04 full rewrite** (not a stub stamp; not a night-split snapshot)  
**Audience:** ChatGPT REF + Claude RED + Grok BLUE + owner  
**Authority packages:**  
- desk / red column → [`improve_loop_20260804/BOARD_STATUS.md`](improve_loop_20260804/BOARD_STATUS.md)  
- this rewrite’s audit trail → [`open_board_refresh_20260804/`](open_board_refresh_20260804/)  

**Hard rules (standing):**  
NO FABRICATIONS · no PolyChord · **leave cobaya MCMCs alone** · OMP=1/nice for desk compute · no premature CANDIDATE · no peek-book H₀ · **exit-0 ≠ PASS** · **delivered ≠ graded**.

---

## 0. One-screen truth (read this first)

| Lane | Item | Status (2026-08-04) | Book / claim? |
|---|---|---|---|
| **E2** | bbnfix pair booking | progress R−1 **lcdm 0.059** / **dyad 0.189**; both `converged: false` | **NOT bookable** |
| **Page / Q6** | dynamical Page curve | champion **`coevolve_v13`** T8 early = **0.113** (need ≤0.10); **D4** freeze | **no CANDIDATE**; `page_curve_claimed: false` |
| **Strong CP** | θ̄ / white-hole bridge | **COMPLETE-ABSTENTION** + seat hunt (itch only) + **R5 DENY** | **no θ̄ mechanism lane** |
| **Desk** | improve packages | **desk clear** (delivery DONE) | red column mostly **none** — see BOARD_STATUS |
| **Residual owners** | what is still open | **machine / owner / theory** — not desk thrash | see §5 |

---

## 1. E2 — bbnfix posterior booking (**NOT bookable**)

### Live progress (authoritative gate inputs)

Source stamps: `book_bbnfix_when_ready.py` → **REFUSED**  
cards e.g. `bbnfix_booking_20260804_084239/`, `bbnfix_booking_GATECHECK_20260804/`,  
live surfaces / CHAIN_TABLES / REFEREE_CALENDAR (2026-08-04).

| chain | N (progress) | R−1 | stop | `converged` | ready |
|---|---:|---:|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` (ΛCDM+mν twin) | 19013 | **0.059055** (~**0.059**) | 0.05 | **false** | **NO** |
| `dyad_mnu_bbnfix` (model) | 18837 | **0.189201** (~**0.189**) | 0.05 | **false** | **NO** |

**Gate (both legs required):** progress R−1 **< 0.05** **and** checkpoint **`converged: true`**.  
Temporary R−1 < 0.05 without self-stop is **not** bookable (lcdm once hit ~0.0488 then rose).

**Offline GetDist max GR** (`bbnfix_mcmc_watch_diag.py`): diagnostic only (~0.07 lcdm / ~0.086 dyad) — **UNBOOKABLE**; **not** booking authority.

**Route-D** (`cmp_prtoe_routeD`): separate instrument; early (R−1 ~102.79 at N~1609); **not** part of the bbnfix pair gate; leave alone.

### Book when ready (only path)

Do **not** hand-edit tables. Do **not** treat watch/diag as book.

```bash
# single gate + GetDist booking card
python3 scripts/book_bbnfix_when_ready.py

# full ordered pipeline (book → finalize H₀ → tables → Δχ² proxy)
bash scripts/bbnfix_when_ready_all.sh
```

Pipeline order inside `bbnfix_when_ready_all.sh`:  
(0) dual progress+self-stop gate → (1) `book_bbnfix_when_ready.py` → (2) `finalize_h0_at_convergence.py` → (3) `make_getdist_tables.py --include-bbnfix` → (4) optional Δχ² proxy.  
Exit **2** = gate refused (no partial booking promoted). CosmicForge Laplace is **not** auto-launched.

**MCMC stance:** production cobaya ranks **still live** — **leave alone** (no kill, no reseed, no PolyChord on this box).

### Explicit non-claims (E2)

- No letter H₀ / Σm_ν / S₈ / Ω_b h² from live bbnfix tables.  
- No “almost bookable.”  
- BBN ε **ARITHMETIC VERIFIED (internal)** (~3.196% ≈ 3.20% 2σ PASS); **EXTERNAL WIN PENDING (no DOI)** — does **not** close E2.

---

## 2. Page / Q6 — instrument freeze (**not claimed**)

**Package:** [`page_full_freeze_20260804/`](page_full_freeze_20260804/)  
(`REPORT.md`, `SCORECARD_SNAPSHOT.md`, `HYGIENE.md`)

| Field | Truth |
|---|---|
| Champion instrument | **`coevolve_v13`** (`schedule_version: v23_champion_locked`) |
| Artifact | `quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| T1–T6 (machine) | **PASS** |
| DC3 | **PASS** |
| **T8** single-valued S(u) | **FAIL** — early bin **[0.10, 0.11)** range/S* = **0.113** (need ≤ **0.10**) |
| Standing **CANDIDATE** | **none** (binding False; denied path still stands) |
| `page_curve_claimed` | **false** |
| Deeper construction | **D1–D3 exhausted**; **D4** = accept near-miss until **new microphysics** |
| Next unblock | licensed new coupling / dump / free-H law — **not** header thrash |

**Forbidden:** claim Page closed; set `page_curve_claimed: true`; file CANDIDATE without T1–T8 + DC3 + claim-decoupling + red AGREE; treat Q2 area-law coefficient as dynamical Page.

---

## 3. Strong CP — abstention + seat hunt + **R5 DENY**

| Layer | Status | Where |
|---|---|---|
| Constitutional | **COMPLETE-ABSTENTION** (θ̄ outside jurisdiction permanently) | `docs/PRTOE_strong_cp.md` |
| Seat hunt | **itch registered only** — kinship to missing EM-anomalous angular mode; **not** a solution | [`physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md`](physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md) |
| Red | **R5 DENY standing** — pre-emptive denial of any white-hole / reverse / genesis / medium **θ̄ bridge** | Claude RED NOTE `R5-strongcp-whitehole` (ForGrok&Claude); BOARD_STATUS “DENY standing (R5)” |

**Not allowed:** “Strong CP drives the cyclic reverse”; axion-as-dark-medium; θ̄ = 0 “prediction”; any PAPER_CANDIDATE on θ̄.  
Birefringence is a **propagation** effect (electron anomaly channel), not a white-hole epoch; Strong CP is **gluon** θ̄ — wrong gauge field for a medium bridge under EM-neutrality.

---

## 4. Packages delivered (desk) — **red column lives on BOARD_STATUS**

**Pointer (authoritative red audit column):**  
→ [`docs/working_logs/_runs/improve_loop_20260804/BOARD_STATUS.md`](improve_loop_20260804/BOARD_STATUS.md)

**Rule:** **delivered ≠ red-graded.** Column `red` defaults to **none** unless Claude filed a verdict.

| package | delivery | red (see BOARD_STATUS) |
|---|---|---|
| page_full_freeze | DONE | none |
| open_machine_full | DONE | none |
| open_theory_full | DONE | none (recompute re-grade used Claude rule) |
| debts_hardwins_full | DONE | none |
| live_surfaces_full | DONE | none |
| shelf_map_currency | DONE | none |
| hubble_completion_full | DONE | none |
| soft_claim_sweep | DONE | none |
| laplace_booking_full | DONE | none |
| neutrino_full_honesty | DONE | none |
| bounce_full_freeze | DONE | none |
| quantum_status_sync | DONE | none |
| current_core_full | DONE | none |
| qg_goalB_honesty | DONE | none (supertrace third copy cured under red VERIFY) |
| shelf_residual_pass | DONE | **AGREE-IF** (exit-0≠PASS + fbar + supertrace cures closed) |
| all4lanes / physics_improve | DONE (partial parent) | **AGREE-IF** on audited lanes |
| arxiv_owner_prep | DONE | none |
| STRONG_CP_SEAT_HUNT | DONE | none (itch-only) |
| **open_board_refresh_20260804** | **DONE** (this rewrite) | none (record only) |

Red audits remaining **none** rows on request or when load-bearing (booking / paper / grade change).

---

## 5. Explicit residual ownership — **desk clear; machine / owner / theory residual**

### Desk

| Statement | Meaning |
|---|---|
| **Desk clear** | Formulable improve packages for this wave are **delivered** (see §4). No open desk thrash owed to “finish the board.” |
| Not forceable from desk | Booking, Fairbank post, Page microphysics, theory walls |

### Machine residual

| Residual | Owner | Notes |
|---|---|---|
| **bbnfix book** (0.059 / 0.189) | **Machine** | wait self-stop + `book_bbnfix_when_ready.py` / `bbnfix_when_ready_all.sh` |
| routeD / zon_disp / conv_desi | **Machine** (owner restart where parked) | separate instruments; not E2 pair |
| PolyChord nested | **Skip** on this box | offline; not a desk paydown |

### Owner residual

| Residual | Owner | Notes |
|---|---|---|
| **Fairbank / arXiv** | **Owner** | HOLD; packages ready on disk (`arxiv_owner_prep_20260804/`); no post without greenlight |
| neutrino-mbb first post | **Owner** | when Fairbank replies |

### Theory residual (walls — do not invent-close)

| Residual | Grade posture | Pointer |
|---|---|---|
| **Page T8 joint / Q6** | OPEN; needs microphysics (**D4**) | page_full_freeze |
| Bounce H_re / turn | OPEN-BLOCKED | bounce_full_freeze; THEORY_WALLS |
| Void IGMF floor ×20 | OPEN-BLOCKED | cosmic_magnetism / debt_magnetism |
| Koide mechanism residual | OPEN-BLOCKED | koide debt packages |
| Forward ω_J (baryo) | OPEN-BLOCKED | debt_omegaJ_forward |
| DE occupancy / coincidence | OPEN | coincidence shelf |
| MEDR r / pair H / Born / atomic QM | MISSING_INPUT or BLOCKED seating | quantum residual |

Authority walls queue: [`THEORY_WALLS_QUEUE_20260803.md`](THEORY_WALLS_QUEUE_20260803.md) + [`open_theory_full_20260804/`](open_theory_full_20260804/).

---

## 6. Claude red rules (standing process)

| Rule | Meaning |
|---|---|
| **exit-0 ≠ PASS** | A recompute that returns shell exit 0 is **not** automatically a physics **PASS**. Grade must be explicit (PASS verdict vs desk audit / residual open). Applied on shelf_residual / all4lanes re-grade (3 PASS / 5 desk audits among 8 exit-0 runs). |
| **delivered ≠ graded** | Package directory **DONE** on disk ≠ Claude red AGREE. Red column on BOARD_STATUS is the audit truth. |
| **R5 DENY** | Strong CP / white-hole θ̄ bridge is **pre-emptively denied**; do not open a θ̄ mechanism lane. |
| **No premature CANDIDATE** | Page: T1–T8 + DC3 + claim-decoupling + red before any standing candidate. |
| **No invent closes** | Walls stay OPEN / OPEN-BLOCKED until licensed derivation or machine book. |

---

## 7. Owner-only HOLD (do not chase from blue/red)

| ID | Item | Status |
|---|---|---|
| **O1** | arXiv / Fairbank endorsement | **HOLD** — owner desk only |
| O1a | neutrino-mbb + READY packages | ready on disk; wait greenlight |

---

## 8. External credibility path (short)

| ID | Item | Status |
|---|---|---|
| **E1** | BBN ε recompute card | **ARITHMETIC VERIFIED (internal)** — ε 2σ ≈ 3.196% ≈ 3.20%; **EXTERNAL WIN PENDING (no DOI)** |
| **E2** | bbnfix posterior booking | **NOT bookable** — §1 |
| E2c | Preflight | READY on disk (`hard_wins_90day…/BBNFIX_BOOKING_PREFLIGHT.md`) |
| E2d | GetDist include-bbnfix | gated — only after book script passes |
| E2e | RouteD | separate; leave alone |

---

## 9. Explicit non-actions (all seats)

- No arXiv chase while Fairbank **HOLD**  
- No H₀ / Σm_ν book while R−1 ≥ 0.05 **or** before self-stop  
- No `page_curve_claimed: true`  
- No standing **CANDIDATE** on Page without full gate + red  
- No invent θ̄ / medium \(r\) / pair \(H\) / Born / atomic QM / A_ωJ seat  
- No PolyChord; **no kill/reseed** production MCMC  
- No treating **exit 0** as **PASS** without explicit grade  

---

## 10. Record hygiene

| Surface | Role |
|---|---|
| This file | Outsider-readable **open board record** (2026-08-04 full rewrite) |
| `improve_loop_20260804/BOARD_STATUS.md` | **Red column** + package index |
| `PRTOE_CHAIN_TABLES.md` | Live chain banner / freeze language |
| `PRTOE_REFEREE_CALENDAR.md` | Sitting NOW instruments |
| `SCIENCE_DEBTS_2026-08-03.md` | D1–D9 currency (via debts_hardwins_full) |
| `open_board_refresh_20260804/REPORT.md` | What changed vs prior night board |

*NO FABRICATIONS. Desk clear ≠ physics closed. Machine/owner/theory residual remains.*

---

## Publish split (2026-08-04 Claude red)

`bbnfix_when_ready_all.sh` Stage A only by default. Forward tables require red stamp  
`bbnfix_booking_*/RED_AUDIT.md` then `--write-tables`. See `booking_pipeline_red_gate_20260804/`.

