# RED TEAM BRIEF — the audit's standing facts and rules (2026-07-17)

*The operator has authorised red team to go through the files to verify accuracy and coherence.
**You find and report. You do not fix.** Every finding is verified by the maintainer against the
engine before any edit is made — a red-team claim is a hypothesis, not a warrant.*

## THE STANDING INPUTS — these are the model. Anything contradicting them is a defect.

| quantity | value | note |
|---|---|---|
| **ε** | **c·f̄·α_c = 27α/5π = 1.2543%** | the coupling; three factors, multiplicative |
| **c** | **9/10** | census counting fraction (N−1)/N: 9 charged species + the vacuum's seat. **DERIVED.** `c = 1` is a DEAD candidate. |
| **f̄** | **2/π = 0.63662** | the winding time-average ⟨\|cos\|⟩. **DERIVED.** `f_amp ≈ 0.6 / 0.69` is the RETIRED decomposition. |
| **α_c** | **3α = d·α = 0.02189206** | **the dCDF's** condensate coupling; the 3 is the SPATIAL DIMENSION |
| **T_c** | **177.10 keV** | = τ·m_e with τ = ½ln2 from the Koide kernel. **193 keV is a CROSS-CHECK ONLY — illegal as the keying value.** |
| **M₂** | **α²·T_c = 9.43 eV** | the "electromagnetic handshake"; T_c is the **dyad's** |
| **ρ_Λ¼** | **½α_c²M₂ = (9/2)α⁴T_c = 2.2599 meV** | obs 2.25 (+0.44%). α⁴ → dCDF; T_c → dyad; 9/2 → geometry |
| **Y_p** (ramped) | **0.248995** | +1.09σ vs Aver; **+3.53σ** vs EMPRESS. `0.2495–0.2505` is the RETIRED step interval; **`+3.7σ` is the step-era pull.** |
| **D/H** (standing) | **2.387×10⁻⁵** | **−2.49σ** on the standing 3-term width (0.0563); **−2.9σ** on the 2-term budget (0.0476 = obs ±0.030 ⊕ PRIMAT ±0.037). The width standardization is owner-gated (ForJustin/10) — quote the fork, not one side. |
| **Σm_ν** | **61.4 meV**, normal ordering | m_ββ ∈ [0.04, 5.3] meV, ~3.3 typical |
| **N_gen** | **3** | str[k₁] = 16N_gen − 48 = 0 |
| **N_c (dark)** | **2** | 2N_f·N_c − 4(N_c²−1) = 0; N_f = 3 |
| **ξ_H** | **1/6 — AN INPUT, NOT DERIVED** | P-045's generation count is conditional on it |

## RETIRED / WITHDRAWN — must never appear as a live claim

- **`f_amp` decomposition** (ε = c·f_amp·Ψ₀/M_red) — retired; standing is ε = c·f̄·α_c
- **`c = 1`** (the UV conformal-origin candidate) — dead; c = 9/10 is derived. *(`c ~ 1` meaning "order unity" is fine.)*
- **D/H `2.470340` / `2.454498` / `2.4305`** — PRyM-DEFAULT-ω_b absolutes, **WITHDRAWN** (process error 38). Relative effects only.
- **D/H `2.468`** — the v5-era champion's value; superseded by the ramp
- **D/H scar `−1.2σ` / `−2.0σ`** — v5-era; the standing ramp is **−2.9σ**
- **Y_p `+3.7σ` vs EMPRESS**, **`+1.24σ` vs Aver** — step-era pulls
- **P-022's "sharp global step" reading** — RETIRED. The registry predicts a **σ8-tracking FADE over z ≈ 30–60**; a sharp global step **counts against** the model.
- **"δm_q = ε full"** quark-bleed — **EXCLUDED, but by loop-order and data, NOT by symmetry.** Do not defend this line with lepton number: the dyad is not the Majoron (separate fields since the one-scale corner went tie-dead), and the operator |Ψ|² is a total singlet — L-neutral — so it screens the quark bilinear no more than the lepton one. What does exclude it: the quark bilinear is reached only at two EW/EM loops, ~(α/4π)², and full ε on the quarks moves D/H by +12–18σ. The margin is four orders wider than needed; the *argument* is the part that was wrong.
- **ODDS of any kind** (~10%, ~12%, ~16%) — **NEVER audience-facing.** This is an absolute standing law.

## THE SIX SPECIES — hunt all six

1. **stale value** — a retired number quoted as current *(a stale number looks exactly like a fresh one; RECOMPUTE, do not read)*
2. **withdrawn baseline** — a number whose provenance was retired
3. **retired object cited live** — the only species a name-grep catches
4. **self-contradictory row** — two halves disagreeing by orders of magnitude (e.g. "ε full → ~1σ" was really +12…+18σ)
5. **arithmetic that does not close** — recompute every stated chain END TO END
6. **unreachable answer / unsearched debt** — a thing booked "owed"/"unstated" while the answer exists elsewhere in the corpus. **THE COSTLIEST SPECIES.** Before accepting any "owed", SEARCH THE CORPUS FOR THE NUMBER.

## AUDIENCE LAW (for reader-facing files)

No odds. No restatement stacks (multiple dated passes saying the same thing — state the working
product once). No provenance chatter ("this morning's pass", "walked past this one"). No
strikethrough. True math symbols (H₀, S₈, Σm_ν, χ², ±, ⁴) — no ASCII math. Broken/failed content
does not get restated in a live file: it is replaced by the working product, and its history goes
to the FAILURES LEDGER with the why. **A retirement notice IS allowed to name the value it buries.**

## RULES OF ENGAGEMENT

1. **REPORT ONLY. Change nothing.** No edits, no commits.
2. **Every finding needs: `file:line`, the exact quoted text, WHICH SPECIES, why it is wrong, and what the correct value/statement is — with the arithmetic or the corpus citation that proves it.**
3. **A finding without evidence is noise.** "This looks stale" is not a finding. "Line 47 says +3.7σ; the ramped 0.24900 vs EMPRESS 0.2370±0.0034 gives +3.53σ" is a finding.
4. **"Nothing found" is a valid and valuable report.** Do not manufacture findings to look useful.
5. **Do not flag the FAILURES LEDGER or the archive for naming retired values** — that is their job.
6. **If you are unsure, say so and mark it UNVERIFIED.** The maintainer re-derives everything anyway; a flagged uncertainty costs nothing, a confident wrong claim costs trust.
