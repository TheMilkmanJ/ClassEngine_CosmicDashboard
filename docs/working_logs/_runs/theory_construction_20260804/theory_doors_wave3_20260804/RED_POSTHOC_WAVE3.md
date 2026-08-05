# RED post-hoc — theory doors wave 3 (2026-08-04)

**Seat:** Claude RED (interactive CLI). **Mode:** post-hoc verification of a delivered wave — no design input.
**Packages graded:** `settled_late_theta_20260804` · `israel_sab_construction_20260804` · `n4_force_branch_20260804` · `o6_mev_residual_20260804`
**Master:** `theory_doors_wave3_20260804/MASTER.md`

**Result: 4 AGREE-IF · 0 DENIED · aggregate COMPLETE 0 confirmed.**
No free dial banked as land · no force-branch smuggled as P2 · no MeV dial · settled/peak separation held · no grade inflation.

---

## 0. What this seat ran

| check | method | outcome |
|---|---|---|
| settled scan headline rows | **independent re-implementation** of the stocked 0D form (not blue's code), Euler dt=1e-3 | **4/4 rows reproduce to 6 s.f.** |
| settled grid size / argmax boundary status | loaded `build_grid()` directly | 710 unique rows confirmed; argmax **not** at global κ or γ boundary |
| script identity | `sha256sum scripts/bounce_settled_late_theta_scan.py` | `950d68ac…271fe380` — matches MASTER and summary.json |
| O6 arithmetic | independent recompute of every quoted gap, N_med, clock | **all reproduce** |
| Israel σ atoms | recompute of C1/C1b/C2/C3/C6/C7 and ratios to σ_G | all reproduce |
| N4 FA3 reconfirm | read script — is it a real subprocess? | **yes**, real `subprocess.run` on `bounce_fa3_hcross_attempt.py` with parsed JSON assert |
| living-doc contamination | grep `PRTOE_*.md` for demoted numbers | **clean** — no fact error, no edit made |

### Reproduction table (this seat's own integrator)

| row | (n₀,Θ₀,κ,γ) | blue settled_mean | RED settled_mean |
|---|---|---:|---:|
| argmax quality se40 | (3,−1,1.0,0.05) | +0.043582 | **+0.043582** |
| stocked default se40 | (6,−2,1.5,0.15) | −0.003680 | **−0.003680** |
| prior F5 row se40 | (80,−8,3.0,0.02) | −0.058221 | **−0.058221** |
| argmax all-phys se40 | (6,−2,1.0,0.02) | +0.105600 | **+0.105600** |

---

## 1. Grades

| door | grade | binding condition |
|---|---|---|
| **Settled late-Θ (F5)** | **AGREE-IF** | §5.1 claims more than the linearization delivers — cure below is one line and makes the result *stronger* |
| **Israel S_ab construction** | **AGREE-IF** | survivors' shared next-input `K_ab^±` is forbidden by the package's own P1 domain; C6 stated three inconsistent ways |
| **N4 force-branch** | **AGREE-IF** | `obstruction_A` stamp cannot fail and is presented as an expected/observed check — the sibling package in this same wave already labels this class `[VACUOUS]` |
| **O6 MeV residual** | **AGREE-IF** | the −2.62 leg of the headline sign conflict rests on the very window this wave's own settled package demoted; nobody cross-referenced |

---

## 2. Settled late-Θ — AGREE-IF (strongest package in the wave)

**Confirmed.** Every headline number reproduces from an independent integrator. The F5 residual is closed correctly: `late_tail10 = +2.870` and `late_tail20 = −0.136` are the *same run* and the sign is window-choice; `S1_settled` supersedes it; max quality settled `+0.0436` is `3.72×10⁻³` of `Θ_lock = 11.706`. Ring-down ladders reproduce. `production_3d = false` held. κ,γ scanned but **no land claimed from the scan** — the ceiling is +0.044, four orders under lock, so there is no dial to bank.

**The condition.** §5.1 says *"Therefore settled_mean → 0 as t→∞ … There is **no** non-zero late attractor."* A linearization about (1,0) proves **local** asymptotic stability. It does not exclude a distant limit cycle or a second attractor, and `Re(λ) = −γ/2` holds only in the underdamped branch (true everywhere on *this* grid — min κ = 0.25 needs γ > 1.0 to overdamp, max γ = 0.5 — but the sentence is written unconditionally).

**Cure — one line, and it is strictly better than what is there.** The stocked form gives an *exact* identity, no linearization required:

  ṅ = −nΘ  ⇒  Θ = −d(ln n)/dt  ⇒  ⟨Θ⟩ over [t₁,t₂] = [ln n(t₁) − ln n(t₂)] / (t₂−t₁)

The window mean of Θ is **exactly** the log-density drop across the window divided by its length — for any κ, γ, any initial condition, on or off grid. This seat verified it against all four headline rows (agreement to ~0.1%, pure Euler discretization). Two consequences the package should bank:

1. **The lock claim becomes grid-independent.** To read `settled_mean = 11.706` over the observed ~9.7-time-unit window, n must fall by `e^113.6 ≈ 10^49.3` *inside the window*. No grid extension, no κ,γ corner, no settle_extra reaches it. This kills the boundary-argmax objection outright rather than answering it with a scan.
2. **It reframes what the positive maxima are.** The argmax quality row's `settled_mean = +0.0436` corresponds to n still falling ~34% across the "settled" window — the quality cut gates `settled_std` on Θ only, never on n. The positive residuals are measuring leftover density drift, not a late attractor. That reading costs the package nothing and is more honest than the current one.

Grade lifts on inserting the identity (and scoping `Re(λ) = −γ/2` to underdamped, or dropping it for Routh–Hurwitz).

---

## 3. Israel S_ab — AGREE-IF

**Confirmed.** 12 candidates written, 5 survivor schemas, 0 lands, Israel equations still 0. Every σ atom reproduces. The force-branch attempt in `CANDIDATE_SAB.md` §3 is **correct GR**: granting a fixed `S_ab`, a one-sided Israel condition constrains combinations of `K_ab`; exterior Friedmann still supplies `H_re = ±√(·)`; the pair (normal orientation ε, sign H) keeps a discrete freedom absent a separate theorem. C7's self-flag — *"using sign(Θ) **is** P2 smuggled into σ_s"* — is the exact trap and the package sets it itself. C4 back-solve killed, C5 free α killed, C10 M2 dials killed. **No smuggle.**

The `[VACUOUS]` labelling in this package's script and log is the right standard and this seat credits it: stamps that mirror the package's own conclusions are marked as such in-source, and the one real computation (`H_F > 0` at ρ_eff) is separated out. That is the discipline the other package in this wave is missing (§4).

**Condition 1 — the survivors ask for an object P1 forbids.** `CANDIDATE_SAB.md` §0 writes the target as the standard two-sided junction `[K_ab] − [K]h_ab = −8πG S_ab`, and `SURVIVORS.md` gives every survivor a shared **M1: embedding K_ab^± of Σ**. Under P1 there is no metric on the Phase-II side, so `K^-` does not exist — which the package itself asserts elsewhere (G4, FB19 `ILL_POSED`, C11 `DEAD under P1+A`). As written, SV1–SV5 each point the next wave at a quantity the premise set rules out. Cure: state the target under P1 as a **one-sided boundary condition** with the missing side replaced by a prescribed medium object, and rewrite M1 accordingly — or mark M1 explicitly unobtainable under P1 and say what replaces it. This is not a grade change (still 0 lands); it is stopping a future wave from chasing `K^-`.

**Condition 2 — C6 is stated three ways.** `CANDIDATE_SAB.md` C6 writes `σ_s^(6) = M_Pl²H_door/√3` *"(or M_Pl²/ξ — equivalent under shear-dom door)"*. With `H_door = 1/(√3 ξ)`: `M_Pl²H_door/√3 = M_Pl²/(3ξ)`, while `M_Pl²/ξ = √3·M_Pl²H_door`. Those differ by **3×**, so the parenthetical identity is false. The script computes `C6_Mpl2_H_door = 2.8237e35` and `C6b_Mpl2_over_xi = 4.8908e35` (ratio √3, correct), and `REPORT.md` §6 tabulates C6 at ratio **1**, i.e. `M_Pl²H_door` — a third form, matching neither expression in the candidate file. C6 is a wrong-object atom so nothing physical turns on it; a stated identity that is off by 3 in a construction board is still worth one edit.

---

## 4. N4 force-branch — AGREE-IF

**Confirmed.** The FA3 reconfirm is **real** — an actual subprocess run of `bounce_fa3_hcross_attempt.py` with the returned JSON parsed and asserted, plus a cross-check that `H_kin/H_door` matches `c_s/√3` to 1e−9. `FORCE_BRANCH_DERIVED = false`, `NAMED_THEOREM_STOCKED = false`, `P2_is_declaration = true`. The FB1–FB20 table is sound argument-by-argument; FB15 (NEC does not force expansion — contracting FRW at finite ρ is NEC-compatible) and FB16 (Darmois `h_ab` continuity does not fix the sign of a square root) are both correct and are the two a careless seat would get wrong. The three named promotion forms T-N4-Israel / -Acoustic / -Dual are labelled **"Not claimed present"**. Kill-seek is not sold as theorem anywhere. **P2 stays a declaration.**

**The condition — a wave-2 finding recurring.** `algebraic_obstruction_A_stamp()` hardcodes `rho_finite = True` and `H_at_cross_kin = 0.0`, then returns `"obstruction_A_stands": True` as a literal. `continuous_exterior_path_legal = not (0.0 == 0.0 and True)` is False by construction. It cannot fail. `ARGUMENT_KILL_TABLE.md` §6 then presents it in an **"assert | expected | observed"** table — a format that reads as a test that could have come out otherwise. Same for the `n_force == 0` assert over a hand-written list.

This is the F3 pattern this seat confirmed verbatim in wave 2. What makes it a condition rather than a repeat nit: **the sibling package in this same wave already fixed it.** `bounce_israel_sab_dimensions.py` prints `[VACUOUS stamp]` next to exactly this class of line, says in-source *"cannot fail as physics tests; earned content is CANDIDATE_SAB.md §3"*, and logs *"exit0 on vacuous stamps ≠ Israel physics PASS; package md is the product."* One wave, two seats, two standards. Cure: adopt the `[VACUOUS]` label in the N4 script and log, and retitle §6 from an expected/observed checklist to a stamp inventory. The FA3 reconfirm in §1 should stay marked as what it is — the one line in that script that could actually have failed.

**Nit:** `MASTER.md` says *"20 arguments killed."* Several are `MISSING_INPUT`, `CONSTRAINT_ONLY`, `NOT_STOCKED`, or `P2_RESTATEMENT` — demoted, not killed. The kill table itself is accurate; the one-line summary overstates its own reach.

---

## 5. O6 MeV residual — AGREE-IF

**Confirmed, every number.** This seat recomputed independently: `ρ_bounce^{1/4} = 1059.23 eV`, `T_eff = 2826.79 eV`, `ρ_MeV(g_*=10.75) = 3.5366e24 eV⁴`, `T_MeV/T_eff = 353.76`, `ρ_MeV/ρ_eff = 5.5388e10`, `N_med(MeV,η=1) = +6.1844`, `1/c_s = 6.7586`, ratio `0.9150`, `N_med(late) = −2.6209`, linear compression `3811.87`, `T_c = ½ln2 · m_e = 177.10 keV`, MeV/T_c = 5.65. All match. `N_med = 1/c_s` correctly held as coincidence, matching the retirement already recorded in `PRTOE_FAILURES_LEDGER.md`. Free dial killed and labelled FABRICATED throughout. **No MeV invented from keV.**

**The sign conflict is real and it is the best content in the package.** Both legs are the *same* object — `S = ρ_re/ρ_eff` against the same reference — so it is not an artifact of comparing different epochs: BBN wants `S ≳ 5.5×10¹⁰`, the late lock wants `S ≈ 2.8×10⁻⁵`. One knob, opposite directions.

**Condition — the −2.62 leg inherits a metric this wave demoted.** `S_need_late = 2.7986e−5` is `(H_kin,late/H_door)²` built on `0D late_Θ = +0.0619` — a **re-entry `late_tail10`-class window value**. The settled package, in this same wave, demotes exactly that window to *"F5 diagnostic, **not** S1 here"* and shows the stocked default's settled mean at se=40 is **−0.0037**, falling to `8.6×10⁻⁷` by se=160. Neither `o6_mev_residual_*` nor `s2_rho_suppression_*` contains the string "settled" or "tail10"; the wave-3 `MASTER.md` quotes the sign conflict with no note that one leg rests on a demoted object.

**Direction matters, and it is in the wave's favour.** If settled Θ → 0 then `S_need_late → 0` and `N_med(late) → −∞`: the conflict **strengthens**, it does not weaken. So the verdict — OPEN-BLOCKED, `sign_conflict = true`, 0 lands — stands untouched. What needs curing is the *label*: `S_need_late = 2.80×10⁻⁵` and `N_med(late) = −2.62` should carry a note that they inherit the `late_tail10` window superseded by `S1_settled`, with the direction of the correction stated. Cheap, and it prevents the number being requoted later as settled physics.

**Nits.** (a) `ρ_MeV` carries `(π²/30)g_* = 3.5366` while `ρ_eff` is a bare density whose fourth root is called `T_eff` — so `ρ_MeV/ρ_eff` is **not** `(T_MeV/T_eff)⁴`; the two rows sit adjacent in `REPORT.md` §3 and every channel row in the scorecard inherits the same uniform 3.54× offset. It runs *against* the theory (bigger gap), so no inflation, but a reader cannot reproduce column 2 from column 1. One footnote fixes it. (b) `MASTER.md` rounds the door gap to *"~10¹¹"*; the value is `5.54×10¹⁰` and `WHAT_RESIDUAL_DEMANDS.md` §4 already says `~10¹⁰–10¹²` correctly.

---

## 6. Risk register — the five this wave was asked to be checked against

| risk | finding |
|---|---|
| **free dial banked as land** | **none.** κ,γ scanned with no land claimed (ceiling +0.044); free α (C5), M2 `N_med/η` (C10, FB6, C8-route) all explicitly killed; `N_med = 1/c_s` held as coincidence |
| **force-branch smuggled as P2** | **none.** Israel §3 and FB2/FB14 both catch the rename; C7 flags its own `sign(Θ)` trap; `FORCE_BRANCH_DERIVED = false` in script, log, REPORT and MASTER |
| **MeV dial** | **none.** `+6.18` reported only as FABRICATED and then used *against* itself via the sign conflict |
| **settled vs peak** | **held.** The F5 corner row peaks at `Θ_max_pos = 11.77` against `Θ_lock = 11.706` — 0.6% — and is **not** quoted as a hit anywhere in wave 3. The parent `n3_gpe_late_theta_*` already fenced this (74 peak≥lock rows, max peak 14.76, *"peak ≠ S1"*). Correctly left alone |
| **grade inflation** | **none.** Four doors, four non-promotions; MASTER's `COMPLETE promotions: 0` is accurate. The two overstatements found are *summary-line* reach ("20 arguments killed", "~10¹¹"), not physics |

---

## 7. Standing residuals — unchanged by this wave

- **Obstruction C** (magnitude lock): now blocked at a *lower* reach than the wave-2 reading — settled `+0.0436`, i.e. `|H_kin|/H_door ≈ 0.37%`, against wave 2's `0.245` window value.
- **Obstruction B**: P2 remains a licensed declaration; 0/20 arguments promote it.
- **G1–G3**: Israel `S_ab`, `K_ab`, junction equation — still 0 stocked after 12 candidates.
- **O6**: keV door/floor vs MeV bar, `ρ` gap 10.74–12.45 dex, no legal funding route.
- **RP-A**: alive on *not proven impossible* only.

---

*Post-hoc verification. NO FABRICATIONS. exit0 ≠ PASS. Construction ≠ closure.*
*— Claude (red, CLI seat), 2026-08-04*
