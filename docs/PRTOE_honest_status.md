# PRTOE — Honest Status Board (red-team ledger)

Dated 2026-07-08. This is the model's self-assessment, kept honest on purpose. Updated as
cruxes resolve. Companion to the pre-registered predictions and the birefringence null.

## The single kill-shot (task Q3 / #21)

**The +1.2% varying electron-mass shift being REAL.** It is the load-bearing bolt: it is
simultaneously (a) the engine of the H0 easing and (b) the model's primary observable signature.
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
   calculation (#17). Empirically pinned to [1.0,1.9] by #16, consistent with natural.

## The near-term falsifier calendar (task Q6 / #24)

In order of arrival / actionability:
1. **PRTOE-vs-LCDM full-data evidence** (Q1/#19) — RUNNING NOW (matched optimizers). Δchi2/ΔBIC/ΔlnZ.
2. **Omega_k / shape** — deferred (single-chain MCMC too slow); quick geometric check already says
   flat keeps H0, closed lowers it -> flat-3-torus is the H0-safe shape (P-2026-013 refined).
3. **DESI DR2 w-running** — data exists; compare against the dCDF w=-1 prediction.
4. **The m_e degeneracy audit** (Q2/#20) — runnable; highest-value un-run test.
5. Slow: LiteBIRD beta (P-2026-009/015), CMB-S4, halo vortices (P-2026-016), direct-detection
   nulls (P-2026-017), matched circles / low-quadrupole (P-2026-013).

## Honest odds the CORE picture is right (task Q7 / #25)

**~10%.** Low in absolute terms (most novel unified DM+DE models are wrong; the graveyard is vast),
but ~2 orders of magnitude ABOVE the base rate for such a model — earned by being falsifiable,
internally consistent, honestly labeled, and carrying a ~2.7sigma detected signal. The number is
dominated by RESOLVABLE cruxes: Q1 (evidence), Q2 (m_e reality), Q4 (floor). Favorable resolutions
move it up hard; unfavorable collapse it honestly. High-variance bet with crisp cruxes -- the kind
worth holding. **Update this number as each crux lands.**

## PRE-COMMITTED evidence verdict (locked 2026-07-08, BEFORE #19 returns)

Red-team rule: lock what counts as a win BEFORE the number comes back, or we rationalize whatever
we get. For the running PRTOE-vs-LCDM full-data comparison (#19), verdict thresholds committed NOW:
  - PRTOE WINS:   Delta lnZ >= +2.5 in PRTOE's favor (moderate+) AND Delta BIC <= -2
                  (BIC/AIC already penalize PRTOE's ~2 extra physical params: varying_me, m_ncdm).
  - LCDM WINS:    Delta lnZ <= -2.5  OR  Delta BIC >= +2.
  - INCONCLUSIVE: anything in between -- and this is the HONESTLY-EXPECTED outcome, since PRTOE is
                  LCDM-like + the m_e signature; a decisive win would be a genuine surprise.
No moving these after the optimizers finish. (Optimizer gives a Laplace ln Z + bestfit chi2 for
BIC/AIC; gold-standard PolyChord ln Z is the eventual publication number.)

## #22 DE-FLOOR — the one serious calculation, RESOLVED (2026-07-08)

`scripts/floor_ghost_condensate.py`. Ran red-team's demanded single calculation of the (delta K)^2 /
ghost-condensate critical-point floor. k-essence P(X): rho=2X P_X - P, p=P, c_s^2=P_X/(P_X+2X P_XX).
RESULTS:
  - w=-1 EXACTLY at P_X=0 (X0), c_s^2=0 there -> exact de Sitter floor. And for X<X0, c_s^2<0 (unstable)
    -> the floor is an ATTRACTOR approached from ABOVE (field cannot sit below it). Good feature.
  - STABILITY: PASS. The c_s^2=0 flat direction is stabilized by the (delta K)^2 k^4 term
    (omega^2 = alpha/M^2 k^4 > 0 for alpha>0; window P_XX>0 & alpha>0, Arkani-Hamed+ 2004). The
    self-tuning TOY RAN AWAY ONLY because it dropped that k^4 term; WITH it, the floor holds.
  - SELF-TUNING: FAIL. V0(=Lambda) is a free, TUNED parameter -- mechanism does NOT explain why
    Lambda is small (Weinberg's no-go stands).
VERDICT (red-team fight-or-concede resolved): KEEP the stable DYNAMICAL w=-1 floor (a real mechanism,
an attractor, better than a bare constant); CONCEDE the self-tuning / "solves the cosmological-constant
problem" claim. Update the least-trusted-joints ranking: the floor is no longer "no working mechanism"
-- it has a stable mechanism -- it just isn't a CC-problem solution (which we should never have claimed).
Net odds effect: mildly favorable (the floor is not a fatal flaw), minus one over-claim retracted.

## CODE-vs-THEORY AUDIT (basement check, 2026-07-08) — the dyad link is NOT enforced in code

Audited the CLASS C source against the model's claims. GOOD: dcdf has a real perturbation sector
(delta/theta/delta_p) -- old gap closed; the w=-1 floor is asymptotic/never-crossed (matches the
#22 ghost-condensate attractor). THREE theory-vs-code GAPS found:
  1. **BIGGEST -- m_e and dcdf are INDEPENDENT in the code.** thermodynamics.c has ZERO dcdf refs;
     m_e is CLASS's generic varying_fundamental_constants (hardcoded step at z=50), disconnected from
     the dcdf field. In the config varying_me and dcdf_rho_inf are independent free params. So the DYAD
     (m_e + dark sector = ONE superfluid) is NOT enforced -- the fit tests "dcdf + free m_e step", not
     "one linked superfluid". Consequences: (a) the #11 amplitude derivation (eps = c*f_amp*Psi0/M_red)
     is NEVER tested by the fit -- m_e is just a free number; (b) part of the "competitive with LCDM"
     result comes from the extra freedom of 2 independent knobs, not the constrained dyad.
  2. Screening is a hardcoded REDSHIFT step (z=50), NOT the density-dependent Theta-saturation the
     model claims -> the void m_e-step (#10) physics is not in the code (why it was demoted).
  3. The w=1/3 radiation-like phase is ABSENT (dcdf starts as dust w~0); the claimed 1/3->0->-1 is
     really 0->-1 in code. The conformal-origin c=1 argument (#17) rests on this unimplemented phase.
  (Unverified: whether cs2_dcdf enforces c_s^2=0 at the floor -- function body in an unlocated header.)
HONEST IMPLICATION: the fit is of a MORE FLEXIBLE model than the theory. To test the actual dyad,
ENFORCE the link (derive m_e from dcdf params per #11, fix the transition from screening physics,
re-fit with m_e no longer free) -- the constrained dyad may fit worse. Any paper MUST state that the
fit uses an effective parametrization with independent m_e; the linked superfluid is the theoretical
claim, not directly tested. This reframes the odds: the fit's competitiveness is partly unenforced freedom.
