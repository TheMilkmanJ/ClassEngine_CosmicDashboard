# FILL_ATTEMPT — `holonomy_evaluator`

**Package:** `theory_construction_wave_20260805/wilson/`  
**Track:** T-W5 Wilson  
**Date:** 2026-08-05  
**Requirement:** zero-knob Wilson-line / path-ordered electric holonomy evaluator for family cycle \(C\)  
**Fence:** NO FABRICATIONS · do not invent evaluator over missing \(A_\mu\) · do not embed \(2/9\)  

---

## 1. Corpus hunt (file:line / path)

| Probe | Result | file:line / path |
|---|---|---|
| Named evaluator candidates | **all ABSENT** | `scripts/koide_wilson_holonomy.py`, `scripts/wilson_family_cycle.py`, `scripts/branch_a_holonomy.py` |
| What exists | inventory **gate only** (never scores \(\theta_W\)) | `scripts/koide_wilson_holonomy_inventory.py:1–25`, `:132–149` |
| Live filesystem (this wave) | only `scripts/koide_wilson_holonomy_inventory.py` | `ls scripts/*holonomy* scripts/*wilson*` |
| Inventory status | **MISSING** | inventory.py:141–148 |
| Prior T7 | **MISSING** | `desk_t7/WILSON_HUNT.md:96–104` |
| Wave re-run | exit **2**; no \(\theta_W\) | [`logs/koide_wilson_holonomy_inventory.log`](logs/koide_wilson_holonomy_inventory.log) |

**Pre-registered bins stand unscored** (HIT_PRIMARY / HIT_SIBLING / ELSE; \(W_\mathrm{hit}=2.617994\times 10^{-5}\) rad) — documentation only until evaluator + inputs 1–4 exist.

---

## 2. Status

| Label | Value |
|---|---|
| **Status** | **MISSING** |
| Fills zero-knob? | **No** |
| Free dial used? | **No** |
| \(\theta_W\) scored? | **0** |

**No PRESENT zero-knob path-ordered / line-integral evaluator.** Building one *over missing \(A_\mu\)* would be invention — refused.

---

## 3. Licensed fill path (without free dial)

| Licensed fill | Still forbidden |
|---|---|
| Zero-knob path-ordered exp / electric line integral **after** requirements 1–4 exist | Evaluator embedding \(2/9\) as target |
| Unit tests on known center elements; continuous non-center angle output | Scoring bins before \(A_\mu\) / path / \(n\) / projection exist |
| Single score of pre-registered bins **once** (no width retune after seeing \(\theta_W\)) | Elastic widen of \(W_\mathrm{hit}\) after near-miss |
| Code path that refuses free knobs (same honesty as inventory exit 2) | Toy constant holonomy “so exit 0” |

### Minimal licensed sequence (from T7, reaffirmed)

1. Connection (1) + projection (4) from same campaign.  
2. Path geometry (2) independent of phase target.  
3. Fix \(n\) or prove \(n\)-independence (3).  
4. **Then** implement evaluator (5) → \(\theta_W\) → score pre-registered bins once.  
5. HIT_PRIMARY crowns Branch A for **#102 candidate only**; **#101 still open**.

---

## 4. What would count as filled

- Named evaluator script present **and** runnable with corpus-fixed inputs only; inventory (or successor) reports `holonomy_evaluator` **PRESENT**.  
- Evaluator must **not** invent missing inputs 1–4.

**Today:** **MISSING**. Inventory deliberately does not invent one.

---

## 5. Fill attempt verdict

> **Fill refused.** No family-cycle Wilson evaluator exists. Writing one over empty \(A_\mu\) is fabrication. Status remains **MISSING**.

*End FILL_ATTEMPT_holonomy_evaluator.md*
