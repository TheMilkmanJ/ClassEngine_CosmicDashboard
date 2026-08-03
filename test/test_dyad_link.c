/** @file test_dyad_link.c
 *
 * Unit test for the PRTOE "dyad link" electron-mass derivation added to
 * input_read_parameters_general() in source/input.c ("dcdf_dyad_link").
 *
 * This PR changed only the literal default values of the local variables
 * dyad_c, dyad_f_amp and dyad_Psi0 used inside that block (from the legacy
 * stack c=1.0, f_amp=0.6, Psi0=5.e16 GeV -> eps=1.232%, to the def541
 * "derived stack" c=0.9, f_amp=2/pi, Psi0=5.33073e16 GeV -> eps=1.2543%).
 * The formula itself (dyad_eps = dyad_c * dyad_f_amp * dyad_Psi0 / dyad_Mred)
 * and the parsing/override mechanism (class_read_double) are unchanged.
 *
 * Coverage:
 *   1) dcdf_dyad_link absent            -> behaviour is untouched (backward compat)
 *   2) dcdf_dyad_link = yes, no overrides -> uses the NEW default stack (~1.2543%)
 *   3) dcdf_dyad_link = yes, full override -> reproduces the OLD legacy default (~1.232%)
 *   4) dcdf_dyad_link = yes, partial override (only dyad_c) -> other defaults still apply
 *   5) dcdf_dyad_link = no              -> feature stays off (string must contain 'y'/'Y')
 *   6) dcdf_dyad_link = yes forces varconst_dep = varconst_instant even though
 *      'varying_fundamental_constants' was never set
 *   7) dcdf_dyad_link = yes enables density gate by default (model path)
 *   8) density gate: voids keep bare m_e; clusters screen to lab; recomb plateau full
 */

#include "class.h"
#include <math.h>

static int n_failures = 0;

#define CHECK_CLOSE(desc, got, expected, tol) do {                          \
    double _g = (got), _e = (expected), _t = (tol);                         \
    if (fabs(_g - _e) > _t) {                                               \
      fprintf(stderr, "FAIL: %s -- got %.10g, expected %.10g (tol %.3g)\n", \
              desc, _g, _e, _t);                                            \
      n_failures++;                                                         \
    } else {                                                                \
      fprintf(stdout, "PASS: %s (%.10g ~ %.10g)\n", desc, _g, _e);          \
    }                                                                       \
  } while (0)

#define CHECK_EQ_INT(desc, got, expected) do {                              \
    int _g = (int)(got), _e = (int)(expected);                              \
    if (_g != _e) {                                                         \
      fprintf(stderr, "FAIL: %s -- got %d, expected %d\n", desc, _g, _e);   \
      n_failures++;                                                         \
    } else {                                                                \
      fprintf(stdout, "PASS: %s (%d)\n", desc, _g);                        \
    }                                                                       \
  } while (0)

/* The def541 "derived stack" default constants baked into source/input.c. */
#define DYAD_C_DEFAULT      0.9
#define DYAD_F_AMP_DEFAULT  0.63661977
#define DYAD_PSI0_DEFAULT   5.33073e16
/* dyad_Mred is a fixed constant in the source (not overridable via .ini). */
#define DYAD_MRED           2.435e18

/* Write 'content' to the .ini file at 'path', then run CLASS's input parsing
 * (input_init) against it. Returns _SUCCESS_/_FAILURE_ exactly as input_init
 * would; on success the structs passed in are filled in with the resulting
 * background/thermodynamics parameters (background_init is NOT invoked -
 * this test only exercises parameter parsing/derivation, not the solver). */
static int run_input_init(const char *path, const char *content,
                           struct precision *ppr, struct background *pba,
                           struct thermodynamics *pth, struct perturbations *ppt,
                           struct transfer *ptr, struct primordial *ppm,
                           struct harmonic *phr, struct fourier *pfo,
                           struct lensing *ple, struct distortions *psd,
                           struct output *pop, ErrorMsg errmsg) {

  FILE *f = fopen(path, "w");
  if (f == NULL) {
    fprintf(stderr, "Could not open temp ini file %s for writing\n", path);
    return _FAILURE_;
  }
  fputs(content, f);
  fclose(f);

  char *argv[2];
  argv[0] = (char *)"test_dyad_link";
  argv[1] = (char *)path;

  return input_init(2, argv, ppr, pba, pth, ppt, ptr, ppm, phr, pfo, ple, psd, pop, errmsg);
}

