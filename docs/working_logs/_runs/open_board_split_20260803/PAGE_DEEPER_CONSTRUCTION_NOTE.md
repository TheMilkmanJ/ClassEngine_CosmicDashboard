# Page joint clear — deeper construction note (not header thrash)

**Date:** 2026-08-04  
**Champion artifact:** `page_curve/coevolve_v13.json` (T8 early residual 0.113)  
**Rule:** NO FABRICATIONS · no CANDIDATE without T1–T8+DC3+claim-decoupling+red  

---

## Why small knobs stalled

Early bin [0.10, 0.11) has **monotone** \(S(u)\) while TMS builds. For monotone paths,

\[
\frac{\max S - \min S}{S_\star} \approx \frac{1}{S_\star}\int_{u}^{u+\Delta u}\!\!\frac{dS}{du}\,du
\]

with \(\Delta u = 0.01\). Pure \(G_{\mathrm{TMS}}\) rescales numerator and \(S_\star\) together → **ratio sticky ~0.11**.  
TMS delay / late-dump boosts trade off against T2 or reintroduce late multivalued \(S(u)\).

---

## Deeper construction options (next physics, not edge-tune)

| ID | Idea | Why it might clear early T8 | Risk |
|---|---|---|---|
| **D1** | **Two-phase Hamiltonian:** pure BS until \(u\gtrsim 0.12\), then TMS window | Early bin flat \(S\); peak mid-band | Coupling discontinuity; re-score nulls |
| **D2** | **Occupation dump with fixed free frequencies** (\(w_c\equiv 1\) in free \(A\) too) | Aligns free dynamics with unit-weight \(v\) | May change transfer efficiency |
| **D3** | **Mode-count / continuum band change** (more rad modes) | Changes \(dS/du\) shape | Heavier; not pure header |
| **D4** | **Accept instrument near-miss** until new microphysics | Honest; frees CPU for MCMC booking | Q6 stays OPEN |

**Recommended order:** D1 (cleanest), then D2, then D3. Do **not** resume fine-grid BS_MILD/G_TMS thrash.

### Status (2026-08-04 late)

| ID | Status |
|---|---|
| **D1** | Tried — early T8 improves; T2 not jointly recovered (`B_A_D1_ATTEMPT.md`) |
| **D2** | Tried — **no-op** on champion trajectory (freeze before free-\(w_c\) decay; `B_A_D2_ATTEMPT.md`) |
| **D3** | Tried — densify 20 / mid12 / T2 notch: **not joint** (`B_A_D3_ATTEMPT.md`; v35–v38) |
| **D4** | **Active** — accept instrument near-miss (v13 champion) until new microphysics |

**Stop thrash.** Next Page work only if a licensed new coupling/dump law appears; otherwise machine-wait bbnfix.

---

## Explicit non-actions

- Do not subsample T8 bins  
- Do not loosen T8 threshold  
- Do not file CANDIDATE on v13  
- Do not set `page_curve_claimed`

*NO FABRICATIONS.*

---

## Full residual freeze stamp (2026-08-04)

D1–D4 status above is **locked** for this freeze. Champion remains **coevolve_v13** (T8 early 0.113).  
Full package: `docs/working_logs/_runs/page_full_freeze_20260804/`  
**Do not thrash.** Next Page work only on licensed new microphysics.
