# Neutrino sector — dark energy sets the lightest mass

> ## Residual freeze — consistency stamp (2026-08-04)
>
> **COMPLETE-CONDITIONAL** on the relation + m_ββ window. **Not** a booked Σm_ν joint posterior (that is [PRTOE_neutrino_home.md](PRTOE_neutrino_home.md) / OPEN-MACHINE: waits on `dyad_mnu_bbnfix` book).
>
> **Fairbank HOLD** · **m_ββ package READY not posted:** `papers/neutrino-mbb/` + [arXivReady](arXivReady/README.md) are **READY_PACKAGE**; owner submitted to Fairbank 2026-08-03; **no arXiv post**. Owner prep: [arxiv_owner_prep_20260804](working_logs/_runs/arxiv_owner_prep_20260804/REPORT.md). Full honesty package: [neutrino_full_honesty_20260804](working_logs/_runs/neutrino_full_honesty_20260804/REPORT.md).
>
> **Forbidden:** invent joint posteriors; claim package “posted”; invent second Fairbank TeX; treat null 0νββ as confirmation.

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Home / joint-fit residual: [PRTOE_neutrino_home.md](PRTOE_neutrino_home.md). Letter: [PRTOE_fairbank_note_draft.md](PRTOE_fairbank_note_draft.md).

Consolidates the model’s most experiment-facing claim block. Components range from recorded (Majoron structure, P-2026-012/020) to exploratory (ρ_inf closure, on review hold). Relevant tests: ton-scale 0νββ (nEXO, LEGEND-1000, CUPID) and next-generation cosmology.

**Status.** Mass relation and 0νββ window established (COMPLETE-CONDITIONAL). Ship path: **neutrino-mbb READY not posted** under Fairbank HOLD. Open: exact μ value, flavor-distribution calculation, next falsifiable Majoron consequence, ρ_inf closure; joint Σm_ν booking lives on home / bbnfix.

## 0. Claims

1. **Majorana → 0νββ exists** (P-2026-020). Rate still carries the §3 phase caveat: m_ββ can sit as low as 0.04 meV. Kill is one-way: detection above the ceiling falsifies the model; a null at any sensitivity does not. Dirac cannot be demonstrated directly — only inferred from nulls plus closed Majorana channels.

2. **Lightest mass = dark-energy scale:** m₁ = ρ_Λ¼ = 2.25 meV (lepton-number-breaking scale in the Majoron sector; Majoron = Goldstone of spontaneously broken L — MATH_SPINE §6). Relation form: m₁ = κ_m · ρ_inf¼ with κ_m ≈ 1 (see addendum). Model does **not** derive 2.25 meV (dark-energy-value problem). Claim: one un-derived number does two jobs standard cosmology treats as unrelated.

3. **Sum:** measured splittings → Σm_ν = 61.4 meV, **normal ordering** (favoured by P-2026-004 collision test, not by P-2026-012 alone — ANN-2026-025). **Not a discriminator:** 2.6 meV above the m₁ = 0 floor (58.8 meV) vs ~20 meV planned resolution. Distinctive content is m_ββ (§3).

4. **Exploratory:** occupancy-corrected ρ_inf derivation reproduces the same sum via ρ_Λ, M₂ = α²·T_c, and 3α; the α_c instrument (zon_disp — unconverged, not currently running) checks that claim.

## 1. Why this block bites

Every claim is measurable this decade; none is free:

- Ton-scale 0νββ near the normal-ordering floor; confirmed Dirac (full-sensitivity nulls + other Majorana channels closed) kills claim 1.
- Cosmology’s Σm_ν (DESI+CMB) already brushes 60–80 meV. Two kills here; likelier from below: robust Σ > 70 meV kills 2–3, as does a ΛCDM-conditional upper limit through 61.4 meV (frontier direction). Model: limits are ΛCDM-conditional; squeeze relaxes under its recombination history (testable). Inverted ordering also kills 2–3.
- In-house: P-2026-023 de-biased band (0.07–0.09 eV) sits above this block’s 0.061; the production-chain posterior (once quotable) arbitrates the two neutrino numbers.