int main(void) {

  struct precision pr;
  struct background ba;
  struct thermodynamics th;
  struct perturbations pt;
  struct transfer tr;
  struct primordial pm;
  struct harmonic hr;
  struct fourier fo;
  struct lensing le;
  struct distortions sd;
  struct output op;
  ErrorMsg errmsg;

  const char *ini_path = "test_dyad_link_tmp.ini";

  /* --- Case 1: dcdf_dyad_link not present at all -> defaults untouched --- */
  if (run_input_init(ini_path, "h = 0.67\n# no dyad-link parameters set\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 1): %s\n", errmsg);
    n_failures++;
  } else {
    CHECK_EQ_INT("dyad absent: varconst_dep stays varconst_none", ba.varconst_dep, varconst_none);
    CHECK_CLOSE("dyad absent: varconst_me stays 1.0", ba.varconst_me, 1.0, 1e-12);
    CHECK_EQ_INT("dyad absent: density_gate off", ba.varconst_density_gate, _FALSE_);
  }

  /* --- Case 2: dcdf_dyad_link = yes, no overrides -> def541 derived stack --- */
  if (run_input_init(ini_path, "dcdf_dyad_link = yes\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 2): %s\n", errmsg);
    n_failures++;
  } else {
    double expected_eps = DYAD_C_DEFAULT * DYAD_F_AMP_DEFAULT * DYAD_PSI0_DEFAULT / DYAD_MRED;
    CHECK_EQ_INT("dyad on (defaults): varconst_dep forced to varconst_instant",
                 ba.varconst_dep, varconst_instant);
    CHECK_CLOSE("dyad on (defaults): varconst_me = 1 + eps (derived stack)",
                ba.varconst_me, 1.0 + expected_eps, 1e-9);
    /* Cross-check against the documented headline number (P-040/P-041: 1.2543%),
     * with a loose tolerance since the doc quotes a rounded value. */
    CHECK_CLOSE("dyad on (defaults): eps matches the documented ~1.2543% shift",
                ba.varconst_me - 1.0, 0.012543, 5e-5);
  }

  /* --- Case 3: dcdf_dyad_link = yes with explicit overrides reproducing the
   *             pre-PR legacy default stack (documented as "+1.232% shift") --- */
  if (run_input_init(ini_path,
                      "dcdf_dyad_link = yes\n"
                      "dyad_c = 1.0\n"
                      "dyad_f_amp = 0.6\n"
                      "dyad_Psi0_GeV = 5.e16\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 3): %s\n", errmsg);
    n_failures++;
  } else {
    double expected_eps = 1.0 * 0.6 * 5.e16 / DYAD_MRED;
    CHECK_CLOSE("dyad on (full override = legacy stack): varconst_me = 1 + eps (~1.232%)",
                ba.varconst_me, 1.0 + expected_eps, 1e-9);
  }

  /* --- Case 4: dcdf_dyad_link = yes, partial override (only dyad_c) -> the
   *             other two knobs must still fall back to the NEW defaults --- */
  if (run_input_init(ini_path,
                      "dcdf_dyad_link = yes\n"
                      "dyad_c = 0.5\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 4): %s\n", errmsg);
    n_failures++;
  } else {
    double expected_eps = 0.5 * DYAD_F_AMP_DEFAULT * DYAD_PSI0_DEFAULT / DYAD_MRED;
    CHECK_CLOSE("dyad on (partial override dyad_c=0.5): varconst_me = 1 + eps",
                ba.varconst_me, 1.0 + expected_eps, 1e-9);
  }

  /* --- Case 5: dcdf_dyad_link = no -> the "contains y/Y" switch must stay off --- */
  if (run_input_init(ini_path, "dcdf_dyad_link = no\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 5): %s\n", errmsg);
    n_failures++;
  } else {
    CHECK_EQ_INT("dyad explicitly 'no': varconst_dep stays varconst_none", ba.varconst_dep, varconst_none);
    CHECK_CLOSE("dyad explicitly 'no': varconst_me stays 1.0", ba.varconst_me, 1.0, 1e-12);
  }

  /* --- Case 6: dcdf_dyad_link = yes must force varconst_instant even when
   *             'varying_fundamental_constants' was never set by the user --- */
  if (run_input_init(ini_path, "dcdf_dyad_link = Y\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 6): %s\n", errmsg);
    n_failures++;
  } else {
    CHECK_EQ_INT("dyad on (uppercase 'Y'): varconst_dep forced to varconst_instant",
                 ba.varconst_dep, varconst_instant);
  }

  /* --- Case 7: dcdf_dyad_link = yes enables the density gate by default --- */
  if (run_input_init(ini_path, "dcdf_dyad_link = yes\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 7): %s\n", errmsg);
    n_failures++;
  } else {
    CHECK_EQ_INT("dyad on: density_gate auto-enabled", ba.varconst_density_gate, _TRUE_);
    CHECK_EQ_INT("dyad on: dyad_link flag set", ba.dyad_link, _TRUE_);
    CHECK_CLOSE("dyad on: C_ref default 2", ba.varconst_C_ref, 2.0, 1e-12);
    CHECK_CLOSE("dyad on: gate_n default 4", ba.varconst_gate_n, 4.0, 1e-12);
  }

  /* --- Case 8: density gate physics via background_varconst_of_z[_delta] --- */
  if (run_input_init(ini_path,
                      "dcdf_dyad_link = yes\n"
                      "varying_transition_redshift = 50\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 8): %s\n", errmsg);
    n_failures++;
  } else {
    double alpha, me;
    double me0 = ba.varconst_me; /* 1+eps, full bare value */
    double S;

    /* Gate function: void load -> S=1; deep structure -> S~0 */
    S = background_varconst_gate_S(&ba, 0.0);
    CHECK_CLOSE("gate S(0) = 1 (void/smooth)", S, 1.0, 1e-12);
    S = background_varconst_gate_S(&ba, 100.0);
    CHECK_CLOSE("gate S(100) ~ 0 (cluster)", S, 0.0, 1e-6);

    /* Homogeneous path: recombination plateau (z=1100) keeps nearly full eps */
    if (background_varconst_of_z(&ba, 1100., &alpha, &me) == _FAILURE_) {
      fprintf(stderr, "background_varconst_of_z failed at z=1100\n");
      n_failures++;
    } else {
      CHECK_CLOSE("homogeneous z=1100: me ~ bare (1+eps)", me, me0, 1e-4);
    }

    /* Homogeneous path: today (z=0) screens to lab */
    if (background_varconst_of_z(&ba, 0., &alpha, &me) == _FAILURE_) {
      fprintf(stderr, "background_varconst_of_z failed at z=0\n");
      n_failures++;
    } else {
      CHECK_CLOSE("homogeneous z=0: me ~ lab (1.0)", me, 1.0, 1e-6);
    }

    /* Local path: void at z=0 keeps bare value (P-2026-007 void m_e-step) */
    if (background_varconst_of_z_delta(&ba, 0., -0.8, &alpha, &me) == _FAILURE_) {
      fprintf(stderr, "background_varconst_of_z_delta failed (void)\n");
      n_failures++;
    } else {
      CHECK_CLOSE("local void delta=-0.8 at z=0: me = bare (1+eps)", me, me0, 1e-9);
    }

    /* Local path: overdense cluster at z=0 screens to lab */
    if (background_varconst_of_z_delta(&ba, 0., 50.0, &alpha, &me) == _FAILURE_) {
      fprintf(stderr, "background_varconst_of_z_delta failed (cluster)\n");
      n_failures++;
    } else {
      CHECK_CLOSE("local cluster delta=50 at z=0: me ~ lab (1.0)", me, 1.0, 1e-6);
    }

    /* Explicit density_gate=no recovers legacy step when width=0 */
  }

  if (run_input_init(ini_path,
                      "dcdf_dyad_link = yes\n"
                      "varconst_density_gate = no\n"
                      "varying_transition_redshift = 50\n",
                      &pr, &ba, &th, &pt, &tr, &pm, &hr, &fo, &le, &sd, &op, errmsg) == _FAILURE_) {
    fprintf(stderr, "input_init failed (case 8b legacy): %s\n", errmsg);
    n_failures++;
  } else {
    double alpha, me;
    CHECK_EQ_INT("dyad + density_gate=no: gate off", ba.varconst_density_gate, _FALSE_);
    background_varconst_of_z(&ba, 100., &alpha, &me);
    CHECK_CLOSE("legacy step z=100: me = bare", me, ba.varconst_me, 1e-12);
    background_varconst_of_z(&ba, 10., &alpha, &me);
    CHECK_CLOSE("legacy step z=10: me = lab", me, 1.0, 1e-12);
  }

  remove(ini_path);

  if (n_failures > 0) {
    fprintf(stderr, "\n%d dyad-link check(s) FAILED\n", n_failures);
    return _FAILURE_;
  }

  fprintf(stdout, "\nAll dyad-link checks PASSED\n");
  return _SUCCESS_;
}