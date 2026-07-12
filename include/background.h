/** @file background.h Documented includes for background module */

#ifndef __BACKGROUND__
#define __BACKGROUND__

#include "common.h"
#include "quadrature.h"
#include "growTable.h"
#include "arrays.h"
#include "dei_rkck.h"
#include "parser.h"

/** list of possible parametrisations of the DE equation of state */

enum equation_of_state {CLP,EDE};


/** list of possible parametrizations of the varying fundamental constants */

enum varconst_dependence {varconst_none,varconst_instant};

/** list of formats for the vector of background quantities */

enum vecback_format {short_info, normal_info, long_info};

/** list of interpolation methods: search location in table either
    by bisection (inter_normal), or step by step starting from given
    index (inter_closeby) */

enum interpolation_method {inter_normal, inter_closeby};

/**
 * background structure containing all the background information that
 * other modules need to know.
 *
 * Once initialized by the backgound_init(), contains all necessary
 * information on the background evolution (except thermodynamics),
 * and in particular, a table of all background quantities as a
 * function of time and scale factor, used for interpolation in other
 * modules.
 */

struct background
{
  /** @name - input parameters initialized by user in input module
   *  (all other quantities are computed in this module, given these parameters
   *   and the content of the 'precision' structure)
   *
   * The background cosmological parameters listed here form a parameter
   * basis which is directly usable by the background module. Nothing
   * prevents from defining the input cosmological parameters
   * differently, and to pre-process them into this format, using the input
   * module (this might require iterative calls of background_init()
   * e.g. for dark energy or decaying dark matter). */

  //@{

  double H0; /**< \f$ H_0 \f$: Hubble parameter (in fact, [\f$H_0/c\f$]) in \f$ Mpc^{-1} \f$ */
  double h;  /**< reduced Hubble parameter */

  double Omega0_g; /**< \f$ \Omega_{0 \gamma} \f$: photons */
  double T_cmb;    /**< \f$ T_{cmb} \f$: current CMB temperature in Kelvins */

  double Omega0_b; /**< \f$ \Omega_{0 b} \f$: baryons */

  double Omega0_ur; /**< \f$ \Omega_{0 \nu r} \f$: ultra-relativistic neutrinos */

  double Omega0_cdm;      /**< \f$ \Omega_{0 cdm} \f$: cold dark matter */

  double Omega0_idm; /**< \f$ \Omega_{0 idm} \f$: interacting dark matter with photons, baryons, and idr */


  double Omega0_idr; /**< \f$ \Omega_{0 idr} \f$: interacting dark radiation */
  double T_idr;      /**< \f$ T_{idr} \f$: current temperature of interacting dark radiation in Kelvins */

  double Omega0_dcdmdr;   /**< \f$ \Omega_{0 dcdm}+\Omega_{0 dr} \f$: decaying cold dark matter (dcdm) decaying to dark radiation (dr) */
  double Omega_ini_dcdm;  /**< \f$ \Omega_{ini,dcdm} \f$: rescaled initial value for dcdm density (see 1407.2418 for definitions) */
  double Gamma_dcdm;      /**< \f$ \Gamma_{dcdm} \f$: decay constant for decaying cold dark matter */
  double tau_dcdm;

  int N_ncdm;                            /**< Number of distinguishable ncdm species */
  /* the following parameters help to define tabulated ncdm p-s-d passed in file */
  char * ncdm_psd_files;                 /**< list of filenames for tabulated p-s-d */
  int * got_files;                       /**< list of flags for each species, set to true if p-s-d is passed through file */
  /* the following parameters help to define the analytical ncdm phase space distributions (p-s-d) */
  double * ncdm_psd_parameters;          /**< list of parameters for specifying/modifying ncdm p.s.d.'s, to be customized for given model
                                            (could be e.g. mixing angles) */
  double * M_ncdm;                       /**< vector of masses of non-cold relic: dimensionless ratios m_ncdm/T_ncdm */
  double * m_ncdm_in_eV;                 /**< list of ncdm masses in eV (inferred from M_ncdm and other parameters above) */
  double * Omega0_ncdm, Omega0_ncdm_tot; /**< Omega0_ncdm for each species and for the total Omega0_ncdm */
  double * T_ncdm,T_ncdm_default;        /**< list of 1st parameters in p-s-d of non-cold relics: relative temperature
                                            T_ncdm1/T_gamma; and its default value */
  double * ksi_ncdm, ksi_ncdm_default;   /**< list of 2nd parameters in p-s-d of non-cold relics: relative chemical potential
                                            ksi_ncdm1/T_ncdm1; and its default value */
  double * deg_ncdm, deg_ncdm_default;    /**< vector of degeneracy parameters in factor of p-s-d: 1 for one family of neutrinos
                                             (= one neutrino plus its anti-neutrino, total g*=1+1=2, so deg = 0.5 g*); and its
                                             default value */
  int * ncdm_input_q_size; /**< Vector of numbers of q bins */
  double * ncdm_qmax;      /**< Vector of maximum value of q */

