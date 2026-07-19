# The deuterium scar

*The model's weakest measured row, isolated and taken apart. The finding: the deficit is not made
in the nuclear sector — the dyad's own BBN physics **improves** deuterium — it is imported from the
CMB fit, and it is the same object as the H₀ result seen from the other end. Status: an open
deficit with a priced cure and a named missing ingredient.*

---

## 1. The number

The model predicts **D/H = 2.387×10⁻⁵**. The quasar-optical measurement is **2.527 ± 0.030**
(Cooke). With the theory budget the corpus carries (±0.0476, dominated by the ⁴He(d,γ)⁶Li and
d(p,γ)³He rate uncertainties), the combined width is 0.0563 and the row sits at **−2.49σ**.

Applying the genesis residual and the code-systematic spread, the quotable range is **−2.5σ to
−1.4σ**. That range is the standing book, and this file does not narrow it.

**Against ΛCDM, honestly.** The in-house ΛCDM control on identical data and the same code gives
D/H = 2.420×10⁻⁵, which is **−1.90σ** on the same budget. So:

| | D/H ×10⁵ | vs Cooke |
|---|---|---|
| ΛCDM control (same code, same data) | 2.420 | −1.90σ |
| **PRTOE** | **2.387** | **−2.49σ** |

**The model is worse than ΛCDM on deuterium by 0.59σ.** It is not solved and it is not better. Any
reading of what follows has to start there.

One piece of context, not a defence: the inter-code spread on the same physics (PRIMAT 2.439,
PArthENoPE 2.51–2.54) is ~0.08 in these units, larger than the model's 0.033 excess deficit. ΛCDM
itself carries 1.85σ under PRIMAT. The field's own systematic floor is above the gap between the
two models — which bounds how much this row can currently decide, in either direction.

---

## 2. Where the deficit is made — and where it is not

The prediction is built in two steps from the ΛCDM control. Taking them apart is the whole point of
this file:

| step | D/H ×10⁵ | change | σ moved |
|---|---|---|---|
| ΛCDM control | 2.420 | — | — |
| ω_b pulled up +1.1% (the CMB fit) | 2.372 | **−1.98%** | **−0.85σ** |
| the dyad's BBN window, +0.645% | 2.387 | **+0.645%** | **+0.27σ** |
| **net** | **2.387** | −1.36% | **−0.59σ** |

**The dyad's own nuclear physics helps deuterium.** The ε(T) ramp switching on at T_c ≈ 179 keV
raises D/H by 0.645%, moving it *toward* Cooke — worth +0.27σ. Grafted onto the ΛCDM control alone
it would give D/H = 2.435, or −1.63σ, better than the control's −1.90σ.

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

> **+1.7 km/s/Mpc of H₀ arrives with +1.1% of ω_b, which costs 0.85σ of deuterium.**
>
> **0.50σ of deuterium per km/s/Mpc of H₀.**

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

This is why the m_e degeneracy audit is the corpus's highest-value un-run test: it measures how
much of the +1.1% is forced by the m_e physics and how much is the fit sliding freely along a
direction that a deuterium likelihood would pin. **Deuterium is the natural degeneracy-breaker for
the m_e–ω_b direction** — it constrains ω_b without going through the CMB at all.

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
| shift m̂ at BBN (through B_D) | changes deuterium's binding | **yes** | symmetry-forbidden: quarks carry L = 0 |

**Constant dark radiation fails on shape, not size.** It raises both abundances with the same sign,
but the two rows need opposite moves: deuterium is 2.5σ low and helium is already 1.09σ high. The
committed ζ window (ΔN_eff ≈ 0.26–0.29) sits at this lever's optimum. Zeroing deuterium takes
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
timing window is set by thermal-bath opacity: an injection before ~6 weeks *destroys* deuterium, so
the deposit must land at **t > 4×10⁶ s**. The result would be **joint p = 0.135–0.43**, with helium
the only residual.

It needs a source with three properties at once: **mass ≳ 20 MeV** (so the cascade reaches the
⁴He threshold), **lifetime ~10⁶–10⁸ s** (so the deposit lands in the window), and an abundance
delivering **~30 eV per hydrogen**. The standing configuration does not supply one — see §6.

**The binding-energy route is two routes, and they are shut by different things.** Both move
deuterium through B_D rather than through the expansion rate, so neither touches helium at all —
the cleanest orthogonal levers in principle, and only a **0.2% shift** would close the row.

*Through the electron:* m_e = 1 at BBN is excluded at **12σ**. That is a data exclusion, not a
constitutional one; it stays closed until the data moves.

