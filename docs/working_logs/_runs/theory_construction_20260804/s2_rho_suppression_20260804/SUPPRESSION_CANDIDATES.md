# S2 — SUPPRESSION_CANDIDATES

**Target:** \(S\equiv\rho_\mathrm{re}/\rho_\mathrm{eff}\)  
**Need late:** \(S_\mathrm{need}^\mathrm{late}=(H_\mathrm{kin}(\Theta_\mathrm{late})/H_\mathrm{door})^2\approx2.80\times10^{-5}\)  
**Need \(\Theta=1\):** \(S_\mathrm{need}^{\Theta=1}=(c_s/\sqrt3)^2\approx7.30\times10^{-3}\)  
**Compute:** `scripts/bounce_s2_rho_suppression_hunt.py` · log in `logs/`

Protocol: each candidate has **can-exist** and **should-not-exist**. Land only if both pass and numerics close without dial.

---

## A1 — Acoustic dilution over healing lengths

### A1a · \(S=c_s^2\)

| | |
|---|---|
| **can-exist** | \(c_s\) is stocked; acoustic power \(\sim c_s^2\) appears in media |
| **should-not-exist** | No written law \(\rho_\mathrm{re}=\rho_\mathrm{eff}\,c_s^2\); \(S\sim0.022\) short of late by \(\sim780\times\) |
| **grade** | **DEAD-as-law** |
| **S** | \(2.19\times10^{-2}\) |

### A1b · \(S=c_s^4\)

| | |
|---|---|
| **can-exist** | Fourth power of stocked speed (radiation-like double factor fantasy) |
| **should-not-exist** | Not derived; still short of late by \(\sim17\times\); opportunistic power |
| **grade** | **DEAD-as-law** |
| **S** | \(4.79\times10^{-4}\) |

### A1c · \(S=\exp(-4\,H_\mathrm{door}\,t_\mathrm{heal})\)

| | |
|---|---|
| **can-exist** | \(H t_\mathrm{heal}=1/(\sqrt3\,c_s)\approx3.90\) is stocked; radiation e-fold form familiar |
| **should-not-exist** | Door is not an expanding FRW dilution epoch of that duration; oversuppresses late by \(\sim170\times\) |
| **grade** | **DEAD-as-law** |
| **S** | \(1.66\times10^{-7}\) |

### A1d · \(S=\exp(-H_\mathrm{door}\,t_\mathrm{heal})\)

| | |
|---|---|
| **can-exist** | Same stocked product |
| **should-not-exist** | Speculative single-power; wrong scale (\(S\sim0.02\)) |
| **grade** | **DEAD-as-law** |
| **S** | \(2.02\times10^{-2}\) |

**A1 family verdict:** no acoustic healing-length expression is a closed \(\rho_\mathrm{re}\) law. Best magnitude in family (A1b) still short; best exponential (A1c) overshoots and lacks derivation.

---

## A2 — Shear dilution \(\sigma\)

### A2a · \(S=1-\mathrm{shear\_frac}\) (= residual non-shear)

| | |
|---|---|
| **can-exist** | Door is shear-dominated; non-shear fraction equals \(\rho_\mathrm{rad}/\rho_\mathrm{eff}\) |
| **should-not-exist** | Deleting shear by fiat is **not** re-entry bookkeeping; \(\sigma_\mathrm{re}\) must reappear or convert. Wrong object for F-A2 |
| **grade** | **WRONG-OBJECT** |
| **S** | \(7.20\times10^{-6}\) (\(\sim4\times\) *more* suppressed than late need; \(\Theta=1\) fails by \(\sim10^3\)) |

### A2b · \(S=1\) (keep all energy including shear)

| | |
|---|---|
| **can-exist** | Honest door attachment |
| **should-not-exist** | No suppression; late fails by \(\sim3.6\times10^4\) in \(S\) (\(\sim190\times\) in \(H\)) |
| **grade** | **DEAD-as-law** |

**A2 family verdict:** shear split is a real door fact, not a derived amplitude law. Closest *magnitude* to late need in the whole hunt — still not a land.

---

## A3 — Radiation vs medium energy split

### A3 · \(S=\rho_\mathrm{rad}/\rho_\mathrm{eff}\) (door)

| | |
|---|---|
| **can-exist** | Stocked radiation piece at shear door (M2) |
| **should-not-exist** | Door radiation is not “re-entry density after medium interval”; same as A2a numerically; N1 C5 already **DEAD-as-law** for lock (late \(|H_\mathrm{kin}|/H_F\sim2\); accidental) |
| **grade** | **WRONG-OBJECT** |
| **S** | \(7.20\times10^{-6}\) |

**A3 verdict:** stocked split, wrong object, no land.

---

## A4 — Mixmaster window e-folds (derived, not dialed)

