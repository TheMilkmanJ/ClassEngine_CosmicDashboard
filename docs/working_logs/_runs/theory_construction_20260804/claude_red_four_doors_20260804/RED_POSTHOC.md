# RED POST-HOC — grades of the four landed blue door packages

**Seat:** Claude CLI (interactive red). **Date:** 2026-08-04.
**Authority:** owner instruction, direct — package write restored.
**Mode:** post-hoc grade only. Red did not design these doors and gave no design input before they landed.

**Everything below was recomputed or re-read from disk by this seat.** Where red ran the stocked instrument itself, the numbers are red's own output, not a quote of blue's log. No machine (MCMC) numbers are quoted. Chains untouched.

---

## 0. Grade board

| door | package | grade | binding cure |
|---|---|---|---|
| **1. GPE late-Θ** | `n3_gpe_late_theta_20260804/` | **AGREE-IF** | publish the late-window sensitivity with every headline late-⟨Θ⟩ |
| **2. Israel / junction** | `israel_junction_content_20260804/` | **AGREE-IF** | one Θ_lock on the board; label the content asserts as vacuous |
| **3. N6 kill-RP-A** | `n6_kill_rpa_20260804/` | **AGREE-IF** | refresh the stale +1.80 citation to +2.87 (verdicts re-checked, none move) |
| **4. Page D4 micro** | `page_d4_microphysics_20260804/` | **AGREE-IF** | fence the denominator-only lever, not just the ratio-sticky one |

**No door DENIED. No door unconditionally AGREE. Aggregate COMPLETE promotions: 0 — verified.**

---

## 1. Status of F1–F4 after this pass

| # | prior red status | status now | why |
|---|---|---|---|
| **F1** T8 S⋆ denominator unfenced | CONFIRMED | **CONFIRMED · disclosure cured · lever fence still OPEN** | D4 reports range and S⋆ separately (cure delivered); no package fences the raise-S⋆ move |
| **F2** N3 max-over-scan | substance CONFIRMED · citations WRONG | **CONFIRMED · fully cured** | :1117 / :1241 resolve; argmax + stocked point published |
| **F3** Israel asserts cannot fail | CONFIRMED verbatim | **CONFIRMED · scope sharpened** | content asserts vacuous; anchor asserts are real computations |
| **F4** N6 sign ≠ magnitude | condition CONFIRMED · data UNVERIFIED | **CONFIRMED in full — data now certified** | +1.8005 located and read from disk; red withdraws the non-certification |
| **F5** *(new)* N3 late-⟨Θ⟩ is a tail-window pick | — | **CONFIRMED, dt-robust** | see §2 |

**F4 correction, on red's own hand.** Red's CLI verification said it could not find `turn_paid_toy` or the `+1.8005` figure and did not certify them. They resolve: `n3_theta_3d_20260804/logs/n3_theta_lock_scan.log:20` and `:104`, and SUMMARY_JSON `"max_late_Theta_lock_metric": 1.8004818642857212`. Red certifies the datum. F4 is now confirmed end to end.

---

## 2. Door 1 — GPE late-Θ · **AGREE-IF**

### What red verified as correct

| check | result |
|---|---|
| Θ_lock = 3/(c_s√3) from the package's own c_s | red recomputes **11.706237653490552** — matches log to all digits |
| c_s = √(3α), α = 1/137.036 | confirmed at source: `bounce_fa1_transphononic_table.py:43` — `C_S = math.sqrt(3.0 / 137.036)` |
| Θ_lock = 1/√α exactly (d and √3 cancel) | holds — the door target carries **zero medium content** |
| late/lock = 0.24517440699940274 | red recomputes 2.870069874888626 / 11.706237653490552 — exact match |
| \|H_kin(Θ=1)\|/H_door = c_s/√3 = 1/Θ_lock | consistent to 9 figures |
| **F2 cure** — argmax coordinates published | **delivered** — REPORT §1, MASTER, LATE_THETA_SCORECARD all carry (80, −8, 3, 0.02) |
| **F2 cure** — fixed stocked point published | **delivered** — (6, −2, 1.5, 0.15) in all three |
| grid-wall honesty | **disclosed** — "best late sits on n₀ and γ grid edges" |
| peak ≠ S1 | **explicit** — max peak +14.76 carries late **−1.74**, stated |
| script self-fence | :1117 `production_3d = False`, :1241 `assert ... is False` — both resolve |
| 1D max-late restricted to energy-clean rows | **honest** — the larger +0.1333 row (dE 7.34%) is correctly excluded at the dE<5% cut |
| log ↔ SUMMARY_JSON consistency | clean; [B] 14 rows/9 clean, [C] 2 rows/0 clean, both match the JSON |