  double Omega0_k;         /**< \f$ \Omega_{0_k} \f$: curvature contribution */

  double Omega0_lambda;    /**< \f$ \Omega_{0_\Lambda} \f$: cosmological constant */
  double Omega0_fld;       /**< \f$ \Omega_{0 de} \f$: fluid */
  double Omega0_scf;       /**< \f$ \Omega_{0 scf} \f$: scalar field */
  short use_ppf; /**< flag switching on PPF perturbation equations instead of true fluid equations for perturbations. It could have been defined inside
                    perturbation structure, but we leave it here in such way to have all fld parameters grouped. */
  double c_gamma_over_c_fld; /**< ppf parameter defined in eq. (16) of 0808.3125 [astro-ph] */
  enum equation_of_state fluid_equation_of_state; /**< parametrisation scheme for fluid equation of state */
  double w0_fld;   /**< \f$ w0_{DE} \f$: current fluid equation of state parameter */
  double wa_fld;   /**< \f$ wa_{DE} \f$: fluid equation of state parameter derivative */
  double cs2_fld;  /**< \f$ c^2_{s~DE} \f$: sound speed of the fluid in the frame comoving with the fluid (so, this is
                      not [delta p/delta rho] in the synchronous or newtonian gauge!) */
  double Omega_EDE;        /**< \f$ wa_{DE} \f$: Early Dark Energy density parameter */
  double * scf_parameters; /**< list of parameters describing the scalar field potential */
  short attractor_ic_scf;  /**< whether the scalar field has attractor initial conditions */
  int scf_tuning_index;    /**< index in scf_parameters used for tuning */
  double phi_ini_scf;      /**< \f$ \phi(t_0) \f$: scalar field initial value */
  double phi_prime_ini_scf;/**< \f$ d\phi(t_0)/d\tau \f$: scalar field initial derivative wrt conformal time */
  int scf_parameters_size; /**< size of scf_parameters */
  double varconst_alpha; /**< finestructure constant for varying fundamental constants */
  double varconst_me; /**< electron mass for varying fundamental constants */
  enum varconst_dependence varconst_dep; /**< dependence of the varying fundamental constants as a function of time */
  double varconst_transition_redshift; /**< redshift of transition between varied fundamental constants and normal fundamental constants in the 'varconst_instant' case*/
  double varconst_z_high; /**< PRTOE dyad HIGH-z window edge (2026-07-10): above this
                              redshift the constants return to STANDARD -- the dyad
                              condensate is thermally DISORDERED above its T_c (electron-CW
                              radiative SSB, v ~ m_e[eps(L-1)/4pi^2]^(1/4) ~ 100 keV;
                              leptonic BBN exposure ~0.02-0.25 sigma, gate-0 CLEARS; see
                              docs/PRTOE_me_mechanism_math.md + ForClaude t214). The dyad
                              window is varconst_transition_redshift < z < varconst_z_high.
                              <=0 disables (default): plain varconst_instant step exactly. */

  /* ===== PRTOE v4 -- dCDF: single dark fluid unifying CDM+DE =====
   * See docs/PRTOE_v4_dCDF_derivation.md. Purely-kinetic k-essence,
   * exactly barotropic: w(rho) = -exp(-(s+beta*s^2)), s = ln(rho/rho_inf).
   * No gravity modification (contrast with v1-v3's F(phi)R coupling). */
  short use_dcdf;         /**< flag: replace cdm+lambda with the dCDF fluid */
  double Omega_ini_dcdf;  /**< dust-era abundance at a_ini (shooting unknown) */
  double Omega0_dcdf;     /**< target dCDF density fraction today (shooting target) */
  double dcdf_rho_inf;    /**< rho_infinity, de Sitter floor density, in H0^2 units */
  double dcdf_z_rad_onset; /**< PRTOE #17 conformal-origin phase: redshift above which
                                the dCDF acquires a w=1/3 (radiation-like) component,
                                so total w runs 1/3 -> 0 -> -1. <=0 disables it (default),
                                recovering the pure dust->deSitter fluid exactly.
                                DERIVED IDENTITY (2026-07-10, ForClaude t215/t216): z=4e7
                                <-> T ~ 9.4 keV is the H=m epoch of the fluid's own
                                dyad-amplitude-pinned mass m = 2.24e-20 eV -- i.e. the
                                textbook ULDM start-of-oscillation clock, T = sqrt(m*M_red/
                                0.61) = 9.41 keV (g*=3.36). Radiation-like above H~m, dust
                                below. NOT a condensation T_c (t182 charge dissolved). */
  int dcdf_deltam_mode; /**< what galaxies trace in delta_m/sigma8: 0 = fluid's full
                             density (floor in denominator), 1 = clustering part only
                             (delta rho over (1+w) rho, floor smooth by definition),
                             2 = baryons only (fluid excluded from delta_m) */

