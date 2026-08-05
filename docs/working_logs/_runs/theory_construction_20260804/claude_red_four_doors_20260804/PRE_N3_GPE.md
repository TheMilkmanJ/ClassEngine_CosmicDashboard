> **PROVENANCE:** background `claude -p` subagent (blue-launched), **not** interactive red seat. See `PROVENANCE.md`. Unverified until interactive red post-hoc.

# RED PRE-AUDIT — N3 production GPE late Θ vs Θ_lock

**Seat:** Claude (red) · **Date:** 2026-08-04 · **Mode:** pre-audit, fences only
**Target package:** `n3_gpe_late_theta_20260804` (not yet on disk at write time)
**Instrument:** `scripts/bounce_n3_gpe_late_theta.py` (1213 lines, untracked, written 16:17)
**Priors read:** `n3_theta_3d_20260804/` · `n1_fa2_amplitude_20260804/` · `fa3_metric_off/`

**Scope note (per my board block on pre-audit independence):** this file checks the
plan against fences red did not write, and names dead routes already in the ledger.
It does **not** propose mechanisms, targets, or routes. Where a question would
amount to red designing the physics, red says so and stops.

---

## 0. The target is an anchor, not a medium scale — verified

`THETA_LOCK_HUNT.md:13-18` defines

\[
\Theta_\mathrm{lock}=\frac{d}{c_s\sqrt3},\qquad c_s=\sqrt{3\alpha},\qquad d=3 .
\]

Red recomputed this independently. With \(\alpha=1/137.035999\):

| form | value |
|---|---|
| \(d/(c_s\sqrt3)\) | 11.706237610778283 |
| \(\sqrt3/c_s\) | 11.706237610778281 |
| \(1/\sqrt\alpha\) | 11.706237610778283 |
| \(\sqrt{137.035999}\) | 11.706237610778281 |

**At \(d=3\) the whole expression collapses to \(\alpha^{-1/2}\)** — the \(d\) and the
\(\sqrt3\) cancel exactly. This is consistent with the N1 F-A2 verdict already on
the board (Θ_lock graded not-derived, reciprocal of an anchor) and it is **not a new
finding** — it is restated here because it fixes what the GPE door can and cannot mean.

Consequence for this package:

- \(\Theta_\mathrm{lock}\) contains **zero medium content**. It is the ratio between the
  geometric door clock (\(H_\mathrm{door}=1/(\sqrt3\,\xi)\), set with \(c=1\),
  `CONSTRUCTION.md:27`) and the acoustic clock (\(t_0=\xi/c_s\), `CONSTRUCTION.md:74`).
- The GPE dynamics **never see α**. In `bounce_n3_gpe_late_theta.py`, `ALPHA` (line 49)
  and `C_S` (line 50) feed only `THETA_LOCK` (line 52) and `hkin_over_hdoor` (line 57–59)
  — i.e. the *comparison target*, not the evolution. Red checked line 59 against the
  definitions: `abs(Theta)*C_S*sqrt(3)/d` = \(\Theta c_s\sqrt3/d\), which is the correct
  \(|H_\mathrm{kin}|/H_\mathrm{door}\), and reproduces 0.085424 at \(\Theta=1\). **No bug.**

**Therefore:** a GPE run that "reaches 11.7" has reached a number supplied from outside
the simulation. That is not by itself illegal — S1 asks exactly for the medium to reach
an externally set bar — but it means **coincidence is not evidence**. If a late ⟨Θ⟩ lands
near 11.7, red's prior gets *more* suspicious, not less, and red will ask what in the run
carries the scale.

---

## 1. Pre-registered kill conditions

### K1 — max-over-scan inflation (highest probability failure)

`scan_0d_deep` (lines 209–234) is four axes:

| axis | line | rows |
|---|---|---|
| A: n0 × Θ0 at stocked (κ,γ) | 213–215 | 11 × 9 = 99 |
| B: κ × γ at stocked (6,−2) | 218–220 | 9 × 8 = 72 |
| C: "high-compression corner densification (prior best late region)" | 223–227 | 6 × 4 × 4 × 5 = 480 |
| D: corpus FA3 points × κγ | 230–233 | 5 × 4 × 4 = 80 |

≈ **731 rows before dedupe**, against the prior scan's **83** (`THETA_LOCK_HUNT.md:64`).
The headline S1 number is `max_late = max(...)` over physical rows (line 249).

**A maximum over a sample grows with sample size.** An ~8.8× larger grid will report a
larger `max_late_Theta` for sampling reasons alone, with no change in physics.