**F2 is fully cured. This is the most disclosure-compliant package on the board.**

### F5 — the headline is a tail-window pick (new, CONFIRMED)

`late_Theta` **is** `late_tail10` — the mean of the last 10% of the Θ history (`bounce_n3_gpe_late_theta.py:81`, assigned at `:184–185`, `:407`, `:578`), and the argmax at `:261`/`:263` ranks 710 rows by that statistic.

The package's own SUMMARY_JSON records, on the winning row:

| readout, same trajectory | value |
|---|---:|
| `late_tail10` → **the headline** | **+2.870069874888626** |
| `late_tail20` | **−0.13642625538239697** |
| `settled_std` | 1.2500898284797242 |
| `settled_last` | −1.1523377794660479 |

**The sign of the headline flips with the window.** Red re-ran the stocked ODE at the argmax point across five timesteps to separate window choice from integration error:

| dt | tail10 (headline metric) | tail20, same run | settled σ |
|---:|---:|---:|---:|
| 1.0e−3 *(as run)* | **+2.8701** | **−0.1364** | 3.226 |
| 5.0e−4 | +2.7864 | −0.1382 | 3.131 |
| 2.5e−4 | +2.7402 | −0.1416 | 3.086 |
| 1.0e−4 | +2.7167 | −0.1420 | 3.061 |
| 5.0e−5 | +2.7080 | −0.1425 | 3.052 |

Two things follow, and they cut opposite ways:

1. **The number is not a numerical artifact.** It converges — +2.87 → +2.708 under a 20× timestep refinement, ~5.7% high as reported. Red credits the headline as real. Blue's arithmetic is sound.
2. **But it is a window artifact.** At *every* timestep the tail-10% mean is ≈ +2.7 and the tail-20% mean on the identical trajectory is ≈ −0.14. The residual scatter (σ ≈ 3.05) is ~20× the magnitude of the settled mean. The solution is still oscillating; "late ⟨Θ⟩ = +2.87" is one window's slice of an unsettled ring-down.

This is F1's disease in a second location: a headline carried by a denominator there, by a window here. **It changes no verdict** — +2.87, +2.71 and −0.14 are all ≪ 11.71, and the honest reading is *worse* for the door, not better. That is why this is AGREE-IF and not DENIED.

### Second finding — the "scan-size independent" point is instrument-dependent

`n3_theta_3d` reported the stocked default (6, −2, 1.5, 0.15) at late = **+0.061929**. This package reports **+0.061225** for the same four parameters.

Red reproduced **both** from the current script by varying only the timestep:

| dt | red's recompute | matches |
|---:|---:|---|
| 5e−4 | **0.061929** | prior package exactly |
| 1e−3 | **0.061225** | this package exactly |
| 1e−4 | 0.062969 | (converged ≈ 0.0630) |

Cause identified by diffing `medium_rebound_0d` across the two scripts: **dt was doubled, 5e−4 → 1e−3**, alongside a new re-entry-cut and `hit_cap` break. **No fabrication** — both numbers are correct for their own instrument. But the point was published as "scan-size independent", and it moved 1.15% between packages under a silent instrument change. Scan-size independent is not run independent.

### Cures (binding for the next N3 filing)

1. **Every headline late-⟨Θ⟩ carries its window sensitivity**: publish `late_tail10`, `late_tail20` and `settled_std` together, in the forward-facing tables — not only buried in SUMMARY_JSON. A number whose sign depends on the window must show the window.
2. **Stamp the instrument with the stocked point**: dt and script sha256 beside (6, −2, 1.5, 0.15), so the fixed point is comparable across packages.
3. If a future filing claims a late-⟨Θ⟩ **increase** over a prior package, state which of grid / timestep / window changed. Here all three moved at once.

**Grade: AGREE-IF.** OPEN-BLOCKED · S1 MISSING_INPUT · production_3d false · COMPLETE 0 — all three verdicts stand under every window and timestep red tested.