## 2. Open mechanism items

μ ties the DE floor to the lightest neutrino mass (dimension-1 L-breaking parameter, distinct from the dimensionless varying-m_e amplitude). Value μ = 2.25 meV un-derived. Still needed: new falsifiable Majoron consequence; ρ_inf closure depends on the α_c instrument (not currently running).

## 3. 0νββ

m₁ = 2.25 meV + normal ordering + NuFIT mixings (sin²θ₁₂ = 0.307, sin²θ₁₃ = 0.022): mass contributions |U²m| = (1.52, 2.67, 1.10) meV →

**m_ββ ∈ [0.04, 5.3] meV** over free Majorana phases, ~3.3 meV typical

— below ton-scale target ~5–20 meV. Phases not predicted; position in the window open.

Floor is real but not symmetry-protected. Exists because middle term exceeds the other two (2.67 vs 2.62 at m₁ = 2.25 meV); margin 0.05 meV on O(2) terms.

**The margin's sign is a coin toss on today's data, and where the coin lands is itself structured
(computed 2026-08-02, `scripts/funnel_edge_identity.py`, 9 controls).** At the global-fit central
values (NuFIT 5.0: sin²θ₁₂ = 0.304) the margin's sign flips to −0.0002 meV: the floor's existence
is decided by which side of the closure threshold m₁ sits on, and the 1σ band on the margin,
±0.24 meV, is dominated by θ₁₂ and makes the sign a 50/50 draw. The threshold itself — the smallest
m₁ at which exact cancellation first becomes possible, the lower edge of the well-known
normal-ordering "funnel" — computes to **m₁\* = 2.2496 meV at current centrals, against
ρ_Λ^{1/4} = 2.2395 ± 0.0108 meV: central values agreeing to 0.45%. Read that with its full error
budget: the threshold itself carries ±0.24 meV (±11%, θ₁₂-dominated) today, so the agreement is a
~0.04σ consistency — a statement about central values that current data cannot resolve, not a
precision coincidence** — though one found stated nowhere in the funnel literature (three
searches, null).
Exact cancellation at the threshold occurs at exactly one phase point, and it is CP-conserving:
(α₂₁, α₃₁) = (π, 0). JUNO (θ₁₂ and Δm²₂₁ below 0.5% by ~2031–32) tightens the threshold's error
to 0.06 meV, after which θ₁₃ — frozen at Daya Bay's final precision, with no successor planned —
gates the test at ~3% and the sign stays uncalled if the true margin is under ~0.04 meV. What
would decide it structurally is recorded with its price at the registry annotation to P-2026-012:
a closure mechanism exists in the literature (ee-texture zero, symmetry-protected, viable only in
normal ordering with m₁ pinned to the funnel) but is flavor structure, which this model's own
constitution declares not writable — and adopting it would invert the discriminating band above
into a falsifier, since it predicts m_ββ = |margin| ≲ 0.05 meV, no observable signal.

Derived DE scale 0.44% from observed: 2.2599 meV vs 2.25. **Not a formal error bar** — composite quartic above control edge; higher-order correction 5.4–9.8% uncontrolled. Treat 2.2599 as anchor comparison, not fully converged prediction.

Sum insensitive: Σm_ν = 61.34–61.37 meV → 61.4. Floor more sensitive (0.050 → 0.038 meV); ceiling stable ~5.30 meV. Window **[0.04, 5.3] meV**. Derived anchor 2.8% below the 2.324 meV threshold where floor vanishes.

Floor is soft; nothing observable rides on it. Conclusions use the ceiling. Near-cancellation → **m_ββ is a sharp probe of the DE scale**.

Structure: (i) 0νββ must exist if Majorana holds — Dirac evidence ends the sector (only ever indirect); (ii) normal-ordering floor shape fixed in advance; (iii) **one experiment can reach this model.**

