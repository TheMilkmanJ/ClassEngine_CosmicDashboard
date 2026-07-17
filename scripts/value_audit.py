#!/usr/bin/env python3
"""
VALUE AUDIT -- recompute every quoted number from the standing inputs.

WHY THIS EXISTS (2026-07-17): name-greps cannot find stale values. A retired number looks
exactly like a live one -- "+3.7σ" does not announce that it came from the step splice, and
"2.470340" does not announce that its baseline was withdrawn. Every leak found on 2026-07-17
(process errors 38/40, the step-era EMPRESS pull, the v5-era scar in four docs) was invisible
to a name search and obvious to arithmetic.

USAGE:  python3 scripts/value_audit.py            # audit the live shelf
        python3 scripts/value_audit.py --all      # include the archive (expect noise)
        python3 scripts/value_audit.py --derive   # print the derivation chain only

RULE: a value is legal in a live doc only if it is (a) recomputable from the standing inputs,
or (b) a cited external measurement. Anything matching a RETIRED value, on a line that names
its quantity, is a leak.
"""
import re, glob, os, sys, math

# ============================== THE STANDING INPUTS ==============================
_SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')  # superscript -> ASCII, for float()
alpha   = 1/137.035999206      # CODATA fine structure
m_e     = 510998.95            # eV
d_space = 3                    # THE SPATIAL DIMENSION (JP's ruling: the 3 in alpha_c = 3*alpha)

# ============================== THE DERIVATION CHAIN =============================
def chain():
    c_census = 9/10                       # (N-1)/N over the charged-fermion roster + vacuum seat
    f_bar    = 2/math.pi                  # the winding time-average <|cos|>
    alpha_c  = d_space * alpha            # 3 = the spatial dimension
    eps      = c_census * f_bar * alpha_c # = 27 alpha / 5 pi
    eps_closed = 27*alpha/(5*math.pi)
    T_c      = 179e3                      # eV  (the confining chiral value)
    M2       = alpha**2 * T_c             # eV
    rho_L_4  = 0.5 * alpha_c**2 * M2      # eV  -> the flagship
    tau      = T_c / m_e
    return dict(c=c_census, f_bar=f_bar, alpha_c=alpha_c, eps_pct=eps*100,
                eps_closed_pct=eps_closed*100, T_c_keV=T_c/1e3, M2_eV=M2,
                rho_L_meV=rho_L_4*1e3, tau=tau,
                E_1s=rho_L_4*1e3, E_2p=rho_L_4*1e3/4, E_4f=rho_L_4*1e3/16)

