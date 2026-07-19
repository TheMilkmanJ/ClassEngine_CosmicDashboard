# 07 — z_on: not a labelling problem. Two derived values that disagree by 14%.

**Tested 2026-07-19 against the code, the configs, and the derivation. The answer is worse than
"one is stale," and it touches the running evidence job.**

## What I found

Three numbers, not two.

| route | log₁₀ z_on | z_on | where it lives |
|---|---|---|---|
| **the H = m identity** | **7.605** | 4.03×10⁷ | `include/background.h`, marked **"DERIVED IDENTITY"** |
| the 3α corollary mark | 7.547 | 3.52×10⁷ | cited in the config as the mark to hit |
| **what the running job uses** | **7.5517** | 3.5619×10⁷ | `cmp_prtoe_fixed.yaml` |

I recomputed the identity from the code's own formula, T_on = √(m·M_red/0.61) with
m = 2.24×10⁻²⁰ eV: **9.457 keV → z = 4.026×10⁷**. The code comment says 9.41 keV → 4×10⁷, so the
identity reproduces.

**The identity and the 3α mark differ by 0.058 dex — 14% in z.** Both are described as derived. The
running job sits 0.005 dex from the 3α mark and 0.053 dex from the identity: **twelve times closer
to the mark than to the identity.**

## Why this is not just bookkeeping

Since z_on ∝ √m, a 0.058 dex gap in z is a 0.116 dex gap in m — the two "derived" values correspond
to dyad masses **24% apart** (2.24×10⁻²⁰ vs ≈1.71×10⁻²⁰ eV). And the corollary is supposed to be a
*translation* of the same H = m clock, not an independent route. A translation that lands 14% from
its source has an error in it somewhere, or the two are quietly measuring different epochs.

`PRTOE_quartet_clock.md` §4b already says the grading marks are **superseded** — the two-clock
correction (the zero mode's H = m and the winding mode's k/a = m coexisting) retires them, and "the
ramps-first re-derivation is owed before any center is graded." So the model knows the marks are
retired. What has not happened is the re-derivation that would say which value is right.

## The part that needs your decision

The running evidence job — the zero-parameter test, the headline — is frozen at 3.5619×10⁷, and its
own config says, verbatim:

> `# ZON-FREEZE (operator order 2026-07-12): this value is ILLEGAL until the zon chain converges`
> `dcdf_z_rad_onset: 3.5619e7   # BOBYQA frozen-stack profile ... FAST-FUDGE per operator order;`
> `# the 3-alpha mark 7.547 hit to 0.005 dex; chi2 cost +7.4 vs the free champion`

Three things follow, none of them mine to settle:

1. **The value in the headline run is marked illegal and a fudge by its own config**, pending a
   chain (`cmp_prtoe_zon`) that is at R−1 = 40.4 — nowhere near the 0.05 bar.
2. **The celebrated "0.005 dex hit"** is agreement with a mark that has since been retired, while
   sitting 0.058 dex from the identity the code calls derived. It reads as a success and is at best
   a success against a superseded target.
3. **The Fairbank letter says the transition epoch is "stated in advance — derived or profiled."**
   That is literally true, and "profiled" is carrying a value the config calls a fudge. If a referee
   opens the yaml, the word they find is ILLEGAL. Better you know that than have it pointed out.

## What I did not do

I did not change the running job, the config, or the letter's wording. Nothing here says the
evidence run is invalid — a profiled-then-frozen parameter is a legitimate construction and it is
disclosed. But which of the two derived values is right is a physics judgement that needs the
derivation chain re-walked, and picking one silently would bury the disagreement rather than resolve
it.

**The cheap version, if you want one before the re-derivation:** the identity is coded, documented,
and used by five other configs — `conv`, `conv_desi`, `dyad`, `lepton` and `nulink` all set 4.0e7.
Only the `_fixed` family uses 3.5619e7. That is a provenance argument rather than a physics one, but
it is the direction I would lean if forced.
