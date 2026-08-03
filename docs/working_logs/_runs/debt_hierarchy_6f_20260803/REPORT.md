# Debt run: hierarchy §6f residual + basement μ_5

**Date:** 2026-08-03  
**Goal:** Size the adverse residual after double-count removal. Do **not** close a fake.  
**Scripts (all `nice -n 19`, all <3 min):**

| script | checks | out |
|---|---|---|
| `scripts/hierarchy_6f_double_count.py` | 5/5 | `hierarchy_6f_double_count.out` |
| `scripts/basement_mu5_source.py` | (no asserts) | `basement_mu5_source.out` |
| `scripts/hierarchy_anchor_budget.py` | asserts pass | `hierarchy_anchor_budget.out` |
| `scripts/hierarchy_alpha_scale_fork.py` | run clean | `hierarchy_alpha_scale_fork.out` |
| `scripts/hierarchy_kF_and_bendover.py` | 9/9 | `hierarchy_kF_and_bendover.out` |

Heavy integrators (`hierarchy_vertex_crossed_box.py`, `hierarchy_fock_self_energy.py`) not re-run; numbers taken from the hierarchy file / prior evaluation (c=0.789, a=0.281).

Source text: `docs/PRTOE_hierarchy_problem.md` §6e–§6i and “6f, examined (2026-07-29)”.

---

## 1. Residual after double-count removal (factor on anchor)

### What the double-count removes

Horn (a) as stated — “α is electromagnetic, so evaluate α_c at the pairing scale” — **double-counts medium polarisation**. §6c already uses

```
V(q) = e²/(q² + m_D²) = (e²/q²)/ε(q),   m_D² = e² · 2 N₀
```

so the momentum dependence of the effective charge is already in ε(q). Running α from q=0 to q∼2k_F *is* that same screening statement. Standard many-body construction pairs a **bare** charge with an explicit dielectric, never a running charge *and* a dielectric.

**Size of the already-applied piece vs QED running (script [3]):**

| effect | log measure | note |
|---|---|---|
| §6c Thomas–Fermi screening | ln(1+1/b) = **4.2871** | dominant |
| QED run α(0)→α(M_Z) | ln(α(M_Z)/α(0)) = **0.0686** | |
| ratio | **62.5×** | TF ≫ QED run |

So the double-count argument kills the *naive full replacement* of α(0) by α(scale). Most of what horn (a) proposes to add is already present.

### What survives (the residual)

Two physically distinct polarisations:

1. **Medium Thomas–Fermi** (real carriers, ∝ N₀) — already in §6c.  
2. **QED vacuum polarisation** (virtual SM pairs, present at zero density) — **not** double-counted by ε(q).

Whether (2) applies turns on whether the medium’s constituents carry SM electric charge. The corpus answers **adversely** (§6e): vacuum is *compensated* (n_e = n_h), not uncharged; carriers are charged. On the program’s own reading (light = medium Goldstone → same U(1)), residual running is real.

### Sized residual factor on the anchor

Worst case: full SM running **on top of** screening (script [5]), ratio of M_anchor to the α(0) baseline:

| α used | 1/α | k | **anchor factor vs α(0)** |
|---|---|---|---|
| α(0) (recorded) | 137.036 | 1.36461 | **×1** (baseline) |
| α(M_Z) | 127.951 | 1.34309 | **×5.58** |
| α at ~3 TeV (approx) | 125.5 | 1.33702 | **×8.89** |

**Residual after double-count removal: adverse factor of order 5–10 on the anchor** (×5.6 at M_Z, ~×9 near the pairing shell). This compounds the baseline ×2.00 overshoot of the α(0) convention against 4πm_H.

### Full fork table (absolute anchors, exact-solution prefactor convention)

From `hierarchy_6f_double_count` + `hierarchy_alpha_scale_fork` (4πm_H = 1573.9 GeV):

| α used | 1/α | α_c | k | M_anchor | vs 4πm_H |
|---|---|---|---|---|---|
| **α(0)** | 137.036 | 0.021892 | 1.36461 | **3153 GeV** | **×2.00** |
| α(M_Z) | 127.951 | 0.023446 | 1.34309 | 1.76×10⁴ GeV | **×11.2** |
| α at Planck floor (1/α₂+1/α_Y) | 104.94 | 0.028588 | 1.28100 | 1.50×10⁶ GeV | **×956** |

Sensitivity: ∂lnM/∂lnα_c = **25.77** (recorded 25.8). Exact landing on 4πm_H would need 1/α = **140.74** — **2.70% weaker than the IR endpoint**, which is the *maximum* 1/α QED ever takes. Running cannot rescue; it only moves further adverse.

