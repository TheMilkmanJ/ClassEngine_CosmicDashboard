# Working logs — the reasoning, including its dead ends

Session logs and lab-log documents: derivations recorded chronologically, wrong turns left in.

**How these are audited.** Not for whether their numbers match the standing books — a log
legitimately holds interim and relative results. They are audited for **leaks**: a result that
is sound in its own frame being exported as an absolute one.

That is not hypothetical. The genesis-residual BBN mis-price happened exactly this way: a splice
table here was internally correct as a *relative* comparison and carried an absolute headline,
and the next computation that needed a starting point read the headline. Files whose results are
frame-dependent now say so at the point of use.

## `_OWNER_QUEUE.md`

Decisions the desk cannot make for itself, kept in one place so they can be ruled in one pass
rather than found by reading dated ledger entries. Each item names what is blocked, what the
arithmetic says, and what a ruling would unblock; the workings stay in `_AUDIT_LEDGER.md` under
the dated entry it cites. Items leave the queue when **ruled**, not when acted on — a ruling with
its work still outstanding stays visible on the task board instead.
