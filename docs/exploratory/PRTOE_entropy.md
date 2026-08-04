# Entropy in PRTOE — one page, four statements (2026-07-18)

> **EXPLORATORY — not OEM claim authority (2026-08-04).**  
> Not living shelf / not closed theory. Consolidation page — not expansion core OEM.  
> Nearest living: [`../PRTOE_quantum_gravity.md`](../PRTOE_quantum_gravity.md) (area-law).  
> **Page curve OPEN.** Residual freezes: [`../working_logs/_runs/`](../working_logs/_runs/).

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](../PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](../PRTOE_DEPENDENCY_TREE.md).*

> A consolidation, not a new result. The model makes four separate entropy statements that lived
> in four different files with no single home. This page states each one and points to where its
> derivation lives. Nothing here is derived for the first time; the only claim the page itself
> makes is that these four are the whole list.

## 1. The beginning's entropy — why it was low

The first cycle begins in the vacuum state: the one state that requires no choice. Minimal
coarse-grained **gravitational** entropy follows from uniqueness rather than from luck, which
is what Boltzmann's question was actually asking about. The gravitational measure is the Weyl
curvature (Penrose's hypothesis): identically zero in a smooth beginning, and monotonically
accumulating as structure forms in the **metric-on** regime — an arrow that is **restored
after the bounce** (see [PRTOE_arrow_of_time.md](PRTOE_arrow_of_time.md) §2b). Weyl growth
that cannot be undone by a contraction still compounds **across metric-on epochs**; it is
not a claim that the C² meter is defined while the metric is off.

**The functional.** S = −Tr(ρ̂₁ ln ρ̂₁), the von Neumann entropy of the medium's one-body
density matrix — the Penrose–Onsager object whose largest eigenvalue defines condensation.
It vanishes exactly when that matrix is rank one (a single macroscopically occupied mode), so
**full coherence is the unique zero and any fragmentation makes it strictly positive**: the
beginning's minimality is a rank condition, not a definition. Growth is sourced where the
phase multi-streams — the same event the Weyl invariant tracks — so §1's Penrose connection
becomes a mechanism rather than a postulate; decrease is suppressed by e^(−N) in the fragment
count. Evaluated today with the recorded healing length: ~10³⁶ k_B, subdominant to the
black-hole budget by ~70 orders. **The functional supplies the theorem and the mechanism, not
the entropy budget.**

The uniqueness step is a theorem; the numerical budget was never this functional's job. Home:
[PRTOE_arrow_of_time.md](PRTOE_arrow_of_time.md).

## 2. The medium's own split — zero-entropy ground state, entropic excitations

Landau's two components do the model's thermodynamic bookkeeping: the condensate ground state
carries zero entropy (and is the w = −1 sector — timeless, ageless by theorem), while the
excitations carry all of it (light, matter, observers, and the arrow they experience). This is
why the dark-energy sector has no thermal history and the dark-matter sector has all of one:
they are two components of one fluid, not two substances.

Inherited from two-fluid hydrodynamics. Home: [PRTOE_MATH_SPINE.md](../PRTOE_MATH_SPINE.md) §10.

## 3. Horizon entropy — located, and its coefficient adopted

Black-hole entropy lives in the thermal core the model puts where the singularity was. The
area law S = A/4 is not derived here: it is adopted from induced gravity, where the same
one-loop content that generates Newton's constant generates the horizon entropy with a
universal ratio (the species-cancellation mechanism). The model's own contribution is
locating the entropy in a real thermal object rather than on a mathematical surface.

**The scaling, derived from the medium (2026-07-18).** Counting horizon entanglement across
the medium's own coherence cells gives S = η·N·A/ξ², while induced gravity gives
1/G ≈ N/(12πξ²) from the same species count and the same cutoff. In the ratio **both cancel** —
which is precisely the universality the literature reports — leaving S/(A/4G) = 48π·η. So the
medium reproduces the area law's *form and its independence of the species content* — and the
pure number η is supplied conditionally by the same structure: the coefficient is the ratio of
the two heat-kernel coefficients under the medium's own Bogoliubov regulator, 12π/48π = 1/4
exactly (§5; [PRTOE_quantum_gravity.md](../PRTOE_quantum_gravity.md) §4a). **The entanglement-side
check is paid (2026-07-20), and structurally**: the conical deficit's R-delta makes the horizon
area term the *same* heat-kernel coefficient that generates 1/G, so any regulator multiplies both
by one factor and cancels in the ratio — the quarter is regulator-independent.

**The roster extension (2026-07-28,** `scripts/area_law_roster_extension.py`**).** For the full
field content the two divergences split per class, and the literature has adjudicated each
split: spin-½ produces no contact term and preserves the ratio exactly (Kabat 1995; the
induced-gravity program's standard result); gauge fields break the naive ratio by Kabat's
contact term, which Donnelly & Wall identify as the edge modes' own entanglement entropy — with
edge modes counted as horizon entropy the ratio is restored; and a conformally coupled scalar
drops out of both sides identically, which the Higgs does under the same ξ = 1/6 condition the
induced-G finiteness already requires. Bookkeeping over the model's roster: 63% of the units
(the 48 Weyl fermions and the medium's minimal scalars) carry the quarter unconditionally, and
the remaining 37% (the fifteen gauge bosons) carry it under the one modern-standard commitment
that edge modes are physical horizon entropy. The quarter therefore survives the full roster at
candidate grade with that single named commitment; rejecting edge-mode entropy would break the
gauge sector's share, and that is the extension's kill.

**Status (2026-08-02), area-law roster — so it cannot be misread:**

| piece | status |
|---|---|
| scaling + coefficient (minimally coupled scalars; regulator structural) | **complete** — paid |
| roster extension (full field content; edge-mode commitment named) | **complete** at candidate grade |
| Page-curve *dynamics* (phonon flux off a finite core) | **open** — separate computation; *not* an area-law residue |

Located by the model, with the scaling derived and the coefficient derived for the full roster
at candidate grade (one named commitment; the regulator's entanglement-side check is
structural). **This payment removes only the *coefficient* obstacle; Page-curve dynamics remain OPEN**
([PRTOE_information_paradox.md](PRTOE_information_paradox.md)) — coefficient and roster complete;
the dynamical curve is not an area-law residue and is **not** claimed closed. Homes:
[PRTOE_blackholes_no_singularity.md](../PRTOE_blackholes_no_singularity.md),
[PRTOE_quantum_gravity.md](../PRTOE_quantum_gravity.md).

## 4. The gas entropy floor — what the screening transition deposits

When the medium re-phases around collapsing gas, the electron's rest energy changes by
ε·m_e = 6.41 keV. Because the transition is a **phase answering the local curvature** — it
re-arranges in place rather than standing as a surface for gas to fall through — a gas element
picks up only the fraction of that difference it actually traverses:

> **ΔE = E_ball · f,  E_ball = ε·m_e/3 ≈ 2 keV (the step's ballistic share),  f = v_gas/c_s**

— the transition's spatial width is however far the medium's own re-phasing travels while the
transition happens, so the transition time cancels and only the speed ratio survives; and of the
full 6.41 keV rest-energy step, a traversing element picks up the kinetic third. With the
medium's sound speed c_s = √(3α)·c = 44 000 km/s against ordinary infall near 1000 km/s,
f ≈ 0.023: **~50 eV per particle, adding ~50 keV cm² of entropy** — below the 100–300 keV cm²
floors groups actually show, and large enough to be a real contributor rather than a rounding
error.

**The signature, and its honest ceiling.** The contribution scales with infall speed, reaching
~150 keV cm² at merger-shock velocities — a velocity-dependent floor contribution rather than
a universal one. But it stays **bounded and sub-dominant throughout**: even at the fastest gas
motions in the universe the fraction traversed is f ≈ 0.07, because the medium re-phases some
fifteen times faster, so the pickup never exceeds a few per cent of what the shock itself
supplies. **That also makes it undetectable in practice** — a few-per-cent temperature boost in
merging systems is degenerate with the merger boost already known to be there and modelled with
its own systematics. So this channel neither threatens the model nor tests it; it is a real
contribution living inside a larger effect.

**What this replaces:** the entropy floor was once named as the delivery mechanism for the S₈
suppression. It cannot be — at ordinary speeds it is too small, and the wall reading that
would make it large enough is excluded by an order of magnitude. S₈ delivery rests on the
pre-registered rotation-shed parameter instead ([PRTOE_FAILURES_LEDGER.md](../PRTOE_FAILURES_LEDGER.md)).

**The high-velocity treatment, supplied 2026-07-28** (`scripts/entropy_front_high_velocity.py`,
7 checks; the slow-limit numbers above are reproduced first, so this extends the construction rather
than replacing it).

**Status (2026-08-02), high-velocity section — so it cannot be misread:**

| piece | status |
|---|---|
| saturation law f = min(1, v/c_s); ceiling; Landau identity of threshold | **complete** — paid (7/7 checks) |
| cluster / thermal-gas application (all known systems subcritical) | **complete** — high-velocity correction to cluster entropy is nil |
| detectability of the AGN/jet crossing | **open as a claim** — coupling unfixed; *not* an open half of the treatment above |

The traversed fraction f = v/c_s is a *fraction*, so the linear law can only hold while v < c_s, and
the correct statement is f = min(1, v/c_s). Saturation gives a ceiling of E_step/3 ≈ 2140 eV per
particle — well above the 100–300 keV cm² floors groups show. So the channel is bounded by its
ceiling, not by the law being intrinsically small.

That saturation velocity is the same c_s as the Landau critical velocity of this condensate, and not
by coincidence: both measure how fast the medium re-phases. Below it the medium stays ahead of the
traversing element, the pickup is adiabatic, and Landau forbids any excitation, so the entropy gained
is reversible work rather than dissipation. At and above it the fraction saturates and the excitation
channel opens together. The two regimes are qualitatively different with a sharp line between them.

Nothing made of gas reaches that line. The fastest cluster merger known sits at v/c_s = 0.113, so
the slow-limit treatment is valid everywhere this file applies it and the high-velocity correction to
cluster entropy is nil. The threshold *is* crossed by AGN ultra-fast outflows, whose measured
velocities run from roughly 0.03 c to 0.3 c and therefore straddle √(3α)·c = 0.148 c, and by
relativistic jets. Whether the crossing is observable needs the matter–medium coupling, which is not
fixed, so no detectability claim is made — only that the line falls inside an already-measured,
already-velocity-binned population, and that this is a different observational programme from the
entropy floor entirely.

## 5. What the model does not claim about entropy

- The area law's coefficient is **the ratio 12π/48π = 1/4** of the induced-Newton and entanglement heat-kernel coefficients, both regulated by the medium's own Bogoliubov cutoff ([PRTOE_quantum_gravity.md](../PRTOE_quantum_gravity.md) §4a). The coefficients 12π and 48π are those of minimally coupled scalars, so the cancellation does not *automatically* extend to the roster the model carries — but the extension has been made (§3): spin-½ preserves the ratio exactly, gauge fields restore it once edge modes are counted as horizon entropy, and conformally coupled scalars drop out of both sides under the same ξ = 1/6 that induced-Newton finiteness already requires. Candidate grade, on the single commitment that edge-mode entropy is physical.
- No claim that the medium's entropy is the universe's entropy budget — the functional in §1
  is real but subdominant by ~70 orders; the budget is dominated by black holes.
- No entropic-gravity reading: gravity here is induced by one-loop content, not by an entropy
  gradient — the two pictures are not mixed.
- No claim that the second law is emergent or approximate: it holds, and its low-entropy
  initial condition is what the model addresses.

## Sources
[Penrose1979] (the Weyl curvature hypothesis), [Landau1941] (two-fluid components),
[Bekenstein1973],[Hawking1975] (horizon entropy), [FrolovFursaevZelnikov1997] (the
species-cancellation ratio), [Tolman1934] (cyclic entropy accumulation). Full list:
[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

---

## Claims ledger & discipline (2026-08-03) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | First-cycle low entropy by uniqueness (gravitational / Weyl measure) | **derived** (with arrow_of_time) | §1; arrow_of_time | Our-cycle gap open there |
| 2 | Condensate ground state zero-entropy; excitations carry entropy | **interpretation** (two-fluid inheritance) | §2; MATH_SPINE §10 | Landau bookkeeping |
| 3 | Area-law scaling + coefficient 1/4 (minimal scalars) | **complete** (paid) | §3; `quantum_area_law_quarter.py` | — |
| 4 | Roster extension at candidate grade (edge-mode commitment) | **complete-conditional** | `area_law_roster_extension.py` | Rejecting edge modes kills gauge share |
| 5 | Page-curve *dynamics* | **OPEN-BLOCKED** | §3 status table | **OPEN-MACHINE:** phonon flux off finite core |
| 6 | Gas entropy floor from screening ΔE = E_ball · f | **derived-conditional** / **estimate** | §4 | Coupling not fixed; no detectability claim |
| 7 | Four statements are the whole entropy list | **interpretation** (consolidation) | banner | No new derivation in this file |

**Non-claims:** not universe entropy budget; not entropic gravity; not second-law emergence.

**Triage:** elevate-in-place. Physics ceiling: area law paid; Page dynamics **OPEN-BLOCKED**.