  /* PRTOE rotation-cancellation conversion (operator, 2026-07-09): as the twist
   * relaxes, the dcdf matter-part (rho - rho_inf) sheds to a free-streaming dark-
   * radiation component. Background-only (thermo untouched; the sigma8 effect rides
   * the depleted rho_dcdf through the existing dcdf perturbation sector). */
  double dcdf_conv_g;   /**< conversion strength: Gamma/H = g*shape(a); <=0 disables
                             (default), recovering the pure dust->deSitter fluid exactly */
  double dcdf_conv_at;  /**< conversion turn-on scale factor: shape=(a/at)^n/(1+(a/at)^n) */
  double dcdf_conv_n;   /**< conversion turn-on sharpness */

  /* PRTOE Route-D thawing floor (2026-07-10, ForClaude t217-223): the sequestered-Lambda
   * reading forces turnaround~now -> floor mass m_J ~ H0 -> the de Sitter floor THAWS,
   * 1+w_floor(a) = thaw * a^3 (standard thawing growth). Background-only deviation
   * component (the dcdf barotropic sector untouched), pre-registration branch Route-D
   * vs P-2026-018. Net prediction: w0 ~ -0.92..-0.86, wa ~ -0.2..-0.5, no true phantom. */
  double dcdf_floor_thaw; /**< 1+w of the floor TODAY (thaw*a^3 growth); <=0 disables
                              (default), recovering the exactly-constant floor (w=-1). */

  //@}


  /** @name - related parameters */

  //@{

  double age; /**< age in Gyears */
  double conformal_age; /**< conformal age in Mpc */
  double K; /**< \f$ K \f$: Curvature parameter \f$ K=-\Omega0_k*a_{today}^2*H_0^2\f$; */
  int sgnK; /**< K/|K|: -1, 0 or 1 */
  double Neff; /**< so-called "effective neutrino number", computed at earliest time in interpolation table */
  double Omega0_dcdm; /**< \f$ \Omega_{0 dcdm} \f$: decaying cold dark matter */
  double Omega0_dr; /**< \f$ \Omega_{0 dr} \f$: decay radiation */
  double Omega0_m;  /**< total non-relativistic matter today */
  double Omega0_r;  /**< total ultra-relativistic radiation today */
  double Omega0_de; /**< total dark energy density today, currently defined as 1 - Omega0_m - Omega0_r - Omega0_k */
  double Omega0_nfsm; /**< total non-free-streaming matter, that is, cdm, baryons and wdm */
  double a_eq;      /**< scale factor at radiation/matter equality */
  double H_eq;      /**< Hubble rate at radiation/matter equality [Mpc^-1] */
  double z_eq;      /**< redshift at radiation/matter equality */
  double tau_eq;    /**< conformal time at radiation/matter equality [Mpc] */

  //@}


  /** @name - all indices for the vector of background (=bg) quantities stored in table */

  //@{

  int index_bg_a;             /**< scale factor (in fact (a/a_0), see
                                 normalisation conventions explained
                                 at beginning of background.c) */
  int index_bg_H;             /**< Hubble parameter in \f$Mpc^{-1}\f$ */
  int index_bg_H_prime;       /**< its derivative w.r.t. conformal time */

  /* end of vector in short format, now quantities in normal format */

  int index_bg_rho_g;         /**< photon density */
  int index_bg_rho_b;         /**< baryon density */
  int index_bg_rho_cdm;       /**< cdm density */
  int index_bg_rho_idm;       /**< idm density */
  int index_bg_rho_lambda;    /**< cosmological constant density */
  int index_bg_rho_fld;       /**< fluid density */
  int index_bg_w_fld;         /**< fluid equation of state */
  int index_bg_rho_idr;       /**< density of interacting dark radiation */
  int index_bg_rho_ur;        /**< relativistic neutrinos/relics density */
  int index_bg_rho_dcdm;      /**< dcdm density */
  int index_bg_rho_dr;        /**< dr density */

  int index_bg_rho_dcdf;      /**< dCDF (PRTOE v4) fluid density */
  int index_bg_w_dcdf;        /**< dCDF equation of state w(rho) */
  int index_bg_cs2_dcdf;      /**< dCDF adiabatic sound speed squared, c_s^2(rho) */
  int index_bg_rho_dcdf_conv; /**< dCDF rotation-cancellation shed dark-radiation density */

