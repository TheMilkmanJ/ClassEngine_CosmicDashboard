# Paper red-team fixes — attack → location → status

**Dated:** 2026-08-02/03  
**Sources audited:** live `papers/*/main.tex` (and matching `submission/main.tex` where present).  
**Rule:** status is **FIXED** only if the edited TeX already carries the fix; otherwise **PENDING** or **residual** (honest disclosure present, optional content still owed).

---

## Supertrace — `papers/supertrace-note/main.tex`

| attack | fix location | status |
|---|---|---|
| **comment not discovery** | Abstract (agreement is “arithmetic rather than evidential”); §Remarks opens “This is a comment on existing literature, not a new result” and credits Navarro-Salas / Pauli–Visser | **FIXED** |
| **ξ = 1/6 extra** | §The reduction: scalar term drops only “if one assumes ξ = 1/6”; conformal value is “an input … not by any measurement”; §What still separates them + Table (Higgs “retained if ξ = 1/6 (assumed)”); §Remarks ties ξ to naturalness, not free counting output | **FIXED** |
| **Pauli m2k distinct** | §Remarks: Pauli mass sum rules ∑ (−1)^{2S} g m^{2k} = 0 are “a separate matter … do not reduce to” the boxed N_{1/2}=4N_1; note concerns only curvature-weighted conditions (cites Visser 2019 N_BSM=68) | **FIXED** |

Package status: **SHIPPED** (Zenodo). No residual from this red-team pass.

---

## Neutrino — `papers/neutrino-mbb/main.tex`

| attack | fix location | status |
|---|---|---|
| **coincidence not evidence** | Abstract (“We do not propose a mechanism”); §Introduction (no position on MaVaN etc.); §What is assumed — *The coincidence itself*: hypothesis, not result; “weak grounds”; “not because the coincidence is evidence for itself” | **FIXED** |
| **lower edge fragile** | Abstract + full §Why the lower edge is nonzero, and why it is fragile (triangle margin 0.045 meV; unprotected; vanishes at m₁ ≳ 2.32 meV); useful statements restricted to upper edge | **FIXED** |
| **nEXO low prob** | §What would test it / Where the experiments fall: exceeds 4.7 meV only **10.8%** of phases; “roughly one in nine”; discrimination vs probability separated | **FIXED** |
| **cosmology first** | §The effective mass (Σm_ν ≲ 72 meV; “may well be graded by cosmology before any laboratory experiment”); Conclusion: “Cosmology will likely speak first” | **FIXED** |

Package status: **READY_PACKAGE**. Optional owner note (not a hold): lower edge knife-edge under NuFIT 1σ — already stated in prose.

---

## Radio — `papers/radio-lattice/main.tex`

| attack | fix location | status |
|---|---|---|
| **methanol tighter is the point** | Abstract: methanol few×10⁻⁷, ~35× tighter than 21 cm reinterpretation; §Where the amplitude actually stands + Conclusion: two radio rows “do not improve the limit … and we do not claim that they do”; claim is ratio structure / residual DOF | **FIXED** |
| **two rows only** | Abstract: “Only the 21 cm and Faraday rows are presently usable”; §Sensitivity: treat only those two; σ_ε = σ/√8; √11 is upper bound not forecast | **FIXED** |
| **DM caveat** | Abstract (DM reconstruction “degenerate with the fitted column unless an independent electron column is supplied”); §Sensitivity DM subsection: constant ε absorbed exactly by fitted DM | **FIXED** |
| **synchrotron convention** | Abstract (−1 or −3 by γ vs E label); §Synchrotron characteristic frequency + §What is assumed (*The synchrotron convention*) | **FIXED** |
| **template not survey** | Abstract: “theoretical template for multi-band programmes, not a new observational bound or an end-to-end survey forecast”; pattern not competitive amplitude bound | **FIXED** |
| **no framework** | Abstract / setup: ε free, “commit to no mechanism”; no framework name in TeX; claim independent of model | **FIXED** |

Package status: **READY_PACKAGE**. Content hold from DM demotion closed by two-row framing (not by restoring a third row).

---

## Lattice — `papers/lattice-tc-gap/main.tex`

| attack | fix location | status |
|---|---|---|
| **knowledge limit** | Abstract + §The missing number + Conclusion: no published T_c/√σ for SU(2) N_f=3 light fundamentals; gap is literature fact | **FIXED** |
| **demote stake** | Abstract + §A pre-registered stake (transparency only): stake “not as a result of this note”; ordinary precision expected null on stake | **FIXED** |
| **no result claimed** | Abstract: “The result of the note is that the calculation is conventional, well posed, and missing”; Conclusion: “The computation itself remains to be done” | **FIXED** |

Package status: **READY_PACKAGE**. No lattice number claimed.

---

## BBN — `papers/bbn-eps-bound/main.tex`

| attack | fix location | status |
|---|---|---|
| **prior literature** | §Introduction: Hart–Chluba, Sekiguchi–Takahashi, Dent–Stern–Wetterich (varying-constants BBN response matrices); distinguishes constant/power-law bounds from windowed ramp | **FIXED** |
| **Aver / EMPRESS** | §The Aver bound → boxed ε < 3.2% (2σ); §Why EMPRESS cannot be used: standard BBN already +2.9σ, so EMPRESS yields no ε bound | **FIXED** |
| **T_c scan explicit** | §Setup: T_c free in [70, 500] keV; §The Aver bound: dense ε_max(T_c) map “not reported here”; bound is verified only at measured T_c of the elasticity run (179 keV), not claimed uniform over the window | **FIXED** (disclosure) |

**Residual (optional content, not a missing disclosure):** dense ε_max(T_c) curve over [70, 500] keV still not produced. Bound stands at measured T_c only. See `_ARXIV_CANDIDACY.md` / papers README.

Package status: **READY_PACKAGE** (endorsement-gated; optional curve residual).

---

## Scoreboard

| package | attacks listed | FIXED | residual / PENDING |
|---|---:|---:|---|
| supertrace-note | 3 | 3 | 0 |
| neutrino-mbb | 4 | 4 | 0 |
| radio-lattice | 6 | 6 | 0 |
| lattice-tc-gap | 3 | 3 | 0 |
| bbn-eps-bound | 3 | 3 | optional dense T_c curve (content residual, not attack miss) |
| **Total** | **19** | **19** | dense ε_max(T_c) only |

No **PENDING** red-team prose fixes remaining in live `main.tex` as of this audit.

---

*Filed 2026-08-02/03 after reading edited package sources. Companion: short hardening notes added under each READY/SHIPPED card in `_ARXIV_CANDIDACY.md`.*
