import re

with open('source/perturbations.c', 'r') as f:
    code = f.read()

pattern = r'/\* TRIAD CMB FIX: Phenomenological Phase Boost & Shear Viscosity Suppression \*/.*?}'

new_code = re.sub(pattern, '', code, flags=re.DOTALL)

with open('source/perturbations.c', 'w') as f:
    f.write(new_code)
