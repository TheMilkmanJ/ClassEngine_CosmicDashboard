# T2 — NEW_CANDIDATES (junction-depth sketches → double kill)

**Package:** `desk_t2_fa2_junction_20260804/`  
**Source of sketches:** N2 SURVIVORS R6 · N2 DOMAIN acoustic inversion · S2 residual “\(\sigma_\mathrm{re}\) conversion written” · MATCHING_DICTIONARY Phase III  
**Protocol:** Rule-1 CANDIDATE on entry · **can-exist** · **should-not-exist** · **double kill** (two independent death reasons) · land only if real closed expression without dial.  
**\(n_\mathrm{new}=3\) · \(n_\mathrm{lands}=0\).**

These are **not** reopens of N1 C0–C8 or S2 A1–A8 as laws. They are the three residual *junction → ρ_re* sketches left open after N1/S2.

---

## NC1 — R6 quench-mode integral → \(\rho_\mathrm{re}\)

### Statement (what a land would require)

\[
\rho_\mathrm{re}
=
\int\!\mathrm{d}^3k\,\;
\omega(k)\,n_k^\mathrm{quench}
\quad\text{(or FA1-table Bogoliubov/quench bath → exterior density)}
\]

with **closed** integrand and measure from stocked FA1 parts only (no free mode densify, no \(N_\mathrm{med}\)).

### Prior status

- N2 SURVIVORS: **R6 · MISSING_INPUT sketch** — “Closed integral from FA1 table without dial.”  
- S2 **A7** already killed the *priced total* \(\rho_\mathrm{quench}/\rho_\mathrm{eff}\sim10^{-97}\).  
- task5_door_budget: quench \(\sim8.9\times10^{-84}\,\mathrm{eV}^4\) · \(\times7\times10^{96}\) under the door.  
- N2 DOMAIN §6: “Using quench split as MeV or \(\rho_\mathrm{re}\) law **without integral**” is forbidden; the integral itself is still unwritten.

### can-exist

FA1 stocks \(x=k\xi\), adiabatic/quench split \(x^*\approx2.46\), medium-sector \(\varepsilon,v_g\); task5 prices a **total** quench energy density. In principle a spectrum integral is the right *shape* for a mode bath.

### should-not-exist as land (double kill)

| kill # | death | evidence |
|---|---|---|
| **K-NC1-a (scale)** | Even the *maximum* stocked quench energy is \(\rho_\mathrm{quench}/\rho_\mathrm{eff}\sim1.4\times10^{-97}\). Need \(S\sim2.8\times10^{-5}\) (late) or \(7.3\times10^{-3}\) (\(\Theta=1\)). Short by \(\sim10^{92}\)–\(10^{95}\). Integral over the **same** bath cannot outgrow its total energy. | S2 A7 · task5 · this desk reconfirm `strongest_stocked_S` |
| **K-NC1-b (missing closed form)** | No written \(\int\mathrm{d}^3k\,\omega n_k\) from FA1 in the corpus that yields exterior \(\rho_\mathrm{re}\). “Integral” remains a word; promoting the sketch without the integrand is fabrication-class. | N2 R6 MISSING_INPUT · FA1 medium-only · G8 SM open |

### Grade

**DOUBLE-KILLED as F-A2 land** · residual: **MISSING_INPUT** only if a *new* spectrum with \(\sim10^{92}\times\) more energy appears from **legal** parts (not stocked).  
**Does not reopen A7 as survivor.**

### Numeric stamp (not a land)

| | value |
|---|---:|
| \(S_\mathrm{quench}\) | \(\approx1.40\times10^{-97}\) |
| \(S_\mathrm{need}^\mathrm{late}\) | \(2.80\times10^{-5}\) |
| shortfall | \(\sim5\times10^{-93}\) in \(S\) ratio to need (\(\sim92\) dex) |

---

## NC2 — \(\sigma_\mathrm{re}\) bookkeeping as \(\rho_\mathrm{re}\) law

### Statement (what a land would require)

A **written** map through Phase II:
\[
(\sigma_\mathrm{door},\rho_\mathrm{eff},\ldots)\;\to\;(\rho_\mathrm{re},\sigma_\mathrm{re})
\]
such that the shear-corrected constraint
\[
H_\mathrm{re}^2=\frac{8\pi G\rho_\mathrm{re}}{3}+\frac{\sigma_\mathrm{re}^2}{3}
\]
locks to \(H_\mathrm{kin}\) (or an acoustic-legal target) **without** deleting shear by fiat and **without** free dials.

### Prior status

- N2 R2: shear-corrected form **STOCKED**; \(\sigma_\mathrm{re}\) **OPEN**.  
- S2 A2a/A3: \(S=1-\mathrm{shear\_frac}=\rho_\mathrm{rad}/\rho_\mathrm{eff}\sim7.2\times10^{-6}\) = **WRONG-OBJECT** (closest magnitude tease).  
- S2 SURVIVORS: “Useful budget fact; **not** F-A2 law until \(\sigma_\mathrm{re}\) conversion written.”  
- MATCHING_DICTIONARY Phase III: \(\rho_\mathrm{re}\) and \(\sigma_\mathrm{re}\) both need legal law.

### can-exist

Door is shear-dominated (\(\mathrm{shear\_frac}\approx1\)); GR free shear \(\sigma\propto a^{-3}\) is textbook; re-entry attachment **should** track both isotropic and anisotropic pieces (R2 honesty).