---

## 3. Door 2 — Israel / junction content · **AGREE-IF**

### The package's real deliverable holds up

The door is an inventory, and red tested it the way F2 taught: **by resolving its citations**. Red spot-checked **20** `file:line` citations across `CORPUS_INVENTORY.md` and `KILL_TABLE.md`. **All 20 resolved to exactly the claimed content** — including the shear-corrected Friedmann at `bounce_m2_junction.py:64`, the door scale at `bounce_fa3_hcross_attempt.py:319–320`, the Θ_lock inversion at `:323–326`, obstruction A at `:264–271`, `can_derive_H_re_without_declaration: False` at `:407`, the M2 fabrication labels at `bounce_m2_junction.py:7,131`, the N_med retirement at `PRTOE_FAILURES_LEDGER.md:1237`, and the C8 FABRICATED label at `bounce_n1_fa2_amplitude_hunt.py:31,264`.

**Red states this plainly: the inventory is verifiable, and that is the whole product.** "Zero stocked Israel S_ab" is an earned finding, not an assertion.

`CANDIDATE_ISRAEL.md` is correctly graded — CANDIDATE formalization of a MISSING_INPUT, with explicit non-promotions and a promotion condition that reports **none of (1)–(4) stocked**. No land invented. S-A/S-B/S-C/S-D are shapes, and are labelled as shapes.

### F3 re-confirmed, with the scope sharpened

`bounce_israel_junction_inventory.py:216–221` assigns six literals; `:228–233` asserts those same six literals; `:252` asserts a count that was itself assigned. **These cannot fail.**

Red now draws the line more precisely than the original F3, in the package's favour on one side and against it on the other:

| assert class | lines | verdict |
|---|---|---|
| **anchor / physics asserts** | :169 (obstruction A, computed), :179–180, :190–191, :255–258 | **real** — these test computed quantities and could fail |
| **Israel-content honesty flags** | :216–221 → :228–233, :252 | **vacuous** — literal compared to itself |

The vacuous block is exactly the block the door is named for. `exit 0` from this script certifies the *anchors*, and certifies nothing whatever about Israel physics. The package's own log line 4 says so ("exit 0 = compute done; NOT physics PASS"), and the honest content is an inventory of absence — a legitimate thing to file. The label should just say which asserts are which.

`:210` — `assert 0.8 < ratio_vs_1cs < 1.0`, value 0.9150 — still present. A hardcoded band on a ratio built from the *fabricated* N_med path is a latent dial: if an anchor moves, the script crashes, and the cheapest repair is to move the anchor back. Unchanged from F3.

### New — two Θ_lock values are now on the board

| package | Θ_lock quoted | c_s in its own JSON |
|---|---:|---|
| `n3_gpe_late_theta` | 11.706237653490552 | 0.14795964842319909 |
| `israel_junction_content` | **11.706279802864074** | 0.14795964842319909 |

**Same c_s, different Θ_lock.** Cause found at `bounce_israel_junction_inventory.py:139`: `Theta_lock_d3 = H_door * 3.0 * xi / C_S` routes through the numerically-obtained `H_door` (1.8943916024168856e-21) instead of the analytic `H_shear = 1/(√3 ξ)` (1.894385e-21). The script prints both side by side at log lines 9–10 and they differ by ~3.7×10⁻⁶ relative. The consistency assert at `:255` passes at 3.08×10⁻⁷ — within a third of its 1e−6 tolerance.

**Immaterial to every conclusion in the package** — all of them are order-of-magnitude statements. But Θ_lock is exactly α^(−1/2); it is not a quantity that should have two values on one board, and the second one is drifting toward its own assert's tolerance.

### Cures

1. **One Θ_lock.** Compute it as 1/√α (or from a single door definition) so the board carries one number for an exact identity.
2. **Label the assert classes** in the script docstring and in `KILL_TABLE.md §5`: which asserts test computed quantities, which are honesty literals. An `exit 0` reader should not have to diff the source to learn that the Israel flags are self-comparisons.
3. Replace `:210`'s hardcoded band with a printed sensitivity, or state in-line that a crash there means *the anchor moved*, not *the physics failed*.

**Grade: AGREE-IF.** MISSING_INPUT N4 · 0 S_ab · bounce not closed · 0 lands — all stand, and the inventory that supports them is verifiable.

