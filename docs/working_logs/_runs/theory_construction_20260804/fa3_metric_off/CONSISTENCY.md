# Consistency with existing nogos and F-A3 compute

**Package:** `docs/working_logs/_runs/theory_construction_20260804/fa3_metric_off/`  
**Rule:** This candidate path must **not** reopen dead engines or contradict FA3’s obstruction stack.

---

## 1. Debt_bounce_FA3 conclusions (quoted)

From [`../../debt_bounce_FA3_20260803/REPORT.md`](../../debt_bounce_FA3_20260803/REPORT.md):

### Answer

> **No.** There is no formula that yields a derived exterior \(H_\mathrm{re}\) from stocked medium stress + written junction without a branch / metric-off declaration. O2 remains **PARTIAL**.

### Obstruction A (metric-ON)

> **Metric-ON exterior cannot pass through \(H=0\) at finite \(\rho\)** without modified constraint, vanishing \(\rho_\mathrm{tot}\), or a surface layer. Homogeneous higher-order / quartic routes already dead (`bounce_m8_ledger_quartic.py`).

### Obstruction B (metric-off = declaration)

> Medium stress derives the **fluid** turn; it does not compute an exterior \(H(t)\) trajectory through zero, because exterior \(H\) does not exist in Phase II. That re-attachment rule is exactly the reconstructed F-A3 declaration — not a NEC derivation and not a continuous exterior cross.

### Obstruction C (magnitude)

> Matching \(|H_\mathrm{kin}|=H_F(\rho)\) needs either \(\Theta_\mathrm{heal}\gtrsim d/(c_s\sqrt3)\sim12\) (not produced by verified 1D O(1) overshoot) or \(\rho_\mathrm{re}\) suppressed by \(\sim10^{4}\)–\(10^{5}\) vs door \(\rho_\mathrm{eff}\). No legal junction / F-A2 amplitude law closes this.

### Grade stamp (FA3)

> **F-A3 remains a branch declaration.** Continuous kinematic map \(H=\langle\Theta\rangle/d\) turns the fluid, not the exterior metric: metric-ON Friedmann forbids \(H=0\) at finite \(\rho\); metric-OFF re-entry *is* the declaration. Magnitude lock fails at the \(c_s/\sqrt3\sim0.085\) factor and late-\(\Theta\) damping. **Do not book cyclic cosmology.**

### Audience one-liner (FA3)

> The medium can reverse its expansion rate via gradient stress; that does not derive an exterior cosmological \(H:-\to0\to+\) without either violating Friedmann at finite density or re-declaring the expanding branch when the metric returns.

**This package’s alignment:** we **accept** B as the licensed premise (explicit declaration), we **do not** claim A is solved continuously, and we **leave C OPEN**. That is consistency, not a close.

---

## 2. Reconfirm compute (this package + parent freeze)

Script: `scripts/bounce_fa3_hcross_attempt.py`  
Log: [`bounce_fa3_hcross_attempt.log`](bounce_fa3_hcross_attempt.log)

| assertion / field | required | reconfirm |
|---|---|---|
| medium \(\Theta\) turn | true | **true** |
| \(\mathrm{d}\Theta/\mathrm{d}t\big|_{\mathrm{cross}}>0\) | true | **+10.56** (primary) |
| Friedmann OK at \(H_\mathrm{kin}=0\) finite \(\rho\) | false | **false** |
| `can_derive_H_re_without_declaration` | false | **false** |
| `grade_O2` | PARTIAL | **PARTIAL** |
| `cyclic_cosmology` | false | **false** |
| obstruction string includes metric-off branch | yes | A + B + C |

**Interpretation for construction:** the script’s “PASS path not reached” is **expected**. This package does not re-run a derivation claim; it **books** the branch declaration as the residual path FA3 already named, at CANDIDATE grade.

---

## 3. Consistency with homogeneous FRW nogo stack (DEAD engines)

From bounce_full_freeze / debt_bounce (unchanged by metric-off declaration):

| engine | grade | why metric-off path does not revive it |
|---|---|---|
| CSW floor as FRW min-\(a(t)\) | **DEAD** | Floor is density ceiling; polytrope \(p\sim\rho\) keeps \(\rho+p>0\). Metric-off is **not** a homogeneous FRW bounce. |
| Live barotropic dCDF as turn | **DEAD** | Floor ⇒ \(\dot H=0\) coast in FRW. Phase II is non-FRW medium, not dCDF FRW engine. |
| Thermal \(T=T_c\) as bounce | **DEAD** | Melt threshold ≠ geometry turn; unchanged. |
| Magnetic polarity flip | **DEAD** | \(T(B)=T(-B)\); NEC≥0; unchanged. |
| Vac+rad \(H=0\) | **DEAD** | Turnaround wrong \(\dot H\) sign; metric-off does not make bare+rad bounce. |
| DE-scale / stocked exotic \(X\) | **DEAD** | Prefer kill over fabrication; this path invents **no** \(X\). |
| Quartic / higher-order FRW ledger | **DEAD** | QP vanishes in FRW; standard \(H^2\) returns. Metric-off is exit from FRW, not quartic FRW. |
| Rotation alone as BKL-stiff \(w\ge1\) | **DEAD** (analytic) | Unchanged; not used as turn engine here. |

