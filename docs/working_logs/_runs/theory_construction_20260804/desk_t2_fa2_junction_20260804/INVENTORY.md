# T2 — Inventory of stocked junction → ρ_re maps

**Package:** `desk_t2_fa2_junction_20260804/`  
**Question:** Which junction/matching maps from the corpus could fix \(\rho_\mathrm{re}\) (F-A2 / obstruction C)?  
**Rule:** cite priors; do not invent closed expressions; free \(N_\mathrm{med}\) never land.

---

## 0. Lock target (reconfirmed this desk)

From `scripts/bounce_s2_rho_suppression_hunt.py` → [`logs/s2_Sneed_reconfirm.log`](./logs/s2_Sneed_reconfirm.log) · [`logs/anchors_Sneed.json`](./logs/anchors_Sneed.json):

| quantity | value |
|---|---:|
| \(S_\mathrm{need}^\mathrm{late}=(H_\mathrm{kin}^\mathrm{late}/H_\mathrm{door})^2\) | \(2.798618\times10^{-5}\) |
| \(S_\mathrm{need}^{\Theta=1}=(c_s/\sqrt3)^2\) | \(7.297300\times10^{-3}\) |
| \(\|H_\mathrm{kin}(\Theta=1)\|/H_\mathrm{door}\) | \(0.085424\) |
| \(\|H_\mathrm{kin}(\mathrm{late})\|/H_\mathrm{door}\) | \(0.005290\) |
| \(\Theta_\mathrm{lock}(d=3)\) | \(11.7062\) |
| \(\rho_\mathrm{rad}/\rho_\mathrm{eff}\) (door) | \(7.201\times10^{-6}\) |
| quench \(S=\rho_\mathrm{quench}/\rho_\mathrm{eff}\) | \(\sim1.40\times10^{-97}\) |

---

## 1. Already killed in N1 (cite: do not reopen as land)

**Source:** `n1_fa2_amplitude_20260804/CANDIDATE_MAPS.md` · `SCORECARD.md` · `REPORT.md`  
**Count:** 11 maps · **legal lands: 0**

| ID | map \(\rho_\mathrm{re}=\) | grade | cite |
|---|---|---|---|
| C0 | \(\rho_\mathrm{eff}\) | DEAD-as-law | N1 REPORT §4 |
| C1 | \(\rho_\mathrm{bounce}=m^4/\lambda\) | WRONG-OBJECT | N1 CANDIDATE_MAPS C1 |
| C2a | \(\rho_\mathrm{eff}\,n_\mathrm{late}\) | DEAD-as-law | N1 SCORECARD |
| C2b | \(\rho_\mathrm{bounce}\,n_\mathrm{late}\) | WRONG-OBJECT | N1 SCORECARD |
| C3 | \(\rho_\mathrm{eff}/\mathrm{overshoot}\) | DEAD-as-law | N1 C3 |
| C4 | \(3H_\mathrm{kin}^2 M_\mathrm{Pl}^2/(8\pi)\) | **TAUTOLOGY** | N1 C4 |
| C5 | \(\rho_\mathrm{rad}\) (door) | DEAD-as-law | N1 C5 |
| C6 | \(\rho_\mathrm{eff}\) @ \(\Theta=1\) | STILL-OPEN *diagnostic* (not law) | N1 C6 |
| C7 | \(\rho_\mathrm{eff}\) @ \(\Theta=\Theta_\mathrm{lock}\) | MISSING_INPUT (Θ path) | N1 C7 |
| C8a | \(\eta\rho e^{4N_\mathrm{med}}\) → MeV | **FABRICATED** | N1 C8a |
| C8b | same → late lock | **FABRICATED** | N1 C8b |

---

## 2. Already killed in S2 (cite: do not reopen as land)

**Source:** `s2_rho_suppression_20260804/SUPPRESSION_CANDIDATES.md` · `REPORT.md`  
**Count:** 16 candidates · **legal lands: 0**

| ID | \(S=\rho_\mathrm{re}/\rho_\mathrm{eff}\) | grade | cite |
|---|---|---|---|
| A1a | \(c_s^2\) | DEAD-as-law | S2 A1a |
| A1b | \(c_s^4\) | DEAD-as-law | S2 A1b |
| A1c | \(\exp(-4 H_\mathrm{door}t_\mathrm{heal})\) | DEAD-as-law | S2 A1c |
| A1d | \(\exp(-H_\mathrm{door}t_\mathrm{heal})\) | DEAD-as-law | S2 A1d |
| A2a | \(1-\mathrm{shear\_frac}\) | **WRONG-OBJECT** | S2 A2a |
| A2b | \(S=1\) (keep all) | DEAD-as-law | S2 A2b |
| A3 | \(\rho_\mathrm{rad}/\rho_\mathrm{eff}\) | **WRONG-OBJECT** | S2 A3 (=A2a num.) |
| A4a | \(\exp(-4N_\mathrm{mix})\), \(N_\mathrm{mix}\approx6.26\) derived | DEAD-as-law (wrong-arrow) | S2 A4a |
| A4b | \(\exp(-4N_\mathrm{dir})\), \(N_\mathrm{dir}\sim1.73\) | DEAD-as-law | S2 A4b |
| A5a/b | free \(N_\mathrm{med}\) to \(S_\mathrm{need}\) | **FABRICATED — KILL** | S2 A5 |
| A6a | \(1/\mathrm{overshoot}\) | DEAD-as-law | S2 A6a |
| A6b | \(n_\mathrm{late}\) | DEAD-as-law | S2 A6b |
| A6c | \(\rho_\mathrm{bounce}/\rho_\mathrm{eff}\) | WRONG-OBJECT | S2 A6c |
| A7 | \(\rho_\mathrm{quench}/\rho_\mathrm{eff}\) | DEAD-as-law (scale \(\sim10^{-97}\)) | S2 A7 · task5 |
| A8 | \((H_\mathrm{kin}/H_\mathrm{door})^2\) | **TAUTOLOGY** | S2 A8 |

