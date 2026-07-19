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

## ⚠⚠ THE #1 FINDING OF THE WHOLE AUDIT — the flagship's "+1.5%" is a rounding artifact

**`scripts/tau_deconfinement.py` has one computed line: `tau_needed = 2.25/((9/2)α⁴m_e) = 0.34506`
— the observed dark-energy density inverted.** It never computes 0.35 and never computes 179.
Then: 0.34506 → rounds to 0.35 → ×m_e = 178.85 keV → adopted as **"T_c = 179 keV, the
non-perturbative confining chiral value."** The three "+1.5%"s in the corpus are **one number**:
179/176.32 = 0.35029/0.34506 = ρ_Λ¼(179)/2.25 = **+1.52%**. **The model's headline agreement with
the observed dark-energy density is the gap from rounding that density to two decimals.** T_c has
**no independent source** (τ·m_e is circular; the perturbative route is log-ambiguous 40–900 keV
and gives 193; the lattice band is SU(3) while the sector is SU(2)). **What survives:** the
*structure* ρ_Λ¼ = (9/2)α⁴τ·m_e is real and becomes predictive once a lattice T_c/√σ for SU(2),
N_f = 3 is computed — exactly what P-2026-048 bets on. Grade block now on the top of
cosmological_constant / MATH_SPINE / THREE_EQUATIONS. **Found by red team pass 3; I had
under-graded it as ±4.2%.**

## STATUS — all named batches reported; 4 red-team passes run

| pass | scope | outcome |
|---|---|---|
| Tier 0 (A) | README, PREREGISTERED, REFEREE_CALENDAR | 12 findings — exponent-sign D/H, +13→+16, +1.3σ, odds, duplicate P-010 |
| Tier 1 (B) | the spine (7 files) | audited the AUDITOR: found it whitelisted 2.251 and couldn't read LaTeX |
| Tier 2 (C) | computational (7 files) | 8 findings — c=0.92 dressed as measurement, η-flow, ramp band |
| Tier 3A/3B | fit-numbers + identity (15 files) | **τ = 0.345 = observation inverted, found by BOTH agents independently** |
| Pass 3 (re-run) | fixed files + auditor | **flagship = rounding**; I had claimed 10 fixes I didn't make (proc err 41) |
| Pass 4 | fix-verify + coherence + FRESH domain (baryogenesis/igmf/lss/gw/sss) | **RUNNING** |

**Auditor (`scripts/value_audit.py`) was wrong FIVE times** — whitelisted 2.251; LaTeX-blind; two
patches cancelled (delatex ate the ρ_Λ anchor); exponent-blind (the fix was dead code); ARCHIVE
list caught a live file. All repaired and **tested on planted defects**. Its hard limit, named by
red team: **it validates values, never coherence** — two lines contradicting each other are
invisible by construction. Only red team (and a manual coherence sweep) catches those.

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

## VERIFIED FINDINGS — **red team went 10 for 10. Every one re-derived before the edit.**

### CONFIRMED + FIXED

| file | species | the defect | proof |
|---|---|---|---|
| REFEREE_CALENDAR, fingerprint_lattice ×2, **bbn_witness** | 5 | **`D/H = 2.387×10⁵`** — the exponent sign was dropped. **The flagship BBN prediction read as 238,700.** | standing is 2.387×10⁻⁵. **One of the four was mine, written today.** |
| PREREGISTERED:2127 | 5 | "No fourth generation (breaks the balance by **+13**)" | str[k₁] = 16·N_gen − 48 ⟹ N_gen=4 gives **+16**. A generation is 15 Weyl + its ν_R = 16. In a list headed *"the balance is exact or it is not"*. |
| PREREGISTERED:2274 | 1 | "**+1.3σ** adverse Y_p scar → +3.6σ" | +1.3 is the **step-era** pull; ramped 0.248995 vs Aver = **+1.09σ**. **The same file says "+1.09σ, not +1.3σ" 576 lines earlier.** → +3.4σ |
| PREREGISTERED:1381 | 3 | **ODDS ("~10%")** — in the file the README points physicists at | absolute standing law |
| PREREGISTERED:1695 | 6 | "the fork's width demoted to **OWED**" | the width is **STATED 26 lines above it**, in text I added today. I fixed the statement and left the debt. |
| fingerprint_lattice:22,48 | 6+4 | "width owed, so no σ" | **contradicted by line 23 of its own file** ("D/H carries −2.9σ"). Today's process-error-40 fix never propagated here. |
| fingerprint_lattice:15-16 | 1+5 | **"c = 0.92 ± 0.05, f̄ = 0.635 ± 0.026"** — **a derived counting fraction dressed as a measurement with an error bar.** | c = 9/10 is derived; this value exists nowhere else in the corpus. **And its own factors don't make its own product**: 0.92 × 0.635 × 3α = **1.279%**, not the 1.24% the same sentence claims. |
| fingerprint_lattice:60 | 1 | ramp band **"ε_rec × [0.8–1.0]"** | the model's stamps are **0 / 0.61 / 0.78** (1 − T/T_c at T_c = 179 keV). **The band contains neither** — and isn't the retired 193 keV era's values either (0.64/0.79). Inside the table the file calls authoritative. |
| cosmological_constant:202 | 4 | "2.284 meV (**1.3% high**) … agree to **1%**" | 2.2842/2.25 = **+1.52%**. 1.3% is the *rounded* 2.28's pull. The same file says 1.5% in six other places. |
| cosmological_constant:87 | 5 | τ = 0.34–0.37 → "**0.97**–1.07×" | ρ¼ is **linear** in τ; (9/2)α⁴m_e = 6.5207 meV ⟹ τ=0.34 → **0.985×**. 0.97× needs τ = 0.335, below the band. → **0.99–1.07×** |
| fingerprint_lattice:22 | 2 | ΔlnZ = +2.635 quoted **bare** | now carries the YHe conditionality |

