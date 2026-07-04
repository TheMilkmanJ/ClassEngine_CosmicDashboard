"""Affine-invariant ensemble sampler (Goodman & Weare 2010 stretch move).

Pure NumPy, no dependencies. Replaces fixed-covariance Metropolis: the
stretch move is invariant under affine transformations, so it handles the
curved/banana degeneracies of CMB posteriors (tau-A_s, omega_m-H0) without
any hand-tuned proposal covariance.
"""
import numpy as np


def run_ensemble(log_post_fn, x0, n_steps, n_walkers=None, a=2.0, rng=None,
                 progress_every=0, init_cov=None):
    """Sample log_post_fn starting near x0.

    Returns dict: samples (n_kept, d) flattened post-burn chain, logp values,
    acceptance rate, and the walker-shaped chain for R-hat style diagnostics.
    Burn-in = first half, discarded.
    """
    rng = np.random.default_rng() if rng is None else rng
    x0 = np.asarray(x0, dtype=float)
    ndim = x0.size
    n_walkers = n_walkers or max(4 * ndim, 32)
    if n_walkers % 2:
        n_walkers += 1

    # initialize walkers in a small ball; reject non-finite starts
    walkers = np.empty((n_walkers, ndim))
    logp = np.empty(n_walkers)
    # Overdispersed init: a tight ball needs many steps to decorrelate and
    # biases early covariance low. Use init_cov when available (production:
    # the Laplace covariance from the Forge Hessian); else a unit-scale ball.
    if init_cov is not None:
        # inflate so walkers start over-dispersed relative to the posterior
        L = 2.0 * np.linalg.cholesky(init_cov + 1e-12 * np.eye(ndim))
    else:
        L = None
    scale = np.abs(x0) + 1.0
    for k in range(n_walkers):
        for _ in range(200):
            if L is not None:
                trial = x0 + L @ rng.standard_normal(ndim)
            else:
                trial = x0 + scale * rng.standard_normal(ndim)
            lp = log_post_fn(trial)
            if np.isfinite(lp):
                walkers[k], logp[k] = trial, lp
                break
        else:
            raise ValueError("could not initialize walker in finite-logp region")

    chain = np.empty((n_steps, n_walkers, ndim))
    chain_logp = np.empty((n_steps, n_walkers))
    n_accept = 0
    half = n_walkers // 2

    for step in range(n_steps):
        for first in (True, False):
            sel = slice(0, half) if first else slice(half, n_walkers)
            oth = slice(half, n_walkers) if first else slice(0, half)
            S, O = walkers[sel], walkers[oth]
            ns = S.shape[0]
            z = ((a - 1.0) * rng.random(ns) + 1.0) ** 2 / a
            partners = O[rng.integers(0, O.shape[0], size=ns)]
            proposal = partners + z[:, None] * (S - partners)
            logp_prop = np.array([log_post_fn(p) for p in proposal])
            log_accept = (ndim - 1) * np.log(z) + logp_prop - logp[sel]
            accept = np.log(rng.random(ns)) < log_accept
            idx = np.arange(*sel.indices(n_walkers))[accept]
            walkers[idx] = proposal[accept]
            logp[idx] = logp_prop[accept]
            n_accept += accept.sum()
        chain[step] = walkers
        chain_logp[step] = logp
        if progress_every and (step + 1) % progress_every == 0:
            print(f"[ensemble] step {step+1}/{n_steps} "
                  f"acc={n_accept/((step+1)*n_walkers):.2f}", flush=True)

    burn = n_steps // 2
    kept = chain[burn:].reshape(-1, ndim)
    kept_logp = chain_logp[burn:].reshape(-1)
    return {"samples": kept, "logp": kept_logp,
            "acceptance": n_accept / (n_steps * n_walkers),
            "chain": chain[burn:], "chain_logp": chain_logp[burn:]}


def rhat(chain):
    """Gelman-Rubin R-hat per dimension from a (n_steps, n_walkers, d) chain,
    treating walkers as chains."""
    n, m, d = chain.shape
    means = chain.mean(axis=0)              # (m, d)
    grand = means.mean(axis=0)              # (d,)
    B = n / (m - 1) * np.sum((means - grand) ** 2, axis=0)
    W = chain.var(axis=0, ddof=1).mean(axis=0)
    var_hat = (n - 1) / n * W + B / n
    return np.sqrt(var_hat / np.maximum(W, 1e-300))
