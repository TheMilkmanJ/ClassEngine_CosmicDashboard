# Bounce E2E verdict (2026-07-31) — Track A6

## Grade: **STORY** (permanent for this end-to-end program)

The classical turn **H = 0 and Ḣ > 0** (or a written FRW-exit with the same outer workings) is **not derived**. The density floor ρ_bounce is derived; the turn is not.

**No scaffold script.** A minimal equations file that closes H=0 and Ḣ>0 from **legal parts only** does not exist in the corpus and is not inventable without fabricated matching (RP-A F-A1…F-A3) or an exotic fluid the theory does not stock (RP-B / M5). Prefer this permanent honest stamp over a fake closure.

---

## Hard reasons (why legal parts do not bounce)

| requirement | legal-parts status |
|---|---|
| **H = 0** ⇒ ρ_tot = 0 | Reachable as **turnaround** (radiation + negative vacuum cross under contraction) — wrong epoch / wrong sign of Ḣ |
| **Ḣ > 0** ⇒ ρ + p < 0 | **Fails identically** for w=−1 vacuum + radiation: ρ+p = (4/3)ρ_rad > 0 always (`bounce_handover_sign.py`) |
| Finite ρ_bounce = m⁴/λ | **Derived number** (~(1.1 keV)⁴); is a BH/core ceiling, **not** an FRW a(t) minimum |
| Compact-torus energy ledger | Gives H² = (8πG/3)ρ; **does not** force Ḣ > 0 |
| Homogeneous fluid X | Needs ρ_X ≈ −ρ_rad and w_X > 1/3 at crunch scale — **DE-scale parts short by 10¹⁹–10³²** (`bounce_rp_required_X.py`, M5) |
| Metric exit at ξ (RP-A) | Only surviving **silhouette**; re-entry H>0 still **declared**, MeV needs fabricated N_med ≳ 6.2 |

**Bottom line:** every native FRW engine either kills the turn or only reaches a coast/turnaround. RP-A replaces FRW with a non-metric interval but still fabricates matching and re-entry.

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

Metric dissolution at healing length ξ → medium processes finite density → metric re-emerges expanding/hot.

| item | grade |
|---|---|
| Outer O1 finite density | pass if medium bound holds |
| O2 dynamical H→+ | **fail** on legal parts (hand re-entry) |
| O6 MeV hot start | **fail** without fabricated N_med ≳ 6.2 |
| F-A4 shear door | computed (local-first possible; non-hierarchical R_H/ξ≈√3) |
| M6 medium rebound (1D GPE) | density turn **yes** (toy); MeV **no** |
| F-A1…F-A3 matching | reconstructed / knobs — **not derived** |
| Overall RP-A | **reconstructed candidate**, not OEM, not derived |

Sources: `docs/working_logs/bounce_reconstruction_rp.md`, `bounce_derivation_workplan.md`.

---

## What *is* derived (keep citing)

| object | status |
|---|---|
| ρ_bounce = m⁴/λ ~ (1.1 keV)⁴ | derived finite floor |
| Compact-torus zero-net energy ledger | supports flat FRW balance |
| Local white-hole no-go (time-oriented medium) | stands |
| Live dCDF w→−1 floor structure | derived structure; not a bounce |
| Shear/ξ door timing (M1–M2) | partial constraint, not a turn |

---

## Permanent program stamp

For end-to-end audience and derivation boards:

> **B7 / bounce turn = STORY.** Cite the floor, the kill list, and the RP-A reconstructed silhouette if needed. Do **not** claim cyclic cosmology is derived. Horizon inheritance that rests only on the bounce is **not** independent evidence of a derived turn.

Further bounce work is a **separate research program** (RP-A matching ODEs / medium microphysics), not a desk closure of Track A6. No `scripts/bounce_rpA_scaffold.py` is issued: there are no legal-part-only equations that close the turn.

## Audience one-liner

> The model has a derived sub-Planckian density floor and a reconstructed metric-exit silhouette; it does **not** have a derived cosmological bounce.
