# OVERNIGHT AUDIT — the morning report (2026-07-17 → 18)

*Operator asleep. Red team authorised on the files; every finding verified against the engine
before any edit. **No red-team fix applied unverified.***

## THE DISCIPLINE (why this file exists)

A red-team claim is a **hypothesis**, not a warrant. Today's own scoreboard is why: I made two
false inferences that survived until someone checked them — a stability theorem imported backwards,
and a `git log -S` misread that nearly accused the evidence result of being manufactured. **Red team
will be wrong too.** Every finding below carries a VERDICT from independent re-derivation:

- **CONFIRMED** — re-derived from the engine or the corpus; fixed.
- **REJECTED** — red team was wrong; NOT fixed; reason recorded.
- **PARTIAL** — the defect is real, the proposed correction was not.

## STATUS

| batch | tier | files | state |
|---|---|---|---|
| A | 0 — leaves the repo | README (70-406), PREREGISTERED_PREDICTIONS (2325 ln), REFEREE_CALENDAR | RUNNING |
| B | 1 — the spine | MATH_SPINE, THREE_EQUATIONS, DEPENDENCY_TREE, READERS_GUIDE, INDEX, the_great_chain, INTERACTION_ATLAS | RUNNING |
| C | 2 — computational | bbn_witness, cosmological_constant, neutrino_sector, fingerprint_lattice, CODE_MANIFEST, THE_AMPLITUDE, THE_CHAIN | RUNNING |
| D | 3 — domains (~40) | queued | pending |
| E | 4 — working files (21) | queued | pending |
| F | 5 — code + configs | queued (varconst path done) | pending |

## ⚠ THE HEADLINE — found overnight, tier 5 (the C source). READ THIS FIRST.

### `dcdf_dyad_link` does not do what it is named, and it has been OFF for eight days

**honest_status calls this the model's BIGGEST gap** (line 107): *"m_e and dcdf are INDEPENDENT in
the code… the DYAD is NOT enforced — the fit tests 'dcdf + free m_e step', not 'one linked
superfluid'."* Commit fbb81ec2 added `dcdf_dyad_link` and described it as *"enforcing R1 (the dyad)
**structurally**"*.

**It is set in NO CONFIG.** My first read was "the fix exists and was never armed." **That read is
wrong, and the truth is worse:**

```c
double dyad_c = 0.9, dyad_f_amp = 0.63661977, dyad_Psi0 = 5.33073e16, dyad_Mred = 2.435e18;
dyad_eps = dyad_c * dyad_f_amp * dyad_Psi0 / dyad_Mred;   /* ALL CONSTANTS */
pba->varconst_me = 1.0 + dyad_eps;
```

**It reads no dCDF field parameter.** Not `dcdf_rho_inf`, not anything. It sets `varying_me` from
hardcoded numbers and never touches the fluid's fitted state.

| | varying_me |
|---|---|
| `dcdf_dyad_link` ON | **1.012543** |
| what the configs already write by hand | **1.012543** |
| difference | **2.6×10⁻⁷** |

**⟹ ARMING IT WOULD CHANGE NOTHING. IT CANNOT CLOSE THE GAP.** m_e and the dCDF field remain
independent whether it is on or off. **The thing named as the fix does not fix it** — and because it
was off, nobody found out for eight days. **Gap #1 is REAL, OPEN, and unaddressed.**

### And the retired decomposition is live in the C source

