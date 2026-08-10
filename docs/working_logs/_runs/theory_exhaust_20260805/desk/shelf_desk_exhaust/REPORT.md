# Desk shelf exhaust — REPORT (T-S1, T-S2, T-S3, T-S4, T-X3)

**Date:** 2026-08-05  
**Package:** `docs/working_logs/_runs/theory_exhaust_20260805/desk/shelf_desk_exhaust/`  
**Policy:** Stocked corpus only. NO FABRICATIONS. Leave MCMCs. No PolyChord. exit0 ≠ PASS.  
**Runner:** `OMP_NUM_THREADS=1 nice -n 19 python3 …` from repo root where scripts exist.

---

## Grades table (5 cards)

| Card | Object | Grade | Stamp |
|---|---|---|---|
| **T-S1** | locking_without_Q | **OPEN residual** | PAID procedure (τ Parseval at Q=2/3); residual not closed |
| **T-S2** | c_w / c₂ underived | **OPEN derivation residual** (value of *a* = −c_w) | Name conflict resolved; form paid; value not permanent-assumption |
| **T-S3** | RM n_e amplitude | **OPEN** (external n_e) | Distinct from T-W6 void ×20; scale paid |
| **T-S4** | σσ scattering amplitude | **MISSING_INPUT** | No stocked unitarized amplitude; free dial killed |
| **T-X3** | Supertrace absolute SI *G* | **permanent OPEN** | Finiteness paid; SI *G* not conflated; Failures-Ledger language |

---

## T-S1 — locking_without_Q

### Hunt surfaces
- Shelf: `docs/PRTOE_koide_relation.md:13`, `:732`, residual freeze `:743`
- Script: `scripts/tau_parseval_recompute.py` — field `"locking_without_Q": "OPEN"`
- Board: `open_theory_full_20260804/RECOMPUTES.md` row 5; `THEORY_WALLS_QUEUE_20260803.md:79`

### Script run
| Script | log | exit | verdict |
|---|---|:---:|---|
| `scripts/tau_parseval_recompute.py` | [`tau_parseval_recompute.log`](tau_parseval_recompute.log) | **0** | **PASS** exact τ=½ln2 at Q=2/3; measured-Q Δτ ~9e-6 |

### What is paid
- Parseval identity: Q = 1/3 + (2/3)ρ², τ = −ln ρ → τ = ½ln2 **exactly** when Q = 2/3.
- Conditions stated in script JSON: measured Q=2/3; √σ_dark=m_e pin; e^(−τ) modulus reading. Thermal *delivery* **not** used.

### Grade: **OPEN residual**
- **Not** DEAD, **not** MISSING_INPUT for the algebra, **not** a free close.
- PAID procedure does **not** lock τ without Q. Shelf residual freeze:

> | locking_without_Q | **OPEN** | Independent lock of τ without assuming Q=2/3 |  
> — `docs/PRTOE_koide_relation.md:743`

### REQUIRED_INPUTS (residual still open — no invent lock)
1. A scored mechanism (or external/lattice pin) that fixes τ **independently of assuming Q = 2/3**.
2. Explicit non-identity of that lock with thermal/flat delivery (already **contradicted** for Q mechanism).
3. Shelf/ledger named close — not algebra reconfirm alone.

**Distinct from T-W5:** T-W5 owns #101/#102 + Wilson. T-S1 owns only the τ-without-Q residual on the Koide shelf.

**Forbidden:** treat tau_parseval exit0 / PASS as closing locking_without_Q.

---

## T-S2 — c_w / c₂ underived

### Hunt surfaces
- Name conflict authority: `docs/PRTOE_READERS_GUIDE.md:72–74` (rename 2026-07-28)
- RECOMPUTES disagreement:
  - `open_theory_full_20260804/RECOMPUTES.md:24` → residual **c_w underived**
  - `shelf_residual_pass_20260804/RECOMPUTES.md:24` / `THEORY_WALLS_QUEUE:80` → residual **c₂ underived**
- Amplitude / LO: `scripts/fbar_leading_order_price.py`, `scripts/fbar_cw_lo_closure.py`
- Working log: `docs/working_logs/fbar_cw_lo_closure.md`
- Docket residual object: value of *a* (predicts c₃ = c_w²) — Track A3 / docket #55 remainder

### Name conflict — card resolution
| Symbol | Meaning (post 2026-07-28) | This residual? |
|---|---|---|
| **c_w** | winding-response quadratic coeff.; f̄_eff = 2/π + c_w·ε/2 | **YES — residual object** |
| **c_K** | Koide kernel Q/τ = 4/(3 ln2) ≈ 1.924 (was one old “c₂”) | No |
| **c₂** | second-sound speed √α·c ≈ 0.0854c only | **No** — different dimensions/object |

Board row-6 wording “c₂ underived” is **legacy rename lag**. Residual owned by T-S2 is **c_w** (and its strength *a* = −c_w), not second-sound c₂.

