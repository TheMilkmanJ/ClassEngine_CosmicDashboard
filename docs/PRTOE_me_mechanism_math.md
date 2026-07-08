# The m_e Mechanism: Consolidated Mathematical Formulation

*Assembled 2026-07-07. This is the EQUATIONS-ONLY companion to
`PRTOE_me_trigger.md` (which holds the reasoning, the dead ends, and the
red-team dialogue). Every result here is cross-referenced to its trigger-doc
section. Status tags: [DERIVED] solid, [BOUNDED] size/ceiling fixed but not
exact, [OPEN] owed, [FORCED] required by multiple independent constraints.*

---

## 0. The claim, in one line

The electron mass carries a fractional environmental shift
`m_e(x) = m_e^lab * [1 + eps * S(x)]`, where `S(x)` is a sharp/binary
"smoothness" indicator (1 in unstructured space, 0 in virialized structure)
and `eps ~ 1.24%`. The CMB is imprinted at the bare value `m_e^lab*(1+eps)`;
all present-day (virialized) measurements see `m_e^lab`.

---

## 1. The environmental variable [DERIVED]

The medium is a complex superfluid order parameter (Room 1):

    Psi(x) = |Psi(x)| * exp(i * xi(x))

The coherence/smoothness indicator is built from the phase field. Define the
multi-stream (shell-crossing) bit via vorticity of the phase-gradient
velocity `v = grad(xi)`:

    Theta(x) = 1  if the medium is single-stream (smooth, curl-free, coherent)
    Theta(x) = 0  if multi-streamed / vortex-tangled (structured, decohered)

Key identity (exact): curl(grad(xi)) = 0 for any smooth single-valued phase,
so Theta can only flip at genuine phase defects (vortices) -- structure.
[trigger-doc sec 3, 20]

Smooth observable proxy: the Weyl curvature invariant C^2, which is
IDENTICALLY ZERO in conformally-flat FRW and nonzero only where tidal
structure exists:

    S(x) = f( C^2(x) / C_ref^2 ),   f = a near-step (saturating) function

---

## 2. The coupling [OPEN legality / FORCED form]

    L_int = -eps * S(x) * m_e^lab * (psi_e-bar psi_e)

This is a direct, dimension-5, Planck-suppressed moduli/dilaton-class
operator with S(x) the environmental modulator. Legality under the coupling
census: OPEN (narrow reading -> legal; broad -> forbidden; red-team turns
61-65). Form: FORCED (geometry is 60 orders too weak, sec 32, so a direct
operator is unavoidable). [trigger-doc sec 23, 32, 34]

---

## 3. The functional form is FORCED SHARP [DERIVED / FORCED by 2 constraints]

Requirement A (MICROSCOPE, sec 26): the residual shift inside structure must
satisfy the Eotvos bound. Differential Ti/Pt sensitivity:

    d ln M_atom / d ln m_e  =  Z - E_bind/m_e ,   E_bind = 15.73 * Z^(7/3) eV
    (Ti: 2.517e-4 ;  Pt: 2.171e-4 ;  differential: 3.46e-5)
    => residual |delta m_e/m_e| at Earth  <  8.7e-11

Requirement B (quasar, sec 7/12): a smooth density-dependence gives absorber
differentials 1e4 over bound -> binarity FORCED.

Consequence: a gentle exponential fails -- the curvature gap between
recombination and dwarf cores is only ~22x (1.35 decades) but the required
suppression is 8.2 decades. Minimum power:

    S(x) = exp[ -(C^2/C_ref^2)^n ] ,   n > 2.43   [FORCED, sec 27]

i.e. a near-threshold/step. Both independent constraints force the same
sharpness -> two-constraint pillar. Once suppressed at the dwarf core,
Earth (17 decades higher C^2) is automatically suppressed. [sec 26, 27]

C_ref is NOT a free scale: the transition is set by a topological event
(first shell-crossing / first vortex), not a tuned curvature value. [sec 27]

---

## 4. The amplitude [BOUNDED, coefficient OPEN]

Ceiling (sec 31): only the ELECTROMAGNETIC part of m_e can respond to an
EM-binding environment. Split:

    m_e = m_bare(Higgs-Yukawa, ~99%) + delta_m_EM(self-energy, ~1%)
    delta_m_EM/m_e = (3 alpha / 4pi) * ln(Lambda^2/m_e^2)  ~  1-2%  (O(alpha))

So eps <= (EM self-energy fraction) ~ 1-2%. The observed 1.24% sits AT the
ceiling. Size DERIVED; exact value needs Lambda (cutoff, ~18 MeV -- not yet
motivated) and the modulation fraction. [sec 28, 31]

Why m_e and not alpha: varying-alpha killed by quasars (45-100x); m_e evades
those bounds -- the surviving EM-binding knob, selected by data. [sec 7, 29]

---

## 5. Which curvature piece, and why [DERIVED, 3 independent reasons]

