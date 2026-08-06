# PolyChord on cloud hardware — build notes and the cost correction (2026-08-06)

Purpose: record what it takes to build and run PolyChord + modified CLASS + the full
likelihood stack on a fresh cloud instance, and correct a cost figure that had propagated
across six forward-facing files.

## 1. The cost correction — this is the substantive part

`P-2026-044` priced nested sampling as unaffordable from **66 s per likelihood evaluation**,
giving 163 days to a first checkpoint and 736 days for the reference run. **That figure was
measured on the owner's laptop, under load, with three MCMC chains already running.**

Measured on AWS c7i (Sapphire Rapids), same yaml, same eight-likelihood stack, `plik_lite`
self-check passed at −292.286:

> **6.70 s per likelihood evaluation** (mean of five calls after warm-up; 9.22, 6.12, 6.28,
> 5.92, 5.98 s), 14 sampled parameters.

**9.9× faster.** Against the entry's own 1 809 iterations × 534 slice steps ≈ 9.7×10⁵ calls:

| | core-hours | 96 vCPU | spot | on-demand |
|---|---:|---:|---:|---:|
| dyad alone | ~1 800 | ~19 h | ~$26 | ~$80 |
| + ΛCDM twin | ~3 600 | ~37 h | ~$52 | ~$160 |

The nested referee is affordable. Six forward-facing files were updated to qualify the 66 s
figure as laptop-specific; the failures-ledger entry recording the 2026-07-20 retirement was
**annotated, not rewritten** — that decision was correct for the machine it was taken on.

## 2. The build, in the order the obstacles appear

Ubuntu 26.04 (Python 3.14, GCC 15.2, kernel 7.x). Each of these cost a cycle.

**(a) cobaya's PolyChord installer fails — and it is not PolyChord's fault.**
`cobaya-install polychord` dies with `Error: Unable to get the user home directory` /
`opal_init failed` / `mca_base_var_init failed`, killing `mpifort` on the first source file.
The same `mpifort` compiles fine from an interactive shell (verified with a two-line program).
**cobaya's build subprocess strips the environment OpenMPI needs.** Setting `HOME` on the
outer process does not fix it.

*Fix:* build PolyChord by hand, bypassing cobaya's installer entirely.

**(b) `make clean` does not clean.** After a prior build, plain `make` reports
`Nothing to be done for 'all'`. Remove objects explicitly: `rm -f src/polychord/*.o lib/libchord.so`.

**(c) The executable-stack trap — the expensive one.**
The link emits `warning: interfaces.o: requires executable stack`. Ignore it and the library
imports but fails at load with:

> `ImportError: libchord.so: cannot enable executable stack as shared object requires: Invalid argument`

Relinking with `-Wl,-z,noexecstack` makes it **load**, and it then **segfaults during sampling**:

> `Signal: Segmentation fault (11)`, `Signal code: Invalid permissions (2)`,
> `Failing at address: 0x7ffc…` — a stack address.

**This is the failure mode to recognise.** gfortran puts *trampolines* on the stack when
internal procedures are passed as arguments, which is exactly how PolyChord hands the
likelihood callback to the sampler. Stripping the flag removes the loader's objection without
removing the requirement, so it runs until the first callback and dies. The library importing
successfully is not evidence that it works.

*Fix (GCC ≥ 14):* compile the Fortran with **`-ftrampoline-impl=heap`**.

```
make FFLAGS="-ffree-line-length-none -cpp -fPIC -fno-stack-arrays \
     -fallow-argument-mismatch -Ofast -ftrampoline-impl=heap -DMPI"
```

**The executable-stack warning disappears from the link line.** That absence is the check —
no relink workaround is needed afterwards, because nothing requests an executable stack.

**(d) CLASS cannot find its data.** `thermodynamics_helium_from_bbn` fails on
`external/bbn/sBBN_2025.dat`. The install does not copy `external/` next to the compiled
module: `cp -r <repo>/external <venv>/lib/python3.X/site-packages/`.
Five BBN tables ship in that directory and **which one loads changes Y_p** — relevant because
the helium row is half of the BBN column `P-2026-027` books as net adverse.

**(e) Absolute paths travel in the yaml.** `packages_path` and the candl `data_set_file`
entries carry the author's home directory. Three sites needed repointing on the AWS copy.

## 3. Physics verification — do this before trusting any number

Compare a reference lensed TT spectrum against the local build. Local (Jul-23 build,
`cpython-313`) vs AWS (`cpython-314`, GCC 15.2):

| | local | AWS | rel diff |
|---|---|---|---:|
| `cl[100]` | 2.26157191959e-13 | 2.26156980909e-13 | 9.3e-07 |
| `cl[220]` | 9.96797356011e-14 | 9.96797440241e-14 | 8.5e-08 |
| `cl[1000]` | 8.96737085477e-16 | 8.96733777050e-16 | 3.7e-06 |

**Worst 3.7e-06 — same physics, different arithmetic.** Judged against cosmic variance
(4–12% at these multipoles) the shift is ~3–10×10⁻⁵ σ per mode, four orders below the noise
floor of any likelihood in the stack.

**Two instrument errors of mine, recorded so they are not repeated:**

1. A `sha256` of `np.round(cl, 14)` is **worthless** for values of order 1e-13 — rounding to 14
   *decimal places* leaves one or two significant figures, so any build matches. It matched, and
   it meant nothing.
2. The stated pass threshold of "1e-10 relative or STOP" is **unmeetable**. CLASS integrates
   with adaptive tolerances around 1e-5–1e-8 and is not reproducible to 1e-10 across compilers
   or CPUs. Judge against the measurement error, not against bit-reproducibility.

## 4. Run configuration

- `OMP_NUM_THREADS=1` — CLASS is OpenMP-capable; without this each MPI rank spawns threads and
  they contend. The most common way to make an MPI cosmology run slower than serial.
- **One run per output directory.** Two `cobaya-run` processes on the same `output:` path
  corrupt each other's resume files.
- c7i.8xlarge is 32 vCPU / 16 physical cores. Rank count is worth **measuring** on this
  workload rather than assuming from hyperthreading rules of thumb.
- Account vCPU quota is per-family and blocks `StartInstances` at resize time
  (`VcpuLimitExceeded`) — 96-vCPU types need a quota increase filed first.
- Instance type can be changed in place: stop → `modify-instance-attribute` → start. EBS
  contents survive; the public IP does not.

## 5. Status at close

Dyad leg launched: `nlive 250`, `nDims 14`, `nDerived 20`, 16 ranks, resume file written.
Settings are as registered in `P-2026-044` — unchanged, since the entry is a pre-commitment
and altering the sampler now would defeat what the registry is for.

**ΔlnZ still requires the ΛCDM twin on this same build.** The dyad number alone lands in none
of the entry's bands.
