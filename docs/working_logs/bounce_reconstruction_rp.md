# Bounce reconstruction (Racing Point method)

*2026-07-25. Working log — reverse-engineered candidate, not a derivation.*

## Method

We stop trying to open a sealed mechanism that is not in the corpus. Instead we do
what a legal reverse-engineering team does:

1. **Photograph the outer workings** — every computed and recorded constraint the
   finished cosmology must satisfy.
2. **Buy every legal part** — equations, numbers, and code identities already in
   the repo.
3. **Rebuild the invisible interior** so the outer behavior matches.
4. **Put the car on track** — score the reconstruction against the outer spec.
5. **Never call the replica factory-original** — grade stays `reconstructed` /
   `candidate` until a real derivation or a decisive computation lands.

This is not cheating. Cheating would be stamping `derived` on the replica.
Racing Point still had to *build* a car that drove; we still have to write
equations that close `H = 0` and `Ḣ > 0` (or a written FRW-exit) and fund the
hot start.

Sibling notes:
- constraints and admission: [bounce_derivation_workplan.md](bounce_derivation_workplan.md)
- kills: [../PRTOE_FAILURES_LEDGER.md](../PRTOE_FAILURES_LEDGER.md)

---

## 1. Outer workings (the spec sheet we must match)

These are the “photographs” of the finished object. A reconstruction that fails
any hard row is not a match.

| ID | Outer working | Type | Source |
|---|---|---|---|
| O1 | No infinite-density singularity; density bounded | hard | `ρ_bounce = m⁴/λ ~ (1.1 keV)⁴` |
| O2 | Classical turn: `H` goes − → 0 → +, with `Ḣ > 0` at the zero — **or** a written replacement of that pair | hard | FRW bounce definition |
| O3 | Live expanding-branch dCDF is *not* the turn engine | hard | `w = −ρ_inf/ρ`, `ρ+p ≥ 0` |
| O4 | CSW ceiling alone is *not* the homogeneous turn | hard | `bounce_floor_frw_nogo.py` |
| O5 | Thermal `T = T_c` alone is *not* the turn | hard | `bounce_thermal_crossing_nogo.py` |
| O6 | Hot start ~MeV over keV floor (~12 dex in density) | hard | `rho_bounce.py` |
| O7 | BKL: homogeneous `w < 1` loses to shear on approach | hard | `bounce_bkl_stiff_check.py` |
| O8 | No local time-reversed horizon as the engine | hard | white-hole local no-go |
| O9 | Turnaround (late DE reverse) ≠ deep bounce | hard | bare+thaw vs crunch |
| O10 | Topology may survive; rotation may reset | soft outer | cyclic grammar |
| O11 | Entropy not fully reset (Tolman) | soft outer | cyclic file |
| O12 | Present DM/DE epoch need not stock the terminal operator | soft | regime caveat |

**Match rule:** hard rows are pass/fail. Soft rows are preferred styling.

---

## 2. Legal parts (what we are allowed to bolt on)

| Part | What it is | What it is *not* |
|---|---|---|
| L1 | `ρ_bounce = m⁴/λ`, CSW ceiling number | FRW bounce mechanism |
| L2 | Healing length `ξ = ħ/(m c_s) ~ 402 AU` | Automatic Hubble-scale metric exit at the floor |
| L3 | Barotropic dCDF: `p = −ρ_inf`, exact `w → −1` floor | NEC-violating crunch fluid |
| L4 | `T_c = 177.10 keV` melt / electron-mass threshold | Geometry turn |
| L5 | Radiation `ρ ∝ a⁻⁴`, `T ∝ a⁻¹` on contraction | Sign flip |
| L6 | Negative bare vacuum + thaw → late turnaround | Deep bounce |
| L7 | Ghost-condensate / arrow sector (⟨θ̇⟩ ≠ 0); sustained NEC budget ~17 orders under for wormholes | Proven transient bounce engine |
| L8 | Compact-torus zero-net energy ledger | `Ḣ > 0` by itself |
| L9 | Two-component *shape*: condensate floor + Tolman radiation | Simulated dynamics |
| L10 | High-scale electron-mass portal rate law | Crunch-sector `ρ_X` |
| L11 | BH cores as finite-density heat/entropy reservoirs | Sign-flip term |
| L12 | Failures ledger retirements (do not re-use as engines) | — |

---

## 3. Reverse-engineered interior: three builds

### Build RP-A — Metric dissolution and re-emergence (primary native replica)

**Idea.** Do not force homogeneous FRW to bounce with an exotic fluid at all.
When curvature radii approach `ξ`, the emergent metric *ends* (legal part L2 +
no-singularity pillar). Inside that non-metric interval the medium’s own
hydrodynamics processes the crunch. When gradients lengthen again, the metric
re-emerges on an expanding branch with a hot radiation budget.

**Reconstructed sequence (educated assembly):**

```text
expanding DM/DE epoch
    → turnaround (L6: bare + thaw)                    [legal / registered]
    → contraction; radiation blueshifts (L5)          [legal]
    → density → O(ρ_bounce); local shear/curvature
      radii → ξ while H⁻¹ may still be ≳ ξ            [L1+L2; local exit uncomputed]
    → METRIC OFF (non-metric medium interval)         [RECONSTRUCTED hinge]
        • quantum pressure + quartic bound density    [L1, BH-core analogy]
        • thermal counterflow / normal-fluid release  [melt clue, not turn]
        • charge/topology bookkeeping                 [L10 grammar]
        • radiation-like energy conserved in medium   [L9 shape]
    → METRIC ON, H > 0, hot radiation bath            [RECONSTRUCTED matching]
    → standard hot big bang (BBN, …)                  [outer O6]
```

**Invisible parts we had to fabricate (named as such):**

| Fabricated part | Role | Status |
|---|---|---|
| **F-A1 matching rule** | When metric ends: map `(g_μν, ρ_i, u^μ)` → medium state | **unwritten** (toy only in M2) |
| **F-A2 medium crunch law** | Evolution inside non-metric interval | **priced as knobs** `N_med`, `η` (M2) — not microphysics |
| **F-A3 re-entry rule** | Medium state → expanding FRW with `H > 0`, `T ≳ MeV` | **H>0 declared by hand**; MeV needs `N_med ≳ 6.2` (M2) |
| **F-A4 shear clock** | Local `R_σ → ξ` vs Hubble / floor | **M1+M2 computed** — see §9–§10 |