### Honest one-line size

> After removing the double-count, the residual is **not zero**: if constituents are charged (corpus: yes), genuine vacuum polarisation still multiplies the anchor by **~×5.6 (M_Z) to ~×9 (few TeV)**, adverse, on top of the recorded ×2.00. Total exposure under horn (a) is **~×11 at M_Z**.

**Not closed.** Narrowed, sized, adverse.

---

## 2. μ_5 source status (#146 merge)

Script: `basement_mu5_source.py`.

### Candidate source (corpus pieces, no new field)

| piece | role |
|---|---|
| #125 operator | S (L̄ H e_R)/Λ — phase of S absorbed only by e_R |
| baryogenesis | μ = θ̇; θ̇/H = 2.4×10⁶ at T_sph |

Phase S → e^{iθ}S forces e_R → e^{-iθ}e_R only:

- μ_R = θ̇, μ_L = 0  
- μ_V = θ̇/2 (gauged e-number → **Debye-screened**)  
- **μ_5 = θ̇/2** (ungauged chirality → **survives**)

That is species-selective (electron) and axial after screening — the object #146 asked for.

### Magnitude (only epoch where corpus pins θ̇)

| quantity | value |
|---|---|
| θ̇ ledger | 59.7 eV |
| θ̇ from ratio×H (T_sph=131.7 GeV) | 58.52 eV (2% match) |
| **μ_5 = θ̇/2** | **29.9 eV** |
| w_J at same epoch (comparison only) | ~5.7 keV (~200× larger) |

### Merge verdict

#146 carried two open items that collapse to one:

1. Does charged-lepton selection survive the shell phase?  
2. What puts μ_5 there?

Both hold only in the **broken phase** (Dirac cone exists below EW) and fail in the unbroken shell phase (no vector-like species). Open count: **2 → 1**. Survivor is already registered as §6f’s phase fork: *does the medium screen in the broken phase?*

### Still owed (attackable kill paths)

- **Size:** μ_5 ~ 30 eV at T_sph vs doping the band structure needs — docket states doping via N_screen = 2N₀, **no μ_5 in eV to compare**. Candidate can die on size.  
- **Epoch:** θ̇ pinned at T_sph; if doping is needed elsewhere, must carry θ̇ ~ T³ and respect turn-budget saturation.

**#146 μ_5 source: candidate exists and merges; not verified against doping size; not a closure of §6f.**

---

## 3. Numeric tables (scripts)

### A. Residual running factors (6f double-count [5])

| scale | 1/α | k | factor on M vs α(0) |
|---|---:|---:|---:|
| M_Z | 127.951 | 1.34309 | **5.58** |
| ~3 TeV | 125.5 | 1.33702 | **8.89** |

### B. Scale fork absolute (alpha_scale_fork)

| α | overshoot vs 4πm_H |
|---|---:|
| α(0) | ×2.003 |
| α(M_Z) | ×11.17 |
| α(M_Pl) | ×955.5 |

### C. Anchor band error budget (hierarchy_anchor_budget)

| input | effect on M | share |
|---|---|---|
| shared k (±0.47% A_s) | ±16% | minor |
| α_c = 3α | ±33 · δlnα_c | live bet |
| −3/2 | none | derived exact |
| m_H via 4π | ±0.1% | negligible |
| O(λ) scheme e⁰…e^{-(c+a)} | ×3.2 band | **DOMINANT** |

Bare anchor (no O(λ)): **1.576 TeV**; fully corrected: **0.541 TeV**; band **0.55–1.78 TeV**. Amplification 1/(kα_c) = **33.47**.

### D. Double-count size comparison

| | value |
|---|---:|
| ln(1+1/b) TF | 4.2871 |
| ln(α(M_Z)/α(0)) | 0.0686 |
| ratio | **62.5** |

### E. μ_5 at sphaleron epoch

| | value |
|---|---:|
| θ̇ | 59.7 eV |
| μ_5 | **29.9 eV** |

### F. k_F (hierarchy_kF_and_bendover) — side note, not residual-closing

k_F cancels from λ to 1e-16 over eight decades; only k_F > 0 inside the linear cone is required. Bend-over condenses at λ=0.03 but does **not** source the anchor (ledger: miss e², wrong sign). No change to §6f residual size.

---

## 4. What would close vs kill the residual

### What would **close** the residual (honestly)

