#!/usr/bin/env python3
"""f̄ RE-DERIVED for a MULTI-COMPONENT condensate (the post-basement-rebuild solver).

WHY: the winding average f̄ was computed assuming a SINGLE-component order parameter,
where circulation is quantized in whole 2π units. The basement rebuild (entries 110/122)
established the medium as a SIX-CHANNEL paired condensate — and multi-component
superfluids support FRACTIONAL vortices (³He-A's half-quantum vortices are the canonical
case: the phase winds by π, with the remainder carried by another component).

WHAT CHANGES: with N channels, the total phase winding W can distribute across channels.
The coherent-fraction observable f = |⟨e^{iθ}⟩| is then an average over the channel
phases, not a single phase. Two structural consequences:
  (1) FRACTIONAL WINDING: each channel can carry w_i = W/N + δ_i (integer or half-integer
      depending on the pairing symmetry), so the effective circulation per channel is
      SMALLER than the single-component case.
  (2) PHASE SPREAD: the channels' relative phases (the Leggett sector) fluctuate, and
      those fluctuations REDUCE the coherent fraction — |⟨e^{iθ}⟩| over a spread of
      phases is always ≤ the single-phase value.

TARGET BAN (pre-registered, non-negotiable): this computation is NOT aimed at 2/3, at
2/π, or at any other value. The corpus's firewall binds: nearby rationals are the
dynamics' to produce, not ours to pick. WHATEVER IT GIVES, WE BOOK.

RAMPS: all inputs banded; the roll-up, the freeze window, the pre-ring gap, and the
channel-phase spread are continuous; no menus.
"""
import numpy as np

rng = np.random.default_rng(31)
N_DRAWS = 40000

# ---- the single-component baseline (the old solver, for comparison) ----------
def fbar_single(t_form, tau, p, T, gap, f_lock):
    tg = np.linspace(0, 1, 60)
    G = 1 - np.exp(-tg * t_form / tau)
    m = np.mean(G ** p)
    return f_lock * (1 - (t_form / T) * (1 - m) - gap / T)

# ---- the multi-component correction ------------------------------------------
def coherent_fraction(channel_phases):
    """f = |<e^{i theta}>| over the channels — the observable the winding average tracks."""
    return np.abs(np.mean(np.exp(1j * channel_phases)))

print("=" * 78)
print("f̄ RE-DERIVED — MULTI-COMPONENT CONDENSATE (6 channels, fractional windings)")
print("=" * 78)
print("TARGET BAN IN FORCE: not aimed at 2/3, not aimed at 2/π. Whatever it gives, we book.\n")

N_CH = 6  # the pairing channels (entry 110)

rows = []
for i in range(N_DRAWS):
    # --- the ring dynamics (unchanged, ramped as before) ---
    t_form = rng.uniform(3, 20)
    tau    = t_form / rng.uniform(2, 4)
    p      = rng.uniform(0.5, 2.5)
    T      = rng.uniform(250, 350)
    gap    = rng.uniform(0, 2)
    f_lock = rng.normal(0.635, 0.026)
    base   = fbar_single(t_form, tau, p, T, gap, f_lock)

    # --- THE MULTI-COMPONENT PHYSICS (new) ---
    # (a) the channel phases spread around the mean by the Leggett-sector fluctuation.
    #     the spread is set by the interchannel coupling: weak coupling -> wide spread.
    #     RAMPED over the coupling strength (no menu).
    sigma_phase = rng.uniform(0.0, 1.2)          # rad; 0 = locked channels, 1.2 = loose
    phases = rng.normal(0.0, sigma_phase, N_CH)

    # (b) FRACTIONAL WINDING: a fraction of draws admit half-quantum vortices
    #     (the ³He-A structure). When they occur, half the channels carry a π offset.
    if rng.random() < rng.uniform(0.0, 0.5):     # the HQV occurrence rate, itself ramped
        n_half = rng.integers(1, N_CH // 2 + 1)
        idx = rng.choice(N_CH, size=n_half, replace=False)
        phases[idx] += np.pi

    coh = coherent_fraction(phases)
    rows.append(base * coh)

f = np.array(rows)
q = np.percentile(f, [16, 50, 84])
print(f"  f̄ (multi-component, ramped) = {q[1]:.4f}   [{q[0]:.4f}, {q[2]:.4f}]  (16/84)")
print(f"  f̄ (single-component, today) = 0.6230   [0.5971, 0.6491]   <- the old value")
print()
print("  the reference values (for reading, NOT for aiming):")
for name, v in [("2/π (the old closed-form claim)", 2/np.pi), ("2/3 (Koide's constant)", 2/3),
                ("the ε-fit-implied f̄", 0.6253)]:
    inside = q[0] <= v <= q[2]
    print(f"    {name:34s} = {v:.4f}   {'INSIDE the new band' if inside else 'OUTSIDE the new band'}")

# --- what the fractional-vortex sector does on its own -------------------------
print()
print("  THE MECHANISM'S DIRECTION (isolating the multi-component correction):")
for sp, label in [(0.0, 'channels perfectly locked'), (0.4, 'moderate spread'), (0.8, 'loose'), (1.2, 'very loose')]:
    ph = rng.normal(0.0, sp, (5000, N_CH))
    c = np.abs(np.mean(np.exp(1j*ph), axis=1)).mean()
    print(f"    phase spread {sp:.1f} rad ({label:24s}): coherence factor = {c:.4f}")
print("""
  -> THE MULTI-COMPONENT CORRECTION IS A COHERENCE PENALTY. Channel-phase spread and
     half-quantum vortices both REDUCE |⟨e^{iθ}⟩|. **The correction can only push f̄
     DOWN, never up** — it is a dephasing factor bounded by 1.
""")
print("=" * 78)
print("  READ THE RESULT, THEN CONCLUDE (the standing rule).")
print("=" * 78)
