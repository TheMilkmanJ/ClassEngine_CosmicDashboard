# MEDR / PAIRH deep hunt (R-MEDR + R-PAIRH)

**Date:** 2026-08-03  
**Task:** Deeper inventory after `scripts/quantum_medium_r_inventory.py` reported `medium_pin_found=False` (479 files).  
**Hard rules:** NO FABRICATIONS · no invent of Hamiltonian or \(r\) formula · no PolyChord · no evaluation script unless a closed formula is **corpus-licensed** with numbers.

---

## Verdict

| residual | answer |
|---|---|
| **R-MEDR** (medium pair \(r\)) | **MISSING_INPUT still** |
| **R-PAIRH** (medium-licensed pair \(H\)) | **MISSING_INPUT still** (textbook harness only) |
| **CANDIDATE with exact formula + file:line** | **none** |
| **Script `scripts/quantum_medium_r_from_corpus.py`** | **NOT written** (would require inventing a pin) |

**One line:** Corpus has a **literature** TMSV pair Hamiltonian and \(r=\mathrm{artanh}(|\lambda/\omega|)\) map with **free** \(\lambda/\omega\); it does **not** pin medium \((\omega,\lambda)\) or \(r=r(\mathrm{medium})\).

---

## Scope of this pass vs prior inventory

| pass | coverage | result |
|---|---|---|
| P1 inventory (`quantum_medium_r_inventory.py`) | 479 files: `docs/PRTOE_*.md`, `docs/exploratory/PRTOE_*.md`, `scripts/*.py` | `medium_pin_found=False` |
| **This deep hunt** | ~**799** files under `scripts/**`, `docs/**`, `papers/**`, `ForJustin/**`, `scratch/**`, plus `ForGrok&Claude.md`; expanded patterns (artanh, \(r=\) closed forms, \(\lambda/\omega=\) numeric, gap→\(r\), pair-\(H\) LaTeX, dyad/dCDF pair, Bogoliubov \(u_k,v_k\)) | same MISSING_INPUT |

---

## Files examined (load-bearing / promising)

Read fully enough to decide pin vs non-pin:

| path | role | pin for medium \(r\) / medium \(H\)? |
|---|---|---|
| `scripts/quantum_medium_r_inventory.py` | P1 phrase inventory | no pin |
| `scripts/quantum_pair_hamiltonian_tmsv.py` | textbook \(H=\omega(n_a+n_b)+\lambda(ab+\mathrm{h.c.})\); \(r=\mathrm{artanh}(|\lambda/\omega|)\); free \(\lambda/\omega\) scan | **harness only** — `medium_*_derived=False` by design |
| `scripts/quantum_chsh_tsirelson.py` | literature \(B(r)=2\sqrt{1+\tanh^2(2r)}\); free \(r\) table | no medium \(r\) |
| `docs/working_logs/_runs/quantum_arxiv_worklist_20260803/EN_D2_D3_PAIR_R.md` | EN-D2/D3 audit | states \(r\) not corpus-defined; pair \(H\) missing |
| `docs/working_logs/_runs/quantum_arxiv_worklist_20260803/PAIR_HAMILTONIAN_TMSV.md` | harness report | Medium ω/λ/r **NO** |
| `docs/working_logs/_runs/quantum_arxiv_worklist_20260803/VERDICT_QUANTUM_FOUR.md` | quantum four endpoint | medium \(r\), pair \(H\) = MISSING_INPUT |
| `docs/working_logs/_runs/quantum_arxiv_worklist_20260803/COMPUTE_PASS_20260803.md` | compute fence | medium \((\omega,\lambda)\) still MISSING |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/CHSH_PROVENANCE.md` | Chen et al. 2002 provenance | no first-principles PRTOE pair \(H\) |
| `docs/exploratory/PRTOE_quantum_entanglement.md` | E6/E7 ledger | E6/E7 **MISSING_INPUT**; \(r\) identification aspirational |
| `docs/exploratory/PRTOE_quantum_trio.md` | seating | medium \(r\) / pair \(H\) MISSING |
| `docs/working_logs/_runs/quantum_residual_task_20260803/BOARD.md` | residual board | R-MEDR/R-PAIRH MISSING_INPUT; hunt yes, invent no |
| `docs/working_logs/_runs/quantum_residual_task_20260803/MEDR_PAIRH_INVENTORY.md` | P1 output | NO medium pin |
| `scripts/de_value_fundamental_gp.py` | dyad/NJL pairing \(g\) budget | **not** TMSV \(r\); all model \(g\ll 2\); condensation gap |
| `scripts/settlement_terms.py` | BCS–BEC Leggett gap/number eqs | medium thermodynamics; **no** CHSH/\(r\) map |
| `scripts/bounce_fa1_transphononic_table.py` | Bogoliubov \(u,v\) coherence factors | quasiparticle content; **not** TMSV squeeze \(r\) |
| `scripts/basement_screening_fence.py` | hierarchy pairing \(\lambda=k\alpha_c\) | electroweak/hierarchy shell; **not** Bell pair \(H\) |
| `scripts/quantum_page_srad_unitary_mvp.py` | Page instrument \(G_\mathrm{SQUEEZE}=0.12\) | free dial for Hawking-like pair creation; **not** licensed medium \(r\) |
| `docs/PRTOE_dcdf_superfluid.md` | superfluid medium seating | no TMSV/\(r\)/pair-\(H\) pin |
| `docs/PRTOE_dyad_gas.md` | dyad gas | no squeeze/pair-\(H\) pin |
| `docs/PRTOE_cosmological_constant.md` | BCS–BEC occupancy / condensation energy | different “pairing” object |
| `docs/PRTOE_induced_gravity.md` / `docs/PRTOE_quantum_gravity.md` | Bogoliubov coherence as heat-kernel regulator | not CHSH \(r\) |
| `papers/**` | paper packages | **zero** artanh/TMSV/pair-Hamiltonian hits |
| `docs/PRTOE_me_mechanism_math.md`, `docs/PRTOE_MATH_SPINE.md` | math spine | **zero** artanh/TMSV/medium-pair hits |

---

## Candidates (and why each fails as a medium pin)

### C1 — Textbook pair \(H\) + \(r=\mathrm{artanh}(\lambda/\omega)\)

**Where:** `scripts/quantum_pair_hamiltonian_tmsv.py` lines 7–11, 41–46, 74–85, 100–117; mirrored in `PAIR_HAMILTONIAN_TMSV.md`, E7 text in `PRTOE_quantum_entanglement.md:101`.

\[
H = \omega(a^\dagger a + b^\dagger b) + \lambda(ab + a^\dagger b^\dagger),\quad
|\lambda/\omega|<1 \Rightarrow r=\mathrm{artanh}(|\lambda/\omega|),\quad
B_{\max}(r)=2\sqrt{1+\tanh^2(2r)}.
\]

**Status:** **Licensed as literature harness only.**  
**Fails medium pin because:** \(\omega,\lambda\) are **not** derived from PRTOE medium numbers. Script sets `medium_omega_derived=False`, `medium_lambda_derived=False`, `medium_r_derived=False`. Scan is free \(\lambda/\omega\in[0,0.95]\).

### C2 — CHSH \(B(r)\) family (Chen et al. 2002)

**Where:** `scripts/quantum_chsh_tsirelson.py`; provenance `CHSH_PROVENANCE.md`.

**Status:** null-hardened literature verification.  
**Fails medium pin because:** \(r\) is a free table parameter; corpus itself marks “identify \(r\) with medium pair parameter” as **aspirational only** (`PRTOE_quantum_entanglement.md:107`).

### C3 — BCS/NJL pairing coupling \(g_p\), hierarchy \(\lambda=k\alpha_c\)

**Where:** e.g. `scripts/de_value_fundamental_gp.py`, `scripts/basement_screening_fence.py`, `scripts/settlement_terms.py`, CC BCS–BEC prose.

**Status:** real corpus pairing physics (gap equation, condensation, hierarchy shell).  
**Fails medium pin because:** these \(\lambda,g_p,\Delta\) are **not** identified with the TMSV squeeze \(r\) or with the two-mode pair Hamiltonian of C1. No line of the form \(r=f(\Delta,T_c,g_p,\ldots)\). `de_value_fundamental_gp.py` even records that **no** stocked interaction supplies the strong \(g_p\sim 2.8\) condensation needs — opposite of a closed pin.

### C4 — Bogoliubov coherence factors \(u^2,v^2\) (bounce door)

**Where:** `scripts/bounce_fa1_transphononic_table.py` lines 15–16, 54–55; “quench / squeezed” language for modes with \(\omega<H_\mathrm{door}\).

**Status:** standard Bogoliubov content mix + door quench bookkeeping.  
**Fails medium pin because:** \(v^2(x)\) is **not** mapped to TMSV \(r\); no CHSH/\(B(r)\) connection; “squeezed” here is cosmological mode-creation language, not the Bell-pair parameter.

### C5 — Page-curve free squeeze dials

**Where:** `G_SQUEEZE=0.12` in `quantum_page_srad_unitary_mvp.py`; `G_SCALE=0.35` in evaporating continuum scripts.

**Status:** instrument knobs.  
**Fails medium pin because:** explicitly free; not derived from medium stock equations; different subsystem (core↔radiation Hawking proxy).

### C6 — “dyad pair” string hits

**Where:** MCMC pair `dyad_mnu_bbnfix` / `cmp_lcdm_mnu_bbnfix`; dyad-exchange NJL \(g\) in `de_value_fundamental_gp.py`.

**Status:** naming collision + weak dyad-exchange coupling.  
**Fails medium pin because:** chain-pair ≠ pair Hamiltonian; dyad-exchange \(g\sim 10^{-15}\) is not a licensed \(\lambda/\omega\) for TMSV.

---

## Pattern hunt results (expanded)

| pattern | hits (approx) | medium pin? |
|---|---:|---|
| `artanh` / closed \(r=\mathrm{artanh}\) | **only** textbook harness + E7/PAIR_H docs | no (no medium numbers) |
| \(\lambda/\omega = \) **numeric** | **0** | — |
| medium \(\omega,\lambda\) derived/pin phrases | only **False/NO** flags in harness | no |
| \(r=r(\mathrm{medium})\) claim | **0** | — |
| gap → \(r\) closed map | **0** real maps (noise hits only) | no |
| pair \(H=\omega\ldots+\lambda(ab+\ldots)\) | harness only | textbook |
| dyad/dCDF “pair” | MCMC + NJL weak \(g\) | not TMSV |
| Bogoliubov \(u,v\) | regulator / door table | not \(r\) |

---

## Explicit corpus statements (consistent with this hunt)

- EN-D2: medium pair \(r\) **not** corpus-defined → MISSING_INPUT (`EN_D2_D3_PAIR_R.md`).  
- EN-D3: explicit dark-sector pair Hamiltonian yielding TMSV **not found** (`EN_D2_D3_PAIR_R.md`).  
- E6/E7: MISSING_INPUT (`PRTOE_quantum_entanglement.md:100–101`).  
- R-MEDR / R-PAIRH board: pin **only if** corpus already contains the map — so far **no** (`BOARD.md`).  
- P1 inventory: `medium_pin_found=False` after 479 files.

---

## What would be needed to flip the verdict

To pay **R-MEDR** and/or **R-PAIRH** without fabrication:

1. **Medium-licensed pair Hamiltonian** from stocked PRTOE fields (not textbook import alone), **or** an explicit corpus map  
   \[
   r = r(\text{named medium numbers}),
   \]
   with every symbol already defined on disk and **no free dial**.  
2. If the path is \(H=\omega(n_a+n_b)+\lambda(ab+\mathrm{h.c.})\), then a **forced** \((\omega,\lambda)\) or \(\lambda/\omega\) from gap, density, stiffness, \(\alpha_c\), \(\xi\), etc., cited with **file:line**.  
3. Then (and only then): implement `scripts/quantum_medium_r_from_corpus.py` that evaluates that formula and \(B(r)\), with `OMP_NUM_THREADS=1`, and re-score E6/E7.

**Not enough:** phrase hits for BCS/Cooper/Bogoliubov; free-\(r\) CHSH tables; Page \(G_\mathrm{SQUEEZE}\); hierarchy pairing \(\lambda=k\alpha_c\); aspirational “identify \(r\) with medium.”

---

## Actions taken this pass

| action | done? |
|---|---|
| Deep search scripts/ + docs/ (+ papers, ForJustin, scratch) | **yes** |
| Read promising files for numeric pin | **yes** |
| Write this report | **yes** |
| Write/run `scripts/quantum_medium_r_from_corpus.py` | **no** — no licensed closed formula with corpus numbers |

---

## Recompute (inventory only; no invent)

```bash
OMP_NUM_THREADS=1 python3 scripts/quantum_medium_r_inventory.py
# optional harness recheck (free λ/ω scan only):
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_pair_hamiltonian_tmsv.py
```

*NO FABRICATIONS. EN-D2/D3 remain MISSING_INPUT.*
