# Bounce Derivation Workplan

Goal: derive the bounce, not just name it — and when derivation is not available, say so.

This note collects the hard clues already in the corpus and turns them into a working checklist.
Nothing here is promoted unless another file already supports it.

**Standing admission (2026-07-25):** the classical turn mechanism is not in the current
corpus. Regime caveat and watch-face constraints are in the sections at the end of this
file. Constraints are not derivations.

## What is already established

- Local white holes are forbidden in a globally time-oriented medium.
- The white-hole analogy is candidate-grade only; it is not the derivation source.
- The compact-torus expansion-energy ledger gives a real zero-net-energy cancellation on the flat background.
- The rotating condensate alone cannot supply a BKL-safe stiff phase at sub-Planckian amplitude.
- The cyclic-genesis file says the bounce is two-component: condensate quartic floor plus Tolman-kept radiation.
- The negative bare vacuum is necessary for turnaround, but not sufficient for the bounce profile.
- The dCDF is already derived in its core structure: exact `w = −1`, derived onset/crossover, and a finite quartic floor.
- The white-hole pour remains candidate-grade: a white-hole-like causal event, not a fully derived bounce mechanism.
- The boundary-point reading is now live: if the bounce is the first instant of the next time branch, the local-white-hole counterparty objection does not apply in the same way, but the handover dynamics still have to be derived.
- Candidate mechanism statement: the contracting branch heats until the normal component wins, the condensate gives way at `T_c`, and the boundary becomes the release event; the test is whether that same threshold can also feed `ρ_X(T)` or `Ḟ(T)` strongly enough to make `H = 0` and `Ḣ > 0`.
- White-hole-side upgrade limit: the white-hole analysis can sharpen the branch-boundary framing, but it does not itself create the missing crunch-sector source term. So the reversal mechanism is not hidden in the white-hole label; it still has to come from a sector-local `ρ_X(T)` or branch-changing `Ḟ(T)`.

## The equations that already matter

- FRW balance:
  - `H^2 = (8 pi G / 3) rho`
  - `dot H = -4 pi G (rho + p)` in the standard sign convention
- Bounce condition:
  - `H = 0` at the handover
  - `dot H > 0` at the same point
- Acceleration sign:
  - `rho + 3p` controls the sign of the cosmic acceleration equation
- Rotating-sector no-go:
  - `w = (n - 2)/(n + 2) <= 1` for polynomial tracking
  - kination needs trans-Planckian amplitude in that sector

## The tasks

1. Write the bounce-sector total stress-energy in plain FRW language.
2. Identify which component supplies the turning sign and which component supplies the hot-start energy.
3. Derive the handover condition from the compact-torus energy balance, not from the white-hole analogy.
4. Check whether the negative bare vacuum plus Tolman-kept radiation can produce the required sign change by itself.
5. If not, identify the missing stiff or effectively stiff component and state it as the load-bearing open variable.

## What would count as a real derivation

- The turning point is located by equations, not narrative.
- The source of the turn is named in the stress-energy tensor.
- The hot-start temperature is matched by the same solution that gives the turn.
- The result survives the BKL/Tolman objections without importing a hidden postulate.

## What would fail the attempt

- If the bounce still needs an exterior counterparty.
- If the rotating condensate is used as the stiff source despite the no-go.
- If the workplan ends with "candidate" where the turning profile should be.
- If the derivation only restates the white-hole analogy.

## Current best clue

The hard derivation target is still a contracting-branch solution combining:

- compact-torus energy balance,
- negative bare vacuum,
- Tolman-kept radiation,
- and one missing noncanonical component `X` (or a live modified branch).

What is **no longer** a candidate for that missing piece:

- the thermal `T = T_c` crossing itself (computed no-go: radiation-dominated, `Ḣ < 0`);
- the retired reservoir / timing / release / structure lanes in the failures ledger.

If a crunch-sector `X` never appears, the bounce stays story-grade. The melt threshold
remains a real local clue; it is not the bridge.

## First derivation scaffold

Start from what the corpus already gives:

- The compact-torus background carries a zero-net-energy balance.
- The condensate floor is finite:
  - `rho_bounce = m^4 / lambda`
  - with the recorded values, this is keV-class, not singular
- In contraction, the radiation budget blueshifts as `a^-4`
- The rotating condensate alone is excluded as the stiff source:
  - tracking gives `w = (n - 2)/(n + 2) < 1`
  - kination only appears at trans-Planckian amplitude
- The bounce therefore has to be a coupled problem:
  - condensate floor
  - Tolman-kept / blueshifted radiation
  - negative bare vacuum
  - any missing effective-stiff component

The first pass should answer three questions in order:

1. What is the minimal total energy budget of the contracting phase on the compact torus?
2. Which term actually changes the sign of the evolution at the handover?
3. Which component supplies the hot-start energy without violating the no-go on the rotating condensate?

If these three cannot be answered in equations, the bounce is still only a narrative.

## The energy-ledger clue

The expansion-energy ledger is the right support theorem, but it is not yet the bounce.
It gives the flat-space cancellation

`E = ½ ṙ² − GM/r = 0`

and therefore the standard Friedmann balance

`H² = (8πG/3) ρ`

So the ledger proves:

- the medium can localize the total expansion budget;
- the flat branch is an exact zero-sum account;
- the burst-scale cancellation is finite, not singular.

But the bounce asks for more:

`H = 0` and `Ḣ > 0`

while the standard sign still says

`Ḣ = −4πG(ρ + p)`

So the ledger alone cannot force the turn. It can only say that the handover must
occur at an exact density cancellation, not which term causes the cancellation.
∴ the bounce source still has to be found in the matter sector or in a noncanonical
correction to the Friedmann relation.

## Why black holes stay open as a piece of the handover

Black holes are a real part of the story, and they may still matter as one leg of a combined
handover. The open question is not whether they exist in the crunch; it is whether they can
participate in a mechanism that turns the contracting branch into a hot, finite-density restart.

- In the black-hole interior note, infall is stored as **heat and entropy in a thermal core**.
  That does not by itself make a bounce, but it does make BHs plausible entropy reservoirs in a
  multi-component crunch.
- Hawking radiation is the right sign but the wrong size on its own: the cyclic-genesis file prices
  it as cosmologically negligible for stellar and supermassive black holes, and only very small PBHs
  radiate appreciably on today’s timescale.
- The cyclic file also says BHs **persist across a bounce** as inhomogeneous seeding, which means
  they carry Tolman’s debt unless some other channel discharges it.

So the open version is:

- black holes may be part of the entropy/heat budget that feeds the bounce;
- by themselves they are not yet a full `ρ_X(T)` or `Ḣ > 0` term;
- the plausible combined route is BH heat + blueshifted radiation + whatever thermal residual the
  crunch produces, all acting together at the handover.

In short: BHs are not closed, they are a possible component of the missing coupled mechanism.

### The black-hole route as a three-part test

If the universe's late crunch is black-hole-like, the BH channel still has to pass three
separate checks:

1. **What BHs can supply.** A finite-density thermal core can store heat and entropy, and
   phonon Hawking emission can later release energy into the shared crunch bath.
2. **What BHs cannot supply by themselves.** Hawking emission is a leak / brake / release
   channel; it does not on its own make `H = 0` and it does not force `Ḣ > 0`.
3. **What the bounce still needs.** The handover still requires either a sector-local
   `ρ_X(T)` or a genuine branch-changing `Ḟ(T)` that makes the stored/released energy act
   as a reversal term rather than just a reservoir.

So the black-hole route is useful if it tightens the crunch bath and releases the stored
energy at the right threshold, but it remains only a candidate bridge until the missing
handover term is written down.

## Why magnetars stay open as a possible analog

Magnetars are not a bounce solution in hand. There is no magnetar-specific derivation in the corpus
yet, and no file here prices them as a cosmological handover source.

What they *do* supply is a useful local shape:

- a neutron-star-scale object with enormous stored magnetic energy;
- a crust + superfluid interior where sudden release is at least plausible;
- an inherited link to the model's neutron-star / glitch / superfluid thread.

So the magnetar branch stays open only as a candidate reservoir/trigger inside a combined crunch
budget:

- magnetic storage,
- crustal or reconnection release,
- possible coupling to superfluid rearrangement,
- and then whatever radiation/thermal residual survives the contraction.

That makes magnetars a structural analogue, not a derivation. If they matter, it will be because
they help supply the same pattern already seen with black holes: storage first, release later, then
blueshift on the contracting branch.

## Why the neutrino sector stays open as a timing clue

The neutrino sector is more promising than a generic particle bath, but it still does not close the
bounce by itself. What it does give is a real candidate for the *timing* of the handover:

- the neutrino is the medium's own mass channel;
- the lightest neutrino is the last relativistic species in the recorded settling story;
- the Majoron corner and the freeze dynamics live at the same lepton-number-breaking scale.

So the open neutrino branch is:

