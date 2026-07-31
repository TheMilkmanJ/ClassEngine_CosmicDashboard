# End-to-end derivation board

*Opened 2026-07-31. Goal: maximize Derived / Candidate-closed residues; name permanent inputs; never inflate.*

## Grade key

| Grade | Meaning |
|---|---|
| **Derived** | Medium equations produce the object without external pin |
| **Candidate closed** | Mechanism exhibited; at most one named residual / data referee |
| **Open (closable)** | Attack path exists from corpus objects |
| **Permanent input** | Irreducible or design-level — stated, not hidden |
| **Story** | No mechanism that closes H=0 and Ḣ>0 (or written FRW-exit) |
| **DEAD** | Route killed; do not reopen |

## Track A — closable attack surface

| # | residue | status | notes |
|---|---|---|---|
| A1 | A_s imprint **value** γ*/f from medium | **CANDIDATE CLOSED** | α_B=ε², k_mom=ε⁴, c_chop=d_⊥=2 → γ*=ε²√2 = 2.225e-4 (+0.9% f_ref, A_s +1.7% meas). See `census_alpha_B_first_principles.md`. Named residual: defend d_⊥=2 |
| A2 | n_s residual / r-triangle promotion | **Candidate closed (gates hold)** | r ∈ [0.81, 3.23]; n_s = 0.9677; medium f now supplied by A1 Route T. Full n_s−1 residual still envelope/transient |
| A3 | f̄ LO / c_w residual | **Open (closable)** | Form advanced in `family_coupling_lagrangian_spec.md`; value of a open |
| A4 | α_c same-response identity | **Open (partial)** | “3”=d geometry; base-α identity still a bet |
| A5 | B1 hydrodynamic crown | **Open (partial)** | Ψ₀/f_amp numbers done; pour→release / n not |
| A6 | Bounce turn (B7) | **Story** | RP-A only path; all native FRW engines dead |

## Track B — permanent inputs / blocked

| object | status | why |
|---|---|---|
| √σ_dark = m_e | Permanent input | Irreducible portal |
| ξ_H = 1/6 | Permanent input | Conformal Higgs; induced-G conditional |
| n winding integer | Permanent input (draw) | Kibble; first-principles n needs bounce |
| c = 9/10 | Permanent input | Counting assumption; democratic route dead |
| high-f ~145 TeV, ζ window | Permanent input | Dimensionful + committed dilution |
| Z₄ ε_A = 2/9 | Permanent input | Potential input |
| flatness | Measured | Not derived |
| flavour mixing angles | Constitutional silence | Not a gap |
| lattice T_c/√σ | External | Out of repo |

## Do not reopen

- B2 freeze imprint / 2D-Gaussian tilt (#184)
- T=T_c, CSW floor, barotropic dCDF, exotic X as FRW bounce engines
- c via gravity-blindness democracy (#126)
- Hot-swap production classy under live MPI

## Session log

| date | done |
|---|---|
| 2026-07-31 | Board opened; Phase 1 microphysics script + γ* findings |
| 2026-07-31 | Phase 1 result: overdamped structure derived; absolute γ* **not** derived; α_c²/2 near-miss rejected as coincidence risk |
| 2026-07-31 | Phase 2: r-triangle + n_s envelope re-verified; candidate grade stands; full promotion blocked on A1 |
| 2026-07-31 | **α_B first principles:** portal α_B=ε²; Route T (c_chop=2) → γ*=ε²√2 matches f and A_s to ~1–2% without A_s fit. A1 → CANDIDATE CLOSED |

## Success criterion for “end-to-end”

Not zero free parameters. Success means:

1. Every Track-A item is Derived, Candidate closed, or honestly killed.
2. Every Track-B item is named as permanent input (no false “derived”).
3. Bounce is either RP-A derived or permanent Story with no fake engines.
