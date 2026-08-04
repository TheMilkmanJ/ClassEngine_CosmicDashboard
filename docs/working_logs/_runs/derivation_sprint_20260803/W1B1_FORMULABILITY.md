# W1 + B1 formulability — honest OPEN-BLOCKED stamp

**Date:** 2026-08-03  
**Sprint tracks:** **W1** = ω_J forward; **B1** = Bounce F-A3  
**Blue role:** desk status + recompute only; **NO FABRICATIONS**  
**Grade (both tracks):** **OPEN-BLOCKED** — not DERIVED, not KILLED by new compute this sprint  

**Rules held:**
- Do not invent axiom **A_ωJ** (χ, J_seat / pin curvature).
- Do not invent metric-off **H_re** / expanding-branch declaration as a NEC theorem.
- Do not restate ω_J → 1.9 keV.
- Do not book cyclic cosmology.
- Prefer kill over fake derivation when a legal path is empty.

**Primary sources (read, not reinvented):**
- [`../debt_baryo_omegaJ_20260803/REPORT.md`](../debt_baryo_omegaJ_20260803/REPORT.md)
- [`../debt_omegaJ_forward_formulability_20260803/REPORT.md`](../debt_omegaJ_forward_formulability_20260803/REPORT.md)
- [`../debt_bounce_20260803/REPORT.md`](../debt_bounce_20260803/REPORT.md)
- [`../debt_bounce_FA3_20260803/REPORT.md`](../debt_bounce_FA3_20260803/REPORT.md)
- [`DERIVATION_SPRINT_BOARD.md`](./DERIVATION_SPRINT_BOARD.md)

**Scripts re-run this stamp (2026-08-03):**
- `nice -n 19 python3 scripts/junction_quartet_closure.py` → **VERDICT: THE QUARTET CLOSES**
- `nice -n 19 python3 scripts/baryogenesis_junction_closure.py` → provenance + band; R/R_need = 1.000 at back-solve

---

## Executive one-liners

| Track | One line |
|---|---|
| **W1** | Quartet arithmetic is machine-backed and **closes**; forward ω_J needs **A_ωJ** (χ + pin curvature / J_seat) — **not formulable** from stocked objects. |
| **B1** | Homogeneous bounce engines are **DEAD** with nogo proof; medium ⟨Θ⟩ turn exists in toys; exterior **H_re** needs **F-A3 declaration** — continuous metric-ON cross is **obstructed**. |

**Neither track is desk-closable without invention. Stamp: OPEN-BLOCKED.**

---

## Table 1 — W1 / ω_J: machine-backed (quartet) vs requires A_ωJ

### 1a. Machine-backed (formulable / recomputed; not a forward land)

| Object | Value (recompute 2026-08-03) | Status | Script / source |
|---|---|---|---|
| Γ_φ = G_F² T_sph⁵ | **5.3902×10⁹ eV** | COMPUTED | `junction_quartet_closure.py` |
| θ̇ at T_sph | **59.68 eV** | COMPUTED (winding) | same; `winding_turn_budget.py` integrity only |
| Γ_φ/θ̇ | **9.0319×10⁷** | COMPUTED (not ~10⁷ OOM) | same |
| R_need (η·n band) | **~5×10⁻⁵** | FROM η band | baryogenesis §3a |
| R = ω_J²/(2 Γ_φ θ̇) at back-solve | **5.0499×10⁻⁵** | MATCH need | same |
| j = ω_J²/Γ_φ at back-solve | **6.028 meV** | FOLLOWS ω_J | same |
| ω_J from √(2 R_need Γ_φ θ̇) | **5.672 keV** (≈5.7) | **BACK-SOLVED** grading target | same |
| Rectifier formula + overdamped class | R formula verified **0.06%** | MACHINE-BACKED formula | `kapitza_junction_response.py` |
| ×9 “quartet miss” | **artifact** of ratio ~10⁷ | DISSOLVED | not physics residual |

**Quartet consistency ≠ forward derivation.** Three legs force one residual scale.

### 1b. Requires A_ωJ / χ / pin curvature (not formulable from corpus)

