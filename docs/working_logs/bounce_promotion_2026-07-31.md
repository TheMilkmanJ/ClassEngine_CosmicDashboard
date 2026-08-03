# Bounce promotion request — 2026-07-31

## Grade change

| | before | after |
|---|---|---|
| **Track A6 / B7 turn** | **STORY (permanent)** | **RECONSTRUCTED CANDIDATE** |
| Derived? | no | **no** |
| Cyclic cosmology derived? | no | **no** |

**Not requested:** DERIVED. Hard blockers remain (O2 dynamical NEC / matching declaration; O6 MeV legal budget; O7 full survival theorem).

---

## Why this is a real promotion (not a relabel)

The 2026-07-31 e2e verdict stamped **STORY** in part because:

> *No scaffold script. A minimal equations file that closes H=0 and Ḣ>0 from legal parts only does not exist… No `scripts/bounce_rpA_scaffold.py` is issued.*

That gap is now closed **as a reconstructed equation set**, not as a legal-parts FRW bounce:

| deliverable | path |
|---|---|
| Runnable RP-A scaffold | [`scripts/bounce_rpA_scaffold.py`](../../scripts/bounce_rpA_scaffold.py) |
| Self-check O1–O8 | printed pass/fail/partial per outer working |
| Matching rules F-A1…F-A5 | written with status labels (legal / half-machined / reconstructed / fabricated) |

Success criterion from the work order: *write equations/matching rules that close O1–O8 **or** prove a partial promotion with explicit remaining gaps.*  
This is the **partial promotion** branch: equations exist; O2 PARTIAL, O6 FAIL, O7 PARTIAL named explicitly.

---

## Evidence re-run (2026-07-31)

| script | headline |
|---|---|
| `rho_bounce.py` | ρ_bounce^(1/4) = 1.06 keV; finite; ~12 dex under MeV hot start |
| `bounce_handover_sign.py` | vac+rad: ρ+p=(4/3)ρ_r > 0 always; H=0 = turnaround ≠ bounce |
| `bounce_floor_frw_nogo.py` | CSW ≠ FRW bounce; live dCDF NEC-saturating; H⁻¹/ξ~12 at floor |
| `bounce_thermal_crossing_nogo.py` | T=T_c: Ḣ<0; ρ_rad/ρ_bounce ~ 2.8×10⁹ |
| `bounce_m1_shear_xi.py` | local ξ-door open for CMB-class seeds (F-A4 pass-shaped) |
| `bounce_m2_junction.py` | R_H/ξ→√3; N_mix~6.3; T_eff~2.8 keV; N_med≳6.2 for MeV (knob) |
| `bounce_m5_exotic_fluid.py` | exotic X unbuildable from native parts — RP-B dead |
| **`bounce_rpA_scaffold.py`** | **PROPOSED GRADE: RECONSTRUCTED CANDIDATE** |

Dead engines remain dead (not reopened): T=T_c, CSW-as-FRW, barotropic dCDF, stocked exotic X, BH/magnetar sole engine, magnetic flip.

---

## Equations that now exist (scaffold)

### Phase I — metric-on approach (legal GR)

\[
H^2 = \frac{8\pi G}{3}\rho + \frac{\sigma^2}{3},\qquad
\dot\sigma + 3H\sigma = 0 \;\Rightarrow\; \sigma \propto a^{-3}
\]

**Door (F-A4, computed M1/M2):** \(\sigma = 1/\xi\). In shear domination \(R_H/\xi \to \sqrt{3}\).

### Phase II — medium interval (repulsive GPE form + reduced ODEs)

Legal form (healing units):

\[
i\,\partial_t\psi = -\tfrac12\nabla^2\psi + \big(|\psi|^2 - 1\big)\psi
\]

Reduced 0D stand-in in the scaffold (sign: overdense drives expansion):

\[
\dot n = -n\,\Theta,\qquad
\dot\Theta = -\Theta^2 + \kappa(n-1) - \gamma\Theta
\]

Coarse expansion identity (exhibited; full 1D in `bounce_averaging_decomposition.py`):

\[
\frac{d\langle\Theta\rangle}{dt} = -\langle\Theta\rangle^2 - \mathrm{Var}(\Theta) + \mathrm{Stress}
\]