- the dyad heats the dCDF / sets the thermal gate;
- contraction blueshifts radiation and drives the melt;
- the neutrino sector supplies the final settling / freeze-out timing;
- and the combined handover may then cross `ρ_tot → 0` with the right sign.

That is still not a derivation. It is the best surviving candidate for the *sequence* of the bounce:
dyad heat, neutrino settling, BH / magnetar release, blueshift, handover. If the neutrino sector is
the missing piece, it will be because its freeze dynamics help place the last residual at the same
moment the condensate gives way.

## Why the high-f dyad stays open as the strongest generator candidate

The current ceiling points to the high-f dyad branch rather than the gravitational portal.
`scripts/portal_bar.py` makes the split explicit:

- the gravitational portal thermalizes only at `T ~ M_Pl`;
- the model's stated pour/crunch ceiling sits far below that;
- a non-gravitational portal tied to the high-f dyad could bar lower and fire at a
  sub-Planckian crunch.

That is the first branch in the corpus that looks like a genuine late-rung trigger rather than
another reservoir. The high-f portal rate law itself is already computed in the nonthermal
tribunal; what stays open here is whether that rate law can be promoted into a crunch-sector
source term. It is still only a candidate:

- the branch is a thermal-contact threshold, not yet a bounce source term;
- the corpus does not yet expose a crunch-sector `ρ_X(T)` or `F(T)` for it;
- but if a sharp gate can re-seat the contracting bath into the dyad's own restoration window,
  this is the most plausible place for it.

The dyad mechanism itself is already on the derived side of the ledger in its own file: the even
operator, the data exclusion of the renormalizable portal, the sharp threshold, the amplitude
ceiling, and the high-f rate law are all exposed. What remains open is the crunch-sector bridge,
not the dyad mechanism.

So the current ranking is:

- fountain effect / thermal counterflow = best local release-side clue;
- high-f dyad portal = best surviving generator candidate;
- late-time residual / BH / magnetar / neutrino timing = supporting pieces, not the driver.

## What the radiation-spread idea does and does not buy

The corpus already contains the right partial version of your idea:

- matter drains into radiation (`shed`);
- the crunch mouth thermalizes it;
- contraction blueshifts the radiation bath;
- energy can then circulate through the sector more uniformly.

That is real, but it only gets us thermalization and coupling, not the sign flip.

What it does **not** buy by itself:

- it does not make `ρ_tot → 0`;
- it does not make `Ḣ > 0`;
- it does not create a negative-pressure or modified-gravity term;
- it does not re-seat the neutrino operator or force seat-alignment;
- it does not produce a bounce if the only substance is radiation, because radiation still has
  `ρ + p > 0`.

So the “spread out as radiation and everything talks to everything” idea survives only as:

- a redistribution channel,
- a thermal contact enhancer,
- and a possible way to keep release energy coupled long enough to matter.

It fails as a standalone bounce source.

## Why the regime may be the missing piece

The user analogy is the right one: asking the bounce for a mechanism that only exists
after structure formation is like asking recombination for iron.

The corpus already splits the universe by regime:

- BBN gives light nuclei and a thermal bath, not compact stars or magnetars.
- recombination gives neutral atoms, not black-hole cores.
- structure formation gives stars, neutron stars, black holes, and magnetic reservoirs.

So if the bounce needs a late-stage reservoir/release object, then the wrong question
is "why is it not visible in BBN?" The right question is "does the crunch ever build
the late-stage object before the handover?"

That keeps the open branches honest:

- neutrinos may set timing,
- BHs/magnetars may supply reservoir/release,
- radiation may provide the coupling medium,
- but the sign flip still needs an allowed late-regime term.

## The regime ladder to chase

The corpus already gives the cooling ladder in order, and the bounce clue is most likely
to sit near the top of it:

- `BBN` gives nuclei. It is too hot for atoms, molecules, or compact objects.
- `recombination` gives atoms. It is too hot for chemistry to be the new thing.
- `cosmic dawn` gives molecules and the first stars. These are thermometers of cooling,
  not bounce engines.
- `structure formation` gives galaxies and dark solitons. These are the first genuinely
  late bound structures.
- `late collapse` gives neutron stars, magnetars, and black holes. These are the strongest
  reservoir/release candidates the corpus currently prices.
- `gravitational atoms` and `SMBH atoms` are the model's own late-structure grammar: they
  are bound states that only exist once the medium is cool enough and the potential deep
  enough.

For the current cosmic epoch, the ladder reads from the top down:

- the most massive stars die first;
- the stellar UV budget declines;
- red giants, planetary nebulae, white dwarfs, neutron stars, magnetars, and black holes
  accumulate as the visible sky reddens and dims;
- the baryonic medium becomes more compact-object dominated;
- that is the regime in which late-rung reservoir/release structures become available.

Keep that remnant set as the next-epoch survivor list:

- white dwarfs, with planetary nebulae and enriched gas shed on the way out;
- massive-star deaths as core-collapse supernovae, leaving neutron stars, magnetars, or black holes;
- the leftover gas and compact remnants are the objects most likely to matter once the bright stellar
  era is gone.

The "same room" reading should stay literal-but-causal, not literal-spatial:

- the remnant types do not need to merge into one object now;
- they need to end up in the same late compact-remnant epoch, with the same cooling and clustering
  rules;
- the final reunion is the crunch bath itself, where contraction and thermalization force the
  different survivor channels into one shared handover environment.

The four-piece map is:

| survivor | what it carries | likely bounce-role |
|---|---|---|
| white dwarf | cooled baryonic matter, the late low-mass endpoint | a settled matter reservoir and a cooling landmark |
| neutron star | nuclear-density matter plus neutrino/superfluid structure | the neutrino and superfluid timing side |
| magnetar | extreme magnetic energy storage | the release-side energy reservoir / trigger analogue |
| black hole | deepest gravitational lock, finite-density core, heat and entropy | the strongest reservoir/release ledger |

These are carrier-objects, not the handover term itself. The bridge still has to be a
sector-local `ρ_X(T)` or a genuine branch-changing `Ḟ(T)` that makes the shared late
remnant bath turn the crank on `H = 0`, `Ḣ > 0`.

One more timing note: the **carriers** of the next regime can appear before the reversal
does. That is, the universe may spend a long late epoch assembling the compact-remnant
inventory and sharpening the thermal thresholds, while the actual reversal remains a
terminal threshold in the contracting branch rather than a midpoint feature. So the
epoch-to-epoch map is useful for finding what survives, but the bounce itself still looks
like a late threshold event, not an early hidden mechanism.

So the “lights out” reading should stay literal but narrow:

- it does **not** mean the dark-energy thaw is powered by starlight;
- it does mean the source of abundant stellar radiation disappears as the current epoch burns out;
- and it does mean the next-epoch clue is more likely to live in compact remnants than in early
  thermometers.

So the next-epoch clue is probably not an early-universe species threshold at all. It is a
late-rung object that only appears once the universe has cooled enough to bind tightly:
compact objects first, then their atom-like bound-state grammar.

Current ranking, by bounce relevance:

1. black-hole cores
2. magnetars / neutron-star superfluid interiors
3. gravitational atoms / SMBH atoms
4. atoms and molecules as thermometers only
5. BBN nuclei as too early to matter for the bounce mechanism itself

## What the top three actually buy

**1. Black-hole cores — still alive.** This is the only top-rung object that already carries
an explicit energy ledger: infall becomes heat and entropy in a finite-density core, and the
core can in principle release energy later. That makes BHs the strongest surviving candidate
for the combined crunch budget.

**2. Magnetars — alive only as an analogue.** The neutron-star magnetic reservoir plus
crust/superfluid release channel is a plausible local shape, but the corpus has not priced
a magnetar-specific handover term. So magnetars remain open as a reservoir/trigger picture,
not as a derived bounce source.

**3. Gravitational atoms / SMBH atoms — diagnostic, not source.** These are late-stage
bound states that tell us the universe is cool and structured enough to form compact objects.
They help with regime placement, but they do not themselves supply the missing `ρ_X(T)` or
the sign flip. They are thermometers of the late universe, not the bounce engine.

So the surviving logic is:

- black holes may participate in the handover;
- magnetars may decorate the release side;
- gravitational atoms tell us the late-regime object is real;
- none of the three, by itself, yet produces `H = 0`, `Ḣ > 0`.

## The combined-shape hypothesis

The most promising shape so far is not "BHs alone" but a coupled transfer:

- matter collapses into thermalized cores;
- those cores store heat and entropy instead of point-singular density;
- radiation is generated and/or released from the thermalized part of the budget;
- the contracting branch blueshifts that radiation as `a^-4`;
- the two together may produce the handover if their combined pressure/coupling
  can push `ρ_tot` through zero while keeping `Ḣ > 0`.

That shape is not yet a derivation, but it is the first one that matches the
corpus's repeated pattern of "one reservoir, one transfer, two signs."

The closest explicit structural analogs already written are:

- the black-hole core, where infall energy becomes heat and entropy;
- the `shed` row in `PRTOE_MATH_SPINE.md`, where the same term drains matter and
  grows dark radiation with opposite signs;
- the crunch mouth in the origin note, where photons are massed and thermalized;
- and the thermal counterflow language, which says a heated medium can force the
  condensate to give way.

So the combined answer may be a multi-stage release:

1. collapse and thermalization in BH-like cores;
2. radiation release or matter→radiation conversion from the heated sector;
3. blueshift amplification during contraction;
4. a final thermal residual that tips the handover.

That is the flavor to keep in mind while deriving the actual equations.

## The turnaround is not the bounce

The cyclic-genesis branch gives a clean late-time turnaround law:

`ρ_DE(a)/ρ_Λ = (1 + B)·exp[thaw(1 − a³)] − B`

with

`B ≡ |ρ_bare|/ρ_Λ,obs`

and the recorded solution turns at `a ≈ 2.0–2.8`.

The mechanism is already coded in the background module:

`ρ_floor(a) = ρ_∞·exp[thaw·(1 − a³)]`

with the background-only deviation

`E_th(a) = ρ_floor(a) − ρ_∞`.

Adding the negative bare vacuum gives

`ρ_DE(a) = ρ_Λ·[(1 + B)·exp[thaw·(1 − a³)] − B]`,

where `B ≡ |ρ_bare|/ρ_Λ,obs`. The turn is the zero of that expression:

`ρ_DE(a_turn) = 0`

so

`a_turn = [1 − thaw⁻¹·ln(B/(1 + B))]^{1/3}`.

That is the actual turnaround mechanism: the thawing floor alone only falls toward
zero from above, but the added negative bare vacuum lets the total DE budget cross
zero at finite `a_turn`. The flat Friedmann equation then gives `H = 0` at that
point; the turning sign is the late-time branch reversal, not the bounce.

That is useful, but it is only the expanding-branch reversal. It tells us when the
floor stops propping up acceleration and the universe starts contracting. It does
**not** yet give the contracting-branch bounce, because the bounce still needs:

`H = 0`, `Ḣ > 0`, and the energy cancellation at the handover.

So the negative bare vacuum is now best read as:

- necessary for the turnaround;
- not sufficient for the bounce;
- not the missing stiff component.

The quoted `a ≈ 2.0–2.8` / `16–26 Gyr` window is the registered solution range for
`w₀ ∈ [−0.92, −0.86]` and the allowed `B` span; it is supported by the chain and the
preregistered branch record, not by a fresh standalone simulation in this session.

That is the last clean separation the ledger has to keep in view.

## The ghost-condensate floor is the wrong kind of help

One plausible-looking survivor is the floor operator itself:

- the ghost-condensate branch gives `w = −1` exactly at `P_X = 0`;
- the `c_s² = 0` point is stabilized by the `(δK)²` term;
- the result is a stable de Sitter floor, not a stiff bounce source.

That is useful for the late-time dark-energy sector. It is not enough for the
contracting branch, because a bounce needs either:

`ρ + p < 0` transiently, or a modified gravitational branch that changes the
hand-over condition itself.

So the floor is an attractor from above, not a lift from below. If the bounce is
to come from this neighborhood at all, it has to use a transient NEC-flexible
excursion that the current stable branch does not carry.

The corpus also prices that escape very sharply: the only NEC-flexible sector is
the ghost-condensate branch, and the wormhole audit says its effective negative
energy budget is tiny on the recorded numbers. That makes it a late-time floor
mechanism, not an obvious cosmological bounce engine.

## The radiation clue: contraction heats, and heat is what can melt the floor

This is now the leading candidate for the bounce dynamics:

- contraction automatically blueshifts radiation;
- `ρ_rad ∝ a⁻⁴` and therefore `T ∝ a⁻¹`;
- the hotter branch is the one that can force the condensate out of its
  superfluid regime;
- the bounce can then be read as a thermal handover: the radiation budget rises
  until it melts/retracts the floor and the cycle re-enters the hot branch.

So the hard question is no longer “where does radiation come from?” The answer is
already in the contracting FRW scaling. The hard question is:

`Does the blueshifted radiation cross the melt threshold early enough, and with
enough budget, to produce the handover before BKL wins?`

That makes the derivation target very concrete:

1. Write `T(a)` or `ρ_rad(a)` on the contracting branch.
2. Compare it to the condensate melt scale `T_c` / `ρ_bounce`.
3. Check whether the same crossing also gives `H = 0` and `Ḣ > 0`.
4. If not, the thermal picture is only a partial clue, not the bounce mechanism.

## The thermal handover equation

For the radiation bath, the contracting branch gives the standard scalings:

`ρ_rad ∝ a⁻⁴`

`T ∝ a⁻¹`

So if `T_*` is the bath temperature at some reference scale `a_*`, then

`T(a) = T_* (a_*/a)`

and the condensate melt condition is simply

`T(a_b) = T_c`

or equivalently

`a_b = a_*·(T_*/T_c)`

This is the cleanest clue so far, because it turns the bounce into a concrete
question about the contracting history:

- does the blueshifted bath hit `T_c` early enough?
- once it does, does the condensate actually melt/retract in the right way?
- and does that same moment also satisfy the cosmological bounce conditions
  `H = 0` and `Ḣ > 0`?

If the answer to the last question is no, then the thermal crossing is only the
melting threshold, not the bounce itself. If it is yes, then the bounce is a
thermal handover: radiation wins the local physics first, and the geometry
follows only if the medium's equations allow it.

In superfluid language this is the **thermal counterflow / fountain effect**
picture: heat drives the normal component and forces the condensate to give way.
That is the microphysical phrase for the same melt threshold; it is still not the
cosmological proof, but it is the right dictionary entry.
If the bounce has a release-side mechanism at all, this is the best surviving
candidate: it says what the heated medium does locally, while the cosmological
equations still have to say why that local retraction becomes `H = 0`, `Ḣ > 0`.

The nearest structural analogs are also threshold-shaped, not smooth:

- the `m_e` trigger uses a sharp topological gate, not a density ramp;
- the KMS / freeze-front material locks one face per thermal period.

So the bounce clue probably wants a sharp front or gate in the crunch sector, not
a generic heating curve. That does **not** produce the missing `ρ_X(T)` by itself,
but it does tell us the bridge, if it exists, is likely event-set rather than
adiabatic.

The "next regime" guess is therefore not a new substance so much as a phase of the
same medium: a radiation-like / normal-phase release where the matter-like part is
shed and the dark-radiation part grows with opposite sign. The corpus already has
that grammar in the `shed` row and in the late-crunch thermalized-core picture.
What it does **not** yet have is the statement that this release, by itself, is the
bounce engine.

So the three hunts now read:

- **Sharp front / gate:** yes, in the `m_e` trigger and the KMS / freeze-front material.
  The bridge wants a threshold event, not a smooth curve.
- **Late-time `shed` analogue:** yes, in the dCDF matter-part → dark-radiation conversion.
  That gives the right opposite-sign bookkeeping, but it is still a release channel, not a
  proved bounce source.
- **Fountain-effect bridge:** still the best surviving local mechanism. It is the only
  place in the corpus where heating a superfluid explicitly forces retraction / re-routing
  flow, so it remains the best candidate for the release side of the handover.
  The same thermal program names its leftover as a **residual fountain excitation** and
  ties it to the medium's one genesis injection, so the bounce hunt should treat the
  fountain effect as a real residual component of the same field, not as a new species.
  I have not found any corpus equation that lifts that residual into a bounce-sector
  `ρ_X(T)` yet; every explicit `ρ_X` I can point to is still late-time or support-grade.
  So the fountain effect stays load-bearing as a clue for the thermal residual program,
  but it is not yet a bounce-source term in the crunch sector.
- **Topology / Casimir lane:** useful for the compact spectrum and the axis surviving the
  bounce, but not a live handover term. The corpus prices boundary-modified spectra and the
  flat-torus mode cutoff as structure, not as a crunch-sector `ρ_X(T)`, so this lane helps
  explain the cavity but does not yet turn `H = 0` into `Ḣ > 0`.

## What the thermal clue would have to do

The thermal threshold by itself is not enough. To become a bounce, the melt must
enter the equations that control the handover.

The recorded ramp has the right shape:

`ε(T) = ε·(1 − T/T_c)`

So if the bounce sector uses the same order parameter to set an effective
coupling, then any induced-gravity or response coefficient `F` must satisfy

`F = F(ε(T))`

and therefore

`Ḟ = (dF/dε)(dε/dT) Ṫ`.

On the contracting branch `Ṫ > 0`, so the melt can sharpen `Ḟ` instead of
just changing the matter content. That is the only clean way the thermal clue can
help the geometry:

- either through a noncanonical `ρ_X(T)` that makes `ρ_tot → 0` at the handover,
- or through a sharp `Ḟ(T)` that changes the physical branch in the modified
  Friedmann relation,
- or through both at once.

