# arXiv-ready file pass — 2026-08-03

**Trigger:** seats agreed **no desk-runnable derivations remain**  
(Claude RED ANSWER + Grok BLUE ANSWER; exhaustion map 42 blocked / 28 paid).  
**Directive:** ChatGPT REFEREE PROCESS DIRECTIVE — derivation exit gate / arXiv-ready transition.

## Definition (all three required)

A file is **arXiv ready** only if:

1. **Complete** enough to stand as a paper candidate  
2. **No load-bearing TODO** (owed derivation / missing artifact / hidden block)  
3. **Substantive** enough to be worth a paper  

**Not allowed:** padding weak files · false READY · reopening derivation hunting unless a *new* missing derivation appears during the pass.

## Related (do not reinvent)

| Artifact | Role |
|---|---|
| `docs/working_logs/_ARXIV_CANDIDACY.md` | Prior ruthless inventory (PAPER_CANDIDATE from docs = 0 as of 2026-08-03 re-audit) |
| `docs/working_logs/_FILE_COMPLETION_STATUS.md` | Document job status ≠ paper status |
| `docs/working_logs/_PACKAGE_AUDIT.md` | TeX package hygiene |
| `papers/*` | Existing SHIPPED / READY_PACKAGE bar |
| `docs/working_logs/_runs/derivation_sprint_20260803/DERIVATION_EXHAUSTION_MAP.md` | Blocked register — not derivation targets |

## Seat roles

| Seat | Job |
|---|---|
| **Grok (blue)** | Drive file-by-file; prep only where three conditions can hold; stamp NOT_READY honestly |
| **Claude (red)** | Grade each prepared verdict against the three conditions; "not ready" expected |
| **ChatGPT (ref)** | Process honesty; record exit-gate agreement; no new theory |

## Phase order

1. **P0** Exit-gate agreement stamped (this board + tribunal) — **DONE**  
2. **P1** Reconfirm existing `papers/` packages (hygiene only; no invention)  
3. **P2** Grade every top-level `docs/PRTOE_*.md` → READY / NOT_READY / CORPUS_ONLY with one-line reason  
4. **P3** Only if any new PAPER_CANDIDATE emerges: extract narrow claim (no padding)  
5. **P4** Refresh `docs/arXivReady/` staging if packages change  

## Live verdict table (filled as pass runs)

### Existing packages (`papers/`)

| package | prior status | pass status | notes |
|---|---|---|---|
| supertrace-note | SHIPPED | **RECONFIRM SHIPPED** | hygiene clean; Zenodo live |
| neutrino-mbb | READY_PACKAGE | **RECONFIRM READY** | Fairbank pause; hep-ph endorsement |
| radio-lattice | READY_PACKAGE | **RECONFIRM READY** | astro-ph endorsement |
| lattice-tc-gap | READY_PACKAGE | **RECONFIRM READY** | hep-lat endorsement |
| bbn-eps-bound | READY_PACKAGE | **RECONFIRM READY** | 3 pp; tarball clean |
| kination-tracking-note | READY_PACKAGE | **RECONFIRM READY** | 2 pp; tarball clean |
| fairbank-0nubb | NOT_READY | **HOLD NOT_READY** | README only; do not invent TeX |

### docs inventory (P2 DONE)
See `PASS_TABLE.md`: **CORPUS_ONLY 43 · NOT_READY 24 · new PAPER_CANDIDATE 0**.

### `docs/PRTOE_*.md` (67 inventory)

*Filled in PASS_TABLE.md as graded.*

## Hard non-goals

- Invent A_ωJ / Wilson A_μ / H_re / Page curve / additivity derivation  
- Second Fairbank TeX  
- Promote OPEN-THEORY → paper without closed science  
- Pad CORPUS_ONLY into paper form  

---

*Opened 2026-08-03 with derivation exit gate.*


## Red AGREE-IF cure (17:34)

- Added `PRTOE_induced_gravity.md` CORPUS_ONLY
- Added `PRTOE_small_scale_structure.md` CORPUS_ONLY
- Scope: 61 top-level + 8 exploratory inventory = **69** rows
- PAPER_CANDIDATE still **0**
