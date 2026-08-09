import sympy as sp

x = sp.Symbol('x')
expr = (sp.exp(x) - 1 - x) / x**2

print("Limit =", sp.limit(expr, x, 0))