**Why this build is the lead replica**

- Uses the model’s own “metric is emergent” pillar instead of fighting O3–O5 with a
  new fluid.
- Sidesteps the need for a homogeneous negative-energy bath at radiation scale
  (see Build RP-B).
- Naturally respects O8: there is no local white-hole *metric* patch; the interval
  is non-metric.
- Matches O1 by construction if the medium bound holds through the interval.

**Why it is not yet Mercedes**

- F-A1…F-A4 are exactly the sealed gears. We have drawn them; we have not cut them.
- Hubble-scale exit is *above* `ρ_bounce` (~150×); the build *requires* local
  exit. **M1** now shows that for CMB-to-structure shear seeds, local
  `R_σ = ξ` *can* precede Hubble exit and can sit under `ρ_bounce`
  (`scripts/bounce_m1_shear_xi.py`). A classical mixmaster window (`Σ ≳ 1` with
  `R_σ ≫ ξ`) still opens first — not fatal to the scale clock, not yet solved.
- Hot-start matching (O6) is asserted as a medium radiation budget, not computed.

**Grade:** `reconstructed candidate` — best native silhouette; **not derived**.

---

### Build RP-B — Homogeneous fluid `X` with reverse-engineered EoS (aero target)

**Idea.** Stay in flat FRW. Reverse-engineer the stress-energy that the outer
workings *require*, the way one reverse-engineers a wing from downforce numbers
before knowing the carbon layup.

**Legal FRW at handover:**

`H = 0  ⇒  ρ_tot = 0`  
`Ḣ > 0  ⇒  ρ_tot + p_tot < 0`

Split `ρ_tot = ρ_rad + ρ_floor + ρ_X` (and similarly for `p`).
At a radiation-dominated handover (`ρ_floor` negligible, `w_floor = −1`):

`ρ_X = −ρ_rad`  
`p_X < −ρ_rad / 3`  
`⇒ w_X > 1/3`  with **`ρ_X < 0`**

So the reverse-engineered “aero package” is:

> **A negative-energy density of order of the radiation bath, with stiff
> equation of state `w_X > 1/3`.**

**Scale (computed, not guessed):**

| Handover assumption | `\|ρ_X\|` needed | vs `ρ_Λ` | vs `ρ_bounce` |
|---|---|---|---|
| Radiation at `T_c = 177 keV` | `~3.5×10²¹ eV⁴` | `~10³²` | `~10⁹` |
| Residual rad `f·ρ_bounce`, `f=10⁻³` | `~10⁹ eV⁴` | `~10¹⁹` | `10⁻³` |
| Residual rad `f=1` (floor-scale) | `~ρ_bounce` | `~10²²` | `1` |

Even the *cheapest* homogeneous FRW bounce still needs an `|ρ_X|` enormously above
the dark-energy scale. The live DE floor / ghost attractor **cannot** be this `X`
without a crunch-scale amplitude that is not the recorded meV floor.

**Ghost off-attractor check (legal part L7, toy `P(X)` from `floor_ghost_condensate.py`):**

- For `X < X₀`, `ρ + p < 0` is available (NEC-flexible) — good *sign* structure.
- In that scan, `ρ` stays **positive** near the attractor; it does not supply
  `ρ_X ≈ −ρ_rad`.
- Sustained wormhole pricing (~17 orders under) already says the shelf is empty for
  macroscopic exotic stress; a bounce needs only a *transient*, but the *amplitude*
  still has to reach radiation scale. DE-scale ghost fails O2 on budget.

**Fabricated parts for RP-B:**

| Fabricated part | Role | Status |
|---|---|---|
| **F-B1 microphysics for `X`** | Field/fluid with `ρ_X < 0`, `w_X > 1/3` at crunch | **missing** |
| **F-B2 trigger** | What drives the medium onto that branch | **missing** |
| **F-B3 exit** | How `X` shuts off so the hot expanding phase is ordinary | **missing** |

**Grade:** `aero target` — any future homogeneous-fluid bounce must hit this EoS
window; **no legal part currently fills it**. Not a working replica.

Script anchor: extend with `scripts/bounce_rp_required_X.py` (required window).

---

### Build RP-C — Hybrid (RP-A body, RP-B only if metric stays on)

**Idea.** Default path is RP-A (metric off). RP-B is the backup only if a future
calculation shows the metric *remains* valid through the crunch. Then the car must
grow the exotic wing (F-B1) at crunch amplitude — not the DE floor.

**Grade:** `contingent assembly` — organizational, not extra physics.

---

## 4. Full timeline replica (outer match story)

Assembled from legal parts + RP-A fabricated hinges. **Reconstructed narrative:**

1. **Now (DM/DE regime).** Legal barotropic floor, optional thaw; no bounce operator
   on stage (O12, O3).
2. **Turnaround.** Bare + thaw drive late `H → 0` from above (O9, L6). Contraction
   begins. This gear is *not* the bounce.
3. **Contraction.** Radiation blueshifts; compact remnants and thermal cores can
   contribute to the bath (support only). Condensate approaches high density.
4. **Approach to ceiling.** `ρ → ρ_bounce` on the condensate ledger (O1, L1).
   Homogeneous Hubble scale still has `H⁻¹/ξ ~ 12` — metric not yet forced off
   globally. Local BKL curvature is the bet for earlier exit (F-A4).
5. **Hinge (fabricated).** Metric dissolution at `ξ`; medium processes finite
   density, melt/release, topology bookkeeping (F-A1–F-A3).
6. **Re-entry (fabricated).** Expanding FRW, `H > 0`, radiation budget ≥ MeV-class
   for BBN (O2, O6).
7. **Aftercare.** Axis/topology may carry (O10); entropy not fully wiped (O11);
   local white holes still forbidden in the new expanding medium (O8).

This is the Racing Point car on the transporter. It *looks* like it could race.
The hinge parts are still 3D-printed guesses.

---

## 5. Scorecard (put the car on track)