  int index_bg_phi_scf;       /**< scalar field value */
  int index_bg_phi_prime_scf; /**< scalar field derivative wrt conformal time */
  int index_bg_V_scf;         /**< scalar field potential V */
  int index_bg_dV_scf;        /**< scalar field potential derivative V' */
  int index_bg_ddV_scf;       /**< scalar field potential second derivative V'' */
  int index_bg_rho_scf;       /**< scalar field energy density */
  int index_bg_p_scf;         /**< scalar field pressure */
  int index_bg_p_prime_scf;         /**< scalar field pressure */

  int index_bg_rho_ncdm1;     /**< density of first ncdm species (others contiguous) */
  int index_bg_p_ncdm1;       /**< pressure of first ncdm species (others contiguous) */
  int index_bg_pseudo_p_ncdm1;/**< another statistical momentum useful in ncdma approximation */

  int index_bg_rho_tot;       /**< Total density */
  int index_bg_p_tot;         /**< Total pressure */
  int index_bg_p_tot_prime;   /**< Conf. time derivative of total pressure */

  int index_bg_Omega_r;       /**< relativistic density fraction (\f$ \Omega_{\gamma} + \Omega_{\nu r} \f$) */

  /* end of vector in normal format, now quantities in long format */

  int index_bg_rho_crit;      /**< critical density */
  int index_bg_Omega_m;       /**< non-relativistic density fraction (\f$ \Omega_b + \Omega_cdm + \Omega_{\nu nr} \f$) */
  int index_bg_conf_distance; /**< conformal distance (from us) in Mpc */
  int index_bg_ang_distance;  /**< angular diameter distance in Mpc */
  int index_bg_lum_distance;  /**< luminosity distance in Mpc */
  int index_bg_time;          /**< proper (cosmological) time in Mpc */
  int index_bg_rs;            /**< comoving sound horizon in Mpc */

  int index_bg_D;             /**< scale independent growth factor D(a) for CDM perturbations */
  int index_bg_f;             /**< corresponding velocity growth factor [dlnD]/[dln a] */

  int index_bg_varc_alpha;    /**< value of fine structure constant in varying fundamental constants */
  int index_bg_varc_me;      /**< value of effective electron mass in varying fundamental constants */

  int bg_size_short;  /**< size of background vector in the "short format" */
  int bg_size_normal; /**< size of background vector in the "normal format" */
  int bg_size;        /**< size of background vector in the "long format" */

  //@}


  /** @name - background interpolation tables */

  //@{

  int bt_size;               /**< number of lines (i.e. time-steps) in the four following array */
  double * loga_table;       /**< vector loga_table[index_loga] with values of log(a) (in fact \f$ log(a/a0) \f$, logarithm of relative scale factor compared to today) */
  double * tau_table;        /**< vector tau_table[index_loga] with values of conformal time \f$ \tau \f$ (in fact \f$ a_0 c tau \f$, see normalisation conventions explained at beginning of background.c) */
  double * z_table;          /**< vector z_table[index_loga] with values of \f$ z \f$ (redshift) */
  double * background_table; /**< table background_table[index_tau*pba->bg_size+pba->index_bg] with all other quantities (array of size bg_size*bt_size) **/

  //@}


  /** @name - table of their second derivatives, used for spline interpolation */

  //@{

  double * d2tau_dz2_table; /**< vector d2tau_dz2_table[index_loga] with values of \f$ d^2 \tau / dz^2 \f$ (conformal time) */
  double * d2z_dtau2_table; /**< vector d2z_dtau2_table[index_loga] with values of \f$ d^2 z / d\tau^2 \f$ (conformal time) */
  double * d2background_dloga2_table; /**< table d2background_dtau2_table[index_loga*pba->bg_size+pba->index_bg] with values of \f$ d^2 b_i / d\log(a)^2 \f$ */

  //@}


  /** @name - all indices for the vector of background quantities to be integrated (=bi)
   *
   * Most background quantities can be immediately inferred from the
   * scale factor. Only few of them require an integration with
   * respect to conformal time (in the minimal case, only one quantity needs to
   * be integrated with time: the scale factor, using the Friedmann
   * equation). These indices refer to the vector of
   * quantities to be integrated with time.
   * {B} quantities are needed by background_functions() while {C} quantities are not.
   */

  //@{

