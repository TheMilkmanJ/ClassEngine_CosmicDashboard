# N1 — F-A2 amplitude / ρ_re law hunt (2026-08-04)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/n1_fa2_amplitude_20260804/`  
**Seat:** Grok blue  
**Prior:** `bounce_residual_demand` N1 · `fa3_metric_off` obstruction C · `debt_bounce_FA3` · FA3 script  
**Fences:** NO invent \(H_\mathrm{re}\) · no free dial N_med/η as Derived · no bounce closed · no cyclic · leave MCMCs · no PolyChord · no Strong CP  
**COMPLETE:** **0** — grade **OPEN-BLOCKED**

---

## 0. One-liner

**Eleven candidate ρ_re / amplitude maps (C0–C8, plus C2b and C8b) from stocked parts: 0 legal lands. Obstruction C stands. Tautology and M2 dials can “lock” only by cheating. Residual still forces either derived Θ_heal ≳ 11.7 or a non-dialled ρ_re law or a different matching rule (N2).**

---

## 1. Mission

After P1+P2 (sign architecture) are accepted as CANDIDATE premises, N1 attacks obstruction **C**:

\[
|H_\mathrm{kin}| \;\stackrel{?}{=}\; H_F(\rho_\mathrm{re}),\qquad
H_\mathrm{kin}=\Theta_\mathrm{heal}\,\frac{c_s}{d\,\xi}.
\]

**Land** would be a closed expression \(\rho_\mathrm{re}(\ldots)\) in legal parts that closes the lock without free dials.  
**This package does not invent a land.**

---

## 2. Package contents

| File | Role |
|---|---|
| [`REPORT.md`](./REPORT.md) | This executive |
| [`CANDIDATE_MAPS.md`](./CANDIDATE_MAPS.md) | Eleven maps (C0–C8, plus C2b and C8b) + can-exist / should-not-exist |
| [`SCORECARD.md`](./SCORECARD.md) | Numeric scores from hunt script |
| [`SURVIVORS.md`](./SURVIVORS.md) | What remains for deeper work |
| [`NON_CLAIMS.md`](./NON_CLAIMS.md) | Fences |
| [`logs/n1_fa2_amplitude_hunt.log`](./logs/n1_fa2_amplitude_hunt.log) | Full compute |
| Script | `scripts/bounce_n1_fa2_amplitude_hunt.py` |

---

## 3. Reconfirm anchors (disk, this run)

| quantity | value |
|---|---|
| \(c_s=\sqrt{3\alpha}\) | 0.14796 |
| \(H_\mathrm{door}\) | \(1.894\times10^{-21}\) eV |
| \(\rho_\mathrm{eff}^{1/4}\) (door) | 2.827 keV |
| \(\rho_\mathrm{bounce}^{1/4}\) | 1.059 keV |
| \(\|H_\mathrm{kin}(\Theta=1,d=3)\|/H_\mathrm{door}\) | **0.08542** (\(=c_s/\sqrt3\)) |
| \(\|H_\mathrm{kin}(\Theta_\mathrm{late},d=3)\|/H_\mathrm{door}\) | **0.00529** |
| \(\Theta_\mathrm{lock}\) for door match | **11.71** |
| 0D late \(\Theta\) | +0.062 |
| 0D overshoot | 1.34 |
| \(\rho_\mathrm{need}/\rho_\mathrm{eff}\) (late inverse) | \(2.80\times10^{-5}\) |

Matches FA3 parent within rounding.

---

## 4. Candidate outcomes (headline)

| ID | map | grade | lock? |
|---|---|---|---|
| C0 | \(\rho_\mathrm{re}=\rho_\mathrm{eff}\) | DEAD-as-law | no (~190× late) |
| C1 | \(\rho_\mathrm{re}=\rho_\mathrm{bounce}\) | WRONG-OBJECT | no |
| C2a/b | \(\rho\times n_\mathrm{late}\) | DEAD / WRONG-OBJECT | no |
| C3 | \(\rho_\mathrm{eff}/\mathrm{overshoot}\) | DEAD-as-law | no (O(1) only) |
| C4 | inverse \(\rho=3H_\mathrm{kin}^2 M_\mathrm{Pl}^2/(8\pi)\) | **TAUTOLOGY** | yes by definition |
| C5 | \(\rho_\mathrm{rad}\) door | DEAD-as-law | ~2× late (wrong object) |
| C6 | \(\rho_\mathrm{eff}\), \(\Theta=1\) optimistic | STILL-OPEN | 0.085 ≠ 1 |
| C7 | \(\rho_\mathrm{eff}\), \(\Theta=\Theta_\mathrm{lock}\) | **MISSING_INPUT** | would lock if Θ derived |
| C8a | M2 \(N_\mathrm{med}\) → MeV | **FABRICATED** | MeV dial |
| C8b | M2 \(N_\mathrm{med}\) → late lock | **FABRICATED** | lock dial |

**Legal LANDs: 0.**

---

## 5. What residual still forces

After exhaustive stocked maps:

1. **Derive \(\Theta_\mathrm{heal}\gtrsim 11.7\)** at re-entry from legal stress (beyond 0D/1D O(1) overshoot), **or**  
2. **Derive \(\rho_\mathrm{re}/\rho_\mathrm{eff}\sim (H_\mathrm{kin}/H_\mathrm{door})^2\)** without \(N_\mathrm{med}/\eta\) dial, **or**  
3. **Different matching rule** than \(H_\mathrm{kin}=H_F(\rho)\) that is still acoustic-legal → **N2 match-book**, not N1 alone.

None of (1)–(2) is stocked. (3) is the next construction door.

---

## 6. Grade stamp

| claim | grade |
|---|---|
| F-A2 closed from stocked parts | **false** |
| Obstruction C | **stands** |
| Bounce / exterior \(H_\mathrm{re}\) | **OPEN-BLOCKED** |
| P1+P2 | still CANDIDATE premises only |
| Cyclic | **not booked** |
| N1 package COMPLETE promotion | **0** |

> **One-line:** N1 F-A2 hunt — 0 lands; C stands; OPEN-BLOCKED.

---

## 7. Red ask

Fabrication / grade inflation / free-dial sold as land / bounce soft-close. Blue claims **0 COMPLETE**.
