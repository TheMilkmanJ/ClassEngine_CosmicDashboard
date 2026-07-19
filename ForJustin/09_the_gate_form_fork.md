# The dyad gate: two forms in the corpus, and they predict different things

**What I found.** `PRTOE_interaction_map.md` described the gate as a Gaussian,
exp(−C²/C_ref²). `PRTOE_me_trigger.md` derives that the exponent must exceed 2.43. A Gaussian
is n = 2. I reproduced the derivation independently: an 8.2-decade suppression has to ride a
1.35-decade curvature window (recombination to a dwarf core is only ~22× in Weyl curvature),
and requiring the gate still 99% open at recombination gives **n ≥ 2.44**. A Gaussian that
suppresses hard enough at the dwarf core has already eaten 3.8% of the early-universe ε.

I corrected the interaction map, the readers' guide, and the great chain to the near-step form.
**The part I did not decide is which of two readings is standing**, because they are not the
same physics and they make different predictions.

| | the sharp-but-smooth gate | the topological gate |
|---|---|---|
| form | exp(−(C/C_ref)ⁿ), n > 2.43 | Θ, the shell-crossing bit |
| reference scale | C_ref is a real parameter | **none** — the transition is an event, not a value |
| inside a galaxy | exponentially small, never exactly zero | **exactly zero** |
| in a void | small but present | **fully on** |

**Why it matters and is not bookkeeping.**

1. **The interaction map's signature law was "no screen in this model reaches zero."** That
   holds for the smooth form and fails for the topological one, where the gate shuts exactly
   inside shell-crossed regions. I rewrote the law to survive either reading — the two
   unscreenable channels carry it — but the file's own headline claim depends on the answer.
2. **P-2026-007 changes character.** The registry calls it "the void/IGM m_e-**STEP**." The
   interaction map called it "the residual whisper." Under the topological reading the registry
   is right and the map was understating: voids are precisely the un-shell-crossed regions, so
   the gate is **fully on** there — a step, not a tail. That is a materially stronger prediction
   than the corpus was advertising.
3. **The two files disagree about whether C_ref exists.** `me_trigger` §7: "There is no free
   reference scale C_ref to place, because the transition is set by a topological event." But
   `PRTOE_THE_AMPLITUDE.md` quotes **C_ref ≈ 2** as a live corner value for the supernova
   host-mass-step claim. One of those is wrong, and the amplitude file's SN corner rides on it.

**What I did not do.** I did not pick a reading, and I did not touch the amplitude file's SN
corner. Both need you.

**The related grading question.** The atlas's graveyard carries the shell-crossing bit (as
candidate R1) graded **"CONSISTENCY-CONSTRUCTION, not derivation"** — null in every accessible
channel by construction. `me_trigger` treats the same object as the *forced* implementation.
Those are different gradings of one thing, and if the topological reading is standing, the
graveyard entry's grade is the more honest of the two and should probably govern.