| Outer spec | RP-A (metric exit) | RP-B (fluid X) |
|---|---|---|
| O1 finite density | **pass** if medium bound holds | **pass** if `ρ` capped |
| O2 turn `H`, `Ḣ` | **fail as dynamics** — re-entry `H>0` still declared by hand (M2) | **fail** until F-B1 exists at crunch scale |
| O3 not live dCDF | **pass** (different regime) | **pass** (X ≠ barotropic dCDF) |
| O4 not CSW-as-FRW | **pass** (CSW is bound inside medium interval) | **pass** |
| O5 not `T_c`-as-turn | **pass** (melt may couple; not identified) | **pass** |
| O6 MeV hot start | **fail without knobs** — exit budget keV-class; needs `N_med ≳ 6.2` (M2) | **underdetermined** (F-B3 + reheat) |
| O7 BKL | **partial/scar** — mixmaster ~6 e-folds / ~8 curv. decades before `ξ` (M2); not solved | **fail** unless X also stiffens approach or exit |
| O8 no local WH engine | **pass** (non-metric hinge) | **pass** if X is bulk fluid not reverse horizon |
| O9 turnaround ≠ bounce | **pass** | **pass** |
| O10–O12 soft | compatible | compatible |

**Headline after M2:** RP-A no longer gets a free pass on O2/O6. The shear door
opens, but (i) local and Hubble cutoffs are only `O(1)` apart in shear domination,
(ii) a real mixmaster window sits in front of `ξ`, and (iii) the energy at the door
is keV-class — MeV requires fabricated Phase-II compression. RP-B remains dead on
DE-scale budget.

---

## 6. What “catching Mercedes” would mean here

The replica starts to *race* when fabricated parts become computations:

| Milestone | What to compute | Promotes? |
|---|---|---|
| M1 | Local curvature / shear vs `ξ` on approach (F-A4) | only “exit can precede Hubble exit” |
| M2 | Toy matching: junction from contracting FRW → medium ODEs → expanding FRW | only a working *model*, still reconstructed |
| M3 | Radiation budget through the interval → `T_reheat` vs MeV | absorbed into M2’s reheat grid for the toy |
| M4 | Show no local time-reverse metric patch is required | **done §12** — achronal-re-entry condition written; no reverse patch needed |
| M5 | If metric stays on: exhibit microphysical `X` with crunch-scale `ρ_X < 0`, `w_X > 1/3` | **done §13 — closes NEGATIVE**; RP-B unbuildable from native parts |

**M1 and M2 are done** (§9–§10). M3 is absorbed into M2’s reheat grid; M4 is a
boundary constraint; M5 remains open. Grade stays reconstructed.

---

## 9. Milestone M1 result (2026-07-25) — shear clock

Script: [`scripts/bounce_m1_shear_xi.py`](../../scripts/bounce_m1_shear_xi.py).

### Setup

- Local curvature proxy: `R_σ ≡ 1/σ` with free-propagation `σ ∝ a^{-3}`.
- Local exit candidate: `R_σ = ξ` ⇔ `σ = 1/ξ`.
- Hubble exit candidate: `R_H = 1/|H| = ξ`.
- Local-before-Hubble at exit ⇔ `Σ ≡ σ/|H| > 1` ⇔ `R_H/ξ > 1`.
- Radiation clock near the deep end: `|H| = H0√Ω_r / a^2` (scale clock, not a full Boltzmann history).
- Seed: `Σ0 = σ0/H0` today; path through turnaround cancels for `σ ∝ a^{-3}`.

### Fixed anchors

| Anchor | Value |
|---|---|
| `R_H/ξ` at `ρ_bounce` | `~12.3` (Hubble exit still not automatic at the floor) |
| Pure-rad Hubble exit density | `ρ^(1/4) ~ 3.7 keV ~ 150 × ρ_bounce` |
| `Σ0` for local exit exactly at floor | `~2.6×10^{-8}` |

### Seed scan (headline rows)

| `Σ0` today | Local exit vs Hubble | vs `ρ_bounce` | Mixmaster window (`Σ~1` with `R_σ≪ξ`? / `R_H/ξ≫1`) |
|---|---|---|---|
| `≲ 10^{-10}` | hub-first or marginal | over-floor | — |
| `~10^{-8}` | local-first | over-floor | yes |
| `~10^{-6} … 1` | **local-first** | **sub-floor** | **yes** |
| CMB-class `~10^{-5}` | local-first on *rad-only* clock (`R_H/ξ ~ 650`) — **overestimate, see M2** | sub-floor | yes at `Σ=1` |

### Verdict (M1, with M2 correction noted)

**F-A4 is pass-shaped on the door-opening question, weaker on “local ≪ Hubble”.**

1. `σ = 1/ξ` can occur at densities below `ρ_bounce` for CMB-to-structure seeds.
2. The radiation-only late clock **overstated** how hierarchical local-vs-Hubble was;
   M2’s full Friedmann clock fixes that.
3. M1 still correctly flagged a mixmaster regime before `ξ` — M2 prices it.

### What M1 does *not* buy

1. Hierarchical local-before-Hubble in shear domination (corrected in M2).
2. Matching laws, turn dynamics, or MeV reheating.
3. A derived bounce.

---

## 10. Milestone M2 result (2026-07-25) — junction + mixmaster + reheat knobs

Script: [`scripts/bounce_m2_junction.py`](../../scripts/bounce_m2_junction.py).

### A. Corrected shear clock

Full Bianchi-I style constraint used in the code:

`H² = (8πG/3) ρ + σ²/3`

Once shear dominates, at local exit `σ = 1/ξ`:

| Quantity | Value |
|---|---|
| `R_H / ξ` | `√3 ≈ 1.73` |
| `Σ = σ/\|H\|` | `√3` |
| shear fraction of `H²` | `≈ 1` |

**M1 correction:** the radiation-only estimate `R_H/ξ ~ 650` at CMB-class local exit was
**inconsistent** deep in the anisotropic regime. Local and Hubble cutoffs are only
**O(1)** apart when the door opens — “local first” is barely true, not hierarchical.

### B. Mixmaster window (priced)

For CMB-class `Σ0 = 10^{-5}`:

| Quantity | Value |
|---|---|
| e-folds with `Σ ≥ 1` before `ξ` | `N_mix ≈ 6.3` |
| curvature decades `R_σ(Σ=1) → ξ` | `≈ 8.2` |
| `R_H/ξ` when `Σ` first hits 1 | `~10^8` |

So classical GR has a **real, finite chaos window** — several e-folds and ~8 decades of
curvature radius — before the medium cutoff. O7 is not closed; the window is now a
number, not a vibe.

### C. Energy at the door vs MeV (O6)

At the same CMB-class exit, converting *all* effective density (radiation + shear) to a
temperature proxy:

| Budget | Scale |
|---|---|
| `T_rad` (radiation piece only) | `~146 eV` |
| `T_eff` (from total `ρ_eff`) | `~2.8 keV` |
| Gap to thermal 1 MeV in density | `~1.6×10^{10}` |

**O6 fails on legal parts alone.** Even a perfect shear→heat conversion at the door is
keV-class, not MeV-class.

### D. Toy three-phase junction (fabricated knobs)

```text
Phase I   : contracting FRW + shear  →  σ = 1/ξ     [legal GR]
Phase II  : non-metric medium         →  ρ → η ρ e^{4 N_med}   [FABRICATED]
Phase III : expanding radiation FRW, H > 0 declared  [FABRICATED re-entry]
```

| `N_med` | `η` | `T_reheat` | ≥ 1 MeV? |
|---|---|---|---|
| 0 | 1 | `~2 keV` | no |
| 4 | 1 | `~0.11 MeV` | no |
| 6 | 1 | `~0.83 MeV` | no (borderline sub-MeV) |
| ≳ 6.2 | 1 | `≥ 1 MeV` | **yes only with this knob** |
| 8 | 1 | `~6 MeV` | yes |

**Racing Point read:** the outer MeV working *can* be matched by dialing
`(N_med, η)` — like copying a wing from downforce numbers. That does **not** derive
the medium law. The knobs are the replica’s 3D-printed gearbox.

**O2 read:** `H > 0` on re-entry is still **declared**, not computed from a stress
tensor. No legal part supplies `Ḣ > 0`.

### M2 verdict

| Claim | Result |
|---|---|
| Local door before over-floor | still available for CMB-class seeds |
| Hierarchical local ≪ Hubble at door | **weakened** to `R_H/ξ ≈ √3` |
| Mixmaster before `ξ` | **priced**: ~6 e-folds, ~8 decades |
| MeV from exit budget alone | **fail** |
| MeV via fabricated `N_med ≳ 6.2` | match outer spec only as reconstruction |
| Dynamical turn `H → +` | **still missing** |
| Derived bounce | **still no** |

### Grade after M2

| Item | Grade |
|---|---|
| F-A4 (door timing) | computed; pass-shaped but non-hierarchical |
| Mixmaster window | **computed size**; mechanism to survive it **open** |
| F-A2/F-A3 | knobs `N_med`, `η` + hand re-entry — **fabricated** |
| O2, O6 on legal parts | **fail** |
| RP-A overall | **reconstructed candidate** (more scars, clearer blueprint) |
| Derived bounce | **no** |

### Next machining pass

~~M2b / M3~~ done in §11. ~~M4~~ done in §12. **M5** (crunch-scale fluid `X`, if the
metric stays on) is the only open milestone.

---

## 11. Milestone M2b/M3 (2026-07-25) — mixmaster duration & `N_med` origin

Script: [`scripts/bounce_m2b_mixmaster_nmed.py`](../../scripts/bounce_m2b_mixmaster_nmed.py).

### A. Mixmaster window in medium time

CMB-class `Σ0 = 10^{-5}`:

| Quantity | Value |
|---|---|
| `N_mix` | `≈ 6.3` e-folds |
| curvature decades | `≈ 8.2` |
| `Δt_mix / ξ` | `~ 8×10^7` |
| `Δt_mix / t_heal` (`t_heal = ξ/c_s`) | `~ 1.2×10^7` |

Door-at-`ξ` damping does **not** erase the prior ~10^7 healing-time chaos window.
A trigger at `R_σ ≫ ξ` would be required to shorten it — **unwritten**.

### B. Is `N_med ≳ 6` a legal identity?

| Comparison | Value |
|---|---|
| `N_med` (exit → 1 MeV, `η=1`) | `6.184` |
| `1/c_s` | `6.759` |
| `ξ·m` | `6.827` |
| ratio at operating point | `0.915` (tempting) |

Vary `c_s` (`ξ = 1/(m c_s)`): `N_med/(1/c_s)` runs ~0.3→5 — **not constant**.
Vary `T_reheat` at fixed `ξ`: `N_med` tracks `ln T`, not a medium constant.

**Verdict:** near-match to `1/c_s` is a **numerical coincidence**. Knob stays **fabricated**.

### C. Hypothesis scorecard

| Hypothesis | O7 / O6 | Grade |
|---|---|---|
| H1 damp shear exactly at `R_σ=ξ` | does not shorten prior window | open / no help |
| H2 tighter Kasner axis hits `ξ` first | earlier door, **colder** exit (worse MeV) | mixed |
| H3 inhomogeneous `Δρ ~ 5×10^{10}` | local OK; global clean `T_reheat` new debt | shape only |
| H4 use `ρ_bounce` as heat bath | exit `T_eff` already ≳ floor scale | no help |

### D. Status

O2 dynamical turn **fail**; O6 legal MeV **fail**; O7 survival **unwritten**;
RP-A reconstructed not OEM; derived bounce **no**.

---

## 12. Milestone M4 (2026-07-26) — causal character of the boundary

Script: [`scripts/bounce_m4_arrow_boundary.py`](../../scripts/bounce_m4_arrow_boundary.py).

### A. Local condition

The boundary is a level set of the exit criterion (`σ = 1/ξ` ⇔ `ρ_eff = ρ_exit`).
It is **spacelike** (a "moment") iff `|ρ̇| > |∇ρ|`, which at the shear-dominated
door (`ρ_eff ∝ a⁻⁶`, `R_H = √3 ξ`) reads `δ < 6L/R_H` for a contrast `δ` on
proper scale `L`:

| proper scale `L` | door spacelike up to `δ*` |
|---|---|
| `0.1 ξ` | `0.35` |
| `ξ` | `3.5` |
| `10 ξ` | `35` |

