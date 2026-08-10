# C code vs theory audit — live core, evidence lanes, restart decision (2026-08-06)

## Question

Does the current C/CLASS implementation match the theory well enough that the live AWS
`cmp_prtoe_dyad_ev` PolyChord run is still valid?

## Sources checked

- `README.md`
- `cmp_prtoe_dyad_ev.yaml`
- `cmp_lcdm_ev.yaml`
- `docs/PRTOE_CODE_MANIFEST.md`
- `docs/PRTOE_honest_status.md`
- `source/input.c`
- `source/background.c`
- `source/thermodynamics.c`
- `include/background.h`

## Public-core theory lane

The current public expansion core is documented as:

- `use_dcdf`
- screened/derived `varying_me`
- `dcdf_dyad_link`

This is the harder lane: the electron-mass shift is derived from the amplitude stack and
the density gate is the model path.

## Live AWS evidence lane

The current AWS PolyChord run is **not** that hard lane. Its config is the documented softer
evidence lane:

- `use_dcdf: yes`
- `varconst_density_gate: yes`
- sampled `varying_me`
- sampled `log10_zon`

This lane asks whether the data prefers a varying-`m_e` cosmology at all, with Occam penalty,
before the harder fixed/derived-`m_e` case is taken as decisive.

## Code check

The source implements both lanes explicitly.

1. `source/input.c`
- parses `use_dcdf`
- parses direct `varying_me`
- parses `varconst_density_gate`
- parses `dcdf_dyad_link`
- when `dcdf_dyad_link=yes`, derives `varying_me = 1 + eps` from the amplitude stack and
  auto-selects the density-gate path unless explicitly overridden

2. `include/background.h`
- documents the density-gate path as the model path
- records `dyad_link`, gate parameters, and dCDF state on the background structure
- labels legacy `use_prtoe` fields as scalar-tensor dummies retained only so older
  perturbation code compiles

3. `source/background.c` and `source/thermodynamics.c`
- consume the background varying-constants path
- carry the density-gate handling
- do not invent a separate thermodynamics-side `m_e` mechanism behind the input layer

## Judgment

The C code matches the theory **lanes** that are actually in the repo:

- derived/screened public-core lane
- sampled-ε evidence lane

The mismatch I found was **in shelf wording**, not in implementation:

- some docs had drifted into speaking as if the live AWS nested run were the fixed/derived-ε
  zero-extra-parameter lane
- it is not; it is the documented sampled-ε evidence dyad

## Restart decision

**No restart required** on code-vs-theory grounds.

Reason:

- the live `cmp_prtoe_dyad_ev` run is consistent with its own documented sampled-ε purpose
- the C source supports that lane directly
- nothing in the audit showed the running config relying on a nonexistent or contradictory C path

## Desk action

The correct fix is documentary:

- keep sampled-ε and fixed/derived-ε lanes separate in living docs
- do not call the live AWS run “zero extra parameters”
- do not speak as if `dcdf_dyad_link` were active in `cmp_prtoe_dyad_ev.yaml`