| Object | What would be needed | Corpus state | Class |
|---|---|---|---|
| **A_ωJ** (single missing axiom) | Independent micro price of ω_J **or** pair (χ, J_seat) with ω_J² ≡ J_seat/χ | **Unstated** | **OPEN-BLOCKED** |
| χ (junction-phase stiffness / decay constant) | Numeric independent of η | Cancels in EOM; never priced as this phase’s stiffness | MISSING INPUT |
| J_seat / pinning curvature of U_J | Cos-term curvature independent of ω_J | Stage 7 *names* J; stage 8 never numbers it without ω_J | MISSING INPUT |
| C1 forward form ω_J² = (curvature)/χ | Both inputs | Only real route; blocked | MISSING INPUT ×2 |
| Forbidden: decay constant = v_L | MeV/GeV/2.4 TeV corners | Explicitly **declined** (#39) | FORBIDDEN ID |
| Forbidden: f_e-scalar → χ | 100–500 TeV f | Different sector; no map | FORBIDDEN ID |
| Wrong object: Jeans √(4πGρ) | Fully formulable | Unrelated; ~8 orders under at T_sph | WRONG OBJECT |
| Circular: C0/C0b/C8/C11 | Feed R_need or stale ratio | Grades target only | NOT A LAND |

**FORMULABLE non-circular junction ω_J from existing corpus: 0.**

### 1c. Pre-registered grading band only (does not create formulability)

| Disposition | Derived ω_J | Meaning |
|---|---|---|
| ACCEPT | **[3.0, 12.0] keV** | magnitude reading lives (~×2 of 5.7) |
| ANOMALOUS-REVIEW | (0.057, 3.0) ∪ (12, 30] keV | retune before booking |
| KILL junction route | **&lt; 0.057 keV** | ×100 under ~5.7 |
| Forbidden target | **1.90 keV** under stale Γ/θ̇=10⁷ | artifact; do not grade against |

---

## Table 2 — B1 / Bounce: nogos paid vs F-A3 needs declaration

### 2a. Nogos paid (DEAD — do not reopen as FRW bounce engines)

| Engine | Kill | Script (re-run / archived) | Key number |
|---|---|---|---|
| Thermal T = T_c as cosmological bounce | ρ+p ≈ (4/3)ρ_rad > 0 ⇒ Ḣ &lt; 0 | `bounce_thermal_crossing_nogo.py` | ρ_rad/ρ_bounce ≈ **2.76×10⁹** |
| CSW / ρ_bounce as homogeneous FRW bounce | ρ+p &gt; 0 ceilings; bare cannot cancel floor | `bounce_floor_frw_nogo.py` (A) | ρ_bounce^(1/4) = **1.059 keV** |
| Live barotropic dCDF w = −ρ_inf/ρ | at floor: ρ+p = 0 coast, not bounce | same (B) | (ρ+p)/ρ_inf = 0 |
| Hubble-scale metric exit at ρ_bounce | exit above CSW ceiling | same (C) | H⁻¹/ξ ≈ **12.3** at floor |
| Magnetic polarity flip as turn | T(B)=T(−B); NEC ≥ 0 | `bounce_magnetic_flip_nogo.py` | max \|T(B)−T(−B)\| = **0** |
| Vac + rad homogeneous bounce | 1+w_vac ≡ 0; H=0 is **turnaround** | `bounce_handover_sign.py` | identity |
| Stocked exotic X / DE-scale ghost | wrong budget by many orders | `bounce_rp_required_X.py`, M5 | ~10¹⁹–10³² short |
| Quartic / higher-order Friedmann bounce | QP vanishes in FRW | `bounce_m8_ledger_quartic.py` | dead |
| N_med = 1/c_s as derived MeV compression | coincidence under c_s variation | M2b | fabricated knob |

**Standing derived (not confused with turn):** finite floor ρ_bounce = m⁴/λ ~ (1.06 keV)⁴ is a **density ceiling**, not a bounce. Turnaround ≠ bounce.

### 2b. What F-A3 still needs (declaration wall — OPEN-BLOCKED)

| Item | Status | Note |
|---|---|---|
| Medium ⟨Θ⟩: − → 0 → + with Θ̇ &gt; 0 | **YES in 0D/1D toys** | interaction + quantum gradient; averaging identity |
| Door geometry R_H/ξ → √3 | COMPUTED (M2) | H_door = 1/(√3 ξ) |
| Continuous H_kin = ⟨Θ⟩_phys / d | Kinematic ID only | tracks fluid, not exterior FRW |
| Exterior H: − → 0 → + at finite ρ (metric-ON) | **OBSTRUCTED (A)** | H² ∝ ρ forbids H=0 at finite ρ |
| Metric-off Phase II re-entry H_re = +√(8πG ρ_re/3) | **F-A3 declaration (B)** | Medium derives fluid turn; re-attachment is branch choice |
| Magnitude lock \|H_kin\| = H_F(ρ_re) | **FAILS (C)** | c_s/√3 ~ 0.085; late Θ ~ 0.06 → ratio ~5×10⁻³ |
| O2 overall | **PARTIAL** | medium yes; exterior H-cross **not** derived |
| RP-A silhouette | **RECONSTRUCTED CANDIDATE** | written ODEs ≠ derived bounce |
| Cyclic cosmology | **not booked** | no full cycle as OEM/DERIVED |

**Answer from FA3 attempt:** Can H_re be derived from stocked medium stress + written junction without declaration? **No.**

---

## Table 3 — Illegal “desk closes” (do not do)

| Illegal move | Why illegal | Track |
|---|---|---|
| Invent pin curvature / J_seat number | Unstated micro input; manufactures A_ωJ | W1 |
| Invent χ (decay constant of junction phase) | Cancels in EOM; no corpus numeric | W1 |
| Silent decay constant = v_L | Explicitly declined (#39) | W1 |
| Map electron-scalar f → χ | Different sector; new ID | W1 |
| Adopt √(m₁ Γ_φ) ≈ 3.5 keV as land | Chance proximity; no mechanism chain | W1 |
| Identify ω_J with T_on ≈ 9.4 keV | Proximity only (×1.7) | W1 |
| Identify ω_J with Jeans √(4πGρ) | Wrong object; fails kill by ≫10² | W1 |
| Restate target to **1.9 keV** | Stale ratio artifact; R short ×8.9 on real Γ_φ | W1 |
| Claim “quartet closes ⇒ ω_J derived” | Quartet is back-solve consistency | W1 |
| Invent negative-energy stiff X for FRW bounce | Homogeneous legal parts fail; prefer kill | B1 |
| Reopen killed engines as turn primitives | Thermal, magnetic flip, CSW floor, dCDF, ghost, … | B1 |
| Declare H_re &gt; 0 from ⟨Θ⟩ &gt; 0 and call it **derived** | That *is* F-A3 declaration, not NEC theorem | B1 |
| Smuggle continuous exterior H-cross at finite ρ | Conflicts Friedmann H²∝ρ | B1 |
| Fabricate N_med ≳ 6.2 or spherical F ≳ 10⁹ for MeV start | O6 FAIL on legal parts | B1 |
| Book cyclic cosmology from RP-A scaffold | Scaffold ≠ cycle derivation | B1 |
| Equate ρ_bounce floor with cosmological bounce | Ceiling number ≠ Ḣ &gt; 0 | B1 |
| Equate late turnaround H=0 with bounce | Wrong Ḣ sign for crunch restart | B1 |

---

## Table 4 — Legal next steps (no invention)

| Step | Owner class | Track | What it does **not** claim |
|---|---|---|---|
| Recompute quartet only (`junction_quartet_closure.py`) | Desk / blue | W1 | Not a forward land |
| Keep 5.672 keV as **grading target**, band pre-registered | Bookkeeping | W1 | Not derivation |
| Owner / seat-sector write **explicit A_ωJ** from existing seat micro (or prove sector cannot) | Theory owner | W1 | Blue does not invent χ/J |
| External lattice / seat micro computation if model supplies operators | External | W1 | Only if inputs already named in corpus |
| Pin L_gen / n band (#180) — moves 𝒯 target, not first-principles ω_J | Hygiene | W1 | Does not create ω_J |
| Rename Jeans ω_J → ω_Jeans (naming collision hygiene) | Docs | W1 | Non-blocking |
| Re-run nogo suite; archive PASS asserts | Desk | B1 | Confirms DEAD list only |
| Document F-A3 as **declaration** in live ledgers | Honesty stamp | B1 | No false DERIVED |
| Attempt continuous/Israel matching **only** with stocked stress; prefer **kill** if fails | Theory + compute | B1 | No exotic X |
| Fill F-A1 SM-crossing corners with labeled fabrication (if any) | Scaffold honesty | B1 | Does not close O2 turn sign |
| Owner decide: keep RP-A reconstructed, or kill O2 as permanently PARTIAL | Owner | B1 | Not auto-promotion |
| Leave crunch-sector X **unnamed** if metric stays on | Honesty | B1 | No minting illegal fluid |

---

## Recompute confirmation (quartet)

| Quantity | Report `debt_baryo_omegaJ` | This re-run | Match? |
|---|---|---|---|
| Γ_φ | 5.3902×10⁹ eV | 5.3902×10⁹ eV | **YES** |
| Γ_φ/θ̇ | 9.0319×10⁷ | 9.0319×10⁷ | **YES** |
| R at ω_J=5.7 keV | 5.0499×10⁻⁵ | 5.0499×10⁻⁵ | **YES** |
| ω_J required from R_need | 5671.8 eV = **5.672 keV** | same | **YES** |
| j | 6.028 meV | 6.028 meV | **YES** |
| 1.90 keV → R short | ×8.91 | ×8.91 | **YES** |
| Verdict | QUARTET CLOSES | QUARTET CLOSES | **YES** |

Commands:
```bash
nice -n 19 python3 scripts/junction_quartet_closure.py
nice -n 19 python3 scripts/baryogenesis_junction_closure.py
```

---

## Explicit NOT DERIVED list

Do **not** promote any of the following to DERIVED / OEM / closed without new legal inputs:

1. **Forward junction plasma frequency ω_J** from seat microphysics.
2. **Axiom A_ωJ** (χ and/or J_seat / pin curvature) — named missing, not written.
3. **χ** as a numeric junction-phase decay constant.
4. **Any identification** decay constant = v_L, f → χ, ω_J = T_on, ω_J = √(m₁ Γ_φ), ω_J = Jeans scale.
5. **1.9 keV** as physical target or land.
6. **Classical homogeneous FRW bounce** from legal stocked parts (DEAD, not open-to-fix).
7. **Exterior cosmological H_re** (H: −→0→+ with Ḣ&gt;0) from medium stress + junction without declaration.
8. **F-A3** as NEC theorem or continuous exterior H-cross (it is a **branch / metric-off re-attachment declaration**).
9. **Magnitude lock** |H_kin| = H_F(ρ_re) from legal F-A2 amplitude law.
10. **MeV hot start** over keV door on legal parts (O6 FAIL).
11. **BKL / mixmaster survival theorem** (O7 PARTIAL only).
12. **Cyclic cosmology** (expansion → crunch → bounce → hot start → re-expansion).
13. **RP-A** as derived bounce (RECONSTRUCTED CANDIDATE only).
14. **ρ_bounce floor** as cosmological bounce event.
15. **Turnaround H=0** (bare+thaw) as bounce restart.

---

## Sprint grade stamp (W1 + B1)

| Track | Success-criteria bin | Named blocker |
|---|---|---|
| **W1** ω_J forward | **OPEN-BLOCKED** | **A_ωJ**: seat χ + pinning curvature (or micro ω_J from J) |
| **B1** Bounce F-A3 | **OPEN-BLOCKED** | **F-A3 / O2**: metric-off expanding re-entry is declaration; metric-ON H=0 at finite ρ conflicts Friedmann; magnitude lock fails |

> **Blue does not invent A_ωJ or H_re.** Desk work ends at: quartet recompute confirmed; nogos and FA3 obstruction recorded; illegal closes listed; legal next steps are owner axiom / external micro / honest kill — not fabrication.

### Audience one-liner

> Quartet math for baryogenesis is closed and re-verified; the forward keV land is blocked on a missing seat axiom. Bounce homogeneous engines stay dead; the medium can reverse expansion in toys, but exterior re-entry Hubble remains a declaration, not a derivation.

---

## Artifact map

| Path | Role |
|---|---|
| This file | W1+B1 formulability stamp |
| `../debt_baryo_omegaJ_20260803/REPORT.md` | Quartet + candidate kill roster |
| `../debt_omegaJ_forward_formulability_20260803/REPORT.md` | H2: zero formulable expressions; names A_ωJ |
| `../debt_bounce_20260803/REPORT.md` | Nogo synthesis; RP-A candidate |
| `../debt_bounce_FA3_20260803/REPORT.md` | Obstruction A/B/C; H_re not derived |
| `scripts/junction_quartet_closure.py` | Canonical quartet close |
| `scripts/baryogenesis_junction_closure.py` | Provenance types + band |
| `scripts/bounce_fa3_hcross_attempt.py` | FA3 compute (exterior H-cross? No) |

*End W1B1_FORMULABILITY.md — derivation_sprint_20260803*
