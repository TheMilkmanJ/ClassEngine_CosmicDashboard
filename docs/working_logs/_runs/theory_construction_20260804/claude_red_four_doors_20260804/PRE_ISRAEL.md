> **PROVENANCE:** background `claude -p` subagent (blue-launched), **not** interactive red seat. See `PROVENANCE.md`. Unverified until interactive red post-hoc.

# RED PRE-AUDIT — Israel / junction content (not M2 dials)

**Seat:** Claude (red) · **Date:** 2026-08-04 · **Mode:** pre-audit, fences only
**Target package:** `israel_junction_content_20260804` (not on disk at write time)
**Instrument:** `scripts/bounce_israel_junction_inventory.py` (295 lines, untracked, 16:16)
**Priors read:** `n2_match_book_20260804/` · `fa3_metric_off/` · `n1_fa2_amplitude_20260804/`
**Run by red:** yes — read-only, no chains touched. Output quoted below.

---

## 0. Headline: the instrument reports the absence of the thing the package is named for

Red ran the script. It exits 0. Here is what it actually establishes about Israel:

```
[7] Israel / N4 honesty flags
  ISRAEL_S_AB_STOCKED           = False
  ISRAEL_K_AB_STOCKED           = False
  N4_FORCE_BRANCH_DERIVED       = False
  can_derive_H_re_w/o_decl.     = False
  bounce_closed                 = False
  lands                         = 0
[8] ...
  israel_S_ab_equations            = 0
```

Lines 216–221 **assign** these booleans as literals. Lines 228–233 then **assert** them.
Line 248 sets `israel_S_ab_equations: 0`; line 252 asserts it equals 0.

> **These asserts cannot fail.** They test constants written twelve lines above them.
> `exit 0` on this script carries **no information whatsoever** about Israel junction
> physics. It is a stamp that the package is honest about being empty — which is a real
> and useful thing, and red says so — but it is **not** content.

The package is titled *israel_junction_content*. What exists is an **inventory of
absence**. `n2/ALTERNATE_MATCH_RULES.md:19-23` already grades R3 (Israel surface stress)
**MISSING_INPUT**; `n2/SURVIVORS.md:14` grades R3/N4 **MISSING_INPUT**. This script
re-asserts that row. It does not move it.

---

## 1. Pre-registered kill conditions

### K1 — the C4 tautology, with indices

`n1_fa2/CANDIDATE_MAPS.md:44-49` graded C4 (\(\rho_\mathrm{re}=3H_\mathrm{kin}^2M_\mathrm{Pl}^2/8\pi\))
**TAUTOLOGY**, reason: *"Not a medium law — imports \(H_\mathrm{kin}\) as the answer.
Residual rename."*

A junction condition has exactly the same failure shape one level up. If the surface
stress \(S_{ab}\) is obtained by back-solving the jump from a desired \(H_\mathrm{re}\),
the package has renamed the residual from "declare \(H_\mathrm{re}\)" to "declare
\(S_{ab}\)" and added indices.

> **KILL:** \(S_{ab}\) back-solved from a target \(H_\mathrm{re}\), \(\rho_\mathrm{re}\),
> or \(\Theta_\mathrm{lock}\) is **C4-class TAUTOLOGY** and red will grade it as such
> regardless of how much tensor apparatus surrounds it. Red will ask one question:
> **what determines \(S_{ab}\) that is not the answer?**

### K2 — M2 dials wearing a tensor

`CANDIDATE_MAPS.md:80-85` — C8a/C8b (\(N_\mathrm{med}\), \(\eta\)) graded **FABRICATED**.
`NON_CLAIMS.md:7` — \(N_\mathrm{med}\), \(\eta\) not Derived.
`MATCHING_DICTIONARY.md:43` — \(\rho_\mathrm{re}\) from free \(N_\mathrm{med},\eta\) sold
as Derived is M2 fabrication.

> **KILL:** a surface layer carrying one free coefficient is \(N_\mathrm{med}\) with an
> index pair. The brief for this door says *real Israel, **not** M2 dials*. Red will
> count free constants in the junction content. **Any free constant not fixed by stocked
> medium parts = DENIED**, and specifically: an \(S_{ab}\) whose normalisation is chosen
> to hit MeV, or to hit \(\Theta_\mathrm{lock}\), is C8 relabelled.

### K3 — the retired coincidence is asserted as a test invariant

Line 199–211:

```python
N_med_needed = 0.25 * math.log(rho_mev / max(door["rho_eff"], 1e-300))
ratio_vs_1cs = N_med_needed / (1.0 / C_S)
...
# coincidence is near but NOT identity (retired): allow 0.8–1.0 at OP only as observation
assert 0.8 < ratio_vs_1cs < 1.0
```

Red's run: `N_med_needed = 6.184`, \(1/c_s = 6.759\), **ratio = 0.915** — a 9% miss.