So the real question is not whether `T_c` exists. It does. The question is
whether the condensate's collapse at `T_c` can be written into the same equation
that sets `H = 0` and `Ḣ > 0`.

## Thermal-crossing no-go (computed, 2026-07-25)

The comparison the workplan asked for is now run in
`scripts/bounce_thermal_crossing_nogo.py`. Recorded inputs only:

- `T_c = 177.10 keV`
- `ρ_bounce = m⁴/λ` with `m = 2.24×10⁻²⁰ eV`, `λ = 2×10⁻⁹¹`
- `ρ_rad = (π²/30) g_* T⁴` at `g_* = 10.75`

Result:

| quantity | value |
|---|---|
| `ρ_bounce^(1/4)` | `1.06 keV` |
| `ρ_rad(T_c)^(1/4)` | `~243 keV` |
| `ρ_rad(T_c) / ρ_bounce` | `~2.8×10⁹` (~9.4 dex) |
| `|ρ_bare| ~ ρ_Λ` vs `ρ_rad(T_c)` | bare is `~10⁻³²` of radiation — invisible |
| canonical `ρ + p` at `T_c` | `≈ (4/3) ρ_rad > 0` |
| `Ḣ` at `T_c` | `< 0` in standard FRW |

So the thermal crossing **fails as a bounce**:

1. `H = 0` in flat FRW still needs `ρ_tot = 0`. Radiation at `T_c` is nine orders
   above the condensate floor; bare vacuum cannot cancel it.
2. Even the historical flat `F`-equation `3 F H² + 3 H Ḟ = ρ_tot` forces
   `ρ_tot = 0` at `H = 0`. `Ḟ` can select a branch; it does not invent the zero.
3. `Ḣ > 0` needs `ρ + p < 0`. At radiation-dominated `T_c` the canonical piece is
   `ρ + p ≈ (4/3) ρ_rad > 0`, so the sign is wrong.
4. Closing the sign at `T_c` would need a noncanonical budget
   `|ρ_X + p_X| ≳ (4/3) ρ_rad(T_c)` — radiation-scale, not keV-floor scale
   (`need / ρ_bounce ~ 10⁹`). No such crunch-sector term is written in the corpus.
5. The ghost-condensate NEC-flexible window is the wrong scale and the wrong job:
   it is a late-time floor / arrow sector, priced ~17 orders under engineering need
   for sustained exotic stress ([PRTOE_wormholes.md](../PRTOE_wormholes.md)). It cannot
   cancel a `T_c⁴` radiation bath.

**What survives from the thermal picture:** `T(a) = T_*(a_*/a)` and the melt condition
`T(a_b) = T_c` remain real local physics. They tell you when the condensate can give
way. They do **not** make `H = 0` with `Ḣ > 0`.

**Grade:** melt threshold = real clue; thermal crossing as bounce source = retired.
See the failures ledger for the retirement row. The bridge is still missing.

## Floor / live-dCDF / metric-exit no-go (computed, 2026-07-25)

The next natural promotions after the thermal no-go also fail. Script:
`scripts/bounce_floor_frw_nogo.py`.

### (A) CSW ceiling ≠ homogeneous FRW bounce

`ρ_bounce = m⁴/λ` is a real finite density. It does **not** turn the contracting
branch around in homogeneous FRW:

- CSW polytrope `p = K ρ²` has `ρ + p > 0` for all `ρ > 0`;
- the relativistic `p ~ ρ` ceiling still has `ρ + p = 2ρ > 0` ⇒ `Ḣ < 0`;
- bare vacuum is `~10²³` too small to cancel `ρ_bounce` for `H = 0`;
- homogeneous quantum pressure vanishes (no spatial gradients).

The right reading: the CSW ceiling is a **black-hole / core hydrostatic** result
(finite central density under self-gravity). Promoting it to a cosmological bounce
conflates an inhomogeneous equilibrium with a homogeneous FRW minimum of `a(t)`.

FRW identity that makes this sharp:

`ρ̇ = −3H(ρ + p)`

During contraction (`H < 0`), if `ρ + p > 0` then density **rises**. Homogeneous
density stops rising only if `H = 0`, or `ρ + p = 0`, or the description leaves FRW.
CSW pressure alone does none of those three.

### (B) Live production dCDF never bounces

The code fluid (`include/background.h`) is barotropic with

`w = −ρ_inf / ρ`  ⇒  `ρ + p = ρ − ρ_inf ≥ 0`

for every density on the branch. At the floor, `ρ + p = 0` gives `Ḣ = 0` — de Sitter
**coast**, not a bounce (`Ḣ > 0`). The Route-D thaw makes `1+w > 0` at late times,
which is still NEC-saturating or above, not below. So the live expanding-branch
implementation does not carry a crunch-sector NEC violation.

### (C) Hubble-scale metric exit is above the recorded floor

With `ξ = 402 AU` and `ρ_bounce^(1/4) ≈ 1.06 keV`:

| quantity | value |
|---|---|
| `H⁻¹ / ξ` at `ρ_bounce` | `~12` |
| density where `H⁻¹ = ξ` | `~150 × ρ_bounce` |
| `ρ_exit^(1/4)` | `~3.7 keV` |

So at the recorded floor the homogeneous metric is still classically OK by a factor
~12 on the Hubble scale. The no-singularity synthesis’s “crunch exits the metric at
`ξ`” is therefore **not** automatic at `ρ_bounce`. Local BKL curvature radii can in
principle hit `ξ` while the Hubble scale has not — that is uncomputed, and must not
be treated as a free substitute for the missing `X`.

### What this narrows the target to

Still alive only as open structure, not as derived bounce:

1. a **crunch-sector** noncanonical `ρ_X` / `p_X` that is not the live barotropic dCDF;
2. a genuine **departure from homogeneous FRW** (metric exit / strong inhomogeneity)
   with equations, not a slogan;
3. a **two-component** simulation that funds MeV reheating over the keV floor
   *after* a turn that has already been derived.

Still dead as bounce sources (failures ledger): thermal `T_c` crossing, CSW-floor-as-FRW-bounce,
live dCDF NEC flip, Hubble-scale metric exit at `ρ_bounce`, plus the earlier reservoir/timing
lanes.

## What the thermal clue is not

The old scalar-tensor route does not revive here.

- The historical `F(φ)R` program is closed.
- The current emergent-gravity frame says `v4` does **not** modify gravity.
- The induced-gravity / Sakharov material in the corpus is a support theorem for
  the background and the area law, not a live bounce mechanism.

So `Ḟ(T)` is only a conditional placeholder: it would matter if the medium had a
running gravitational coupling, but the current model does not carry one as an
active bounce sector.

That leaves one honest live target:

- a noncanonical `ρ_X(T)` or `p_X(T)` produced by the thermal residual itself,
- with a sign strong enough to satisfy `ρ_X + p_X < −(ψ̇² + 4ρ_rad/3)`,
- and a zero-crossing strong enough to keep `H = 0` at the handover.

The only explicit residual template the corpus already exposes is the thermal door:
freeze at a threshold, then a residual fraction survives. That pattern is **late-time**
and neutrino-settling in the recorded model, so it is not yet a bounce source term.
But it is the right *shape* to test against the crunch: if the bounce closes through a
residual, it will have to look like a freeze-out fraction written at the crunch's own
threshold, not like a generic heating curve.

If the thermal residual cannot do that, then the bounce is still missing its
mechanism, and the melt threshold remains a clue only.

The other explicit handover in the corpus, the quartic-to-mass release in the
transfer-integral spec, is useful only as a template for "two regimes, one
threshold." It does **not** solve the bounce problem:

- it belongs to the baryogenesis / sphaleron track, not the crunch track;
- its handover is tied to the AD field and the sphaleron epoch, not the
  contracting bounce;
- and it produces a transfer current, not a bounce-sector `ρ_X(T)`.

So it is a structural analogue, not a bounce source.

Likewise, the `T = m_e` localizable-zero burst in the expansion-energy ledger is a
real finite handover support, but it is still only a localization of the budget:
it tells us the handover can be finite, not why the contracting branch turns.
So the burst is another bridge-shaped template, not a live crunch-sector bridge.

## Stress-energy scaffold

Write the bounce sector in FRW form first:

`T^μ_ν = diag(−ρ_tot, p_tot, p_tot, p_tot)`

with

`ρ_tot = ρ_bare + ρ_rad + ρ_ψ`

`p_tot = −ρ_bare + ρ_rad/3 + p_ψ`

and for the condensate degree of freedom

`ρ_ψ = ½ ψ̇² + V(ψ)`

`p_ψ = ½ ψ̇² − V(ψ)`

so that

`ρ_tot + p_tot = ψ̇² + 4ρ_rad/3`

in the canonical case.

That last line is the first hard clue: if the bounce sector is only a canonical scalar plus radiation plus a constant bare vacuum, then

`Ḣ = −4πG (ρ_tot + p_tot) ≤ 0`