---

## 4. Door 3 — N6 kill-RP-A · **AGREE-IF**

### The F4 distinction is correctly applied

This was red's live concern, and the package handles it right. K1 is a **sign** condition — "legal GPE/averaging **cannot** produce ⟨Θ⟩>0". N6 grades it NOT_FIRED precisely because stocked toys *do* turn, and separates magnitude as a different object: `EVIDENCE_LEDGER` E-K1-d reads "magnitude, not gate existence", and `K1_K2_K3.md §K1 Score` says the open items are production instrument and late magnitude, "neither is a proof that ⟨Θ⟩ cannot go positive."

That is F4's point, made by blue, without red handing it over. Red agrees with the disposition.

The "beyond toys" hazard red flagged is also handled: K1's *what would fire next* requires the toys be shown **illegal** under framework GPE — i.e. it refuses to let a universal over unstocked instruments be established by absence.

### Citations red resolved

| N6 claim | resolves to |
|---|---|
| max late Θ (N3) = **+1.80** | `n3_theta_3d_20260804/logs/n3_theta_lock_scan.log:20,104`; JSON 1.8004818642857212 ✓ |
| stocked 0D late Θ = **+0.0619** | same log `:177` — 0.061928525036595815 ✓ **and independently reproduced by red** at dt=5e−4 |
| N1 **0 / 11** maps | `n1_fa2_amplitude_20260804/MASTER.md:9` ✓ |
| S2 **0 / 16** candidates | `s2_rho_suppression_20260804/MASTER.md:9` ✓ |
| S_need late 2.80e−5 · Θ=1 7.30e−3 | S2 MASTER `:12–13`; and 7.30e−3 = (c_s/√3)² checks out ✓ |
| `medium_Theta_turn: true` | `bounce_fa3_hcross_attempt.py:408` — **`bool(medium_turn)`, a computed flag** ✓ |

That last row matters. N6's central against-K1 evidence rests on a **computation**, not on a declaration — materially unlike the Israel honesty-flag block. Red notes for the record that `:407` `can_derive_H_re_without_declaration: False` *is* a hardcoded literal; N6 cites it but its negative ledger already refuses "can_derive=false ⇒ kill RP-A". Correct handling of a declaration.

### The defect — a stale input, and what red did about it

N6 cites **max late Θ = +1.80** in four places (REPORT §3, EVIDENCE_LEDGER §2 and E-K1-d, K1_K2_K3 K1 and K3 tables). The GPE deepen filed after it supersedes this with **+2.87** (0.245× of lock, against the prior 0.154×).

Per the standing rule — re-grade the conclusion at the corrected input, do not just fix the number — red re-checked each criterion at +2.87 rather than only editing the citation:

| K | direction of the change | verdict at +2.87 |
|---|---|---|
| **K1** | a *larger* turn weakens "cannot produce ⟨Θ⟩>0" further | **NOT_FIRED** — strengthened |
| **K2** | no Θ input; K2 is about branch sign, not amplitude | **NOT_FIRED** — untouched |
| **K3** | 2.87 still ≪ 11.71; pressure unchanged, no class proof gained | **NOT_FIRED** — unchanged |

**No verdict moves.** And red notes the honest reading of §2 above (tail-20 negative) would not move them either. This is a citation refresh, not a re-grade.

### Cures

1. Refresh the four `+1.80` citations to **+2.87** with the source package named, and record 0.245× of lock.
2. State the currency rule in the ledger: N6 is a disposition over parent packages, so it must name the parent *version* it scored. A disposition that outlives its inputs silently is the failure mode here.

**Grade: AGREE-IF.** NOT_FIRED · none of K1–K3 fired · residual OPEN-BLOCKED · RP-A RECONSTRUCTED CANDIDATE — all correct, and correct for the right reasons.

---

## 5. Door 4 — Page D4 microphysics · **AGREE-IF**

### Provenance — red recomputed the hashes

| stamp | package claims | red's own `sha256sum` |
|---|---|---|
| `input_sha256` | `048de43e1bc766c8…` | **048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8** ✓ |
| `tool_sha256` | `06bd9661be39d1ff…` | **06bd9661be39d1ffb0479898a2c0d6e444c45d7b0d127fcfc2abd903c460a390** ✓ |

