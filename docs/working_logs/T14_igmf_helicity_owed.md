# T14 IGMF helicity (the chirality family's possible FIRST DATUM) — OWED
1. THE SIGN MAP (load-bearing): the family predicts sign(helicity_B) = sign(n) = the matter draw — but the map owes TWO signs on two different objects. WHICH handedness the genesis flow has (the seeding step, sign(H_kin)) and WHICH handedness corresponds to matter-wins (the AD-direct rectification, sign(θ̇·n)). Until both are explicit, the measured hint cannot be read.
2. The hint's status pass: Tashiro–Vachaspati-class claims (~2σ, left-handed, Fermi parity-odd statistics; disputed) — literature refresh + systematics status.
3. IF the map lands and the hint firms: the family becomes one-measured/two-predicted — the strongest cross-messenger test on the board.


## THE SIGN MAP — structure laid (2026-07-13, post-entry-77; two links owed)

The chain of signs, each link graded:

| link | carries the sign from → to | status |
|---|---|---|
| 1 | the ± residual of the phase-slip anneal (the only surviving dice — the swirl direction around the headless axis is not topologically carried; rotation resets at the crunch) → sign(Γ_ring) | [D-frame] — the coin's home is the quantization event |
| 2 | sign(Γ_ring) → sign(n) (the quantization event: n = Γm/2π preserves sign) | [D] |
| 3 | sign(n) → the winding current's direction (the P-028 engine) | [RECORDED] |
| 4 | the current's direction → helicity_B handedness (left vs right) | **the convention is fixed and then cancels: Harrison's coefficient enters the helicity squared, so H_B = k²·H_kin and sign(helicity_B) = sign(H_kin) exactly. What is owed is sign(H_kin), and sign(n) does not reach it on the recorded structure — the section at the foot of this file** |
| 5 | sign(n) → matter-vs-antimatter (which handedness means matter wins) | **CLOSED, negative. The winding n and rotation θ̇ evolve independently on one trajectory (`scripts/genesis_joint_draw.py`): their joint correlation holds at −0.06 to +0.09 against a ±0.13 floor. Reversing the ring flips n → −n while the charge Q and tilt torque are site-sums that do not move, so every draw's mirror keeps θ̇ and flips n — sign(θ̇·n) is a coin the model cannot call. Injecting a parity-odd term the model lacks makes the correlation appear at once (+0.51/−0.75), so the null is measured, not forced.** |

**The read:** links 1–3 form a connected sign chain from the anneal's coin to the winding
current's direction. **Link 4 does not continue it.** Its conversion step is exact and
convention-free — Harrison's battery maps the medium's vorticity to B through a constant
coefficient, so the seeded magnetic helicity is the flow's *kinetic* helicity rescaled by a
positive number — but the sign it hands on is sign(H_kin), and sign(n) does not reach that object
on the recorded structure. The chain therefore has **two** open junctions, not one:
link 4 (which handedness the genesis flow has) and link 5 (which handedness means matter). They
are different objects and neither substitutes for the other, so **closing link 5 alone still
leaves the measured left-handed hint unreadable** — the cross-messenger test needs both.
Until then: the map is STRUCTURE-COMPLETE, two links from live.

## PAID item 2: the hint's status pass — it survives, and it made a successful prediction

**Recorded status confirmed current, and modestly upgraded.** The claim
[TashiroVachaspati2013; TashiroChenFerrerVachaspati2015; ChenChowdhuryFerrerTashiroVachaspati2015]:
non-vanishing **parity-odd correlators** of Fermi-LAT diffuse gamma-ray arrival directions ⟹ a
**helical** intergalactic field, **B ≈ 10⁻¹⁴ G on ≈ 10 Mpc scales, LEFT-handed** — matching this
file's recorded "~10⁻¹⁴ G-class on Mpc, left-handed" exactly.

**What strengthens it (and was not recorded here before):**
- **It has been stress-tested, not merely fitted:** more stringent data cuts; Monte Carlo with
  Fermi-LAT time-exposure information; **separate Northern/Southern galactic-hemisphere analyses**.
- **It made a successful forward prediction:** the parity-odd correlator's peaks were predicted to
  follow a **simple power-law scaling with gamma-ray energy** *if* sourced by a helical field — and
  that scaling held. A hint that predicted its own energy dependence is a different object from a
  hint that only fits.

**The dispute, stated precisely:** a contrary analysis found **no handedness using Q-statistics** —
but its authors state they **cannot distinguish "no handedness is present" from "the Q-statistic is
not sensitive enough to see it."** That is a **non-detection by a different statistic, not a
refutation**. No point-source-contamination or systematics result was located that retires the
signal.