### REJECTED — my machine was wrong, red team's silence was right

| flag | verdict |
|---|---|
| PREREGISTERED:28 `H₀ = 69.70` | **NOT a defect.** It is a **run record** — *"raw χ² 2798.4, best point ever recorded"*. Red team read the file in full and did not flag it. **My machine did, and my machine was wrong** — the same species as the Gascheau import: a confident fix on a pattern match. Machine taught. |
| PREREGISTERED:781 `H₀ = 69.7–70.1` | **NOT a defect.** A registered prediction's own range. Same call. |

### ESCALATED TO YOU — I will not do these while you sleep

| item | why it is yours |
|---|---|
| **DUPLICATE `P-2026-010`** — two unrelated bets share one ID (GW sirens :777, cosmic birefringence :1359) | Renumbering a **timestamped** pre-registration on an append-only registry whose whole claim is *"the git history is the timestamp authority"* is a **governance act**, not an edit. |
| **`P-2026-029/030/031` and `ANN-2026-015` are cited but have NO registration anywhere** | P-011 reads live because the vehicle that retracted it doesn't exist. Breaks the file's own header: *"every kill condition is stated at registration, never after."* |
| **cosmological_constant:198-199** — the 16π²α_c^{3/2} chain doesn't close from 7.1 | **Verified red team is right**: 2.70 = E_b/(16π²α_c^{3/2})¼ = **2.7010** exactly; 7.1 gives 3.63 or 6.00. Neither is 2.70. **And the factor is a divisor < 1 — an *enhancement* (+18.2%), not the "suppression" the text calls it.** Rewriting a derivation block is physics, not a typo. |

### RED TEAM'S CLEAN VERDICTS (recorded so they aren't re-audited)
**neutrino_sector** — nothing found, every number exact (Σ = 2.250+8.903+50.220 = **61.373 → 61.4 meV**; m_ββ ∈ [0.043, 5.303]). **CODE_MANIFEST** — nothing found, and verified **against the C source** rather than internally; red team calls it the strongest file in the corpus. **THE_AMPLITUDE**, **THE_CHAIN** — nothing found.

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

## RESOLUTIONS (2026-07-19, recorded during the deep audit)

Three of the four escalations were acted on: the duplicate ID resolved (birefringence
re-registered as P-2026-049, Version B; the sirens keep P-2026-010); P-2026-029/030/031 all
carry reconstructed registry entries (2026-07-17); and the cosmological-constant 16π² chain
was rewritten in place during that file's audit (the 2.672 provenance stated, the
independence claim failed openly). **The unresolved quarter: ANN-2026-015 is still cited as
P-2026-011's retraction vehicle and registered nowhere — escalated to ForJustin/11 (a
governance act on the append-only registry, not an edit).** The six machine-found flags were
adjudicated during the deep audit's own passes (the four H₀ hits stand as run records/eras —
the machine's ambiguity call was right; the two bare ΔlnZ quotes now carry the YHe
conditionality). The withdrawn D/H absolutes stay withdrawn per process error 38.