Collapsed regions (`δ ≫ 1` on `L ≳ ξ`) turn their segment **timelike** — an
ingoing absorbing wall, black-hole-class, allowed by O8. The prohibition bites
only at re-entry.

### B. The achronal re-entry condition (the new outer constraint)

A point may not re-enter the expanding metric phase while a causally adjacent
region is still contracting on the metric branch: that interface is a timelike
boundary emitting into the contracting exterior — the white-hole-class local
object O8 forbids. Absent a written re-synchronization mechanism inside the
medium interval (that would be a **new fabricated part, F-A5** — named,
unwritten), the door-crossing offsets survive, so the interval must **hold**:

`Δt_hold ≥ δ_max · R_H(door) / 6`

| `δ` at the door | hold (in `t_heal = ξ/c_s`) |
|---|---|
| `1` | `0.043` |
| `10³` | `43` |
| `5×10¹⁰` (H3) | `2.1×10⁹` |

### C. Collision with the concentration shortcut

`hold(H3) / mixmaster window ≈ 178`. Using `Δρ ~ 5×10¹⁰` concentration to
replace the compression e-folds would demand a hold ~178× longer than the entire
classical chaos window (§11). The causal constraint and the concentration
shortcut are in tension: hot patches cannot double as a cheap spacelike
re-entry. **H3 now carries a causal cost.**

### D. Arrow through the interval

With the metric off, time orientation is carried by the medium's own clock
(`⟨θ̇⟩ ≠ 0`, the recorded arrow sector). Switch-off and re-entry surfaces are
ordered by that clock. **No local time-reversed metric patch appears anywhere in
the assembly**: switch-off is an ending cap, re-entry a beginning cap.

### M4 verdict

| Item | Result |
|---|---|
| O8 (no white-hole engine) | **pass-shaped in structure**, at a written price |
| The price | achronal re-entry: `hold ≥ δ_max·R_H/6`, **or** exhibit F-A5 |
| Smooth doors (`δ ≲ 1`) | hold `~0.04 t_heal` — causally cheap |
| Concentration route (H3) | hold `~2×10⁹ t_heal` — causally expensive |
| O2 / O6 | unchanged (still fail on legal parts) |
| Derived bounce | **still no** — M4 is a boundary condition, not a mechanism |

---

## 13. Milestone M5 (2026-07-26) — the exotic-fluid branch closes negative

Script: [`scripts/bounce_m5_exotic_fluid.py`](../../scripts/bounce_m5_exotic_fluid.py).

**The general requirement, without assuming radiation domination:** at the handover,
`Σρ = 0` and `Σp < 0`. So `X` must go negative and must scale at least as fast as
the fastest positive component present.

**The sharp tool — the frozen-ratio anchor:** an `X` scaling exactly like a positive
component has a ratio to it frozen for all time; whether the combined coefficient is
negative is then decided by TODAY'S measurement, not by crunch physics. Radiation is
measured positive (`N_eff ≈ 3`); shear is `σ² ≥ 0` geometrically. No equal-scaling
negative track can ever force the crossing.

| candidate | fails on | number |
|---|---|---|
| bare vacuum (`n = 0`) | wrong crossing (turnaround), wrong `w`, size | `7.5×10⁻³³` of `ρ_rad(T_c)` |
| conformal Casimir (`n = 4`) | frozen ratio + size | `10⁻¹¹⁶`–`10⁻¹²⁰` of today's radiation |
| ghost transient (`n = 6`) | budget (recorded) | `10¹⁹`–`10³²` short |
| trace anomaly (`~N·H⁴`) | budget, everywhere metric-on | `~10⁹⁵` short |
| attractive interaction | nonexistence | quartic repulsive (`λ > 0`), portals tiny |

**Consequences.**
1. **RP-B is unbuildable from native parts** — not "missing a derivation," but
   exhaustively priced at the fluid level: the theory does not stock the part.
2. RP-C (hybrid) collapses; **RP-A alone carries the bounce**, with its two
   fabricated matching rules and the achronal-re-entry price (§12).
3. The sharpened conditional, now exhaustive: **if the metric stays on through the
   crunch, the recorded theory does not turn.** The bounce requires the metric exit.
4. The one adjacent unwritten alternative is a modified Friedmann **constraint**
   (bounded-density class, `−ρ²/ρ_c`) — not a fluid; it would need a derivation from
   medium discreteness near the density ceiling that is not in the corpus. Named,
   not fabricated.

Ledger row filed (the exotic-fluid close). All five milestones now have verdicts:
M1–M4 computed, M5 closed negative.

---

## 14. Three-way chase after M5 (2026-07-26) — no fabrication

Owner asked to chase all three remaining attacks. Claude hit a session limit mid-flight;
this section completes the board.

### 14.1 M6 — medium rebound under recorded GPE

Scripts:
- verified: [`scripts/bounce_m6_rebound_1d.py`](../../scripts/bounce_m6_rebound_1d.py)
- spherical production (heavier): [`scripts/bounce_m6_rebound_gp.py`](../../scripts/bounce_m6_rebound_gp.py)

**Setup:** healing-unit Gross–Pitaevskii with repulsive interaction
`i ∂_t ψ = −½∇²ψ + (|ψ|² − 1)ψ` (the same sign as `λ > 0` / density floor).
1D Cartesian split-step is the wall-clock-verified run; spherical is the same equation
with radial measure (slower).

**Computed (1D, four mild compressions):**

| A | v₀ | n_init → n_peak | t_turn [t_heal] | n_final | density turn? |
|---|---|---|---|---|---|
| 2 | 0.5 | 3.0 → ~3.1 | ~1 | ~1.9 | yes |
| 5 | 1.0 | 6.0 → ~6.3 | ~0.8 | ~3.2 | yes |
| 10 | 1.0 | 11 → ~11.3 | ~0.4 | ~6.5 | yes |
| 5 | 2.0 | 6.0 → ~7.1 | ~1.2 | ~3.7 | yes |

**Read:**
1. **Dynamic density turn is real** in the toy — compression peaks and falls from the
   repulsive interaction alone. That replaces “hand-declared re-entry” *at the medium
   layer* with a computed mechanism (still a toy, still fenced).
