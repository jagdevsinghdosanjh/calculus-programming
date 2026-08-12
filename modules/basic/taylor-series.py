import sympy as sp

x = sp.Symbol('x')
f = sp.sin(x)

taylor = f.series(x, 0, 6)
print(taylor)