| path | content | status |
|---|---|---|
| **Ontology horn (b)** | Medium *is* the vacuum (light = Goldstone) → one polarisation function; vacuum pairs *are* medium excitations; m_D² already resums them; α(0) only value with right meaning in §6c | Framework claim; A_s data-selects IR value (§6i) but **rides C=1 to ±22%** — joint with “count exact”, not free |
| **Uncharged constituents** | If carriers had no SM charge, SM vacuum polarisation would not couple | **Contradicted by §6e** (compensated charged pockets) |
| **Show residual Π_vac is negligible at pairing shell after medium screening** | Quantitative bound ≪ factor 5, not a verbal “double count” | **Not done**; script sizes worst case 5–10, not a suppression proof |

Closing by “better vertex/Fock” does **not** work: those are O(λ) at fixed α and already in the 0.55–1.78 TeV band. §6f is orthogonal (α scale / ontology). Examined pass (2026-07-29): double-count is **conditional on horn (b)**, not a general many-body freebie.

### What would **kill** the residual (or kill the anchor under residual)

| path | effect |
|---|---|
| Horn (a) true (medium sits *inside* a QED vacuum) | Residual applies; anchor → **×11 at M_Z**, worse toward Planck; identification with few-TeV EW scale fails |
| C ≠ 1 at the ±22% level | §6i IR selection fails jointly; UV α reopens |
| Exact landing demand | Already impossible: needs 1/α=140.74, beyond IR cap; residual only deepens the miss |
| μ_5 size mismatch | Kills #146 doping candidate, **not** the §6f α residual (separate debt) |
| Broken-phase screening unavailable at shell | μ_5 source + lepton selection fail together; re-opens basement, not α-running arithmetic |

### Manuscript-safe statement

> Anchor band **0.55–1.78 TeV** is **conditional on horn (b)** (medium = vacuum / α_c scale-independent IR medium constant). Under horn (a) the residual vacuum polarisation multiplies the anchor by **~5–10** after double-count removal (total ~**×11** at M_Z vs 4πm_H). The residual is **sized, adverse, open** — a consistency test of the Goldstone identification, not a closed technical detail.

---

## 5. Non-claims

1. **Does not claim §6f is closed.** Verdict of the script and of this run: **NARROWED, NOT CLOSED.**  
2. **Does not claim the double-count removes all running.** It removes naive scale-replacement; residual SM vacuum polarisation remains if carriers are charged.  
3. **Does not claim the residual factor is smaller than 5.** Sized **×5.58–×8.89** (M_Z to ~3 TeV); order **5–10**, adverse.  
4. **Does not claim α(0) landing is exact.** Best available is still **×2.00** on 4πm_H; exact landing needs 1/α=140.74, unavailable at any scale.  
5. **Does not promote 1576 GeV as precision.** Supportable claim remains “EW scale within a factor of a few,” conditional.  
6. **Does not claim #146 μ_5 is verified.** Source *candidate* from owned pieces; size vs doping **owed**; epoch for θ̇ **owed**.  
7. **Does not claim μ_5 closes or shrinks the §6f α residual.** Different debt (basement doping / phase).  
8. **Does not use the unconverged α_c ∈ [0.0205, 0.0214] band as a constraint** (R−1 was 93 / 40 — worthless as edges).  
9. **Does not re-evaluate O(λ) integrals** this run; band 0.55–1.78 TeV is carried from prior evaluation.  
10. **Does not claim A_s free-closes the fork** without C=1; they stand or fall together (§6i).

---

## Run integrity

- All listed scripts executed under `nice -n 19` on 2026-08-03.  
- hierarchy_6f: **5/5** checks.  
- hierarchy_kF: **9/9** checks.  
- hierarchy_anchor_budget: asserts on amp, bare anchor ~1.57 TeV, dk, band ratio.  
- Outputs archived in this directory.  
- **No fake close:** residual remains open and sized adverse.


## Claude D4 cure (2026-08-03) — horn conditionality

**Condition:** The residual factor ×5.6–×9 (and ~×11 total with the recorded ×2) is the price under
**horn (a)** — treating medium polarization and SM vacuum polarization as two independent
runnings on charged carriers. Under **horn (b)** — the corpus’s A_s-selected stance that the
medium *is* the vacuum polarization already resummed in ε(q) — that multiplier is **not** a
standing unconditional correction; the carriers *are* the polarization channel already counted.
Quote ×5–×11 only as **horn (a)’s adverse price**, never bare.

μ_5 merge 2→1 and broken-phase screening survivor: unchanged AGREE.
