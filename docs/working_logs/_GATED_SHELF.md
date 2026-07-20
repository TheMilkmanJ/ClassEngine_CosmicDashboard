# The Gated Shelf — what is genuinely waiting, and on what (2026-07-20)

> *Docket #43. The shelf exists to separate two things the word "pending" hides: work that
> **cannot** proceed until something outside the desk happens, and work that simply has not been
> done. Only the first is gated. Calling the second "gated" is how a task sits still for a month
> while reading as though someone were on it — the same failure the audit protocol's check 13
> names, one level up.*

**The rule for this page.** An item earns a place here only if a named external event unblocks it,
and the event is written down. If the answer to "what has to happen first?" is "someone has to sit
down and do it", it belongs in the last section, not the first four.

---

## 1. Gated on the owner

| item | what it waits on | which way it moves |
|---|---|---|
| **#157 — the D/H error budget** | JP's ruling on the two-term vs three-term width. The desk work is finished and it inverted the standing recommendation: PRIMAT's ±0.037 is quoted **post-LUNA**, and LUNA's measurement *is* d(p,γ)³He, so the third term appears to double-count the dominant deuterium reaction | **Against the model.** Two-term moves the standing row from −2.49σ to −2.94σ. ForJustin/10 says in its own words that standardising on the friendlier number "must be yours, not mine" — more true now the direction has flipped |
| **#67 — the lattice note** | an external group picking it up; the note is APPROVED FOR CIRCULATION and sent | three numbers of one campaign (T_c/√σ, F_π/√σ, w·√σ). Note the decision rule **cannot currently be executed**: the prediction sits +0.44% from the observation-inverted value against a registered tolerance of ±5.7%, thirteen times wider |

## 2. Gated on in-house runs

| item | what it waits on | honest status |
|---|---|---|
| **#3 / #54 — routeD + conv_desi** | the chains converging | Both relaunched 2026-07-20 on a corrected sampler. Acceptance is repaired and measured (0.99 → 0.25–0.31). **Convergence is not established**, and the seeds are diagonal — they carry no correlation structure, which is what the ±1.00 degeneracy actually requires. First R−1 rows are the test |
| **#13 — the dispersion zon chain** | a converged zon_disp | Dead at R−1 = 23.3. **Not relaunched deliberately**: its config already feeds a covmat that covers 12 of its 13 parameters and knows nothing about `log10_zon`, the one parameter it exists to measure. Restarting on that seed would burn a core to reproduce a known failure |
| **#155 — the sampler proposal** | routeD's own R−1 | Promoted today from housekeeping to critical path: with nested sampling ended, chain convergence gates the evidence verdict itself |

## 3. Gated on external data or facilities

DESI DR3 (the w(z) peg and P-2026-056's XOR), CMB-S4 (ΔN_eff window; the Majoron corner),
nEXO/LEGEND-1000/CUPID (m_ββ), LiteBIRD (the anti-anomaly bet), SKA-class cosmic dawn (P-2026-043's
trough), PTA/LISA/ET (the vortex Gμ null), Belle II-class lepton masses (P-2026-051), lunar-farside
21-cm (the bare-value offset), the SU(2) N_f = 3 lattice campaign, and a direct DESI 4PCF parity
measurement. These are the calendar's business and need no shelf entry beyond the pointer.

## 4. Gated on cluster time — new today

**The nested evidence run.** Ended 2026-07-20 after ~48 h that never reached a first checkpoint.
Costed: 66 s per likelihood evaluation × 534 slice steps = 9.8 h per iteration, so 163 days to
checkpoint one and 736 days for the reference run, with the ΛCDM twin doubling it. Not a stall —
the configuration simply costs more than this hardware can pay. **Consequence:** the verdict rests
on Laplace-from-MCMC until cluster time is bought, which is what promotes section 2 to the top of
the board.

## 5. Gated on sims that do not exist yet

Distinct from section 3, because nothing external is being waited on — the code has not been built.

- **#150 (B1, the genesis solver)** and **#151 (B6, the BipoSH joint pipeline)** — both still PROJECT
- **#160 — the low-ℓ regeneration**, which gates #151: the booked 83% retention came from a
  scratch-era pass that no longer exists, and the retained toy gives ~49%
- **#173 — the R1 caustic-bit two-field sims**, the named remaining gate on the carrier-ratio exhumation
- **the two surviving staged tests** (χ-lag core-halo, granule heating) — sim-gated, and neither
  waits on any remaining mathematics. The granule meter's statistical core is finished; only its
  dynamical half is missing

## 6. NOT GATED — simply not done

**This is the longest section, and that is the point of the page.** Nothing below waits on a run, a
measurement, a ruling or a facility. Each waits only on someone doing it.

- **#141 — the vertex correction.** One coefficient from one well-posed integral. It dominates the
  anchor's 1–8 TeV band and blocks **#124**. Attempted twice, retracted twice, both times as an
  *argument* rather than an integral and both times pointing the favourable way
- **#146** the basement's band structure · **#168** the count C (now known to be an identification,
  not a result) · **#101/#102** the Koide mechanism and the Brannen phase · **#115–#118** the family
  potential, seat alignment, bounce sector, two-draws · **#120** the regulator's entanglement side ·
  **#121** exact Ψ₀ and f_amp · **#123** the Gibbs–Duhem mode sum · **#125/#126** the two ends of one
  joint — a gauge-singlet scalar does not inherit gravity's universality, and one argument pays both
  · **#129** the ladder's matching section · **#130** the base α's two pieces · **#133** which rung
  condensation picks · **#134** the dark vortex pair · **#154** the joint genesis draw · **#161** the
  matched lensing likelihood · **#175** the RECFAST thermal history · **#180** the winding integer,
  whose input `L_gen` is never assigned a value anywhere in the corpus
- **#22 — the flavour puzzle**, reopened: its lever ("α_c = 3α counts the three flavours") was
  retired as a false receipt, so reopening is a re-scope rather than a re-run

*Discipline for this page: an item moves out of section 6 only when a real external dependency is
named, and moves into sections 1–5 with that dependency written beside it. "Waiting" is not a
dependency.*
