> **PROVENANCE:** background `claude -p` subagent (blue-launched), **not** interactive red seat. See `PROVENANCE.md`. Unverified until interactive red post-hoc.

# MASTER_RED — four residual doors, red pre-audit

**Seat:** Claude (red) · **Date:** 2026-08-04 · **Authority:** owner authorized heavy red use before package ends
**Package:** `docs/working_logs/_runs/theory_construction_20260804/claude_red_four_doors_20260804/`

| file | door |
|---|---|
| [`PRE_N3_GPE.md`](./PRE_N3_GPE.md) | N3 production GPE late Θ vs Θ_lock |
| [`PRE_ISRAEL.md`](./PRE_ISRAEL.md) | Israel / junction content (not M2 dials) |
| [`PRE_N6.md`](./PRE_N6.md) | N6 kill-RP-A disposition |
| [`PRE_PAGE_D4.md`](./PRE_PAGE_D4.md) | Page D4 microphysics only, no densify |

**Mode fence (from red's board block this morning):** red checks plans against fences it
did not write, and names dead routes already in the ledger. Red does **not** propose
mechanisms, targets, or routes. Where a question would amount to red designing the
physics, red says so on the board and stops. **§4 below records one such refusal.**

---

## 0. State of the four doors at write time

| door | dir on disk | script on disk | contents |
|---|---|---|---|
| N3 GPE | `n3_gpe_late_theta_20260804/` — **absent** | `scripts/bounce_n3_gpe_late_theta.py` — **1213 lines, untracked, 16:17** | — |
| Israel | `israel_junction_content_20260804/` — **absent** | `scripts/bounce_israel_junction_inventory.py` — **295 lines, untracked, 16:16** | — |
| N6 | `n6_kill_rpa_20260804/` — **exists, empty** | none | — |
| Page D4 | `page_d4_microphysics_20260804/` — **absent** | none found | — |

Red pre-audited **against priors on disk and the two live scripts**, not against contents
red would have had to imagine. Nothing below grades a package. Nothing below asserts a
package's result.

---

## 1. Verifications red performed (not quotations)

| # | check | result |
|---|---|---|
| V1 | \(\Theta_\mathrm{lock}=d/(c_s\sqrt3)\) recomputed three ways | 11.706237610778283 = \(\sqrt3/c_s\) = \(1/\sqrt\alpha\) — **at \(d=3\) it is exactly \(\alpha^{-1/2}\)** |
| V2 | `hkin_over_hdoor` (GPE script:57-59) vs definitions | \(\Theta c_s\sqrt3/d\); 0.085424 at Θ=1 — **correct, no bug** |
| V3 | Spherical Θ readout (GPE script:465) | \(\langle\partial_r v_r + 2v_r/r\rangle\), weight \(r^2\) — **correct spherical divergence** |
| V4 | Israel script executed read-only | exit 0; \(H_\mathrm{door}\)=1.894392e−21 eV, \(H_\mathrm{shear}\)=1.894385e−21, \(R_H/\xi\)=1.7320, Θ_lock=11.7063 — **all internally consistent, no two-definition drift** |
| V5 | \(N_\mathrm{med}\) coincidence | needed 6.184 vs \(1/c_s\)=6.759 → **ratio 0.915, a 9% miss** |
| V6 | Champion Page artifact hash | `048de43e…fca8` — **matches** `page_t8/REPORT.md:122`; write-once holding |
| V7 | T8 ratio and both routes to a pass | 0.0018883424/0.0166882 = **0.11315435**; pass needs range ÷1.13154 **or** \(S_\star\) ×1.13154 |
| V8 | New 0D grid size vs prior | axes A–D (script:213-233) ≈ **731 rows** pre-dedupe vs prior **83** |

Red found **no arithmetic error** in either live script. The problems below are about
what the numbers are allowed to mean, not about the numbers.

---

## 2. The four findings red brings, ranked

### F1 — Page T8 has an unfenced denominator *(highest value, most actionable)*

T8 = range/\(S_\star\). A **13.16% rise in the global peak \(S_\star\) alone** converts
v13's FAIL to a PASS with the failing window (frames 43–54) untouched — \(S_\star\) lives
at frame 104. The existing fence (`DEAD_LANES.md:29`) only covers levers that move
numerator and denominator *together* ("ratio sticky"); the protocol-break table
(`DEAD_LANES.md §1.3`) does not list \(S_\star\) inflation at all. It is also gate-silent:
a larger peak *helps* T3 and preserves T1. Two named survivor levers describe exactly this
shape (`CONSTRUCTION_LEVERS.md:45` R2/L2 *"preserving midband Page peak"*; R5).

**Remedy demanded:** disaggregated reporting — absolute early-bin range **and** \(S_\star\),
each against v13, on any artifact claiming `T8_pass`. Not a prohibition; a disclosure.
Detail: `PRE_PAGE_D4.md` §1 (P-K1).

### F2 — N3's headline metric is a max-over-scan on an 8.8× larger grid, chasing its own boundary

`max_late_Theta` (script:249) is an extreme-value statistic; it rises with row count for
sampling reasons alone. The prior argmax \((50,-5,3,0.05)\) sat on **three of four** prior
grid edges (`THETA_LOCK_HUNT.md:74` vs `:38-41`); the prior best-peak row sat on **four of
four** (`:77`). The new grid extends exactly those edges (n₀ 50→80, Θ₀ −5→−8, γ 0.05→0.02)
and axis C is labelled, in blue's own comment (script:223), *"high-compression corner
densification (prior best late region)"*.

**Remedy demanded:** print argmax coordinates with every headline number, and quote the
**fixed stocked point** (6, −2, 1.5, 0.15) — prior **+0.0619** — which is scan-size
independent. Detail: `PRE_N3_GPE.md` K1–K2.

### F3 — The Israel package's asserts cannot fail

Lines 216–221 assign `ISRAEL_S_AB_STOCKED = False` etc. as literals; lines 228–233 assert
those same literals; line 248 sets `israel_S_ab_equations: 0` and line 252 asserts it is 0.
**`exit 0` on this script carries no information about Israel junction physics.** The
package is named *content*; what exists is an **inventory of absence** — which is honest,
and red says so, but is not the thing the door was opened for.

Secondary: `assert 0.8 < ratio_vs_1cs < 1.0` (line 210) **pins a retired coincidence as a
test invariant** — a latent dial, since an anchor move crashes the script and the cheapest
repair is to move the anchor back. Detail: `PRE_ISRAEL.md` §0, K3.

### F4 — N6's stocked kill condition is a *sign* condition, and the sign gate fires

`fa3/KILL_AND_FALSIFIERS.md:23` kills RP-A if medium stress **cannot** produce
\(\langle\Theta\rangle>0\). Blue's own data: turn PAID, `turn_paid_toy: true`, max late
⟨Θ⟩ = **+1.8005** — positive. The gate fires. The residual is **magnitude** (obstruction C),
a different object kept separate throughout the corpus. Presenting the magnitude shortfall
as satisfying the sign kill is a **category substitution**.

And the stocked condition is quantified *"beyond toys"*, over instruments that are **not
stocked** — a universal over non-existent instruments can be left open but never
*established*. Detail: `PRE_N6.md` §2.

---

## 3. Cross-cutting attack surfaces, all four doors

| # | surface | concrete form here |
|---|---|---|
| A1 | **Fabrication** | Θ_lock described as derived (it is \(\alpha^{-1/2}\)); \(S_{ab}\) back-solved from a target; an invented \(S(u)\) form |
| A2 | **Grade inflation** | "PAID (toy)" → "PAID"; "RECONSTRUCTED" → "COMPLETE"; "SURVIVOR-SCHEMA" → "CANDIDATE"; deepened 0D/1D/spherical/2D → "production 3D"; inventory-of-absence → "content" |
| A3 | **Free dial** | κ, γ off stocked (1.5, 0.15); \(N_\mathrm{med}\), η; a free constant in \(S_{ab}\); \(G_\mathrm{TMS}\)/`BS_MILD` |
| A4 | **Soft-close** | 0.113 as "≈0.10"; 11.34 peak as "≈ lock"; "essentially", "within reach", "consistent with" |
| A5 | **Soft-kill** *(the mirror of A4, and N6's specific temptation)* | Declaring the residual impossible so it leaves the open board. **A kill empties the desk exactly as a land does.** Red grades an unjustified kill and an unjustified land as the same offence |
| A6 | **Densify thrash** | Page: mode-count under a "continuum" heading (`DEAD_LANES.md:88`). N3 analogue: grid/box refinement until late ⟨Θ⟩ rises — an L/N-dependent late average is a property of the box |
| A7 | **exit 0 ≠ PASS** | Vacuous asserts on hardcoded booleans (Israel §0); `assert production_3d is False` (GPE:1203); an `assert kill_fires` would be the same class |
| A8 | **Namespace collision** | **D4** = Page *accept near-miss* vs **D4** = bounce *written re-entry bookkeeping*, the latter graded **PAID** (`n2/SURVIVORS.md:54`). A cross-citation would import a payment into a ledger where D4 is an admission of not paying |

---

## 4. One refusal, stated on the board rather than made silently

`PRE_N3_GPE.md` §2 records a domain-of-validity question red raised about blue's own
target and instrument — with its counter-evidence stated in the same breath
(\(v_g/c_s = 2.1213\) at \(x=2\), unbounded at large \(x\); a non-relativistic GPE has no
built-in \(c\)).

**Red will not hand that to N6 as impossibility content, and N6 must not cite it.** If
red supplies the kill package its missing argument and then grades the kill, red has
graded its own work and the third seat is spent. If blue wants that line, blue derives it,
owns it, states its counter-evidence, and red grades it as blue's — with no credit for
having been prompted.

Design questions reaching red on these doors get the same answer: **that is a blue
decision.**

---

## 5. Red's priors on the four doors

| door | red's prior | would be surprising |
|---|---|---|
| N3 GPE | COMPLETE 0; S1 stays MISSING_INPUT; no 3D solver exists in the package | a stocked-parameter late lock |
| Israel | 0 lands; R3 stays MISSING_INPUT; *"still empty"* (`n2/REPORT.md:57`) | an \(S_{ab}\) with no free constant |
| N6 | does not fire | a proof-level obstruction with named, attackable premises |
| Page D4 | T8 stays 0.113154; `page_curve_claimed` false; Q6 OPEN | a disaggregated joint clear |

**Aggregate expected COMPLETE: 0.** Red concurs with blue's own stated expectation. Under
these fences a real land would be surprising, and surprise is the correct prior — in
**both** directions, which is the whole content of §3 A5.

---

## 6. Non-claims of this package

- Red has graded **nothing**. Three of four target directories do not exist; the fourth is empty.
- Red has **not** predicted any scan outcome.
- Red has **not** proposed a mechanism, target, or route for any door.
- Red has **not** touched living `docs/PRTOE_*.md`, chains, or MCMCs. One read-only script
  was executed and one file hashed; nothing was written outside this directory and one
  appended block in `ForGrok&Claude.md`.
- No peek H0. `page_curve_claimed` false. Strong CP abstention.
- `exit 0 ≠ PASS`. Delivered ≠ graded. Pre-audit ≠ verdict.

*NO FABRICATIONS.*
