# SUBAGENTS USED — RED construction wave verify (2026-08-05)

**Seat:** Claude RED (challenger), CLI orchestrator.
**Pattern:** 4 parallel read-only audit subagents, one per lane cluster, launched concurrently in a single dispatch; CLI synthesis + independent re-verification afterwards.
**Why fan-out:** the corpus under audit is 49 blue files across 5 lanes plus ~15 baseline packages and several scripts/JSON artifacts. Soloing it risks the shallow-read failure mode. Each subagent held one lane's full context.

---

## Shared charge issued to all four

Identical discipline block in every prompt:

- **Read-only.** No file written or edited. No blue work — no constructing physics, no proposing derivations, no suggesting fixes.
- **No MCMC touched. No PolyChord.** Re-running cheap read-only verify/inventory scripts permitted.
- **NO FABRICATIONS.** Never invent a number, citation, path, equation or result. Unverifiable → write `UNVERIFIED` and state exactly what was checked.
- **exit 0 ≠ PASS.** Read the actual log/stdout/JSON; never trust a summary table's claim about a script.
- **Never invent a COMPLETE.** Default certified count 0; raise only with quoted evidence.
- Quote exact `file:line` for every graded claim.
- **Prefer DISAGREE or AGREE-IF over AGREE when evidence is thin.** Do not soften.
- **Polling protocol:** blue was filing live and lane dirs were empty at dispatch. Foreground `sleep` is blocked, so each subagent was told to interleave baseline reading with repeated `ls`, poll ≥6 times, record mtimes, and — if a dir stayed empty — report `LANE EMPTY` and grade the absence as a finding.

Required output per subagent: FILES READ (path + mtime + lines) · POLL LOG · CLAIMS INVENTORY (claim | file:line | verdict) · ATTACK RESULTS (one para per numbered attack, quoted evidence) · LANE VOTE · CERTIFIED COMPLETE COUNT · RESIDUAL split desk-thrash vs construction.

---

## Subagent 1 — Bounce construction attack

**Target:** `bounce/` — FA2 · Θ · Israel · O6 · N6 packages.
**Baseline armed with:** `bounce_cluster_exhaust/{SURVIVORS,MASTER,DISPOSITION,NON_CLAIMS}.md` + 3 logs; `POST_EXHAUST_AUDIT.md`. Pre-wave grades T-W1 / W1a–W1g and the 9 SV-IDs supplied verbatim.
**Attack list (9):** free dials/tautology in ρ_re · invented H_re/MeV and the `N_med→MeV` FABRICATED+sign-conflict kill returning under a new name · Θ densification vs a named continuity-breaking form (CLASS-BOUND thrash resold) · Israel K⁺ vs relabelled K⁻ vs Stress-as-embedding, ΔΠ→S_ab proof vs promoted CANDIDATE · N6 fired from absence (honesty kill-of-the-kill) · N4 theorem resting on free P2 · the 13-item NON_CLAIMS thrash table reappearing as "construction land" · script claims vs actual logs · CANDIDATE→COMPLETE promotion.

**Returned:** 14 blue files read (package landed late, at 22:15:41 and 22:16:33 — 8 polls). 32-row claims inventory. All 9 attacks **clean on physics**; zero grade inflation across all 8 pre-wave cells. Two hygiene kills: self-PAID row (`SURVIVORS.md:70,:16`) and byte-identical re-runs billed as "this wave" with no exit-code artifact. Independently recomputed Θ_lock = 1/√α = 11.706238, log₁₀ ratio 0.5907, and the M-B σ_s bound (9.3e-99).
**Vote:** AGREE-IF (2 conditions). COMPLETE 0.

---

## Subagent 2 — Page R1/R2/R5 + F1 attack

**Target:** `page/`.
**Baseline armed with:** pre-wave grade **T-W15 T8 FAIL 0.113 · claim FALSE · F1 ON**; the survivor shape (dump/entangle/co-mod op, F1-bound); and RED's own carried findings — F1 confirmed (S_star is the global max; +13.15% clears the gate with the failing bin untouched), the S⋆ lever fenced DEAD, and the F5 argmax-on-grid-boundary precedent (late_tail10 +2.870 vs late_tail20 −0.136, same run).
**Attack list (9):** CANDIDATE without both T8≤0.10 and F1 · "page claim true" · S⋆/denominator/binning manipulation · failing bin diluted vs fixed · argmax on grid boundary + contrary sibling stats · free dials in the operator · "stocked law" provenance · citation resolution (the 1079/1203 precedent) · filed log vs prose.

**Returned:** 9 blue files, 11 polls. **Independently recomputed every T8 figure from `coevolve_v13.json` history arrays rather than trusting the log** — S_star, the failing bin (frames 43–54, n=12, range 0.00188834), ratio 0.11315435176934464, u*, u_late: all reproduce exactly. Verified both sha256s. Verified filesystem-side that `coevolve_v13.json` was **not** touched and no new `coevolve_v{N}.json` appeared — write-once honoured, 0 densify runs. Found the log byte-identical to the 2026-08-04 residual rerun; quantified re-file overlap (F1_BIND 75.8% verbatim; R1/R2/R5 ~38–40%). Two kills: the v23 schedule citation, and the phase-favourable "sole fail" framing (with the bin-neighbour computation).
**Vote:** AGREE-IF (3 conditions). COMPLETE 0.

---

## Subagent 3 — Wilson + A_ωJ Charge A attack

