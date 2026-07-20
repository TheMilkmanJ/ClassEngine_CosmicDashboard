# Link 5 — the joint genesis draw: sign(θ̇·n) is a coin the model cannot call

Link 5 of the helicity sign map owes the product **sign(θ̇·n)** — whether the genesis field's
zero-mode rotation θ̇ (which signs the matter-vs-antimatter draw, μ = θ̇) is correlated with its
spatial winding n = ∮∇θ·dl ⁄ 2π (which signs the magnetic helicity). The two halves stood in
different states. sign(θ̇) alone is a fair coin, forced by the reflection σ : θ → π/2 − θ under
which the charge L = R²θ̇ is odd. The winding rides a different component of ∂_μθ — the spatial
gradient, set at the Kibble transition — and the product had no instrument: one half-solver evolves
the rotation with no winding, the other carries the winding with no time evolution. This is that
instrument, and its verdict.

Instrument: `scripts/genesis_joint_draw.py`.

## The instrument

A one-dimensional periodic ring of the complex genesis field ψ_j = x_j + i y_j, evolved on the
model's recorded potential

  V = m²R² + λR⁴ + 2 ε_A λ R⁴ cos 4θ,  ε_A = 2/9,

released at rest, with radiation-era Hubble friction H = 1/(2t) and a nearest-neighbour spatial
stiffness κ (the gradient term that lets the ring hold a winding). One trajectory carries **both**
objects at once:

- the winding **n = (1/2π) ∮ ∇θ·dl** — a spatial loop integral, the sum of the wrapped
  neighbour phase differences;
- the zero-mode rotation **θ̇**, read off the comoving charge Q = a³ Σ_j R_j² θ̇_j — the total
  R²θ̇ redshift-compensated, the same frozen dark charge the twist-sign roll tracks.

The tilt torque ∝ R⁴ acts at high R early in the roll and generates the rotation; once it shuts off
Q is conserved, so a late-window mean is the frozen generated rotation. The solver reduces to the
homogeneous zero-mode roll at N = 1, and carries the same winding object the multi-component
coherent fraction is built on.

## It reproduces both half-solvers where they overlap

**The zero-mode roll.** At N = 1 the ring is the homogeneous release. Over one Z4 period the
generated rotation's sign splits **12 positive / 12 negative**, and the σ-antisymmetry
Q(θ) = −Q(π/2 − θ) holds to a maximum residual/scale of **5.0×10⁻¹⁵** — the even split, reproduced
from the mechanism rather than asserted.

**The winding sector.** The winding counter returns exact integers for a clean n-ramp (n = −3…+3);
the coherent fraction |⟨e^{iθ}⟩| matches its definition to machine zero; a half-quantum vortex
(a π offset on half the sites) drops the coherence 1.000 → 0.000 — the coherence penalty, in its
own direction. The ring holds the winding net-conserved across the full trajectory (R dips to
≈ 0.01 near a core on the first radial in-swing but does not reconnect for N ≥ 12).

## The result — the joint (sign θ̇, sign n) distribution

Scanning θ_i over one Z4 period × winding n over a symmetric set, with small per-site phase noise
so the +n and −n draws are **not** exact mirrors (a genuine statistical test, not a rigged pairing),
the 2×2 joint is flat and the sign correlation sits at the noise floor:

| stiffness κ | (θ̇+, n+) | (θ̇+, n−) | (θ̇−, n+) | (θ̇−, n−) | corr | noise floor |
|---|---|---|---|---|---|---|
| 0.0 | 15 | 17 | 17 | 15 | −0.06 | ±0.13 |
| 0.5 | 17 | 14 | 15 | 18 | +0.09 | ±0.13 |

sign(θ̇) and sign(n) are drawn **independently**.

## The verdict — independent, and a symmetry says it must be

