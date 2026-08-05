# Owner action when Fairbank replies (one-pager)

**Date:** 2026-08-04 · **re-stamp:** 2026-08-04T18:14Z (`fairbank_arxiv_trigger_20260804`)  
**Status:** packages **READY on disk** · **HOLD** until you decide after his reply  
**Desk will not:** post · email · invent endorsement · invent second Fairbank TeX

Materials: `docs/arXivReady/<name>.{pdf,tar.gz}` · living `papers/<name>/`  
Checklist: `ForJustin/ARXIV_OWNER_CHECKLIST.md`  
Inventory: `PACKAGE_INVENTORY.md` (this run)  
**Ship-now one-pager:** [`../fairbank_arxiv_trigger_20260804/OWNER_SHIP_NOW.md`](../fairbank_arxiv_trigger_20260804/OWNER_SHIP_NOW.md)

---

## 0. Standing hold (until you break it)

| do | do not |
|---|---|
| Track Fairbank reply | Post any package to arXiv “to get it out” |
| Keep neutrino-mbb packaging **paused** unless he asks a concrete edit | Invent `papers/fairbank-0nubb/` TeX |
| Optional: Zenodo PDF+tar (no endorsement) for non-neutrino packages | Quote H₀ / outperform / unconverged chains as results |
| | File under default `physics.space-ph` |
| | Wait on bbnfix / R−1 / PolyChord for any READY note |

**bbnfix still NOT bookable (2026-08-04T18:14):** lcdm R−1 **0.086466** N=20409 · dyad R−1 **0.128943** N=20302 · both `converged: false`.  
**BBN ε:** **ARITHMETIC VERIFIED (internal)** 3.196%≈3.20% · **EXTERNAL WIN PENDING (no DOI)**.

---

## 1. Branch on Fairbank’s reply

### A. Positive / “happy to endorse” / asks for endorsement code

1. Generate arXiv **hep-ph** endorsement request code (your account).  
2. Send **finished** `docs/arXivReady/neutrino-mbb.pdf` + `neutrino-mbb.tar.gz` (or rebuild from `papers/neutrino-mbb/submission/`).  
3. After endorse → submit **primary category hep-ph**.  
4. Submitter fields: Justin Pulford · pulfordj420@gmail.com · Unaffiliated · USA · career Other.  
5. Paste arXiv ID into owner status / tribunal only when the ID **exists**.  
6. **Do not** wait to “batch” other archives — first successful post on an archive usually auto-endorses you there later.

**Claim fence on post (exactly this):**  
*If* m₁ = ρ_Λ¼ ≃ 2.25 meV (hypothesis) + NO + NuFIT ⇒ m_ββ ∈ [0.04, 5.30] meV; useful comparison is the upper edge vs minimal-ordering ceiling 3.69 meV. Null does not kill; detection >5.30 meV kills the hypothesis.

### B. Content feedback (wants wording / numbers / experimental reach change)

1. Apply **only** concrete requested edits to `papers/neutrino-mbb/` (not the multi-layer Fairbank letter as a second paper).  
2. Rebuild PDF + tarball; refresh `docs/arXivReady/neutrino-mbb.*`.  
3. Re-run `python3 scripts/arxiv_package_audit.py`; re-derive the 8/8 number set if arithmetic moved.  
4. Send revised package; **still HOLD** arXiv until endorse path is clear.  
5. If he revises **nEXO / Ba-tagging reach** in a way that changes the discrimination table, update neutrino-mbb prose — that is still **one** package, not a new Fairbank TeX.

### C. Negative / no endorsement / “not my area”

1. Do **not** invent a different hep-ph endorser story from desk silence — find a **recent hep-ph author** yourself, or park hep-ph.  
2. **Recommended parallel public path (no Fairbank):**  
   - **astro-ph** endorsement for **radio-lattice** (first) + **bbn-eps-bound** (same endorse usually covers both).  
   - Highest non-Fairbank surface; both READY, framework-light.  
