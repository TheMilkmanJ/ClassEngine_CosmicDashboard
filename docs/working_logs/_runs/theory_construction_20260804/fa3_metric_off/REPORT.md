# F-A3 metric-off candidate path — theory construction (2026-08-04)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/fa3_metric_off/`  
**Grade (one-line):** **CANDIDATE / OPEN-BLOCKED residual path** — metric-off + expanding-branch re-entry is a **licensed premise**, not a Derived exterior \(H_\mathrm{re}\) from stocked stress alone.  
**Rule:** **NO FABRICATIONS.** Do **not** claim bounce closed. Do **not** book cyclic cosmology. Do **not** invent \(H_\mathrm{re}\) number from medium stress as Derived. No MCMC. No PolyChord. Strong CP **fenced** (bounce ≠ \(\bar\theta\)).

**Parents (read-only authority):**
- [`../../debt_bounce_FA3_20260803/REPORT.md`](../../debt_bounce_FA3_20260803/REPORT.md)
- [`../../bounce_full_freeze_20260804/REPORT.md`](../../bounce_full_freeze_20260804/REPORT.md)
- [`../../../../PRTOE_bigbang_no_singularity.md`](../../../../PRTOE_bigbang_no_singularity.md) residual freeze
- Script: [`../../../../../scripts/bounce_fa3_hcross_attempt.py`](../../../../../scripts/bounce_fa3_hcross_attempt.py)
- Reconfirm log (this package): [`bounce_fa3_hcross_attempt.log`](bounce_fa3_hcross_attempt.log)

**Sibling construction files:** [`CONSTRUCTION.md`](CONSTRUCTION.md) · [`CONSISTENCY.md`](CONSISTENCY.md) · [`KILL_AND_FALSIFIERS.md`](KILL_AND_FALSIFIERS.md) · [`EDITS.md`](EDITS.md)

---

## 1. Executive summary

debt_bounce_FA3 proved that exterior cosmological re-entry \(H_\mathrm{re}\) **cannot** be derived from stocked medium stress + continuous kinematic map under metric-ON FRW. The only remaining non-killed silhouette is **RP-A**: metric dissolves at healing length \(\xi\) (Phase II), fluid expansion \(\langle\Theta\rangle\) may reverse under gradient stress, and exterior FRW is re-attached **after** \(\langle\Theta\rangle>0\).

This package **does not close** that silhouette. It constructs the **honest candidate path** that residual freeze already named as the unstick option:

> Explicit **metric-off / branch declaration** left labeled reconstructed (not sold as NEC derivation).

Under that licensed premise, the expanding square-root (flat + shear-corrected form, matching [`CONSTRUCTION.md`](CONSTRUCTION.md) §1 — **DECLARATION not DERIVATION**)
\[
H_\mathrm{re}=+\sqrt{\frac{8\pi G\rho_\mathrm{re}}{3}\;+\;\frac{\sigma_\mathrm{re}^2}{3}}
\]
is the **branch choice at re-entry**, not a continuous exterior \(H:-\to0\to+\) trajectory computed through the non-metric interval. (If \(\sigma_\mathrm{re}=0\), this reduces to \(+\sqrt{8\pi G\rho_\mathrm{re}/3}\).) Magnitude lock and MeV hot start remain **OPEN**. Homogeneous FRW engines stay **DEAD**. Cyclic cosmology stays **not booked**.

---

## 2. Grade table

| item | grade | note |
|---|---|---|
| \(\rho_\mathrm{bounce}=m^4/\lambda\) floor | **PAID** (parent freeze) | Not re-derived here; not a turn engine |
| Homogeneous FRW bounce engines | **DEAD** (parent nogo) | Unchanged; not reopened |
| Medium \(\langle\Theta\rangle\) turn (toy/M6) | **PAID medium layer only** | Stress channel can reverse fluid expansion; not exterior FRW |
| Continuous exterior H-cross metric-ON | **KILLED** (obstruction A) | \(H=0\) at finite \(\rho\) conflicts Friedmann |
| Exterior \(H_\mathrm{re}\) from stress alone (no declaration) | **KILLED** (FA3) | `can_derive_H_re_without_declaration: false` |
| **Metric-off / branch declaration (this package)** | **CANDIDATE licensed premise** | Axiom choice with kill clauses — **not Derived** |
| \(H_\mathrm{re}\) as continuous exterior trajectory | **not claimed** | Exterior \(H\) does not exist in Phase II |
| Magnitude lock \(\|H_\mathrm{kin}\|=H_F(\rho_\mathrm{re})\) | **OPEN** (obstruction C / F-A2) | Factor \(c_s/\sqrt3\sim0.085\); late \(\Theta\) worse |
| MeV hot start over keV door (O6) | **OPEN-BLOCKED** | Residual still open; not closed by branch declaration |
| RP-A silhouette overall | **RECONSTRUCTED CANDIDATE** | Unchanged promotion status |
| O2 / F-A3 dynamical content | **PARTIAL** | Medium turn yes; exterior H-cross not derived |
| Classical turn residual | **OPEN-BLOCKED** | Residual freeze unchanged |
| Cyclic cosmology | **NOT BOOKED** | Explicit non-claim |
| Strong CP / \(\bar\theta\) as bounce | **FENCED OFF** | bounce ≠ Strong CP |

---

## 3. What this construction is (and is not)

### Is