**sign(θ̇·n) is not a quantity the model signs; it is a coin it cannot call.** The reason is
spatial parity. Space carries no preferred orientation for the winding loop, so the dynamics is
invariant under the reflection **P** that reverses the ring, j → N−1−j. Under P the winding flips,
n → −n, while the total charge Q = Σ_j R_j² θ̇_j and the tilt torque Σ_j R_j⁴ sin 4θ_j are
site-sums — unchanged. So every trajectory's P-mirror has the **identical θ̇ history** and the
**opposite n**: the two signs cannot lock. The instrument confirms it to machine precision —
reversing the ring leaves Q identical (relative difference 0.0) and flips n exactly (residual
4×10⁻¹⁶).

This is the exact partner of half one's result. Half one's reflection σ : θ → π/2 − θ makes each
sign individually undetermined; spatial parity P : x → −x makes their **product** undetermined too.
The winding only modulates the roll's magnitude — an even-in-n suppression, since the zero-mode
torque projection Σ_j cos(8π n (j − (N−1)/2)/N) is even in n — but it never biases the direction.

**The null is measured, not assumed.** Injecting a parity-odd coupling the model does not have (a
toy θ̇·∇θ tangential drive) makes the correlation appear at once: corr jumps to **+0.51** for one
sign of the coupling and **−0.75** for the other, while the recorded potential holds it at −0.09.
The instrument can register a correlation; there is simply none to register. The corpus's only
parity-odd genesis coupling is the gravitational Chern-Simons θ R R̃ acting on θ̇ — the graviton
handedness of a different link — not a term coupling the spatial winding to the temporal rotation.

## What this decides

The helicity↔matter **cross-messenger test closes negatively.** The map's distinctive claim was
that one topological draw set both the magnetic helicity's handedness and the matter-vs-antimatter
direction — a correlation no other magnetogenesis framework predicts, where helicity (if any) is an
independent accident. On the recorded genesis dynamics that correlation is absent: the handedness
and the baryon draw are independent accidents here as well. A measured left-handed helicity cannot
be turned into a statement about the baryon asymmetry through link 5. The sharpest cross-messenger
test on the board does not live at this junction.

The reading the map's framing invited — "one owed computation away from a cross-messenger test" —
is the branch that does not hold. The roll gives a definite θ̇ sign per patch, the Kibble draw gives
an independent n sign, and their correspondence is a coin. That is a real answer, and it is as
valuable as the positive would have been.

## Scope — this is link 5 only

This closes link 5, sign(θ̇·n). It does not touch link 4's **sign(H_kin)**: the kinetic helicity is
a writhe+twist quantity of the trajectory's full three-dimensional flow, and a zero-mode-plus-winding
solver cannot return it at any resolution — writhe is a property of the centerline's embedding in
three dimensions, twist of its internal framing, and neither reduces to a loop integral or a zero
mode. Link 4 still needs a genuine three-dimensional genesis flow.

## What should change in the protected records (for the main thread to integrate)

- **The sign map's link-5 row** (`T14_igmf_helicity_owed.md`): from SPLIT/owed to **CLOSED,
  NEGATIVE** — sign(θ̇·n) is independent, forced by spatial parity, computed by the joint-draw
  instrument. The census's link-5 debt moves off the owed list; link 4's sign(H_kin) remains.
- **The forward helicity doc** (`PRTOE_igmf_helicity.md`): the claim that the matter draw and the
  helicity handedness are "the same topological draw" is **not carried by the recorded dynamics**.
  The prediction that the helicity sign correlates with the baryon asymmetry should be marked **not
  supported** — the model joins the generic case where the two are independent. The distinctiveness
  that rode this correlation is withdrawn; the magnitude-level helicity claim (sign(helicity_B) =
  sign(n)) is untouched, only its lock to the baryon draw.
- **The residual-debt census**: link 5 closes (negative); the remaining owed object at this thread
  is link 4's sign(H_kin), and its home is the three-dimensional flow instrument, not this one.