  int index_bi_rho_dcdm;/**< {B} dcdm density */
  int index_bi_rho_dr;  /**< {B} dr density */
  int index_bi_rho_fld; /**< {B} fluid density */
  int index_bi_rho_dcdf;/**< {B} dCDF (PRTOE v4) fluid density */
  int index_bi_rho_dcdf_conv;/**< {B} dCDF rotation-cancellation shed dark-radiation density */
  int index_bi_phi_scf;       /**< {B} scalar field value */
  int index_bi_phi_prime_scf; /**< {B} scalar field derivative wrt conformal time */

  int index_bi_time;    /**< {C} proper (cosmological) time in Mpc */
  int index_bi_rs;      /**< {C} sound horizon */
  int index_bi_tau;     /**< {C} conformal time in Mpc */
  int index_bi_D;       /**< {C} scale independent growth factor D(a) for CDM perturbations. */
  int index_bi_D_prime; /**< {C} D satisfies \f$ [D''(\tau)=-aHD'(\tau)+3/2 a^2 \rho_M D(\tau) \f$ */

  int bi_B_size;        /**< Number of {B} parameters */
  int bi_size;          /**< Number of {B}+{C} parameters */

  //@}

  /** @name - flags describing the absence or presence of cosmological
      ingredients
      *
      * having one of these flag set to zero allows to skip the
      * corresponding contributions, instead of adding null contributions.
      */


  //@{

  short has_cdm;       /**< presence of cold dark matter? */
  short has_idm;       /**< presence of interacting dark matter with photons, baryons, and idr */
  short has_dcdm;      /**< presence of decaying cold dark matter? */
  short has_dr;        /**< presence of relativistic decay radiation? */
  short has_scf;       /**< presence of a scalar field? */
  short has_ncdm;      /**< presence of non-cold dark matter? */
  short has_lambda;    /**< presence of cosmological constant? */
  short has_fld;       /**< presence of fluid with constant w and cs2? */
  short has_dcdf;      /**< presence of the PRTOE v4 dCDF unified dark fluid? */
  short has_ur;
    /* DUMMIES to make perturbations.c compile */
    short use_prtoe;
    int index_bg_phi_prtoe;
    int index_bg_dphi_prtoe;
    int index_bg_rho_prtoe;
    int index_bg_p_prtoe;
    double zeta_prtoe;
    double xi_prtoe;
    double lambda_prtoe;
    double V0_prtoe;
    double m_prtoe;
    double dphi_prtoe_ini;
        /**< presence of ultra-relativistic neutrinos/relics? */
  short has_idr;       /**< presence of interacting dark radiation? */
  short has_curvature; /**< presence of global spatial curvature? */
  short has_varconst;  /**< presence of varying fundamental constants? */

  //@}


  /**
   *@name - arrays related to sampling and integration of ncdm phase space distributions
   */

  //@{

  int * ncdm_quadrature_strategy; /**< Vector of integers according to quadrature strategy. */
  double ** q_ncdm_bg;  /**< Pointers to vectors of background sampling in q */
  double ** w_ncdm_bg;  /**< Pointers to vectors of corresponding quadrature weights w */
  double ** q_ncdm;     /**< Pointers to vectors of perturbation sampling in q */
  double ** w_ncdm;     /**< Pointers to vectors of corresponding quadrature weights w */
  double ** dlnf0_dlnq_ncdm; /**< Pointers to vectors of logarithmic derivatives of p-s-d */
  int * q_size_ncdm_bg; /**< Size of the q_ncdm_bg arrays */
  int * q_size_ncdm;    /**< Size of the q_ncdm arrays */
  double * factor_ncdm; /**< List of normalization factors for calculating energy density etc.*/

  //@}

  /** @name - technical parameters */

  //@{

  short shooting_failed;  /**< flag is set to true if shooting failed. */
  ErrorMsg shooting_error; /**< Error message from shooting failed. */

  short background_verbose; /**< flag regulating the amount of information sent to standard output (none if set to zero) */

  ErrorMsg error_message; /**< zone for writing error messages */

  short is_allocated; /**< flag is set to true if allocated */
  //@}
};


/**
 * temporary parameters and workspace passed to the background_derivs function
 */

struct background_parameters_and_workspace {

  /* structures containing fixed input parameters (indices, ...) */
  struct background * pba;

  /* workspace */
  double * pvecback;

};

/**
 * temporary parameters and workspace passed to phase space distribution function
 */

struct background_parameters_for_distributions {

  /* structures containing fixed input parameters (indices, ...) */
  struct background * pba;

  /* Additional parameters */

  /* Index of current distribution function */
  int n_ncdm;

  /* Used for interpolating in file of tabulated p-s-d: */
  int tablesize;
  double *q;
  double *f0;
  double *d2f0;
  int last_index;

};

/**************************************************************/
/* @cond INCLUDE_WITH_DOXYGEN */
/*
 * Boilerplate for C++
 */
