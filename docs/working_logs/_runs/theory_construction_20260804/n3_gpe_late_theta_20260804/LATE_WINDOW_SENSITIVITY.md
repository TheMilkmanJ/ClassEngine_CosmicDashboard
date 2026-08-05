# Late-window sensitivity (red F5 cure)

**S1 primary definition in script:** `late_Theta` ≡ last **10%** of Θ history (`late_tail10`).

On the **winning 0D row** (n0=80, Θ0=−8, κ=3, γ=0.02) the package SUMMARY_JSON also records:

| window | value | role |
|---|---:|---|
| late_tail10 (headline) | **+2.8701** | S1 primary as run |
| late_tail20 | **−0.1364** | opposite sign |
| settled_mean | **+0.1085** | last-20% mean |
| settled_std | **~1.25** | ring-down not settled |

Red re-ran stocked ODE (dt refinement): tail10 converges ~+2.71–2.87; tail20 stays **~−0.14**.  
**Headline late is real but window-choice-sensitive.** All values ≪ Θ_lock=11.71 — no verdict moves; honest reading is *worse* for S1.

**Stocked default (6,−2,1.5,0.15):** late depends on dt (5e−4 → ~0.06193; 1e−3 → ~0.06122). Not fabrication — stamp **dt=5e−4 default path in deeper scan used 1e−3 in places**; both ≪ lock.

**Rule going forward:** every headline late-⟨Θ⟩ carries tail10 **and** tail20 (or settled) on the same row.