and no bounce occurs in standard FRW. So the derivation target is now sharper:

* either the medium contains a noncanonical term that makes `ρ + p < 0`,
* or the effective Friedmann equation is modified by the compact-torus / induced-gravity setup,
* or both.

This is the first place the bounce work has to leave the canonical textbook lane.

## The handover condition, written as an equation

Let the full bounce sector be split into a canonical piece and an extra medium term:

`ρ_tot = ρ_can + ρ_X`

`p_tot = p_can + p_X`

with

`ρ_can = ρ_bare + ρ_rad + ½ ψ̇² + V(ψ)`

`p_can = −ρ_bare + ρ_rad/3 + ½ ψ̇² − V(ψ)`

Then

`ρ_can + p_can = ψ̇² + 4ρ_rad/3 ≥ 0`

so the canonical piece alone cannot satisfy `Ḣ > 0`.

The bounce therefore demands an extra contribution `X` such that

`ρ_X + p_X < −(ψ̇² + 4ρ_rad/3)`

at the handover, while the Hamiltonian constraint still closes at

`H = 0  ⇒  ρ_can + ρ_X = 0`.

This is the actual mathematical target: identify the medium term `X` that makes
the handover possible without reintroducing the rotating-condensate no-go.

The next pass should ask whether `X` is:

- an induced-gravity correction,
- a ghost/phantom effective piece,
- a compact-topology correction to the Friedmann relation,
- or some other noncanonical medium contribution already buried in the corpus.

## The strongest candidate lane: induced gravity / varying `F`

The old scalar-tensor working formulation already contains the noncanonical Friedmann
relation:

`3F H² + 3H Ḟ = ρ_tot - 3F K/a²`

For the flat compact torus, `K = 0`, so the equation is

`3F H² + 3H Ḟ = ρ_tot`

or equivalently

`H = [−Ḟ ± √(Ḟ² + 4Fρ_tot/3)] / (2F)`

This is the first concrete place where a bounce can happen without forcing the
canonical matter sector to violate its own no-go by hand. The branch structure is
the clue:

- if `Ḟ` is slowly varying, the equation reduces to the usual Friedmann sign;
- if `Ḟ` changes fast enough, the physical branch can flip from contracting to
  expanding;
- but in the flat case `H = 0` still requires `ρ_tot = 0` at the handover.

So `Ḟ` is not a magic source of the turn by itself. It is the branch-selector and
the local sign-control term near the handover; the density cancellation at the turn
must still come from the medium's energy ledger.

The bounce then comes from the medium's own effective gravitational coupling plus
the zero-crossing of the total density, not from the rotating condensate alone.

So the next derivation pass should test whether the current medium data can be
written as such an `F(φ)` term in the bounce sector, and whether the resulting
branch switch also matches the hot-start budget.

This is the only bridge-shaped structure the corpus currently exposes: a branch change
through `Ḟ` with a density crossing. It remains a historical template until a live
crunch-sector `F(T)` is actually written from the medium.

The late-time thermal door gives the second reusable pattern: a freeze-out residual
fraction. That is a better shape match to a crunch-sector source term than a generic
smooth ramp, but the corpus still prices it only in the neutrino / dark-energy lane.
So the bounce hunt currently has two templates and zero live bridge terms.

There is a third general decomposition in the corpus, "freeze-out third + release
memory," but it lives in the inflation / ergodic-mechanics notes, not in the crunch
sector. It is a real partial-mechanism split, but it is not a bounce bridge.

## Bounce criterion in the modified equation

For the flat case, a genuine bounce requires:

`H = 0` at the handover,
`Ḣ > 0` at the same point,
and the physical root of the quadratic in `H` to cross from the contracting to the expanding branch.

In the `F`-equation, that means the handover has to be driven by the medium's
effective gravitational coupling changing fast enough that the physical branch
switches while the total density stays finite.

So the concrete test is:

1. Can the bounce-sector fields produce a sufficiently sharp `Ḟ`?
2. Can the same sector make `ρ_tot` cross through zero at the handover?
3. Does that `Ḟ` arise from the already-recorded medium, or does it require a new assumption?
4. Does the same branch switch also leave enough positive energy for the hot start?

If the answer to (1) is no, the modified Friedmann lane dies too. If the answer to
(2) is no, the modified Friedmann lane is incomplete even if the algebra looks promising.
If the answer to (3) is yes, we may have the real derivation lane the white-hole analogy
was only pointing at.
Right now the corpus only gives us the retired scalar-tensor lane as a historical template
and the late-time thermal residual as a different sector's floor; it does **not** yet give
an active crunch-sector `F(T)` to feed here.

## The three-lane chase, now checked

The hunt just ran the three surviving lanes as far as the corpus lets it:

- **Black-hole release side:** still open. The interior ledger is real: infall becomes heat and
  entropy in a finite-density core, so BHs can still participate in a combined crunch budget.
  But ordinary Hawking evaporation is far too slow to be the next-generator on any
  near-term crunch clock: stellar and supermassive holes outlive it by many orders. Only a
  primordial substellar population, if it exists, lands in the ~10^10–10^11 yr band.
- **Neutrino freeze timing:** still open. The lightest neutrino remains the last relativistic
  species, and the Majoron corner can still set the handover clock, but it does not supply the
  sign flip by itself.
- **Late-rung residual search:** searched and not promoted. The only explicit residual the corpus
  names lives in the late-time dark-energy program; `w = −1` is exact there, but that floor is
  the wrong epoch and the wrong job for the contracting bounce. It can tune the DE floor, not
  furnish a bounce-sector `ρ_X(T)`. The failures ledger already kills the move "borrow the
  late-time residual and rename it for the bounce"; only a sector-local residual or a genuine
  branch change stays live here.

So the current state is narrower, not wider: no named late-rung `X` yet, only reservoirs,
timing locks, thresholds, and the compact-geometry spectrum. The high-f dyad portal is
the strongest trigger candidate, but it is still trigger-only until it is written as a
crunch-sector source term. If the bounce closes, it will still need either a noncanonical
medium term or a genuine branch-changing correction that is derived inside this sector,
not borrowed from late-time dark energy. The detailed retirements are tracked in
[`docs/PRTOE_FAILURES_LEDGER.md`](/home/themilkmanj/prtoe_class/docs/PRTOE_FAILURES_LEDGER.md).

---

## Admission (2026-07-25): the bounce mechanism is not in the current corpus

**Plain statement.** After the computed no-gos (thermal crossing, CSW-as-FRW-bounce,
live barotropic dCDF, Hubble-scale metric exit at the floor) and the retired support-only
lanes (BH / magnetar / neutrino timing / fountain / high-scale portal / topology as
*sources*), the honest grade is:

> **The classical bounce mechanism — the term that makes `H = 0` and `Ḣ > 0`, or the
> controlled departure from homogeneous FRW that replaces that pair — is not written in
> the present corpus. It is not derived. It is not hiding under a relabel of an existing
> late-time residual.**

That is option 3: admit the mechanism is not exposed. This is not a temporary
documentation gap. The equations that would close the turn are not in hand.

### Caveats — what this admission is *not*

1. **Not “the bounce is impossible.”** Finite `ρ_bounce`, the local white-hole no-go, the
   energy-ledger localization, and the two-component *shape* of hot start over a keV floor
   all still stand. What is missing is the *turn*, not the entire cyclic grammar.

2. **Not “give up forever.”** The claim is weaker and more physical: the load-bearing
   object may belong to a **regime we are not in**. The corpus already treats cosmic
   history as a ladder of thresholds (BBN → recombination → structure → compact remnants).
   Asking the present dark-matter / dark-energy epoch to hand over the terminal
   contracting-branch engine is like asking recombination to hand over iron, or BBN to
   hand over a livable planet. The next regime can enable degrees of freedom the current
   one does not stock.

3. **Not “educated guesses are derivations.”** What follows is reverse-engineering from
   visible constraints — the watch-face method. Constraints narrow the interior. They do
   not open the case. Every line below is graded as **hard constraint**, **soft
   structural inference**, or **guess**. Nothing in this section is promoted to `derived`.

4. **Not a license to invent `X` and stamp it.** If a future regime or a future
   calculation supplies the term, it must still pass `H = 0`, `Ḣ > 0` (or a written
   FRW-exit), BKL, Tolman, and the MeV-over-keV hot-start joint. The failures ledger
   stays the graveyard for shortcuts.

### Regime reading (soft structural inference)

We are mid-ladder in the dark sector: matter-like dCDF behavior, a near-`w = −1` floor,
and a possible late thaw / turnaround on Gyr scales. The bounce, if real, is a
**terminal threshold of the contracting branch** after turnaround — tens of Gyr out on
the registered corner, not a present-day observable operator.

So the admission has a time-and-regime clause:

- **Available now:** expanding-branch physics, melt thresholds, floor number, no-gos,
  support roles (reservoir / timing / release / structure).
- **Not available now:** the species or operator that only exists (or only becomes
  dynamically dominant) in the deep contracting / handover regime.