# ============================== CANONICAL / RETIRED ==============================
# Each check binds a number to its ROLE via a capture group. Matching by VALUE alone is what
# made the first cut of this tool useless (it flagged the "2" in "2 dof" as the retired -2.0s
# D/H scar, and every "1" in the corpus as the retired c=1). A number is only a leak if it is
# quoted AS the quantity.
CHECKS = [
 dict(q="Y_p value", rx=r"Y_?p[^.\n]{0,40}?=\s*([0-9]\.[0-9]{3,6})",
      ok=[0.248995,0.24900,0.2490],
      bad={0.2495:"the LT-STEP interval (P-036 predecessor, retired on the ramp)",
           0.2505:"the LT-STEP interval (P-036 predecessor, retired on the ramp)"}),
 # EXPONENT CHECK -- REWRITTEN 2026-07-17 (the first version was DEAD CODE: its capture group
 # grabbed a SIGN STRING, so "2.387x10^5" yielded no groups and the rule could not fire, while
 # "2.387x10^-5" threw on float('⁻') and was swallowed by the except. ok=[]/bad={} meant nothing
 # to match even if reached, and exponent_sign_check was never read. The two real sign-drops were
 # fixed BY HAND; the rule meant to prevent recurrence was inert. THE AUDITOR'S FIFTH ERROR.
 # This version captures the EXPONENT DIGIT and flags any D/H power that is not 10^-5.
 dict(q="D/H exponent", rx=r"D/H[^.\n]{0,44}?[0-9]\.[0-9]{3,6}\s*[x×]\s*10(?!⁻)(?!\^?-)([⁰¹²³⁴⁵⁶⁷⁸⁹0-9])",
      ok=[], bad={5.0:"D/H = 2.387x10^+5 -- THE EXPONENT SIGN IS DROPPED. D/H is ~1e-5; as written this states 238,700.",
                  4.0:"D/H exponent is not -5", 6.0:"D/H exponent is not -5"}),
 dict(q="D/H value", rx=r"D/H[^.\n]{0,40}?([0-9]\.[0-9]{3,6})",
      ok=[2.387],
      bad={2.470340:"PRyM-DEFAULT-omega_b absolute -- WITHDRAWN (process error 38); RELATIVE effects only",
           2.47034 :"PRyM-DEFAULT-omega_b absolute -- WITHDRAWN (process error 38); RELATIVE effects only",
           2.4305  :"the eta-flow applied to the DEFAULT baseline -- WITHDRAWN (process error 38)",
           2.468   :"the v5-era champion's D/H -- superseded by the ramp (standing 2.387)"}),
 dict(q="EMPRESS pull", rx=r"([0-9]\.?[0-9]*)\s*(?:σ|sigma)\s*(?:vs\s*)?EMPRESS|EMPRESS[^.\n]{0,30}?([0-9]\.?[0-9]*)\s*(?:σ|sigma)",
      ok=[3.53,3.5],
      bad={3.7:"the STEP-era EMPRESS pull (from Y_p=0.2495) -- the ramped 0.24900 gives +3.53",
           3.68:"the STEP-era EMPRESS pull (from Y_p=0.2495) -- the ramped 0.24900 gives +3.53",
           4.0:"the STEP-era EMPRESS kill (P-036 predecessor) -- amended to +3.5"}),
 dict(q="Aver pull", rx=r"([0-9]\.?[0-9]*)\s*(?:σ|sigma)[^.\n]{0,24}?Aver|Aver[^.\n]{0,30}?([0-9]\.?[0-9]*)\s*(?:σ|sigma)",
      ok=[1.09,1.12],
      bad={1.24:"the STEP-era Aver pull (from Y_p=0.2495)",
           1.3 :"the pre-ramp Aver pull -- the ramp gives +1.09"}),
 dict(q="D/H pull vs Cooke", rx=r"(?:D/H|deuterium|Cooke|scar)[^.\n]{0,70}?([0-9]\.[0-9])\s*(?:σ|sigma)",
      ok=[2.94,2.9,4.67,4.7,2.18,1.42,1.85],   # 1.85 = LCDM's OWN tension under PRIMAT (legal)
      bad={1.89:"the WITHDRAWN-baseline pull (2.470340 vs Cooke) -- process error 38",
           1.9 :"the WITHDRAWN-baseline pull, rounded -- process error 38",
           1.2 :"the v5-era scar (2.468, full budget) -- the standing ramp is -2.9",
           2.0 :"the v5-era scar (2.468, obs-only) -- the standing ramp is -2.9",
           3.22:"the withdrawn eta-flow-on-default pull -- process error 38"}),
 # "c ~ 1" means ORDER UNITY and is TRUE of c = 9/10 -- only the exact claim "c = 1" is dead.
 dict(q="c (census)", rx=r"\bc\s*=\s*([01]\.?[0-9]*)\b",
      ok=[0.9,0.90],
      bad={1.0:"the RETIRED c=1 conformal-origin candidate (UV #17) -- c=9/10 is derived by the census"}),
 dict(q="f_amp / f-bar", rx=r"(?:f̄|f_bar|f_amp)\s*(?:=|≈|~)\s*([0-9]\.[0-9]+)",
      ok=[0.6366,0.63662,0.636620,0.635,0.625],   # 0.635 sim / 0.625 fit are legal CHECKS on f-bar
      bad={0.6 :"the RETIRED f_amp decomposition value (eps = c*f_amp*Psi0/M_red)",
           0.69:"the RETIRED f_amp scan 'independent check'"}),

 # ---- added 2026-07-17 (overnight audit): the conditionality checks ----
 # The evidence number is DIRTY until the fits are re-run: the chains that made it fed CLASS a
 # LCDM helium fraction (the YHe lambda declared varying_me and never applied it). Any live file
 # quoting it BARE -- without the conditionality -- is a species-2 defect.
 dict(q="DlnZ quoted bare", rx=r"(?:Δ\s*ln\s*Z|DlnZ|ΔlnZ)\s*(?:=|≈|~)\s*\+?(2\.6[0-9]*)",
      ok=[],   # nothing is OK bare -- the CONTEXT check below decides
      bad={2.6:"the evidence number is conditional on the YHe defect (chains scored with a LCDM helium fraction); it must carry the asterisk until the fits are re-run",
           2.635:"the evidence number is conditional on the YHe defect; must carry the asterisk until re-run"}),
 dict(q="H_0 standing", rx=r"H[_₀0]\s*(?:=|≈)\s*([0-9]{2}\.[0-9])",
      ok=[69.9, 68.2],   # 69.9 = the standing claim; 68.2 = the LCDM foil, legal
      bad={69.7:"the v5-era refit value -- the standing claim is 69.9",
           69.82:"a single dyad run's value -- the standing claim is 69.9"}),
 dict(q="rho_Lambda^1/4", rx=r"(?:ρ_Λ|rho_L|ρ_∞)[^.\n]{0,30}?([0-9]\.[0-9]{2,3})\s*meV",
      ok=[2.284, 2.2842, 2.25],   # 2.284 derived / 2.25 observed
      bad={1.98:"a retired door value (M_2-tuned)", 2.695:"a retired door value (Landau-capped)",
           1.71:"a retired door value (KP-unpinned)",
           # I had 2.251 WHITELISTED. FAILURES_LEDGER:346 retires it by name: the "M_2 selected ->
           # 2.251, 4 parts in 10^4" framing -- "that precision was circular". The auditor could
           # not see it BY CONSTRUCTION. Found by red team auditing the auditor, 2026-07-17.
           2.251:"the RETIRED circular precision (M_2 back-solved from the answer; 'that precision was circular' -- FAILURES_LEDGER). Standing: 2.284 meV, +1.5%"}),
 dict(q="Sigma m_nu", rx=r"(?:Σm_ν|Sigma m_nu|Σ)\s*(?:=|≈)\s*([0-9]{2}\.?[0-9]*)\s*meV",
      ok=[61.4, 61], bad={}),
 # tau RULE (added 2026-07-17): tau = T_c/m_e = 0.3503 DERIVED. 0.345 is the OBSERVED rho_L
 # inverted (2.25/((9/2)alpha^4 m_e) = 0.34506) -- and quoting it as the model's tau converts the
 # flagship's claim into a 0.0% match. No rule existed; three passes missed CC:86 because of it.
 dict(q="tau = T_c/m_e", rx=r"(?:τ|tau)\s*(?:=|≈)\s*(0\.3[0-9]{2,4})",
      ok=[0.3503, 0.35029],
      bad={0.345:"the OBSERVED rho_Lambda inverted (2.25/6.5207 = 0.34506), not the model's tau. Derived tau = 179/511 = 0.3503. Quoting 0.345 as the model's value deletes the flagship's claim.",
           0.34506:"the observed rho_Lambda inverted -- not a derivation"}),
 dict(q="T_c keying", rx=r"T_?c\s*(?:=|≈)\s*([0-9]{2,3})\s*(?:keV)",
      ok=[179],
      bad={193:"the perturbative mu=T CROSS-CHECK -- legal only AS a cross-check, never as the keying value"}),
]
# the audit's OWN meta-files name retired values by design -- excluding them is not a blind spot,
# it is the same rule as the graveyard's.
ARCHIVE = ("_MORNING_REPORT","_AUDIT_LEDGER","_REDTEAM_BRIEF",
           "FAILURES","honest_status","v5_dCDF","v4_dCDF","session_2026","math_story","granule",
           "room1","gate0_qft","kill_and_patch","STATE_OF_MODEL","intellectual_history","SKELETON",
           "amplitude_derivation","Second_Order","references","me_trigger","me_mechanism",
           "kappa_v_derivation","v5_five_verdict","v5_SIDM","UV_completion")
