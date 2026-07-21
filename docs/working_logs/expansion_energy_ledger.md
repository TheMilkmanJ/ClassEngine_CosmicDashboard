# The expansion-energy ledger — Friedmann as +kinetic/−binding, and its honest cost

*What is the "expansion energy"? The chase's answer: **not a new substance.** The expansion is the
medium's own collective motion — the same medium that spreads (kinetic), binds (induced gravity), and
sinks (dilution). This log writes the ledger explicitly (the gap the corpus left) and grades it
without flattery. Code: `scripts/friedmann_from_medium.py` (self-checking; anchors in the harness).*

## The ledger

**Friedmann is an energy balance.** For a comoving sphere (physical radius r = aχ, mass
M = (4/3)πr³ρ, ṙ = Hr), the energy per unit test mass on its surface is E = ½ṙ² − GM/r. A **flat**
universe is E = 0, i.e. the expansion **kinetic** energy `+½H²r²` exactly cancels the gravitational
**binding** `−(4/3)πGρr²`, which rearranges to **H² = (8πG/3)ρ**. Verified to machine precision at
H = 67 km/s/Mpc. In the medium reading: the medium's spreading is balanced by its own induced-gravity
self-attraction, and the flat universe carries **zero net energy** — the cosmic "free lunch," now
read as the medium's kinetic against the medium's binding.

**Local conservation is the first law.** With comoving volume V = a³ and U = ρa³, the continuity
equation ρ̇ + 3H(ρ+p) = 0 **is** dU = −p dV — verified component by component (radiation w = ⅓ →
ρ ∝ a⁻⁴, matter w = 0 → a⁻³, dark energy w = −1 → const). So energy is locally conserved in the
thermodynamic sense already: radiation **pays** energy (does +p dV work pushing space out), dark
energy is **paid** (its negative pressure is pulled on). There is no separate expansion-energy
reservoir; the content does p dV work on the growing volume, and the books close by the first law.

## What this is, and is not — graded without flattery

- **SHOWN:** the medium is **consistent** with Friedmann and the first law. It reproduces the
  expansion without breaking known cosmology. That is the minimum bar, and it clears it.
- **NOT a new result:** the Newtonian energy-balance route to H² = (8πG/3)ρ is textbook and holds for
  *any* Newton's constant. Reproducing it is consistency, **not correctness**, and not a triumph.
- **The PRTOE-specific claim, and it is UNBUILT:** that the medium supplies a well-defined, conserved
  **global** total energy — the thing GR genuinely cannot provide (its gravitational energy is
  non-localizable; only pseudotensors, no global conservation in an expanding spacetime). Showing
  that needs Friedmann derived **from** the medium's own energy functional, not merely shown
  consistent with it. Not done here. It is the actual object worth building.
- **The cost, and it is unavoidable:** a *localizable* energy requires the medium's **rest frame** — a
  **preferred frame**, hence Lorentz violation. The concreteness that makes this answer feel better
  than GR's is bought with an exposure GR does not carry, bounded to ~27 orders on the one live
  channel ([PRTOE_LV_pricing.md](../PRTOE_LV_pricing.md)). More concrete is here also **more
  falsifiable** — not more likely true.

**Net:** the expansion energy is the **medium's own collective motion** — spreading, binding, and
sinking are one flow, not three substances — and it nets to zero against its binding the way every
flat-universe expansion does. What is *not* yet shown is the part that would actually beat GR: a
conserved global total in the medium. And what it *costs* is a preferred frame. Consistent, concrete,
more falsifiable — not shown correct.

## The localizable zero, on the board at the burst (T = m_e)

The claim "the medium hosts a *localizable* zero" is now a computation, not an argument
(`scripts/localizable_zero_burst.py`). At the burst temperature T = m_e = 0.511 MeV, the relativistic
medium has ρ = 5.0×10²⁴ J/m³; one Hubble volume holds M = 1.1×10³⁶ kg; and a test mass on the Hubble
sphere (receding at exactly c) carries expansion energy **+4.494×10¹⁶ J/kg** against gravitational
binding **−4.494×10¹⁶ J/kg** — cancelling to machine zero. Equivalently the **Hubble radius equals the
Schwarzschild radius** of the enclosed mass exactly (R_H/R_s = 1 for a flat universe): the burst sits
at its own Schwarzschild radius, so its glow is bound to net zero, which is why it needs no
counterparty to pour from. Both halves are the medium's — its collective recession, its induced
gravity. *Exact and computed; still not shown: the bounce (why it turns at m_e), the total magnitude
(needs L_gen, #180), Friedmann derived FROM the medium's energy functional, and the preferred-frame
cost is deferred not paid.*

## Sources

Standard: the Newtonian energy-balance derivation of Friedmann (Milne–McCrea); the continuity
equation as the first law. Internal: induced gravity ([PRTOE_quantum_gravity.md](../PRTOE_quantum_gravity.md)),
the preferred-frame cost ([PRTOE_LV_pricing.md](../PRTOE_LV_pricing.md)), the DE floor it does *not*
change ([PRTOE_cosmological_constant.md](../PRTOE_cosmological_constant.md)).
