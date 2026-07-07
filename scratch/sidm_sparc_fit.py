import numpy as np
from scipy.optimize import minimize
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import os

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
                    args=(sigma0,), method='RK45', rtol=1e-8, atol=1e-10)
    
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
                    args=(sigma0,), method='RK45', rtol=1e-8, atol=1e-10)
        M_out[mask_in] = sol.y[1]
        
    # outer
    mask_out = r_arr > r1
    if np.any(mask_out):
        x = r_arr[mask_out] / r_s
        x1 = r1 / r_s
        M_nfw_r1 = 4 * np.pi * rho_s * r_s**3 * (np.log(1+x1) - x1/(1+x1))
        M_nfw_r = 4 * np.pi * rho_s * r_s**3 * (np.log(1+x) - x/(1+x))
        M_out[mask_out] = M_r1 + (M_nfw_r - M_nfw_r1)
        
    return M_out

def objective(theta, r_data, v_data, err_data, v_gas, v_disk, v_bul):
    log_rho0, sigma0, r1, Y_disk, Y_bul = theta
    rho0 = 10**log_rho0
    
    if not (6 < log_rho0 < 11) or not (10 < sigma0 < 400) or not (0.1 < r1 < 100):
        return 1e10
    if not (0.2 < Y_disk < 1.2) or not (0.2 < Y_bul < 1.2):
        return 1e10
        
    try:
        M_arr = get_sidm_mass_profile(r_data, rho0, sigma0, r1)
        if M_arr is None:
            return 1e10
        
        # Total velocity squared = DM + Baryons
        v_DM_sq = G * M_arr / r_data
        v_bar_sq = v_gas * np.abs(v_gas) + Y_disk * v_disk**2 + Y_bul * v_bul**2
        v_tot_sq = v_DM_sq + v_bar_sq
        v_model = np.sqrt(np.maximum(v_tot_sq, 0))
        
        chi2 = np.sum(((v_model - v_data) / err_data)**2)
        return chi2
    except:
        return 1e10

def fit_galaxy(table, gal_name, p0=[8.0, 40.0, 2.0, 0.5, 0.7]):
    print(f"\nFitting {gal_name}...")
    mask = table['ID'] == gal_name
    gal_data = table[mask]
    
    if len(gal_data) == 0:
        print(f"Galaxy {gal_name} not found.")
        return
        
    r_data = gal_data['R']
    v_data = gal_data['Vobs']
    err_data = gal_data['e_Vobs']
    v_gas = gal_data['Vgas']
    v_disk = gal_data['Vdisk']
    v_bul = gal_data['Vbul']
    
    res = minimize(objective, p0, args=(r_data, v_data, err_data, v_gas, v_disk, v_bul), method='Nelder-Mead', options={'maxiter': 1000, 'disp': True})
    
    best_fit = res.x
    log_rho0, sigma0, r1, Y_disk, Y_bul = best_fit
    rho0 = 10**log_rho0
    
    v_avg = (4.0 / np.sqrt(np.pi)) * sigma0
    t_age_s = 10 * 3.154e16
    rho_r1, _ = integrate_isothermal(rho0, sigma0, r1)
    rho_r1_cgs = rho_r1 * 1.989e33 / (3.086e21)**3 # g / cm^3
    v_avg_cgs = v_avg * 1e5 # cm/s
    sigma_over_m = 1.0 / (rho_r1_cgs * v_avg_cgs * t_age_s)
    
    print(f"{gal_name} Best Fit:")
    print(f"log_rho0 = {log_rho0:.2f}")
    print(f"sigma0   = {sigma0:.1f} km/s")
    print(f"r1       = {r1:.2f} kpc")
    print(f"Y_disk   = {Y_disk:.2f}")
    print(f"Y_bul    = {Y_bul:.2f}")
    print(f"Inferred sigma/m: {sigma_over_m:.2f} cm^2/g at <v>={v_avg:.1f} km/s")
    print(f"Final chi2 / dof = {res.fun:.2f} / {len(r_data)-5}")
    print("-" * 40)

def parse_mrt(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('---') or line.startswith('Note') or line.startswith('Title') or line.startswith('Authors') or line.startswith('Table') or line.startswith('='):
                continue
            if line.strip() == '' or line.startswith('Byte') or line.startswith('   Bytes'):
                continue
            # Parse fixed width
            try:
                gal_id = line[0:11].strip()
                D = float(line[12:18].strip())
                R = float(line[19:25].strip())
                Vobs = float(line[26:32].strip())
                e_Vobs = float(line[33:38].strip())
                Vgas = float(line[39:45].strip())
                Vdisk = float(line[46:52].strip())
                Vbul = float(line[53:59].strip())
                data.append((gal_id, D, R, Vobs, e_Vobs, Vgas, Vdisk, Vbul))
            except ValueError:
                continue
    # Convert to structured numpy array or just return a dict of arrays
    dtype = [('ID', 'U11'), ('D', 'f8'), ('R', 'f8'), ('Vobs', 'f8'), 
             ('e_Vobs', 'f8'), ('Vgas', 'f8'), ('Vdisk', 'f8'), ('Vbul', 'f8')]
    return np.array(data, dtype=dtype)

if __name__ == "__main__":
    table = parse_mrt("SPARC_data_repo/data/MassModels_Lelli2016c.mrt")
    fit_galaxy(table, "DDO154", p0=[7.5, 20.0, 2.0, 0.5, 0.7])
    fit_galaxy(table, "IC2574", p0=[7.5, 40.0, 5.0, 0.5, 0.7])
    fit_galaxy(table, "NGC2903", p0=[8.5, 150.0, 10.0, 0.5, 0.7])
    fit_galaxy(table, "UGC2885", p0=[8.5, 250.0, 20.0, 0.5, 0.7])