**Grade: unchanged in kind, upgraded in strength — still ~2–3σ class, still not a detection, no
longer fairly described as merely "disputed."** The honest reading: an anomaly that has survived
its own robustness program and one successful prediction, against one admitted-possibly-insensitive
null. *(Caveat on this pass: read from the literature record, not from re-analysis of Fermi data;
the significance figure is inherited, not independently verified.)*

**This does not make the hint readable.** Item 1's **link 5 (the AD-direct rectification:
sign(n) → matter-vs-antimatter)** is one of the two owed junctions — the other being link 4's
seeding sign, taken apart at the foot of this file. Until both land, a measured
left-handed helicity cannot be turned into a statement about the baryon draw, and the
cross-messenger test does not close. **The 2026-07-16 chirality result sharpens what link 5 must
deliver:** the medium's handedness is sourced from the **genesis pour's winding integer n**, not from
the pairing channel ([PRTOE_dcdf_superfluid.md](../PRTOE_dcdf_superfluid.md) §2 banner;
[PRTOE_cosmological_constant.md](../PRTOE_cosmological_constant.md) §4c) — so link 5 is a statement
about the AD rectification of *n*, and nothing about the condensate's partial wave can supply it.

Coupling-geometry status: medium-sector (web-scale magnetogenesis) — untouched by the gate geometry.

## Link 5 scoped (2026-07-20): the roll's half is a few lines away; the join may not exist at all

Scoping #147 rather than attempting it, because the two halves of link 5 are in very different states.

**Half one — sign(θ̇) — is computable now, from an existing validated script.** The asymmetry rides
the *temporal* phase rotation: baryogenesis records μ = θ̇, so sign(n_B) = sign(θ̇). And
`scripts/genesis_famp_Z4.py` already integrates exactly the roll that generates it, on the model's
own potential (V = m²R² + λR⁴ + 2ε_Aλ R⁴cos4θ, ε_A = 2/9, released at rest at θ_i, scanned over a
uniform prior — "rotation is GENERATED, not assumed"). The generated rotation's sign is present in
that integration as the angular momentum L = x·v_y − y·v_x; the script simply does not record it,
because it reports f_amp. **Adding sign(L) to the θ_i scan gives the distribution of sign(θ̇) over the
prior directly** — whether the first roll picks a definite handedness or splits the prior evenly.

**Half two — the join to sign(n) — may not exist, and that possibility should be held open.** The
helicity rides the *spatial* winding, n = ∮∇θ·dl/2π, set at the Kibble transition by the spatial
variation of θ. The asymmetry rides θ̇, set by the zero-mode roll from θ_i. These are different
components of ∂_μθ, and `genesis_famp_Z4.py` is a homogeneous two-dimensional integration with no
spatial structure — it cannot produce n at all. **Nothing yet identified forces the two to share a
sign**, and if they are independent then link 5 has no mechanism rather than an owed one.

**Which is the honest fork, and it is not the one the chain's framing assumes.** The map reads as
"one owed computation away from a cross-messenger test". It may instead be: the roll gives a definite
θ̇ sign, the Kibble draw gives an independent n sign, and the handedness↔matter correspondence is a
coin the model cannot call. That outcome would *close* T14 item 1 — negatively — and remove the
cross-messenger test rather than deliver it. Worth knowing before the computation is run, so the
result is read as an answer either way rather than as a failure to find the expected one.

**Next step, concretely:** add sign(L) tracking to the θ_i scan in `genesis_famp_Z4.py` and record
the distribution; then, separately, establish whether anything in the genesis links θ_i to the
winding draw. The first is small. The second is the real question.

## Half one, run (2026-07-20): the prior splits evenly, and a symmetry says it must

**The answer is the second branch of the fork above.** Tracking sign(L) over the θ_i scan returns
an even split at every tilt strength ε_A ∈ {0.1, 0.2, 0.3, 0.5} — which brackets the recorded 2/9 —
with Σ L ⁄ Σ|L| at 10⁻¹⁶–10⁻¹⁵: 12 and 12 on the solver's own 24-point prior grid, 30 and 30 on a
60-point scan. The first roll does not pick a handedness.