### Script runs
| Script | log | exit | verdict |
|---|---|:---:|---|
| `scripts/fbar_leading_order_price.py` | [`fbar_lo.log`](fbar_lo.log) | **0** | desk audit — LO ~1%/unit; c2 itself not derived |
| `scripts/fbar_cw_lo_closure.py` | [`fbar_cw_lo.log`](fbar_cw_lo.log) | **0** | desk audit — CANDIDATE CLOSED form; *a* residual |

### Split grade (honest)
| Piece | Status | Source |
|---|---|---|
| f̄ LO = 2/π | settled | mass-positivity + equidistribution |
| LO dominance \|x\| ≫ c_w x² | **proved as bound** | ε≈1.25%; worst quad/lead ≲2% on data band |
| **form** c_w = −a | **mechanism exhibited** | medium back-reaction (C16) |
| **value of a (= −c_w)** | **OPEN named residual** | ensemble a∈[0.32,1.36]; fit a≈1.80 (1.9σ); no unique a forced |

### Grade: **OPEN derivation residual** (value of *a*)
- **Not** permanent assumption stamp: form is paid; value remains docket-class derivation residual.
- **Not** silent rename of c_w ↔ c₂ (Kill on card).
- Second-sound c₂ is **out of scope** for this residual (separate prediction / α_c seat).

**Forbidden:** claim c_w fully derived; average the two data readings; treat LO desk audit as value close.

---

## T-S3 — RM n_e amplitude (≠ void ×20)

### Hunt surfaces
- Shelf: `docs/PRTOE_cosmic_magnetism.md:101–114`, residual freeze `:235`, claims ledger `:227`
- Script: `scripts/rm_coherence_kibble.py`
- Distinctness: T-W6 owns **void floor ×20** only; this card owns **absolute RM amplitude / n_e**

### Script run
| Script | log | exit | verdict |
|---|---|:---:|---|
| `scripts/rm_coherence_kibble.py` | [`rm_coherence.log`](rm_coherence.log) | **0** | desk audit — geometric scale paid; void ×20 **not** closed; no absolute σ_RM without n_e |

### What is paid vs open
| Object | Grade | Owner |
|---|---|---|
| RM geometric two-point / multipole transfer (ξ_K → ℓ ~ 25–60 survey plane) | **machine-backed / derived-conditional (scale)** | paid here / RM debt |
| Void B floor ×20 shortfall | **OPEN-BLOCKED** | **T-W6** — not absorbed here |
| **RM absolute amplitude / C_ℓ / catalog** | **OPEN** | **T-S3** — needs external n_e |

Shelf `:235`: *“RM absolute amplitude | **OPEN** | needs external n_e model”*.

### Grade: **OPEN**
If treated as input gate: **MISSING_INPUT** = external n_e model + survey transfer + galactic RM cleaning.

### What’s missing (no invent n_e law)
1. External electron-density model n_e(χ) for amplitude (not inventable as free desk law).
2. Absolute C_ℓ / σ_RM catalog comparison path using that n_e.
3. Galactic RM cleaning protocol for survey comparison.

**Kill:** absorb this residual into T-W6 void-only; claim absolute σ_RM from geometry alone.

---

## T-S4 — σσ scattering amplitude (HIGH PRIORITY)

### Hunt surfaces (primary)
- `docs/PRTOE_cosmological_constant.md:30–31` — two decimal places wait on σσ amplitude; “desk question”
- `:402–406` — 0.10–0.90% band “closed at the desk **given** the σσ amplitude”; precision waits
- `:727–753` — tree-level contact vs contact+σ-exchange table at **λ = 45.7**; reliability open
- `:747–749` — **remaining blocker:** is tree-level reliable at λ=45.7? ChPT/unitarised tools named; **“that calculation is not attempted here.”**
- `docs/PRTOE_DEPENDENCY_TREE.md:68` (ρ_Λ row) — existence not precision; residual = scattering amplitude desk question

### Scripts considered / run
| Candidate | Role | Computes unitarized σσ amp? |
|---|---|---|
| `scripts/lhy_control_edge_refuted.py` | LHY demotion-reason check vs QMC literature | **No** — gate openability, not a₀ |
| Tree table in shelf prose (`:730–733`) | contact −6λ vs full −36λ bookkeeping | **Tree estimates only**; reliability at λ=45.7 **unpaid** |
| `scripts/*scatter*`, `*ss_amp*`, `*unitar*`, `*sigma_sigma*` | hunt under `scripts/` | **None present** |

**LHY log:** [`lhy_control_edge.log`](lhy_control_edge.log) exit **0** — establishes “gate openable at desk, not that it is open”; still owes QMC-minus-LHY residual and potential-shape spread. **Does not replace T-S4 amplitude.**

### Grade: **MISSING_INPUT**

Exact residual demand (file:line):

