# WHAT_RESIDUAL_DEMANDS — O6 MeV over keV after P1+P2

**Package:** `docs/working_logs/_runs/theory_construction_20260804/o6_mev_residual_20260804/`  
**Date:** 2026-08-04  
**Residual ID:** **N5** (from [`../bounce_residual_demand/CANDIDATE_NEXT.md`](../bounce_residual_demand/CANDIDATE_NEXT.md))  
**Mode:** residual demand inventory — **not** a land, **not** bounce closed  
**Fences:** NO FABRICATIONS · no free \(N_\mathrm{med}/\eta\) as Derived · no invent MeV from keV by dial · exit0≠PASS · no bounce closed by O6 alone · leave MCMCs · no PolyChord · no Strong CP bounce

**Parents (read-only):**
- [`../bounce_residual_demand/`](../bounce_residual_demand/) — P1+P2 premise; N5 named OPEN-BLOCKED
- [`../s2_rho_suppression_20260804/`](../s2_rho_suppression_20260804/) — late-lock \(N_\mathrm{med}<0\) sign conflict
- [`../fa3_metric_off/`](../fa3_metric_off/) — sign ≠ temperature
- Scripts: `scripts/rho_bounce.py`, `scripts/bounce_m2b_mixmaster_nmed.py`, `scripts/bounce_task5_door_budget.py`, `scripts/bounce_o6_mev_gap.py`
- Reconstruction: `docs/working_logs/bounce_reconstruction_rp.md` §10.C, §18, §23

---

## 0. Residual identity

| Field | Value |
|---|---|
| Residual family | **O6** MeV-class hot start / reheat over keV door/floor |
| Living grade | **OPEN-BLOCKED** / FAIL on legal parts |
| Relation to P1+P2 | **Orthogonal** — P2 selects **sign** of \(H_\mathrm{re}\); O6 selects **temperature / energy density** |
| Relation to F-A2 / S2 | **Sign-conflicted** if both forced through one free \(N_\mathrm{med}\) dial |
| What this package pays | Stocked gap factors + channel kill map |
| What this package does **not** pay | Derived MeV; bounce close; cyclic; genesis dynamics |

**Standing bar:** after P1+P2 are accepted as CANDIDATE premises, classical turn still does **not** fund BBN. O6 remains a separate residual.

---

## 1. Stocked scales (arithmetic only)

From [`logs/bounce_o6_mev_gap.log`](logs/bounce_o6_mev_gap.log) (exit 0 = compute finished; grade OPEN-BLOCKED):

| Anchor | Value | Source |
|---|---|---|
| \(\rho_\mathrm{bounce}^{1/4}\) | **1.059 keV** | \(m^4/\lambda\); `rho_bounce.py` |
| Door \(T_\mathrm{eff}=\rho_\mathrm{eff}^{1/4}\) | **2.827 keV** | M2 CMB-class \(\Sigma_0=10^{-5}\) |
| Door \(T_\mathrm{rad}\) | **146.4 eV** | radiation piece only |
| BBN bar | **\(T\gtrsim 1\,\mathrm{MeV}\)** | weak-equilibrium start |
| \(\rho_\mathrm{MeV}\) (\(g_*=10.75\)) | \(3.54\times10^{24}\,\mathrm{eV}^4\) | radiation density |

---

## 2. Gap factors MeV must force

| Gap | Factor | Dex |
|---|---|---|
| \(T_\mathrm{MeV}/T_\mathrm{eff}\) | **\(3.54\times10^{2}\)** | 2.55 |
| \(T_\mathrm{MeV}/T_\mathrm{bounce}\) | **\(9.44\times10^{2}\)** | 2.98 |
| \(T_\mathrm{MeV}/T_\mathrm{rad}(\mathrm{door})\) | **\(6.83\times10^{3}\)** | 3.83 |
| \(\rho_\mathrm{MeV}/\rho_\mathrm{eff}\) | **\(5.54\times10^{10}\)** | 10.74 |
| \(\rho_\mathrm{MeV}/\rho_\mathrm{bounce}\) | **\(2.81\times10^{12}\)** | 12.45 |
| \(\rho_\mathrm{MeV}/\rho_\mathrm{rad}(\mathrm{door})\) | **\(7.69\times10^{15}\)** | 15.89 |

**Compression translation (if O6 funded by focus alone from door \(\rho_\mathrm{eff}\)):**

