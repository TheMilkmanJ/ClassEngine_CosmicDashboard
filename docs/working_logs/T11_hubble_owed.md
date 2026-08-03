# T11 Hubble tension — OWED
1. POLYCHORD (the evidence cap's confirmer — the 25% gate). — **RETIRED AS UNAFFORDABLE
   (2026-07-27 sync; the decision executed 2026-07-20):** the nested run ended after ~48 h
   without a first checkpoint (163 days/checkpoint priced on this hardware), archived to
   `chains/_archive_polychord_ended_20260720_0915/`; P-2026-044 amended — the graded number
   is now the Laplace-from-MCMC estimate at chain convergence (docket #155).
2. P-2026-001 TRGB tracking (the no-hedge ladder bet).
3. The independent-detection instruments' pricing: P-007 (void step), P-024 (dipole), P-029 (comb), P-030 (mid-ramp lines) — each converts fit→physics if it lands.
4. The EDE-comparison table's fairness pass (steelman the competitors' latest) — **PAID
   (2026-07-28).** The "MCMC-queued behind capacity" tag was wrong: the item asks for the
   *table's* refresh against current literature, which is desk work and needs no chain. The pass
   is in `PRTOE_hubble_tension.md` §5 — four competitors with each one's strongest card face-up,
   an added interacting-dark-energy row, a SH0ES counterweight against the CCHP JWST row, and
   this model's own row conceding it cannot reach 73 and is beaten by EDE on every column.
   **The closing act was verifying the EDE status card's source**, which had been booked as a
   bare identifier with no author, title or year anywhere in the corpus: it is Poulin, Smith,
   Calderón & Simon (2025), arXiv:2505.08051 — by EDE's own originator, and it reports *more* for
   the competitor than the card claimed (residual tension ~2σ down from 3.7σ; EDE at H₀ = 73
   beating ΛCDM at 68.4 once DESI is in; above 5σ with SH0ES). Card and bibliography both
   corrected in the direction that makes this model look worse, which is the direction a fairness
   pass is for.

Coupling-geometry status: early-universe/production (ε fully ON at recombination under every reading) — unchanged.

## Literature half of the EDE fairness pass (2026-08-02) — desk closed; machine half open

Item 4's *table* refresh is PAID (2026-07-28). This section records what that pass is, what
literature alone can already say, and what still waits on the live BBN-fixed pair — so the
desk half is not re-opened every time a chain checkpoint lands, and so no unconverged Δχ² is
mistaken for a result.

### What the fairness pass is

The field's reference is Schöneberg et al. 2026 (arXiv:2607.13282): **fourteen models, one
pipeline, one data stack** (current CMB + BAO + supernovae), scored on the same columns —
−ΔAIC, ln BF, residual Δ_DMAP against SH0ES — rather than each paper's own preferred cut.
Against a ΛCDM baseline of Δ_DMAP = 5.4σ, its Table 1 puts early dark energy at residual
**2.51σ** (−ΔAIC 23.40, ln BF 10.51) and free varying-m_e at residual **4.25σ** (−ΔAIC 12.58,
ln BF 3.53). This model's mechanism is the *fixed-amplitude* member of the varying-m_e class;
it inherits that class's reach ceiling and pays none of free-m_e's re-fit freedom. A fairness
pass in that spirit is therefore: put every competitor's strongest published card face-up on
the same scoreboard, put this model's own card next to them without special pleading, and
correct the cards when the sources say more (or worse) than the corpus first booked. The
executed pass lives in `PRTOE_hubble_tension.md` §5 — EDE, free varying-m_e, the ladder /
systematics row, interacting dark energy, and this model's zero-extra-parameter row.

### What literature alone can already say (no new chain)

- **On residual H₀ tension, EDE is ahead of this mechanism class on every Schöneberg column.**
  Nothing in the derivation changes that: a derived ε buys parameter economy and a kill-list,
  not extra reach toward 73.
- **The competitor's 2025–26 status is stronger than the first card claimed.** Poulin, Smith,
  Calderón & Simon 2025 (arXiv:2505.08051) — EDE's own originators — report residual SH0ES
  tension ~2σ (down from 3.7σ) under Planck ℓ<1000 + ACT DR6 + lensing + Pantheon+ + DESI DR2;
  with DESI, EDE at H₀ = 73 fits better than ΛCDM at 68.4; adding SH0ES raises the preference
  above 5σ (their Δχ² = −35.4 is *their* published figure, not this corpus's). The fairness
  correction of 2026-07-28 moved the card in the direction that makes this model look worse.
- **This model cannot reach 73.** The audited ladder-side ceiling remains ~70.9–71.3; the
  standing production claim is H₀ ≈ 69.9 under the earlier joint fit, with the residual owned
  and the TRGB side of the calibration dispute pre-registered.
- **Where this model is stronger is not fit quality:** zero extra sampled parameters versus
  EDE's three (and free-m_e's one-to-two), and one amplitude on the hook across BBN, CMB,
  21-cm and neutrinos. Cheaper and more falsifiable are different virtues from "beats EDE on
  residual tension."
- **The S₈ charge against EDE is real** (Hill et al. 2020) **and does not clear this class:**
  Lee–Zhou 2026 (arXiv:2606.06495) find that raising H₀ by modifying recombination generically
  lowers Ω_m in a way DESI DR2 BAO dislikes — a structural obstruction aimed at varying-m_e
  as a family, not a free pass for the fixed-ε member.

None of the above requires a new MCMC. None of it is a claim that this corpus's own Δχ² or
ΔlnZ has been re-measured under the BBN-fixed likelihood.

### What still requires the dyad / ΛCDM bbnfix pair — MACHINE

The literature half grades *competitors* and *mechanism class*. The machine half grades
*this implementation* on *this likelihood*:

| owed number | instrument | status (2026-08-02) |
|---|---|---|
| this model's joint-fit H₀ posterior (BBN-fixed, Σm_ν free) | `dyad_mnu_bbnfix` | **running, not converged** — latest `.progress` R−1 ≈ 0.19 at N ≈ 1.45×10⁴ (2026-08-02); bar is R−1 < 0.05 |
| the matched ΛCDM twin under the same stack | `cmp_lcdm_mnu_bbnfix` | **running, not converged** — latest R−1 ≈ 0.14 at N ≈ 1.32×10⁴ |
| model−ΛCDM Δχ² / Laplace ΔlnZ under that stack | both, at convergence | **blocked** — `scripts/finalize_h0_at_convergence.py` refuses to print until both sit under the bar |
| deuterium-inclusive joint grades | model chain's D/H term | **blocked on the same gate** |

**Do not quote a numerical Δχ², ΔlnZ, or replacement H₀ sentence from these chains until that
gate opens.** Earlier production numbers (joint fit ≈ 69.7–69.9; Laplace ΔlnZ ≈ +2.6,
SH0ES-conditional) remain the standing *pre-bbnfix* claims; they are not to be silently
replaced by unconverged means. If any live-chain H₀ is cited for operational awareness only,
label it **preliminary**, point at `chains/dyad_mnu_bbnfix.progress` and
`chains/cmp_lcdm_mnu_bbnfix.progress`, and do not promote it into the letter or the fairness
table.

**Desk half of item 4: closed.** The scoreboard, the competitor cards, and the concession that
EDE wins on residual tension are literature work and stand. **Machine half: open** — the
bbnfix pair's H₀ and the model−ΛCDM evidence difference under the production-faithful BBN
treatment. Progress lives under `chains/`; the fairness *table* does not move again until
those numbers exist.
