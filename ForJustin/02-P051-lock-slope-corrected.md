# P-2026-051's lock slope was 2× too steep — corrected

**No decision needed, but you should know a registered prediction moved.**

The Koide deviation lock registered the line **δθ = (2√2/9)·δA = 0.3143·δA**, calling it "the
holonomy-equals-Q closure's differential." The closure — named in the entry's own kill (iii) —
is θ = (1 + A²/2)/9. Its derivative is A/9 = **√2/9 = 0.1571**. The registered slope is exactly
double it.

**Corrected in place.** The kill now points Belle II at the 0.1571 line.

**Nothing structural falls.** On the corrected slope the current data sits −0.54σ from the line
instead of −0.31σ — still consistent, so "the deviations lie on the line" survives. The closure
itself, the circulant algebra, and the Parseval identity Q = 1/3 + (2/3)|f₁/f₀|² are untouched.

Found by the math-verification pass, which recomputes every closed-form claim from its own
inputs. It is now check #47 in `scripts/audit_math_pass.py`, so it cannot drift back.
