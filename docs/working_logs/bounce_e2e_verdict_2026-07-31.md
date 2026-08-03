# Bounce E2E verdict (2026-07-31) — Track A6

## Grade: **RECONSTRUCTED CANDIDATE** (was STORY; promoted 2026-07-31 evening)

The classical turn **H = 0 and Ḣ > 0** from **homogeneous legal parts** is **not derived** and remains **DEAD**.  
Build **RP-A** (metric / hydro exit at ξ → medium rebound → re-entry matching) now has a **written equation scaffold** with O1–O8 self-check:  
[`scripts/bounce_rpA_scaffold.py`](../../scripts/bounce_rpA_scaffold.py).

Promotion note: [`bounce_promotion_2026-07-31.md`](bounce_promotion_2026-07-31.md).

| claim | status |
|---|---|
| Homogeneous FRW bounce from stocked parts | **DEAD** (do not reopen) |
| RP-A equations + matching F-A1…F-A5 | **written** (reconstructed) |
| O1, O3–O5, O8 | **PASS** on RP-A |
| O2 turn | **PARTIAL** — medium ⟨Θ⟩ turn (toy/M6); H_re declared by F-A3 |
| O6 MeV | **FAIL** on legal parts (keV door; N_med knob fabricated) |
| O7 BKL | **PARTIAL** |
| **DERIVED** bounce | **no** |

**Earlier permanent-STORY stamp** held because no scaffold file existed and legal FRW engines all kill. The scaffold does **not** invent a legal-parts FRW bounce; it writes the RP-A replica with fabrication labels. Prefer that honest reconstruction over STORY-with-no-equations *or* a fake DERIVED.

---

## Hard reasons (why legal homogeneous parts do not bounce)

| requirement | legal-parts status |
|---|---|
| **H = 0** ⇒ ρ_tot = 0 | Reachable as **turnaround** (radiation + negative vacuum cross under contraction) — wrong epoch / wrong sign of Ḣ |
| **Ḣ > 0** ⇒ ρ + p < 0 | **Fails identically** for w=−1 vacuum + radiation: ρ+p = (4/3)ρ_rad > 0 always (`bounce_handover_sign.py`) |
| Finite ρ_bounce = m⁴/λ | **Derived number** (~(1.1 keV)⁴); is a BH/core ceiling, **not** an FRW a(t) minimum |
| Compact-torus energy ledger | Gives H² = (8πG/3)ρ; **does not** force Ḣ > 0 |
| Homogeneous fluid X | Needs ρ_X ≈ −ρ_rad and w_X > 1/3 at crunch scale — **DE-scale parts short by 10¹⁹–10³²** (`bounce_rp_required_X.py`, M5) |
| Metric exit at ξ (RP-A) | Only surviving **silhouette**; scaffold now writes ODEs + matching; re-entry H>0 still **declared** (F-A3); MeV needs fabricated N_med ≳ 6.2 |

**Bottom line:** every native homogeneous FRW engine either kills the turn or only reaches a coast/turnaround. RP-A replaces FRW with a non-metric / hydro-exit interval; matching and MeV remain the named residuals.

---

## Dead engines — do not reopen

| engine | kill | script / ledger |
|---|---|---|
| Thermal **T = T_c** as cosmological bounce | radiation-dominated, Ḣ < 0; melt is real, turn is not | `bounce_thermal_crossing_nogo.py` |
| **CSW / ρ_bounce** as homogeneous FRW bounce | ρ+p > 0 for p~ρ and p=Kρ²; bare vacuum ~10²³ too small | `bounce_floor_frw_nogo.py` |
| Live **barotropic dCDF** (w=−ρ_inf/ρ) | ρ+p = ρ−ρ_inf ≥ 0; floor ⇒ Ḣ=0 coast, not bounce | same |
| **Hubble-scale metric exit at ρ_bounce** | H⁻¹/ξ ~ 12 at floor; H⁻¹=ξ needs ~150×ρ_bounce | same |
| Homogeneous **exotic X** from stocked parts | M5 exhaustive close-negative; frozen-ratio anchors kill equal-scaling negatives | `bounce_m5_exotic_fluid.py` |
| DE-scale **ghost** as X | wrong budget / wrong attractor | floor_ghost + RP-B |
| **N_med = 1/c_s** as derived MeV compression | coincidence under c_s / T_reheat variation | `bounce_m2b_mixmaster_nmed.py` |
| Inverse acoustic matching as closed F-A1 alone | underdetermined without extra structure (half-machined later; still not OEM) | reconstruction §14.2 |
| Homogeneous **quartic / higher-order Friedmann** bounce | QP vanishes in FRW; ledger returns standard H² | `bounce_m8_ledger_quartic.py` |
| BH / magnetar / fountain / neutrino freeze / high-f portal as **sole** turn engines | reservoir / timing / trigger only — no ρ_X(T) | failures ledger retirements |
| Magnetic polarity flip | nogo script | `bounce_magnetic_flip_nogo.py` |

**Do not reopen** these as FRW bounce engines. Support roles (reservoir, timing, structure) remain allowed language.

---

## RP-A status (only non-killed silhouette)

Metric dissolution / hydro exit at healing length ξ → medium processes finite density → metric re-emerges expanding.

| item | grade |
|---|---|
| Outer O1 finite density | **PASS** if medium bound holds |
| O2 dynamical H→+ | **PARTIAL** — medium turn yes (toy); F-A3 declares H_re>0 |
| O6 MeV hot start | **FAIL** without fabricated N_med ≳ 6.2 (or unresolved F / cascade) |
| F-A4 shear door | computed (local-first possible; non-hierarchical R_H/ξ≈√3) |
| M6 medium rebound (1D GPE) | density turn **yes** (toy); MeV **no** |
| F-A1…F-A3 matching | written in scaffold — **not derived** |
| Overall RP-A | **reconstructed candidate**, not OEM, not derived |

Sources: `bounce_reconstruction_rp.md`, `bounce_derivation_workplan.md`, `bounce_rpA_scaffold.py`, `bounce_promotion_2026-07-31.md`.

---

## What *is* derived (keep citing)

| object | status |
|---|---|
| ρ_bounce = m⁴/λ ~ (1.1 keV)⁴ | derived finite floor |
| Compact-torus zero-net energy ledger | supports flat FRW balance |
| Local white-hole no-go (time-oriented medium) | stands |
| Live dCDF w→−1 floor structure | derived structure; not a bounce |
| Shear/ξ door timing (M1–M2) | partial constraint, not a homogeneous turn |

---

## Program stamp (updated)

> **B7 / bounce turn = RECONSTRUCTED CANDIDATE (RP-A).** Cite the floor, the kill list, the scaffold equations, and the explicit O2/O6/O7 residuals. Do **not** claim cyclic cosmology is derived. Do **not** claim homogeneous FRW bounce from legal fluids. Horizon inheritance that rests only on the bounce is **not** independent evidence of a derived turn.

Further bounce work: close F-A3 dynamical content without hand declaration, O6 funding (genesis cascade / clean spherical F), O7 handoff theorem — separate research, not desk reopening of dead engines.

## Audience one-liner

> The model has a derived sub-Planckian density floor and a reconstructed metric-exit bounce candidate with written ODEs/matching; it does **not** have a derived classical turn or legal-parts MeV hot start.