| experiment | projected reach (ME range) | vs 5.30 meV ceiling |
|---|---|---|
| nEXO | 4.7–20.3 meV | **overlaps 4.7–5.3 meV** (favourable ¹³⁶Xe ME) |
| LEGEND-1000 | 9–21 meV | entirely above |
| CUPID | 12–34 meV | entirely above |

Flat phases: exceeds 4.7 meV **~10.8%** of the time (~1/9 chance of signal, conditional on model + ME). Detection outside the band kills; null constrains nothing.

Barium tagging (projected ×4 half-life): √4 = 2 in m_ββ → ~2.35 meV; detection probability 10.8% → **69%**. No discrimination: minimal ordering [1.48, 3.69] exceeds 2.35 meV **63.7%** of the time. **Discriminating band 3.69–5.30 meV** — minimal ordering impossible; this model **31.7%**. All of baseline nEXO’s 10.8% sits there. Tagging → likely; baseline → decisive.

0νββ never observed; Heidelberg–Moscow claim refuted by KamLAND-Zen/GERDA. Current limits m_ββ ≲ 28–180 meV (ME-dependent), 5–30× above this band. Cosmology may grade sooner; ton-scale grades cleaner. DESI-era Σm_ν ≲ 72 meV already; model at 61.4 just inside. Sector may be graded in 1–2 years by that number.

## 3b. Majoron mode 0νββχ (wrong instrument)

Second neutrinoless mode: Majoron + two electrons. Continuum (not a Q_ββ peak); searched separately.

Rate not free: mass-basis-diagonal singlet → g_ij = (m_i/v_L) δ_ij →

**⟨g_ee⟩ = m_ββ / v_L**

— same m_ββ as mass mode. Check: g₃₃ = 1.2×10⁻⁸ → v_L = m₃/g₃₃ = 4.18 MeV.

v_L has two viable points:

| point | v_L | ⟨g_ee⟩ at m_ββ = 3.05 meV | T½(¹³⁶Xe) |
|---|---|---|---|
| MeV-scale | 4.18 MeV | 7.3×10⁻¹⁰ | 3×10³² – 1×10³³ yr |
| high-v_L, GeV end | 1 GeV | 3.1×10⁻¹² | ~2×10³⁷ yr |
| high-v_L, 2.4 TeV ceiling | 2.4 TeV | 1.3×10⁻¹⁵ | ~10⁴⁴ yr |

*(Half-life spans = ME range; calibrated on KamLAND-Zen ordinary-Majoron limit T½ > 2.6×10²⁴ yr at ⟨g_ee⟩ < (0.8–1.6)×10⁻⁵, arXiv:1205.6372.)*

Even at the favourable point, Majoron mode is **~4 orders slower than the mass mode** (itself just past nEXO baseline); coupling 4 orders below limit → 8 orders in rate. **No observable Majoron mode at any surviving point** — kill-only bet.

Useful structure:

- Coupling is a **CMB** observable, not ββ. CMB-S4 reaches g ~ 10⁻⁸–10⁻⁹; model’s largest g₃₃ = 1.2×10⁻⁸ sits in band. CMB-S4 ~**four orders** more sensitive to this coupling than 0νββχ; registered discriminator (detection → MeV-scale + resonant leptogenesis; null → high-v_L).
- Peak search clean of continuum background under 0νββ — small positive for ton-scale.

Some singlet-Majoron treatments add seesaw suppression on top; that only makes the rate smaller.

## Sources

[SNO 2002], [Super-K 1998] (oscillations); [Planck 2018] (Σm_ν context). Internal: MATH_SPINE §6, [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md), P-2026-012/020/023. Full: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## 4. Addendum — one vertex, two roles

Baryogenesis transfer first run wants portal y ≈ 0.7–3×10⁻⁵; seesaw neutrino-mass vertex y ≈ 1.3–1.8×10⁻⁶ — same order, factor 4–20 in the crude rate. If the detailed calc closes the gap, one vertex could do mass + baryon asymmetry if the portal has no L channel.

