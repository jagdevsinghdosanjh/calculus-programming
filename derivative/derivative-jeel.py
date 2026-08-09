import sympy as sp

x = sp.Symbol('x')
f = x**x

print("Derivative =", sp.diff(f, x))