- **Best present tool:** constrain what that operator *must be able to do* from the
  hands we can see, without pretending we have opened the watch.

---

## Watch-face method: what the visible hands force about the interior

Analogy (for method only, not as physics): a sealed watch shows hour, minute, and second
hands in lockstep. You do not see the gears, but you can still require: at least three
coupled rotating degrees of freedom; a one-way or ratchet relation from seconds → minutes
→ hours; a common drive or escapement so the hands do not free-run. That narrows the
interior. It does not name the brand of gear.

Apply the same discipline to the bounce.

### The hands we can actually see (hard, from corpus + computation)

| # | Visible hand | Grade | What it forces inside |
|---|---|---|---|
| H1 | Finite `ρ_bounce = m⁴/λ ~ (1.1 keV)⁴` | computed | Interior must not need a curvature singularity; density is bounded on the condensate ledger |
| H2 | Canonical FRW: `Ḣ = −4πG(ρ+p)` with `ρ+p ≥ 0` on live matter+radiation+barotropic dCDF | computed / code | Interior must supply either noncanonical `X` with `ρ_X+p_X` negative enough, or a written exit from homogeneous FRW |
| H3 | Flat `H = 0` still needs `ρ_tot = 0` (including historical `F`-equation) | computed | Density cancellation and sign flip are two jobs; one gadget rarely does both by accident |
| H4 | Thermal `T = T_c` melt is real; as bounce it fails (`ρ_rad/ρ_bounce ~ 10⁹`, `Ḣ < 0`) | computed | Melt and turn are **different gears**; they may couple but must not be identified |
| H5 | CSW ceiling is core/hydrostatic, not homogeneous FRW bounce | computed | BH-core physics and cosmic turn share a floor *number*, not a shared turn *mechanism* |
| H6 | Live dCDF: `ρ+p = ρ−ρ_inf ≥ 0`; floor ⇒ `Ḣ = 0` coast | code identity | Expanding-branch fluid is not the crunch engine; bounce operator ≠ today’s barotropic law |
| H7 | Rotating condensate tracking: `w = (n−2)/(n+2) < 1`; kination only trans-Planckian | computed | BKL-safe stiff phase is **not** this sector at sub-Planckian amplitude |
| H8 | Turnaround ≠ bounce: bare+thaw can give late `H = 0` on the expanding branch | derived structure / registered | Reverse from acceleration is a different gear train from the deep crunch restart |
| H9 | Local white holes forbidden; global bounce ID still provisional | derived / provisional | Time-orientation is global; any white-hole-like reading is boundary-scale, not a local reverse patch |
| H10 | Hot start needs ~MeV over ~keV floor (~12 dex in density) | computed gap | Turn and reheating are coupled books: floor alone does not fund BBN; radiation (or equivalent) must carry the hot budget |
| H11 | Hubble-scale metric exit at floor: `H⁻¹/ξ ~ 12`, exit density ~150× higher | computed | “Metric ends at ξ” is not automatic at `ρ_bounce` on the Hubble scale; local high-curvature exit is uncomputed |
| H12 | Topology can survive; rotation is dynamical and can reset | recorded cyclic grammar | Something must re-seed twist / axis after the turn without requiring the same dynamical rotation to be conserved through the crunch |
| H13 | Tolman: entropy (esp. BH) grows; eternal identical cycles blocked | recorded | If cycles exist they lengthen / change; pure reset is not free |
| H14 | Epoch ladder: each threshold enables the next (BBN→atoms→stars→compact remnants) | structural corpus pattern | Terminal engine likely sits at a **late/contracting** rung, not at early thermometers |

### Synchronization requirements (what must grip what)

Like second/minute/hour hands, the bounce interior has to keep several visible motions
from free-running. These are **coupling requirements**, still not a named mechanism:

1. **Density hand ↔ sign hand.**  
   At handover, something drives `ρ_tot` through a cancellation (or replaces the
   Friedmann constraint) *while* `ρ+p` (or the modified branch) allows `Ḣ > 0`.
   Two hands, one escapement. Hard constraint from H2–H3.

2. **Melt hand ↔ turn hand.**  
   `T_c` can open the condensate (normal component wins) without turning the geometry.
   If both happen in one epoch, there must be a coupling from order-parameter collapse
   into the stress-energy or into the FRW-exit — not identity of the two events.
   Soft inference from H4, H6.

3. **Floor hand ↔ hot-start hand.**  
   KeV condensate ceiling and MeV radiation budget are different ledgers. The interior
   must transfer or preserve enough radiation-like energy across the turn (Tolman-kept
   / blueshifted / re-released), not ask the floor density to be the hot start.
   Hard gap from H10; shape from the two-component reading.

4. **Arrow hand ↔ boundary hand.**  
   Global time-orientation forbids local reverse patches; a white-hole-like global event
   is only allowed as branch boundary, and only provisionally. The interior cannot be “a
   local white hole somewhere in the bulk.” Hard from H9.

5. **Anisotropy hand ↔ stiff-or-exit hand.**  
   Homogeneous contraction with `w < 1` loses to BKL shear. Either a stiff (`w ≥ 1`)
   component appears in the *crunch* roster, or the description leaves smooth FRW
   before shear wins. Hard from H7; open which branch.

6. **Topology hand ↔ reheat hand.**  
   Compact topology / axis survival is structure; reheating is thermal. They can share a
   moment without one deriving the other. Soft from H12.

7. **Present floor hand ↔ future crunch hand.**  
   Today’s stable `w = −1` attractor is the wrong job for `Ḣ > 0`. The crunch operator,
   if it exists, is off this attractor or in another sector. Hard from H6 and the
   ghost-floor stability result.

### What the interior must contain (constraint list, not a model)

From the hands alone, any future bounce mechanism is required to provide at least:

**C1. A turn primitive**  
Either:
- a crunch-sector `X` with `ρ_X + p_X < −(ψ̇² + 4ρ_rad/3)` and `ρ_can + ρ_X = 0` at
  handover, **or**
- a controlled, equation-level exit from homogeneous FRW (e.g. curvature radii → `ξ`
  with a matching rule for re-entry),
not a narrative of either.

**C2. A thermal / radiation primitive**  
Something that funds ~MeV after the turn without identifying `ρ_bounce` with the hot
start (two-component or equivalent).

**C3. A BKL primitive**  
Stiff phase in the crunch roster, or FRW-exit early enough that shear does not win —
computed, not hoped.

**C4. An arrow / causality primitive**  
No local time-reverse horizon as the engine; global boundary reading only if dynamics
close.

**C5. A regime primitive**  
The operator may be inactive or subdominant in the present DM/DE epoch; absence from
today’s Lagrangian is allowed, **absence from the eventual crunch equations is not**.

**C6. Synchronization**  
Melt, turn, reheating, and topology re-seed may share thresholds but must be coupled by
written maps (which clock drives which), not by renaming one hand as all four.

### What the interior need *not* contain (retired as necessary engines)

These may still decorate the budget; they are not required as the turn primitive:

- black-hole Hawking as the sign flip;
- magnetar magnetic release as cosmology;
- neutrino freeze as the turn;
- fountain / thermal counterflow as `ρ_X`;
- high-scale portal as the bridge (trigger only);
- topology / Casimir as `Ḣ > 0`;
- live expanding-branch dCDF or CSW ceiling as homogeneous bounce;
- thermal `T_c` crossing as `H = 0`, `Ḣ > 0`.

### Educated-guess silhouette (guess grade only)

If one had to sketch the *shape* of the missing interior without claiming it — the
watchmaker’s hypothesis, not a derivation — the silhouette consistent with the hands is:

1. **Late assembly of carriers** (compact remnants, thermal cores, radiation bath) during
   and after the present epoch — the “parts that will be in the case when the spring
   fires,” not the spring itself.
2. **Turnaround first** (bare + thaw or successor), then long contraction, then a
   **terminal threshold** that does not exist as a dominant operator today.
3. **At that threshold:** simultaneous (or tightly ordered) melt / release, density
   cancellation or FRW-exit, and radiation-dominated re-expansion — three hands, one
   escapement.
4. **Aftercare:** topology-carried axis, entropy not fully reset (Tolman), lengthening
   cycles if cycles exist.

That silhouette is **guess-grade**. It organizes search. It does not close the bounce.

### What we refuse to do next

- Invent a field, call it `X`, and mark the bounce derived.
- Borrow the late-time residual and rename it for the crunch.
- Treat regime-unavailability as proof that a favorite reservoir is the engine.
- Soften computed no-gos because the admission feels uncomfortable.

### What we allow next

- Keep pricing constraints (more hands → tighter interior).
- Keep support roles honest (reservoir, timing, structure).
- If a new regime’s operator is ever written, run it through C1–C6 and the scripts
  before any grade change.
- Prefer “open, constrained” over “derived by story.”

---

## Standing grade after the admission

