# The Trials Factor — How Large the Search Space Was, Counted Against Ourselves

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim
> conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

> Written 2026-08-02, at the corpus's own red-team review. This document exists because the
> strongest attack on this program is not "the arithmetic is wrong" — it reproduces — but
> "closed forms in α, π and ln 2 are dense in the reals, and you searched that space until
> things landed." A skeptic will construct this document if we do not. Better to be its author,
> with hostile assumptions, and let every conclusion below bind the corpus's own quotation
> practice.

## 1. The charge, stated at full strength

The corpus reports closed-form matches to measured numbers at the 0.1–1% level: an amplitude
from (α_c/4πk)³, a dark-energy scale from (9/2)α⁴τm_e, a spectral shift from 27α/5π, a shared
coupling k = ln(1 + π/2α_c)/π. The charge is that expressions of this class are so numerous
that percent-level agreement with *any* target is expected by chance, and that the discovery
process — try forms, keep what lands — guarantees hits regardless of whether the underlying
physics is real. This is the look-elsewhere effect applied to model-building rather than to
data analysis, and it is a fair charge.

## 2. The hostile density calculation

Take a deliberately generous but plausible grammar of the kind this corpus permits itself:

> G = (p/q) · αⁿ · πᵐ · 2ˢ · (ln 2)ʲ, with p, q ≤ 10 coprime, n ∈ {0…4}, m ∈ {−2…2},
> s ∈ {−1, 0, 1}, j ∈ {0, 1}

That is 63 rationals × 5 × 5 × 3 × 2 ≈ **9,450 expressions** (fewer distinct values after
collisions; the estimate below is order-of-magnitude). Their values spread over roughly 12
decades, giving a density of order **800 expressions per decade**. For values distributed
log-uniformly, the expected number landing within ±δ (fractional) of one fixed target is
≈ 800 · 2δ/ln 10. Evaluated:

| tolerance δ | expected matches to a single target |
|---|---|
| ±1% | ≈ 7 |
| ±0.5% | ≈ 3.5 |
| ±0.1% | ≈ 0.7 |

**Conclusion, binding on this corpus: a lone match at the half-percent level is *expected*,
not surprising. Quoted by itself, it carries approximately zero evidential weight.** Nothing
below this line softens that sentence; everything below classifies what does and does not
survive it.

## 3. The denominator, from this corpus's own records

The failures ledger is the honest count of the search. As of this writing:

- **162 dated entries** in [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md), of which 64
  carry headings that self-describe as dead routes, withdrawals, falsifications or kills.
- **Standing predictions** live in [PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md)
  (final-product register; count the `## P-2026-NNN:` headings there). **Failed / withdrawn /
  rehomed predictions and repair narrative** live in
  [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) (R1-predfile recategorization). The honest
  denominator for look-elsewhere is **registry + ledger**, not the live register alone. A prior
  snapshot used ~50 registered / ~10 falsification markers before recategorization; after
  rehome, do not quote those snapshot counts without citing both files.
- Documented per-constant multiplicities, which are the trials factor in miniature: the
  hierarchy exponent's 3/2 survived after **four attachment routes were computed and failed**
  (Coleman–Weinberg ½, tachyonic onset ¾, sharp-cutoff BCS ln 2, scheme constants {0, 5/6, 1})
  plus a closed bracket identification (the T_c derivation's own −3/2, excluded on
  squared-log grounds). The Koide arc's deposition peak has **three recorded dead routes**.
  The Koide-neutrino branch was withdrawn outright when its "0.5%" match re-adjudicated to a
  4.33% miss.

Two readings of the same ledger, and both are true. It is the program's integrity credential —
misses are recorded, dated, and never rewritten. And it is the prosecution's denominator — it
proves the search was wide. This document exists so the second reading is priced rather than
discovered.

The ledger also records the practice that most distinguishes this search from curve-fitting:
**numerically matching forms have been rejected on structure.** The N = 10⁹ "within 2%"
coincidence was computed, reproduced, and labeled a red herring because averaging cannot act
on the width it would need to act on. The pairing shell's ln 2 offset was found to brush the
Koide kernel's τ = ½ln2, inspected, and recorded closed as a convention artifact (the match is
to 2τ, and no derivation connects the two). A grammar that only kept hits would have kept
both.

## 4. What survives a hostile trials correction

Three classes, in descending order of immunity:

**(a) Preregistered bets with future referees.** A prediction registered before its deciding
data exists cannot be a selection effect on that data. This is the only fully trials-immune
class, and its cost is patience: as the reader's-risk file states plainly, **no bet in this
registry has yet been paid by post-registration data.** Pay dates: JUNO ~2031–32, ton-scale
0νββ in the 2030s, CMB-S4, HL-LHC, a LUNA-class d(d,n)³He measurement.

**(b) Multi-role constants — joint fits.** The grammar argument prices *one* expression
hitting *one* target. It cannot cheaply price one value serving several unrelated targets at
once: of the ~3 grammar members within 0.5% of target A, the fraction also within 0.5% of an
unrelated target B is of order 0.4% — joint double hits are ~100× rarer than single hits, and
triple hits ~10⁴× rarer. The corpus's genuinely joint objects are α_c = 3α (the amplitude ε,
the dark-energy floor, the primordial amplitude A_s, and the hierarchy anchor's exponent all
spend the same value) and k (derived from the screened kernel, appearing in the A_s closed
form, and read back from the measured amplitude at 1.3602 ± 0.0064). **The honest caveat
travels with the claim: the joint counting is only as good as the independence of its
targets** — which is exactly what [PRTOE_INDEPENDENCE_AUDIT.md](PRTOE_INDEPENDENCE_AUDIT.md)
audits, pair by pair. Where two roles collapse into one (it has happened once already —
the finiteness count against Navarro-Salas 2024), the joint suppression is forfeited for that
pair.

**(c) Structural results carrying no tuned number.** The lepton-number bookkeeping theorem
(an L-violating medium can reach only Majorana neutrino operators), the particle-hole channel
selection (a charged condensate is excluded by thirty orders on the photon mass), the
demotion of Σm_ν as a discriminator. These are not percent-level matches and the density
argument does not touch them; their exposure is correctness, not coincidence.

**What does not survive: any single percent-class agreement quoted alone.** The +0.44% on
ρ_Λ^¼, the −0.34% on A_s against the frozen pipeline value, the +0.14% on the anchor's
convention value, the 0.45% central-value gap at the 0νββ funnel edge — each of these, cited
in isolation, is inside the expected-by-chance band of §2 and must never be presented as
freestanding evidence. Their evidential content, where they have any, lives entirely in
membership of class (a) or (b).

## 5. Worked example — the funnel edge, priced honestly

The sharpest recent case. The smallest lightest-neutrino mass at which m_ββ can cancel
exactly computes to m₁\* = 2.2496 meV; the dark-energy scale is 2.2395 ± 0.0108 meV; central
values agree to 0.45%. Priced: (i) today the threshold itself carries ±0.24 meV from
oscillation inputs, so the agreement is a ~0.04σ consistency — the data cannot currently
resolve the claim at all; (ii) under a flat-log prior across the decade where the funnel edge
could plausibly sit, a ±0.45% window is ≈ 0.4% of the decade — a ~1-in-250 surprise *before*
any trials correction, and this corpus scans many scale pairs; (iii) what rescues it from
class-nothing is only its **future referee**: JUNO shrinks the threshold error to ≈ 0.06 meV
by ~2031–32, converting the identity into a ~3%-level test that can fail. The registry
annotation to P-2026-012 carries this framing; forward files must not quote the bare 0.45%.

## 6. Recorded tensions, kept visible

A search that only reports agreements should be disbelieved. This corpus's own bookings
include: the concordance ε = 1.2403 ± 0.0079% sitting **1.8σ from the closed form's 1.2543%**;
primordial deuterium at −2.9σ on the tightest error budget; the anchor's exact landing
requiring a coupling weaker than α's infrared limit, unavailable at any scale; Y_p adverse
against EMPRESS at 3.8–4.4σ. These stay quoted at full strength wherever their sectors are
discussed.

## 7. Quotation rules (binding)

1. No forward file quotes a lone percent-class match as evidence. Every such number is quoted
   with its class: joint role, registered bet, or *decoration* — and decorations say so.
2. Every "N independent confirmations" claim must cite its row in
   [PRTOE_INDEPENDENCE_AUDIT.md](PRTOE_INDEPENDENCE_AUDIT.md).
3. Central-value agreements are quoted with their full error budgets, both sides.
4. This document's density table is re-run if the corpus's effective grammar widens (new
   constants, larger rationals, new exponent ranges). Widening the grammar *raises* the bar.

## Sources

The density model is standard look-elsewhere accounting (log-uniform value density over a
bounded grammar). Internal: [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md),
[PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md),
[PRTOE_INDEPENDENCE_AUDIT.md](PRTOE_INDEPENDENCE_AUDIT.md),
[PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md).