| Quantity | Value |
|---|---|
| Volume focus need | \(\sim5.54\times10^{10}\) |
| Linear compression need | \(\sim3.81\times10^{3}\) |
| Energy-clean instrument ceiling | \(\lesssim25\times\) (spherical drift scaling) |
| Shortfall ceiling→need | \(\sim2\times10^{9}\) (∼9.3 dex) |
| Fabricated \(N_\mathrm{med}\) (\(\eta=1\)) | **6.184** (not Derived) |

---

## 3. What the residual keeps forcing (demand list)

### 3.1 Core hot-start demands

| # | Model is pointing at… | Why forced | Anchor |
|---|---|---|---|
| D1 | A **MeV-class radiation budget** at re-entry / early expanding phase from **legal** parts, **or** an honest kill that this silhouette cannot fund BBN | BBN needs \(T\gtrsim1\,\mathrm{MeV}\); door/floor are keV | O6 FAIL; task5 |
| D2 | Either **pre-door contraction already funds MeV** (genesis / SM bath riding \(1/a\)) **or** a **derived** medium compression / multi-component law that multiplies door energy by \(\gtrsim10^{10}\) in density | Legal door channels all keV-class or below | §19/§23 reconstruction |
| D3 | Separation of **sign residual** (P2 / F-A3) from **temperature residual** (O6) | P1+P2 do not set \(T\) | bounce_residual D6 |
| D4 | Separation of **magnitude residual** (F-A2 needs \(\rho\) **suppression** for late lock) from O6 (needs \(\rho\) **amplification** for MeV) | Opposite arrows on free \(N_\mathrm{med}\) | S2 REPORT |

### 3.2 Honesty / process demands

| # | Model / protocol points at… | Why forced |
|---|---|---|
| D5 | Keep free \(N_\mathrm{med},\eta\) labeled **fabricated** — never Derived | M2; M2b coincidence kill |
| D6 | Do **not** sell \(N_\mathrm{med}=1/c_s\) as identity | M2b: ratio runs ~0.3→5 under \(c_s\) scan |
| D7 | Do **not** invent MeV by dialing keV anchors | Fence |
| D8 | Prefer recorded outer-spec tension over perpetual knob theater | task5 honest endpoint |
| D9 | Bounce not closed by O6 alone even if MeV later lands | O2/F-A3 still PARTIAL |

### 3.3 Negative demands (what residual refuses)

| # | Points **away from**… | Why refused |
|---|---|---|
| D10 | Floor \(\rho_\mathrm{bounce}\) as MeV heat bath | Ceiling PAID ≠ bath; \(T_\mathrm{eff}>T_\mathrm{bounce}\) already |
| D11 | Quench injection at door | Priced \(\sim10^{-84}\,\mathrm{eV}^4\) — ~97 orders under door |
| D12 | 1D overshoot as MeV fund | O(1) only |
| D13 | Unquotable spherical focus rows as measured \(F\) | Energy errors 22–1817%; not converged |
| D14 | P1+P2 ⇒ MeV | Sign ≠ temperature |
| D15 | One dial \(N_\mathrm{med}\) closing both O6 and late lock | Sign conflict: \(+6.18\) vs \(-2.62\) |

---

## 4. Single demand sentence

**After P1+P2, O6 still forces a legal-parts path from keV door/floor (\(\rho_\mathrm{eff}^{1/4}\sim2.8\,\mathrm{keV}\), \(\rho_\mathrm{bounce}^{1/4}\sim1.06\,\mathrm{keV}\)) to a MeV radiation bath (\(\rho\) gap \(\sim10^{10}\)–\(10^{12}\)), without free \(N_\mathrm{med}/\eta\), without inventing MeV by dial, and without confusing sign declaration or magnitude-lock suppression with hot-start funding — or an honest kill that this silhouette under-funds BBN.**

---

## 5. Explicit non-claims

- No Derived MeV hot start.  
- No free \(N_\mathrm{med}=1/c_s\) identity.  
- No bounce closed.  
- No cyclic cosmology.  
- exit 0 ≠ PASS.

---

*End WHAT_RESIDUAL_DEMANDS.md*


## Sign-conflict label (red AGREE-IF cure)

The **−2.62** \(N_\mathrm{med}\) late-lock leg is built from **late_tail10-class** Θ≈0.0619 (S2 / prior N1). Wave-3 **settled_late_theta** demotes that window: stocked default settles to ~0 (or negative). **Do not re-quote −2.62 as settled physics.** Conflict with MeV \(N_\mathrm{med}=+6.18\) remains genuine and **strengthens** under settled Θ→0 (S_need_late→0, N_med(late)→−∞). Both legs are the same object \(S=\rho_\mathrm{re}/\rho_\mathrm{eff}\).
