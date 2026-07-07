import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

G = 4.30091e-6 # kpc/M_sun (km/s)^2

def isothermal_jeans_ode(r, y, sigma0):
    ln_rho, M = y
    rho = np.exp(ln_rho)
    dlnrho_dr = - G * M / (sigma0**2 * r**2)
    dM_dr = 4 * np.pi * r**2 * rho
    return [dlnrho_dr, dM_dr]

def integrate_isothermal(rho0, sigma0, r1):
    r_start = 1e-5
    M_start = (4.0/3.0) * np.pi * r_start**3 * rho0
    ln_rho_start = np.log(rho0)
    
    sol = solve_ivp(isothermal_jeans_ode, [r_start, r1], [ln_rho_start, M_start], 
                    args=(sigma0,), method='Radau', rtol=1e-8, atol=1e-10)
    
    return np.exp(sol.y[0, -1]), sol.y[1, -1]

def get_nfw_params(rho_r1, M_r1, r1):
    target = M_r1 / (4 * np.pi * rho_r1 * r1**3)
    if target <= 0.5:
        return None, None
        
    def match_eq(x):
        return (1+x)**2 / x**2 * (np.log(1+x) - x/(1+x)) - target
        
    res = root_scalar(match_eq, bracket=[1e-5, 1e5], method='brentq')
    x = res.root
    r_s = r1 / x
    rho_s = rho_r1 * x * (1+x)**2
    return rho_s, r_s

def get_sidm_mass_profile(r_arr, rho0, sigma0, r1):
    rho_r1, M_r1 = integrate_isothermal(rho0, sigma0, r1)
    rho_s, r_s = get_nfw_params(rho_r1, M_r1, r1)
    if rho_s is None:
        return None
        
    M_out = np.zeros_like(r_arr)
    # inner
    mask_in = r_arr <= r1
    if np.any(mask_in):
        sol = solve_ivp(isothermal_jeans_ode, [1e-5, r1], [np.log(rho0), 0.0], 
                    t_eval=np.maximum(r_arr[mask_in], 1e-5),
                    args=(sigma0,), method='Radau', rtol=1e-8, atol=1e-10)
        M_out[mask_in] = sol.y[1]
        
    # outer
    mask_out = r_arr > r1
    if np.any(mask_out):
        x = r_arr[mask_out] / r_s
        x1 = r1 / r_s
        M_nfw_r1 = 4 * np.pi * rho_s * r_s**3 * (np.log(1+x1) - x1/(1+x1))
        M_nfw_r = 4 * np.pi * rho_s * r_s**3 * (np.log(1+x) - x/(1+x))
        # Ensure continuity
        M_out[mask_out] = M_r1 + (M_nfw_r - M_nfw_r1)
        
    return M_out

def objective(theta, r_data, v_data, err_data):
    log_rho0, sigma0, r1 = theta
    rho0 = 10**log_rho0
    
    if not (6 < log_rho0 < 10) or not (10 < sigma0 < 100) or not (0.1 < r1 < 20):
        return 1e10
        
    try:
        M_arr = get_sidm_mass_profile(r_data, rho0, sigma0, r1)
        if M_arr is None:
            return 1e10
        v_model = np.sqrt(G * M_arr / r_data)
        
        # Calculate chi-squared
        chi2 = np.sum(((v_model - v_data) / err_data)**2)
        return chi2
    except:
        return 1e10

def fit_galaxy(r_data, v_data, err_data, name="Galaxy", p0=[8.0, 40.0, 2.0]):
    print(f"Fitting {name}...")
    
    res = minimize(objective, p0, args=(r_data, v_data, err_data), method='Nelder-Mead', options={'maxiter': 300, 'disp': True})
    
    best_fit = res.x
    log_rho0, sigma0, r1 = best_fit
    rho0 = 10**log_rho0
    
    v_avg = (4.0 / np.sqrt(np.pi)) * sigma0
    t_age_s = 10 * 3.154e16
    rho_r1, _ = integrate_isothermal(rho0, sigma0, r1)
    rho_r1_cgs = rho_r1 * 1.989e33 / (3.086e21)**3 # g / cm^3
    v_avg_cgs = v_avg * 1e5 # cm/s
    sigma_over_m = 1.0 / (rho_r1_cgs * v_avg_cgs * t_age_s)
    
    print(f"{name} Best Fit: log_rho0={log_rho0:.2f}, sigma0={sigma0:.1f} km/s, r1={r1:.2f} kpc")
    print(f"{name} Inferred sigma/m: {sigma_over_m:.2f} cm^2/g at <v>={v_avg:.1f} km/s")
    print("-" * 40)
    
if __name__ == "__main__":
    r_data = np.linspace(0.5, 10.0, 15)
    
    # Galaxy A (Cored, shallow)
    # We generated it with 1e7, 30.0, 5.0
    M_arr_A = get_sidm_mass_profile(r_data, rho0=1e7, sigma0=30.0, r1=5.0)
    v_data_A = np.sqrt(G * M_arr_A / r_data) + np.random.randn(15) * 0.5
    err_A = np.ones(15) * 1.0
    
    # Galaxy B (Dense, cuspy)
    # We generated it with 1e8, 30.0, 5.0
    M_arr_B = get_sidm_mass_profile(r_data, rho0=1e8, sigma0=30.0, r1=5.0)
    v_data_B = np.sqrt(G * M_arr_B / r_data) + np.random.randn(15) * 0.5
    err_B = np.ones(15) * 1.0
    
    fit_galaxy(r_data, v_data_A, err_A, "Galaxy A (Cored)", p0=[7.0, 30.0, 5.0])
    fit_galaxy(r_data, v_data_B, err_B, "Galaxy B (Dense)", p0=[8.0, 30.0, 5.0])
