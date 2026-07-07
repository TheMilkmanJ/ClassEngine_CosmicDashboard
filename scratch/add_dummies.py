import sys

def add_dummies():
    # add variables to background.h
    with open('include/background.h', 'r') as f:
        bg = f.read()
    
    if 'short use_prtoe;' not in bg:
        dummy_bg = """
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
"""
        bg = bg.replace('short has_ur;', 'short has_ur;' + dummy_bg)
        with open('include/background.h', 'w') as f:
            f.write(bg)

    # add variables to perturbations.h
    with open('include/perturbations.h', 'r') as f:
        pt = f.read()
    
    if 'index_pt_delta_phi' not in pt:
        dummy_pt = """
    /* DUMMIES for perturbations.c */
    int index_pt_delta_phi;
    int index_pt_ddelta_phi;
"""
        pt = pt.replace('int index_pt_ur2;', 'int index_pt_ur2;' + dummy_pt)
        with open('include/perturbations.h', 'w') as f:
            f.write(pt)

add_dummies()