**And the evenness is exact, for a reason that does not depend on the tilt strength.** The tilt
2 ε_A λ R⁴ cos 4θ is invariant under the reflection σ : θ → π/2 − θ; so are release-at-rest, the
isotropic Hubble friction, and the uniform prior over one Z4 period. The charge L = R² θ̇ is odd
under σ. So each θ_i is exactly mirrored by π/2 − θ_i at equal |L|, equal radial history and equal
f_amp — verified at L(θ) = −L(π/2 − θ) to 5.7×10⁻¹³ and f_amp σ-invariance to 8.2×10⁻¹⁵. Because σ
holds for **any** ε_A, the split is even at the recorded value without needing to be scanned there.

**A CP phase in the tilt does not change it.** With the tilt written cos(4θ + δ), the substitution
φ = θ + δ/4 recovers the δ = 0 problem exactly — equations of motion, L = R² φ̇, and a uniform prior
over a full period are all invariant under a constant shift. One tilt's phase is removable.

**What this does and does not settle.** It confirms the corpus's relative-sign reading — neither sign
is determined alone — and replaces the assertion with a mechanism: a reflection symmetry the uniform
prior does not break. It leaves the product untouched. A repo-wide check confirms half two's
obstruction is structural rather than pending: `genesis_famp_Z4.py` evolves the zero mode with no
winding, `genesis_multicomponent.py` carries the six-channel winding with no time evolution, and no
script holds both. **The product is unmeasured because no instrument computes it**, which is a build
(#154), not an owed calculation.

**Reading it as an answer, as this file asked.** The handedness↔matter correspondence is a coin the
model cannot call *a priori* — that much is now proven rather than suspected. Whether it can call the
*correlation* is what #154 decides, and that is the branch on which the cross-messenger test still
lives.

## Link 4 taken apart (2026-07-20, #158): the convention was never the obstruction

Link 4 was graded "[RECORDED mechanism, SIGN CONVENTION unfixed]". Both halves of that grade fail in
the same direction: the convention is fixable in one line and then *cancels*, and the mechanism run
for its sign rather than its magnitude does not deliver a sign(n)-carried handedness at all.

**What the recorded mechanism actually is.** Not a chiral term and not a Chern–Simons term. It is the
**Harrison (1970) battery**: in the pre-recombination plasma, photon drag spins electrons and ions
differently where the medium rotates, and the charge separation is a current —
B_seed ≈ 2(m_p c/e)·ω_vort ≈ 5×10⁻¹⁸ G at ω_vort ~ 0.5 H(rec)
([PRTOE_cosmic_magnetism.md](../PRTOE_cosmic_magnetism.md) §2; P-2026-028's registry entry). The
chiral route is not merely unused but **forbidden**: the condensate's EM-neutrality is forced to
q_EM < 4.7×10⁻³⁸…10⁻⁴⁷ by the photon-mass bound, so the model "is not allowed to make fields
directly; it is allowed to stir" (same file, §2). Link 4 is a *mechanical* seeding, and it must be
read with a mechanical seeding's geometry rules.

**The convention, fixed — and then it cancels.** Adopt the standard object H_B = ∫A·B d³x with
right-handed positive: a force-free field ∇×B = λB has H_B = (1/λ)∫|B|² d³x, so sign(H_B) = sign(λ)
(checked numerically, force-free residual 9.6×10⁻¹⁵). Harrison gives B = k ω = k ∇×u with
**k = 2 m_p c/e a constant**, so A = k u + ∇φ is a valid vector potential and

  H_B = ∫(k u + ∇φ)·(k ∇×u) d³x = k² ∫u·(∇×u) d³x + ∮ φ ω·dS = **k² H_kin**

— the surface term dying because ∇·ω = 0 and the model's own registered geometry is a *closed* flat
3-torus (P-2026-013). Verified to machine precision on a periodic box for **both signs of k**.
**The Harrison coefficient enters the helicity squared.** Whether B is parallel or antiparallel to
the vorticity — the thing link 4 was recorded as waiting on — makes no difference at all:

  **sign(helicity_B) = sign(H_kin), exactly.**

That much is link 4, derived. It is a real gain: the junction becomes an identity with one named
input, and the corpus already owns that input's functional — H = ∫v·(∇×v) is the same object the
torus/sphere theorem is written in ([PRTOE_cyclic_torus_genesis.md](../PRTOE_cyclic_torus_genesis.md) §7).

**But sign(n) does not reach that input, for two recorded reasons.**

1. **The winding current is curl-free.** The chain hands the winding off as **k₀ = 2πn/L**
   ([PRTOE_THE_CHAIN.md](../PRTOE_THE_CHAIN.md), tether 3→4) — a uniform phase gradient around a
   torus cycle. Then v_s = (ħ/m)∇θ is spatially uniform, ∇×v_s = 0, and u·(∇×u) = 0 pointwise
   (checked at n = ±3). This is exactly the purely-toroidal-current case: **the winding current by
   itself seeds zero helicity**, of either sign. Link 3 delivers a direction and link 4 has no use
   for it.
2. **A bulk rotation carries none either.** The vorticity Harrison actually eats is the flow line's
   ω_vort ~ 0.5 H(rec), a rotation *rate*
   ([PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md), the flow-line row). For any rigid
   rotation u = ½ ω × r, u·ω = 0 identically. A rotation of either sense seeds a field of zero
   helicity.

**Where the helicity does live — and why one integer cannot sign it.** The corpus does record a
helicity-carrying structure: the fountain "rolls up … into a vortex ring; background swirl makes it
**helical**", and a torus-supported Beltrami flow reaches **H/E = 0.998** — maximal twist — where a
sphere gives H = 0 exactly (cyclic-torus file §7 and §9; the same numbers in P-2026-013's second
motivation). But that structure's helicity is **bilinear in its circulations, not linear**: two
linked circulations give H = 2·Lk·Φ_tor·Φ_pol, and a single quantized filament gives
H = Γ²(Wr + Tw) = n²κ²(Wr + Tw) [Moffatt1969]. **In the self-term sign(n) squares away** — checked,
n = +1 and n = −1 return identical H_kin — and in the mutual term the sign is sign(n_tor·n_pol), a
product of the ring's **two** circulations, the "poloidal + toroidal … two counter-rotations" the
corpus names but grades only as a magnitude. The recorded 0.998 is the sphere-can't/torus-must
theorem; the mirror Beltrami flow (λ → −λ) is equally torus-supported and returns −0.998. The sign
was never computed, and `c1_locus_twist.py`, which computed the magnitude, is scratch-era and not
retained.

**The one missing object.** Link 4 owes **the handedness of the genesis roll-up's flow — the sign of
the helical vortex ring's poloidal circulation relative to its toroidal one, i.e. sign(H_kin)**. One
object, and not link 5's: link 5 owes sign(θ̇·n), link 4 owes sign(H_kin). Note what this does *not*
say — it does not strike sign(helicity_B) = sign(n). If the poloidal circulation carries a fixed
genesis-set sense (the buoyant fountain's own axial direction is the obvious candidate) while the
toroidal one is the genome's draw, then sign(H_kin) = sign(n) up to a fixed factor and the recorded
prediction is recovered exactly. If instead the two circulations are locked to each other, the
helicity comes out with a *universal* handedness and the prediction becomes a different — and
sharper — claim. Both live; the missing object decides which.

**What this does to the census's reading.** The census counted link 5 as the single owed junction;
its row now carries both. **A closed link 5 alone leaves the measured left-handed hint unreadable**,
because link 4 is the junction between the current and the observable handedness and it is open on
its own terms.
The two debts share a plausible home — #154's joint genesis draw is the only build in the corpus
that would evolve a genesis trajectory carrying spatial structure — but #154 as scoped reads sign(n)
and sign(θ̇) off one trajectory, while sign(H_kin) needs that trajectory's **three-dimensional
flow**, which the scoping does not yet say it carries. Whether link 4 rides #154 or needs its own
instrument is worth settling *before* #154 is built rather than after.

**Settled (2026-07-20): link 4 does NOT ride #154 as scoped, and the reason is dimensional.**
The two signs are read off objects of different dimensionality. sign(n) is a **loop** integral,
n = ∮∇θ·dl/2π — a topological charge that needs only θ around one circuit. sign(θ̇) is a
**zero-mode** quantity, one number per trajectory. A solver carrying winding plus time evolution
delivers both, which is exactly #154's scope and exactly why that scope is right for link 5.

sign(H_kin) is neither. For a single quantized filament H = n²κ²(Wr + Tw), and **writhe is a
property of the centerline's embedding in three dimensions** while twist is a property of its
internal framing — neither survives reduction to a loop integral or a zero mode. In the mutual
term the sign is sign(n_tor·n_pol), which needs the ring's two circulations as separate
three-dimensional objects, not one winding integer. **A 0D or 1D instrument cannot return
sign(H_kin) at any resolution**; this is a structural limit of what those solvers represent, not
a question of grid refinement.

**So the build order is: #154 as scoped closes link 5 and leaves link 4 exactly where it is.**
Link 4 needs a genuine three-dimensional genesis flow — the same class of object as the granule
sim (#181), and worth checking against it for shared machinery before a third solver is written.
Recorded here so #154 is not built expecting to discharge a debt it structurally cannot reach,
and so the census's row is not closed on link 5's delivery alone.
