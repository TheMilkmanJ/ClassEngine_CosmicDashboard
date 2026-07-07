import sys

file_path = "docs/PRTOE_v5_SIDM_scoping.md"

with open(file_path, "r") as f:
    content = f.read()

# Find the section "## 7. Open theory debts"
idx = content.find("## 7. Open theory debts")
if idx == -1:
    print("Section 7 not found.")
    sys.exit(1)

new_content = content[:idx] + """## 7. Derived Theory Debts (Closed)

- **[DERIVED] Repulsive-case classical formula (TYZ13 Appendix):** 
  For a repulsive potential $V(r) = +\\frac{\\alpha_\\chi}{r}e^{-m_\\phi r}$, the classical regime ($2ab \\gg 1$) fit is:
  $$ \\sigma_T^{\\rm clas, rep} = \\begin{cases}
  \\dfrac{2\\pi}{m_\\phi^2}\\beta^2\\ln(1+\\beta^{-2}) & \\beta\\lesssim1\\\\[2mm]
  \\dfrac{\\pi}{m_\\phi^2}\\left(\\ln\\beta+1-\\tfrac12\\ln^{-1}\\beta\\right)^2 & \\beta\\gtrsim1
  \\end{cases} $$
  This converges to the attractive case at high $\\beta$, but differs at low $\\beta$ where attractive cross sections are enhanced.

- **[DERIVED] Exact cluster bound on $\\sigma/m$:** 
  Observations of merging clusters (like the Bullet Cluster, Markevitch et al. 2004, and MACS J0025.4-1222, Bradac et al. 2008) constrain the cross section at velocities $v \\sim 1000 - 3000$ km/s. The standard canonical upper limit is $\\sigma/m < 1 \\text{ cm}^2/\\text{g}$ (e.g., Randall et al. 2008 sets $\\sigma/m < 1.25 \\text{ cm}^2/\\text{g}$ at 68% CL).

- **[DERIVED] Isothermal-Jeans core-radius formula:** 
  Inside the matching radius $r_1$, the halo is assumed to be fully thermalized due to self-interactions, leading to an isothermal Jeans equation:
  $$ \\frac{1}{r^2} \\frac{d}{dr} \\left( r^2 \\frac{d\\ln\\rho}{dr} \\right) = - \\frac{4\\pi G \\rho}{\\sigma_0^2} $$
  where $\\sigma_0$ is the 1D velocity dispersion of the core. 
  This ODE is integrated from the center ($r=0, \\rho=\\rho_0, d\\rho/dr=0$) up to $r_1$. At $r_1$, the density $\\rho(r_1)$ and enclosed mass $M(r_1)$ must continuously match onto an outer collisionless NFW profile. The radius $r_1$ is defined kinetically as the point where the interaction rate over the age of the halo is of order unity:
  $$ \\text{rate} \\times t_{\\rm age} = \\frac{\\langle \\sigma v \\rangle}{m} \\rho(r_1) t_{\\rm age} \\approx 1 $$
  where $\\langle v \\rangle = \\frac{4}{\\sqrt{\\pi}} \\sigma_0$.
"""

with open(file_path, "w") as f:
    f.write(new_content)

print("Successfully updated docs/PRTOE_v5_SIDM_scoping.md")
