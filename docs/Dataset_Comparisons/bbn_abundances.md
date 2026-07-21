# BBN light-element abundances

*At BBN the condensate is not yet formed, so m_e = 1 and the model's BBN is standard BBN; the figure
shows it reproduces the light-element abundances. Code: `scripts/bbn_abundances.py`; figure
`chains/bbn_abundances.png`.*

## The setup

The deuterium heal by varying-mₑ is excluded at 12σ, so m_e = 1 at BBN is data-required, not a knob —
the varying-mₑ shift applies only later, at recombination. The abundance relations are the ones the
model's config carries (the BBN prior in `cmp_prtoe_fixed.yaml`).

## The abundances

At Planck's ω_b = 0.02237 the model's helium is Y_p = 0.2471, +0.6σ from the measured 0.2449 ± 0.0040,
and deuterium D/H = 2.528×10⁻⁵ sits exactly on the measured 2.527 ± 0.030×10⁻⁵. At the model's
slightly higher ω_b = 0.02276 the helium is unchanged at +0.6σ and D/H falls to 2.460×10⁻⁵, −2.2σ
from the measured value — the deuterium tension the model carries from preferring a higher baryon
density than Planck. Lithium is a separate sector: standard BBN over-predicts Li-7/H (~5×10⁻¹⁰ against
the observed ~1.6×10⁻¹⁰, the lithium problem), and the model's lithium row addresses it apart.