# NOTE 2026-07-17: "weakest_joints" was REMOVED from this list. It is a LIVE doc (it carries a
# NEW STANDING RISK section) and was being scanned as a graveyard -- which is why its "width owed"
# survived a fix that landed in the two files beside it.

# A retirement notice MUST be allowed to name the value it retires, or the graveyard becomes
# unwritable. And "c" is overloaded: the census coefficient vs the SPEED OF LIGHT.
# TRUE retirement words -- these legitimately exempt ANY rule (a graveyard names what it buries).
RETIREMENT_CTX = re.compile(r"retir|supersed|dead|excludes|former|was booked|archive|Standing:|"
                            r"relic|predecessor|no longer|does not exist|withdraw|amended|"
                            r"historical|era.s frozen|frozen record|that era|refit tables|"
                            r"do not cite|provenance only", re.I)
# H0-ONLY context: a run record / TRGB anchor is not a stale H0 claim. THIS MUST NOT EXEMPT OTHER
# RULES -- folding it into RETIREMENT_CTX let a TRGB table-row exempt a real D/H exponent defect two
# lines away (found by the pass-4 planted test, 2026-07-17). Applied only to the H_0 rule.
H0_RUNRECORD_CTX = re.compile(r"raw χ²|raw chi2|best point|ever recorded|joint optimum|"
                              r"TRGB|joint best-fit|joint reading|ladder value|"
                              r"km/s/Mpc\*\*? \(|recorded on", re.I)
