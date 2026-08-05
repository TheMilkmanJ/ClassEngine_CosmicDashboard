# Cosmic Magnetism — the Rotation Machine's Receipt (2026-07-11)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Standalone document for P-2026-028, built from recorded structure. One gap remains open (the void
floor). The claim of uniqueness is stated precisely in §5 — the mechanism class is standard; the
source and the sign are not.*

---

## 0. The mystery

Magnetic fields are everywhere: ~μG in galaxies, ~nG-class hints in clusters, and — decisively —
**in the voids**: blazar TeV halo observations imply B ≳ 10⁻¹⁶ G in regions where no dynamo can
ever have operated. The CMB caps any primordial comoving field at ~10⁻⁹ G. Something seeded
fields in the emptiest places in the universe, and the standard model of cosmology has no
linear-order way to do it: **vector perturbations decay; no primordial vorticity survives; the
Harrison mechanism — the natural charge-separation battery — starves for lack of spin.**

The known escape attempts and their pathologies:

| mechanism | field | pathology |
|---|---|---|
| inflationary magnetogenesis | up to nG with tuning | must break conformal invariance by hand; strong-coupling & backreaction problems |
| EW/QCD phase transitions | locally large | coherence length microscopic (horizon at the transition); decays by processing |
| Biermann battery (reionization) | ~10⁻²⁰ G | too late and too small-scale for the void floor |
| Harrison (1970) | ~10⁻¹⁸ G IF vorticity exists | **standard cosmology supplies no vorticity** |

## 1. This model is a rotation machine — the vorticity is structural, not optional

The founding identity is a charged **rotating** superfluid, and rotation in a superfluid is not
a free profile — it is **quantized circulation** (Onsager–Feynman: a rotating
superfluid cannot have n = 0). The recorded sources of spin:

1. **The winding** — the topological n ≠ 0 (Kibble-generated at the first genesis;
 topologically locked through every crunch).
2. **The vortex network** — Kibble domains of comoving size ξ ~ 256 Mpc thread
 the medium with quantized vortex lines.
3. **The genesis helicity** — the AD roll's self-generated rotation (the first-roll theorem).

So the one ingredient Harrison lacked in ΛCDM — primordial vorticity — is here **by identity**:
removing it would contradict the model's own name.

## 2. The seed, computed (the galactic bill — paid)

Harrison's battery: in the pre-recombination plasma, vorticity spins electrons and ions
differently (photon drag couples to them unequally), separating charge into a current:

 B_seed ≈ 2 (m_p c / e) · ω_vort ≈ **5×10⁻¹⁸ G** at ω_vort ~ 0.5 H(rec) (graded)

That is precisely a viable **galactic** seed: compressed and dynamo-amplified over ~30 e-folds
to the observed μG. **The model accounts for the galactic magnetism where ΛCDM cannot** —
a genuine new explanatory front, registered as P-2026-028.