| item | grade |
|---|---|
| Finite `ρ_bounce`, no infinite-density singularity from the ceiling | derived number |
| Local white-hole no-go in a time-oriented medium | derived |
| Compact-torus zero-net energy localization | derived support |
| Turnaround (bare + thaw) as expanding-branch reverse | structure / registered corner |
| Global bounce as white-hole-like boundary event | provisional identification |
| Thermal melt at `T_c` | real threshold, not bounce |
| Classical bounce mechanism (`H=0`, `Ḣ>0` or written FRW-exit) | **open — not in current corpus** |
| Regime-unavailability of the engine | soft structural inference |
| Watch-face interior constraint list C1–C6 | constraints + method; not a mechanism |
| Educated-guess silhouette | guess only |

**Bottom line.** We admit the mechanism is not on the table in this regime. We keep the
watch closed. We keep reading the hands. That is the respected path; shortcuts are how
this project would stop being real.

---

## Racing Point reconstruction (2026-07-25)

Separate track from pure admission: **rebuild the movement from the outer workings**,
label every invisible gear as fabricated, and score the replica on track.

Full build log: [bounce_reconstruction_rp.md](bounce_reconstruction_rp.md).

| Build | Idea | Score vs hard outer specs |
|---|---|---|
| **RP-A** | Metric off at `ξ` → medium crunch → metric on hot | Lead replica: no hard *fail* from missing legal part; O2/O6/O7 sit on unwritten matching (F-A1…F-A4) |
| **RP-B** | Homogeneous fluid `X` with reverse-engineered EoS | Aero target: `ρ_X = −ρ_rad`, `w_X > 1/3`. DE-scale ghost/floor **fails budget** by many orders (`scripts/bounce_rp_required_X.py`) |
| **RP-C** | Hybrid policy: RP-A default; RP-B only if metric stays on | Organizational |

**Grade of the whole track:** `reconstructed candidate`, not `derived`.

**M1 done** (`scripts/bounce_m1_shear_xi.py`): door can open under `ρ_bounce` for
CMB-to-structure seeds.

**M2 done** (`scripts/bounce_m2_junction.py`):
- Shear-dom correction: at exit `R_H/ξ → √3` (M1’s rad-only `~650` was inconsistent).
- Mixmaster window **priced**: ~6 e-folds / ~8 curvature decades at CMB-class seed.
- Exit energy **keV-class**; MeV needs fabricated `N_med ≳ 6.2` (or equivalent).
- Re-entry `H>0` still hand-declared — O2 not dynamical.

Details: [bounce_reconstruction_rp.md](bounce_reconstruction_rp.md) §9–§10.

**M2b/M3 done** (`scripts/bounce_m2b_mixmaster_nmed.py`):
- Mixmaster lasts `~10^7` healing times before homogeneous `σ = 1/ξ`.
- `N_med ≈ 6 ≈ 1/c_s` is a **coincidence**, not an identity (`N_med/(1/c_s)` not
  stable under `c_s` or `T_reheat` variation) — knob stays fabricated.
- Damping at the door does not erase prior chaos; tighter Kasner axes hurt MeV;
  `ρ_bounce` is not an extra heat bath; inhomogeneous `Δρ ~ 10^{11}` is shape-only.

Details: [bounce_reconstruction_rp.md](bounce_reconstruction_rp.md) §11.
RP-A remains reconstructed candidate; bounce **not derived**.

---

## The electron-contact proposal (2026-07-26, owner)

**Proposal:** the bounce bridge involves the electron — the carrier that "lets a
current flow" so the dCDF can heat at the crunch.

**Where it lands in the corpus:** squarely on the top-ranked trigger lane. The dyad
is the leptophilic **electron**-coupler; the melt scale is electron-anchored by
construction (`T_c = τ·m_e`); and the nonthermal tribunal already computed the
contact rate — `Γ/H ~ 1.3×10¹⁷` at `T = m_e`, still `~2×10¹⁶` at `T_c` with the
e± bath Boltzmann-thinned to ~6%. The "wire" the proposal asks for exists, is
priced, and passes with ~15 orders of margin.

**Priced** (`scripts/bounce_electron_contact.py`, recorded inputs only):

| check | result |
|---|---|
| contact (bath ↔ dark sector through the dyad) | **pass** — recorded, overwhelming |
| presence of e± at `T_c` on contraction | **pass** — `e^{−m_e/T_c} = 0.056`, contact survives |
| turn (`ρ_X + p_X < 0` at handover) | **fail by class** — every channel in the lane (e± bath, Maxwell stress, drift current, two-fluid counterflow) is NEC-nonnegative; best case saturation, never negative |
| clock (electron gate legalizes `N_med`?) | **candidate only** — gates at `T_c`/`m_e` give `N_med = 4.5/5.5` vs the needed `6.2`; `T_reheat` = 177–511 keV, ×2–6 under the MeV bar; and no corpus mechanism selects the gate (the model's own hot history runs a metric at `T ≫ T_c`, so the metric does not ride the condensate order parameter) |

**Verdict:** the electron is the computed **contact carrier** of the handover and a
candidate **synchronization clock** (constraint C6) — the melt and the e±
re-ignition are one scale family, `T_c = τ·m_e`, so the heat door and the electron
gate open together for free. What the lane cannot supply, by NEC class rather than
by margin, is the turn primitive (C1). Heating is still not turning. The bridge
stays open; the failures ledger carries the retirement row for "electron / current
as the turn."

### Owner intuition: “electrons have a big role” — role map (keep this)

The intuition is **half right and load-bearing**. Electrons are not a small decoration;
they sit on several of the bounce *synchronization* gears. What they are not is the
gear that flips `Ḣ`.

| Role | Electron / leptonic content | Grade | Constraint |
|---|---|---|---|
| **Wire (contact)** | Dyad leptophilic portal: `Γ/H ~ 10¹⁶–10¹⁷` at melt scales | **computed pass** | C6 coupling melt↔bath |
| **Scale family** | `T_c = τ m_e` with `τ = ½ln2` from the lepton-mass kernel | **recorded identity** | melt clock tied to electron mass |
| **Presence** | e± re-ignite as `T` climbs through `T_c`→`m_e` on contraction | **computed** (`e^{−m_e/T_c}≈0.056` at melt) | who is in the bath |
| **Heat / normal fluid** | e± + photons are the SM side of the heated bath that can force condensate melt | **structural + contact pass** | release-side / melt (not turn) |
| **Candidate gate** | peg re-entry or medium interval end to `T_c` or `m_e` | **candidate only** (under MeV bar ×2–6; gate unselected) | C2 reheat timing |
| **Turn primitive (`ρ+p<0`)** | e± plasma, currents, Maxwell, counterflow | **retired by class** (ledger) | **not C1** |

**How to use this without cheating:**
- Build the bounce *story* with electrons as the **thermal handshake and scale lock**
  between the dark condensate and the Standard Model bath — that is already earned.
- Do **not** ask electrons (or EM currents) to be the exotic stress that makes
  `H = 0` with `Ḣ > 0` in flat FRW — that lane is closed by NEC class.
- The open program is: medium-layer turn (M6-class repulsive rebound / metric exit)
  **plus** electron-locked melt and contact, **plus** a still-missing MeV budget path
  that may or may not peg to `m_e`.

**One-line:** electrons are likely *essential infrastructure* for the handover’s
heat and timing; they are not the bounce engine’s sign flip.

### Owner intuition: “what if it’s magnetism / a cosmic pole flip?”

The analogy (Earth poles flip, Sun flips slower, why not the universe?) is a real
pattern-recognition move. It points at **signed, cyclic, large-scale field structure** —
which this model already cares about (rotation machine, helicity, IGMF). It does **not**
by itself supply the bounce’s energy-condition flip.

**Two different meanings of “flip”:**

| Kind of flip | What changes | Bounce relevance |
|---|---|---|
| **Polarity / direction** (`B → −B`, geomagnetic, solar cycle) | direction of **B**; energy `∝ B²` **unchanged** | does **not** change `ρ_B` or `ρ+p` |
| **Energy-condition / expansion** (`Ḣ` sign, `H` through zero) | whether the universe turns from contraction to expansion | what the bounce actually needs |

Earth and Sun reverse **polarity**. The bounce needs something closer to reversing
**whether space is shrinking or growing**. Those are not the same operation.

**Maxwell / FRW class (same NEC fence as the electron lane):**

- Random / tangled cosmic **B** behaves like extra radiation: `w ≈ 1/3`, `ρ+p > 0` — adds
  to the positive budget, does not cancel it.
- Coherent uniaxial **B**: `p_∥ = −ρ_B`, `p_⊥ = +ρ_B`; along the field you at best
  **saturate** NEC (`ρ+p_∥ = 0`), you do not get a homogeneous isotropic `Ḣ > 0` engine.
- Even if `ρ_B` were comparable to `ρ_rad` at the handover, isotropic magnetic stress
  makes the turn **harder**, not easier.
- Today’s IGMF/void scales in the magnetism note are tiny vs the radiation bath; the
  crunch can amplify **B**, but amplification of `B²` still feeds a NEC-nonnegative
  channel.

**What magnetism *does* own in this corpus (real, not the bounce turn):**

| Role | Content | Grade |
|---|---|---|
| Rotation → seed **B** | Harrison battery on structural vorticity (P-2026-028) | computed / registered |
| **Helicity sign** | `sign(H_B) = sign(H_kin)` on the torus (coefficient squares out) | derived link |
| Handedness chain | helicity ↔ winding / baryon sign (open links remain) | partial / registered risk |
| Crunch survival of topology | winding/genome through bounce | structural grammar |

So magnetism is part of the model’s **parity / seed / handedness** story. A cosmic
“pole flip” would be a statement about **helicity or large-scale field direction**
across epochs — interesting for signatures — not a substitute for `ρ_X + p_X < 0`
or metric-exit rebound.

**Scaling intuition check:** longer flip times for larger bodies (Earth → Sun) is a
dynamo / diffusion timescale story (`L²/η`, convective turnover). The universe’s
bounce clock is a **cosmological density / causal** problem, not automatically the
same scaling law. Analogy ≠ derivation.

**One-line:** a universe-scale magnetic polarity flip is a **direction** story this
model already partially owns (helicity); the bounce is an **expansion-sign** story.
Do not identify them. Retirement of “magnetic pole flip = bounce turn” goes to the
failures ledger only.

---

## The regime reading, sharpened by M5 (2026-07-26, owner + computed support)

**Owner's standing position (restated 2026-07-26):** the object that sets the reversal
is not shown in this regime — it belongs to a later iteration of the universe, the way
iron cannot exist before its epoch and could not be inferred from recombination's
visible inventory.

**What M5 adds — the first computed leg under this inference.** The frozen-ratio
anchor (`scripts/bounce_m5_exotic_fluid.py`) says: any negative component scaling like
an existing positive one has a ratio frozen for all time, so a turn-capable fluid
CANNOT have existed as a scaling track through our epoch — we would measure it (a
net-negative radiation sector, excluded by N_eff). Therefore any viable turn component
must be **threshold-born**: absent from every earlier epoch, appearing at a transition
we have not crossed. "Not of our time" is no longer only an analogy; at the fluid
level it is now a mechanism-independent *requirement*.

**The fork inside the position, named so it does not blur:**
- **Iron-like reading (future STRUCTURE, present laws).** Iron's operators all exist
  at recombination; what is missing is the stellar core, not the law. If the turn
  object is iron-like, it must be assemblable from the recorded Lagrangian — and M5
  just exhausted that Lagrangian's fluid inventory. The one assembly that survives is
  the crunch's own metric-ending state (the reconstruction's remaining branch): a
  STATE our epoch never realizes, whose equations we can in principle write now
  (the matching rules). Under this reading, the future object is not a species; it
  is the medium interval itself.