> **KILL:** quoting a new `max_late_Theta` against the prior **1.8005** as evidence of
> "deeper reach" is a **sampling artifact**, not a result. The only scan-size-independent
> comparator is the value at the **fixed stocked point** \((n_0,\Theta_0,\kappa,\gamma)=(6,-2,1.5,0.15)\),
> prior value **+0.0619** (`SCORECARD.md:18`, `THETA_LOCK_HUNT.md:79`).
> **Red will require the stocked-point number in any TASK COMPLETE.**

### K2 — boundary chase

Prior argmax for late Θ was \((n_0,\Theta_0,\kappa,\gamma)=(50,-5,3,0.05)\)
(`THETA_LOCK_HUNT.md:74`) against the prior grid \(n_0\in\{2..50\}\), \(\Theta_0\in[-0.5,-5]\),
\(\kappa\in[0.5,5]\), \(\gamma\in[0.05,0.5]\) (`THETA_LOCK_HUNT.md:38-41`).
**Three of four coordinates sat on the prior grid boundary.** The prior best *peak* row
(50, −5, 5, 0.05) sat on **four of four** (`THETA_LOCK_HUNT.md:77`).

The new grid extends precisely those edges: \(n_0\) 50→**80**, \(\Theta_0\) −5→**−8**,
\(\gamma\) 0.05→**0.02**. Axis C is labelled, in blue's own comment (line 223), as
densification of "prior best late region".

> **KILL:** if the new argmax again lies **on the boundary** of the extended box, the
> reported max is **not a bound on late Θ** and cannot be cited either as a reach
> (toward a land) or as a ceiling (toward an N6 kill). It is where the box stopped.
> **Red will require argmax coordinates printed for every headline late/settled number.**

Counter-note red owes blue for fairness: `PEAK_VS_LATE.md:16` records that the prior
0D scan *already* probed \((60,-8,5)\) and got late ≈ **0.033**. So extension into that
corner is not obviously monotone. Red is pre-registering the test, **not** predicting
the outcome.

### K3 — κ, γ as dials

`INSTRUMENT_INVENTORY.md:26` — κ, γ are "toy reduced, not Derived GPE coefficients".
`INSTRUMENT_INVENTORY.md:54` lists "free dial κ,γ to force late Θ~12" as a **fake land**.
`NON_CLAIMS.md:11` — "κ,γ **not** Derived cosmological constants".

> **KILL:** any late-Θ gain traceable to κ↑ or γ↓ relative to stocked (1.5, 0.15) is the
> forbidden dial, regardless of how many rows support it. Red will diff the winning
> row's (κ, γ) against stocked and grade accordingly.

### K4 — the UNEXPECTED-LATE-LOCK branch

Lines ~1070–1076 set `grade = "UNEXPECTED-LATE-LOCK"` and
`s1_status = "CLAIM-REVIEW-REQUIRED"` when `lock_late` fires.

**Red credits this design.** Blue routed a surprise into review rather than into a claim,
which is the correct instrument behaviour and red says so plainly.

> **KILL (still):** `lock_late` is driven by `max_late` over *all* physical rows (line 249).
> A single extreme-corner row can fire it. If UNEXPECTED-LATE-LOCK fires from a boundary
> row with non-stocked κ,γ, the correct disposition is **DIAL**, not land, not
> "unexpected result". Red will not accept "the instrument flagged it for review" as a
> substitute for grading it.

### K5 — weighting / vacuum-core contamination

The 1D log records `max_raw_local_Theta = 2909.30`, already excluded as vacuum-core
artifact (`INSTRUMENT_INVENTORY.md:54`, `NON_CLAIMS.md:9`, log `"max_raw_local_NOT_S1"`).
Blue's spherical readout (line 465) is \(\langle\partial_r v_r + 2v_r/r\rangle\) with
volume weight \(r^2\) — red checked, that is the correct spherical divergence, **no bug**.

> **AGREE-IF:** every headline late ⟨Θ⟩ is reported **both** mass-weighted and
> volume-weighted, with the density floor / support threshold stated. If mass-weighted
> greatly exceeds volume-weighted, the number is carried by a thin set of cells and red
> will treat it as the 2909 artifact class until blue shows otherwise.

### K6 — "production 3D" is hardcoded off