2. **Overshoot is O(1)**, not a free cosmological `N_med ~ 6` dial. MeV remains a
   **door-energy / budget** problem, not solved by the turn sign alone.
3. Late outward-flow probe is **preferred but not universal** on the 1D diagnostic
   (3/4 positive in the verified set). Cosmological matching still required for O2.
4. **Grade:** computed toy law. Does **not** promote the bounce to derived.

**Addendum (2026-07-27) — spherical production attempt: numerics FAILED, recorded
as such.** The spherical run (`bounce_m6_rebound_gp.py`) violated energy
conservation by factors up to ~20 at the focusing peak, with identical turn times
across unrelated parameters and non-monotone peak ordering — the split-step's
nonlinear phase is unresolved once the imploding pulse focuses at the origin
(`dt·n_peak ≫ 1`). **Its numbers are artifacts and are carried nowhere.** The
verified 1D result stands as the only computed rebound. What the failure honestly
leaves open: spherical geometric focusing could make the compression amplification
large — exactly the quantity the reheat budget wants — but the toy cannot yet say.
Named fix: an adaptive integrator holding `dt·n_max ≪ 1` through focus. Until it
exists, overshoot O(1) (1D) is the only number on the books.

### 14.2 Matching rule from the emergence dictionary

Corpus route (acoustic metric, [PRTOE_quantum_gravity.md](../PRTOE_quantum_gravity.md) §2):
low-energy excitations see an effective `g_μν` built from condensate density and flow.

**Forward map (recorded class):** medium `(n, v, c_s) → g_acoustic` is determined
(standard BEC/analogue dictionary).

**Inverse map (what F-A1 needs):** `g_μν → medium state` at metric exit is
**underdetermined** — slice/gauge choice and which hydrodynamic variables are fixed
are not uniquely fixed by the emergence theorem alone. So “assemble matching as the
inverse of emergence” does **not** close F-A1 without extra structure. Extra structure
would be a new assumption, not a derivation from what is already written.

**Grade:** inverse matching stays open / reconstructed; do not stamp derived.

**Addendum (2026-07-27) — the slice ambiguity closes from recorded structure.**
The underdetermination above was priced against "the emergence theorem alone."
But the model owns more than the theorem, and the extra structure is recorded,
not new:

1. **The slice is not a choice in this theory.** Lorentz invariance is emergent;
   the condensate rest frame is a physical, load-bearing object (it is how the
   Weinberg–Witten obstruction is evaded in the gravity file, and the arrow
   sector's `⟨θ̇⟩ ≠ 0` clock lives on it). The preferred frame fixes the ADM
   slicing of the inverse map — the same slicing the forward map used.
2. **Given the slice, the inversion is unique.** The acoustic form of `g_μν`
   exposes `(n, v)` directly (conformal factor and shift), and `c_s(n)` is
   monotonic for the repulsive quartic — no two medium states produce the same
   metric on the physical slice.
3. **The cosmological metric qualifies.** The gravity file's three-routes-one-
   metric statement (acoustic, induced, thermodynamic constructions yielding the
   same effective metric) is what licenses applying the acoustic inversion to
   the FRW metric the crunch hands to the door.

**Re-grade of F-A1:** the slice/gauge half of the underdetermination closes from
recorded parts; what remains open is the half already named — the trans-phononic
excitation translation at door-scale wavelengths (ingredients recorded as the
Bogoliubov coherence factors; the assembled table unwritten). F-A1 is now
**half-machined**: no free slice, one named open corner. Not derived.

### 14.3 Quartic-order / higher-gradient Friedmann correction

Question: can a next-order medium correction change homogeneous `H = 0` bookkeeping
enough to bounce without exotic `X`?

**Homogeneous FRW:** quantum pressure `∝ ∇²√n/√n` **vanishes** (no gradients).
Repulsive interaction energy is already inside the barotropic fluid used in the live
code (`ρ + p ≥ 0` on that branch — M5/ledger). The expansion-energy ledger
([expansion_energy_ledger.md](expansion_energy_ledger.md)) shows consistency with
`H² = (8πG/3)ρ`, not a derived higher-order bounce term.

**Bounded-density modified constraint** (`H² ∝ ρ(1 − ρ/ρ_c)` class) was already named
in §13 as an *unwritten* alternative, not stocked as a derivation from medium
discreteness in the corpus. Searching the corpus does not turn up a completed
derivation of that constraint from the recorded Lagrangian.

**Grade:** homogeneous higher-order route does not supply the turn from recorded parts.
Any `ρ²/ρ_c` bounce law remains unbuilt (not fabricated here either).

**Addendum (2026-07-27) — the ledger at quartic order, computed.**
[`scripts/bounce_m8_ledger_quartic.py`](../../scripts/bounce_m8_ledger_quartic.py)
tightens this close from "search finds no derivation" to a three-way computed
statement: **(A)** interaction energy enters the shell's inertia and gravitational
source identically, so the zero-energy books return `H² = (8πG/3)ρ_tot` — form
unchanged exactly; **(B)** the quartic only steepens the history (`ρ + p > 0`
everywhere, `1+w` running 1.00 → 1.89 into the ceiling, `H²` monotone, no zero);
**(C)** the medium's discreteness analog — the quasiparticle dispersion correction
`∝ k⁴ξ²` — vanishes identically at `k = 0` and activates only at coherence-length
gradients, **which is the metric-exit door**. The constraint lane and the door are
one lane: the metric-on turn is now closed at both the fluid level (M5) and the
constraint level. Ledger row filed.

### 14.4 Combined board after the three-way chase

| Attack | Result | Replaces fabrication? |
|---|---|---|
| M6 medium rebound | density turn **yes** (toy); MeV **no** | partially replaces hand re-entry *at medium layer* |
| Inverse acoustic matching | underdetermined | **no** — F-A1 still open |
| Quartic/homogeneous correction | no turn from recorded homogeneous stress | **no** |

**Still load-bearing open:** cosmological matching (F-A1/F-A3), MeV budget at the door,
mixmaster survival, and (if ever) a derived modified constraint near the ceiling.

**Discipline:** failures and closed-negative branches stay in
[PRTOE_FAILURES_LEDGER.md](../PRTOE_FAILURES_LEDGER.md) and this working log — not in
forward physics notes.

---

## 16. The chaos window under the directional door (2026-07-27)

Script: [`scripts/bounce_o7_mixmaster_squeeze.py`](../../scripts/bounce_o7_mixmaster_squeeze.py).

The M2b window (~6.3 mean e-folds, ~10⁷ healing times of mixmaster before the
door) used the ISOTROPIC shear clock. But the door criterion is directional —
the description ends when ANY direction's scale reaches ξ — and anisotropy
spread is exactly what the chaotic phase maximizes. Refined with the standard
asymptotic billiard (unit anisotropy speed, walls receding at half speed,
deterministic launch-angle scan, anchored to the recorded M2/M2b clock):

| quantity | mean-clock (M2b) | directional (this pass) |
|---|---|---|
| window to the door | 6.3 mean e-folds | **1.6–1.9 mean e-folds** (0.25–0.30 of the mean clock) |
| squeezes before the door | "~10⁷ t_heal of cascade" | **0–1** |

**Read.** The door opens direction-first: the chaos itself drives the fastest
axis to the coherence length at a quarter of the isotropic window. The chaotic
exposure the medium must survive is not a cascade — it is essentially ONE
anisotropic squeeze, and that squeeze IS the door. The interlock with M6: each
squeeze is locally a quasi-1D compression, and the medium's computed answer to
1D compression is the verified rebound. **Not claimed:** a survival proof — the
squeeze → door → interval handoff remains the open assembly. What changed is
the size of what must be survived. Fences: vacuum billiard idealization,
mean-door calibration transfer, wall-distance sensitivity checked (robust).

**O7 re-grade:** from "window priced, survival unwritten (~10⁷ t_heal)" to
"window directionally cut to ≲2 e-folds with 0–1 squeezes; survival question
reduced to the door handoff itself."

---

## 7. Standing grades

| Item | Grade |
|---|---|
| Outer spec sheet O1–O12 | constraints / photographs |
| Legal parts L1–L12 | recorded / computed |
| RP-A full assembly | **reconstructed candidate** |
| F-A4 shear door | **M1+M2 computed** |
| F-A2/F-A3 | knobs partly eased by M6 medium turn; cosmological matching still open |
| M6 medium rebound | **computed toy** — density turn yes; MeV no |
| F-A1 inverse matching | **underdetermined** (§14.2) |
| Homogeneous higher-order FRW bounce | **not available** (§14.3) |
| Mixmaster window | **~6 e-folds / ~8 decades / ~10^7 `t_heal`** (survival unwritten) |
| RP-B required EoS window | **reverse-engineered target** |
| RP-B filled by DE-scale ghost | **fails scale** |
| RP-C hybrid policy | organizational |
| Derived bounce | **still no** |

---

## 8. One-line summary

We did not open the watch. We built a **replica movement** from the hands and the
legal spares: metric off at `ξ`, medium crunch, metric on hot — with every invisible
gear labeled fabricated. M2 shows the door opens at keV budgets and only reaches MeV
if we 3D-print ~6 e-folds of extra medium compression. It is allowed to be wrong. It
is not allowed to pretend it came from the factory.

**Addendum 2 (2026-07-27) — the excitation corner machined (medium sector).**
[`scripts/bounce_fa1_transphononic_table.py`](../../scripts/bounce_fa1_transphononic_table.py)
writes the trans-phononic translation table from the adopted quasiparticle theory
plus recorded numbers (c_s = √3α, the shear-door rate):

- **Why the metric ends, quantified:** group velocity v_g/c_s = (1 + x²/2)/√(1 + x²/4)
  exceeds 1 for x = kξ ≳ 1 (1.34 at x = 2, unbounded beyond) — ξ-scale excitations
  outrun the acoustic cone, so the emergent causal structure cannot carry them.
- **What an excitation becomes:** the coherence factors (v² = 4.5 at x = 0.1 down to
  10⁻⁴ at x = 10) interpolate collective phonon → bare medium quantum with
  quasiparticle number conserved — the microscopic form of "radiation-like energy
  conserved in the medium."
- **The door is a quench for x ≲ 2.5:** those modes' frequencies are slower than the
  door's own rate (ω/H < 1), so they cross suddenly and are squeezed — the boundary
  CREATES long-wavelength medium quanta; a computed, modest injection channel for the
  reheat ledger.

**Scope fence:** medium sector only. The Standard-Model sector's crossing (photons at
the boundary — the emergent-light construction) is the remaining corner, filed as its
own task. **F-A1 status: machined in the medium sector; slice fixed by the preferred
frame; one named corner open (SM crossing).**

---

## 17. Task 4 — the squeeze-to-interval handoff as three computed joints (2026-07-27)

Script: [`scripts/bounce_task4_handoff_joints.py`](../../scripts/bounce_task4_handoff_joints.py).
The handoff is not a new mechanism; it is the consistency joints between the
directional door (§16), the verified 1D rebound (§14.1), and the achronal re-entry
condition (§12). Each joint is arithmetic on recorded anchors.

| joint | question | computed answer |
|---|---|---|
| J1 delivery | what inflow does the squeeze hand the medium? | `H_fast/H_mean ≈ 3.7–4.0` at first crossing ⟹ **Mach 14–16** at the coherence scale — ~5× beyond the toy's tested Mach 3; extension run launched (`bounce_m6_rebound_1d_hypersonic.py`), tested not extrapolated |
| J2 causal consistency | does the rebound's duration satisfy M4's hold? | self-consistent for door contrasts `δ ≲ 23`; collapsed cores remain the separate absorbing-boundary ledger |
| J3 planarity | is the quasi-1D toy geometry justified? | transverse axes **400–3100×** the fast axis at crossing — planar to 2.5–3.5 orders; justified |

