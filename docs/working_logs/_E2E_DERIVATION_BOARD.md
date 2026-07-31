# End-to-end derivation board

*Opened 2026-07-31. Updated end of day — full Track A pass.*

## Grade key

| Grade | Meaning |
|---|---|
| **Derived** | Medium equations produce the object without external pin |
| **Candidate closed** | Mechanism exhibited; at most one named residual / data referee |
| **Partial** | One factor derived, another bet/open |
| **Open (closable)** | Attack path exists |
| **Permanent input / bet** | Stated, not hidden |
| **Story** | No mechanism for H=0,Ḣ>0 |
| **DEAD** | Do not reopen |

## Track A — final status (2026-07-31)

| # | residue | status | notes / files |
|---|---|---|---|
| A1 | A_s γ*/f + c_chop | **CANDIDATE CLOSED** | α_B=ε², k_mom=ε⁴, c_chop=d_⊥=2 → γ*=ε²√2 (+0.9% f, +1.7% A_s). d_⊥=2 theorem (codim-2); p=α=f_ℓ=1 forced on overdamped one-scale; C_geom=d_⊥ primary (non-double-count vs VOS v); sensitivity π/2 (−11% γ*). Residual: κ≈1 in c_chop=κ d_⊥. `census_alpha_B_first_principles.md`, `census_c_chop_derivation.md` |
| A2 | n_s / r-triangle | **CANDIDATE CLOSED** | Route T f=2.225e-4 ⇒ **r=0.992** (point; was [0.81,3.23]); S/ζ=**1.63%** in P-2026-031; n_s env=0.9677 (+0.66σ). Approach OOM open (gap −0.0028). `ns_routeT_closure.md` / `.py` |
| A3 | f̄ / c_w / LO | **CANDIDATE CLOSED** | f̄=2/π (equidistribution + rectified linear); LO dominance proved as bound (quad/lead ≤2% on data band); form c_w=−a (C16 back-reaction). Named residual: value of a (ens [0.32,1.36]; fit 1.80 @1.9σ). `fbar_cw_lo_closure.md` + `scripts/fbar_cw_lo_closure.py` |
| A4 | α_c same-response | **Permanent bet (P-2026-040)** | Factor 3=d **derived**; same-response base α **not derived** (μ=0 tautology or doped-pair ≤12.5%); value bet with **A_s referee only**. Not open derivation debt. `alpha_c_same_response.md` + `scripts/alpha_c_same_response.py` |
| A5 | B1 hydro crown | **PARTIAL (scoped)** | Ψ₀/f_amp **done**; comoving intake share **0.839@χ=5.3** (vs 0.843) candidate; L/D computable in [4.3,5.3]; flow coherent fraction **small** (~0.02, not full-coherence ladder); pour→release / first-principles n **open**. No full inverse claim. `B1_crown_status_2026-07-31.md` |
| A6 | Bounce turn (B7) | **STORY (permanent)** | Legal parts cannot close H=0∧Ḣ>0; all native FRW engines **DEAD** (do not reopen); RP-A reconstructed silhouette only; no legal-part scaffold equations. `bounce_e2e_verdict_2026-07-31.md` |

## Track B — permanent inputs (named, not claimed derived)

| object | status |
|---|---|
| √σ_dark = m_e | Permanent input |
| ξ_H = 1/6 | Permanent input (conformal Higgs) |
| n winding integer | Permanent input (Kibble draw) |
| c = 9/10 | Permanent input (counting; democratic route dead) |
| high-f ~145 TeV, ζ window | Permanent input |
| Z₄ ε_A = 2/9 | Permanent input |
| flatness | Measured, not derived |
| flavour mixing angles | Constitutional silence |
| lattice T_c/√σ | External |
| base α in α_c=3α | Permanent bet (A4) |
| back-reaction a (c_w=−a) | O(1) residual in band |
| κ in c_chop=κ d_⊥ | Unit residual ≈1 |

## Do not reopen

- B2 freeze / 2D-Gaussian tilt (#184)
- Bounce: T=T_c, CSW floor, barotropic dCDF, exotic X, BH/magnetar as sole engines
- c via gravity-blindness democracy (#126)
- Hot-swap production classy under live MPI
- Claiming zero free parameters

## End-state verdict

**Maximal honest derivation (not zero free parameters):**

- ε stack: c counting input; f̄ candidate-closed; α_c = permanent bet (3 derived, base bet P-2026-040)
- A_s: closed form + medium γ* candidate-closed (portal friction + transverse chop)
- n_s: envelope candidate-closed with Route T f
- Bounce: **permanent story** (native engines dead; RP-A reconstructed only)
- Genesis numbers: done; hydro crown partial (intake candidate; n/pour open)

## Session log

| date | done |
|---|---|
| 2026-07-31 | Board opened; Phase 1 structure (VOS microphysics) |
| 2026-07-31 | α_B=ε² Route T candidate-closes γ* |
| 2026-07-31 | Full Track A: c_chop, n_s, f̄/c_w, α_c, B1, bounce verdicts |
| 2026-07-31 | c_chop kinematics pass: d_⊥ defended, residual narrowed to κ≈1; script `census_c_chop_transverse.py` + `census_c_chop_derivation.md` |
| 2026-07-31 | **A4 hardened:** permanent bet P-2026-040 (A_s referee); geometric 3 derived; same-response not derivation debt (`alpha_c_same_response.md`/`.py`) |
| 2026-07-31 | **A5 scoped push:** comoving intake numbers forced; coherent fraction small; crown still open (`B1_crown_status_2026-07-31.md`) |
| 2026-07-31 | **A6 permanent STORY:** kill list + legal-parts no-go; no bounce_rpA_scaffold (`bounce_e2e_verdict_2026-07-31.md`) |