`ε = c · f_amp · Ψ₀/M_red` is the **retired** form (standing: ε = c·f̄·α_c = 27α/5π). Inside it:
- `dyad_f_amp = 0.63661977` — that is **f̄ = 2/π** wearing the dead name (identical to 8 digits)
- `Ψ₀/M_red = 0.02189211` vs **α_c = 3α = 0.02189206** — **Ψ₀ is BACK-SOLVED** so the ratio *is* α_c
  (Ψ₀ = α_c·M_red = 5.33072×10¹⁶ against the code's 5.33073×10¹⁶, +0.0003%)

**Ψ₀ is presented as a physical input (a GeV-scale field amplitude) and is α_c in a costume.**
The number it produces is right; the parametrisation is retired and the input is not an input.

**Not fixed here — this is a design question, not a typo.** Closing gap #1 means making m_e a
*function of the dCDF's fitted state*, which is a modelling decision for the operator, not an edit.

## MACHINE-FOUND, PENDING AGENT CROSS-CHECK

*Found by the extended `scripts/value_audit.py` while red team was still running. **All six sit in
files a running agent owns**, so they are NOT touched here — that would collide. They serve as a
GRADE ON THE AGENTS: an agent that misses a defect the machine caught independently ran a weak
pass, and I will know.*

| file:line | species | the claim | machine's verdict | owner |
|---|---|---|---|---|
| fingerprint_lattice:20 | **2** | `ΔlnZ = +2.635` quoted **bare** | the crux is conditional on the YHe defect; needs the asterisk until re-run | tier-2 agent |
| the_great_chain:114 | **2** | `ΔlnZ = +2.635 (capped)` quoted **bare** | same | tier-1 agent |
| PREREGISTERED:28 | 1? | `H₀ = 69.70 (raw χ² 2798.4, best point ever recorded)` | **AMBIGUOUS — likely a legitimate RUN RECORD, not a stale claim.** Do not blind-fix. | tier-0 agent |
| PREREGISTERED:781 | 1? | `H₀ = 69.7-70.1 (joint optimum 69.70)` | **AMBIGUOUS — a registered prediction's own range.** Do not blind-fix. | tier-0 agent |
| INTERACTION_ATLAS:46 | 1? | `H₀=69.7 (TRGB)` | **AMBIGUOUS — TRGB-anchored, a different value by design.** Do not blind-fix. | tier-1 agent |
| PHYSICS_DOMAINS:25 | 1? | `buys H₀ = 69.7 at zero χ² cost` | **AMBIGUOUS — may be an era statement.** Standing CMB claim is 69.9 (THE_AMPLITUDE, dyad_gas, H0_CEILING, CMB_map all agree). | tier-3A agent |

**Note on the four H₀ hits:** the machine flags 69.7 against the standing 69.9, but 69.70 is also a
real historical run record and a TRGB-anchored value. **This is exactly the case where a confident
fix would be wrong** — the same species as my Gascheau import. They go to the agents, then to
re-derivation, then and only then to an edit. *And every one of them is dirty anyway until the fits
are re-run.*

## VERIFIED FINDINGS

*(populated as batches land — each with its independent re-derivation)*

## ALREADY FIXED BEFORE RED TEAM RAN (today's own audit)

| file | species | defect |
|---|---|---|
| README | 3 | **ODDS ("~16%") on the repo's front door** |
| README | 1 | sold "a varying-mₑ **STEP** in cosmic voids" — P-022 retired that reading; a sharp step now counts AGAINST the model |
| README | 2 | ΔlnZ ≈ +2.6 quoted bare — the chains that made it were scored with a ΛCDM helium fraction |
| fairbank_note_draft | 4 | BBN claimed inside a favourable fit record — it is the model's WORST column (p = 0.007–0.20) |
| bbn_witness | 2,5 | the η-flow spent twice; a withdrawn-baseline σ propagated to 4 live docs |
| MATH_SPINE | 1 | `+3.7σ` vs EMPRESS = the step-era pull (ramped gives +3.53σ) |
| PREREGISTERED | 3,6 | "exact c owed via threshold matching" — c = 9/10 is derived |
| fingerprint_lattice | 4 | "δm_q = ε full → ~1σ" — really +12…+18σ; now known symmetry-forbidden |
| UV_completion | 3,6 | a working docket on the reader shelf; its c = 1 candidate live |
| 13 configs | 2 | YHe/bbn lambdas declared varying_me and never applied it |
| MATH_SPINE, CC | 6 | α_c's owner stated only in a build spec |

## THE TWO THINGS BLOCKING A CLEAN NUMBER

1. **The fits have not been re-run.** The YHe fix is in (measured PRyM response, verified to six
   digits), the chains are down. **ΔlnZ ≈ +2.6 stays asterisked until they are re-run.**
2. **D/H `0.00782` and the `2.470340` table row remain UNREPRODUCIBLE** from the model's own engine.
   Three explanations were tried and all failed. They need re-deriving, not defending.
