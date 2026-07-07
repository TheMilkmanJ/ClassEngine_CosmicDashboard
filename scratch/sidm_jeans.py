import numpy as np
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

if __name__ == "__main__":
    r_arr = np.linspace(0.1, 10, 20)
    M_arr = get_sidm_mass_profile(r_arr, 1e7, 30.0, 5.0)
    V_c = np.sqrt(G * M_arr / r_arr)
    print("V_c:", V_c)
