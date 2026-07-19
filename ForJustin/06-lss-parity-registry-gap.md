# 06 — The LSS parity bet: a real position, an unmirrored registry entry

**ANSWERED 2026-07-19 — you called it: claim the bet, timestamped to when it was placed.**
Registered as **P-2026-055**, placement date 2026-07-11, mirrored 2026-07-19. The entry states its
own provenance in full, including that the mirroring happened after the DESI result was known, so
a reader can discount it themselves. The rest of this file is the reasoning that led there.

## What happened

`PRTOE_lss_parity.md` says the model "formally **bets the claim is systematic** (the second
registered anti-anomaly bet, after birefringence)."

It is not in `PRTOE_PREREGISTERED_PREDICTIONS.md`. It never was. The word "registered" in that
sentence points at nothing.

## Why it still counts

The position is genuinely dated. The file was committed **2026-07-11** (`b0b1dab1`) and the
"bets the claim is systematic" language was in place by **2026-07-12** (`4488b945`). Git is the
timestamp, and it predates the check below by a week. So this is a real recorded position, just
one that lives in the wrong drawer.

## What the referee said

Checked 2026-07-19:

- **arXiv:2604.06021** (2026-04-07), *Testing parity with composite-field spectra of BOSS and DESI
  luminous red galaxies* — **no evidence for parity violation in either survey**, with DESI's
  scatter ~4× smaller than BOSS DR12's.
- The **blind** BOSS CMASS 4PCF test returns **2.9σ**, against **7.1σ** unblinded.
- Sample variance is still on the table as the whole explanation (Phil. Trans. R. Soc. A 383,
  20240034, 2025).

The model's position is winning. Not conclusively — arXiv:2604.06021 uses composite-field spectra,
not the 4PCF, so it denies confirmation rather than refuting the original on its own terms.

## The decision I did not make for you

Whether to mirror this into the registry now. Arguments both ways:

**Mirror it.** The position is real, git-dated, and predates the result. Leaving it out of the
registry undercounts the model's record, and the registry is supposed to be the record.

**Don't.** I read the DESI paper *before* writing any registry entry. Anything I add today is
written with the answer in hand, and a registry that admits entries under those conditions is worth
less than one that doesn't. The bet's value comes from the registry being strict.

**My read:** mirror it, but with the provenance stated in the entry itself — recorded in
`lss_parity.md` 2026-07-11, mirrored late on 2026-07-19 with the arXiv:2604.06021 result already
known. That way the record is complete and the reader can discount it themselves. What I did *not*
want to do is quietly add it and let it read as a clean pre-registration.

Meanwhile the outcome is written up in `PRTOE_lss_parity.md` §3a, where the position actually
lives, with the same caveat.

## Also worth knowing

The corpus had two dead internal tags, `def-atom-night` and `def-quiet`, neither of which resolved
anywhere — same family as the `def357` orphan behind the portal-scale item in `01`. Both are gone:
the first now points at `PRTOE_arrow_of_time.md`, which actually carries the Landauer accounting it
was gesturing at; the second was a dateline on a corollary that already had its date.
