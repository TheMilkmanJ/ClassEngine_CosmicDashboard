# S2 — LEGAL_PARTS_INVENTORY (what may enter ρ_re(…))

**Package:** `s2_rho_suppression_20260804`  
**Rule:** only stocked / previously paid quantities. Free dials labeled **FABRICATED** and never counted as land.

---

## 1. Door / shear clock (M1–M2; PAID bookkeeping)

| symbol | value / form | status | may enter ρ_re? |
|---|---|---|---|
| \(\xi\) | 402 AU | corpus coherence | length scale only |
| \(c_s=\sqrt{3\alpha}\) | 0.14796 | corpus sound speed | dimensionless factor |
| \(\Sigma_0\) | \(10^{-5}\) (CMB-class default) | seed scan param | sets door, not free amplitude |
| \(H_0,\Omega_r\) | standard order | cosmology clock | door construction |
| \(\sigma\propto a^{-3}\) | GR free shear | textbook | door \(\sigma\), shear_frac |
| \(a_\mathrm{loc}=(\sigma_0\xi)^{1/3}\) | local \(R_\sigma=\xi\) exit | derived | door state |
| \(H_\mathrm{door}\) | \(\approx 1/(\sqrt3\,\xi)\) shear-dom | derived at door | magnitude reference |
| \(\rho_\mathrm{eff}=3H^2 M_\mathrm{Pl}^2/(8\pi)\) | door total | derived | **denominator** of \(S\) |
| \(\rho_\mathrm{rad}\) | \(\Omega_r\rho_c/a_\mathrm{loc}^4\) | derived | piece of door budget |
| \(\mathrm{shear\_frac}=(\sigma^2/3)/H^2\) | \(\approx1\) at door | derived | split diagnostic |
| \(N_\mathrm{mix}=\ln(a_{\Sigma=1}/a_\mathrm{loc})\) | \(\approx6.26\) | **derived** shear clock | e-fold *count*; not a free dial |
| \(\Delta t_\mathrm{mix}/t_\mathrm{heal}\) | \(\sim10^7\) | derived (M2b) | duration diagnostic |
| \(H_\mathrm{door}\,t_\mathrm{heal}=1/(\sqrt3\,c_s)\) | \(\approx3.90\) | derived | acoustic time ratio |

## 2. Floor / medium stand-ins

| symbol | value / form | status | may enter ρ_re? |
|---|---|---|---|
| \(\rho_\mathrm{bounce}=m^4/\lambda\) | \(T\sim1.06\,\mathrm{keV}\) | **PAID** ceiling | wrong object as turn amplitude |
| \(m,\lambda\) | recorded | corpus | only via floor |
| 0D \((n,\Theta)\) ODE | \(\kappa=1.5,\gamma=0.15\) | stand-in toy | late \(\Theta\), overshoot, \(n_\mathrm{late}\) |
| overshoot \(n_\mathrm{peak}/n_0\) | \(\approx1.34\) | 0D measured | O(1) only |
| late \(\Theta\) | \(\approx+0.062\) | 0D measured | sets late \(H_\mathrm{kin}\) |
| late \(n\) | \(\approx0.68\) | 0D measured | O(1) |
| 1D rebound overshoot | \(\sim O(1)\) (M6) | verified class | not MeV / not \(10^{4}\) suppression |
| \(t_\mathrm{heal}=\xi/c_s\) | medium time | definition | clock only |

## 3. Kinematic / matching objects (F-A2 residual)

| symbol | form | status | note |
|---|---|---|---|
| \(H_\mathrm{kin}=\Theta_\mathrm{heal}\,c_s/(d\,\xi)\) | kinematic fluid scale | stocked definition | needs \(\Theta\) from stress |
| \(H_F(\rho)=\sqrt{8\pi G\rho/3}\) | Friedmann | stocked | lock target |
| \(\Theta_\mathrm{lock}=d/(c_s\sqrt3)\) | \(\approx11.71\) (d=3) | **algebra**, not derived stress | MISSING_INPUT if used as land |
| \(S_\mathrm{need}=(H_\mathrm{kin}/H_\mathrm{door})^2\) | required \(\rho_\mathrm{re}/\rho_\mathrm{eff}\) | residual demand | not a medium law |

## 4. Junction / translation (half-machined)

| piece | status | may enter ρ_re? |
|---|---|---|
| FA1 trans-phononic table (\(x=k\xi\), quench \(x_*\approx2.5\)) | medium-sector machined | quench \(\rho\) **tiny** (task5) |
| Task4 handoff Mach / planarity | joints computed | kinematics, not density law |
| O7 directional mean e-folds \(\sim1.6\)–\(1.9\) | computed band | not a \(\rho\) map |
| M4 hold / achronal | structural | not density |
| SM-sector crossing | **UNWRITTEN** | cannot invent content |

## 5. Explicitly **not** legal as Derived land

| knob / move | label | why |
|---|---|---|
| \(N_\mathrm{med}\) free | **FABRICATED** (M2) | Phase-II compression dial |
| \(\eta\) heat efficiency free | **FABRICATED** (M2) | toy junction |
| \(N_\mathrm{med}=1/c_s\) as identity | **KILLED** (M2b) | numerical coincidence only |
| Free \(H_\mathrm{re}\) number | **FORBIDDEN** | invent |
| Inverse \(\rho=3H_\mathrm{kin}^2 M_\mathrm{Pl}^2/(8\pi)\) as law | **TAUTOLOGY** | N1 C4 |
| Continuous metric-ON \(H:-\to0\to+\) | **DEAD** | obstruction A |
| Homogeneous FRW bounce engines | **DEAD** | nogo stack |
| Strong CP as bounce | **FENCED** | sector |

## 6. What is *missing* for a real \(\rho_\mathrm{re}(\ldots)\) law

1. Microphysical matching content under acoustic inversion (F-A1 re-entry book) — **N2**.  
2. Production \(\Theta_\mathrm{heal}\) from 3D stress if door \(\rho_\mathrm{eff}\) kept — **N3**.  
3. Written conversion of shear \(\leftrightarrow\) isotropic radiation at re-entry (cannot drop \(\sigma\) by fiat).  
4. SM-sector energy at the door (task #14) if that is the real budget.

**Inventory conclusion:** many stocked *numbers*; **no stocked derived map** \(\rho_\mathrm{re}(\text{legal parts})\) that closes \(S\sim2.8\times10^{-5}\) without dial or tautology.
