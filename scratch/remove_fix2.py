import re
with open('source/perturbations.c', 'r') as f: code = f.read()
code = re.sub(r'/\* PRTOE: Phenomenological fixes.*?\}', '', code, flags=re.DOTALL)
with open('source/perturbations.c', 'w') as f: f.write(code)