**Consistency, forced:** the seeding runs through the *plasma's* response to the medium's
rotation — never through dark-charge currents, because the condensate's EM-neutrality is
forced to 37–47 orders below unit charge by the Meissner/photon-mass bound
(q_EM < 4.7×10⁻³⁸…10⁻⁴⁷ — P-2026-028's constraint-closed-en-route). The model is not
allowed to make fields directly; it is allowed to stir.

## 3. The void floor — the open gap

The blazar bound constrains the field between structures. The vortex-network rms boost
(×3400) concentrates B on the **filaments/lines**, while the void floor constrains the
**inter-line** field — which stays **~1.5 orders short** on the smooth estimate. Two
candidate rescues fail on inspection: (i) return-flux topology falls to flux
conservation — the return flux through the void cell equals the flux-average, i.e. the
smooth estimate; concentrating B on lines cannot raise the inter-line floor. (ii)
post-recombination vorticity persistence sources the same average and cannot beat the same
theorem. Therefore the void column rides solely on (iii): the blazar bound's own
robustness. The live external debate (plasma instabilities — beam-plasma energy loss may
relax the ≥10⁻¹⁶ G floor entirely) is the referee: **if the blazar floor survives that
debate, P-028's void column fails while the galactic column stands** — the registered risk,
sharpened to a single external question.

### 3a. Void-floor shortfall and RM coherence — priced vs open (2026-08-02)

**The shortfall is arithmetic from recorded numbers; no internal formula closes it.**

| quantity | value | source |
|---|---|---|
| B_seed (smooth Harrison, ω_vort ~ 0.5 H(rec)) | **5×10⁻¹⁸ G** | §2 / P-2026-028 |
| B_void floor (blazar TeV-halo bound) | **≳ 10⁻¹⁶ G** | [NeronovVovk2010] |
| ratio B_void / B_seed | **20** | = 10⁻¹⁶ / 5×10⁻¹⁸ |
| shortfall in decades | **log₁₀(20) = 1.30 dex ≈ "1.5 orders"** | the registered gap |

The inter-line floor equals the smooth estimate under flux conservation: if Φ_line is
concentrated on the vortex network and the return flux through a void cell equals the
cell-averaged flux, then B_inter-line ≲ B_seed regardless of the ×3400 rms boost on the
lines. **No further desk pricing changes that identity** — the shortfall is not an uncomputed
integral; it is a theorem against the two internal rescues already tried.

**What would be needed to close the void column from inside the model (and is not on
record):** a mechanism that raises the *inter-line* field above the flux-averaged seed —
equivalently, a formula for B_void that is not bounded by B_seed under flux conservation.
No such formula exists in the corpus. The open object is therefore either (a) an external
relaxation of the blazar floor, or (b) a new internal seed mechanism — neither of which is
desk-doable from existing numbers without inventing content.

**RM coherence scale — geometric formula paid; amplitude / survey comparison open (2026-08-03).**

§4 notes that the Kibble network sets ~100-Mpc-class comoving structure, "testable in
principle in Faraday-rotation-measure correlation functions." That geometric content is now
on record ([`working_logs/_runs/debt_rm_formula_20260803/REPORT.md`](working_logs/_runs/debt_rm_formula_20260803/REPORT.md);
`scripts/rm_coherence_kibble.py`):

- ⟨RM(n̂₁) RM(n̂₂)⟩ = K² ∬ n_e n_e ⟨B_∥ B_∥⟩ dχ₁ dχ₂ with ⟨B B⟩ structured on ξ_K;
- θ_ξ(χ)=ξ_K/χ, ℓ_geo=χ/ξ_K, ℓ_π=π χ/ξ_K (parameter-free transfer of recorded ξ_K);
- unit-normalized thin-shell shape w(θ)/w(0)=exp(−½(θ/θ_ξ)²);
- **Survey-plane prediction:** at χ ~ 2–5 Gpc, **ℓ ~ 25–60** (do **not** quote ℓ_π≈169 = last-scatter χ_* as “the” RM prediction).

**Still open:** absolute C_ℓ amplitude / catalog comparison (external n_e; galactic RM cleaning);
void floor (below) is **not** touched by this formula.

## 4. The signature no one else can write down: the sign

Every other mechanism predicts a magnitude and (at best) a spectrum. This model's field
inherits **magnetic helicity with a sign tied to the genesis flow**, because the Harrison step
copies that flow's handedness across faithfully. Writing H_B = ∫A·B d³x (right-handed positive) and
using B = k ω with k = 2 m_p c/e a constant, the vector potential A = k u + ∇φ gives

 H_B = k² ∫u·(∇×u) d³x = k² H_kin  ⟹  **sign(helicity_B) = sign(H_kin)** — exactly, on
 the closed 3-torus, with the battery's coefficient entering squared so no sign convention
 survives to be argued over.

The registered routing sign(helicity_B) = sign(n) is that identity plus one structural condition:
that the genesis roll-up's handedness is itself carried by the winding's draw. **That condition is
the sector's open sign question** — kinetic helicity is a linkage, and the two rotations the model
records outright do not supply one. A rigid rotation has u·ω = 0 identically, and the winding
current handed off as k₀ = 2πn/L is a uniform phase gradient, hence curl-free. The handedness lives
instead in the helical vortex ring of §1's third source, whose helicity is bilinear in its poloidal
and toroidal circulations — so the owed object is the sign of one relative to the other
([working_logs/T14_igmf_helicity_owed.md](working_logs/T14_igmf_helicity_owed.md), the seeding
link). The sign chain's links 1–3 are laid; link 4 is this condition, and link 5 is the
rectification below.

**The third leg does not stand, and the file states that rather than assuming past it.** Reading the
helicity back as *which* handedness means matter-over-antimatter needs one further link — the
AD-direct rectification, sign(n) → matter-vs-antimatter. The three-way convergence of matter
asymmetry, helicity and winding on a single draw is the *payoff* of that link, not a standing result:
the asymmetry rides the temporal rotation θ̇, the helicity rides the spatial winding n, and the two
are different components of ∂_μθ.

**One of the two signs is now settled, and it settles as a coin.** The genesis tilt
2 ε_A λ R⁴ cos 4θ is invariant under the reflection θ → π/2 − θ, as are release-at-rest, the
isotropic Hubble friction and the uniform release prior — while the charge L = R² θ̇ is odd under it.
Every release phase is exactly mirrored at equal magnitude and opposite rotation, so sign(θ̇) splits
the prior evenly at any tilt strength, confirmed to machine precision
([working_logs/T14_igmf_helicity_owed.md](working_logs/T14_igmf_helicity_owed.md)). **The absolute
handedness is therefore not something this sector can predict** — not pending a computation, but
forbidden by a symmetry the model's own content does not break.

**The correlation has since been computed, and it is negative.** Whether θ̇ and n are locked
requires one draw carrying both; that joint draw was built and run (2026-07-20), and it finds the
two signs **independent** — the joint correlation sits at −0.06 to +0.09 against a ±0.13 noise
floor, a result forced by the same spatial parity that makes each sign separately a fair coin. So
this sector predicts a helicity sign **relative to the winding**, cannot say which handedness the
matter universe corresponds to, and now knows why: the relative lock does not exist, and its
absence is a symmetry statement rather than a missing computation.

Consequences:
- **Parity-odd observables** (helical-field signatures in radio Faraday statistics and in
 γ-ray halo parity asymmetries) must correlate with a single axis — the winding axis —
 which is also P-024's ε-dipole axis and P-029's comb axis. **Three predictions, one axis.**
- The falsifier that once stood here — a measured magnetic helicity of the wrong sign
 relative to the baryon asymmetry's own sign — is **void, and by the model's own
 computation**: the two signs are drawn independently at genesis, so no measured
 correlation between them can confirm or kill anything. What survives as testable is the
 helicity's sign *relative to the winding*, which is a different and narrower claim.
- The coherence scale is not microscopic: the Kibble network sets ~100-Mpc-class comoving
 structure in the seed — distinctive against phase-transition mechanisms (which cannot reach
 such scales causally) and testable in principle in Faraday-rotation-measure correlation
 functions.

## 5. What is unique here, and what is not (the precise boast)

- **Not unique:** the Harrison mechanism (standard, 1970); the seed magnitude class (~10⁻¹⁸ G).
- **Unique to this model:** (i) a *structural* primordial vorticity source — rotation as
 founding identity, quantized, crunch-proof — where every competitor must add a field or an
 epoch by hand; (ii) the **helicity sign fixed relative to the winding**, sign(helicity_B) =
 sign(n) — the sky's magnetic parity tied to the same topological integer that sets the comb
 axis, though not to the matter–antimatter draw, which §4 shows is an independent sign;
 (iii) the shared-axis triple (ε-dipole, the winding comb, the helicity parity).

## 6. Ledger summary

| item | status |
|---|---|
| galactic seed (~5×10⁻¹⁸ G, Harrison from structural vorticity) | computed, graded, P-028 |
| EM-neutrality consistency (stir, don't charge) | forced (Meissner) |
| void floor (≥10⁻¹⁶ G inter-filament) | **Open — shortfall priced at ×20 = 1.30 dex vs B_seed = 5×10⁻¹⁸ G; no internal formula closes it (§3a)** |
| helicity sign = the seeded flow's sign, sign(helicity_B) = sign(H_kin) | derived (the battery's coefficient squares out of it) |
| helicity sign = winding sign, sign(helicity_B) = sign(n) | the surviving registered content — testable against the winding axis, not against the matter–antimatter draw (§4: the two signs are drawn independently, joint correlation −0.06 to +0.09 against a ±0.13 noise floor) |
| helicity sign = baryon sign | **void** — no measured correlation between them can confirm or kill anything |
| RM coherence ~ Kibble ξ | **Geometric two-point + multipole transfer paid** (`rm_coherence_kibble.py`; survey ℓ~25–60); absolute amplitude / survey fit **open**; void floor **unchanged open** (§3a) |

## Sources

[Harrison1970] (the vorticity battery — the mechanism this file inherits), [NeronovVovk2010]
(the blazar TeV-halo void floor, ≳10⁻¹⁶ G — this file's falsifier), [Onsager1949] +
[Feynman1955] (quantized circulation), [Kibble1976] (the domain network), [Biermann1950],
[Durrer2013] (the magnetogenesis review and its pathologies). Full list:
[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

*Everyone else must explain where the spin came from. This model cannot explain where it would
have gone: a rotating superfluid universe magnetizes its plasma as surely as it swings its
vortices — and it signs the work with the winding integer that also fixes the comb axis.*

---

## Claims ledger & residual freeze (2026-08-04) — above story-grade discipline

**Stamp:** OPEN-THEORY honesty. Galactic Harrison seed stays graded; **void floor remains OPEN-BLOCKED** (×20 / 1.30 dex short). RM geometric scale reconfirmed PASS; absolute σ_RM and void B not closed.  
**Reconfirm package:** [working_logs/_runs/open_theory_full_20260804/](working_logs/_runs/open_theory_full_20260804/) (`rm_coherence.log` **PASS**).  
**Parent debts:** [debt_magnetism_20260803/REPORT.md](working_logs/_runs/debt_magnetism_20260803/REPORT.md); [debt_rm_formula_20260803/REPORT.md](working_logs/_runs/debt_rm_formula_20260803/REPORT.md). Companion: [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md).  
**Currency (2026-08-05):** Void floor ×20 residual **OPEN-BLOCKED** (1.30 dex classic). Door A external lit pass **done** — robust floors still ~1–3×10⁻¹⁷ G (> seed); dissolve **not** met; void **FAIL not fired**; still OPEN intermediate. Package: [void_door_A_lit_20260805/](working_logs/_runs/theory_residual_blue_20260805/void_door_A_lit_20260805/). RM \(n_e\) absolute amplitude **OPEN** (geometric scale paid). Exhaust: [T-W6_Void_IGMF.md](working_logs/_runs/theory_exhaust_20260805/mb/mb_walls_exhaust/T-W6_Void_IGMF.md); shelf RM reconfirm [desk/shelf_desk_exhaust/](working_logs/_runs/theory_exhaust_20260805/desk/shelf_desk_exhaust/); [audit/POST_EXHAUST_AUDIT.md](working_logs/_runs/theory_exhaust_20260805/audit/POST_EXHAUST_AUDIT.md).

| # | Claim | Grade | Evidence | Residual / blocker | **Forbidden** |
|---|---|---|---|---|---|
| 1 | Structural primordial vorticity supplies Harrison’s missing spin | **interpretation** / structural | §1; Onsager–Feynman / Kibble seating | Mechanism class (Harrison) is standard | Uniqueness of magnitude class without dynamo |
| 2 | Galactic seed B ≈ 5×10⁻¹⁸ G at ω_vort ~ 0.5 H(rec) | **machine-backed** / graded | §2; P-2026-028 | Viable seed class, not observed μG without dynamo | Quote as observed void field |
| 3 | EM-neutrality: stir plasma, do not dark-charge magnetize | **derived** / forced | §2; Meissner/photon-mass bound | — | Dark-charge magnetogenesis as model path |
| 4 | sign(helicity_B) = sign(H_kin) (Harrison k²) | **derived** | §4 | — | Absolute sky sign without link-4 production |
| 5 | sign(helicity_B) = sign(n) conditional on poloidal–toroidal relative | **OPEN-BLOCKED** (OPEN-MACHINE) | §4; [T14_igmf_helicity_owed.md](working_logs/T14_igmf_helicity_owed.md); [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md) | Overall seeding sign; no production booking | Production T14 overall sign from smoke/partial i6 |
| 6 | Helicity sign = baryon sign | **failed / void** | §4; `scripts/genesis_joint_draw.py` | Independent draws | Matter–helicity three-way lock |
| 7 | Void floor ≥10⁻¹⁶ G inter-filament vs model inter-line ≲ B_seed | **OPEN-BLOCKED** | §3a: shortfall log₁₀(20)≈**1.30 dex**; [debt_magnetism_20260803](working_logs/_runs/debt_magnetism_20260803/REPORT.md) | **WATCH-EXTERNAL** (blazar floor debate) **or** new internal seed axiom — no desk close | Close void column from RM formula or Harrison seed alone; invent B_void boost |
| 8 | RM geometric two-point / multipole transfer from ξ_K | **machine-backed** / derived-conditional (scale) | [debt_rm_formula_20260803](working_logs/_runs/debt_rm_formula_20260803/REPORT.md); `scripts/rm_coherence_kibble.py` (reconfirm PASS 2026-08-04) | Survey ℓ~**25–60** (χ 2–5 Gpc); not ℓ~169 as RM catalog. Amplitude / n_e **OPEN** | Quote ℓ_π≈169 as survey RM prediction; absolute σ_RM without n_e |
| 9 | Magnetic polarity / ρ_B as bounce *turn* engine | **failed / retired** | `scripts/bounce_magnetic_flip_nogo.py` | Orthogonal to void-floor gap | Bounce-from-magnetism reopen |

### Residual freeze (named OPEN-BLOCKED)

| Residual | Grade | Blocker path / axiom | What would unstick |
|---|---|---|---|
| Void B floor ×20 shortfall | **OPEN-BLOCKED** | [debt_magnetism_20260803](working_logs/_runs/debt_magnetism_20260803/REPORT.md) §1–2; blazar ≳10⁻¹⁶ G vs B_seed 5×10⁻¹⁸ G | External floor revision **or** licensed new seed/amplification (not inventable at desk) |
| RM absolute amplitude | **OPEN** | needs external n_e model | Survey n_e + transfer; scale already paid |
| Overall sign(H_kin)/link-4 | **OPEN-BLOCKED** (OPEN-MACHINE) | T14 four-branch production criteria; [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md) | Production booking under pre-registered gates only |

**Non-claims:** Void column closed internally; absolute σ_RM without external n_e; matter–helicity lock; uniqueness of Harrison magnitude class; bounce from magnetism; treating last-scatter ℓ_π≈169 as the catalog RM prediction; production T14 sign from incomplete runs.

**Triage:** elevate-in-place; **blocked** on void floor (WATCH-EXTERNAL / missing internal seed); RM *scale* paid, amplitude/survey still open; galactic column stays graded.

**Debt wire (2026-08-04):** RM scale reconfirmed in `open_theory_full_20260804/rm_coherence.log`; void floor still OPEN-BLOCKED (×20 short).