1. A **precise statement** of the metric-off declaration as a **licensed premise** (see [`CONSTRUCTION.md`](CONSTRUCTION.md)).
2. A map of what \(H_\mathrm{re}\) means **if** metric-off is admitted: branch selection at acoustic re-emergence, not a continuous exterior Friedmann path through \(H=0\).
3. Consistency bookkeeping against existing nogos and FA3 compute ([`CONSISTENCY.md`](CONSISTENCY.md)).
4. Kill / promote clauses that keep the residual honest ([`KILL_AND_FALSIFIERS.md`](KILL_AND_FALSIFIERS.md)).

### Is not

1. **Derived** exterior \(H_\mathrm{re}\) from stocked medium stress alone.
2. A completed bounce profile or closed classical turn.
3. A booking of cyclic cosmology.
4. A fix of MeV-over-keV (O6) or F-A2 amplitude law.
5. A Strong CP mechanism.
6. A reopen of homogeneous CSW / dCDF / thermal / magnetic / vac+rad / DE-scale X / quartic engines.

---

## 4. Reconfirm compute (this package)

```text
OMP_NUM_THREADS=1 nice -n 19 python3 scripts/bounce_fa3_hcross_attempt.py
```

| field | value (2026-08-04 re-run) |
|---|---|
| exit | **0** |
| `can_derive_H_re_without_declaration` | **false** |
| `medium_Theta_turn` | **true** |
| `dTheta_dt_at_cross` | \(+10.56\) (primary \(n_0=6\)) |
| \(c_s\) | \(0.14796\) |
| \(H_\mathrm{door}\) | \(1.894\times10^{-21}\,\mathrm{eV}\) |
| \(\|H_\mathrm{kin}(\Theta=1,d=3)\|/H_\mathrm{door}\) | \(\approx0.0854\) |
| late \(\|H_\mathrm{kin}\|/H_\mathrm{door}\) (d=3) | \(\sim5.29\times10^{-3}\) |
| `grade_O2` | **PARTIAL** |
| `cyclic_cosmology` | **false** |
| obstruction | A + B + C |

Full capture: [`bounce_fa3_hcross_attempt.log`](bounce_fa3_hcross_attempt.log). Matches parent freeze FA3 key numbers within script numerics.

---

## 5. Kill conditions (summary)

| stance | dies if… |
|---|---|
| Metric-off premise as viable silhouette | metric remains ON and continuous through \(\xi\)-scale door **and** Friedmann holds with finite \(\rho\) at \(H=0\) without surface stress / modified constraint |
| Expanding-branch declaration as honest candidate | a derived continuous or Israel map forces \(H:-\to0\to+\) **without** branch choice (then declaration is obsolete — **promotion**, not kill of physics) **or** medium stress cannot produce \(\langle\Theta\rangle>0\) under legal GPE/averaging (then RP-A silhouette dies) |
| This package grade **CANDIDATE** | someone sells it as **Derived turn closed** without new premises — honesty kill |
| Floor paid (parent) | recorded \(m,\lambda\) / CSW seating fails |
| Homogeneous nogo table (parent) | new legal premises supply \(\rho_X+p_X<0\) dominating at max compression |

Full table + promotion ladder: [`KILL_AND_FALSIFIERS.md`](KILL_AND_FALSIFIERS.md).

---

## 6. Non-claims (absolute)

1. Bounce closed / classical turn paid / exterior \(H_\mathrm{re}\) Derived from stocked stress alone.
2. Cyclic cosmology booked (OEM or DERIVED).
3. Floor number = bounce dynamics.
4. Melt \(T=T_c\) = geometry turn.
5. Turnaround (\(H=0\), wrong \(\dot H\)) = bounce.
6. MeV hot start residual closed by this declaration.
7. Magnitude lock closed by this declaration.
8. Strong CP / \(\bar\theta\) identified with bounce.
9. Horizon inheritance resting only on the bounce as independent evidence of a derived turn.
10. Homogeneous engines reopened without new premises.
11. Invented negative-energy stiff \(X\) to fake FRW bounce.
12. Metric isometry of bounce to eternal white-hole spacetime.

---

## 7. Residual freeze alignment

Parent residual freeze already names the unstick path:

> Licensed stress+junction derivation **or** explicit metric-off / branch declaration with graded proof — **not** invent \(H_\mathrm{re}\).

This package is the **second arm**, graded as **CANDIDATE premise + OPEN-BLOCKED residual**, not as completion of the first arm. Living docs stay OPEN-BLOCKED; see [`EDITS.md`](EDITS.md) for surgical pointer only.

---

## 8. Audience one-liner

> The only path F-A3 left open is: admit metric-off at \(\xi\), let the medium turn \(\langle\Theta\rangle\), and re-attach expanding FRW by **declaration**. That is a licensed candidate premise with kill clauses — not a derived exterior Hubble cross, not a MeV hot start, and not a booked cycle.

---

## 9. Package contents

| file | role |
|---|---|
| `REPORT.md` | this executive summary + grade table |
| `CONSTRUCTION.md` | licensed premise, maps \(\xi\), metric end, \(H_\mathrm{re}\), FRW relation, MeV residual OPEN |
| `CONSISTENCY.md` | consistency with nogos + FA3 quotes |
| `KILL_AND_FALSIFIERS.md` | kill / promote ladder |
| `EDITS.md` | living-doc touch rules (surgical residual freeze pointer) |
| `bounce_fa3_hcross_attempt.log` | OMP=1 nice reconfirm |

*NO FABRICATIONS. Construction = CANDIDATE / OPEN-BLOCKED residual path. Bounce not closed.*