#ifdef __cplusplus
extern "C" {
#endif

  int background_at_z(
                      struct background *pba,
                      double a_rel,
                      enum vecback_format return_format,
                      enum interpolation_method inter_mode,
                      int * last_index,
                      double * pvecback
                      );

  int background_at_tau(
                        struct background *pba,
                        double tau,
                        enum vecback_format return_format,
                        enum interpolation_method inter_mode,
                        int * last_index,
                        double * pvecback
                        );

  int background_tau_of_z(
                          struct background *pba,
                          double z,
                          double * tau
                          );

  int background_z_of_tau(
                          struct background *pba,
                          double tau,
                          double * z
                          );

  int background_functions(
                           struct background *pba,
                           double a_rel,
                           double * pvecback_B,
                           enum vecback_format return_format,
                           double * pvecback
                           );

  int background_w_fld(
                       struct background * pba,
                       double a,
                       double * w_fld,
                       double * dw_over_da_fld,
                       double * integral_fld);

  int background_varconst_of_z(
                               struct background* pba,
                               double z,
                               double* alpha,
                               double* me
                               );

  int background_init(
                      struct precision *ppr,
                      struct background *pba
                      );

  int background_free(
                      struct background *pba
                      );

  int background_free_noinput(
                              struct background *pba
                              );

  int background_free_input(
                            struct background *pba
                            );

  int background_indices(
                         struct background *pba
                         );

  int background_ncdm_distribution(
                                   void *pba,
                                   double q,
                                   double * f0
                                   );

  int background_ncdm_test_function(
                                    void *pba,
                                    double q,
                                    double * test
                                    );

  int background_ncdm_init(
                           struct precision *ppr,
                           struct background *pba
                           );

  int background_ncdm_momenta(
                              double * qvec,
                              double * wvec,
                              int qsize,
                              double M,
                              double factor,
                              double z,
                              double * n,
                              double * rho,
                              double * p,
                              double * drho_dM,
                              double * pseudo_p
                              );

  int background_ncdm_M_from_Omega(
                                   struct precision *ppr,
                                   struct background *pba,
                                   int species
                                   );

  int background_checks(
                        struct precision * ppr,
                        struct background *pba
                        );

  int background_solve(
                       struct precision *ppr,
                       struct background *pba
                       );

  int background_initial_conditions(
                                    struct precision *ppr,
                                    struct background *pba,
                                    double * pvecback,
                                    double * pvecback_integration,
                                    double * loga_ini
                                    );

  int background_find_equality(
                               struct precision *ppr,
                               struct background *pba
                               );


  int background_output_titles(struct background * pba,
                               char titles[_MAXTITLESTRINGLENGTH_]
                               );

  int background_output_data(
                             struct background *pba,
                             int number_of_titles,
                             double *data);

  int background_derivs(
                        double loga,
                        double * y,
                        double * dy,
                        void * parameters_and_workspace,
                        ErrorMsg error_message
                        );

  int background_sources(
                         double loga,
                         double * y,
                         double * dy,
                         int index_loga,
                         void * parameters_and_workspace,
                         ErrorMsg error_message
                         );

  int background_timescale(
                           double loga,
                           void * parameters_and_workspace,
                           double * timescale,
                           ErrorMsg error_message
                           );

  int background_output_budget(
                               struct background* pba
                               );

  /** Scalar field potential and its derivatives **/
  double V_scf(
               struct background *pba,
               double phi
               );

  double dV_scf(
                struct background *pba,
                double phi
                );

  double ddV_scf(
                 struct background *pba,
                 double phi
                 );

  /** Coupling between scalar field and matter **/
  double Q_scf(
               struct background *pba,
               double phi,
               double phi_prime
               );

#ifdef __cplusplus
}
#endif

/**************************************************************/

/**
 * @name Some conversion factors and fundamental constants needed by background module:
 */

//@{

#define _Mpc_over_m_ 3.085677581282e22  /**< conversion factor from meters to megaparsecs */
/* remark: CAMB uses 3.085678e22: good to know if you want to compare  with high accuracy */

#define _Gyr_over_Mpc_ 3.06601394e2 /**< conversion factor from megaparsecs to gigayears
                                       (c=1 units, Julian years of 365.25 days) */
#define _c_ 2.99792458e8            /**< c in m/s */
#define _G_ 6.67428e-11             /**< Newton constant in m^3/Kg/s^2 */
#define _eV_ 1.602176487e-19        /**< 1 eV expressed in J */

