# PASS3 — desk/script derive paydown (2026-08-03)

**Owner:** Grok blue (PASS3)  
**Rule:** NO FABRICATIONS. Pay only what existing corpus + cheap scripts can support.  
**Did not touch:** live MCMC chains; A4 T14 i6 production (`run_t14_i6_production.sh` / ring_toroidal 128³).  
**Parent board:** [`docs/working_logs/SCIENCE_DEBTS_2026-08-03.md`](../../SCIENCE_DEBTS_2026-08-03.md)

---

## 0. Mission

For debts D2–D9 (and open desk items on the board):

1. If a `REPORT.md` already paid the debt → **wire RESULT into** the relevant `docs/PRTOE_*.md` claims ledger (upgrade OPEN → machine-backed / derived-conditional with path).
2. If a cheap script exists (<2 min) → **run**, confirm, cite.
3. If blocked → one-line **OPEN-BLOCKED** with exact missing input; move on.

---

## 1. Recompute-only scripts (this pass)

| Script | Result | Wall |
|---|---|---|
| `papers/bbn-eps-bound/recompute_eps_bound.py` | **PASS** — ε 2σ ceiling **3.196%** ≈ paper 3.20% | <1 s |
| `scripts/junction_quartet_closure.py` | **VERDICT: quartet closes** at Γ_φ/θ̇=9.03e7; ω_J=5.672 keV; R=5.050e−5 | <1 s |
| `scripts/rm_coherence_kibble.py` | Geometric transfer + multi-χ table; void shortfall **×20 unchanged** | <1 s |
| `scripts/quantum_wkb_medium_identity.py` | 4/4 PASS; WKB↔medium identity hardened | <1 s |
| `scripts/funnel_edge_identity.py` | ALL CONTROLS PASS (m1* edge coin; not a Koide close) | <1 s |
| `scripts/koide_lock_algebra_verification.py` | Algebra holds; physics residuals open | <1 s |
| `scripts/occupancy_frequency_keystone_identity.py` | c_K debt re-seated as instance; no new mechanism | <1 s |

BBN hard-win arithmetic remains package-ready (`papers/bbn-eps-bound/`). Prior debt reports not re-derived as physics; only reconfirmed where recompute-cheap.

---

## 2. Ledger upgrades (by debt)

### D2 — P-042 / w(a) + template

| Action | Detail |
|---|---|
| **Wired** | P-040 corollary OWED block annotated in [`PRTOE_PREREGISTERED_PREDICTIONS.md`](../../../PRTOE_PREREGISTERED_PREDICTIONS.md) (PASS3 / D2 paydown note) |
| **Wired** | [`PRTOE_dcdf_superfluid.md`](../../../PRTOE_dcdf_superfluid.md) claims **#9–#12** added |
| Sources | `w_a_onset_20260803`, `debt_p042_d2_cures_20260803`, `debt_p042_template_20260803` |

| Claim | New grade |
|---|---|
| True `(.)w_dcdf` bare/conv/thaw/both | **machine-backed** |
| `(.)w_dcdf` blind to thaw (VOID thaw column) | **machine-backed** |
| Template R(x) centers + analytic log10 bias | **machine-backed** / desk |
| High-z budget = photons/ν not w_dcdf | **machine-backed** |
| Full onset-likelihood / MCMC template bias | **OPEN-BLOCKED** (needs free log10_zon likelihood; no MCMC this pass) |

