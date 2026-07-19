# PRTOE BIBLIOGRAPHY — every external source the model stands on (2026-07-11)

*The source list (the working docket). Keys are used across the docs as [AuthorYear]. Internal
provenance (t###/def### turn-tags) traces to the internal working record; THIS file traces everything
we borrowed from the field. If a claim in any doc leans on a result not listed here,
that is a bug — file it.*

## 1. Data and likelihoods (what the model is tested against)

- **[Planck2018]** Planck Collaboration (N. Aghanim et al.), "Planck 2018 results. VI. Cosmological parameters," A&A 641, A6 (2020), arXiv:1807.06209. — The CMB baseline; all chain likelihoods.
- **[PlanckLik2019]** Planck Collaboration, "Planck 2018 results. V. CMB power spectra and likelihoods," A&A 641, A5 (2020), arXiv:1907.12875. — The plik/lowl likelihood stack the pipeline calls.
- **[PlanckIso2019]** Planck Collaboration, "Planck 2018 results. VII. Isotropy and statistics," A&A 641, A7 (2020), arXiv:1906.02552. — The isotropy/anomaly baseline for the axis-family predictions.
- **[Riess2022]** A. G. Riess et al. (SH0ES), "A comprehensive measurement of the local value of the Hubble constant," ApJL 934, L7 (2022), arXiv:2112.04510. — H₀ = 73.0 ± 1.0; the tension's ladder side.
- **[Freedman2021]** W. L. Freedman, "Measurements of the Hubble constant: tensions in perspective," ApJ 919, 16 (2021), arXiv:2106.15656. — The TRGB counterweight; polices P-2026-001.
- **[DESI2024]** DESI Collaboration, "DESI 2024 VI: cosmological constraints from BAO," arXiv:2404.03002. — The BAO/w(z) frontier; DR3 is the model's named top falsifier.
- **[eBOSS2021]** S. Alam et al. (eBOSS), "Completed SDSS-IV eBOSS: cosmological implications," PRD 103, 083533 (2021), arXiv:2007.08991. — Pre-DESI BAO in the chain stacks.
- **[Pantheon+2022]** D. Brout et al., "The Pantheon+ analysis: cosmological constraints," ApJ 938, 110 (2022), arXiv:2202.04077. — The SNe leg.
- **[Cooke2018]** R. J. Cooke, M. Pettini, C. C. Steidel, "One percent determination of the primordial deuterium abundance," ApJ 855, 102 (2018), arXiv:1710.11129. — D/H = (2.527 ± 0.030)×10⁻⁵ — the observational pole of the D/H fork; the model predicts 2.407–2.463×10⁻⁵ across its committed genesis window, **−2.5 to −1.4σ** on the full budget (obs ±0.030 ⊕ PRIMAT theory ±0.037 = ±0.0476).
- **[Aver2021]** E. Aver et al., "Improved helium abundance determination with EMP galaxies," JCAP 03 (2021) 027, arXiv:2010.04180. — Y_p = 0.2453 ± 0.0034; one side of the helium war.
- **[EMPRESS2022]** A. Matsumoto et al. (EMPRESS VIII), "EMPRESS. VIII. A new determination of primordial He abundance," ApJ 941, 167 (2022), arXiv:2203.09617. — The low-Y_p side; the war's other pole.
- **[FIRAS1996]** D. J. Fixsen et al., "The CMB spectrum from the full COBE FIRAS data set," ApJ 473, 576 (1996). — The perfect blackbody; the plasma's witness.
- **[GW170817]** B. P. Abbott et al. (LIGO/Virgo), PRL 119, 161101 (2017); and B. P. Abbott et al., ApJL 848, L13 (2017). — GW speed = c to 10⁻¹⁵; the one-metric constraint.
- **[NANOGrav2023]** G. Agazie et al. (NANOGrav), "The NANOGrav 15 yr data set: evidence for a gravitational-wave background," ApJL 951, L8 (2023), arXiv:2306.16213. — The PTA band; the vortex-string Gμ null lives here.
- **[SNO2002]** Q. R. Ahmad et al. (SNO), PRL 89, 011301 (2002). / **[SuperK1998]** Y. Fukuda et al., PRL 81, 1562 (1998). — Neutrino flavor transformation; the fusion-neutrino record.

- **[KamLANDZen2024]** KamLAND-Zen Collaboration (S. Abe et al.), "Search for Majorana neutrinos with the complete KamLAND-Zen dataset," arXiv:2406.11438. — The strongest current 0νββ limit (m_ββ ≲ 28–122 meV); also the refuter (with GERDA) of the historical Heidelberg–Moscow claim.
- **[GERDA2020]** GERDA Collaboration (M. Agostini et al.), "Final results of GERDA on the search for 0νββ decay," PRL 125, 252502 (2020), arXiv:2009.06079.
- **[nEXO2021]** nEXO Collaboration (G. Adhikari et al.), "nEXO: neutrinoless double β decay search beyond 10²⁸ year half-life sensitivity," J. Phys. G 49, 015104 (2022), arXiv:2106.16243. — The ton-scale referee this sector names.
- **[LEGEND2021]** LEGEND Collaboration, "The Large Enriched Germanium Experiment for Neutrinoless ββ Decay: LEGEND-1000 pCDR," arXiv:2107.11462.
- **[CUPID2019]** CUPID Interest Group, "CUPID pre-CDR," arXiv:1907.09376.
- **[NuFIT]** I. Esteban et al., "The fate of hints: updated global analysis of three-flavor neutrino oscillations," JHEP 09 (2020) 178, arXiv:2007.14792 (nufit.org). — The mixing angles and splittings used in the m_ββ computation.

## 2. Codes and tools (what the pipeline runs on)

- **[CLASS2011]** D. Blas, J. Lesgourgues, T. Tram, "The Cosmic Linear Anisotropy Solving System (CLASS) II," JCAP 07 (2011) 034, arXiv:1104.2933. — The Boltzmann code the model is implemented in.
- **[cobaya2021]** J. Torrado, A. Lewis, "Cobaya: code for Bayesian analysis," JCAP 05 (2021) 057, arXiv:2005.05290. — The sampler driving every chain in chains/.
- **[PolyChord2015]** W. J. Handley, M. P. Hobson, A. N. Lasenby, "PolyChord: next-generation nested sampling," MNRAS 453, 4384 (2015), arXiv:1506.00171. — The committed evidence gate (the working docket).
- **[HyRec2011]** Y. Ali-Haïmoud, C. M. Hirata, "HyRec: a fast and highly accurate primordial hydrogen and helium recombination code," PRD 83, 043513 (2011), arXiv:1011.3758. — Recombination micro-physics (m_e-sensitive).
- **[PRyMordial2023]** A.-K. Burns, T. M. P. Tait, M. Valli, "PRyMordial: the first three minutes, within and beyond the Standard Model," arXiv:2307.07061. — The BBN engine behind the windowed run (tools/PRyMordial).
- **[PRIMAT2018]** C. Pitrou, A. Coc, J.-P. Uzan, E. Vangioni, "Precision big bang nucleosynthesis with improved helium-4 predictions," Phys. Rept. 754, 1 (2018), arXiv:1801.08023. — The BBN rate compilation standard.
- **[PyBOBYQA2019]** C. Cartis, J. Fiala, B. Marteau, L. Roberts, "Improving the flexibility and robustness of model-based derivative-free optimization solvers," ACM TOMS 45, 32 (2019), arXiv:1804.00154. — The optimizer (see the plateau law in memory).

## 3. The mechanism's literature (varying m_e and the H₀ tension)

- **[HartChluba2018]** L. Hart, J. Chluba, "New constraints on time-varying fundamental constants from Planck," MNRAS 474, 1850 (2018), arXiv:1705.03925.
- **[HartChluba2020]** L. Hart, J. Chluba, "Updated fundamental constant constraints from Planck 2018 data and possible relations to the Hubble tension," MNRAS 493, 3255 (2020), arXiv:1912.03986. — The varying-m_e ↔ H₀ degeneracy the dyad gives an ontology to.
- **[SekiguchiTakahashi2021]** T. Sekiguchi, T. Takahashi, "Early recombination as a solution to the H₀ tension," PRD 103, 083507 (2021), arXiv:2007.03381. — The independent varying-m_e H₀ result.
- **[DiValentino2021]** E. Di Valentino et al., "In the realm of the Hubble tension — a review of solutions," Class. Quant. Grav. 38, 153001 (2021), arXiv:2103.01183. — The competitor map.

## 4. Condensates, superfluids, and analog gravity (the medium's physics)

- **[Gross1961]** E. P. Gross, Nuovo Cimento 20, 454 (1961). / **[Pitaevskii1961]** L. P. Pitaevskii, Sov. Phys. JETP 13, 451 (1961). — The GP equation (Equation 1 of the three-equation file).
- **[Onsager1949]** L. Onsager, Nuovo Cimento 6 (Suppl. 2), 279 (1949). / **[Feynman1955]** R. P. Feynman, Prog. Low Temp. Phys. 1, 17 (1955). — Quantized circulation; the winding sector's protection.
- **[BCS1957]** J. Bardeen, L. N. Cooper, J. R. Schrieffer, Phys. Rev. 108, 1175 (1957). — The pairing grammar (the 3b "family business" lane).
- **[Josephson1962]** B. D. Josephson, Phys. Lett. 1, 251 (1962). — The junction template for the Card-4 AD-direct transfer.
- **[Haken1975]** H. Haken, "Cooperative phenomena in systems far from thermal equilibrium and in nonphysical systems," Rev. Mod. Phys. 47, 67 (1975). — The laser threshold as a nonequilibrium phase transition (the laser file's GL mapping).
- **[GinzburgLandau1950]** V. L. Ginzburg, L. D. Landau, Zh. Eksp. Teor. Fiz. 20, 1064 (1950). — Mean-field order parameters; the λ-ceiling's β = 1/2 lock.
- **[Kibble1976]** T. W. B. Kibble, "Topology of cosmic domains and strings," J. Phys. A 9, 1387 (1976). / **[Zurek1985]** W. H. Zurek, "Cosmological experiments in superfluid helium?," Nature 317, 505 (1985). — Defect formation at the transition; the first-draw statistics.
- **[Landau1941]** L. D. Landau, "Theory of the superfluidity of helium II," J. Phys. USSR 5, 71 (1941) [Phys. Rev. 60, 356 (1941)]. — The criterion; sub-critical motion is dissipation-free (the inertia file's spine).
- **[Kapitza1938]** P. Kapitza, Nature 141, 74 (1938). / **[AllenMisener1938]** J. F. Allen, A. D. Misener, Nature 141, 75 (1938). — Superfluidity's discovery.
- **[ColemanGlashow1999]** S. Coleman, S. L. Glashow, "High-energy tests of Lorentz invariance," PRD 59, 116008 (1999), arXiv:hep-ph/9812418. — Vacuum-Cherenkov / UHECR bounds; the inertia file's dispersion exam.
- **[Turyshev2012]** S. G. Turyshev et al., "Support for the thermal origin of the Pioneer anomaly," PRL 108, 241101 (2012), arXiv:1204.2507. — The vacuum-drag null's case study.
- **[Synge1950]** J. L. Synge, Proc. R. Irish Acad. A 53, 83 (1950). / **[Kruskal1960]** M. D. Kruskal, Phys. Rev. 119, 1743 (1960). / **[Szekeres1960]** G. Szekeres, Publ. Math. Debrecen 7, 285 (1960). — The maximal Schwarzschild extension; the white-hole region's actual discoverers (post-Einstein — the white-holes file's historical note).
- **[HaggardRovelli2015]** H. M. Haggard, C. Rovelli, "Black hole fireworks: quantum-gravity effects outside the horizon spark black to white hole tunneling," PRD 92, 104020 (2015), arXiv:1407.0989. — The literature's white-hole revival; cited for pedigree, refused for local objects (the arrow ban).
- **[Unruh1981]** W. G. Unruh, "Experimental black-hole evaporation?," PRL 46, 1351 (1981). — Acoustic horizons; the analog frame.
- **[BLV2005]** C. Barceló, S. Liberati, M. Visser, "Analogue gravity," Living Rev. Rel. 8, 12 (2005), arXiv:gr-qc/0505065. — The emergent-metric toolbox and its known limits (the linearized-plus caveat).
- **[Volovik2003]** G. E. Volovik, *The Universe in a Helium Droplet*, Oxford (2003). — The deepest prior art for medium-cosmology; the model's closest intellectual neighbor.
- **[vonKlitzing1980]** K. von Klitzing, G. Dorda, M. Pepper, PRL 45, 494 (1980). — Topological quantization on a bench (the lab-cousin row).

- **[ArkaniHamed2004]** N. Arkani-Hamed, H.-C. Cheng, M. Luty, S. Mukohyama, "Ghost condensation and a consistent infrared modification of gravity," JHEP 05 (2004) 074, arXiv:hep-th/0312099. — The ghost-condensate frame the arrow-giver adopts (θ-dot background = the permanent μ); its bounded NEC-flexibility is the exotic-spacetime shelf's priced sector.

- **[Leggett1980]** A. J. Leggett, "Diatomic molecules and Cooper pairs," in *Modern Trends in the Theory of Condensed Matter*, Springer (1980). / **[NSR1985]** P. Nozières, S. Schmitt-Rink, "Bose condensation in an attractive fermion gas," J. Low Temp. Phys. 59, 195 (1985). — The BCS–BEC crossover machinery the measurement-sector computation runs on.

- **[Combescot1990]** R. Combescot, "Critical temperature of superconductors: Exact solution from Eliashberg equations on the weak-coupling side," Phys. Rev. B 42, 7810 (1990). / **[Marsiglio2018]** F. Marsiglio et al., "Eliashberg theory in the weak-coupling limit," arXiv:1807.04907; real-axis companion arXiv:1912.09460. — The exact weak-coupling prefactor T_c = 1.13 e^{-3/2} ω_c e^{-1/λ} the referee sessions run on.

- **[NBV2006]** A. Nayeri, R. Brandenberger, C. Vafa, "Producing a scale-invariant spectrum of perturbations in a Hagedorn phase of string cosmology," PRL 97, 021302 (2006), arXiv:hep-th/0511140. / **[BrandenbergerVafa1989]** R. Brandenberger, C. Vafa, "Superstrings in the early universe," Nucl. Phys. B 316, 391 (1989). / **[SGCreview2011]** R. Brandenberger, "String gas cosmology: progress and problems," Class. Quantum Grav. 28, 204005 (2011), arXiv:1105.3247. — The thermal/maximal-temperature/area-specific-heat cousin of lock 2's lane: the model's "maximal thermal allowance" = the Hagedorn concept; its winding-mode C_V ∝ R² = the exemption-clause drift, thermodynamic road.

- **[KSS2005]** P. Kovtun, D. T. Son, A. O. Starinets, "Viscosity in strongly interacting quantum field theories from black hole physics," PRL 94, 111601 (2005), arXiv:hep-th/0405231. — The lower viscosity fence (η/s ≥ hbar/4pi); the zero-infinity asymmetry's other end.

- **[WidnallTsai1977]** S. E. Widnall, C.-Y. Tsai, "The instability of the thin vortex ring of constant vorticity," Phil. Trans. R. Soc. A 287, 273 (1977). / **[Gharib1998]** M. Gharib, E. Rambod, K. Shariff, "A universal time scale for vortex ring formation," J. Fluid Mech. 360, 121 (1998). — The Widnall azimuthal selection (ka = 2.26-2.51 → the n-predictor) and the universal formation number (F ~ 4 → the partition/window targets).

- **[Ubachs-μ-class]** M. Daprà et al., MNRAS 454, 489 (2015) & MNRAS 465, 4057 (2017) (H₂/HD, Δμ/μ ~ 10⁻⁶⁻⁷); J. Albornoz Vásquez et al., A&A 562, A88 (2014) (Q J0643−5041); N. Kanekar-class NH₃/CH₃OH toward PKS 1830−211 (Δμ/μ ~ 10⁻⁷ at z=0.89). — The μ-variation bounds; the structural audit: all constraining absorbers are dense molecular gas = screened rooms under reading B.

## 5. Emergent gravity, entropy, and the keystone

- **[Sakharov1967]** A. D. Sakharov, "Vacuum quantum fluctuations in curved space and the theory of gravitation," Dokl. Akad. Nauk SSSR 177, 70 (1967). — Induced gravity; the NO-BARE clause's ancestor.
- **[Jacobson1995]** T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state," PRL 75, 1260 (1995), arXiv:gr-qc/9504004. — The route from the area law to Einstein's equations.
- **[Bekenstein1973]** J. D. Bekenstein, PRD 7, 2333 (1973). / **[Hawking1975]** S. W. Hawking, Commun. Math. Phys. 43, 199 (1975). — S = A/4 and its temperature.
- **[FFZ1997]** V. P. Frolov, D. V. Fursaev, A. I. Zelnikov, "Statistical origin of black hole entropy in induced gravity," Nucl. Phys. B 486, 339 (1997), arXiv:hep-th/9607104. — The species-cancellation the keystone leans on.
- **[WeinbergWitten1980]** S. Weinberg, E. Witten, "Limits on massless particles," Phys. Lett. B 96, 59 (1980). — The no-go the preferred frame evades.
- **[Penrose1965]** R. Penrose, "Gravitational collapse and space-time singularities," PRL 14, 57 (1965). — The theorem the CSW-floor core discharges by violating its energy condition honestly.

## 6. Particle theory (the census arc and the portal)

- **[MachacekVaughn1983]** M. E. Machacek, M. T. Vaughn, "Two-loop renormalization group equations in a general quantum field theory (I). Wave function renormalization," Nucl. Phys. B 222, 83 (1983). — The two-loop coefficients behind the P-039 suspension.
- **[FLHJ1989]** R. Foot, H. Lew, X.-G. He, G. C. Joshi, "See-saw neutrino masses induced by a triplet of leptons," Z. Phys. C 44, 441 (1989). — Type-III seesaw; the Y=0 triplet's job description.
- **[CMS2020typeIII]** CMS Collaboration, "Search for physics beyond the standard model in multilepton final states (type-III seesaw)," arXiv:1911.04968. / **[ATLAS2022typeIII]** ATLAS Collaboration, arXiv:2202.02039. — The ~0.9–1.0 TeV exclusion the knife edge sits above.
- **[AffleckDine1985]** I. Affleck, M. Dine, "A new mechanism for baryogenesis," Nucl. Phys. B 249, 361 (1985). — The AD-direct route (charge = abundance).
- **[FukugitaYanagida1986]** M. Fukugita, T. Yanagida, "Baryogenesis without grand unification," Phys. Lett. B 174, 45 (1986). — The thermal-leptogenesis baseline the empty-surface scan retired in-model.
- **[ColemanWeinberg1973]** S. Coleman, E. Weinberg, "Radiative corrections as the origin of spontaneous symmetry breaking," PRD 7, 1888 (1973). — Cited by the legacy action's activation form.
- **[Koide1983]** Y. Koide, "A fermion-boson composite model of quarks and leptons," Phys. Lett. B 120, 161 (1983); PRD 28, 252 (1983). — The charged-lepton relation the dyad must not break (thread 6).
- **[Tsirelson1980]** B. S. Tsirelson, "Quantum generalizations of Bell's inequality," Lett. Math. Phys. 4, 93 (1980). — The bound the quantum wing treats as a standing exam.

- **[Zurek2003]** W. H. Zurek, "Environment-assisted invariance, entanglement, and probabilities in quantum physics," PRL 90, 120404 (2003), arXiv:quant-ph/0211037 (and PRA 71, 052105). — The envariance derivation of the Born rule; the swap partners are the twins (the selection law, clause ii — adopted).

## 7. Precision tests (the constraints the medium must satisfy)

- **[Will2014]** C. M. Will, "The confrontation between general relativity and experiment," Living Rev. Rel. 17, 4 (2014), arXiv:1403.7377. — The PPN tests.
- **[Vainshtein1972]** A. I. Vainshtein, "To the problem of nonvanishing gravitation mass," Phys. Lett. B 39, 393 (1972). — The screening margin in the EP gate.
- **[HNS2009]** L. Hui, A. Nicolis, C. Stubbs, "Equivalence principle implications of modified gravity models," PRD 80, 104002 (2009), arXiv:0905.2966. — The EP test the gate clears with five orders.
- **[Herrmann2009]** S. Herrmann et al., "Rotating optical cavity experiment testing Lorentz invariance at the 10⁻¹⁷ level," PRD 80, 105011 (2009), arXiv:1002.1284. — Modern Michelson-Morley; the M3 bill's size.
- **[Mattingly2005]** D. Mattingly, "Modern tests of Lorentz invariance," Living Rev. Rel. 8, 5 (2005). / **[Liberati2013]** S. Liberati, "Tests of Lorentz invariance: a 2013 update," Class. Quant. Grav. 30, 133001 (2013), arXiv:1304.5795. — The LV pricing pass's sources.
- **[Bailey1977]** J. Bailey et al., "Measurements of relativistic time dilatation for positive and negative muons in a circular orbit," Nature 268, 301 (1977). — Time dilation with no atoms to heat.
- **[Ashby2003]** N. Ashby, "Relativity in the Global Positioning System," Living Rev. Rel. 6, 1 (2003). — The 38 μs/day that keeps maps working.
- **[DamourDyson1996]** T. Damour, F. Dyson, "The Oklo bound on the time variation of the fine-structure constant revisited," Nucl. Phys. B 480, 37 (1996), arXiv:hep-ph/9606486. — The Oklo fence (great chain, Appendix B).
- **[Detweiler1980]** S. Detweiler, "Klein-Gordon equation and rotating black holes," PRD 22, 2323 (1980). — The superradiance rate behind the SMBH spin-dip band (P-035).

## 8. Anisotropy, topology, and the axis family

- **[CSS1998]** N. J. Cornish, D. N. Spergel, G. D. Starkman, "Circles in the sky: finding topology with the microwave background," Class. Quant. Grav. 15, 2657 (1998), arXiv:astro-ph/9801212. — Matched circles; the compact-axis search method.
- **[HajianSouradeep2003]** A. Hajian, T. Souradeep, "Measuring the statistical isotropy of the CMB anisotropy," ApJL 597, L5 (2003), arXiv:astro-ph/0308001. — The BipoSH formalism policing the axis family.
- **[JackiwPi2003]** R. Jackiw, S.-Y. Pi, "Chern-Simons modification of general relativity," PRD 68, 104012 (2003), arXiv:gr-qc/0308071. / **[AlexanderYunes2009]** S. Alexander, N. Yunes, "Chern-Simons modified general relativity," Phys. Rept. 480, 1 (2009), arXiv:0907.2562. — The dCS machinery the chiral-GW debt inherits.

## 9. Neighboring dark-sector models (the honest competitors and cousins)

- **[BerezhianiKhoury2015]** L. Berezhiani, J. Khoury, "Theory of dark matter superfluidity," PRD 92, 103510 (2015), arXiv:1507.01019. — The nearest superfluid-DM cousin; differs by scope (galactic vs cosmological) and by the dyad.
- **[HBG2000]** W. Hu, R. Barkana, A. Gruzinov, "Cold and fuzzy dark matter," PRL 85, 1158 (2000), arXiv:astro-ph/0003365. / **[Hui2017]** L. Hui, J. P. Ostriker, S. Tremaine, E. Witten, "Ultralight scalars as cosmological dark matter," PRD 95, 043541 (2017), arXiv:1610.08297. — The ultralight-field toolbox (ξ-scale physics).
- **[Kamenshchik2001]** A. Kamenshchik, U. Moschella, V. Pasquier, "An alternative to quintessence," Phys. Lett. B 511, 265 (2001), arXiv:gr-qc/0103004. — The unified-dark-fluid (Chaplygin) precedent dCDF improves on.
- **[Hu1998]** W. Hu, "Structure formation with generalized dark matter," ApJ 506, 485 (1998), arXiv:astro-ph/9801234. — The GDM formalism the perturbation-sector debt (the working docket) will be phrased in.
- **[Milgrom1983]** M. Milgrom, ApJ 270, 365 (1983). / **[MLS2016]** S. McGaugh, F. Lelli, J. Schombert, "The radial acceleration relation in rotationally supported galaxies," PRL 117, 201101 (2016), arXiv:1609.05917. — The RAR the galactic-atoms thread engages; MOND's kill/reopen history.
- **[Banik2024]** I. Banik et al., "Strong constraints on MOND from wide binaries," MNRAS 527, 4573 (2024), arXiv:2311.03436. / **[Chae2023]** K.-H. Chae, ApJ 952, 128 (2023), arXiv:2305.04613. — The live wide-binary dispute (P-036 sides with Newton).

## 10. Historical foundations (the legacy action's ancestry — retired era)

- **[BransDicke1961]** C. Brans, R. H. Dicke, Phys. Rev. 124, 925 (1961). — The e^{ξφ}-class ancestor.
- **[Horndeski1974]** G. W. Horndeski, Int. J. Theor. Phys. 10, 363 (1974). — The general scalar-tensor frame.
- **[LangloisNoui2016]** D. Langlois, K. Noui, "Degenerate higher derivative theories beyond Horndeski," JCAP 02 (2016) 034, arXiv:1510.06930. — The DHOST conditions the legacy spec invoked.

## 11. Exotic spacetime (the impossibility shelf — PRTOE_wormholes.md + PRTOE_white_holes.md)

- **[MorrisThorne1988]** M. Morris, K. Thorne, "Wormholes in spacetime and their use for interstellar travel," Am. J. Phys. 56, 395 (1988). — The traversable-wormhole exotic-matter requirement (NEC violation) the solvency reading re-derives.
- **[FordRoman1995]** L. H. Ford, T. A. Roman, "Averaged energy conditions and quantum inequalities," Phys. Rev. D 51, 4277 (1995), arXiv:gr-qc/9410043. — The quantum bounds squeezing sustained negative energy; the record's version of "no eternal overdraft."
- **[Eardley1974]** D. M. Eardley, "Death of white holes in the early universe," PRL 33, 442 (1974). — The classical white-hole instability; the record's statistical/instability kill the arrow argument upgrades structurally.
- **[Hawking1992]** S. W. Hawking, "Chronology protection conjecture," Phys. Rev. D 46, 603 (1992). — The record's CTC ban; the principle is "no state can be its own source."
- **[Alcubierre1994]** M. Alcubierre, "The warp drive: hyper-fast travel within general relativity," Class. Quantum Grav. 11, L73 (1994), arXiv:gr-qc/0009013. — The warp bubble paying the same NEC bill.
- **[RovelliHaggard2014]** H. Haggard, C. Rovelli, "Black hole fireworks: quantum-gravity effects outside the horizon spark black to white hole tunneling," Phys. Rev. D 92, 104020 (2015), arXiv:1407.0989. / **[RovelliVidotto2018]** C. Rovelli, F. Vidotto, "Small black/white hole stability and dark matter," Universe 4, 127 (2018), arXiv:1805.03872. — The black-to-white transition program the model's mirror mechanism independently reproduces; its confirmed LOCAL remnant signature is this shelf's named killer.

---

*Coverage note: keys appear in the docs as [AuthorYear]. The five internal-provenance
stragglers found by the audit (SKELETON, the legacy action spec, intellectual_history,
lss_parity, v4_dCDF_results) are stamped in this pass. Anything cited in a doc but missing
here is a filed bug — the rule: no borrowed result without a line in this file.*

- **[KSTVZ2000]** J. B. Kogut, M. A. Stephanov, D. Toublan, J. J. M. Verbaarschot, A. Zhitnitsky, "QCD-like theories at finite baryon density," Nucl. Phys. B 582, 477 (2000), arXiv:hep-ph/0001171. / **[Hands2006]** S. Hands, S. Kim, J.-I. Skullerud, "Deconfinement in dense 2-color QCD," Eur. Phys. J. C 48, 193 (2006), arXiv:hep-lat/0604004. — Two-color QCD: the fundamental representation of SU(2) is pseudo-real, so colour singlets require an even number of quarks and **baryons are bosonic diquarks**; the lightest baryon is a scalar diquark, and the theory realizes the **BEC–BCS crossover** with a diquark condensate. The structural cousin of the dark-sector colour group the finiteness count selects (PRTOE_DERIVATION_HUNT §6).
- **[FingbergHellerKarsch1993]** J. Fingberg, U. Heller, F. Karsch, "Scaling and asymptotic scaling in the SU(2) gauge theory," Nucl. Phys. B 392, 493 (1993), arXiv:hep-lat/9208012. / **[Boyd1996]** G. Boyd et al., "Thermodynamics of SU(3) lattice gauge theory," Nucl. Phys. B 469, 419 (1996), arXiv:hep-lat/9602007. — The pure-glue deconfinement-to-string-tension anchors: **SU(2) T_c/√σ ≈ 0.69–0.71**, **SU(3) ≈ 0.63**. The τ = T_c/√σ band the dark-energy scale rides on (§2) is quoted from the SU(3)-with-light-quarks value; the SU(2) N_f = 3 counterpart is the open number of §6's candidate.

- **[TashiroVachaspati2013]** H. Tashiro, T. Vachaspati, "Parity-odd correlators of diffuse gamma-rays and intergalactic magnetic fields," MNRAS 448, 299 (2015), arXiv:1409.3627. / **[ChenEtAl2015]** W. Chen, B. D. Chowdhury, F. Ferrer, H. Tashiro, T. Vachaspati, "Intergalactic magnetic field spectra from diffuse gamma-rays," MNRAS 450, 3371 (2015), arXiv:1412.3171. — The parity-odd correlator of Fermi-LAT diffuse gamma-ray arrival directions, read as a **helical** intergalactic magnetic field: **B ≈ 10⁻¹⁴ G on ≈ 10 Mpc, left-handed**. Stress-tested with stringent cuts, exposure-aware Monte Carlo, and N/S hemisphere splits; the correlator peaks' **power-law scaling with gamma-ray energy** was predicted and held. The possible first datum of this model's chirality family (T14; P-2026-028, sign(helicity_B) = sign(n)) — **but unreadable until the AD-direct rectification (link 5) fixes which handedness corresponds to matter winning.** The contrary result (no handedness via Q-statistics) is a non-detection whose authors state they cannot separate absence from insufficient sensitivity.

- **[ColpiShapiroWasserman1986]** S. Colpi, S. L. Shapiro, I. Wasserman, "Boson stars: gravitational equilibria of self-interacting scalar fields," Phys. Rev. Lett. 57, 2485 (1986). — The maximum mass of a self-interacting boson star, M_max ≈ 0.22 √λ M_Pl³/m². Used to price the quartic against black-hole support: holding the largest known black holes needs λ ≳ 8×10⁻⁹⁴, which the derived value clears by more than two orders (no-singularities §5, black holes §3).
- **[SchiveChiuehBroadhurst2014]** H.-Y. Schive, T. Chiueh, T. Broadhurst, "Cosmic structure as the quantum interference of a coherent dark wave," Nature Physics 10, 496 (2014); and Schive et al., PRL 113, 261302 (2014). — The soliton core profile and the soliton–halo mass relation for an ultralight condensate. Used for the central-soliton radii and the Galactic-Centre mass pricing at the recorded ultralight mass (galactic atoms §1).
- **[PenroseOnsager1956]** O. Penrose, L. Onsager, "Bose–Einstein condensation and liquid helium," Phys. Rev. 104, 576 (1956). — Condensation defined by the largest eigenvalue of the one-body density matrix. That matrix's von Neumann entropy is the medium's entropy functional, whose vanishing is exactly the rank-one condition (entropy §1, arrow of time §4).
- **[Kraichnan1967]** R. H. Kraichnan, "Inertial ranges in two-dimensional turbulence," Phys. Fluids 10, 1417 (1967). — The dual cascade in two dimensions: energy to large scales, enstrophy to small. Used for the genesis cascade's spectral shape in the Kelvin-vertex work (T6).
