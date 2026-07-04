"""Bridge-sampling evidence estimation for CosmicForge.

Replaces the truncated Gelfand-Dey estimator: bridge sampling (Meng & Wong
1996) is the statistically optimal member of the same estimator family, is
far more robust to non-Gaussian posteriors, and carries a computable error
estimate. A Bayes factor without an error bar is not evidence.

Cost note: unlike Gelfand-Dey, bridge sampling evaluates the unnormalized
log-posterior at N2 fresh proposal draws. With the 2026-07-03 CLASS speedups
(~seconds per call) N2 ~ 500-1000 is cheap and buys controlled accuracy.
"""
import numpy as np


def _fit_gaussian_proposal(samples, shrink=1.0):
    """Moment-matched Gaussian proposal, mildly shrunk toward the mean so the
    proposal has thinner tails than the posterior (keeps weights bounded)."""
    mean = np.mean(samples, axis=0)
    cov = np.cov(samples, rowvar=False)
    n = samples.shape[1]
    if cov.ndim == 0:
        cov = np.array([[float(cov)]])
    cov = shrink * cov + (1.0 - shrink) * np.diag(np.diag(cov))
    cov += np.eye(n) * 1e-10 * max(np.max(np.diag(cov)), 1e-10)
    return mean, cov


def _log_gauss(x, mean, cov_inv, logdet, n):
    d = x - mean
    maha = np.einsum('...i,ij,...j->...', d, cov_inv, d)
    return -0.5 * (n * np.log(2 * np.pi) + logdet + maha)