- **New-operator reading (future LAW-ACTIVATION).** A genuinely new operator absent
  from the recorded theory. Allowed by the regime fence (constraint C5), but it is a
  statement that the recorded theory is incomplete — and the only honest work it
  permits today is constraint-tightening (C1–C6, the achronal-re-entry price, the
  MeV joint), never naming the operator.

**Grade discipline, unchanged:** the regime reading stays soft structural inference.
The 99% is a stance, not a grade; regime-unavailability is never promoted to a
mechanism and never excuses a fabricated X. What it now has that it did not have
yesterday: a computed reason the engine must be threshold-born, and a two-branch map
of where it could live.

---

## Three-way chase complete (2026-07-26) — rebound, matching, quartic ledger

Owner: chase all three; do not fabricate. Full write-up:
[bounce_reconstruction_rp.md](bounce_reconstruction_rp.md) §14.

| # | Attack | Honest result |
|---|---|---|
| 1 | **M6 medium rebound** (`bounce_m6_rebound_1d.py`) | Repulsive GPE shows **dynamic density turn** (n peaks then falls) in the verified 1D toy. Overshoot O(1). Does **not** by itself deliver MeV or cosmological `H>0` matching. |
| 2 | **Matching = inverse emergence** | Acoustic map medium→`g` is determined; **inverse** `g`→medium is underdetermined without extra slice/gauge structure. F-A1 not closed. |
| 3 | **Quartic / higher-order homogeneous Friedmann** | Homogeneous quantum pressure vanishes; live barotropic stress already NEC-safe; no derived `ρ(1−ρ/ρ_c)` bounce constraint in corpus. No free turn from this lane. |

**Net:** one real medium-layer computation (rebound sign); two honest non-closures.
RP-A still reconstructed. Derived bounce still no. Failures only in the ledger + these logs.

---

## The genesis-cascade parts-list (2026-07-28) — the mechanism's vertebrae exist; the spine between them is the open piece

Task #11's sweep, run on the owner's order ("see if the corpus carries one
somewhere, or signs one might exist"). The answer: no assembled mechanism — and
five recorded parts that are exactly mechanism-shaped, three of which are
computed rates:

| part | where recorded | what it supplies |
|---|---|---|
| the high-scale portal rate law | spine §(operating point); `PRTOE_me_mechanism_math.md` — "already computed in the high-energy matching calculation" | the coupling that moves energy between sectors at the high scale; f ≈ 145 TeV; the missing piece is named there as "the crunch-sector bridge" |
| thermalization gates clearing by 10⁸–10⁹ | same operating point, closed-form | wherever priced, thermalization is FAST — the cascade's rate side is supported, not open |
| K = Γ_N/H = 9×10⁷ | the baryogenesis route (neutrino home §3) | an independent portal-class rate ratio ≫ 1 at its epoch |
| freeze-out third + release memory | PHYSICS_DOMAINS (the dice); the backbone's extrapolation retired to the ledger, the decomposition standing | the deposit's statistics decompose into a thermal part and a memory part born at L = 0 |
| the T = m_e localizable-zero burst | `expansion_energy_ledger.md` | the handover can be finite — a localization of the budget |
| the legal window | the coupling inventory (gravitational-only binds only after condensation) | the cascade must complete above T_c, where a direct coupling is allowed — consistent with the gates' high-scale timing |

**The signs the owner asked about: three, independent.** (1) Every rate ratio
the corpus has computed at the relevant scales is enormous (10⁸–10⁹ gates,
K = 9×10⁷) — nothing rate-shaped obstructs a fast cascade. (2) The deposit's
statistics already decompose. (3) The handover is finite. What no file
supplies: the ASSEMBLY — which channel carries the genesis deposit into
radiation, evaluated at the genesis epoch with the recorded portal law, ending
in the bath the thermal history needs. That is one computation with a named
input (evaluate the recorded high-scale rate law at the genesis epoch inside
the legal window) — a construction task for the owner, not a missing physics
idea. Stakes raised by the bounce board: task #5 closed with O6's funding
moved here, so this assembly now owns the hot start.

## The cascade assembled (2026-07-28) — mechanism at candidate grade, one computed gap

`scripts/genesis_cascade_assembly.py`, on the parts-list above; recorded inputs
only. The assembly, four steps:

1. **Equilibration at the top is over-determined.** The portal vertex
   κm_e0 = 7.15×10⁻²⁶ eV⁻¹ gives Γ/H rising as T: the minimal-vertex estimate
   clears equilibrium by 10³–10⁴·⁵ at Planck-class temperatures, the file's
   own fuller channel count by 10⁸–10⁹. The genesis deposit thermalizes; the
   sectors are one bath at the top.
2. **Decoupling is the portal's own freeze-out:** T_dec ≈ 4×10¹⁴ GeV at the
   minimal vertex (fuller rates push toward 10¹⁰–10¹³ GeV; band carried; EFT
   caveat named — T_dec sits in the UV completion's regime). **The legal
   window — gravitational-only below, direct coupling above — is thereby
   DERIVED from the portal itself**, not postulated: a structural unification
   with the coupling inventory's law.
3. **The hot start is genesis-funded:** the Standard-Model bath is standard
   from T_dec down; MeV is passed trivially en route to BBN. O6's funding,
   moved here by the bounce board's closure, is delivered by
   equilibration-at-the-top plus ordinary adiabatic history.
4. **The ζ test, first pass, gap priced:** standard entropy bookkeeping with
   the recorded dark reheat (27/14)^⅓ gives ζ = 1.245·(10.75/g*(dec))^⅓; the
   committed window [0.25, 0.35] demands g*(dec) ∈ [484, 1327] while a
   roster-class count is ~150–250 → the full-equilibrium first pass lands
   ζ ≈ 0.42–0.47, OVERSHOOTING by ×1.2–1.9. Three candidate owners, none
   chosen: a larger genesis-era roster; partial equilibration (freeze-in-class
   heating of the dark side, which lowers ζ); a different dark-side reheat
   chain. **Closing the ζ gap is the assembly's promotion gate; the gap
   proving unclosable at any legal roster is its kill.**
