import sympy as sp

x = sp.Symbol('x')
expr = sp.sin(x)/x

limit_value = sp.limit(expr, x, 0)
print("Limit =", limit_value)