### A4a · \(S=\exp(-4 N_\mathrm{mix})\) with \(N_\mathrm{mix}\approx6.26\) **derived**

| | |
|---|---|
| **can-exist** | \(N_\mathrm{mix}\) is a **legal derived number** from \(\Sigma\ge1\to a_\mathrm{loc}\) (M2) — **not** a free dial |
| **should-not-exist as suppression** | Mixmaster is **contraction**: densities **grow** as \(a\) falls. Using \(e^{-4N_\mathrm{mix}}\) as re-entry *dilution* is **wrong-arrow** bookkeeping. Also \(S\sim1.3\times10^{-11}\) oversuppresses late by \(\sim10^6\) |
| **grade** | **DEAD-as-law** (number real; application illegal) |
| **S** | \(1.34\times10^{-11}\) |

### A4b · \(S=\exp(-4 N_\mathrm{dir})\) with \(N_\mathrm{dir}\sim1.73\) (O7 directional band)

| | |
|---|---|
| **can-exist** | Directional mean e-folds stocked \(\sim1.6\)–\(1.9\) (O7) |
| **should-not-exist** | Still not a written \(\rho_\mathrm{re}\) law; \(S\sim10^{-3}\) wrong for both targets |
| **grade** | **DEAD-as-law** |
| **S** | \(9.88\times10^{-4}\) |

**A4 family verdict:** **score the real \(N_\mathrm{mix}\)**; do **not** promote wrong-arrow dilution. Short (actually overshoot) by orders when forced into \(e^{-4N}\).

---

## A5 — Explicit KILL of free \(N_\mathrm{med}\) to target ratio

### A5a · \(\rho_\mathrm{out}=\rho_\mathrm{eff}\,e^{4N_\mathrm{med}}\) with \(N_\mathrm{med}=\tfrac14\ln S_\mathrm{need}^\mathrm{late}\)

| | |
|---|---|
| **can-exist** | As *labeled* M2 sensitivity toy only |
| **should-not-exist as F-A2 land** | Hits late \(S\) **by dial**. \(N_\mathrm{med}^\mathrm{late}\approx-2.62\) (fabricated *dilution*). \(N_\mathrm{med}^\mathrm{MeV}\approx+6.18\) has **opposite sign**. M2b: not \(1/c_s\) identity |
| **grade** | **FABRICATED — KILL** |
| **S** | \(=S_\mathrm{need}^\mathrm{late}\) by construction |

### A5b · same dial to \(\Theta=1\) need

| | |
|---|---|
| **grade** | **FABRICATED — KILL** |
| \(N_\mathrm{med}\)| \(\approx-1.23\) |

**A5 verdict:** free \(N_\mathrm{med}/\eta\) **never** Derived F-A2 land. Explicit honesty kill.

---

## A6 — O(1) medium stand-ins

| ID | expression | S | grade |
|---|---|---:|---|
| A6a | \(1/\mathrm{overshoot}\) | 0.746 | **DEAD-as-law** (O(1)) |
| A6b | \(n_\mathrm{late}\) | 0.682 | **DEAD-as-law** (O(1)) |
| A6c | \(\rho_\mathrm{bounce}/\rho_\mathrm{eff}\) | 0.0197 | **WRONG-OBJECT** (floor; short \(\sim700\times\)) |

**can-exist:** all measured/PAID.  
**should-not-exist as late lock:** none supply \(10^{4}\)–\(10^{5}\) suppression.

---

## A7 — Quench injection (task5)

| | |
|---|---|
| **can-exist** | FA1 quench channel priced: \(\rho_\mathrm{quench}\sim0.5\,m\,c_s^2/\xi^3\) |
| **should-not-exist as F-A2 control** | \(S\sim10^{-97}\); closed for MeV; not a tunable suppression law |
| **grade** | **DEAD-as-law** |

---

## A8 — Inverse tautology

| | |
|---|---|
| **statement** | \(S=(H_\mathrm{kin}/H_\mathrm{door})^2\) |
| **can-exist** | Always consistent with \(H_F=\|H_\mathrm{kin}\|\) |
| **should-not-exist as law** | Imports the answer (N1 C4) |
| **grade** | **TAUTOLOGY** — not a land |

---

## Aggregate scorecard

| metric | value |
|---|---:|
| candidates | 16 |
| legal LANDs | **0** |
| fabricated | 2 (A5a/b) |
| tautology | 1 (A8) |
| wrong-object near magnitude | A2a/A3 (\(S\sim7.2\times10^{-6}\)) |
| best non-fab \(\|log_{10}(S/S_\mathrm{need}^\mathrm{late})\|\) | A2a/A3 · 0.59 dex · **WRONG-OBJECT** |
| free \(N_\mathrm{med}\) to target | **KILLED** |

> **One-line:** Every can-exist path either dies as law, is wrong object, is tautology, or is a free dial. **0 lands.**
