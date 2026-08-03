# Bounce turn dynamics — OPEN-THEORY synthesis (2026-08-03)

**Track:** A6 / B7 turn dynamics debt audit  
**Grade (unchanged):** OPEN-THEORY for classical turn; **RECONSTRUCTED CANDIDATE** for RP-A silhouette only  
**Derived bounce?** **No.**  
**Cyclic cosmology booked?** **No.**

Sources (read, not reinvented):

- [`docs/working_logs/bounce_derivation_workplan.md`](../../bounce_derivation_workplan.md)
- [`docs/working_logs/bounce_e2e_verdict_2026-07-31.md`](../../bounce_e2e_verdict_2026-07-31.md)
- [`docs/working_logs/bounce_promotion_2026-07-31.md`](../../bounce_promotion_2026-07-31.md)

Nogo scripts re-run 2026-08-03 under `nice -n 19` (all exit 0; asserts hold). Outputs archived below as proof.

---

## 1. DEAD / NOGO (with script proof)

Do **not** reopen these as FRW bounce engines. Support / timing / structure language may remain; turn-source language is retired.

| engine | kill (why) | script (re-run 2026-08-03) | key numbers |
|---|---|---|---|
| Thermal **T = T_c** as cosmological bounce | Radiation-dominated; `ρ+p ≈ (4/3)ρ_rad > 0` ⇒ `Ḣ < 0`; melt ≠ turn | `scripts/bounce_thermal_crossing_nogo.py` | `ρ_rad/ρ_bounce ≈ 2.76×10⁹` (9.44 dex); bare vac / ρ_rad(T_c) ≈ 7×10⁻³³ |
| **CSW / ρ_bounce** as homogeneous FRW bounce | Polytrope and p~ρ ceilings both have `ρ+p > 0`; bare cannot cancel floor | `scripts/bounce_floor_frw_nogo.py` (A) | `ρ_bounce^(1/4) = 1.059 keV`; `ρ_bounce/|ρ_Λ| ≈ 4.9×10²²` |
| Live **barotropic dCDF** (`w = −ρ_inf/ρ`) | `ρ+p = ρ−ρ_inf ≥ 0`; floor ⇒ `Ḣ = 0` coast, not bounce | same script (B) | at floor: `(ρ+p)/ρ_inf = 0` (coast) |
| **Hubble-scale metric exit at ρ_bounce** | Homogeneous metric still classically OK at floor | same script (C) | `H⁻¹/ξ ≈ 12.3` at floor; exit needs ~152× ρ_bounce (~3.72 keV) |
| **Magnetic polarity flip** / diamagnetism as turn | `T(B)=T(−B)` (quadratic); NEC ≥ 0; budget frozen ≪ radiation | `scripts/bounce_magnetic_flip_nogo.py` | max \|T(B)−T(−B)\| = 0; CMB-cap ρ_B / ρ_rad0 ≈ 5.8×10⁻⁸ |
| Vac + rad homogeneous bounce | `1+w_vac ≡ 0` ⇒ vacuum inert in `Ḣ`; `ρ+p = (4/3)ρ_r > 0` always; H=0 is **turnaround** (wrong sign) | `scripts/bounce_handover_sign.py` | identity, not a near-miss |
| Homogeneous **exotic X** from stocked / DE-scale parts | Required window: `ρ_X ≈ −ρ_rad`, `w_X > 1/3`; DE-scale short by 10¹⁹–10³² | `scripts/bounce_rp_required_X.py`, `bounce_m5_exotic_fluid.py` | at T_c: \|ρ_X\|/ρ_Λ ~ 10³² |
| DE-scale **ghost** as crunch X | Wrong budget / wrong attractor (late-time floor) | floor / RP-B path | retired |
| **N_med = 1/c_s** as derived MeV compression | Coincidence under c_s / T_reheat variation | `bounce_m2b_mixmaster_nmed.py` | knob stays fabricated |
| Homogeneous **quartic / higher-order Friedmann** bounce | QP vanishes in FRW; ledger returns standard H² | `bounce_m8_ledger_quartic.py` | dead engine |
| BH / magnetar / fountain / neutrino freeze / high-f portal / electron current as **sole** turn engines | Reservoir / timing / contact / trigger only — no `ρ_X+p_X < 0` | failures ledger + electron-contact pricing | NEC class fail for turn primitive |

### Proof dump (nogo re-runs, 2026-08-03)

**A. Floor / dCDF / metric-exit** (`bounce_floor_frw_nogo.py`, exit 0):

```
(A) CSW ceiling in homogeneous FRW
  rho_bounce^(1/4)     = 1.059e+03 eV
  rho_bounce/|rho_L|   = 4.912e+22  (bare cannot cancel)
  VERDICT A: CSW floor ≠ FRW bounce

(B) Live barotropic dCDF  w = -rho_inf/rho
  rho/rho_inf=1 → (rho+p)/rho_inf = 0  (Ḣ=0 coast, not bounce)
  VERDICT B: NEC combination never negative

(C) Metric exit at xi vs recorded floor
  H^-1/xi at floor  = 12.34
  rho_exit/rho_bounce  = 1.522e+02
  VERDICT C: Hubble-scale metric exit is above the CSW ceiling
```