*Through the light quark mass:* this one is **forbidden by the model's own symmetry**, and the
distinction matters because it cannot be reopened by better data. The dyad **is** the Majoron, the
Goldstone of U(1)_L breaking, so it couples to the current of its broken charge — and **quarks
carry L = 0**, making the tree coupling exactly zero rather than small. The only surviving path is
a loop, dyad → lepton loop → 2γ → quark, suppressed by **(α/π)² = 5.4×10⁻⁶**. Applied to the dyad's
own amplitude that delivers 6.8×10⁻⁶ percent where P-2026-006 needs 0.14–0.21% — short by a factor
of **21,000 to 31,000**.

This is the sharpest statement of where the scar comes from. **The model's one matter-to-matter
channel is the lepton current, and deuterium's binding is nuclear.** The dyad can reach the
electron and cannot reach the nucleus, and reopening the quark door means surrendering the Majoron
identification — which the entire neutrino sector rests on.

---

## 6. What is missing, named

The census leaves exactly one shape of object unaccounted for:

> **A state of mass ≳ 20 MeV with a lifetime of 10⁶–10⁸ s and an abundance carrying ~30 eV per
> hydrogen.**

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
| the below-T_c boost | **too weak** — 8–33× short | **+0.09σ to +0.34σ** — real, and the only additive term |
| a sharper transition (0.61ε → 1.0ε at the bottleneck) | blocked by the Ginzburg certification | +0.21σ, and only if that certification is broken |
| the dyad → lepton loop → 2γ → quark bridge | **forbidden** — quarks carry L = 0 | **exactly zero**; the tree amplitude is not small, it is absent |
| a right-handed neutrino at 4.2 MeV | **below threshold** — ⁴He needs 19.8–20.6 MeV | **exactly zero**; thresholds do not partly fire |
| m_e at BBN | data-excluded at 12σ | unusable at any fraction |
| constant ΔN_eff | wrong shape | negative — buys deuterium, sells helium at +4.9σ |

Adding everything that is not identically zero, **and** breaking the Ginzburg certification to
include the sharper transition, moves the row from **−2.49σ to −1.94σ**. It survives at about 2σ.

Two things this makes explicit. First, a 2.49σ deficit needs a lever of order the deficit, and
everything available is sub-0.35σ — closing it by summation would take seven or eight independent
partial levers, and there are two. Second, and easier to get wrong: **the window's +0.27σ is
already inside the −2.49σ.** The 2.387 figure is the value *after* the dyad's BBN window helped, so
counting the window again as a separate lever would be counting the same physics twice.

---

## 7. What would move the books

Ranked by how much they would change the row, cheapest first:

1. **The m_e degeneracy audit.** Measures how much of the +1.1% ω_b shift is forced. If a
   meaningful part of it is free, deuterium improves at a fraction of the §3 rate and the whole
   trade is re-priced. Runnable; nothing is gated on hardware.
2. **A deuterium-inclusive joint fit.** Adding the D/H likelihood to the CMB fit lets the data pick
   the point on the degeneracy instead of the CMB alone. This is the correct treatment regardless
   of outcome, and it is where the −0.59σ either shrinks or is confirmed as the model's real price.
3. **The below-T_c reheat — checked, and it closes.** The lever is right and short by 8–33×, and
   the shortfall rides on one count. Both ends of that count are forced by group theory: the
   deconfined g* = 2(N_c²−1) + (7/8)(4N_cN_f) = **27** for SU(2) with three flavours, and the
   confined side is the Goldstone count of SU(2N_f) → Sp(2N_f) = 2N_f² − N_f − 1 = **14**. Neither
   has a dial, and N_c = 2 and N_f = 3 are themselves fixed by the same finiteness balance that
   gives three generations. **The shortfall cannot narrow.** The model's one native orthogonal
   lever is permanently 8–33× too weak.
4. **The BBN code systematic.** The model runs PRyM, a third code, against a tension defined by the
   PRIMAT/PArthENoPE spread. A cross-code run of the model's own configuration would say how much of
   the −2.49σ is physics and how much is the code.
5. **P-2026-027's radio referee.** The model sits on the low side of the deuterium fork as an owned,
   self-adverse bet. The referee decides it from the other direction entirely.

---

## 8. In plain language

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
decaying at a specific time, in a specific amount. It does not currently have one.

---

*Sources: [PRTOE_bbn_witness.md](PRTOE_bbn_witness.md) (the standing books and the two-run
discipline), [PRTOE_hubble_tension.md](PRTOE_hubble_tension.md) (the H₀ result),
[PRTOE_neutrino_sector.md](PRTOE_neutrino_sector.md) (the Majoron corners),
[PRTOE_honest_status.md](PRTOE_honest_status.md) (the m_e audit's standing).
Every number in §1–§5 is recomputed by `scripts/audit_math_pass.py`.*