/* parameters entering in Stefan-Boltzmann constant sigma_B */
#define _k_B_ 1.3806504e-23
#define _h_P_ 6.62606896e-34
/* remark: sigma_B = 2 pi^5 k_B^4 / (15h^3c^2) = 5.670400e-8
   = Stefan-Boltzmann constant in W/m^2/K^4 = Kg/K^4/s^3 */

//@}

/**
 * @name Some limits on possible background parameters
 */

//@{

#define _h_BIG_ 1.5            /**< maximal \f$ h \f$ */
#define _h_SMALL_ 0.3         /**< minimal \f$ h \f$ */
#define _omegab_BIG_ 0.039    /**< maximal \f$ omega_b \f$ */
#define _omegab_SMALL_ 0.005  /**< minimal \f$ omega_b \f$ */

//@}

/**
 * @name Some limits imposed in other parts of the module:
 */

//@{

#define _SCALE_BACK_ 0.1  /**< logarithmic step used when searching
                             for an initial scale factor at which ncdm
                             are still relativistic */

#define _PSD_DERIVATIVE_EXP_MIN_ -30 /**< for ncdm, for accurate computation of dlnf0/dlnq, q step is varied in range specified by these parameters */
#define _PSD_DERIVATIVE_EXP_MAX_ 2  /**< for ncdm, for accurate computation of dlnf0/dlnq, q step is varied in range specified by these parameters */

#define _zeta3_ 1.2020569031595942853997381615114499907649862923404988817922 /**< for quandrature test function */
#define _zeta5_ 1.0369277551433699263313654864570341680570809195019128119741 /**< for quandrature test function */

//@}

/* ===== PRTOE v4 -- dCDF equation of state and sound speed =====
 * See docs/PRTOE_v4_dCDF_derivation.md eq. (9)-(10). s = ln(rho/rho_inf) is
 * clamped at 0 (i.e. rho/rho_inf clamped at 1 before the log) to guard
 * against numerical overshoot below the de Sitter fixed point: the
 * continuity equation has an exact fixed point at rho=rho_inf (w=-1 there),
 * approached asymptotically from above and never crossed in exact
 * integration, but finite-step integrators can overshoot slightly. */
static inline double dcdf_s_of_rho(struct background *pba, double rho) {
  double ratio = rho / MAX(pba->dcdf_rho_inf, 1e-300);
  return log(MAX(ratio, 1.0));
}

static inline double w_dcdf(struct background *pba, double rho) {
  double s = dcdf_s_of_rho(pba, rho);
  return -exp(-s); /* == -rho_inf/rho: p = -rho_inf exactly (LCDM-form background) */
}

/* beta (the eq.-9 barotropic shape parameter) was removed 2026-07-05 (v5):
 * the honest-pipeline MCMC drove beta -> 0 (log10beta ~ -8 at best fit) and
 * every beta > 1e-6 only destroyed sigma8 (0.827 -> 0.185 at 1e-4). With
 * beta == 0 the adiabatic sound speed dp/drho is identically zero. */
static inline double cs2_dcdf(struct background *pba, double rho) {
  (void)pba; (void)rho;
  return 0.0;
}

/* [REMOVED 2026-07-09] The v6 "environmental coupling" sandbox (dcdf_w_env +
 * dcdf_xe_saha, knobs c_gamma / c_EM) is deleted as census-illegal, not merely
 * disabled. c_EM coupled the medium to free-electron / ionization density -- the
 * EM (matter-matter) sector the medium provably has no account in (L1a, the
 * birefringence null). c_gamma coupled it to the photon density specifically,
 * violating L1 identity-blindness (gravity reads total w/energy, it cannot single
 * out photons). Both were off in every config and drove nothing. A legal
 * environmental coupling, if ever wanted, must read total energy / H, not a
 * species. See docs/laws_and_rules/README.md. */

/* PRTOE #17 conformal-origin radiation. A SEPARATE, background-only dark-radiation
 * energy density active above z_rad_onset, so the total dCDF-associated energy
 * redshifts ~a^-4 (radiation) -> a^-3 (dust) -> const (de Sitter): the equation
 * of state runs 1/3 -> 0 -> -1. By design it drives ONLY the expansion -- it is
 * added to rho_tot / p_tot / rho_r (like any relativistic species) and is
 * DELIBERATELY NOT folded into w_dcdf, rho_m, or the dcdf perturbation sector:
 * radiation has pressure support and must not bleed into clustering/structure.
 * The amplitude is DERIVED from the fluid's own abundance (Omega_ini_dcdf) and is
 * continuous with the dust density at the onset -- no free amplitude knob, only
 * z_rad_onset. f(a) = x^2/(1+x^2), x = a_onset/a: ->1 early, ->0 late.
 * dcdf_z_rad_onset <= 0 disables it, recovering the pure dust->deSitter fluid. */