def bridge_sampling_logz(post_samples, post_logq, log_post_fn,
                         n_proposal=1000, max_iter=500, tol=1e-10,
                         rng=None):
    """Estimate ln Z with the iterative Meng-Wong bridge estimator.

    Parameters
    ----------
    post_samples : (N1, d) posterior samples (thinned MCMC output)
    post_logq    : (N1,) ln[ likelihood x prior ] at those samples
    log_post_fn  : callable x -> ln[ likelihood x prior ] (fresh evaluations
                   at proposal draws; the honest cost of the method)
    n_proposal   : number of proposal draws N2

    Returns dict: logz, logz_err (approximate RMSE), n_eff_post, diagnostics.
    """
    rng = np.random.default_rng() if rng is None else rng
    post_samples = np.atleast_2d(np.asarray(post_samples, dtype=float))
    post_logq = np.asarray(post_logq, dtype=float)
    N1, ndim = post_samples.shape

    mean, cov = _fit_gaussian_proposal(post_samples)
    cov_inv = np.linalg.inv(cov)
    sign, logdet = np.linalg.slogdet(cov)
    if sign <= 0:
        raise ValueError("proposal covariance not positive definite")

    prop = rng.multivariate_normal(mean, cov, size=n_proposal)
    prop_logq = np.array([log_post_fn(x) for x in prop])
    # Draws where q = 0 (outside prior/basin support) are LEGITIMATE zero-
    # weight terms in the proposal-side expectation. Discarding them would
    # silently renormalize g over the truncated region and bias Z.
    prop_logq = np.where(np.isfinite(prop_logq), prop_logq, -np.inf)
    N2 = len(prop)
    if np.sum(np.isfinite(prop_logq)) < 10:
        raise ValueError("proposal draws almost all landed outside support; "
                         "posterior/prior mismatch")

    # l = ln q(theta) - ln g(theta) on both sample sets
    l1 = post_logq - _log_gauss(post_samples, mean, cov_inv, logdet, ndim)
    l2 = prop_logq - _log_gauss(prop, mean, cov_inv, logdet, ndim)
    lstar = np.median(l1)          # numerical anchor
    s1 = N1 / (N1 + N2)
    s2 = N2 / (N1 + N2)
    
    from scipy.special import logsumexp
    logs1 = np.log(s1)
    logs2 = np.log(s2)
    l1_star = l1 - lstar
    l2_star = l2 - lstar

    # iterate r; r converges to Z/exp(lstar)
    logr = 0.0
    for _ in range(max_iter):
        log_num = logsumexp(l2_star - np.logaddexp(logs1 + l2_star, logs2 + logr)) - np.log(N2)
        log_den = logsumexp(-np.logaddexp(logs1 + l1_star, logs2 + logr)) - np.log(N1)
        logr_new = log_num - log_den
        if abs(logr_new - logr) < tol:
            logr = logr_new
            break
        logr = logr_new
    logz = logr + lstar

    # Approximate RMSE (Fruhwirth-Schnatter 2004): treat proposal side as iid,
    # posterior side with an effective sample size from autocorrelation of the
    # bridge integrand.
    f1 = np.exp(l2_star - np.logaddexp(logs1 + l2_star, logs2 + logr))
    f2 = np.exp(-np.logaddexp(logs1 + l1_star, logs2 + logr))
    n_eff = _ess_1d(f2)
    var_num = np.var(f1) / max(np.mean(f1) ** 2, 1e-300) / N2
    var_den = np.var(f2) / max(np.mean(f2) ** 2, 1e-300) / max(n_eff, 1.0)
    logz_err = float(np.sqrt(max(var_num + var_den, 0.0)))

    result = {"logz": float(logz), "logz_err": logz_err,
              "n_eff_post": float(n_eff), "n_proposal_used": int(N2),
              "proposal_mean": mean.tolist()}

    # Jackknife over posterior-sample blocks: an EMPIRICAL error that includes
    # walker/chain correlation the analytic formula cannot see. Uses only the
    # cached l1/l2 arrays (no fresh likelihood calls). Reported as
    # logz_err_jackknife; consumers should quote max(analytic, jackknife).
    n_blocks = min(32, max(8, N1 // 64))
    blocks = np.array_split(np.arange(N1), n_blocks)
    jk = []
    for bl in blocks:
        mask = np.ones(N1, dtype=bool); mask[bl] = False
        n1_j = int(mask.sum())
        s1_j = n1_j / (n1_j + N2)
        s2_j = N2 / (n1_j + N2)
        logs1_j = np.log(s1_j)
        logs2_j = np.log(s2_j)
        
        lr = 0.0
        l1_mask_star = l1_star[mask]
        for _ in range(200):
            log_num = logsumexp(l2_star - np.logaddexp(logs1_j + l2_star, logs2_j + lr)) - np.log(N2)
            log_den = logsumexp(-np.logaddexp(logs1_j + l1_mask_star, logs2_j + lr)) - np.log(n1_j)
            lr_new = log_num - log_den
            if abs(lr_new - lr) < 1e-9:
                lr = lr_new; break
            lr = lr_new
        jk.append(lr + lstar)
    jk = np.array(jk)
    result["logz_err_jackknife"] = float(np.sqrt((n_blocks - 1) / n_blocks
                                                 * np.sum((jk - jk.mean()) ** 2)))
    return result


def _ess_1d(x, max_lag=None):
    """Effective sample size of a 1-d series via initial-positive-sequence
    autocorrelation summation."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n < 8:
        return float(n)
    xc = x - x.mean()
    var = np.dot(xc, xc) / n
    if var <= 0:
        return float(n)
    max_lag = max_lag or min(n // 3, 1000)
    tau = 1.0
    for lag in range(1, max_lag):
        rho = np.dot(xc[:-lag], xc[lag:]) / ((n - lag) * var)
        if rho <= 0.0:
            break
        tau += 2.0 * rho
    return float(n / tau)


def combine_multimode_logz(mode_results):
    """Total evidence over well-separated modes: Z_tot = sum_k Z_k.

    mode_results: list of dicts from bridge_sampling_logz (one per mode).
    Errors combined in quadrature via linear Z-space weights.
    Returns dict with logz_total, logz_total_err, weights.
    """
    logzs = np.array([m["logz"] for m in mode_results])
    errs = np.array([
        max(m.get("logz_err", 0.0), m.get("logz_err_jackknife", 0.0))
        for m in mode_results
    ])
    lmax = logzs.max()
    w = np.exp(logzs - lmax)
    ztot = w.sum()
    logz_total = lmax + np.log(ztot)
    # dZ_tot^2 = sum (Z_k * dlogz_k)^2  -> dlogz_tot = sqrt(sum (w_k/ztot * err_k)^2)
    logz_total_err = float(np.sqrt(np.sum((w / ztot * errs) ** 2)))
    return {"logz_total": float(logz_total),
            "logz_total_err": logz_total_err,
            "mode_weights": (w / ztot).tolist()}


def basin_restricted(log_post_fn, centers, k, metric=None):
    """Restrict a multimodal log-posterior to the Voronoi basin of mode k.

    Z_total = sum_k Z_k over basin-restricted posteriors is EXACT for any
    mode separation (no overlap assumption): the basins partition the space.
    centers: (K, d) mode locations from the optimizer; metric: optional
    per-dimension scales for the distance (defaults to unit)."""
    import numpy as _np
    centers = _np.atleast_2d(_np.asarray(centers, dtype=float))
    if not 0 <= k < centers.shape[0]:
        raise ValueError("k must select one of the provided centers")
    scale = _np.ones(centers.shape[1]) if metric is None else _np.asarray(metric)
    if scale.shape != (centers.shape[1],) or _np.any(scale <= 0):
        raise ValueError("metric must contain positive per-dimension scales")

    def wrapped(x):
        d2 = _np.sum(((x - centers) / scale) ** 2, axis=1)
        if _np.argmin(d2) != k:
            return -_np.inf
        return log_post_fn(x)
    return wrapped