---

## 3. Stocked junction / matching objects **not** already scored as closed \(\rho_\mathrm{re}\) lands

These are the only remaining stocked *junction-class* objects that still touch F-A2 without having been sold as Derived \(\rho_\mathrm{re}\) laws in N1/S2. **None is a closed expression.**

| ID | object | prior grade | why not already an N1/S2 land | cite |
|---|---|---|---|---|
| **MB-R1** | \(H_\mathrm{kin}\) as re-entry *target* only | CANDIDATE-REFRAME | renames residual; no \(\rho_\mathrm{re}\) | N2 ALTERNATE_MATCH_RULES R1 |
| **MB-R2** | shear-corrected \(H^2=8\pi G\rho/3+\sigma^2/3\) | STOCKED-SHEAR form | form paid; \(\sigma_\mathrm{re}\) OPEN | N2 R2 · MATCHING_DICTIONARY Phase III |
| **MB-R3** | Israel / surface stress across Phase II | MISSING_INPUT | 0 stocked \(S_{ab}\) eqs | N2 R3 · israel_junction GAP G1–G3 |
| **MB-R6** | quench mode energy → \(\rho_\mathrm{re}\) integral | MISSING_INPUT sketch | no closed integral; A7 killed *ratio only* | N2 SURVIVORS R6 · DOMAIN §6 |
| **MB-Dict** | Phase I–III matching dictionary | RECONSTRUCTED-PARTIAL | bookkeeping; magnitude OPEN | N2 MATCHING_DICTIONARY · REPORT |
| **S-A** | two acoustic maps \(\Phi_\mathrm{out},\Phi_\mathrm{in}\) | RECONSTRUCTED-PARTIAL | inverse underdetermined (G7) | israel CANDIDATE_ISRAEL S-A |
| **S-B/C** | Israel on metric sides / medium \(\Delta\Pi\) | MISSING_INPUT | no \(S_{ab},K_{ab}\) | israel S-B/S-C · sab C1–C12 |
| **FA1-table** | \(x=k\xi\), \(x^*\approx2.5\), \(v_g,c_s\) | PAID medium partial | not \(\rho_\mathrm{re}\) law; SM open | FA1 · N2 DOMAIN §6 |
| **task5 quench ρ** | \(\rho_\mathrm{quench}\sim\tfrac12 m c_s^2/\xi^3\) | DEAD for MeV / A7 | number paid; not F-A2 control | task5_door_budget · S2 A7 |
| **door split** | \(\rho_\mathrm{rad},\sigma,\mathrm{shear\_frac}\) | FACT | budget fact ≠ re-entry law | S2 A2/A3 · LEGAL_PARTS |
| **N_mix** | \(\approx6.26\) derived shear clock | FACT | illegal as wrong-arrow dilution | S2 A4a · SURVIVORS |

---

## 4. Explicitly **not** legal inputs (reconfirmed)

| forbidden | cite |
|---|---|
| free \(N_\mathrm{med},\eta\) as Derived | N1 C8 · S2 A5 · israel K1 |
| invent \(H_\mathrm{re}\) | fences all packages |
| continuous metric-ON \(H:-\to0\to+\) | obstruction A · N2 R4 |
| inverse Friedmann as medium law | N1 C4 · S2 A8 |
| free \(\alpha\) on \(\sigma_s=\alpha\rho\xi\) | israel_sab C5 |

---

## 5. Inventory conclusion

- **Killed closed maps (N1+S2):** \(11+16\) scored · **0 lands**.  
- **Not-yet-killed as *new closed* \(\rho_\mathrm{re}\) expressions:** only **sketches / missing inputs** (R6 integral, \(\sigma_\mathrm{re}\) conversion, acoustic \(\Phi_\mathrm{in}\), Israel \(S_{ab}\to\rho\)).  
- **T2 action:** formalize those three junction-depth sketches as named candidates and **double-kill** each (§ NEW_CANDIDATES).  
- **Still true:** no stocked closed \(\rho_\mathrm{re}(\text{legal parts})\) that hits \(S\sim2.8\times10^{-5}\) without dial or tautology.

---

*End INVENTORY.md — cite-only; no new land.*