/* [2026-07-12 THE DISPERSION UPGRADE, derivation-hunt sweep 1] The phenomenological
 * ramp x^2/(1+x^2) is REPLACED by the DERIVED single-mode shape: the winding is one
 * comoving mode, so its energy is the exact massive dispersion rho ~ omega(a)/a^3,
 * omega = sqrt(m^2 + (k/a)^2), normalized to the dust density late. With x = a_on/a
 * (a_on = the H=m clock, now EXACTLY the fit parameter -- the fit-vs-clock offset
 * dissolves by construction): total/dust = sqrt(1+x^2), i.e. the EXTRA (radiation-like)
 * part is dust*(sqrt(1+x^2)-1). Pressure exact: p_extra = dust * x^2/(3*sqrt(1+x^2)).
 * Old-template chains (pre-2026-07-12) carry the old shape; do not resume them. */
static inline double dcdf_rho_rad(struct background *pba, double a) {
  if (pba->dcdf_z_rad_onset <= 0.0) return 0.0;
  double a_on = 1.0 / (1.0 + pba->dcdf_z_rad_onset);
  double x = a_on / MAX(a, 1e-300);
  double dust = pba->Omega_ini_dcdf * pba->H0 * pba->H0 / (a*a*a);
  return dust * (sqrt(1.0 + x*x) - 1.0);
}
static inline double dcdf_p_rad(struct background *pba, double a) {
  if (pba->dcdf_z_rad_onset <= 0.0) return 0.0;
  double a_on = 1.0 / (1.0 + pba->dcdf_z_rad_onset);
  double x = a_on / MAX(a, 1e-300);
  double dust = pba->Omega_ini_dcdf * pba->H0 * pba->H0 / (a*a*a);
  return dust * x*x / (3.0 * sqrt(1.0 + x*x));
}
static inline double dcdf_dpdloga_rad(struct background *pba, double a) {
  if (pba->dcdf_z_rad_onset <= 0.0) return 0.0;
  double a_on = 1.0 / (1.0 + pba->dcdf_z_rad_onset);
  double x = a_on / MAX(a, 1e-300);
  double dust = pba->Omega_ini_dcdf * pba->H0 * pba->H0 / (a*a*a);
  double s = sqrt(1.0 + x*x);
  /* d/dlna of p_extra: -(dust)*( x^2/s + x^2*(2+x^2)/(3*s^3) ) */
  return -dust * ( x*x/s + x*x*(2.0 + x*x)/(3.0*s*s*s) );
}

/* PRTOE rotation-cancellation conversion rate Gamma/H (dimensionless, per dln a).
 * The twist relaxes -> the dcdf matter-part sheds to free-streaming dark radiation.
 * shape(a) = x^n/(1+x^n), x=a/at: ->0 early, ->1 late (turns on near at). This is the
 * fraction-per-e-fold of the matter-part that converts. dcdf_conv_g<=0 disables it,
 * recovering the pure dust->deSitter fluid exactly (backward compatible). */
static inline double dcdf_conv_rate(struct background *pba, double a) {
  if (pba->dcdf_conv_g <= 0.0) return 0.0;
  double x = a / MAX(pba->dcdf_conv_at, 1e-300);
  double xn = pow(x, pba->dcdf_conv_n);
  return pba->dcdf_conv_g * xn / (1.0 + xn);
}

/* PRTOE Route-D thawing floor: 1+w_floor(a) = thaw * a^3 (thawing growth), normalized so
 * rho_floor(a=1) = rho_inf. rho_floor(a) = rho_inf * exp(thaw*(1-a^3)) (decreasing).
 * Implemented as a background-only DEVIATION component (like dcdf_rho_rad):
 *   E(a)   = rho_floor(a) - rho_inf                              (>=0 for a<1, ->0 today)
 *   P_E(a) = (-1 + thaw*a^3) * rho_floor(a) + rho_inf            (floor pressure minus the
 *                                                                  constant part already in
 *                                                                  the barotropic sector)
 *   dP_E/dlna = 3*thaw*a^3 * rho_floor(a) * (2 - thaw*a^3)
 * Added to rho_tot / p_tot / dp_dloga ONLY (DE-like: not rho_m, not rho_r, no perturbation
 * sector). dcdf_floor_thaw <= 0 disables it: the exactly-constant floor is recovered. */
static inline double dcdf_floor_rho(struct background *pba, double a) {
  if (pba->dcdf_floor_thaw <= 0.0) return pba->dcdf_rho_inf;
  double a3 = a*a*a;
  return pba->dcdf_rho_inf * exp(pba->dcdf_floor_thaw * (1.0 - a3));
}

#endif
/* @endcond */