3. Optional same week: **Zenodo** one record each for radio-lattice and bbn-eps-bound (PDF + tar.gz, CC BY 4.0) — DOI/Scholar without arXiv.  
4. Keep neutrino-mbb READY on disk for a later hep-ph endorser; do not dilute with a second 0νββ note.

### D. Silence (no reply yet)

1. Continue HOLD on neutrino-mbb packaging.  
2. Owner-only choices that do **not** require Fairbank:  
   - find **astro-ph** endorser for radio-lattice + bbn-eps-bound;  
   - Zenodo those two;  
   - optional gr-qc path for supertrace mirror and/or kination.  
3. Do **not** email Fairbank from blue desk; follow-up is owner judgment.

---

## 2. Order of posts (recommended)

| order | package | archive | when |
|---:|---|---|---|
| **1a** | **neutrino-mbb** | **hep-ph** | If Fairbank (or other hep-ph) endorses |
| **1b** | **radio-lattice** | **astro-ph.CO** (+ .IM) | If hep-ph stalls **or** in parallel after 1a |
| **2** | **bbn-eps-bound** | **astro-ph.CO** | Same astro-ph endorsement as radio-lattice |
| **3** | **lattice-tc-gap** | **hep-lat** | When convenient (thin gap note) |
| **4** | **kination-tracking-note** | **gr-qc** | When convenient |
| **optional** | **supertrace-note** | **gr-qc** | Mirror of existing Zenodo only |

**Why radio before bbn if only one astro post:** ratio-pattern paper is the sharper independent phenomenology; bbn is a clean bound with optional T_c residual. Both are READY; either order is honest if endorsement opens both.

**Why not multi-claim overview / H₀ / fingerprint first:** NOT_READY or wrong shape; chain hygiene and multi-problem hubs draw reclassification risk.

---

## 3. What NOT to claim (any post / any letter)

| forbidden | why |
|---|---|
| “PRTOE predicts m₁ = 2.25 meV” as proven | neutrino-mbb states **hypothesis**; Fairbank letter is complete-conditional bridge |
| Second arXiv note that is Fairbank letter with framework stripped | Duplicate of neutrino-mbb (`fairbank-0nubb` stays README-only) |
| H₀ ≈ 69.9 or “outperforms ΛCDM” as a result | Unconverged chains; R−1 not at stop; letter demoted 2026-08-04 |
| Laplace ΔlnZ / stopped-run best-fit as evidence | Draft itself forbids; sample asymmetry |
| EMPRESS-based ε upper limit | ε=0 already inconsistent; paper states non-result |
| Dense ε_max(T_c) curve as done | Optional residual **not produced** |
| Lattice T_c/√σ central value from gap note | Gap note claims **no** lattice result |
| Improved |ε| bound from radio-lattice vs methanol | Methanol tighter ~35×; paper claims ratio structure |
| Endorsement obtained / “posted” without arXiv ID | NO FABRICATIONS |
| Primary category `physics.space-ph` | Wrong home for all six |

---

## 4. Zenodo without arXiv (always available)

One record per paper: PDF + matching `.tar.gz` · Resource type Preprint · CC BY 4.0 · Get DOI · Publish.  
Never bundle multiple papers. Supertrace already done. Does **not** replace arXiv listing.

**bbn-eps-bound click-path (checklist only, no desk upload):**  
[`../fairbank_arxiv_trigger_20260804/ZENODO_BBN_EPS_BOUND_CHECKLIST.md`](../fairbank_arxiv_trigger_20260804/ZENODO_BBN_EPS_BOUND_CHECKLIST.md)

---

## 5. After first successful arXiv post

1. Record ID + primary category in owner status.  
2. Same archive: subsequent packages usually need no new endorsement.  
3. Other archives still need their own first endorse.  
4. Do not treat process lock / 4-of-10 desk grade as a truth upgrade.

---

*One-pager for owner only. Desk HOLD continues until you act on a real reply or a parallel endorsement path.  
Trigger re-audit 2026-08-04T18:14Z: 6/6 clean · staged MD5 MATCH · no post · no Fairbank contact.*