The comment correctly says the \(N_\mathrm{med}=1/c_s\) coincidence is **retired** and
not an identity (consistent with `CONSTRUCTION.md:137` and `SURVIVORS.md:18` "MeV via
\(N_\mathrm{med}\)" dead). But the line below it **asserts the coincidence holds**.

> **FLAG (not yet a kill):** a retired coincidence pinned inside an `assert` acquires
> de facto currency as a passing condition. Two concrete hazards:
> 1. If any anchor (\(\rho_\mathrm{eff}\), \(g_\star=10.75\), the 1 MeV reference) moves,
>    the script **crashes**, and the cheapest repair is to move the anchor back. That is
>    a latent dial pointed at the door.
> 2. A later reader greps `assert` for "what this package established" and finds the
>    coincidence among the invariants.
>
> Red is **not** asking blue to change the physics. Red is asking for the assertion to
> be labelled at the assert site as an **observation band on a retired coincidence**,
> or dropped, so nothing downstream can cite it. If it survives into TASK COMPLETE
> unlabelled, red grades **AGREE-IF** at best.

### K4 — sign vs magnitude must be stated, not blurred

The corpus keeps these separate: obstruction **B** (which branch / sign) and obstruction
**C** (magnitude lock). `CONSTRUCTION.md:205` — the observer argument "softens obstruction
B severity; does **not** touch obstruction **C**". `fa3/KILL_AND_FALSIFIERS.md:25` — a
junction map that *forces* a branch would kill or replace P2.

> **AGREE-IF / DENIED:** blue must state explicitly which obstruction the junction content
> addresses — **B, C, both, or neither** — and give a separate argument for each it claims.
> "The junction handles the matching" covering both with one argument is **grade inflation**
> and red will split it back apart. A package that pays B and claims C, or pays neither
> and claims either, is **DENIED**.
>
> **Red declines to say which of B or C is reachable by this route.** That is the design
> question, and answering it would make red the co-author of the door it must grade.

### K5 — the standing bar red already filed on the board

From red's prior board block: *"Israel junction — must supply χ or J_seat **independently**,
or it does not touch Charge A's standing bar on A_ωJ."*

Verified referent: `A_omegaJ_rule1/REPORT.md:13,47,69` — A_ωJ is the CANDIDATE premise
\(\omega_J^2 = J_\mathrm{seat}/\chi\), with blue's own strongest kill case recorded at
`:125` — *"A_ωJ may be a **free-parameter rename**"*.

> **KILL:** junction content that supplies \(\omega_J^2\) as a *form* without fixing
> \(\chi\) or \(J_\mathrm{seat}\) from independent stocked parts leaves A_ωJ exactly where
> `:125` put it. It does not lower the A_ωJ bar and must not be cited as doing so.

### K6 — Phase II fence

`MATCHING_DICTIONARY.md:20-25` and script lines 152–157 forbid an exterior \(H\) in
Phase II. A junction across the metric-off interval must not smuggle \(H\) back in as a
"limit from either side" evaluated *inside* the interval.

> **KILL:** any expression evaluating exterior \(H\), \(a(t)\), or Friedmann **within**
> Phase II — including as an interpolation, a limit, or a "formal continuation" — is a
> category error under P1 and is **DENIED** (`MATCHING_DICTIONARY.md:25`).

---

## 2. What red verified as *correct* (fairness)

Red recomputed rather than assuming, and found no error in:

| check | script | red's independent value | verdict |
|---|---|---|---|
| \(|H_\mathrm{kin}(\Theta{=}1,d{=}3)|/H_\mathrm{door}\) vs \(c_s/\sqrt3\) | line 137–141, assert 255 | 0.085424 vs 0.085425 | **agree** |
| \(H_\mathrm{door}\) vs \(1/(\sqrt3\xi)\) | line 125, assert 256 | 1.894392e−21 vs 1.894385e−21 eV | **agree**, 4e−6 |
| \(R_H/\xi \to \sqrt3\) | assert 257 | 1.7320 vs 1.7320508 | **agree** |
| \(\Theta_\mathrm{lock}\) from numeric \(H_\mathrm{door}\) (line 139) vs closed form \(d/(c_s\sqrt3)\) | assert 258 | 11.7063 vs 11.706238 | **agree** — red checked specifically for a two-definition drift and found none |

The loose assert bands (`11.0 < Θ_lock < 12.5`, `1.5 < R_H/ξ < 2.0`) would have hidden a
drift of several percent. There is no drift today. Red notes the bands are wider than the
agreement they guard, which is a tolerance-hygiene point, not a finding.

---

## 3. Grade conditions when blue files TASK COMPLETE

| grade | conditions |
|---|---|
| **AGREE** | Package described as **inventory of absence** / MISSING_INPUT reconfirm, **not** as junction *content*; `israel_S_ab_equations = 0` stated in prose; 0 lands; B/C separation explicit; N_med assert labelled as retired-coincidence observation; no free constants introduced |
| **AGREE-IF** | Physics clean but ≥1 of: title/prose reads as "content delivered" · N_med assert left unlabelled · B and C covered by one argument · `exit 0` cited as evidence about Israel |
| **DENIED** | Any of: \(S_{ab}\) back-solved from a target (**C4-class**) · a free coefficient in the junction (**C8-class**) · `can_derive_H_re_without_declaration` flipped true · exterior \(H\) evaluated inside Phase II · A_ωJ bar claimed lowered without independent χ or J_seat · "Israel written ⇒ obstruction C closed" |

**Red's prior:** 0 lands. `n2/REPORT.md:57` already says it — *"Israel (R3) remains the
only structural missing input that could change the game — still empty."* Nothing red
found on disk today changes "still empty".

---

## 4. Non-claims of this red note

- Red has **not** proposed how to obtain \(S_{ab}\), and will not.
- Red has **not** said whether obstruction B or C is reachable by a junction route.
- Red found **no arithmetic error** in the script; the asserts that are vacuous are
  vacuous by construction, not by mistake.
- Running the script and getting `exit 0` is **not** a grade. `exit 0 ≠ PASS`.

*NO FABRICATIONS. Pre-audit ≠ verdict.*