Both match. Every T8 number in `SCORECARD.md` matches the recompute JSON on disk exactly: S_range 0.0018883423986319587, S⋆ 0.016688199517780646, ratio 0.11315435176934464, threshold 0.0016688199517780646, 83 occupied bins, 1 failing, worst bin [0.10, 0.11) with n=12.

`page_curve_claimed: false` in the log, in the JSON, and in every package file. `CANDIDATE_TURN_binding: False`. No CANDIDATE packet. Zero densify, zero coevolve production — confirmed; the only write is the arrays-only recompute.

### F1's disclosure cure is delivered — and one under-claim corrected in blue's favour

`SCORECARD.md` reports the in-bin S range, S⋆, and the threshold as **three separate rows**. That is exactly what F1 demanded of any T8 filing. Credit.

`SCORECARD.md` marks stall / co_frac / swap / peak as "(as in freeze snapshot; binding stack intact)", which reads like a citation. It is not: those gates were **recomputed in this run** and sit in the recompute JSON's `coevolution_gates` — stall 10/10 ok, `frac_S_rise_while_u_advances` 0.9999521029263491, `swap_back_max_u_minus_v` 1.504836142332544e−05, `peak_in_motion` true. The package under-claims its own work. Not a defect; the record should be right.

### F1's *lever* fence is still open — the one real gap

The kill boards fence the numerator side and the protocol side thoroughly. `DEAD_DENIFY.md §2` kills G_TMS scans, TMS shape/delay grids, BS_MILD/G_BS grids, late EXTRA_BS, and coarse sampling; `§4` kills soft-passing 0.113, widening Δu, and bin subsampling. `D4_LEVER_MAP.md:91` fences the ratio-sticky case — "pure G_TMS rescale scales ΔS **and** S⋆ together".

**Every one of those fences covers levers that move numerator and denominator together, or that touch the failing bin.** None covers the complement: a lever that raises **S⋆ alone**.

Red recomputed the size of the opening:

| quantity | value |
|---|---:|
| failing-bin absolute S range | 0.0018883423986319587 |
| current S⋆ | 0.016688199517780646 |
| S⋆ required for T8 to pass | 0.018883423986319585 |
| **required increase in S⋆** | **+13.1544%** |
| peak location u* | 0.26697 |
| failing bin | [0.10, 0.11) |

The peak and the failing bin are **disjoint regions of the trajectory**. Raising the midband peak by 13.15% clears T8 **with the failing bin untouched** — the numerator never moves, and the test passes because the denominator did. It is gate-silent because every other test rewards a larger midband peak: it helps T3, preserves T1, and does not touch T2's reach.

No R1–R7 "should-not-exist" list names this move. R1 forbids "free dump dial to 0.10", R2 forbids G_TMS retune sold as law, R5 forbids "two free knobs in a trenchcoat" — all numerator-side.

**In fairness: T8 fails in this package, so no fake pass was banked here.** The hole is prospective. It bites the first filing that claims `T8_pass`.

### Cures

1. **Add the denominator-only lever to `DEAD_DENIFY.md`** as a named dead lane: *raising S⋆ without lowering the absolute early-bin range is a fake pass.*
2. **Extend each R1–R7 "should-not-exist" row** to include "raises S_peak without reducing the [0.10, 0.11) absolute range" — the fence must cover the complement of ratio-sticky, not only ratio-sticky.
3. **Binding on any future `T8_pass`:** report the absolute early-bin range **and** S⋆, each against v13, and state which one moved. Already satisfied in format by this package's SCORECARD; make it a protocol row rather than a habit.

**Grade: AGREE-IF.** T8 FAIL 0.113154… · 0 lands · claim false · densify dead · D4 active — all verified against the artifact and the tool by hash.

---

## 6. What red did not do

Red graded four packages post-hoc. Red did **not** design any door, did not supply N6 its impossibility argument, did not run any coevolve or MCMC, did not touch chains, and did not edit any living `docs/PRTOE_*.md` — no final-product fact error was found in this pass. Red ran one stocked instrument (`bounce_n3_gpe_late_theta.medium_rebound_0d`) as a timestep-convergence and window check, and reports that output as red's own.

`exit 0 ≠ PASS`. Four AGREE-IF is not four lands. **Aggregate COMPLETE promotions this wave: 0.**

*NO FABRICATIONS.*
