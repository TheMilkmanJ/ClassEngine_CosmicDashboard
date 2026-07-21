# The deuterium scar

*The model's weakest measured row, isolated and taken apart. The finding: the deficit is not made
in the nuclear sector — the dyad's own BBN physics **improves** deuterium — it is imported from the
CMB fit, and it is the same object as the H₀ result seen from the other end. Status: **answered as
structure** — an owned adverse trade with a named missing ingredient the field content cannot
supply; not an unfinished calculation (§8).*

---

## 1. The number

The model predicts **D/H = 2.387×10⁻⁵**. The quasar-optical measurement is **2.527 ± 0.030**
(Cooke).

**The error budget, settled 2026-07-21 (#157).** Two components, one width:

| component | value | what it is |
|---|---|---|
| observational | ±0.030 | Cooke's quasar-optical measurement error |
| BBN nuclear theory | ±0.037 | PRIMAT **post-LUNA** (arXiv:2011.11320, D/H = 2.439 ± 0.037) |

> **Standing width ±0.0476** = observational ⊕ nuclear theory → the standing row reads **−2.94σ**.

**Why not three terms.** A third ±0.0300 for d(p,γ)³He was carried for a time as a separate
nuclear-rate uncertainty, giving ±0.0563 and a friendlier −2.49σ. That folding is **retired**:
PRIMAT's ±0.037 is the Monte-Carlo prediction error *after* adopting the LUNA D(p,γ)³He rate
(Mossa et al. 2020; Table 1 and §2.2 of arXiv:2011.11320), varying nuclear rates, τ_n, and the
CMB+BAO baryon posterior. Adding d(p,γ)³He again double-counts the dominant deuterium destruction
channel. The retired three-term arithmetic is pinned in the harness so a stale −2.49σ is caught on
sight, and the kill is in `PRTOE_FAILURES_LEDGER.md`.

**Why this was hard to see.** The third term is numerically equal to the observational error, so
observational ⊕ nuclear and nuclear ⊕ rate both give **±0.0476** to five figures — no arithmetic
check can separate them. Only the citation settles it. *(An earlier attribution also named
⁴He(d,γ)⁶Li as a D/H driver; that reaction is a ⁶Li channel and is not one.)*

Applying the genesis residual, the quotable committed window is **−2.5σ to −1.4σ** on this same
two-term width. That range is unchanged by the ruling; only the standing (pre-window-edge) figure
moves from the retired −2.49σ to **−2.94σ**.

**Against ΛCDM, honestly.** The in-house ΛCDM control on identical data and the same code gives
D/H = 2.420×10⁻⁵, which is **−2.25σ** on the standing width. So:

| | D/H ×10⁵ | vs Cooke |
|---|---|---|
| ΛCDM control (same code, same data) | 2.420 | −2.25σ |
| **PRTOE** | **2.387** | **−2.94σ** |

**The model is worse than ΛCDM on deuterium by 0.69σ.** It is not solved and it is not better. Any
reading of what follows has to start there.

One piece of context, not a defence: the inter-code spread on the same physics (PRIMAT 2.439,
PArthENoPE 2.51–2.54) is ~0.08 in these units, larger than the model's 0.033 excess deficit. ΛCDM
itself carries 1.85σ under PRIMAT. The field's own systematic floor is above the gap between the
two models — which bounds how much this row can currently decide, in either direction.

---

## 2. Where the deficit is made — and where it is not

The prediction is built in two steps from the ΛCDM control. Taking them apart is the whole point of
this file:

| step | D/H ×10⁵ | change | σ moved (2-term) |
|---|---|---|---|
| ΛCDM control | 2.420 | — | — |
| ω_b pulled up +1.1% (the CMB fit) | 2.372 | **−1.98%** | **−1.01σ** |
| the dyad's BBN window, +0.645% | 2.387 | **+0.645%** | **+0.31σ** |
| **net** | **2.387** | −1.36% | **−0.69σ** |

**The dyad's own nuclear physics helps deuterium.** The ε(T) ramp switching on at T_c ≈ 179 keV
raises D/H by 0.645%, moving it *toward* Cooke — worth +0.31σ. Grafted onto the ΛCDM control alone
it would give D/H = 2.435, or −1.93σ, better than the control's −2.25σ.

**That last sentence is a decomposition, not a scenario, and the distinction matters.** The window
and the ω_b shift are both consequences of the same ε — one at nucleosynthesis, one at
recombination. There is no configuration of this model that has the window without the baryon shift,
so "the dyad beats ΛCDM on deuterium" is not a claim available to it. What the counterfactual
establishes is narrower and still worth having: **the deficit is not manufactured in the nuclear
sector.** Attributing it correctly is what tells you which cures can work.

**The deficit is carried entirely by the baryon density.** The CMB fit returns ω_b 1.1% above the
control, because varying m_e and ω_b are degenerate in the acoustic peaks. Deuterium is the most
ω_b-sensitive abundance in the network — the production run gives
d ln(D/H)/d ln ω_b = **−1.83** — so a 1.1% baryon shift becomes a 2.0% deuterium loss, three times
larger than the window's help and in the opposite direction.

*(The corpus elsewhere quotes −1.6 for that exponent as a rule of thumb. The production run is the
authority and gives −1.83; the rule of thumb understates the sensitivity by 14%.)*

---

## 3. The exchange rate — deuterium and H₀ are one object

The same fit that pulls ω_b up is what delivers the model's H₀ result: **68.2 → 69.9 km/s/Mpc**,
same data, same pipeline. The two move together along one degeneracy direction. That fixes a rate:

> **+1.7 km/s/Mpc of H₀ arrives with +1.1% of ω_b, which costs 1.01σ of deuterium.**
>
> **0.59σ of deuterium per km/s/Mpc of H₀.**

**What the rate is, and what it is not.** It is a secant between two computed points — the model's
fit and the ΛCDM control — not a slope measured along the degeneracy. Over the 1.7 km/s/Mpc that
separates them it is as good as the two endpoints. Beyond that it is an extrapolation, and the
table below says how far:

| target | H₀ given back | H₀ lands at | status |
|---|---|---|---|
| parity with the ΛCDM control | 1.17 km/s/Mpc | 68.7 | inside the measured interval |
| deuterium at −1.0σ | 2.97 km/s/Mpc | 66.9 | 1.7× beyond it |
| deuterium centred on Cooke | 4.96 km/s/Mpc | 64.9 | 2.9× beyond it |

Only the first row is interpolation. The lower two assume the degeneracy stays linear well past
where it was measured, which is not established — they should be read as showing the direction and
rough scale of the trade, not as predicted landing points.

**Even taking only the first row, reaching parity with ΛCDM costs 69% of the H₀ relief.** That much
is inside the measured range and does not depend on the extrapolation. The deuterium scar and the H₀ result are not two
problems; they are one trade, and the model is currently sitting at the end of it that buys H₀.

**The m_e degeneracy audit (Q2/#20), first measurement 2026-07-21.** The free-`varying_me`
`dyad_mnu` chain (N ≈ 8700 post burn-in) measures the ridge directly:

| quantity | value |
|---|---|
| corr(ω_b, m_e) | **+0.69** |
| ridge | ω_b = 0.022560 + 0.01621·(m_e − 1) |
| at m_e = 1 | ω_b = 0.022560 (+0.19% vs ΛCDM control 0.022517) |
| at derived m_e = 1.012543 | ω_b = 0.022764 (+1.10% vs ΛCDM) |
| posterior mean | ω_b = 0.022762, m_e = 1.01246 ± 0.00456 (**2.7σ from 1**) |

**Essentially all of the +1.1% is forced by the m_e shift along the ridge.** The free-slide residual
beyond the derived amplitude is consistent with zero (mean tracks the ridge to 0.01%). The shift is
not a pure degeneracy artifact: the data pull m_e off 1 at 2.7σ on this chain. What the audit does
*not* yet do is re-fit with a deuterium likelihood in the joint — that is still the correct next
treatment (§7 item 2), and it is where the −0.69σ either shrinks or is confirmed as the model's real
price. **Deuterium remains the natural degeneracy-breaker for the m_e–ω_b direction** — it constrains
ω_b without going through the CMB at all.

---

## 4. What this rules out

The rate above is a statement about one direction in parameter space. It has a sharp consequence
for what can cure the scar:

> **Any real cure must be orthogonal to the m_e–ω_b degeneracy — it must raise D/H at fixed ω_b and
> fixed m_e.** Anything that works by adjusting the fit pays the full exchange rate and surrenders
> the H₀ result.

That single test sorts every route the model has, and explains which ones survive.

---

## 5. The lever census

| route | mechanism | orthogonal? | verdict |
|---|---|---|---|
| slide back down the degeneracy | lower ω_b | **no** | works, at the rate in §3 — surrenders H₀ |
| constant dark radiation (ΔN_eff, all epochs) | faster expansion | **no** | wrong shape — see below |
| expansion boost confined below T_c | faster expansion, deuterium epoch only | **yes** | right shape, 8–33× too weak |
| helium photodissociation | late injection breaks ⁴He into D | **yes** | right shape, no source |
| shift m_e at BBN | changes the electron's contribution | **yes** | excluded by data at 12σ |
| shift m̂ at BBN (through B_D) | changes deuterium's binding | **yes** | no channel: the quark bilinear is two EW/EM loops down, and full ε on the quarks is itself excluded at 12–18σ |
| evaporating PBHs at 10¹¹ g (§5b) | hadronic spallation of ⁴He into D | **yes** | right shape on *both* rows; killed by the ⁶Li co-signature, 39–156×; pure-EM dodge closed (no T ∩ τ overlap) |

**Constant dark radiation fails on shape, not size.** It raises both abundances with the same sign,
but the two rows need opposite moves: deuterium is 2.5σ low and helium is already 1.09σ high. The
committed ζ window (ΔN_eff ≈ 0.06–0.24) tops out just under this lever's optimum (≈0.26). Zeroing deuterium takes
ΔN_eff = 0.42, which lands helium at +2.5 to +2.7σ against Aver and +4.9 to +5.1σ against EMPRESS —
trading a 2.5σ deficit for a 2.5σ excess.

**Confining the boost below T_c is the model's one native orthogonal lever, and it is real.** The
dyad's T_c ≈ 179 keV sits between helium's n/p freeze-out (~800 keV) and deuterium's bottleneck
(~70 keV). A component that switches on at T_c is *absent* when helium is set and *present* when
deuterium is set. Measured directly:

| | ∂ln(D/H)/∂N_eff | dY_p/dN_eff | deuterium per unit helium |
|---|---|---|---|
| all epochs | 0.1350 | 0.0131 | 10.3 |
| below T_c only | 0.1160 | 0.0041 | 28.3 |

**2.75× more efficient.** Deuterium keeps 86% of its leverage while helium's cost falls to 31%,
because n/p freeze-out is nearly all of the helium response but only part of the deuterium one.
Priced at the healing amplitude: ΔN_eff = 0.49 below T_c zeroes deuterium for ΔY_p = 0.0020,
landing helium at **+1.7σ instead of +2.7σ**.

The obstruction is size, not principle. The dark confinement transition (27 → 14 degrees of
freedom, reheat factor (27/14)^⅓ = 1.245) delivers a below-T_c excess of only **ΔN_eff =
0.015–0.059** — short by a factor of **8 to 33**.

**Photodissociation is the other orthogonal lever, and it is the cheapest cure on the books.**
Deuterium is fragile (2.22 MeV) but helium is abundant: ⁴He sits at 8.3% of hydrogen by number
against a deuterium abundance of 2.5×10⁻⁵. Breaking **1.7×10⁻⁵ of the helium** — a fraction far too
small to move Y_p (ΔY_p = −4.2×10⁻⁶, 0.001σ) — supplies enough deuterium to centre the row. The
timing window is set by thermal-bath opacity, **and it is a property of the photon channel, not of
the cure.** High-energy photons pair-produce off the CMB, which caps the surviving spectrum at
E_C ≈ m_e²/(22T); that cutoff clears ⁴He's 19.8 MeV only once T < 599 eV, i.e. after ~6 weeks. Since
deuterium is bound by only 2.22 MeV it is destroyed at every earlier time, so **an electromagnetic
injection before ~6 weeks destroys deuterium** and the deposit must land at **t > 4×10⁶ s**. A
*hadronic* injection is not subject to that cutoff — fast nucleons spall ⁴He whatever the photon
bath is doing — and in that channel the same interval net *produces* deuterium (§5b). The result would be **joint p = 0.135–0.43**, with helium
the only residual.

It needs a source with three properties at once: **mass ≳ 20 MeV** (so the cascade reaches the
⁴He threshold), **lifetime ~10⁶–10⁸ s** (so the deposit lands in the window), and an abundance
delivering **~30 eV per hydrogen**. **All three numbers are photon-channel quantities** — the mass
is the ⁴He photodissociation threshold, the lifetime is the pair-production cutoff's timing, and the
abundance is 1.7×10⁻⁵ × (He/H) × 20 MeV. The hadronic channel has its own, different spec (§5b).
The standing configuration supplies neither — see §6.

**The binding-energy route is two routes, and they are shut by different things.** Both move
deuterium through B_D rather than through the expansion rate, so neither touches helium at all —
the cleanest orthogonal levers in principle, and only a **0.2% shift** would close the row.

*Through the electron:* m_e = 1 at BBN is excluded at **12σ**. That is a data exclusion, not a
constitutional one; it stays closed until the data moves.

*Through the light quark mass:* this one is closed **by loop order and by this row itself**, not by
symmetry — and the distinction matters, because it is the difference between a door that is bolted
and one that is merely very far away. The dyad's portal is the dark-neutral bilinear |Ψ|², a total
singlet, which reaches the quark bilinear only through a loop — dyad → lepton loop → 2γ → quark,
suppressed by **(α/π)² = 5.4×10⁻⁶**. Applied to the dyad's own amplitude that delivers 6.8×10⁻⁶
percent where P-2026-006 needs 0.14–0.21% — short by a factor of **21,000 to 31,000**. A quark
shift anywhere near what a heal would need is independently excluded at **12–18σ** by the very row
it would be healing.

*(This was argued for a time as forbidden **by the model's own symmetry** — the dyad read as the
Majoron, so that lepton number would forbid a quark coupling outright. That route is closed:
the dyad and the Majoron are separate fields, and |Ψ|² is L-neutral, so U(1)_L screens the quark
bilinear no more than the lepton one. The conclusion is unchanged and the margin is four orders
wider than it needs to be — but it is a quantitative wall, not a constitutional one, and this
paragraph previously claimed the opposite.)*

This is the sharpest statement of where the scar comes from. **The model's one matter-to-matter
channel is the lepton current, and deuterium's binding is nuclear.** The dyad can reach the
electron and cannot reach the nucleus, and reopening the quark door means surrendering the Majoron
identification — which the entire neutrino sector rests on.


**⁶Li is this file's only spallation-aware constraint, and it kills the one lever that had the
right shape.** The section below records it.

---

## 5b. The hadronic channel, and the one source that got past the roster

Everything above §5's photodissociation row is electromagnetic: the ≳20 MeV threshold, the
six-week window, the ³He co-signature are all properties of a *photon* cascade. There is a second
channel. **Hadro-dissociation** — energetic free nucleons spalling ⁴He directly — is not subject to
the photon bath's pair-production cutoff, so its window opens earlier (τ ≲ 10⁷ s rather than
t > 4×10⁶ s), and its net effect is the literature's, not a hope: an increase in D and a decrease
in ⁴He (Carr, Kohri, Sendouda & Yokoyama, Rep. Prog. Phys. 84, 116902 (2021), and references
therein). **That is the right shape on both rows at once** — the only mechanism in this census that
moves deuterium up while moving helium down — and the price of entry is steep: the parent must
fragment into hadrons, so it must clear ~2m_N ≈ 1.9 GeV, ninety times the photon channel's
threshold. Every field-content candidate that failed the photon spec by being too light fails this
one by more.

**One source is exempt from the roster, and it is the only one.** Pauli finiteness (P-2026-045)
counts *fields* — sixteen Weyl fermions per generation, every seat taken. A black hole is not a
field and adds nothing to str[k₁]. An evaporating primordial black hole therefore enters this
census without touching the balance that forces three generations, and its Hawking emission is
identity-blind — it needs no lepton charge, so the census's leptophilic lock does not bind it. The
numbers land in the window without tuning: τ ∝ M³ puts evaporation at t = 4×10⁶–10⁸ s for
**M = 1.1–3.1×10¹¹ g**, with Hawking temperatures of 34–99 GeV — comfortably above the hadronic
threshold, fragmenting into QCD jets whose nucleons do the spalling. The required abundance is an
initial mass fraction β ~ 2×10⁻²⁸ at unit cascade efficiency.

**The kill is the co-signature, and it is efficiency-free.** Nucleon spallation of ⁴He produces
non-thermal **⁶Li** alongside the deuterium, and ⁶Li/H is bound far more tightly than D/H is. Read
off the BBN constraint figure of the Carr et al. review (curves extracted from the vector source
and calibrated against the figure's own axis ticks), at M = 10¹¹ g:

> β′(⁶Li) = 4.6×10⁻²⁶  ·  β′(D) = 1.5×10⁻²⁴ — **lithium binds 33× tighter than deuterium.**

The decisive form of the argument needs no cascade model at all. Both curves are computed from the
same PBH population, so whatever the cascade efficiency is, it multiplies the D yield and the ⁶Li
yield alike, and the 33× gap between the bounds is a **nuclear yield ratio** — model-free. At the
⁶Li bound, deuterium has moved only 0.04–0.15% (the spread being where the D curve's own tolerance
is drawn); this row needs +5.9%. **Short by 39–156×, independent of efficiency, abundance, or the
mass within the window.** A one-parameter population cannot dodge it: temperature and lifetime are
locked to each other through M, so there is no corner of the window where the deuterium arrives
without the lithium.

**Verdict: killed by the ⁶Li co-signature** — the census's first entry killed neither by shape,
size, nor symmetry, but by a receipt. The route's post-mortem is worth its line: it was the only
candidate to clear the roster, the only one with the right shape on both rows, and it failed on a
number that is nuclear physics rather than model structure. *(The five-lever audit's earlier PBH
kill addressed PBHs as an expansion-rate component — a different job; this entry prices them as an
injector, which had never been done.)*

**The pure-EM dodge is closed too (2026-07-21).** Hawking temperature and lifetime lock through M.
In the ⁴He photodissociation window (t ~ 4×10⁶–10⁸ s) every evaporating PBH has
T_H ~ 35–100 GeV — fully hadronic, well above Λ_QCD. Cooling to T_H ≲ 200 MeV (to suppress
hadrons and hope for an electromagnetic-only cascade) forces M ≳ 5×10¹³ g and τ ≳ 5×10¹⁴ s —
years to Gyr later, outside the window by six orders. **There is no mass that is both on-time for
⁴He photodissociation and cool enough to be EM-only.** Microscopic black holes cannot be the
electromagnetic cure either. Both kills are in `PRTOE_FAILURES_LEDGER.md`.

---

## 6. What is missing, named

The census leaves exactly one shape of object unaccounted for:

> **A state of mass ≳ 20 MeV with a lifetime of 10⁶–10⁸ s and an abundance carrying ~30 eV per
> hydrogen — for an electromagnetic injection.** The hadronic channel asks for a heavier parent and
> a wider window; §5b states it. Neither is supplied.

The standing configuration cannot currently supply it, and the reasons are specific rather than
accidental:

- **The dCDF cannot decay.** Its shift symmetry forbids it, and this is load-bearing elsewhere — a
  confirmed dark-sector decay line is a registered falsifier of the dCDF identification. Giving the
  medium a decay channel to heal deuterium would trade this row for that one.
- **The dyad and the census portal are too long-lived.** Decay constants of 100–500 TeV and
  13–20 TeV put their lifetimes beyond cosmological by many orders.
- **The Majoron is far too light.** Its recorded mass is m_J ~ (1–3)H₀, some 30 orders below the
  20 MeV threshold. Its MeV corner refers to the L-breaking scale v_L, not to a state at that mass.

**And the field content is not merely short of one — it is provably full.** P-2026-045 registers
Pauli finiteness, str[k₁] = 16·N_gen − 48 = 0, satisfied exactly by the Standard Model plus three
right-handed neutrinos: **sixteen Weyl fermions per generation, every seat taken.** Adding one
returns +3 instead of 0, and the balance that breaks is the same one that forces N_gen = 3. The
entry's own named kills are "a light sterile; a 4th generation" — precisely the object a cure would
need. So the price of healing this row is the three-generation derivation, which is the strongest
statement available about why the row stays open.

**The three seats that do exist are too light.** At the MeV corner of v_L the seesaw puts the
right-handed neutrinos near 4.2 MeV, against a ⁴He photodissociation threshold of 19.8–20.6 MeV —
short by **4.7 to 4.9×**, and a threshold does not partly fire.

**The transition route reduces to this one — it does not replace it.** A natural alternative is to
ask for a *vacuum* that releases rather than a *particle* that decays: a field trapped in a false
vacuum at a 20 MeV scale, firing late. The two are not the same object, and the difference is
instructive. **A particle species can be arbitrarily dilute, because its abundance is free; a false
vacuum's energy density is fixed at Λ⁴ and cannot be.** Filling space, a 20 MeV vacuum carries
2.1×10⁴³ eV/cm³ against an ambient 1.5×10²⁵ at the deposit epoch — it would dominate by **1.4×10¹⁸**
and drive a second inflation, not warm the plasma by 30 eV per baryon.

Tuned instead to deliver exactly the required injection, it may occupy no more than **5×10⁻³⁰ of
space** — at which point it is not a vacuum phase at all but a dilute population of isolated,
localized lumps each carrying ~20 MeV. That is a particle species, and the requirement lands back
on the roster it started from. What the two routes genuinely share is the **energy scale**; the
abundance is where they part, and it parts by thirty orders.

So the missing ingredient is not a free parameter that has yet to be fixed — it is a state the
current field content **cannot** contain. That is a real structural statement about where a cure
would have to come from, and it is worth more than a fitted patch.

**The honest reading of the constitution.** The dark sector couples to the Standard Model
gravitationally and nothing else. That law is exactly what forces every native lever to be an
expansion lever — and §5 shows expansion levers are the wrong shape for this row. The two levers
with the right shape both act on deuterium's own physics (its binding, its destruction) rather than
on the universe's expansion, and both are therefore non-gravitational in character. The scar is the
gravitational-only law's price, stated plainly. Whether that law should hold in this corner is a
live question, not a settled one — but it is a question about the model's foundations, not about
deuterium, and it should be answered there.

---

## 6b. Do the levers add?

The obvious question about a census of partial cures is whether they sum. Asked and answered: they
do not, and the reason is that **the failures are of three kinds and only one of them is additive.**

| lever | kind of failure | contributes |
|---|---|---|
| the below-T_c boost | **too weak** — 8–33× short | **+0.09σ to +0.34σ** — real, and the largest additive term |
| a sharper transition (0.61ε → 1.0ε at the bottleneck) | blocked by the Ginzburg certification | +0.21σ, and only if that certification is broken |
| the dyad → lepton loop → 2γ → quark bridge | **too weak** — two EW/EM loops, 20 000–31 000× short of the lever it would need | **+8×10⁻⁵σ** — nonzero, and four orders under the smallest term above |
| a right-handed neutrino at 4.2 MeV | **below threshold** — ⁴He needs 19.8–20.6 MeV | **exactly zero**; thresholds do not partly fire |
| m_e at BBN | data-excluded at 12σ | unusable at any fraction |
| constant ΔN_eff | wrong shape | negative — buys deuterium, sells helium at +4.9σ |

Adding the two terms of usable size, **and** breaking the Ginzburg certification to
include the sharper transition, moves the row from **−2.94σ to −2.39σ** (the quark bridge's
+8×10⁻⁵σ is four orders too small to register). It survives at about 2.4σ.

Two things this makes explicit. First, a 2.94σ deficit needs a lever of order the deficit, and
everything available is sub-0.35σ — closing it by summation would take eight or nine independent
partial levers, and there are two. Second, and easier to get wrong: **the window's +0.31σ is
already inside the −2.94σ.** The 2.387 figure is the value *after* the dyad's BBN window helped, so
counting the window again as a separate lever would be counting the same physics twice.

---

## 7. What would move the books

Ranked by how much they would change the row, cheapest first:

1. **The m_e degeneracy audit — first pass done (§3).** The free-m_e chain says the +1.1% is forced
   by the ridge, not free slide. What remains is tightening (multi-chain, fixed-m_e control re-fit)
   and the deuterium joint below.
2. **A deuterium-inclusive joint fit.** Adding the D/H likelihood to the CMB fit lets the data pick
   the point on the degeneracy instead of the CMB alone. This is the correct treatment regardless
   of outcome, and it is where the −0.69σ either shrinks or is confirmed as the model's real price.
3. **The below-T_c reheat — checked, and it closes.** The lever is right and short by 8–33×, and
   the shortfall rides on one count. Both ends of that count are forced by group theory: the
   deconfined g* = 2(N_c²−1) + (7/8)(4N_cN_f) = **27** for SU(2) with three flavours, and the
   confined side is the Goldstone count of SU(2N_f) → Sp(2N_f) = 2N_f² − N_f − 1 = **14**. Neither
   has a dial, and N_c = 2 and N_f = 3 are themselves fixed by the same finiteness balance that
   gives three generations. **The shortfall cannot narrow.** The model's one native orthogonal
   lever is permanently 8–33× too weak.
4. **The BBN code systematic.** The model runs PRyM, a third code, against a tension defined by the
   PRIMAT/PArthENoPE spread. A cross-code run of the model's own configuration would say how much of
   the −2.94σ is physics and how much is the code.
5. **P-2026-027's radio referee.** The model sits on the low side of the deuterium fork as an owned,
   self-adverse bet. The referee decides it from the other direction entirely.

---

## 8. The answer (not a patch)

**What the scar is.** It is not a bug in the nuclear sector and not an unfinished fit. The dyad's
own BBN window *helps* deuterium. The deficit is the CMB fit's +1.1% in ω_b, forced by the m_e–ω_b
ridge (degeneracy audit, 2026-07-21: free-slide residual consistent with zero; m_e off 1 at ~2.7σ).
That same ridge is the H₀ relief. **D/H and H₀ are one trade.** Standing row: **−2.94σ** on the
two-term width (#157).

**What does not fix it** — checked, not hoped:

| candidate | why it is not the answer |
|---|---|
| slide ω_b back / joint D/H fit | works only by selling H₀ (or fighting the CMB); prices the trade, does not cancel it |
| constant ΔN_eff | wrong shape — helium already high |
| below-T_c reheat | right shape, permanently 8–33× too weak (dof count forced) |
| quark / binding door | loop floor ~20 000× short, or data-excluded |
| field-content particle at the EM spec | roster full (P-2026-045); adding a seat breaks three generations |
| MeV-corner ν_R (~4.2 MeV) | below the ⁴He threshold; a threshold does not partly fire |
| evaporating PBHs (hadronic) | ⁶Li co-signature, 39–156× |
| evaporating PBHs (pure EM) | no mass is both on-time and cool enough |
| false vacuum at 20 MeV | space-filling over-delivers by 10¹⁸; dilute limit is a particle again |
| intermediate M_N ~ 20–50 MeV with seesaw τ | *near-miss only* — mass/lifetime can land in the EM window under U²~m/M, but (i) that is not either surviving v_L corner, (ii) abundance ~30 eV/H is a third requirement and does not follow from seating, (iii) claiming it would be inventing a third corner the sector does not currently select |

**What the answer is.** The scar is the **owned structural price** of two load-bearing choices
together:

1. **varying-m_e as the H₀ lever** — which forces +ω_b along a CMB degeneracy that deuterium
   reads as a deficit;
2. **gravitational-only dark–SM coupling** — which forces every *native* lever to be an expansion
   lever, and expansion levers are the wrong shape for this row.

The named missing piece (≳20 MeV, 10⁶–10⁸ s, ~30 eV/H electromagnetic injector) is real as a
*spec*. The standing configuration cannot contain a source for it without breaking something that
elsewhere is load-bearing (Pauli finiteness, dCDF shift symmetry, or the H₀ result itself). That is
why the row stays open as an **owned adverse bet**, not as an unfinished calculation.

**What still changes the number without being a fake cure** (external or diagnostic, not a patch):

- P-2026-027's radio referee — decides the fork from the other side;
- BBN code systematic (PRyM vs PRIMAT/PArthENoPE) — how much of −2.94σ is code vs physics;
- a production-faithful D/H term in the joint likelihood — the live chain's BBN prior still uses a
  stale formula (exponent −1.6, obs-only width, D/H~2.47 at the mean vs production 2.39); fixing
  that is honesty about the trade's price, not a heal;
- CMB-S4 on the Majoron corner — selects v_L; it does **not** by itself supply the 20 MeV injector
  (the MeV corner is a scale, not that state).

**One-line answer.** The deuterium scar is the H₀ mechanism's other face under a gravitational-only
dark sector; the model has named the only shape of object that would break the tie and does not
contain one.

---

## 9. In plain language

The model makes slightly too little deuterium — less than ΛCDM does, and both make less than
astronomers measure. The surprise is where the shortfall comes from. The new physics that acts
during nucleosynthesis itself actually *helps*: it pushes deuterium up, in the right direction, by
about half of what is needed to beat ΛCDM.

What overwhelms it comes from somewhere else entirely. Fitting the cosmic microwave background
requires slightly more ordinary matter — 1.1% more — and deuterium is the one element that is
acutely sensitive to exactly that. That 1.1% costs three times what the nuclear physics gained.

And the extra matter is not optional: it arrives with the model's headline result, the higher
expansion rate that eases the Hubble tension. So the two are the same trade. Buying back the
deuterium means selling the Hubble result, roughly two-thirds of it just to draw level with
standard cosmology.

The way out cannot be an adjustment; it has to be a genuinely different effect — something that
makes deuterium without touching how fast the universe expands. There are two candidates that would
work, and the model knows precisely what shape the missing piece has: a particle of a specific mass,
decaying at a specific time, in a specific amount. It does not currently have one. That is the
answer, not a temporary gap in the fit.

---

*Sources: [PRTOE_bbn_witness.md](PRTOE_bbn_witness.md) (the standing books and the two-run
discipline), [PRTOE_hubble_tension.md](PRTOE_hubble_tension.md) (the H₀ result),
[PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md) (the Majoron corners),
[PRTOE_honest_status.md](PRTOE_honest_status.md) (the m_e audit's standing),
[PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) (PBH and three-term kills).
Every number in §1–§5 is recomputed by `scripts/audit_math_pass.py`.*