# A file that STATES the evidence number's conditionality is compliant, not defective.
CONDITIONALITY_CTX = re.compile(r"asterisk|LCDM helium|ΛCDM helium|YHe|conditional|defect|not a standing|"
                                r"re-?run|CODE_MANIFEST|SHOES-conditional|SH0ES-conditional|Laplace-marginal|"
                                r"marginal|gated|pending", re.I)
LIGHTSPEED_CTX = re.compile(r"acoustic|horizon|dispersion|c_s|speed of light|perturbations hit|"
                            r"dumb hole|k\*=M|trapped inside", re.I)

def delatex(line):
    """Strip LaTeX so the value rules can see the numbers inside math.

    THE BLIND SPOT, found 2026-07-17 by red team auditing this auditor: the T_c rule was CORRECT
    and still missed `T_c \\approx 193\\ \\text{keV}` in THREE_EQUATIONS eq.2 -- the
    physicist-facing front door -- because \\approx and \\text{} evade a plain-text regex.
    EVERY LATEX-BEARING LINE IN THE CORPUS WAS UNAUDITED. A rule that cannot read the file is
    not a rule."""
    t = line
    t = re.sub(r"\\t?frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)   # \frac{a}{b} -> a/b
    t = re.sub(r"\\text\{([^{}]*)\}", r"\1", t)                     # \text{keV} -> keV
    t = t.replace(r"\approx", "≈").replace(r"\simeq", "≈").replace(r"\times", "x")
    # THE COMPOSITION BUG (found 2026-07-17 by red team, re-run): deleting every \macro also
    # deleted the SYMBOLS the rules anchor on -- \rho_\Lambda became " _ ", so the de-whitelisted
    # 2.251 rule could never fire on the very lines delatex was added to expose. The two patches
    # cancelled to nothing. TRANSLATE the anchors before dropping the rest.
    for macro, sym in ((r"\rho_\Lambda", "ρ_Λ"), (r"\rho_\infty", "ρ_∞"), (r"\Lambda", "Λ"),
                       (r"\varepsilon", "ε"), (r"\epsilon", "ε"), (r"\alpha_c", "α_c"),
                       (r"\alpha", "α"), (r"\bar{f}", "f̄"), (r"\Sigma", "Σ"),
                       (r"\sigma", "σ"), (r"\tau", "τ"), (r"\rho", "ρ"), (r"\mu", "μ"),
                       (r"\nu", "ν"), (r"\Delta", "Δ"), (r"\chi", "χ"), (r"\pi", "π"),
                       # \ln was absent, so the catch-all ate it and "Δ \ln Z" became "Δ   Z" --
                       # the DlnZ rule went blind. The SAME species the ledger said was fixed.
                       (r"\ln", "ln"), (r"\log", "log"), (r"\sqrt", "sqrt"), (r"\beta", "β"),
                       (r"\gamma", "γ"), (r"\lambda", "λ"), (r"\theta", "θ"), (r"\xi", "ξ")):
        t = t.replace(macro, sym)
    t = re.sub(r"\\[a-zA-Z]+", " ", t)                               # any remaining \macro
    t = re.sub(r"\\(?=[\s,;:!])|\\\s", " ", t)                        # LaTeX escaped space: 193\ keV -> 193 keV
    t = t.replace("\\", " ")                                        # any stragglers
    t = t.replace("$", "").replace("{", " ").replace("}", " ").replace("^", "")
    return t

def audit(include_archive=False):
    ch = chain()
    print("="*82); print("THE DERIVATION CHAIN -- recomputed from the standing inputs"); print("="*82)
    print(f"  alpha = 1/137.035999206 ,  d = {d_space} (the SPATIAL dimension -- JP's ruling)")
    print(f"  c      = (N-1)/N census                 = {ch['c']:.6f}")
    print(f"  f-bar  = 2/pi  (winding <|cos|>)        = {ch['f_bar']:.6f}")
    print(f"  alpha_c= d * alpha                      = {ch['alpha_c']:.8f}")
    print(f"  eps    = c * f-bar * alpha_c            = {ch['eps_pct']:.4f} %")
    print(f"         = 27 alpha / 5 pi  (closed form) = {ch['eps_closed_pct']:.4f} %   {'MATCH' if abs(ch['eps_pct']-ch['eps_closed_pct'])<1e-9 else 'MISMATCH!!'}")
    print(f"  T_c                                     = {ch['T_c_keV']:.0f} keV")
    print(f"  M2     = alpha^2 * T_c                  = {ch['M2_eV']:.3f} eV")
    print(f"  rho_L^(1/4) = 1/2 alpha_c^2 M2          = {ch['rho_L_meV']:.4f} meV   (observed 2.25 -> {(ch['rho_L_meV']/2.25-1)*100:+.2f}%)")
    print(f"  tau    = T_c/m_e                        = {ch['tau']:.4f}")
    print(f"  partial waves E_n = rho^(1/4)/n^2 : 1s {ch['E_1s']:.3f} | 2p {ch['E_2p']:.3f} ({(ch['E_2p']/2.25-1)*100:+.1f}%) | 4f {ch['E_4f']:.3f} ({(ch['E_4f']/2.25-1)*100:+.1f}%)")
    print()
    print("="*82); print("SCAN -- retired values quoted AS their quantity (role-bound, not value-bound)"); print("="*82)
    hits=[]; seen=set()
    files = sorted(set(glob.glob("docs/*.md")+glob.glob("docs/**/*.md", recursive=True)))
    for f in files:
        b=os.path.basename(f)
        if not include_archive and any(a in b for a in ARCHIVE): continue
        L=open(f,encoding="utf-8",errors="replace").readlines()
        for ln,line in enumerate(L,1):
            window = "".join(L[max(0,ln-2):ln+1])   # prose wraps; context can sit a line away
            line = delatex(line)                    # math is not exempt from the value rules
            for c in CHECKS:
                for m in re.finditer(c["rx"], line, re.I):
                    g=[x for x in m.groups() if x]
                    if not g: continue
                    try: v=float(g[0].translate(_SUP))
                    except: continue
                    if any(abs(v-o)<5e-4 for o in c["ok"]): continue
                    if RETIREMENT_CTX.search(window): continue        # naming what it buries: legal
                    if c["q"]=="DlnZ quoted bare" and CONDITIONALITY_CTX.search(window): continue
                    if c["q"]=="c (census)" and LIGHTSPEED_CTX.search(window): continue  # different c
                    if c["q"]=="H_0 standing" and H0_RUNRECORD_CTX.search(window): continue  # run record / TRGB anchor -- H0 only
                    if c["q"]=="tau = T_c/m_e" and re.search(
                        r"invert|observ|read backwards|rounding|0\.35\b|→ ?0\.35|→0\.35|"
                        r"flagship-grade|not a sourced|not the model|deletes the|"
                        r"observed value fixes|the problem, not the answer|"
                        r"back-solved|lands inside|consistency check|did not have to|"
                        r"weak.{0,15}consistency", window, re.I):
                        continue   # a line EXPLAINING 0.345 = the observation inverted is not a claim
                    for badv,why in c["bad"].items():
                        if abs(v-badv) < 5e-4:
                            key=(b,ln,c["q"],v)
                            if key in seen: continue
                            seen.add(key); hits.append((b,ln,c["q"],v,why,line.strip()[:92]))
    if hits:
        print(f"  {len(hits)} LEAK(S):\n")
        for b,ln,q,v,why,txt in hits:
            print(f"   {b}:{ln}  [{q}] = {v}")
            print(f"      -> {why}")
            print(f"      {txt}\n")
    else:
        print("  CLEAN: no retired value is quoted as its quantity on the live shelf.")
    return hits

if __name__ == "__main__":
    if "--derive" in sys.argv:
        for k,v in chain().items(): print(f"  {k:16s} {v}")
    else:
        h = audit("--all" in sys.argv); sys.exit(1 if h else 0)
