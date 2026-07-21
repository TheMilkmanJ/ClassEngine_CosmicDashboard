# The SNe Ia Hubble diagram

*The model's distance modulus μ(z) tracks the 1580 Pantheon+ Hubble-flow supernovae in shape, with a
single absolute offset set by the M_B / H0 calibration. Code: `scripts/sn_hubble.py`; figure
`chains/sn_hubble.png`.*

## The data

Pantheon+SH0ES gives 1580 non-calibrator supernovae above z = 0.01, each with a SH0ES-calibrated
distance modulus. The supernovae fix the shape of μ(z) — the deceleration-to-acceleration history —
while the absolute rung of the ladder is the supernova absolute magnitude M_B, set by the Cepheid
anchor.

## The model

The model's μ(z) runs through the Hubble diagram with a shape χ² of 689 over 1580 supernovae on the
diagonal errors, so the acceleration history is reproduced. The one free offset is −0.12 mag, which is
the M_B / H0 calibration: the model's H0 = 69.6 sits below the SH0ES anchor's 73, and the supernovae
alone do not set the absolute rung, so the offset absorbs that difference — the same H0 gap that the
distance-ladder comparison shows, seen here as the calibration constant.
