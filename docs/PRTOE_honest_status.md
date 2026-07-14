# PRTOE — Honest Status Board (internal review ledger)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


> **STALENESS NOTE (updated 2026-07-13):** dated 2026-07-08 — predates the threading program, the
> derivation hunt (68 entries), the freezes (ε/A_s/n_s/z_on stated), and the running
> zero-parameter evidence test; see DEPENDENCY_TREE for current conditionality — plus the
> derivation hunt, and the evidence run. Current state: [PRTOE_INDEX.md](PRTOE_INDEX.md);
> current standing and live bets: [PRTOE_PREREGISTERED_PREDICTIONS.md](PRTOE_PREREGISTERED_PREDICTIONS.md)
> (banner). Kept as the honest historical baseline.

Dated 2026-07-08. This is the model's self-assessment, kept honest on purpose. Updated as
cruxes resolve. Companion to the pre-registered predictions and the birefringence null.

## The single kill-shot (task Q3 / #21)

**The +1.2% varying electron-mass shift being REAL.** It is the load-bearing bolt: it is
simultaneously (a) the engine of the H₀ easing and (b) the model's primary observable signature.
If a full systematics/degeneracy audit (Q2/#20) or better CMB data (CMB-S4) shows the shift is
consistent with m_e = 1 — i.e. that N_eff, the calibration, or the SHOES prior absorbs the same
improvement — the headline collapses and only the (unbuilt) DE floor remains. **Everything hangs
on this one number being physics, not a degeneracy artifact.**
Runners-up: a negative evidence verdict (Q1/#19), or DESI pinning w robustly away from -1.

## The two least-trusted joints (task Q5 / #23)

Ranked, honestly:
1. **The DE-floor self-tuning mechanism** — no working mechanism; the self-tuning toy ran away
   when computed; Weinberg's no-go for self-tuning is unaddressed. Trusted least. (Q4/#22.)
2. **The m_e shift's robustness** — unproven it isn't absorbing a systematic. (Q2/#20.)
3. **c is not derived** — natural ~1, but the conformal-origin fixed-point is a hypothesis, not a
   calculation (docketed). Empirically pinned to [1.0,1.9] by #16, consistent with natural.

## The near-term falsifier calendar (task Q6 / #24)

In order of arrival / actionability:
1. **PRTOE-vs-ΛCDM full-data evidence** (Q1/#19) — RUNNING NOW (matched optimizers). Δchi2/ΔBIC/ΔlnZ.
2. **Ω_k / shape** — deferred (single-chain MCMC too slow); quick geometric check already says
   flat keeps H₀, closed lowers it → flat-3-torus is the H₀-safe shape (P-2026-013 refined).
3. **DESI DR2 w-running** — data exists; compare against the dCDF w=-1 prediction.
4. **The m_e degeneracy audit** (Q2/#20) — runnable; highest-value un-run test.
5. Slow: LiteBIRD β (P-2026-009/015), CMB-S4, halo vortices (P-2026-016), direct-detection
   nulls (P-2026-017), matched circles / low-quadrupole (P-2026-013).

## Honest odds the CORE picture is right (task Q7 / #25)

**~10%.** Low in absolute terms (most novel unified DM+DE models are wrong; the graveyard is vast),
but ~2 orders of magnitude ABOVE the base rate for such a model — earned by being falsifiable,
internally consistent, honestly labeled, and carrying a ~2.7sigma detected signal. The number is
dominated by RESOLVABLE cruxes: Q1 (evidence), Q2 (m_e reality), Q4 (floor). Favorable resolutions
move it up hard; unfavorable collapse it honestly. High-variance bet with crisp cruxes -- the kind
worth holding. **Update this number as each crux lands.**

## PRE-COMMITTED evidence verdict (locked 2026-07-08, BEFORE #19 returns)

internal review rule: lock what counts as a win BEFORE the number comes back, or we rationalize whatever
we get. For the running PRTOE-vs-ΛCDM full-data comparison (docketed), verdict thresholds committed NOW:
  - PRTOE WINS:   Δ lnZ ≥ +2.5 in PRTOE's favor (moderate+) AND Δ BIC ≤ -2
                  (BIC/AIC already penalize PRTOE's ~2 extra physical params: varying_me, m_ncdm).
  - ΛCDM WINS:    Δ lnZ ≤ -2.5  OR  Δ BIC ≥ +2.
  - INCONCLUSIVE: anything in between -- and this is the HONESTLY-EXPECTED outcome, since PRTOE is
                  ΛCDM-like + the m_e signature; a decisive win would be a genuine surprise.
No moving these after the optimizers finish. (Optimizer gives a Laplace ln Z + bestfit χ² for
BIC/AIC; gold-standard PolyChord ln Z is the eventual publication number.)

## #22 DE-FLOOR — the one serious calculation, RESOLVED (2026-07-08)

`scripts/floor_ghost_condensate.py`. Ran internal review's demanded single calculation of the (δ K)² /
ghost-condensate critical-point floor. k-essence P(X): ρ=2X P_X - P, p=P, c_s²=P_X/(P_X+2X P_XX).
RESULTS:
  - w=-1 EXACTLY at P_X=0 (X0), c_s²=0 there → exact de Sitter floor. And for X<X0, c_s²<0 (unstable)
    → the floor is an ATTRACTOR approached from ABOVE (field cannot sit below it). Good feature.
  - STABILITY: PASS. The c_s²=0 flat direction is stabilized by the (δ K)² k⁴ term
    (ω² = α/M² k⁴ > 0 for α>0; window P_XX>0 & α>0, Arkani-Hamed+ 2004). The
    self-tuning TOY RAN AWAY ONLY because it dropped that k⁴ term; WITH it, the floor holds.
  - SELF-TUNING: FAIL. V0(=Λ) is a free, TUNED parameter -- mechanism does NOT explain why
    Λ is small (Weinberg's no-go stands).
VERDICT (internal review fight-or-concede resolved): KEEP the stable DYNAMICAL w=-1 floor (a real mechanism,
an attractor, better than a bare constant); CONCEDE the self-tuning / "solves the cosmological-constant
problem" claim. Update the least-trusted-joints ranking: the floor is no longer "no working mechanism"
-- it has a stable mechanism -- it just isn't a CC-problem solution (which we should never have claimed).
Net odds effect: mildly favorable (the floor is not a fatal flaw), minus one over-claim retracted.

## CODE-vs-THEORY AUDIT (basement check, 2026-07-08) — the dyad link is NOT enforced in code

Audited the CLASS C source against the model's claims. GOOD: dcdf has a real perturbation sector
(δ/θ/delta_p) -- old gap closed; the w=-1 floor is asymptotic/never-crossed (matches the
#22 ghost-condensate attractor). THREE theory-vs-code GAPS found:
  1. **BIGGEST -- m_e and dcdf are INDEPENDENT in the code.** thermodynamics.c has ZERO dcdf refs;
     m_e is CLASS's generic varying_fundamental_constants (hardcoded step at z=50), disconnected from
     the dcdf field. In the config varying_me and dcdf_rho_inf are independent free params. So the DYAD
     (m_e + dark sector = ONE superfluid) is NOT enforced -- the fit tests "dcdf + free m_e step", not
     "one linked superfluid". Consequences: (a) the amplitude derivation (eps = c*f_amp*Psi0/M_red)
     is NEVER tested by the fit -- m_e is just a free number; (b) part of the "competitive with ΛCDM"
     result comes from the extra freedom of 2 independent knobs, not the constrained dyad.
  2. Screening is a hardcoded REDSHIFT step (z=50), NOT the density-dependent Theta-saturation the
     model claims → the void m_e-step (docketed) physics is not in the code (why it was demoted).
  3. The w=1/3 radiation-like phase is ABSENT (dcdf starts as dust w~0); the claimed 1/3→0→-1 is
     really 0→-1 in code. The conformal-origin c=1 argument (docketed) rests on this unimplemented phase.
  (Unverified: whether cs2_dcdf enforces c_s²=0 at the floor -- function body in an unlocated header.)
HONEST IMPLICATION: the fit is of a MORE FLEXIBLE model than the theory. To test the actual dyad,
ENFORCE the link (derive m_e from dcdf params per #11, fix the transition from screening physics,
re-fit with m_e no longer free) -- the constrained dyad may fit worse. Any paper MUST state that the
fit uses an effective parametrization with independent m_e; the linked superfluid is the theoretical
claim, not directly tested. This reframes the odds: the fit's competitiveness is partly unenforced freedom.

## EVIDENCE VERDICT — LANDED 2026-07-09 (docketed; resolved; the pre-committed gate met, marginally)

The constrained-dyad vs ΛCDM full-data comparison (matched optimizers, same 10
likelihoods) CONVERGED. Result graded cold against the pre-committed gate:
  - ΛCDM:  χ² = 2809.179 | Laplace lnZ = -1474.566 | H₀ = 68.18
  - dyad:  χ² = 2799.654 | Laplace lnZ = -1471.931 | H₀ = 69.82  (m_e FIXED at 1.01232)
  - Δ χ² = -9.52 (dyad better) ; **Δ lnZ = +2.635 (Laplace, dyad favored)** ; Δ BIC ~ -9.5.

**VERDICT: the +2.5 win threshold is CROSSED (+2.635) — the first time — but heavily qualified:**
  1. LAPLACE, not PolyChord: margin over the line (+0.135) < the Laplace estimator's own
     systematic uncertainty ⇒ a MARGINAL crossing on the APPROXIMATE number. PolyChord is
     the only thing that makes it robust. (Pipeline itself says "use --polychord to cross-validate.")
  2. SHOES-CONDITIONAL: the -9.52 edge is dominated by SN+SHOES (~-13.7, the H₀ easing
     68.18→69.82) + ACT (~-3.8, high-l m_e). So the win RIDES ON the H₀ tension being physical
     (Stage 0). SHOES-as-systematic sinks it. The win and the single window are the same brick.
  3. Gate A SIDESTEPPED (stronger than passed): m_e was FIXED, not floated → no prior to game;
     the win comes from a better fit with m_e pinned at the prediction.
  4. Gate B CAPS it SUGGESTIVE (f_amp partial-mover, Psi0 OOM-fixed); SHOT 1 SURVIVES (amplitude
     ontology un-derived). w=1/3 phase confirmed NEUTRAL (onset never moved) → kept, free.

**LABEL: suggestive / SHOES-conditional / Laplace-marginal WIN.** Best realistic outcome on the
table, landed exactly at the line. NOT decisive, NOT robust, NOT prediction-confirmed.

**ODDS UPDATE: ~10% → ~13-16%** (real first positive, discounted hard for marginality + Laplace +
SHOES-conditionality + PolyChord-pending). The ONE lever that moves it hard: PolyChord confirming
the +2.6 on the paid cluster (configs pc_prtoe.yaml / pc_lcdm.yaml ready). The two things that
still sink it: SHOES-as-systematic (Stage 0), or PolyChord pulling +2.6 back under +2.5. Full
internal review grading in the the private internal review record (defender "THE NUMBER" turn).

### SHARPENED by internal review, (accepted): the win INVERTS without SHOES, adds ZERO ontology evidence
Two corrections to the verdict above, both taken: (1) BRAKE 2 is worse than "conditional" — it is
SHOES-DEPENDENT: net Δ χ² -9.52 minus SHOES ~-13.7 = +4.2, i.e. WITHOUT SHOES the dyad is
~4 WORSE than ΛCDM (the edge INVERTS to a loss). The m_e signature alone (ACT -3.8) does NOT beat
the ~+8 Planck-lowlEE/BAO/SPT cost, so m_e wins ONLY by easing the SHOES H₀ tension — NOT on
CMB-internal merits. And that easing is NON-ORIGINAL (whole varying-m_e family does it, the internal review),
so the win adds ZERO evidence for the ontology (superfluid/census/dyad). (2) Standing revised
DOWN: ~10% → ~12% (not 13-16%), because the win is robust only if BOTH PolyChord confirms +2.6
AND SHOES is physical (two live-uncertain gates). Final label: "suggestive / SHOES-DEPENDENT /
Laplace-marginal / non-original-class win, no ontology evidence." Deciders from here: PolyChord
(marginal→robust or sinks it) and SHOES-vs-TRGB (physical→holds, systematic→INVERTS to a loss).
