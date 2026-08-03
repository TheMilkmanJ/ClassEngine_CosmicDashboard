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
| **#67 — the lattice note** | an external group picking it up; the note is APPROVED FOR CIRCULATION and sent | three numbers of one campaign (T_c/√σ, F_π/√σ, w·√σ). Note the decision rule **cannot currently be executed**: the prediction sits +0.44% from the observation-inverted value against a registered tolerance of ±5.7%, thirteen times wider |

*(**#157 — the D/H error budget** left this shelf 2026-07-21.** Source check on arXiv:2011.11320
closed it: three-term double-counts LUNA; standing is two-term ±0.0476 / **−2.94σ**. Kill in
`PRTOE_FAILURES_LEDGER.md`; deuterium row §1 and harness re-pinned. No owner taste call remained once the
citation was read.)*

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

- ~~**#150 (B1, the genesis solver)** and **#151 (B6, the BipoSH joint pipeline)** — both still PROJECT~~
  **(2026-08-02 hygiene: both are no longer sim-gated as "unbuilt".)** #150 is **built and delivering**
  (`scripts/genesis_solver_B1.py`; production run deferred only). #151's **estimator is built**
  (`scripts/biposh_estimator_pass.py`); what remains is the external data application, not a missing
  pipeline. #160's gate on #151 was already lifted 2026-07-20.
- ~~**#160 — the low-ℓ regeneration**~~ *(PAID 2026-07-20 — `scripts/torus_lowell_pattern.py`, 90%
  retention, S/N 0.16; the #151 gate is lifted)*
- **#173 — the R1 caustic-bit two-field sims** — re-typed 2026-07-27: the precision test this row
  gated is discharged by theorem; the sweep is confirmation-class and MACHINE-gated (run when MCMC
  is off the box). Genuine residual is the non-polynomial coupling's UV story, not the sim itself
- **the two surviving staged tests** (χ-lag core-halo, granule heating) — sim-gated, and neither
  waits on any remaining mathematics. The granule meter's statistical core is finished; only its
  dynamical half is missing

## 6. NOT GATED — simply not done

**This is the longest section, and that is the point of the page.** Nothing below waits on a run, a
measurement, a ruling or a facility. Each waits only on someone doing it.

> **Reverse-audit correction (2026-07-21; list hygiene 2026-08-02):** the following closed in the
> files after this page was written and are **no longer listed below** — **#141** (vertex integral,
> c = 0.789262), **#133** (rung fixed by κ-cancellation), **#134** (F_dark/√σ = 0.40–0.47),
> **#175** (RECFAST-class thermal-history run made and booked), **#120** (regulator O(1), structural),
> **#121** (exact Ψ₀ and f_amp), **#123** (Gibbs–Duhem reframe — DE rides Door A), **#154** (joint
> genesis draw, proven independent), **#180** (n ≳ 1.65 adjudicated; first-principles n under #117),
> plus the earlier struck set **#168, #125/#126, #129**. Docket rows carry the receipts.

**Still genuinely owed on this shelf (desk work, no external gate):**

- **#101 / #102** — the Koide-node physics: what seats the hopping at |b|/a = 1/√2, and what sources
  the Brannen phase
- **#115** — family-field / lock-arc residue (ring-centre face supplied 2026-07-28; live residue is
  L2 deposit argument and the graded-norm mechanism with #101). **#117** bounce sector (owns a
  first-principles winding integer beyond #180's bound). **#118** closed by the chain file's own
  record (two draws are separate mechanism classes) — not listed as open here
- **#116** — seat-alignment: medium is identity-blind; gated on a flavor-resolved settling profile
  Φ_med(T) (inherits the basement build — belongs with basement-blocked work rather than pure desk)
- **#130** — base α piece 1 only (two-channel Π at zero momentum); piece 2 closed and propagated.
  Piece 1 is basement-blocked behind #113/#146
- **#146** — basement band structure (reduced; open count is §6f's third horn / phase condition)
- **#161** — the matched lensing-likelihood fit
- **#22** — the flavour puzzle, reopened: its lever ("α_c = 3α counts the three flavours") was
  retired as a false receipt, so reopening is a re-scope rather than a re-run

*Discipline for this page: an item moves out of section 6 only when a real external dependency is
named, and moves into sections 1–5 with that dependency written beside it. "Waiting" is not a
dependency. Closed items do not remain in the bullet list with a parenthetical "paid" note — they
leave the list and sit in the reverse-audit box above.*
