# BBN light-element abundances

*The model's helium matches the measured value; deuterium sits in a mild tension because the
varying-mₑ CMB fit prefers a higher baryon density than deuterium wants. Code:
`scripts/bbn_abundances.py`; figure `chains/bbn_abundances.png`.*

## The setup

At BBN the condensate is not yet formed, so m_e = 1 and the model's nucleosynthesis is standard: the
deuterium heal by varying-mₑ is excluded at 12σ, so the varying-mₑ shift acts only later, at
recombination, and the abundances follow the standard relations in ω_b. The dyad is L-neutral and
reaches the deuteron only at two loops, ~2×10⁴ times too weakly to touch it.

## The abundances

Helium is Y_p = 0.247, +0.6σ from the measured 0.2449 ± 0.0040, across the ω_b range. Deuterium is a
sharp baryometer, D/H ∝ ω_b⁻¹·⁶: at ω_b = 0.02238 it sits exactly on the measured
2.527 ± 0.030×10⁻⁵, and at ω_b = 0.0228 it falls to 2.452×10⁻⁵, −2.5σ.

## The tension

Those two ω_b values are the tension. The varying-mₑ realigns the CMB acoustic scale by raising ω_b to
~0.0228 (the CMB peak-fit value), while deuterium wants ω_b ~ 0.0224. The same baryon-density knob
that fits the CMB pushes deuterium off, so the joint fit — the CMB pulling ω_b up, the deuterium
constraint pulling it down — settles at a compromise carrying a mild deuterium tension. It is a
genuine cost of the varying-mₑ H0 mechanism, one ΛCDM does not pay because its ω_b lands on deuterium
exactly. Lithium is a separate sector: standard BBN over-predicts Li-7/H (~5×10⁻¹⁰ against the
observed ~1.6×10⁻¹⁰, the lithium problem), which the model's lithium row addresses apart.
