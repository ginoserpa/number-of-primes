import sympy as sp
expr = sp.log(2**1024, evaluate=False)
expanded = sp.expand_log(expr, force=True)
print(expanded)  # Output: 1024*log(2)