Resonance μ ≈ Γ_N pushes required coupling ~100× larger — single vertex hard at TeV-scale M. Shared-vertex picture needs non-resonant leptogenesis → v_L ≥ GeV, Majoron coupling too small for CMB-S4. CMB-S4: detection at g ~ 10⁻⁸–10⁻⁹ favours shared vertex; null favours high-v_L.

---

## Mass-generation channel and lightest-mass relation (2026-07-18)

Splittings from the seesaw; lightest mass tied to the DE scale. At surviving points (MeV- or TeV-scale L-breaking, CMB-S4 selects): Yukawa ~6×10⁻⁷ gives m₃ = 50 meV. Lightest seesaw eigenvalue can still sit far below 1 meV.

Absolute floor:

**m_ν,lightest = κ_m · ρ_inf¼, κ_m ≈ 1**

Does not derive observed 2.25 meV. Means the same lightest-mass scale appears in DE and neutrino sectors. ρ_Λ¼ = m_ν,lightest is a mass-generation identity, not a thermal coincidence. Freeze-out connects the relation to thermal history; the relation is the source of the tie.

Open: how the mass term is shared among three eigenstates. Simplest medium-level operator is flavor-blind; state selection must come from dynamics.

Operator above the L-breaking scale:

**O_A = (c_A/v_L)·Φ_med·σ_L·ν̄₁ᶜν₁ + h.c.**

(Φ_med = medium scalar; σ_L carries the L-breaking VEV.) Dimension-5; cutoff = symmetry-breaking scale. Below v_L → lightest-state Majorana term. Majoron coupling:

**g = m₁/v_L**

→ g = 5.4×10⁻¹⁰ (MeV-scale, v_L = 4.18 MeV); 9.4×10⁻¹⁶ (TeV-scale, 2.4 TeV ceiling). Safe vs supernova limits; far below ββ limits.

Still open:

- pure number b in ρ_inf = b·m₁⁴
- settling calculation for mass sharing among eigenstates
- α_c instrument for occupancy-corrected ρ_inf closure (zon_disp — unconverged, not currently running)

---

## Claims ledger & discipline (2026-08-04 residual freeze) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Majorana → 0νββ required (P-2026-020) | **registered** | §0 claim 1 | Detection above ceiling kills; null does not |
| 2 | m₁ = ρ_Λ¼ = 2.25 meV (one number, two jobs) | **complete-conditional** / existence | §0 claim 2 | Does not derive 2.25; μ un-derived |
| 3 | Σm_ν = 61.4 meV normal ordering (relation) | **complete-conditional** | NuFIT + m₁; P-004 ordering | Not a discriminator vs floor (2.6 meV); **≠ booked joint posterior** (home / bbnfix) |
| 4 | m_ββ ∈ [0.04, 5.3] meV | **machine-backed** | §3; phases free | Floor soft/coin-toss on θ₁₂; ceiling stable |
| 5 | Funnel edge m₁* ≈ ρ_Λ¼ at centrals (~0.45%) | **machine-backed** arithmetic | `funnel_edge_identity.py` | ±0.24 meV θ₁₂ band → ~0.04σ; not precision coincidence |
| 6 | Only nEXO overlaps ceiling; ~10.8% phase space | **machine-backed** / literature reach | experiment table | Ba tagging weakens discrimination |
| 7 | Exact μ; flavor distribution; ρ_inf closure | **OPEN-BLOCKED** | §2 open | **OPEN-THEORY** + α_c instrument offline |
| 8 | `neutrino-mbb` arXiv package | **READY_PACKAGE** not posted | papers/ · arXivReady · arxiv_owner_prep | Fairbank HOLD; hep-ph endorsement; desk does not post |
| 9 | Fairbank correspondence / letter | **WATCH-EXTERNAL** / **HOLD** | fairbank_note_draft; HOLD companion | Owner-only; not a second TeX package |

**Non-claims:** not derived DE value; not flavor structure; not confirmation via null; not booked Σm_ν joint; not “posted to arXiv.”

**Triage:** elevate-in-place. Physics ceiling: registered experiment-facing; mechanism residual **OPEN-BLOCKED**; ship path READY under Fairbank HOLD (2026-08-04).