**Do not quote:** thaw physics from `(.)w_dcdf`; onset clock from w_dcdf alone (#17 is ρ_tot/ρ_r).

---

### D3 — Baryogenesis ω_J

| Action | Detail |
|---|---|
| **Confirmed** | Quartet **machine-backed** as **back-solve only** |
| **Recompute** | `junction_quartet_closure.py` → Γ_φ/θ̇=**9.0319×10⁷**, ω_J=**5.672 keV**, R=**5.050e−5** |
| **Wired** | [`PRTOE_baryogenesis.md`](../../../PRTOE_baryogenesis.md) ledger #5–#6 paths + recompute numbers; A_ωJ named |

| Claim | Grade |
|---|---|
| Quartet closes at computed ratio (not ~10⁷ shorthand) | **machine-backed** (circular as derivation) |
| Forward ω_J from seat micro | **OPEN-BLOCKED** #39 |

**OPEN-BLOCKED exact missing input:** axiom **A_ωJ** — seat-term **decay constant χ + pinning curvature** (or micro definition of ω_J from junction coupling J). Corpus states neither. **Do not invent.**

Reports: `debt_baryo_omegaJ_20260803`, `debt_baryo_d3_provenance_20260803`, `debt_omegaJ_forward_formulability_20260803`.

---

### D4 — Hierarchy §6f / μ_5

| Action | Detail |
|---|---|
| **Wired** | [`PRTOE_hierarchy_problem.md`](../../../exploratory/PRTOE_hierarchy_problem.md) #3, #5, #9 → debt_hierarchy_6f + full script list |
| Sources | `hierarchy_6f_double_count`, `hierarchy_alpha_scale_fork`, `hierarchy_anchor_budget`, `hierarchy_kF_and_bendover`, `basement_mu5_source` |

| Claim | Grade |
|---|---|
| Anchor band 0.55–1.78 TeV | **complete-conditional on horn (b)** |
| §6f residual after double-count | **OPEN-BLOCKED** (sized: horn (a) ×5.6–×9 residual; ~×11 total at M_Z) |
| #146 μ_5 = θ̇/2 candidate | **derived-conditional** candidate (size vs doping owed) |

**Manuscript rule (Claude D4):** quote ×5–×11 **only as horn (a)**; horn (b) is A_s-selected stance, not unconditional ×11.

---

### D5 — Koide #101/#102

| Action | Detail |
|---|---|
| **Leave OPEN-THEORY** | No mechanism invented |
| **Wired** | [`PRTOE_koide_relation.md`](../../../PRTOE_koide_relation.md) #3–#4 cite 15 scripts + Wilson inventory; #10 algebra row |

| Claim | Grade |
|---|---|
| Protection / fence | paid (unchanged) |
| #101 null enforcer / #102 Brannen phase | **OPEN-BLOCKED** (OPEN-THEORY) |
| Desk algebra re-runs | **machine-backed** (algebra only) |

**OPEN-BLOCKED exact missing inputs:** mechanism forcing graded null to ~10⁻⁵; for Wilson branch — **dark-SU(2)** coupling / lattice inputs with **pre-registered bin widths** (`debt_koide_wilson_20260803`).

---

### D6 — Magnetism void / RM

| Action | Detail |
|---|---|
| **Upgrade** | RM geometric formula **paid** → ledger #8 **machine-backed** / derived-conditional (scale) |
| **Body** | §3a + §6 summary rewritten (no longer “formula missing”) |
| **Void** | stays **OPEN-BLOCKED** |
| **Recompute** | `rm_coherence_kibble.py` |

| Claim | Grade |
|---|---|
| ⟨RM·RM⟩ geometric + ξ_K → (θ_ξ, ℓ) | **machine-backed** (scale); survey **ℓ ~ 25–60** (χ 2–5 Gpc) |
| Absolute C_ℓ / n_e amplitude | **OPEN** (external) |
| Void floor ≥10⁻¹⁶ G vs B_seed ×20 short | **OPEN-BLOCKED** |

**OPEN-BLOCKED exact missing input (void):** either external relaxation of blazar floor (WATCH-EXTERNAL) **or** new internal inter-line seed mechanism not bounded by return-flux theorem. Formula does not raise B_void.

Reports: `debt_rm_formula_20260803`, `debt_magnetism_20260803`.

---

### D7 — Bounce turn / F-A3

| Action | Detail |
|---|---|
| **Confirm** | Classical turn **OPEN-BLOCKED** |
| **Wired** | [`PRTOE_bigbang_no_singularity.md`](../../../PRTOE_bigbang_no_singularity.md) #3 → debt_bounce + **debt_bounce_FA3** + `bounce_fa3_hcross_attempt.py` |

| Claim | Grade |
|---|---|
| ρ_bounce number | **machine-backed** (floor ≠ turn) |
| Homogeneous FRW bounce from floor/T_c alone | **failed / retired** |
| Exterior H_re from medium stress+junction | **OPEN-BLOCKED** (F-A3) |

**OPEN-BLOCKED exact missing input:** F-A3 **branch / metric-off re-attachment declaration** — continuous H-cross at finite ρ **conflicts** FRW constraint H²∝ρ. Cannot derive exterior H_re without declaration. Report: `debt_bounce_FA3_20260803` (Derived exterior H-cross? **No.**).

---

### D8 — Leptophilia

| Status | **Left obstructed** — no desk reopen without new charge assignment |
|---|---|
| Action this pass | None (board CONFIRMED) |

---

### D9 — Page curve

| Action | Detail |
|---|---|
| **Confirm already wired** | [`PRTOE_information_paradox.md`](../../../exploratory/PRTOE_information_paradox.md) #2 coefficient **derived/paid**; #4 curve **OPEN-BLOCKED** |
| Entropy | same split in `PRTOE_entropy.md` |

| Claim | Grade |
|---|---|
| Area-law coefficient 12π/48π=1/4 | **derived** / paid |
| Roster extension | **complete-conditional** (commitment E) |
| Dynamical S_rad(v) vs Page time | **OPEN-BLOCKED** |

**OPEN-BLOCKED exact missing input:** finite-core **phonon Hawking** exterior entropy functional of retarded time + mass-loss law + Page-time estimate. Scaffold only (`quantum_page_curve_scaffold.py`). **Forbidden to fake from coefficient alone.** Report: `debt_page_curve_20260803`.

---

## 3. Files touched (ledger / body wire)

| Path | Change |
|---|---|
| `docs/PRTOE_PREREGISTERED_PREDICTIONS.md` | D2 PASS3 paydown note on P-040 OWED |
| `docs/PRTOE_dcdf_superfluid.md` | claims #9–#12 |
| `docs/PRTOE_hierarchy_problem.md` | #3 horn (b), #5 sized residual, #9 μ_5 |
| `docs/PRTOE_baryogenesis.md` | #5 recompute + #6 A_ωJ |
| `docs/PRTOE_koide_relation.md` | #3–#4 script cite; #10 algebra |
| `docs/PRTOE_cosmic_magnetism.md` | §3a, §6, claims #7–#8 RM paid / void open |
| `docs/PRTOE_bigbang_no_singularity.md` | #3 F-A3 wire |
| `docs/working_logs/SCIENCE_DEBTS_2026-08-03.md` | board residual column PASS3 |

**Not rewritten as new physics:** any OPEN-THEORY residual listed below.

---

## 4. Summary table — upgrades vs hard blocks

### Ledger upgrades this pass

| Debt | Upgrade |
|---|---|
| D2 | w_dcdf truth + thaw-blind + template centers → **machine-backed** (3 ledger rows + prereg note) |
| D3 | Quartet recompute numbers on ledger; forward named A_ωJ |
| D4 | horn (b) conditionality + full script paths + μ_5 candidate row |
| D5 | Full 15-script cite + Wilson inventory; algebra row |
| D6 | RM formula **OPEN → machine-backed (scale)**; body §3a/§6 |
| D7 | F-A3 report + script on bounce turn row |
| D9 | Confirmed coefficient paid / curve OPEN (already wired) |
| HW3 | BBN ε recompute **PASS** 3.196% |

### Remaining hard blocks (exact missing input)

| Debt | OPEN-BLOCKED missing input |
|---|---|
| **D2 residual** | Full onset-likelihood / MCMC template bias on free `log10_zon` |
| **D3** | **A_ωJ:** seat χ + pinning curvature (micro ω_J from J) |
| **D4** | Ontology resolution horn (a) vs (b); host Fermi-surface vs point; μ_5 size vs doping |
| **D5** | #101 null enforcer to ~10⁻⁵; dark-SU(2) Wilson inputs (bins registered) |
| **D6 void** | Blazar-floor external debate **or** new inter-line seed (not return-flux bounded) |
| **D6 RM amp** | External n_e model + survey pipeline |
| **D7** | F-A3 exterior H_re without inventing branch/metric-off declaration |
| **D8** | New lepton charge assignment (obstructed) |
| **D9** | Phonon-Hawking finite-core Page dynamics formalism |
| **D1** | T14 i6 128³ production TC (A4 **in flight** — left alone) |

---

## 5. Honesty lock

- **Zero false closures.** Nothing marked COMPLETE that is still OPEN-THEORY.
- Quartet “closes” = **arithmetic at back-solved ω_J**, not a forward derivation.
- RM “paid” = **geometric scale transfer**, not void floor, not σ_RM.
- Hierarchy residual = **sized adverse under horn (a) only**.
- Page coefficient paid ≠ Page curve computed.
- Bounce FA3 attempt: **explicit No** on derived H_re.

**4/10 claim-credibility gap unchanged** — formulability kills remain formulability kills.

---

## 6. Artifact index (debt reports walked)

```
docs/working_logs/_runs/debt_p042_d2_cures_20260803/REPORT.md
docs/working_logs/_runs/debt_p042_template_20260803/REPORT.md
docs/working_logs/_runs/w_a_onset_20260803/REPORT.md
docs/working_logs/_runs/debt_baryo_omegaJ_20260803/REPORT.md
docs/working_logs/_runs/debt_baryo_d3_provenance_20260803/REPORT.md
docs/working_logs/_runs/debt_omegaJ_forward_formulability_20260803/REPORT.md
docs/working_logs/_runs/debt_hierarchy_6f_20260803/REPORT.md
docs/working_logs/_runs/debt_koide_20260803/REPORT.md
docs/working_logs/_runs/debt_koide_wilson_20260803/REPORT.md
docs/working_logs/_runs/debt_magnetism_20260803/REPORT.md
docs/working_logs/_runs/debt_rm_formula_20260803/REPORT.md
docs/working_logs/_runs/debt_bounce_20260803/REPORT.md
docs/working_logs/_runs/debt_bounce_FA3_20260803/REPORT.md
docs/working_logs/_runs/debt_page_curve_20260803/REPORT.md
docs/working_logs/_runs/hard_win3_bbn_eps_recompute_20260803/REPORT.md
```

*End PASS3. No MCMC. No A4 kill. No invented physics.*