**Rule preserved:** metric-off is an **exit from the FRW arena**, not a homogeneous legal-parts bounce. Nogo scripts remain authoritative for metric-ON engines.

---

## 4. Consistency with bounce_full_freeze residual freeze

From [`../../bounce_full_freeze_20260804/REPORT.md`](../../bounce_full_freeze_20260804/REPORT.md) §7 (what would unstick OPEN-BLOCKED):

> 1. Licensed continuous or Israel junction map … **without** hand-picking the expanding square root; **or**  
> 2. Explicit, graded **metric-off / branch declaration** left labeled reconstructed (not sold as NEC derivation); **or**  
> 3. Prefer **kill** of RP-A if every legal GPE/averaging stress cannot produce exterior turn.

**This package implements option (2) only**, labeled reconstructed / CANDIDATE, not NEC derivation. Option (1) remains unstocked. Option (3) not triggered (medium turn stands at toy layer).

Forbidden claims list in freeze §4 remains fully in force (see REPORT.md non-claims).

---

## 5. Consistency with bigbang residual freeze

From [`../../../../PRTOE_bigbang_no_singularity.md`](../../../../PRTOE_bigbang_no_singularity.md) residual freeze:

| residual | freeze grade | this package |
|---|---|---|
| Classical turn / H_re sign | **OPEN-BLOCKED** | **stays OPEN-BLOCKED** — declaration does not complete residual |
| Homogeneous FRW engines | **failed / retired** | **unchanged DEAD** |
| Unstick language | “licensed stress+junction **or** explicit metric-off / branch declaration with graded proof — **not** invent \(H_\mathrm{re}\)” | we supply graded **declaration**, not invented continuous \(H_\mathrm{re}\) number |

**Ledger row 3 forbidden:** desk-derive \(H_\mathrm{re}\); book cyclic cosmology; claim “bounce closed” — **all respected**.

---

## 6. Consistency with RP-A / promotion scorecard

| ID | parent | this package |
|---|---|---|
| O1 finite density | PASS | untouched |
| O2 turn | PARTIAL (medium yes; H_re declared) | still PARTIAL; declaration made **explicit and graded**, not promoted |
| O3 not live dCDF | PASS | untouched |
| O4 not CSW-as-FRW | PASS | untouched |
| O5 not \(T=T_c\) | PASS | untouched |
| O6 MeV hot start | FAIL / OPEN-BLOCKED | **still OPEN** (sign ≠ temperature) |
| O7 BKL | PARTIAL | untouched |
| O8 no local WH engine | PASS | untouched |
| RP-A overall | RECONSTRUCTED CANDIDATE | **unchanged** |

---

## 7. Strong CP fence

bounce_full_freeze: reverse/bounce **is not** Strong CP; keep silence toward `PRTOE_strong_cp.md`.

**This package:** zero Strong CP content; no \(\bar\theta\) seating; no claim that metric-off re-entry solves CP.

---

## 8. Cyclic cosmology non-booking

FA3 and freeze: **not booked**.  
Metric-off + expanding re-entry is a **local matching rule for one turn silhouette**, not a past-eternal or closed cycle theorem. Tolman / chain / Kibble residuals remain OPEN interpretation / estimate per bigbang freeze.

---

## 9. Consistency verdict

| check | result |
|---|---|
| Contradicts FA3 “cannot derive without declaration”? | **No** — we *are* the declaration arm |
| Claims Derived \(H_\mathrm{re}\) from stress alone? | **No** |
| Reopens homogeneous DEAD engines? | **No** |
| Closes MeV residual? | **No** (left OPEN) |
| Closes magnitude lock? | **No** (left OPEN) |
| Books cyclic cosmology? | **No** |
| Touches Strong CP? | **No** |
| Changes residual freeze COMPLETE? | **No** (OPEN-BLOCKED preserved) |

**Verdict:** construction is **consistent** with stocked nogos and FA3. Grade remains **CANDIDATE / OPEN-BLOCKED residual path**.