with \(\mathrm{Stress}\) from interaction + quantum-gradient terms **killed by homogeneous averaging**.

### Phase III — matching (written; not all legal)

| rule | content | status |
|---|---|---|
| F-A1 | \(g_{\mu\nu}\|_{door}\to(n,v)\) preferred-frame acoustic inversion | half-machined |
| F-A2 | medium GPE law; cosmological amplitude / \(N_\mathrm{med}\) | legal form / knobs fabricated |
| F-A3 | \(\langle\Theta\rangle>0 \wedge \ell_\mathrm{grad}\gtrsim\xi \Rightarrow H_\mathrm{re}=+\sqrt{8\pi G\rho_\mathrm{re}/3}\) | **reconstructed declaration** |
| F-A4 | shear door clock | computed |
| F-A5 | achronal hold \(\Delta t_\mathrm{hold}\ge \delta_\mathrm{max} R_H/6\) | reconstructed |

**Critical honesty on O2:** \(H_\mathrm{re}>0\) is a **branch declaration** once the medium expansion rate turns — *not* a derivation of homogeneous \(\rho+p<0\). Homogeneous legal parts still cannot bounce (handover_sign + M5).

---

## O1–O8 scorecard (scaffold self-check)

| ID | status | note |
|---|---|---|
| O1 finite density | **PASS** | ρ_bounce ~ (1.06 keV)⁴; medium n bounded |
| O2 turn / written replacement | **PARTIAL** | medium ⟨Θ⟩ turn (toy); H_re by F-A3; no legal ρ+p<0 |
| O3 not live dCDF | **PASS** | not used as engine |
| O4 not CSW-as-FRW | **PASS** | floor is bound, not FRW min a(t) |
| O5 not T=T_c | **PASS** | melt ≠ turn |
| O6 MeV hot start | **FAIL** | legal T_reh ~ keV; MeV needs fabricated N_med≳6.2 or unresolved F≳10⁹ / genesis cascade |
| O7 BKL | **PARTIAL** | window priced; directional squeeze helps; not full theorem |
| O8 no local WH engine | **PASS** | non-metric / hydro-exit hinge; M4 structure |

---

## What still blocks DERIVED

1. **O2 (load-bearing):** No stocked stress-energy with \(\rho+p<0\) at handover. F-A3 declares expanding FRW when medium ⟨Θ⟩>0 — reconstructed matching, not NEC derivation.
2. **O6 (load-bearing):** Door budget ~keV; 1D overshoot O(1); spherical focusing energy-clean F≳10⁹ unreachable on current instruments; SM two-scale bath is candidate-grade only and still arrives cold at the door unless contraction already funded MeV *before* the door (then O6 is “already hot,” which is a different book — genesis cascade / task #11).
3. **O7:** Mixmaster handoff joints exist; not a GR survival theorem through chaos.
4. **F-A1 SM crossing** and **F-A2 cosmological amplitude law** remain open corners.

---

## What is *not* claimed

- Cyclic cosmology is **not** derived.
- Homogeneous FRW bounce from vacuum + radiation + dCDF / CSW / ghost / stocked X is **still DEAD**.
- \(N_\mathrm{med}=1/c_s\) remains a coincidence, not an identity.
- Horizon inheritance that rests only on the bounce is still not independent evidence of a derived turn.

---

## Audience one-liner (updated)

> The model has a derived sub-Planckian density floor and a **reconstructed** metric-exit bounce candidate with written ODEs and matching rules (RP-A scaffold); it does **not** have a derived classical turn or a legal-parts MeV hot start.

---

## Board / verdict actions

- Update `_E2E_DERIVATION_BOARD.md` A6: **STORY (permanent)** → **RECONSTRUCTED CANDIDATE**
- Update `bounce_e2e_verdict_2026-07-31.md` grade + note scaffold exists
- Keep kill list and “do not reopen” engines unchanged
- Prefer kill over fake derivation: O6 stays FAIL; O2 stays PARTIAL

---

## Grade assignment

**RECONSTRUCTED CANDIDATE** for the bounce turn (A6 / B7).

Not DERIVED. Residual sharper than pure STORY: the missing pieces are now named equations (F-A3 dynamical content, O6 funding channel), not “the turn is a story with no equations.”