**B. Magnetic flip** (`bounce_magnetic_flip_nogo.py`, exit 0):

```
max |T(B) − T(−B)| = 0.0e+00   (identically zero)
NEC along principal axes: ≥ 0 always
CMB comoving cap: ρ_B / ρ_rad0 ≈ 5.8e-08 (frozen a^-4 ratio)
VERDICT: turn mechanism FAIL by class, twice
```

**C. Thermal crossing** (`bounce_thermal_crossing_nogo.py`, exit 0):

```
T_c = 177.10 keV
rho_rad/rho_bounce = 2.764e+09   (9.44 dex)
rho + p ≈ (4/3) rho_rad > 0  ⇒ Ḣ < 0  ⇒ bounce FAILS
need |rho_X+p_X| ≳ radiation scale (~10^9 × rho_bounce)
VERDICT: melt threshold only; not a bounce
```

**D. Handover sign identity** (`bounce_handover_sign.py`, exit 0):

```
w=-1 component contributes EXACTLY zero to rho+p
rho+p = (4/3) rho_r > 0 always → Hdot < 0 always
H=0 from vac+rad is TURNAROUND, opposite of bounce
Missing homogeneous object: negative-energy stiff (w=+1, rho<0)
  — and stocked parts do not supply it (M5 / rp_required_X)
```

---

## 2. Still OPEN for turn dynamics

These are **not** promotions. They are the residual surface after the kill list.

### 2.1 Load-bearing gaps (named residuals)

| ID | residual | grade | note |
|---|---|---|---|
| **O2** | Dynamical turn / re-entry `H_re > 0` | **PARTIAL** | Medium `⟨Θ⟩` turn exists in toy/M6 GPE; FRW re-entry is still **F-A3 declaration**, not NEC derivation |
| **O6** | MeV hot start over keV door | **FAIL** on legal parts | Door ~keV; needs fabricated `N_med ≳ 6.2`, clean spherical F ≳ 10⁹, or genesis-cascade “already hot” book |
| **O7** | BKL / mixmaster survival through medium interval | **PARTIAL** | Window priced; directional squeeze helps; not a GR survival theorem |
| **F-A1** | Metric ↔ medium map at door | half-machined | Preferred-frame acoustic inversion underdetermined without extra structure |
| **F-A2** | Cosmological amplitude / `N_med` law | legal form + knobs | Amplitude law not OEM |
| **F-A3** | Expanding re-entry rule | reconstructed | `⟨Θ⟩>0 ∧ ℓ_grad ≳ ξ ⇒ H_re = +√(8πGρ_re/3)` — **declaration** |
| Crunch-sector **X** or written **FRW exit** | classical turn primitive | **not written** | Homogeneous legal fluids cannot bounce; only non-metric / hydro-exit silhouette (RP-A) survives as candidate shape |

### 2.2 What *is* derived / standing (cite, do not re-derive)

- Finite floor `ρ_bounce = m⁴/λ ~ (1.06 keV)⁴` — BH/core ceiling number, not FRW min `a(t)`
- Compact-torus zero-net energy ledger → standard flat `H² = (8πG/3)ρ` (does **not** force `Ḣ > 0`)
- Local white-hole no-go in a globally time-oriented medium
- Live dCDF structure (`w → −1` floor) as expanding-branch fluid — not a bounce engine
- Shear/ξ door timing (M1–M2): local-first door possible; `R_H/ξ → √3` in shear domination
- Turnaround ≠ bounce: bare+thaw can give late expanding-branch `H = 0`; wrong epoch / wrong `Ḣ` sign for crunch restart

### 2.3 Only non-killed silhouette: RP-A

**RP-A:** metric / hydro exit at healing length `ξ` → medium processes finite density (GPE-class) → metric re-emerges expanding.

- Equations + matching F-A1…F-A5: **written** in `scripts/bounce_rpA_scaffold.py`
- Grade: **RECONSTRUCTED CANDIDATE** (2026-07-31 promotion), **not DERIVED**, not OEM
- O1, O3–O5, O8: PASS on scaffold honesty labels
- Homogeneous FRW bounce from stocked parts: **DEAD** (orthogonal to RP-A; do not smuggle back)

### 2.4 Support roles still allowed (not turn engines)

BH cores, magnetars, fountain residual, neutrino freeze timing, high-f dyad portal, electron contact wire: may participate as reservoir / timing / contact / trigger inside a **combined** crunch bath. None supplies the turn primitive alone (NEC class or budget class).

### 2.5 What homogeneous FRW would still need (if metric stays on)

From `bounce_handover_sign.py` + `bounce_rp_required_X.py`:

- either negative-energy stiff (`w = +1`, `ρ < 0`) that dominates at max compression,
- or phantom / noncanonical with `ρ_X + p_X < −(4/3)ρ_rad` at handover,
- **and** stocked DE-scale / live-dCDF / ghost-floor parts **fail that window** by many orders.