Line **1117**: `production_3d = False  # none of these instruments are full 3D production`.
Line **1241**: `assert summary["production_3d"] is False`.
(Prior draft cited 1079/1203 — **stale after script growth**; substance unchanged. Red CLI verify 2026-08-04.)
Section headers: [A] 0D, [B] 1D Cartesian, [C] spherical DST ("spherical symmetry ≠ full
3D", line 559), [D] 2D pancake, [E] synthetic averaging.

> **There is no 3D solver in this package.** The instrument **cannot** pay N3 production
> by construction. That is honest — but it means the package title "production GPE" is
> the loosest thing in the door.
> **DENIED** if TASK COMPLETE reads as "production A_Θ-3D delivered / instrument promoted".
> The truthful description is: **deepened 0D + 1D + spherical + 2D late-Θ metric**.
> `INSTRUMENT_INVENTORY.md:31` already grades full-3D GPE "**Not stocked**"; this package
> does not change that row.

### K7 — box, boundary and energy hygiene

The 1D late mean (+0.0013) is a **box average** over "outward shell + ambient"
(`THETA_LOCK_HUNT.md:134`). Spherical probe runs `L=120.0, N=2400` with Dirichlet
deviation \(w=u-r\) (lines 455–468).

> **AGREE-IF:** late ⟨Θ⟩ shown stable under (a) box size L, (b) grid N, (c) dt, and the
> boundary treatment named. An outward shell reaching or reflecting at the domain edge
> changes the late average directly; without an L-scan the late number is a property of
> the box. `dE_frac` (line 386) must be quoted per layer, as the 1D prior did (<5%).

---

## 2. Domain question — RED-Q1 (asked, not answered, and not donated)

Blue's own definitions give \(\Theta_\mathrm{phys}=\Theta_\mathrm{heal}\,c_s/\xi\)
(`CONSTRUCTION.md:74`), so \(\Theta_\mathrm{lock}\) corresponds to
\(\Theta_\mathrm{phys}=\sqrt3/\xi\) — **\(c_s\) cancels**, which is just the restatement
\(H_\mathrm{re}=H_\mathrm{door}\). For a volume average over a ball of radius \(R\),
the divergence theorem gives \(\langle\Theta\rangle = 3v_R/R\) exactly, hence
\(v_R = R/(\sqrt3\,\xi)\) in \(c=1\) units:

| R | required mean radial outflow \(v_R\) | Mach \(v_R/c_s\) |
|---|---|---|
| ξ | 0.577 c | 3.90 |
| √3 ξ (= R_H) | 1.000 c | 6.76 |
| 3 ξ | 1.732 c | 11.71 |
| 10 ξ | 5.774 c | 39.02 |

**The question to blue:** the re-entry gate requires \(\ell_\mathrm{grad}\gtrsim\xi\)
(`CONSTRUCTION.md:75,176`) and FRW attachment requires an averaging domain that is not
sub-healing. Over such a domain, is the required mean flow inside the domain of validity
of the instrument being used to look for it?

Red states the counter-evidence itself, so this is not one-sided: FA1's own table gives
\(v_g/c_s = 2.1213\) at \(x=2\) and \(v_g/c_s\) is **unbounded** at large \(x\)
(`bounce_israel_junction_inventory.py:91-92`, run output §5). A non-relativistic GPE has
no built-in \(c\) at all. So "faster than c" is not automatically illegal in the
substrate — but if the medium routinely exceeds \(c\), the seating that wrote
\(H_\mathrm{door}=1/(\sqrt3\xi)\) with \(c=1\) needs restating, and that is a framework
question, not a scan question.

> **Red does not answer this and does not hand it to N6.** Supplying an impossibility
> argument to the kill package would make red a co-author of the kill it must then grade.
> Per my board block: *that is a blue decision.* If N6 wants this line, N6 must derive
> and own it, and red will grade it as blue's work with no credit for having been asked.

---

## 3. Grade conditions when blue files TASK COMPLETE

| grade | conditions (all must hold) |
|---|---|
| **AGREE** | COMPLETE = 0 stated; `production_3d` false and **described as such** in prose; stocked-point late Θ quoted alongside any max; argmax coordinates printed; mass- and volume-weighted late ⟨Θ⟩ both reported; dE per layer; no κ,γ excursion sold as reach; Θ_lock explicitly re-stated as not-derived |
| **AGREE-IF** | Physics and numbers clean but ≥1 of: argmax coordinates missing · only max quoted without stocked point · single weighting reported · no L/N/dt sensitivity · package prose calls the deepened scan "production" |
| **DENIED** | Any of: late Θ ≥ Θ_lock banked as a land from a boundary/non-stocked-κγ row · "production A_Θ-3D COMPLETE" or N3 promoted · S1 moved off MISSING_INPUT without a *stocked-parameter* late lock · raw/local or support-Θ used as the S1 number · Θ_lock described as derived · larger max over larger grid presented as progress |

**Red's prior:** COMPLETE = 0, S1 stays MISSING_INPUT. Blue's own instrument asserts
this (line 1241). A land here would be surprising and surprise is the correct prior.

---

## 4. Non-claims of this red note

- Red has **not** predicted the scan outcome.
- Red has **not** proposed a mechanism, target, or route for N3.
- Red has **not** graded the package (it does not exist on disk at write time).
- Red found **no arithmetic bug** in lines 52, 57–59, 465 — those were checked and are correct.
- `exit 0` of the scan ≠ PASS. Delivered ≠ graded.

*NO FABRICATIONS. Pre-audit ≠ verdict.*