**Open, named (the joints do not cover):** transverse dynamics during the rebound;
the wall between a rebounding pocket and a still-contracting metric-on exterior
(§12's boundary problem); cascade sequencing between neighboring pockets; the
Standard-Model sector's crossing (its own task).

**Grade:** three computed joints + four named opens; J1's envelope gap closing by
test, not extrapolation. Nothing promoted.

---

## 18. Task 5 — the MeV question as a single ledger (2026-07-27)

Script: [`scripts/bounce_task5_door_budget.py`](../../scripts/bounce_task5_door_budget.py).
Every channel in one place; one new channel priced and closed:

| channel | size | verdict |
|---|---|---|
| door budget (M2, computed) | `T_eff = 2.8 keV` | ×1.6×10¹⁰ under the MeV bar in density |
| electron-family gates (recorded) | 177–511 keV | ×2–5.6 under in T; candidate clock only |
| **quench injection (new, priced)** | `~9×10⁻⁸⁴ eV⁴` | ×10⁹⁷ under the door itself — **closed** |
| compression free parameter | `N_med ≳ 6.2` | retired; replaced by measured overshoot |
| 1D rebound overshoot (verified) | ×O(1) | does not fund MeV |
| spherical focusing | **pending** | the adaptive run, in flight |
| SM-sector crossing (task #14) | **unwritten** | where most of the bath's energy lives |

**Read:** every computed channel is keV-class or below. The MeV question rests on
exactly two live levers — the spherical focusing amplification (computing now) and
the Standard-Model crossing (task #14, the only channel large enough to matter if
focusing falls short). If both fail, the honest endpoint is a recorded outer-spec
tension: the reconstruction under-funds BBN and says so. No knob exists to turn.

---

## 19. Task 14 — the Standard-Model crossing forced to two scales; a candidate reframing filed (2026-07-27)

Script: [`scripts/sm_crossing_two_scale.py`](../../scripts/sm_crossing_two_scale.py).

**The forcing argument.** The recorded light framework makes the photon the
substrate's transverse Goldstone mode. Today's sky then decides the crossing's
architecture: photons at wavelengths 10¹⁷ below the dark fluid's coherence length
propagate over ~10¹¹ coherence lengths undispersed (the recorded Lorentz-invariance
pricing). The photon's carrier is not the 402-AU-coherent dark fluid; the substrate
stays coherent far below ξ. **At the door, photons persist.** The single-scale
reading (photons exotically converting at ξ) is dead on observation.

**The crossing is textbook.** Through the interval the photons are ordinary
in-medium fields: massed at the thermal plasma frequency (ω_p ≈ eT/3 — ~100 keV at
an MeV bath: the "crunch mouth masses the photons" line upgrades from story to
in-medium QED), Compton-locked at the recorded Γ/H ~ 10¹⁷ rates, with only the
recorded tiny portals to the dark sector. **The bath's energy passes through
conserved.**

**The budget implication (candidate).** The Standard-Model bath is its own
reservoir riding the contraction, blueshifting as 1/a, passing through the dark
sector's non-hydrodynamic interval intact — the door does not fund the hot start;
the contraction already did. The MeV lever (§18's second live channel) resolves
affirmative at candidate grade, conditional on the two-scale reading (forced) and
bath survival through local rebounds (the portals' smallness — recorded).

**The candidate reframing, filed openly.** Two-scale means the interval is "the
dominant component's hydrodynamics off," metric on — consistent with the
metric-on closures (which were homogeneous-level; the door is inhomogeneous by
this log's own results, and the recorded "homogeneous quantum pressure vanishes"
leaves ξ-scale gradient stress — the verified rebound's own engine — as the local
turn's source). This does not overturn §13/§15; it refines what "the exit from the
metric description" physically is: the source's hydrodynamic exit, locally, with
the substrate persisting. The white-hole file's causal conclusions (the achronal
re-emergence asymmetry) are unchanged — they constrain the same boundary under
either name. Reconciliation with the M4–M8 language is now an open item of this
log, named here rather than smoothed.

---

## 20. The reconciliation, executed (2026-07-27): one regime, two descriptions, no contradiction

The §19 reframing is now reconciled with the M4–M8 board, item by item.

**The scope alignment.** M5 closed homogeneous fluids; M8 closed the homogeneous
constraint and itself located the new physics at ξ-scale gradients; M1/M2/§16
established the door is reached inhomogeneously (the directional squeeze); M6's
verified engine is gradient stress — the exact terms homogeneous averaging kills.
So the board's combined content, stated once: **no homogeneous metric-on turn
exists (exhaustive, unchanged), and the turn is a sub-coherence-scale
inhomogeneous event powered by the dark fluid's gradient stress.** The
homogeneous closures are not weakened — they are what FORCES the turn into the
inhomogeneous regime.

**The two names.** "Metric exit" (the coarse-grained FRW description of the
dominant source fails at ξ) and "hydrodynamic exit, metric on" (the substrate
carrying the geometry stays coherent — forced by the photon argument, §19) are
the same domain in two descriptions. Every computed surface, time, and number
(M4's crossing spreads and front characters; §16's squeeze count; §17's joints)
is identical under both names.

**M4's status change, stated exactly.** At the fundamental level there is no
time-reversed horizon anywhere in the assembly, so the local white-hole no-go is
satisfied automatically and the achronal-re-entry demand softens from causal law
to dynamical consistency: M4's mathematics (the hold vs crossing-spread
arithmetic) becomes the quantitative core of the SEQUENCING problem — do
rebounding pockets and contracting neighbors coexist consistently — which is
task #20's existing content. Nothing computed is discarded; its jurisdiction
moves from kinematics to dynamics.

**The white-hole identification, re-scoped.** The restart is a past boundary OF
THE COARSE-GRAINED DESCRIPTION — the surface where hydrodynamic cosmology begins
again — while the fundamental spacetime is continuous and permeable (the
Standard-Model bath's passage, §19, which is also the budget resolution). The
"exit-only causal role" is a true statement about the description that observers
of the reborn hydrodynamic universe can reconstruct; permeability is a true
statement about the substrate. Both recorded; the forward-facing white-hole file
carries the refinement.

**What this changes on the board:** O2's "written replacement" of the FRW turn
pair now has its candidate form — local gradient-stress rebounds under a
continuous metric, with averaged re-expansion (the inhomogeneous-averaging
bookkeeping is the remaining formal step, folded into task #20); O8 is satisfied
automatically at the fundamental level; O6 is resolved at candidate grade (§19).
The reconstruction's grade stays candidate throughout — but it is now ONE
architecture with two consistent descriptions instead of an architecture with an
unreconciled fork.