| Demand | Location |
|---|---|
| Reliability of tree-level σσ at λ≈45.7; unitarised / ChPT amplitude | `docs/PRTOE_cosmological_constant.md:747–749` |
| Precision claim waits on amplitude (not lattice half) | `:30–31`, `:406` |
| Band closed *given* σσ amplitude | `:402–403` |
| DEPENDENCY_TREE ρ_Λ residual = scattering amplitude desk question | `docs/PRTOE_DEPENDENCY_TREE.md:68` |

### Kill free dials
- **Kill:** invent a scattering amplitude number to “finish” two-decimal ρ_Λ precision.
- **Kill:** claim precision ρ_Λ from τ-chain alone without amplitude (or without keeping existence-only grade).
- **Kill:** treat LHY control-edge exit0 as amplitude close.
- **Kill:** silent drop of residual while advertising precision.

Tree contact/exchange *estimates* on shelf (`:730–733`: 0.59% / 0.10% on ρ_Λ¼) are **not** a measured or unitarised amplitude; shelf itself says tree level “not quantitatively reliable” (`:785–787`).

**What would unstick (stocked language only):** desk computation of (unitarised) threshold 2→2 σσ amplitude at sector coupling λ~45.7, or a literature a₀/(range) with documented map into the 1.345%/(Λa₀) bound — **not invented**.

---

## T-X3 — Supertrace absolute SI *G*

### Hunt surfaces
- Card: `theory_task_inventory_20260804/REPORT.md` T-X3 — Close: named close **or permanent open stamp**; **Kill: silent drop without ledger**
- Shelf: `docs/PRTOE_induced_gravity.md:7`, `:55–58`, `:112`, `:153` (§5.6), `:207`
- Failures Ledger: `docs/PRTOE_FAILURES_LEDGER.md` “The G-closure” / **G-COMPUTATION RETIRED AS A ZOMBIE** (`:134–137`)
- Script: `scripts/supertrace_k1_verify.py`

### Script run
| Script | log | exit | verdict |
|---|---|:---:|---|
| `scripts/supertrace_k1_verify.py` | [`supertrace_k1_verify.log`](supertrace_k1_verify.log) | **0** | **desk audit** — str[k1]=0 for SM+3ν_R (ξ_H=1/6); unit correction note (SM-alone −1/2 vs Weyl deficit −3) |

### Non-conflation (binding)
> Supertrace finiteness ≠ SI *G*.  
> `induced_gravity.md:112`: absolute SI *G* **OPEN** — mass-scale half (ρ*/portal/lattice); closed-form 1/G under str[k₁]=0 is **finiteness, not SI prediction**.

### Disposition: **permanent OPEN stamp**
Failures-Ledger-compatible language:

- Claim to **compute** Newton’s constant from the roster: **WITHDRAWN / RETIRED AS A ZOMBIE** (G-closure row; G-computation row) — *PRTOE_FAILURES_LEDGER.md:134–137*.
- **Keeper that survives:** Pauli finiteness str[k₁]=0 + forward kills (P-2026-045) — **not** absolute SI *G*.
- Residual on expansion attach remains named: medium collective-mode masses at Planck scale within O(1) — **not paid** (`induced_gravity.md:153`).

This is a **permanent open stamp** on absolute SI *G*, not a silent drop and not a demotion that erases the residual without ledger language (Kill on card: **silent drop of residual without ledger**).

**Forbidden:** “supertrace PASS ⇒ G derived”; drop SI *G* residual without Failures-Ledger / shelf OPEN row.

---

## Scripts executed this exhaust

| # | Command | log | exit |
|---|---|---|:---:|
| 1 | `OMP_NUM_THREADS=1 nice -n 19 python3 scripts/tau_parseval_recompute.py` | `tau_parseval_recompute.log` | 0 |
| 2 | `OMP_NUM_THREADS=1 nice -n 19 python3 scripts/fbar_leading_order_price.py` | `fbar_lo.log` | 0 |
| 3 | `OMP_NUM_THREADS=1 nice -n 19 python3 scripts/fbar_cw_lo_closure.py` | `fbar_cw_lo.log` | 0 |
| 4 | `OMP_NUM_THREADS=1 nice -n 19 python3 scripts/rm_coherence_kibble.py` | `rm_coherence.log` | 0 |
| 5 | `OMP_NUM_THREADS=1 nice -n 19 python3 scripts/lhy_control_edge_refuted.py` | `lhy_control_edge.log` | 0 |
| 6 | `OMP_NUM_THREADS=1 nice -n 19 python3 scripts/supertrace_k1_verify.py` | `supertrace_k1_verify.log` | 0 |

**σσ unitarized amplitude script:** none stocked — T-S4 not runnable to a number.

---

## Cross-links
- Card source: `docs/working_logs/_runs/theory_task_inventory_20260804/REPORT.md` §G T-S1…T-S4, T-X3  
- Prior recomputes: `open_theory_full_20260804/RECOMPUTES.md`  
- Package mates: [`MASTER.md`](MASTER.md) · [`NON_CLAIMS.md`](NON_CLAIMS.md) · [`SURVIVORS.md`](SURVIVORS.md)
