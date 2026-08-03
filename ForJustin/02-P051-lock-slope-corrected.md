# P-2026-051's lock slope was 2× too steep — corrected

**No decision needed, but you should know a registered prediction moved.**

The Koide deviation lock registered the line **δθ = (2√2/9)·δA = 0.3143·δA**, calling it "the
holonomy-equals-Q closure's differential." The closure — named in the entry's own kill (iii) —
is θ = (1 + A²/2)/9. Its derivative is A/9 = **√2/9 = 0.1571**. The registered slope is exactly
double it.

**Corrected in place.** The kill now points Belle II at the 0.1571 line.

**Nothing structural falls.** The data is still consistent with the line, so "the deviations lie
on the line" survives. The closure itself, the circulant algebra, and the Parseval identity
Q = 1/3 + (2/3)|f₁/f₀|² are untouched.

**The data row underneath the slope was also wrong, found 2026-07-20 (#102).** The −0.54σ quoted
here — and the −0.31σ it replaced — do not survive: δθ is **+7.409×10⁻⁶ rad**, not −7.0×10⁻⁶;
both deviations had been computed from rounded displays rather than from the masses; and the σ
belongs on the residual, because the two axes are functions of m_τ alone and anti-correlated at
exactly −1. **The current number is +0.89σ**, on the side a positive slope does not predict. The
lesson is the sharper one: this note re-derived the *line* and re-quoted the *data* beneath it
untouched, which is how a sign error survived the pass that was looking straight at it.

Found by the math-verification pass, which recomputes every closed-form claim from its own
inputs. It is now check #47 in `scripts/audit_math_pass.py`, so it cannot drift back.