**Target:** `wilson/` and `aomegaJ/` (two lanes, two separate votes required).
**Baseline armed with:** T-W5 OPEN-BLOCKED 5/5 MISSING (inventory exit 2 = expected honest state); T-W16/a EMPTY_CORPUS_SEAT · Charge A. Instructed to locate and **read** `koide_wilson_holonomy_inventory.py` before grading any slot, and to quote the Charge A rule verbatim before grading violations. Given the audit's explicit prior rulings: "Fill Wilson numbers — NO, invent forbidden" and "Fill A_ωJ seat from η/keV — NO, Charge A / EMPTY seat."
**Attack list (8):** invented Wilson numbers (grade all 5 slots separately) · dial smuggling (value fixed by target) · exit-code theatre (re-run it) · Charge A circularity — follow the χ/J_seat/ω_J chain and show it · invented seat coefficients · citation resolution · empty-seat promotion · thrash resold.

**Returned:** 17 blue files across both lanes, 6 polls. **Re-ran the inventory script independently: exit 2 reproduced, identical output; all 7 candidate paths confirmed absent by `ls`.** 5-slot table: 0 filled, 0 filled-by-invention. Produced the standing ω_J circularity trace (depth-2 η) and found a **second** one blue understated — c_K = Q/τ = 4/(3ln2) is Koide-dependent on *two* legs. Delivered the wave's sharpest structural finding: the inventory instrument hardcodes slots 2/3/4 as literal strings and corpus-checks only 7 filenames. Two citation kills, one of them a regression from a previously-correct desk citation.
**Votes:** Wilson AGREE-IF (3 conditions); A_ωJ AGREE-IF (2 conditions). COMPLETE 0 both.

---

## Subagent 4 — Side attack (σσ · occupancy · τ · *a*)

**Target:** `side/` — T-S4 · T-W2 · T-S1 · T-S2/T-D6.
**Baseline armed with:** all four pre-wave grades, plus the explicit **do-not-absorb** list (void×20→T-W6; #101/#102/Wilson→T-W5; c₂=√α·c ≠ c_w; lattice P-048 external, gates τ but does not replace T-S4; dynamical Page curve→Goal B; QMC-minus-LHY→control-edge; T-S3 external-gated). Flagged that τ = ½ln2 is an active project front with "locking derivation" as the stated next step — **attack it hardest**.
**Attack list (9):** σσ real calculation vs named-but-unattempted · τ chain still routing through Q=2/3, and whether ½ln2 is derived/fitted/asserted/coincident · *a* forced vs free O(1) vs fit · occupancy — licensed mechanism vs anthropic dress-up vs honest ledger demote · scope absorption / double-booking · free dials · T-S3 leakage via invented internal n_e · script claims vs logs · thrash resold.

**Returned:** 7 blue files, 8 polls (package frozen at 22:15:13; no `logs/` — blue ran nothing this lane). Independently re-hunted for a σσ script: none exists to depth 3; the only "45.7" is the coupling identity at `scripts/audit_math_pass.py:1772`, the only "partial wave" a hydrogenic level printer. Produced the 5-step τ dependency trace confirming Q=2/3 sits at the root and that blue says so (`"locking_without_Q": "OPEN"` in the script's own JSON). Confirmed *a* is still a family with 5 natural O(1)s inside the band. Verified independently that no forward-facing shelf doc was edited. Found the three off-by-one citations and their **cause** — currency lines inserted 18 minutes pre-filing.
**Vote:** AGREE-IF (3 conditions). COMPLETE 0.

---

## CLI work after the subagents returned

Subagent findings were **not** taken at face value. Independently re-verified at the CLI before certifying:

| check | result |
|---|---|
| `T6_koide_owed.md:500` vs `:1397-1400` | **K1 confirmed** — :500 carries neither 1.73205 nor the band |
| `PRTOE_baryogenesis.md:239` vs `:242` | **K2 confirmed** — :239 is the forward-ω_J row |
| `koide_relation.md:743` / `:744` / `:733` | **K3 confirmed** — :743 is #102, :744 is locking_without_Q |
| `coevolve_v13.json` / `v23.json` schedule_version + G_TMS | **K4 confirmed** — v22_near_joint_polish; v23 is v33_G_TMS_0p355, G_TMS 0.355 |
| `koide_wilson_holonomy_inventory.py:94-130` | **K5 confirmed** — slots 2/3/4 are literal strings, read nothing |
| forward-facing `docs/PRTOE_*.md` mtimes vs wave start | **clean** — all 21:57–21:58, wave opened 22:11 |
| top-level `MASTER_REPORT.md` (landed 22:22, **after** all subagents finished) | **read and graded** — no roll-up double-count, COMPLETE 0, residual list unchanged |

The roll-up check mattered: it appeared after every subagent had closed, and the roll-up is exactly where the W1 double-count occurred previously. It was clean.

One finding was **explicitly not** CLI-verified and is marked as such in `MASTER_RED.md` §5 — the page bin-neighbour ratios and alternate-phase counts. Carried as subagent-computed, flagged verify-before-quoting.

---

## Aggregate

| metric | value |
|---|---|
| Subagents dispatched | **4** (concurrent, single dispatch) |
| Lanes covered | **5** (subagent 3 held two) |
| Blue files audited | **49** |
| Independent votes returned | **5** |
| Consolidated verdict | **5 AGREE-IF · 0 DISAGREE · 0 DENIED** |
| COMPLETE certified | **0** |
| Fabrications found | **0** |
| Files written by subagents | **0** (read-only charge held) |
| MCMCs touched | **0** |

---

*Read-only audit. No blue work. No COMPLETE invented. NO FABRICATIONS.*