The trigger couples to WEYL (tidal/radiative), not RICCI (local/binding):
  R1. Ricci fails directionally -- large at BOTH high-z background AND in
      halos, cannot distinguish smooth-dense from clumped. [sec 25]
  R2. Weyl = 0 identically in smooth FRW (conformal flatness) -- exactly the
      "bare in smooth space" requirement. [sec 23]
  R3. The switch fires on a DECOHERENCE event; decoherence is driven by a
      force's RADIATIVE/far piece; Weyl IS gravity's radiative piece; Ricci
      (binding piece) cannot trigger a decoherence event. [sec 30]

Near/far force split (general): every long-range force = near piece (binds)
+ far/radiative piece (carries info away = decoheres). EM: Coulomb binds,
photons decohere. Gravity: Ricci binds, Weyl decoheres. [sec 30]

---

## 6. The amplitude-channel constraint (why the roof is one question) [DERIVED]

A viable channel must be simultaneously STRONG [S] (O(alpha), not curvature-
suppressed), LEGAL [L] (census + MICROSCOPE), VARYING [V] (smooth vs
structured). Scored:

    curvature       : L,V   not S  (60 orders weak, R/m_e^2~1e-69)
    direct coupling : S,V   not L  (census scope, OPEN)
    khronon/frame   : S,L   not V  (spatially uniform)
    intrinsic dm_EM : S,L   not V  (present everywhere equally)

Only the direct coupling has S+V; its sole missing property is L, and
MICROSCOPE-safety within L is already delivered by the sec-27 sharp
screening. => the whole roof reduces to the census-scope question. [sec 34]

---

## 7. The EP escape (fifth-force gate) [RESOLUTION DIRECTION, computation OPEN]

Smooth dilaton: needs beta~0.012, MICROSCOPE allows beta<~1e-4 -> 2 orders
over -> DEAD. [red-team turn 64]

Escape: the field is the SHARP/SATURATED Theta (sec 27 sharpness), not a
smooth dilaton. Inside the virialized MW halo Theta is at its ceiling ->
grad(Theta) ~ 0 (flat top) -> grad(phi) exponentially suppressed -> no
fifth force. Chameleon-class screening; screening agent = Theta saturation
(forced, not tuned). Freezing agent = VIRIALIZATION (medium's own dynamics,
static in a virialized halo). [defender turn 65]

Screening-test corroboration (sec 37, computed): atomic clocks are a GENUINE
third independent leg -- they kill the continuous version via temporal physics
(a continuous 1% coupling gives ~1e-4 clock modulation, ruled out), while the
saturated form predicts a null (observed). Caveat: clocks force the screening-
CONSEQUENCE, not the sharp-form-CAUSE uniquely. White-dwarf spectroscopy =
consistency-check (saturated -> lab value, confirmed ~1e-5). Continuous version
now killed by TWO independent experiments (quasar spatial + clocks temporal).

OWED COMPUTATION (make-or-break):
  (i)   eps = 1.24% at recombination (Theta~0, smooth), AND
  (ii)  saturated-Theta screening: grad(phi) < MICROSCOPE at Earth AND
        clears the reopened chameleon/Casimir/EP bounds, AND
  (iii) virialization delivers freezing (Theta static by medium EOM), AND
  (iv)  quasar delta_mu/mu ~ 0 (all virialized absorbers Theta-saturated).
Screening machinery is cousin to the abandoned v1-v3 sector -> must earn
its place fresh (graveyard Rule 3), inherits nothing. [turn 65]

---

## 8. Observable signature [DERIVED, testable]

Under a single m_e amendment, ALL EM-binding observables shift in LOCKED
correlation (sec 29):

    binding energies (Rydberg ~ m_e):        +1.24%
    atomic sizes (Bohr radius ~ 1/m_e):      -1.24%
    transition frequencies:                  +1.24%
    21-cm hyperfine (~m_e^2/m_p):            ~+2.5%

Discriminator: the dark-ages/cosmic-dawn 21-cm sky (unvirialized IGM,
Theta~1, BARE value) vs the standard (virialized) sky. A specific
CORRELATED pattern across all EM-binding observables, not a single-line
shift. [sec 8, 29] REACH/SKA-low class instruments.

---

## 9. What is DERIVED vs OPEN (honest ledger)

DERIVED / FORCED:
  - the environmental variable (Theta, vorticity-based, exact identity) [1]
  - the coupling FORM is forced (geometry 60 orders too weak) [2]
  - the transition is FORCED sharp by 2 independent constraints [3]
  - Weyl not Ricci, 3 independent reasons [5]
  - the amplitude SIZE/CEILING (EM self-energy fraction, ~1-2%) [4]
  - the roof reduces to ONE question (census scope) [6]
  - the locked-correlation observable signature [8]

OPEN:
  - census-scope legality (a/b) -- reproduce the census derivation [2,6]
  - exact amplitude coefficient (cutoff + modulation fraction) [4]
  - the EP-screening computation (grad phi < MICROSCOPE; chameleon bounds) [7]
  - virialization-delivers-freezing, from the medium's EOM [7]
  - the two-field sims (#11): confirm S=(1+f_rot^2)/2, psi/chi layering [trigger-doc]

The empirical fit (m_e = 1.0124, fits the CMB) is UNTOUCHED by all of the
above -- this document concerns the MECHANISM's legality/derivation, not
the data.