### should-not-exist as land (double kill)

| kill # | death | evidence |
|---|---|---|
| **K-NC2-a (no conversion map)** | Corpus has **zero** written \(\sigma_\mathrm{door}\to\sigma_\mathrm{re}\) through metric-off Phase II. Keeping door \(\sigma\) at re-entry is an *assumption*, not a derivation. Dropping \(\sigma\) (“use \(\rho_\mathrm{rad}\) only”) is the A2a wrong-object already killed. | N2 R2 OPEN · S2 A2a WRONG-OBJECT · LEGAL_PARTS §6.3 |
| **K-NC2-b (does not supply \(S_\mathrm{need}\))** | If \(\sigma_\mathrm{re}\sim\sigma_\mathrm{door}\) kept, \(H\) is *larger* for given \(\rho\), so the isotropic \(\rho\) needed for a target \(H\) is **smaller** — but the target lock still requires a **law** for which piece is \(\rho_\mathrm{re}\). Setting \(\rho_\mathrm{re}=\rho_\mathrm{rad}\) recovers A3 (\(S\sim7.2\times10^{-6}\)): within \(\sim0.59\) dex of late need, **fails \(\Theta=1\) by \(\sim10^3\)**, and is still door radiation ≠ re-entry law. Setting \(\rho_\mathrm{re}=\rho_\mathrm{eff}\) is N1 C0 (fails late by \(\sim190\times\) in \(H\)). No intermediate stocked rule. | S2 A2a/A3 · N1 C0 · reconfirm anchors |

### Grade

**DOUBLE-KILLED as F-A2 land** · door shear/rad **FACT** remains; \(\sigma_\mathrm{re}\) conversion remains **MISSING_INPUT** (not a survivor land).

---

## NC3 — Acoustic inversion \(\Phi_\mathrm{in}\) → \(\rho_\mathrm{re}\)

### Statement (what a land would require)

Unique re-entry map (S-A / N2 dictionary):
\[
\Phi_\mathrm{in}:\quad
(n,v,\Theta,\ell_\mathrm{grad},\ldots)_\mathrm{gate}
\;\to\;
(\rho_\mathrm{re},\sigma_\mathrm{re},H_\mathrm{re})
\]
with domain \(\langle\Theta\rangle>0\wedge\ell_\mathrm{grad}\gtrsim\xi\), **closed** functional form from stocked acoustic/GPE parts, expanding root not smuggled as free choice sold as Derived magnitude.

### Prior status

- N2 dictionary: **RECONSTRUCTED-PARTIAL** — Phase III magnitude “needs legal \(\rho_\mathrm{re}\) (F-A2 OPEN)”.  
- israel CANDIDATE_ISRAEL **S-A**: stocked half is exit *direction* partial; missing half includes \(\rho_\mathrm{re}\) law.  
- GAP **G7**: inverse F-A1 underdetermined (slice/gauge).  
- N2 R0 default \(H_\mathrm{kin}=H_F(\rho)\) fails magnitude (N1).

### can-exist

Forward acoustic / FA1 medium table exists; kinematic \(H_\mathrm{kin}=\Theta c_s/(d\xi)\) when metric on; preferred-frame fluid description is the seat of F-A1.

### should-not-exist as land (double kill)

| kill # | death | evidence |
|---|---|---|
| **K-NC3-a (no closed inverse)** | Written inverse \(\Phi_\mathrm{in}\) that outputs \(\rho_\mathrm{re}\) **does not exist** in the corpus. Dictionary states domain and forbids Phase-II exterior \(H\); it does **not** supply the density functional. | N2 MATCHING_DICTIONARY · DOMAIN §4 “\(\rho_\mathrm{re}(n,\ldots)\) closed law **OPEN**” |
| **K-NC3-b (underdetermined + residual rename)** | Inverse F-A1 is underdetermined (G7). Identifying \(\rho_\mathrm{re}\) with inverse-Friedmann of \(H_\mathrm{kin}\) is N1 **C4 TAUTOLOGY**. Identifying with door \(\rho_\mathrm{eff}\) is C0. Medium stand-ins \(n,\Theta\) are O(1) (C2/C3/A6). No stocked branch yields \(S\sim10^{-5}\) without dial. | israel G7 · N1 C4 · N1 C0–C3 |

### Grade

**DOUBLE-KILLED as F-A2 land** · dictionary remains **RECONSTRUCTED-PARTIAL construction** (not magnitude land).

---

## Aggregate (new candidates only)

| ID | name | double-kill | land? |
|---|---|---|---|
| NC1 | R6 quench integral | scale \(10^{-97}\) + no closed integral | **NO** |
| NC2 | \(\sigma_\mathrm{re}\) bookkeeping | no conversion map + no stocked \(S_\mathrm{need}\) rule | **NO** |
| NC3 | acoustic inversion \(\Phi_\mathrm{in}\) | no closed inverse + underdetermined/tautology | **NO** |

| metric | value |
|---|---:|
| \(n_\mathrm{new}\) | **3** |
| \(n_\mathrm{lands}\) | **0** |
| real closed expression found | **false** |

> **One-line:** Three residual junction sketches named and double-killed; still **0** F-A2 lands.

---

*End NEW_CANDIDATES.md — NO FABRICATIONS. Sketch formalization ≠ land.*