Honest path if metric stays on: invent nothing — keep the object **unnamed and open**. RP-A is the path that *leaves* homogeneous FRW instead of minting illegal X.

---

## 3. Single highest-leverage NEXT compute

**Target: close F-A3 dynamical content without hand declaration (O2 load-bearing).**

Concretely:

1. Start from the written Phase-II reduced medium ODEs / 1D GPE rebound already in the scaffold and M6 scripts (`bounce_rpA_scaffold.py`, `bounce_m6_rebound_*.py`, `bounce_averaging_decomposition.py`).
2. Define a **matching observable** from medium → exterior: not “declare `H_re > 0` when `⟨Θ⟩ > 0`,” but derive a continuous (or junction-condition) map from
   - medium expansion rate `⟨Θ⟩`, density `n`, gradient scale `ℓ_grad`,
   - to exterior FRW `(H, ρ_re)` under F-A1’s preferred-frame acoustic structure.
3. Pass/fail criterion:
   - **PASS path:** exterior `H` crosses through 0 with `Ḣ > 0` **as a consequence** of medium stress + junction, with fabrication labels only on unfilled F-A1 SM-crossing corners — not on the turn sign itself.
   - **FAIL path:** show that every legal GPE / averaging stress (interaction + quantum gradient killed by homogeneous average) **cannot** produce exterior `Ḣ > 0` without a new noncanonical medium term — then RP-A O2 stays PARTIAL forever until that term is written, and the honest stamp remains reconstructed-not-derived.

**Why this is highest leverage (not O6, not O7 first):**

- O6 (MeV) is a **funding** residual; solving it without a dynamical turn still leaves no bounce.
- O7 (BKL) is a **survival** residual; it assumes a turn interval exists.
- O2 / F-A3 is the **turn primitive**. Without it, every other residual is polishing a declaration.
- Homogeneous engines are already dead with proof; reopening them is negative leverage.
- The compute is local to existing scripts (GPE rebound + averaging + scaffold matching) — no need to invent cosmology.

**Explicit non-goal of the next compute:** do **not** introduce a fabricated negative-energy stiff fluid to “close” homogeneous FRW. Prefer kill over fake derivation.

---

## 4. Explicit non-claims (no cyclic cosmology booking)

1. **Cyclic cosmology is not derived.** No full closed cycle (expansion → turnaround → crunch → bounce → hot start → re-expansion) is booked as OEM or DERIVED.
2. **Classical homogeneous FRW bounce from legal stocked parts is DEAD.** Vac+rad, CSW floor, live dCDF, thermal T_c, magnetic flip, stocked exotic X, ghost floor, quartic ledger — all killed with script proof.
3. **RP-A is a reconstructed candidate, not a derived bounce.** Written ODEs and matching do not equal derivation of `H = 0`, `Ḣ > 0` from legal stress-energy.
4. **F-A3 is a branch declaration**, not a NEC theorem. Medium `⟨Θ⟩` turn ≠ exterior cosmological bounce until matching closes O2.
5. **Finite `ρ_bounce` is not a bounce.** It is a sub-Planckian density ceiling (core/hydrostatic number).
6. **Turnaround ≠ bounce.** Late bare+thaw `H = 0` is expanding-branch reversal with the wrong `Ḣ` sign for restart.
7. **Melt ≠ turn.** `T = T_c` is real local physics; it does not produce `Ḣ > 0`.
8. **Horizon inheritance that rests only on the bounce is not independent evidence** of a derived turn.
9. **`N_med = 1/c_s` is coincidence, not identity.** MeV over keV remains FAIL on legal parts.
10. **This report invents no bounce source term X** and promotes no retired engine.

---

## Program stamp (2026-08-03)

> **Bounce turn dynamics = OPEN-THEORY.** Homogeneous legal-parts turn = **DEAD**. RP-A = **RECONSTRUCTED CANDIDATE** with named residuals O2 PARTIAL / O6 FAIL / O7 PARTIAL. Next compute: dynamical F-A3 / O2 matching from medium stress — prefer kill over fabrication. **Do not book cyclic cosmology.**

### Audience one-liner

> The model has a derived sub-Planckian density floor and a reconstructed metric-exit bounce *silhouette* with written ODEs; it does **not** have a derived classical turn, a legal-parts MeV hot start, or a derived cyclic cosmology.

---

## Artifact paths

| item | path |
|---|---|
| This report | `docs/working_logs/_runs/debt_bounce_20260803/REPORT.md` |
| Workplan | `docs/working_logs/bounce_derivation_workplan.md` |
| E2E verdict | `docs/working_logs/bounce_e2e_verdict_2026-07-31.md` |
| Promotion | `docs/working_logs/bounce_promotion_2026-07-31.md` |
| RP-A scaffold | `scripts/bounce_rpA_scaffold.py` |
| Nogo scripts | `scripts/bounce_floor_frw_nogo.py`, `bounce_magnetic_flip_nogo.py`, `bounce_thermal_crossing_nogo.py` |
| Sign / X window | `scripts/bounce_handover_sign.py`, `scripts/bounce_rp_required_X.py` |
